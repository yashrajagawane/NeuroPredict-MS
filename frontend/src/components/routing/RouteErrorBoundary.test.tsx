import { fireEvent, render, screen } from "@testing-library/react";
import { MemoryRouter } from "react-router-dom";
import { afterEach, beforeEach, describe, expect, it, vi } from "vitest";

import { RouteErrorBoundary } from "./RouteErrorBoundary";

let shouldThrow = true;

function UnstableScreen() {
  if (shouldThrow) throw new Error("sensitive patient detail");
  return <p>Screen recovered</p>;
}

describe("route error boundary", () => {
  beforeEach(() => {
    shouldThrow = true;
    vi.spyOn(console, "error").mockImplementation(() => undefined);
  });

  afterEach(() => vi.restoreAllMocks());

  it("shows a generic fallback, hides error details, and recovers on retry", () => {
    render(
      <MemoryRouter>
        <RouteErrorBoundary>
          <UnstableScreen />
        </RouteErrorBoundary>
      </MemoryRouter>,
    );

    const heading = screen.getByRole("heading", { name: "We couldn’t load this screen" });
    expect(heading).toHaveFocus();
    expect(screen.queryByText("sensitive patient detail")).not.toBeInTheDocument();

    shouldThrow = false;
    fireEvent.click(screen.getByRole("button", { name: "Try again" }));

    expect(screen.getByText("Screen recovered")).toBeInTheDocument();
  });
});
