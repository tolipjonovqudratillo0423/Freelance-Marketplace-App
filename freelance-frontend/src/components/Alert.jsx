export default function Alert({ children, tone = 'error' }) {
  const styles = tone === 'success'
    ? 'border-emerald-900/60 bg-emerald-950/30 text-emerald-300'
    : 'border-red-900/60 bg-red-950/30 text-red-300'

  return <div className={`rounded-lg border px-3.5 py-3 text-sm ${styles}`}>{children}</div>
}
