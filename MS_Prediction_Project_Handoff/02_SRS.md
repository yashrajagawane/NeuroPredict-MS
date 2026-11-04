# 02 — Software Requirements Specification (SRS)

## 1. Purpose and system context

Specify the mandatory research pipeline and doctor-facing web application for future CIS-to-MS conversion research. The system consists of a React/TypeScript client, FastAPI application/API, SQLAlchemy persistence layer, and Supabase PostgreSQL with Supabase Auth and RLS. Offline model training remains separate from API inference. No clinical prediction is currently available.

## 2. Actors

- **Doctor / authorized user:** authenticated application user authorized to manage pseudonymous patient and visit records and request a prediction only when its gate is satisfied.
- **Researcher / administrator:** authorized technical role for data quality, model metadata, and approved research operations. Exact role matrix and account provisioning policy require governance/design review.
- **ML pipeline operator:** runs offline validation, patient-level splitting, preprocessing, training, and evaluation against permitted data.

## 3. Functional requirements and acceptance evidence

| ID | Requirement | Acceptance evidence |
|---|---|---|
| FR-01 | The system shall authenticate doctor users through Supabase Auth and provide secure logout/session handling. | Valid login succeeds; invalid credentials fail safely; logout invalidates access as designed. |
| FR-02 | The system shall enforce role authorization on protected routes and every backend operation. | Unauthenticated and unauthorized route/API tests are denied; RLS prevents cross-role/tenant access under the approved policy. |
| FR-03 | The system shall register, retrieve, search, and update permitted patient records using unique pseudonymous identifiers. | Duplicate IDs are rejected; patient records contain no direct identifiers; authorized CRUD and denied-access tests pass. |
| FR-04 | The system shall associate visits to exactly one patient and display actual visits in chronological order. | Foreign-key, missing-patient, duplicate-visit, repeated-date, and ordering tests pass. |
| FR-05 | The system shall accept only approved clinical fields and preserve their source meaning, measurement time, and units. | Schema/type/range/unit/date tests reject malformed values and report missing/unassessed values without converting them to zero. |
| FR-06 | The system shall accept a prediction request only for eligible history and a compatible, validated, versioned model/preprocessor. | With no model, incompatible schema, or insufficient history, API returns an explicit unavailable/error state and no predicted class. |
| FR-07 | The system shall show actual research results with the model version, request/result timestamp, limitations, and research-only disclaimer. | A compatible test artifact returns a traceable result; every response includes disclaimer and version metadata. |
| FR-08 | The system shall retain and retrieve prediction history and appropriate audit metadata without fabricating prediction results. | History is patient-linked and authorized; request, unavailable, and successful-result states are distinguishable; audit metadata is traceable. |
| FR-09 | The research pipeline shall validate source, schema, values, dates, labels, duplicates, and leakage before modeling. | Reproducible reports include cohort counts, missingness, label/follow-up status, chronology, exclusions, and leakage findings. |
| FR-10 | The pipeline shall split by patient and fit learned preprocessing on training patients only. | Automated tests show no patient overlap and no validation/test influence on fitted transforms. |
| FR-11 | The pipeline shall build chronological sequences only from genuine eligible visits preceding the index. | Sequence tests preserve real ordering/timing and exclude post-index observations; current interim cohorts are refused. |
| FR-12 | The pipeline shall compare appropriate baselines with the proposed SimpleRNN → LSTM → Dense model only if data support it. | Experiment record uses the same patient partitions, locked test set, model version, and suitable metrics. |
| FR-13 | The system shall clearly state when research prediction is unavailable and shall not substitute a fabricated class. | Missing model, invalid inputs, insufficient visits, authorization failure, and database failure return safe explicit states. |

## 4. Six mandatory application modules: responsibilities and checks

### APP-01 — Doctor login and authentication

- **Workflow:** doctor signs in → session is established → protected app is available → doctor signs out.
- **Backend:** validate Supabase Auth credentials/tokens; enforce authorization on all endpoints; never trust frontend-only route guards.
- **Database:** use Supabase Auth identity and approved role/authorization metadata; do not create a second password store without a reviewed design.
- **Security:** least privilege, secure session/token handling, no secrets in browser bundles, safe auth errors, RLS and backend policy checks.
- **Validation/tests:** valid/invalid credentials, expired/revoked session, logout, protected route, role denial, and cross-user record access.
- **Acceptance:** unauthenticated/unauthorized users cannot access patient or prediction data; an authorized doctor can access only approved functions.

### APP-02 — Patient registration and management

- **Workflow:** authorized doctor registers a patient → system assigns/validates a unique pseudonymous ID → doctor searches/views/updates permitted fields.
- **Backend:** validate schemas, enforce uniqueness and field-level permissions, apply auditable updates.
- **Database:** one patient record per pseudonymous key; constrain uniqueness and preserve created/updated timestamps. Final fields depend on approved data minimization rules.
- **Security:** reject direct identifiers unless a future approved requirement explicitly permits them; scope every read/write by authorization.
- **Validation/tests:** duplicate ID, malformed fields, prohibited identifiers, unauthorized CRUD, search filtering, and update/audit tests.
- **Acceptance:** authorized users can perform permitted operations; identifiers remain pseudonymous and unique; no unauthorized record is disclosed.

