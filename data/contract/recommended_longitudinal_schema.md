# Recommended Normalized Contract for an Approved CIS Cohort

## Purpose

This contract is the minimum structure required before the project can train a
future-outcome sequence model. It is intentionally not populated from the
current public workbooks. All records must be genuine source observations and
all identifiers must be pseudonymous.

## Table: patients

One row per patient.

| Field | Requirement |
|---|---|
| patient_id | Stable, pseudonymous project identifier. Never use as a model feature. |
| source_cohort_id | Cohort/release identifier, not a direct personal identifier. |
| source_patient_key | Secure, restricted linkage key or one-way reference; never publish it. |
| site_id | Pseudonymous centre identifier where permitted. |
| birth_year_or_age_at_cis | Use the least identifying representation permitted by the data-use agreement. |
| sex_at_record | Source-defined value and codebook reference. |
| cis_presentation | Controlled source term plus original raw value. |
| cis_onset_date | Retain only when permitted; otherwise preserve a defensible relative time. |
| cis_diagnosis_date | Required to establish the baseline/index date when baseline prediction is used. |
| cis_diagnostic_criteria_version | Required source value or documented derivation status. |
| ocb_status and ocb_test_date | Optional only if source definition/date are available. |
| igg_index and igg_test_date | Optional only if the actual measure is an IgG index with units and date. |

Static CSF and baseline values must be stored once at their actual observation
time. They must not be copied to every visit.

## Table: visits

One row per genuine clinical or MRI observation. A source visit must not be
invented merely to make sequences equal length.

| Field | Requirement |
|---|---|
| patient_id | Foreign key to patients.patient_id. |
| visit_id | Unique pseudonymous visit key. |
| visit_date | Required ISO 8601 date or approved date representation preserving interval order. |
| visit_type | Clinical, MRI, lab, relapse assessment, or source-defined type. |
| months_from_baseline | Derived from a documented baseline date; retain calculation method/version. |
| edss | Optional ordinal value with source scale/version and assessment date. |
| kfs_* | Optional Kurtzke functional-system fields, retained separately from EDSS. |
| relapses_since_previous_visit | Derived only from dated relapse records and a documented interval rule. |
| total_t2_lesions | Optional count with MRI date/report provenance. |
| new_or_enlarging_t2_lesions | Optional interval count, with the comparison scan and interval explicitly known. |
| gd_enhancing_lesions | Optional count with contrast/report provenance. |
| periventricular_lesions | Count only if the source supplies a count; otherwise use a separate presence field. |
| infratentorial_lesions | Count only if the source supplies a count; otherwise use a separate presence field. |
| spinal_cord_lesions | Count only if the source supplies a count; otherwise use a separate presence field. |
| mri_report_format and measurement_source | Required for any MRI-derived feature. |
| observation_status | Observed, not assessed, unavailable, or invalid; missingness must not be silently coerced to zero. |

Dates and rows after the chosen prediction index may remain in the secure
longitudinal store for outcome adjudication, but they must be excluded from
the input sequence supplied to the model.

## Table: outcomes

One row for each approved patient-index-horizon combination.

| Field | Requirement |
|---|---|
| patient_id | Foreign key to patients.patient_id. |
| landmark_id | Required if more than one landmark is used; current validator supports one row per patient until extended and tested. |
| index_date | Required; model inputs must be on or before this date. |
| index_definition | Baseline CIS diagnosis or explicitly described landmark rule. |
| prediction_horizon_months | Fixed preregistered value for an analysis cohort. |
| conversion_status | 1, 0, unknown, or censored. |
| conversion_date | Required for status 1; must be after index and within the horizon. |
| last_follow_up_date | Required for all records; Class 0 must reach the full horizon. |
| ms_diagnosis_date | Preserve separately when distinct from event adjudication date. |
| diagnostic_criteria_version | Required for conversion adjudication. |
| outcome_certainty | Confirmed, source-reported, derived-under-documented-rule, uncertain, or censored. |
| censoring_reason | Required for censored/unknown records where available. |

## Outcome assignment rules

1. Include a patient only after confirming CIS at or before index.
2. Mark Class 1 only if conversion is confirmed after index and on/before the
   declared horizon.
3. Mark Class 0 only if no conversion is confirmed and last follow-up reaches
   the horizon.
4. Mark early loss to follow-up or unresolved diagnosis as unknown/censored,
   not Class 0.
5. Exclude patients converted before a later landmark from that landmark
   cohort.
6. Preserve original dates and raw diagnostic fields in the restricted source
   layer; document every derivation in a data dictionary.

## Required provenance and validation

Each approved release needs:

- source/cohort name, contact, release date, data-use authority, and hash;
- data dictionary and original variable names;
- field-mapping and unit-harmonization record;
- exclusion log with patient counts by reason;
- immutable raw layer, cleaned layer, and modeling-ready layer kept separate;
- reproducible extraction/validation script version; and
- a patient-level split manifest that prevents cross-split leakage.

Before any model preparation, run
data/scripts/validate_longitudinal_cis_contract.py against the three tables.
The validator blocks absent dates, broken foreign keys, invalid outcome windows,
and inadequate Class 0 follow-up. It does not replace clinical review or prove
that a field was measured before the index; those require source-specific audit.
