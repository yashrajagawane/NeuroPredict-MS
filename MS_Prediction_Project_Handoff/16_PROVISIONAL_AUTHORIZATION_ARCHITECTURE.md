# 16 — Provisional Authentication and Authorization Architecture

**Status:** Design proposal only; not approved for live accounts, patient records, or deployment.  
**Scope:** Define trust boundaries and testable authorization expectations for the approved React, FastAPI, Supabase Auth, and PostgreSQL RLS stack.

## 1. Requirements and non-goals

The application requires doctor login/logout, authenticated sessions, role authorization, and protected routes and APIs. “Doctor” is a product role requirement; it is not evidence of professional credentials, clinician endorsement, or institutional authorization. This proposal creates no Supabase project, account, claim, secret, token, RLS policy, SQL migration, or patient record.

## 2. Trust boundaries and proposed flow

1. Supabase Auth authenticates the user and issues a short-lived access token. The React client uses the session to call FastAPI over HTTPS; the browser is not trusted to make authorization decisions.
2. FastAPI validates the bearer token using a supported verification library and the configured Supabase issuer/signing keys. It must check signature, allowed algorithm, issuer, audience, expiry, and required subject; reject malformed, expired, wrongly-issued, or unprovisioned identities by default. Do not implement JWT cryptography manually.
3. Each protected route checks the verified identity and the approved role and patient scope on the server. Frontend route guards are a usability feature only.
4. PostgreSQL RLS is a second authorization boundary. Any eventual exposed table needs deliberate grants plus policies. A `TO authenticated` clause alone does not define which patient rows a doctor may access. The actual ownership/assignment/clinic-scope rule is not yet known.
5. The backend-to-Postgres design must preserve the verified request identity for RLS without leaking context across pooled connections. A direct database connection does not automatically inherit a browser JWT. The chosen transaction-scoped context and pool reset behavior must be implemented and tested before enabling patient operations.

## 3. Identity, roles, and account lifecycle

- Supabase Auth owns passwords and identity credentials; application tables must not duplicate them.
- The minimum product role is `doctor`, pending policy approval. Anonymous, authenticated-but-unprovisioned, and disabled users receive no patient-data access.
- Account self-registration versus invitation/administrator provisioning remains undecided. Open registration must not imply authorization.
- If authorization claims are used, they must be set by a trusted administrative/server process. Never make authorization decisions from user-editable `user_metadata`. Trusted `app_metadata` may carry server-controlled claims, but stale JWT claims and refresh/revocation timing must be handled.
- Administrator, researcher, and support roles are not approved. Do not implement broad administrator bypasses by assumption.
- Account disablement, token/session revocation, refresh behavior, expiry, recovery, MFA requirements, audit access, and deletion lifecycle require policy decisions before production use.

## 4. Provisional access matrix

| Actor/request | Public health/readiness | Patient/visit API | Research prediction/history |
|---|---|---|---|
| Anonymous | May access only a minimal non-sensitive liveness response, if deployment chooses to expose it | Deny | Deny |
| Authenticated, not provisioned | Same minimal response | Deny | Deny |
| Provisioned doctor | Same minimal response | Deny by default until patient-scope policy is approved; then only explicitly permitted records | Disabled until dataset, model, workflow, and policy gates pass |
| Invalid/expired token | Minimal response may remain public | Deny without revealing record existence | Deny |
| Administrator or service process | No special health-detail response | No broad bypass is defined here | No bypass is defined here |

The app may display a non-clinical unavailable state when the prediction service is gated. It must not emit a fabricated label or imply diagnosis.

## 5. Credential and database boundaries

- No Supabase secret/service-role key or database credential may be placed in Vite-prefixed variables, bundles, browser storage, source control, logs, or screenshots.
- Supabase documents that the service-role/secret key bypasses RLS. It must not be the general request-path database credential. Any exceptional privileged operation requires a separately reviewed, narrowly scoped server boundary and audit trail.
- Prefer ordinary least-privilege database roles and explicit grants. RLS policies must be deny-by-default and include row scope, not just an authenticated-role check.
- Avoid returning claims, database errors, connection details, clinical counts, or patient existence in auth failures. Record security events using minimized metadata without tokens or clinical payloads.

## 6. Required future security tests

Before patient-data access is enabled, test at minimum:

- anonymous, invalid-signature, wrong-issuer/audience, expired, and malformed token denial;
- authenticated but unprovisioned user denial;
- user-editable metadata cannot grant a role;
- authorized doctor can access only the approved patient scope;
- cross-patient reads and writes are denied through both API and direct database paths;
- disabled/revoked account behavior and stale claims are understood;
- pool reuse does not leak one request's RLS identity into another;
- every exposed table has deliberate grants and RLS, including views/functions;
- privileged keys are absent from frontend artifacts and logs.

No live security test was run because no Supabase project, approved policy, or clinical records are available.

## 7. Decisions required before implementation

1. Institutional identity and account-provisioning policy; how “doctor” authorization is verified.
2. Patient scope: individually assigned, shared clinic, study team, or another approved model.
3. Whether role claims, a server-side membership table, or both provide authorization; claim refresh/revocation behavior.
4. A supported FastAPI token-validation method and key-rotation/error behavior.
5. A transaction-bound Postgres RLS identity propagation design with safe connection-pool cleanup.
6. MFA, session duration, recovery, disablement, audit retention, and administrator permissions.
7. Security/governance review of hosting, data residency, and incident handling.

## 8. References

- [Supabase Row Level Security](https://supabase.com/docs/guides/database/postgres/row-level-security) — grants and policies both matter; service-role bypass; editable user metadata is unsuitable for authorization; JWT claims can be stale.
- [Supabase JSON Web Tokens](https://supabase.com/docs/guides/auth/jwts) — token claims and verification guidance; use a supported library rather than custom cryptography.
- [Supabase Auth Users](https://supabase.com/docs/guides/auth/users) — user-editable metadata warning and secret-key handling.

This design does not complete implementation acceptance for Phase 45. Live Auth, RLS, account provisioning, and patient access remain gated by Phases 08, 46, governance, and security review.
