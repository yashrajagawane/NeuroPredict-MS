# NeuroPredict-MS Project Master Plan

**Single source of truth for roadmap and progress**

**Project:** Deep Learning Approach for Prediction of Multiple Sclerosis Using Hybrid RNN & LSTM

**Last updated:** 2026-11-05

**Plan version:** 1.0
**Approved stack:** React + TypeScript + Vite + Tailwind CSS + shadcn/ui + React Router + TanStack Query + React Hook Form + Zod + Recharts + Lucide React; Python 3.12 + FastAPI + SQLAlchemy + Alembic + Pydantic; Supabase PostgreSQL + Supabase Auth + PostgreSQL RLS; Pandas + NumPy + scikit-learn + TensorFlow/Keras + Matplotlib + Seaborn; pytest, Git/GitHub, VS Code, Jupyter Notebook.

> This is a research and educational prototype, not a clinically validated diagnostic product. The current NO-GO for supervised training remains active. No phase status below implies clinical approval, model validity, or deployment readiness beyond the cited repository evidence.

## A. Executive dashboard

| Measure | Current value | Basis |
|---|---:|---|
| Total phases | 64 | Unique phase IDs 00-63. |
| COMPLETE | 10 | Acceptance evidence exists for the bounded public-source audit, project-charter work, and reproducible developer environment listed below. |
| IN PROGRESS | 12 | Documented planning or reusable validation work has begun but is not fully accepted. |
| BLOCKED | 33 | Work depends on approved longitudinal clinical data, endpoint decisions, or clinical/governance input. |
| NOT STARTED | 9 | No execution evidence exists; mainly application, validation, operations, and handover phases. |
| NOT APPLICABLE | 0 | Nothing is formally excluded at this time. |
| Overall progress | **23.7% phase-weighted evidence score** | Sum of documented phase completion percentages / 64. Not labor-hours or a prediction of calendar completion. |
| Current active phase | Phase 55 - Performance and Reliability Testing (IN PROGRESS, 20%; plan only). | Test scenarios and measurement fields are documented; no service/model workload test or target has been approved or run. |
| Current critical blocker | Approved longitudinal cohort with genuine dated visits, confirmed CIS status, event and follow-up dates, criteria, and permitted research use. | Public interim cohorts do not meet the target definition. |
| Next recommended action | Wait for service/model and workload-target dependencies before executing performance tests; continue only independent documentation and test-design slices. | Do not train while data feasibility and clinical target adjudication remain unresolved. |

### Progress calculation

Progress is **phase-weighted**, using integer completion estimates anchored to verified checklist evidence. COMPLETE phases count 100%; NOT STARTED phases count 0%; IN PROGRESS and BLOCKED phases retain only evidence-backed partial values. Current partial values are Phase 02 50%, Phase 03 25%, Phase 27 60%, Phase 44 50%, Phase 45 30%, Phase 46 25%, Phase 49 40%, Phase 50 60%, Phase 53 30%, Phase 54 30%, Phase 55 20%, Phase 56 50%, Phase 58 25%, and Phase 60 20%. Thus `(10 x 100 + 50 + 25 + 60 + 50 + 30 + 25 + 40 + 60 + 30 + 30 + 20 + 50 + 25 + 20) / 64 = 23.7%`. Phase 02's 50% records the confirmed research objective and label handling principles, not an approved operational target. Phase 01 is complete based on project-owner scope approval and reconciled acceptance documentation. Any institutionally required supervisor review is tracked separately; no supervisor approval is claimed. This is not an effort-weighted estimate.

### Current verified project state

- Public Mexican source: 273 rows, 272 unique source IDs, one duplicate source identifier retained; group codes 1/2 remain unmapped.
- Public Lithuanian source: 138 records and unique source IDs; final MS grouping is 0/1 but has no individual conversion or follow-up dates.
- Cohorts remain separate. The current interim extracts contain source fields, not approved model features. Approved future-conversion model inputs: 0. Valid fixed-horizon labels: 0. Genuine dated repeated visit records available from these downloads: 0.
- The doctor-facing application with six modules is a mandatory user-confirmed final deliverable. A static React shell and health-only FastAPI scaffold exist; no patient-data application workflow, database instance, or inference integration exists. Real-data access and prediction remain gated.
- No selected prediction horizon, final index-date rule, eligible model cohort, patient split manifest, trained model, model metrics, live patient API, authenticated frontend workflow, or deployment exists.
- The latest local verification ran 14/14 tests under Python 3.12.10; Ruff lint/format checks and `pip check` passed. GitHub Actions run 41892334989 for `a525779` completed successfully across Python/API and frontend checks. Phase 26's earlier 13-test suite also passed on Python 3.13.5.
- A task-level reassessment of every incomplete phase is recorded in [PROJECT_DEPENDENCY_REASSESSMENT.md](PROJECT_DEPENDENCY_REASSESSMENT.md). It distinguishes approved no-data design/foundation work from live clinical-data and model gates.
- Raw source workbooks and processed patient-level extracts are Git-ignored. Do not add them to Git or upload them to unapproved services.

## B. Master phase tracker

Status definitions: COMPLETE requires verified acceptance; IN PROGRESS means evidenced work has started; BLOCKED means a stated dependency prevents responsible execution; NOT STARTED means no execution evidence exists; NOT APPLICABLE requires an explicit scope decision and reason.

