"""Guarded utilities for an approved longitudinal CIS-to-MS cohort.

These functions operate in memory and write no datasets. Every modeling
operation requires both a passing structural contract and explicit source-
level approval flags. They cannot turn interim public extracts into training
data.
"""

from __future__ import annotations

import random
from collections import defaultdict
from datetime import datetime
from typing import Any, Sequence

from validate_longitudinal_cis_contract import parse_date, validate


class ModelDataReadinessError(ValueError):
    """Raised when data do not meet the approved longitudinal model contract."""


REQUIRED_APPROVALS = (
    "source_access_approved",
    "baseline_cis_confirmed",
    "label_adjudication_approved",
    "feature_timing_reviewed",
)


def assess_model_readiness(
    patients: list[dict[str, str]],
    visits: list[dict[str, str]],
    outcomes: list[dict[str, str]],
    *,
    approvals: dict[str, bool],
) -> dict[str, Any]:
    """Combine contract validation with required source/clinical approvals."""

    contract = validate(patients, visits, outcomes)
    missing_approvals = [name for name in REQUIRED_APPROVALS if approvals.get(name) is not True]
    temporal_issues: list[dict[str, Any]] = []

    if contract["ready_for_modeling"]:
        indexes = {row["patient_id"].strip(): parse_date(row["index_date"]) for row in outcomes}
        visit_dates: dict[str, list[datetime]] = defaultdict(list)
        for row in visits:
            patient_id = row["patient_id"].strip()
            try:
                date = parse_date(row["visit_date"])
            except (TypeError, ValueError):
                continue
            if patient_id in indexes:
                if date <= indexes[patient_id]:
                    visit_dates[patient_id].append(date)
        too_short = [patient_id for patient_id in indexes if len(visit_dates[patient_id]) < 2]
        for patient_id in too_short:
            temporal_issues.append(
                {
                    "severity": "critical",
                    "check": "minimum_pre_index_history",
                    "patient_id": patient_id,
                    "message": "At least two genuine dated visits on or before index are required.",
                }
            )

    ready = contract["ready_for_modeling"] and not missing_approvals and not temporal_issues
    return {
        "ready_for_modeling": ready,
        "contract_validation": contract,
        "missing_approvals": missing_approvals,
        "temporal_issues": temporal_issues,
    }


def require_model_ready(assessment: dict[str, Any]) -> None:
    """Raise with actionable reasons unless the approved gate has passed."""

    if assessment.get("ready_for_modeling") is True:
        return
    reasons = list(assessment.get("missing_approvals", []))
    reasons.extend(issue["check"] for issue in assessment.get("temporal_issues", []))
    reasons.extend(
        issue.get("check", "contract_validation")
        for issue in assessment.get("contract_validation", {}).get("issues", [])
    )
    raise ModelDataReadinessError(
        "Model-data operation refused; cohort readiness requirements failed: "
        + (", ".join(sorted(set(reasons))) or "readiness not established")
    )


def split_patient_ids(
    assessment: dict[str, Any],
    outcomes: list[dict[str, str]],
    *,
    seed: int,
    train_fraction: float = 0.70,
    validation_fraction: float = 0.15,
) -> dict[str, list[str]]:
    """Create an in-memory patient-level split after the approval gate passes."""

    require_model_ready(assessment)
    test_fraction = 1.0 - train_fraction - validation_fraction
    if min(train_fraction, validation_fraction, test_fraction) <= 0:
        raise ValueError("Train, validation, and test fractions must all be positive.")
    if abs(train_fraction + validation_fraction + test_fraction - 1.0) > 1e-9:
        raise ValueError("Split fractions must sum to 1.")

    eligible = sorted(
        {
            row["patient_id"].strip()
            for row in outcomes
            if row["conversion_status"].strip() in {"0", "1"}
        }
    )
    shuffled = eligible[:]
    random.Random(seed).shuffle(shuffled)
    train_end = int(len(shuffled) * train_fraction)
    validation_end = train_end + int(len(shuffled) * validation_fraction)
    return {
        "train": shuffled[:train_end],
        "validation": shuffled[train_end:validation_end],
        "test": shuffled[validation_end:],
    }


def build_patient_sequences(
    assessment: dict[str, Any],
    visits: list[dict[str, str]],
    outcomes: list[dict[str, str]],
    feature_columns: Sequence[str],
) -> list[dict[str, Any]]:
    """Build genuine pre-index visit sequences in memory after approval."""

    require_model_ready(assessment)
    if not feature_columns:
        raise ValueError("At least one reviewed feature column is required.")
    missing = sorted(set(feature_columns) - (set(visits[0]) if visits else set()))
    if missing:
        raise ValueError(f"Visit feature columns are absent: {', '.join(missing)}")
    forbidden = {
        "patient_id",
        "visit_id",
        "conversion_date",
        "conversion_status",
        "final_diagnosis",
    }
    if forbidden.intersection(feature_columns):
        raise ValueError("Identifiers and outcome fields cannot be sequence features.")

    indexes = {row["patient_id"].strip(): parse_date(row["index_date"]) for row in outcomes}
    labels = {row["patient_id"].strip(): row["conversion_status"].strip() for row in outcomes}
    by_patient: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in visits:
        patient_id = row["patient_id"].strip()
        date = parse_date(row["visit_date"])
        if date <= indexes[patient_id]:
            by_patient[patient_id].append(
                {
                    "visit_date": date,
                    "features": {column: row[column] for column in feature_columns},
                }
            )

    sequences = []
    for patient_id in sorted(indexes):
        ordered = sorted(by_patient[patient_id], key=lambda row: row["visit_date"])
        sequences.append(
            {
                "patient_id": patient_id,
                "visits": ordered,
                "label": labels[patient_id],
            }
        )
    return sequences
