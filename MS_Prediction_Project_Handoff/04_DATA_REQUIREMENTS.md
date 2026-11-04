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
| `index_date` | Approved prediction/index time | Yes for future-outcome prediction | Must follow the approved baseline or landmark rule; no future observation may enter model input. |
| `prediction_horizon_months` | Predeclared future outcome window | Yes for fixed-horizon training | Set only after follow-up feasibility and clinical review. |
| `conversion_status` | Confirmed conversion / no conversion with adequate follow-up / unknown / censored | Yes for supervised training | Class 1 requires confirmed post-index event within horizon; Class 0 requires follow-up through horizon. |
| `conversion_date` | Date of confirmed CIS-to-MS conversion | Required for Class 1 | Preserve source and diagnostic-criteria evidence; never use as a predictor. |
| `last_follow_up_date` | Last known observation date | Required to establish Class 0/censoring | Unknown/short follow-up is not a negative label. |
| `diagnostic_criteria_version` | Criteria used to establish baseline CIS and conversion | Required for adjudication | Preserve source-specific version; do not silently harmonize diagnostic eras. |
| `source_record_id` | Original record reference | Optional | Keep only if safe and permitted. |

## 4. Future CIS-to-MS target — operational details remain blocking

The confirmed research objective is to predict whether a patient with confirmed baseline CIS subsequently converts to MS. This is not a current-status MS/Non-MS classifier. The target is not operational until a suitable cohort and clinical review establish the index, horizon, eligibility, diagnostic criteria, and event evidence.

- **Class 1:** confirmed conversion after index and on or before the approved horizon, with conversion date and diagnostic criteria/evidence.
- **Class 0:** no confirmed conversion and last follow-up reaches or exceeds the entire approved horizon.
- **Unknown/censored:** uncertain diagnosis or follow-up ends before the horizon; never coerce to Class 0.
- **Index:** either CIS baseline or a later landmark. A landmark sequence design requires genuine pre-index visits and excludes conversion before the landmark.
- **Predictor cutoff:** all predictor measurements must be available on or before index. Exclude conversion date, final diagnosis, post-index measurements, and future follow-up.
- The horizon must be selected using a permitted cohort's actual follow-up/event timing and clinical justification. Do not choose among 24/36/60 months from the existing public workbooks, which contain no individual dates.

Do not train until the target protocol is documented, independently reviewable, and approved by the relevant clinical/project authority.

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
