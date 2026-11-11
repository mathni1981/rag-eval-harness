"""Prompt variants for answer generation. Week 4 compares them."""

from __future__ import annotations

from harness.retrieve import Hit

BASE = (
    "You answer questions about companies' annual reports (SEC Form 10-K filings). "
    "Use only the numbered excerpts provided. Do not use outside knowledge. "
    "Each excerpt notes which company's filing and which Item it comes from; keep companies "
    "and reporting periods straight."
)

CITE = (
    " Support every factual claim with the number of the excerpt it comes from, in square "
    "brackets, like [2]. Cite only excerpts that actually support the claim."
)

ABSTAIN = (
    " If the excerpts do not contain the information needed to answer, say clearly that the "
    "documents provided do not contain it, and do not guess."
)

PROMPTS = {
    "plain": BASE,
    "cited": BASE + CITE,
    "cited_abstain": BASE + CITE + ABSTAIN,
}

ABSTAIN_MARKERS = (
    "do not contain",
    "does not contain",
    "doesn't contain",
    "don't contain",
    "not provided in",
    "no information",
    "not disclosed",
    "not mentioned",
    "cannot be determined",
    "can't be determined",
    "not specified",
)


def system_prompt(name: str) -> str:
    if name not in PROMPTS:
        raise ValueError(f"Unknown prompt '{name}'. Options: {sorted(PROMPTS)}")
    return PROMPTS[name]


def format_context(hits: list[Hit], companies: dict[str, str]) -> str:
    parts = []
    for h in hits:
        c = h.chunk
        company = companies.get(c.doc, c.doc)
        header = f"[{h.rank}] {company} ({c.doc}), Item {c.section or 'front matter'}"
        parts.append(f"{header}\n{c.text.strip()}")
    return "\n\n---\n\n".join(parts)


def user_message(question: str, hits: list[Hit], companies: dict[str, str]) -> str:
    return f"Excerpts:\n\n{format_context(hits, companies)}\n\nQuestion: {question}"
