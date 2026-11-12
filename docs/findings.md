# Findings: evaluating RAG over SEC 10-K filings

Mahesh Nidhruva · November 2026

## Summary

I built a retrieval-augmented question-answering system over six 10-K filings from insurers and
asset managers, and an evaluation harness to measure it honestly: hand-validated LLM judging,
bootstrap confidence intervals, and a pre-registered test on held-out questions.

1. **Retrieval was the bottleneck, not generation.** When the gold evidence reached the model,
   the baseline answered correctly every time (20 of 20). When it didn't, correctness fell to 38%.
   All 7 declined answers on answerable questions traced to evidence that was never retrieved.
2. **Generation was safe throughout.** Every unanswerable question was declined in every judged
   configuration on both question sets (10 of 10 each time), and faithfulness stayed between 90%
   and 100%.
3. **Better retrieval beat more retrieval.** Cross-encoder reranking matched the recall of showing
   three times as many excerpts, at no extra token cost, and gave the largest development-set gain
   in correctness (+11 points).
4. **On held-out questions, the retrieval gains held but the answer gain was not confirmed.** The
   pre-registered final design raised recall from 60% to 68% and doubled comparison recall
   (20% → 40%), but its +5 point correctness gain has a 95% interval of −5 to +16.
5. **The remaining failures have concrete causes:** a judge rubric ambiguity on one-sided
   comparisons, and table headers (units, years) separated from table rows by chunking.

## Setup

**Corpus.** The latest 10-K of MetLife, Principal Financial Group, Lincoln National, BlackRock,
T. Rowe Price and Franklin Templeton, from SEC EDGAR. Each filing was converted once to
normalized text and frozen with a SHA-256 hash; every evidence span and chunk is a character
range in those frozen files. Franklin's fiscal year ends September 30, so its filing covers a
different period from the others (calendar 2025).

**Questions.** Two sets of 50, each with the same mix: 18 single-fact, 12 multi-passage,
10 cross-company comparisons, 10 unanswerable near-misses. Each answerable question has a gold
answer, key points, and gold evidence stored as exact quoted spans with offsets.
- *Development set (q001–q050):* used to design and tune the system.
- *Held-out set (h001–h050):* drawn mostly from parts of the filings the development set barely
  used (risk factors, market risk, equity and properties sections), and used once, to test the
  final design.

Both sets were drafted by Claude and reviewed by me. Each unanswerable question was checked
against the full corpus; one planned unanswerable question turned out to be answerable and was
converted.

**Baseline system.** Fixed 1,500-character chunks with 200 overlap, each prefixed (for retrieval
only) with company name, fiscal year and 10-K Item, because filings say "we" rather than the
company's name. Local embeddings (`BAAI/bge-small-en-v1.5`), top 5 excerpts, and Claude
(`claude-sonnet-5-5`) answering only from numbered excerpts with citations.

## How answers were scored

**Retrieval recall.** A question counts as retrieved when every gold evidence span overlaps an
excerpt the model was shown.

**LLM judge.** `claude-opus-5-5` grades each answer on correctness (against the gold answer and
key points), faithfulness (against the excerpts the system actually saw, rebuilt from stored
offsets) and citation accuracy. Correctness score: correct = 1, partial = 0.5, otherwise 0.

**Judge validation.** I hand-labeled 30 development answers (stratified by question type) blind
to the judge's verdicts, using the same rubric.

| Dimension | Rubric v1 | Rubric v2 |
|---|---|---|
| Correctness | 77% agreement (κ 0.68) | 87% (κ 0.80) |
| Faithfulness | 80% | 97% |
| Citations | 70% | 100% |
| Correct vs. not correct | 100% | 100% |

Every v1 disagreement concerned *how to label a failure*, not *whether* an answer failed, so v2
clarified three rules (one-sided comparisons are partial; declines are "abstained" whatever the
cause; faithfulness and citations grade any facts inside a decline). One collision remains: when
an answer gives one side of a comparison and declines the other, I graded it partial and the judge
sometimes graded it abstained. I froze rubric v2 at that point rather than tune it a third time
against the same 30 labels, which would have inflated agreement circularly.

**Statistics.** Every metric has a 95% percentile bootstrap interval (2,000 resamples, fixed
seed). Differences between runs use a paired bootstrap over the same questions.

## Baseline (development set)

| Metric | Value (95% CI) |
|---|---|
| Question recall (all evidence in top 5) | 50% (35–65%) |
| Correctness score, answerable | 69% (56–81%) |
| Fully correct / partial / incorrect / declined | 60% / 18% / 5% / 18% |
| Faithful · citations accurate | 98% · 98% |
| Unanswerable correctly declined | 100% (10 of 10) |
| Correctness: single-fact · multi-passage · comparison | 83% · 83% · 25% |

| Retrieval outcome | Correctness |
|---|---|
| All gold evidence retrieved (n = 20) | 100% |
| Some evidence missing (n = 20) | 38% (22–55%) |

When evidence was missing, the model declined (18%) far more often than it answered wrongly (5%).
For financial documents, that is the right way to fail.

## Experiments (development set)

Each experiment changed one setting from the baseline.

