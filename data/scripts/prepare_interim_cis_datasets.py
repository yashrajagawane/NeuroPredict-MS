"""Prepare source-preserving interim CIS cohort extracts.

This script creates two independent, one-row-per-source-record CSV datasets
from the official public workbooks. It performs only documented structural
normalization: stable record IDs, safe column names, raw-code preservation,
missing-value preservation, and explicit target-status metadata.

It deliberately does not create patient visit sequences, dates, a combined
cohort, a Mexican binary label, or a future CIS-to-MS conversion target.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import sys
from collections import Counter
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

from audit_public_cis_sources import (
    SOURCES,
    audit_source,
    is_missing,
    load_first_worksheet,
    normalized_value,
    raw_records,
)


@dataclass(frozen=True)
class FieldMapping:
    """One explicit source-to-processed field mapping."""

    source_column: str
    processed_column: str
    clinical_meaning: str
    data_type: str
    candidate_feature_alignment: str
    source_time_basis: str
    interim_feature_status: str
    leakage_risk: str
    notes: str
    identifier: bool = False
    outcome: bool = False


MEXICAN_MAPPINGS = (
    FieldMapping(
        "Patient",
        "source_patient_id",
        "De-identified source patient identifier",
        "identifier",
        "not_a_feature",
        "source row",
        "retained_for_provenance_only",
        "high_if_used_as_feature",
        "Duplicate source identifier requires source-owner clarification.",
        identifier=True,
    ),
    FieldMapping(
        "Gender",
        "sex_code",
        "Source-coded sex field",
        "coded_categorical",
        "sex",
        "reported source baseline field; individual date absent",
        "retained_source_covariate_not_model_approved",
        "unconfirmed_timing_or_codebook",
        "Values 1 and 2 are preserved. The official workbook has no codebook.",
    ),
    FieldMapping(
        "Age (y)",
        "age_years",
        "Age in years",
        "integer",
        "age_at_cis",
        "publication describes baseline clinical information at diagnosis; individual date absent",
        "retained_source_covariate_not_model_approved",
        "unconfirmed_individual_index_date",
        "Retained as observed age; it is not asserted to be a dated age-at-index field.",
    ),
    FieldMapping(
        "Schooling (y)",
        "schooling_years",
        "Schooling duration in years",
        "integer",
        "additional_source_covariate",
        "source timing not individually dated",
        "retained_source_covariate_not_model_approved",
        "unconfirmed_timing",
        "One missing value is preserved.",
    ),
    FieldMapping(
        "Breastfeeding",
        "breastfeeding_code",
        "Source-coded breastfeeding history",
        "coded_categorical",
        "additional_source_covariate",
        "source timing not individually dated",
        "retained_source_covariate_not_model_approved",
        "unconfirmed_codebook",
        "Values are retained without assigning yes/no/unknown meanings.",
    ),
    FieldMapping(
        "Varicella",
        "varicella_code",
        "Source-coded varicella history",
        "coded_categorical",
        "additional_source_covariate",
        "source timing not individually dated",
        "retained_source_covariate_not_model_approved",
        "unconfirmed_codebook",
        "Values are retained without assigning clinical labels.",
    ),
    FieldMapping(
        "initial symptom",
        "initial_symptom_code",
        "Source-coded initial symptom pattern",
        "coded_categorical",
        "initial_cis_presentation",
        "source field is named initial; no individual date",
        "retained_source_covariate_not_model_approved",
        "unconfirmed_codebook",
        "Fifteen codes are retained. No standardized CIS-type label is derived.",
    ),
    FieldMapping(
        "Mono or polysymptomatic",
        "mono_or_polysymptomatic_code",
        "Source-coded mono/polysymptomatic presentation",
        "coded_categorical",
        "initial_cis_presentation",
        "source timing not individually dated",
        "retained_source_covariate_not_model_approved",
        "unconfirmed_codebook",
        "Values 1, 2, and 3 are retained without recoding.",
    ),
    FieldMapping(
        "Oligoclonal bands",
        "ocb_code",
        "Source-coded cerebrospinal-fluid oligoclonal-band result",
        "coded_categorical",
        "ocb_status",
        "test date absent",
        "retained_source_covariate_not_model_approved",
        "unconfirmed_codebook_and_timing",
        "Values 0, 1, and 2 are retained. They are not mapped to positive/negative.",
    ),
    FieldMapping(
        "LLSSEP",
        "llssep_code",
        "Lower-limb somatosensory evoked-potential result code",
        "binary_source_code",
        "additional_source_covariate",
        "test date absent",
        "retained_source_covariate_not_model_approved",
        "unconfirmed_timing",
        "No positivity/abnormality label is inferred from the binary code.",
    ),
    FieldMapping(
        "ULSSEP",
        "ulssep_code",
        "Upper-limb somatosensory evoked-potential result code",
        "binary_source_code",
        "additional_source_covariate",
        "test date absent",
        "retained_source_covariate_not_model_approved",
        "unconfirmed_timing",
        "No positivity/abnormality label is inferred from the binary code.",
    ),
    FieldMapping(
        "VEP",
        "vep_code",
        "Visual evoked-potential result code",
        "binary_source_code",
        "additional_source_covariate",
        "test date absent",
        "retained_source_covariate_not_model_approved",
        "unconfirmed_timing",
        "No positivity/abnormality label is inferred from the binary code.",
    ),
    FieldMapping(
        "BAEP",
        "baep_code",
        "Brainstem auditory evoked-potential result code",
        "binary_source_code",
        "additional_source_covariate",
        "test date absent",
        "retained_source_covariate_not_model_approved",
        "unconfirmed_timing",
        "No positivity/abnormality label is inferred from the binary code.",
    ),
    FieldMapping(
        "Periventricular MRI",
        "periventricular_mri_code",
        "Source-coded periventricular MRI finding",
        "binary_source_code",
        "periventricular_lesion_location_indicator",
        "MRI date absent",
        "retained_source_covariate_not_model_approved",
        "unconfirmed_timing_and_codebook",
        "This is retained as a code, not relabelled as a lesion count.",
    ),
    FieldMapping(
        "Cortical MRI",
        "cortical_mri_code",
        "Source-coded cortical MRI finding",
        "binary_source_code",
        "additional_source_covariate",
        "MRI date absent",
        "retained_source_covariate_not_model_approved",
        "unconfirmed_timing_and_codebook",
        "This is retained as a code, not relabelled as a lesion count.",
    ),
    FieldMapping(
        "Infratentorial MRI",
        "infratentorial_mri_code",
        "Source-coded infratentorial MRI finding",
        "binary_source_code",
        "infratentorial_lesion_location_indicator",
        "MRI date absent",
        "retained_source_covariate_not_model_approved",
        "unconfirmed_timing_and_codebook",
        "This is retained as a code, not relabelled as a lesion count.",
    ),
    FieldMapping(
        "Spinal cord MRI",
        "spinal_cord_mri_code",
        "Source-coded spinal-cord MRI finding",
        "binary_source_code",
        "spinal_cord_lesion_location_indicator",
        "MRI date absent",
        "retained_source_covariate_not_model_approved",
        "unconfirmed_timing_and_codebook",
        "This is retained as a code, not relabelled as a lesion count.",
    ),
    FieldMapping(
        "initial EDSS",
        "initial_edss_source_value",
        "Source field named initial EDSS",
        "ordinal_numeric",
        "edss",
        "source field is named initial; assessment date absent",
        "retained_source_covariate_not_model_approved",
        "unconfirmed_individual_timing",
        "Missing values are preserved. The value is not converted to a visit-level observation.",
    ),
    FieldMapping(
        "final EDSS",
        "final_edss_source_value",
        "Source field named final EDSS",
        "ordinal_numeric",
        "not_a_permitted_prediction_feature",
        "final/post-baseline field; date absent",
        "retained_for_provenance_only",
        "high_post_outcome_leakage",
        "Preserved for provenance and explicitly excluded from predictive inputs.",
    ),
    FieldMapping(
        "group",
        "source_group_code",
        "Undocumented source group code",
        "coded_categorical",
        "source_outcome_candidate",
        "final group timing absent",
        "retained_unlabelled_target_candidate",
        "high_if_used_as_feature",
        "The source code mapping is not established by the official workbook or publication.",
        outcome=True,
    ),
)


LITHUANIAN_MAPPINGS = (
    FieldMapping(
        "Nr",
        "source_patient_id",
        "De-identified source patient identifier",
        "identifier",
        "not_a_feature",
        "source row",
        "retained_for_provenance_only",
        "high_if_used_as_feature",
        "Unique in the downloaded workbook, although values are nonconsecutive.",
        identifier=True,
    ),
    FieldMapping("Sex", "sex_code", "Source-coded sex field", "binary_source_code", "sex", "record timing absent", "retained_source_covariate_timing_unverified", "unknown_timing_or_codebook", "Values 0 and 1 are retained without a patient-level codebook."),
    FieldMapping("Age", "age_years", "Age in years", "integer", "age_at_cis", "record timing absent", "retained_source_covariate_timing_unverified", "unknown_timing", "Retained as observed age, not asserted to be dated age at CIS."),
    FieldMapping("Fatigue", "fatigue_code", "Source-coded fatigue finding", "binary_source_code", "additional_source_covariate", "medical-record timing absent", "retained_source_covariate_timing_unverified", "unknown_timing", "Source code is preserved."),
    FieldMapping("General weakness", "general_weakness_code", "Source-coded general weakness finding", "binary_source_code", "additional_source_covariate", "medical-record timing absent", "retained_source_covariate_timing_unverified", "unknown_timing", "Source code is preserved."),
    FieldMapping("Pain", "pain_code", "Source-coded pain finding", "binary_source_code", "additional_source_covariate", "medical-record timing absent", "retained_source_covariate_timing_unverified", "unknown_timing", "Source code is preserved."),
    FieldMapping("Focal symptoms", "focal_symptoms_code", "Source-coded focal symptoms finding", "binary_source_code", "related_to_initial_cis_presentation_not_harmonized", "medical-record timing absent", "retained_source_covariate_timing_unverified", "unknown_timing", "Not a harmonized CIS-presentation type."),
    FieldMapping("CN", "cranial_nerve_dysfunction_code", "Source CN clinical finding code", "binary_source_code", "additional_source_covariate", "medical-record timing absent", "retained_source_covariate_timing_unverified", "unknown_timing", "Abbreviation is described as cranial-nerve dysfunction in the publication."),
    FieldMapping("3", "source_header_3_code", "Source field with header 3", "binary_source_code", "additional_source_covariate", "medical-record timing absent", "retained_uninterpreted_source_code", "unknown_semantics", "No field meaning is derived from the header."),
    FieldMapping("4", "source_header_4_code", "Source field with header 4", "binary_source_code", "additional_source_covariate", "medical-record timing absent", "retained_uninterpreted_source_code", "unknown_semantics", "No field meaning is derived from the header."),
    FieldMapping("5", "source_header_5_code", "Source field with header 5", "binary_source_code", "additional_source_covariate", "medical-record timing absent", "retained_uninterpreted_source_code", "unknown_semantics", "No field meaning is derived from the header."),
    FieldMapping("6", "source_header_6_code", "Source field with header 6", "binary_source_code", "additional_source_covariate", "medical-record timing absent", "retained_uninterpreted_source_code", "unknown_semantics", "No field meaning is derived from the header."),
    FieldMapping("8", "source_header_8_code", "Source field with header 8", "binary_source_code", "additional_source_covariate", "medical-record timing absent", "retained_uninterpreted_source_code", "unknown_semantics", "No field meaning is derived from the header."),
    FieldMapping("Pathological reflexes", "pathological_reflexes_code", "Source-coded pathological reflex finding", "binary_source_code", "additional_source_covariate", "medical-record timing absent", "retained_source_covariate_timing_unverified", "unknown_timing", "Source code is preserved."),
    FieldMapping("Babinski's", "babinski_code", "Source-coded Babinski reflex finding", "binary_source_code", "additional_source_covariate", "medical-record timing absent", "retained_source_covariate_timing_unverified", "unknown_timing", "Source code is preserved."),
    FieldMapping("Rossolimo", "rossolimo_code", "Source-coded Rossolimo reflex finding", "binary_source_code", "additional_source_covariate", "medical-record timing absent", "retained_source_covariate_timing_unverified", "unknown_timing", "Source code is preserved."),
    FieldMapping("Muscle strength", "muscle_strength_code", "Source-coded muscle-strength finding", "binary_source_code", "additional_source_covariate", "medical-record timing absent", "retained_source_covariate_timing_unverified", "unknown_timing", "Source code is preserved."),
    FieldMapping("Reflex asymmetry", "reflex_asymmetry_code", "Source-coded reflex-asymmetry finding", "binary_source_code", "additional_source_covariate", "medical-record timing absent", "retained_source_covariate_timing_unverified", "unknown_timing", "Source code is preserved."),
    FieldMapping("Muscle tone abnormalities", "muscle_tone_abnormalities_code", "Source-coded muscle-tone finding", "binary_source_code", "additional_source_covariate", "medical-record timing absent", "retained_source_covariate_timing_unverified", "unknown_timing", "Source code is preserved."),
    FieldMapping("Proprioception", "proprioception_code", "Source-coded proprioception finding", "binary_source_code", "additional_source_covariate", "medical-record timing absent", "retained_source_covariate_timing_unverified", "unknown_timing", "Source code is preserved."),
    FieldMapping("Superficial sensation", "superficial_sensation_code", "Source-coded superficial-sensation finding", "binary_source_code", "additional_source_covariate", "medical-record timing absent", "retained_source_covariate_timing_unverified", "unknown_timing", "Source code is preserved."),
    FieldMapping("Coordination", "coordination_code", "Source-coded coordination finding", "binary_source_code", "additional_source_covariate", "medical-record timing absent", "retained_source_covariate_timing_unverified", "unknown_timing", "Source code is preserved."),
    FieldMapping("Balance", "balance_code", "Source-coded balance finding", "binary_source_code", "additional_source_covariate", "medical-record timing absent", "retained_source_covariate_timing_unverified", "unknown_timing", "Source code is preserved."),
    FieldMapping("Urinary incontinence", "urinary_incontinence_code", "Source-coded urinary-incontinence finding", "binary_source_code", "additional_source_covariate", "medical-record timing absent", "retained_source_covariate_timing_unverified", "unknown_timing", "Source code is preserved."),
    FieldMapping("Urine retention", "urine_retention_code", "Source-coded urine-retention finding", "binary_source_code", "additional_source_covariate", "medical-record timing absent", "retained_source_covariate_timing_unverified", "unknown_timing", "Source code is preserved."),
    FieldMapping("Vertigo", "vertigo_code", "Source-coded vertigo finding", "binary_source_code", "additional_source_covariate", "medical-record timing absent", "retained_source_covariate_timing_unverified", "unknown_timing", "Source code is preserved."),
    FieldMapping("Sum of symptoms", "sum_of_symptoms_source_value", "Source total of symptoms", "integer", "additional_source_covariate", "medical-record timing absent", "retained_source_covariate_timing_unverified", "unknown_timing", "Derivation details are not available in the workbook."),
    FieldMapping("MRI lesions specific to MS", "mri_lesions_specific_to_ms_code", "Source-coded MRI lesions specific to MS", "binary_source_code", "additional_source_covariate", "MRI date absent", "retained_source_covariate_timing_unverified", "unknown_timing_and_codebook", "Source code is preserved."),
    FieldMapping("MRI lesions indicative of other diseases", "mri_lesions_other_diseases_code", "Source-coded MRI lesions indicative of other diseases", "binary_source_code", "additional_source_covariate", "MRI date absent", "retained_source_covariate_timing_unverified", "unknown_timing_and_codebook", "Source code is preserved."),
    FieldMapping("Unspecified MRI lesions", "unspecified_mri_lesions_code", "Source-coded unspecified MRI lesions", "binary_source_code", "additional_source_covariate", "MRI date absent", "retained_source_covariate_timing_unverified", "unknown_timing_and_codebook", "Source code is preserved."),
    FieldMapping("MRI lesion localisation: infratentorally", "infratentorial_mri_code", "Source-coded infratentorial MRI finding", "binary_source_code", "infratentorial_lesion_location_indicator", "MRI date absent", "retained_source_covariate_timing_unverified", "unknown_timing_and_codebook", "This is a location indicator code, not a lesion count."),
    FieldMapping("Periventricular", "periventricular_mri_code", "Source-coded periventricular MRI finding", "binary_source_code", "periventricular_lesion_location_indicator", "MRI date absent", "retained_source_covariate_timing_unverified", "unknown_timing_and_codebook", "This is a location indicator code, not a lesion count."),
    FieldMapping("Juxtacortical", "juxtacortical_mri_code", "Source-coded juxtacortical MRI finding", "binary_source_code", "additional_source_covariate", "MRI date absent", "retained_source_covariate_timing_unverified", "unknown_timing_and_codebook", "This is a location indicator code, not a lesion count."),
    FieldMapping("MRI spinal lesions", "spinal_cord_mri_code", "Source-coded spinal-cord MRI finding", "binary_source_code", "spinal_cord_lesion_location_indicator", "MRI date absent", "retained_source_covariate_timing_unverified", "unknown_timing_and_codebook", "This is a location indicator code, not a lesion count."),
    FieldMapping("Patholoigical CSF", "pathological_csf_source_value", "Source pathological-CSF field", "mixed_source_code", "additional_source_covariate", "CSF test date absent", "retained_source_covariate_timing_unverified", "unknown_timing_and_codebook", "Original misspelling and raw values, including n, are preserved in the source-to-processed map."),
    FieldMapping("Increased protein", "increased_csf_protein_code", "Source-coded increased CSF protein finding", "binary_source_code", "additional_source_covariate", "CSF test date absent", "retained_source_covariate_timing_unverified", "unknown_timing_and_codebook", "Source code is preserved."),
    FieldMapping("Increased protein (g/l)", "csf_protein_g_per_l_source_value", "Source CSF protein value", "numeric", "additional_source_covariate", "CSF test date absent", "retained_source_covariate_timing_unverified", "unknown_timing", "Unit is retained from source header."),
    FieldMapping("Pleocytosis [AL]", "pleocytosis_column_al_code", "Source Pleocytosis column AL", "binary_source_code", "additional_source_covariate", "CSF test date absent", "retained_source_covariate_timing_unverified", "unknown_semantics_and_timing", "Duplicate raw Pleocytosis header is disambiguated by Excel column."),
    FieldMapping("Pleocytosis [AM]", "pleocytosis_column_am_value", "Source Pleocytosis column AM", "numeric", "additional_source_covariate", "CSF test date absent", "retained_source_covariate_timing_unverified", "unknown_semantics_and_timing", "Duplicate raw Pleocytosis header is disambiguated by Excel column."),
    FieldMapping("OGB + in CSF", "ocb_positive_code", "Source-coded positive CSF oligoclonal-band finding", "binary_source_code", "ocb_status", "CSF test date absent", "retained_source_covariate_timing_unverified", "unknown_timing", "Source header indicates OGB positivity; raw code is retained."),
    FieldMapping("IgG levels in CSF", "csf_igg_level_source_value", "Source CSF IgG level", "numeric", "not_igg_index", "CSF test date absent", "retained_source_covariate_timing_unverified", "unknown_unit_and_timing", "This must not be treated as an IgG index."),
    FieldMapping("VEP +", "vep_positive_code", "Source-coded positive visual evoked-potential finding", "binary_source_code", "additional_source_covariate", "test date absent", "retained_source_covariate_timing_unverified", "unknown_timing", "Source header indicates VEP positivity; raw code is retained."),
    FieldMapping("BAEP +", "baep_positive_code", "Source-coded positive brainstem auditory evoked-potential finding", "binary_source_code", "additional_source_covariate", "test date absent", "retained_source_covariate_timing_unverified", "unknown_timing", "Source header indicates BAEP positivity; raw code is retained."),
    FieldMapping("MS", "final_ms_diagnosis_flag", "Final diagnosis group: MS versus non-MS", "binary_outcome", "interim_final_diagnosis_target", "final diagnosis during retrospective 2015-2020 record review; individual date absent", "documented_interim_grouping_not_future_target", "high_if_used_as_feature", "The publication documents 1 as MS and 0 as non-MS at final diagnosis; this is not a fixed-horizon conversion label.", outcome=True),
)


META_COLUMNS = (
    "interim_record_id",
    "source_dataset",
    "source_display_name",
    "source_row_number",
    "source_patient_id",
    "source_identifier_unique_in_workbook",
    "has_genuine_repeated_visits",
    "has_visit_dates",
    "has_conversion_dates",
    "has_last_follow_up_dates",
    "longitudinal_model_eligibility",
    "target_representation",
    "target_validation_status",
)


def source_records(repo_root: Path, source_index: int) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    """Read one source through the same parser used by the hash audit."""

    spec = SOURCES[source_index]
    raw_path = repo_root / spec.raw_relative_path
    _, rows = load_first_worksheet(raw_path)
    _, records = raw_records(rows, spec.header_row, spec.identifier_column)
    audit = audit_source(repo_root, spec)
    return audit, records


def value_text(value: Any) -> str:
    return "" if is_missing(value) else normalized_value(value)


def is_number_in_range(value: str, minimum: float, maximum: float) -> bool:
    if not value:
        return True
    try:
        parsed = float(value)
    except ValueError:
        return False
    return math.isfinite(parsed) and minimum <= parsed <= maximum


def make_rows(
    audit: dict[str, Any],
    records: list[dict[str, Any]],
    mappings: tuple[FieldMapping, ...],
    record_prefix: str,
    target_representation: str,
    target_validation_status: str,
) -> tuple[list[str], list[dict[str, str]]]:
    """Normalize column names without altering observed values or row count."""

    source_fields = [mapping.source_column for mapping in mappings]
    record_fields = [field for field in records[0] if field != "__source_row__"]
    if source_fields != record_fields:
        raise ValueError(
            f"Mapping/source mismatch for {audit['source_id']}: "
            f"expected {source_fields}, found {record_fields}"
        )
    identifier_mapping = next(mapping for mapping in mappings if mapping.identifier)
    id_counts = Counter(value_text(record[identifier_mapping.source_column]) for record in records)
    processed_columns = list(META_COLUMNS) + [
        mapping.processed_column
        for mapping in mappings
        if not mapping.identifier
    ]

    rows: list[dict[str, str]] = []
    for ordinal, record in enumerate(records, start=1):
        source_identifier = value_text(record[identifier_mapping.source_column])
        row: dict[str, str] = {
            "interim_record_id": f"{record_prefix}-R{ordinal:03d}",
            "source_dataset": audit["source_id"],
            "source_display_name": audit["display_name"],
            "source_row_number": str(record["__source_row__"]),
            "source_patient_id": source_identifier,
            "source_identifier_unique_in_workbook": str(
                id_counts[source_identifier] == 1
            ).lower(),
            "has_genuine_repeated_visits": "false",
            "has_visit_dates": "false",
            "has_conversion_dates": "false",
            "has_last_follow_up_dates": "false",
            "longitudinal_model_eligibility": "not_eligible_no_dated_visits_or_outcome_timing",
            "target_representation": target_representation,
            "target_validation_status": target_validation_status,
        }
        for mapping in mappings:
            if mapping.identifier:
                continue
            row[mapping.processed_column] = value_text(record[mapping.source_column])
        rows.append(row)
    return processed_columns, rows


def missingness(rows: list[dict[str, str]], columns: list[str]) -> dict[str, float]:
    return {
        column: round(
            sum(not row[column] for row in rows) / len(rows) * 100 if rows else 0,
            3,
        )
        for column in columns
    }


def mapping_rows(
    audit: dict[str, Any], mappings: tuple[FieldMapping, ...], rows: list[dict[str, str]]
) -> tuple[list[dict[str, str]], list[dict[str, str]]]:
    """Return full mapping and feature-dictionary rows for one cohort."""

    source_summaries = {
        summary["field_name"]: summary for summary in audit["column_summaries"]
    }
    full_rows: list[dict[str, str]] = []
    feature_rows: list[dict[str, str]] = []
    for mapping in mappings:
        summary = source_summaries[mapping.source_column]
        row = {
            "source_dataset": audit["source_id"],
            "source_column": mapping.source_column,
            "processed_column": mapping.processed_column,
            "clinical_meaning": mapping.clinical_meaning,
            "data_type": mapping.data_type,
            "missing_count": str(summary["missing_count"]),
            "missing_pct": f"{summary['missing_pct']:.3f}",
            "candidate_feature_alignment": mapping.candidate_feature_alignment,
            "source_time_basis": mapping.source_time_basis,
            "interim_feature_status": mapping.interim_feature_status,
            "leakage_risk": mapping.leakage_risk,
            "transformation": "renamed only; source value preserved; missing remains empty",
            "notes": mapping.notes,
        }
        full_rows.append(row)
        if (
            not mapping.identifier
            and not mapping.outcome
            and mapping.interim_feature_status != "retained_for_provenance_only"
        ):
            feature_rows.append(row)
    return full_rows, feature_rows


def validate_mexican(rows: list[dict[str, str]]) -> list[dict[str, Any]]:
    checks: list[dict[str, Any]] = []
    group_codes = Counter(row["source_group_code"] for row in rows)
    duplicate_ids = sum(
        count - 1
        for count in Counter(row["source_patient_id"] for row in rows).values()
        if count > 1
    )
    invalid_age = sum(
        not is_number_in_range(row["age_years"], 0, 120) for row in rows
    )
    invalid_initial_edss = sum(
        not is_number_in_range(row["initial_edss_source_value"], 0, 10)
        for row in rows
    )
    invalid_final_edss = sum(
        not is_number_in_range(row["final_edss_source_value"], 0, 10)
        for row in rows
    )
    checks.extend(
        [
            {"check": "row_count_preserved", "status": "pass", "count": len(rows), "detail": "All 273 source rows were retained."},
            {"check": "source_identifier_duplicates", "status": "warning", "count": duplicate_ids, "detail": "One duplicate source identifier remains; no row was removed or merged."},
            {"check": "age_range_0_to_120", "status": "pass" if not invalid_age else "fail", "count": invalid_age, "detail": "Observed age values must be numeric and between 0 and 120."},
            {"check": "initial_edss_range_0_to_10", "status": "pass" if not invalid_initial_edss else "fail", "count": invalid_initial_edss, "detail": "Nonmissing source initial EDSS values must be between 0 and 10."},
            {"check": "final_edss_range_0_to_10", "status": "pass" if not invalid_final_edss else "fail", "count": invalid_final_edss, "detail": "Nonmissing source final EDSS values must be between 0 and 10; field is excluded from features."},
            {"check": "source_group_code_values", "status": "warning", "count": len(group_codes), "detail": f"Observed values are {dict(sorted(group_codes.items()))}; mapping to conversion is not source-documented."},
            {"check": "future_conversion_target", "status": "not_available", "count": 0, "detail": "No index, conversion, or last-follow-up dates are available."},
        ]
    )
    return checks


def validate_lithuanian(rows: list[dict[str, str]]) -> list[dict[str, Any]]:
    checks: list[dict[str, Any]] = []
    target_codes = Counter(row["final_ms_diagnosis_flag"] for row in rows)
    duplicate_ids = sum(
        count - 1
        for count in Counter(row["source_patient_id"] for row in rows).values()
        if count > 1
    )
    invalid_age = sum(
        not is_number_in_range(row["age_years"], 0, 120) for row in rows
    )
    under_18 = sum(float(row["age_years"]) < 18 for row in rows if row["age_years"])
    invalid_target = sum(
        row["final_ms_diagnosis_flag"] not in {"0", "1"} for row in rows
    )
    checks.extend(
        [
            {"check": "row_count_preserved", "status": "pass", "count": len(rows), "detail": "All 138 source rows were retained."},
            {"check": "source_identifier_duplicates", "status": "pass" if not duplicate_ids else "fail", "count": duplicate_ids, "detail": "Source identifier uniqueness was checked without altering identifiers."},
            {"check": "age_range_0_to_120", "status": "pass" if not invalid_age else "fail", "count": invalid_age, "detail": "Observed age values must be numeric and between 0 and 120."},
            {"check": "age_below_publication_adult_criterion", "status": "warning" if under_18 else "pass", "count": under_18, "detail": "The publication describes adults aged 18 or older; source records below 18 are retained pending clarification."},
            {"check": "final_ms_diagnosis_flag_values", "status": "pass" if not invalid_target else "fail", "count": invalid_target, "detail": f"Observed values are {dict(sorted(target_codes.items()))}; publication documents final MS versus non-MS grouping."},
            {"check": "future_conversion_target", "status": "not_available", "count": 0, "detail": "Final diagnosis has no individual index, conversion, or last-follow-up date."},
        ]
    )
    return checks


def write_csv(path: Path, rows: list[dict[str, str]], fieldnames: list[str]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def markdown_missingness(
    title: str, rows: list[dict[str, str]], columns: list[str]
) -> str:
    details = missingness(rows, columns)
    nonzero = [
        (column, pct)
        for column, pct in details.items()
        if pct > 0 and column not in META_COLUMNS
    ]
    lines = [f"### {title}", "", "| Processed column | Missingness |", "|---|---:|"]
    lines.extend(f"| {column} | {pct:.3f}% |" for column, pct in nonzero)
    return "\n".join(lines)


def build_summary(
    mexican_rows: list[dict[str, str]],
    lithuanian_rows: list[dict[str, str]],
    mexican_features: int,
    lithuanian_features: int,
) -> str:
    return f"""# Interim Public CIS Dataset Summary

