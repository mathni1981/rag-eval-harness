# Week 4: Experiments

## The experiments

Each config in `experiments/configs/` is identical to `baseline.yaml` except for one change, so
any difference in results can be attributed to that change.

| Config | Change | Why |
|---|---|---|
| `topk10`, `topk15` | Show 10 or 15 excerpts instead of 5 | Half the baseline's misses may simply be cut off at 5 |
| `company_aware` | Search only the company named in the question; for comparisons, search each company separately (about 5 excerpts total) | Comparisons scored 25%: one search rarely surfaces two companies |
| `hybrid` | Embeddings + BM25 keyword search, fused by reciprocal rank | Filings are full of exact terms and figures that keyword search matches well |
| `section_chunks` | Chunks never cross a 10-K Item boundary | Keeps each chunk about one topic |
| `rerank` | Rerank the top 30 with a cross-encoder (`BAAI/bge-reranker-base`), keep 5 | A stronger relevance model on a small candidate pool |

## Workflow

1. **Free first pass, retrieval only:**
   `python -m experiments.run_all --retrieval-only` then `python -m experiments.compare`
   Shows recall for every experiment before spending anything. First run downloads the reranker
   model and builds the section-chunk index (a few minutes).
2. **Full runs (answers + judge):** `python -m experiments.run_all`
   Runs all six. Resumes, so an interruption never repeats paid work. Run them all, not just the
   ones that looked good in step 1: reporting only the winners would bias the results.
3. **Compare:** `python -m experiments.compare` → `results/experiments.md`

## Reading the results

- **Δ correctness** uses a paired bootstrap: both runs are resampled on the same questions, so the
  interval reflects the difference itself. If the interval includes 0, the change isn't
  distinguishable from noise with 40 questions.
- **Input tokens per question** is the cost side: `topk15` will improve recall partly by sending
  three times as much text.
- **Company detection** matches company names in the question text only (never the question's
  type or gold evidence). It found the right companies for all 50 questions, but these questions
  name companies explicitly; real users may not, so treat `company_aware` results as an upper bound.

## Lines to add to README.md (under "Running the pipeline")

```bash
python -m experiments.run_all --retrieval-only   # all experiments, recall only, free
python -m experiments.run_all                    # all experiments, answers + judge
python -m experiments.compare                    # → results/experiments.md
```

## Lines to add to CLAUDE.md (repository layout)

```
experiments/
  configs/                one YAML per run; each experiment changes one thing from baseline
  run_all.py              runs and scores experiments (resumable)
  compare.py              comparison table with paired bootstrap deltas → results/experiments.md
```

Also add under harness/: `retrieve.py` now covers dense, BM25 and hybrid retrieval, company-aware
search and cross-encoder reranking.
