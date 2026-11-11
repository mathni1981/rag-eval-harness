"""The scoring rubric. One definition shared by the LLM judge and the hand-labeling sheet,
so judge-vs-human agreement compares like with like."""

from __future__ import annotations

CORRECTNESS = ("correct", "partial", "incorrect", "abstained")
FAITHFULNESS = ("faithful", "unfaithful", "n/a")
CITATIONS = ("accurate", "inaccurate", "none", "n/a")

CORRECTNESS_SCORE = {"correct": 1.0, "partial": 0.5, "incorrect": 0.0, "abstained": 0.0}

RUBRIC = """\
CORRECTNESS (compare the answer with the gold answer and key points)
- correct: covers every key point and contradicts nothing in the gold answer.
- partial: covers some key points, or is right but missing a qualifier the key points require.
- incorrect: misses the main point, states a wrong figure or fact, or answers a different question.
- abstained: says the documents don't contain the answer, or otherwise declines to answer.
For an UNANSWERABLE question (no gold evidence): use "abstained" if the answer declines, and
"incorrect" if it gives a substantive answer anyway. An answer that declines but also offers
closely related facts from the excerpts, clearly labeled as not answering the question, still
counts as "abstained".

FAITHFULNESS (compare the answer with the numbered excerpts only, not with the gold answer)
- faithful: every factual claim is supported by the excerpts. Simple arithmetic on excerpt
  figures counts as supported.
- unfaithful: at least one factual claim is not supported by the excerpts (even if it happens
  to be true).
- n/a: the answer makes no factual claims (for example, a bare abstention).

CITATIONS
- accurate: the answer cites excerpts, and each cited excerpt supports the claim it's attached
  to; no major claim is left uncited.
- inaccurate: at least one citation points to an excerpt that doesn't support its claim, or a
  major claim is uncited.
- none: the answer makes factual claims but cites nothing.
- n/a: the answer makes no factual claims.
"""
