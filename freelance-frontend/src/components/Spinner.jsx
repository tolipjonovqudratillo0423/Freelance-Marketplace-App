export default function Spinner({ label = 'Loading' }) {
  return (
    <div className="flex min-h-48 flex-col items-center justify-center gap-3 text-sm text-zinc-500">
      <span className="size-5 animate-spin rounded-full border-2 border-zinc-700 border-t-zinc-200" />
      <span>{label}</span>
    </div>
  )
}
