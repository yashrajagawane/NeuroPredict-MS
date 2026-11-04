# 10 — Testing and Evaluation Plan

This is a plan, not evidence that application or model tests have been implemented. Use `pytest` for Python data/API/ML tests. The frontend test tools will be selected within the approved React stack before UI implementation; do not add a different application framework.

## 1. Mandatory application module test scenarios

| Module | Required scenarios and expected result |
|---|---|
| Doctor login/authentication | Valid sign-in establishes an authorized session; invalid credentials fail safely; logout/revoked/expired sessions cannot call protected APIs; unauthorized roles and cross-patient access are denied. |
| Patient registration/management | Unique pseudonymous ID is assigned/validated; duplicates and prohibited direct identifiers are rejected; authorized search/view/update works; unauthorized CRUD is denied and auditable. |
| Patient visit history | Visits link to the correct patient; missing patient and duplicate visit are rejected or handled by an approved rule; out-of-order input is returned chronologically; repeated dates follow documented ordering behavior. |
| Clinical data management | Only approved fields can be submitted; invalid type/range/category/unit/date is rejected; missing/unassessed is distinct from zero; measurement time and unit remain traceable. |
| Research prediction | No model, incompatible schema/artifact, insufficient pre-index history, post-index measurement, invalid input, service failure, or denied caller returns an explicit unavailable/error state with no class; a compatible approved test artifact returns version, timestamp, limitations and disclaimer. |
| Prediction history/results | Actual events are associated with the correct patient and model version; successful results and unavailable/failed requests are distinguishable; unauthorized history access is denied; no fabricated result is displayed. |

## 2. Data and preprocessing tests

- Required columns, types, identifiers, units, dates, foreign keys, and allowed values are checked.
- Duplicate patients/visits, inconsistent chronology, missingness, and invalid measurement ranges are reported.
- No patient ID overlaps partitions; each patient stays in one split.
- Learned imputation, scaling, encoding, and feature selection fit using training patients only.
- Sequence shape/order preserves genuine time and excludes all post-index observations.
- Unknown or insufficiently followed outcomes never become Class 0.
- Current cross-sectional interim cohorts are refused by future-outcome split/sequence utilities.

## 3. Model tests and evaluation

- Verify model input/output shapes, serialization, compatible preprocessing, and reproducible configuration.
- Use train for fitting, validation for model/threshold selection, and an untouched patient-level test partition for final evaluation.
- Compare appropriate baselines and SimpleRNN → LSTM → Dense on identical patient partitions when data support both.
- Report class counts, positive class, accuracy, precision, sensitivity/recall, specificity, F1, confusion matrix, ROC-AUC/PR-AUC where appropriate, and uncertainty where feasible.
- If probabilities are shown, evaluate calibration and document threshold selection.
- Do not report synthetic-data metrics as clinical performance or claim that a model is accurate based on one metric.

## 4. Security and integration tests

- Verify protected frontend routes and, independently, backend authorization and RLS.
- Test token/session expiry, role denial, IDOR/cross-patient denial, safe errors, and absence of secrets/clinical payloads in logs.
- Verify frontend/backend schema compatibility, model-unavailable handling, model-version traceability, database failure behavior, and complete authorized flows using non-sensitive fixtures.
- Use synthetic test fixtures only when clearly labelled; never represent them as genuine patient data.

## 5. Test reporting

For each test run, record exact command, environment/runtime version, pass/fail counts, relevant dataset/model version (if any), failures, and scope. A past test result is not evidence of a current run. Do not claim tests passed unless executed.

## 6. Evaluation report template

- Dataset/version and permitted-use status:
- Eligible patients / visits / event and non-event counts:
- Index/horizon/label rules and diagnostic criteria:
- Split strategy, patient overlap check, and seed:
- Preprocessing and leakage checks:
- Model architecture/version and baselines:
- Accuracy / precision / recall-sensitivity / specificity / F1:
- ROC-AUC / PR-AUC / calibration if appropriate:
- Confusion matrix / uncertainty:
- Limitations, subgroup support, and generalization boundaries:
- Exact test commands and results:
