"""Validate eval_set/questions.jsonl against the schema and the frozen filings.

Usage:
    python -m tools.validate_eval_set
    python -m tools.validate_eval_set --path eval_set/questions.jsonl

Exit code 1 on errors; 0 if only warnings.
"""

from __future__ import annotations

import argparse
import difflib
import json
import re
import sys
from collections import Counter
from pathlib import Path

from data.common import ROOT, load_manifest, sha256_file
from data.freeze_text import section_at

DEFAULT_PATH = ROOT / "eval_set" / "questions.jsonl"
TYPES = {"single_fact", "multi_passage", "comparison", "unanswerable"}
SOURCE_KINDS = {"narrative", "table", "mixed"}
DIFFICULTIES = {"easy", "medium", "hard"}
AUTHORS = {"human", "claude"}
TARGET_MIX = {"single_fact": 18, "multi_passage": 12, "comparison": 10, "unanswerable": 10}
ID_PATTERN = re.compile(r"^q\d{3,}$")
LEAK_NGRAM = 6


def _tokens(text: str) -> list[str]:
    return re.findall(r"[a-z0-9]+", text.lower())


def shared_ngram(a: str, b: str, n: int = LEAK_NGRAM) -> str | None:
    ta, tb = _tokens(a), _tokens(b)
    grams_b = {tuple(tb[i : i + n]) for i in range(len(tb) - n + 1)}
    for i in range(len(ta) - n + 1):
        g = tuple(ta[i : i + n])
        if g in grams_b:
            return " ".join(g)
    return None


class Report:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def error(self, qid: str, msg: str) -> None:
        self.errors.append(f"{qid}: {msg}")

    def warn(self, qid: str, msg: str) -> None:
        self.warnings.append(f"{qid}: {msg}")


def validate(questions: list[dict], manifest: dict, report: Report) -> None:
    texts: dict[str, str] = {}
    for doc_id, entry in manifest.items():
        if not entry.get("text_path"):
            continue
        path = ROOT / entry["text_path"]
        if not path.exists():
            report.error("manifest", f"{doc_id}: frozen text missing at {entry['text_path']}")
            continue
        if sha256_file(path) != entry.get("text_sha256"):
            report.error("manifest", f"{doc_id}: frozen text hash mismatch; offsets are invalid")
            continue
        texts[doc_id] = path.read_text(encoding="utf-8")

    seen_ids: set[str] = set()
    for q in questions:
        qid = str(q.get("id", "?"))
        if not ID_PATTERN.match(qid):
            report.error(qid, "id must look like q001")
        if qid in seen_ids:
            report.error(qid, "duplicate id")
        seen_ids.add(qid)

        qtype = q.get("type")
        if qtype not in TYPES:
            report.error(qid, f"type must be one of {sorted(TYPES)}")
        for field in ("question", "gold_answer"):
            if not str(q.get(field, "")).strip():
                report.error(qid, f"{field} is empty")
        kp = q.get("key_points")
        if not isinstance(kp, list) or not kp or not all(str(k).strip() for k in kp):
            report.error(qid, "key_points must be a non-empty list of strings")
        if q.get("difficulty") not in DIFFICULTIES:
            report.error(qid, f"difficulty must be one of {sorted(DIFFICULTIES)}")
        if q.get("author") not in AUTHORS:
            report.error(qid, f"author must be one of {sorted(AUTHORS)}")

        evidence = q.get("evidence")
        if not isinstance(evidence, list):
            report.error(qid, "evidence must be a list")
            continue

        if qtype == "unanswerable":
            if evidence:
                report.error(qid, "unanswerable questions must have empty evidence")
            if not str(q.get("notes", "")).strip():
                report.error(qid, "unanswerable questions need notes explaining why")
        else:
            if q.get("source_kind") not in SOURCE_KINDS:
                report.error(qid, f"source_kind must be one of {sorted(SOURCE_KINDS)}")
            minimum = 1 if qtype == "single_fact" else 2
            if len(evidence) < minimum:
                report.error(qid, f"{qtype} needs at least {minimum} evidence spans")
            if qtype == "comparison" and len({e.get("doc") for e in evidence}) < 2:
                report.error(qid, "comparison evidence must span at least 2 documents")

        for i, ev in enumerate(evidence):
            label = f"evidence[{i}]"
            doc = ev.get("doc")
            if doc not in manifest:
                report.error(qid, f"{label}: unknown doc '{doc}'")
                continue
            if doc not in texts:
                report.error(qid, f"{label}: no valid frozen text for '{doc}'")
                continue
            start, end, quote = ev.get("char_start"), ev.get("char_end"), ev.get("quote", "")
            if not isinstance(start, int) or not isinstance(end, int) or not 0 <= start < end:
                report.error(qid, f"{label}: invalid char_start/char_end")
                continue
            actual = texts[doc][start:end]
            if actual != quote:
                report.error(
                    qid,
                    f"{label}: quote does not match text at [{start}:{end}] "
                    f"(found: {actual[:60]!r}); use tools.find_quote --json",
                )
                continue
            expected = section_at(manifest[doc].get("sections") or {}, start)
            if ev.get("section") != expected:
                report.error(
                    qid, f"{label}: section is {ev.get('section')!r}, offset is in {expected!r}"
                )
            leak = shared_ngram(q.get("question", ""), quote)
            if leak:
                report.warn(qid, f"question copies the passage's wording ('{leak}'); paraphrase it")

    for i, a in enumerate(questions):
        for b in questions[i + 1 :]:
            ratio = difflib.SequenceMatcher(
                None, a.get("question", ""), b.get("question", "")
            ).ratio()
            if ratio > 0.85:
                report.warn(
                    f"{a.get('id')}/{b.get('id')}", f"near-duplicate questions ({ratio:.2f})"
                )


