"""Split frozen filings into chunks that keep exact character offsets.

Every chunk's text is exactly text[char_start:char_end] of the frozen file, so retrieval
can be scored against gold evidence spans regardless of chunking strategy.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass

from data.freeze_text import section_at


@dataclass
class Chunk:
    chunk_id: str
    doc: str
    section: str | None
    char_start: int
    char_end: int
    text: str

    def to_dict(self) -> dict:
        return asdict(self)


def _snap_end(text: str, start: int, end: int, limit: int) -> int:
    """Move a cut point back to the nearest paragraph, sentence or word break."""
    if end >= limit:
        return limit
    window = text[start:end]
    for sep in ("\n\n", "\n", ". ", " "):
        pos = window.rfind(sep)
        if pos > len(window) * 0.5:
            return start + pos + len(sep)
    return end


def _snap_start(text: str, start: int, lower: int) -> int:
    """Move a start point forward to the next word boundary."""
    if start <= lower:
        return lower
    while start < len(text) and not text[start - 1].isspace():
        start += 1
    return start


def _split_range(text: str, lo: int, hi: int, size: int, overlap: int) -> list[tuple[int, int]]:
    spans = []
    start = lo
    while start < hi:
        end = _snap_end(text, start, min(start + size, hi), hi)
        if text[start:end].strip():
            spans.append((start, end))
        if end >= hi:
            break
        nxt = _snap_start(text, max(end - overlap, start + 1), lo)
        start = nxt if nxt > start else end
    return spans


def chunk_document(
    doc_id: str, text: str, sections: dict[str, int], strategy: str, size: int, overlap: int
) -> list[Chunk]:
    if size <= 0 or not 0 <= overlap < size:
        raise ValueError("Need size > 0 and 0 <= overlap < size")
    if strategy == "fixed":
        ranges = [(0, len(text))]
    elif strategy == "section":
        bounds = sorted(set([0, *sections.values(), len(text)]))
        ranges = list(zip(bounds[:-1], bounds[1:], strict=True))
    else:
        raise ValueError(f"Unknown chunking strategy: {strategy}")

    chunks = []
    for lo, hi in ranges:
        for start, end in _split_range(text, lo, hi, size, overlap):
            chunks.append(
                Chunk(
                    chunk_id=f"{doc_id}:{start}",
                    doc=doc_id,
                    section=section_at(sections, start),
                    char_start=start,
                    char_end=end,
                    text=text[start:end],
                )
            )
    return chunks
