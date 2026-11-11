import json
from pathlib import Path
from types import SimpleNamespace

import numpy as np
import pytest

from data.common import sha256_bytes
from data.freeze_text import detect_sections, html_to_text
from harness.chunking import chunk_document
from harness.config import RunConfig, load_config
from harness.generate import generate, looks_like_abstention, parse_citations
from harness.index import load_or_build
from harness.prompts import format_context, system_prompt
from harness.retrieve import BM25Retriever, DenseRetriever, overlaps
from harness.run import run

FIXTURE = Path(__file__).parent / "fixtures" / "sample_10k.htm"
REPO = Path(__file__).resolve().parents[1]


def corpus_text():
    t = html_to_text(FIXTURE.read_bytes())
    return t * 3  # long enough for several chunks


@pytest.mark.parametrize("strategy", ["fixed", "section"])
def test_chunks_keep_exact_offsets_and_cover_text(strategy):
    t = corpus_text()
    secs = detect_sections(t)
    chunks = chunk_document("TST", t, secs, strategy, size=300, overlap=50)
    assert chunks
    for c in chunks:
        assert c.text == t[c.char_start : c.char_end]
        assert len(c.text) <= 300
    covered = set()
    for c in chunks:
        covered.update(range(c.char_start, c.char_end))
    non_space = {i for i, ch in enumerate(t) if not ch.isspace()}
    assert non_space <= covered


def test_section_chunks_do_not_cross_section_boundaries():
    t = corpus_text()
    secs = detect_sections(t)
    bounds = sorted(secs.values())
    for c in chunk_document("TST", t, secs, "section", size=300, overlap=50):
        assert not any(c.char_start < b < c.char_end for b in bounds)


def test_bad_chunk_params():
    with pytest.raises(ValueError):
        chunk_document("TST", "abc", {}, "fixed", size=100, overlap=100)
    with pytest.raises(ValueError):
        chunk_document("TST", "abc", {}, "magic", size=100, overlap=0)


def test_overlap_check():
    c = SimpleNamespace(doc="A", char_start=100, char_end=200)
    assert overlaps(c, {"doc": "A", "char_start": 150, "char_end": 400})
    assert not overlaps(c, {"doc": "A", "char_start": 200, "char_end": 300})
    assert not overlaps(c, {"doc": "B", "char_start": 150, "char_end": 160})


class FakeEmbedder:
    """Bag-of-words hashing embedder, so dense retrieval can be tested offline."""

    def _vec(self, text):
        v = np.zeros(256, dtype=np.float32)
        for tok in text.lower().split():
            v[hash(tok.strip(".,$")) % 256] += 1
        n = np.linalg.norm(v)
        return v / n if n else v

    def embed_documents(self, texts):
        return np.stack([self._vec(t) for t in texts])

    def embed_query(self, text):
        return self._vec(text)


@pytest.fixture
def mini_corpus(tmp_path, monkeypatch):
    import data.common
    import harness.index

    text = corpus_text()
    (tmp_path / "data" / "text").mkdir(parents=True)
    (tmp_path / "data" / "text" / "TST_FY2025_10K.txt").write_text(text, encoding="utf-8")
    manifest = {
        "TST_FY2025_10K": {
            "doc_id": "TST_FY2025_10K",
            "company": "Test Co",
            "text_path": "data/text/TST_FY2025_10K.txt",
            "text_sha256": sha256_bytes(text.encode()),
            "sections": detect_sections(text),
        }
    }
    monkeypatch.setattr(harness.index, "ROOT", tmp_path)
    monkeypatch.setattr(data.common, "ROOT", tmp_path)
    return tmp_path, text, manifest


def small_cfg(method="dense"):
    cfg = RunConfig()
    cfg.chunking.size, cfg.chunking.overlap = 300, 50
    cfg.retrieval.method, cfg.retrieval.top_k = method, 2
    return cfg


def test_index_cached_and_rebuilt_when_corpus_changes(mini_corpus, tmp_path):
    _, _, manifest = mini_corpus
    cfg = small_cfg()
    idx1 = load_or_build(cfg, manifest, FakeEmbedder(), index_dir=tmp_path / "idx")
    idx2 = load_or_build(cfg, manifest, embedder=None, index_dir=tmp_path / "idx")  # cached
    assert len(idx1.chunks) == len(idx2.chunks)
    manifest["TST_FY2025_10K"]["text_sha256"] = "changed"
    idx3 = load_or_build(cfg, manifest, FakeEmbedder(), index_dir=tmp_path / "idx")
    assert idx3.embeddings is not None


