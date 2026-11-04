# 08 — Proposed Database and API Design

This is an initial design template. Final schema fields depend on the confirmed dataset and whether a web application is required.

## 1. Database entities

### `patients`
- `patient_id` — pseudonymous primary key.
- `display_code` — optional human-readable code with no direct identity.
- `created_at` — record creation timestamp.
- Avoid name, phone, address, medical-record number, or other direct identifiers.

### `visits`
- `visit_id` — unique primary key.
- `patient_id` — foreign key to patient.
- `visit_date` — date/time used for chronology.
- Dataset-defined feature columns — must be added only after the data dictionary is confirmed.
- `created_at` — record creation timestamp.

### `predictions` (optional)
- `prediction_id` — primary key.
- `patient_id` — pseudonymous patient reference.
- `predicted_label` — `MS` or `Non-MS`.
- `probability` — nullable; include only if its interpretation and calibration are documented.
- `model_version` — artifact version.
- `preprocessing_version` — transform/schema version.
- `created_at` — timestamp.
- `disclaimer_shown` — record whether the non-diagnostic notice was displayed, if appropriate.

### `users` (optional)
Only add this table if authentication is implemented. Store password hashes using a suitable secure library; never store plain-text passwords.

## 2. Relationships

- One patient has many visits.
- One patient may have many prediction records, if history is enabled.
- A user may create/manage records only within authorized permissions, if authentication/roles are implemented.

## 3. API endpoints (proposed)

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/api/health` | Service health check |
| POST | `/api/patients` | Create pseudonymous patient record |
| GET | `/api/patients` | List permitted patient records |
| GET | `/api/patients/{patient_id}` | Retrieve patient summary |
| POST | `/api/patients/{patient_id}/visits` | Add a visit |
| GET | `/api/patients/{patient_id}/visits` | Retrieve visits in chronological order |
| POST | `/api/predictions` | Request a prediction for a patient with sufficient records |
| GET | `/api/predictions/{prediction_id}` | Retrieve a prior result, if history is enabled |

## 4. Prediction request example

```json
{
  "patient_id": "PSEUDO-0001"
}
```

The backend retrieves visit data from the database. The browser should not send arbitrary preprocessed tensors or claim a prediction succeeded before the backend returns a result.

## 5. Prediction response example

```json
{
  "prediction_id": "pred-example",
  "patient_id": "PSEUDO-0001",
  "predicted_label": "MS",
  "probability": null,
  "model_version": "not-yet-trained",
  "status": "research_prototype",
  "disclaimer": "Research prediction only — not a medical diagnosis. Do not use this result to make treatment decisions."
}
```

This is a contract example only, not a real prediction or an indication that a model exists. `probability` remains null unless validated and intentionally implemented.

## 6. Error response examples

- `400` — invalid request or malformed data.
- `404` — patient or visit not found.
- `409` — duplicate visit or incompatible state.
- `422` — insufficient or invalid sequence data.
- `503` — model not trained, unavailable, or incompatible.
- `500` — unexpected server error with a safe client message and internal diagnostic log.

Never return patient-sensitive values in error messages or logs.
