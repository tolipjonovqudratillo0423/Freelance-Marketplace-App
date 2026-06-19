import { useEffect, useState } from 'react'
import { Link } from 'react-router-dom'
import EmptyState from '../components/EmptyState'
import Spinner from '../components/Spinner'
import StatusBadge from '../components/StatusBadge'
import { apiRequest, getResults } from '../lib/api'
import { formatMoney, projectName } from '../lib/format'
import { useLanguage } from '../context/language'

export default function FreelancerDashboard() {
  const [bids, setBids] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState('')
  const { t } = useLanguage()

  async function loadBids() {
    setLoading(true)
    setError('')
    try {
      const response = await apiRequest('/freelancer/bid/')
      setBids(getResults(response))
    } catch (requestError) {
      setError(requestError.message)
    } finally {
      setLoading(false)
    }
  }

  useEffect(() => {
    let active = true
    async function initialLoad() {
      try {
        const response = await apiRequest('/freelancer/bid/')
        if (active) setBids(getResults(response))
      } catch (requestError) {
        if (active) setError(requestError.message)
      } finally {
        if (active) setLoading(false)
      }
    }
    initialLoad()
    return () => { active = false }
  }, [])

  const accepted = bids.filter((bid) => bid.status === 'ACCEPTED').length
  const pending = bids.filter((bid) => bid.status === 'NEW').length

  return (
    <div className="page-shell">
      <div className="mb-8 flex flex-col gap-5 sm:flex-row sm:items-end sm:justify-between">
        <div>
          <p className="text-xs font-semibold uppercase tracking-[0.16em] text-zinc-600">{t('freelancerWorkspace')}</p>
          <h1 className="mt-3 text-3xl font-semibold tracking-tight text-white">{t('yourProposals')}</h1>
          <p className="mt-3 text-sm text-zinc-500">{t('freelancerIntro')}</p>
        </div>
        <Link to="/projects" className="btn-primary">{t('findProjects')}</Link>
      </div>

      {!loading && !error && bids.length > 0 && (
        <div className="mb-6 grid grid-cols-3 gap-px overflow-hidden rounded-xl border border-line bg-line">
          {[
            [bids.length, t('totalBids')],
            [pending, t('pending')],
            [accepted, t('accepted')],
          ].map(([value, label]) => (
            <div key={label} className="bg-panel px-4 py-5 sm:px-6">
              <div className="text-xl font-semibold text-zinc-100">{value}</div>
              <div className="mt-1 text-xs text-zinc-600">{label}</div>
            </div>
          ))}
        </div>
      )}

      {loading ? (
        <Spinner label={t('loadingProposals')} />
      ) : error ? (
        <EmptyState title={t('proposalsError')} description={error} action={<button className="btn-secondary" onClick={loadBids}>{t('retry')}</button>} />
      ) : bids.length ? (
        <div className="space-y-3">
          {bids.map((bid) => (
            <article key={bid.id} className="surface p-5 sm:p-6">
              <div className="flex flex-col gap-4 sm:flex-row sm:items-start sm:justify-between">
                <div>
                  <p className="text-xs text-zinc-700">{t('bid')} #{bid.id}</p>
                  <h2 className="mt-2 font-semibold text-zinc-100">{projectName(bid.project)}</h2>
                </div>
                <div className="flex items-center gap-3">
                  <span className="text-sm font-semibold text-zinc-200">{formatMoney(bid.price)}</span>
                  <StatusBadge status={bid.status} />
                </div>
              </div>
              <p className="mt-4 border-t border-line pt-4 text-sm leading-6 text-zinc-500">{bid.reply}</p>
            </article>
          ))}
        </div>
      ) : (
        <EmptyState
          title={t('noProposals')}
          description={t('noProposalsText')}
          action={<Link to="/projects" className="btn-primary">{t('browse')}</Link>}
        />
      )}
    </div>
  )
}
