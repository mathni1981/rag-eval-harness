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
