import { Button } from '@/components/ui/button'
import { createLazyFileRoute } from '@tanstack/react-router'

export const Route = createLazyFileRoute('/')({
  component: Index,
})

function Index() {
  return (
    <div className="h-svh flex justify-center items-center">
      <Button>Hello world!</Button>
    </div>
  )
}