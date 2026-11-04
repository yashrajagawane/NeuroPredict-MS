# Approved Technology Stack — Decision Record

**Project:** Deep Learning Approach for Prediction of Multiple Sclerosis Using Hybrid RNN–LSTM

**Status:** Approved by the user; requirements only, not evidence of implementation

**Authoritative roadmap/context:** [`PROJECT_MASTER_PLAN.md`](../PROJECT_MASTER_PLAN.md)

This decision supersedes the earlier read-only stack recommendation previously stored in this file. Do not use its historical Flask/Jinja/SQLite or “React/PostgreSQL later” alternatives as project implementation choices.

## Approved stack

| Layer | Approved technologies |
|---|---|
| Frontend | React, TypeScript, Vite, Tailwind CSS, shadcn/ui, React Router, TanStack Query, React Hook Form, Zod, Recharts, Lucide React |
| Backend | Python 3.12, FastAPI, SQLAlchemy ORM, Alembic, Pydantic |
| Database and authentication | Supabase PostgreSQL, Supabase Auth, PostgreSQL Row Level Security (RLS) |
| Data and ML | Pandas, NumPy, scikit-learn, TensorFlow, Keras, Matplotlib, Seaborn |
| Development and testing | pytest, Git, GitHub, VS Code, Jupyter Notebook |

## Architecture

```text
React + TypeScript frontend
        ↓
FastAPI backend
        ↓
SQLAlchemy ORM
        ↓
Supabase PostgreSQL with RLS and Supabase Auth
```

The offline ML training pipeline remains separate from the application backend. FastAPI may provide inference only after a valid, tested, versioned model and matching preprocessing artifact have been developed from an approved cohort.

## Security and scope constraints

- Do not introduce MongoDB, Flask, Django, Next.js, or another primary database/backend/frontend framework without discussing the change first.
- Never expose Supabase service-role keys, database credentials, or other secrets in frontend code, public environment variables, Git, or logs.
- Keep patient-data access behind authorized backend operations and appropriate database RLS policies.
- The doctor-facing application is a mandatory final deliverable with six modules, but no application, database schema, or model has been implemented yet.
- Real patient data and hosting require separate source, ethics, privacy, and institutional approvals.
- The current public interim data do not support supervised future CIS-to-MS training; preserve the NO-GO decision.
