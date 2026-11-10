import pytest

from data.download_filings import archive_url, latest_10k, make_doc_id, pad_cik, resolve_ciks


def test_pad_cik():
    assert pad_cik(1099219) == "0001099219"
    assert pad_cik("38777") == "0000038777"


def test_resolve_ciks():
    payload = {
        "fields": ["cik", "name", "ticker", "exchange"],
        "data": [
            [1099219, "MetLife, Inc.", "MET", "NYSE"],
            [38777, "Franklin Resources", "BEN", "NYSE"],
        ],
    }
    out = resolve_ciks(payload, ["MET", "BEN"])
    assert out["MET"]["cik"] == 1099219
    with pytest.raises(ValueError):
        resolve_ciks(payload, ["ZZZ"])


def test_latest_10k_skips_amendments_and_other_forms():
    subs = {
        "name": "X",
        "filings": {
            "recent": {
                "form": ["10-K/A", "10-Q", "10-K", "10-K"],
                "accessionNumber": ["a4", "a3", "a2", "a1"],
                "filingDate": ["2026-04-01", "2026-05-01", "2026-02-20", "2025-02-21"],
                "reportDate": ["2025-12-31", "2026-03-31", "2025-12-31", "2024-12-31"],
                "primaryDocument": ["d4.htm", "d3.htm", "d2.htm", "d1.htm"],
            }
        },
    }
    f = latest_10k(subs)
    assert f["accession"] == "a2" and f["primary_document"] == "d2.htm"


def test_archive_url_and_doc_id():
    url = archive_url(1099219, "0001099219-26-000012", "met-20251231.htm")
    assert (
        url == "https://www.sec.gov/Archives/edgar/data/1099219/000109921926000012/met-20251231.htm"
    )
    assert make_doc_id("ben", "2025-09-30") == "BEN_FY2025_10K"
