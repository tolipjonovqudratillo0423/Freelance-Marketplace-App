import { useEffect, useState } from 'react'
import { Link, useParams } from 'react-router-dom'
import Alert from '../components/Alert'
import EmptyState from '../components/EmptyState'
import SkillTags from '../components/SkillTags'
import Spinner from '../components/Spinner'
import StatusBadge from '../components/StatusBadge'
import { useAuth } from '../context/auth'
import { apiRequest, getResults } from '../lib/api'
import { formatMoney } from '../lib/format'
import { useLanguage } from '../context/language'

export default function ProjectDetail() {
  const { id } = useParams()
  const { isAuthenticated, role } = useAuth()
  const [project, setProject] = useState(null)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState('')
  const [bid, setBid] = useState({ reply: '', price: '' })
  const [bidState, setBidState] = useState({ loading: false, error: '', success: '' })
  const { t } = useLanguage()

  useEffect(() => {
    let active = true
    async function load() {
      try {
        const response = await apiRequest('/common/projects/?page_size=1000')
        const found = getResults(response).find((item) => String(item.id) === String(id))
        if (!found) throw new Error('This project was not found or is no longer open.')
        if (active) setProject(found)
      } catch (requestError) {
        if (active) setError(requestError.message)
      } finally {
        if (active) setLoading(false)
      }
    }
    load()
    return () => { active = false }
  }, [id])

  async function placeBid(event) {
    event.preventDefault()
    setBidState({ loading: true, error: '', success: '' })
    try {
      const response = await apiRequest('/freelancer/bid/create', {
        method: 'POST',
        body: JSON.stringify({ project: Number(id), reply: bid.reply, price: Number(bid.price) }),
      })
      setBid({ reply: '', price: '' })
      setBidState({ loading: false, error: '', success: response.message || 'Your bid has been placed.' })
    } catch (requestError) {
      setBidState({ loading: false, error: requestError.message, success: '' })
    }
  }

  if (loading) return <div className="page-shell"><Spinner label={t('loadingProject')} /></div>
  if (error || !project) return <div className="page-shell"><EmptyState title={t('unavailable')} description={error} action={<Link to="/projects" className="btn-secondary">{t('backProjects')}</Link>} /></div>

  const embeddedBids = Array.isArray(project.bids) ? project.bids : []

  return (
    <div className="page-shell">
      <Link to="/projects" className="text-sm text-zinc-600 transition hover:text-zinc-300">← {t('backProjects')}</Link>
      <div className="mt-7 grid gap-6 lg:grid-cols-[1fr_360px]">
        <div className="space-y-6">
          <section className="surface p-6 sm:p-8">
            <div className="flex flex-col gap-5 sm:flex-row sm:items-start sm:justify-between">
              <div>
                <p className="text-xs text-zinc-600">{t('postedBy')} {project.client || t('client')}</p>
                <h1 className="mt-3 text-3xl font-semibold tracking-tight text-white">{project.title}</h1>
              </div>
              <StatusBadge status={project.status} />
            </div>
            <div className="mt-8 border-t border-line pt-7">
              <h2 className="text-sm font-medium text-zinc-300">{t('aboutProject')}</h2>
              <p className="mt-3 whitespace-pre-wrap text-sm leading-7 text-zinc-500">{project.description}</p>
            </div>
            <div className="mt-8 border-t border-line pt-7">
              <h2 className="mb-3 text-sm font-medium text-zinc-300">{t('skills')}</h2>
              <SkillTags skills={project.required_skills || []} />
            </div>
          </section>

          <section className="surface p-6 sm:p-8">
            <div className="flex items-center justify-between">
              <h2 className="font-semibold text-zinc-200">{t('proposals')}</h2>
              <span className="text-xs text-zinc-600">{embeddedBids.length} {t('visible')}</span>
            </div>
            {embeddedBids.length ? (
              <div className="mt-5 divide-y divide-line border-y border-line">
                {embeddedBids.map((item) => (
                  <div key={item.id} className="py-5">
                    <div className="flex items-center justify-between gap-4">
                      <span className="text-sm font-medium text-zinc-300">{item.freelancer}</span>
                      <span className="text-sm text-zinc-300">{formatMoney(item.price)}</span>
                    </div>
                    <p className="mt-2 text-sm leading-6 text-zinc-500">{item.reply}</p>
                  </div>
                ))}
              </div>
            ) : (
              <p className="mt-4 rounded-lg border border-dashed border-line px-4 py-6 text-sm leading-6 text-zinc-600">
                {t('privateProposals')}
              </p>
            )}
          </section>
        </div>

        <aside className="space-y-4">
          <section className="surface p-6">
            <p className="text-xs uppercase tracking-wider text-zinc-600">{t('projectBudget')}</p>
            <p className="mt-3 text-xl font-semibold text-white">
              {formatMoney(project.min_price)} <span className="text-zinc-700">—</span> {formatMoney(project.max_price)}
            </p>
            {project.freelancer && <p className="mt-3 text-xs text-zinc-600">{t('assignedTo')} {project.freelancer}</p>}
          </section>

          {role === 'freelancer' && project.status === 'open' && (
            <form onSubmit={placeBid} className="surface space-y-4 p-6">
              <div>
                <h2 className="font-semibold text-zinc-200">{t('placeBid')}</h2>
                <p className="mt-1 text-xs text-zinc-600">{t('bidHint')}</p>
              </div>
              {bidState.error && <Alert>{bidState.error}</Alert>}
              {bidState.success && <Alert tone="success">{bidState.success}</Alert>}
              <label className="block">
                <span className="mb-2 block text-xs text-zinc-500">{t('yourPrice')}</span>
                <input className="field" type="number" step="0.01" min={project.min_price} max={project.max_price} value={bid.price} onChange={(event) => setBid((current) => ({ ...current, price: event.target.value }))} placeholder={project.min_price} required />
              </label>
              <label className="block">
                <span className="mb-2 block text-xs text-zinc-500">{t('proposal')}</span>
                <textarea className="field min-h-32 resize-y" value={bid.reply} onChange={(event) => setBid((current) => ({ ...current, reply: event.target.value }))} placeholder={t('proposalPlaceholder')} required />
              </label>
              <button className="btn-primary w-full" disabled={bidState.loading}>
                {bidState.loading ? t('submitting') : t('submitProposal')}
              </button>
            </form>
          )}

          {!isAuthenticated && project.status === 'open' && (
            <section className="surface p-6">
              <p className="text-sm leading-6 text-zinc-500">{t('loginToBidText')}</p>
              <Link to="/login" className="btn-primary mt-4 w-full">{t('loginToBid')}</Link>
            </section>
          )}
        </aside>
      </div>
    </div>
  )
}
