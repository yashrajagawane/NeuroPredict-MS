# 09 — Implementation Roadmap Summary

The root [`PROJECT_MASTER_PLAN.md`](../PROJECT_MASTER_PLAN.md) is authoritative for the 64 phase IDs, exact phase order, dependencies, statuses, completion percentages, acceptance evidence, and change history. This file is only a high-level orientation; it does not define alternate phases or permit skipping a master-plan gate.

## Mandatory end-state

The final-year project has two required components:

1. A reproducible research pipeline for future conversion from confirmed CIS to MS using genuine, permitted longitudinal observations, with justified labels/index/horizon, data validation, patient-level partitions, baselines, and the proposed SimpleRNN → LSTM experiment only if data support it.
2. A doctor-facing React/TypeScript application with all six modules: authentication/authorization; pseudonymous patient management; chronological visit history; approved clinical-data management; gated research prediction; and traceable prediction history/results.

The approved stack is defined in the master plan. Do not substitute older Flask/SQLite/HTML recommendations in this handoff pack.

## High-level gated sequence

1. Complete the project-owner-approved charter and intended-use/product requirements (Phases 01 and 03).
2. Establish an operational future CIS-to-MS target, index/horizon, endpoint adjudication, source access, ethics, and data governance (Phases 02-10).
3. Acquire and validate an approved cohort; define eligibility, labels, features, leakage controls, cleaning, sequence design, sample feasibility, and evaluation protocol (Phases 11-25).
4. Complete the approved environment, contracts, tests, patient-level split, preprocessing, and sequence pipeline (Phases 26-27 and 31, following dependencies).
5. Train/evaluate baselines and the hybrid model only after all data gates pass (Phases 28-43).
6. Build the approved database, authentication, API, six UI modules, integration, and security tests in dependency order (Phases 44-54).
7. Complete reliability, deployment, governance, operations, usability, reproducibility, and academic handover only when applicable gates pass (Phases 55-63).

## Current gates

- The public Mexican and Lithuanian data remain separate interim datasets and are unsuitable for future CIS-to-MS training.
- No selected index date/horizon, fixed-horizon labels, model-approved inputs, or genuine repeated dated visits exist for the intended task. Model training remains NO-GO.
- Prediction functionality must remain unavailable until an approved cohort and a valid, tested, versioned model/preprocessor are available.
- Do not access or store real patient records before source permission and required ethics/security approvals.
- Continue automatically one phase at a time through eligible work under the current user authorization. If a phase is externally blocked, document the specific dependency and continue with independent eligible work. Commit and push each genuinely completed phase, then report it; do not falsely mark blocked work complete.
