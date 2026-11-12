# Evaluation: `rerank`

Values are means with 95% bootstrap confidence intervals over questions.

## Retrieval

| Metric | Value |
|---|---|
| span_recall@1 | 29% (18–40%) · n=62 |
| question_recall@1 | 25% (12–40%) · n=40 |
| span_recall@3 | 58% (45–71%) · n=62 |
| question_recall@3 | 52% (38–68%) · n=40 |
| span_recall@5 | 69% (58–81%) · n=62 |
| question_recall@5 | 65% (50–80%) · n=40 |
| span_recall@all | 69% (58–81%) · n=62 |
| question_recall@all | 65% (50–80%) · n=40 |

| Question type | Recall (all shown) |
|---|---|
| comparison | 0% (0–0%) · n=10 |
| multi_passage | 75% (50–100%) · n=12 |
| single_fact | 94% (83–100%) · n=18 |

## Answers (judge: `claude-opus-5-5`, rubric v2)

| Metric | Value |
|---|---|
| Answerable · correctness score | 80% (69–90%) · n=40 |
| Answerable · fully correct | 72% (57–85%) · n=40 |
| Answerable · partial | 15% (5–28%) · n=40 |
| Answerable · incorrect | 0% (0–0%) · n=40 |
| Answerable · false abstention | 12% (2–22%) · n=40 |
| Answerable · faithful | 98% (92–100%) · n=40 |
| Answerable · citations accurate | 95% (88–100%) · n=40 |
| Unanswerable · abstained | 100% (100–100%) · n=10 |
| Unanswerable · answered anyway | 0% (0–0%) · n=10 |

## Declines on answerable questions

5 answerable questions were declined. Declining when the gold evidence was not
retrieved is a retrieval failure; declining when it was retrieved is a generation failure.

| Cause | Count | Questions |
|---|---|---|
| Gold evidence not retrieved | 5 | q013, q031, q033, q037, q038 |
| Gold evidence was retrieved | 0 | – |

## Correctness by question type

| Type | Score |
|---|---|
| comparison | 45% (20–70%) · n=10 |
| multi_passage | 88% (75–100%) · n=12 |
| single_fact | 94% (83–100%) · n=18 |

## Is it retrieval or generation?

Correctness when all gold evidence was in the top-k excerpts, versus when some was missing.

| Retrieval outcome | Correctness |
|---|---|
| all evidence retrieved | 98% (94–100%) · n=26 |
| evidence missing | 46% (25–68%) · n=14 |

## Correctness by question author

| Author | Score |
|---|---|
| claude | 80% (69–90%) · n=40 |

Correctness score: correct = 1, partial = 0.5, incorrect or abstained = 0.
