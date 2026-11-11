"""Score a run: retrieval recall, LLM-judged correctness/faithfulness/citations, abstention.

Usage:
    python -m harness.evaluate --run baseline                 # judge + score
    python -m harness.evaluate --run baseline --no-judge      # retrieval metrics only, free
    python -m harness.evaluate --run baseline --limit 3       # judge a few to check cost

Writes to results/runs/<run>/:
    judgments.jsonl   one judge verdict per question (resumable)
    scores.json       all metrics with 95% bootstrap confidence intervals
    report.md         readable summary
"""

from __future__ import annotations

import argparse
import json
import random
import sys
from collections import defaultdict
from pathlib import Path

from dotenv import load_dotenv

from data.common import ROOT, load_manifest
from harness.excerpts import excerpts_for, format_excerpts
from harness.judge import judge_answer
from harness.rubric import CORRECTNESS_SCORE
from harness.run import QUESTIONS_PATH, RUNS_DIR, load_questions

DEFAULT_JUDGE = "claude-opus-5-5"
BOOTSTRAP_SAMPLES = 2000
SEED = 7


# ---------- statistics ----------


def mean(xs: list[float]) -> float | None:
    return sum(xs) / len(xs) if xs else None


def bootstrap_ci(xs: list[float], samples: int = BOOTSTRAP_SAMPLES, seed: int = SEED):
    """95% percentile bootstrap interval for the mean."""
    if len(xs) < 2:
        return None
    rng = random.Random(seed)
    n = len(xs)
    means = sorted(sum(rng.choice(xs) for _ in range(n)) / n for _ in range(samples))
    return [round(means[int(0.025 * samples)], 3), round(means[int(0.975 * samples) - 1], 3)]


def metric(xs: list[float]) -> dict:
    m = mean(xs)
    return {"value": None if m is None else round(m, 3), "ci95": bootstrap_ci(xs), "n": len(xs)}


# ---------- retrieval ----------


def _overlap(r: dict, ev: dict) -> bool:
    return (
        r["doc"] == ev["doc"]
        and r["char_start"] < ev["char_end"]
        and ev["char_start"] < r["char_end"]
    )


def retrieval_at(record: dict, evidence: list[dict], k: int) -> tuple[list[bool], bool]:
    top = [r for r in record["retrieved"] if r["rank"] <= k]
    spans = [any(_overlap(r, ev) for r in top) for ev in evidence]
    return spans, all(spans)


def retrieval_metrics(pairs: list[tuple[dict, dict]], ks: list[int]) -> dict:
    out = {}
    for k in ks:
        span_hits, question_hits = [], []
        for q, rec in pairs:
            spans, all_hit = retrieval_at(rec, q["evidence"], k)
            span_hits += [float(s) for s in spans]
            question_hits.append(float(all_hit))
        out[f"span_recall@{k}"] = metric(span_hits)
        out[f"question_recall@{k}"] = metric(question_hits)
    return out


# ---------- answer metrics ----------


