import { describe, expect, it } from "vitest";

import { apiUrl, type ApiConfiguration } from "./api-client";

describe("API URL configuration", () => {
  const configuration: ApiConfiguration = { baseUrl: "http://127.0.0.1:8000/api/v1/" };

  it("joins a relative route without duplicating slashes", () => {
    expect(apiUrl("health/live", configuration)).toBe(
      "http://127.0.0.1:8000/api/v1/health/live",
    );
  });

  it("normalizes a leading slash on the supplied route", () => {
    expect(apiUrl("/health/ready", configuration)).toBe(
      "http://127.0.0.1:8000/api/v1/health/ready",
    );
  });
});
