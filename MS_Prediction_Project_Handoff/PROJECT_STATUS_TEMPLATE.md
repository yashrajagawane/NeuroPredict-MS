# Project Status Log

Update this file at the end of every implementation session.

## Current status
- Current phase: Phase 0 and Phase 2 research/audit plus multi-CSV and guarded modeling utilities complete; final cohort acquisition is blocked pending controlled-access feasibility
- Dataset: Two public CIS sources acquired, audited, and separately extracted into source-preserving interim CSVs. Neither is eligible for the required longitudinal sequence model. MSBase/MSBasis is the recommended controlled-access feasibility route.
- Label definition/index time: Confirmed project question is future CIS-to-MS conversion. Patient-level index date and prediction horizon remain unconfirmed because the public sources lack the required dates.
- Application: Not confirmed as implemented
- Trained model: Not confirmed as implemented
- Deployment: Not planned/confirmed

## Completed
- [x] Repository inventory
- [ ] Dataset and target confirmation
- [x] Public-source data audit and label-feasibility review
- [x] Source-preserving interim public-cohort preparation (not model-ready preprocessing)
- [ ] Preprocessing and sequence builder
- [ ] Baseline models
- [ ] Hybrid RNN–LSTM
- [ ] Evaluation
- [ ] Backend/API
- [ ] Frontend
- [ ] Integration/security tests
- [ ] Final documentation and demo

## Latest changes
- Date: 2026-11-04
- Files changed: data/ (added pipeline entry scripts, guarded in-memory data utilities, four CSV architecture and readiness reports, README, and safeguard tests); MS_Prediction_Project_Handoff/ (status record)
- Commands run: python -m py_compile .\data\scripts\prepare_datasets.py .\data\scripts\validate_datasets.py .\data\scripts\prepare_model_inputs.py .\data\scripts\create_patient_splits.py .\data\scripts\guarded_model_data.py; python -m unittest discover -s .\data\tests -v; git diff --check
- Tests passed/failed: 13 passed / 0 failed
- Actual completed work: Preserved all 273 Mexican source rows (272 unique source IDs; one duplicate retained) and all 138 Lithuanian rows in separate interim files. Preserved raw codes, source-row traceability, missing values, and target uncertainty; documented 17 and 42 retained source covariate columns respectively. Existing header-only templates remain. Added `prepare_datasets.py`, `validate_datasets.py`, `create_patient_splits.py`, and `prepare_model_inputs.py` entry points backed by source-preserving extraction and readiness guards. Added reports describing data grain, counts, and current NO-GO. The splitter and sequence builder refuse current cohort data. No records were deleted, deduplicated, imputed, combined, split, or used for training.
- Remaining blockers: No public candidate has patient-linked repeated dated visits, conversion dates, or last-follow-up dates. The Mexican group-code target is unverified. The Lithuanian final-MS flag is an untimed final-diagnosis grouping, not a future conversion label. An approved feasibility extract must establish these fields before a horizon, labels, features, or recurrent model can be finalized.

## Current model evidence
- Dataset/version: No final model dataset. Source-preserving interim extracts only: Mexican 273 rows / 17 retained source covariates; Lithuanian 138 rows / 42 retained source covariates; see [final_dataset_readiness_review.md](../data/reports/final_dataset_readiness_review.md).
- Target definition: Future confirmed CIS-to-MS conversion within a fixed post-index horizon; horizon/index still require an approved extract.
- Split strategy: Required patient-level split; no split constructed because no model cohort exists.
- Model version:
- Metrics:
- Limitations: Current public workbooks are one-row-per-patient extracts and cannot support genuine RNN-LSTM sequences or validated Class 0 follow-up.

Do not fill in results until they are generated from actual experiments.
