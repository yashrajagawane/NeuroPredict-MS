import {
  Activity,
  ArrowRight,
  Database,
  FileClock,
  FlaskConical,
  HeartPulse,
  LayoutDashboard,
  LockKeyhole,
  Menu,
  Stethoscope,
  UsersRound,
} from "lucide-react";
import { useEffect, useRef, useState, type KeyboardEvent } from "react";
import { Link, NavLink, Outlet, Route, Routes, useLocation } from "react-router-dom";

import { Card } from "@/components/ui/card";
import { RouteErrorBoundary } from "@/components/routing/RouteErrorBoundary";
import { ModuleCard } from "@/features/dashboard/ModuleCard";
import { ServiceStatusCard } from "@/features/system/ServiceStatusCard";
import {
  ClinicalDataEntryPage,
  PatientManagementPage,
  PatientRegistrationPage,
  PatientVisitHistoryPage,
  PredictionHistoryPage,
  ResearchPredictionPage,
} from "@/features/workspace/StaticWorkflowPages";

const navigation = [
  { label: "Overview", to: "/", icon: LayoutDashboard, end: true },
  { label: "Patients", to: "/patients", icon: UsersRound },
  { label: "Visit history", to: "/visits", icon: Activity },
  { label: "Clinical data", to: "/clinical-data", icon: Database },
  { label: "Research prediction", to: "/research-prediction", icon: FlaskConical },
  { label: "Prediction history", to: "/prediction-history", icon: FileClock },
];

