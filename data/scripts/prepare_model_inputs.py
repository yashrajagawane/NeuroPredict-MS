"""Build in-memory chronological sequences from approved longitudinal CSVs.

This utility does not fit imputation, scaling, encoding, or feature selection.
Those transformations require a separately reviewed training-only pipeline.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from guarded_model_data import assess_model_readiness, build_patient_sequences, require_model_ready
from validate_longitudinal_cis_contract import read_csv


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    for table in ("patients", "visits", "outcomes"):
        parser.add_argument(f"--{table}", required=True, type=Path)
    parser.add_argument("--feature", action="append", required=True, dest="features")
    for approval in (
        "source-access-approved",
        "baseline-cis-confirmed",
        "label-adjudication-approved",
        "feature-timing-reviewed",
    ):
        parser.add_argument(f"--{approval}", action="store_true")
    args = parser.parse_args()
    patients, visits, outcomes = (
        read_csv(args.patients),
        read_csv(args.visits),
        read_csv(args.outcomes),
    )
    approvals = {
        "source_access_approved": args.source_access_approved,
        "baseline_cis_confirmed": args.baseline_cis_confirmed,
        "label_adjudication_approved": args.label_adjudication_approved,
        "feature_timing_reviewed": args.feature_timing_reviewed,
    }
    assessment = assess_model_readiness(patients, visits, outcomes, approvals=approvals)
    require_model_ready(assessment)
    sequences = build_patient_sequences(assessment, visits, outcomes, args.features)
    print(
        json.dumps(
            {
                "patient_sequences": len(sequences),
                "feature_columns": args.features,
                "sequences_written": False,
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
