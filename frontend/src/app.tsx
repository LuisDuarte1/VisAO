import { StrictMode } from "react";
import ReactDOM from "react-dom/client";
import { RouterProvider, createRouter } from "@tanstack/react-router";
import "./globals.css";

// Import the generated route tree
import { routeTree } from "./routeTree.gen";
import { GRPCContext, createGRPCContext } from "./lib/context";

// Create a new router instance
const router = createRouter({ routeTree });

// Register the router instance for type safety
declare module "@tanstack/react-router" {
  interface Register {
    router: typeof router;
  }
}

// Render the app
const rootElement = document.getElementById("app")!;
if (!rootElement.innerHTML) {
  const root = ReactDOM.createRoot(rootElement);
  root.render(
    <StrictMode>
      <GRPCContext.Provider value={createGRPCContext()}>
        <RouterProvider router={router} />
      </GRPCContext.Provider>
    </StrictMode>,
  );
}
