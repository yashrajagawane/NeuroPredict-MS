# Remaining Phase Dependency Reassessment

**Reviewed:** 2026-11-04  
**Baseline:** `PROJECT_MASTER_PLAN.md` at `dc93a1f` (Phase 26 complete)  
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
| 44 Database architecture | NOT STARTED; design slice eligible | Provisional logical ER/schema and security assumptions, with no deployment or patient records. | Governance and workflow review for final clinical columns, retention, RLS, and live persistence. |
| 45 Authentication/authorization | NOT STARTED; design slice eligible after Phase 44 draft | Draft least-privilege role/access matrix and trust boundaries; no live Auth setup or policy migration. | Institutional role policy, governance, DB/backend implementation, and security testing. |
| 46 FastAPI backend | NOT STARTED; minimal foundation eligible | A non-sensitive health/readiness endpoint and typed app config can be built after Phase 26. | Patient, database, authentication, and inference services require their own upstream gates. |
| 47 Patient/visit management | NOT STARTED | Draft endpoint and validation contracts only. | Governance, schema, auth, and approved source fields before CRUD or real records. |
| 48 Prediction service | NOT STARTED | Define safe unavailable response contract only. | Versioned approved model and authorized patient-history path. |
| 49 UI/UX architecture | NOT STARTED; design slice eligible | Route map, component inventory, accessible styles, empty/error/insufficient-data states from existing UX guidance. | Review with representative users; model-specific screens remain unavailable. |
| 50 React frontend | NOT STARTED; static foundation eligible | Vite/React/TypeScript shell and research-only empty states; no patient records or prediction values. | Auth/API integration and final design before protected workflows. |
| 51 Patient screens | NOT STARTED | Static layouts and validation states can be designed without records. | No patient CRUD/timeline/prediction success UI until authorized API and model exist. |
| 52 Frontend/backend integration | NOT STARTED | No integration until both foundations exist. | Auth, API contracts, and inference gates. |
| 53 Security/privacy audit | NOT STARTED; threat-model planning eligible | Threat-model architecture and secret/data-flow controls. | Live implementation, RLS tests, deployment boundary, and PI/DPO acceptance. |
| 54 App testing | NOT STARTED; scaffold tests eligible | Unit tests for independent backend/frontend foundations. | Integration/E2E requires implemented auth, DB, UI, and API. |
| 55 Performance/reliability | NOT STARTED | Define provisional test approach only. | Running service/model and agreed workload/targets. |
| 56 CI/CD | NOT STARTED; CI foundation eligible | Extend Phase 26 CI for backend/frontend checks as those foundations appear. | Release/deploy pipeline requires security, reliability, and governance gates. |
| 57 Deployment readiness | NOT STARTED | None for health-data deployment. | Governance, security, model artifact, hosting and recovery approval. |
| 58 Monitoring/drift | NOT STARTED | Privacy-safe metric design can be documented. | Deployed service and approved model/data monitoring. |
| 59 Backup/operations | NOT STARTED | Draft questions only. | Live database, policy-approved retention, and restore target. |
| 60 Clinical usability review | NOT STARTED | Prepare review script when prototype screens exist. | Representative clinician/user availability and approved intended-use language. |
| 61 Final handover | NOT STARTED | Keep development docs current. | Final data/model/application deliverables. |
| 62 Final acceptance | NOT STARTED | None. | Valid evaluation, application, and academic review. |
| 63 Maintenance roadmap | NOT STARTED | Document maintenance standards for implemented foundations. | Deployment and final evaluation results. |

## Work selection

The first executable item is Phase 27's test-only split safety coverage (high priority). After recording that the remaining phase is blocked by Phase 25, Phase 44's provisional logical schema is the first application architecture dependency. FastAPI and React foundations can then be built as isolated, non-sensitive scaffolds; no live database, authentication secrets, patient CRUD, or prediction behavior is implied.

## Persistent restrictions

- Never create or publish patient records, visit histories, outcome labels, actual split manifests, or model metrics from fixtures.
- Test-only synthetic rows must be explicitly named and stay in test code.
- No live Supabase resources, credentials, migrations, or health data until governance permits the exact use.
- An unavailable model returns no class and no probability.
