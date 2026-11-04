# Multiple Sclerosis Prediction Project — Agent Handoff Pack

**Project title:** Deep Learning Approach for Prediction of Multiple Sclerosis Using Hybrid RNN–LSTM  
**Project type:** Final-year engineering research prototype  
**Documentation status:** Initial requirements and design baseline; several decisions remain open.

## Purpose

This folder is the project reference pack for Codex, Claude, or another coding agent. Read `AGENTS.md` first, then `00_PROJECT_BRIEF.md`, `01_PRD.md`, and the remaining design documents before creating or changing code.

The pack describes a proposed end-to-end prototype that uses **structured patient records collected over multiple visits** and explores a **hybrid RNN–LSTM** model to predict an **MS / Non-MS** class.

## Important status disclosure

The project has so far been developed as a research concept, literature review, presentation, and workflow design. A previous review of the available project files found a LaTeX manuscript and diagrams, but no working application, trained model, or confirmed dataset. Re-check the actual repository before assuming that this is still true.

Do not represent planned features, model performance, real patient data, or clinical validity as completed facts.

## Recommended reading order

1. `AGENTS.md` — rules for coding agents.
2. `00_PROJECT_BRIEF.md` — one-page project summary and current decisions.
3. `01_PRD.md` — product requirements.
4. `02_SRS.md` — functional and non-functional requirements.
5. `03_SCOPE_AND_ASSUMPTIONS.md` — in-scope, out-of-scope, assumptions, and risks.
6. `04_DATA_REQUIREMENTS.md` — dataset and longitudinal data rules.
7. `05_ML_MODEL_SPECIFICATION.md` — baselines, proposed RNN–LSTM, training, and evaluation.
8. `06_WORKFLOWS.md` — development and prediction workflows.
9. `07_SYSTEM_ARCHITECTURE.md` — components and architecture.
10. `08_DATABASE_AND_API_DESIGN.md` — proposed storage model and API contract.
11. `09_IMPLEMENTATION_ROADMAP.md` — phases, deliverables, and gates.
12. `10_TESTING_AND_EVALUATION.md` — software and model testing.
13. `11_PRIVACY_SAFETY_AND_ETHICS.md` — health-data and responsible-use requirements.
14. `12_UI_UX_GUIDELINES.md` — screens and interface direction.
15. `13_ACCEPTANCE_CRITERIA.md` — definition of done.
16. `14_OPEN_DECISIONS.md` — questions that must be resolved before finalizing implementation.
17. `CODEX_KICKOFF_PROMPT.md` — prompt to start work safely.

## Recommended initial stack (not yet committed)

- **Language:** Python.
- **Data and ML:** Pandas, NumPy, scikit-learn.
- **Deep learning:** TensorFlow/Keras.
- **Backend:** Flask for a small student prototype; FastAPI is an alternative if a typed API-first design is preferred.
- **UI:** Flask templates + Bootstrap for the simplest first version. React can be considered later if there is a clear need.
- **Database:** SQLite for local development; PostgreSQL only if multi-user deployment or hosting requires it.
- **Development:** VS Code, Jupyter Notebook, Git, GitHub.

These are recommendations, not evidence that these technologies have already been implemented.

## Core scope clarification

The current project idea is a binary **MS / Non-MS classification** based on patient information collected across multiple visits. This is not automatically the same as predicting future disability progression or future conversion from clinically isolated syndrome (CIS). The exact target definition, prediction time, and label source must be confirmed in `14_OPEN_DECISIONS.md` before model development.
