# 13 — Definition of Done and Acceptance Criteria

## Data readiness

- [ ] Dataset provenance and permitted use are documented.
- [ ] Label meaning, source, index time, and positive class are documented.
- [ ] Data dictionary is complete.
- [ ] Multiple genuine time-ordered visits per patient are available, or sequence modeling is reconsidered.
- [ ] Data quality and leakage report is reviewed.
- [ ] Patient-level split is implemented and overlap-tested.

## ML pipeline

- [ ] Preprocessing fits on training data only.
- [ ] Sequence generation preserves chronology and passes tests.
- [ ] Appropriate baseline models are trained.
- [ ] Hybrid RNN–LSTM is trained only if data support it.
- [ ] Evaluation uses a held-out patient-level test set.
- [ ] Class-wise metrics and confusion matrix are reported.
- [ ] Threshold and positive class are stated.
- [ ] Model and preprocessing artifacts are versioned together.
- [ ] Reproduction instructions are documented.

## Application (if included in final scope)

- [ ] Patient and visit records can be created/retrieved safely.
- [ ] Visits display in chronological order.
- [ ] Input validation and errors work.
- [ ] Prediction endpoint loads the compatible saved model.
- [ ] Missing/incompatible model produces a clear error.
- [ ] Result displays model version and disclaimer.
- [ ] Sensitive data are not exposed in logs or public repositories.

## Documentation and final demonstration

- [ ] README setup instructions work from a clean environment.
- [ ] All tests are run and results recorded.
- [ ] Screenshots show only demo/de-identified data.
- [ ] Architecture and workflows match actual implementation.
- [ ] Planned versus implemented features are clearly distinguished.
- [ ] Limitations and non-clinical intended use are documented.
