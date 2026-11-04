# 09 — Implementation Roadmap and Phases

Work phase-by-phase. Do not skip dataset validation to start building a neural network.

## Phase 0 — Repository reconnaissance and requirement freeze

**Tasks**
- Inspect existing repository and list current assets.
- Identify available data files, data licenses, notebooks, model code, LaTeX, and diagrams.
- Confirm task definition, dataset source, target label, feature schema, and whether a web app is required.
- Choose one backend framework and one UI approach.

**Deliverables**
- Repository inventory.
- Updated `14_OPEN_DECISIONS.md`.
- Confirmed MVP scope and stack.

**Gate:** Do not proceed to supervised training until the data and target are defensible.

## Phase 1 — Project scaffold and environment

**Tasks**
- Create clean folders for app, ML, data, tests, docs, and artifacts.
- Create Python environment and dependency file.
- Add configuration example, logging, formatting/linting, and basic CI if appropriate.

**Deliverables**
- Runnable project scaffold.
- Setup and run instructions.
- Health-check test.

## Phase 2 — Dataset audit and exploratory analysis

**Tasks**
- Load only permitted data.
- Validate schema, labels, units, timestamps, duplicates, missingness, class counts, visits per patient, and leakage risk.
- Produce a data-quality report.

**Deliverables**
- Data dictionary.
- EDA notebook/report.
- Explicit go/no-go recommendation for longitudinal modeling.

**Gate:** Confirm that data genuinely support patient-level longitudinal sequences and the target.

## Phase 3 — Data pipeline

**Tasks**
- Implement schema validation.
- Create patient-level split.
- Fit transforms on training data only.
- Build chronological sequences and variable-length handling if needed.
- Add tests for no patient overlap, chronology, shapes, and train-only fitting.

**Deliverables**
- Reusable preprocessing and sequence builder.
- Tests and serialized preprocessing artifacts.

## Phase 4 — Baseline models

**Tasks**
- Train appropriate simple tabular baselines.
- Use only information available at the index time.
- Evaluate on the same patient-level splits.

**Deliverables**
- Baseline metrics, confusion matrices, and experiment record.

## Phase 5 — Hybrid RNN–LSTM model

**Tasks**
- Implement candidate `SimpleRNN(return_sequences=True) → LSTM → Dense(sigmoid)` or justified variant.
- Tune using validation data only.
- Handle class imbalance carefully.
- Compare to baseline models fairly.

**Deliverables**
- Versioned model artifact.
- Training history and configuration.
- Validation and test report.

**Gate:** If sequences are not meaningful or the model does not outperform/justify complexity, report that honestly.

## Phase 6 — Evaluation and model report

**Tasks**
- Calculate accuracy, precision, recall, F1, confusion matrix, specificity, ROC-AUC/PR-AUC where appropriate.
- Document positive class, threshold, class balance, uncertainty, and limitations.
- Assess calibration if probability is exposed.

**Deliverables**
- Reproducible model evaluation report and tables/plots.

## Phase 7 — Backend and persistence

**Tasks**
- Implement patient/visit services if app is required.
- Connect to SQLite for local prototype.
- Implement prediction endpoint loading saved artifacts.
- Handle invalid/incomplete data and model-unavailable scenarios.

**Deliverables**
- API, database schema, API tests, migration/initialization instructions.

## Phase 8 — Frontend

**Tasks**
- Build patient list/detail, chronological visit history, and prediction result screens.
- Show validation and non-diagnostic notice.
- Keep UI simple and accessible.

**Deliverables**
- Working demonstrator UI and screenshots.

## Phase 9 — Integration and security review

**Tasks**
- Test full request-to-result flow.
- Add authentication if non-public access or sensitive records are used.
- Check privacy, logs, secrets, and error handling.

**Deliverables**
- Integrated demo and security checklist.

## Phase 10 — Final testing, documentation, and presentation

**Tasks**
- Run all tests and clean setup from scratch.
- Record actual limitations and results.
- Update architecture diagrams, user guide, README, project report, and PPT.

**Deliverables**
- Final source, model artifacts (if legitimate), test report, setup guide, demo guide, and updated presentation.
