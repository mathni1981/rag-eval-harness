"""Rebuild the exact excerpts a run showed the model, from frozen text and stored offsets."""

from __future__ import annotations

from functools import lru_cache

from data.common import ROOT, load_manifest
from harness.companies import display_name, fiscal_label


@lru_cache(maxsize=16)
def _text(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def excerpts_for(record: dict, manifest: dict | None = None) -> list[dict]:
    manifest = manifest if manifest is not None else load_manifest()
    out = []
    for r in record["retrieved"]:
        entry = manifest[r["doc"]]
        text = _text(entry["text_path"])[r["char_start"] : r["char_end"]]
        out.append(
            {
                "rank": r["rank"],
                "label": f"{display_name(r['doc'], manifest)}, {fiscal_label(r['doc'], manifest)}",
                "doc": r["doc"],
                "section": r["section"],
                "text": text.strip(),
            }
        )
    return out


def format_excerpts(excerpts: list[dict]) -> str:
    return "\n\n---\n\n".join(
        f"[{e['rank']}] {e['label']} ({e['doc']}), Item {e['section'] or 'front matter'}\n{e['text']}"
        for e in excerpts
    )