| Phase ID | Phase name | Status | Completion % | Priority | Dependencies | Blocker | Evidence |
|---|---|---:|---:|---|---|---|---|
| 00 | Repository Reconnaissance and Current-State Audit | COMPLETE | 100 | Critical | None | - | Repository inventory; test/status log; data reports. |
| 01 | Project Charter and Scope Definition | COMPLETE | 100 | High | 00 | - | Reconciled PRD/SRS/scope and six-module acceptance criteria; explicit project-owner approval in updated authorization. Supervisor approval is not claimed. |
| 02 | Research Question and Prediction Target Definition | BLOCKED | 50 | Critical | 01 | No approved longitudinal cohort with patient-level dates; clinician adjudication and operational target approval unavailable. | Confirmed future CIS-to-MS objective; label report and data contract document unresolved requirements. |
| 03 | Clinical Workflow and Intended-Use Definition | IN PROGRESS | 25 | High | 01-02 | Intended users/workflow are design assumptions pending stakeholder review. | PRD, SRS, UI/UX, safety docs. |
| 04 | Prediction Index Date and Horizon Design | BLOCKED | 0 | Critical | 02, 09, 23 | No patient-level dated follow-up distributions. | Label validation report. |
| 05 | Clinical Expert Review and Endpoint Adjudication | BLOCKED | 0 | Critical | 02, 04 | Clinical investigator/neurologist decision needed. | No sign-off evidence in repository. |
| 06 | Clinical Dataset Source Research | COMPLETE | 100 | High | 00 | Initial source survey complete; new-source searches may be reopened as needed. | Candidate comparison and evidence ledger. |
| 07 | Data Access and Research Collaboration | BLOCKED | 0 | Critical | 05-06 | No approved controlled-access feasibility request or data-use agreement. | MSBase/MSBasis request specification only. |
| 08 | Ethics, Privacy, and Data Governance | BLOCKED | 0 | Critical | 07 | Institutional/source approvals and governance conditions for a clinical cohort absent. | Safety guidance exists; approval evidence absent. |
| 09 | Dataset Feasibility Assessment | COMPLETE | 100 | Critical | 06 | Feasibility of acquired public downloads assessed; any new source requires a new feasibility pass. | Source audit and final readiness report. |
| 10 | Approved Data Acquisition | BLOCKED | 0 | Critical | 07-09 | No suitable approved longitudinal source acquired. | Only public, insufficient interim sources exist. |
| 11 | Raw Data Security and Versioning | COMPLETE | 100 | High | 09 | Local raw protection/hash evidence exists for current public sources. New governed data need a new release-specific review. | `.gitignore`, provenance report, hash audit. |
| 12 | Dataset Inventory and Data Dictionary | COMPLETE | 100 | High | 09, 11 | Complete for acquired public files only; future source requires new mapping. | Source audit and mapping dictionaries. |
| 13 | Cohort Inclusion and Exclusion Rules | BLOCKED | 0 | Critical | 02, 05, 10, 12 | Final cohort and clinical eligibility criteria not defined. | Current future-cohort rules are prospective contract guidance only. |
| 14 | Outcome and Label Definition | BLOCKED | 0 | Critical | 02, 04, 05, 10 | No horizon-specific verified patient outcomes. | Label rules drafted; actual labels unavailable. |
| 15 | Follow-Up and Censoring Management | BLOCKED | 0 | Critical | 04, 10, 14 | Patient-level follow-up/censor dates absent. | Outcome contract requirements documented. |
| 16 | Feature Mapping and Clinical Feature Assessment | COMPLETE | 100 | High | 12 | Assessment complete for available public columns; approved cohort requires reassessment. | Feature assessment and interim mapping reports. |
| 17 | Feature Selection and Feature Approval | BLOCKED | 0 | Critical | 05, 10, 13, 16, 18 | Zero model-approved input features for target. | Assessment documents 14 candidates and exclusions. |
| 18 | Temporal Leakage Assessment | COMPLETE | 100 | Critical | 12, 14, 16 | Current public-source leakage review complete; repeat for selected cohort. | Final EDSS/post-index and target leakage notes. |
| 19 | Exploratory Data Analysis and Data Quality Assessment | COMPLETE | 100 | High | 09, 12 | Completed for current sources only; final eligible cohort EDA remains future work. | Quality reports, missingness, source audit. |
| 20 | Data Cleaning and Clinical Harmonization | BLOCKED | 0 | High | 10, 12, 13, 16 | No selected compatible source or codebooks/units to harmonize. | Interim files are source-preserving; no medical recoding. |
| 21 | Missing Data and Outlier Strategy | BLOCKED | 0 | High | 10, 17, 19, 20, 25 | Final data and train split needed for defensible learned policies. | Public missingness is described; no model imputation policy approved. |
| 22 | Longitudinal Visit Structure and Sequence Design | BLOCKED | 0 | Critical | 04, 10, 14, 17, 19 | No real repeated dated visits in current downloads. | Templates and guarded utility exist; no eligible sequence data. |
| 23 | Sample Size, Event Count, and Statistical Feasibility | BLOCKED | 0 | Critical | 10, 14, 15, 19 | Eligible patient/event/follow-up counts unknown. | Public cohort cannot establish usable class counts. |
| 24 | Dataset Freeze and Reproducibility | BLOCKED | 0 | High | 08, 13-23 | No approved modeling cohort to version/freeze. | Current source provenance and manifests cover interim sources only. |
| 25 | Model Evaluation Protocol and Patient-Level Splitting | BLOCKED | 0 | Critical | 02, 14, 19, 23-24 | Cannot make valid future-conversion partitions without cohort/labels. | Guarded splitter refuses current data; no manifest exists. |
| 26 | Development Environment and Engineering Standards | COMPLETE | 100 | Medium | 00 | - | Python/Node versions, locked developer tools, secrets template, Ruff standards, and CI workflow; 13 tests pass under Python 3.12.10 and 3.13.5. |
| 27 | Data Contracts and Automated Pipeline Tests | BLOCKED | 60 | High | 12, 14, 22, 25-26 | Approved cohort and Phase 25 evaluation protocol are unavailable; only cohort-independent test work can proceed. | Contract guards plus test-only split reproducibility, overlap, and uncertain-outcome exclusion checks; 14 local tests pass. |
| 28 | Classical Baseline Model Design | BLOCKED | 0 | High | 17, 23, 25 | Modeling target/features/sample size unresolved. | Baseline candidates in model specification only. |
| 29 | Baseline Model Training | BLOCKED | 0 | Critical | 21, 25, 27-28 | No valid labeled training cohort. | No training evidence. |
| 30 | Baseline Model Evaluation | BLOCKED | 0 | Critical | 29 | No trained baseline or held-out patient set. | No metrics/artifacts. |
| 31 | Longitudinal Model Input Pipeline | BLOCKED | 0 | Critical | 17, 21-27 | No approved dated visits or target. | Sequence utility is gated and has produced no clinical sequences. |
| 32 | Hybrid RNN-LSTM Architecture Design | BLOCKED | 0 | High | 22-23, 31 | Data-derived sequence and capacity decisions unavailable. | SimpleRNN -> LSTM is proposed, not parameterized. |
| 33 | Model Implementation | BLOCKED | 0 | High | 26, 31-32 | No model source implementation permitted before data gates. | No model code found. |
| 34 | Reproducible Model Training Pipeline | BLOCKED | 0 | Critical | 25, 27, 33 | No approved dataset/model implementation. | No checkpoints, configs, or experiment logs. |
| 35 | Hyperparameter Tuning and Model Selection | BLOCKED | 0 | High | 29-30, 34 | No train/validation cohort. | No tuning record. |
| 36 | Internal Validation and Final Locked Test Evaluation | BLOCKED | 0 | Critical | 25, 30, 35 | No valid untouched test patients or model. | No evaluation output. |
| 37 | Robustness, Sensitivity, and Ablation Studies | BLOCKED | 0 | High | 35-36 | No selected model or validated cohort. | No experiment evidence. |
| 38 | Calibration and Decision Threshold Assessment | BLOCKED | 0 | High | 14, 36 | No valid predictions or positive-class definition. | Output probability policy remains open. |
| 39 | Explainability and Clinical Interpretability | BLOCKED | 0 | Medium | 17, 33, 36 | No approved feature/model behavior to explain. | No explanation artifacts. |
| 40 | Subgroup, Bias, and Generalization Assessment | BLOCKED | 0 | High | 10, 23, 36 | Cohort composition and subgroup sizes unavailable for final cohort. | Existing quality report notes limited diversity; no model subgroup results. |
| 41 | External Validation | BLOCKED | 0 | High | 10, 36 | Independent approved cohort unavailable. | No external validation evidence. |
| 42 | Final Model Reporting and Model Card | BLOCKED | 0 | High | 36-41 | No model/results to report. | Dataset card exists for data status, not a trained model. |
| 43 | Model and Preprocessing Artifact Versioning | BLOCKED | 0 | High | 24, 34-36, 42 | No trained model or fitted preprocessing artifact. | No model artifact. |
| 44 | Supabase PostgreSQL Architecture | IN PROGRESS | 50 | Medium | 01, 03, 08, 12 | Clinical-field, retention, role/RLS, and deployment decisions remain pending. | Provisional logical model, candidate constraints/indexes, and access-boundary decisions in `15_PROVISIONAL_DATA_ARCHITECTURE.md`; no migrations or live data. |
| 45 | Supabase Authentication and Authorization | IN PROGRESS | 30 | Critical | 08, 44, 46 | Live Auth/RLS implementation waits for Phase 46 and institutional role/patient-scope decisions. | Provisional trust boundaries, access matrix, and security test requirements in `16_PROVISIONAL_AUTHORIZATION_ARCHITECTURE.md`; no live policies or credentials. |
| 46 | FastAPI Backend Implementation | IN PROGRESS | 25 | Medium | 26, 43-45 | Patient/auth/database and inference APIs require Phases 43-45, governance, and validated model readiness. | Health-only scaffold with explicit unavailable integrations in `backend/app/main.py`; 3 API tests pass; no clinical routes or persistence. |
| 47 | Patient and Visit Management | NOT STARTED | 0 | High | 08, 44-46 | - | No database or API CRUD code. |
| 48 | Prediction and Model Inference Service | NOT STARTED | 0 | Critical | 43, 46-47 | - | No validated model to serve. |
| 49 | UI/UX Architecture and Design System | IN PROGRESS | 40 | Medium | 03, 46, 48 | Clinical-user review and model-dependent screens remain gated; visual/accessibility testing is pending. | Provisional routes, components, states, disclaimers, and accessibility checklist in `17_PROVISIONAL_UI_UX_ARCHITECTURE.md`. |
| 50 | React Frontend Implementation | IN PROGRESS | 60 | Medium | 26, 45-46, 49 | Real auth/session integration, protected route enforcement, error boundaries, and backend data remain gated. | Static React/TypeScript/Vite shell, safe unavailable pages, typed API config, reusable components, tests, and lockfile in `frontend/`; no patient data or secrets. |
| 51 | Patient, Visit History, and Prediction Screens | NOT STARTED | 0 | High | 47-50 | - | No UI files; data and inference remain unavailable. |
| 52 | Frontend and Backend Integration | NOT STARTED | 0 | High | 45-51 | - | No app components exist. |
| 53 | Application Security and Privacy Audit | IN PROGRESS | 30 | Critical | 08, 45-48, 52 | Threat-model planning is provisional; implementation-based audit, governance review, and security tests await application/data gates. | Threat register, trust boundaries, assets, and verification plan in `18_PROVISIONAL_THREAT_MODEL.md`; no penetration test or audit claim. |
| 54 | Unit, Integration, and End-to-End Testing | IN PROGRESS | 30 | High | 27, 46-53 | Auth/database/RLS, patient workflow, inference, full leakage tests, and E2E dependencies remain unavailable. | Existing data contract/split tests plus FastAPI and React foundation tests; no clinical records or integration environment. |
| 55 | Performance and Reliability Testing | IN PROGRESS | 20 | Medium | 48, 52, 54 | Service/model workflows and approved workload targets are unavailable; only test planning can proceed. | Provisional test scenarios and reporting plan in `21_PROVISIONAL_PERFORMANCE_RELIABILITY_PLAN.md`; no load or inference tests run. |
| 56 | CI/CD and Deployment Preparation | IN PROGRESS | 50 | Medium | 26, 53-55 | Deployment preparation remains gated. | Locked Python/API and Node frontend checks pass in GitHub Actions run 41892334989 for `a525779`; read-only workflow only, no deployment credentials. |
| 57 | Production Deployment Readiness | NOT STARTED | 0 | Critical | 08, 43, 53-56 | - | No deployment approval or application. |
| 58 | Monitoring, Logging, and Model Drift | IN PROGRESS | 25 | Medium | 43, 48, 57 | Operational telemetry, dashboards, alerts, and drift analysis require the service/model/deployment gates; only privacy-safe design can proceed now. | `19_PROVISIONAL_OBSERVABILITY_DESIGN.md`; no telemetry or dashboard is implemented. |
| 59 | Backup, Disaster Recovery, and Operations | NOT STARTED | 0 | High | 44-45, 53, 57 | - | No database instance/runbook. |
| 60 | Clinical Workflow and Usability Review | IN PROGRESS | 20 | High | 03, 49-54 | Participant review and any applicable institutional determination are outstanding; current shell has no patient/service workflows. | Draft no-data static-shell walkthrough protocol in `20_PROVISIONAL_USABILITY_WALKTHROUGH.md`; no sessions performed. |
| 61 | Final Documentation and Reproducibility Package | NOT STARTED | 0 | High | 24, 42-60 | - | Current documents are planning/audit records, not final handover. |
| 62 | Final Project Acceptance and Academic Presentation | NOT STARTED | 0 | High | 36, 42, 53-61 | - | No final model/app acceptance evidence. |
| 63 | Maintenance and Future Research Roadmap | NOT STARTED | 0 | Medium | 57-62 | - | No operational system or owner assigned. |

## C. Detailed phase records

Effort estimates are person-days of focused work, excluding institutional approval waiting time, source-owner response time, participant recruitment, and unforeseeable data harmonization. Estimates are planning ranges, not commitments. For each phase, status and completion are based on evidence as of the update date. Dependencies refer to phase IDs above.

### PHASE 00 - Repository Reconnaissance and Current-State Audit

- **Purpose/outcome:** Establish an evidence-based inventory before implementation. **Status:** COMPLETE (100%). **Priority:** Critical. **Dependencies:** None. **Effort:** 2-3 days; completed.
- **Description/tasks:** [x] Inventory root, data and handoff files. [x] Inspect raw/interim/template presence without exposing patient values. [x] Review scripts/tests/status and Git state. [x] Record current no-model/no-app condition.
- **Prerequisites/tools/inputs:** Repository access; PowerShell/Git; handoff pack; existing reports.
- **Deliverables:** Existing handoff, data inventory, source reports, scripts and tests; this baseline record.
- **Acceptance/testing:** File inventory agrees with filesystem; raw source hashes/counts documented; test result taken from status record rather than assumed rerun.
- **Risks/clinical-security considerations:** Git ignores patient-level data; must not stage these files during reconnaissance.
- **Evidence/remaining/blockers:** `data/reports/final_dataset_readiness_review.md`, `PROJECT_STATUS_TEMPLATE.md`, `git log/status`; no remaining reconnaissance task for current checkout. Re-run only after repository changes.

### PHASE 01 - Project Charter and Scope Definition

- **Purpose/outcome:** Define the two mandatory project deliverables, research-only boundaries, measurable success evidence, and change control. **Status:** COMPLETE (100%). **Priority:** High. **Dependencies:** 00. **Effort:** 1-2 days.
- **Description/tasks:** [x] Draft PRD/SRS/scope. [x] Reconcile the intended task throughout requirements as future CIS-to-MS conversion, while preserving unresolved operational index/horizon. [x] Confirm the doctor-facing web app is mandatory and document all six modules, responsibilities, workflows, security, validation, tests, and acceptance criteria. [x] Record project-owner approval of scope in the updated development authorization.
- **Prerequisites/tools/inputs:** Handoff documents and confirmed user scope/stack instruction.
- **Deliverables:** Reconciled project brief, PRD, SRS, scope, architecture/workflow/data/API/safety/UI/testing/acceptance requirements, and approved-stack decision record.
- **Acceptance/testing:** Research objective and app scope are consistent across requirements; all six modules have functional and acceptance criteria; no clinical-use claims; operational prediction details remain explicitly gated; project-owner approval and decision authority are recorded. **Documentation consistency review and project-owner acceptance completed.**
- **Risks/clinical-security considerations:** Mandatory app scope does not authorize real-patient data use or deployment. Prediction remains disabled without approved data and a validated versioned model. Doctor-facing wording is a product role requirement, not clinician endorsement.
- **Evidence/remaining/blockers:** Updated development authorization explicitly approves the two-part scope and six mandatory app modules; aligned handoff documents and acceptance criteria are present. Supervisor approval is not claimed. Any institutional supervisor review required for future clinical research or real-data use remains a separate governance item and does not block independent planning/engineering work. Phase 02 remains blocked on approved dated cohort data and clinical adjudication.

### PHASE 02 - Research Question and Prediction Target Definition

- **Purpose/outcome:** Operationally define future CIS-to-MS prediction. **Status:** BLOCKED (50% evidence-backed progress). **Priority:** Critical. **Dependencies:** 01. **Effort:** 2-4 days with clinician review, excluding cohort-access wait time.
- **Description/tasks:** [x] Establish intended future conversion task. [x] Record outcome handling principles for Class 0, Class 1, unknown, and censored in the data contract. [ ] Define eligible CIS population and diagnostic criteria at baseline for a selected cohort. [ ] Define event evidence, index, horizon, and unit of analysis with clinical/data evidence. [ ] Obtain clinical approval of the operational protocol and positive class.
- **Prerequisites/tools/inputs:** Label report, data contract, clinical collaborator, source codebook.
- **Deliverables:** Target protocol/version and adjudication worksheet.
- **Acceptance/testing:** Independent reviewers can classify protocol test vignettes consistently; no outcome relies on post-index predictors; horizon has an evidence-based follow-up basis.
- **Risks/clinical-security considerations:** Cannot infer Mexican group mapping or treat Lithuanian final diagnosis as fixed-horizon conversion.
- **Evidence/remaining/blockers:** User instruction and `14_OPEN_DECISIONS.md` confirm future CIS-to-MS conversion; `data/reports/label_validation_report.md` and `data/contract/recommended_longitudinal_schema.md` specify label handling. Both public workbooks lack patient-level index, conversion, and last-follow-up dates; the 24-, 36-, and 60-month horizons cannot be evaluated. **Blocker:** an approved dated cohort plus clinician/supervisor adjudication. **Acceptance:** NOT MET; no target protocol is approved. No tests were run because this phase is blocked on clinical/data evidence, not executable software. **Completion evidence:** approved target protocol based on cohort feasibility and review.

### PHASE 03 - Clinical Workflow and Intended-Use Definition