### APP-03 — Patient visit history

- **Workflow:** doctor selects a patient → adds genuine dated visit → reviews visits chronologically.
- **Backend:** confirm patient exists and is accessible; validate visit relationships/dates; return stable chronological order including documented same-date behavior.
- **Database:** visits reference one patient with enforced foreign key; retain visit timestamp and source/record metadata as approved.
- **Security:** authorize each visit through its parent patient; do not permit IDOR or cross-patient reads/writes.
- **Validation/tests:** invalid date, future/impossible chronology according to approved rule, duplicate visit, missing patient, repeated date, and chronological sorting.
- **Acceptance:** only real observations are saved; linked visits are returned in correct order; no generated or duplicated visit is presented as genuine.

### APP-04 — Clinical data management

- **Workflow:** doctor enters or updates approved clinical/MRI-related structured measurement with its actual measurement date and unit → validation results are shown → valid record is saved.
- **Backend:** validate the source-approved schema, units, ranges, categories, timing, and missingness state; preserve audit history where authorized.
- **Database:** store each value at its genuine patient/visit/measurement grain; use source-specific fields only after the data dictionary and governance are approved.
- **Security:** enforce role- and patient-scoped access; minimize stored data; exclude data from logs/errors.
- **Validation/tests:** unit conversion only under a documented rule; invalid range/category/date; missing versus not-assessed distinction; immutable provenance; authorized access.
- **Acceptance:** data meaning, time, and units are preserved; invalid values are rejected with actionable feedback; unsupported features are not invented.

### APP-05 — Research prediction interface

- **Workflow:** doctor requests a prediction → backend checks authorization, patient history, feature timing and model compatibility → if all gates pass, inference runs → result or explicit unavailable reason is returned.
- **Backend:** FastAPI retrieves permitted records, applies the matching saved preprocessing/model, records actual status and returns version/timestamp/disclaimer. Training is never run in the request path.
- **Database:** link a request/result to the pseudonymous patient and model version; store no predicted label for unavailable/failed inference. Exact result schema is subject to model/output approval.
- **Security:** authorize request and patient scope; validate payload; prevent arbitrary tensor submission; protect artifacts and credentials; audit access without logging clinical payloads.
- **Validation/tests:** no model, incompatible artifact/schema, insufficient genuine pre-index visits, invalid fields, post-index input, denied role, timeout, and successful compatible artifact.
- **Acceptance:** prediction is unavailable until approved clinical data and a valid, tested, versioned model/preprocessor exist; no failure path invents a class; every actual result carries research-only limitations.

### APP-06 — Prediction history and results

- **Workflow:** authorized doctor opens patient history → views actual prior requests/results in time order with status and model version.
- **Backend:** retrieve patient-scoped records, distinguish completed prediction from unavailable/failed request, enforce retention and audit rules.
- **Database:** prediction/request record references patient and authenticated actor as permitted; contains timestamp, status, actual result only when generated, model/preprocessing version, and audit fields.
- **Security:** least privilege, RLS, tamper-aware audit policy, data minimization, retention/deletion rules, and no sensitive data in logs.
- **Validation/tests:** patient association, timestamp, artifact version, denied cross-user reads, no-result status, retention/deletion policy, and audit event correctness.
- **Acceptance:** history contains only real system events/results and is traceable to the correct patient, time, actor scope, and model version; no fabricated output is shown.

## 5. Non-functional requirements

- **Correctness:** reject malformed, unsupported, or incomplete inputs instead of guessing.
- **Privacy/security:** pseudonymous records, authenticated least-privilege access, backend authorization, RLS, secure secrets, and approved retention.
- **Research integrity:** no prediction without valid target/model; no post-index leakage; no unsupported performance or clinical claims.
- **Reproducibility:** record dataset release/hash, schema, split seed, preprocessing, model version, and software versions without exposing restricted data.
- **Maintainability:** separate frontend, API, persistence, offline ML training, and inference contracts.
- **Usability/accessibility:** keyboard-accessible workflows, clear validation and unavailable states, legible timeline, persistent research disclaimer.
- **Portability/performance:** document local setup; set performance targets only after actual workload and hosting are known.

## 6. Error handling

Return safe, actionable errors for authentication/authorization failure, invalid schema/value/date, missing patient/visit, duplicate record, insufficient history, no/incompatible model, and database/service failure. Do not expose patient values or internals in error messages/logs, and never replace an error with a predicted class.

## 7. Technology and implementation status

Use the approved React/TypeScript/Vite frontend, Python 3.12/FastAPI backend, SQLAlchemy/Alembic persistence, Supabase PostgreSQL/Auth/RLS, and approved Python ML stack listed in the root master plan. These are decisions, not evidence of implementation. The application, database, and trained model have not been built.
