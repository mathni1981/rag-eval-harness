# Eval set schema

`eval_set/questions.jsonl`: one JSON object per line.

| Field | Type | Rule |
|---|---|---|
| `id` | string | `q001`, `q002`, ... unique |
| `type` | string | `single_fact`, `multi_passage`, `comparison`, `unanswerable` |
| `question` | string | Paraphrase; don't copy the passage's wording |
| `gold_answer` | string | The correct answer |
| `key_points` | list of strings | Facts a correct answer must contain. For `unanswerable`: the expected behavior, e.g. "States the 10-K does not disclose this" |
| `evidence` | list | `single_fact` ≥ 1 span; `multi_passage` ≥ 2; `comparison` ≥ 2 across ≥ 2 documents; `unanswerable` empty |
| `source_kind` | string | `narrative`, `table` or `mixed`; omit for `unanswerable` |
| `difficulty` | string | `easy`, `medium`, `hard` |
| `notes` | string | Required for `unanswerable` (why the corpus can't answer it) |
| `author` | string | `human` or `claude` (who drafted the question) |

Evidence span, produced by `python -m tools.find_quote --doc <DOC> --quote "<text>" --json`:

```json
{"doc": "MET_FY2025_10K", "section": "7", "quote": "exact text", "char_start": 123, "char_end": 456}
```

`section` is the Item number (e.g. `7`, `1A`, `15`), or `FS` for financial statements that a
filer places after the last Item (BlackRock does this). `find_quote` fills it in for you.

Offsets are 0-based and end-exclusive, into the frozen file listed in `data/manifest.json`.

Example line (illustrative only, not a real filing fact):

```json
{"id": "q001", "type": "single_fact", "question": "...", "gold_answer": "...", "key_points": ["..."], "evidence": [{"doc": "...", "section": "7", "quote": "...", "char_start": 0, "char_end": 10}], "source_kind": "narrative", "difficulty": "easy", "notes": "", "author": "human"}
```

Target mix for the first 50: 18 single fact, 12 multi-passage, 10 comparison, 10 unanswerable.