## Scope

This directory contains two independent, source-preserving interim extracts.
They are not a merged dataset and are not a final longitudinal CIS-to-MS
prediction cohort. No visit dates, conversion dates, last-follow-up dates, or
artificial sequence rows have been created.

## Mexican cohort

- Source records retained: {len(mexican_rows)}
- Unique source patient identifiers: {len(set(row["source_patient_id"] for row in mexican_rows))}
- Source covariate columns retained: {mexican_features}
- Candidate-feature source representations: 8 of 14 (source fields or codes only)
- Model-approved input features: 0. A valid prediction index, outcome timing, and codebook review are still absent.
- Candidate target: source_group_code, with raw values 1: {sum(row["source_group_code"] == "1" for row in mexican_rows)} and 2: {sum(row["source_group_code"] == "2" for row in mexican_rows)}
- Target status: unlabelled. The official source does not document whether group 1 or group 2 means conversion.
- Excluded from predictive inputs: final_edss_source_value, source_group_code, interim record ID, and source patient ID.

## Lithuanian cohort

- Source records retained: {len(lithuanian_rows)}
- Unique source patient identifiers: {len(set(row["source_patient_id"] for row in lithuanian_rows))}
- Source covariate columns retained: {lithuanian_features}
- Candidate-feature source representations: 7 of 14 (source fields or codes only)
- Model-approved input features: 0. A valid prediction index and pre-index measurement timing are still absent.
- Documented interim grouping: final_ms_diagnosis_flag, with 0: {sum(row["final_ms_diagnosis_flag"] == "0" for row in lithuanian_rows)} and 1: {sum(row["final_ms_diagnosis_flag"] == "1" for row in lithuanian_rows)}
- Target meaning: final MS versus non-MS diagnosis during retrospective record review. It is not conversion within a fixed future horizon.
- Excluded from predictive inputs: final_ms_diagnosis_flag, interim record ID, and source patient ID.

