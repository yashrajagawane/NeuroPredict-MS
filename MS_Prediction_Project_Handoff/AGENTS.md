# Instructions for Coding Agents

This repository supports a final-year research and educational project on future CIS-to-MS conversion prediction from genuine longitudinal patient records, plus a mandatory doctor-facing research web application. It is not a clinical diagnostic or treatment system.

## 1. Mandatory first steps

1. Read the root `PROJECT_MASTER_PLAN.md`; it is the single source of truth for phase order, dependencies, status, and progress.
2. Read this handoff pack and inspect actual repository files, data, tests, and Git status before acting.
3. Work on one phase at a time, but continue automatically through eligible phases under the current user authorization. Do not repeat completed phases or skip dependencies. If a phase is externally blocked, document it and continue independent eligible work.
4. Preserve existing work and report discrepancies; do not assume proposed files exist.
5. If an external clinical, data-access, ethics, governance, or supervisor decision blocks a phase, document that blocker and continue with the next independent eligible phase. Do not invent approval or evidence.

## 2. Source of truth and fixed decisions

Priority order:

1. Confirmed user instructions and approvals.
2. Root `PROJECT_MASTER_PLAN.md` for sequencing and phase state.
3. Current handoff requirements and verified data dictionaries/reports.
4. General engineering recommendations, labelled as recommendations.

The approved research target is future conversion from confirmed CIS to MS. The index date, prediction horizon, cohort eligibility, diagnostic-criteria version, and outcome adjudication still require suitable data and clinical review. Do not recast the task as cross-sectional MS/Non-MS classification.

The approved stack is React, TypeScript, Vite, Tailwind CSS, shadcn/ui, React Router, TanStack Query, React Hook Form, Zod, Recharts, Lucide React; Python 3.12, FastAPI, SQLAlchemy, Alembic, Pydantic; Supabase PostgreSQL, Supabase Auth, PostgreSQL RLS; Pandas, NumPy, scikit-learn, TensorFlow/Keras, Matplotlib, Seaborn; pytest, Git/GitHub, VS Code, and Jupyter Notebook. Do not introduce another frontend framework, backend framework, or primary database without discussing it first.

The web application is a mandatory final deliverable with six modules: (1) doctor authentication/authorization; (2) pseudonymous patient registration and management; (3) chronological patient visit history; (4) approved clinical data management; (5) gated research prediction; and (6) prediction history/results with model-version and audit metadata.

## 3. Data and model integrity

- Current Mexican and Lithuanian public interim cohorts are separate and are not valid future-conversion training cohorts. Preserve the documented NO-GO until a suitable, permitted longitudinal cohort passes review.
- Never fabricate, duplicate, or synthesize clinical patients, visits, dates, labels, or prediction results. Synthetic fixtures may test software only and must be unmistakably labelled.
- Never use patient or visit identifiers as model features. Do not use conversion dates, final diagnosis, post-index observations, or future follow-up information as predictors.
- Unknown or insufficiently followed outcomes are not Class 0. Do not select a horizon without cohort follow-up evidence and clinical justification.
- Split by patient; fit imputation, scaling, encoding, and feature selection on training patients only.
- Preserve source values and provenance. Do not silently remove, recode, or impute clinical values.
- Do not train until the target, index, horizon, cohort, features, permissions, and leakage checks pass the master-plan gates.

## 4. Application security and safety

- The UI/API must state: “Research prediction only — not a medical diagnosis. Do not use this result to make treatment decisions.”
- Keep prediction unavailable when the model is missing, unvalidated, incompatible, or the patient history is insufficient. Return a clear unavailable/error state rather than a guessed class.
- Use pseudonymous identifiers and least-privilege access. Protect routes and APIs; enforce authorization server-side and with approved PostgreSQL RLS policies.
- Never expose Supabase service-role keys, database credentials, or other secrets to frontend code, Git, logs, prompts, or screenshots.
- Do not upload restricted patient information to external tools or cloud services without explicit data-owner and institutional approval.
- The user requirement for a doctor-facing application does not itself establish clinician approval, authorization to access real records, or hosting permission.

## 5. Engineering and delivery

- Keep dataset preparation, model training, inference, API, persistence, and UI concerns separate. Training is offline; FastAPI serves only a validated, versioned artifact and matching preprocessing.
- Prefer typed, readable, modular code with focused tests. Add validation for data contracts, chronology, leakage, patient-level splits, authorization, API failures, and model compatibility when those phases become eligible.
- Use environment configuration for secrets; pin compatible dependencies when environment work is authorized. Use Alembic for database schema changes.
- At phase end, report changed files, exact checks and results, acceptance criteria, unresolved blockers, and actual implementation status. Commit and push only work that satisfies the phase’s completion criteria; otherwise follow the master-plan approval rules for partial work.
