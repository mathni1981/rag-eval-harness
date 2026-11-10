import shutil
from pathlib import Path

import data.freeze_text as ft

FIXTURE = Path(__file__).parent / "fixtures" / "sample_10k.htm"


def _prepare(tmp_path, monkeypatch):
    (tmp_path / "data" / "raw").mkdir(parents=True)
    shutil.copy(FIXTURE, tmp_path / "data" / "raw" / "TST_FY2025_10K.htm")
    monkeypatch.setattr(ft, "ROOT", tmp_path)
    monkeypatch.setattr(ft, "TEXT_DIR", tmp_path / "data" / "text")
    return {"doc_id": "TST_FY2025_10K", "raw_path": "data/raw/TST_FY2025_10K.htm"}


def test_freeze_then_rerun_is_noop(tmp_path, monkeypatch):
    entry = _prepare(tmp_path, monkeypatch)
    assert ft.freeze_one(entry, new_version=False).startswith("[ok]")
    assert entry["text_version"] == 1 and entry["sections"]
    assert ft.freeze_one(entry, new_version=False).startswith("[same]")


def test_changed_output_refuses_without_flag(tmp_path, monkeypatch):
    entry = _prepare(tmp_path, monkeypatch)
    ft.freeze_one(entry, new_version=False)
    original = entry["text_sha256"]
    entry["text_sha256"] = "different"  # simulate extraction change
    assert ft.freeze_one(entry, new_version=False).startswith("[STOP]")
    assert ft.freeze_one(entry, new_version=True).startswith("[ok]")
    assert entry["text_version"] == 2
    assert entry["text_path"].endswith("_v2.txt")
    assert (tmp_path / "data" / "text" / "TST_FY2025_10K.txt").exists()  # v1 kept
    assert entry["text_sha256"] == original


def test_redetect_sections_keeps_text(tmp_path, monkeypatch):
    entry = _prepare(tmp_path, monkeypatch)
    ft.freeze_one(entry, new_version=False)
    digest = entry["text_sha256"]
    entry["sections"] = {"1": 0}
    assert ft.redetect_one(entry).startswith("[ok]")
    assert entry["text_sha256"] == digest and "15" in entry["sections"]
