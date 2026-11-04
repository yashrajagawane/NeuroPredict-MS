# 03 — Scope, Assumptions, and Constraints

## Confirmed project scope

### Research component

- Predict future conversion from confirmed CIS to MS using genuine longitudinal clinical records, where cohort, dates, outcomes, permissions, and follow-up support the task.
- Validate source provenance, schema, clinical meaning, missingness, chronology, labels, censoring, and leakage.
- Use patient-level partitions and train-only learned preprocessing.
- Compare suitable classical baselines and the proposed SimpleRNN → LSTM → Dense model only if the data support genuine sequences.
- Report evidence and limitations without claims of clinical validation or a guaranteed performance threshold.

### Mandatory doctor-facing application

The final project must deliver all six modules: (1) doctor login/authentication and role authorization; (2) pseudonymous patient registration and management; (3) patient-linked chronological visit history; (4) source-approved clinical and structured MRI-related data management with measurement dates/units; (5) gated research prediction through FastAPI; and (6) traceable prediction history/results with timestamps, patient association, model version, and audit metadata.

Approved architecture: React + TypeScript frontend → FastAPI → SQLAlchemy → Supabase PostgreSQL, with Supabase Auth and PostgreSQL RLS. Offline training is separate from API inference. See root `PROJECT_MASTER_PLAN.md` for the approved technology stack and phase sequence.

## Out of scope

- Clinical diagnosis, treatment recommendations, automated care decisions, or representation as a medical device.
- Cross-sectional MS/Non-MS classification as a substitute for future CIS-to-MS conversion.
- Raw MRI image processing, lesion segmentation, or unsupported clinical feature creation.
- Fabricated/duplicated patients, labels, dates, observations, or prediction results.
- Training or prediction on current public interim cohorts for the intended future-conversion task.
- Real-patient use, production deployment, or cloud storage before data-owner, ethics, privacy, security, and institutional approval.
- Claims of clinical benefit, clinical validity, fairness, or generalizability without suitable evidence.

## Current evidence and assumptions

1. The Mexican and Lithuanian public datasets are separate interim cohorts; neither contains the required patient-linked repeated dated visits, conversion dates, and adequate individual follow-up.
2. A future approved source must supply pseudonymous patient linkage, actual observations, documented clinical definitions, units, timing, and outcome/follow-up evidence.
3. The exact index date, horizon, minimum eligible history, diagnostic-criteria version, and adjudication rules remain open pending data feasibility and clinical review.
4. Patient IDs are pseudonymous and never model features. No direct identifiers are required by this project scope.
5. Patient and visit fields depend on the approved source. Do not assume every proposed MRI/CSF feature exists or is suitable.
6. Research prediction remains disabled until a validated compatible versioned model and preprocessing artifact are available.
7. Doctor-facing workflows are product requirements; the existence of a “doctor” role does not mean clinicians have approved the system or will use it in care.
8. Project-owner approval of the charter scope is recorded. Any institutionally required supervisor/ethics/data-owner approval before real clinical data use remains a separate governance item; no supervisor approval is claimed.

## Constraints and change control

- Keep every patient's observations in one evaluation partition; exclude post-index data from model input.
- Unknown or insufficiently followed outcomes cannot be labelled negative.
- Never select an index/horizon to optimize observed performance; justify and document it using cohort follow-up and clinical input.
- Keep model training outside the inference API. No model training until the master-plan data/clinical gates pass.
- Do not expose Supabase service-role keys or database credentials in client code.
- A target, data source, model family, mandatory module, user role, or deployment change requires a documented user decision and updates to the PRD, SRS, data/model specification, architecture, and master plan.

## Acceptance boundary

Phase 01 documents the confirmed product/research scope and acceptance criteria and is accepted by the project owner. It does not authorize patient-data access, clinical use, model training, or deployment. Any institutionally required supervisor/ethics/data-owner approval remains a separate gate before real clinical-data use.
