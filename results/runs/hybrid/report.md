# Evaluation: `hybrid`

Values are means with 95% bootstrap confidence intervals over questions.

## Retrieval

| Metric | Value |
|---|---|
| span_recall@1 | 34% (23–47%) · n=62 |
| question_recall@1 | 25% (12–40%) · n=40 |
| span_recall@3 | 56% (44–69%) · n=62 |
| question_recall@3 | 45% (30–60%) · n=40 |
| span_recall@5 | 69% (58–81%) · n=62 |
| question_recall@5 | 65% (50–80%) · n=40 |
| span_recall@all | 69% (58–81%) · n=62 |
| question_recall@all | 65% (50–80%) · n=40 |

| Question type | Recall (all shown) |
|---|---|
| comparison | 20% (0–50%) · n=10 |
| multi_passage | 83% (58–100%) · n=12 |
| single_fact | 78% (56–94%) · n=18 |

## Answers (judge: `claude-opus-5-5`, rubric v2)

| Metric | Value |
|---|---|
| Answerable · correctness score | 74% (61–85%) · n=40 |
| Answerable · fully correct | 68% (52–80%) · n=40 |
| Answerable · partial | 12% (2–22%) · n=40 |
| Answerable · incorrect | 0% (0–0%) · n=40 |
| Answerable · false abstention | 20% (8–32%) · n=40 |
| Answerable · faithful | 98% (92–100%) · n=40 |
| Answerable · citations accurate | 98% (92–100%) · n=40 |
| Unanswerable · abstained | 100% (100–100%) · n=10 |
| Unanswerable · answered anyway | 0% (0–0%) · n=10 |

## Declines on answerable questions

8 answerable questions were declined. Declining when the gold evidence was not
retrieved is a retrieval failure; declining when it was retrieved is a generation failure.

| Cause | Count | Questions |
|---|---|---|
| Gold evidence not retrieved | 8 | q002, q007, q013, q033, q035, q037, q038, q039 |
| Gold evidence was retrieved | 0 | – |

## Correctness by question type

| Type | Score |
|---|---|
| comparison | 35% (10–60%) · n=10 |
| multi_passage | 92% (79–100%) · n=12 |
| single_fact | 83% (67–100%) · n=18 |

## Is it retrieval or generation?

Correctness when all gold evidence was in the top-k excerpts, versus when some was missing.

| Retrieval outcome | Correctness |
|---|---|
| all evidence retrieved | 98% (94–100%) · n=26 |
| evidence missing | 29% (11–46%) · n=14 |

## Correctness by question author

| Author | Score |
|---|---|
| claude | 74% (61–85%) · n=40 |

Correctness score: correct = 1, partial = 0.5, incorrect or abstained = 0.
