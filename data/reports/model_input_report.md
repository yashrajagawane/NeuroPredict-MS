# Model Input Readiness Report

## Current decision

**NO-GO for model input generation and Hybrid RNN-LSTM training.** Both
source-specific interim cohorts have zero approved model features and zero
valid future conversion labels. Neither contains repeated dated visits.

## Implemented reusable path

`scripts/prepare_model_inputs.py` reads approved patients, visits, and outcomes
CSVs, applies the readiness gates, and constructs chronological in-memory
sequences from genuine visits at or before each index. It rejects identifier
and target fields as features. It writes no model tensors or datasets.

The current utility does not fit imputation, scaling, encoding, or feature
selection. A future implementation must fit all learned transforms using
training patients only, preserve missingness semantics, define padding/masking
for unequal histories, and test static-feature handling before use. Static
features are not copied into every clinical visit as though newly measured.
Post-index visits are excluded from model inputs.

## Current availability

| Cohort | Patients/records | Genuine dated visits | Candidate representations among 14 | Approved inputs | Valid future labels |
|---|---:|---:|---:|---:|---:|
| Mexican | 273 records / 272 IDs | 0 available | 8 | 0 | 0 |
| Lithuanian | 138 records / 138 IDs | 0 available | 7 | 0 | 0 |

Candidate representations are raw source fields or codes, not model-ready
features. Cohort definitions and code meanings remain unharmonized.
