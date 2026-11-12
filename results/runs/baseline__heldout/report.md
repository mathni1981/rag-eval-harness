# Evaluation: `baseline__heldout`

Values are means with 95% bootstrap confidence intervals over questions.

## Retrieval

| Metric | Value |
|---|---|
| span_recall@1 | 36% (24–47%) · n=62 |
| question_recall@1 | 30% (15–45%) · n=40 |
| span_recall@3 | 55% (42–66%) · n=62 |
| question_recall@3 | 42% (28–57%) · n=40 |
| span_recall@5 | 69% (58–81%) · n=62 |
| question_recall@5 | 60% (45–75%) · n=40 |
| span_recall@all | 69% (58–81%) · n=62 |
| question_recall@all | 60% (45–75%) · n=40 |

| Question type | Recall (all shown) |
|---|---|
| comparison | 20% (0–50%) · n=10 |
| multi_passage | 75% (50–100%) · n=12 |
| single_fact | 72% (50–89%) · n=18 |

## Answers (judge: `claude-opus-5-5`, rubric v2)

| Metric | Value |
|---|---|
| Answerable · correctness score | 70% (56–82%) · n=40 |
| Answerable · fully correct | 62% (48–78%) · n=40 |
| Answerable · partial | 15% (5–28%) · n=40 |
| Answerable · incorrect | 5% (0–12%) · n=40 |
| Answerable · false abstention | 18% (8–30%) · n=40 |
| Answerable · faithful | 97% (92–100%) · n=39 |
| Answerable · citations accurate | 97% (92–100%) · n=39 |
| Unanswerable · abstained | 100% (100–100%) · n=10 |
| Unanswerable · answered anyway | 0% (0–0%) · n=10 |

## Declines on answerable questions

7 answerable questions were declined. Declining when the gold evidence was not
retrieved is a retrieval failure; declining when it was retrieved is a generation failure.

| Cause | Count | Questions |
|---|---|---|
| Gold evidence not retrieved | 7 | h014, h015, h026, h031, h032, h037, h038 |
| Gold evidence was retrieved | 0 | – |

## Correctness by question type

| Type | Score |
|---|---|
| comparison | 40% (15–65%) · n=10 |
| multi_passage | 79% (54–100%) · n=12 |
| single_fact | 81% (64–94%) · n=18 |

## Is it retrieval or generation?

Correctness when all gold evidence was in the top-k excerpts, versus when some was missing.

| Retrieval outcome | Correctness |
|---|---|
| all evidence retrieved | 100% (100–100%) · n=24 |
| evidence missing | 25% (9–41%) · n=16 |

## Correctness by question author

| Author | Score |
|---|---|
| claude | 70% (56–82%) · n=40 |

Correctness score: correct = 1, partial = 0.5, incorrect or abstained = 0.
