# Week 1 Spec: Corpus, Tools and Eval Set Foundation

Goal: a frozen, reproducible corpus of six 10-K filings, plus tools that let Mahesh write
50 eval questions with exact, verifiable evidence spans.

Claude Code builds Steps 1–4. Mahesh writes the questions (Step 5).

## Companies

| Ticker | Company | Type | Fiscal year end |
|---|---|---|---|
| MET | MetLife | Insurer | Dec 31 |
| PFG | Principal Financial Group | Insurer / retirement | Dec 31 |
| LNC | Lincoln National | Insurer / retirement | Dec 31 |
| BLK | BlackRock | Asset manager | Dec 31 |
| TROW | T. Rowe Price | Asset manager | Dec 31 |
| BEN | Franklin Resources | Asset manager | **Sep 30** |

Prudential is deliberately excluded (owner's employer).

Note for comparison questions: BEN's fiscal year ends in September, so its most recent 10-K
covers a different period from the others. Record `period_end` in the manifest.

## Step 1: `data/download_filings.py`

1. Read `SEC_USER_AGENT` from `.env`. Exit with a clear error if missing.
2. Resolve tickers to CIKs from `https://www.sec.gov/files/company_tickers_exchange.json`.
   Do not hard-code CIKs. Zero-pad CIKs to 10 digits for data.sec.gov.
3. For each CIK, fetch `https://data.sec.gov/submissions/CIK##########.json`.
   Select the most recent filing with form exactly `10-K` (not `10-K/A`).
4. Download the primary document:
   `https://www.sec.gov/Archives/edgar/data/{cik}/{accession_no_dashes}/{primaryDocument}`.
   Use `primaryDocument` from the API; never guess file names.
5. Save to `data/raw/{doc_id}.htm`. Skip if it already exists.
6. Rate-limit to ≤ 5 requests/second; retry 429/5xx with exponential backoff (max 3 tries).
7. Write/update `data/manifest.json`:

```json
{
  "doc_id": "MET_FY2025_10K",
  "ticker": "MET",
  "company": "MetLife, Inc.",
  "cik": "0001099219",
  "form": "10-K",
  "accession": "0001099219-26-000012",
  "filing_date": "2026-02-20",
  "period_end": "2025-12-31",
  "source_url": "https://www.sec.gov/Archives/edgar/data/...",
  "raw_sha256": "…",
  "text_path": null,
  "text_sha256": null,
  "text_version": null,
  "sections": {}
}
```

(Values above are illustrative only; fill every field from the API response.)

Tests: CIK padding, 10-K vs 10-K/A selection, URL construction, skip-if-exists. Mock HTTP.

## Step 2: `data/freeze_text.py`

1. Parse each raw file with BeautifulSoup (lxml).
2. Remove: `<ix:header>` and its contents, `<script>`, `<style>`, and elements with
   `display:none`.
3. Extract text with block-level elements separated by newlines. Keep table rows on one
   line with cells separated by ` | ` so table facts stay findable.
4. Normalize: Unicode NFKC; non-breaking spaces → spaces; collapse runs of spaces/tabs to
   one space; collapse 3+ newlines to 2; strip trailing whitespace per line.
5. Write `data/text/{doc_id}.txt` (UTF-8, `\n` line endings).
6. Detect section start offsets for Items 1, 1A, 1B, 1C, 2, 3, 4, 5, 7, 7A, 8, 9A.
   **The table of contents also contains these headings.** Use the occurrence after the
   table of contents: e.g., the last match for each item whose following 2,000 characters
   are mostly prose, or the first match after the TOC block ends. Log the chosen offset and
   a 100-character preview for each section so Mahesh can verify.
7. Update the manifest: `text_path`, `text_sha256`, `text_version: 1`, `sections`
   (item → start offset).
8. **Immutability:** if `text_sha256` is already set and the new text differs, refuse to
   overwrite. Require an explicit `--new-version` flag that writes `{doc_id}_v2.txt`.

Tests: normalization rules on small HTML fixtures; TOC-vs-body section detection on a
fixture with both; immutability guard.

## Step 3: `tools/find_quote.py`

The tool Mahesh uses while writing questions.

```
python -m tools.find_quote --doc MET_FY2025_10K --quote "exact text from the filing"
```

- Normalizes the input quote with the same rules as Step 2 before searching.
- Prints every match: `char_start`, `char_end`, section, and 80 characters of context on
  each side.
- If no exact match: print the three closest fuzzy matches (difflib) with offsets, clearly
  labeled as not exact.
- `--json` flag prints a ready-to-paste evidence object:
  `{"doc": ..., "section": ..., "quote": ..., "char_start": ..., "char_end": ...}`.

## Step 4: `tools/validate_eval_set.py` and `eval_set/SCHEMA.md`

Schema for each line of `eval_set/questions.jsonl`:

| Field | Type | Rule |
|---|---|---|
| `id` | string | `q001`… unique |
| `type` | enum | `single_fact`, `multi_passage`, `comparison`, `unanswerable` |
| `question` | string | non-empty |
| `gold_answer` | string | non-empty |
| `key_points` | list[string] | ≥ 1; for `unanswerable`, the expected abstention behavior |
| `evidence` | list[object] | `single_fact`: ≥ 1; `multi_passage`: ≥ 2; `comparison`: ≥ 2 spanning ≥ 2 docs; `unanswerable`: empty |
| `source_kind` | enum | `narrative`, `table`, `mixed` (omit for `unanswerable`) |
| `difficulty` | enum | `easy`, `medium`, `hard` |
| `notes` | string | required non-empty for `unanswerable` (why it isn't answerable) |

Evidence object: `doc`, `section`, `quote`, `char_start`, `char_end`.

Validator checks:

1. JSON parses; schema and type rules above.
2. `doc` exists in the manifest; the frozen file's hash matches `text_sha256`.
3. `text[char_start:char_end] == quote` exactly.
4. `section` matches the section containing `char_start`.
5. Duplicate or near-duplicate questions (warn).
6. Question shares long n-grams with its evidence (warn: lexical leakage — the question
   copies the passage's wording, which makes retrieval artificially easy). Flag any shared
   sequence of 6+ words.
7. Summary: counts by type, company, section, source kind and difficulty, versus the target
   mix (18 single fact, 12 multi-passage, 10 comparison, 10 unanswerable).

Exit code non-zero on errors, zero with warnings.

## Step 5: Questions (Mahesh)

Written by Mahesh using `find_quote` and `validate_eval_set`. Claude Code does not touch
this file. Target: 50 questions in the mix above, spread across all six companies.

## Done when

- `pytest -q` passes
- Six raw filings and six frozen text files exist; manifest complete with hashes and
  section offsets; section previews checked by Mahesh
- `find_quote` and `validate_eval_set` work on a hand-made sample
- 50 questions written and passing validation
