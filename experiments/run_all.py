"""Run experiments: generate answers (or retrieval only) and score each one.

Usage:
    python -m experiments.run_all --retrieval-only        # all configs, retrieval recall only, free
    python -m experiments.run_all --configs topk10,hybrid # full runs: answers + judge
    python -m experiments.run_all                         # every config in experiments/configs

Runs resume, so re-running never repeats paid work. Then:
    python -m experiments.compare
"""

from __future__ import annotations

import argparse
from pathlib import Path

from dotenv import load_dotenv

from data.common import ROOT, load_manifest
from harness.config import load_config
from harness.evaluate import DEFAULT_JUDGE, evaluate
from harness.run import SPLITS, load_questions, run, run_dir_for

CONFIG_DIR = ROOT / "experiments" / "configs"


def config_paths(names: str | None) -> list[Path]:
    if names:
        paths = [CONFIG_DIR / f"{n.strip()}.yaml" for n in names.split(",") if n.strip()]
        missing = [p.name for p in paths if not p.exists()]
        if missing:
            raise SystemExit(f"No such config: {', '.join(missing)}")
        return paths
    return sorted(CONFIG_DIR.glob("*.yaml"))


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("--configs", help="comma-separated config names (default: all)")
    parser.add_argument("--retrieval-only", action="store_true", help="no API calls")
    parser.add_argument("--judge-model", default=DEFAULT_JUDGE)
    parser.add_argument(
        "--split",
        choices=sorted(SPLITS),
        default="dev",
        help="heldout: only for the pre-registered final comparison",
    )
    args = parser.parse_args(argv)

    load_dotenv(ROOT / ".env")
    manifest = load_manifest()
    questions = load_questions(SPLITS[args.split])
    embedders: dict[str, object] = {}
    rerankers: dict[str, object] = {}
    client = None
    if not args.retrieval_only:
        from harness.generate import make_client

        client = make_client()

    for path in config_paths(args.configs):
        cfg = load_config(path)
        print(f"\n=== {cfg.name} ({path.name}) ===")
        r = cfg.retrieval
        embedder = None
        if r.method in ("dense", "hybrid"):
            if r.embedding_model not in embedders:
                from harness.index import SentenceTransformerEmbedder

                embedders[r.embedding_model] = SentenceTransformerEmbedder(r.embedding_model)
            embedder = embedders[r.embedding_model]
        reranker = None
        if r.rerank_model:
            if r.rerank_model not in rerankers:
                from harness.retrieve import CrossEncoderReranker

                rerankers[r.rerank_model] = CrossEncoderReranker(r.rerank_model)
            reranker = rerankers[r.rerank_model]
        run_dir = run_dir_for(cfg.name, args.split)
        run(
            cfg,
            questions,
            run_dir,
            retrieval_only=args.retrieval_only,
            embedder=embedder,
            client=client,
            manifest=manifest,
            reranker=reranker,
        )
        evaluate(
            run_dir,
            questions,
            client,
            args.judge_model,
            judge=not args.retrieval_only,
            manifest=manifest,
        )
    print("\nDone. Compare with: python -m experiments.compare")


if __name__ == "__main__":
    main()
