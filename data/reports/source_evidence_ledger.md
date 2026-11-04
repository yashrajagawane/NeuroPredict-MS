# Longitudinal CIS-to-MS Source Evidence Ledger

## How to read this ledger

This is a source-selection record, not a claim that every named study can be
used. “Described longitudinally” refers to the protocol or publication.
“Downloadable longitudinally” is reserved for an actual permitted
patient-linked file with repeated dates and outcomes. The distinction is
critical for this project.

## 1. Mexican prospective CIS cohort

- **Provider and access:** Official [Mendeley Data record](https://doi.org/10.17632/8wk5hjx7x2.1),
  Version 1, containing Data Base.xlsx; public CC BY 4.0 download.
- **Publication:** [Chavarria et al., 2023](https://pubmed.ncbi.nlm.nih.gov/37429750/).
- **Population and criteria:** Single-centre prospective cohort of newly
  diagnosed CIS participants enrolled 2006–2010. The publication reports
  conversion assessment with the 2010 McDonald criteria at ten years.
- **Downloaded evidence:** 273 source rows, 272 unique source IDs, one
  duplicate identifier, 20 columns. It contains demographics, coded initial
  symptoms, OCB, evoked potentials, binary MRI-location indicators, initial
  and final EDSS, and group.
- **Outcome/follow-up:** Publication-level report: 125/273 conversions over
  ten years. Downloaded group codes are 125/148 but lack a codebook. No
  conversion dates, last-follow-up dates, visit dates, or repeated visit rows.
- **Verdict:** Publicly usable under the dataset license with attribution, but
  unsuitable for the requested longitudinal prediction target.

## 2. Lithuanian retrospective CIS cohort

- **Provider and access:** Official [Mendeley Data record](https://doi.org/10.17632/yjfydt34rs.1),
  Version 1, containing Database.xlsx; public CC BY 4.0 download.
- **Publication:** [Balnytė et al., 2022](https://doi.org/10.3390/medicina58091178).
- **Population and criteria:** Retrospective Lithuanian clinical-record study
  spanning 2015–2020; the publication describes specialist CIS/MS assessment
  in the 2017 McDonald era.
- **Downloaded evidence:** 138 source rows and 138 unique source IDs, 44
  columns. It contains symptom flags, MRI-location/presence fields, selected
  CSF and evoked-potential fields, and an MS flag.
- **Outcome/follow-up:** Publication-level report: 49 of 138 progressed to
  MS. The downloaded MS flag is 49 positive/89 negative but has no index,
  conversion, or last-follow-up date and no repeated visit records.
- **Verdict:** Publicly usable under the dataset license with attribution, but
  a final-status cross-sectional extract rather than a dated outcome cohort.

## 3. Multiple-Sclerosis-Conversion GitHub repository

- **Provider and access:** [tsantosh7/Multiple-Sclerosis-Conversion](https://github.com/tsantosh7/Multiple-Sclerosis-Conversion);
  code is MIT licensed.
- **Original data:** The repository identifies the two Mendeley sources above
  and includes a concatenated derivative.
- **Longitudinal evidence:** No additional patient-linked dates, visit records,
  or conversion timing are supplied.
- **Verdict:** It is not an independent cohort and must not be counted as one.
  The primary data licenses/citations, not merely the repository license,
  govern reused source data.

## 4. MultipleMS

- **Provider and access:** [MultipleMS data page](https://multiplems.eu/data);
  access/collaboration requires contact with the project rather than a public
  patient-level download.
- **Population and follow-up:** The public page reports a 510-person
  prospective cohort with planned/observed M0, M6, M12, M24, M36, M48, and M60
  timepoints; it shows EDSS, relapse, and MRI-date coverage.
- **Unknowns:** The page does not establish the number with baseline CIS,
  confirmed conversion count/date, last follow-up per patient, diagnostic
  criteria, or a permitted patient-level export.
- **Verdict:** Potential secondary feasibility route. Its reported total is
  below 2,000 and it must not be assumed that all 510 are eligible CIS cases.

## 5. MSBase/MSBasis

- **Provider and access:** [MSBase](https://www.msbase.org/membership/);
  global data access is a governed collaborative request made through eligible
  members/clinical PIs.
- **Publication/protocol evidence:** The [MSBasis publication](https://pmc.ncbi.nlm.nih.gov/articles/PMC4435703/)
  reported 3,623 CIS participants. The [MSBASIS description](https://hdl.handle.net/11343/127259)
  describes CIS within 12 months of onset and a minimum observation set with
  visit date, EDSS, KFS, relapse onset, and treatment dates.
- **Potential conversion timing:** Current [iMed documentation](https://www.msbase.org/media/0wohaehq/imed-web-ms-user-guide-version-20.pdf)
  describes CIS/RR classification based on onset, confirmed-diagnosis, and/or
  relapse dates. A data request must establish what date and criterion fields
  exist in the historical extract.
- **Unknowns:** Current eligible patient count, event counts at any horizon,
  patient-level last follow-up, MRI count detail, and permission for this exact
  research question.
- **Verdict:** Best primary candidate, but controlled access and a feasibility
  extract are mandatory before selection.

## 6. MS PATHS

- **Provider and access:** [MS PATHS publication and data-access statement](https://pmc.ncbi.nlm.nih.gov/articles/PMC7426489/);
  no public patient-level download. Requests are directed through the program
  and its governance.
- **Population and longitudinal data:** It includes people diagnosed with MS,
  including CIS, with linked pseudonymous longitudinal clinical data and
  standardized MRI infrastructure.
- **Unknowns:** Baseline-CIS count, conversion-date availability, criterion
  version, sufficient follow-up, and whether the desired extract can be
  released to this project.
- **Verdict:** A high-capacity secondary controlled route, not a public
  dataset and not yet a confirmed CIS-to-MS conversion cohort.

## 7. CLIMB

- **Provider and access:** [Brigham CLIMB study](https://brighammscenter.org/research/research-studies/climb-study).
- **Population and longitudinal data:** Eligible participants include MS or
  monosymptomatic disease; neurological examination and MRI are yearly, with
  blood and questionnaires.
- **Unknowns:** CIS-specific baseline count, individual conversion dates,
  data-access approval, diagnostic criteria, MRI variables, and allowable
  linkage.
- **Verdict:** A plausible collaborator-led fallback only.

## 8. CINOCIS

- **Provider and access:** [ClinicalTrials.gov NCT03541226](https://clinicaltrials.gov/study/NCT03541226).
- **Population and longitudinal data:** Prospective CIS monitoring with
  clinical/MRI observations; final enrollment reported as 134.
- **Access and limitation:** The registry indicates no individual participant
  data-sharing plan. Even if accessible, the study is far below 2,000.
- **Verdict:** Scientifically aligned but not an available primary source.

## 9. OFSEP First Attack cohort

- **Provider and access:** [OFSEP CIS cohort](https://www.ofsep.org/en/studies/cohorte-cis)
  and [data-access process](https://www.ofsep.org/en/28-data-access).
- **Population and longitudinal data:** Prospective French CIS/RRMS First
  Attack cohort, described with clinical assessment, MRI, and biological
  samples; its stated proposal targets 500 patients.
- **Unknowns:** Current enrollment, CIS-only count, conversion/last-follow-up
  dates, exportable visit linkage, MRI variable definitions, and terms for an
  external educational project.
- **Verdict:** Strong secondary controlled-access feasibility route.

## 10. SWIMS

- **Provider and access:** [University of Plymouth SWIMS study](https://www.plymouth.ac.uk/research/penctu/swims).
- **Population and longitudinal data:** Around 1,600 people with MS or CIS in
  a long-term regional study.
- **Unknowns:** CIS-only number, conversion definitions/dates, visit-level
  export, MRI detail, access agreement, and criteria version.
- **Verdict:** May support a targeted partnership but should not be treated as
  a 1,600-CIS cohort.

## 11. Queen Square 30-year CIS cohort

- **Publication:** [30-year clinical and MRI observational study](https://pmc.ncbi.nlm.nih.gov/articles/PMC6973080/).
- **Population and longitudinal data:** 132 CIS participants prospectively
  followed at planned long-term clinical and MRI timepoints; 80 were known to
  have developed MS by 30 years in the publication.
- **Limitations:** Some historical scans/outcomes are missing, early EDSS was
  not captured consistently, no public IPD access was identified, and the
  cohort is small.
- **Verdict:** Useful as scientific precedent or possible external-validation
  discussion, not a primary training source.

## Overall conclusion

The public sources establish that genuine CIS conversion research exists but do
not supply the individual temporal evidence required here. MSBase/MSBasis is
the most promising route to the aspiration of approximately 2,000 eligible
patients; its historical 3,623-CIS report is not a guarantee of a usable
current export. No controlled source should be acquired or modeled until
written approval and feasibility results establish the required dates, labels,
visits, and data-use terms.
