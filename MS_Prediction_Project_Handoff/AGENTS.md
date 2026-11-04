# Instructions for Coding Agents

You are working on a student research prototype concerning Multiple Sclerosis (MS) status prediction from structured longitudinal patient data using a proposed hybrid RNN–LSTM architecture.

## 1. Mandatory first steps

1. Inspect the repository and report its existing folders, source files, datasets, notebooks, model files, and current run status.
2. Read all project documents in this handoff pack before coding.
3. Identify existing work and preserve it. Do not overwrite or delete user work without permission.
4. Compare the repository with the project documents and report discrepancies.
5. Do not make up missing details. Record unresolved decisions and ask for the one decision that blocks the next phase.

## 2. Source of truth

Use the project documents as the current intended design. If an actual repository file conflicts with the documents, do not silently choose one. Report the conflict and propose a resolution.

Priority order:
- Confirmed user instruction in the current conversation.
- Existing, verified project assets and data dictionary.
- This handoff pack.
- General engineering recommendations, clearly labelled as recommendations.

## 3. Critical project constraints

- The current proposed input is structured patient data collected across multiple visits.
- The current proposed output is a binary MS / Non-MS class.
- Do not add MRI image processing to the current implementation unless the user explicitly changes scope.
- Do not claim that the model is trained, validated, deployed, clinically useful, or accurate until evidence exists.
- A synthetic dataset may be used only for software pipeline demonstrations unless the user explicitly approves a simulation study. Never present synthetic-data metrics as clinical performance.
- Do not generate labels from the same input features or arbitrary thresholds and then claim the model discovered clinically meaningful patterns. That creates a circular target/leakage problem.
- Split data by patient, not by individual visit row. Keep every visit from a patient in only one partition for the primary evaluation.
- Fit imputation, scaling, feature selection, and other learned preprocessing using training data only. Apply the fitted transforms unchanged to validation, test, and inference data.
- Preserve chronological order and timestamps. Do not treat unrelated columns as time steps.
- Never store real patient identifiers, names, contact details, or other direct identifiers in development/test data. Use legally obtained, de-identified data and follow applicable ethics, consent, licensing, and institutional requirements.
- The app is a research/educational prototype, not a diagnostic device or medical decision system.

## 4. Engineering rules

- Prefer readable, modular, typed code with clear docstrings and focused functions.
- Keep data preparation, model training, model inference, API, persistence, and UI concerns separated.
- Use configuration files/environment variables for settings. Never commit secrets.
- Add tests for data validation, sequence generation, preprocessing leakage, patient-level splitting, API behavior, and prediction output.
- Log reproducible experiment metadata: dataset version/hash, feature schema, split strategy, random seed, preprocessing configuration, model architecture, hyperparameters, library versions, and metrics.
- Save trained model artifacts and preprocessing artifacts together with a version/metadata file.
- Handle missing or malformed data explicitly; do not silently fill unknown values with arbitrary constants.
- Keep dependencies minimal and pin compatible versions once the environment is selected.
- Use migrations or a clearly documented schema evolution path if the database changes.
- Provide exact run/test commands in README files.

## 5. Medical and evaluation integrity

- Do not return a real-world diagnosis. UI must state: “Research prediction only — not a medical diagnosis. Do not use this result to make treatment decisions.”
- Do not display a confidence/probability as a calibrated risk unless calibration and threshold selection have been evaluated and documented.
- Report class balance, confusion matrix, precision, recall/sensitivity, specificity, F1-score, ROC-AUC and PR-AUC where appropriate. State the positive class and decision threshold.
- Include uncertainty intervals where feasible. Do not compare scores across different studies as if they were a common leaderboard.
- A high accuracy score alone is insufficient, especially under class imbalance.
- Compare the hybrid model against sensible, tuned baselines on identical patient-level splits.
- If the dataset does not support longitudinal observations for each patient, stop and report that the RNN–LSTM premise is not supported by the data. Do not fabricate sequences.

## 6. Collaboration and delivery

At the end of each phase:
1. Summarize files changed/created.
2. State exact commands run and whether they passed.
3. Show test results and unresolved issues.
4. State what is genuinely implemented versus planned.
5. Update project documentation to reflect verified changes.
6. Do not move to a later phase if an earlier phase has a blocking data/label/design issue.

## 7. Work style

Implement incrementally. Start with repository reconnaissance and Phase 0 in `09_IMPLEMENTATION_ROADMAP.md`. Do not generate the entire app in one unreviewed step. Do not invent a dataset, label definition, feature list, hardware result, or clinical claim.
