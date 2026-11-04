# 19 — Provisional Privacy-Safe Observability Design

**Status:** Design guidance only. No telemetry, dashboard, alert, model monitoring, or operational runbook has been deployed or tested.
**Scope:** Future service health and data-quality observability for the research prototype. This document does not authorize collection of patient or model-use data.
**Dependencies:** A deployed service, approved inference contract, and approved hosting/security boundary are still required for operational acceptance (Master Plan Phases 43, 48, and 57).

## 1. Design principles

- Collect the smallest operational signal that can diagnose service availability or software failure.
- Treat pseudonymous identifiers, patient-level event counts, timestamps, request metadata, and prediction activity as potentially sensitive.
- Never log patient identifiers, clinical values, outcome labels, prediction inputs/outputs, request/response bodies, access tokens, authorization headers, secrets, or database connection strings.
- Do not add patient, user, site, cohort, diagnosis, or model-score dimensions to metric labels.
- Do not infer that aggregation alone makes health-data telemetry anonymous. Small counts and precise timestamps may still identify activity.
- Alerts may request human investigation. Drift signals must never trigger automatic retraining, model promotion, or clinical action.
- Retention, access, location, ownership, and institutional permission must be approved before any operational telemetry is enabled.

## 2. Proposed signal inventory (not active)

| Signal | Proposed collection | Prohibited dimensions/content | Gate |
|---|---|---|---|
| Liveness/readiness | Service state and dependency availability, with a coarse health result | Patient data, credentials, detailed database errors | May be observed for the health-only scaffold; production collection still requires an approved host and retention policy |
| Request volume | Aggregate counts by fixed route template, method, and status class | User/patient/site IDs, raw URL/query string, body, precise patient-linked timestamp | Enable only after privacy/security approval; suppress or coarsen low-volume windows |
| Latency | Bounded histogram by fixed route template | Request identifiers linked to records; user/patient dimensions | Same approval as request-volume metrics; choose buckets from an agreed service objective |
| Errors | Count by stable internal error category and status class | Raw exception text, SQL, payload, tokens, record values, or stack traces in a shared telemetry sink | Sanitize at the application boundary and test before deployment |
| Data-quality checks | Approved aggregate schema/missingness summaries computed in the governed data environment | Row-level reports, rare-category counts, patient-level failure detail, unapproved exports | Requires data-owner approval, minimum-cell suppression policy, and a defined audience |
| Model version | Version identifier/digest attached to a controlled aggregate service measure | Patient-level prediction history or request-to-model event linkage | No model exists; enable only after artifact/version approval and inference implementation |
| Prediction count | Aggregate total over a sufficiently broad approved interval | Per-user/patient counts or exact event timestamps | No inference route exists; count may itself be sensitive and requires explicit approval |
| Feature drift | Approved aggregate comparison against a frozen reference distribution | Patient rows, outcome-informed monitoring, unapproved feature export | Requires an approved cohort, reference dataset, statistical plan, and reviewer; review signal only |

No numeric alert thresholds, service-level objectives, low-count thresholds, retention duration, or alert owner are selected here. Those decisions depend on the approved hosting, governance, and intended operational use.

## 3. Logging contract

If logging is later approved, structured events should use a short allowlist such as `event_name`, `service_version`, `environment`, `route_template`, `http_method`, `status_class`, `error_category`, and a random request correlation token that is not derived from a user or patient identifier. Correlation tokens must not be reused as database keys and should have bounded retention.

The implementation must redact authorization/cookie headers and avoid recording request/response bodies, query strings, raw URLs, exception messages from dependencies, SQL parameters, and form state. A correlation token must not provide a join path to patient records. Local developer logs must follow the same restrictions as hosted logs.

## 4. Drift review workflow

Drift monitoring is unavailable until a model and approved reference cohort exist. If authorized later, an aggregate signal should open a human review that checks data pipeline changes, coding/unit changes, population or site shifts, and measurement process changes. A signal alone is not evidence of degraded clinical performance. Recalibration, retraining, threshold changes, or model replacement require a separately approved evaluation and release process; no automatic promotion is permitted.

## 5. Future verification checklist

- [ ] Approve telemetry purpose, data categories, host/region, access roles, retention, and deletion process.
- [ ] Select route-level service objectives and an accountable alert owner.
- [ ] Test that identifiers, clinical payloads, tokens, query strings, SQL values, and raw exception details cannot reach logs or metrics.
- [ ] Test alert routing using non-sensitive fixtures and document response/escalation steps.
- [ ] Define and validate minimum-cell/coarsening rules before aggregate health-data quality or prediction metrics are exposed.
- [ ] Version and approve a reference distribution before any feature-drift analysis.
- [ ] Confirm drift alerts lead to human review only and cannot trigger automatic training or deployment.

## 6. Current limitations

The repository contains only a health-only FastAPI scaffold and static frontend. There is no deployed environment, database, authentication flow, prediction endpoint, model artifact, approved patient cohort, telemetry sink, dashboard, or tested alert. Accordingly, this document is provisional design evidence for Phase 58 and does not change the longitudinal training NO-GO decision or authorize storing real patient data in application services.
