import type { LucideIcon } from "lucide-react";
import { Link } from "react-router-dom";

import { Card } from "@/components/ui/card";

interface ModuleCardProps {
  title: string;
  description: string;
  to: string;
  icon: LucideIcon;
  status?: string;
}

export function ModuleCard({ title, description, to, icon: Icon, status = "Not connected" }: ModuleCardProps) {
  return (
    <Link className="group rounded-2xl" to={to}>
      <Card className="h-full p-5 transition-shadow group-hover:shadow-md sm:p-6">
        <div className="mb-5 flex items-center justify-between gap-3">
          <span className="flex size-11 items-center justify-center rounded-xl bg-muted text-slate-700">
            <Icon aria-hidden="true" size={20} strokeWidth={1.8} />
          </span>
          <span className="rounded-full bg-muted px-2.5 py-1 text-[11px] font-semibold text-muted-foreground">
            {status}
          </span>
        </div>
        <h3 className="font-semibold">{title}</h3>
        <p className="mt-1 text-sm leading-6 text-muted-foreground">{description}</p>
      </Card>
    </Link>
  );
}
