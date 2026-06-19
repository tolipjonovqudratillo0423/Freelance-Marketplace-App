import { Link } from 'react-router-dom'
import { formatMoney } from '../lib/format'
import { ArrowRightIcon } from './Icons'
import SkillTags from './SkillTags'
import StatusBadge from './StatusBadge'
import { useLanguage } from '../context/language'

export default function ProjectCard({ project }) {
  const { t } = useLanguage()
  return (
    <article className="surface group p-5 transition-colors hover:border-zinc-700 sm:p-6">
      <div className="flex items-start justify-between gap-4">
        <div className="min-w-0">
          <p className="mb-2 text-xs text-zinc-600">{t('postedBy')} {project.client || t('client')}</p>
          <h2 className="text-lg font-semibold tracking-tight text-zinc-100">{project.title}</h2>
        </div>
        <StatusBadge status={project.status} />
      </div>
      <p className="mt-3 line-clamp-2 text-sm leading-6 text-zinc-500">{project.description}</p>
      <div className="mt-5"><SkillTags skills={project.required_skills || []} limit={4} /></div>
      <div className="mt-6 flex items-center justify-between border-t border-line pt-4">
        <p className="text-sm font-medium text-zinc-300">
          {formatMoney(project.min_price)} <span className="text-zinc-700">—</span> {formatMoney(project.max_price)}
        </p>
        <Link to={`/projects/${project.id}`} className="flex items-center gap-1.5 text-sm font-medium text-zinc-400 transition group-hover:text-white">
          {t('view')} <ArrowRightIcon />
        </Link>
      </div>
    </article>
  )
}
