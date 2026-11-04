# 01 — Product Requirements Document (PRD)

## 1. Product summary

NeuroPredict-MS is a research and educational system with two mandatory deliverables: (A) a reproducible ML research pipeline studying future CIS-to-MS conversion from permitted genuine longitudinal records, and (B) a doctor-facing web application for authorized pseudonymous patient and visit management and, only after model validation, research prediction and result history. It is not a diagnostic or treatment system.

The target is confirmed conversion from CIS to MS after a defined index date and within a clinically justified future horizon. The index rule, horizon, cohort eligibility, diagnostic-criteria version, and adjudication method remain open pending a suitable cohort and clinical review. The Mexican and Lithuanian interim datasets do not support the intended target and must not be used as a surrogate classification task.

## 2. Goals and success criteria

- Preserve provenance and validate approved patient/visit/outcome data.
- Use only information available on or before the prediction index; split by patient and fit preprocessing on training patients only.
- Compare suitable classical baselines with the proposed SimpleRNN → LSTM → Dense model only if the approved cohort supports genuine sequences.
- Report valid held-out patient evaluation, class-wise metrics, uncertainty where feasible, and limitations without unsupported clinical claims.
- Deliver all six application modules in Section 5, with authenticated, authorized access and a mandatory research-only interface.
- Keep prediction unavailable until a compatible, tested, versioned model and preprocessing artifact are approved.
- Reproduce the research pipeline and application checks from documented instructions and obtain supervisor acceptance.

The aspiration of 2,000 patients is not a fabricated-data target or a guarantee of reliable performance.

## 3. Non-goals and boundaries

- Clinical diagnosis, treatment recommendations, or autonomous care decisions.
- Cross-sectional MS-versus-healthy/control classification as a replacement for the approved future CIS-to-MS research question.
- Raw MRI image processing or lesion segmentation; only source-supported structured measurements may be considered.
- Real patient use, prospective clinical deployment, regulatory approval, or claims of clinical utility.
- Accessing, storing, or hosting identifiable/restricted data without source permission and institutional governance approval.
- Training or prediction using fabricated patient records, dates, labels, or visits.

## 4. User roles and user stories

### Doctor / authorized application user

- I can securely sign in and out, and can access only the role-authorized functions and records.
- I can register and manage a pseudonymous patient record without entering direct identifiers.
- I can add and review genuine dated visits in chronological order.
- I can enter only approved clinical fields with valid units, dates, and validation feedback.
- I can request a research prediction only when the history is eligible and a validated compatible model is available; otherwise I receive an explicit unavailable reason.
- I can inspect actual prior prediction records, request time, model version, and research disclaimer.

### Student / researcher / administrator

- I can inspect approved source definitions, data quality, and provenance.
- I can run reproducible validation, patient-level split, train-only preprocessing, and sequence generation.
- I can train and evaluate baselines and the hybrid model only when data gates pass.
- I can maintain versioned artifacts and provide an evidence-based research report.

## 5. Mandatory application modules

| ID | Module | Required capability | Gate / primary acceptance |
|---|---|---|---|
| APP-01 | Doctor login and authentication | Secure login/logout, authenticated sessions, role authorization, protected routes and APIs. | Unauthenticated and unauthorized requests are denied; no credentials or service keys in frontend. |
| APP-02 | Patient registration and management | Create, view, update permitted fields, search/manage records, assign unique pseudonymous patient IDs. | IDs are unique and not derived from direct identifiers; unauthorized access is denied. |
| APP-03 | Patient visit history | Link multiple genuine visits to the correct patient and display visit dates and history chronologically. | Relationships and ordering are correct; duplicate/invalid visits are handled explicitly. |
| APP-04 | Clinical data management | Enter/manage source-approved assessments and available structured MRI measurements, retaining measurement dates and units. | Schema, ranges, units, missingness and field permissions are validated; no unsupported field is invented. |
| APP-05 | Research prediction interface | Submit eligible patient history through FastAPI to a compatible validated model; display result, limitations and disclaimer. | Prediction is disabled or returns unavailable until approved artifact, data, and sufficient history exist; failures never fabricate a result. |
| APP-06 | Prediction history and results | Store/retrieve actual requests and results with timestamps, patient association, model version and audit metadata. | Only actual service outcomes are recorded; model lineage and authorization are verified. |

Detailed backend, database, security, validation, test, and acceptance criteria are in the SRS and `13_ACCEPTANCE_CRITERIA.md`.

## 6. Machine-learning research requirements

- Candidate dataset: only a permitted cohort with confirmed baseline CIS, stable pseudonymous linkage, genuine dated visits, outcome evidence, conversion date where applicable, and last follow-up date.
- Target labels: Class 1 is confirmed conversion after index and within the approved horizon; Class 0 requires adequate follow-up through that horizon; uncertain/insufficient outcomes remain unknown/censored.
- Do not use patient ID, visit ID, conversion date, final diagnosis, post-index observations, or future follow-up as input features.
- Compare baseline models and the proposed SimpleRNN(return_sequences=True) → LSTM → Dense output architecture on the same patient-level partitions if eligible data support it.
- Keep final test patients untouched; report metrics appropriate to class counts and study design. Do not claim accuracy until a valid experiment exists.

## 7. Product priorities and dependencies

All six app modules are mandatory final deliverables. Their implementation is sequenced by the root master plan and remains downstream of data governance and design gates. Authentication and secure persistence precede real-record use. Prediction functionality depends on an approved dataset, target and features, validated preprocessing/model artifacts, and inference compatibility. The current public datasets cannot meet those conditions.

## 8. User experience requirements

- Accessible, readable, restrained research dashboard with plain-language field errors.
- Display pseudonymous patient codes and genuine chronological visit history only.
- Clearly distinguish missing, unassessed, invalid, and unavailable measurements.
- Make the research-only disclaimer visible alongside every actual prediction and in relevant workflows.
- Show no prediction or probability when unavailable; do not use diagnostic red/green cues or uncalibrated risk language.
- Make model version and prediction timestamp traceable for every actual result.

## 9. Project status

No application, database, or trained model is currently implemented. The public interim cohorts have zero approved features and zero valid fixed-horizon labels for the intended target. Training remains NO-GO. The application is mandatory as a final deliverable, but its real-data use and hosting remain subject to governance and supervisor approval.