def answer_metrics(rows: list[dict]) -> dict:
    """rows: {'q': question, 'j': judgment, 'retrieved_all': bool}"""
    answerable = [r for r in rows if r["q"]["type"] != "unanswerable"]
    unanswerable = [r for r in rows if r["q"]["type"] == "unanswerable"]
    out: dict = {}
    if answerable:
        c = [r["j"]["correctness"] for r in answerable]
        out["answerable"] = {
            "correctness_score": metric([CORRECTNESS_SCORE[x] for x in c]),
            "fully_correct": metric([float(x == "correct") for x in c]),
            "partial": metric([float(x == "partial") for x in c]),
            "incorrect": metric([float(x == "incorrect") for x in c]),
            "false_abstention": metric([float(x == "abstained") for x in c]),
            "faithful": metric(
                [
                    float(r["j"]["faithfulness"] == "faithful")
                    for r in answerable
                    if r["j"]["faithfulness"] != "n/a"
                ]
            ),
            "citations_accurate": metric(
                [
                    float(r["j"]["citations"] == "accurate")
                    for r in answerable
                    if r["j"]["citations"] != "n/a"
                ]
            ),
        }
        hit = [r for r in answerable if r["retrieved_all"]]
        miss = [r for r in answerable if not r["retrieved_all"]]
        out["correctness_by_retrieval"] = {
            "all_evidence_retrieved": metric(
                [CORRECTNESS_SCORE[r["j"]["correctness"]] for r in hit]
            ),
            "evidence_missing": metric([CORRECTNESS_SCORE[r["j"]["correctness"]] for r in miss]),
        }
    if unanswerable:
        c = [r["j"]["correctness"] for r in unanswerable]
        out["unanswerable"] = {
            "abstained": metric([float(x == "abstained") for x in c]),
            "answered_anyway": metric([float(x != "abstained") for x in c]),
        }
    by_type = defaultdict(list)
    for r in answerable:
        by_type[r["q"]["type"]].append(CORRECTNESS_SCORE[r["j"]["correctness"]])
    out["correctness_by_type"] = {t: metric(v) for t, v in sorted(by_type.items())}
    by_author = defaultdict(list)
    for r in answerable:
        by_author[r["q"].get("author", "unknown")].append(CORRECTNESS_SCORE[r["j"]["correctness"]])
    out["correctness_by_author"] = {a: metric(v) for a, v in sorted(by_author.items())}
    return out


# ---------- report ----------


def fmt(m: dict | None, pct: bool = True) -> str:
    if not m or m["value"] is None:
        return "–"
    v = f"{m['value'] * 100:.0f}%" if pct else f"{m['value']:.2f}"
    if m["ci95"]:
        lo, hi = m["ci95"]
        v += f" ({lo * 100:.0f}–{hi * 100:.0f}%)" if pct else f" ({lo:.2f}–{hi:.2f})"
    return f"{v} · n={m['n']}"


def render_report(run_name: str, scores: dict, judged: bool) -> str:
    lines = [
        f"# Evaluation: `{run_name}`",
        "",
        "Values are means with 95% bootstrap confidence intervals over questions.",
        "",
    ]
    lines += ["## Retrieval", "", "| Metric | Value |", "|---|---|"]
    for key, m in scores["retrieval"].items():
        lines.append(f"| {key} | {fmt(m)} |")
    if judged:
        a = scores["answers"]
        lines += [
            "",
            f"## Answers (judge: `{scores['judge_model']}`)",
            "",
            "| Metric | Value |",
            "|---|---|",
        ]
        for key, m in a.get("answerable", {}).items():
            lines.append(f"| Answerable · {key.replace('_', ' ')} | {fmt(m)} |")
        for key, m in a.get("unanswerable", {}).items():
            lines.append(f"| Unanswerable · {key.replace('_', ' ')} | {fmt(m)} |")
        lines += ["", "## Correctness by question type", "", "| Type | Score |", "|---|---|"]
        for t, m in a["correctness_by_type"].items():
            lines.append(f"| {t} | {fmt(m)} |")
        lines += [
            "",
            "## Is it retrieval or generation?",
            "",
            "Correctness when all gold evidence was in the top-k excerpts, versus when some was missing.",
            "",
            "| Retrieval outcome | Correctness |",
            "|---|---|",
        ]
        for t, m in a.get("correctness_by_retrieval", {}).items():
            lines.append(f"| {t.replace('_', ' ')} | {fmt(m)} |")
        lines += ["", "## Correctness by question author", "", "| Author | Score |", "|---|---|"]
        for t, m in a["correctness_by_author"].items():
            lines.append(f"| {t} | {fmt(m)} |")
    lines += ["", "Correctness score: correct = 1, partial = 0.5, incorrect or abstained = 0.", ""]
    return "\n".join(lines)


