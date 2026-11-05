import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { act, fireEvent, render, screen, waitFor } from "@testing-library/react";
import { MemoryRouter } from "react-router-dom";
import { beforeEach, describe, expect, it, vi } from "vitest";

import { AppRoutes } from "./App";

function renderAt(path = "/") {
  const queryClient = new QueryClient({ defaultOptions: { queries: { retry: false } } });
  return render(
    <QueryClientProvider client={queryClient}>
      <MemoryRouter initialEntries={[path]}>
        <AppRoutes />
      </MemoryRouter>
    </QueryClientProvider>,
  );
}

beforeEach(() => {
  vi.stubGlobal(
    "matchMedia",
    vi.fn((media: string) => ({
      matches: false,
      media,
      addEventListener: vi.fn(),
      removeEventListener: vi.fn(),
    })),
  );
  vi.stubGlobal(
    "fetch",
    vi.fn((input: RequestInfo | URL) => {
      const body = String(input).endsWith("health/live")
        ? { status: "ok" }
        : {
            status: "not_ready",
            checks: {
              database: "not_configured",
              authentication: "not_configured",
              model: "not_available",
            },
          };
      return Promise.resolve({ ok: true, json: () => Promise.resolve(body) } as Response);
    }),
  );
});

describe("research application shell", () => {
  it("shows the research-only disclaimer and accurately reports unavailable services", () => {
    renderAt();

    expect(
      screen.getByText(
        "Research and education only — not a medical diagnosis. Do not use this prototype to make treatment decisions.",
      ),
    ).toBeInTheDocument();
    expect(screen.getByText(/No patient records, authentication provider/)).toBeInTheDocument();
    expect(screen.getAllByText("Research prediction").length).toBeGreaterThan(0);
  });

  it("reports API availability separately from database, auth, and model readiness", async () => {
    renderAt();

    await waitFor(() => {
      expect(screen.getByText(/API process available; application readiness is not ready/)).toBeVisible();
    });
    expect(screen.getByText("Database").parentElement!).toHaveTextContent("Not configured");
    expect(screen.getByText("Authentication").parentElement!).toHaveTextContent("Not configured");
    expect(screen.getByText("Model").parentElement!).toHaveTextContent("Not available");
  });

  it("shows a generic API failure state and supports a safe health-check retry", async () => {
    vi.stubGlobal("fetch", vi.fn(() => Promise.reject(new Error("patient data leaked"))));
    renderAt();

    await waitFor(() => {
      expect(screen.getByText(/API status is unavailable/)).toBeVisible();
    });
    expect(screen.queryByText(/patient data leaked/)).not.toBeInTheDocument();

    vi.stubGlobal(
      "fetch",
      vi.fn((input: RequestInfo | URL) => {
        const body = String(input).endsWith("health/live")
          ? { status: "ok" }
          : {
              status: "not_ready",
              checks: {
                database: "not_configured",
                authentication: "not_configured",
                model: "not_available",
              },
            };
        return Promise.resolve({ ok: true, json: () => Promise.resolve(body) } as Response);
      }),
    );
    fireEvent.click(screen.getByRole("button", { name: "Retry API check" }));

    await waitFor(() =>
      expect(screen.getByText(/API process available; application readiness is not ready/)).toBeVisible(),
    );
  });

  it("announces a pending health check while both endpoints are loading", async () => {
    const pendingResponses: Array<(response: Response) => void> = [];
    vi.stubGlobal(
      "fetch",
      vi.fn(
        () =>
          new Promise<Response>((resolve) => {
            pendingResponses.push(resolve);
          }),
      ),
    );
    renderAt();

    expect(screen.getByRole("status")).toHaveTextContent("Checking API availability");
    await waitFor(() => expect(pendingResponses).toHaveLength(2));
    pendingResponses.forEach((resolve, index) =>
      resolve({
        ok: true,
        json: () =>
          Promise.resolve(
            index === 0
              ? { status: "ok" }
              : {
                  status: "not_ready",
                  checks: {
                    database: "not_configured",
                    authentication: "not_configured",
                    model: "not_available",
                  },
                },
          ),
      } as Response),
    );
    await waitFor(() =>
      expect(screen.getByText(/API process available; application readiness is not ready/)).toBeVisible(),
    );
  });

  it("shows prediction unavailable without a class or probability", () => {
    renderAt("/research-prediction");

    expect(screen.getByRole("heading", { name: "Research prediction is unavailable" })).toBeVisible();
    expect(screen.getByText(/No prediction class, probability/)).toBeVisible();
    expect(screen.queryByText(/Class [01]|\b\d+%\b/)).not.toBeInTheDocument();
  });

  it("does not render patient rows when opening patient management", () => {
    renderAt();
    fireEvent.click(
      screen.getByRole("navigation", { name: "Main navigation" }).querySelector('a[href="/patients"]')!,
    );

    expect(screen.getByRole("heading", { name: "Patient management" })).toBeVisible();
    expect(screen.getByText("No patient records are available")).toBeVisible();
    expect(screen.queryByRole("table")).not.toBeInTheDocument();
  });

  it("keeps registration controls disabled and does not save a patient", () => {
    renderAt("/patients/register");

    expect(screen.getByRole("heading", { name: "Patient registration" })).toBeVisible();
    expect(screen.getByLabelText("Pseudonymous patient ID")).toBeDisabled();
    expect(screen.getByLabelText("CIS index date")).toBeDisabled();
    expect(screen.getByRole("button", { name: "Save patient" })).toBeDisabled();
    expect(screen.getByText("No information has been entered or stored.")).toBeVisible();
  });

  it("shows a visit-history empty state without synthetic timeline entries", () => {
    renderAt("/visits");

    expect(screen.getByRole("heading", { name: "Patient visit history" })).toBeVisible();
    expect(screen.getByLabelText("Patient")).toBeDisabled();
    expect(screen.getByText("No visit timeline is available")).toBeVisible();
    expect(screen.queryByRole("list")).not.toBeInTheDocument();
  });

  it("keeps clinical entry fields disabled pending an approved feature dictionary", () => {
    renderAt("/clinical-data");

    expect(screen.getByRole("heading", { name: "Clinical data entry" })).toBeVisible();
    expect(screen.getByLabelText("Measurement")).toBeDisabled();
    expect(screen.getByLabelText("Value")).toBeDisabled();
    expect(screen.getByLabelText("Observed at")).toBeDisabled();
    expect(screen.getByText(/Do not enter patient information/)).toBeVisible();
  });

  it("shows prediction history as empty without fabricated results", () => {
    renderAt("/prediction-history");

    expect(screen.getByRole("heading", { name: "Prediction history" })).toBeVisible();
    expect(screen.getByText("No prediction history is available")).toBeVisible();
    expect(screen.queryByRole("table")).not.toBeInTheDocument();
    expect(screen.queryByText(/Class [01]|\b\d+%\b/)).not.toBeInTheDocument();
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

  it("traps keyboard focus in the mobile drawer and restores it when closed", async () => {
    renderAt();
    const trigger = screen.getByRole("button", { name: "Open navigation menu" });
    fireEvent.click(trigger);

    const dialog = screen.getByRole("dialog", { name: "Mobile navigation" });
    const firstLink = dialog.querySelector('a[href="/"]');
    const focusable = dialog.querySelectorAll<HTMLElement>('a[href], button:not([disabled])');
    const lastFocusable = focusable[focusable.length - 1];
    await waitFor(() => expect(firstLink).toHaveFocus());

    fireEvent.keyDown(dialog, { key: "Tab", shiftKey: true });
    expect(lastFocusable).toHaveFocus();

    fireEvent.keyDown(dialog, { key: "Escape" });
    expect(trigger).toHaveAttribute("aria-expanded", "false");
    expect(trigger).toHaveFocus();
  });

  it("closes the mobile drawer when the viewport enters the desktop layout", () => {
    let onBreakpointChange: ((event: MediaQueryListEvent) => void) | undefined;
    vi.stubGlobal(
      "matchMedia",
      vi.fn(() => ({
        matches: false,
        media: "(min-width: 1024px)",
        addEventListener: (_type: string, listener: (event: MediaQueryListEvent) => void) => {
          onBreakpointChange = listener;
        },
        removeEventListener: vi.fn(),
      })),
    );
    renderAt();

    const trigger = screen.getByRole("button", { name: "Open navigation menu" });
    fireEvent.click(trigger);
    act(() => onBreakpointChange?.({ matches: true } as MediaQueryListEvent));

    expect(trigger).toHaveAttribute("aria-expanded", "false");
  });
});
