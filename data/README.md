# CIS-to-MS Dataset Research Area

This directory separates immutable source workbooks from non-patient-level audit
artifacts, reports, and reusable validation code.

## Current status

**NO-GO for Hybrid RNN-LSTM training.** The two legally downloadable public
sources are genuine CIS cohorts, but their workbooks contain one row per
patient, no patient-linked visit table, no visit dates, no conversion dates,
and no patient-level last-follow-up dates. They must not be converted into
synthetic visit sequences.

The recommended acquisition route is a supervised, approved request to
MSBase/MSBasis or another cohort owner. See
[candidate_source_comparison.md](reports/candidate_source_comparison.md) and
[msbase_access_request_spec.md](contract/msbase_access_request_spec.md). The
full research evidence record is
[source_evidence_ledger.md](reports/source_evidence_ledger.md), and the final
gate decision is in
[final_dataset_readiness_review.md](reports/final_dataset_readiness_review.md).

## Layout

- raw/ — immutable official source files. This is ignored by Git.
- audit/ — non-patient-level source inventory, missingness report, manifest,
  and an SVG cohort-size chart.
- reports/ — provenance, quality, label, feature, and source-access reports.
- contract/ — the normalized data contract and a request specification for a
  controlled-access cohort.
- scripts/ — standard-library-only audit and contract validators.
- tests/ — automated checks for the audit and longitudinal outcome rules.

## Reproducible commands

For the shared Python 3.12 developer environment, locked tooling, CI checks,
and secret-handling rules, see the repository [development guide](../DEVELOPMENT.md).

Run from the repository root:

    python .\data\scripts\audit_public_cis_sources.py --repo-root .
    python -m unittest discover -s .\data\tests -v

The first command only profiles source files and creates non-patient-level audit
outputs. It does not create patients.csv, visits.csv, or outcomes.csv.

## Source-preserving interim extracts

Two cohort-specific interim CSV extracts can be generated locally from the
official raw workbooks:

    python .\data\scripts\prepare_interim_cis_datasets.py --repo-root .

They are written to `processed/interim/`, which is Git-ignored because the
files retain source-row linkage. The extracts deliberately remain separate:
the Mexican group-code mapping is unverified, while the Lithuanian final-MS
flag is an untimed final-diagnosis grouping. They are descriptive,
provenance-preserving interim data only, not `patients.csv`, `visits.csv`, or
`outcomes.csv` for future CIS-to-MS training. The empty schemas in
`templates/` are for a future approved longitudinal acquisition and contain no
patient records.

## Guarded modeling utilities

`scripts/guarded_model_data.py` provides in-memory readiness assessment,
patient-level splitting, and pre-index sequence construction for a future
approved cohort. Each operation requires a passing normalized contract plus
explicit approvals for source access, confirmed baseline CIS, outcome
adjudication, and feature timing. It also requires at least two genuine dated
visits at or before the prediction index. It writes no split or sequence files.
The current interim extracts fail these gates and cannot be passed to these
operations as supervised future-conversion data.

To validate a future approved normalized export:

    python .\data\scripts\validate_longitudinal_cis_contract.py ^
      --patients .\approved\patients.csv ^
      --visits .\approved\visits.csv ^
      --outcomes .\approved\outcomes.csv ^
      --report .\data\audit\approved_contract_validation.json

The command exits nonzero when a required temporal or outcome-integrity rule
fails. It does not modify the input files.

## Future longitudinal pipeline

The scripts `prepare_datasets.py`, `validate_datasets.py`,
`create_patient_splits.py`, and `prepare_model_inputs.py` support a future
approved three-table release. `prepare_datasets.py --source-workbooks` calls
the existing interim extractor and never produces longitudinal tables.
Validation, splitting, and sequence creation require the paths to all three
tables and four explicit approval flags. Current interim cohorts fail the
required contract and receive no splits or model inputs.

Split and sequence outputs remain in memory except for the opt-in patient split
manifest. That manifest must be stored only in the approved secure modeling
area. The splitter is seeded and patient-level, but currently does not perform
class stratification; class counts and sample size must be reviewed before
using it. Sequence generation is not model training and does not fit any
learned preprocessing.
