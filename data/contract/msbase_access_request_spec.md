# MSBase/MSBasis Feasibility Request Specification

## Purpose

This is a narrow feasibility specification for an eligible institutional
collaborator. It is not a request to download a broad registry dump and does
not authorize acquisition automatically.

The published MSBasis design is highly aligned with the project: CIS patients
were enrolled close to first onset and the registry's minimum data model
describes dated visits, EDSS/KFS, relapses, and treatment dates. MSBase's
current membership rules require an appropriate clinical principal investigator
and governed research request. The actual historical extract must still be
checked field by field.

## Proposed scientific question

Among patients recorded with CIS at a confirmed baseline/index date, estimate
the risk of clinically confirmed MS conversion within a prespecified future
horizon using only data observed on or before the index. The project is
educational research, not a clinical diagnostic product or decision-support
tool.

## First request: aggregate feasibility only

Before requesting patient-level data, request a de-identified aggregate report
for 24-, 36-, and 60-month candidate horizons:

- count of patients with confirmed CIS at baseline;
- count with a confirmed post-index MS conversion and a usable conversion date;
- count with no conversion and last follow-up through each horizon;
- count censored/unknown before each horizon;
- count with two or more dated pre-index visits for candidate landmarks;
- visit-count distribution and follow-up-duration distribution;
- availability/missingness for age/sex, CIS presentation, OCB/IgG, dated EDSS,
  dated relapse, MRI lesion metrics, and treatment fields;
- counts by site/country, calendar era, diagnostic criteria version, and
  treatment exposure; and
- a statement confirming whether required dates are directly recorded or
  derived, and how any date shifting preserves interval validity.

The feasibility report must distinguish total registry participants from the
eligible analysis cohort. It should not disclose direct identifiers or small
cell counts contrary to registry policy.

## Conditional patient-level extract requirements

If feasibility is favourable and data access is approved, request only the
minimum pseudonymized fields:

### Patient and diagnosis

- stable pseudonymous patient key and optional pseudonymous centre key;
- sex and either age at CIS/index or a permitted birth-year representation;
- CIS onset date and CIS diagnosis/index date;
- baseline CIS presentation/phenotype;
- diagnosis status history, MS diagnosis/conversion date, and MS phenotype;
- the original diagnostic criteria version, whether clinician-entered or
  derived, and diagnostic certainty;
- last documented follow-up/visit date.

### Longitudinal clinical history

- visit identifier, visit date, EDSS, and KFS score components;
- dated relapse records and CNS-region information;
- corticosteroid exposure where it affects relapse interpretation;
- disease-modifying treatment start/end dates and agent category.

### Paraclinical and MRI data, only where documented

- test date, source format, and raw unit/coding for CSF OCB and IgG index;
- MRI date plus total T2 count, new/enlarging T2 count, gadolinium-enhancing
  count, and lesion-location counts or presence indicators;
- scan/report linkage and protocol/site metadata sufficient to identify
  incompatible measures;
- evoked potentials, NfL, vitamin D, or other candidate biomarkers only if
  source definition, date, units, and missingness are retained.

Do not request free-text notes or direct identifiers. Do not request fields
that cannot be used under the approved protocol.

## Essential confirmations from the registry team

1. Can historical MSBasis/MSBase records supply an auditable conversion date
   rather than only a current phenotype?
2. Is the original diagnostic criterion/version directly available for each
   conversion, and how were derived dates/criteria calculated?
3. Can a last-follow-up date be exported for all patients?
4. Are dated visits patient-linkable, and are serial MRI measures genuinely
   comparable within and across centres?
5. Which centres consent to secondary use for this research question?
6. Are date transformations, small-cell disclosure rules, and cross-border
   transfer constraints compatible with the proposed label validation?
7. Are treatment histories sufficiently complete to describe and adjust for
   treatment-confounding rather than leaking post-index care decisions?
8. Is there a source data dictionary and a release/version identifier?

## Governance and analysis controls

- Submit through a senior treating neurologist/MSBase PI or another registry
  route explicitly authorized by MSBase.
- Obtain institutional ethics/IRB review and execute the applicable data-use
  agreement before patient-level transfer.
- Store data in approved encrypted local/institutional storage. Keep raw data
  outside public Git repositories and do not upload it to unapproved services.
- Assign project pseudonyms; keep any linkage file separately restricted.
- Register a data-management plan, extraction version, hashes, cleaning log,
  and patient-level split plan before model training.
- Do not report predictions as medical advice or make claims of clinical
  performance without external validation and governance review.

## Fallback controlled-access routes

If MSBase feasibility is inadequate, approach OFSEP first. Its public
description identifies a prospective French CIS/RRMS First Attack cohort with
clinical assessment, MRI, and biological sampling, and states that researchers
can submit data-access projects. MultipleMS, MS PATHS, CLIMB, SWIMS, and the
UK MS Register are secondary possibilities, but each requires explicit
confirmation of baseline-CIS eligibility, conversion timing, longitudinal
linkage, and permitted use before it can be considered a substitute.
