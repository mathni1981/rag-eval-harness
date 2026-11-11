"""The scoring rubric. One definition shared by the LLM judge and the hand-labeling sheet,
so judge-vs-human agreement compares like with like."""

from __future__ import annotations

CORRECTNESS = ("correct", "partial", "incorrect", "abstained")
FAITHFULNESS = ("faithful", "unfaithful", "n/a")
CITATIONS = ("accurate", "inaccurate", "none", "n/a")

CORRECTNESS_SCORE = {"correct": 1.0, "partial": 0.5, "incorrect": 0.0, "abstained": 0.0}

# Bump when the rubric changes. Judgments made under an older version are set aside and redone.
RUBRIC_VERSION = "2"

RUBRIC = """\
CORRECTNESS (compare the answer with the gold answer and key points)
- correct: covers every key point and contradicts nothing in the gold answer.
- partial: covers some key points, or is right but missing a qualifier the key points require.
  A COMPARISON that gives the right facts for one side but not the other is "partial".
- incorrect: misses the main point, states a wrong figure or fact, or answers a different question.
- abstained: declines to answer the question asked, for example by saying the documents don't
  contain the answer. Use "abstained" even if the answer was in fact in the excerpts; the harness
  reports separately whether the evidence was retrieved. A decline that also offers related facts
  (for example, a figure for a different segment or period), clearly not answering the question
  asked, is still "abstained". If a related fact is presented AS the answer, grade it as
  "incorrect" instead.
For an UNANSWERABLE question (no gold evidence): "abstained" if the answer declines, and
"incorrect" if it gives a substantive answer anyway.

FAITHFULNESS (compare the answer with the numbered excerpts only, not with the gold answer)
Grade every factual claim the answer makes, including facts mentioned inside a decline.
- faithful: every factual claim is supported by the excerpts. Simple arithmetic on excerpt
  figures counts as supported.
- unfaithful: at least one factual claim is not supported by the excerpts (even if it happens
  to be true).
- n/a: the answer states no facts at all (for example, only "the documents don't contain this").
  A claim about what the excerpts do or don't contain is not a fact for this purpose.

CITATIONS (grade every factual claim, including facts mentioned inside a decline)
- accurate: the answer cites excerpts, and each cited excerpt supports the claim it's attached
  to; no major claim is left uncited.
- inaccurate: at least one citation points to an excerpt that doesn't support its claim, or a
  major claim is uncited.
- none: the answer states facts but cites nothing.
- n/a: the answer states no facts at all.
"""
