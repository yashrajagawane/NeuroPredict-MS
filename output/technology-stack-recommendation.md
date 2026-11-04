# Recommended Technology Stack

**Project:** Deep Learning Approach for Prediction of Multiple Sclerosis Using Hybrid RNN-LSTM  
**Assessment date:** 2026-11-04  
**Purpose:** Read-only technology recommendation before implementation approval

## Executive recommendation

Use a Python-first, local-first stack: Python 3.12, Pandas, NumPy, scikit-learn, TensorFlow/Keras, Matplotlib/Seaborn, FastAPI, Jinja templates with Bootstrap, and SQLite for a local prototype. Keep PostgreSQL, React, and hosted inference as later options if multi-user deployment or richer UI needs justify them.

The immediate next phase should remain data feasibility and requirements alignment, not model training. The handoff documents describe provisional MS/Non-MS status classification in places, while the clarified project objective in this conversation is future CIS-to-MS conversion. That target, index definition, and prediction horizon need to be reflected consistently in the project requirements before model development.

The current repository has source audits and guarded preparation utilities, but no approved longitudinal cohort, model implementation, trained artifact, backend, or frontend. The latest logged test run reports 13 passed and 0 failed; tests were not rerun for this assessment.

## Stack selection

| Component | Recommendation | Reason | Alternatives and trade-offs |
|---|---|---|---|
| Programming language | **Python 3.12** | The existing pipeline and planned ML stack are Python. Python 3.12 is within the documented compatibility range for both TensorFlow and PyTorch. | R or Julia could support analysis, but would split implementation across languages without a clear benefit. |
| Data processing | **Pandas + NumPy** | Suitable for current CSVs and linked patient/visit/outcome tables. Pandas supports tabular, missing, time-series, and spreadsheet data; NumPy supports array-based ML workflows. | Polars may help at much larger scale or under memory pressure, but current cohort size does not justify adding it. |
| Classical ML | **scikit-learn** | Provides interpretable baselines, metrics, preprocessing, and pipelines. Pipelines help ensure learned transformations are fitted on training data only. | Avoid building custom preprocessing infrastructure before the source schema and target are finalized. |
| Deep learning | **TensorFlow/Keras** | Already proposed in the handoff and directly supports the required recurrent layers and masking. It is a simple fit for the sequence-to-one experiment. | PyTorch is also suitable and gives explicit training-loop control. Choose it only if the team has stronger PyTorch experience; do not maintain both. |
| Model architecture | **Keras `SimpleRNN(return_sequences=True) -> LSTM -> Dense(sigmoid)`** | Matches the proposed hybrid architecture. The SimpleRNN must return a sequence for the LSTM to process its outputs. | Choose widths, masking, dropout, and padding only after reviewing real sequence lengths and cohort size. The hybrid is not automatically better than baselines. |
| Visualization | **Matplotlib + Seaborn** | Suitable for static research figures: class counts, missingness, confusion matrices, ROC/PR curves, and training histories. | Plotly is useful for an interactive evaluation page, but is not needed for initial offline analysis. |
| Backend | **FastAPI** | Fits the proposed API contract and provides request validation and generated OpenAPI/interactive docs. | Flask is simpler for a small server-rendered application and is already suggested by the handoff. Django adds an ORM/admin/authentication system that is unnecessary unless scope expands. |
| Frontend | **Jinja templates + Bootstrap first** | Keeps the prototype in one Python application and avoids a second toolchain while the app requirement is still open. | React fits a richer interactive dashboard or separately staffed UI. Next.js adds server rendering and routing complexity not currently needed. |
| Database | **SQLite locally; PostgreSQL later if justified** | SQLite suits a local single-user demonstration and requires no database server. | PostgreSQL is appropriate for concurrent users, hosted persistence, or multi-user access. Do not store real health data in a free hosting database without approved governance. |
| Model deployment | **Offline training; local API inference for demonstration** | Keeps experimentation separate from prediction requests and versions the model alongside its preprocessing and feature schema. | Consider hosted inference only after model validity, data access, and platform requirements are established. |
| Testing | **pytest, FastAPI TestClient/httpx, and ML pipeline tests** | Covers data contracts, patient-level overlap, chronology, leakage, endpoint behavior, and artifact compatibility. | Existing tests use `unittest`; keep them or migrate gradually rather than maintaining two conventions indefinitely. |
| Environment | **Python 3.12; `venv` + pip initially; `uv` optional** | A virtual environment and pinned dependencies are adequate. Python 3.12 is a documented compatibility intersection for TensorFlow and PyTorch. | Conda is reasonable if already familiar or needed for a specific hardware setup. Pin after stack approval and runtime selection. |
| Hosting | **Local demo first; Render or similar only for synthetic/demo data** | Render offers free instances with meaningful limits: services spin down and local filesystem changes are ephemeral; free Postgres databases expire after 30 days. | Vercel Hobby is free for personal projects and fits a frontend better than a Python ML backend. Streamlit Community Cloud offers a free Python app path but represents a different application style. Recheck provider terms before use. |

## Proposed system architecture

```text
Approved data source
       |
       v
Read-only raw files -> source audit -> normalized patients / visits / outcomes
                                          |
                                          v
                             contract and clinical approval gate
                                          |
                                          v
                          patient-level split: train / validation / test
                                          |
                                          v
                         train-only preprocessing and sequence builder
                                  |                   |
                                  v                   v
                        scikit-learn baselines   Keras RNN -> LSTM
                                  \                   /
                                   v                 v
                                patient-level evaluation
                                             |
                                             v
                           versioned model + preprocessing metadata
                                             |
                                      local FastAPI
                                             |
                                      Jinja + Bootstrap
                                             |
                               SQLite only for local demo if needed
```

