import { describe, expect, it } from "vitest";

import { initialAuthState } from "./auth-state";

describe("authentication placeholder", () => {
  it("fails closed while no approved provider is configured", () => {
    expect(initialAuthState).toEqual({ status: "not_configured" });
  });
});