def summary(questions: list[dict]) -> str:
    by_type = Counter(q.get("type") for q in questions)
    docs = Counter(e.get("doc") for q in questions for e in q.get("evidence") or [])
    sections = Counter(e.get("section") for q in questions for e in q.get("evidence") or [])
    kinds = Counter(q.get("source_kind") for q in questions if q.get("type") != "unanswerable")
    diff = Counter(q.get("difficulty") for q in questions)
    authors = Counter(q.get("author") for q in questions)

    lines = [f"Questions: {len(questions)}", "", "By type (have / target):"]
    for t, target in TARGET_MIX.items():
        lines.append(f"  {t:<14} {by_type.get(t, 0):>3} / {target}")
    lines.append(f"\nEvidence by document: {dict(sorted(docs.items()))}")
    lines.append(
        f"Evidence by section:  {dict(sorted(sections.items(), key=lambda kv: str(kv[0])))}"
    )
    lines.append(f"Source kind:          {dict(kinds)}")
    lines.append(f"Difficulty:           {dict(diff)}")
    lines.append(f"Author:               {dict(authors)}")
    return "\n".join(lines)


def load_questions(path: Path, report: Report) -> list[dict]:
    questions = []
    for n, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            questions.append(json.loads(line))
        except json.JSONDecodeError as e:
            report.error(f"line {n}", f"invalid JSON: {e}")
    return questions


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--path", type=Path, default=DEFAULT_PATH)
    args = parser.parse_args(argv)

    if not args.path.exists():
        sys.exit(f"No eval set at {args.path}. Create it (one JSON object per line).")

    report = Report()
    questions = load_questions(args.path, report)
    validate(questions, load_manifest(), report)

    print(summary(questions))
    if report.warnings:
        print(f"\nWarnings ({len(report.warnings)}):")
        print("\n".join(f"  - {w}" for w in report.warnings))
    if report.errors:
        print(f"\nErrors ({len(report.errors)}):")
        print("\n".join(f"  - {e}" for e in report.errors))
        sys.exit(1)
    print("\nValid.")


if __name__ == "__main__":
    main()
