"""Tests for the non-destructive public-source audit."""

from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT / "data" / "scripts"))

from audit_public_cis_sources import SOURCES, audit_source, run  # noqa: E402
from validate_longitudinal_cis_contract import validate  # noqa: E402


class PublicSourceAuditTests(unittest.TestCase):
    @unittest.skipUnless(
        all((REPO_ROOT / source.raw_relative_path).is_file() for source in SOURCES),
        "requires the local-only source workbooks, which are intentionally not committed",
    )
    def test_official_workbooks_match_documented_hashes_and_counts(self) -> None:
        mexican = audit_source(REPO_ROOT, SOURCES[0])
        lithuanian = audit_source(REPO_ROOT, SOURCES[1])

        self.assertTrue(mexican["hash_matches_official"])
        self.assertEqual(mexican["source_row_count_with_identifier"], 273)
        self.assertEqual(mexican["identifier"]["unique_non_missing_count"], 272)
        self.assertEqual(mexican["outcome"]["raw_value_counts"], {"1": 125, "2": 148})
        self.assertFalse(mexican["has_patient_linked_repeated_visits"])

        self.assertTrue(lithuanian["hash_matches_official"])
        self.assertEqual(lithuanian["source_row_count_with_identifier"], 138)
        self.assertEqual(lithuanian["outcome"]["raw_value_counts"], {"0": 89, "1": 49})
        self.assertFalse(lithuanian["has_visit_dates"])

    @unittest.skipUnless(
        all((REPO_ROOT / source.raw_relative_path).is_file() for source in SOURCES),
        "requires the local-only source workbooks, which are intentionally not committed",
    )
    def test_audit_outputs_state_no_go_without_fabricating_tables(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            outputs = Path(temp_dir)
            run(REPO_ROOT, outputs)
            manifest = (outputs / "dataset_manifest.json").read_text(encoding="utf-8")
            self.assertIn('"dataset_readiness": "NO_GO"', manifest)
            self.assertTrue((outputs / "missingness_report.csv").is_file())
            self.assertTrue((outputs / "public_candidate_cohort_sizes.svg").is_file())


class LongitudinalContractTests(unittest.TestCase):
    def test_valid_minimal_contract_passes(self) -> None:
        patients = [{"patient_id": "P-001"}]
        visits = [
            {"patient_id": "P-001", "visit_id": "V-001", "visit_date": "2020-01-01"},
            {"patient_id": "P-001", "visit_id": "V-002", "visit_date": "2020-06-01"},
        ]
        outcomes = [
            {
                "patient_id": "P-001",
                "index_date": "2020-06-01",
                "prediction_horizon_months": "24",
                "conversion_status": "0",
                "last_follow_up_date": "2022-07-01",
                "diagnostic_criteria_version": "McDonald 2017",
                "outcome_certainty": "confirmed",
                "conversion_date": "",
            }
        ]
        report = validate(patients, visits, outcomes)
        self.assertTrue(report["ready_for_modeling"])

    def test_short_follow_up_blocks_class_zero(self) -> None:
        patients = [{"patient_id": "P-001"}]
        visits = [
            {"patient_id": "P-001", "visit_id": "V-001", "visit_date": "2020-01-01"},
            {"patient_id": "P-001", "visit_id": "V-002", "visit_date": "2020-06-01"},
        ]
        outcomes = [
            {
                "patient_id": "P-001",
                "index_date": "2020-06-01",
                "prediction_horizon_months": "24",
                "conversion_status": "0",
                "last_follow_up_date": "2021-01-01",
                "diagnostic_criteria_version": "McDonald 2017",
                "outcome_certainty": "confirmed",
                "conversion_date": "",
            }
        ]
        report = validate(patients, visits, outcomes)
        self.assertFalse(report["ready_for_modeling"])
        self.assertIn(
            "nonconversion_follow_up",
            {issue["check"] for issue in report["issues"]},
        )

    def test_one_visit_blocks_longitudinal_contract(self) -> None:
        patients = [{"patient_id": "P-001"}]
        visits = [
            {"patient_id": "P-001", "visit_id": "V-001", "visit_date": "2020-01-01"},
        ]
        outcomes = [
            {
                "patient_id": "P-001",
                "index_date": "2020-01-01",
                "prediction_horizon_months": "24",
                "conversion_status": "0",
                "last_follow_up_date": "2022-02-01",
                "diagnostic_criteria_version": "McDonald 2017",
                "outcome_certainty": "confirmed",
                "conversion_date": "",
            }
        ]
        report = validate(patients, visits, outcomes)
        self.assertFalse(report["ready_for_modeling"])
        self.assertIn(
            "minimum_history",
            {issue["check"] for issue in report["issues"]},
        )

    def test_class_one_outside_horizon_blocks_contract(self) -> None:
        patients = [{"patient_id": "P-001"}]
        visits = [
            {"patient_id": "P-001", "visit_id": "V-001", "visit_date": "2020-01-01"},
            {"patient_id": "P-001", "visit_id": "V-002", "visit_date": "2020-06-01"},
        ]
        outcomes = [
            {
                "patient_id": "P-001",
                "index_date": "2020-06-01",
                "prediction_horizon_months": "24",
                "conversion_status": "1",
                "conversion_date": "2022-08-01",
                "last_follow_up_date": "2022-08-01",
                "diagnostic_criteria_version": "McDonald 2017",
                "outcome_certainty": "confirmed",
            }
        ]
        report = validate(patients, visits, outcomes)
        self.assertFalse(report["ready_for_modeling"])
        self.assertIn(
            "conversion_date_window",
            {issue["check"] for issue in report["issues"]},
        )


if __name__ == "__main__":
    unittest.main()
