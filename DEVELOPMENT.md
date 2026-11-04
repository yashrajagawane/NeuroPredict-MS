# Development environment

This repository follows the approved project stack. The research pipeline and
application are separate workstreams; this setup installs only shared
developer tools and does not install or train the ML stack.

## Runtime and package managers

- Python **3.12** for backend and data/ML work (`.python-version` selects the
  supported 3.12 minor line; use the latest patch available for the platform). Create
  isolated environments with the standard-library `venv` module and install
  Python packages with `pip`.
- Node.js **24.22.2 LTS** for the future React/Vite frontend (`.nvmrc`); use
  the npm version bundled with that Node release. Commit `package-lock.json`
  when the frontend is introduced.
- Python developer dependencies are declared in `requirements-dev.in` and
  resolved/pinned in `requirements-dev.lock`. The checked-in lock is for
  developer tooling only. Runtime/API/ML dependencies must be added and locked
  in the phase that implements those components, after Python 3.12 compatibility
  and cross-platform resolution are checked.

## Local setup

Install a supported Python 3.12 runtime, then from the repository root run:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements-dev.lock
python -m unittest discover -s .\data\tests -v
python -m pytest
python -m ruff check .\data\scripts .\data\tests
python -m ruff format --check .\data\scripts .\data\tests
```

On macOS or Linux, use `python3.12 -m venv .venv` and activate
`.venv/bin/activate`. Do not install dependencies globally. Raw and processed
patient-level data remain excluded by `.gitignore`.

## Configuration and secrets

`.env.example` documents variable names only and contains no credentials.
Copy it to a local `.env` when application configuration is implemented;
`.env` is ignored by Git. Keep the Supabase service-role key on the backend
only. Never put it in a `VITE_` variable, browser bundle, commit, log, or test
fixture. CI uses no patient data or application secrets.

## Code quality and logs

Ruff checks Python formatting and the configured `E4`, `E7`, `E9`, `F`, and `I` lint
rules. Run tests with both the existing `unittest` command and pytest. Use the
standard-library `logging` module for application and pipeline diagnostics;
do not log patient values, identifiers, credentials, or row contents. CI is
read-only and runs on pushes and pull requests to `main`.

Tests that inspect the original workbooks run when those local-only files are
present and skip with an explicit reason when they are absent from CI. The
workbooks are intentionally excluded from Git; CI does not download or upload
patient-level source data.

## Current limitations

This repository still has no approved longitudinal cohort. The developer
environment does not make either interim cohort eligible for supervised
future-conversion prediction, and no model training is configured here.
