# Evaluation: `topk10`

Values are means with 95% bootstrap confidence intervals over questions.

## Retrieval

| Metric | Value |
|---|---|
| span_recall@1 | 32% (21–44%) · n=62 |
| question_recall@1 | 28% (15–40%) · n=40 |
| span_recall@3 | 53% (40–66%) · n=62 |
| question_recall@3 | 40% (25–55%) · n=40 |
| span_recall@10 | 69% (58–81%) · n=62 |
| question_recall@10 | 60% (45–75%) · n=40 |
| span_recall@all | 69% (58–81%) · n=62 |
| question_recall@all | 60% (45–75%) · n=40 |

| Question type | Recall (all shown) |
|---|---|
| comparison | 10% (0–30%) · n=10 |
| multi_passage | 58% (33–83%) · n=12 |
| single_fact | 89% (72–100%) · n=18 |

## Answers (judge: `claude-opus-5-5`, rubric v2)

| Metric | Value |
|---|---|
| Answerable · correctness score | 76% (64–86%) · n=40 |
| Answerable · fully correct | 68% (52–80%) · n=40 |
| Answerable · partial | 18% (8–30%) · n=40 |
| Answerable · incorrect | 0% (0–0%) · n=40 |
| Answerable · false abstention | 15% (5–28%) · n=40 |
| Answerable · faithful | 98% (92–100%) · n=40 |
| Answerable · citations accurate | 100% (100–100%) · n=40 |
| Unanswerable · abstained | 100% (100–100%) · n=10 |
| Unanswerable · answered anyway | 0% (0–0%) · n=10 |

## Declines on answerable questions

6 answerable questions were declined. Declining when the gold evidence was not
retrieved is a retrieval failure; declining when it was retrieved is a generation failure.

| Cause | Count | Questions |
|---|---|---|
| Gold evidence not retrieved | 6 | q013, q033, q034, q037, q038, q039 |
| Gold evidence was retrieved | 0 | – |

## Correctness by question type

| Type | Score |
|---|---|
| comparison | 35% (10–60%) · n=10 |
| multi_passage | 83% (71–96%) · n=12 |
| single_fact | 94% (83–100%) · n=18 |

## Is it retrieval or generation?

Correctness when all gold evidence was in the top-k excerpts, versus when some was missing.

| Retrieval outcome | Correctness |
|---|---|
| all evidence retrieved | 100% (100–100%) · n=24 |
| evidence missing | 41% (22–59%) · n=16 |

## Correctness by question author

| Author | Score |
|---|---|
| claude | 76% (64–86%) · n=40 |

Correctness score: correct = 1, partial = 0.5, incorrect or abstained = 0.
