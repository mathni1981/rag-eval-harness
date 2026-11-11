import csv
import json
from types import SimpleNamespace

import pytest

import harness.excerpts as ex
from data.common import sha256_bytes
from harness.evaluate import answer_metrics, bootstrap_ci, evaluate, retrieval_at
from harness.judge import judge_answer, parse_judgment
from tools.judge_agreement import agreement_report, cohen_kappa, load_labels
from tools.make_label_sheet import stratified_sample

VALID = {
    "correctness": "correct",
    "key_points_covered": [True, False],
    "faithfulness": "faithful",
    "unsupported_claims": [],
    "citations": "accurate",
    "reasoning": "ok",
}


def test_parse_judgment_accepts_fenced_json_and_validates():
    out = parse_judgment("```json\n" + json.dumps(VALID) + "\n```", 2)
    assert out["correctness"] == "correct"
    with pytest.raises(ValueError):
        parse_judgment(json.dumps(VALID | {"correctness": "great"}), 2)
    with pytest.raises(ValueError):
        parse_judgment(json.dumps(VALID), 3)  # wrong number of key points
    with pytest.raises(ValueError):
        parse_judgment("no json here", 2)


class FakeJudge:
    def __init__(self, replies):
        self.replies = list(replies)
        self.messages = self
        self.calls = 0

    def create(self, **kwargs):
        self.calls += 1
        text = self.replies.pop(0) if len(self.replies) > 1 else self.replies[0]
        return SimpleNamespace(
            content=[SimpleNamespace(type="text", text=text)],
            usage=SimpleNamespace(input_tokens=1000, output_tokens=80),
        )


def test_judge_retries_once_on_bad_output():
    q = {
        "id": "q1",
        "type": "single_fact",
        "question": "?",
        "gold_answer": "x",
        "key_points": ["a", "b"],
    }
    client = FakeJudge(["not json", json.dumps(VALID)])
    out = judge_answer(client, "judge-model", q, "answer", "excerpts")
    assert client.calls == 2 and out["judge_model"] == "judge-model"
    with pytest.raises(RuntimeError):
        judge_answer(FakeJudge(["bad"]), "m", q, "answer", "excerpts")


def test_bootstrap_ci_brackets_the_mean_and_is_deterministic():
    xs = [1.0] * 30 + [0.0] * 20
    ci = bootstrap_ci(xs)
    assert ci[0] < 0.6 < ci[1] and ci == bootstrap_ci(xs)
    assert bootstrap_ci([1.0]) is None


def test_retrieval_at_k():
    rec = {
        "retrieved": [
            {"rank": 1, "doc": "A", "char_start": 0, "char_end": 100},
            {"rank": 4, "doc": "B", "char_start": 0, "char_end": 100},
        ]
    }
    ev = [
        {"doc": "A", "char_start": 10, "char_end": 20},
        {"doc": "B", "char_start": 50, "char_end": 60},
    ]
    assert retrieval_at(rec, ev, 3) == ([True, False], False)
    assert retrieval_at(rec, ev, 5) == ([True, True], True)


def test_answer_metrics_split_answerable_and_unanswerable():
    rows = [
        {
            "q": {"type": "single_fact", "author": "claude"},
            "j": {"correctness": "correct", "faithfulness": "faithful", "citations": "accurate"},
            "retrieved_all": True,
        },
        {
            "q": {"type": "comparison", "author": "claude"},
            "j": {
                "correctness": "partial",
                "faithfulness": "unfaithful",
                "citations": "inaccurate",
            },
            "retrieved_all": False,
        },
        {
            "q": {"type": "unanswerable", "author": "claude"},
            "j": {
                "correctness": "incorrect",
                "faithfulness": "unfaithful",
                "citations": "accurate",
            },
            "retrieved_all": False,
        },
    ]
    m = answer_metrics(rows)
    assert m["answerable"]["correctness_score"]["value"] == 0.75
    assert m["unanswerable"]["answered_anyway"]["value"] == 1.0
    assert m["correctness_by_retrieval"]["all_evidence_retrieved"]["value"] == 1.0
    assert m["correctness_by_retrieval"]["evidence_missing"]["value"] == 0.5


