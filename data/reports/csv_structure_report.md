# CSV Structure Report

## Current files and grain

| File | Grain | Rows | Purpose |
|---|---|---:|---|
| `processed/interim/mexican_interim.csv` | One source workbook record | 273 | Source-preserving Mexican cohort extract; 272 unique source IDs, with one repeated ID retained. |
| `processed/interim/lithuanian_interim.csv` | One source workbook record | 138 | Source-preserving Lithuanian cohort extract; 138 unique source IDs. |
| `templates/patients_template.csv` | One patient (header only) | 0 | Proposed static patient table. |
| `templates/visits_template.csv` | One genuine dated observation (header only) | 0 | Proposed longitudinal observation table. |
| `templates/outcomes_template.csv` | One patient/index/horizon outcome (header only) | 0 | Proposed verified outcome table. |

The interim files remain independent. Their source-specific columns are
documented in `processed/interim/source_to_processed_mapping.csv` and
`processed/interim/interim_feature_dictionary.csv`. These local files retain
source linkage and are Git-ignored. The original XLSX workbooks remain in the
existing `data/raw/` acquisition layout; they were not moved or altered.

## Proposed linked longitudinal tables

`patients.csv` has one row per pseudonymous patient. `visits.csv` references
`patients.patient_id` and has one row per actual dated observation.
`outcomes.csv` references the same patient and carries the prediction index,
horizon, adjudicated conversion status, event/follow-up dates, criteria, and
certainty. The three header-only templates define the draft columns. No
populated files exist because neither public cohort includes dated visits or a
verifiable future-conversion outcome.

## Validation rules

- Patient keys are nonblank and unique in patients; visit IDs are unique.
- Visits and outcomes must reference known patient IDs.
- Visit dates must parse as ISO dates and each modeled patient must have at
  least two dated observations.
- Class 1 requires a confirmed conversion date after index and within horizon.
- Class 0 requires last follow-up through the full horizon.
- Unknown or censored outcomes are not binary labels.
- All source clinical measures retain their original values and missingness;
  no value is interpreted without its codebook and timing.
- Identifiers, target fields, and post-index records are excluded from inputs.

See `contract/recommended_longitudinal_schema.md` and
`scripts/validate_longitudinal_cis_contract.py` for the executable contract.
