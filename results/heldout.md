# Held-out confirmation

Each run changes one thing from `baseline`. Recall counts a question as retrieved
when every gold evidence span overlaps an excerpt the model was shown. Correctness: correct = 1,
partial = 0.5, otherwise 0, over the answerable questions. Δ is versus the baseline, with a
paired bootstrap 95% interval; an interval that includes 0 means the change isn't distinguishable
from noise at this sample size.

| Run | Change | Recall (shown) | Recall: comparisons | Correctness | Δ correctness (95% CI) | Comparisons | Declined (answerable) | Unanswerable declined | Faithful | Input tokens / question |
|---|---|---|---|---|---|---|---|---|---|---|
| baseline__heldout | baseline | 60% | 20% | 70% | – | 40% | 18% | 100% | 97% | 2,740 |
| final__heldout | company_aware=True, rerank_model=BAAI/bge-reranker-base | 68% | 40% | 75% | +5 pts (-5 to +16) | 40% | 18% | 100% | 90% | 2,894 |
