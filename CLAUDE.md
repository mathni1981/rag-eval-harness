# RAG Eval Harness — Claude Code instructions

Question answering over public SEC 10-K filings, with an evaluation harness that measures
retrieval recall, faithfulness, correctness, citation accuracy and abstention.
Owner: Mahesh Nidhruva. Code is built with Claude Code and reviewed by Mahesh.

Week 1 design (built and tested): @docs/week1-spec.md
Week 2 (built and tested): `harness/` runs the baseline pipeline; see README "Running the pipeline".
Next: Week 3 evaluation in `harness/evaluate.py` (recall@k, LLM judge, abstention, judge agreement).

## Hard rules

1. **Eval questions sign-off.** The first 50 questions were drafted by Claude
   (`"author": "claude"`) and then reviewed by Mahesh using `eval_set/REVIEW.md`. Never change
   question content, gold answers or evidence without being asked, and never relabel a
   question's `author`. New human-written questions use `"author": "human"`.
2. **Never commit data or secrets.** `data/raw/`, `data/text/` and `.env` stay out of git.
   Commit `data/manifest.json` only.
3. **Frozen text is immutable.** Once a file in `data/text/` is listed in the manifest with a
   hash, never regenerate or modify it. If extraction must change, write to a new version
   (`_v2`) and say so; existing offsets point into the old file.
4. **SEC fair access.** Every EDGAR request sends `User-Agent` from the `SEC_USER_AGENT`
   environment variable (name + email). Stay at or below 5 requests/second. Cache raw
   downloads; never re-download a file that exists.
5. **Small, reviewable changes.** One module per change, with tests. Explain design choices
   in the PR/commit message so Mahesh can review them.

## Stack and commands

- Python 3.11+, virtual env in `.venv/`
- Dependencies in `requirements.txt` (pin versions)
- Tests: `pytest -q`
- Lint/format: `ruff check . && ruff format .`

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env            # then set SEC_USER_AGENT
python -m data.download_filings # Step 1
python -m data.freeze_text      # Step 2
python -m tools.find_quote --doc MET_FY2025_10K --quote "exact text"
python -m tools.validate_eval_set
pytest -q
```

## Repository layout

```
data/
  common.py               paths, manifest I/O, text normalization (changing it invalidates offsets)
  download_filings.py     EDGAR download → data/raw/, writes manifest
  freeze_text.py          HTML → normalized text in data/text/, section offsets, hashes
  manifest.json           committed: companies, filings, hashes, section offsets
  raw/                    ignored
  text/                   ignored (reproducible from manifest)
tools/
  find_quote.py           returns char offsets for an exact quote in a frozen file
  validate_eval_set.py    checks questions.jsonl against schema and frozen text
eval_set/
  questions.jsonl         eval set (first 50 drafted by Claude, reviewed by Mahesh)
  REVIEW.md               review checklist for the drafted questions
  SCHEMA.md               field definitions
harness/
  config.py               run configs (experiments/configs/*.yaml)
  chunking.py             fixed and section-aware chunks with exact offsets
  companies.py            readable company names for headers and prompts
  index.py                chunk index + embeddings cache in data/index/ (ignored)
  retrieve.py             dense and BM25 retrievers; gold-span overlap check
  prompts.py              prompt variants: plain, cited, cited_abstain
  generate.py             Claude call, citation parsing
  run.py                  end-to-end run → results/runs/<name>/ (committed)
experiments/configs/      one YAML per run (baseline.yaml)
results/runs/             answers.jsonl + run.json per run (committed)
tests/
```

## Conventions

- Document IDs: `{TICKER}_FY{year}_10K`, e.g. `MET_FY2025_10K`
- Character offsets are 0-based, end-exclusive, into the frozen UTF-8 text file
- All scripts are runnable as modules and idempotent
- Prefer standard library + requests + beautifulsoup4/lxml; ask before adding dependencies
- No notebooks in `harness/`; notebooks only under `notebooks/` with outputs stripped
