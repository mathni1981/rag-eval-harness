import json
from pathlib import Path

import pytest

import tools.find_quote as fq
import tools.validate_eval_set as v
from data.common import sha256_bytes
from data.freeze_text import detect_sections, html_to_text

FIXTURE = Path(__file__).parent / "fixtures" / "sample_10k.htm"


@pytest.fixture
def corpus(tmp_path, monkeypatch):
    text = html_to_text(FIXTURE.read_bytes())
    (tmp_path / "data" / "text").mkdir(parents=True)
    (tmp_path / "data" / "text" / "TST_FY2025_10K.txt").write_text(text, encoding="utf-8")
    manifest = {
        "TST_FY2025_10K": {
            "doc_id": "TST_FY2025_10K",
            "text_path": "data/text/TST_FY2025_10K.txt",
            "text_sha256": sha256_bytes(text.encode()),
            "sections": detect_sections(text),
        },
        "OTH_FY2025_10K": {
            "doc_id": "OTH_FY2025_10K",
            "text_path": "data/text/TST_FY2025_10K.txt",
            "text_sha256": sha256_bytes(text.encode()),
            "sections": detect_sections(text),
        },
    }
    monkeypatch.setattr(fq, "ROOT", tmp_path)
    monkeypatch.setattr(v, "ROOT", tmp_path)
    return text, manifest


def evidence(text, manifest, quote, doc="TST_FY2025_10K"):
    ((s, e),) = fq.find_exact(text, quote)
    return fq.evidence_object(doc, manifest[doc], text, s, e)


def test_find_quote_matches_across_line_breaks(corpus):
    text, manifest = corpus
    ev = evidence(text, manifest, "interest rates could reduce our earnings")
    assert ev["quote"] == "interest rates could\nreduce our earnings"
    assert ev["section"] == "1A"


def test_find_quote_fuzzy_when_not_exact(corpus):
    text, _ = corpus
    assert fq.find_exact(text, "Total revenue was $12.5 billion") == []
    assert fq.find_fuzzy(text, "Total revenue was $12.5 billion")


def run_validate(questions, manifest):
    report = v.Report()
    v.validate(questions, manifest, report)
    return report


def good_question(text, manifest):
    return {
        "id": "q001",
        "type": "single_fact",
        "question": "How much did the company earn in total during fiscal 2025?",
        "gold_answer": "$12.5 billion",
        "key_points": ["$12.5 billion"],
        "evidence": [evidence(text, manifest, "Total revenues were $12.5 billion in 2025.")],
        "source_kind": "narrative",
        "difficulty": "easy",
        "notes": "",
        "author": "human",
    }


def test_valid_question_passes(corpus):
    text, manifest = corpus
    report = run_validate([good_question(text, manifest)], manifest)
    assert report.errors == [] and report.warnings == []


def test_wrong_offset_fails(corpus):
    text, manifest = corpus
    q = good_question(text, manifest)
    q["evidence"][0]["char_start"] += 1
    assert any("does not match" in e for e in run_validate([q], manifest).errors)


def test_wrong_section_fails(corpus):
    text, manifest = corpus
    q = good_question(text, manifest)
    q["evidence"][0]["section"] = "1A"
    assert any("section" in e for e in run_validate([q], manifest).errors)


def test_lexical_leak_warns(corpus):
    text, manifest = corpus
    q = good_question(text, manifest)
    q["question"] = "Were total revenues were $12.5 billion in 2025 or not?"
    assert any("copies the passage" in w for w in run_validate([q], manifest).warnings)


def test_type_rules(corpus):
    text, manifest = corpus
    unans = {
        "id": "q002",
        "type": "unanswerable",
        "question": "What is the 2030 target?",
        "gold_answer": "Not in the documents.",
        "key_points": ["Declines to answer"],
        "evidence": [],
        "difficulty": "medium",
        "notes": "",
        "author": "human",
    }
    comp = good_question(text, manifest) | {"id": "q003", "type": "comparison"}
    comp["evidence"] = comp["evidence"] * 2  # two spans, same doc
    errors = run_validate([unans, comp], manifest).errors
    assert any("need notes" in e for e in errors)
    assert any("span at least 2 documents" in e for e in errors)


def test_hash_mismatch_is_an_error(corpus, tmp_path):
    text, manifest = corpus
    (tmp_path / "data/text/TST_FY2025_10K.txt").write_text(text + "x", encoding="utf-8")
    assert any("hash mismatch" in e for e in run_validate([], manifest).errors)


def test_summary_counts(corpus):
    text, manifest = corpus
    out = v.summary([good_question(text, manifest)])
    assert "single_fact      1 / 18" in out
    json.dumps(out)
