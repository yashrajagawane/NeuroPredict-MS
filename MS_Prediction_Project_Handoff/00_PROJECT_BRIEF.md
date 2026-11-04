# 00 — Project Brief

## Working title

**Deep Learning Approach for Prediction of Multiple Sclerosis Using Hybrid RNN–LSTM**

## Problem context

Multiple Sclerosis is a complex neurological condition. Patient information may be recorded at multiple clinical visits, and the proposed research explores whether a sequence model can learn useful patterns from structured records collected over time.

## Project idea

Build a research prototype that:

1. accepts structured patient information and visit records;
2. validates and prepares the data;
3. orders visits chronologically and creates patient sequences;
4. uses a proposed RNN → LSTM model to learn from those sequences;
5. produces an experimental MS / Non-MS class prediction; and
6. evaluates the model against held-out patient data using appropriate metrics.

## Current target — important clarification

The current presentation plan describes the output as **MS or Non-MS**. This is a binary status-classification task unless the team explicitly changes it. It is not automatically a prediction of future disability progression, relapse, or conversion from CIS. The index time and label definition still need confirmation.

## Intended users

- Doctor / authorized user persona for the planned interface.
- Student/researcher or project administrator for dataset preparation, model training, and evaluation.

The doctor persona is a design assumption for a demonstration interface, not a claim that clinicians have approved or will use the tool.

## Current project status

- Research review and presentation content have been prepared.
- A proposed workflow and architecture have been discussed.
- A previous inspection of available files found a LaTeX research review and diagrams, but no confirmed working application, trained model, or dataset. Re-inspect the repository before beginning implementation.

## Main output

A reproducible research prototype and documentation, not a clinically validated diagnostic product.

## Proposed stack

Python, Pandas, NumPy, scikit-learn, TensorFlow/Keras, Flask, and SQLite for an initial local prototype. Bootstrap/HTML/CSS/JavaScript may be used for a simple UI. Confirm the stack during Phase 0.

## Success at project level

- Dataset provenance, licensing/permission, target, and feature definitions are documented.
- Longitudinal sequences are genuinely derived from multiple time-stamped visits per patient.
- Evaluation uses patient-level separation and has no known preprocessing leakage.
- Baselines and RNN–LSTM are compared fairly on the same splits.
- Results include class-wise metrics and limitations.
- A user can enter/view sample records and request a research prediction only if the app/model is genuinely implemented.
- The project is reproducible and clearly labelled as non-clinical research.
