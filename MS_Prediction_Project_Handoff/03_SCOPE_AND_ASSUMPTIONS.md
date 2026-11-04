# 03 — Scope, Assumptions, and Constraints

## In scope for the current project

- Structured/tabular patient records with multiple time-stamped visits.
- Binary MS / Non-MS classification as the current provisional target.
- Patient-level data splitting.
- Data quality checks, preprocessing, and chronological sequence creation.
- Conventional ML baselines for comparison.
- Proposed hybrid RNN → LSTM model.
- Model evaluation and transparent reporting.
- Optional educational web interface for entering/viewing patient records and requesting research predictions.

## Out of scope unless explicitly approved

- Raw MRI image processing or lesion segmentation.
- Clinical diagnosis, treatment decisions, or clinician-facing medical advice.
- Prediction of EDSS progression, relapse, CIS conversion, or other future outcomes under the current binary-label definition.
- Deployment for real patient-care decisions.
- Collecting identifiable patient records without permission and ethics review.
- Claims of fairness, safety, clinical benefit, or external validity without suitable evidence.

## Provisional assumptions

1. Data are structured and include a pseudonymous patient identifier.
2. Each patient has multiple visit records with usable timestamps.
3. There is a defensible MS / Non-MS label and a clear label reference time.
4. The dataset owner permits the intended research use.
5. The model predicts one class per patient at a defined index time.
6. The exact feature list, visit count, and sequence length are not yet fixed.
7. The app is a demonstration prototype, not a production clinical tool.

## Constraints

- A sequence model is not justified by a single cross-sectional row per patient.
- A model trained on arbitrary synthetic labels can only demonstrate code execution, not MS prediction validity.
- A random row split can put visits from one patient in both train and test partitions, inflating performance.
- Data from after the prediction/index time can leak the answer into predictors.
- Different clinical endpoints must not be combined into one label without a clear and justified definition.

## Scope-change process

Any change to prediction target, modality, dataset, model family, or deployment audience must be recorded in `14_OPEN_DECISIONS.md` and reflected in the PRD, SRS, data specification, model specification, and architecture before implementation continues.
