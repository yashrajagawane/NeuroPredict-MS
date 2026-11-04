# 20 — Provisional Research-App Usability Walkthrough

**Status:** Draft protocol for the current static, no-data prototype. No participant session has been conducted.
**Purpose:** Review whether users can navigate the research-only shell and understand its unavailable states. This is not a clinical validation, diagnostic-utility study, or evaluation of prediction quality.
**Scope:** Routes and static states currently present in the React application. Patient management, clinical timelines, prediction results, authentication, and backend workflows are out of scope because they are not implemented.

## 1. Preconditions

- Use only the local/static application with no patient records, credentials, or connected database.
- Confirm that every screen displays or links to the research-only limitation and does not imply diagnosis or treatment guidance.
- Follow institutional requirements for recruiting, consent, recording, and review. If those requirements are unclear, obtain the applicable determination before inviting participants or collecting feedback.
- Do not record names, contact details, health information, patient stories, or identifiable screen/audio recordings in research notes.
- Explain that this is a software prototype review, not a clinical consultation, and that feedback will not be used as evidence of clinical safety or effectiveness.

## 2. Session outline

1. Give the participant the purpose statement above and ask them to describe what they think the application is for.
2. Ask them to locate the research-use limitation and describe what the prototype does not currently provide.
3. Ask them to navigate among the six module entry routes and identify which features are unavailable.
4. Ask them to explain what they would expect to happen when data, authentication, or a prediction service is unavailable.
5. Ask them to identify any wording, navigation, contrast, focus, or layout that makes the prototype confusing or inaccessible.
6. Close by restating that no patient data or clinically actionable predictions are present, and invite general interface feedback.

Use neutral prompts. Do not ask participants to diagnose a case, judge a risk score, select treatment, or infer conversion from clinical features. Do not simulate a patient record or prediction result.

## 3. Notes to capture (only if approved)

Use a session code unrelated to a participant identity. Record task completion (completed / needed help / not completed), the route/state involved, the observed usability issue, and a short de-identified paraphrase. Avoid exact timestamps and details that could identify a participant. Store notes only in an institutionally approved location with an approved retention/deletion rule.

Do not claim quantitative usability success from an informal walkthrough. Summarize recurring confusion, accessibility barriers, and high-impact wording issues separately from individual preferences. Any changes to clinical workflow or intended-use wording require the relevant project owner and clinical/governance review.

## 4. Review checklist

- [ ] Participant can state that this is a research prototype and not a diagnostic system.
- [ ] Participant can find the six module routes and distinguish available shell navigation from unavailable functionality.
- [ ] Empty, unavailable, and access-denied placeholders are not mistaken for successful data access or a prediction.
- [ ] Keyboard navigation and visible focus are usable on the tested routes.
- [ ] Text remains understandable at enlarged zoom and narrow viewport sizes.
- [ ] No screen requests real patient information or encourages clinical action.
- [ ] Findings, limitations, and unresolved issues are documented without participant identifiers or patient data.

## 5. Acceptance boundary and blockers

Completing this protocol does not complete Phase 60. The required walkthrough, participant availability, any applicable institutional review, issue fixes, and retest remain outstanding. Since actual patient screens and service flows do not exist, this protocol covers only the static shell and cannot establish clinician workflow suitability or safety.
