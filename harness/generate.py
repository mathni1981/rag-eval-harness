"""Generate an answer with Claude from retrieved excerpts."""

from __future__ import annotations

import re
import time
from dataclasses import dataclass

from harness.config import GenerationConfig
from harness.prompts import ABSTAIN_MARKERS, system_prompt, user_message
from harness.retrieve import Hit

CITATION = re.compile(r"\[(\d+)\]")


@dataclass
class Answer:
    text: str
    cited: list[int]
    abstained: bool
    input_tokens: int
    output_tokens: int
    latency_s: float
    stop_reason: str | None


def parse_citations(text: str, k: int) -> list[int]:
    return sorted({int(n) for n in CITATION.findall(text) if 1 <= int(n) <= k})


def looks_like_abstention(text: str) -> bool:
    """Cheap heuristic for the run summary only; Week 3 scores abstention properly."""
    lowered = text.lower()
    return any(marker in lowered for marker in ABSTAIN_MARKERS)


def make_client():
    import anthropic

    return anthropic.Anthropic(max_retries=4)  # reads ANTHROPIC_API_KEY from the environment


def generate(
    client, cfg: GenerationConfig, question: str, hits: list[Hit], companies: dict[str, str]
) -> Answer:
    started = time.monotonic()
    params = {
        "model": cfg.model,
        "max_tokens": cfg.max_tokens,
        "system": system_prompt(cfg.prompt),
        "messages": [{"role": "user", "content": user_message(question, hits, companies)}],
    }
    if cfg.temperature is not None:  # set to null in the config if a model rejects it
        params["temperature"] = cfg.temperature
    resp = client.messages.create(**params)
    text = "".join(block.text for block in resp.content if getattr(block, "type", "") == "text")
    return Answer(
        text=text,
        cited=parse_citations(text, len(hits)),
        abstained=looks_like_abstention(text),
        input_tokens=resp.usage.input_tokens,
        output_tokens=resp.usage.output_tokens,
        latency_s=round(time.monotonic() - started, 2),
        stop_reason=resp.stop_reason,
    )
