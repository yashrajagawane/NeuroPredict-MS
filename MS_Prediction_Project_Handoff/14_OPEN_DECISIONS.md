# 14 — Open Decisions and Questions

These questions must be answered before finalizing the dataset and model. Do not let a coding agent guess.

## Blocking decisions

### D-01 — Dataset source
- Which exact dataset will be used?
- Is it public, licensed, controlled-access, institutional, or synthetic?
- What are the terms of use and permissions?
- Where is the dataset stored? Do not include sensitive data in public agent workspaces.

**Research update (2026-11-04):** The official public Mexican and Lithuanian
Mendeley workbooks are CC BY 4.0 and were acquired/audited. Separate,
source-preserving interim extracts were created locally, but neither source
has patient-linked dated visits, conversion dates, or last-follow-up dates.
The Mexican group mapping remains unverified; the Lithuanian final-MS flag is
an untimed final-diagnosis grouping. Neither is selected as the final
recurrent-model dataset. An approved MSBase/MSBasis feasibility request is
recommended; OFSEP is a secondary controlled-access route. See
[source_evidence_ledger.md](../data/reports/source_evidence_ledger.md).

### D-02 — Research objective — RESOLVED; operational target remains open

**User-confirmed objective:** Predict future conversion from confirmed CIS to MS using genuine longitudinal clinical records. This is not cross-sectional MS/Non-MS classification. Index date, horizon, eligibility, criteria version, and adjudication remain unresolved under D-03 until supported by a suitable approved cohort and clinical review.

### D-03 — Operational event, index, and horizon
- Which approved source and clinical evidence confirm baseline CIS and subsequent MS conversion?
- Which diagnostic criteria/version and event-date rule apply?
- Is prediction made at CIS diagnosis or a later landmark, and what information is eligible at that index?
- Which evidence-based horizon is supported by available follow-up?
- How are uncertain diagnosis, competing events, missing follow-up, and censoring handled?

**Current evidence:** Do not assign a future-conversion label from either
public workbook. Mexican group codes remain unlabelled. The Lithuanian final-MS
flag is retained only as a documented descriptive grouping, never as a
fixed-horizon conversion label. The future contract requires confirmed CIS
at/preceding index, conversion date and diagnostic criteria for Class 1, last
follow-up through the horizon for Class 0, and separate unknown/censored
statuses.

### D-04 — Longitudinal structure
- Does each patient actually have multiple time-stamped observations?
- How many patients and visits are available?
- Are visits irregularly spaced?
- What minimum number of visits is required?

**Current evidence:** The two acquired public workbooks have no repeated dated
visits. A future recurrent-model cohort must have at least two genuine dated
pre-index observations per included patient; a controlled-access feasibility
report must quantify visit and follow-up distributions before the landmark and
horizon are selected.

### D-05 — Feature list
- What exact columns are present?
- Which are static and which change per visit?
- Which values are available at the prediction time?
- Which variables could reveal the outcome after the index time?
- Are units and allowed ranges documented?

**Current evidence:** Source mappings, missingness, and exclusions are recorded
in [feature_assessment_report.md](../data/reports/feature_assessment_report.md)
and the local `data/processed/interim/source_to_processed_mapping.csv`. Final
EDSS, final diagnosis, and any post-index observation are prohibited as input.
The public MRI fields are location indicators rather than the requested serial
lesion counts; codebooks and individual measurement timing also remain
incomplete.

## Product and implementation decisions

### D-06 — Application requirement — RESOLVED

**User decision:** A doctor-facing web application is a mandatory final deliverable alongside the ML research component. It must include all six modules: doctor login/authentication; patient registration/management; patient visit history; clinical data management; gated research prediction; and prediction history/results. This decision does not constitute implementation, supervisor approval, clinician endorsement, or permission to use real patient data.

### D-07 — Frontend and backend — RESOLVED

**User-approved stack:** React + TypeScript + Vite and the approved React libraries; Python 3.12 + FastAPI + SQLAlchemy + Alembic + Pydantic. Do not substitute Flask, Django, or another frontend/backend framework without discussing the change first.

### D-08 — Database and identity — RESOLVED AT STACK LEVEL

**User-approved stack:** Supabase PostgreSQL, Supabase Auth, PostgreSQL RLS. Exact roles/claims, RLS policies, data residency, and schema remain to be designed and approved before implementation or real-record use.

### D-09 — Authentication and roles — SCOPE RESOLVED; POLICY DETAILS OPEN

Doctor login/logout, authenticated sessions, role authorization, and protected routes/APIs are mandatory requirements. The role matrix, account provisioning, session policy, and patient-level authorization need detailed design and security review.

### D-10 — Deployment and data hosting — OPEN

Will the final application run locally, in an institution-controlled environment, or be hosted? Supabase/cloud suitability, data residency, retention, backup, and institutional approval must be confirmed before restricted or real patient data is stored.

### D-11 — Prediction output semantics — PARTLY OPEN

The target is future CIS-to-MS conversion, with Class 1 requiring confirmed conversion in the approved horizon and Class 0 requiring adequate follow-up. The index, horizon, label adjudication, threshold, probability calibration, and exact display policy remain open. Do not show a probability as personal risk unless separately validated and approved.

### D-12 — Model choice — ARCHITECTURE CONFIRMED; TRAINING CONDITIONAL

The proposed experiment is SimpleRNN → LSTM → Dense, with appropriate classical baselines. Training remains NO-GO until data, target, index, horizon, feature timing, permissions, and evaluation gates pass. A no-go recommendation remains appropriate if the available data do not support a sequence model.

## Agent instruction

Resolve blocking decisions using available documentation and user/supervisor direction. Do not manufacture answers. If an answer is unavailable, record it as unresolved and work only on non-blocked tasks (e.g., repository scaffolding, schema-independent tests, or synthetic UI examples clearly marked as demo data).