# ---------- main ----------


def evaluate(
    run_dir: Path,
    questions: list[dict],
    client=None,
    judge_model: str = DEFAULT_JUDGE,
    judge: bool = True,
    limit: int | None = None,
    manifest: dict | None = None,
) -> dict:
    manifest = manifest if manifest is not None else load_manifest()
    answers = {}
    for line in (run_dir / "answers.jsonl").read_text(encoding="utf-8").splitlines():
        rec = json.loads(line)
        answers[rec["id"]] = rec
    run_meta = (
        json.loads((run_dir / "run.json").read_text()) if (run_dir / "run.json").exists() else {}
    )
    top_k = run_meta.get("config", {}).get("retrieval", {}).get("top_k") or max(
        len(r["retrieved"]) for r in answers.values()
    )
    qs = [q for q in questions if q["id"] in answers]
    answerable_pairs = [(q, answers[q["id"]]) for q in qs if q["type"] != "unanswerable"]
    ks = sorted({1, 3, top_k})
    scores: dict = {"run": run_dir.name, "retrieval": retrieval_metrics(answerable_pairs, ks)}

    if judge:
        jpath = run_dir / "judgments.jsonl"
        judged = {}
        if jpath.exists():
            for line in jpath.read_text(encoding="utf-8").splitlines():
                rec = json.loads(line)
                judged[rec["id"]] = rec
        todo = [q for q in qs if q["id"] not in judged]
        if limit:
            todo = todo[:limit]
        print(f"{len(judged)} already judged, {len(todo)} to judge with {judge_model}")
        with jpath.open("a", encoding="utf-8") as f:
            for n, q in enumerate(todo, 1):
                rec = answers[q["id"]]
                text = format_excerpts(excerpts_for(rec, manifest))
                verdict = judge_answer(client, judge_model, q, rec["answer"]["text"], text)
                out = {"id": q["id"], **verdict}
                f.write(json.dumps(out, ensure_ascii=False) + "\n")
                f.flush()
                judged[q["id"]] = out
                print(
                    f"  [{n}/{len(todo)}] {q['id']}: {verdict['correctness']}, "
                    f"{verdict['faithfulness']}, citations {verdict['citations']}"
                )
        rows = []
        for q in qs:
            if q["id"] not in judged:
                continue
            all_hit = (
                retrieval_at(answers[q["id"]], q["evidence"], top_k)[1] if q["evidence"] else None
            )
            rows.append({"q": q, "j": judged[q["id"]], "retrieved_all": bool(all_hit)})
        scores["judge_model"] = judge_model
        scores["judged"] = len(rows)
        scores["answers"] = answer_metrics(rows)

    (run_dir / "scores.json").write_text(json.dumps(scores, indent=2))
    (run_dir / "report.md").write_text(render_report(run_dir.name, scores, judge), encoding="utf-8")
    return scores


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("--run", required=True, help="run name under results/runs/")
    parser.add_argument("--judge-model", default=DEFAULT_JUDGE)
    parser.add_argument("--no-judge", action="store_true", help="retrieval metrics only")
    parser.add_argument("--limit", type=int, help="judge at most N more questions")
    args = parser.parse_args(argv)

    load_dotenv(ROOT / ".env")
    run_dir = RUNS_DIR / args.run
    if not (run_dir / "answers.jsonl").exists():
        sys.exit(f"No answers at {run_dir}/answers.jsonl; run harness.run first.")
    client = None
    if not args.no_judge:
        from harness.generate import make_client

        client = make_client()
    evaluate(
        run_dir,
        load_questions(QUESTIONS_PATH),
        client,
        args.judge_model,
        judge=not args.no_judge,
        limit=args.limit,
    )
    print(f"\nWrote {run_dir.relative_to(ROOT)}/report.md")
    print((run_dir / "report.md").read_text())


if __name__ == "__main__":
    main()
