import { Activity, Database, FileClock, FlaskConical, UserPlus, UsersRound } from "lucide-react";
import { Link } from "react-router-dom";

import { Card } from "@/components/ui/card";
import { StaticWorkflowPage } from "@/features/workspace/StaticWorkflowPage";

function EmptyState({ title, children }: { title: string; children: string }) {
  return (
    <Card className="border-dashed bg-surface p-6 sm:p-8">
      <h2 className="font-semibold">{title}</h2>
      <p className="mt-2 text-sm leading-6 text-muted-foreground">{children}</p>
    </Card>
  );
}

export function PatientManagementPage() {
  return (
    <StaticWorkflowPage
      title="Patient management"
      description="Patient access is not available until governance, authentication, and an authorized backend are in place."
      icon={UsersRound}
    >
      <Card className="p-5 sm:p-6">
        <div className="flex flex-wrap items-end gap-4">
          <label className="min-w-52 flex-1 text-sm font-medium" htmlFor="patient-search">
            Search patients
            <input
              id="patient-search"
              className="mt-2 min-h-11 w-full rounded-lg border border-border bg-muted px-3 text-sm"
              disabled
              placeholder="Unavailable until an authorized source is connected"
              type="search"
            />
          </label>
          <Link
            className="inline-flex min-h-11 items-center gap-2 rounded-lg border border-border px-4 text-sm font-semibold text-foreground"
            to="/patients/register"
          >
            <UserPlus aria-hidden="true" size={17} />
            Preview registration layout
          </Link>
        </div>
      </Card>
      <EmptyState title="No patient records are available">
        This screen contains no patient rows or search results. Patient records will only appear
        after an approved source, access policy, and backend workflow are established.
      </EmptyState>
    </StaticWorkflowPage>
  );
}

export function PatientRegistrationPage() {
  return (
    <StaticWorkflowPage
      title="Patient registration"
      description="This form is a non-interactive layout preview. It does not collect or save information."
      icon={UserPlus}
    >
      <Card className="p-5 sm:p-6">
        <form aria-describedby="registration-unavailable" onSubmit={(event) => event.preventDefault()}>
          <fieldset disabled className="grid gap-5 sm:grid-cols-2">
            <legend className="mb-4 text-sm font-semibold">Registration fields are unavailable</legend>
            <label className="text-sm font-medium" htmlFor="pseudonymous-id">
              Pseudonymous patient ID
              <input id="pseudonymous-id" className="mt-2 min-h-11 w-full rounded-lg border border-border bg-muted px-3" />
            </label>
            <label className="text-sm font-medium" htmlFor="baseline-date">
              CIS index date
              <input id="baseline-date" className="mt-2 min-h-11 w-full rounded-lg border border-border bg-muted px-3" type="date" />
            </label>
            <p id="registration-unavailable" className="text-sm leading-6 text-muted-foreground sm:col-span-2">
              An approved data dictionary, identity policy, authentication, and persistence service are
              required before fields can be enabled.
            </p>
            <button className="min-h-11 rounded-lg bg-primary px-4 font-semibold text-primary-foreground disabled:opacity-50 sm:col-span-2" type="submit">
              Save patient
            </button>
          </fieldset>
        </form>
      </Card>
      <p className="text-sm text-muted-foreground">No information has been entered or stored.</p>
    </StaticWorkflowPage>
  );
}

export function PatientVisitHistoryPage() {
  return (
    <StaticWorkflowPage
      title="Patient visit history"
      description="A longitudinal timeline requires genuine patient-linked visit dates and approved clinical observations."
      icon={Activity}
    >
      <Card className="p-5 sm:p-6">
        <label className="block text-sm font-medium" htmlFor="visit-patient">
          Patient
          <select id="visit-patient" className="mt-2 min-h-11 w-full rounded-lg border border-border bg-muted px-3 text-sm sm:max-w-md" disabled>
            <option>No patient records available</option>
          </select>
        </label>
      </Card>
      <EmptyState title="No visit timeline is available">
        No visits, dates, or clinical measurements are loaded. The final research dataset must contain
        only genuine observations in their source order.
      </EmptyState>
    </StaticWorkflowPage>
  );
}

export function ClinicalDataEntryPage() {
  return (
    <StaticWorkflowPage
      title="Clinical data entry"
      description="Clinical fields and units have not been approved for this application."
      icon={Database}
    >
      <Card className="p-5 sm:p-6">
        <fieldset disabled className="space-y-5">
          <legend className="text-sm font-semibold">Feature fields pending source review</legend>
          <div className="grid gap-4 sm:grid-cols-3">
            {[
              ["Measurement", "clinical-measurement"],
              ["Value", "clinical-value"],
              ["Observed at", "clinical-time"],
            ].map(([label, id]) => (
              <label key={id} className="text-sm font-medium" htmlFor={id}>
                {label}
                <input id={id} className="mt-2 min-h-11 w-full rounded-lg border border-border bg-muted px-3" />
              </label>
            ))}
          </div>
        </fieldset>
        <p className="mt-5 text-sm leading-6 text-muted-foreground">
          Do not enter patient information. Field definitions, permitted values, timing, and units must
          come from an approved source dictionary.
        </p>
      </Card>
    </StaticWorkflowPage>
  );
}

export function ResearchPredictionPage() {
  return (
    <StaticWorkflowPage
      title="Research prediction is unavailable"
      description="This research prototype has no approved longitudinal cohort or validated, versioned model."
      icon={FlaskConical}
    >
      <Card className="space-y-4 p-5 sm:p-6">
        <h2 className="font-semibold">Readiness requirements</h2>
        <ul className="space-y-3 text-sm leading-6 text-muted-foreground">
          <li>Approved patient-linked dated longitudinal observations</li>
          <li>Clinically verified future conversion labels and prediction horizon</li>
          <li>Validated model artifact and authorized inference service</li>
        </ul>
        <button className="min-h-11 rounded-lg bg-primary px-4 font-semibold text-primary-foreground disabled:opacity-50" disabled type="button">
          Run research prediction — unavailable
        </button>
        <p role="status" className="text-sm text-muted-foreground">
          No prediction class, probability, or patient-specific output is available.
        </p>
      </Card>
    </StaticWorkflowPage>
  );
}

export function PredictionHistoryPage() {
  return (
    <StaticWorkflowPage
      title="Prediction history"
      description="Prediction history requires authorized backend records and model provenance."
      icon={FileClock}
    >
      <EmptyState title="No prediction history is available">
        No prediction requests or results are stored. This screen does not create or display example
        records.
      </EmptyState>
    </StaticWorkflowPage>
  );
}
