# Evaluation: `section_chunks`

Values are means with 95% bootstrap confidence intervals over questions.

## Retrieval

| Metric | Value |
|---|---|
| span_recall@1 | 32% (21–44%) · n=62 |
| question_recall@1 | 30% (18–45%) · n=40 |
| span_recall@3 | 53% (40–66%) · n=62 |
| question_recall@3 | 40% (25–55%) · n=40 |
| span_recall@5 | 60% (47–71%) · n=62 |
| question_recall@5 | 48% (32–62%) · n=40 |
| span_recall@all | 60% (47–71%) · n=62 |
| question_recall@all | 48% (32–62%) · n=40 |

| Question type | Recall (all shown) |
|---|---|
| comparison | 0% (0–0%) · n=10 |
| multi_passage | 58% (33–83%) · n=12 |
| single_fact | 67% (44–89%) · n=18 |

## Answers (judge: `claude-opus-5-5`, rubric v2)

| Metric | Value |
|---|---|
| Answerable · correctness score | 70% (57–81%) · n=40 |
| Answerable · fully correct | 57% (42–72%) · n=40 |
| Answerable · partial | 25% (12–40%) · n=40 |
| Answerable · incorrect | 2% (0–8%) · n=40 |
| Answerable · false abstention | 15% (5–28%) · n=40 |
| Answerable · faithful | 100% (100–100%) · n=39 |
| Answerable · citations accurate | 100% (100–100%) · n=39 |
| Unanswerable · abstained | 100% (100–100%) · n=10 |
| Unanswerable · answered anyway | 0% (0–0%) · n=10 |

## Declines on answerable questions

6 answerable questions were declined. Declining when the gold evidence was not
retrieved is a retrieval failure; declining when it was retrieved is a generation failure.

| Cause | Count | Questions |
|---|---|---|
| Gold evidence not retrieved | 6 | q011, q013, q031, q037, q038, q039 |
| Gold evidence was retrieved | 0 | – |

## Correctness by question type

| Type | Score |
|---|---|
| comparison | 30% (15–45%) · n=10 |
| multi_passage | 83% (71–96%) · n=12 |
| single_fact | 83% (67–100%) · n=18 |

## Is it retrieval or generation?

Correctness when all gold evidence was in the top-k excerpts, versus when some was missing.

| Retrieval outcome | Correctness |
|---|---|
| all evidence retrieved | 100% (100–100%) · n=19 |
| evidence missing | 43% (29–57%) · n=21 |

## Correctness by question author

| Author | Score |
|---|---|
| claude | 70% (57–81%) · n=40 |

Correctness score: correct = 1, partial = 0.5, incorrect or abstained = 0.
