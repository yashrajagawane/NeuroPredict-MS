# 21 — Provisional Performance and Reliability Test Plan

**Status:** Test design only. No load, stress, model-inference, database-failure, or production-like performance test has been run.
**Scope:** Future bounded performance/reliability checks for the research application after its API, authorized storage, and inference paths exist. This plan does not set a service-level objective or claim production capacity.
**Dependencies:** Operational tests depend on the API/inference service (Phase 48), integrated application (Phase 52), and completed test foundation/appropriate fixtures (Phase 54). Deployment-like tests additionally require the relevant governance and hosting approvals.

## 1. Guardrails

- Begin with local or isolated non-production infrastructure and non-sensitive software fixtures only.
- Do not use acquired patient-level cohort files, real identifiers, or clinical records as load-test inputs.
- Do not create realistic synthetic patient cohorts to simulate missing study data. Use only minimal, clearly synthetic request fixtures needed to exercise an implemented API contract.
- Do not write request bodies, authentication material, database parameters, or clinical values to benchmark output.
- Do not publish performance claims until the environment, workload, run count, exclusions, and uncertainty are recorded.
- Do not run against a live Supabase project or hosted clinical service without explicit governance and operational authorization.
- Performance results are engineering observations, not evidence of clinical validity, model accuracy, or suitability for clinical use.

## 2. Measurement plan (targets undecided)

For each approved environment and workload, record software commit, runtime/dependency versions, host/CPU/memory class, database/model version if applicable, warm/cold state, concurrency profile, test duration, and observed error rate. Candidate measurements are:

- request latency distribution (p50, p95, p99) per fixed route template;
- completed requests per second and timeout/error counts;
- process memory and CPU trend;
- application startup/readiness time and model-load time, once applicable;
- database connection acquisition/timeout behavior, once persistence exists;
- bounded resource behavior during graceful shutdown and restart.

No numeric latency, throughput, concurrency, memory, recovery-time, or error-rate targets are approved. The project owner and applicable supervisor/operations owner must set targets for the actual hosting tier and intended research workflow before pass/fail assertions are introduced.

## 3. Test progression

1. **Current scaffold smoke check:** Exercise only `/api/v1/health/live` and `/api/v1/health/ready` in the local test client. Verify stable response shape, safe readiness when dependencies are unavailable, and bounded error behavior. Do not interpret this as application or inference capacity.
2. **API contract checks:** After routes exist, use minimal schema-valid software fixtures to test ordinary requests, malformed requests, request limits, timeouts, and cancellation. Include only fixed route labels in reports.
3. **Integration checks:** After an authorized isolated database exists, simulate database unavailable/slow responses and verify fail-closed responses, resource cleanup, and no sensitive values in logs.
4. **Inference checks:** After a versioned model and approved preprocessing exist, measure cold/warm model loading, bounded sequence sizes defined by the approved data contract, and concurrency/resource limits with non-patient fixtures.
5. **Deployment-like checks:** Only after host/security approval, repeat the agreed workload in the approved non-production environment. Protect the live test boundary and obtain authorization before any external load generation.

## 4. Failure scenarios to cover when dependencies exist

- unavailable or slow database, connection exhaustion, and failed transaction cleanup;
- model artifact missing, incompatible version, or load failure;
- malformed, oversized, or out-of-contract request;
- request timeout, client cancellation, process restart, and graceful shutdown;
- transient upstream failure and retry behavior without duplicate patient writes;
- resource exhaustion at the explicitly approved workload boundary.

Expected behavior must remain explicit and non-diagnostic: return a bounded error/unavailable response, do not return a class or probability when inference is unavailable, and do not expose internal stack traces, SQL, credentials, or patient data.

## 5. Reporting template requirements

Each future run report should state purpose, environment, commit, dependency/model version, fixture provenance, workload, measurement method, raw aggregate results, failures, run count, limitations, and approval status. Store reports only in an approved repository location and exclude raw request logs. Re-run after material API, database, preprocessing, model, or hosting changes.

## 6. Current status and acceptance boundary

The current backend exposes health/readiness routes only. There is no patient API, database integration, inference endpoint, model artifact, deployment environment, or approved workload target. Therefore the plan is a preparatory Phase 55 deliverable only; performance characterization and reliability acceptance remain pending.
