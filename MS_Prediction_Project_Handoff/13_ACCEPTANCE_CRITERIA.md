# 13 — Definition of Done and Acceptance Criteria

These criteria specify the required evidence; they are not claims that features are implemented. The six web-application modules are mandatory final deliverables. Real-patient workflows remain gated on source and institutional approvals. Phase 01 is accepted by the project owner based on the updated development authorization. Do not claim supervisor approval; obtain any institutionally required approval before real-data or clinical activity.

## A. Project charter and research-scope acceptance

- [x] Project documents consistently state future CIS-to-MS conversion prediction from genuine longitudinal records; operational index/horizon remain pending.
- [ ] Index date, prediction horizon, cohort eligibility, diagnostic criteria, and label rules are operationally approved before model training.
- [x] Patient-level and temporal leakage rules, unknown/censored handling, and stop conditions are explicit.
- [x] The mandatory two-part deliverable (ML research component and doctor-facing app) and all six app modules are documented.
- [x] Project boundaries, success evidence, dependencies, decision owner, and change-control process are documented and project-owner scope approval is recorded.
- [ ] Any institutionally required supervisor/ethics/data-owner approval is recorded before the relevant clinical-data or deployment activity; it is not inferred from project-owner scope approval.

## B. Mandatory six-module application acceptance

Each module must pass its functional workflow, backend, database, security, validation, and test conditions. Database structures and field details must follow later approved data/governance decisions.

### APP-01 — Doctor login and authentication

- **Functional/workflow:** Doctor can sign in, maintain a valid session, access protected routes, and sign out.
- **Backend:** FastAPI verifies identity/session on every protected request and applies role authorization.
- **Database/identity:** Supabase Auth owns identity; approved role metadata maps to authorization policy; no plaintext password table.
- **Security:** Least privilege, safe session/token handling, protected transport; no service-role key or database credential in frontend.
- **Validation:** Invalid, expired, revoked, and malformed auth state is rejected safely.
- **Test scenarios:** Valid/invalid login, logout, expired session, protected route/API, role denial, and unauthorized patient request.
- **Acceptance:** Only authenticated authorized doctors can access assigned functions and records; failures disclose no sensitive information.

### APP-02 — Patient registration and management

- **Functional/workflow:** Authorized doctor registers a patient, receives a unique pseudonymous ID, searches/views permitted details, and updates allowed fields.
- **Backend:** Validate input, enforce unique identity and field permissions, authorize each operation, and record approved audit metadata.
- **Database:** Patient primary key is pseudonymous/opaque and unique; direct identifiers are excluded; timestamps and permitted static fields follow approved schema.
- **Security:** Patient-scoped authorization and RLS; no IDOR or cross-user record access.
- **Validation:** Duplicate IDs, direct identifiers, malformed/out-of-range fields, and unauthorized updates are rejected.
- **Test scenarios:** Create/read/search/update, duplicate key, prohibited field, role denial, cross-patient access, and audit event.
- **Acceptance:** Permitted patient management works for authorized users; no direct identifiers or unauthorized records are exposed.

### APP-03 — Patient visit history

- **Functional/workflow:** Doctor selects a patient, adds a genuine dated visit, and reviews the patient’s visits in chronological order.
- **Backend:** Verify parent patient access, validate visit date and relationship, and return deterministic chronological ordering.
- **Database:** Visit references exactly one patient; enforce foreign keys and approved uniqueness rules; preserve actual visit time and provenance.
- **Security:** Inherit patient-level access controls for every visit read/write; prevent cross-patient access.
- **Validation:** Invalid/missing patient, invalid date, duplicate visit, repeated date, and impossible chronology follow documented rules.
- **Test scenarios:** Correct linkage, missing parent, duplicate, out-of-order input, same-date ordering, and denied read/write.
- **Acceptance:** Only genuine source/clinical visits are represented; no artificial repeated visits; timeline ordering and patient linkage are correct.

### APP-04 — Clinical data management

