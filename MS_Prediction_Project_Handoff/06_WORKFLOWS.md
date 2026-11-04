# 06 — Project Workflows

## A. Approved cohort and model-development workflow

```mermaid
flowchart TD
    A[Obtain permitted longitudinal cohort] --> B[Verify provenance, CIS status, dates and criteria]
    B --> C[Define index, horizon, labels and censoring with clinical review]
    C --> D[Audit fields, timing, missingness and leakage]
    D --> E[Patient-level train / validation / test split]
    E --> F[Fit preprocessing on training patients only]
    F --> G[Build genuine chronological pre-index sequences]
    G --> H[Train suitable classical baselines]
    G --> I[Train SimpleRNN → LSTM only if data support it]
    H --> J[Compare with same patient partitions]
    I --> J
    J --> K[Evaluate, calibrate if needed, document limitations]
    K --> L[Version model, preprocessing, schema and metadata]
```

The current public Mexican and Lithuanian interim files do not pass the cohort/label gate. Do not manufacture a sequence, label, conversion date, or performance result from them.

## B. Doctor application access and patient management workflow

```mermaid
flowchart TD
    A[Doctor opens app] --> B[Supabase Auth sign-in]
    B --> C{Authenticated and authorized?}
    C -- No --> D[Show safe access error]
    C -- Yes --> E[Protected React application]
    E --> F[Register/search/select pseudonymous patient]
    F --> G[FastAPI authorization and patient-scoped database operation]
    G --> H[Review/add/update permitted patient details]
    H --> I[Add or review genuine dated visits]
    I --> J[Enter approved clinical measurements with dates and units]
    J --> K[Validate, save, and display chronological history]
```

## C. Gated research prediction workflow

```mermaid
flowchart TD
    A[Authorized doctor requests research prediction] --> B[FastAPI verifies role and patient access]
    B --> C{Eligible genuine pre-index history?}
    C -- No --> U[Return unavailable reason; record no predicted class]
    C -- Yes --> D{Compatible validated model and preprocessing?}
    D -- No --> U
    D -- Yes --> E[Validate schema, units, timing and predictor cutoff]
    E --> F[Apply versioned preprocessing and sequence builder]
    F --> G[Offline-trained versioned model inference]
    G --> H[Persist actual result, timestamp, model version and audit metadata]
    H --> I[Display result, limitations and research-only disclaimer]
```

Until the approved cohort and validated artifact gates pass, prediction requests must remain unavailable. A logged unavailable request is not a prediction result.

## D. Prediction history workflow

An authorized doctor opens a patient record → the backend verifies patient-level access → retrieves only permitted request/result events → displays them chronologically with status, timestamp, and model/preprocessing version where applicable. Only real service outcomes may be shown; failed/unavailable requests must not display a class.

## E. Error and safety workflow

- Authentication or authorization failure → deny request and return a safe message; do not disclose whether inaccessible patient data exist.
- Invalid field, unit, date, relationship, or schema → reject with a field-level explanation that contains no sensitive values.
- Insufficient visits, unknown outcome status, unavailable/incompatible model, or unsupported data → do not predict; show why the request is unavailable.
- Database or inference failure → record only approved safe audit metadata and return a generic safe error; never fabricate a result.

## F. Architecture and training/inference separation

React/TypeScript sends authorized structured requests to FastAPI. FastAPI validates authorization and payloads, coordinates SQLAlchemy operations against Supabase PostgreSQL under RLS, and calls a separate inference component only for a compatible validated model. Offline training consumes approved research data and produces versioned model/preprocessing artifacts; it is never run in a user request.