- **Purpose/outcome:** Bound users, tasks, and non-diagnostic presentation. **Status:** IN PROGRESS (25%). **Priority:** High. **Dependencies:** 01-02. **Effort:** 2-3 days plus user review.
- **Tasks:** [x] Record doctor/researcher personas as assumptions. [ ] Confirm whether clinician-facing demo is required. [ ] Map permitted record review and research prediction flow. [ ] Approve cannot-predict states, disclaimer placement, and output semantics.
- **Tools/inputs:** PRD, workflow, UX and safety docs; mockups only after approval.
- **Deliverables:** Workflow diagram, user stories, intended-use statement.
- **Acceptance/testing:** Representative users can explain research-only status and reasons predictions may be unavailable; no diagnostic/treatment claim.
- **Risks/considerations:** Avoid implying clinician authorization or clinical utility. **Evidence:** Handoff drafts only. **Remaining/blocker:** stakeholder review; complete with approved workflow.

### PHASE 04 - Prediction Index Date and Horizon Design

- **Purpose/outcome:** Select defensible index and future window. **Status:** BLOCKED (0%). **Priority:** Critical. **Dependencies:** 02, 09, 23. **Effort:** 2-5 days after data feasibility.
- **Tasks:** [ ] Compare CIS diagnosis baseline with later landmark. [ ] Tabulate visit histories and follow-up/event timing by candidate horizons. [ ] Specify minimum pre-index history and no-conversion-before-landmark rule. [ ] Approve one primary horizon and sensitivity alternatives.
- **Tools/inputs:** Approved dated cohort, source definitions, clinician, survival/follow-up summaries.
- **Deliverables:** Preregistered index/horizon decision record and inclusion flow.
- **Acceptance/testing:** Every included predictor precedes index; Class 0 can be observed through horizon; event timing lies after index and within horizon.
- **Risks:** Horizon selected to maximize performance after inspecting labels; mitigate with clinical justification and preregistration.
- **Evidence/remaining/blocker:** No patient-specific dates exist in acquired downloads. **Blocker:** Phase 10 data. Complete only after review and sign-off.

### PHASE 05 - Clinical Expert Review and Endpoint Adjudication

- **Purpose/outcome:** Validate CIS/MS definitions and event adjudication. **Status:** BLOCKED (0%). **Priority:** Critical. **Dependencies:** 02, 04. **Effort:** 3-7 days plus clinician availability.
- **Tasks:** [ ] Identify PI/neurologist reviewers. [ ] Define evidence hierarchy and criteria version. [ ] Create adjudication workflow for uncertain/conflicting events. [ ] Record reviewer agreement and escalation rule.
- **Tools/inputs:** Source data dictionary, diagnostic notes/criteria, ethics-approved review process.
- **Deliverables:** Adjudication SOP, criteria mapping, sign-off.
- **Acceptance/testing:** Blinded sample review and disagreement resolution meet prespecified agreement threshold approved by PI.
- **Risks:** Model target silently follows heterogeneous diagnostic eras. Protect clinical records and limit reviewer access.
- **Evidence/remaining/blocker:** No expert sign-off in repo. **Blocker:** clinician collaboration/data access. Complete with signed SOP and documented review.

### PHASE 06 - Clinical Dataset Source Research

- **Purpose/outcome:** Identify plausible lawful longitudinal sources. **Status:** COMPLETE (100%) for initial survey. **Priority:** High. **Dependencies:** 00. **Effort:** 5-10 days; initial round complete.
- **Tasks:** [x] Review candidate Mexican/Lithuanian sources and publications. [x] Review MultipleMS, MSBase/MSBasis, OFSEP and access pathways as documented. [x] Compare public availability, cohort fit, visits, labels, license/access limits.
- **Tools/inputs:** Primary publications, data repositories, source evidence ledger.
- **Deliverables:** Candidate source comparison, evidence ledger, recommended access route.
- **Acceptance/testing:** Each candidate separates public downloadable content from study-level claims; provenance and access limitations stated.
- **Risks:** Registry cohort-size claims may not represent eligible/releasable sample. **Evidence:** `candidate_source_comparison.md`, `source_evidence_ledger.md`. Reopen for new candidate research if access route fails.

### PHASE 07 - Data Access and Research Collaboration

- **Purpose/outcome:** Secure qualified source-owner collaboration and permissions. **Status:** BLOCKED (0%). **Priority:** Critical. **Dependencies:** 05-06. **Effort:** 5-15 person-days plus external waiting.
- **Tasks:** [ ] Name institutional PI and collaborators. [ ] Submit feasibility question and field-level request. [ ] Negotiate DUA, permitted purpose, environment, publication and retention. [ ] Confirm release size and fields before acquisition.
- **Tools/inputs:** Request spec, ethics pathway, target protocol.
- **Deliverables:** Approved request, DUA/access letter, data dictionary commitment.
- **Acceptance/testing:** Written authorization covers future CIS-to-MS research and specified processing/storage; feasibility extract includes dates/linkage/outcomes.
- **Risks:** No authority to access controlled patient data; never bypass restrictions.
- **Evidence/remaining/blocker:** `msbase_access_request_spec.md` is preparatory only. **Blocker:** institutional PI/source approval. Close with signed evidence.

### PHASE 08 - Ethics, Privacy, and Data Governance

- **Purpose/outcome:** Establish lawful handling of approved health data. **Status:** BLOCKED (0%). **Priority:** Critical. **Dependencies:** 07. **Effort:** 5-20 days plus committee timelines.
- **Tasks:** [ ] Determine ethics/IRB and consent basis with institution. [ ] Approve minimization, pseudonymization, key custody, access, retention, deletion, transfer, breach, and publication rules. [ ] Approve cloud/Supabase eligibility or select institution-controlled environment. [ ] Record data-flow assessment.
- **Tools/inputs:** DUA, institutional policy, safety requirements, architecture.
- **Deliverables:** Ethics approvals/waiver, data-management plan, access matrix, retention schedule.
- **Acceptance/testing:** PI/data protection officer confirms controls; simulated access review verifies least privilege and no raw data in logs/repos.
- **Risks:** Public cloud or AI services may be prohibited. Supabase deployment requires explicit governance review.
- **Evidence/remaining/blocker:** Safety principles exist, but no cohort approval evidence. Complete after institutional authorization.

### PHASE 09 - Dataset Feasibility Assessment

- **Purpose/outcome:** Determine whether acquired public files can support the target. **Status:** COMPLETE (100%) for acquired sources; decision NO-GO. **Priority:** Critical. **Dependencies:** 06. **Effort:** 3-5 days; completed.
- **Tasks:** [x] Count rows/IDs and duplicates. [x] Inspect available field/date structures and missingness. [x] Compare outcome definitions with intended horizon. [x] Report usable cohort and visit counts honestly.
- **Tools/inputs:** Official public XLSX, standard-library source audit, publications.
- **Deliverables:** Hash audit, missingness, label/feature/quality/readiness reports.
- **Acceptance/testing:** Findings are reproducible and do not equate final group counts with horizon labels; no undocumented code mapping.
- **Risks:** Study follow-up mistaken for downloadable patient follow-up. **Evidence:** audit JSON and `final_dataset_readiness_review.md`. Repeat this phase for every new candidate release.

### PHASE 10 - Approved Data Acquisition

- **Purpose/outcome:** Acquire a genuine, permitted longitudinal CIS cohort. **Status:** BLOCKED (0%). **Priority:** Critical. **Dependencies:** 07-09. **Effort:** 3-10 days after approval.
- **Tasks:** [ ] Receive authorized export through approved channel. [ ] Verify release ID/hash and schema. [ ] Confirm pseudonymous linkage and actual repeated dated visits. [ ] Confirm index, event and last follow-up fields, criteria, and permitted feature history.
- **Tools/inputs:** Approved DUA/ethics, secure storage, transfer SOP.
- **Deliverables:** Immutable restricted raw release plus acquisition manifest.
- **Acceptance/testing:** Hash/provenance matches receipt; only authorized staff can read; no direct IDs in modeling layer.
- **Risks:** Data may be smaller or less complete than requested. Do not supplement with fabricated records.
- **Evidence/remaining/blocker:** No appropriate approved cohort. Complete only after receipt and access validation.

### PHASE 11 - Raw Data Security and Versioning

- **Purpose/outcome:** Protect source files and provide integrity evidence. **Status:** COMPLETE (100%) for current public sources. **Priority:** High. **Dependencies:** 09. **Effort:** 1-2 days; completed for existing sources.
- **Tasks:** [x] Keep raw and patient-level processed paths ignored. [x] Record hashes and source attribution. [x] Preserve raw workbooks during interim extraction. [ ] Reapply controls to any future approved store.
- **Tools/inputs:** Git ignore rules, SHA-256 audit, approved secure storage.
- **Deliverables:** Provenance manifest, access-controlled raw store, version naming convention.
- **Acceptance/testing:** `git status`/tracked-file scan confirms no raw or patient-level records tracked; hashes verify after transfer.
- **Risks:** Git ignore is not access control; use filesystem/IAM controls too. **Evidence:** `.gitignore`, data provenance, audit manifest. Revalidate on new acquisition.

### PHASE 12 - Dataset Inventory and Data Dictionary

- **Purpose/outcome:** Define source fields and semantics. **Status:** COMPLETE (100%) for public workbooks. **Priority:** High. **Dependencies:** 09, 11. **Effort:** 3-6 days; completed for current sources.
- **Tasks:** [x] Inventory original columns and types. [x] Preserve source names and map safe interim names. [x] Record ambiguity, missingness and timing limitations. [ ] Rebuild dictionary for approved cohort.
- **Tools/inputs:** XLSX workbooks, audit report, source publications.
- **Deliverables:** Audit feature dictionary and interim mapping/dictionary.
- **Acceptance/testing:** Each mapped field has source name, meaning, type, timing, missingness and use limitation.
- **Risks:** Similar labels do not establish same clinical construct. **Evidence:** `feature_dictionary.csv`, `source_to_processed_mapping.csv`. Future dataset inventory is a new release-specific task.

### PHASE 13 - Cohort Inclusion and Exclusion Rules

- **Purpose/outcome:** Create reproducible patient-level eligibility logic. **Status:** BLOCKED (0%). **Priority:** Critical. **Dependencies:** 02, 05, 10, 12. **Effort:** 2-4 days.
- **Tasks:** [ ] Define CIS confirmation, criteria era, age/site constraints and baseline. [ ] Specify exclusions for prior MS, linkage failure, unusable chronology, and missing key outcome evidence. [ ] Preserve exclusion counts/reasons. [ ] Obtain clinical/statistical approval.
- **Tools/inputs:** Cohort data dictionary, protocol, clinical SOP.
- **Deliverables:** Versioned cohort selection specification and exclusion log.
- **Acceptance/testing:** Re-running selection reproduces patient counts; no silent row deletion; unknown outcomes remain separately counted.
- **Risks:** Post hoc exclusions can bias estimates. **Blocker:** approved cohort/clinical criteria. Complete with reviewed flow diagram and logs.

### PHASE 14 - Outcome and Label Definition

- **Purpose/outcome:** Assign Class 0/1 only under verified evidence. **Status:** BLOCKED (0%). **Priority:** Critical. **Dependencies:** 02, 04-05, 10. **Effort:** 3-6 days.
- **Tasks:** [ ] Define conversion confirmation and criteria version. [ ] Implement event-after-index-and-within-horizon rule. [ ] Implement nonconversion-through-horizon rule. [ ] Keep unknown/censored separate. [ ] Audit sampled labels against source evidence.
- **Tools/inputs:** Dated outcomes, adjudication SOP, contract validator.
- **Deliverables:** Label algorithm, label validation report, outcome table.
- **Acceptance/testing:** Positive/negative labels satisfy dates and criteria; all unobserved/short follow-up records remain unknown/censored; independent adjudication sample passes.
- **Risks:** Final diagnosis is not a time-bounded event. **Blocker:** Phase 10/05. No labels may be guessed.

### PHASE 15 - Follow-Up and Censoring Management