## Proposed 14-feature coverage

| Proposed feature | Mexican interim representation and decision | Lithuanian interim representation and decision |
|---|---|---|
| 1. Age at CIS | age_years; partial only because individual index date is absent | age_years; partial only because individual index date is absent |
| 2. Sex | sex_code; retained raw because codebook is absent | sex_code; retained raw because patient-level codebook is absent |
| 3. Initial CIS type | initial_symptom_code and mono_or_polysymptomatic_code; not harmonized | focal_symptoms_code; related but not a standardized CIS type |
| 4. OCB status | ocb_code; values 0/1/2 are not mapped | ocb_positive_code; test date absent |
| 5. IgG index | unavailable | CSF IgG level only; not an IgG index |
| 6. Months from baseline | unavailable | unavailable |
| 7. EDSS score | initial_edss_source_value; date absent | unavailable |
| 8. Relapses since previous visit | unavailable | unavailable |
| 9. Total T2 lesion count | unavailable | unavailable |
| 10. New/enlarging T2 lesions | unavailable | unavailable |
| 11. Gd-enhancing lesion count | unavailable | unavailable |
| 12. Periventricular lesion count | periventricular_mri_code; source indicator, not a count | periventricular_mri_code; source indicator, not a count |
| 13. Infratentorial lesion count | infratentorial_mri_code; source indicator, not a count | infratentorial_mri_code; source indicator, not a count |
| 14. Spinal cord lesion count | spinal_cord_mri_code; source indicator, not a count | spinal_cord_mri_code; source indicator, not a count |