@pytest.fixture
def run_dir(tmp_path, monkeypatch):
    text = "Item 7. MD&A\nTotal revenues were $12.5 billion in 2025.\n" * 5
    (tmp_path / "data" / "text").mkdir(parents=True)
    (tmp_path / "data" / "text" / "T.txt").write_text(text)
    manifest = {
        "T": {
            "doc_id": "T",
            "ticker": "TST",
            "company": "Test",
            "period_end": "2025-12-31",
            "text_path": "data/text/T.txt",
            "text_sha256": sha256_bytes(text.encode()),
            "sections": {"7": 0},
        }
    }
    monkeypatch.setattr(ex, "ROOT", tmp_path)
    ex._text.cache_clear()
    run = tmp_path / "runs" / "r"
    run.mkdir(parents=True)
    retrieved = [{"rank": 1, "doc": "T", "section": "7", "char_start": 0, "char_end": 60}]
    answers = [
        {
            "id": "q001",
            "type": "single_fact",
            "retrieved": retrieved,
            "answer": {"text": "$12.5 billion [1]."},
        },
        {
            "id": "q002",
            "type": "unanswerable",
            "retrieved": retrieved,
            "answer": {"text": "Not in the documents."},
        },
    ]
    (run / "answers.jsonl").write_text("\n".join(json.dumps(a) for a in answers) + "\n")
    (run / "run.json").write_text(json.dumps({"config": {"retrieval": {"top_k": 5}}}))
    questions = [
        {
            "id": "q001",
            "type": "single_fact",
            "question": "Revenue?",
            "gold_answer": "$12.5 billion",
            "key_points": ["$12.5 billion"],
            "evidence": [{"doc": "T", "char_start": 13, "char_end": 50}],
            "author": "claude",
        },
        {
            "id": "q002",
            "type": "unanswerable",
            "question": "2030?",
            "gold_answer": "Not in docs",
            "key_points": ["declines"],
            "evidence": [],
            "author": "claude",
        },
    ]
    return run, questions, manifest


def test_evaluate_end_to_end_and_resume(run_dir):
    run, questions, manifest = run_dir
    v1 = VALID | {"key_points_covered": [True]}
    v2 = VALID | {
        "correctness": "abstained",
        "faithfulness": "n/a",
        "citations": "n/a",
        "key_points_covered": [True],
    }
    client = FakeJudge([json.dumps(v1), json.dumps(v2)])
    scores = evaluate(run, questions, client, "judge", manifest=manifest)
    assert scores["retrieval"]["question_recall@1"]["value"] == 1.0
    assert scores["answers"]["unanswerable"]["abstained"]["value"] == 1.0
    assert (run / "report.md").read_text().startswith("# Evaluation")
    evaluate(run, questions, client, "judge", manifest=manifest)
    assert client.calls == 2  # nothing re-judged
    assert "[1] Test" not in (run / "judgments.jsonl").read_text()


def test_no_judge_mode_needs_no_client(run_dir):
    run, questions, manifest = run_dir
    scores = evaluate(run, questions, client=None, judge=False, manifest=manifest)
    assert "answers" not in scores and "span_recall@5" in scores["retrieval"]


def test_stratified_sample_size_and_types():
    qs = [
        {"id": f"q{i:03d}", "type": t}
        for i, t in enumerate(
            ["single_fact"] * 18
            + ["multi_passage"] * 12
            + ["comparison"] * 10
            + ["unanswerable"] * 10
        )
    ]
    s = stratified_sample(qs, 30)
    assert len(s) == 30 and len({q["type"] for q in s}) == 4
    assert s == stratified_sample(qs, 30)