- **Purpose/outcome:** Account for event-free observation and censoring. **Status:** BLOCKED (0%). **Priority:** Critical. **Dependencies:** 04, 10, 14. **Effort:** 2-5 days.
- **Tasks:** [ ] Compute observation duration from index to last follow-up. [ ] Distinguish Class 0, early censoring and unknown outcome. [ ] Summarize loss-to-follow-up and competing events. [ ] Decide whether survival analysis supplements fixed-horizon classification.
- **Tools/inputs:** Patient-specific follow-up/event dates, statistical consultation.
- **Deliverables:** Follow-up table, censoring rules, flow summaries.
- **Acceptance/testing:** Class 0 follow-up reaches horizon; censored cases never become negatives; dates are chronology-checked.
- **Risks:** Informative censoring and variable surveillance. **Blocker:** dated approved outcomes absent.

### PHASE 16 - Feature Mapping and Clinical Feature Assessment

- **Purpose/outcome:** Assess candidate variables in current public sources. **Status:** COMPLETE (100%) for public sources. **Priority:** High. **Dependencies:** 12. **Effort:** 3-5 days; completed.
- **Tasks:** [x] Map proposed 14 features. [x] Separate lesion indicators from counts. [x] Identify IgG level vs index distinction. [x] Record timing, missingness, units, ambiguity and leakage.
- **Tools/inputs:** Source workbooks, publications, feature assessment report.
- **Deliverables:** Feature assessment and mapped interim dictionaries.
- **Acceptance/testing:** No unavailable feature is fabricated; every mapping is labeled candidate/partial/excluded as warranted.
- **Risks:** Similar names invite false harmonization. **Evidence:** `feature_assessment_report.md`. Repeat after approved data access.

### PHASE 17 - Feature Selection and Feature Approval

- **Purpose/outcome:** Approve predictors usable at index. **Status:** BLOCKED (0%). **Priority:** Critical. **Dependencies:** 05, 10, 13, 16, 18. **Effort:** 2-5 days.
- **Tasks:** [ ] Review source definition, units, timing and missingness. [ ] Clinically approve candidate and additional supported variables. [ ] Exclude target proxies, identifiers and post-index data. [ ] Freeze schema/version.
- **Tools/inputs:** Approved data dictionary, clinician/statistician, leakage review.
- **Deliverables:** Approved feature list and signed decision log.
- **Acceptance/testing:** Every feature has acceptable index-time availability, definition, type/unit, missingness policy and no unresolved leakage.
- **Risks:** Feature selection on full outcomes/test set leaks information. **Blocker:** no final cohort; approved inputs currently zero.

### PHASE 18 - Temporal Leakage Assessment

- **Purpose/outcome:** Review timing/leakage in available public sources. **Status:** COMPLETE (100%) for public sources. **Priority:** Critical. **Dependencies:** 12, 14, 16. **Effort:** 2-3 days; completed.
- **Tasks:** [x] Identify missing timestamps and target timing. [x] Flag Mexican final EDSS and final diagnosis as leakage hazards. [x] Prohibit IDs/outcome dates/post-index records as inputs. [ ] Re-audit every approved feature.
- **Tools/inputs:** Feature dictionary, outcome specification, timestamp lineage.
- **Deliverables:** Leakage register and source feature decisions.
- **Acceptance/testing:** Feature timestamps <= index for all model rows; test asserts post-index exclusion and no ID/target columns.
- **Risks:** Date-free records cannot establish ordering. **Evidence:** label/feature/readiness reports. New dataset re-review required.

### PHASE 19 - Exploratory Data Analysis and Data Quality Assessment

- **Purpose/outcome:** Profile acquired public data and determine quality limits. **Status:** COMPLETE (100%) for acquired sources only. **Priority:** High. **Dependencies:** 09, 12. **Effort:** 3-5 days; completed.
- **Tasks:** [x] Report row/unique-ID counts and missingness. [x] Review feature ranges/codes, duplicate IDs, adult-age discrepancy, target distributions. [x] Document absent chronology/follow-up. [ ] Repeat with approved cohort and site/time strata.
- **Tools/inputs:** Audit scripts, workbook, publication.
- **Deliverables:** Data quality, source audit, missingness and feature reports.
- **Acceptance/testing:** Reports do not infer visit counts or conversion class counts from aggregate study claims; all anomalies retained and flagged.
- **Risks:** Public-file grain is patient record, not repeated visits. **Evidence:** `data_quality_report.md`, audit outputs.

### PHASE 20 - Data Cleaning and Clinical Harmonization

- **Purpose/outcome:** Normalize approved source values without losing meaning. **Status:** BLOCKED (0%). **Priority:** High. **Dependencies:** 10, 12-13, 16. **Effort:** 5-15 days depending on source heterogeneity.
- **Tasks:** [ ] Define allowed value/unit/date transformations. [ ] Resolve duplicates with source owner, never auto-delete. [ ] Harmonize only clinically equivalent coding. [ ] Record transformation lineage and exclusions.
- **Tools/inputs:** Approved dictionary, mapping script, clinical reviewers.
- **Deliverables:** Reproducible clean tables, cleaning log, harmonization map.
- **Acceptance/testing:** Raw inputs unchanged; every output traces to source; deterministic rerun yields same hashes/counts.
- **Risks:** Incompatible criteria/site MRI differences. **Blocker:** suitable source absent.

### PHASE 21 - Missing Data and Outlier Strategy

- **Purpose/outcome:** Handle missingness and anomalies without bias. **Status:** BLOCKED (0%). **Priority:** High. **Dependencies:** 10, 17, 19-20, 25. **Effort:** 3-7 days.
- **Tasks:** [ ] Distinguish not measured/unavailable/invalid. [ ] Clinically review outliers before exclusion. [ ] Define training-only imputation/encoding/scaling. [ ] Compare missingness sensitivity strategies within training/validation.
- **Tools/inputs:** Approved train split, pandas, scikit-learn pipelines, clinical review.
- **Deliverables:** Preprocessing specification and fitted train-only artifact.
- **Acceptance/testing:** No learned statistic uses validation/test; missingness indicators/assumptions documented; outlier decisions logged.
- **Risks:** Missing not at random; zero may mean absence vs not assessed. **Blocker:** no model cohort/splits.

### PHASE 22 - Longitudinal Visit Structure and Sequence Design

- **Purpose/outcome:** Define sequences from genuine dated observations. **Status:** BLOCKED (0%). **Priority:** Critical. **Dependencies:** 04, 10, 14, 17, 19. **Effort:** 4-8 days.
- **Tasks:** [ ] Verify stable patient/visit linkage. [ ] Sort and detect duplicate/impossible dates. [ ] Define minimum pre-index visits and time-spacing representation. [ ] Choose variable-length padding/masking after distribution review. [ ] Keep static measures at actual timestamps.
- **Tools/inputs:** Approved visits/outcomes tables, TensorFlow/Keras masking design.
- **Deliverables:** Sequence contract, builder, unit/property tests.
- **Acceptance/testing:** Sequences exactly match genuine pre-index visits; no artificial repeats; label aligns to one patient/index; masks preserve true observations.
- **Risks:** Irregular intervals and sparse MRI timelines. **Blocker:** current downloads have zero dated visits.

### PHASE 23 - Sample Size, Event Count, and Statistical Feasibility

- **Purpose/outcome:** Decide whether target can support requested analyses. **Status:** BLOCKED (0%). **Priority:** Critical. **Dependencies:** 10, 14-15, 19. **Effort:** 2-5 days plus statistician review.
- **Tasks:** [ ] Count eligible patients, conversions, adequate nonconverters, unknown/censored. [ ] Estimate feature and subgroup support. [ ] Evaluate split/event precision and model complexity. [ ] Treat 2,000 as aspiration, not guaranteed adequacy.
- **Tools/inputs:** Feasibility export, power/precision planning, statistician.
- **Deliverables:** Feasibility memo and proceed/stop decision.
- **Acceptance/testing:** Counts at patient level, uncertainty acknowledged, no synthetic balancing; proposed model complexity justified by actual events.
- **Risks:** Small event count, site clustering, spectrum bias. **Blocker:** eligible counts unknown.

### PHASE 24 - Dataset Freeze and Reproducibility

- **Purpose/outcome:** Freeze approved modeling release and provenance. **Status:** BLOCKED (0%). **Priority:** High. **Dependencies:** 08, 13-23. **Effort:** 2-4 days.
- **Tasks:** [ ] Version source release/schema/processing code. [ ] Hash raw and approved derived tables in secure area. [ ] Record cohort criteria/exclusions and access authority. [ ] Freeze before split/modeling; handle amendments as new version.
- **Tools/inputs:** DUA, data manifest, reproducible scripts, secure storage.
- **Deliverables:** Approved dataset manifest and release tag.
- **Acceptance/testing:** Rebuild matches manifest counts/hashes; raw/processed/modeling layers are distinct; sensitive manifest access controlled.
- **Risks:** Changing labels after seeing test results. **Blocker:** no suitable dataset.

### PHASE 25 - Model Evaluation Protocol and Patient-Level Splitting

- **Purpose/outcome:** Establish leakage-safe evaluation. **Status:** BLOCKED (0%). **Priority:** Critical. **Dependencies:** 02, 14, 19, 23-24. **Effort:** 2-4 days.
- **Tasks:** [ ] Choose grouped patient split or grouped CV based on counts/sites. [ ] Assess stratification feasibility and event-per-partition. [ ] Reserve final test before fitting transforms. [ ] Secure manifest with seed/cohort/version; keep all visits per patient together.
- **Tools/inputs:** Frozen labels, scikit-learn grouping/splitting, statistician.
- **Deliverables:** Preregistered evaluation protocol and split manifest.
- **Acceptance/testing:** No patient overlap; class counts and site distribution reported; small-sample split limitations explicitly accepted.
- **Risks:** Random split instability and center leakage. **Blocker:** no valid patient labels.

### PHASE 26 - Development Environment and Engineering Standards

- **Purpose/outcome:** Establish reproducible approved stack and coding practices. **Status:** COMPLETE (100%). **Priority:** Medium. **Dependencies:** 00. **Effort:** 2-5 days.
- **Tasks:** [x] Approve React/TS/Vite, FastAPI/SQLAlchemy, Supabase, TensorFlow/Keras, pytest. [x] Select package managers and compatible runtime/tool versions (Python 3.12 latest supported patch, Node 24.22.2, venv/pip, npm). [x] Create environment/lock/config/secrets template. [x] Verify locked setup, formatting, lint, and test commands on Python 3.12; configure read-only GitHub CI and document logging standards.
- **Tools/inputs:** Approved stack decision, VS Code, Python 3.12, GitHub.
- **Deliverables:** Reproducible environment specification, developer guide, CI checks.
- **Acceptance/testing:** Developer-tool lock installed in isolated Python 3.12.10 and Python 3.13 environments; 13/13 `unittest` and 13/13 pytest checks pass on both; Ruff lint and format checks, `pip check`, and diff check pass. `.env.example` contains only blank variable names/placeholders and is the only dotenv file eligible for Git. The pushed GitHub Actions workflow is configured for Python 3.12; its run is queued, not reported as passed.
- **Risks:** Framework/GPU version mismatch. ML and API runtime dependencies are intentionally deferred to the phases that implement those components; they are not installed by this shared developer setup. The original workbooks remain local-only and relevant CI tests skip when those files are absent.

### PHASE 27 - Data Contracts and Automated Pipeline Tests

- **Purpose/outcome:** Enforce data/model-readiness invariants. **Status:** BLOCKED (60%). **Priority:** High. **Dependencies:** 12, 14, 22, 25-26. **Effort:** 5-10 days across data release.
- **Tasks:** [x] Implement longitudinal contract, date/outcome checks and gates. [x] Test refusal of interim cohorts, approval requirements, IDs and sequence timing. [ ] Add approved-cohort type/range/foreign-key and censoring tests. [x] Add test-only split reproducibility, patient-overlap and uncertain-label exclusion checks. [ ] Add train-only fit and remaining failure-property tests for the approved pipeline.
- **Tools/inputs:** Existing Python scripts/tests; pytest target stack.
- **Deliverables:** Contract suite, fixtures that contain no real patient data, test report.
- **Acceptance/testing:** Test-only split fixture passes; 14/14 `unittest` and 14/14 pytest tests pass on Python 3.12.10. This fixture is not a patient cohort, split manifest, or modeling dataset. Full acceptance remains unmet until approved source contracts, Phase 25 policy, and train-only preprocessing checks are verified.
- **Risks:** Test fixtures mistaken for research data; identifiers and values are visibly test-only and remain in test code. **Blocker for completion:** approved source contract and Phase 25 evaluation protocol.

