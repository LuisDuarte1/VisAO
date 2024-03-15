import { VisAOClient } from "@/gen/main.client";
import { GrpcWebFetchTransport } from "@protobuf-ts/grpcweb-transport";
import { QueryClient } from "@tanstack/react-query";
import React from "react";

const transport = new GrpcWebFetchTransport({
  baseUrl: "http://localhost:5173/api",
});

export const GRPCContext = React.createContext(createGRPCContext());

export function createGRPCContext() {
  return {
    transport: transport,
    client: new VisAOClient(transport),
  };
}

export const queryClient = new QueryClient();
