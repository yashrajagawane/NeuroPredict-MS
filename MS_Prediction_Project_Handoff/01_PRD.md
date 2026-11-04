# 01 — Product Requirements Document (PRD)

## 1. Product summary

The proposed product is a local or hosted educational research application for exploring MS / Non-MS classification from structured longitudinal patient records. It combines a small patient-record interface with a backend, a database, preprocessing/sequence generation, and a saved hybrid RNN–LSTM model.

## 2. Goals

- Demonstrate an end-to-end workflow for structured patient visit records.
- Preserve the chronological order of visits.
- Explore whether a hybrid RNN–LSTM can learn from longitudinal records.
- Compare the hybrid model with simpler baselines.
- Present predictions and evaluation results transparently.
- Make the project reproducible for academic review.

## 3. Non-goals

- Replacing a neurologist or making clinical diagnoses.
- Giving treatment recommendations or medication advice.
- Predicting relapse, EDSS progression, CIS conversion, or disease course unless the target is formally changed and supported by the dataset.
- Processing raw MRI images in the current scope.
- Claiming clinical deployment, prospective validation, or regulatory approval.
- Using identifiable patient data without authorization and appropriate safeguards.

## 4. Primary user stories

### Authorized user
- As an authorized user, I can create or select a pseudonymous patient record.
- I can add structured information for a dated visit.
- I can review visits in chronological order.
- I can request a research prediction when enough valid visits are available.
- I can see the predicted MS / Non-MS class, model version, and a clear non-diagnostic disclaimer.
- I can review previous predictions if prediction-history storage is implemented.

### Student / researcher
- I can inspect the dataset schema and data quality.
- I can run reproducible preprocessing and sequence generation.
- I can train baseline models and the hybrid RNN–LSTM model.
- I can evaluate all models on identical patient-level partitions.
- I can inspect metrics, confusion matrices, and experiment metadata.

## 5. Product features and priority

| ID | Feature | Priority | Notes |
|---|---|---:|---|
| PR-01 | Dataset import and schema validation | Must | CSV/Parquet selection after dataset confirmation |
| PR-02 | Patient/visit chronology | Must | Requires patient ID and visit date/time |
| PR-03 | Missingness and data-quality report | Must | Do not silently modify source data |
| PR-04 | Patient-level train/validation/test split | Must | One patient must not appear in multiple partitions |
| PR-05 | Train-only preprocessing pipeline | Must | Fit transforms on training partition only |
| PR-06 | Sequence construction | Must | Preserve visit order and true time spacing where relevant |
| PR-07 | Baseline models | Must | Logistic regression and/or tree/SVM baseline; choose after data inspection |
| PR-08 | Hybrid RNN–LSTM experiment | Must | Proposed sequence architecture; data must support sequences |
| PR-09 | Evaluation report | Must | Include class-wise metrics and confusion matrix |
| PR-10 | Patient/visit interface | Should | Only if app is part of final deliverable |
| PR-11 | Prediction endpoint | Should | Load saved, versioned model and preprocessing artifact |
| PR-12 | Prediction history | Could | Include only if needed and privacy design is settled |
| PR-13 | Authentication and roles | Should | Required before multi-user access or real sensitive data |

## 6. User experience principles

- Simple, clean, accessible interface.
- Use plain language and explain missing/invalid fields.
- Show the patient timeline clearly.
- Do not present output as a diagnosis.
- Do not display uncalibrated probabilities as personal medical risk.
- Show which model version generated a result.

## 7. Constraints and dependencies

- Dataset availability, permission, and label quality are currently unconfirmed.
- Longitudinal data must contain multiple ordered visits per patient.
- Binary target semantics must be confirmed before model development.
- The sequence model is only justified if genuine temporal observations exist.
- Clinical validity cannot be established by a student prototype alone.

## 8. MVP definition

The minimum credible MVP is a reproducible notebook/pipeline that loads a documented dataset, validates it, creates patient-level splits and chronological sequences, trains baselines and a hybrid RNN–LSTM if the data support it, and generates a report. A web application is a secondary layer and should not delay fixing dataset/target validity.