### PHASE 28 - Classical Baseline Model Design

- **Purpose/outcome:** Specify fair, proportionate comparator models. **Status:** BLOCKED (0%). **Priority:** High. **Dependencies:** 17, 23, 25. **Effort:** 2-3 days after feasibility.
- **Tasks:** [ ] Select logistic/regularized regression and at most justified tree/boosting/SVM models. [ ] Define comparable predictors and patient split. [ ] Decide whether censored outcomes require a survival-analysis supplement. [ ] Predefine metrics and tuning bounds.
- **Tools/inputs:** Approved features, event count, scikit-learn, statistician.
- **Deliverables:** Baseline protocol and configs.
- **Acceptance/testing:** Models answer same target with index-available information; complexity appropriate to event count; identical partitions.
- **Risks:** Overfitting small cohort. **Blocker:** no valid labels/features.

### PHASE 29 - Baseline Model Training

- **Purpose/outcome:** Fit selected baselines using training patients. **Status:** BLOCKED (0%). **Priority:** Critical. **Dependencies:** 21, 25, 27-28. **Effort:** 3-6 days.
- **Tasks:** [ ] Freeze training-only preprocessing pipeline. [ ] Fit baseline models on training patients only. [ ] Save configs/seeds/versions and training diagnostics. [ ] Do not inspect test outcomes for choices.
- **Tools/inputs:** Frozen dataset/split; pandas, scikit-learn, pytest.
- **Deliverables:** Baseline artifacts and run metadata.
- **Acceptance/testing:** Re-run deterministic within declared tolerance; train membership matches manifest; no test fit calls.
- **Risks:** Leakage through global preprocessing. **Blocker:** no training cohort.

### PHASE 30 - Baseline Model Evaluation

- **Purpose/outcome:** Evaluate baselines on validation and locked test per protocol. **Status:** BLOCKED (0%). **Priority:** Critical. **Dependencies:** 29. **Effort:** 3-5 days.
- **Tasks:** [ ] Report confusion matrix, sensitivity, specificity, precision, recall, F1, ROC-AUC/PR-AUC when valid. [ ] Quantify uncertainty and prevalence. [ ] Document threshold selection on validation only. [ ] Compare fairly across baselines.
- **Tools/inputs:** Baseline artifacts, held-out predictions, Matplotlib/Seaborn.
- **Deliverables:** Baseline evaluation report and figures.
- **Acceptance/testing:** Metrics trace to patient-level held-out predictions; positive class, counts, threshold, split and limitations stated.
- **Risks:** Misleading accuracy under imbalance. **Blocker:** Phase 29.

### PHASE 31 - Longitudinal Model Input Pipeline

- **Purpose/outcome:** Transform valid patient histories into model inputs. **Status:** BLOCKED (0%). **Priority:** Critical. **Dependencies:** 17, 21-27. **Effort:** 5-10 days.
- **Tasks:** [ ] Join static/visit/outcome tables by validated IDs. [ ] Restrict sequence to observations <= index. [ ] Transform from training-fitted preprocessors. [ ] Pad/mask unequal sequences and preserve time intervals. [ ] Pair one outcome per patient/index.
- **Tools/inputs:** Approved CSV tables, TensorFlow/Keras, Pandas/NumPy.
- **Deliverables:** Deterministic input builder and schema metadata.
- **Acceptance/testing:** Shape/dtype/mask tests; no post-index values; same patient split manifest; missing values retain defined meaning.
- **Risks:** Static values duplicated as repeated new observations. **Blocker:** no valid visits/outcomes.

### PHASE 32 - Hybrid RNN-LSTM Architecture Design

- **Purpose/outcome:** Select data-justified network configuration. **Status:** BLOCKED (0%). **Priority:** High. **Dependencies:** 22-23, 31. **Effort:** 2-4 days.
- **Tasks:** [ ] Specify SimpleRNN(return_sequences=True) -> LSTM -> output. [ ] Decide masking and static feature fusion. [ ] Constrain trainable parameter count relative to events. [ ] Define binary loss/positive-class handling and baseline rationale.
- **Tools/inputs:** Sequence stats, Keras, baseline performance.
- **Deliverables:** Architecture diagram, parameter rationale, model config.
- **Acceptance/testing:** Input/output shapes agree with builder; masking works; architecture is justified against sample size and baseline.
- **Risks:** Model complexity exceeds available events; do not preselect arbitrary units. **Blocker:** data shape unknown.

### PHASE 33 - Model Implementation

- **Purpose/outcome:** Implement tested TensorFlow/Keras model. **Status:** BLOCKED (0%). **Priority:** High. **Dependencies:** 26, 31-32. **Effort:** 3-6 days.
- **Tasks:** [ ] Build model module from approved config. [ ] Validate input mask, output dimensions, loss and serialization. [ ] Add deterministic forward/save/load tests. [ ] Keep training separate from FastAPI app.
- **Tools/inputs:** Python 3.12, TensorFlow/Keras, pytest.
- **Deliverables:** Model module and unit tests.
- **Acceptance/testing:** Correct batch/time/feature shapes; finite output; save/load parity; no clinical data in fixtures.
- **Risks:** Framework compatibility and nondeterministic GPU kernels. **Blocker:** preceding data/model design.

### PHASE 34 - Reproducible Model Training Pipeline

- **Purpose/outcome:** Train repeatably and record all experiment conditions. **Status:** BLOCKED (0%). **Priority:** Critical. **Dependencies:** 25, 27, 33. **Effort:** 4-8 days.
- **Tasks:** [ ] Configure all seeds, batch, optimizer, checkpoint, early stopping. [ ] Train on train partition only; validation tunes. [ ] Record data version, schema, package/device, config and logs. [ ] Keep test isolated.
- **Tools/inputs:** Frozen train/validation sets, TensorFlow/Keras, experiment metadata store.
- **Deliverables:** Training runner, checkpoints and run manifest.
- **Acceptance/testing:** Run is reproducible to stated tolerance; no test use; model artifacts matched to preprocessing.
- **Risks:** Low-event instability and compute limits. **Blocker:** no data/model.

### PHASE 35 - Hyperparameter Tuning and Model Selection

- **Purpose/outcome:** Select model without test contamination. **Status:** BLOCKED (0%). **Priority:** High. **Dependencies:** 29-30, 34. **Effort:** 3-10 days, bounded.
- **Tasks:** [ ] Predeclare compact search space. [ ] Tune on training/validation or grouped CV only. [ ] Compare to baselines on identical inputs. [ ] Freeze architecture, preprocessing and threshold before test.
- **Tools/inputs:** Training pipeline, validation reports, compute budget.
- **Deliverables:** Selection log and frozen configuration.
- **Acceptance/testing:** Search trials and selection metric recorded; no final test-driven choices; complexity/performance trade-off stated.
- **Risks:** Repeated tuning on small validation set. **Blocker:** model/training unavailable.

### PHASE 36 - Internal Validation and Final Locked Test Evaluation

- **Purpose/outcome:** Estimate internal generalization on held-out patients. **Status:** BLOCKED (0%). **Priority:** Critical. **Dependencies:** 25, 30, 35. **Effort:** 3-5 days.
- **Tasks:** [ ] Freeze preprocessing/model/threshold. [ ] Generate one locked test evaluation. [ ] Report patient-level confusion matrix and class-wise metrics with uncertainty. [ ] Archive predictions with privacy controls.
- **Tools/inputs:** Locked test manifest, frozen artifacts, metric code.
- **Deliverables:** Test evaluation record.
- **Acceptance/testing:** No test use before lock; test IDs disjoint; metrics reproducible from frozen artifacts.
- **Risks:** Small test event counts yield wide intervals. **Blocker:** valid model/split absent.

### PHASE 37 - Robustness, Sensitivity, and Ablation Studies

- **Purpose/outcome:** Test whether conclusions depend on design choices. **Status:** BLOCKED (0%). **Priority:** High. **Dependencies:** 35-36. **Effort:** 5-10 days.
- **Tasks:** [ ] Predefine meaningful ablations (feature groups, history length, missingness policy). [ ] Rerun within training/validation only for choices. [ ] Report sensitivity analysis without test fishing. [ ] Limit claims to available sample support.
- **Tools/inputs:** Frozen pipeline, protocol, compute budget.
- **Deliverables:** Ablation and sensitivity report.
- **Acceptance/testing:** Every analysis prespecified or labeled exploratory; patient splits stay intact; conclusions include uncertainty.
- **Risks:** Multiplicity and selective reporting. **Blocker:** no selected model.

### PHASE 38 - Calibration and Decision Threshold Assessment

- **Purpose/outcome:** Determine whether scores are calibrated and choose operating threshold. **Status:** BLOCKED (0%). **Priority:** High. **Dependencies:** 14, 36. **Effort:** 3-6 days.
- **Tasks:** [ ] Define intended output (class vs score). [ ] Assess calibration with adequate validation support. [ ] Choose threshold on validation data under explicit utility assumptions. [ ] Report Brier/calibration curve and sensitivity/specificity trade-off where valid.
- **Tools/inputs:** Validation predictions, calibration methods, clinical/statistical review.
- **Deliverables:** Threshold/calibration policy.
- **Acceptance/testing:** No probability called risk absent calibration; no threshold chosen on test set; uncertainty stated.
- **Risks:** Calibration unreliable in small data; no clinical utility claim. **Blocker:** predictions unavailable.

### PHASE 39 - Explainability and Clinical Interpretability

- **Purpose/outcome:** Explain model behavior without causal overclaim. **Status:** BLOCKED (0%). **Priority:** Medium. **Dependencies:** 17, 33, 36. **Effort:** 4-8 days.
- **Tasks:** [ ] Select explanation methods compatible with sequence model. [ ] Check stability across patients/seeds. [ ] Separate explanation from causal inference. [ ] Obtain clinical review of display wording.
- **Tools/inputs:** Frozen model, feature mapping, explanation libraries/methods.
- **Deliverables:** Technical explanation report and limitations.
- **Acceptance/testing:** Explanations do not use outcomes/post-index data as features; stability and method limits reported.
- **Risks:** Saliency plots can appear clinically authoritative. **Blocker:** model/features absent.

### PHASE 40 - Subgroup, Bias, and Generalization Assessment

- **Purpose/outcome:** Assess supported subgroup performance. **Status:** BLOCKED (0%). **Priority:** High. **Dependencies:** 10, 23, 36. **Effort:** 4-8 days.
- **Tasks:** [ ] Predefine clinically relevant groups. [ ] Count per group/event before estimating. [ ] Report uncertainty and suppress unsafe small cells. [ ] Check site/population shift and missing data.
- **Tools/inputs:** Approved subgroup fields, held-out predictions, governance approval.
- **Deliverables:** Subgroup/generalization report.
- **Acceptance/testing:** No unsupported fairness claim; small groups reported as insufficient evidence; privacy thresholds met.
- **Risks:** Underrepresentation and re-identification. **Blocker:** final cohort unavailable.

### PHASE 41 - External Validation

- **Purpose/outcome:** Test transportability on an independent approved cohort. **Status:** BLOCKED (0%). **Priority:** High. **Dependencies:** 10, 36. **Effort:** 5-10 days after access.
- **Tasks:** [ ] Identify independent cohort with comparable target. [ ] Harmonize only defensible shared features. [ ] Freeze model before access to external labels. [ ] Report deviations and performance uncertainty.
- **Tools/inputs:** Second DUA/ethics, locked artifact, external data dictionary.
- **Deliverables:** External validation report.
- **Acceptance/testing:** External patient/site independence documented; no retraining on external test data; target criteria compared.
- **Risks:** Criterion/population shifts. **Blocker:** independent data access.

### PHASE 42 - Final Model Reporting and Model Card