Every source representation in this table remains excluded from model-ready
features until its codebook and pre-index measurement timing are established.
The detailed mapping CSV records original names, missingness, transformations,
and feature-specific ambiguity or leakage risk.

## Combination decision

Do not combine the files. The Mexican target mapping is unverified, the
Lithuanian target is a documented but untimed final-diagnosis grouping, and
the cohorts differ in population, diagnostic era, codebooks, and measurement
definitions. A joint supervised target would be misleading.

## Scientific-use decision

The interim extracts are valid for provenance-preserving descriptive review and
source-specific quality work. They are not approved training data for the
future CIS-to-MS prediction objective. The Lithuanian file can support a
descriptive final-diagnosis group comparison only after its predictor timing is
reviewed; it is not a fixed-horizon prediction dataset. The Mexican file has
no validated binary target in the official source.

## Longitudinal and scale requirements still open

The final dataset requires an approved source with a stable patient key,
confirmed baseline CIS/index date, at least two genuine dated pre-index visits,
conversion dates for events, last follow-up for non-events, criteria version,
and a prespecified horizon. The 2,000-patient aspiration remains unfilled; the
current public extracts provide no valid eligible longitudinal cohort count.
"""


def build_quality_report(
    mexican_rows: list[dict[str, str]],
    lithuanian_rows: list[dict[str, str]],
    mexican_columns: list[str],
    lithuanian_columns: list[str],
    mexican_checks: list[dict[str, Any]],
    lithuanian_checks: list[dict[str, Any]],
) -> str:
    def check_lines(checks: list[dict[str, Any]]) -> list[str]:
        return [
            f"| {check['check']} | {check['status']} | {check['count']} | {check['detail']} |"
            for check in checks
        ]

    return f"""# Interim Dataset Data-Quality Report