def test_kappa_and_agreement(tmp_path):
    assert cohen_kappa(["a", "b", "a", "b"], ["a", "b", "a", "b"]) == 1.0
    assert round(cohen_kappa(["a", "a", "b", "b"], ["a", "b", "a", "b"]), 3) == 0.0
    p = tmp_path / "l.csv"
    with p.open("w", newline="") as f:
        w = csv.DictWriter(
            f, fieldnames=["id", "type", "correctness", "faithfulness", "citations", "notes"]
        )
        w.writeheader()
        w.writerow(
            {
                "id": "q001",
                "type": "single_fact",
                "correctness": "Correct",
                "faithfulness": "faithful",
                "citations": "accurate",
            }
        )
        w.writerow({"id": "q002", "type": "unanswerable"})  # unlabeled row is skipped
        w.writerow(
            {
                "id": "q003",
                "type": "single_fact",
                "correctness": "great",
                "faithfulness": "faithful",
                "citations": "accurate",
            }
        )
    labels, problems = load_labels(p)
    assert set(labels) == {"q001", "q003"} and len(problems) == 1
    del labels["q003"]
    report = agreement_report("r", labels, {"q001": VALID | {"citations": "inaccurate"}})
    assert (
        "| correctness | 1/1 (100%)" in report
        and "| q001 | citations | accurate | inaccurate |" in report
    )


def test_api_key_lookup_prefers_env_then_keychain(monkeypatch):
    import harness.secrets as sec

    monkeypatch.setenv("ANTHROPIC_API_KEY", "from-env")
    assert sec.anthropic_api_key() == "from-env"
    monkeypatch.delenv("ANTHROPIC_API_KEY")
    monkeypatch.setattr(sec.platform, "system", lambda: "Darwin")
    monkeypatch.setattr(
        sec.subprocess,
        "run",
        lambda *a, **k: SimpleNamespace(returncode=0, stdout="from-keychain\n"),
    )
    assert sec.anthropic_api_key() == "from-keychain"
    monkeypatch.setattr(
        sec.subprocess, "run", lambda *a, **k: SimpleNamespace(returncode=44, stdout="")
    )
    assert sec.anthropic_api_key() is None


def test_make_client_uses_key_if_present_else_profile(monkeypatch):
    import anthropic

    import harness.secrets as sec
    from harness.generate import make_client

    calls = []
    monkeypatch.setattr(anthropic, "Anthropic", lambda **kw: calls.append(kw) or "client")
    monkeypatch.setattr(sec, "anthropic_api_key", lambda: "k")
    make_client()
    monkeypatch.setattr(sec, "anthropic_api_key", lambda: None)
    make_client()
    assert calls[0]["api_key"] == "k" and "api_key" not in calls[1]


def test_old_rubric_judgments_are_archived_and_redone(run_dir):
    run, questions, manifest = run_dir
    old = VALID | {"key_points_covered": [True], "id": "q001"}  # no rubric_version → v1
    (run / "judgments.jsonl").write_text(json.dumps(old) + "\n")
    v1 = VALID | {"key_points_covered": [True]}
    v2 = VALID | {
        "correctness": "abstained",
        "faithfulness": "n/a",
        "citations": "n/a",
        "key_points_covered": [True],
    }
    client = FakeJudge([json.dumps(v1), json.dumps(v2)])
    scores = evaluate(run, questions, client, "judge", manifest=manifest)
    assert client.calls == 2 and (run / "judgments.rubric-v1.jsonl").exists()
    assert scores["rubric_version"] == "2"
    assert all(
        json.loads(x)["rubric_version"] == "2"
        for x in (run / "judgments.jsonl").read_text().splitlines()
    )


def test_declines_split_by_whether_evidence_was_retrieved():
    j = {"correctness": "abstained", "faithfulness": "n/a", "citations": "n/a"}
    rows = [
        {"q": {"id": "q1", "type": "single_fact"}, "j": j, "retrieved_all": True},
        {"q": {"id": "q2", "type": "single_fact"}, "j": j, "retrieved_all": False},
        {
            "q": {"id": "q3", "type": "single_fact"},
            "j": j | {"correctness": "correct"},
            "retrieved_all": True,
        },
    ]
    d = answer_metrics(rows)["answerable_declines"]
    assert d == {"total": 2, "evidence_was_retrieved": ["q1"], "evidence_not_retrieved": ["q2"]}


def test_rubric_states_the_agreed_rules():
    from harness.rubric import RUBRIC

    assert 'for one side but not the other is "partial"' in RUBRIC
    assert "including facts mentioned inside a decline" in RUBRIC
