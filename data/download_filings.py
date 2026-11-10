"""Download the most recent 10-K for each company from SEC EDGAR.

Usage:
    python -m data.download_filings

Requires SEC_USER_AGENT in .env ("Name email@example.com"), per SEC fair-access rules.
Raw HTML goes to data/raw/ (not committed); metadata goes to data/manifest.json (committed).
"""

from __future__ import annotations

import os
import sys
import time

import requests
from dotenv import load_dotenv

from data.common import (
    MANIFEST_PATH,
    RAW_DIR,
    ROOT,
    load_manifest,
    save_manifest,
    sha256_bytes,
)

COMPANIES: dict[str, str] = {
    "MET": "insurer",
    "PFG": "insurer",
    "LNC": "insurer",
    "BLK": "asset_manager",
    "TROW": "asset_manager",
    "BEN": "asset_manager",
}

TICKER_FILE_URL = "https://www.sec.gov/files/company_tickers_exchange.json"
SUBMISSIONS_URL = "https://data.sec.gov/submissions/CIK{cik10}.json"
ARCHIVE_URL = "https://www.sec.gov/Archives/edgar/data/{cik}/{acc}/{doc}"

MAX_REQUESTS_PER_SECOND = 5
MAX_TRIES = 3


class EdgarClient:
    """Rate-limited HTTP client that always identifies itself to the SEC."""

    def __init__(self, user_agent: str, session: requests.Session | None = None):
        self.session = session or requests.Session()
        self.session.headers.update({"User-Agent": user_agent, "Accept-Encoding": "gzip, deflate"})
        self._min_interval = 1.0 / MAX_REQUESTS_PER_SECOND
        self._last = 0.0

    def get(self, url: str) -> requests.Response:
        for attempt in range(1, MAX_TRIES + 1):
            wait = self._min_interval - (time.monotonic() - self._last)
            if wait > 0:
                time.sleep(wait)
            self._last = time.monotonic()
            resp = self.session.get(url, timeout=60)
            if resp.status_code == 200:
                return resp
            if resp.status_code in (429, 500, 502, 503, 504) and attempt < MAX_TRIES:
                time.sleep(2**attempt)
                continue
            resp.raise_for_status()
        raise RuntimeError(f"Failed to fetch {url}")


def pad_cik(cik: int | str) -> str:
    return str(int(cik)).zfill(10)


def resolve_ciks(ticker_json: dict, tickers: list[str]) -> dict[str, dict]:
    """Map tickers to {cik, name} using the SEC company_tickers_exchange.json payload."""
    fields = ticker_json["fields"]
    i_cik, i_name, i_ticker = fields.index("cik"), fields.index("name"), fields.index("ticker")
    wanted = {t.upper() for t in tickers}
    found: dict[str, dict] = {}
    for row in ticker_json["data"]:
        t = str(row[i_ticker]).upper()
        if t in wanted and t not in found:
            found[t] = {"cik": int(row[i_cik]), "name": row[i_name]}
    missing = wanted - found.keys()
    if missing:
        raise ValueError(f"Tickers not found in SEC ticker file: {sorted(missing)}")
    return found


def latest_10k(submissions: dict) -> dict:
    """Most recent filing whose form is exactly '10-K' (excludes 10-K/A)."""
    recent = submissions["filings"]["recent"]
    candidates = [
        {
            "accession": recent["accessionNumber"][i],
            "filing_date": recent["filingDate"][i],
            "period_end": recent["reportDate"][i],
            "primary_document": recent["primaryDocument"][i],
        }
        for i, form in enumerate(recent["form"])
        if form == "10-K"
    ]
    if not candidates:
        raise ValueError(f"No 10-K in recent filings for {submissions.get('name')}")
    return max(candidates, key=lambda c: c["filing_date"])


def archive_url(cik: int | str, accession: str, primary_document: str) -> str:
    return ARCHIVE_URL.format(cik=int(cik), acc=accession.replace("-", ""), doc=primary_document)


def make_doc_id(ticker: str, period_end: str) -> str:
    return f"{ticker.upper()}_FY{period_end[:4]}_10K"


def run(client: EdgarClient, tickers: list[str]) -> dict[str, dict]:
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    manifest = load_manifest()
    ciks = resolve_ciks(client.get(TICKER_FILE_URL).json(), tickers)

    for ticker in tickers:
        info = ciks[ticker]
        subs = client.get(SUBMISSIONS_URL.format(cik10=pad_cik(info["cik"]))).json()
        filing = latest_10k(subs)
        doc_id = make_doc_id(ticker, filing["period_end"])
        url = archive_url(info["cik"], filing["accession"], filing["primary_document"])
        raw_path = RAW_DIR / f"{doc_id}.htm"

        if raw_path.exists():
            print(f"[skip] {doc_id}: already downloaded")
            raw = raw_path.read_bytes()
        else:
            raw = client.get(url).content
            raw_path.write_bytes(raw)
            print(f"[ok]   {doc_id}: {len(raw):,} bytes")

        entry = manifest.get(doc_id, {})
        entry.update(
            {
                "doc_id": doc_id,
                "ticker": ticker,
                "company": info["name"],
                "company_type": COMPANIES.get(ticker, "unknown"),
                "cik": pad_cik(info["cik"]),
                "form": "10-K",
                "accession": filing["accession"],
                "filing_date": filing["filing_date"],
                "period_end": filing["period_end"],
                "source_url": url,
                "raw_path": str(raw_path.relative_to(ROOT)),
                "raw_sha256": sha256_bytes(raw),
            }
        )
        for key in ("text_path", "text_sha256", "text_version", "sections"):
            entry.setdefault(key, None if key != "sections" else {})
        manifest[doc_id] = entry

    save_manifest(manifest)
    print(f"Manifest: {MANIFEST_PATH.relative_to(ROOT)} ({len(manifest)} documents)")
    return manifest


def main() -> None:
    load_dotenv(ROOT / ".env")
    user_agent = os.environ.get("SEC_USER_AGENT", "").strip()
    if not user_agent or "example.com" in user_agent:
        sys.exit("Set SEC_USER_AGENT in .env to your name and personal email (see .env.example).")
    run(EdgarClient(user_agent), list(COMPANIES))


if __name__ == "__main__":
    main()