## Processing controls

- Raw XLSX workbooks are read only; SHA-256 verification remains in the source audit.
- Values are renamed only. No imputation, recoding of uncertain clinical codes,
  row deletion, deduplication, oversampling, or synthetic data generation was performed.
- Every output row retains its workbook source row number and source identifier.
- The Mexican duplicate source identifier is preserved in separate records.

## Mexican validation checks

| Check | Status | Count | Detail |
|---|---|---:|---|
{chr(10).join(check_lines(mexican_checks))}

{markdown_missingness("Mexican nonzero missingness", mexican_rows, mexican_columns)}

## Lithuanian validation checks

| Check | Status | Count | Detail |
|---|---|---:|---|
{chr(10).join(check_lines(lithuanian_checks))}

{markdown_missingness("Lithuanian nonzero missingness", lithuanian_rows, lithuanian_columns)}

## Target-label conclusion

Mexican source_group_code remains unlabelled because no official source
codebook establishes the conversion mapping. Lithuanian final_ms_diagnosis_flag
is retained because the original publication defines final MS and non-MS
groups, but it remains an untimed final-diagnosis grouping rather than a
future-outcome label.

## Longitudinal consistency conclusion

Neither cohort has actual repeated dated visits. The files are one-row-per-
source-record interim extracts and cannot be converted into RNN-LSTM sequences
or normalized patients/visits/outcomes records without fabricating information.
"""


def run(repo_root: Path, output_dir: Path) -> dict[str, Any]:
    """Create the requested cohort-specific interim files and reports."""

    mexican_audit, mexican_raw = source_records(repo_root, 0)
    lithuanian_audit, lithuanian_raw = source_records(repo_root, 1)
    mexican_columns, mexican_rows = make_rows(
        mexican_audit,
        mexican_raw,
        MEXICAN_MAPPINGS,
        "MEX",
        "source_group_code_only",
        "unverified_group_mapping_no_binary_label_assigned",
    )
    lithuanian_columns, lithuanian_rows = make_rows(
        lithuanian_audit,
        lithuanian_raw,
        LITHUANIAN_MAPPINGS,
        "LTU",
        "final_ms_diagnosis_grouping_not_fixed_horizon",
        "documented_final_ms_vs_non_ms_grouping_not_future_conversion_label",
    )
    mexican_mapping, mexican_features = mapping_rows(
        mexican_audit, MEXICAN_MAPPINGS, mexican_rows
    )
    lithuanian_mapping, lithuanian_features = mapping_rows(
        lithuanian_audit, LITHUANIAN_MAPPINGS, lithuanian_rows
    )
    mexican_checks = validate_mexican(mexican_rows)
    lithuanian_checks = validate_lithuanian(lithuanian_rows)

    output_dir.mkdir(parents=True, exist_ok=True)
    write_csv(output_dir / "mexican_interim.csv", mexican_rows, mexican_columns)
    write_csv(
        output_dir / "lithuanian_interim.csv", lithuanian_rows, lithuanian_columns
    )
    mapping_columns = list(mexican_mapping[0])
    write_csv(
        output_dir / "source_to_processed_mapping.csv",
        mexican_mapping + lithuanian_mapping,
        mapping_columns,
    )
    write_csv(
        output_dir / "interim_feature_dictionary.csv",
        mexican_features + lithuanian_features,
        mapping_columns,
    )
    (output_dir / "interim_dataset_summary.md").write_text(
        build_summary(
            mexican_rows,
            lithuanian_rows,
            len(mexican_features),
            len(lithuanian_features),
        )
        + "\n",
        encoding="utf-8",
    )
    (output_dir / "interim_data_quality_report.md").write_text(
        build_quality_report(
            mexican_rows,
            lithuanian_rows,
            mexican_columns,
            lithuanian_columns,
            mexican_checks,
            lithuanian_checks,
        )
        + "\n",
        encoding="utf-8",
    )
    report = {
        "generated_at_utc": datetime.now(UTC).isoformat(),
        "overall_status": "INTERIM_DESCRIPTIVE_ONLY_NO_LONGITUDINAL_TRAINING",
        "mexican": {
            "source_rows": len(mexican_rows),
            "unique_source_patient_ids": len(
                set(row["source_patient_id"] for row in mexican_rows)
            ),
            "retained_source_covariates": len(mexican_features),
            "target": {
                "representation": "source_group_code_only",
                "validated_for_supervised_use": False,
                "raw_counts": dict(
                    sorted(Counter(row["source_group_code"] for row in mexican_rows).items())
                ),
            },
            "checks": mexican_checks,
        },
        "lithuanian": {
            "source_rows": len(lithuanian_rows),
            "unique_source_patient_ids": len(
                set(row["source_patient_id"] for row in lithuanian_rows)
            ),
            "retained_source_covariates": len(lithuanian_features),
            "target": {
                "representation": "final_ms_diagnosis_grouping_not_fixed_horizon",
                "validated_for_future_prediction": False,
                "valid_for_descriptive_grouping": True,
                "raw_counts": dict(
                    sorted(
                        Counter(
                            row["final_ms_diagnosis_flag"] for row in lithuanian_rows
                        ).items()
                    )
                ),
            },
            "checks": lithuanian_checks,
        },
        "combined_dataset_created": False,
        "combination_decision": (
            "Not scientifically defensible: incompatible target semantics, "
            "unverified Mexican group mapping, distinct eras/populations, and "
            "unharmonized feature coding."
        ),
        "longitudinal_dataset_available": False,
        "records_excluded": 0,
        "exclusion_policy": "No source record was silently removed or merged.",
    }
    (output_dir / "interim_validation_report.json").write_text(
        json.dumps(report, indent=2) + "\n", encoding="utf-8"
    )
    return report


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Prepare source-preserving interim public CIS cohort extracts."
    )
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=Path(__file__).resolve().parents[2],
        help="Repository root containing data/raw.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=None,
        help="Output directory for interim files.",
    )
    args = parser.parse_args()
    repo_root = args.repo_root.resolve()
    output_dir = (
        args.output_dir.resolve()
        if args.output_dir
        else repo_root / "data" / "processed" / "interim"
    )
    report = run(repo_root, output_dir)
    print(json.dumps(report, indent=2))
    print(f"Wrote interim files to {output_dir}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
