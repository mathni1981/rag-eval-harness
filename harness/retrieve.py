"""Retrieval: dense, BM25 or hybrid search, with optional company-aware search and reranking.

Every retriever supports restricting the search to a set of documents, which is what
company-aware retrieval uses.
"""

from __future__ import annotations

import math
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
    idx: int = -1  # position in the index, so rerankers can see the indexed text


def _tokens(text: str) -> list[str]:
    return re.findall(r"[a-z0-9]+", text.lower())


def _mask(index: Index, docs: set[str] | None) -> np.ndarray | None:
    if not docs:
        return None
    return np.array([c.doc in docs for c in index.chunks])


def _top(index: Index, scores: np.ndarray, k: int, docs: set[str] | None) -> list[Hit]:
    scores = scores.astype(np.float64).copy()
    mask = _mask(index, docs)
    if mask is not None:
        scores[~mask] = -np.inf
    order = [i for i in np.argsort(-scores) if np.isfinite(scores[i])][:k]
    return [Hit(r + 1, float(scores[i]), index.chunks[i], int(i)) for r, i in enumerate(order)]


class DenseRetriever:
    def __init__(self, index: Index, embedder: Embedder):
        if index.embeddings is None:
            raise ValueError("Index has no embeddings; build it with retrieval.method: dense")
        self.index = index
        self.embedder = embedder

    def scores(self, query: str) -> np.ndarray:
        return self.index.embeddings @ self.embedder.embed_query(query)  # L2-normalized

    def search(self, query: str, k: int, docs: set[str] | None = None) -> list[Hit]:
        return _top(self.index, self.scores(query), k, docs)


class BM25Retriever:
    def __init__(self, index: Index):
        from rank_bm25 import BM25Okapi

        self.index = index
        self.bm25 = BM25Okapi([_tokens(t) for t in index.texts])

    def scores(self, query: str) -> np.ndarray:
        return np.asarray(self.bm25.get_scores(_tokens(query)))

    def search(self, query: str, k: int, docs: set[str] | None = None) -> list[Hit]:
        return _top(self.index, self.scores(query), k, docs)


class HybridRetriever:
    """Dense + BM25, combined by reciprocal rank fusion: score = sum of 1 / (rrf_k + rank)."""

    def __init__(self, index: Index, embedder: Embedder, rrf_k: int = 60):
        self.index = index
        self.dense = DenseRetriever(index, embedder)
        self.bm25 = BM25Retriever(index)
        self.rrf_k = rrf_k

    def search(self, query: str, k: int, docs: set[str] | None = None) -> list[Hit]:
        mask = _mask(self.index, docs)
        fused = np.zeros(len(self.index.chunks))
        for scores in (self.dense.scores(query), self.bm25.scores(query)):
            scores = scores.astype(np.float64).copy()
            if mask is not None:
                scores[~mask] = -np.inf
            ranks = np.empty(len(scores))
            ranks[np.argsort(-scores)] = np.arange(1, len(scores) + 1)
            fused += 1.0 / (self.rrf_k + ranks)
        if mask is not None:
            fused[~mask] = -np.inf
        return _top(self.index, fused, k, None)


class CrossEncoderReranker:
    def __init__(self, model_name: str):
        from sentence_transformers import CrossEncoder  # heavy import, keep lazy

        self.model = CrossEncoder(model_name)

    def score(self, query: str, texts: list[str]) -> list[float]:
        return [float(s) for s in self.model.predict([(query, t) for t in texts])]


class Pipeline:
    """Base retriever plus optional company-aware search and reranking."""

    def __init__(
        self,
        base,
        index: Index,
        manifest: dict,
        *,
        company_aware: bool = False,
        company_k: str = "split",
        reranker=None,
        rerank_candidates: int = 30,
    ):
        self.base = base
        self.index = index
        self.manifest = manifest
        self.company_aware = company_aware
        self.company_k = company_k
        self.reranker = reranker
        self.rerank_candidates = rerank_candidates

    def _search_group(self, query: str, k: int, docs: set[str] | None) -> list[Hit]:
        if not self.reranker:
            return self.base.search(query, k, docs)
        pool = self.base.search(query, max(k, self.rerank_candidates), docs)
        scores = self.reranker.score(query, [self.index.texts[h.idx] for h in pool])
        ranked = sorted(zip(scores, pool, strict=True), key=lambda x: -x[0])[:k]
        return [Hit(r + 1, s, h.chunk, h.idx) for r, (s, h) in enumerate(ranked)]

    def search(self, query: str, k: int) -> list[Hit]:
        groups: list[set[str] | None] = [None]
        if self.company_aware:
            from harness.companies import detect_companies

            companies = detect_companies(query, self.manifest)
            if companies:
                groups = [{d} for d in companies]
        per_group = k
        if len(groups) > 1 and self.company_k == "split":
            per_group = math.ceil(k / len(groups))
        results = [self._search_group(query, per_group, g) for g in groups]
        merged, seen = [], set()
        for i in range(max(len(r) for r in results)):  # interleave: best of each company first
            for r in results:
                if i < len(r) and r[i].chunk.chunk_id not in seen:
                    seen.add(r[i].chunk.chunk_id)
                    merged.append(r[i])
        return [Hit(n + 1, h.score, h.chunk, h.idx) for n, h in enumerate(merged)]


def build_pipeline(cfg, index: Index, manifest: dict, embedder=None, reranker=None) -> Pipeline:
    r = cfg.retrieval
    if r.method in ("dense", "hybrid") and embedder is None:
        from harness.index import SentenceTransformerEmbedder

        embedder = SentenceTransformerEmbedder(r.embedding_model)
    if r.method == "dense":
        base = DenseRetriever(index, embedder)
    elif r.method == "bm25":
        base = BM25Retriever(index)
    elif r.method == "hybrid":
        base = HybridRetriever(index, embedder, r.rrf_k)
    else:
        raise ValueError(f"Unknown retrieval method: {r.method}")
    if r.rerank_model and reranker is None:
        reranker = CrossEncoderReranker(r.rerank_model)
    return Pipeline(
        base,
        index,
        manifest,
        company_aware=r.company_aware,
        company_k=r.company_k,
        reranker=reranker if r.rerank_model else None,
        rerank_candidates=r.rerank_candidates,
    )


def overlaps(chunk: Chunk, evidence: dict) -> bool:
    """True if a chunk overlaps a gold evidence span in the same document."""
    return (
        chunk.doc == evidence["doc"]
        and chunk.char_start < evidence["char_end"]
        and evidence["char_start"] < chunk.char_end
    )
