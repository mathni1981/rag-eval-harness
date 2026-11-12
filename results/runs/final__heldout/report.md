# Evaluation: `final__heldout`

Values are means with 95% bootstrap confidence intervals over questions.

## Retrieval

| Metric | Value |
|---|---|
| span_recall@1 | 45% (34–58%) · n=62 |
| question_recall@1 | 40% (25–55%) · n=40 |
| span_recall@3 | 69% (58–81%) · n=62 |
| question_recall@3 | 65% (50–80%) · n=40 |
| span_recall@5 | 73% (61–84%) · n=62 |
| question_recall@5 | 65% (50–80%) · n=40 |
| span_recall@all | 74% (63–84%) · n=62 |
| question_recall@all | 68% (52–82%) · n=40 |

| Question type | Recall (all shown) |
|---|---|
| comparison | 40% (10–70%) · n=10 |
| multi_passage | 67% (42–92%) · n=12 |
| single_fact | 83% (67–100%) · n=18 |

## Answers (judge: `claude-opus-5-5`, rubric v2)

| Metric | Value |
|---|---|
| Answerable · correctness score | 75% (62–86%) · n=40 |
| Answerable · fully correct | 68% (52–82%) · n=40 |
| Answerable · partial | 15% (5–28%) · n=40 |
| Answerable · incorrect | 0% (0–0%) · n=40 |
| Answerable · false abstention | 18% (8–30%) · n=40 |
| Answerable · faithful | 90% (80–98%) · n=40 |
| Answerable · citations accurate | 95% (88–100%) · n=40 |
| Unanswerable · abstained | 100% (100–100%) · n=10 |
| Unanswerable · answered anyway | 0% (0–0%) · n=10 |

## Declines on answerable questions

7 answerable questions were declined. Declining when the gold evidence was not
retrieved is a retrieval failure; declining when it was retrieved is a generation failure.

| Cause | Count | Questions |
|---|---|---|
| Gold evidence not retrieved | 7 | h014, h015, h032, h037, h038, h039, h040 |
| Gold evidence was retrieved | 0 | – |

## Correctness by question type

| Type | Score |
|---|---|
| comparison | 40% (15–70%) · n=10 |
| multi_passage | 83% (71–96%) · n=12 |
| single_fact | 89% (72–100%) · n=18 |

## Is it retrieval or generation?

Correctness when all gold evidence was in the top-k excerpts, versus when some was missing.

| Retrieval outcome | Correctness |
|---|---|
| all evidence retrieved | 96% (91–100%) · n=27 |
| evidence missing | 31% (12–50%) · n=13 |

## Correctness by question author

| Author | Score |
|---|---|
| claude | 75% (62–86%) · n=40 |

Correctness score: correct = 1, partial = 0.5, incorrect or abstained = 0.
