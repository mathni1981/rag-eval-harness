"""Run configuration, loaded from a YAML file in experiments/configs/."""

from __future__ import annotations

import hashlib
import json
from dataclasses import asdict, dataclass, field
from pathlib import Path

import yaml


@dataclass
class ChunkingConfig:
    strategy: str = "fixed"  # "fixed" or "section"
    size: int = 1500  # characters
    overlap: int = 200  # characters


@dataclass
class RetrievalConfig:
    method: str = "dense"  # "dense" or "bm25"
    embedding_model: str = "BAAI/bge-small-en-v1.5"
    top_k: int = 5
    # Prepend "company, fiscal year, Item" to each chunk before embedding/BM25. Filings say
    # "we", not the company name, so without this retrieval can't tell companies apart.
    contextual_header: bool = True


@dataclass
class GenerationConfig:
    model: str = "claude-sonnet-5-5"
    max_tokens: int = 800
    temperature: float | None = None
    prompt: str = "cited"  # see harness/prompts.py


@dataclass
class RunConfig:
    name: str = "baseline"
    chunking: ChunkingConfig = field(default_factory=ChunkingConfig)
    retrieval: RetrievalConfig = field(default_factory=RetrievalConfig)
    generation: GenerationConfig = field(default_factory=GenerationConfig)

    def to_dict(self) -> dict:
        return asdict(self)

    def index_key(self) -> str:
        """Identifies a chunking + embedding combination, so indexes can be reused."""
        payload = {
            "chunking": asdict(self.chunking),
            "model": self.retrieval.embedding_model,
            "header": self.retrieval.contextual_header,
        }
        return hashlib.sha256(json.dumps(payload, sort_keys=True).encode()).hexdigest()[:12]


def load_config(path: str | Path) -> RunConfig:
    raw = yaml.safe_load(Path(path).read_text(encoding="utf-8")) or {}
    unknown = set(raw) - {"name", "chunking", "retrieval", "generation"}
    if unknown:
        raise ValueError(f"Unknown config keys: {sorted(unknown)}")
    return RunConfig(
        name=raw.get("name", "baseline"),
        chunking=ChunkingConfig(**raw.get("chunking", {})),
        retrieval=RetrievalConfig(**raw.get("retrieval", {})),
        generation=GenerationConfig(**raw.get("generation", {})),
    )