function AppShell() {
  const [menuOpen, setMenuOpen] = useState(false);
  const sidebarRef = useRef<HTMLElement>(null);
  const menuButtonRef = useRef<HTMLButtonElement>(null);
  const location = useLocation();
  const previousPathnameRef = useRef(location.pathname);

  useEffect(() => {
    if (previousPathnameRef.current === location.pathname) return;
    previousPathnameRef.current = location.pathname;
    document.querySelector<HTMLElement>("#main-content h1")?.focus();
  }, [location.pathname]);

  useEffect(() => {
    if (!menuOpen) return;
    sidebarRef.current?.querySelector<HTMLElement>('a[href], button:not([disabled])')?.focus();
  }, [menuOpen]);

  useEffect(() => {
    if (!menuOpen) return;
    const desktopBreakpoint = window.matchMedia("(min-width: 1024px)");
    const closeOnDesktop = (event: MediaQueryListEvent) => {
      if (event.matches) setMenuOpen(false);
    };
    desktopBreakpoint.addEventListener("change", closeOnDesktop);
    return () => desktopBreakpoint.removeEventListener("change", closeOnDesktop);
  }, [menuOpen]);

  function closeNavigation() {
    setMenuOpen(false);
    if (menuOpen) menuButtonRef.current?.focus();
  }

  function handleDrawerKeyDown(event: KeyboardEvent<HTMLElement>) {
    if (!menuOpen) return;
    if (event.key === "Escape") {
      event.preventDefault();
      closeNavigation();
      return;
    }
    if (event.key !== "Tab") return;

    const focusable = sidebarRef.current?.querySelectorAll<HTMLElement>(
      'a[href], button:not([disabled])',
    );
    if (!focusable?.length) return;

    const first = focusable[0];
    const last = focusable[focusable.length - 1];
    if (!first || !last) return;
    if (event.shiftKey && document.activeElement === first) {
      event.preventDefault();
      last.focus();
    } else if (!event.shiftKey && document.activeElement === last) {
      event.preventDefault();
      first.focus();
    }
  }

  return (
    <div className="min-h-screen bg-background text-foreground">
      <a
        className="sr-only z-30 rounded-md bg-white px-4 py-2 font-semibold text-primary focus:not-sr-only focus:fixed focus:left-4 focus:top-4"
        href="#main-content"
      >
        Skip to main content
      </a>
      <aside
        ref={sidebarRef}
        id="application-sidebar"
        role={menuOpen ? "dialog" : undefined}
        aria-label={menuOpen ? "Mobile navigation" : undefined}
        aria-modal={menuOpen || undefined}
        onKeyDown={handleDrawerKeyDown}
        className={`fixed inset-y-0 left-0 z-20 w-72 flex-col border-r border-border bg-white px-5 py-6 lg:flex ${menuOpen ? "flex" : "hidden"}`}
      >
        <Link
          className="flex items-center gap-3 rounded-lg"
          to="/"
          onClick={closeNavigation}
        >
          <span className="flex size-11 items-center justify-center rounded-xl bg-primary-quiet text-primary">
            <HeartPulse aria-hidden="true" size={23} />
          </span>
          <span>
            <span className="block text-sm font-bold tracking-tight">NeuroPredict MS</span>
            <span className="block text-xs text-muted-foreground">Research workspace</span>
          </span>
        </Link>

        <p className="mb-2 mt-9 px-3 text-[11px] font-bold uppercase tracking-[0.14em] text-muted-foreground">
          Workspace
        </p>
        <nav aria-label="Main navigation" className="space-y-1">
          {navigation.map(({ label, to, icon: Icon, end }) => (
            <NavLink
              key={to}
              to={to}
              end={end}
              onClick={closeNavigation}
              className={({ isActive }) =>
                `flex min-h-11 items-center gap-3 rounded-lg px-3 text-sm font-medium transition-colors ${isActive ? "bg-primary-quiet text-primary" : "text-slate-600 hover:bg-slate-50 hover:text-foreground"}`
              }
            >
              <Icon aria-hidden="true" size={18} strokeWidth={1.8} />
              {label}
            </NavLink>
          ))}
        </nav>

        <div className="mt-auto rounded-xl border border-border bg-slate-50 p-4">
          <div className="mb-2 flex items-center gap-2 text-sm font-semibold">
            <LockKeyhole aria-hidden="true" className="text-primary" size={16} />
            Research access
          </div>
          <p className="text-xs leading-5 text-muted-foreground">
            Sign-in and patient access are not configured in this prototype.
          </p>
          <Link
            className="mt-3 inline-flex min-h-9 items-center gap-1 text-xs font-semibold text-primary hover:underline"
            to="/login"
          >
            View sign-in status <ArrowRight aria-hidden="true" size={14} />
          </Link>
        </div>
      </aside>

      {menuOpen && (
        <button
          aria-label="Close navigation drawer"
          className="fixed inset-0 z-10 bg-slate-950/30 lg:hidden"
          onClick={closeNavigation}
        />
      )}

      <div className="min-h-screen lg:pl-72">
        <header className="sticky top-0 z-10 border-b border-border bg-white/95 px-5 py-3 backdrop-blur md:px-9">
          <div className="mx-auto flex max-w-7xl items-center justify-between gap-4">
            <button
              ref={menuButtonRef}
              aria-controls="application-sidebar"
              aria-expanded={menuOpen}
              aria-label={menuOpen ? "Close navigation menu" : "Open navigation menu"}
              className="flex size-10 items-center justify-center rounded-lg text-slate-600 hover:bg-slate-100 lg:hidden"
              onClick={menuOpen ? closeNavigation : () => setMenuOpen(true)}
            >
              <Menu aria-hidden="true" size={20} />
            </button>
            <div className="hidden items-center gap-2 text-xs text-muted-foreground sm:flex">
              <Stethoscope aria-hidden="true" size={15} />
              Educational research prototype
            </div>
            <Link
              className="ml-auto rounded-md text-sm font-semibold text-primary hover:underline"
              to="/login"
            >
              Sign-in status
            </Link>
          </div>
        </header>

        <div className="border-b border-teal-100 bg-primary-quiet px-5 py-2.5 text-center text-xs leading-5 text-teal-950 md:px-9">
          Research and education only — not a medical diagnosis. Do not use this prototype to make
          treatment decisions.
        </div>

        <main id="main-content" className="mx-auto max-w-7xl px-5 py-8 md:px-9 md:py-10">
          <Outlet />
        </main>

        <footer className="border-t border-border px-5 py-5 text-center text-xs text-muted-foreground md:px-9">
          For research and education only. No clinical records or validated prediction model are
          connected.
        </footer>
      </div>
    </div>
  );
}

