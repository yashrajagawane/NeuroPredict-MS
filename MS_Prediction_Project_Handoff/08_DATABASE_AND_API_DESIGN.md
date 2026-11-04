# 08 — Database and API Requirements

This is a requirements-level design for the mandatory application, not a migration plan or implemented schema. Final clinical fields depend on the approved cohort and data dictionary. Real patient records remain prohibited until data-governance and security approvals are in place.

## 1. Approved persistence and identity stack

- Supabase PostgreSQL is the application database; SQLAlchemy is the ORM and Alembic manages later schema changes.
- Supabase Auth provides doctor identity and sessions. Role assignment/provisioning must be an approved server-side policy; do not create a parallel password table.
- PostgreSQL Row Level Security (RLS) and FastAPI authorization protect every patient-linked operation. A frontend guard alone is insufficient.
- Never expose Supabase service-role keys or database credentials in React code or a public environment variable.

## 2. Conceptual entities

### `patients`

One record per pseudonymous patient. Require a unique opaque `patient_id` and only approved patient-level fields. Prohibit names, contact data, MRNs, and direct identifiers unless a future governance-approved requirement explicitly changes scope. Created/updated timestamps may be recorded.

### `visits` and structured measurements

Each genuine patient-linked observation has a unique visit/measurement key, foreign key to `patients`, actual observation date/time, visit type where known, and source-approved clinical values with units and measurement timing. Exact columns and whether measurements are normalized as visit child records depend on the approved source. Do not create visits or repeat static fields to simulate time.

### `prediction_requests` / `predictions`

Keep a traceable event for requests and results, with pseudonymous patient reference, authorized actor reference where permitted, request/result timestamp, status, model/preprocessing version, and approved audit metadata. Store a predicted label only for a real successful inference. Unavailable/failed requests must not contain a predicted label. Probabilities remain absent unless calibration and display policy are approved.

### `model_versions`

Store non-sensitive artifact/version metadata and compatibility information. Model binaries and preprocessors must be handled under approved storage controls; do not expose service paths or secrets.

### Identity and roles

Supabase Auth owns credentials and identity. Application roles/claims and their RLS mapping must be specified before database implementation. Avoid storing passwords in application tables.

## 3. Relationships and integrity

- One patient has many genuine visits/measurements.
- One patient can have many prediction-request events; successful results reference the exact model/preprocessing version.
- Each visit belongs to exactly one patient; enforce foreign keys and uniqueness rules.
- Actor-to-patient access must be checked in FastAPI and RLS policies; test cross-patient and unauthorized access.
- Preserve source identifiers only in restricted, permitted provenance fields; never use identifiers as model features.

## 4. Proposed API resource groups

All endpoints except health checks require authentication and authorization. Paths are conceptual and may be refined during backend design without changing the six mandatory modules.

| Method | Endpoint | Module / purpose |
|---|---|---|
| GET | `/api/health` | Operational health only; disclose no sensitive details. |
| GET/POST | `/api/patients` | Search/list permitted patients and register a pseudonymous patient. |
| GET/PATCH | `/api/patients/{patient_id}` | View/update permitted patient fields. |
| GET/POST | `/api/patients/{patient_id}/visits` | Retrieve chronologically or add a genuine dated visit. |
| GET/PATCH | `/api/patients/{patient_id}/measurements` | View/update approved structured measurements and timing. |
| POST | `/api/patients/{patient_id}/prediction-requests` | Request gated research inference; return unavailable if any gate fails. |
| GET | `/api/patients/{patient_id}/prediction-history` | Retrieve authorized actual request/result events. |
| GET | `/api/prediction-requests/{request_id}` | Retrieve one authorized event/result and its model version. |

## 5. Prediction API behavior

The client submits a request for a patient ID only; it must not send arbitrary preprocessed tensors or a fabricated target. FastAPI verifies caller role and patient scope, retrieves real permitted history, checks the index cutoff/schema/model compatibility, and invokes inference only when all gates pass.

Success response requirements: actual result from the loaded artifact, request/result timestamp, model and preprocessing versions, status, limitations, and the non-diagnostic disclaimer. Failure/unavailable response requirements: safe status and reason, no predicted class, no probability, and no sensitive payload in errors/logs. No example here represents a real patient or prediction.

## 6. Error and validation behavior

- `400` malformed request; `401` unauthenticated; `403` unauthorized; `404` inaccessible or missing resource with safe disclosure policy; `409` uniqueness/state conflict; `422` invalid schema/value/date or insufficient history; `503` model absent/unvalidated/incompatible or dependent service unavailable; `500` generic unexpected error.
- Validate all values, units, dates, allowed categories, foreign keys, and patient access server-side.
- Model unavailable, insufficient history, incompatible schema, denied access, or inference failure must never be replaced with a predicted class.
- Do not log clinical payloads, credentials, tokens, or direct identifiers.

## 7. Database/API acceptance gates

Before implementation, define the approved role matrix, data minimization, RLS rules, retention/deletion policy, audit metadata, source-specific schema, and deployment boundary. Later tests must cover uniqueness, patient/visit relationships, chronological reads, per-role authorization, cross-patient denial, invalid clinical values, no-model behavior, model-version traceability, and safe errors. No database tables or migrations are created in Phase 01.
