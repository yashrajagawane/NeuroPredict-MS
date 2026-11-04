# 11 — Privacy, Safety, and Ethics

## 1. Intended use

This project is an educational/research prototype. It is not a medical device, diagnostic service, or substitute for clinical assessment.

## 2. Required user-facing disclaimer

Display this near each result:

> Research prediction only — not a medical diagnosis. Do not use this result to make treatment decisions. Consult a qualified healthcare professional for medical assessment.

## 3. Data governance

- Confirm dataset source, license, permitted use, and institutional requirements before processing.
- Use de-identified or properly pseudonymized records.
- Do not commit patient-level files to GitHub or public repositories.
- Do not upload sensitive patient data to external AI agents or cloud tools unless explicitly permitted by the data owner and institutional policy.
- Keep data out of screenshots, logs, prompts, and issue trackers.
- Store only data necessary for the research objective.
- Restrict access and protect data at rest and in transit if the application is exposed beyond the local machine.

## 4. Model safety

- Model outputs must be described as experimental estimates.
- No treatment recommendations.
- Do not equate model confidence with clinical certainty.
- Do not show a probability as personal risk unless calibrated and appropriately validated.
- Explain limitations and possible false positives/false negatives.
- Any real-world use would require appropriate clinical, ethical, legal, and regulatory review.

## 5. Bias and generalization

Where dataset size and permissions allow, assess whether performance differs across clinically relevant subgroups and care settings. Report sample sizes and uncertainty; do not overinterpret small groups. A lack of subgroup evidence is not proof of fairness.

## 6. External AI agents

Before sharing a repository or data with Codex/Claude/another agent:
- Share this documentation pack and non-sensitive code.
- Keep real patient data, API secrets, credentials, and private identifiers out of the prompt/workspace unless approved.
- Use synthetic/demo examples for UI and API development.
- Do not ask an agent to invent missing labels, clinical facts, or validation results.
