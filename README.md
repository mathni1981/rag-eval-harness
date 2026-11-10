# RAG Eval Harness for Financial Documents

**How do you know a retrieval-augmented answer is right?** This project builds a small, honest
evaluation harness for question answering over public SEC 10-K filings, and uses it to
measure which design choices actually matter.

> Status: in progress. Week 1 done: corpus frozen, first 50 questions drafted and in review.

## Why this project

Most RAG demos show a few good answers. In financial services, the questions that matter are
different: How often is an answer unsupported by its source? Does the system say "not in the
documents" when it should? Can a reviewer trace every claim to a passage? This harness
measures those things directly.

## Corpus

The most recent annual reports (Form 10-K) of six public insurers and asset managers:
MetLife, Principal Financial Group, Lincoln National, BlackRock, T. Rowe Price and Franklin
Resources, downloaded from SEC EDGAR. Each filing is converted once to normalized text and
frozen, with a hash recorded in `data/manifest.json`, so every result is reproducible.

## Eval set

About 150 questions in four types. The first 50 were drafted with Claude and reviewed and
corrected by hand; later questions are written by hand. Each question records its `author`.

| Type | Tests |
|---|---|
| Single fact | Basic retrieval |
| Multi-passage | Combining several passages |
| Comparison | Reasoning across two companies |
| Unanswerable | Saying "not in the documents" |

Each question has a gold answer, key points a correct answer must contain, and gold evidence
stored as **exact quoted spans with character offsets** into the frozen text. Anchoring
evidence to text rather than to chunks means retrieval recall can be measured fairly under
any chunking strategy. A 30-question subset is hand-labeled to calibrate the automated judge.

## Metrics

| Metric | Question it answers |
|---|---|
| Retrieval recall@k | Did a retrieved chunk overlap the gold evidence span? |
| Faithfulness | Is every claim in the answer supported by the retrieved text? |
| Answer correctness | Does the answer contain the gold key points? |
| Citation accuracy | Do cited passages support the claims they're attached to? |
| Abstention | On unanswerable questions, does the system decline? |
| Judge agreement | How often does the LLM judge agree with hand labels? |

Every result is reported with a bootstrap confidence interval.

## Experiments

Each changes one thing against a fixed baseline:

1. Chunking: fixed-size vs. section-aware
2. Retrieval depth: top-k of 3, 5 and 10
3. Reranking: with and without
4. Prompting: plain answer vs. required citations vs. explicit permission to abstain
5. Judge reliability: where the LLM judge disagrees with hand labels

## Results

To come: results tables, judge agreement, and failure examples.

## How it was built

Design, review of the eval set, hand labels and analysis by Mahesh Nidhruva. The first 50
questions were drafted by Claude and reviewed by me. Code built with
[Claude Code](https://claude.com/claude-code) and reviewed by me. `CLAUDE.md` and
`docs/` record the specs it was built from.

## Reproduce

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env                 # set SEC_USER_AGENT
python -m data.download_filings
python -m data.freeze_text
python -m tools.validate_eval_set
pytest -q
```

## Limitations

The eval set reflects one reviewer's blind spots. Because some questions were drafted by
Claude and answered by Claude, results are also reported by question `author` to check
whether Claude-drafted questions are easier for the system. LLM judges make their
own errors; the calibration subset measures that rather than assuming it away. Results on
10-Ks may not transfer to other document types.
