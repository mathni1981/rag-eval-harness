"""Retrieve the top-k chunks for a question: dense (embeddings) or BM25 (keywords)."""

from __future__ import annotations

import re
from dataclasses import dataclass

import numpy as np

from harness.chunking import Chunk
from harness.index import Embedder, Index


@dataclass
class Hit:
    rank: int
    score: float
    chunk: Chunk


def _tokens(text: str) -> list[str]:
    return re.findall(r"[a-z0-9]+", text.lower())


class DenseRetriever:
    def __init__(self, index: Index, embedder: Embedder):
        if index.embeddings is None:
            raise ValueError("Index has no embeddings; build it with retrieval.method: dense")
        self.index = index
        self.embedder = embedder

    def search(self, query: str, k: int) -> list[Hit]:
        q = self.embedder.embed_query(query)
        scores = self.index.embeddings @ q  # embeddings are L2-normalized
        top = np.argsort(-scores)[:k]
        return [Hit(r + 1, float(scores[i]), self.index.chunks[i]) for r, i in enumerate(top)]


class BM25Retriever:
    def __init__(self, index: Index):
        from rank_bm25 import BM25Okapi

        self.index = index
        self.bm25 = BM25Okapi([_tokens(t) for t in index.texts])

    def search(self, query: str, k: int) -> list[Hit]:
        scores = self.bm25.get_scores(_tokens(query))
        top = np.argsort(-scores)[:k]
        return [Hit(r + 1, float(scores[i]), self.index.chunks[i]) for r, i in enumerate(top)]


def overlaps(chunk: Chunk, evidence: dict) -> bool:
    """True if a chunk overlaps a gold evidence span in the same document."""
    return (
        chunk.doc == evidence["doc"]
        and chunk.char_start < evidence["char_end"]
        and evidence["char_start"] < chunk.char_end
    )
