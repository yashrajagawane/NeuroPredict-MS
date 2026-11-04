# 05 — Machine Learning and Hybrid RNN–LSTM Specification

## 1. Prediction task

Current provisional task: binary classification of MS versus Non-MS using structured patient records collected across multiple visits.

This must be confirmed with a precise label definition and index time. Do not confuse current status classification with future prognosis, CIS conversion, relapse prediction, or disability progression.

## 2. Modeling strategy

Start with data validation and baselines. The hybrid RNN–LSTM should not be treated as automatically superior because it is more complex.

Recommended comparison set, selected based on data size and feature properties:

- Logistic regression as an interpretable baseline.
- Random forest or gradient-boosted trees as tabular baselines.
- Support vector machine if suitable for dataset scale and feature type.
- A sequence model only if multiple ordered observations per patient are available.
- Proposed hybrid RNN–LSTM as the main deep-learning experiment.

All models must use the same patient-level partitions and comparable input information where feasible.

## 3. Proposed hybrid architecture

Candidate architecture for implementation testing:

`Input Sequence (batch, time_steps, features)`  
`→ SimpleRNN(return_sequences=True)`  
`→ LSTM`  
`→ Dropout (optional, tuned)`  
`→ Dense(1, activation="sigmoid")`

For a binary label, a sigmoid output and binary cross-entropy are a reasonable starting point. The exact design must be adjusted based on data shape, class distribution, sequence length, and validation results. Do not lock arbitrary numbers of units, layers, or dropout rates before the data audit.

Potential configuration items:

- Feature count: derived from confirmed data dictionary.
- Sequence length: derived from visit distributions and a documented window policy.
- Hidden units: tuned on validation data.
- Batch size and epochs: selected experimentally.
- Optimizer and learning rate: documented and tuned.
- Early stopping: use validation monitoring without touching test data.
- Class imbalance: inspect first; consider class weights or resampling only within training data.

## 4. Preprocessing pipeline

1. Validate schema and types.
2. Separate patient IDs, timestamps, predictors, and labels.
3. Apply documented missing-value rules.
4. Encode categorical predictors where appropriate.
5. Scale numeric predictors using train-fitted transforms.
6. Arrange observations chronologically.
7. Create patient sequences using a documented index/window policy.
8. Pad/mask variable-length sequences if required.
9. Save the fitted preprocessing artifacts and feature schema with the model.

The exact same saved preprocessing must be used for inference.

## 5. Training procedure

- Patient-level train/validation/test split.
- Train baselines on training data.
- Tune model/hyperparameters using validation data.
- Freeze model, preprocessing, and threshold before final test evaluation.
- Evaluate on the untouched test patients once for final reported metrics.
- Save random seeds, configurations, versions, logs, and artifacts.

## 6. Evaluation metrics

Minimum metrics requested for the presentation:

- Accuracy.
- Precision.
- Recall/sensitivity.
- F1-score.

Recommended additional metrics for a health-related binary classifier:

- Confusion matrix.
- Specificity.
- ROC-AUC.
- PR-AUC, particularly if class distribution is imbalanced.
- Calibration assessment if probabilities are displayed.
- Confidence intervals where feasible.

State which class is positive, how the decision threshold was selected, and the class counts. Do not use accuracy alone.

## 7. Model artifact

Store the model together with:

- Model version and creation date.
- Feature names/order and schema version.
- Preprocessing artifacts.
- Sequence/window configuration.
- Label mapping and positive-class definition.
- Training data version/hash (without distributing sensitive data).
- Patient split metadata or reproducible split seed.
- Training configuration and evaluation summary.
- Library/runtime versions.

## 8. Inference contract

Input: one pseudonymous patient ID or a structured sequence of that patient's permitted visit records.  
Processing: validate, retrieve, transform with saved artifacts, create sequence, load compatible model.  
Output: predicted class (`MS` or `Non-MS`), model version, timestamp, and disclaimer.  
Probability: optional only if the output is clearly described and calibration/threshold behavior is documented.  
Failure: return a clear reason if data are insufficient, schema is incompatible, or the model artifact is unavailable.

## 9. Interpretation and limitation

An RNN–LSTM prediction is not a clinical diagnosis. A successful internal test does not prove usefulness in a different hospital, population, or clinical setting. External and prospective validation would be required for stronger claims.
