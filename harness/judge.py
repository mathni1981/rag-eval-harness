"""LLM judge: scores one answer for correctness, faithfulness and citations."""

from __future__ import annotations

import json
import re

from harness.rubric import CITATIONS, CORRECTNESS, FAITHFULNESS, RUBRIC

JUDGE_SYSTEM = (
    "You are a strict, careful grader for a question-answering system over SEC 10-K filings. "
    "Grade only against the rubric, the gold answer and the excerpts given. Do not reward "
    "fluency or length. Respond with a single JSON object and nothing else."
)

JUDGE_TEMPLATE = """\
RUBRIC
{rubric}

QUESTION TYPE: {qtype}
QUESTION: {question}

GOLD ANSWER: {gold}
KEY POINTS:
{key_points}

NUMBERED EXCERPTS THE SYSTEM SAW:
{excerpts}

SYSTEM ANSWER:
{answer}

Return JSON with exactly these fields:
{{
  "correctness": one of {correctness},
  "key_points_covered": [true/false for each key point, in order],
  "faithfulness": one of {faithfulness},
  "unsupported_claims": [short quotes of any claims not supported by the excerpts],
  "citations": one of {citations},
  "reasoning": "two or three sentences explaining the grades"
}}"""

_FENCE = re.compile(r"^```(?:json)?\s*|\s*```$", re.MULTILINE)


def build_prompt(question: dict, answer_text: str, excerpts_text: str) -> str:
    kps = "\n".join(f"{i + 1}. {k}" for i, k in enumerate(question["key_points"]))
    return JUDGE_TEMPLATE.format(
        rubric=RUBRIC,
        qtype=question["type"],
        question=question["question"],
        gold=question["gold_answer"],
        key_points=kps,
        excerpts=excerpts_text or "(none)",
        answer=answer_text,
        correctness=list(CORRECTNESS),
        faithfulness=list(FAITHFULNESS),
        citations=list(CITATIONS),
    )


def parse_judgment(text: str, n_key_points: int) -> dict:
    cleaned = _FENCE.sub("", text.strip())
    start, end = cleaned.find("{"), cleaned.rfind("}")
    if start == -1 or end == -1:
        raise ValueError("no JSON object in judge output")
    data = json.loads(cleaned[start : end + 1])
    checks = {
        "correctness": CORRECTNESS,
        "faithfulness": FAITHFULNESS,
        "citations": CITATIONS,
    }
    for field, allowed in checks.items():
        if data.get(field) not in allowed:
            raise ValueError(f"{field}={data.get(field)!r} not in {allowed}")
    kpc = data.get("key_points_covered")
    if not isinstance(kpc, list) or len(kpc) != n_key_points:
        raise ValueError(f"key_points_covered must have {n_key_points} entries")
    data["key_points_covered"] = [bool(x) for x in kpc]
    data.setdefault("unsupported_claims", [])
    data.setdefault("reasoning", "")
    return data


def judge_answer(
    client,
    model: str,
    question: dict,
    answer_text: str,
    excerpts_text: str,
    max_tokens: int = 700,
    attempts: int = 2,
) -> dict:
    prompt = build_prompt(question, answer_text, excerpts_text)
    last_error = None
    for _ in range(attempts):
        resp = client.messages.create(
            model=model,
            max_tokens=max_tokens,
            system=JUDGE_SYSTEM,
            messages=[{"role": "user", "content": prompt}],
        )
        text = "".join(b.text for b in resp.content if getattr(b, "type", "") == "text")
        try:
            out = parse_judgment(text, len(question["key_points"]))
            out["judge_model"] = model
            out["judge_input_tokens"] = resp.usage.input_tokens
            out["judge_output_tokens"] = resp.usage.output_tokens
            return out
        except (ValueError, json.JSONDecodeError) as e:
            last_error = e
    raise RuntimeError(f"Judge output unparseable for {question['id']}: {last_error}")
