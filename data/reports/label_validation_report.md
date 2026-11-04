# CIS-to-MS Outcome and Label Validation Report

## Decision

No public source currently passes label validation for the requested future
CIS-to-MS conversion prediction task. No prediction horizon has been selected,
because neither downloadable workbook contains the individual dates needed to
test 24-, 36-, or 60-month follow-up adequacy.

This is a stop condition, not a reason to recast the task as contemporary
MS-versus-non-MS classification.

## Required label definition

For each patient and one declared index date:

| Status | Required evidence | Handling |
|---|---|---|
| Class 1 | Confirmed MS conversion after the index date and on or before the selected horizon, with a conversion date and diagnostic criterion/version. | Include only after date and criterion validation. |
| Class 0 | No confirmed conversion through the full selected horizon, with a last-follow-up date at or after the horizon. | Include only after follow-up validation. |
| unknown | Outcome cannot be established from the available record. | Exclude from supervised binary training; retain for cohort accounting. |
| censored | Follow-up ends before the horizon without observed conversion. | Do not convert to Class 0; retain separately or use an approved time-to-event design. |

The conversion event must represent a clinically confirmed MS diagnosis, not a
post-hoc final status field, a patient identifier, a treatment change, or a
feature measured after the index date.

## Evidence from the audited sources

| Label prerequisite | Mexican public workbook | Lithuanian public workbook | Result |
|---|---|---|---|
| Baseline CIS population | Supported by the prospective-cohort publication. The publication reports 2010 McDonald conversion assessment. | Supported at study level by the retrospective-study publication; the study describes neurologist-confirmed CIS evaluation in the 2015–2020 record period. | Patient-level confirmation and dates are not exported. |
| Individual index date | Absent | Absent | Cannot establish prediction time zero. |
| Individual conversion date | Absent | Absent | Cannot place a conversion inside a horizon. |
| Individual last-follow-up date | Absent | Absent | Cannot establish an adequate Class 0. |
| Repeated dated observations | Absent | Absent | Cannot construct a sequence up to an index/landmark. |
| Diagnostic criterion version per event | Aggregate publication context only | No patient-level criterion field | Cannot audit criterion drift or event certainty. |
| Fixed future horizon | Study-level 10-year follow-up reported, but not per patient | Record-review period reported, but not patient-specific follow-up | No defensible horizon. |

The Mexican group values of 1 and 2 occur 125 and 148 times, respectively.
The 125 count matches the published conversion total, but the workbook does
not define the codes. This relationship is evidence for a hypothesis, not a
validated data dictionary.

The Lithuanian MS column has 49 positive and 89 negative values. It is a
final-diagnosis indicator without timing; it cannot distinguish a conversion
within a chosen horizon from conversion after the horizon, loss to follow-up,
or a non-converter observed for too short a period.

## Diagnostic-context considerations

The concept of conversion changes with diagnostic criteria and clinical era.
The Mexican study reports its ten-year result under the 2010 McDonald
criteria. The Lithuanian publication describes the 2017 McDonald era, but the
downloaded file lacks a criterion-version field for each diagnosis. A future
cohort must retain the original clinical criterion/version, whether the
conversion date was directly entered or derived, and the evidence used to
confirm it. It must not silently harmonize conversions across diagnostic eras.

## Recommended longitudinal setup after a controlled-access extract

The research question and model architecture call for two distinct designs,
which must not be conflated:

1. **Baseline risk analysis.** At CIS diagnosis, use only information available
   at baseline to predict conversion in a preregistered horizon. This can
   address the clinical question but does not provide an RNN-LSTM with a
   multi-visit history.

2. **Landmark sequence analysis.** For a recurrent model, set an early
   landmark only after a feasibility audit shows adequate dated histories. Each
   eligible patient needs at least two genuine pre-index observations, no MS
   conversion before the landmark, and a future horizon after the landmark.
   All input visits must occur on or before the index; post-index visits must
   be excluded from model input. Each patient must remain in one evaluation
   partition even if a future protocol explicitly permits more than one
   landmark.

The scientifically preferred Hybrid SimpleRNN-LSTM analysis is the second
design, because it actually uses temporally ordered observations. The exact
landmark, minimum history, and 24-/36-/60-month horizon must remain
undecided until the controlled extract's visit and censoring distributions
are audited. A reasonable feasibility question is whether a 12-month
landmark with at least two pre-index visits and a subsequent 24-month horizon
has adequate event and non-event support; this is a question to test, not a
decision already made.

## Approval gate

Do not create labels or begin training until the selected source passes all of
the following:

- linkable pseudonymous patient identifier;
- validated baseline CIS/index date;
- dated genuine visits;
- confirmed conversion date and criterion/version for Class 1;
- last follow-up date for every candidate Class 0;
- a documented rule for unknown and censored records;
- patient-level split plan; and
- written permission for the approved research use.

The current decision is **NO-GO**.
