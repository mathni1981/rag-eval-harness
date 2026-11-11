# Week 3: Evaluation

## Workflow

1. **Retrieval metrics (free):** `python -m harness.evaluate --run baseline --no-judge`
2. **Judge a few, check cost and sanity:** `python -m harness.evaluate --run baseline --limit 3`
   Read `results/runs/baseline/judgments.jsonl`: do the verdicts and reasoning make sense?
3. **Judge the rest:** `python -m harness.evaluate --run baseline` (resumes; nothing is judged twice)
4. **Make your labeling sheet:** `python -m tools.make_label_sheet --run baseline`
5. **Label 30 questions blind:** read `eval_set/hand_labels/baseline_packet.md`, fill in
   `eval_set/hand_labels/baseline_labels.csv`. Don't open `judgments.jsonl` while labeling.
6. **Measure judge agreement:** `python -m tools.judge_agreement --run baseline`

## Design choices

- **One rubric** (`harness/rubric.py`) is used by both the judge and the labeling packet, so
  agreement compares like with like.
- **Judge model defaults to a stronger model than the generator** (`claude-opus-5-5` judging
  `claude-sonnet-5-5`) to reduce the chance the judge shares the generator's blind spots. Both
  are Claude models, so some shared bias remains; hand labels are the check on that.
- **Faithfulness is judged against the excerpts the system saw**, rebuilt exactly from stored
  offsets; correctness is judged against the gold answer and key points.
- **Correctness by retrieval outcome** separates errors caused by missing evidence from errors
  the model made with the evidence in hand.
- **Bootstrap confidence intervals** (2,000 resamples, fixed seed) on every metric: with 40
  answerable questions, differences of a few points are often noise.
- **Blind labeling:** the packet never shows judge verdicts; the sample is stratified by type
  with a fixed seed.

## Lines to add to README.md

Under "Running the pipeline", add:

```bash
python -m harness.evaluate --run baseline            # score the run → results/runs/baseline/report.md
python -m tools.make_label_sheet --run baseline      # hand-labeling packet + sheet
python -m tools.judge_agreement --run baseline       # judge vs hand labels
```

## Lines to add to CLAUDE.md (repository layout, under harness/)

```
  rubric.py               the grading rubric shared by judge and hand labels
  excerpts.py             rebuilds the exact excerpts a run showed the model
  judge.py                LLM judge (JSON verdicts, validated)
  evaluate.py             retrieval + answer metrics with bootstrap CIs → report.md
```

and under tools/:

```
  make_label_sheet.py     blind hand-labeling packet and CSV (never overwrites labels)
  judge_agreement.py      judge vs hand labels: agreement and Cohen's kappa
```

Also add this hard rule: **Never fill in or edit `eval_set/hand_labels/*_labels.csv`.** Those
labels are Mahesh's independent ground truth for checking the judge.
