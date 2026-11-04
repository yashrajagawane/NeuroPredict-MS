# Patient Split Report

No train, validation, or test assignments have been created. The current
interim cohorts do not have a validated future-conversion label, dated
longitudinal observations, or a clinically approved prediction index. Creating
assignments for them would imply a supervised dataset that does not exist.

The reusable `scripts/create_patient_splits.py` refuses to write a manifest
unless the normalized tables pass validation and the caller explicitly
confirms approved access, baseline CIS, label adjudication, and feature timing.
It assigns patient IDs, never visit rows, and records cohort ID, split, seed,
and conversion status. Default proportions are 70%/15%/15%; they remain
configurable. The current implementation uses a seeded random patient-level
assignment and does not claim stratification. Class-aware stratification and
small-sample feasibility checks remain to be added and validated before use
with an approved cohort.

Manifest path requested by the future workflow:
`data/modeling/patient_split_manifest.csv`. No file has been created.
