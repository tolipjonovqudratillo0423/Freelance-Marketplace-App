import { humanize } from '../lib/format'

const tones = {
  open: 'border-sky-900/60 bg-sky-950/40 text-sky-300',
  in_progress: 'border-amber-900/60 bg-amber-950/40 text-amber-300',
  completed: 'border-emerald-900/60 bg-emerald-950/40 text-emerald-300',
  NEW: 'border-zinc-700 bg-zinc-800/70 text-zinc-300',
  ACCEPTED: 'border-emerald-900/60 bg-emerald-950/40 text-emerald-300',
  DECLINED: 'border-red-900/60 bg-red-950/40 text-red-300',
}

export default function StatusBadge({ status }) {
  return (
    <span className={`inline-flex rounded-full border px-2.5 py-1 text-[11px] font-semibold tracking-wide ${tones[status] || tones.NEW}`}>
      {humanize(status)}
    </span>
  )
}