- **Purpose/outcome:** Communicate methods, evidence and limits. **Status:** BLOCKED (0%). **Priority:** High. **Dependencies:** 36-41. **Effort:** 3-6 days.
- **Tasks:** [ ] Report cohort flow, source/license, target/index/horizon, features and missingness. [ ] Include split, preprocessing, architecture, baselines and metrics. [ ] State intended use, prohibited uses, uncertainty and limitations. [ ] Clinical review.
- **Tools/inputs:** Frozen analyses, model metadata, reporting template.
- **Deliverables:** Model card and reproducible results report.
- **Acceptance/testing:** Every numeric claim traceable to run artifacts; no accuracy or clinical claim without evidence.
- **Risks:** Overstating validation from internal test. **Blocker:** no trained model.

### PHASE 43 - Model and Preprocessing Artifact Versioning

- **Purpose/outcome:** Package compatible inference artifacts. **Status:** BLOCKED (0%). **Priority:** High. **Dependencies:** 24, 34-36, 42. **Effort:** 2-4 days.
- **Tasks:** [ ] Package model, preprocessors, schema, feature order, horizon, label mapping. [ ] Record hashes/runtime/model card. [ ] Validate load in clean environment. [ ] Store only where approved.
- **Tools/inputs:** TensorFlow SavedModel/Keras format, manifest, secure artifact store.
- **Deliverables:** Versioned model bundle and compatibility test.
- **Acceptance/testing:** Bundle loads and reproduces expected outputs; exact data/model version traceability; no patient data bundled.
- **Risks:** Mismatched preprocessing/model version. **Blocker:** no model artifact.

### PHASE 44 - Supabase PostgreSQL Architecture

- **Purpose/outcome:** Design secure relational persistence around approved data needs. **Status:** IN PROGRESS (50%). **Priority:** Medium. **Dependencies:** 01, 03, 08, 12. **Effort:** 3-6 days.
- **Tasks:** [x] Define provisional entities, keys, candidate constraints and indexes. [x] Separate patient, visit, outcome, prediction-request and model-version records. [ ] Obtain data-minimization/retention and clinical-field approval. [x] Document proposed Supabase network/service boundaries and unresolved RLS/JWT pattern.
- **Tools/inputs:** Approved schema, PostgreSQL, Supabase, SQLAlchemy.
- **Deliverables:** ER diagram, schema decisions, threat/access assumptions.
- **Acceptance/testing:** Provisional ER model and design constraints are documented; no direct identifiers are in the default patient entity. No executable migration or database test was run because clinical fields, retention, RLS session propagation, and hosting approval remain open.
- **Risks:** Supabase data residency/access suitability not institutionally approved. **Remaining:** stakeholder workflow, governance, feature-dictionary mapping, and security review before migration/live persistence.

### PHASE 45 - Supabase Authentication and Authorization

- **Purpose/outcome:** Enforce authenticated least-privilege access. **Status:** IN PROGRESS (30%; design only). **Priority:** Critical. **Dependencies:** 08, 44, 46. **Effort:** 4-8 days.
- **Tasks:** [x] Draft provisional roles/claims and access matrix. [x] Document RLS/service/API trust boundaries and required token-validation properties. [ ] Approve role provisioning, patient scope, session policy, and RLS connection pattern. [ ] Implement and test cross-user and unauthorized access after Phase 46 and governance review.
- **Tools/inputs:** Supabase Auth/PostgreSQL RLS, FastAPI security dependencies.
- **Deliverables:** Policy migrations, auth architecture, access matrix.
- **Acceptance/testing:** Provisional architecture and future test matrix documented in `16_PROVISIONAL_AUTHORIZATION_ARCHITECTURE.md`; no live Auth/RLS security test was run. Final deny-by-default tests and secret scanning remain required.
- **Risks:** RLS bypass via privileged credentials; restrict backend secrets and audit access.
- **Remaining/blocker:** Governance decisions, patient-scope definition, Phase 46 backend, and security review block executable authorization.

### PHASE 46 - FastAPI Backend Implementation

- **Purpose/outcome:** Implement typed API and service layers. **Status:** IN PROGRESS (25%; non-sensitive foundation only). **Priority:** Medium. **Dependencies:** 26, 43-45. **Effort:** 8-15 days.
- **Tasks:** [x] Add a minimal FastAPI app and typed health response schemas. [x] Add liveness and explicitly not-ready routes with no patient/model details. [x] Add isolated API dependency lock and health endpoint tests. [ ] Define approved patient/model Pydantic contracts. [ ] Implement authorized routers/services/repositories, SQLAlchemy sessions, Alembic workflow, safe errors/logging, and reviewed OpenAPI.
- **Tools/inputs:** Python 3.12, FastAPI, Pydantic, SQLAlchemy, Alembic, pytest.
- **Deliverables:** Backend package, API docs, and health/readiness tests for the initial slice.
- **Acceptance/testing:** `pytest` 17/17, data `unittest` 14/14, Ruff check/format, `pip check`, and `git diff --check` passed locally on Python 3.12.10. No database/migration/security integration test is applicable yet; full acceptance remains unmet.
- **Risks:** API becomes coupled to model-specific schema prematurely. **Remaining:** all clinical routes, auth, persistence, error/logging review, and integration tests.

### PHASE 47 - Patient and Visit Management

- **Purpose/outcome:** Authorized CRUD and chronology views for permitted records. **Status:** NOT STARTED (0%). **Priority:** High. **Dependencies:** 08, 44-46. **Effort:** 5-10 days.
- **Tasks:** [ ] Implement patient create/read under approved pseudonymous schema. [ ] Add visits with date/type validation. [ ] Reject invalid references/duplicate visit IDs. [ ] Sort retrieval chronologically and enforce ownership/role.
- **Tools/inputs:** FastAPI, SQLAlchemy, Supabase PostgreSQL/RLS, pytest.
- **Deliverables:** Patient/visit endpoints and integration tests.
- **Acceptance/testing:** Unauthorized access denied; duplicate/invalid chronology handled by documented rule; no direct identifiers in fixtures/logs.
- **Risks:** Do not enable real records before governance/security review.

### PHASE 48 - Prediction and Model Inference Service

- **Purpose/outcome:** Serve only approved model outputs. **Status:** NOT STARTED (0%). **Priority:** Critical. **Dependencies:** 43, 46-47. **Effort:** 5-10 days.
- **Tasks:** [ ] Load model/preprocessor by immutable version. [ ] Validate patient history and sufficient pre-index sequence. [ ] Return clear unavailable/error states. [ ] Record safe model metadata; no probability unless calibrated and approved.
- **Tools/inputs:** FastAPI, artifact manifest, sequence builder, Pydantic.
- **Deliverables:** Inference service and compatibility tests.
- **Acceptance/testing:** No training in request path; bad/incomplete data returns no prediction; version and disclaimer accompany result.
- **Risks:** App currently has no approved model. Never fabricate a class on failure.

### PHASE 49 - UI/UX Architecture and Design System

- **Purpose/outcome:** Design accessible research workflow. **Status:** IN PROGRESS (40%; provisional route/state design). **Priority:** Medium. **Dependencies:** 03, 46, 48. **Effort:** 3-6 days.
- **Tasks:** [x] Define provisional routes/navigation and patient timeline. [x] Specify loading/error/unauthorized/unavailable/empty states. [x] Inventory shared components and keyboard/screen-reader requirements. [x] Specify persistent research disclaimer and future model provenance. [ ] Select and measure final design tokens and responsive components. [ ] Review workflow with representative users and complete accessibility checks.
- **Tools/inputs:** React stack, UI/UX handoff, user feedback.
- **Deliverables:** Provisional screen flow, component/state inventory, and accessibility requirements in `17_PROVISIONAL_UI_UX_ARCHITECTURE.md`.
- **Acceptance/testing:** Design artifact reviewed for consistency with the mandatory six modules and no-model state; no user study, visual contrast test, responsive implementation, or screen-reader test has occurred. Full acceptance remains unmet.
- **Risks:** No representative clinical users confirmed. **Remaining:** confirm workflow terminology, finalize tokens, and validate responsive/accessibility behavior.

### PHASE 50 - React Frontend Implementation

- **Purpose/outcome:** Build approved React/TypeScript app. **Status:** IN PROGRESS (60%; static shell only). **Priority:** Medium. **Dependencies:** 26, 45-46, 49. **Effort:** 10-20 days.
- **Tasks:** [x] Scaffold Vite/React/TypeScript with the relevant approved UI/runtime libraries. Form/chart packages remain deferred until approved form/data use exists. [x] Create responsive route/layout/component structure for module entry points. [x] Add typed API base URL and explicit unconfigured auth-state type; no provider or token handling. [x] Add lint/type/test scripts and a non-secret public API URL example. [ ] Implement approved Auth integration, protected-route behavior, backend contract integration, and error boundaries after their dependencies pass.
- **Tools/inputs:** React, TypeScript, Vite, Tailwind, shadcn/ui, Router, TanStack Query, RHF, Zod, Recharts, Lucide.
- **Deliverables:** Static frontend foundation and module unavailable states in `frontend/`.
- **Acceptance/testing:** Node 24.22.2 `typecheck`, ESLint, Vitest 8/8, Vite production build, and `npm audit` (0 vulnerabilities) passed. Desktop and mobile rendering inspected; no secrets or patient data in the static bundle. Auth route guards, production error boundaries, real API integration, and formal accessibility/contrast audit are not yet implemented.
- **Risks:** Frontend may not access sensitive DB directly. All patient data must be mediated by backend.

### PHASE 51 - Patient, Visit History, and Prediction Screens

- **Purpose/outcome:** Deliver functional protected research screens. **Status:** NOT STARTED (0%). **Priority:** High. **Dependencies:** 47-50. **Effort:** 8-15 days.
- **Tasks:** [ ] Patient list/detail with pseudonymous IDs. [ ] Chronological timeline with missingness/observation status. [ ] Validated forms using RHF/Zod. [ ] Prediction screen with insufficient-data state, model version and disclaimer.
- **Tools/inputs:** Approved API schemas, React components, Recharts if supported evaluation view.
- **Deliverables:** Screens and accessibility tests.
- **Acceptance/testing:** Forms match server validation; sorted timeline; no success state until backend responds; screen reader/keyboard basics checked.
- **Risks:** Avoid visual red/green diagnostic cues and unsupported risk percentages.

### PHASE 52 - Frontend and Backend Integration

- **Purpose/outcome:** Integrate auth, requests, errors and prediction flow. **Status:** NOT STARTED (0%). **Priority:** High. **Dependencies:** 45-51. **Effort:** 4-8 days.
- **Tasks:** [ ] Connect typed client and token flow. [ ] Test loading/retry/expired-auth states. [ ] Validate CORS/CSRF/session behavior for chosen auth design. [ ] Verify API response model version/disclaimer.
- **Tools/inputs:** FastAPI OpenAPI contract, TanStack Query, local test environment.
- **Deliverables:** Integrated app and end-to-end flow tests.
- **Acceptance/testing:** No patient record leaks across users; errors do not reveal sensitive server details; full authorized flow works with non-sensitive test fixtures.
- **Risks:** Auth token exposure and stale model schema. Keep token storage/security design reviewed.

### PHASE 53 - Application Security and Privacy Audit

- **Purpose/outcome:** Verify security controls before any deployment. **Status:** IN PROGRESS (30%; threat model only). **Priority:** Critical. **Dependencies:** 08, 45-48, 52. **Effort:** 5-10 days.
- **Tasks:** [x] Document proposed assets, actors, trust boundaries, and threat scenarios across frontend/API/Supabase/offline ML. [x] Record future RLS, auth, secret/log, model artifact, and privacy verification gates. [ ] Test implemented RLS/authorization/IDOR. [ ] Scan deployed configuration and verify encryption, retention, audit logging, incident procedure, and institutional acceptance.
- **Tools/inputs:** Security review checklist, test deployment with synthetic fixtures, Supabase policies.
- **Deliverables:** Provisional threat register and verification plan in `18_PROVISIONAL_THREAT_MODEL.md`.
- **Acceptance/testing:** Design-only review against current architecture and known constraints. No live configuration scan, RLS/IDOR test, penetration test, encryption/backup validation, or DPO/PI approval was performed; full audit acceptance remains unmet.
- **Risks:** Student prototype is not automatically compliant or production-secure.

### PHASE 54 - Unit, Integration, and End-to-End Testing

