# Backend foundation

This folder currently contains a minimal FastAPI process-health scaffold only.

- `GET /api/v1/health/live` reports that this process can answer requests.
- `GET /api/v1/health/ready` explicitly reports that database, authentication, and model integrations are unavailable.
- There are no patient, visit, clinical-data, authentication, prediction, or history endpoints.
- OpenAPI documentation describes only these health routes; it is not evidence that clinical workflows are ready.

Install both pinned runtime and development/test dependencies in the Python 3.12 environment:

```powershell
python -m pip install -r requirements-api.lock -r requirements-dev.lock
```

Run locally from the repository root:

```powershell
python -m uvicorn backend.app.main:app --reload
```

Run the API tests with the API and development requirements installed:

```powershell
python -m pytest backend/tests
```

Do not connect this scaffold to real patient data. Database, authorization, data governance, clinical workflows, and validated model gates remain prerequisites for their respective endpoints.
