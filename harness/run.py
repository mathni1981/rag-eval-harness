"""Run the RAG pipeline over the eval set and save every answer.

Usage:
    python -m harness.run --config experiments/configs/baseline.yaml --limit 3   # smoke test
    python -m harness.run --config experiments/configs/baseline.yaml             # all questions
    python -m harness.run --config experiments/configs/baseline.yaml --retrieval-only

Output goes to results/runs/<config name>/:
    answers.jsonl   one record per question: retrieved chunks, answer, citations, tokens
    run.json        config, corpus fingerprint, model, summary
Re-running resumes: questions already answered are skipped. Use --overwrite to start over.
"""

from __future__ import annotations

import argparse
import json
import subprocess
from datetime import UTC, datetime
from pathlib import Path

from dotenv import load_dotenv

from data.common import ROOT, load_manifest
from harness.companies import display_name, fiscal_label
from harness.config import RunConfig, load_config
from harness.generate import generate, make_client
from harness.index import SentenceTransformerEmbedder, corpus_fingerprint, load_or_build
from harness.retrieve import BM25Retriever, DenseRetriever, overlaps

RUNS_DIR = ROOT / "results" / "runs"
QUESTIONS_PATH = ROOT / "eval_set" / "questions.jsonl"


def load_questions(path: Path = QUESTIONS_PATH) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line]


def make_retriever(cfg: RunConfig, index, embedder=None):
    if cfg.retrieval.method == "dense":
        embedder = embedder or SentenceTransformerEmbedder(cfg.retrieval.embedding_model)
        return DenseRetriever(index, embedder)
    if cfg.retrieval.method == "bm25":
        return BM25Retriever(index)
    raise ValueError(f"Unknown retrieval method: {cfg.retrieval.method}")


def gold_hit(chunks: list[dict], evidence: list[dict]) -> dict:
    """Which gold spans were covered by at least one retrieved chunk (quick recall check)."""
    from harness.chunking import Chunk

    objs = [Chunk(**c) for c in chunks]
    covered = [any(overlaps(c, ev) for c in objs) for ev in evidence]
    return {
        "spans": len(evidence),
        "covered": sum(covered),
        "all": all(covered) if covered else None,
    }


def git_commit() -> str | None:
    try:
        out = subprocess.run(
            ["git", "rev-parse", "--short", "HEAD"], cwd=ROOT, capture_output=True, text=True
        )
        return out.stdout.strip() or None
    except OSError:
        return None


def summarize(records: list[dict]) -> dict:
    answerable = [r for r in records if r["type"] != "unanswerable"]
    unans = [r for r in records if r["type"] == "unanswerable"]
    with_ans = [r for r in records if r.get("answer")]
    summary = {
        "questions": len(records),
        "retrieval_all_gold_spans_covered": sum(1 for r in answerable if r["gold_hit"]["all"]),
        "answerable": len(answerable),
    }
    if with_ans:
        summary.update(
            {
                "unanswerable_that_looked_abstained": sum(
                    1 for r in unans if r["answer"]["abstained"]
                ),
                "unanswerable": len(unans),
                "answerable_that_looked_abstained": sum(
                    1 for r in answerable if r.get("answer") and r["answer"]["abstained"]
                ),
                "input_tokens": sum(r["answer"]["input_tokens"] for r in with_ans),
                "output_tokens": sum(r["answer"]["output_tokens"] for r in with_ans),
            }
        )
    return summary


def run(
    cfg: RunConfig,
    questions: list[dict],
    out_dir: Path,
    retrieval_only: bool = False,
    overwrite: bool = False,
    embedder=None,
    client=None,
    manifest: dict | None = None,
) -> dict:
    manifest = manifest if manifest is not None else load_manifest()
    companies = {d: f"{display_name(d, manifest)}, {fiscal_label(d, manifest)}" for d in manifest}
    out_dir.mkdir(parents=True, exist_ok=True)
    answers_path = out_dir / ("retrieval.jsonl" if retrieval_only else "answers.jsonl")
    if overwrite and answers_path.exists():
        answers_path.unlink()

    done = {}
    if answers_path.exists():
        for line in answers_path.read_text(encoding="utf-8").splitlines():
            rec = json.loads(line)
            done[rec["id"]] = rec

    index = load_or_build(cfg, manifest, embedder=embedder)
    retriever = make_retriever(cfg, index, embedder)
    if not retrieval_only and client is None:
        client = make_client()

    todo = [q for q in questions if q["id"] not in done]
    print(f"{len(done)} already done, {len(todo)} to run -> {answers_path.name}")
    with answers_path.open("a", encoding="utf-8") as f:
        for n, q in enumerate(todo, 1):
            hits = retriever.search(q["question"], cfg.retrieval.top_k)
            chunks = [h.chunk.to_dict() for h in hits]
            rec = {
                "id": q["id"],
                "type": q["type"],
                "question": q["question"],
                "retrieved": [
                    {
                        "rank": h.rank,
                        "score": round(h.score, 4),
                        "chunk_id": h.chunk.chunk_id,
                        "doc": h.chunk.doc,
                        "section": h.chunk.section,
                        "char_start": h.chunk.char_start,
                        "char_end": h.chunk.char_end,
                    }
                    for h in hits
                ],
                "gold_hit": gold_hit(chunks, q.get("evidence") or []),
            }
            if not retrieval_only:
                ans = generate(client, cfg.generation, q["question"], hits, companies)
                rec["answer"] = ans.__dict__
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")
            f.flush()
            done[q["id"]] = rec
            status = "" if retrieval_only else f" ({rec['answer']['output_tokens']} tokens out)"
            gh = rec["gold_hit"]
            print(
                f"  [{n}/{len(todo)}] {q['id']} gold covered {gh['covered']}/{gh['spans']}{status}"
            )

    records = [done[q["id"]] for q in questions if q["id"] in done]
    meta = {
        "config": cfg.to_dict(),
        "index_key": cfg.index_key(),
        "corpus": corpus_fingerprint(manifest),
        "git_commit": git_commit(),
        "finished_at": datetime.now(UTC).isoformat(timespec="seconds"),
        "retrieval_only": retrieval_only,
        "summary": summarize(records),
    }
    (out_dir / ("retrieval_run.json" if retrieval_only else "run.json")).write_text(
        json.dumps(meta, indent=2)
    )
    return meta


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("--config", required=True)
    parser.add_argument("--limit", type=int, help="run only the first N questions")
    parser.add_argument("--ids", help="comma-separated question ids, e.g. q001,q019")
    parser.add_argument("--retrieval-only", action="store_true", help="no API calls")
    parser.add_argument("--overwrite", action="store_true", help="discard previous results")
    args = parser.parse_args(argv)

    load_dotenv(ROOT / ".env")
    cfg = load_config(args.config)

    questions = load_questions()
    if args.ids:
        wanted = set(args.ids.split(","))
        questions = [q for q in questions if q["id"] in wanted]
    if args.limit:
        questions = questions[: args.limit]

    meta = run(cfg, questions, RUNS_DIR / cfg.name, args.retrieval_only, args.overwrite)
    print("\nSummary:")
    for key, value in meta["summary"].items():
        print(f"  {key}: {value}")


if __name__ == "__main__":
    main()
