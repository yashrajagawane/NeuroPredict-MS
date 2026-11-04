# 02 — Software Requirements Specification (SRS)

## 1. Purpose

Specify the functional and non-functional requirements for the proposed MS prediction research prototype.

## 2. System context

The proposed system accepts structured patient and visit records, stores/retrieves authorized records, prepares chronological sequences, obtains an output from a saved RNN–LSTM model, and displays a research prediction.

## 3. Functional requirements

| ID | Requirement | Acceptance evidence |
|---|---|---|
| FR-01 | The system shall accept a documented patient/visit data format. | Valid sample record imports successfully. |
| FR-02 | The system shall validate required fields, data types, and visit dates. | Invalid rows are rejected with actionable errors. |
| FR-03 | The system shall associate each visit with one pseudonymous patient ID. | Visits can be retrieved by patient ID. |
| FR-04 | The system shall display visits in chronological order. | Dates are sorted correctly, including repeated-date handling. |
| FR-05 | The training pipeline shall split data by patient. | No patient ID overlaps between partitions. |
| FR-06 | The training pipeline shall fit preprocessing transforms on training data only. | Tests confirm validation/test data do not affect fitted transforms. |
| FR-07 | The pipeline shall construct ordered sequences from actual visit records. | Sequence test preserves visit order and feature dimensions. |
| FR-08 | The system shall train and evaluate appropriate baseline models. | Experiment report includes selected baselines. |
| FR-09 | The system shall train a hybrid RNN–LSTM only if the dataset supports meaningful sequences. | Training configuration and rationale are documented. |
| FR-10 | The prediction service shall load a saved model and matching preprocessing artifact. | Inference succeeds with a compatible model version. |
| FR-11 | The prediction service shall return an MS/Non-MS class or a clear “cannot predict” response. | Invalid/incomplete input is not silently classified. |
| FR-12 | The UI/API shall display a non-diagnostic research disclaimer. | Disclaimer appears with every prediction result. |
| FR-13 | The evaluation pipeline shall report accuracy, precision, recall, F1-score, and confusion matrix. | Metrics are generated from held-out predictions and labels. |
| FR-14 | The evaluation pipeline should report specificity, ROC-AUC, and PR-AUC where statistically appropriate. | Report states positive class and metric definitions. |
| FR-15 | The system shall record model version and relevant prediction metadata if prediction history is enabled. | Stored result can be traced to model version. |

## 4. Non-functional requirements

- **Correctness:** Reject malformed, unsupported, or incomplete data instead of guessing.
- **Reproducibility:** Persist dataset version, split seed, preprocessing, configuration, model version, and software versions.
- **Privacy:** Use pseudonymous/de-identified data; do not expose direct identifiers in logs.
- **Security:** Protect any non-public application with authentication and authorization; keep secrets outside source control.
- **Usability:** Use clear forms, validation messages, readable charts, and a visible disclaimer.
- **Maintainability:** Separate data, model, API, storage, and UI layers.
- **Portability:** Support documented local setup on a standard development machine.
- **Performance:** Establish response-time targets only after dataset size and deployment environment are known.
- **Availability:** No production SLA is claimed for the student prototype.

## 5. User requirements

- Enter or import permitted patient and visit data.
- Open a patient record and review visits in date order.
- Request an experimental prediction when sufficient data exist.
- View the predicted class, model version, and non-diagnostic notice.

## 6. Hardware and software

Hardware is to be finalized after dataset size and model complexity are known. A typical modern laptop may support initial development; GPU acceleration is optional and should be justified by training needs. The recommended software stack is listed in `00_PROJECT_BRIEF.md`; it is not yet an implemented stack.

## 7. Error handling

The system should provide explicit errors for missing features, invalid values, unsupported schema versions, insufficient visits, unavailable model artifacts, and database failures. A failed prediction must never be replaced by a fabricated class.
