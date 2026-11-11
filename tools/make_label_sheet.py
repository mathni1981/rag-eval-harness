"""Create the hand-labeling sheet for checking the LLM judge.

Usage:
    python -m tools.make_label_sheet --run baseline            # 30 questions, stratified by type

Writes, without ever overwriting existing labels:
    eval_set/hand_labels/<run>_packet.md   what to read: rubric, question, gold, excerpts, answer
    eval_set/hand_labels/<run>_labels.csv  where to record your grades

The packet never shows the judge's verdicts, so your labels stay independent.
"""

from __future__ import annotations

import argparse
import csv
import json
import random
import sys
from collections import defaultdict

from data.common import ROOT
from harness.excerpts import excerpts_for, format_excerpts
from harness.rubric import CITATIONS, CORRECTNESS, FAITHFULNESS, RUBRIC, RUBRIC_VERSION
from harness.run import QUESTIONS_PATH, RUNS_DIR, load_questions

LABELS_DIR = ROOT / "eval_set" / "hand_labels"
FIELDS = ["id", "type", "correctness", "faithfulness", "citations", "notes"]
SEED = 11


def stratified_sample(questions: list[dict], n: int, seed: int = SEED) -> list[dict]:
    by_type = defaultdict(list)
    for q in questions:
        by_type[q["type"]].append(q)
    total = len(questions)
    alloc = {t: max(1, round(n * len(qs) / total)) for t, qs in by_type.items()}
    while sum(alloc.values()) > n:  # trim rounding overshoot from the largest group
        alloc[max(alloc, key=alloc.get)] -= 1
    while sum(alloc.values()) < n:
        alloc[max(by_type, key=lambda t: len(by_type[t]) - alloc[t])] += 1
    rng = random.Random(seed)
    picked = []
    for t, qs in sorted(by_type.items()):
        picked += rng.sample(qs, min(alloc[t], len(qs)))
    return sorted(picked, key=lambda q: q["id"])


def packet(run: str, sample: list[dict], answers: dict) -> str:
    out = [
        f"# Hand-labeling packet: `{run}` (rubric v{RUBRIC_VERSION})",
        "",
        f"{len(sample)} questions. For each, read the excerpts and the answer, then record three grades",
        f"in `{run}_labels.csv` using the rubric below. Grade what you see; don't look at the judge's",
        "verdicts until you're done.",
        "",
        "Allowed values:",
        f"- correctness: {', '.join(CORRECTNESS)}",
        f"- faithfulness: {', '.join(FAITHFULNESS)}",
        f"- citations: {', '.join(CITATIONS)}",
        "",
        "## Rubric",
        "",
        "```",
        RUBRIC.rstrip(),
        "```",
        "",
    ]
    for q in sample:
        rec = answers[q["id"]]
        out += [
            f"---\n\n## {q['id']} · {q['type']}",
            "",
            f"**Question:** {q['question']}",
            "",
            f"**Gold answer:** {q['gold_answer']}",
            "",
            "**Key points:**",
            *[f"{i + 1}. {k}" for i, k in enumerate(q["key_points"])],
            "",
            "**System answer:**",
            "",
            "> " + rec["answer"]["text"].strip().replace("\n", "\n> "),
            "",
            "<details><summary>Excerpts the system saw</summary>",
            "",
            "```",
            format_excerpts(excerpts_for(rec)),
            "```",
            "",
            "</details>",
            "",
        ]
    return "\n".join(out)


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("--run", required=True)
    parser.add_argument("--n", type=int, default=30)
    parser.add_argument(
        "--refresh-packet",
        action="store_true",
        help="rewrite the packet (e.g. after a rubric change) for the questions already in your CSV",
    )
    args = parser.parse_args(argv)

    answers_path = RUNS_DIR / args.run / "answers.jsonl"
    if not answers_path.exists():
        sys.exit(f"No answers at {answers_path}")
    answers = {}
    for line in answers_path.read_text(encoding="utf-8").splitlines():
        rec = json.loads(line)
        answers[rec["id"]] = rec

    csv_path = LABELS_DIR / f"{args.run}_labels.csv"
    if args.refresh_packet:
        if not csv_path.exists():
            sys.exit(
                f"No labels at {csv_path.relative_to(ROOT)}; run without --refresh-packet first."
            )
        with csv_path.open(newline="", encoding="utf-8") as f:
            ids = {row["id"] for row in csv.DictReader(f)}
        sample = [q for q in load_questions(QUESTIONS_PATH) if q["id"] in ids]
        out = LABELS_DIR / f"{args.run}_packet.md"
        out.write_text(packet(args.run, sample, answers), encoding="utf-8")
        print(
            f"Rewrote {out.relative_to(ROOT)} for {len(sample)} questions; your labels are untouched."
        )
        return
    if csv_path.exists():
        sys.exit(f"{csv_path.relative_to(ROOT)} already exists; not overwriting your labels.")

    questions = [q for q in load_questions(QUESTIONS_PATH) if q["id"] in answers]
    sample = stratified_sample(questions, args.n)
    LABELS_DIR.mkdir(parents=True, exist_ok=True)
    (LABELS_DIR / f"{args.run}_packet.md").write_text(
        packet(args.run, sample, answers), encoding="utf-8"
    )
    with csv_path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        w.writeheader()
        for q in sample:
            w.writerow({"id": q["id"], "type": q["type"]})
    counts = defaultdict(int)
    for q in sample:
        counts[q["type"]] += 1
    print(f"Sampled {len(sample)} questions: {dict(counts)}")
    print(f"Read:   {(LABELS_DIR / f'{args.run}_packet.md').relative_to(ROOT)}")
    print(f"Grade:  {csv_path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
