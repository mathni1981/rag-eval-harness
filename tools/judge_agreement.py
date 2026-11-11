"""Measure how often the LLM judge agrees with your hand labels.

Usage:
    python -m tools.judge_agreement --run baseline

Reads eval_set/hand_labels/<run>_labels.csv and results/runs/<run>/judgments.jsonl and writes
results/runs/<run>/judge_agreement.md.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from collections import Counter

from data.common import ROOT
from harness.rubric import CITATIONS, CORRECTNESS, FAITHFULNESS
from harness.run import RUNS_DIR
from tools.make_label_sheet import LABELS_DIR

FIELDS = {"correctness": CORRECTNESS, "faithfulness": FAITHFULNESS, "citations": CITATIONS}


def cohen_kappa(a: list[str], b: list[str]) -> float | None:
    n = len(a)
    if n == 0:
        return None
    observed = sum(x == y for x, y in zip(a, b, strict=True)) / n
    ca, cb = Counter(a), Counter(b)
    expected = sum(ca[k] * cb[k] for k in set(a) | set(b)) / (n * n)
    if expected == 1:
        return 1.0 if observed == 1 else 0.0
    return (observed - expected) / (1 - expected)


def load_labels(path) -> tuple[dict, list[str]]:
    labels, problems = {}, []
    with path.open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            row = {k: (v or "").strip().lower() for k, v in row.items()}
            if not row.get("correctness"):
                continue  # not labeled yet
            for field, allowed in FIELDS.items():
                if row.get(field) not in allowed:
                    problems.append(f"{row['id']}: {field}={row.get(field)!r} not in {allowed}")
            labels[row["id"]] = row
    return labels, problems


def agreement_report(run: str, labels: dict, judged: dict) -> str:
    ids = sorted(set(labels) & set(judged))
    lines = [
        f"# Judge agreement: `{run}`",
        "",
        f"Questions with both a hand label and a judge verdict: {len(ids)}",
        "",
    ]
    lines += ["| Dimension | Agreement | Cohen's kappa |", "|---|---|---|"]
    disagreements = []
    for field in FIELDS:
        h = [labels[i][field] for i in ids]
        j = [judged[i][field] for i in ids]
        agree = sum(x == y for x, y in zip(h, j, strict=True))
        k = cohen_kappa(h, j)
        lines.append(
            f"| {field} | {agree}/{len(ids)} ({agree / len(ids):.0%}) | {k:.2f} |"
            if ids
            else f"| {field} | – | – |"
        )
        disagreements += [
            (i, field, labels[i][field], judged[i][field])
            for i in ids
            if labels[i][field] != judged[i][field]
        ]
    if ids:
        h = [labels[i]["correctness"] == "correct" for i in ids]
        j = [judged[i]["correctness"] == "correct" for i in ids]
        agree = sum(x == y for x, y in zip(h, j, strict=True))
        lines.append(
            f"| correctness (correct vs not) | {agree}/{len(ids)} ({agree / len(ids):.0%}) | – |"
        )
    lines += [
        "",
        "Kappa corrects for chance agreement: above 0.6 is usually read as substantial, above 0.8 as",
        "near-perfect. With about 30 labels, treat these as rough.",
        "",
        "## Disagreements",
        "",
    ]
    if disagreements:
        lines += ["| Question | Dimension | You | Judge | Your notes |", "|---|---|---|---|---|"]
        for i, field, h, j in disagreements:
            lines.append(f"| {i} | {field} | {h} | {j} | {labels[i].get('notes', '')} |")
    else:
        lines.append("None.")
    return "\n".join(lines) + "\n"


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("--run", required=True)
    args = parser.parse_args(argv)

    csv_path = LABELS_DIR / f"{args.run}_labels.csv"
    jpath = RUNS_DIR / args.run / "judgments.jsonl"
    for p in (csv_path, jpath):
        if not p.exists():
            sys.exit(f"Missing {p.relative_to(ROOT)}")
    labels, problems = load_labels(csv_path)
    if problems:
        sys.exit("Fix these labels first:\n  " + "\n  ".join(problems))
    judged = {}
    for line in jpath.read_text(encoding="utf-8").splitlines():
        rec = json.loads(line)
        judged[rec["id"]] = rec
    report = agreement_report(args.run, labels, judged)
    out = RUNS_DIR / args.run / "judge_agreement.md"
    out.write_text(report, encoding="utf-8")
    print(report)


if __name__ == "__main__":
    main()
