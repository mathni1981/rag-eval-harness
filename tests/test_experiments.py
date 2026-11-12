import numpy as np
import pytest

from experiments.compare import config_diff, paired_delta
from experiments.run_all import config_paths
from harness.chunking import Chunk
from harness.companies import detect_companies
from harness.evaluate import retrieval_metrics
from harness.index import Index
from harness.retrieve import BM25Retriever, HybridRetriever, Pipeline

MANIFEST = {
    "MET_FY2025_10K": {"ticker": "MET"},
    "PFG_FY2025_10K": {"ticker": "PFG"},
    "LNC_FY2025_10K": {"ticker": "LNC"},
    "TROW_FY2025_10K": {"ticker": "TROW"},
}


def test_detect_companies_order_and_case():
    assert detect_companies("Compare Principal with MetLife", MANIFEST) == [
        "PFG_FY2025_10K",
        "MET_FY2025_10K",
    ]
    assert detect_companies(
        "Where are Lincoln National's principal executive offices?", MANIFEST
    ) == ["LNC_FY2025_10K"]
    assert detect_companies("What about T. Rowe Price?", MANIFEST) == ["TROW_FY2025_10K"]
    assert detect_companies("Which LLANY arrangement?", MANIFEST) == ["LNC_FY2025_10K"]
    assert detect_companies("No company here", MANIFEST) == []


def toy_index():
    rows = [
        ("MET_FY2025_10K", "MetLife employees total 46,000 people"),
        ("MET_FY2025_10K", "MetLife segments group benefits"),
        ("PFG_FY2025_10K", "Principal employees total 19,700 people"),
        ("PFG_FY2025_10K", "Principal assets under management"),
        ("LNC_FY2025_10K", "Lincoln employees total 9,423 people"),
    ]
    chunks = [Chunk(f"{d}:{i}", d, "1", i, i + 1, t) for i, (d, t) in enumerate(rows)]
    return Index(chunks, None, [c.text for c in chunks])


class FakeEmbedder:
    def _v(self, t):
        v = np.zeros(64)
        for w in t.lower().split():
            v[hash(w) % 64] += 1
        return v / (np.linalg.norm(v) or 1)

    def embed_query(self, t):
        return self._v(t)


def test_doc_filter_restricts_results():
    idx = toy_index()
    hits = BM25Retriever(idx).search("employees total people", 5, docs={"PFG_FY2025_10K"})
    assert hits and all(h.chunk.doc == "PFG_FY2025_10K" for h in hits)


def test_company_aware_pipeline_searches_each_company_and_interleaves():
    idx = toy_index()
    p = Pipeline(BM25Retriever(idx), idx, MANIFEST, company_aware=True, company_k="split")
    hits = p.search("How many employees do MetLife and Principal have?", 4)
    assert [h.chunk.doc for h in hits][:2] == ["MET_FY2025_10K", "PFG_FY2025_10K"]
    assert [h.rank for h in hits] == list(range(1, len(hits) + 1)) and len(hits) == 4
    single = p.search("How many employees does Lincoln have?", 3)
    assert {h.chunk.doc for h in single} == {"LNC_FY2025_10K"}


def test_hybrid_and_reranker():
    idx = toy_index()
    idx.embeddings = np.stack([FakeEmbedder()._v(t) for t in idx.texts])
    hits = HybridRetriever(idx, FakeEmbedder()).search("Lincoln employees", 2)
    assert hits[0].chunk.doc == "LNC_FY2025_10K"

    class Reverse:  # prefers longer texts, to prove the reranker reorders
        def score(self, q, texts):
            return [len(t) for t in texts]

    p = Pipeline(BM25Retriever(idx), idx, MANIFEST, reranker=Reverse(), rerank_candidates=5)
    out = p.search("employees", 2)
    lengths = [len(h.chunk.text) for h in out]
    assert lengths == sorted(lengths, reverse=True)


def test_recall_at_all_counts_everything_shown():
    rec = {
        "retrieved": [
            {"rank": r, "doc": "A", "char_start": 10 * r, "char_end": 10 * r + 5}
            for r in range(1, 7)
        ]
    }
    q = {"type": "single_fact", "evidence": [{"doc": "A", "char_start": 61, "char_end": 63}]}
    m = retrieval_metrics([(q, rec)], [5])
    assert m["question_recall@5"]["value"] == 0.0 and m["question_recall@all"]["value"] == 1.0


def test_compare_helpers():
    base = {"name": "baseline", "retrieval": {"top_k": 5, "method": "dense"}}
    assert (
        config_diff({"name": "x", "retrieval": {"top_k": 10, "method": "dense"}}, base)
        == "top_k=10"
    )
    d, ci = paired_delta({"a": 1.0, "b": 1.0, "c": 0.5}, {"a": 0.0, "b": 1.0, "c": 0.5})
    assert round(d, 3) == 0.333 and ci[0] <= d <= ci[1]


def test_all_experiment_configs_load():
    from harness.config import load_config

    paths = config_paths(None)
    names = {p.stem for p in paths}
    assert {
        "baseline",
        "topk10",
        "topk15",
        "company_aware",
        "hybrid",
        "section_chunks",
        "rerank",
    } <= names
    for p in paths:
        assert load_config(p).name == p.stem
    with pytest.raises(SystemExit):
        config_paths("nope")


def test_config_diff_ignores_settings_added_later():
    old_baseline = {"name": "baseline", "retrieval": {"method": "dense", "top_k": 5}}
    new = {
        "name": "hybrid",
        "retrieval": {"method": "hybrid", "top_k": 5, "company_aware": False, "rrf_k": 60},
    }
    assert config_diff(new, old_baseline) == "method=hybrid"


def test_split_helpers_and_final_config():
    from harness.config import load_config
    from harness.run import SPLITS, run_dir_for, split_of

    assert run_dir_for("final", "heldout").name == "final__heldout"
    assert run_dir_for("final").name == "final"
    assert split_of("final__heldout") == "heldout" and split_of("topk10") == "dev"
    assert set(SPLITS) == {"dev", "heldout"}
    from experiments.run_all import CONFIG_DIR

    cfg = load_config(CONFIG_DIR / "final.yaml")
    assert cfg.retrieval.company_aware and cfg.retrieval.rerank_model and cfg.retrieval.top_k == 5


def test_heldout_set_is_valid_and_separate():
    import json
    from pathlib import Path

    root = Path(__file__).resolve().parents[1]
    path = root / "eval_set" / "heldout.jsonl"
    if not path.exists():
        pytest.skip("held-out set not present")
    held = [json.loads(x) for x in path.read_text().splitlines() if x]
    assert len(held) == 50 and all(q["id"].startswith("h") for q in held)
    dev_path = root / "eval_set" / "questions.jsonl"
    if dev_path.exists():
        dev = {json.loads(x)["question"] for x in dev_path.read_text().splitlines() if x}
        assert not dev & {q["question"] for q in held}
