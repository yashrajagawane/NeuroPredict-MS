import type { LucideIcon } from "lucide-react";
import type { ReactNode } from "react";

interface StaticWorkflowPageProps {
  title: string;
  description: string;
  icon: LucideIcon;
  children: ReactNode;
}

export function StaticWorkflowPage({
  title,
  description,
  icon: Icon,
  children,
}: StaticWorkflowPageProps) {
  return (
    <section aria-labelledby="page-title" className="space-y-6">
      <header className="max-w-3xl">
        <p className="mb-3 flex items-center gap-2 text-sm font-semibold text-muted-foreground">
          <Icon aria-hidden="true" size={17} />
          Unavailable in this build
        </p>
        <h1 id="page-title" tabIndex={-1} className="text-2xl font-bold tracking-tight sm:text-3xl">
          {title}
        </h1>
        <p className="mt-3 leading-7 text-muted-foreground">{description}</p>
      </header>
      {children}
    </section>
  );
}
