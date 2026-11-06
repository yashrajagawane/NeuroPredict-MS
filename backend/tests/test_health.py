import httpx
import pytest
from backend.app.main import app


@pytest.fixture
def anyio_backend() -> str:
    return "asyncio"


@pytest.mark.anyio
async def test_liveness_reports_only_process_status() -> None:
    async with httpx.AsyncClient(
        transport=httpx.ASGITransport(app=app), base_url="http://test"
    ) as client:
        response = await client.get("/api/v1/health/live")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


@pytest.mark.anyio
async def test_readiness_does_not_claim_unavailable_integrations() -> None:
    async with httpx.AsyncClient(
        transport=httpx.ASGITransport(app=app), base_url="http://test"
    ) as client:
        response = await client.get("/api/v1/health/ready")

    assert response.status_code == 200
    assert response.json() == {
        "status": "not_ready",
        "checks": {
            "database": "not_configured",
            "authentication": "not_configured",
            "model": "not_available",
        },
    }


def test_patient_and_prediction_endpoints_are_not_exposed() -> None:
    paths = set(app.openapi()["paths"])

    assert paths == {"/api/v1/health/live", "/api/v1/health/ready"}


def test_openapi_documents_literal_health_contracts() -> None:
    schemas = app.openapi()["components"]["schemas"]

    liveness_status = schemas["LivenessResponse"]["properties"]["status"]
    liveness_values = (
        [liveness_status["const"]] if "const" in liveness_status else liveness_status["enum"]
    )
    assert liveness_values == ["ok"]
    assert schemas["ReadinessResponse"]["properties"]["status"]["enum"] == [
        "ready",
        "not_ready",
    ]
    expected_check_statuses = ["connected", "not_configured", "not_available"]
    for name in ("database", "authentication", "model"):
        assert schemas["ReadinessChecks"]["properties"][name]["enum"] == expected_check_statuses
