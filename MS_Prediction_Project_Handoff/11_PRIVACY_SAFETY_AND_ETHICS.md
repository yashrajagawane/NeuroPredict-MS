# 11 — Privacy, Safety, and Ethics

## 1. Intended use and user roles

NeuroPredict-MS is a research and educational project investigating future CIS-to-MS conversion and providing a doctor-facing research application. It is not a medical device, clinical diagnostic service, treatment recommender, or substitute for professional judgment. The “doctor” application role is a product requirement, not evidence of clinician endorsement or authority to use patient records.

## 2. Required user-facing limitation

Display with every actual prediction:

> Research prediction only — not a medical diagnosis. Do not use this result to make treatment decisions. Consult a qualified healthcare professional for medical assessment.

Also show that the target is future CIS-to-MS conversion, the model version, prediction timestamp, and known limitations. Do not display a probability as personal risk unless calibration, threshold behavior, and display policy have been reviewed. Before a valid model is available, show an unavailable state and no prediction.

## 3. Data governance and privacy

- Verify source, license, permitted use, ethics/consent basis, institution policy, and data-use agreement before acquiring or processing restricted clinical data.
- Use pseudonymous IDs and data minimization. Never place direct identifiers in development/test fixtures, logs, Git, screenshots, prompts, or issue trackers.
- Keep raw, linkage-key, and processed/model layers separate with approved access control. Hashes and manifests must not reveal restricted patient information.
- Do not upload patient records, credentials, tokens, or secrets to external AI tools or cloud services unless explicitly permitted by the data owner and institution.
- Require authenticated sessions, server-side role authorization, patient-scoped access, Supabase PostgreSQL RLS, encryption in transit, secure credential storage, and approved retention/deletion/audit procedures before real-record use.
- Never expose Supabase service-role keys or database credentials in the frontend bundle.
- Prediction history must record only real system requests/results with approved metadata; unavailable/failed requests cannot contain an invented class.

## 4. Model and application safety

- No training or prediction from the existing public interim data for the future-conversion objective.
- Do not assign unknown or insufficient follow-up as Class 0; exclude post-index information from inputs.
- Do not equate model confidence with clinical certainty, recommend treatment, or claim prospective validation, fairness, or clinical utility without evidence.
- Failure, insufficient history, absent model, schema incompatibility, or access denial must fail closed and clearly state that prediction is unavailable.
- Any real-world use requires separate clinical, ethical, legal, security, and regulatory review.

## 5. Bias and generalization

When permitted data and adequate subgroup counts exist, report cohort composition and uncertainty for relevant subgroups and centres. Small or absent groups do not support fairness claims. Cross-cohort differences in population, measurement, and diagnostic criteria must be discussed.

## 6. External tools and synthetic data

Share only non-sensitive code and documentation with external agents/services unless explicit authorization permits more. Synthetic data may support software tests only, must be labelled unmistakably, and must never be presented as genuine patients, clinical predictions, or clinical performance.
