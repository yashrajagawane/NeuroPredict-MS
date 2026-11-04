# Candidate Feature Assessment Report

## Assessment rule

This assessment evaluates the proposed 14 inputs against the actual public
workbook columns. A field is not suitable merely because its name is similar
to a requested feature. It must have an understood definition, known
collection time, valid unit/coding, and availability on or before the model
index date.

All fields are excluded from a current recurrent-model dataset because there is
no valid longitudinal cohort. “Potential” below means only that a future
approved baseline or dated longitudinal extract could be assessed further; it
does not approve the public field for modeling.

| Candidate feature | Mexican workbook mapping and missingness | Lithuanian workbook mapping and missingness | Clinical meaning and grain | Prediction-time availability / leakage | Current decision |
|---|---|---|---|---|---|
| Age at CIS diagnosis | Age (y), 0% | Age, 0% | Static age; source timing needs confirmation. | Likely baseline but no individual index date. | Potential baseline candidate after date validation. |
| Sex | Gender, 0%; codes 1/2 undefined | Sex, 0%; codes 0/1 need documentation | Static demographic variable. | Available only after source-code mapping confirmation. | Potential after codebook confirmation. |
| Initial CIS presentation/type | initial symptom, 0.366%; 15 undefined codes; Mono or polysymptomatic | Focal symptoms, 0%; symptom flags; not a harmonized CIS subtype | Initial clinical presentation, but source semantics differ. | Intended baseline field; exact timing and code definitions unverified. | Potential only after clinical-codebook harmonization. |
| CSF oligoclonal bands | Oligoclonal bands, 0%; values 0/1/2 undefined | OGB + in CSF, 21.739% | CSF OCB result, generally static for an episode. | Must retain test date and result interpretation; do not repeat across visits as a new measurement. | Potential baseline candidate after code/timing review. |
| CSF IgG index | Not present | IgG levels in CSF, 35.507%; not labelled as an index and unit is absent | An IgG level is not necessarily an IgG index. | Cannot assume timing, unit, or interchangeability. | Exclude as proposed IgG-index feature. |
| Months from baseline | Absent | Absent | Derived temporal position, not a measured clinical value. | Must be calculated from genuine dated visits and index date. | Exclude; must be derived only in a valid longitudinal extract. |
| EDSS score | initial EDSS, 54.212%; final EDSS, 54.212% | Absent | Disability score. The public Mexican fields are not dated. | Initial might be baseline after verification. Final EDSS is post-outcome/future leakage. | Exclude final EDSS; initial EDSS only a possible baseline field after timing confirmation. |
| Relapses since previous visit | Absent | Absent | Time-varying relapse burden. | Requires dated adjacent visits and a clear interval definition. | Exclude. |
| Total T2 lesion count | Absent; only binary location flags | Absent; only binary lesion/location flags | T2 lesion burden count. | Location/presence cannot be relabelled as count. | Exclude. |
| New or enlarging T2 lesions | Absent | Absent | Interval MRI activity. | Requires comparable serial MRI and an interval ending on/before index. | Exclude. |
| Gadolinium-enhancing lesion count | Absent | Absent | Active contrast-enhancing lesion count. | Requires MRI date and acquisition/reporting details. | Exclude. |
| Periventricular lesion count | Periventricular MRI, 0%; binary source field | Periventricular, 11.594%; binary source field | Lesion-location indicator, not count. | Timing unknown; baseline-only use needs confirmation. | Do not call it a count; possible binary baseline feature after validation. |
| Infratentorial lesion count | Infratentorial MRI, 0%; binary source field | MRI lesion localisation: infratentorally, 11.594%; binary source field | Lesion-location indicator, not count. | Timing unknown. | Do not call it a count; possible binary baseline feature after validation. |
| Spinal cord lesion count | Spinal cord MRI, 0%; binary source field | MRI spinal lesions, 64.493%; binary source field | Lesion-location indicator, not count. | Timing unknown; high missingness in Lithuanian source. | Do not call it a count; exclude from current model. |

## Additional source-supported fields

The public workbooks contain possible baseline research variables that should
not be added automatically:

- Mexican: schooling, breastfeeding, varicella, mono/polysymptomatic
  presentation, lower/upper-limb somatosensory evoked potentials, visual
  evoked potentials, brainstem auditory evoked potentials, and a cortical MRI
  indicator.
- Lithuanian: focal and neurological symptom indicators; MRI flags for lesions
  specific to MS, other disease, and unspecified lesions; CSF protein,
  pleocytosis, OGB, IgG level, VEP, and BAEP.

These may become candidate baseline variables only after a clinical reviewer
verifies their clinical definitions, coding, collection timing, and missingness
mechanism. No public file provides treatment history, serial MRI activity,
neurofilament light chain, vitamin D, or patient-linked repeated EDSS/relapse
measurements for the requested sequence model.

## Required safeguards for a future extract

- Preserve the actual test date for OCB, IgG, MRI, and evoked-potential fields.
- Treat static baseline results as static; do not copy OCB or IgG into every
  visit as if measured repeatedly.
- Keep raw MRI report/measurement provenance and unit definitions. Harmonize
  lesion measures only when acquisition/reporting rules support it.
- Exclude final diagnosis, conversion date, final EDSS, post-index MRI, and
  post-index relapse data from model input.
- Fit imputation, scaling, encoding, and feature selection on training
  patients only.
- Maintain all observations of one patient in one split.

The corresponding machine-readable mapping is
[feature_dictionary.csv](../audit/feature_dictionary.csv). It is a candidate
field dictionary for audit purposes, not a statement that a final feature set
has been selected.
