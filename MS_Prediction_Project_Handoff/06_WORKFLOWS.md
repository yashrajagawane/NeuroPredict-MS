# 06 — Project Workflows

## A. Dataset and model-development workflow

```mermaid
flowchart TD
    A[Confirm dataset provenance and permissions] --> B[Inspect schema and label definition]
    B --> C[Data quality and leakage audit]
    C --> D[Patient-level train / validation / test split]
    D --> E[Fit preprocessing on training data only]
    E --> F[Create chronological patient sequences]
    F --> G[Train baseline models]
    F --> H[Train proposed RNN-LSTM model]
    G --> I[Compare on same validation/test partitions]
    H --> I
    I --> J[Evaluate class-wise metrics and calibration]
    J --> K[Save model, preprocessing, schema, and metadata]
```

## B. Prediction-time workflow

```mermaid
flowchart TD
    A[Authorized user selects patient] --> B[Backend retrieves permitted visit records]
    B --> C[Validate required fields and visit dates]
    C --> D[Apply saved preprocessing pipeline]
    D --> E[Order visits and build sequence]
    E --> F[Load matching saved RNN-LSTM model]
    F --> G[Generate experimental MS / Non-MS class]
    G --> H[Store result if history feature is enabled]
    H --> I[Display result and non-diagnostic disclaimer]
```

## C. Error workflow

```mermaid
flowchart TD
    A[Prediction request] --> B{Sufficient valid visit data?}
    B -- No --> C[Show missing/invalid data message]
    B -- Yes --> D{Compatible model available?}
    D -- No --> E[Show model unavailable message]
    D -- Yes --> F[Run prediction]
    F --> G[Display research result and disclaimer]
```

## D. System data-flow summary

- The user submits patient/visit details and requests a prediction.
- The frontend sends structured requests to the backend.
- The backend validates data and reads/writes permitted records in the database.
- The inference pipeline retrieves chronological visits and applies saved preprocessing.
- The saved model produces a predicted class.
- The backend returns the result to the frontend.

## E. Model-training versus inference distinction

Training is an offline development activity. It uses labelled dataset partitions to train and evaluate the model. Prediction-time inference reuses the saved model and fitted preprocessing artifacts; it does not train the model again for each patient.
