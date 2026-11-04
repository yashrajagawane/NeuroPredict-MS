# Remaining Phase Dependency Reassessment

**Reviewed:** 2026-11-05
**Baseline:** Project state including successful hosted validation at `a525779` and subsequent provisional Phase 55/58/60 design slices
**Scope:** Identify safe, independent work slices without weakening clinical, governance, or model-readiness gates.

## Decision

Phase 02 and Phase 25 remain genuine blockers for an operational future-conversion target, approved cohort, clinical training, evaluation, and inference. They do not block provisional application design, test-only utility checks, an empty service foundation, or a static research-only UI foundation. Those slices must be explicitly separated from live patient-data features and cannot be reported as clinically usable.

Project-owner authorization confirms the doctor-facing application and its six modules. It also permits provisional schemas, forms, API contracts, and non-sensitive demonstration flows. It does not approve data access, clinical definitions, a live database, user roles, retention, hosting, or clinical use.

## Phase-by-phase disposition

| Phase | Current state | Work that can proceed independently | Gate that remains |
|---|---|---|---|
| 02 Research target | BLOCKED (50%) | Maintain target requirements and access requests. | Dated eligible cohort and clinician review needed to select index/horizon and operational labels. |
| 03 Workflow/intended use | IN PROGRESS (25%) | Draft a safe, provisional review and unavailable-prediction workflow from the approved six-module scope. | Representative-user review and finalized target semantics remain open. |
| 04 Index/horizon | BLOCKED | None beyond documenting options. | Patient-level follow-up/event distributions and clinical/statistical approval. |
| 05 Endpoint adjudication | BLOCKED | Prepare reviewer questions or SOP outline. | Clinician/PI review and approved source/criteria. |
| 07 Data access | BLOCKED | Existing access-request specification may be maintained. | Data-owner response, permitted use and collaboration route. |
| 08 Ethics/governance | BLOCKED | Prepare governance questions and data-flow diagrams. | Institutional and source approvals; no live health-data storage. |
| 10 Data acquisition | BLOCKED | Continue source feasibility research. | Approved suitable longitudinal cohort. |
| 13 Cohort rules | BLOCKED | Draft rule candidates only. | Target, source, and clinical inclusion decisions. |
| 14 Outcome labels | BLOCKED | Preserve validator rules and ambiguity handling. | Approved horizon, criteria, and adjudicated outcomes. |
| 15 Follow-up/censoring | BLOCKED | Test generic censoring logic only with test-only fixtures. | Real patient follow-up and approved outcome rules. |
| 17 Feature approval | BLOCKED | Keep feature candidates documented. | Approved source mapping, timing, and clinical review. |
| 20 Cleaning/harmonization | BLOCKED | Improve source-agnostic validation utilities. | Compatible source dictionaries, units, and approved cohort. |
| 21 Missingness/outliers | BLOCKED | Document candidate methods only. | Final cohort and train-only policy; no fitted transformations now. |
| 22 Sequence design | BLOCKED | Test guards on clearly synthetic software fixtures. | Genuine repeated dated observations and approved target. |
| 23 Sample/event feasibility | BLOCKED | None for the intended prediction task. | Eligible cohort/event/follow-up counts. |
| 24 Dataset freeze | BLOCKED | Current public-source manifests remain valid for interim data only. | Approved cohort release and governance. |
| 25 Evaluation/splits | BLOCKED | Test split utility reproducibility and patient non-overlap in memory only. | Approved label protocol, sample/event counts, site policy, and preregistered split decision. No actual split manifest. |
| 27 Data contracts/tests | BLOCKED (60% after this reassessment work) | Add synthetic test-only tests for generic split and contract safeguards. | Approved cohort ranges, censoring rules, and train-only preprocessing behavior. |
| 28 Baseline design | BLOCKED | Compare candidate algorithms conceptually only. | Approved features, labels, sample/event size, and Phase 25. |
| 29 Baseline training | BLOCKED | None. | Valid labeled training cohort and locked split. |
| 30 Baseline evaluation | BLOCKED | None. | Trained baseline and untouched patient test set. |
| 31 Longitudinal inputs | BLOCKED | Maintain the existing refusal gates. | Approved dated visit data and target. |
| 32 Hybrid architecture design | BLOCKED | Keep SimpleRNN → LSTM → Dense as the proposed architecture. | Sequence length, dimensions, event count, and modeling protocol. |
| 33 Model implementation | BLOCKED | No clinical model code now. | Phases 25, 31, and 32. |
| 34 Training pipeline | BLOCKED | Keep environment and code-quality infrastructure ready. | Approved cohort and model implementation. |
| 35 Tuning | BLOCKED | None. | Valid train/validation partitions and baseline/model candidates. |
| 36 Locked evaluation | BLOCKED | None. | Locked test set and trained model. |
| 37 Robustness/ablation | BLOCKED | Define metric/report templates only. | Selected model and valid evaluation cohort. |
| 38 Calibration/threshold | BLOCKED | Document that probabilities remain unavailable. | Valid predictions, calibration evidence, and policy. |
| 39 Explainability | BLOCKED | No clinical explanations from a nonexistent model. | Approved features/model and validation. |
| 40 Subgroups/generalization | BLOCKED | Preserve diversity requirements. | Approved cohort/subgroup counts and model results. |
| 41 External validation | BLOCKED | Identify candidate independent cohorts. | Approved external cohort and trained model. |
| 42 Model reporting | BLOCKED | None beyond data-readiness documentation. | Completed valid evaluation. |
| 43 Artifact versioning | BLOCKED | Environment metadata can be recorded. | Approved trained model and fitted preprocessing. |
| 44 Database architecture | IN PROGRESS (50%; provisional design) | Logical ER/schema, candidate constraints/indexes, and service boundaries documented without deployment or patient records. | Governance and workflow review for clinical columns, retention, RLS, and live persistence. |
| 45 Authentication/authorization | IN PROGRESS (30%; design only) | Provisional trust boundaries, access matrix, credential rules, and future security test requirements documented. | Institutional role/patient-scope policy, governance, Phase 46, RLS context implementation, and security testing. |
| 46 FastAPI backend | IN PROGRESS (25%; health-only scaffold) | Pinned API runtime, typed liveness/readiness routes, and tests; readiness explicitly reports database/auth/model as unavailable. | Patient, database, authentication, and inference services require their own upstream gates. |
| 47 Patient/visit management | NOT STARTED | Draft endpoint and validation contracts only. | Governance, schema, auth, and approved source fields before CRUD or real records. |
| 48 Prediction service | NOT STARTED | Define safe unavailable response contract only. | Versioned approved model and authorized patient-history path. |
| 49 UI/UX architecture | IN PROGRESS (40%; provisional design) | Route map, component inventory, empty/error/access-denied/unavailable states, disclaimer placement, and accessibility requirements documented. | Review with representative users; final tokens, contrast checks, responsive implementation, and model-specific screens remain unavailable. |
| 50 React frontend | IN PROGRESS (60%; static shell) | Responsive Vite/React/TypeScript shell, six module entry routes, no-auth/no-data states, typed API URL config, components, and tests; no patient records or results. | Auth/API integration, route authorization, error boundaries, formal accessibility acceptance, and final design review before protected workflows. |
| 51 Patient screens | NOT STARTED | Static layouts and validation states can be designed without records. | No patient CRUD/timeline/prediction success UI until authorized API and model exist. |
| 52 Frontend/backend integration | NOT STARTED | Health-only API and static UI shells exist; typed auth/request integration design can be advanced without patient data. | Auth, patient API/database contracts, and inference workflow are not implemented; no protected integration flow may be claimed. |
| 53 Security/privacy audit | IN PROGRESS (30%; threat model only) | Provisional assets, actors, trust boundaries, 16 threats, controls, and required evidence documented. | Live implementation review, RLS/IDOR tests, deployment boundary, and institutional/data-owner acceptance. |
| 54 App testing | IN PROGRESS (30%; foundation tests) | Deterministic data-guard, API readiness, frontend unavailable-state, auth placeholder, and API URL configuration unit tests. | Integration/E2E requires implemented auth, DB, patient UI/API, and inference. |
| 55 Performance/reliability | IN PROGRESS (20%; test design only) | Document guarded progression, candidate measures, failure scenarios, and report fields without inventing load targets. | API/inference service, integrated paths, approved workload/targets, and authorized environment are still needed to run tests. |
| 56 CI/CD | IN PROGRESS (50%; validation CI only) | Read-only GitHub Actions runs locked Python/API tests, Ruff, Node 24 type/lint/Vitest/build, and npm audit with no secrets or patient files. Hosted run 41892334989 passed for `a525779`. | Release/deploy pipeline requires security, reliability, and governance gates. |
| 57 Deployment readiness | NOT STARTED | None for health-data deployment. | Governance, security, model artifact, hosting and recovery approval. |
| 58 Monitoring/drift | IN PROGRESS (25%; provisional design) | Document candidate health/error/latency signals, an allowlisted log contract, aggregate-only approval-gated data/model drift, and future alert/retention tests. | No telemetry/dashboard/alerts may be activated without service/model/deployment and privacy approvals (43, 48, 57); no model/cohort exists for drift analysis. |
| 59 Backup/operations | NOT STARTED | Draft questions only. | Live database, policy-approved retention, and restore target. |
| 60 Clinical usability review | IN PROGRESS (20%; draft protocol only) | Prepare a no-data walkthrough for research-only disclaimer, static routes, unavailable states, and accessibility. | No participant sessions, applicable institutional determination, user findings, fixes, or retest; real clinical screens remain unavailable. |
| 61 Final handover | NOT STARTED | Keep development docs current. | Final data/model/application deliverables. |
| 62 Final acceptance | NOT STARTED | None. | Valid evaluation, application, and academic review. |
| 63 Maintenance roadmap | NOT STARTED | Document maintenance standards for implemented foundations. | Deployment and final evaluation results. |