The prediction setup must be defined before model inputs are created. A later-landmark design can use multiple visits; baseline-only prediction would not demonstrate temporal learning. Select the landmark and prediction horizon only after reviewing an approved cohort's visit and follow-up distributions.

## Suggested project structure after approval

```text
project/
|-- pyproject.toml                 # after stack approval
|-- README.md
|-- configs/
|   `-- example.yaml               # non-sensitive defaults
|-- data/
|   |-- raw/                       # immutable, access-controlled source data
|   |-- processed/
|   |   |-- interim/               # existing cohort-specific extracts
|   |   `-- longitudinal/          # only after approved acquisition
|   |-- templates/                 # existing header-only schemas
|   |-- modeling/                  # split manifest and model-input metadata
|   |-- reports/                   # data and evaluation reports
|   |-- scripts/                   # existing audit and guarded utilities
|   `-- tests/                     # existing data tests
|-- src/
|   `-- ms_prediction/
|       |-- data/                  # validation and sequence preparation
|       |-- models/                # baselines and hybrid network
|       |-- evaluation/            # metrics and plots
|       |-- api/                   # FastAPI routes and schemas
|       `-- web/                   # templates and static assets
|-- artifacts/                     # versioned model/preprocessor outputs, ignored
`-- tests/
    |-- unit/
    |-- integration/
    `-- ml/
```

This is a recommendation, not the current repository structure. Keep the existing `data/` layout. Introduce `src/` when implementation begins. Do not populate longitudinal or artifact directories with empty files that could be mistaken for approved data.

## Development roadmap

1. **Resolve requirements and data access:** align project documents on future CIS-to-MS conversion, index, horizon, and application scope; obtain permission and a data dictionary for a candidate longitudinal cohort.
2. **Feasibility audit:** quantify patient and visit counts, outcome certainty, follow-up, features, missingness, and leakage; decide whether the source supports the target and sequence model.
3. **Normalize and validate:** create linked patient, visit, and outcome CSVs only from approved records; preserve provenance and validate the contract.
4. **Model dataset design:** freeze index/horizon and inclusion rules; define patient-level partitions and check whether class stratification is feasible.
5. **Baselines and preprocessing:** fit transformations on training patients only; evaluate simpler models before the hybrid network.
6. **Hybrid RNN-LSTM experiment:** implement only if the cohort contains sufficient genuine pre-index sequences; compare on the same patient partitions and evaluation protocol.
7. **Evaluation and reporting:** report class-wise metrics, uncertainty where feasible, and limitations; keep the final test set untouched during model selection.
8. **Application, if approved:** build the API and UI around a saved, versioned model and preprocessing artifact; begin locally.
9. **Deployment review:** consider hosting only with permitted, non-sensitive data and verified platform storage/access behavior.

## Technical risks and limitations

- **Target inconsistency:** handoff documents describe current-status MS/Non-MS classification, while the clarified project objective is future CIS-to-MS conversion. Update the project requirements as a group before implementation.
- **Data suitability:** acquired public workbooks lack patient-linked dated visits, conversion dates, and patient-level follow-up. They cannot support longitudinal prediction or a meaningful RNN-LSTM evaluation.
- **Feature leakage:** final diagnosis, conversion date, post-index EDSS/MRI, and follow-up-derived information must be excluded from model inputs.
- **Small cohort and class balance:** 2,000 patients is an aspiration, not a guarantee of reliable model performance. Neural networks may be unjustified if eligible event counts are low.
- **Unequal visit histories:** padding and masking choices affect inputs; select and test a policy only after obtaining genuine visit distributions.
- **Environment compatibility:** framework and GPU support change. Pin compatible versions after confirming runtime and hardware; Python 3.12 is a reasonable current intersection.
- **Privacy and hosting:** free hosting is not a default for sensitive patient data. Use local approved access-controlled systems unless governance permits otherwise.
- **Application scope:** the PRD makes a reproducible pipeline the minimum credible MVP and treats the web app as secondary. Prioritize data and target validity.

## Final selection for approval

**Python 3.12 + Pandas/NumPy + scikit-learn + TensorFlow/Keras + Matplotlib/Seaborn + FastAPI + Jinja/Bootstrap + SQLite locally.** Keep React, PostgreSQL, and hosted inference as later choices driven by actual interface and deployment needs.

No project files or dependencies were changed or installed for this assessment. The recommendation does not change the current NO-GO for supervised baselines or Hybrid RNN-LSTM training with the acquired public interim cohorts.

## Official references

- Python 3.12 documentation: <https://docs.python.org/3.12/>
- PyTorch install compatibility: <https://pytorch.org/get-started/locally/>
- TensorFlow pip installation: <https://www.tensorflow.org/install/pip>
- Pandas overview: <https://pandas.pydata.org/docs/getting_started/overview.html>
- scikit-learn leakage guidance: <https://scikit-learn.org/stable/common_pitfalls>
- Keras recurrent layers: <https://keras.io/api/layers/recurrent_layers/>
- Keras SimpleRNN API: <https://keras.io/2/api/layers/recurrent_layers/simple_rnn/>
- FastAPI features and OpenAPI docs: <https://fastapi.tiangolo.com/features/>
- Flask documentation: <https://flask.palletsprojects.com/en/stable/>
- Django installation and framework docs: <https://docs.djangoproject.com/en/dev/topics/install/>
- pytest documentation: <https://docs.pytest.org/en/stable/>
- Streamlit Community Cloud: <https://docs.streamlit.io/deploy/streamlit-community-cloud>
- Render free-service limitations: <https://render.com/docs/free>
- Vercel Hobby plan: <https://vercel.com/docs/plans/hobby>
- Railway pricing: <https://docs.railway.com/pricing/plans>
- Hugging Face Spaces overview: <https://huggingface.co/docs/hub/spaces-overview>
