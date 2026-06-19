import { useCallback, useEffect, useState } from 'react'
import AcceptBidControl from '../components/AcceptBidControl'
import CreateProjectForm from '../components/CreateProjectForm'
import EmptyState from '../components/EmptyState'
import SkillTags from '../components/SkillTags'
import Spinner from '../components/Spinner'
import StatusBadge from '../components/StatusBadge'
import { apiRequest, getResults } from '../lib/api'
import { formatMoney } from '../lib/format'
import { useLanguage } from '../context/language'

export default function ClientDashboard() {
  const [projects, setProjects] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState('')
  const [showCreate, setShowCreate] = useState(false)
  const { t } = useLanguage()

  const loadProjects = useCallback(async () => {
    setLoading(true)
    setError('')
    try {
      const response = await apiRequest('/client/projects/all')
      setProjects(getResults(response))
    } catch (requestError) {
      setError(requestError.message)
    } finally {
      setLoading(false)
    }
  }, [])

  useEffect(() => {
    let active = true
    async function initialLoad() {
      try {
        const response = await apiRequest('/client/projects/all')
        if (active) setProjects(getResults(response))
      } catch (requestError) {
        if (active) setError(requestError.message)
      } finally {
        if (active) setLoading(false)
      }
    }
    initialLoad()
    return () => { active = false }
  }, [])

  async function refreshed() {
    setShowCreate(false)
    await loadProjects()
  }

  return (
    <div className="page-shell">
      <div className="mb-8 flex flex-col gap-5 sm:flex-row sm:items-end sm:justify-between">
        <div>
          <p className="text-xs font-semibold uppercase tracking-[0.16em] text-zinc-600">{t('clientWorkspace')}</p>
          <h1 className="mt-3 text-3xl font-semibold tracking-tight text-white">{t('yourProjects')}</h1>
          <p className="mt-3 text-sm text-zinc-500">{t('clientIntro')}</p>
        </div>
        <button className="btn-primary" onClick={() => setShowCreate((value) => !value)}>
          {showCreate ? t('hideForm') : t('newProject')}
        </button>
      </div>

      {showCreate && <CreateProjectForm onCreated={refreshed} onCancel={() => setShowCreate(false)} />}

      {loading ? (
        <Spinner label={t('loadingProjects')} />
      ) : error ? (
        <EmptyState title={t('dashboardError')} description={error} action={<button className="btn-secondary" onClick={loadProjects}>{t('retry')}</button>} />
      ) : projects.length ? (
        <div className="grid gap-4 lg:grid-cols-2">
          {projects.map((project) => (
            <article key={project.id} className="surface p-5 sm:p-6">
              <div className="flex items-start justify-between gap-4">
                <div>
                  <p className="mb-2 text-xs text-zinc-700">{t('project')} #{project.id}</p>
                  <h2 className="font-semibold text-zinc-100">{project.title}</h2>
                </div>
                <StatusBadge status={project.status} />
              </div>
              <p className="mt-3 line-clamp-2 text-sm leading-6 text-zinc-500">{project.description}</p>
              <div className="mt-4"><SkillTags skills={project.required_skills || []} limit={3} /></div>
              <div className="mt-5 flex items-center justify-between text-sm">
                <span className="text-zinc-600">{t('budget')}</span>
                <span className="font-medium text-zinc-300">{formatMoney(project.min_price)} — {formatMoney(project.max_price)}</span>
              </div>
              {project.freelancer && (
                <div className="mt-3 flex items-center justify-between text-sm">
                  <span className="text-zinc-600">{t('freelancer')}</span>
                  <span className="text-zinc-300">{project.freelancer}</span>
                </div>
              )}
              <AcceptBidControl project={project} onAccepted={loadProjects} />
            </article>
          ))}
        </div>
      ) : (
        <EmptyState
          title={t('noProjects')}
          description={t('noProjectsText')}
          action={<button className="btn-primary" onClick={() => setShowCreate(true)}>{t('createProject')}</button>}
        />
      )}
    </div>
  )
}
