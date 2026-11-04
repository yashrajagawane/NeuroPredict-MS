# 10 — Testing and Evaluation Plan

## 1. Data and preprocessing tests

- Required columns are present and correctly typed.
- Patient IDs are pseudonymous and non-empty.
- Visit dates parse and sort chronologically.
- Duplicate patient/visit records are detected.
- Missingness is reported and handled according to documented rules.
- Numeric scaling handles constant or invalid columns safely.
- Preprocessing fit uses training data only.
- No patient ID appears in more than one partition.
- Sequence shape matches `(batch, time_steps, features)` for model input.
- A patient's visits remain in the correct order.
- Insufficient visits produce a clear outcome rather than a fabricated sequence.

## 2. Model tests

- Model input and output shapes are checked.
- Binary label mapping is consistent.
- Training uses only training partition.
- Hyperparameter selection/early stopping uses validation partition.
- Final test partition is not used for tuning.
- Model save/load produces consistent predictions.
- Baselines and hybrid model use comparable partitions.
- Random seed/configuration is saved.

## 3. Minimum software test cases

| Test case | Expected result |
|---|---|
| Valid patient data | Accepted and stored/processed |
| Missing required field | Clear validation error |
| Invalid visit date | Rejected with useful error |
| Duplicate visit | Handled using documented duplicate rule |
| Visits out of input order | Retrieved/processed chronologically |
| Unknown patient ID | Not-found response |
| Too few visits | Clear “insufficient data” response |
| No trained model artifact | Prediction unavailable response; no fabricated class |
| Compatible saved model | Prediction returned with version and disclaimer |
| Database unavailable | Safe error response |

## 4. Model evaluation metrics

Report at minimum:
- Accuracy.
- Precision.
- Recall/sensitivity.
- F1-score.
- Confusion matrix.

Also report where appropriate:
- Specificity.
- ROC-AUC.
- PR-AUC.
- Calibration and Brier score if probabilities are displayed.
- Confidence intervals or uncertainty estimates where feasible.

Always state:
- Positive class.
- Class counts and prevalence.
- Decision threshold and how it was selected.
- Patient-level split strategy.
- Whether the result is validation, test, cross-validation, external, or prospective evidence.

## 5. Evaluation integrity

- A random row split is not acceptable as the primary split if multiple rows belong to each patient.
- Do not use future visits or post-index variables to predict an earlier label.
- Do not tune on the test set.
- Do not report metrics from synthetic data as clinical performance.
- Do not state “the model is accurate” based only on a single accuracy score.
- Do not compare results directly against publications with different labels, populations, horizons, and validation designs.

## 6. Final testing report template

- Dataset/version:
- Number of patients:
- Number of visit records:
- Class counts:
- Target and index time:
- Split strategy and seed:
- Preprocessing:
- Model architecture/version:
- Baseline models:
- Accuracy:
- Precision:
- Recall/sensitivity:
- Specificity:
- F1-score:
- ROC-AUC / PR-AUC:
- Confusion matrix:
- Calibration (if applicable):
- Limitations:
- Tests run and results:
