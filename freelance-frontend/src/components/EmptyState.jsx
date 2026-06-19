export default function EmptyState({ title, description, action }) {
  return (
    <div className="surface flex min-h-64 flex-col items-center justify-center px-6 text-center">
      <div className="mb-4 grid size-10 place-items-center rounded-lg border border-line bg-[#111] text-zinc-600">·</div>
      <h2 className="font-semibold text-zinc-200">{title}</h2>
      <p className="mt-2 max-w-md text-sm leading-6 text-zinc-500">{description}</p>
      {action && <div className="mt-5">{action}</div>}
    </div>
  )
}
