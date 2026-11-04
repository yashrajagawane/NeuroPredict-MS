"""Validate approved longitudinal patients, visits, and outcomes CSV files."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from guarded_model_data import assess_model_readiness
from validate_longitudinal_cis_contract import read_csv


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--patients", required=True, type=Path)
    parser.add_argument("--visits", required=True, type=Path)
    parser.add_argument("--outcomes", required=True, type=Path)
    parser.add_argument("--source-access-approved", action="store_true")
    parser.add_argument("--baseline-cis-confirmed", action="store_true")
    parser.add_argument("--label-adjudication-approved", action="store_true")
    parser.add_argument("--feature-timing-reviewed", action="store_true")
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()
    approvals = {
        "source_access_approved": args.source_access_approved,
        "baseline_cis_confirmed": args.baseline_cis_confirmed,
        "label_adjudication_approved": args.label_adjudication_approved,
        "feature_timing_reviewed": args.feature_timing_reviewed,
    }
    result = assess_model_readiness(
        read_csv(args.patients),
        read_csv(args.visits),
        read_csv(args.outcomes),
        approvals=approvals,
    )
    rendered = json.dumps(result, indent=2)
    print(rendered)
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(rendered + "\n", encoding="utf-8")
    return 0 if result["ready_for_modeling"] else 2


if __name__ == "__main__":
    sys.exit(main())
