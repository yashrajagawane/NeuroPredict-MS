import { useQuery } from "@tanstack/react-query";
import { Activity } from "lucide-react";

import { Button } from "@/components/ui/button";
import { Card } from "@/components/ui/card";

import { describeCheck, getServiceHealth } from "./service-health";

export function ServiceStatusCard() {
  const health = useQuery({
    queryKey: ["service-health"],
    queryFn: ({ signal }) => getServiceHealth(signal),
    staleTime: 30_000,
  });

  return (
    <Card aria-labelledby="service-status-title" className="p-5 sm:p-6">
      <div className="flex items-start gap-3">
        <span className="flex size-10 shrink-0 items-center justify-center rounded-xl bg-slate-100 text-slate-700">
          <Activity aria-hidden="true" size={19} />
        </span>
        <div className="min-w-0 flex-1">
          <h2 id="service-status-title" className="font-semibold">
            Service status
          </h2>
          {health.isPending ? (
            <p role="status" className="mt-1 text-sm text-muted-foreground">
              Checking API availability…
            </p>
          ) : health.isError ? (
            <p role="status" className="mt-1 text-sm text-muted-foreground">
              {health.isFetching
                ? "Retrying API status check…"
                : "API status is unavailable. Patient and prediction services remain disconnected."}
            </p>
          ) : (
            <>
              <p role="status" className="mt-1 text-sm text-muted-foreground">
                API process available; application readiness is {health.data.readiness.replace("_", " ")}.
              </p>
              <dl className="mt-4 grid gap-2 text-sm sm:grid-cols-3">
                <div>
                  <dt className="text-xs text-muted-foreground">Database</dt>
                  <dd className="font-medium">{describeCheck(health.data.checks.database)}</dd>
                </div>
                <div>
                  <dt className="text-xs text-muted-foreground">Authentication</dt>
                  <dd className="font-medium">{describeCheck(health.data.checks.authentication)}</dd>
                </div>
                <div>
                  <dt className="text-xs text-muted-foreground">Model</dt>
                  <dd className="font-medium">{describeCheck(health.data.checks.model)}</dd>
                </div>
              </dl>
            </>
          )}
          <Button
            className="mt-3"
            size="sm"
            variant="secondary"
            type="button"
            disabled={health.isFetching}
            onClick={() => void health.refetch()}
          >
            {health.isFetching ? "Checking…" : health.isError ? "Retry API check" : "Refresh status"}
          </Button>
        </div>
      </div>
    </Card>
  );
}
