# Processing Report

## Existing interim processing

The existing `scripts/prepare_interim_cis_datasets.py` reads the two acquired
official workbooks and writes source-specific interim CSVs. It preserves every
record, raw clinical code, missing value, source row number, and source ID.
Transformations are limited to explicit column renaming and provenance
metadata. It does not impute, recode uncertain values, deduplicate, combine,
or construct visits.

| Cohort | Rows retained | Unique source IDs | Source covariate columns retained | Valid future conversion labels | Genuine visit rows |
|---|---:|---:|---:|---:|---:|
| Mexican | 273 | 272 | 17 | 0 | 0 available |
| Lithuanian | 138 | 138 | 42 | 0 | 0 available |

The Mexican `group` codes (1: 125, 2: 148) remain unlabelled. The Lithuanian
`MS` field (0: 89, 1: 49) is documented as final MS/non-MS grouping but has no
patient-specific index, event, or follow-up dates. Neither is approved as a
future conversion label. Each cohort has zero approved model input features.

## Reproduction

    python .\data\scripts\prepare_datasets.py --repo-root . --source-workbooks
    python -m unittest discover -s .\data\tests -v

The preparation command regenerates only the separate ignored interim
extracts. It does not create longitudinal tables or fit preprocessing.
