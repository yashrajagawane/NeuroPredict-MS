# 00 — Project Brief

## Working title

**Deep Learning Approach for Prediction of Multiple Sclerosis Using Hybrid RNN–LSTM**

## Objective and intended use

This final-year research project will investigate whether genuine, time-ordered clinical observations from patients initially diagnosed with Clinically Isolated Syndrome (CIS) can support prediction of subsequent confirmed conversion to Multiple Sclerosis (MS) within a future, clinically justified period. It is a research and educational prototype, not a diagnostic product or treatment decision system.

The operational index date, prediction horizon, cohort eligibility criteria, diagnostic-criteria version, and adjudication protocol are not yet established. The available public Mexican and Lithuanian datasets do not provide patient-linked dated visits, conversion dates, or adequate individual follow-up. They are not approved training cohorts. The project must preserve the current NO-GO for supervised training until a suitable cohort is approved and validated.

## Machine-learning research component

The required research component will, when data gates pass:

1. preserve provenance and validate an approved longitudinal cohort;
2. define the index, horizon, labels, and censored/unknown outcomes with clinical review;
3. prepare genuine patient-linked visits without fabricating observations;
4. split by patient and fit learned preprocessing on training patients only;
5. compare suitable classical baselines with the proposed **SimpleRNN → LSTM → Dense** model, only when genuine sequences support it; and
6. report patient-level evaluation, uncertainty, limitations, and reproducibility evidence.

The target is future CIS-to-MS conversion, not current MS/Non-MS status classification. No horizon, feature set, eligible cohort count, or performance result is currently approved.

## Mandatory doctor-facing web application

The final project must include these six modules:

1. Doctor login, logout, authenticated sessions, role authorization, and protected routes.
2. Patient registration and management using pseudonymous identifiers.
3. Patient visit history, linked to each patient and displayed chronologically.
4. Clinical data entry and management with source-approved fields, measurement dates, units, and validation.
5. Research prediction requests through FastAPI, enabled only after a valid, tested, versioned model exists; otherwise show a clear unavailable state.
6. Prediction history with actual request/result timestamps, patient association, model version, and appropriate audit metadata. Never fabricate results.

The app stack and architecture are fixed in the approved technology decision documented in the master plan: React/TypeScript frontend, FastAPI backend, SQLAlchemy, and Supabase PostgreSQL/Auth/RLS. Application requirements do not authorize handling real patient data before required governance approvals.

## Users and boundaries

- **Doctor/authorized user:** manages permitted pseudonymous records and, only when available, requests and reviews research predictions.
- **Student/researcher/administrator:** prepares approved research data, trains and evaluates models offline, and maintains documented versions.
- The doctor-facing interface must not claim clinical approval, diagnosis, treatment guidance, or validated clinical utility.
- No raw MRI image processing is in scope. MRI-derived structured measurements may be used only if supported by the approved source and data dictionary.
- The web app is mandatory; actual real-data use, hosting, and clinical workflow remain subject to security, ethics, and supervisor approval.

## Success criteria

The project is successful only when all applicable evidence exists:

- Approved data provenance, permitted use, cohort definition, and target protocol are documented.
- Genuine longitudinal sequences and label/follow-up rules pass validation without patient-level or temporal leakage.
- Baselines and the hybrid model, if data support it, use identical patient-level partitions and are reported with suitable class-wise metrics and limitations.
- The mandatory six-module application passes module, integration, access-control, validation, and failure-state acceptance tests.
- Prediction remains disabled when no compatible validated model is available; every actual result is traceable to its patient record, time, and model version.
- A clean, reproducible research handover is accepted by the project supervisor.

The aspirational 2,000-patient goal is not a success criterion that permits fabrication and does not by itself establish statistical adequacy. The project owner has approved this scope; no supervisor approval is claimed. Any institutionally required review for clinical research or real-data use remains a separate governance gate.