## Work selection

Phase 27's high-priority test-only split safety coverage is complete as an independent slice; the remainder is blocked by Phase 25. Phase 44 has a provisional logical schema, Phase 45 has a provisional authorization design, Phase 46 has a health-only API scaffold, Phase 49 has provisional UI/UX architecture, Phase 50 has a static React shell, Phase 53 has a provisional threat model, Phase 54 has foundation tests, and Phase 56's read-only validation CI passed hosted run 41892334989. Phase 55 now has a guarded test plan; actual measurement waits for API/inference paths, approved workload targets, and an authorized environment. Phase 58 has a provisional privacy-safe observability design; activation, alert testing, and drift analysis remain blocked on the real service/model/deployment and governance approvals. Phase 60 has a no-data walkthrough protocol for the static shell; participant review, applicable institutional determination, fixes, and retest remain outstanding. The existing API and frontend shells support further typed, non-sensitive foundation work, but not a patient workflow. Phase 61 documentation can be maintained incrementally but cannot be accepted as a reproducibility handover until its dependencies complete. Do not create live database use, auth secrets, patient CRUD, prediction behavior, completed security audit, or deployment readiness to bypass these gates.

## Persistent restrictions

- Never create or publish patient records, visit histories, outcome labels, actual split manifests, or model metrics from fixtures.
- Test-only synthetic rows must be explicitly named and stay in test code.
- No live Supabase resources, credentials, migrations, or health data until governance permits the exact use.
- An unavailable model returns no class and no probability.
