"""Tests for source-preserving interim CIS cohort preparation."""

from __future__ import annotations

import csv
import sys
import tempfile
import unittest
from collections import Counter
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT / "data" / "scripts"))

from audit_public_cis_sources import SOURCES  # noqa: E402
from guarded_model_data import (  # noqa: E402
    ModelDataReadinessError,
    assess_model_readiness,
    build_patient_sequences,
    split_patient_ids,
)
from prepare_interim_cis_datasets import run, source_records  # noqa: E402
from validate_longitudinal_cis_contract import (  # noqa: E402
    OUTCOME_REQUIRED,
    PATIENT_REQUIRED,
    VISIT_REQUIRED,
)

SOURCE_WORKBOOKS_AVAILABLE = all(
    (REPO_ROOT / source.raw_relative_path).is_file() for source in SOURCES
)


def read_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        return reader.fieldnames or [], list(reader)


class InterimDatasetPreparationTests(unittest.TestCase):
    @unittest.skipUnless(
        SOURCE_WORKBOOKS_AVAILABLE,
        "requires the local-only source workbooks, which are intentionally not committed",
    )
    def test_interim_outputs_preserve_rows_and_target_boundaries(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            output_dir = Path(temp_dir)
            report = run(REPO_ROOT, output_dir)

            mexican_headers, mexican_rows = read_csv(output_dir / "mexican_interim.csv")
            lithuanian_headers, lithuanian_rows = read_csv(output_dir / "lithuanian_interim.csv")

            self.assertEqual(len(mexican_rows), 273)
            self.assertEqual(len(set(row["source_patient_id"] for row in mexican_rows)), 272)
            self.assertIn("final_edss_source_value", mexican_headers)
            self.assertEqual(
                Counter(row["source_group_code"] for row in mexican_rows),
                {"1": 125, "2": 148},
            )
            self.assertEqual(
                {row["target_validation_status"] for row in mexican_rows},
                {"unverified_group_mapping_no_binary_label_assigned"},
            )

            self.assertEqual(len(lithuanian_rows), 138)
            self.assertEqual(
                Counter(row["final_ms_diagnosis_flag"] for row in lithuanian_rows),
                {"0": 89, "1": 49},
            )
            self.assertEqual(
                {row["target_validation_status"] for row in lithuanian_rows},
                {"documented_final_ms_vs_non_ms_grouping_not_future_conversion_label"},
            )
            self.assertFalse(report["mexican"]["target"]["validated_for_supervised_use"])
            self.assertFalse(report["lithuanian"]["target"]["validated_for_future_prediction"])
            self.assertFalse(report["combined_dataset_created"])
            self.assertFalse((output_dir / "combined_interim.csv").exists())
            self.assertEqual(report["records_excluded"], 0)

    @unittest.skipUnless(
        SOURCE_WORKBOOKS_AVAILABLE,
        "requires the local-only source workbooks, which are intentionally not committed",
    )
    def test_processed_rows_trace_to_original_source_values(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            output_dir = Path(temp_dir)
            run(REPO_ROOT, output_dir)
            _, mexican_raw = source_records(REPO_ROOT, 0)
            _, lithuanian_raw = source_records(REPO_ROOT, 1)
            _, mexican_rows = read_csv(output_dir / "mexican_interim.csv")
            _, lithuanian_rows = read_csv(output_dir / "lithuanian_interim.csv")

            for position in (0, len(mexican_raw) // 2, len(mexican_raw) - 1):
                self.assertEqual(
                    mexican_rows[position]["source_patient_id"],
                    str(mexican_raw[position]["Patient"]),
                )
                self.assertEqual(
                    mexican_rows[position]["age_years"],
                    str(mexican_raw[position]["Age (y)"]),
                )
                self.assertEqual(
                    mexican_rows[position]["source_group_code"],
                    str(mexican_raw[position]["group"]),
                )
            for position in (0, len(lithuanian_raw) // 2, len(lithuanian_raw) - 1):
                self.assertEqual(
                    lithuanian_rows[position]["source_patient_id"],
                    str(lithuanian_raw[position]["Nr"]),
                )
                self.assertEqual(
                    lithuanian_rows[position]["age_years"],
                    str(lithuanian_raw[position]["Age"]),
                )
                self.assertEqual(
                    lithuanian_rows[position]["final_ms_diagnosis_flag"],
                    str(lithuanian_raw[position]["MS"]),
                )

    @unittest.skipUnless(
        SOURCE_WORKBOOKS_AVAILABLE,
        "requires the local-only source workbooks, which are intentionally not committed",
    )
    def test_mapping_reports_expose_uncertainty_and_leakage(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            output_dir = Path(temp_dir)
            run(REPO_ROOT, output_dir)
            _, mappings = read_csv(output_dir / "source_to_processed_mapping.csv")
            by_processed = {
                (row["source_dataset"], row["processed_column"]): row for row in mappings
            }
            mexican_final_edss = by_processed[("mendeley_8wk5hjx7x2_v1", "final_edss_source_value")]
            self.assertEqual(mexican_final_edss["leakage_risk"], "high_post_outcome_leakage")
            mexican_group = by_processed[("mendeley_8wk5hjx7x2_v1", "source_group_code")]
            self.assertEqual(
                mexican_group["interim_feature_status"],
                "retained_unlabelled_target_candidate",
            )
            lithuanian_target = by_processed[("mendeley_yjfydt34rs_v1", "final_ms_diagnosis_flag")]
            self.assertEqual(
                lithuanian_target["interim_feature_status"],
                "documented_interim_grouping_not_future_target",
            )
            self.assertIn(
                "not a fixed-horizon conversion label",
                lithuanian_target["notes"],
            )

    def test_empty_longitudinal_templates_have_contract_headers(self) -> None:
        template_dir = REPO_ROOT / "data" / "templates"
        template_specs = {
            "patients_template.csv": PATIENT_REQUIRED,
            "visits_template.csv": VISIT_REQUIRED,
            "outcomes_template.csv": OUTCOME_REQUIRED,
        }
        for filename, required in template_specs.items():
            headers, rows = read_csv(template_dir / filename)
            self.assertTrue(required.issubset(headers))
            self.assertEqual(rows, [])

    @unittest.skipUnless(
        SOURCE_WORKBOOKS_AVAILABLE,
        "requires the local-only source workbooks, which are intentionally not committed",
    )
    def test_interim_cohorts_cannot_be_split_or_sequenced(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            output_dir = Path(temp_dir)
            run(REPO_ROOT, output_dir)
            _, patients = read_csv(REPO_ROOT / "data" / "templates" / "patients_template.csv")
            _, visits = read_csv(output_dir / "mexican_interim.csv")
            _, outcomes = read_csv(output_dir / "lithuanian_interim.csv")
            assessment = assess_model_readiness(
                patients,
                visits,
                outcomes,
                approvals={
                    name: True
                    for name in (
                        "source_access_approved",
                        "baseline_cis_confirmed",
                        "label_adjudication_approved",
                        "feature_timing_reviewed",
                    )
                },
            )
            self.assertFalse(assessment["ready_for_modeling"])
            with self.assertRaises(ModelDataReadinessError):
                split_patient_ids(assessment, outcomes, seed=7)
            with self.assertRaises(ModelDataReadinessError):
                build_patient_sequences(assessment, visits, outcomes, ["age_years"])

    def test_model_utilities_require_source_approvals(self) -> None:
        patients = [{"patient_id": "P-001"}]
        visits = [
            {"patient_id": "P-001", "visit_id": "V-001", "visit_date": "2020-01-01", "edss": "1"},
            {"patient_id": "P-001", "visit_id": "V-002", "visit_date": "2020-06-01", "edss": "2"},
        ]
        outcomes = [
            {
                "patient_id": "P-001",
                "index_date": "2020-06-01",
                "prediction_horizon_months": "24",
                "conversion_status": "0",
                "conversion_date": "",
                "last_follow_up_date": "2022-07-01",
                "diagnostic_criteria_version": "McDonald 2017",
                "outcome_certainty": "confirmed",
            }
        ]
        assessment = assess_model_readiness(
            patients,
            visits,
            outcomes,
            approvals={"source_access_approved": True},
        )
        self.assertFalse(assessment["ready_for_modeling"])
        with self.assertRaises(ModelDataReadinessError):
            split_patient_ids(assessment, outcomes, seed=7)

    def test_approved_sequence_excludes_post_index_visits_and_patient_ids(self) -> None:
        patients = [{"patient_id": "P-001"}]
        visits = [
            {"patient_id": "P-001", "visit_id": "V-001", "visit_date": "2020-01-01", "edss": "1"},
            {"patient_id": "P-001", "visit_id": "V-002", "visit_date": "2020-06-01", "edss": "2"},
        ]
        outcomes = [
            {
                "patient_id": "P-001",
                "index_date": "2020-06-01",
                "prediction_horizon_months": "24",
                "conversion_status": "0",
                "conversion_date": "",
                "last_follow_up_date": "2022-07-01",
                "diagnostic_criteria_version": "McDonald 2017",
                "outcome_certainty": "confirmed",
            }
        ]
        approvals = {
            name: True
            for name in (
                "source_access_approved",
                "baseline_cis_confirmed",
                "label_adjudication_approved",
                "feature_timing_reviewed",
            )
        }
        assessment = assess_model_readiness(patients, visits, outcomes, approvals=approvals)
        self.assertTrue(assessment["ready_for_modeling"])
        sequences = build_patient_sequences(assessment, visits, outcomes, ["edss"])
        self.assertEqual(len(sequences), 1)
        self.assertEqual(len(sequences[0]["visits"]), 2)
        with self.assertRaises(ValueError):
            build_patient_sequences(assessment, visits, outcomes, ["patient_id"])


if __name__ == "__main__":
    unittest.main()