- **Purpose/outcome:** Verify complete data-to-app behavior. **Status:** IN PROGRESS (30%; foundation tests only). **Priority:** High. **Dependencies:** 27, 46-53. **Effort:** 8-15 days.
- **Tasks:** [x] Add deterministic unit tests for existing data-contract/split guards and non-sensitive API/frontend foundation states. [ ] Complete approved-sequence, leakage, train-only preprocessing, and label property tests when a valid cohort contract exists. [ ] Integration test DB migrations/RLS/API after authorized DB and auth implementation. [ ] E2E test auth, patient/visit flow, and model-unavailable response after those screens/services exist. [ ] Record full coverage and failures.
- **Tools/inputs:** pytest, FastAPI TestClient/httpx, frontend test framework/browser runner.
- **Deliverables:** Data and foundation unit test suites in `data/tests`, `backend/tests`, and `frontend/src`.
- **Acceptance/testing:** Python pytest 17/17 and data `unittest` 14/14 pass on Python 3.12.10; frontend Vitest 8/8 passes on Node 24.22.2. Tests verify split guards and unavailable app behavior only; no implemented auth, RLS, DB, patient CRUD, or inference path exists to integration-test. Full acceptance remains unmet.
- **Risks:** Coverage percent alone does not prove clinical correctness.

### PHASE 55 - Performance and Reliability Testing

- **Purpose/outcome:** Characterize supported workload and failure behavior. **Status:** IN PROGRESS (20%; test design only). **Priority:** Medium. **Dependencies:** 48, 52, 54. **Effort:** 3-6 days.
- **Tasks:** [x] Specify guarded test progression, candidate measurements, failure scenarios, and report contents. [ ] Measure API latency and inference memory with approved fixture boundaries. [ ] Test database/model failures and malformed requests after those paths exist. [ ] Establish service targets with the responsible owner. [ ] Verify bounded resource use in an authorized environment.
- **Tools/inputs:** Non-sensitive fixtures, profiling/load tools, deployment-like environment.
- **Deliverables:** Provisional plan in `MS_Prediction_Project_Handoff/21_PROVISIONAL_PERFORMANCE_RELIABILITY_PLAN.md`; measured report remains pending.
- **Acceptance/testing:** No workload target or performance test has been approved/run. Future acceptance requires targets and environment to be recorded, failures to be safe/explicit, and patient values to be absent from performance logs.
- **Risks:** Free hosting resources are variable and not production SLA.

### PHASE 56 - CI/CD and Deployment Preparation

- **Purpose/outcome:** Automate safe build/test and controlled releases. **Status:** IN PROGRESS (50%; validation CI only). **Priority:** Medium. **Dependencies:** 26, 53-55. **Effort:** 3-6 days.
- **Tasks:** [x] Define GitHub checks for Python, API, and frontend tests/type/lint/build/audit. [x] Keep CI secretless with repository read-only permissions. [ ] Design approved secret/environment handling if deployment is authorized. [ ] Separate dev/staging/prod configuration and document rollback/migration sequencing after governance and release decisions.
- **Tools/inputs:** GitHub Actions, approved runtime/container config, secret manager.
- **Deliverables:** Updated read-only workflow `.github/workflows/ci.yml`; no deployment runbook yet.
- **Acceptance/testing:** Workflow syntax reviewed; local commands passed; GitHub Actions run 41892334989 passed both Python and frontend jobs for `a525779`. No secrets, patient files, migration steps, or deployment stages are part of CI. Full release acceptance remains unmet.
- **Risks:** CI must not ingest restricted patient data or artifacts.

### PHASE 57 - Production Deployment Readiness

- **Purpose/outcome:** Approve suitable hosting and deployment boundary. **Status:** NOT STARTED (0%). **Priority:** Critical. **Dependencies:** 08, 43, 53-56. **Effort:** 3-8 days after governance.
- **Tasks:** [ ] Confirm data residency and institutional permission. [ ] Assess Supabase plan/RLS/backups and application host. [ ] Configure TLS/domain/access restrictions. [ ] Obtain PI/security approval before data migration.
- **Tools/inputs:** Approved governance, deployment architecture, vendor terms.
- **Deliverables:** Deployment decision and approved release checklist.
- **Acceptance/testing:** Environment satisfies data agreement/security requirements; secrets, access, recovery and monitoring verified; research-only labeling visible.
- **Risks:** Free hosting is not presumed appropriate for health data.

### PHASE 58 - Monitoring, Logging, and Model Drift

- **Purpose/outcome:** Monitor service and data quality without exposing patient data. **Status:** IN PROGRESS (25%; design only). **Priority:** Medium. **Dependencies:** 43, 48, 57. **Effort:** 3-6 days.
- **Tasks:** [x] Document candidate uptime/error/latency signals and forbidden telemetry fields. [x] Specify aggregate-only, approval-gated data/feature drift review. [x] Specify conditional safe model-version and prediction-count metrics. [ ] Approve thresholds, alert owner, retention, deployment and validate alerts.
- **Tools/inputs:** Hosting metrics, privacy-safe logging, data quality monitor.
- **Deliverables:** Provisional observability design in `MS_Prediction_Project_Handoff/19_PROVISIONAL_OBSERVABILITY_DESIGN.md`; dashboard and operational runbook remain pending.
- **Acceptance/testing:** Design prohibits direct identifiers and clinical payloads in logs/metrics and states drift is review-only. No deployed log path, alert, drift monitor, or access/retention policy exists; phase acceptance remains unmet.
- **Risks:** Monitoring itself can create sensitive records.

### PHASE 59 - Backup, Disaster Recovery, and Operations

- **Purpose/outcome:** Recover approved data/service safely. **Status:** NOT STARTED (0%). **Priority:** High. **Dependencies:** 44-45, 53, 57. **Effort:** 3-6 days.
- **Tasks:** [ ] Define backup frequency/retention/encryption. [ ] Test restore to isolated environment. [ ] Define incident contacts, key rotation, access revocation and data deletion. [ ] Review migration recovery steps.
- **Tools/inputs:** Supabase backup features, institutional policies, operations runbook.
- **Deliverables:** Backup/restore procedure and test record.
- **Acceptance/testing:** Restore test meets approved recovery objective; backups access-controlled; incident/rotation procedure rehearsed.
- **Risks:** Free-tier database lifecycle/retention unsuitable for continuity.

### PHASE 60 - Clinical Workflow and Usability Review

- **Purpose/outcome:** Evaluate usability without claiming clinical effectiveness. **Status:** IN PROGRESS (20%; protocol only). **Priority:** High. **Dependencies:** 03, 49-54. **Effort:** 3-7 days.
- **Tasks:** [x] Draft no-data walkthrough protocol for the static prototype. [ ] Obtain any required institutional determination and conduct a walkthrough with intended research users. [ ] Test comprehension of research-only limitation and unavailable states. [ ] Document de-identified findings, fix priorities, and retest.
- **Tools/inputs:** Prototype, task script, consent/ethics rules if applicable.
- **Deliverables:** Draft protocol in `MS_Prediction_Project_Handoff/20_PROVISIONAL_USABILITY_WALKTHROUGH.md`; usability report and issue disposition remain pending.
- **Acceptance/testing:** No participant sessions or acceptance evidence yet. Required future review must show participants understand research-only limitations; critical use errors must be addressed and retested. Current protocol is limited to the static shell and has no clinical workflow validation.
- **Risks:** Usability feedback is not evidence of clinical utility.

### PHASE 61 - Final Documentation and Reproducibility Package

- **Purpose/outcome:** Deliver reproducible technical/research handover. **Status:** NOT STARTED (0%). **Priority:** High. **Dependencies:** 24, 42-60. **Effort:** 5-10 days.
- **Tasks:** [ ] Document setup, data access constraints, contracts, API, model protocol and tests. [ ] Publish non-sensitive manifests/model card. [ ] Reproduce from clean environment. [ ] Reconcile architecture docs with implemented system.
- **Tools/inputs:** Actual code/configs, approved docs, test and experiment outputs.
- **Deliverables:** Final README, user/admin guide, reproducibility pack.
- **Acceptance/testing:** A second team member can reproduce checks/results without access to unauthorized patient values; docs match code.
- **Risks:** Never include private records/secrets in example commands or screenshots.

### PHASE 62 - Final Project Acceptance and Academic Presentation

- **Purpose/outcome:** Demonstrate only verified project results. **Status:** NOT STARTED (0%). **Priority:** High. **Dependencies:** 36, 42, 53-61. **Effort:** 5-8 days.
- **Tasks:** [ ] Verify acceptance checklist and supervisor sign-off. [ ] Prepare architecture/data/model results with true counts and limitations. [ ] Rehearse demo on approved synthetic/de-identified fixture. [ ] Prepare viva responses on leakage, censoring and generalizability.
- **Tools/inputs:** Final code, reports, permitted demo data.
- **Deliverables:** Academic report/slides/demo and acceptance record.
- **Acceptance/testing:** Every claim traced to evidence; no fabricated results; app has visible disclaimer; demonstration uses permitted data.
- **Risks:** Presentation pressure may encourage unsupported accuracy claims.

### PHASE 63 - Maintenance and Future Research Roadmap

- **Purpose/outcome:** Define stewardship after academic delivery. **Status:** NOT STARTED (0%). **Priority:** Medium. **Dependencies:** 57-62. **Effort:** 2-4 days.
- **Tasks:** [ ] Name maintenance owner and support horizon. [ ] Document dependency/security updates, data access renewal, model review and retirement triggers. [ ] Define future cohort expansion/external validation proposals. [ ] Archive or delete data under agreement.
- **Tools/inputs:** Operations, DUA, model card, institutional lifecycle policy.
- **Deliverables:** Maintenance plan and research backlog.
- **Acceptance/testing:** Owner, review cadence, funding/access assumptions and retirement procedure approved.
- **Risks:** Model performance may drift; changes require renewed validation, not automatic promotion.

## D. Blocker register

| Blocker ID | Related phases | Description / why it blocks | Required resolution | Responsible role | Status |
|---|---|---|---|---|---|
| B-01 | 02, 04, 14, 15, 25 | Operational index/horizon and endpoint rules are not confirmed; public files lack patient event/follow-up dates. | Clinical investigator and supervisor approve target protocol using candidate cohort feasibility. | PI / neurologist / statistician | OPEN - CRITICAL |
| B-02 | 07-10, 13-25, 28-43 | No approved longitudinal source with genuine repeated dated observations and reliable outcomes. | Obtain permission and a feasibility extract; verify cohort counts, event counts, follow-up and feature definitions. | PI / data owner / institutional research office | OPEN - CRITICAL |
| B-03 | 05, 08, 13-17 | Clinical criteria, inclusion rules, codebooks and adjudication need expert approval. | Appoint clinician reviewer and record adjudication/governance sign-off. | PI / neurologist / ethics office | OPEN - HIGH |
| B-04 | 23, 25, 28-43 | Eligible sample size and event count unknown; 2,000 is aspirational and not evidence of adequate power. | Assess actual eligible patients/events and uncertainty before choosing model complexity/splits. | Biostatistician / ML lead | OPEN - HIGH |
| B-05 | 08, 44-59 | Supabase/cloud hosting suitability for eventual health data is not approved. | Data-governance review of residency, access, retention, security, RLS and institutional policy. | PI / security lead / DPO | OPEN - HIGH |
| B-06 | 03, 08, 45-54 | Mandatory doctor-facing app and six modules are project-owner approved. Detailed clinical workflow, role policy, and any institutionally required review remain to be established before real-data use. | Complete user/role workflow review and obtain applicable institutional approvals before handling real clinical data. | Project team / institutional authority | OPEN - MEDIUM |
| B-07 | 26-27 | Approved stack was decided; shared developer environment and CI were pending. | Select pinned tooling compatible with Python 3.12 and implement reproducible setup/CI. | Engineering lead | CLOSED - Python 3.12.10 and 3.13 local checks pass; GitHub Actions run 41892334989 passed for commit `a525779`. |

## E. Milestone register

