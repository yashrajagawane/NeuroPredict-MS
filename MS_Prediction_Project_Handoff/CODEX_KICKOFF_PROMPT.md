# Codex Kickoff Prompt — NeuroPredict-MS

You are assisting with the final-year research project **Deep Learning Approach for Prediction of Multiple Sclerosis Using Hybrid RNN–LSTM**.

Before any work, read the root `PROJECT_MASTER_PLAN.md`, this handoff pack, existing code/data/tests/reports, and Git status. The root master plan is the single source of truth for phase order, dependencies, status, and acceptance. Execute one phase at a time and continue automatically through eligible phases under the current user authorization; do not pause for approval between phases.

## Confirmed project decisions

- **Research target:** future conversion from confirmed CIS to MS using genuine longitudinal patient records. This is not cross-sectional MS/Non-MS classification. Operational index/horizon/cohort/criteria still require suitable data and clinical review.
- **Mandatory deliverables:** an evidence-based ML research pipeline and a doctor-facing app with all six modules: (1) authentication/authorization, (2) pseudonymous patient management, (3) patient visit history, (4) approved clinical-data management, (5) gated research prediction, and (6) traceable prediction history/results.
- **Model:** proposed SimpleRNN → LSTM → Dense, compared with suitable baselines only if data support it.
- **Approved stack:** React/TypeScript/Vite/Tailwind/shadcn/ui/React Router/TanStack Query/React Hook Form/Zod/Recharts/Lucide; Python 3.12/FastAPI/SQLAlchemy/Alembic/Pydantic; Supabase PostgreSQL/Auth/RLS; Pandas/NumPy/scikit-learn/TensorFlow/Keras/Matplotlib/Seaborn; pytest, Git/GitHub, VS Code, Jupyter Notebook.
- **Approval:** the project owner has approved the two-part scope and six application modules. Do not claim supervisor approval. Record institutionally required review separately and require it before relevant real-data/clinical activity.
- **Safety:** research and education only; never diagnose or recommend treatment. Prediction remains unavailable until a valid tested versioned model and preprocessing are trained on approved data.

## Current data and blockers

The Mexican and Lithuanian public cohorts are separate interim datasets without the patient-linked repeated dated visits, conversion dates, and adequate follow-up required by the intended future-outcome task. They have zero approved model features and zero valid fixed-horizon labels. Keep the supervised-training NO-GO. Never fabricate or duplicate patients, visits, dates, labels, or predictions.

Do not expose direct identifiers or secrets. Do not upload restricted health records to unapproved tools/cloud services. Keep patient access behind authorized backend operations and database RLS. Keep model training separate from inference.

## Execution rules

1. Resume only the next eligible master-plan phase; never repeat accepted phases or skip a prerequisite.
2. If clinical, data-owner, ethics, governance, or supervisor input blocks a phase, record the exact blocker and continue with the next independent eligible phase. Do not claim approval without evidence.
3. Preserve current source data and user changes. Implement only the selected phase.
4. Run and report relevant checks honestly. Update tracker evidence and change log.
5. Commit/push each genuinely completed phase with a meaningful message; stage only phase-related files. Never force-push or stage unrelated/sensitive files. A blocked phase is not reported as complete.
6. After each completed phase is pushed, report files, tests, acceptance, commit/push status, and next eligible phase; continue automatically if dependencies permit. If blocked, record the dependency and continue independently.
