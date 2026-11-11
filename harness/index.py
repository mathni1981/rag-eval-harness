"""Build (or load) the chunk index for a config: chunks plus, for dense retrieval, embeddings.

Usage:
    python -m harness.index --config experiments/configs/baseline.yaml

Indexes are cached in data/index/<index_key>/ (not committed) and rebuilt automatically if
any frozen filing changes.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Protocol

import numpy as np

from data.common import DATA_DIR, ROOT, load_manifest
from harness.chunking import Chunk, chunk_document
from harness.companies import display_name, fiscal_label
from harness.config import RunConfig, load_config

INDEX_DIR = DATA_DIR / "index"

# Some embedding models expect an instruction prefix on queries (not on documents).
QUERY_PREFIXES = {
    "BAAI/bge-small-en-v1.5": "Represent this sentence for searching relevant passages: ",
    "BAAI/bge-base-en-v1.5": "Represent this sentence for searching relevant passages: ",
}


class Embedder(Protocol):
    def embed_documents(self, texts: list[str]) -> np.ndarray: ...
    def embed_query(self, text: str) -> np.ndarray: ...


class SentenceTransformerEmbedder:
    """Local embedding model; downloads once from Hugging Face, then runs offline."""

    def __init__(self, model_name: str, batch_size: int = 32):
        from sentence_transformers import SentenceTransformer  # heavy import, keep lazy

        self.model = SentenceTransformer(model_name)
        self.prefix = QUERY_PREFIXES.get(model_name, "")
        self.batch_size = batch_size

    def embed_documents(self, texts: list[str]) -> np.ndarray:
        vecs = self.model.encode(
            texts, batch_size=self.batch_size, normalize_embeddings=True, show_progress_bar=True
        )
        return np.asarray(vecs, dtype=np.float32)

    def embed_query(self, text: str) -> np.ndarray:
        vec = self.model.encode([self.prefix + text], normalize_embeddings=True)
        return np.asarray(vec[0], dtype=np.float32)


def corpus_fingerprint(manifest: dict) -> dict[str, str]:
    return {d: e["text_sha256"] for d, e in sorted(manifest.items()) if e.get("text_sha256")}


def build_chunks(cfg: RunConfig, manifest: dict) -> list[Chunk]:
    chunks: list[Chunk] = []
    for doc_id, entry in sorted(manifest.items()):
        if not entry.get("text_path"):
            continue
        text = (ROOT / entry["text_path"]).read_text(encoding="utf-8")
        chunks += chunk_document(
            doc_id,
            text,
            entry.get("sections") or {},
            cfg.chunking.strategy,
            cfg.chunking.size,
            cfg.chunking.overlap,
        )
    return chunks


def index_text(chunk: Chunk, manifest: dict, header: bool) -> str:
    """Text used for retrieval. The chunk's own text (and offsets) never change."""
    if not header:
        return chunk.text
    name = display_name(chunk.doc, manifest)
    item = chunk.section or "front matter"
    return f"{name} 10-K, {fiscal_label(chunk.doc, manifest)}, Item {item}\n{chunk.text}"


class Index:
    def __init__(self, chunks: list[Chunk], embeddings: np.ndarray | None, texts: list[str]):
        self.chunks = chunks
        self.embeddings = embeddings
        self.texts = texts  # what retrieval sees: chunk text, optionally with a header


def load_or_build(
    cfg: RunConfig,
    manifest: dict | None = None,
    embedder: Embedder | None = None,
    index_dir: Path | None = None,
) -> Index:
    manifest = manifest if manifest is not None else load_manifest()
    index_dir = index_dir if index_dir is not None else INDEX_DIR  # resolved at call time
    path = index_dir / cfg.index_key()
    fingerprint = corpus_fingerprint(manifest)
    dense = cfg.retrieval.method == "dense"

    meta_path = path / "meta.json"
    if meta_path.exists():
        meta = json.loads(meta_path.read_text())
        fresh = meta.get("corpus") == fingerprint
        has_vectors = (path / "embeddings.npy").exists()
        if fresh and (has_vectors or not dense):
            chunks = [Chunk(**json.loads(line)) for line in (path / "chunks.jsonl").open()]
            vecs = np.load(path / "embeddings.npy") if has_vectors else None
            texts = [index_text(c, manifest, cfg.retrieval.contextual_header) for c in chunks]
            print(f"Loaded index {cfg.index_key()}: {len(chunks):,} chunks")
            return Index(chunks, vecs, texts)

    chunks = build_chunks(cfg, manifest)
    texts = [index_text(c, manifest, cfg.retrieval.contextual_header) for c in chunks]
    print(f"Built {len(chunks):,} chunks ({cfg.chunking.strategy}, size {cfg.chunking.size})")
    vecs = None
    if dense:
        embedder = embedder or SentenceTransformerEmbedder(cfg.retrieval.embedding_model)
        print(f"Embedding with {cfg.retrieval.embedding_model} (first run takes a few minutes)...")
        vecs = embedder.embed_documents(texts)

    path.mkdir(parents=True, exist_ok=True)
    with (path / "chunks.jsonl").open("w", encoding="utf-8") as f:
        for c in chunks:
            f.write(json.dumps(c.to_dict(), ensure_ascii=False) + "\n")
    if vecs is not None:
        np.save(path / "embeddings.npy", vecs)
    meta = {"config": cfg.to_dict(), "corpus": fingerprint, "n_chunks": len(chunks)}
    meta_path.write_text(json.dumps(meta, indent=2))
    return Index(chunks, vecs, texts)


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", required=True)
    args = parser.parse_args(argv)
    idx = load_or_build(load_config(args.config))
    lengths = [c.char_end - c.char_start for c in idx.chunks]
    print(f"Chunks: {len(idx.chunks):,}; mean length {sum(lengths) / len(lengths):,.0f} chars")


if __name__ == "__main__":
    main()
