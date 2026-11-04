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

### D-02 — Exact prediction target
Current presentation wording says MS / Non-MS. Confirm:
- Is this current MS status classification at a defined visit?
- Or is the task future conversion from CIS to MS within a fixed horizon?
- Or is it another future outcome?

These are different prediction tasks and need different labels, cohorts, and evaluation.

**Resolved by current user instruction:** The intended task is future conversion
from confirmed CIS to MS, not cross-sectional MS/non-MS classification. The
specific index definition and horizon remain open under D-03.

### D-03 — Label source and timing
- Who/what defines MS and Non-MS?
- Does the target apply at baseline, each visit, or a later follow-up?
- How are uncertain or missing labels handled?
- What is the prediction index time?

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

### D-06 — Application requirement
Is a working web app required for the final deliverable, or is a reproducible ML pipeline/notebook sufficient?

### D-07 — Backend and frontend
Recommended simple default: Flask + HTML templates + Bootstrap. Confirm or select FastAPI/React only if needed.

### D-08 — Database
Recommended local default: SQLite. Confirm whether a persistent database or PostgreSQL deployment is needed.

### D-09 — Authentication
Is the app local/demo only, or will multiple authorized users access it? Real sensitive data require stronger access controls.

### D-10 — Deployment
Will the final project run locally, in a lab, or be hosted? Do not deploy sensitive data to an unapproved service.

### D-11 — Output semantics
Should the interface show only the predicted class, or also a probability? Probability requires calibration/threshold decisions.

### D-12 — Final model choice
Confirm RNN → LSTM as the desired experiment, but allow baseline comparison and a no-go recommendation if the data do not support it.

## Agent instruction

Resolve blocking decisions using available documentation and user/supervisor direction. Do not manufacture answers. If an answer is unavailable, record it as unresolved and work only on non-blocked tasks (e.g., repository scaffolding, schema-independent tests, or synthetic UI examples clearly marked as demo data).
