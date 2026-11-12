# Experiments

Each run changes one thing from `baseline`. Recall counts a question as retrieved
when every gold evidence span overlaps an excerpt the model was shown. Correctness: correct = 1,
partial = 0.5, otherwise 0, over the 40 answerable questions. Δ is versus the baseline, with a
paired bootstrap 95% interval; an interval that includes 0 means the change isn't distinguishable
from noise at this sample size.

| Run | Change | Recall (shown) | Recall: comparisons | Correctness | Δ correctness (95% CI) | Comparisons | Declined (answerable) | Unanswerable declined | Faithful | Input tokens / question |
|---|---|---|---|---|---|---|---|---|---|---|
| baseline | baseline | 50% | 10% | 69% | – | 25% | 18% | 100% | 98% | 2,762 |
| company_aware | company_aware=True | 50% | 10% | 72% | +4 pts (+0 to +9) | 40% | 15% | 100% | 100% | 2,864 |
| hybrid | method=hybrid | 65% | 20% | 74% | +5 pts (-5 to +15) | 35% | 20% | 100% | 98% | 2,707 |
| rerank | rerank_model=BAAI/bge-reranker-base | 65% | 0% | 80% | +11 pts (+0 to +22) | 45% | 12% | 100% | 98% | 2,860 |
| section_chunks | strategy=section | 48% | 0% | 70% | +1 pts (-5 to +8) | 30% | 15% | 100% | 100% | 2,655 |
| topk10 | top_k=10 | 60% | 10% | 76% | +8 pts (-1 to +18) | 35% | 15% | 100% | 98% | 5,508 |
| topk15 | top_k=15 | 65% | 10% | – | – | – | – | – | – | 8,252 |