@pytest.mark.parametrize("method", ["dense", "bm25"])
def test_retrievers_find_the_relevant_chunk(mini_corpus, tmp_path, method):
    _, _, manifest = mini_corpus
    cfg = small_cfg(method)
    idx = load_or_build(cfg, manifest, FakeEmbedder(), index_dir=tmp_path / "idx")
    r = DenseRetriever(idx, FakeEmbedder()) if method == "dense" else BM25Retriever(idx)
    hits = r.search("total revenues billion 2025", 2)
    assert hits[0].rank == 1 and "Total revenues" in hits[0].chunk.text


def test_prompts_and_parsing():
    assert "square brackets" in system_prompt("cited")
    assert "do not guess" in system_prompt("cited_abstain")
    assert "square brackets" not in system_prompt("plain")
    with pytest.raises(ValueError):
        system_prompt("nope")
    assert parse_citations("Revenue rose [2][1], see [2] and [9].", k=5) == [1, 2]
    assert looks_like_abstention("The documents provided do not contain this information.")
    assert not looks_like_abstention("Revenue was $12.5 billion [1].")


class FakeClient:
    def __init__(self, text="Total revenues were $12.5 billion [1]."):
        self.calls = []
        self.messages = self
        self.text = text

    def create(self, **kwargs):
        self.calls.append(kwargs)
        return SimpleNamespace(
            content=[SimpleNamespace(type="text", text=self.text)],
            usage=SimpleNamespace(input_tokens=500, output_tokens=20),
            stop_reason="end_turn",
        )


def test_generate_sends_excerpts_and_omits_null_temperature(mini_corpus, tmp_path):
    _, _, manifest = mini_corpus
    cfg = small_cfg("bm25")
    idx = load_or_build(cfg, manifest, index_dir=tmp_path / "idx")
    hits = BM25Retriever(idx).search("total revenues", 2)
    client = FakeClient()
    cfg.generation.temperature = None
    ans = generate(
        client, cfg.generation, "What were revenues?", hits, {"TST_FY2025_10K": "Test Co"}
    )
    sent = client.calls[0]
    assert "temperature" not in sent
    assert "[1] Test Co (TST_FY2025_10K)" in sent["messages"][0]["content"]
    assert ans.cited == [1] and ans.input_tokens == 500
    assert "[1]" in format_context(hits, {})


def test_run_end_to_end_and_resume(mini_corpus, tmp_path, monkeypatch):
    import harness.index

    _, text, manifest = mini_corpus
    monkeypatch.setattr(harness.index, "INDEX_DIR", tmp_path / "idx")
    start = text.index("Total revenues")
    questions = [
        {
            "id": "q001",
            "type": "single_fact",
            "question": "What were total revenues in 2025?",
            "evidence": [{"doc": "TST_FY2025_10K", "char_start": start, "char_end": start + 20}],
        },
        {
            "id": "q002",
            "type": "unanswerable",
            "question": "What is the 2030 target?",
            "evidence": [],
        },
    ]
    cfg = small_cfg("dense")
    out = tmp_path / "runs" / "t"
    client = FakeClient()
    meta = run(cfg, questions, out, embedder=FakeEmbedder(), client=client, manifest=manifest)
    rows = [json.loads(line) for line in (out / "answers.jsonl").read_text().splitlines()]
    assert [r["id"] for r in rows] == ["q001", "q002"]
    assert rows[0]["gold_hit"]["all"] is True
    assert meta["summary"]["questions"] == 2 and (out / "run.json").exists()
    run(cfg, questions, out, embedder=FakeEmbedder(), client=client, manifest=manifest)
    assert len(client.calls) == 2  # resumed: nothing re-asked


def test_baseline_config_loads():
    cfg = load_config(REPO / "experiments" / "configs" / "baseline.yaml")
    assert cfg.retrieval.method == "dense" and cfg.generation.prompt == "cited"
