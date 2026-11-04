# Candidate Source Comparison and Access Plan

## Decision

No public candidate is suitable for the requested **longitudinal,
patient-sequence CIS-to-MS conversion model**. The two public workbooks are
valuable baseline-outcome research sources, but they cannot supply genuine
RNN-LSTM sequences or an individually auditable conversion horizon.

The best next acquisition route is an approved collaborative request to
**MSBase/MSBasis**. A published MSBasis description reports 3,623 CIS
participants with a baseline CIS date, annual dated clinical follow-up,
EDSS/Kurtzke Functional System scores, relapses, treatment changes, and MRI
classification. It is large enough in principle to meet the 2,000-patient
aspiration, but feasibility, exact fields, criteria version, and permitted use
must be confirmed before any extract is accepted.

## Candidate assessment

| Candidate | Evidence of CIS-to-MS outcome | Public downloadable patient data | Longitudinal visits in downloadable data | Size and outcome evidence | Access / legal status | Suitability |
|---|---|---|---|---|---|---|
| Mexican Mendeley cohort | The publication reports 125 of 273 CIS patients met 2010 McDonald criteria for CDMS after 10 years. | Yes, official Data Base.xlsx. | No. One row per patient; no visit ID/date, conversion date, or last-follow-up date. | 273 rows; raw group values 125/148. Mapping to conversion is inferred from the matching publication count, not documented in a codebook. | CC BY 4.0; cite the dataset and publication. | Baseline-only exploratory reference at most; **not** a longitudinal RNN-LSTM dataset. |
| Lithuanian Mendeley cohort | The paper reports 49 of 138 CIS patients progressed to MS. Baseline CIS was confirmed under 2017 McDonald criteria; MS was confirmed by three neurologists. | Yes, official Database.xlsx. | No. One row per patient; no index, visit, conversion, or last-follow-up dates. | 138 rows; raw MS values 49/89. | CC BY 4.0; cite the dataset and publication. | Final-diagnosis cross-sectional label only; **not** a valid fixed-horizon longitudinal target. |
| GitHub mirror / concatenation | Reuses the Mexican and Lithuanian cohorts. | Yes, public code and derivatives. | No additional longitudinal information. | At most the two source cohorts; no independent cohort. | Repository code is MIT; source clinical data retain Mendeley provenance and CC BY attribution. | Do not treat it as a third dataset or use it to avoid source-level quality gates. |
| MultipleMS prospective cohort | The public site reports a 510-person prospective cohort with planned M0–M60 follow-up and clinical/MRI collection. It does not state CIS count, conversion labels, or conversion criteria on the public page. | No public patient-level file. | The protocol table lists repeated timepoints, but a usable extract has not been released publicly. | 510 total reported; too small for 2,000 even if all were eligible. | Collaboration/data-access request required through MultipleMS. | Potential secondary cohort only after written confirmation of CIS baseline and conversion fields. |
| MSBase/MSBasis | A published MSBasis description reports CIS within 12 months of onset, baseline CIS date, and longitudinal dated visits. The registry classifies confirmed MS under McDonald criteria, but the requested extract must verify date and criteria fields. | No anonymous public download. | Yes in the published design: annual visits include date, EDSS/KFS, relapses, and treatment changes. | 3,623 CIS participants reported at one study extraction. Current eligible count is unverified. | Approved MSBase member/collaborator request, feasibility review, data-use agreement, centre opt-out process. | **Best candidate** for a final longitudinal CIS-to-MS dataset, subject to approval and a feasibility extract. |
| MS PATHS | Includes CIS among its research population and has longitudinal clinical/MRI infrastructure. | No public patient-level download. | Longitudinal data are described, but CIS conversion-label availability and count are unverified. | No verified CIS conversion count for this task. | Research data request through participating institutions/Biogen. | Secondary access-controlled option; only pursue after MSBase feasibility is known. |
| CLIMB | Enrols MS or monosymptomatic disease, with yearly neurological examinations and MRI. | No public patient-level download identified. | Yes by protocol, but specific CIS conversion variables and availability are unverified. | No verified CIS-to-MS eligible count. | Contact study team; terms not published on the participant page. | Possible collaborator-led fallback. |
| CINOCIS (NCT03541226) | Exact prospective CIS cohort, with MRI and clinical monitoring; 134 completed participants. | No individual participant data sharing planned. | Repeated clinical/MRI monitoring by protocol. | 134, far below the target. | Trial registry states no IPD-sharing plan. | Scientifically relevant but unavailable and undersized. |
| OFSEP First Attack cohort | Public study description identifies a prospective French CIS/RRMS cohort, with clinical assessment, MRI, and biological sampling. | No public patient-level download identified. | Planned repeated clinical/MRI/biological assessments; exact exported visit and conversion fields are unverified. | Target of 500 patients reported for this cohort; CIS-only count and current usable count are unverified. | Researchers can submit a project through OFSEP data access. | Strong secondary controlled-access feasibility route; do not assume a conversion label until its data dictionary is reviewed. |
| SWIMS | Longitudinal Devon and Cornwall study of around 1,600 people with MS or CIS. | No public patient-level download identified. | Longitudinal by study design; detailed visit, conversion, and MRI export fields are unverified. | Mixed MS/CIS population; CIS-specific count and outcome timing not published on the study page. | University of Plymouth owns the contributed data; contact the study team. | Potential regional collaborator-led route, but it cannot be assumed to meet the 2,000-CIS target. |
| Queen Square 30-year CIS cohort | Published prospective CIS study with clinical and MRI assessments at repeated long-term timepoints. | No public individual-level dataset identified. | Yes in publication, but historical MRI/EDSS completeness varies and access terms are not publicly stated. | 132 recruited; 80 known to have developed MS by 30 years. | Source-owner/University College London collaboration would be required. | Valuable external validation concept only; too small and insufficiently accessible for primary training. |

## Primary sources

- [Mexican Mendeley dataset](https://doi.org/10.17632/8wk5hjx7x2.1) and
  [publication](https://pubmed.ncbi.nlm.nih.gov/37429750/).
- [Lithuanian Mendeley dataset](https://doi.org/10.17632/yjfydt34rs.1) and
  [open-access publication](https://doi.org/10.3390/medicina58091178).
- [MultipleMS data page](https://multiplems.eu/data).
- [MSBasis longitudinal CIS cohort description](https://pmc.ncbi.nlm.nih.gov/articles/PMC4435703/),
  [MSBase membership terms](https://www.msbase.org/membership/), and
  [MSBase request governance](https://www.msbase.org/media/1701/msbase-foundation-p-p-authorship-and-publication-v30-june-2023.pdf).
- [MS PATHS description and access statement](https://pmc.ncbi.nlm.nih.gov/articles/PMC7426489/).
- [CLIMB study page](https://brighammscenter.org/research/research-studies/climb-study).
- [CINOCIS registration](https://clinicaltrials.gov/study/NCT03541226).
- [OFSEP CIS cohort](https://www.ofsep.org/en/studies/cohorte-cis) and
  [OFSEP data-access page](https://www.ofsep.org/en/28-data-access).
- [SWIMS study page](https://www.plymouth.ac.uk/research/penctu/swims).
- [Queen Square 30-year CIS cohort publication](https://pmc.ncbi.nlm.nih.gov/articles/PMC6973080/).

## Required access decision

Do not request or ingest a broad registry dump. Submit a narrow scientific
feasibility request that asks whether a compliant extract can meet the contract
in [msbase_access_request_spec.md](../contract/msbase_access_request_spec.md).
The request must be made through a supervisor, participating neurologist, or
eligible institutional collaborator as required by the registry.
