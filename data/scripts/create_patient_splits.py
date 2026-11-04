"""Create a patient-level split manifest only for an approved cohort."""

from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

from guarded_model_data import assess_model_readiness, split_patient_ids, require_model_ready
from validate_longitudinal_cis_contract import read_csv


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    for table in ("patients", "visits", "outcomes"):
        parser.add_argument(f"--{table}", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--cohort-id", required=True)
    parser.add_argument("--seed", required=True, type=int)
    parser.add_argument("--train-fraction", type=float, default=0.70)
    parser.add_argument("--validation-fraction", type=float, default=0.15)
    for approval in ("source-access-approved", "baseline-cis-confirmed", "label-adjudication-approved", "feature-timing-reviewed"):
        parser.add_argument(f"--{approval}", action="store_true")
    args = parser.parse_args()
    patients, visits, outcomes = (read_csv(args.patients), read_csv(args.visits), read_csv(args.outcomes))
    approvals = {
        "source_access_approved": args.source_access_approved,
        "baseline_cis_confirmed": args.baseline_cis_confirmed,
        "label_adjudication_approved": args.label_adjudication_approved,
        "feature_timing_reviewed": args.feature_timing_reviewed,
    }
    assessment = assess_model_readiness(patients, visits, outcomes, approvals=approvals)
    require_model_ready(assessment)
    splits = split_patient_ids(
        assessment, outcomes, seed=args.seed,
        train_fraction=args.train_fraction,
        validation_fraction=args.validation_fraction,
    )
    labels = {row["patient_id"].strip(): row["conversion_status"].strip() for row in outcomes}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=("patient_id", "cohort_id", "split", "seed", "conversion_status"))
        writer.writeheader()
        for split, patient_ids in splits.items():
            for patient_id in patient_ids:
                writer.writerow({"patient_id": patient_id, "cohort_id": args.cohort_id, "split": split, "seed": args.seed, "conversion_status": labels[patient_id]})
    return 0


if __name__ == "__main__":
    sys.exit(main())
