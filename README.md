# RAG Eval Harness for Financial Documents

**How do you know a retrieval-augmented answer is right?** This project builds a small, honest evaluation harness for question answering over public financial filings, and uses it to measure which design choices actually matter.

## Why this project

Most RAG demos show a few good answers. In financial services, the questions that matter are different: how often is an answer unsupported by its source? Does the system say "I don't know" when the document doesn't contain the answer? Can a reviewer trace every claim to a passage? This harness measures those things directly.

## Corpus

Annual reports (Form 10-K) from public insurers and asset managers, downloaded from SEC EDGAR. Public, long, dense, and realistic for FS use.

## Eval set

About 150 questions I wrote, in four types:

| Type | Example | Tests |
|---|---|---|
| Single fact | What was total revenue in the most recent fiscal year? | Basic retrieval |
| Multi-passage | How does the company describe its interest-rate risk and its hedging? | Combining sources |
| Comparison | Which of the two companies reported higher statutory capital? | Cross-document reasoning |
| Unanswerable | What is the CEO's 2030 compensation target? | Saying "not in the documents" |

Each question has a gold answer and the gold passages that support it. A 30-question subset is hand-labeled to calibrate the automated judge.

## Metrics

| Metric | Question it answers |
|---|---|
| Retrieval recall@k | Did the right passage get retrieved? |
| Faithfulness | Is every claim in the answer supported by the retrieved text? |
| Answer correctness | Does the answer match the gold answer? |
| Citation accuracy | Do cited passages support the claims they're attached to? |
| Abstention | On unanswerable questions, does the system decline? |
| Judge agreement | How often does the LLM judge agree with my hand labels? |

Every result is reported with a bootstrap confidence interval: with 150 questions, small differences are often noise.

## Experiments

Each changes one thing against a fixed baseline:

1. Chunking: fixed-size vs. section-aware (10-Ks have strong section structure)
2. Retrieval depth: top-k of 3, 5 and 10
3. Reranking: with and without
4. Prompting: plain answer vs. required citations vs. explicit permission to abstain
5. Judge reliability: where the LLM judge disagrees with hand labels

## Results

(Results table, judge-agreement numbers, and failure examples go here.)

## Repository structure

    data/download_filings.py     pulls 10-Ks from EDGAR (raw filings not committed)
    eval_set/questions.jsonl     questions, types, gold answers, gold passage IDs
    eval_set/hand_labels.jsonl   30-question calibration subset
    harness/                     ingest, retrieve, generate, judge, metrics
    experiments/configs/         one YAML per experiment
    results/report.md            findings and failure examples

## Limitations

The eval set is small and written by one person, so it reflects my blind spots. LLM judges make their own errors; the calibration subset measures that rather than assuming it away. Results on 10-Ks may not transfer to other document types.

## Author

Mahesh Nidhruva · [Portfolio](PORTFOLIO_LINK) · [LinkedIn](https://www.linkedin.com/in/mahesh-nidhruva)
