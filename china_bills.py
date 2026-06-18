#!/usr/bin/env python3

import argparse
import csv
import json
import re
import sys
from typing import Iterable


CHINA_WORD_RE = re.compile(r"\bchina\b", re.IGNORECASE)


def _in_target_congress(congress: object) -> bool:
    try:
        value = int(congress)
    except (TypeError, ValueError):
        return False
    return 107 <= value <= 118


def _title_mentions_china(title: object) -> bool:
    if not isinstance(title, str):
        return False
    return bool(CHINA_WORD_RE.search(title))


def filter_china_bills(bills: Iterable[dict]) -> list[dict]:
    results: list[dict] = []
    for bill in bills:
        if not _in_target_congress(bill.get("congress")):
            continue
        if not _title_mentions_china(bill.get("title")):
            continue
        congress = bill.get("congress")
        title = bill.get("title")
        results.append(
            {
                "congress": congress,
                "bill_type": bill.get("bill_type", ""),
                "bill_number": bill.get("bill_number", ""),
                "title": title,
                "label": "China",
            }
        )
    return results


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("input_json")
    args = parser.parse_args()

    with open(args.input_json, "r", encoding="utf-8") as f:
        data = json.load(f)

    if not isinstance(data, list):
        raise ValueError("Input JSON must be an array of bill objects.")

    rows = filter_china_bills(data)

    writer = csv.DictWriter(
        sys.stdout,
        fieldnames=["congress", "bill_type", "bill_number", "title", "label"],
    )
    writer.writeheader()
    writer.writerows(rows)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
