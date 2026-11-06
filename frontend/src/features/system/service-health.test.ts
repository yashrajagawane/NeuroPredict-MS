import { afterEach, describe, expect, it, vi } from "vitest";

import { describeCheck, getServiceHealth } from "./service-health";

const liveResponse = { status: "ok" };
const readinessResponse = {
  status: "not_ready",
  checks: {
    database: "not_configured",
    authentication: "not_configured",
    model: "not_available",
  },
};

function stubHealthResponses() {
  vi.stubGlobal(
    "fetch",
    vi.fn((input: RequestInfo | URL) => {
      const body = String(input).endsWith("health/live") ? liveResponse : readinessResponse;
      return Promise.resolve({
        ok: true,
        json: () => Promise.resolve(body),
      } as Response);
    }),
  );
}

afterEach(() => vi.unstubAllGlobals());

describe("read-only API health contract", () => {
  it("reports process availability separately from unavailable integrations", async () => {
    stubHealthResponses();

    await expect(getServiceHealth(new AbortController().signal)).resolves.toEqual({
      api: "available",
      readiness: "not_ready",
      checks: readinessResponse.checks,
    });
  });

  it("does not expose server details when the endpoint fails", async () => {
    vi.stubGlobal(
      "fetch",
      vi.fn(() => Promise.resolve({ ok: false, status: 500, json: () => Promise.resolve({ detail: "internal SQL error" }) })),
    );

    await expect(getServiceHealth(new AbortController().signal)).rejects.toThrow(
      "API health check is unavailable.",
    );
  });

  it("preserves abort cancellation instead of converting it to an API outage", async () => {
    const controller = new AbortController();
    const abortError = new DOMException("The request was aborted", "AbortError");
    controller.abort();
    vi.stubGlobal("fetch", vi.fn(() => Promise.reject(abortError)));

    await expect(getServiceHealth(controller.signal)).rejects.toBe(abortError);
  });

  it("normalizes unknown future dependency values to a safe typed state", async () => {
    vi.stubGlobal(
      "fetch",
      vi.fn((input: RequestInfo | URL) =>
        Promise.resolve({
          ok: true,
          json: () =>
            Promise.resolve(
              String(input).endsWith("health/live")
                ? liveResponse
                : {
                    status: "not_ready",
                    checks: {
                      database: "future-private-status",
                      authentication: "not_configured",
                      model: "not_available",
                    },
                  },
            ),
        } as Response),
      ),
    );

    const health = await getServiceHealth(new AbortController().signal);

    expect(health.checks.database).toBe("unknown");
    expect(describeCheck(health.checks.database)).toBe("Unknown");
  });

  it("uses a fixed safe label for unknown dependency status values", () => {
    expect(describeCheck("unexpected sensitive detail")).toBe("Unknown");
    expect(describeCheck("__proto__")).toBe("Unknown");
    expect(describeCheck("not_configured")).toBe("Not configured");
  });

  it("rejects malformed readiness data instead of rendering arbitrary fields", async () => {
    vi.stubGlobal(
      "fetch",
      vi.fn((input: RequestInfo | URL) =>
        Promise.resolve({
          ok: true,
          json: () => Promise.resolve(String(input).endsWith("health/live") ? liveResponse : { detail: "unexpected" }),
        } as Response),
      ),
    );

    await expect(getServiceHealth(new AbortController().signal)).rejects.toThrow(
      "API health check returned an invalid response.",
    );
  });
});
