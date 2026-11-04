# Dataset Card — CIS-to-MS Longitudinal Dataset Feasibility Audit

## Status

**NO-GO for Hybrid SimpleRNN-LSTM training.**

This is a research-audit dataset card, not a released training dataset. The
two public sources were legally acquired, hash-verified, and inspected. Neither
has genuine patient-linked longitudinal visits or the individual dates required
to construct the project's future CIS-to-MS conversion outcome.

Accordingly, patients.csv, visits.csv, and outcomes.csv have deliberately not
been created. Creating them from these workbooks would manufacture sequence
structure, timing, and/or labels that the source does not contain.

## Intended research question

For a patient with confirmed CIS at a defined index date, predict whether a
confirmed MS conversion occurs within a prespecified future horizon. A valid
binary label requires:

- confirmed CIS before or at the index date;
- a documented index date and horizon;
- a conversion date for Class 1;
- a last-follow-up date at or beyond the horizon for Class 0; and
- an explicit criterion version and outcome-certainty assessment.

The source audit found no public workbook satisfying these requirements.

## Audited public source inventory

| Source | Raw rows | Unique source IDs | Raw outcome values | Repeated dated visits | Conversion and follow-up dates | Final-model status |
|---|---:|---:|---|---|---|---|
| Mexican prospective CIS cohort | 273 | 272 | group 1: 125; group 2: 148 | No | No | Not eligible |
| Lithuanian retrospective CIS cohort | 138 | 138 | MS 1: 49; MS 0: 89 | No | No | Not eligible |

The Mexican workbook has one duplicate source identifier and no exact duplicate
full row. The workbook's group mapping is not defined in a source data
dictionary; the apparent conversion mapping is an inference from the
publication's aggregate count and is not promoted to a model label here.

The Lithuanian MS field has an apparent 49/89 final-diagnosis split, but no
individual baseline, conversion, or last-follow-up dates. It therefore cannot
provide a known 24-, 36-, or 60-month future-outcome label.

The raw row counts must not be summed into a 411-patient model cohort. The
studies have different populations, coding, timing, diagnostic eras, and
unresolved field semantics. More importantly, neither supports the required
longitudinal prediction design.

## What is present

- Official, publicly downloadable source files under CC BY 4.0.
- De-identified source identifiers in the original workbooks.
- Baseline-like demographic, symptom, MRI-location, CSF, and evoked-potential
  fields with source-specific coding.
- An aggregate published report of study follow-up and conversion outcomes.

## What is absent

- Patient-linked visit identifiers and multiple observations per patient.
- Visit dates or a reliable months-from-baseline field.
- Individual CIS diagnosis/index dates.
- Individual MS conversion dates.
- Individual last-follow-up dates.
- A public data dictionary for key categorical values in the Mexican workbook.
- A validated fixed prediction horizon.
- MRI lesion counts, new/enlarging lesion counts, and gadolinium-enhancing
  lesion counts in the public files.

## Appropriate and inappropriate uses

Appropriate uses are source auditing, provenance work, field-mapping research,
and a clearly labelled baseline-only exploratory analysis only after separate
ethical and methodological approval.

Inappropriate uses include training the requested recurrent model, claiming
multi-visit temporal prediction, imputing visit histories, duplicating baseline
rows, treating final EDSS as an input, or treating insufficient follow-up as a
negative conversion label.

## Recommended path to a usable cohort

Request a constrained feasibility extract from MSBase/MSBasis through an
eligible clinical collaborator. Published descriptions support the existence of
CIS onset/diagnosis information, dated visits, EDSS/KFS, relapse dates, and
treatment dates, but the actual extract must confirm conversion-date,
criterion-version, follow-up, MRI, and permission details. The required
request fields are specified in
[msbase_access_request_spec.md](../contract/msbase_access_request_spec.md).

See [label_validation_report.md](label_validation_report.md) for the outcome
gate, [data_quality_report.md](data_quality_report.md) for actual audit
findings, and [candidate_source_comparison.md](candidate_source_comparison.md)
for the source-access assessment.
