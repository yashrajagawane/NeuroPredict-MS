# Codex Kickoff Prompt — Build the MS Prediction Project

You are the engineering agent for my final-year project:

**Deep Learning Approach for Prediction of Multiple Sclerosis Using Hybrid RNN–LSTM**

I have provided a project documentation pack in this repository. Before writing code:

1. Read `AGENTS.md` and every relevant document in this pack.
2. Inspect the existing repository carefully. Do not assume files, datasets, models, or app features exist.
3. Produce a concise repository inventory: current files, languages/frameworks, dataset/model assets, and how to run existing code.
4. Compare the actual repository with the PRD/SRS and list any discrepancies.
5. Review `14_OPEN_DECISIONS.md`. Identify which decisions block dataset/model work.

## Critical requirements

- Current intended data: structured patient records collected across multiple visits.
- Current provisional target: MS / Non-MS classification. Confirm whether this represents status at an index visit or a future outcome before training.
- Proposed model: hybrid RNN → LSTM, evaluated against sensible baselines.
- Do not add MRI processing to the current scope.
- Do not invent a dataset, patient count, feature list, labels, sequence length, metrics, or achieved results.
- Synthetic data can be used for plumbing/UI tests only and must be labelled synthetic.
- A random visit-row split is not acceptable as the primary evaluation; split by patient.
- Fit preprocessing on training data only.
- The result must be described as research-only, not a diagnosis.

## First task: Phase 0 only

Do not implement the entire system yet. Complete repository reconnaissance and Phase 0 from `09_IMPLEMENTATION_ROADMAP.md`.

Return:
1. Repository inventory.
2. Existing code and assets that can be reused.
3. Missing inputs and blocking questions.
4. Proposed final directory structure.
5. Recommended stack with reasons, distinguishing confirmed from proposed choices.
6. Phase-by-phase implementation plan tailored to what is actually present.
7. Any risks or inconsistencies in the current project documents.

Do not start model training or fabricate a dataset. Wait for confirmation of the target/data decisions before implementing blocked phases. You may create a non-destructive project scaffold only if it does not lock in unresolved data assumptions.
