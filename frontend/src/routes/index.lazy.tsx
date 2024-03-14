import { Button } from '@/components/ui/button'
import { createLazyFileRoute } from '@tanstack/react-router'
import { Input } from "@/components/ui/input"
import { Label } from "@/components/ui/label"
import { GrpcWebFetchTransport } from '@protobuf-ts/grpcweb-transport'
import { VisAOClient } from '@/gen/main.client'
import { ChangeEvent } from 'react'
 

export const Route = createLazyFileRoute('/')({
  component: Index,
})

function Index() {

  async function handleFileUpload(event: ChangeEvent<HTMLInputElement>): Promise<void>{
    let transport = new GrpcWebFetchTransport({
      baseUrl: "http://localhost:5173/api"
    })
    let client = new VisAOClient(transport)
    if  (event.target.files == null){
      throw new Error("File list is empty")
    }

    const file: File | null = event.target.files.item(0)
    if (file == null){
      throw new Error("Could not find first file...")
    }
    const a = await client.uploadFile({
      file: new Uint8Array(await file.arrayBuffer())
    })
    console.log(a.response)
  }

  return (
    <div className="flex flex-col h-svh gap-1.5 justify-center items-center">
      <Label htmlFor="file_upload">Upload .fits file</Label>
      <Input className='w-75' id="file_upload" type="file" onChange={handleFileUpload}/>
    </div>
  )
}