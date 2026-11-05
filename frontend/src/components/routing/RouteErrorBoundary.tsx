import { Component, createRef, type ReactNode } from "react";
import { Link } from "react-router-dom";

import { Button } from "@/components/ui/button";
import { Card } from "@/components/ui/card";

interface RouteErrorBoundaryProps {
  children: ReactNode;
}

interface RouteErrorBoundaryState {
  hasError: boolean;
}

export class RouteErrorBoundary extends Component<
  RouteErrorBoundaryProps,
  RouteErrorBoundaryState
> {
  state: RouteErrorBoundaryState = { hasError: false };
  private headingRef = createRef<HTMLHeadingElement>();

  static getDerivedStateFromError(): RouteErrorBoundaryState {
    return { hasError: true };
  }

  componentDidMount() {
    if (this.state.hasError) this.headingRef.current?.focus();
  }

  componentDidUpdate(_previousProps: RouteErrorBoundaryProps, previousState: RouteErrorBoundaryState) {
    if (!previousState.hasError && this.state.hasError) {
      this.headingRef.current?.focus();
    }
  }

  private retry = () => this.setState({ hasError: false });

  render() {
    if (this.state.hasError) {
      return (
        <section aria-labelledby="route-error-title" className="mx-auto max-w-2xl py-8 sm:py-14">
          <Card className="p-6 sm:p-9">
            <p className="text-xs font-bold uppercase tracking-wider text-muted-foreground">
              Screen unavailable
            </p>
            <h1
              ref={this.headingRef}
              id="route-error-title"
              tabIndex={-1}
              className="mt-2 text-2xl font-bold tracking-tight"
            >
              We couldn’t load this screen
            </h1>
            <p role="status" className="mt-3 leading-7 text-muted-foreground">
              An unexpected display error occurred. No patient information or technical details are
              shown here.
            </p>
            <div className="mt-6 flex flex-wrap items-center gap-4">
              <Button type="button" onClick={this.retry}>
                Try again
              </Button>
              <Link className="text-sm font-semibold text-primary hover:underline" to="/">
                Back to overview
              </Link>
            </div>
          </Card>
        </section>
      );
    }

    return this.props.children;
  }
}
