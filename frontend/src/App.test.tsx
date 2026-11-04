import { fireEvent, render, screen } from "@testing-library/react";
import { MemoryRouter } from "react-router-dom";
import { describe, expect, it } from "vitest";

import { AppRoutes } from "./App";

function renderAt(path = "/") {
  return render(
    <MemoryRouter initialEntries={[path]}>
      <AppRoutes />
    </MemoryRouter>,
  );
}

describe("research application shell", () => {
  it("shows the research-only disclaimer and accurately reports unavailable services", () => {
    renderAt();

    expect(
      screen.getByText(
        "Research prediction only — not a medical diagnosis. Do not use this result to make treatment decisions.",
      ),
    ).toBeInTheDocument();
    expect(screen.getByText(/No patient records, authentication provider/)).toBeInTheDocument();
    expect(screen.getAllByText("Research prediction").length).toBeGreaterThan(0);
  });

  it("shows prediction unavailable without a class or probability", () => {
    renderAt("/research-prediction");

    expect(screen.getByRole("heading", { name: "Research prediction is unavailable" })).toBeVisible();
    expect(screen.getByText(/does not provide a class or probability/)).toBeVisible();
    expect(screen.queryByText(/Class [01]|\b\d+%\b/)).not.toBeInTheDocument();
  });

  it("does not render patient rows when opening patient management", () => {
    renderAt();
    fireEvent.click(
      screen.getByRole("navigation", { name: "Main navigation" }).querySelector('a[href="/patients"]')!,
    );

    expect(screen.getByRole("heading", { name: "Patient management is not connected" })).toBeVisible();
    expect(screen.getByText(/No patient records or prediction results are loaded/)).toBeVisible();
    expect(screen.queryByRole("table")).not.toBeInTheDocument();
  });

  it("keeps sign-in disabled until the authentication policy exists", () => {
    renderAt("/login");

    expect(screen.getByRole("heading", { name: "Sign-in is not configured" })).toBeVisible();
    expect(screen.getByText(/No login form or session is active/)).toBeVisible();
  });

  it("exposes the mobile navigation state to assistive technology", () => {
    renderAt();
    const openButton = screen.getByRole("button", { name: "Open navigation menu" });

    expect(openButton).toHaveAttribute("aria-expanded", "false");
    fireEvent.click(openButton);

    expect(screen.getByRole("button", { name: "Close navigation menu" })).toHaveAttribute(
      "aria-expanded",
      "true",
    );
    expect(document.getElementById("application-sidebar")).toHaveClass("flex");
  });
});
