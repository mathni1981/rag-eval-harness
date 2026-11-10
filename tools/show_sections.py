"""Print each frozen filing's detected sections with a preview, for manual checking.

Usage:
    python -m tools.show_sections
    python -m tools.show_sections --doc MET_FY2025_10K
"""

from __future__ import annotations

import argparse

from data.common import ROOT, load_manifest


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--doc", help="show one document only")
    args = parser.parse_args(argv)

    manifest = load_manifest()
    for doc_id in sorted(manifest):
        if args.doc and doc_id != args.doc:
            continue
        entry = manifest[doc_id]
        if not entry.get("text_path"):
            print(f"{doc_id}: not frozen yet\n")
            continue
        text = (ROOT / entry["text_path"]).read_text(encoding="utf-8")
        print(f"{doc_id}  (period end {entry.get('period_end')}, {len(text):,} chars)")
        for key, start in sorted(entry.get("sections", {}).items(), key=lambda kv: kv[1]):
            preview = text[start : start + 90].replace("\n", " / ")
            print(f"  Item {key:<3} @ {start:>9,}  {preview}")
        print()


if __name__ == "__main__":
    main()