function OverviewPage() {
  return (
    <div className="space-y-8">
      <section aria-labelledby="page-title" className="max-w-3xl">
        <p className="mb-3 flex items-center gap-2 text-sm font-semibold text-primary">
          <span className="size-2 rounded-full bg-amber-500" /> Project setup in progress
        </p>
        <h1 id="page-title" tabIndex={-1} className="text-3xl font-bold tracking-tight sm:text-4xl">
          Longitudinal CIS-to-MS research workspace
        </h1>
        <p className="mt-4 max-w-2xl text-base leading-7 text-muted-foreground">
          A research prototype for studying future conversion from Clinically Isolated Syndrome to
          Multiple Sclerosis using genuine longitudinal observations when an approved cohort is
          available.
        </p>
      </section>

      <ServiceStatusCard />

      <Card className="flex gap-4 border-amber-200 bg-amber-50 p-5 sm:p-6">
        <span className="flex size-10 shrink-0 items-center justify-center rounded-xl bg-white text-amber-700">
          <LockKeyhole aria-hidden="true" size={19} />
        </span>
        <div>
          <h2 className="font-semibold text-amber-950">Clinical workflows are not connected</h2>
          <p className="mt-1 text-sm leading-6 text-amber-950/80">
            No patient records, authentication provider, clinical database, or validated model is
            connected to this frontend. Patient management and prediction are unavailable.
          </p>
        </div>
      </Card>

      <section aria-labelledby="modules-heading">
        <div className="mb-4 flex items-end justify-between gap-4">
          <div>
            <h2 id="modules-heading" className="text-lg font-bold">
              Research workspace modules
            </h2>
            <p className="mt-1 text-sm text-muted-foreground">
              Navigation is present; modules remain disabled until their backend and approval gates
              are met.
            </p>
          </div>
        </div>
        <div className="grid gap-4 sm:grid-cols-2 xl:grid-cols-3">
          {navigation.slice(1).map(({ label, to, icon: Icon }) => (
            <ModuleCard
              key={to}
              title={label}
              description="This module will remain unavailable until its approved services are implemented."
              to={to}
              icon={Icon}
            />
          ))}
        </div>
      </section>
    </div>
  );
}

function UnavailablePage({ title, reason }: { title: string; reason: string }) {
  return (
    <section aria-labelledby="page-title" className="mx-auto max-w-2xl py-8 sm:py-14">
      <Card className="p-6 sm:p-9">
        <span className="mb-5 flex size-12 items-center justify-center rounded-xl bg-slate-100 text-slate-700">
          <LockKeyhole aria-hidden="true" size={21} />
        </span>
        <p className="text-xs font-bold uppercase tracking-wider text-muted-foreground">
          Not available in this build
        </p>
        <h1 id="page-title" tabIndex={-1} className="mt-2 text-2xl font-bold tracking-tight">
          {title}
        </h1>
        <p className="mt-3 leading-7 text-muted-foreground">{reason}</p>
        <p className="mt-4 rounded-lg bg-slate-50 p-4 text-sm leading-6 text-slate-700">
          No patient records or prediction results are loaded or generated by this screen.
        </p>
        <Link
          className="mt-6 inline-flex min-h-10 items-center gap-2 rounded-lg text-sm font-semibold text-primary hover:underline"
          to="/"
        >
          Back to overview <ArrowRight aria-hidden="true" size={16} />
        </Link>
      </Card>
    </section>
  );
}

export function AppRoutes() {
  return (
    <Routes>
      <Route element={<AppShell />}>
        <Route index element={<RouteErrorBoundary><OverviewPage /></RouteErrorBoundary>} />
        <Route
          path="login"
          element={
            <RouteErrorBoundary>
              <UnavailablePage
                title="Sign-in is not configured"
                reason="Account provisioning and the authentication policy are still under design. No login form or session is active."
              />
            </RouteErrorBoundary>
          }
        />
        <Route
          path="patients/register"
          element={
            <RouteErrorBoundary>
              <PatientRegistrationPage />
            </RouteErrorBoundary>
          }
        />
        <Route
          path="patients/*"
          element={<RouteErrorBoundary><PatientManagementPage /></RouteErrorBoundary>}
        />
        <Route
          path="visits/*"
          element={<RouteErrorBoundary><PatientVisitHistoryPage /></RouteErrorBoundary>}
        />
        <Route
          path="clinical-data/*"
          element={<RouteErrorBoundary><ClinicalDataEntryPage /></RouteErrorBoundary>}
        />
        <Route
          path="research-prediction/*"
          element={<RouteErrorBoundary><ResearchPredictionPage /></RouteErrorBoundary>}
        />
        <Route
          path="prediction-history/*"
          element={<RouteErrorBoundary><PredictionHistoryPage /></RouteErrorBoundary>}
        />
        <Route
          path="*"
          element={
            <RouteErrorBoundary>
              <UnavailablePage title="Page not found" reason="The requested page is not part of this prototype." />
            </RouteErrorBoundary>
          }
        />
      </Route>
    </Routes>
  );
}

export default function App() {
  return <AppRoutes />;
}
