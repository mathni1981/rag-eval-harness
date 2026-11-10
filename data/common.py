"""Shared paths, manifest I/O and text normalization."""

from __future__ import annotations

import hashlib
import json
import re
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
RAW_DIR = DATA_DIR / "raw"
TEXT_DIR = DATA_DIR / "text"
MANIFEST_PATH = DATA_DIR / "manifest.json"


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def load_manifest(path: Path = MANIFEST_PATH) -> dict[str, dict]:
    """Manifest is a dict keyed by doc_id."""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def save_manifest(manifest: dict[str, dict], path: Path = MANIFEST_PATH) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    ordered = {k: manifest[k] for k in sorted(manifest)}
    path.write_text(json.dumps(ordered, indent=2) + "\n", encoding="utf-8")


_SPACES = re.compile(r"[ \t\f\v]+")
_MANY_NEWLINES = re.compile(r"\n{3,}")


def normalize_text(text: str) -> str:
    """Normalization applied to frozen filings. Changing this invalidates offsets."""
    text = unicodedata.normalize("NFKC", text)
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = text.replace("\u200b", "")  # zero-width space
    lines = [_SPACES.sub(" ", line).strip() for line in text.split("\n")]
    text = "\n".join(lines)
    text = _MANY_NEWLINES.sub("\n\n", text)
    return text.strip() + "\n"


def normalize_quote(quote: str) -> str:
    """Normalization for user-supplied quotes before searching."""
    quote = unicodedata.normalize("NFKC", quote).replace("\u200b", "")
    return " ".join(quote.split())
