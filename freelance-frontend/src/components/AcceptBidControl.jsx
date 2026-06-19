import { useState } from 'react'
import Alert from './Alert'
import { apiRequest } from '../lib/api'
import { useLanguage } from '../context/language'

export default function AcceptBidControl({ project, onAccepted }) {
  const [open, setOpen] = useState(false)
  const [bidId, setBidId] = useState('')
  const [state, setState] = useState({ loading: false, error: '' })
  const { t } = useLanguage()

  async function accept(event) {
    event.preventDefault()
    setState({ loading: true, error: '' })
    try {
      await apiRequest('/client/bid/accept', {
        method: 'POST',
        body: JSON.stringify({ bid: Number(bidId) }),
      })
      setOpen(false)
      setBidId('')
      onAccepted?.()
    } catch (error) {
      setState({ loading: false, error: error.message })
    }
  }

  if (project.status !== 'open') return null

  return (
    <div className="mt-5 border-t border-line pt-4">
      {!open ? (
        <button className="btn-secondary" onClick={() => setOpen(true)}>{t('acceptBid')}</button>
      ) : (
        <form onSubmit={accept} className="space-y-3">
          {state.error && <Alert>{state.error}</Alert>}
          <p className="text-xs leading-5 text-zinc-600">{t('acceptHint')}</p>
          <div className="flex flex-col gap-2 sm:flex-row">
            <input className="field" type="number" min="1" value={bidId} onChange={(event) => setBidId(event.target.value)} placeholder="Bid ID" required />
            <button className="btn-primary shrink-0" disabled={state.loading}>{state.loading ? t('accepting') : t('confirmAction')}</button>
            <button type="button" className="btn-ghost shrink-0" onClick={() => { setOpen(false); setState({ loading: false, error: '' }) }}>{t('cancel')}</button>
          </div>
        </form>
      )}
    </div>
  )
}
