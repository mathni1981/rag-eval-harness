"""Compare every scored run against the baseline.

Usage:
    python -m experiments.compare                 # all runs in results/runs/
    python -m experiments.compare --baseline baseline

Writes results/experiments.md. The change in correctness versus the baseline comes with a
paired bootstrap 95% interval: the same questions are resampled for both runs, so the
interval reflects the difference itself, not the noise in each run separately.
"""

from __future__ import annotations

import argparse
import json
import random

from data.common import ROOT
from harness.rubric import CORRECTNESS_SCORE
from harness.run import RUNS_DIR, SPLITS, load_questions, run_dir_for, split_of

OUT = ROOT / "results" / "experiments.md"
OUT_HELDOUT = ROOT / "results" / "heldout.md"
SEED = 7


def flatten(d: dict, prefix: str = "") -> dict:
    out = {}
    for k, v in d.items():
        key = f"{prefix}{k}"
        out.update(flatten(v, key + ".") if isinstance(v, dict) else {key: v})
    return out


def normalize(cfg: dict) -> dict:
    """Fill in defaults, so runs saved before a setting existed compare correctly."""
    from harness.config import config_from_dict

    return config_from_dict(cfg).to_dict() if cfg else {}


def config_diff(cfg: dict, base: dict) -> str:
    a, b = flatten(normalize(cfg)), flatten(normalize(base))
    changes = [f"{k}={a[k]}" for k in sorted(a) if k != "name" and a.get(k) != b.get(k)]
    return ", ".join(c.split(".", 1)[-1] for c in changes) or "–"


def paired_delta(a: dict[str, float], b: dict[str, float], samples: int = 2000, seed: int = SEED):
    ids = sorted(set(a) & set(b))
    if len(ids) < 2:
        return None, None
    diffs = [a[i] - b[i] for i in ids]
    rng = random.Random(seed)
    n = len(diffs)
    means = sorted(sum(rng.choice(diffs) for _ in range(n)) / n for _ in range(samples))
    return sum(diffs) / n, (means[int(0.025 * samples)], means[int(0.975 * samples) - 1])


def load_run(name: str, answerable: set[str]) -> dict | None:
    d = RUNS_DIR / name
    if not (d / "scores.json").exists():
        return None
    scores = json.loads((d / "scores.json").read_text())
    meta_path = d / "run.json" if (d / "run.json").exists() else d / "retrieval_run.json"
    meta = json.loads(meta_path.read_text()) if meta_path.exists() else {}
    per_q = {}
    jpath = d / "judgments.jsonl"
    if "answers" in scores and jpath.exists():
        for line in jpath.read_text().splitlines():
            j = json.loads(line)
            if j["id"] in answerable:
                per_q[j["id"]] = CORRECTNESS_SCORE[j["correctness"]]
    return {"name": name, "scores": scores, "meta": meta, "per_q": per_q}


def pct(m: dict | None) -> str:
    return "–" if not m or m.get("value") is None else f"{m['value'] * 100:.0f}%"


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("--baseline", default="baseline")
    parser.add_argument("--split", choices=sorted(SPLITS), default="dev")
    args = parser.parse_args(argv)

    questions = load_questions(SPLITS[args.split])
    answerable = {q["id"] for q in questions if q["type"] != "unanswerable"}
    dirs = [p for p in sorted(RUNS_DIR.iterdir()) if p.is_dir() and split_of(p.name) == args.split]
    runs = [r for r in (load_run(p.name, answerable) for p in dirs) if r]
    base_name = run_dir_for(args.baseline, args.split).name
    base = next((r for r in runs if r["name"] == base_name), None)
    if not base:
        raise SystemExit(f"No scored baseline run '{base_name}'")
    runs = [base] + [r for r in runs if r is not base]
    base_cfg = base["meta"].get("config", {})

    lines = [
        "# Experiments" if args.split == "dev" else "# Held-out confirmation",
        "",
        f"Each run changes one thing from `{args.baseline}`. Recall counts a question as retrieved",
        "when every gold evidence span overlaps an excerpt the model was shown. Correctness: correct = 1,",
        "partial = 0.5, otherwise 0, over the answerable questions. Δ is versus the baseline, with a",
        "paired bootstrap 95% interval; an interval that includes 0 means the change isn't distinguishable",
        "from noise at this sample size.",
        "",
        "| Run | Change | Recall (shown) | Recall: comparisons | Correctness | Δ correctness (95% CI) | Comparisons | Declined (answerable) | Unanswerable declined | Faithful | Input tokens / question |",
        "|---|---|---|---|---|---|---|---|---|---|---|",
    ]
    for r in runs:
        s = r["scores"]
        a = s.get("answers", {})
        delta = "–"
        if r is not base and r["per_q"] and base["per_q"]:
            d, ci = paired_delta(r["per_q"], base["per_q"])
            if d is not None:
                delta = f"{d * 100:+.0f} pts ({ci[0] * 100:+.0f} to {ci[1] * 100:+.0f})"
        summ = r["meta"].get("summary", {})
        tokens = (
            f"{summ['input_tokens'] / summ['questions']:,.0f}"
            if summ.get("input_tokens") and summ.get("questions")
            else "–"
        )
        lines.append(
            "| {name} | {chg} | {rec} | {rec_cmp} | {cor} | {delta} | {comp} | {decl} | {un} | {faith} | {tok} |".format(
                name=r["name"],
                chg=config_diff(r["meta"].get("config", {}), base_cfg)
                if r is not base
                else "baseline",
                rec=pct(s["retrieval"].get("question_recall@all")),
                rec_cmp=pct(s["retrieval"].get("by_type", {}).get("comparison")),
                cor=pct(a.get("answerable", {}).get("correctness_score")),
                delta=delta,
                comp=pct(a.get("correctness_by_type", {}).get("comparison")),
                decl=pct(a.get("answerable", {}).get("false_abstention")),
                un=pct(a.get("unanswerable", {}).get("abstained")),
                faith=pct(a.get("answerable", {}).get("faithful")),
                tok=tokens,
            )
        )
    lines.append("")
    out = OUT if args.split == "dev" else OUT_HELDOUT
    out.write_text("\n".join(lines), encoding="utf-8")
    print("\n".join(lines))
    print(f"Wrote {out.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
