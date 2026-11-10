"""Convert raw 10-K HTML into frozen, normalized text with section offsets.

Usage:
    python -m data.freeze_text                 # freeze any filing not yet frozen
    python -m data.freeze_text --new-version   # deliberately write a new text version

Frozen files are immutable: eval-set offsets point into them. If extraction changes,
a new version (_v2, _v3...) is written and every question must be revalidated.
"""

from __future__ import annotations

import argparse
import re
import sys
import warnings
from pathlib import Path

from bs4 import BeautifulSoup, NavigableString, XMLParsedAsHTMLWarning

from data.common import (
    ROOT,
    TEXT_DIR,
    load_manifest,
    normalize_text,
    save_manifest,
    sha256_bytes,
)

BLOCK_TAGS = [
    "p",
    "div",
    "li",
    "ul",
    "ol",
    "h1",
    "h2",
    "h3",
    "h4",
    "h5",
    "h6",
    "section",
    "article",
    "blockquote",
    "pre",
    "center",
    "hr",
]
HIDDEN_STYLE = re.compile(r"display\s*:\s*none", re.I)

SECTION_KEYS = [
    "1",
    "1A",
    "1B",
    "1C",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "7A",
    "8",
    "9",
    "9A",
    "9B",
    "9C",
    "10",
    "11",
    "12",
    "13",
    "14",
    "15",
    "16",
]
ITEM_HEADING = re.compile(
    r"^item\s*(1[0-6]|1a|1b|1c|7a|9a|9b|9c|1|2|3|4|5|6|7|8|9)\b\.?", re.I | re.M
)


def html_to_text(html: str | bytes) -> str:
    # Inline XBRL is XHTML. The HTML parser handles it fine and is what the frozen text was
    # built with; switching parsers would change the output and invalidate offsets.
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", XMLParsedAsHTMLWarning)
        soup = BeautifulSoup(html, "lxml")

    for tag in soup.find_all(["script", "style", "ix:header"]):
        tag.decompose()
    for tag in soup.find_all(style=HIDDEN_STYLE):
        tag.decompose()

    # Tables: one line per row, cells separated by " | ", so table facts stay findable.
    for table in soup.find_all("table"):
        rows = []
        for tr in table.find_all("tr"):
            cells = [c.get_text(" ", strip=True) for c in tr.find_all(["td", "th"])]
            cells = [c for c in cells if c]
            if cells:
                rows.append(" | ".join(cells))
        table.replace_with(NavigableString("\n" + "\n".join(rows) + "\n"))

    for br in soup.find_all("br"):
        br.replace_with(NavigableString("\n"))
    # Newlines only at block boundaries, so inline XBRL spans don't split sentences.
    for tag in soup.find_all(BLOCK_TAGS):
        tag.insert_before(NavigableString("\n"))
        tag.insert_after(NavigableString("\n"))

    return normalize_text(soup.get_text())


def _looks_like_toc(text: str, pos: int, window: int = 1500) -> bool:
    """A table of contents packs many Item headings into a short span; body text doesn't."""
    following = text[pos : pos + window]
    return len(ITEM_HEADING.findall(following)) >= 4


AUDITOR_REPORT = re.compile(
    r"^report of independent registered public accounting firm", re.I | re.M
)


def detect_sections(text: str) -> dict[str, int]:
    """Start offset of each Item heading in the body, skipping table-of-contents entries."""
    candidates: dict[str, list[int]] = {}
    for m in ITEM_HEADING.finditer(text):
        line_end = text.find("\n", m.start())
        line = text[m.start() : line_end if line_end != -1 else len(text)]
        if "|" in line:  # table row, almost always the table of contents
            continue
        candidates.setdefault(m.group(1).upper(), []).append(m.start())

    sections: dict[str, int] = {}
    for key in SECTION_KEYS:
        positions = [p for p in candidates.get(key, []) if not _looks_like_toc(text, p)]
        if positions:
            sections[key] = positions[0]
        elif candidates.get(key):
            sections[key] = candidates[key][-1]  # fallback: last occurrence
    # Some filers (e.g. BlackRock) put the financial statements after Item 16 and the
    # signatures. Label that block "FS" instead of letting it fall under the last Item.
    if sections:
        last_item = max(sections.values())
        after = [m.start() for m in AUDITOR_REPORT.finditer(text) if m.start() > last_item]
        if after:
            sections["FS"] = after[0]
    return dict(sorted(sections.items(), key=lambda kv: kv[1]))


