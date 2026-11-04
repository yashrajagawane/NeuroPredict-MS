"""Validate a future, approved CIS-to-MS longitudinal export before modeling.

The validator accepts normalized patients, visits, and outcomes CSV files.  It
does not impute, alter, merge, or synthesize clinical data.  Its purpose is to
stop a pipeline early when the required temporal linkage or outcome follow-up
cannot be demonstrated.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from collections import Counter
from datetime import UTC, datetime
from pathlib import Path
from typing import Any


PATIENT_REQUIRED = {"patient_id"}
VISIT_REQUIRED = {"patient_id", "visit_id", "visit_date"}
OUTCOME_REQUIRED = {
    "patient_id",
    "index_date",
    "prediction_horizon_months",
    "conversion_status",
    "conversion_date",
    "last_follow_up_date",
    "diagnostic_criteria_version",
    "outcome_certainty",
}
ALLOWED_STATUSES = {"0", "1", "unknown", "censored"}


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8-sig") as handle:
        return list(csv.DictReader(handle))


def parse_date(value: str) -> datetime:
    value = value.strip()
    if value.endswith("Z"):
        value = value[:-1] + "+00:00"
    parsed = datetime.fromisoformat(value)
    if parsed.tzinfo is None:
        return parsed.replace(tzinfo=UTC)
    return parsed.astimezone(UTC)


def add_missing_columns(
    issues: list[dict[str, Any]],
    table: str,
    required: set[str],
    records: list[dict[str, str]],
) -> None:
    actual = set(records[0]) if records else set()
    missing = sorted(required - actual)
    if missing:
        issues.append(
            {
                "severity": "critical",
                "table": table,
                "check": "required_columns",
                "message": f"Missing required columns: {', '.join(missing)}",
            }
        )


def validate(
    patients: list[dict[str, str]],
    visits: list[dict[str, str]],
    outcomes: list[dict[str, str]],
) -> dict[str, Any]:
    """Return a deterministic validation report for the supplied CSV records."""

    issues: list[dict[str, Any]] = []
    add_missing_columns(issues, "patients", PATIENT_REQUIRED, patients)
    add_missing_columns(issues, "visits", VISIT_REQUIRED, visits)
    add_missing_columns(issues, "outcomes", OUTCOME_REQUIRED, outcomes)
    if issues:
        return {
            "ready_for_modeling": False,
            "issues": issues,
            "summary": {
                "patients_rows": len(patients),
                "visit_rows": len(visits),
                "outcome_rows": len(outcomes),
            },
        }

    patient_ids = [row["patient_id"].strip() for row in patients]
    blank_patient_ids = sum(not patient_id for patient_id in patient_ids)
    duplicate_patient_ids = len(patient_ids) - len(set(patient_ids))
    if blank_patient_ids:
        issues.append(
            {
                "severity": "critical",
                "table": "patients",
                "check": "patient_id_not_blank",
                "count": blank_patient_ids,
                "message": "Patient IDs must be nonblank pseudonymous identifiers.",
            }
        )
    if duplicate_patient_ids:
        issues.append(
            {
                "severity": "critical",
                "table": "patients",
                "check": "patient_id_unique",
                "count": duplicate_patient_ids,
                "message": "patients.csv must contain one row per patient_id.",
            }
        )
    patient_id_set = set(patient_ids)

    visit_ids = [row["visit_id"].strip() for row in visits]
    duplicate_visits = len(visit_ids) - len(set(visit_ids))
    if not visits:
        issues.append(
            {
                "severity": "critical",
                "table": "visits",
                "check": "nonempty_visits",
                "message": "No visit rows are available for a longitudinal model.",
            }
        )
    if any(not value for value in visit_ids):
        issues.append(
            {
                "severity": "critical",
                "table": "visits",
                "check": "visit_id_not_blank",
                "message": "Each visit must have a nonblank visit_id.",
            }
        )
    if duplicate_visits:
        issues.append(
            {
                "severity": "critical",
                "table": "visits",
                "check": "visit_id_unique",
                "count": duplicate_visits,
                "message": "visit_id values must be unique.",
            }
        )
    orphan_visits = [
        row for row in visits if row["patient_id"].strip() not in patient_id_set
    ]
    if orphan_visits:
        issues.append(
            {
                "severity": "critical",
                "table": "visits",
                "check": "patient_foreign_key",
                "count": len(orphan_visits),
                "message": "Visits reference patient_id values absent from patients.csv.",
            }
        )

    visit_dates: dict[str, list[datetime]] = {}
    invalid_visit_dates = 0
    for row in visits:
        try:
            visit_date = parse_date(row["visit_date"])
        except (TypeError, ValueError):
            invalid_visit_dates += 1
            continue
        visit_dates.setdefault(row["patient_id"].strip(), []).append(visit_date)
    if invalid_visit_dates:
        issues.append(
            {
                "severity": "critical",
                "table": "visits",
                "check": "visit_date_parseable",
                "count": invalid_visit_dates,
                "message": "Visit dates must be ISO-8601 parseable.",
            }
        )
    patients_with_one_or_fewer_visits = sum(
        len(visit_dates.get(patient_id, [])) <= 1 for patient_id in patient_id_set
    )
    if patients_with_one_or_fewer_visits:
        issues.append(
            {
                "severity": "critical",
                "table": "visits",
                "check": "minimum_history",
                "count": patients_with_one_or_fewer_visits,
                "message": (
                    "Patients with one or fewer dated visits cannot supply the "
                    "required genuine multi-visit sequence."
                ),
            }
        )

    duplicate_outcome_patients = (
        len(outcomes)
        - len(set(row["patient_id"].strip() for row in outcomes))
    )
    if duplicate_outcome_patients:
        issues.append(
            {
                "severity": "critical",
                "table": "outcomes",
                "check": "one_outcome_per_patient_landmark",
                "count": duplicate_outcome_patients,
                "message": (
                    "This contract permits one outcome row per patient. "
                    "Multiple landmarks require an explicit landmark identifier "
                    "and patient-level split protection."
                ),
            }
        )
    orphan_outcomes = [
        row for row in outcomes if row["patient_id"].strip() not in patient_id_set
    ]
    if orphan_outcomes:
        issues.append(
            {
                "severity": "critical",
                "table": "outcomes",
                "check": "patient_foreign_key",
                "count": len(orphan_outcomes),
                "message": "Outcomes reference patient IDs absent from patients.csv.",
            }
        )
    outcome_patient_ids = {row["patient_id"].strip() for row in outcomes}
    patients_without_outcomes = patient_id_set - outcome_patient_ids
    if patients_without_outcomes:
        issues.append(
            {
                "severity": "critical",
                "table": "outcomes",
                "check": "patient_outcome_coverage",
                "count": len(patients_without_outcomes),
                "message": (
                    "Every patient in a model-ready cohort requires one "
                    "documented outcome row."
                ),
            }
        )

    status_counts = Counter()
    invalid_outcome_dates = 0
    insufficient_nonconversion_follow_up = 0
    invalid_conversion_windows = 0
    missing_diagnostic_criteria = 0
    missing_outcome_certainty = 0
    for row in outcomes:
        status = row["conversion_status"].strip().lower()
        status_counts[status] += 1
        if status not in ALLOWED_STATUSES:
            issues.append(
                {
                    "severity": "critical",
                    "table": "outcomes",
                    "check": "allowed_conversion_status",
                    "message": (
                        "conversion_status must be one of 0, 1, unknown, or censored."
                    ),
                }
            )
            continue
        try:
            index_date = parse_date(row["index_date"])
            last_follow_up = parse_date(row["last_follow_up_date"])
            horizon = int(row["prediction_horizon_months"])
            if horizon <= 0:
                raise ValueError("Horizon must be positive")
        except (TypeError, ValueError):
            invalid_outcome_dates += 1
            continue
        if status in {"0", "1"} and not row["diagnostic_criteria_version"].strip():
            missing_diagnostic_criteria += 1
        if status in {"0", "1"} and not row["outcome_certainty"].strip():
            missing_outcome_certainty += 1
        required_follow_up_days = horizon * 30.4375
        if status == "0" and (last_follow_up - index_date).days < required_follow_up_days:
            insufficient_nonconversion_follow_up += 1
        if status == "1":
            conversion_value = row["conversion_date"].strip()
            if not conversion_value:
                invalid_conversion_windows += 1
                continue
            try:
                conversion_date = parse_date(conversion_value)
                if conversion_date <= index_date or (
                    conversion_date - index_date
                ).days > required_follow_up_days or conversion_date > last_follow_up:
                    invalid_conversion_windows += 1
            except (TypeError, ValueError):
                invalid_conversion_windows += 1
    if invalid_outcome_dates:
        issues.append(
            {
                "severity": "critical",
                "table": "outcomes",
                "check": "outcome_dates_and_horizon",
                "count": invalid_outcome_dates,
                "message": (
                    "Index date, last follow-up date, and positive integer "
                    "prediction horizon are required for every outcome."
                ),
            }
        )
    if missing_diagnostic_criteria:
        issues.append(
            {
                "severity": "critical",
                "table": "outcomes",
                "check": "diagnostic_criteria_version",
                "count": missing_diagnostic_criteria,
                "message": (
                    "Class 0 and Class 1 outcomes require a documented "
                    "diagnostic criteria version."
                ),
            }
        )
    if missing_outcome_certainty:
        issues.append(
            {
                "severity": "critical",
                "table": "outcomes",
                "check": "outcome_certainty",
                "count": missing_outcome_certainty,
                "message": (
                    "Class 0 and Class 1 outcomes require a nonblank outcome "
                    "certainty assessment."
                ),
            }
        )
    if insufficient_nonconversion_follow_up:
        issues.append(
            {
                "severity": "critical",
                "table": "outcomes",
                "check": "nonconversion_follow_up",
                "count": insufficient_nonconversion_follow_up,
                "message": (
                    "Class 0 cannot be assigned without follow-up spanning the "
                    "full prediction horizon."
                ),
            }
        )
    if invalid_conversion_windows:
        issues.append(
            {
                "severity": "critical",
                "table": "outcomes",
                "check": "conversion_date_window",
                "count": invalid_conversion_windows,
                "message": (
                    "Class 1 requires a conversion_date after index_date and "
                    "within the declared horizon."
                ),
            }
        )

    critical = any(issue["severity"] == "critical" for issue in issues)
    return {
        "ready_for_modeling": not critical,
        "issues": issues,
        "summary": {
            "patients_rows": len(patients),
            "unique_patient_ids": len(patient_id_set),
            "visit_rows": len(visits),
            "patients_with_dated_visits": len(visit_dates),
            "outcome_rows": len(outcomes),
            "outcome_status_counts": dict(sorted(status_counts.items())),
            "unresolved_or_censored_outcomes": status_counts["unknown"]
            + status_counts["censored"],
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate a normalized CIS-to-MS longitudinal data contract."
    )
    parser.add_argument("--patients", required=True, type=Path)
    parser.add_argument("--visits", required=True, type=Path)
    parser.add_argument("--outcomes", required=True, type=Path)
    parser.add_argument("--report", required=True, type=Path)
    args = parser.parse_args()

    report = validate(
        read_csv(args.patients),
        read_csv(args.visits),
        read_csv(args.outcomes),
    )
    report["generated_at_utc"] = datetime.now(UTC).isoformat()
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report["summary"], indent=2))
    print(f"ready_for_modeling={report['ready_for_modeling']}")
    return 0 if report["ready_for_modeling"] else 2


if __name__ == "__main__":
    sys.exit(main())