- **Functional/workflow:** Doctor enters/updates approved clinical or structured MRI-related measurement and can inspect its actual measurement date and unit.
- **Backend:** Enforce source-specific field schema, allowed values, units, dates, missingness state, and role permissions.
- **Database:** Store at the correct patient/visit/measurement grain with actual timing, units, and provenance; final fields are data-dictionary dependent.
- **Security:** Minimize data, restrict per-patient access, and exclude clinical payloads from logs and public artifacts.
- **Validation:** Reject unsupported columns, invalid range/category/unit/date, and incompatible timing; distinguish missing/not-assessed from zero.
- **Test scenarios:** Valid record, invalid unit/range/category/date, missingness semantics, measurement timing, provenance, and unauthorized access.
- **Acceptance:** Values and clinical meaning are preserved and traceable; no unsupported or fabricated clinical feature is stored.

### APP-05 — Research prediction interface

- **Functional/workflow:** Authorized doctor requests a prediction; the app validates patient-history eligibility and shows either a genuine model result or a clear unavailable reason.
- **Backend:** FastAPI retrieves authorized records, excludes post-index inputs, applies matching versioned preprocessing, calls inference only (never training), and returns result metadata.
- **Database:** Link request and actual successful result to patient, timestamp, and model/preprocessing version; no predicted label on unavailable/failed requests.
- **Security:** Authorize patient and role, reject arbitrary client-supplied tensors/labels, protect artifacts/secrets, and log only approved audit metadata.
- **Validation:** Require approved cohort/model/schema compatibility and adequate genuine pre-index history; reject post-index or invalid measurements.
- **Test scenarios:** No model, incompatible artifact/schema, insufficient visits, post-index input, invalid data, denied caller, inference failure, and compatible approved test artifact.
- **Acceptance:** Prediction stays unavailable until data and a valid tested/versioned model pass required gates; a real result includes limitations and disclaimer; no failure path fabricates a class or probability.

### APP-06 — Prediction history and results

- **Functional/workflow:** Authorized doctor opens patient history and reviews actual request/result events with status, time, and model version.
- **Backend:** Return patient-scoped events in chronological order and distinguish successful results from unavailable/failed requests.
- **Database:** Store only actual events; include patient association, request/result timestamp, authorized actor reference where allowed, status, model/preprocessing version, and approved audit metadata.
- **Security:** RLS and server authorization apply; retention/deletion, audit integrity, and access policy are defined before real data use.
- **Validation:** Enforce patient/model-version references, timestamps, status consistency, and no result value for unavailable/failed events.
- **Test scenarios:** Successful result, unavailable state, duplicate request handling if specified, correct patient/version, cross-patient denial, and retention/audit policy.
- **Acceptance:** History is accurate, traceable, and access-controlled; it never displays fabricated prediction output.

## C. Data readiness

- [ ] Dataset provenance and permitted use are documented.
- [ ] Confirmed baseline CIS, index, horizon, outcome source, diagnostic criteria, and positive class are documented.
- [ ] Genuine repeated dated visits and patient linkage are verified.
- [ ] Class 1 conversion date is confirmed after index and within horizon; Class 0 has adequate follow-up through horizon.
- [ ] Unknown/censored outcomes are retained separately, not forced into Class 0.
- [ ] Feature dictionary, missingness, data quality, outliers, and leakage review are accepted.
- [ ] Patient-level split is implemented and overlap-tested.

## D. ML pipeline

- [ ] Preprocessing is fitted on training patients only.
- [ ] Sequence generation preserves genuine chronology and excludes post-index observations.
- [ ] Suitable baselines are trained and compared on the same patient partitions.
- [ ] Hybrid SimpleRNN → LSTM is trained only if data support it and gates pass.
- [ ] Final evaluation uses an untouched patient-level test set.
- [ ] Positive class, threshold, class-wise metrics, uncertainty and limitations are reported.
- [ ] Model and preprocessing artifacts are versioned together.
- [ ] Results can be reproduced from documented source/data version and configuration.

## E. Documentation and final handover

- [ ] Setup instructions work from a clean environment.
- [ ] Application routes, role policy, data model, API, workflows, and six modules match implementation.
- [ ] All tests and validation checks are run and results recorded honestly.
- [ ] Screenshots/demo use only permitted non-sensitive data, clearly labelled synthetic if applicable.
- [ ] No unsupported performance, clinical utility, fairness, or deployment claims are made.
- [ ] Supervisor accepts the final project and research-only limitations are visible.
