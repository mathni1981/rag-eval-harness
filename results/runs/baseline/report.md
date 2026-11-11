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

## Answers (judge: `claude-opus-5-5`)

| Metric | Value |
|---|---|
| Answerable · correctness score | 67% (0–100%) · n=3 |
| Answerable · fully correct | 67% (0–100%) · n=3 |
| Answerable · partial | 0% (0–0%) · n=3 |
| Answerable · incorrect | 33% (0–100%) · n=3 |
| Answerable · false abstention | 0% (0–0%) · n=3 |
| Answerable · faithful | 100% (100–100%) · n=3 |
| Answerable · citations accurate | 100% (100–100%) · n=3 |

## Correctness by question type

| Type | Score |
|---|---|
| single_fact | 67% (0–100%) · n=3 |

## Is it retrieval or generation?

Correctness when all gold evidence was in the top-k excerpts, versus when some was missing.

| Retrieval outcome | Correctness |
|---|---|
| all evidence retrieved | 100% (100–100%) · n=2 |
| evidence missing | 0% · n=1 |

## Correctness by question author

| Author | Score |
|---|---|
| claude | 67% (0–100%) · n=3 |

Correctness score: correct = 1, partial = 0.5, incorrect or abstained = 0.
