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

  it("shows a generic API failure state without surfacing server details", async () => {
    vi.stubGlobal("fetch", vi.fn(() => Promise.reject(new Error("patient data leaked"))));
    renderAt();

    await waitFor(() => {
      expect(screen.getByText(/API status is unavailable/)).toBeVisible();
    });
    expect(screen.queryByText(/patient data leaked/)).not.toBeInTheDocument();
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
