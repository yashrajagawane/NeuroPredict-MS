# 12 — UI/UX Guidelines

## 1. Visual direction

Build an accessible, restrained research dashboard using React/TypeScript and the approved component stack. Use a light neutral background, dark navy text, restrained blue/teal accents, readable typography, clear spacing, accessible contrast, and no unnecessary animation. Avoid diagnostic red/green status cues.

## 2. Mandatory application modules and screens

### A. Doctor login and authentication

- Sign-in, sign-out, session-expiry, and access-denied screens.
- Explain access errors without revealing whether a restricted patient exists.
- Protected navigation is a user-experience feature; backend authorization remains the security boundary.

### B. Patient registration and management

- Authorized patient search/list and patient detail.
- Registration/update uses pseudonymous identifiers and only permitted fields; never show direct identifiers.
- Duplicate or invalid values receive clear errors. Patient counts are shown only from actual authorized database values.

### C. Patient visit history

- Patient detail shows genuine visit dates in chronological order, including source-supported clinical history.
- Clearly distinguish missing, not assessed, unavailable, and invalid values.
- Show no artificial/duplicated visits and no post-index information in a prediction-input preview.

### D. Clinical data management

- Add/edit only source-approved measurements and categories.
- Collect/display actual measurement date and unit; indicate required/optional and valid ranges from the approved data dictionary.
- Explain validation failures and preserve missingness semantics.

### E. Research prediction interface

- Show a request action only when authenticated/authorized and eligibility/model gates can be checked.
- Until an approved compatible, tested, versioned model exists, show “Research prediction unavailable” with the reason and no class/probability.
- For a valid future result, show target, model version, request/result timestamp, limitations, and the full non-diagnostic disclaimer.
- Never show an uncalibrated probability as personal risk.

### F. Prediction history and results

- Patient-scoped list of real requests/results, chronologically sorted, with request status, timestamps, and model version where applicable.
- Distinguish successful results from unavailable or failed requests; unavailable/failed states display no class.
- Provide access only to authorized roles and make audit provenance available according to policy.

## 3. Shared UX requirements

- Plain-language labels and field-level validation messages.
- Keyboard-operable navigation, forms, tables, and timelines; semantic labels and accessible focus.
- Visible research-only disclaimers on prediction flows and results.
- No claim that the app is clinically approved. Avoid unsupported risk language and health-state color coding.
- Use synthetic/demo records only when clearly labelled; screenshots must not contain confidential patient data.
