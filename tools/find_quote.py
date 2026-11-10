"""Find the exact character offsets of a quote in a frozen filing.

Usage:
    python -m tools.find_quote --doc MET_FY2025_10K --quote "text copied from the filing"
    python -m tools.find_quote --doc MET_FY2025_10K --quote "..." --json

Whitespace in the quote is matched flexibly (a line break in the filing matches a space in
your quote). The reported quote is always the exact text from the frozen file, so it passes
validation as-is.
"""

from __future__ import annotations

import argparse
import difflib
import json
import re
import sys

from data.common import ROOT, load_manifest, normalize_quote
from data.freeze_text import section_at


def load_doc(doc_id: str, manifest: dict | None = None) -> tuple[dict, str]:
    manifest = manifest if manifest is not None else load_manifest()
    if doc_id not in manifest:
        raise KeyError(f"Unknown doc '{doc_id}'. Known: {', '.join(sorted(manifest))}")
    entry = manifest[doc_id]
    if not entry.get("text_path"):
        raise FileNotFoundError(f"{doc_id} has no frozen text yet; run data.freeze_text")
    return entry, (ROOT / entry["text_path"]).read_text(encoding="utf-8")


def quote_pattern(quote: str) -> re.Pattern:
    words = normalize_quote(quote).split(" ")
    return re.compile(r"\s+".join(re.escape(w) for w in words))


def find_exact(text: str, quote: str) -> list[tuple[int, int]]:
    if not normalize_quote(quote):
        return []
    return [(m.start(), m.end()) for m in quote_pattern(quote).finditer(text)]


def find_fuzzy(text: str, quote: str, n: int = 3) -> list[tuple[float, int, int]]:
    """Closest paragraphs by similarity; for when an exact match fails."""
    target = normalize_quote(quote).lower()
    scored = []
    pos = 0
    for para in text.split("\n"):
        start = pos
        pos += len(para) + 1
        if len(para) < 20:
            continue
        sm = difflib.SequenceMatcher(None, target, para.lower(), autojunk=False)
        if sm.quick_ratio() < 0.5:
            continue
        block = sm.find_longest_match(0, len(target), 0, len(para))
        scored.append((sm.ratio(), start + block.b, start + block.b + block.size, start))
    scored.sort(reverse=True)
    return [(round(r, 3), s, e) for r, s, e, _ in scored[:n]]


def evidence_object(doc_id: str, entry: dict, text: str, start: int, end: int) -> dict:
    return {
        "doc": doc_id,
        "section": section_at(entry.get("sections") or {}, start),
        "quote": text[start:end],
        "char_start": start,
        "char_end": end,
    }


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--doc", required=True)
    parser.add_argument("--quote", required=True)
    parser.add_argument("--json", action="store_true", help="print ready-to-paste evidence")
    args = parser.parse_args(argv)

    try:
        entry, text = load_doc(args.doc)
    except (KeyError, FileNotFoundError) as e:
        sys.exit(str(e))

    matches = find_exact(text, args.quote)
    if matches:
        if len(matches) > 1:
            print(f"Note: {len(matches)} exact matches; lengthen the quote to make it unique.\n")
        for start, end in matches:
            ev = evidence_object(args.doc, entry, text, start, end)
            if args.json:
                print(json.dumps(ev, ensure_ascii=False))
            else:
                before = text[max(0, start - 80) : start].replace("\n", " / ")
                after = text[end : end + 80].replace("\n", " / ")
                print(f"Item {ev['section']}  [{start}:{end}]")
                print(f"  ...{before}>>>{ev['quote']}<<<{after}...\n")
        return

    print("No exact match. Closest passages (NOT exact; copy the text precisely and retry):\n")
    for ratio, start, end in find_fuzzy(text, args.quote):
        ctx = text[max(0, start - 60) : end + 60].replace("\n", " / ")
        section = section_at(entry.get("sections") or {}, start)
        print(f"  similarity {ratio}  Item {section}  [{start}:{end}]")
        print(f"  ...{ctx}...\n")
    sys.exit(1)


if __name__ == "__main__":
    main()
