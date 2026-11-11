"""Find an Anthropic API key without storing it in the repo, if you use one.

Preferred: no key at all. Run `ant auth login` once; the SDK then authenticates from your
login profile (~/.config/anthropic) and refreshes it automatically.

If you do use a key, lookup order:
1. ANTHROPIC_API_KEY environment variable (for CI or a one-off export)
2. macOS Keychain, service "rag-eval-harness-anthropic"

Store it once in the Keychain:
    security add-generic-password -a "$USER" -s rag-eval-harness-anthropic -w
(you'll be prompted to paste the key; it never appears in your shell history)
"""

from __future__ import annotations

import os
import platform
import subprocess

KEYCHAIN_SERVICE = "rag-eval-harness-anthropic"


def anthropic_api_key() -> str | None:
    key = os.environ.get("ANTHROPIC_API_KEY", "").strip()
    if key:
        return key
    if platform.system() == "Darwin":
        try:
            out = subprocess.run(
                ["security", "find-generic-password", "-s", KEYCHAIN_SERVICE, "-w"],
                capture_output=True,
                text=True,
                timeout=10,
            )
        except (OSError, subprocess.TimeoutExpired):
            return None
        if out.returncode == 0 and out.stdout.strip():
            return out.stdout.strip()
    return None