| Run | Change | Recall | Comparison recall | Correctness | Δ vs. baseline (95% CI) | Comparisons | Input tokens / question |
|---|---|---|---|---|---|---|---|
| baseline | – | 50% | 10% | 69% | – | 25% | 2,762 |
| rerank | Cross-encoder reranks top 30 → 5 | 65% | 0% | 80% | +11 (+0 to +22) | 45% | 2,860 |
| topk10 | 10 excerpts | 60% | 10% | 76% | +8 (−1 to +18) | 35% | 5,508 |
| hybrid | Embeddings + BM25, fused | 65% | 20% | 74% | +5 (−5 to +15) | 35% | 2,707 |
| company_aware | Search each named company separately | 50% | 10% | 72% | +4 (+0 to +9) | 40% | 2,864 |
| section_chunks | Chunks never cross an Item boundary | 48% | 0% | 70% | +1 (−5 to +8) | 30% | 2,655 |
| topk15 | 15 excerpts | 65% | 10% | [fill in] | [fill in] | [fill in] | 8,252 |

- Reranking and hybrid search reached the same recall as 15 excerpts while showing 5.
- Company-aware retrieval didn't change overall recall but raised comparison correctness from 25%
  to 40%: it ensures both companies appear in the excerpts.
- Section-aware chunking had no effect.
- With 40 answerable questions, most intervals include zero. These results set direction; they
  can't settle close calls.

## Held-out test (pre-registered)

Before running any held-out question, I fixed the final design (`experiments/configs/final.yaml`:
reranking plus company-aware retrieval), the success criterion and the analysis in
`docs/preregistration.md`, and committed them. The criterion: the 95% interval for the correctness
difference must exclude zero.

| Run | Recall | Comparison recall | Correctness | Δ (95% CI) | Comparisons | Unanswerable declined | Faithful | Input tokens / question |
|---|---|---|---|---|---|---|---|---|
| baseline | 60% | 20% | 70% | – | 40% | 100% | 97% | 2,740 |
| final | 68% | 40% | 75% | +5 (−5 to +16) | 40% | 100% | 90% | 2,894 |

**Result: not confirmed.** The answer-quality gain cannot be distinguished from zero. The baseline
itself transferred well: 69% correctness on development questions, 70% on held-out.

**Interpretation.** The retrieval improvement held up on fresh questions. The correctness gain
shrank from +11 (reranking alone, development) to +5 (final design, held-out), the expected
pattern when the best of several experiments is chosen on one question set and retested on
another. A 5-point effect at this variance would need roughly four times as many questions to
detect reliably.

## Diagnosis of the held-out run (exploratory)

Labeled exploratory: this looks at per-question differences after the pre-registered result was
fixed, and doesn't change it.

**Correctness.** 5 questions improved (all retrieval-driven), 4 got worse. Two of the four (h039,
h040) are comparisons where the answer gave one company's figure and declined the other, and the
judge graded them abstained: the rubric collision found during validation. It likely understates
comparison scores for the final design, which helps explain why comparison correctness stayed at
40% while comparison recall doubled.

**Faithfulness (97% → 90%).** Two distinct causes:
- *Model errors (3):* an answer that opened with the wrong conclusion and later corrected itself
  (h033), a misdescribed calculation method (h034), and a misread of what a sensitivity figure
  covers (h023).
- *Table headers lost in chunking (2):* the model attached the right units and years to numbers
  from table fragments whose column headers had landed in a different chunk (h027, h048). The
  figures were correct; the excerpt alone didn't support the units. Reranking may favor
  number-dense table fragments, which would explain why this appears only in the final design.

## Limitations and disclosures

- **Small samples.** 40 answerable questions per set; most differences are within noise.
- **Who wrote the questions.** All 100 were drafted by Claude and reviewed by me. Claude-drafted
  questions answered by Claude may be easier than questions real users would ask. Every question
  records its author so human-written questions can be compared later; none exist yet.
- **Judge family.** The judge (Opus) and the generator (Sonnet) are both Claude models. Hand labels
  check this, but only on 30 development answers.
- **Company-aware retrieval is a best case.** Company names are matched from the question text
  only, but every question names its companies explicitly, and the alias list was written
  knowing these questions.
- **Gold-passage recall is a lower bound.** Filings repeat facts, so the model sometimes answered
  from a passage other than the gold one; comparison correctness exceeded comparison recall in
  several runs.
- **Held-out coverage tilts toward Item 5** (stock, dividends, repurchases): 27 of 62 evidence spans.
  One held-out evidence span (h023) overlaps a development question's evidence.
- **Judge output limit raised mid-run.** During the held-out run of the final design, one verdict
  was cut off; the judge's output limit was raised from 700 to 2,000 tokens. The judge model,
  rubric and prompt were unchanged, and the baseline's held-out judgments hadn't hit the limit.
- **Erratum, h007.** The gold answer says Franklin's $838.4 million AUM sensitivity excludes
  asset-based distribution fees. The judge's reasoning on h023 shows it likely includes them
  ($838.4 million exceeds 10% of investment management fees alone). Scoring is unaffected (the
  only key point is the $838.4 million figure). Left unchanged in the file, per the
  pre-registration.
- **One run per configuration.** Generation is not perfectly deterministic; repeated runs would
  show some variation not captured here.

## What I'd do next

1. **Repeat table headers in every chunk that splits a table,** then re-measure faithfulness on
   table-heavy questions.
2. **Settle the comparison rule** in a rubric v3, validated against fresh hand labels on different
   questions.
3. **Grow the question sets,** with human-written questions, to detect 5-point effects and to
   measure whether Claude-drafted questions are easier.
4. **Test query decomposition without explicit company names** (for example, "the two largest
   insurers") to see how much of company-aware retrieval survives realistic questions.

## How it was built

Design, question review, hand labels and analysis by me. Code built with Claude Code and
reviewed by me; `CLAUDE.md` and `docs/` record the specifications. Questions were drafted by
Claude. API usage authenticated via `ant auth login`; no keys are stored in the repository.
