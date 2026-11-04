# Public CIS Source Data-Quality Report

## Scope and method

This report covers an immutable, source-level audit of the two official public
Mendeley workbooks acquired on 2026-11-04. The audit reads XLSX XML using the
Python standard library, verifies published SHA-256 values, profiles headers,
missingness, identifiers, outcome coding, and possible temporal fields, and
does not alter raw files or create patient records.

The complete machine-readable audit is
[public_source_audit.json](../audit/public_source_audit.json). Field-level
missingness for every available source column is in
[missingness_report.csv](../audit/missingness_report.csv).

## Audit results

| Check | Mexican prospective cohort | Lithuanian retrospective cohort |
|---|---|---|
| Official file hash | Match | Match |
| Source data rows | 273 | 138 |
| Unique source IDs | 272 | 138 |
| Duplicate source IDs | 1 | 0 |
| Exact duplicate full rows | 0 | 0 |
| Source columns | 20 | 44 |
| Repeated patient visits | None exported | None exported |
| Date-like source columns | None | None |
| Visit, conversion, or follow-up dates | None | None |
| Candidate target values | group 1: 125; group 2: 148 | MS 0: 89; MS 1: 49 |
| Longitudinal RNN-LSTM ready | No | No |

The workbook-level totals are not model class totals. Neither source can
separate adequate non-converters from patients with unknown or insufficient
follow-up.

## Missingness and source-quality findings

### Mexican cohort

- Age is present for all rows; observed range is 15–77 years and median is 33.
- Initial symptom and schooling each have one missing value, or 0.366%.
- Initial EDSS and final EDSS each have 148 missing values, or 54.212%.
  Final EDSS is a post-baseline field and is a direct leakage risk; it must
  never be used as an input to a future conversion prediction model.
- MRI-region fields are binary source codes, not dated lesion counts. They do
  not establish total T2 burden, new/enlarging T2 activity, or
  gadolinium-enhancing lesion counts.
- The Oligoclonal bands field has values 0, 1, and 2, but the public workbook
  does not supply the code definitions. Sex, symptom, breastfeeding,
  varicella, and mono/polysymptomatic values also require a source codebook
  before clinical interpretation.
- One source patient identifier is duplicated, while no entire row is an exact
  duplicate. The two records must not be deduplicated automatically; their
  provenance and meaning need source-owner confirmation.

### Lithuanian cohort

- Age is present for all rows; observed range is 13–73 years and median is
  41.5. Two records are below 18 despite the publication describing adults.
  This is a documentation/data consistency issue requiring source-owner
  clarification, not an automatic exclusion.
- MRI infratentorial, periventricular, and juxtacortical fields each have
  16 missing values, or 11.594%. MRI spinal lesions has 89 missing values, or
  64.493%.
- OGB-positive CSF has 30 missing values, or 21.739%. IgG levels in CSF has
  49 missing values, or 35.507%; it is not labelled as an IgG index and no
  unit/codebook is provided in the public workbook.
- VEP-positive and BAEP-positive fields have 16.667% and 25.362% missingness,
  respectively.
- The workbook has two columns both labelled Pleocytosis. The audit preserves
  them as Pleocytosis [AL] and Pleocytosis [AM] rather than overwriting one.
  The Patholoigical CSF field includes two nonnumeric n values, and the
  source spelling is retained for provenance.

## Chronology, longitudinal structure, and leakage

There are no source dates to check chronology, visit order, interval
regularity, patient-specific follow-up, or outcome timing. Both workbooks have
one source record per patient, so an average/median/minimum/maximum visit
count per patient cannot be computed as a genuine longitudinal statistic.
Treating the single record as one "visit" would misrepresent the data and is
not reported as a visit distribution.

The public data trigger these leakage safeguards:

- Do not use Mexican final EDSS.
- Do not use the final MS/group field as a feature.
- Do not infer a visit sequence from static fields or repeat baseline rows.
- Do not use source patient identifiers as features.
- Do not label unknown or short-follow-up patients as Class 0.
- Do not combine studies until variables, time definitions, coding, and
  diagnostic criteria have been reconciled under a documented protocol.

## Diversity and generalizability

The audited workbooks show variation in age, coded sex, symptoms, MRI-location
indicators, and selected CSF/evoked-potential measures. They represent one
Mexican single-centre prospective cohort and one Lithuanian retrospective
record cohort. Their populations, centres, diagnostic eras, and collection
methods differ. Race/ethnicity, socioeconomic context beyond one schooling
field, detailed treatment history, and harmonized centre variables are absent
or not interpretable from the public files.

The data must not be described as representative of all CIS or MS
presentations. They are also far below the 2,000-CIS-patient aspiration. The
cohort-size visualization is available at
[public_candidate_cohort_sizes.svg](../audit/public_candidate_cohort_sizes.svg).

## Outcome validation and readiness result

No source can provide:

- the number of confirmed conversions within a selected horizon;
- non-conversions with sufficient individual follow-up;
- unknown/censored outcome count;
- genuine visit-record count or visits-per-patient distribution; or
- a patient-level longitudinal leakage check.

The resulting quality decision is **NO-GO** for recurrent-model training. The
next permitted data step is a controlled-access feasibility extract meeting
the contract in
[recommended_longitudinal_schema.md](../contract/recommended_longitudinal_schema.md).
