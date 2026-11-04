# NeuroPredict MS frontend

This is the initial React/TypeScript/Vite shell for the research application. It includes the responsive navigation, approved six-module entry points, a typed API-base configuration, reusable Tailwind/shadcn-style primitives, and explicit unavailable states.

## Local development

Use the pinned Node.js version from the repository root `.nvmrc` (Node 24.22.2), then from this directory:

```powershell
npm ci
npm run dev
```

Available checks are `npm run typecheck`, `npm run lint`, `npm test`, and `npm run build`.

`VITE_API_BASE_URL` may point to the FastAPI service. It is a public URL only; never place Supabase secret/service-role keys, database credentials, access tokens, or patient information in a `VITE_` variable. Authentication is deliberately marked unconfigured. The typed API helper is not yet connected to health or patient endpoints.

## Current scope

- No Supabase Auth client or login form is active.
- No patient, visit, clinical-data, prediction, or prediction-history data is loaded or fabricated.
- Prediction routes show an unavailable state and no class or probability.
- React Hook Form, Zod, and Recharts are deferred until approved forms and real supported evaluation data exist; they are not installed without a use case.
- This prototype is research/education only and is not a medical diagnostic or treatment tool.
