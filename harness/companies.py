"""Readable company names, used in chunk headers and prompts.

SEC legal names ("PRICE T ROWE GROUP INC") don't match how people ask questions
("T. Rowe Price"), so retrieval and prompts use these instead.
"""

from __future__ import annotations

DISPLAY_NAMES = {
    "MET": "MetLife",
    "PFG": "Principal Financial Group (Principal)",
    "LNC": "Lincoln National (Lincoln Financial)",
    "BLK": "BlackRock",
    "TROW": "T. Rowe Price",
    "BEN": "Franklin Templeton (formerly Franklin Resources)",
}


def display_name(doc_id: str, manifest: dict) -> str:
    entry = manifest.get(doc_id, {})
    ticker = entry.get("ticker") or doc_id.split("_")[0]
    return DISPLAY_NAMES.get(ticker, entry.get("company", doc_id))


def fiscal_label(doc_id: str, manifest: dict) -> str:
    end = manifest.get(doc_id, {}).get("period_end")
    return f"fiscal year ended {end}" if end else doc_id


# How people name each company in questions. Matched case-sensitively on word boundaries, so
# "principal executive offices" doesn't match Principal.
ALIASES = {
    "MET": ["MetLife"],
    "PFG": ["Principal Financial", "Principal"],
    "LNC": ["Lincoln National", "Lincoln Financial", "Lincoln", "LLANY"],
    "BLK": ["BlackRock", "iShares"],
    "TROW": ["T. Rowe Price", "T. Rowe", "T Rowe"],
    "BEN": ["Franklin Templeton", "Franklin Resources", "Franklin"],
}


def detect_companies(question: str, manifest: dict) -> list[str]:
    """Doc IDs of companies named in the question, in order of first mention."""
    import re

    found: list[tuple[int, str]] = []
    for doc_id, entry in manifest.items():
        ticker = entry.get("ticker") or doc_id.split("_")[0]
        positions = [
            m.start()
            for alias in ALIASES.get(ticker, [])
            for m in re.finditer(rf"(?<![\w.]){re.escape(alias)}(?!\w)", question)
        ]
        if positions:
            found.append((min(positions), doc_id))
    return [doc_id for _, doc_id in sorted(found)]
