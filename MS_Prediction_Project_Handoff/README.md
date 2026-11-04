# NeuroPredict-MS — Project Handoff Pack

**Project:** Deep Learning Approach for Prediction of Multiple Sclerosis Using Hybrid RNN–LSTM

**Type:** Final-year research and educational prototype

**Current phase:** Phase 01 is complete with project-owner scope approval; Phase 02 remains blocked by cohort and clinical evidence. Continue independently eligible phases under the updated authorization.

## Source of truth and purpose

The root [`PROJECT_MASTER_PLAN.md`](../PROJECT_MASTER_PLAN.md) is the single source of truth for phase order, status, dependencies, and project progress. This handoff pack defines requirements and design constraints. Confirmed user decisions take precedence over older provisional wording in any document; unresolved clinical, data, privacy, and deployment choices must remain open.

The research objective is **future CIS-to-MS conversion prediction from genuine longitudinal patient records**. It is not cross-sectional MS-versus-healthy classification. The intended model experiment is SimpleRNN → LSTM → Dense, compared with appropriate baselines, only if an approved dataset supports it.

The final-year deliverable has two mandatory components:

1. A reproducible machine-learning research pipeline for permitted clinical data, including validation, preprocessing, patient-level evaluation, baselines, the proposed hybrid model where justified, and limitations.
2. A doctor-facing web application containing all six mandatory modules: authentication; patient registration/management; visit history; clinical data management; gated research prediction; and prediction history/results.

## Current evidence and limitations

- The Mexican and Lithuanian public cohorts remain separate interim datasets. They lack the required patient-linked dated visits, conversion dates, and adequate follow-up data for the intended future-outcome task.
- No operational index date or prediction horizon has been approved; there are zero approved features and zero valid fixed-horizon labels for training.
- The current decision is **NO-GO for supervised future-conversion training**. The app’s prediction operation must remain unavailable until a valid, tested, versioned model is trained on approved clinical data.
- No working application, database, trained model, or deployment is present. Do not describe requirements as implemented.
- Project-owner approval of this charter scope is recorded in the updated development authorization. No supervisor approval is claimed; any institutionally required review for real clinical-data use remains a separate governance gate.

## Approved technology stack

- **Frontend:** React, TypeScript, Vite, Tailwind CSS, shadcn/ui, React Router, TanStack Query, React Hook Form, Zod, Recharts, Lucide React.
- **Backend:** Python 3.12, FastAPI, SQLAlchemy ORM, Alembic, Pydantic.
- **Database and authentication:** Supabase PostgreSQL, Supabase Auth, PostgreSQL Row Level Security (RLS).
- **ML and analysis:** Pandas, NumPy, scikit-learn, TensorFlow/Keras, Matplotlib, Seaborn.
- **Development/testing:** pytest, Git/GitHub, VS Code, Jupyter Notebook.

Use React → FastAPI → SQLAlchemy → Supabase PostgreSQL. Keep offline model training separate from API inference. Never place Supabase service-role credentials in the frontend; patient-data access must be authorized and mediated by the backend and database policies. Do not introduce another framework or database without discussing it first.

## Reading order

1. `AGENTS.md` and root `PROJECT_MASTER_PLAN.md`.
2. `00_PROJECT_BRIEF.md`, `01_PRD.md`, `02_SRS.md`, `03_SCOPE_AND_ASSUMPTIONS.md`.
3. `04_DATA_REQUIREMENTS.md`, `05_ML_MODEL_SPECIFICATION.md`.
4. `06_WORKFLOWS.md`, `07_SYSTEM_ARCHITECTURE.md`, `08_DATABASE_AND_API_DESIGN.md`.
5. `09_IMPLEMENTATION_ROADMAP.md`, `10_TESTING_AND_EVALUATION.md`, `11_PRIVACY_SAFETY_AND_ETHICS.md`, `12_UI_UX_GUIDELINES.md`, `13_ACCEPTANCE_CRITERIA.md`, `14_OPEN_DECISIONS.md`.
6. `CODEX_KICKOFF_PROMPT.md` and `PROJECT_STATUS_TEMPLATE.md`.

All six application modules are mandatory project requirements. Their documentation is not evidence of implementation. Read the master plan and continue through eligible phases in dependency order under the current continuous-execution authorization. If a phase is externally blocked, document that dependency and proceed with independent eligible work. Do not invent records, labels, dates, decisions, or results.
