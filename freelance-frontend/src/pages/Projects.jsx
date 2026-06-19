import { useEffect, useState } from 'react'
import EmptyState from '../components/EmptyState'
import { SearchIcon } from '../components/Icons'
import ProjectCard from '../components/ProjectCard'
import Spinner from '../components/Spinner'
import { apiRequest, getResults } from '../lib/api'
import { useLanguage } from '../context/language'

export default function Projects() {
  const [query, setQuery] = useState('')
  const [debouncedQuery, setDebouncedQuery] = useState('')
  const [projects, setProjects] = useState([])
  const [pagination, setPagination] = useState({ next: null, previous: null, count: 0 })
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState('')
  const { t } = useLanguage()

  useEffect(() => {
    const timer = setTimeout(() => setDebouncedQuery(query.trim()), 350)
    return () => clearTimeout(timer)
  }, [query])

  useEffect(() => {
    const controller = new AbortController()
    loadProjects(`/common/projects/${debouncedQuery ? `?search=${encodeURIComponent(debouncedQuery)}` : ''}`, controller.signal)
    return () => controller.abort()
  }, [debouncedQuery])

  async function loadProjects(path, signal) {
    setLoading(true)
    setError('')
    try {
      const response = await apiRequest(path, { signal })
      setProjects(getResults(response))
      setPagination({
        next: response?.data?.next || null,
        previous: response?.data?.previous || null,
        count: response?.data?.count ?? getResults(response).length,
      })
    } catch (requestError) {
      if (requestError.name !== 'AbortError') setError(requestError.message)
    } finally {
      if (!signal?.aborted) setLoading(false)
    }
  }

  return (
    <div className="page-shell">
      <div className="mb-10 flex flex-col gap-6 md:flex-row md:items-end md:justify-between">
        <div>
          <p className="text-xs font-semibold uppercase tracking-[0.16em] text-zinc-600">{t('openWork')}</p>
          <h1 className="mt-3 text-3xl font-semibold tracking-tight text-white sm:text-4xl">{t('findProject')}</h1>
          <p className="mt-3 text-sm text-zinc-500">{pagination.count} {t('project')} {t('available')}</p>
        </div>
        <label className="relative block w-full md:max-w-sm">
          <SearchIcon className="absolute left-3.5 top-1/2 size-4 -translate-y-1/2 text-zinc-600" />
          <input className="field pl-10" value={query} onChange={(event) => setQuery(event.target.value)} placeholder={t('searchProjects')} />
        </label>
      </div>

      {loading ? (
        <Spinner label={t('finding')} />
      ) : error ? (
        <EmptyState title={t('loadProjectsError')} description={error} action={<button className="btn-secondary" onClick={() => loadProjects('/common/projects/')}>{t('retry')}</button>} />
      ) : projects.length ? (
        <>
          <div className="grid gap-4 lg:grid-cols-2">
            {projects.map((project) => <ProjectCard key={project.id} project={project} />)}
          </div>
          {(pagination.previous || pagination.next) && (
            <div className="mt-8 flex justify-center gap-2">
              <button className="btn-secondary" disabled={!pagination.previous} onClick={() => loadProjects(pagination.previous)}>{t('previous')}</button>
              <button className="btn-secondary" disabled={!pagination.next} onClick={() => loadProjects(pagination.next)}>{t('next')}</button>
            </div>
          )}
        </>
      ) : (
        <EmptyState title={t('noMatches')} description={t('noMatchesText')} />
      )}
    </div>
  )
}
