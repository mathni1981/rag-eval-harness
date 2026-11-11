# Evaluation: `baseline`

Values are means with 95% bootstrap confidence intervals over questions.

## Retrieval

| Metric | Value |
|---|---|
| span_recall@1 | 32% (21–44%) · n=62 |
| question_recall@1 | 28% (15–40%) · n=40 |
| span_recall@3 | 53% (40–66%) · n=62 |
| question_recall@3 | 40% (25–55%) · n=40 |
| span_recall@5 | 61% (48–73%) · n=62 |
| question_recall@5 | 50% (35–65%) · n=40 |

## Answers (judge: `claude-opus-5-5`, rubric v2)

| Metric | Value |
|---|---|
| Answerable · correctness score | 69% (56–81%) · n=40 |
| Answerable · fully correct | 60% (45–75%) · n=40 |
| Answerable · partial | 18% (8–30%) · n=40 |
| Answerable · incorrect | 5% (0–12%) · n=40 |
| Answerable · false abstention | 18% (8–30%) · n=40 |
| Answerable · faithful | 98% (92–100%) · n=40 |
| Answerable · citations accurate | 98% (92–100%) · n=40 |
| Unanswerable · abstained | 100% (100–100%) · n=10 |
| Unanswerable · answered anyway | 0% (0–0%) · n=10 |

## Declines on answerable questions

7 answerable questions were declined. Declining when the gold evidence was not
retrieved is a retrieval failure; declining when it was retrieved is a generation failure.

| Cause | Count | Questions |
|---|---|---|
| Gold evidence not retrieved | 7 | q011, q013, q033, q037, q038, q039, q040 |
| Gold evidence was retrieved | 0 | – |

## Correctness by question type

| Type | Score |
|---|---|
| comparison | 25% (5–45%) · n=10 |
| multi_passage | 83% (71–96%) · n=12 |
| single_fact | 83% (67–100%) · n=18 |

## Is it retrieval or generation?

Correctness when all gold evidence was in the top-k excerpts, versus when some was missing.

| Retrieval outcome | Correctness |
|---|---|
| all evidence retrieved | 100% (100–100%) · n=20 |
| evidence missing | 38% (22–55%) · n=20 |

## Correctness by question author

| Author | Score |
|---|---|
| claude | 69% (56–81%) · n=40 |

Correctness score: correct = 1, partial = 0.5, incorrect or abstained = 0.
