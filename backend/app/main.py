"""Non-sensitive service health endpoints for the research application."""

from typing import Literal

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="NeuroPredict MS Research API",
    version="0.1.0",
    description=(
        "Research and educational API foundation. No patient-data, authentication, or model "
        "endpoints are enabled in this scaffold."
    ),
)


class LivenessResponse(BaseModel):
    status: Literal["ok"]


class ReadinessChecks(BaseModel):
    database: Literal["connected", "not_configured", "not_available"]
    authentication: Literal["connected", "not_configured", "not_available"]
    model: Literal["connected", "not_configured", "not_available"]


class ReadinessResponse(BaseModel):
    status: Literal["ready", "not_ready"]
    checks: ReadinessChecks


@app.get("/api/v1/health/live", response_model=LivenessResponse, tags=["health"])
def liveness() -> LivenessResponse:
    """Report that the API process can serve requests."""
    return LivenessResponse(status="ok")


@app.get("/api/v1/health/ready", response_model=ReadinessResponse, tags=["health"])
def readiness() -> ReadinessResponse:
    """Report unavailable integrations without implying product readiness."""
    return ReadinessResponse(
        status="not_ready",
        checks=ReadinessChecks(
            database="not_configured",
            authentication="not_configured",
            model="not_available",
        ),
    )
