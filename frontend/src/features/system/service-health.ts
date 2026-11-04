import { apiUrl } from "@/lib/api-client";

export interface ServiceHealth {
  api: "available";
  readiness: "ready" | "not_ready";
  checks: {
    database: string;
    authentication: string;
    model: string;
  };
}

async function getJson(path: string, signal: AbortSignal): Promise<unknown> {
  let response: Response;
  try {
    response = await fetch(apiUrl(path), { method: "GET", signal });
  } catch {
    throw new Error("API health check is unavailable.");
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

export async function getServiceHealth(signal: AbortSignal): Promise<ServiceHealth> {
  const [live, ready] = await Promise.all([
    getJson("health/live", signal),
    getJson("health/ready", signal),
  ]);

  if (!isRecord(live) || live.status !== "ok") {
    throw new Error("API health check returned an invalid response.");
  }

  if (
    !isRecord(ready) ||
    (ready.status !== "ready" && ready.status !== "not_ready") ||
    !isRecord(ready.checks) ||
    typeof ready.checks.database !== "string" ||
    typeof ready.checks.authentication !== "string" ||
    typeof ready.checks.model !== "string"
  ) {
    throw new Error("API health check returned an invalid response.");
  }

  return {
    api: "available",
    readiness: ready.status,
    checks: {
      database: ready.checks.database,
      authentication: ready.checks.authentication,
      model: ready.checks.model,
    },
  };
}

export function describeCheck(value: string): string {
  const knownStatuses: Record<string, string> = {
    connected: "Connected",
    not_configured: "Not configured",
    not_available: "Not available",
  };

  return Object.hasOwn(knownStatuses, value) ? (knownStatuses[value] ?? "Unknown") : "Unknown";
}
