<!-- Paste this into README.md, replacing the current "## Results" section. -->

## Results

Full write-up: [docs/findings.md](docs/findings.md).

**Retrieval was the bottleneck.** When the gold evidence reached the model, the baseline answered
correctly 20 times out of 20; when it didn't, correctness fell to 38%. Every unanswerable question
was declined in every judged configuration, and faithfulness stayed at 90–100%.

**Development-set experiments** (40 answerable questions; Δ with paired bootstrap 95% CI):

| Change | Recall | Correctness | Δ vs. baseline | Tokens / question |
|---|---|---|---|---|
| Baseline | 50% | 69% | – | 2,762 |
| Cross-encoder reranking | 65% | 80% | +11 (+0 to +22) | 2,860 |
| 10 excerpts instead of 5 | 60% | 76% | +8 (−1 to +18) | 5,508 |
| Hybrid (embeddings + BM25) | 65% | 74% | +5 (−5 to +15) | 2,707 |
| Company-aware retrieval | 50% | 72% | +4 (+0 to +9) | 2,864 |
| Section-aware chunking | 48% | 70% | +1 (−5 to +8) | 2,655 |

**Pre-registered held-out test** (50 new questions; design fixed and committed before the run):
reranking plus company-aware retrieval raised recall from 60% to 68% and comparison recall from
20% to 40%, but the correctness gain of +5 points (95% CI −5 to +16) was **not confirmed**. The
gain from development to held-out shrank as expected after choosing winners on one question set.

**Judge validation:** 30 blind hand labels; 87% agreement on correctness (Cohen's κ 0.80) and 100%
on correct vs. not correct.
