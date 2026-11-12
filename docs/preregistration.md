# Pre-registration: final design and held-out test

Written 2026-11-11, before the held-out questions were run through any configuration.
Committed to Git before the held-out run, so the commit history shows it came first.

## Why pre-register

The six Week 4 experiments were all scored on the same 50 development questions. Picking the
best-looking combination from those results and reporting its score on the same questions would
overstate it. Instead, the final design is fixed here, then measured once on 50 new questions it
was never tuned on.

## The final design (`experiments/configs/final.yaml`)

Baseline plus two changes, both of which helped on the development set at no extra cost:

| Change | Development-set evidence |
|---|---|
| Cross-encoder reranking (`BAAI/bge-reranker-base`, top 30 candidates reranked to 5) | Correctness 69% → 80% (+11 points, 95% CI +0 to +22) |
| Company-aware retrieval (search each named company separately, about 5 excerpts total) | Comparisons 25% → 40%; overall +4 points (+0 to +9) |

They address different failure modes (ranking quality vs. covering both companies in a
comparison), so the expectation is that they combine. The combination itself was not tested on the
development set before this was written.

Not included: `topk10`/`topk15` (gains came with 2–3× the input tokens), `hybrid` (recall rose
but correctness gain was within noise), `section_chunks` (no effect).

## The test

- **Held-out set:** `eval_set/heldout.jsonl`, 50 questions (h001–h050) drafted by Claude and
  reviewed by Mahesh before any run. Same mix as the development set: 18 single fact,
  12 multi-passage, 10 comparison, 10 unanswerable. One evidence span (h023) overlaps a
  development question's evidence.
- **Runs:** `baseline` and `final`, each once, on the held-out set.
- **Scoring:** unchanged: judge `claude-opus-5-5`, rubric v2, same prompts and generation model.

## Primary outcome

Correctness score on the 40 answerable held-out questions, `final` minus `baseline`, with a
paired bootstrap 95% interval.

- **Confirmed:** the interval's lower bound is above 0.
- **Not confirmed:** the interval includes 0. Reported as such.

## Secondary outcomes (reported, not used to decide)

- Comparison correctness.
- Unanswerable questions declined: should stay at or near 100%.
- Faithfulness: should stay at or above 95%.
- Input tokens per question.

## Commitments

1. No changes to `final.yaml`, the judge, the rubric, the prompts or the held-out questions after
   the held-out run.
2. Each configuration runs on the held-out set once. No re-running to get a better number.
3. Results are reported whatever they show.
4. `final` may also be run on the development set for reference; that doesn't change the design.
