from pathlib import Path

from data.common import normalize_quote, normalize_text
from data.freeze_text import detect_sections, html_to_text, section_at

FIXTURE = Path(__file__).parent / "fixtures" / "sample_10k.htm"


def text():
    return html_to_text(FIXTURE.read_bytes())


def test_removes_hidden_xbrl_and_scripts():
    t = text()
    assert "HIDDEN XBRL METADATA" not in t
    assert "var x" not in t


def test_inline_spans_do_not_split_sentences():
    assert "We are a global provider of retirement and insurance products." in text()


def test_whitespace_normalized_and_br_kept_as_newline():
    t = text()
    assert "Changes in interest rates could\nreduce our earnings." in t
    assert "\u00a0" not in t
    assert "$12.5 billion" in t


def test_tables_become_pipe_rows_and_empty_rows_dropped():
    t = text()
    assert "Segment | Revenue" in t
    assert "Retirement | $ 5.1" in t
    assert "\n | \n" not in t


def test_sections_skip_table_of_contents():
    t = text()
    sections = detect_sections(t)
    assert t[sections["1"] :].startswith("Item 1. Business")
    assert t[sections["1A"] :].startswith("Item 1A. Risk Factors")
    assert t[sections["7"] :].startswith("Item 7. Management")
    toc_pos = t.index("TABLE OF CONTENTS")
    assert all(pos > toc_pos for pos in sections.values())
    assert section_at(sections, t.index("Total revenues")) == "7"


def test_normalize_text_is_idempotent():
    t = text()
    assert normalize_text(t) == t


def test_normalize_quote():
    assert normalize_quote(" a\u00a0 b\n c ") == "a b c"


def test_items_after_9a_detected_and_10_not_read_as_1():
    t = text()
    sections = detect_sections(t)
    assert t[sections["15"] :].startswith("Item 15. Exhibits")
    assert "1" in sections and sections["1"] < sections["15"]
    assert section_at(sections, t.index("Consolidated statements of income")) == "15"
    assert section_at(sections, t.index("Controls were effective")) == "9A"


def test_financial_statements_after_last_item_get_fs_label():
    t = (
        text()
        + "\nSIGNATURES\nReport of Independent Registered Public Accounting Firm\nWe audited.\n"
    )
    sections = detect_sections(t)
    assert section_at(sections, t.index("We audited.")) == "FS"


def test_auditor_report_inside_item_8_is_not_fs():
    t = text().replace("See notes.", "Report of Independent Registered Public Accounting Firm\nX")
    assert "FS" not in detect_sections(t)