def section_at(sections: dict[str, int], offset: int) -> str | None:
    """Which Item contains this offset."""
    current = None
    for key, start in sorted(sections.items(), key=lambda kv: kv[1]):
        if start <= offset:
            current = key
        else:
            break
    return current


def _next_version_path(doc_id: str, version: int) -> Path:
    suffix = "" if version == 1 else f"_v{version}"
    return TEXT_DIR / f"{doc_id}{suffix}.txt"


def freeze_one(entry: dict, new_version: bool) -> str:
    doc_id = entry["doc_id"]
    raw_path = ROOT / entry["raw_path"]
    if not raw_path.exists():
        return f"[miss] {doc_id}: raw file missing; run data.download_filings"

    text = html_to_text(raw_path.read_bytes())
    data = text.encode("utf-8")
    digest = sha256_bytes(data)

    if entry.get("text_sha256"):
        if entry["text_sha256"] == digest:
            return f"[same] {doc_id}: frozen text unchanged"
        if not new_version:
            return (
                f"[STOP] {doc_id}: extraction output differs from the frozen text. "
                "Refusing to overwrite. Re-run with --new-version to write a new version; "
                "then revalidate every question."
            )
        version = (entry.get("text_version") or 1) + 1
    else:
        version = 1

    TEXT_DIR.mkdir(parents=True, exist_ok=True)
    path = _next_version_path(doc_id, version)
    path.write_bytes(data)
    sections = detect_sections(text)
    entry.update(
        {
            "text_path": str(path.relative_to(ROOT)),
            "text_sha256": digest,
            "text_version": version,
            "text_chars": len(text),
            "sections": sections,
        }
    )
    lines = [f"[ok]   {doc_id} v{version}: {len(text):,} chars, {len(sections)} sections"]
    for key, start in sections.items():
        preview = text[start : start + 100].replace("\n", " / ")
        lines.append(f"         Item {key:<3} @ {start:>9,}  {preview}")
    return "\n".join(lines)


def redetect_one(entry: dict) -> str:
    """Recompute section offsets from the existing frozen text. The text itself is unchanged."""
    doc_id = entry["doc_id"]
    if not entry.get("text_path"):
        return f"[miss] {doc_id}: not frozen yet"
    data = (ROOT / entry["text_path"]).read_bytes()
    if sha256_bytes(data) != entry.get("text_sha256"):
        return f"[STOP] {doc_id}: frozen text hash mismatch; not touching it"
    text = data.decode("utf-8")
    old = entry.get("sections") or {}
    entry["sections"] = detect_sections(text)
    changed = sorted(set(old.items()) ^ set(entry["sections"].items()))
    lines = [f"[ok]   {doc_id}: {len(entry['sections'])} sections ({len(changed)} changed)"]
    for key, start in entry["sections"].items():
        preview = text[start : start + 90].replace("\n", " / ")
        lines.append(f"         Item {key:<3} @ {start:>9,}  {preview}")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--new-version", action="store_true", help="write a new text version")
    parser.add_argument(
        "--redetect-sections",
        action="store_true",
        help="recompute section offsets from existing frozen text (text unchanged)",
    )
    args = parser.parse_args(argv)

    manifest = load_manifest()
    if not manifest:
        sys.exit("Manifest is empty. Run: python -m data.download_filings")
    for doc_id in sorted(manifest):
        entry = manifest[doc_id]
        if args.redetect_sections:
            print(redetect_one(entry))
        else:
            print(freeze_one(entry, args.new_version))
    save_manifest(manifest)
    if args.redetect_sections:
        print("\nSections changed: run python -m tools.validate_eval_set if you have questions.")


if __name__ == "__main__":
    main()
