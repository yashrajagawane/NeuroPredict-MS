# 12 — UI/UX Guidelines

## 1. Visual direction

- Clean, modern academic/clinical-research dashboard.
- Use a light neutral background with dark navy text and restrained blue/teal accents.
- Avoid crowded cards, decorative medical imagery, and unnecessary animation.
- Use readable typography, consistent spacing, clear form labels, and accessible contrast.

## 2. Proposed screens

### A. Dashboard
- Project/app name.
- Short research-prototype disclaimer.
- Patient count and visit count only if based on actual database values.
- Navigation to patient records and model information.

### B. Patient list
- Pseudonymous patient code.
- Number of visits.
- Most recent visit date.
- Search/filter where useful.
- Do not display identifying personal information.

### C. Patient detail and visit timeline
- Patient code.
- Chronological visit list.
- Visit date and confirmed data fields.
- Clear indication of missing or unavailable fields.

### D. Add/edit visit
- Only dataset-approved fields.
- Validate dates, numeric ranges, categories, and required values.
- Clearly mark optional versus required fields.

### E. Prediction result
- Predicted class: MS / Non-MS.
- Model version.
- Prediction timestamp.
- Data sufficiency status.
- Non-diagnostic disclaimer.
- Probability/confidence only if calibration and display policy are approved.

### F. Model information/evaluation
- Dataset and target definition.
- Model architecture.
- Evaluation split and metrics.
- Known limitations.

## 3. UX rules

- Do not make a prediction button available when required records are missing.
- Explain why a prediction cannot be generated.
- Do not imply that a result is a diagnosis.
- Avoid red/green visual treatment that suggests a definitive health state.
- Use neutral labels and accessible charts.
- Every successful prediction should be traceable to a saved model version.
