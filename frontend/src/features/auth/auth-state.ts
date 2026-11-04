export type AuthState =
  | { status: "not_configured" }
  | { status: "signed_out" }
  | { status: "authenticated"; subject: string };

// Kept explicitly unconfigured until Phase 45 policy and provider integration are approved.
export const initialAuthState: AuthState = { status: "not_configured" };
