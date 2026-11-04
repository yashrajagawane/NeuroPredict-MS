# 04 — Data Requirements and Data Dictionary Template

## 1. Data purpose

The model is intended to learn from **structured patient observations collected across multiple visits**. The dataset must be appropriate for the target and must contain true temporal information.

## 2. Required dataset properties

- A stable pseudonymous `patient_id` to group all observations belonging to one person.
- A visit identifier or a way to distinguish repeated visits.
- A visit date/time or reliable visit order.
- A documented set of predictor features and their units/categories.
- A documented binary target label with source, timing, and meaning.
- Sufficient numbers of patients and visits in each class for the planned analysis.
- Permission, provenance, license, and any ethics/consent requirements documented.

## 3. Data schema template

The exact feature names must come from the confirmed dataset, not from assumptions.

| Field | Meaning | Required? | Notes |
|---|---|---:|---|
| `patient_id` | Pseudonymous patient key | Yes | Must not contain name, MRN, phone, or other direct identifier. |
| `visit_id` | Unique visit key | Recommended | Can be generated from dataset key if permitted. |
| `visit_date` | Visit timestamp/date | Yes for sequences | Must support chronological ordering. |
| `feature_*` | Dataset-defined clinical/structured predictors | TBD | Record type, units, allowed values, and missingness. |
| `target_label` | MS or Non-MS class | Yes for supervised training | Define label time and source. Do not infer label from arbitrary feature thresholds. |
| `target_time` | Time at which label/status applies | Strongly recommended | Needed to align label with index time. |
| `source_record_id` | Original record reference | Optional | Keep only if safe and permitted. |

## 4. Label definition — blocking requirement

The project currently says “MS / Non-MS,” but this is insufficient as a formal label definition. Confirm:

- Does the label represent disease status at the index visit, or a future diagnosis within a fixed horizon?
- Which diagnostic/clinical source defines MS versus Non-MS?
- Are controls healthy people, other neurological conditions, or a mixture?
- How are uncertain, missing, or conflicting diagnoses handled?
- Is each patient assigned one final label, or can status change across visits?
- At what time are predictors frozen so post-index information cannot leak into the model?

Do not train until these questions are answered using dataset documentation and project-supervisor guidance.

## 5. Longitudinal requirements

- Sort visits by patient ID and date/time.
- Preserve irregular visit intervals; do not assume equal time spacing without evidence.
- Resolve duplicate visits using documented rules.
- Handle patients with too few visits explicitly.
- Avoid padding/truncation that silently changes the meaning of the sequence.
- If variable-length sequences require padding/masking, document and test the method.
- Do not convert unrelated columns into artificial time steps.

## 6. Data quality report

Before modeling, generate:

- Dataset row and unique-patient counts.
- Visits per patient distribution.
- Class counts at patient level and, if applicable, visit level.
- Missing values per feature and per class.
- Duplicate patient/visit checks.
- Date range and time-gap distribution.
- Numeric ranges, units, categorical levels, and outliers.
- Potential target leakage and post-index variables.
- Patient/site/source distribution if available.

## 7. Train/validation/test split

- Split by unique patient ID, not by visit rows.
- Keep every visit from one patient in one partition for the primary evaluation.
- Stratify at patient level if appropriate and possible.
- Use a fixed random seed and store the exact patient IDs/indices per split securely.
- Fit imputers, scalers, encoders, feature selection, and other learned transforms on training data only.
- Use validation data for tuning and threshold selection; reserve the test data for final evaluation.
- Consider site/time-based or independent external validation if the dataset supports it.

## 8. Synthetic data policy

Synthetic data may be used to test the application, schema validation, sequence generation, and training code path. Clearly name it as synthetic/demo data. Do not use it to make clinical claims or report the resulting metrics as MS prediction performance. Avoid defining synthetic labels as simple thresholds of the same features used as predictors, because the model would mainly learn the artificial rule.

## 9. Data dictionary template

For each confirmed predictor record:

| Name | Description | Type | Unit/category | Visit-level or static | Missingness | Available at index time? | Leakage risk |
|---|---|---|---|---|---|---|---|
| TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
