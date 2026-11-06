import { apiUrl } from "@/lib/api-client";

export interface ServiceHealth {
  api: "available";
  readiness: "ready" | "not_ready";
  checks: {
    database: DependencyStatus;
    authentication: DependencyStatus;
    model: DependencyStatus;
  };
}

export type DependencyStatus = "connected" | "not_configured" | "not_available" | "unknown";

export interface ApiLivenessResponse {
  status: "ok";
}

export interface ApiReadinessResponse {
  status: "ready" | "not_ready";
  checks: {
    database: string;
    authentication: string;
    model: string;
  };
}

const dependencyStatuses = new Set<DependencyStatus>([
  "connected",
  "not_configured",
  "not_available",
  "unknown",
]);

function normalizeDependencyStatus(value: string): DependencyStatus {
  return dependencyStatuses.has(value as DependencyStatus) ? (value as DependencyStatus) : "unknown";
}

async function getJson(path: string, signal: AbortSignal): Promise<unknown> {
  let response: Response;
  try {
    response = await fetch(apiUrl(path), { method: "GET", signal });
  } catch (error) {
    if (signal.aborted) throw error;
    throw new Error("API health check is unavailable.", { cause: error });
  }

  if (!response.ok) {
    throw new Error("API health check is unavailable.");
  }

  try {
    return await response.json();
  } catch {
    throw new Error("API health check returned an invalid response.");
  }
}

function isRecord(value: unknown): value is Record<string, unknown> {
  return typeof value === "object" && value !== null;
}

function isApiLivenessResponse(value: unknown): value is ApiLivenessResponse {
  return isRecord(value) && value.status === "ok";
}

function isApiReadinessResponse(value: unknown): value is ApiReadinessResponse {
  return (
    isRecord(value) &&
    (value.status === "ready" || value.status === "not_ready") &&
    isRecord(value.checks) &&
    typeof value.checks.database === "string" &&
    typeof value.checks.authentication === "string" &&
    typeof value.checks.model === "string"
  );
}

export async function getServiceHealth(signal: AbortSignal): Promise<ServiceHealth> {
  const [live, ready] = await Promise.all([
    getJson("health/live", signal),
    getJson("health/ready", signal),
  ]);

  if (!isApiLivenessResponse(live)) {
    throw new Error("API health check returned an invalid response.");
  }

  if (!isApiReadinessResponse(ready)) {
    throw new Error("API health check returned an invalid response.");
  }

  return {
    api: "available",
    readiness: ready.status,
    checks: {
      database: normalizeDependencyStatus(ready.checks.database),
      authentication: normalizeDependencyStatus(ready.checks.authentication),
      model: normalizeDependencyStatus(ready.checks.model),
    },
  };
}

export function describeCheck(value: string): string {
  const knownStatuses: Record<string, string> = {
    connected: "Connected",
    not_configured: "Not configured",
    not_available: "Not available",
    unknown: "Unknown",
  };

  return Object.hasOwn(knownStatuses, value) ? (knownStatuses[value] ?? "Unknown") : "Unknown";
}
