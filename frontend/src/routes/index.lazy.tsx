import { createLazyFileRoute } from "@tanstack/react-router";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { ChangeEvent, useContext } from "react";
import { GRPCContext } from "@/lib/context";
import React, {useCallback} from 'react'
import {useDropzone} from 'react-dropzone'

export const Route = createLazyFileRoute("/")({
  component: Index,
});

function Index() {
  const grpc = useContext(GRPCContext);

  async function handleFileUpload(
    event: ChangeEvent<HTMLInputElement>,
  ): Promise<void> {
    if (event.target.files == null) {
      throw new Error("File list is empty");
    }
    const file: File | null = event.target.files.item(0);
    if (file == null) {
      throw new Error("Could not find first file...");
    }
    const a = await grpc.client.uploadFile({
      file: new Uint8Array(await file.arrayBuffer()),
    });
    console.log(a.response);
  }

  const onDrop = useCallback((acceptedFiles: File[]) => {
    acceptedFiles.forEach(async (file: File) => {
      console.log("batatinhas")

      const value_read: ArrayBuffer = await file.arrayBuffer();

      const a = await grpc.client.uploadFile({
        file: new Uint8Array(value_read),
      });
      console.log(a.response);
    })
    
  }, [])
  const {getRootProps, getInputProps} = useDropzone({onDrop})
  
  return (
    <div className="flex flex-col h-svh w-svh gap-1.5 justify-center items-center px-40">
      <div {...getRootProps()} className="w-screen bg-gray-200 rounded-sm border-2 border-black border-dashed cursor-pointer">
        <input {...getInputProps()} />
        <p className="mt-3 text-center">Click or drag a file</p>
        <p className="text-5xl text-center mb-3">+</p>
      </div>
    </div>
  );
}
/*
<div className="flex flex-col h-svh gap-1.5 justify-center items-center">
  <Label htmlFor="file_upload">Upload .fits file</Label>
  <Input
    className="w-75"
    id="file_upload"
    type="file"
    onChange={handleFileUpload}
  />
</div>
*/
