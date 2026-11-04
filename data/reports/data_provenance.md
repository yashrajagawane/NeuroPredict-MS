# Data Provenance

## Scope

This provenance record covers the two official public workbooks acquired on
2026-11-04 for evaluation. They are preserved unchanged in data/raw/ and are
not committed to Git. This document does not assert that either file is an
approved longitudinal training dataset.

## Acquired sources

| Source | Official dataset and publication | Original file | License | Official SHA-256 | Local verification |
|---|---|---|---|---|---|
| Mexican prospective CIS cohort | [Mendeley Data DOI](https://doi.org/10.17632/8wk5hjx7x2.1); [Chavarria et al., 2023](https://doi.org/10.1016/j.arcmed.2023.102843) | Data Base.xlsx | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) | 070bfe92c78ef3b0bbd3169b61b8befa98c687b61322298b9143d540ae3c00d7 | Match |
| Lithuanian retrospective CIS cohort | [Mendeley Data DOI](https://doi.org/10.17632/yjfydt34rs.1); [Balnytė et al., 2022](https://doi.org/10.3390/medicina58091178) | Database.xlsx | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) | 0e9e56026c9de83c38edbe934cd93a4e44cd845507a0e844a4b3d1926e1e8880 | Match |

The Mendeley snapshots reported that both datasets are non-confidential,
publicly downloadable, Version 1 datasets. Their source metadata and file
checksums were queried before download. The local audit records the observed
hashes in [public_source_audit.json](../audit/public_source_audit.json).

## Source context

- The Mexican publication describes a single-centre prospective cohort of
  273 newly diagnosed CIS patients enrolled from 2006 to 2010. It reports
  10 years of follow-up and 125 conversions under the 2010 McDonald criteria.
  The workbook contains 273 data rows.
- The Lithuanian publication describes retrospective records from 2015 through
  2020. It reports 138 CIS patients, of whom 49 progressed to MS. The workbook
  contains 138 data rows.
- The public GitHub repository
  [tsantosh7/Multiple-Sclerosis-Conversion](https://github.com/tsantosh7/Multiple-Sclerosis-Conversion)
  mirrors both datasets and a concatenated derivative. It does not add
  patient-level visit dates or longitudinal observations. Its MIT repository
  license should not replace the primary Mendeley data citation and CC BY
  attribution requirements.

## Handling rules

- Raw workbooks remain unchanged and local.
- No row-level clinical data appear in Markdown reports, screenshots, or logs.
- Derived patient-level datasets are deliberately absent because the public
  files fail the longitudinal and label-timing gates.
- Any future controlled-access extract must be stored outside public version
  control, accompanied by its data-use agreement, data dictionary, release
  identifier, and hash.

## Reproducibility

data/scripts/audit_public_cis_sources.py uses the standard library to inspect
the raw XLSX XML and emits the manifest, missingness report, and cohort-size
chart. It never alters the source workbooks.