| Milestone | Exit condition | Target phase | Status |
|---|---|---:|---|
| M0 - Current repository baseline verified | Inventory, public-source audit and current NO-GO recorded. | 00 | ACHIEVED |
| M1 - Research protocol approved | Target, index, horizon, eligibility and clinical endpoint signed off. | 02-05 | BLOCKED |
| M2 - Governed cohort feasibility approved | Data access, ethics/governance route and extract feasibility established. | 07-10 | BLOCKED |
| M3 - Longitudinal dataset accepted | Cohort, labels, visits, feature mapping, QC and provenance pass gates. | 13-24 | BLOCKED |
| M4 - Data pipeline ready | Contracts, splits, preprocessing, sequences and tests pass for approved cohort. | 25-27, 31 | BLOCKED |
| M5 - Baselines evaluated | Valid baseline training/evaluation completed on approved patient partitions. | 28-30 | BLOCKED |
| M6 - Hybrid model evaluated | Hybrid model has fair validation/test comparison and limitation report. | 31-42 | BLOCKED |
| M7 - Model artifact approved for inference | Versioned model/preprocessor passes compatibility/security review. | 43, 48 | BLOCKED |
| M8 - Application integrated | Authorized React/FastAPI/Supabase flow and tests pass. | 44-54 | NOT STARTED |
| M9 - Deployment approved | Governance, security, recovery and operational readiness approved. | 55-59 | NOT STARTED |
| M10 - Academic handover accepted | Reproducible report/demo and supervisor acceptance. | 60-63 | NOT STARTED |

## F. Change log

| Date | Phase(s) | Previous -> new | Progress change | Work/evidence | Remaining blockers |
|---|---|---|---|---|---|
| 2026-11-04 | 00, 06, 09, 11-12, 16, 18-19 | Audited current public-source activity -> COMPLETE | Captured as 8 completed bounded phases in this baseline; no historical phase percentages claimed. | Public workbooks, hash audit, interim mapping, label/feature/quality reports, readiness NO-GO; see linked repo evidence. | Suitable longitudinal data and operational target remain absent. |
| 2026-11-04 | 01-03, 26-27 | Existing planning/code evidence -> IN PROGRESS | 25%, 50%, 25%, 50%, 50% respectively, based on documented tasks in phase records. | Handoff documents, approved technology decision, data contract, guarded utilities, last logged 13 passing tests. | Sign-off, environment implementation, approved cohort contract/tests. |
| 2026-11-04 | 04-05, 07-08, 10, 13-15, 17, 20-25, 28-43 | No execution / unmet prerequisite -> BLOCKED | 0% credited. | Repository shows missing dates/outcomes, no selected horizon, no final features, no model cohort. | Resolve blockers B-01 through B-04; do not advance by generating synthetic data. |
| 2026-11-04 | 44-63 | No execution evidence -> NOT STARTED | 0% credited. | No backend, frontend, database migrations, model, deployment, or operations artifacts found. | Application, model, governance and data prerequisites as listed. |
| 2026-11-04 | 02 | IN PROGRESS -> BLOCKED | Remains at 50%; the task definition and label handling principles are documented, but no operational target is approved. | User-confirmed future CIS-to-MS objective; public-source label audit and longitudinal data contract reviewed. | Obtain approved longitudinal data with dated visits, conversion/follow-up dates, and clinician/supervisor adjudication; do not choose a horizon from the current public workbooks. |
| 2026-11-04 | 01 | IN PROGRESS 75% -> COMPLETE 100% | Owner-approved scope is reconciled and six-module acceptance criteria are documented. | User explicitly approved both deliverables and all six app modules; aligned project documents and acceptance criteria. No supervisor approval is claimed. | Any institutionally required supervisor review for clinical data use is a separate governance item. |
| 2026-11-04 | 26 | IN PROGRESS 50% -> IN PROGRESS 90% | Overall score 16.8% -> 17.4%; remaining acceptance check is 3.12 CI. | Added Python 3.12/Node 24 runtime pins, locked developer tools, isolated environment guide, secret template/ignore rules, Ruff standards, formatting cleanup, and read-only GitHub CI. `unittest` 13/13, pytest 13/13, Ruff check and format check passed locally on Python 3.13. Raw-workbook tests explicitly skip in CI when local-only source files are absent. | Python 3.12 is not installed locally; verify the 3.12 CI run after push. ML/API dependency locks are deferred to their implementation phases; no model or app dependencies are installed. |
| 2026-11-04 | 26 | IN PROGRESS 90% -> COMPLETE 100% | Overall score 17.4% -> 17.6%; completed count 9 -> 10. | Installed Python 3.12.10 in an isolated environment; `unittest` 13/13, pytest 13/13, Ruff lint/format, and `pip check` pass under Python 3.12.10. Previous Python 3.13.5 checks also pass. CI is pushed and queued, not reported as passed. | ML/API dependency locks are deferred to their implementation phases; no model or app dependencies are installed. No next phase meets its dependencies while target/cohort and evaluation prerequisites remain blocked. |
| 2026-11-04 | 27 | IN PROGRESS 50% -> BLOCKED 60% | Overall score 17.6% -> 17.7%; in-progress count 2 -> 1 and blocked count 32 -> 33. | Added explicitly test-only synthetic split checks for seeded reproducibility, disjoint patient assignments, complete eligible coverage, and exclusion of unknown outcomes. 14/14 unittest and pytest checks pass on Python 3.12.10. Added a phase-by-phase dependency reassessment. | Phase 25 and approved-cohort-specific tests remain blocked; no actual split manifest or clinical dataset was created. Phase 44 is next for provisional database architecture only. |
| 2026-11-04 | 44 | NOT STARTED 0% -> IN PROGRESS 50% | Overall score 17.7% -> 18.5%; in-progress count 1 -> 2 and not-started count 20 -> 19. | Added a provisional logical ER model, candidate entity keys/relationships/constraints/indexes, and proposed service boundaries in `15_PROVISIONAL_DATA_ARCHITECTURE.md`. No migrations, cloud resources, credentials, or patient records were created. | Final clinical fields, retention, role/RLS propagation, hosting and governance approval remain open; real database work is not authorized by this design artifact. |
| 2026-11-04 | 45 | NOT STARTED 0% -> IN PROGRESS 30% | Overall score 18.5% -> 19.0%; in-progress count 2 -> 3 and not-started count 19 -> 18. | Added provisional identity/authentication trust boundaries, access matrix, credential rules, future security tests, and decision gates in `16_PROVISIONAL_AUTHORIZATION_ARCHITECTURE.md`. Supabase documentation was checked; no project, credentials, policies, or patient records were created. | Role provisioning, patient scope, session policy, RLS request context, backend integration, and institutional security review remain unresolved; no live security tests were run. |
| 2026-11-04 | 46 | NOT STARTED 0% -> IN PROGRESS 25% | Overall score 19.0% -> 19.4%; in-progress count 3 -> 4 and not-started count 18 -> 17. | Added a health-only FastAPI app, separate pinned API dependencies, non-sensitive liveness/readiness routes, and tests. Full pytest 17/17, data unittest 14/14, Ruff and package checks pass locally on Python 3.12.10. | Auth, DB, patient, and model endpoints remain gated; hosted CI result not checked and no clinical integration is claimed. |
| 2026-11-04 | 49 | NOT STARTED 0% -> IN PROGRESS 40% | Overall score 19.4% -> 20.0%; in-progress count 4 -> 5 and not-started count 17 -> 16. | Added provisional app routes, six-module flow, component inventory, loading/error/access-denied/unavailable states, research disclaimer placement, and accessibility checklist in `17_PROVISIONAL_UI_UX_ARCHITECTURE.md`. | Representative-user review, final tokens, visual contrast, responsive implementation, and accessibility testing remain outstanding. |
| 2026-11-05 | 50 | NOT STARTED 0% -> IN PROGRESS 60% | Overall score 20.0% -> 20.9%; in-progress count 5 -> 6 and not-started count 16 -> 15. | Added a static responsive React/TypeScript/Vite app shell, module routes, no-auth/no-data states, typed API URL configuration, reusable Tailwind/shadcn-style components, and tests. Node 24.22.2 typecheck/lint/Vitest 8/8/build and npm audit 0 findings pass. | No Supabase Auth, patient/API integration, route authorization, error boundary, user workflow review, or formal accessibility audit. |
| 2026-11-05 | 53 | NOT STARTED 0% -> IN PROGRESS 30% | Overall score 20.9% -> 21.4%; in-progress count 6 -> 7 and not-started count 15 -> 14. | Added provisional assets, actors, trust boundaries, 16 threat scenarios, required future controls/evidence, and stop conditions in `18_PROVISIONAL_THREAT_MODEL.md`. | No implementation audit, live security tests, penetration test, institutional acceptance, or deployment review has occurred. |
| 2026-11-05 | 54 | NOT STARTED 0% -> IN PROGRESS 30% | Overall score 21.4% -> 21.9%; in-progress count 7 -> 8 and not-started count 14 -> 13. | Added frontend API URL normalization and fail-closed auth-placeholder unit tests. Combined foundation coverage is pytest 17/17, data unittest 14/14, and frontend Vitest 8/8. | No end-to-end user workflow, auth/RLS denial, DB integration, valid model path, or approved-cohort leakage test could run. |
| 2026-11-05 | 56 | NOT STARTED 0% -> IN PROGRESS 40% | Overall score 21.9% -> 22.5%; in-progress count 8 -> 9 and not-started count 13 -> 12. | Extended read-only GitHub Actions to install locked API/dev dependencies, run Python/unittest/pytest/Ruff checks, and run Node 24 typecheck/lint/Vitest/build/npm audit. | Hosted workflow result not yet checked; no secrets, data files, deployment stages, DB migrations, or release environments included. |
| 2026-11-05 | 56 | IN PROGRESS 40% -> IN PROGRESS 50% | Hosted validation workflow passed; score is subsequently recalculated with Phase 58 design work. | GitHub Actions run 41892334989 passed for commit `a525779`; Python/API checks and frontend checks all completed successfully. | Deployment secrets/environments, release controls, rollback, and environment separation remain unimplemented and governance-gated. |
| 2026-11-05 | 58 | NOT STARTED 0% -> IN PROGRESS 25% | Overall score 22.5% -> 23.0%; in-progress count 9 -> 10 and not-started count 12 -> 11. | Added provisional privacy-safe observability design covering metric allowlist, prohibited fields, log contract, drift review, and future approval/test gates. | No deployed service, approved cohort/model, telemetry, dashboard, alert owner, retention policy, or alert test; Phases 43, 48, and 57 remain dependencies. |
| 2026-11-05 | 60 | NOT STARTED 0% -> IN PROGRESS 20% | Overall score 23.0% -> 23.4%; in-progress count 10 -> 11 and not-started count 11 -> 10. | Drafted a no-data walkthrough for the static shell, with research-only comprehension, unavailable states, accessibility checks, and privacy limits. | No participant sessions, institutional determination, real patient screens, service workflow, usability findings, fixes, or retest. |
| 2026-11-05 | 55 | NOT STARTED 0% -> IN PROGRESS 20% | Overall score 23.4% -> 23.7%; in-progress count 11 -> 12 and not-started count 10 -> 9. | Drafted guarded performance/reliability scenarios, candidate measurements, failure cases, and reporting requirements. | No service/model workload, target, database failure test, or deployment-like measurement is approved or run. |

## How to maintain this plan

1. Read this file before starting future project work and identify phase prerequisites.
2. Only change statuses after verifying repository evidence and running relevant checks. Record the exact evidence and date.
3. A phase is COMPLETE only when all mandatory acceptance criteria pass; file creation alone is insufficient.
4. For each update, revise tracker status/percentage, the detailed checklist, blockers/milestones as needed, and append a change-log row. Preserve old history.
5. Treat percentage as evidence-weighted checklist progress within a phase. Keep overall calculation phase-weighted and recalculate the arithmetic explicitly.
6. Do not mark external approval or dataset access complete based on a request being drafted or submitted.
7. Keep raw/patient-level data and secrets out of Git, logs, screenshots, public cloud and frontend bundles unless explicit institutional authorization allows the exact handling.
8. Keep the approved stack unchanged. Discuss any alternative with the user before introducing it.
9. Do not start training until Phases 02, 04-05, 08, 10, 13-27 pass their applicable gates. Preserve NO-GO otherwise.
10. Never report model performance, clinical benefit, fairness, or deployment readiness without direct evidence.
