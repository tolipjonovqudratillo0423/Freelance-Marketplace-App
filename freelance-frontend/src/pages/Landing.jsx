import { Link } from 'react-router-dom'
import { ArrowRightIcon, CheckIcon, SearchIcon } from '../components/Icons'
import { useLanguage } from '../context/language'

const projects = [
  { title: 'Product designer for fintech app', skills: ['Figma', 'Product'], price: '$2.4k', active: true },
  { title: 'Build a React analytics dashboard', skills: ['React', 'API'], price: '$3.8k' },
  { title: 'Brand identity for AI startup', skills: ['Branding', 'Design'], price: '$1.9k' },
]

const steps = [
  ['01', 'Publish the work', 'Define the outcome, budget, and expertise your project needs.'],
  ['02', 'Compare proposals', 'Review focused bids from specialists who understand the brief.'],
  ['03', 'Start building', 'Choose the right fit and move from idea to finished work.'],
]

function MarketplacePreview() {
  return (
    <div className="relative mx-auto w-full max-w-[560px] lg:ml-auto">
      <div className="absolute -left-8 top-16 hidden h-64 w-px bg-line lg:block" />
      <div className="absolute -right-6 bottom-10 hidden size-3 rounded-full border border-zinc-700 bg-ink lg:block" />

      <div className="overflow-hidden rounded-2xl border border-zinc-700/80 bg-[#121212] shadow-[0_28px_80px_rgba(0,0,0,0.42)]">
        <div className="flex h-11 items-center justify-between border-b border-line px-4">
          <div className="flex gap-1.5">
            <span className="size-2 rounded-full bg-zinc-700" />
            <span className="size-2 rounded-full bg-zinc-800" />
            <span className="size-2 rounded-full bg-zinc-800" />
          </div>
          <span className="text-[10px] font-medium uppercase tracking-[0.18em] text-zinc-700">Marketplace</span>
          <span className="size-5 rounded-md border border-line" />
        </div>

        <div className="grid min-h-[390px] grid-cols-[54px_1fr] sm:grid-cols-[148px_1fr]">
          <aside className="border-r border-line p-3 sm:p-4">
            <div className="mb-7 flex items-center gap-2">
              <span className="grid size-6 shrink-0 place-items-center rounded-md bg-white text-[9px] font-black text-black">F</span>
              <span className="hidden text-xs font-semibold text-zinc-300 sm:block">Freeform</span>
            </div>
            <div className="space-y-1.5">
              {['Discover', 'Proposals', 'Messages'].map((item, index) => (
                <div key={item} className={`flex h-8 items-center gap-2 rounded-md px-2 ${index === 0 ? 'bg-white/[0.06] text-zinc-300' : 'text-zinc-700'}`}>
                  <span className={`size-1.5 rounded-full ${index === 0 ? 'bg-accent' : 'border border-zinc-700'}`} />
                  <span className="hidden text-[10px] sm:block">{item}</span>
                </div>
              ))}
            </div>
          </aside>

          <div className="min-w-0 p-4 sm:p-5">
            <div className="flex items-center justify-between">
              <div>
                <p className="text-[9px] uppercase tracking-[0.15em] text-zinc-700">Discover</p>
                <h3 className="mt-1 text-sm font-semibold text-zinc-200">Open projects</h3>
              </div>
              <span className="rounded-md border border-line px-2 py-1 text-[9px] text-zinc-600">24 live</span>
            </div>

            <div className="mt-4 flex items-center gap-2 rounded-lg border border-line bg-[#0e0e0e] px-3 py-2.5">
              <SearchIcon className="size-3 text-zinc-700" />
              <span className="text-[10px] text-zinc-700">Search opportunities...</span>
            </div>

            <div className="mt-3 space-y-2">
              {projects.map((project) => (
                <div
                  key={project.title}
                  className={`rounded-xl border p-3.5 transition ${project.active ? 'border-zinc-600 bg-white/[0.035]' : 'border-line bg-[#101010]'}`}
                >
                  <div className="flex items-start justify-between gap-3">
                    <div className="min-w-0">
                      <div className="flex items-center gap-2">
                        {project.active && <span className="size-1.5 shrink-0 rounded-full bg-accent" />}
                        <p className="truncate text-[11px] font-medium text-zinc-300">{project.title}</p>
                      </div>
                      <div className="mt-3 flex gap-1">
                        {project.skills.map((skill) => (
                          <span key={skill} className="rounded border border-line px-1.5 py-0.5 text-[8px] text-zinc-600">{skill}</span>
                        ))}
                      </div>
                    </div>
                    <span className="shrink-0 text-[10px] font-medium text-zinc-400">{project.price}</span>
                  </div>
                </div>
              ))}
            </div>
          </div>
        </div>
      </div>

      <div className="float-slow absolute -bottom-5 -left-3 flex items-center gap-3 rounded-xl border border-zinc-700 bg-[#171717] px-3.5 py-3 shadow-xl sm:-left-8">
        <span className="grid size-8 place-items-center rounded-full bg-accent text-black"><CheckIcon className="size-4" /></span>
        <div>
          <p className="text-[10px] font-medium text-zinc-300">Proposal accepted</p>
          <p className="mt-0.5 text-[9px] text-zinc-600">Project ready to begin</p>
        </div>
      </div>
    </div>
  )
}

export default function Landing() {
  const { t } = useLanguage()
  return (
    <div className="relative overflow-hidden">
      <div className="pointer-events-none absolute inset-0">
        <div className="dot-field drift absolute -left-24 top-[720px] h-[420px] w-[420px] opacity-25" />
        <div className="dot-field drift absolute -right-32 top-[1380px] h-[520px] w-[520px] opacity-20" />
        <div className="absolute left-[8%] top-[1180px] h-28 w-28 border border-line/60" />
        <div className="absolute right-[6%] top-[2140px] size-20 rounded-full border border-line/70" />
      </div>

      <section className="relative overflow-hidden border-b border-line">
        <div className="dot-field pointer-events-none absolute -right-16 -top-16 h-72 w-72 opacity-30" />
        <div className="dot-field pointer-events-none absolute -bottom-28 left-[22%] h-64 w-64 opacity-20" />
        <div className="pointer-events-none absolute inset-0 mx-auto grid max-w-[1180px] grid-cols-8 opacity-40">
          {Array.from({ length: 8 }).map((_, index) => <span key={index} className="border-l border-line last:border-r" />)}
        </div>
        <div className="pointer-events-none absolute left-0 right-0 top-28 h-px bg-line/60" />
        <div className="pointer-events-none absolute bottom-24 left-0 right-0 h-px bg-line/40" />
        <span className="cross-mark pointer-events-none left-[8%] top-28 hidden opacity-70 md:block" />
        <span className="cross-mark pointer-events-none bottom-24 right-[12%] hidden opacity-50 md:block" />
        <div className="pointer-events-none absolute left-[5%] top-1/2 hidden h-px w-16 border-t border-dashed border-zinc-800 lg:block" />

        <div className="relative mx-auto grid max-w-[1180px] gap-20 px-5 py-20 sm:py-28 md:px-8 lg:grid-cols-[0.95fr_1.05fr] lg:items-center lg:gap-12 lg:py-32">
          <div className="reveal">
            <div className="mb-7 inline-flex items-center gap-2 rounded-full border border-line bg-panel px-3 py-1.5 text-xs text-zinc-400">
              <span className="relative flex size-2">
                <span className="absolute inline-flex size-full animate-ping rounded-full bg-accent opacity-40" />
                <span className="relative inline-flex size-2 rounded-full bg-accent" />
              </span>
              {t('heroBadge')}
            </div>

            <h1 className="max-w-2xl text-5xl font-semibold leading-[1.02] tracking-[-0.05em] text-white sm:text-6xl lg:text-[68px]">
              {t('heroTitle')}
            </h1>
            <p className="mt-7 max-w-xl text-base leading-7 text-zinc-500 sm:text-lg">
              {t('heroText')}
            </p>

            <div className="mt-9 flex flex-col gap-3 sm:flex-row">
              <Link to="/projects" className="btn-primary px-5 py-3">
                {t('explore')} <ArrowRightIcon />
              </Link>
              <Link to="/register" className="btn-secondary px-5 py-3">{t('postProject')}</Link>
            </div>

            <div className="mt-9 flex flex-wrap items-center gap-x-6 gap-y-3 text-xs text-zinc-600">
              {[t('clearBudgets'), t('directProposals'), t('noClutter')].map((item) => (
                <span key={item} className="flex items-center gap-2">
                  <CheckIcon className="size-3 text-zinc-500" /> {item}
                </span>
              ))}
            </div>
          </div>

          <div className="reveal reveal-delay-2"><MarketplacePreview /></div>
        </div>
      </section>

      <section className="border-b border-line">
        <div className="mx-auto grid max-w-[1180px] grid-cols-2 divide-x divide-line border-x border-line md:grid-cols-4">
          {[
            ['24h', 'Average first proposal'],
            ['3×', 'Faster shortlisting'],
            ['100%', 'Project focused'],
            ['Direct', 'Client collaboration'],
          ].map(([value, label], index) => (
            <div key={label} className={`reveal px-5 py-7 sm:px-8 ${index > 1 ? 'border-t border-line md:border-t-0' : ''}`} style={{ animationDelay: `${index * 80}ms` }}>
              <div className="text-2xl font-semibold tracking-tight text-zinc-100">{value}</div>
              <div className="mt-2 text-xs leading-5 text-zinc-600">{label}</div>
            </div>
          ))}
        </div>
      </section>

      <section className="page-shell relative py-24 sm:py-32">
        <span className="cross-mark pointer-events-none -left-10 top-32 hidden opacity-50 xl:block" />
        <div className="pointer-events-none absolute -right-24 top-20 hidden h-40 w-40 border border-line/50 xl:block">
          <div className="absolute left-1/2 top-0 h-full w-px bg-line/50" />
          <div className="absolute left-0 top-1/2 h-px w-full bg-line/50" />
          <span className="absolute left-1/2 top-1/2 size-2 -translate-x-1/2 -translate-y-1/2 rounded-full border border-zinc-700 bg-ink" />
        </div>
        <div className="mb-12 max-w-2xl">
          <p className="text-xs font-semibold uppercase tracking-[0.18em] text-zinc-600">{t('momentum')}</p>
          <h2 className="mt-4 text-3xl font-semibold tracking-[-0.035em] text-white sm:text-5xl">
            {t('everything')}
          </h2>
          <p className="mt-5 max-w-xl text-sm leading-7 text-zinc-500">
            From discovery to decision, each part of the experience is built to keep the work moving.
          </p>
        </div>

        <div className="grid gap-4 lg:grid-cols-3">
          <article className="surface card-lift overflow-hidden p-7 lg:col-span-2 sm:p-9">
            <div className="flex items-start justify-between gap-4">
              <div>
                <span className="font-mono text-[10px] text-zinc-700">01 / DISCOVER</span>
                <h3 className="mt-4 text-xl font-semibold text-zinc-100">Find work that fits</h3>
                <p className="mt-3 max-w-md text-sm leading-6 text-zinc-500">
                  Search focused project briefs with clear scope, skills, and budgets before you invest time in a proposal.
                </p>
              </div>
              <span className="grid size-10 shrink-0 place-items-center rounded-xl border border-line bg-[#111] text-zinc-500">
                <SearchIcon className="size-4" />
              </span>
            </div>
            <div className="mt-10 grid gap-2 sm:grid-cols-3">
              {['Development', 'Design', 'Marketing'].map((category, index) => (
                <div key={category} className={`rounded-xl border p-4 ${index === 0 ? 'border-zinc-600 bg-white/[0.025]' : 'border-line bg-[#111]'}`}>
                  <span className={`mb-7 block size-2 rounded-full ${index === 0 ? 'bg-accent' : 'bg-zinc-800'}`} />
                  <p className="text-xs font-medium text-zinc-400">{category}</p>
                  <p className="mt-1 text-[10px] text-zinc-700">{[18, 12, 9][index]} open projects</p>
                </div>
              ))}
            </div>
          </article>

          <article className="surface card-lift flex min-h-[340px] flex-col p-7 sm:p-9">
            <span className="font-mono text-[10px] text-zinc-700">02 / PROPOSE</span>
            <h3 className="mt-4 text-xl font-semibold text-zinc-100">Simple, serious proposals</h3>
            <p className="mt-3 text-sm leading-6 text-zinc-500">Lead with your approach and a transparent price.</p>
            <div className="mt-auto space-y-2 pt-8">
              <div className="rounded-xl border border-zinc-700 bg-[#111] p-4">
                <div className="flex items-center justify-between">
                  <span className="text-[10px] text-zinc-500">Your proposal</span>
                  <span className="text-xs font-semibold text-zinc-200">$2,800</span>
                </div>
                <div className="mt-4 h-1.5 w-full rounded-full bg-zinc-800">
                  <div className="h-full w-3/4 rounded-full bg-zinc-400" />
                </div>
              </div>
              <div className="ml-7 rounded-xl border border-line bg-[#111] p-3 text-[10px] text-zinc-600">Ready to send</div>
            </div>
          </article>

          <article className="surface card-lift p-7 sm:p-9">
            <span className="font-mono text-[10px] text-zinc-700">03 / DECIDE</span>
            <h3 className="mt-4 text-xl font-semibold text-zinc-100">Make a confident choice</h3>
            <p className="mt-3 text-sm leading-6 text-zinc-500">Compare price, expertise, and thinking in one calm view.</p>
            <div className="mt-8 space-y-2">
              {[['AM', 'Alex Morgan', 'Selected'], ['SK', 'Sara Kim', 'Reviewing']].map(([initials, name, status], index) => (
                <div key={name} className={`flex items-center gap-3 rounded-xl border p-3 ${index === 0 ? 'border-zinc-600' : 'border-line'}`}>
                  <span className="grid size-8 place-items-center rounded-full bg-zinc-800 text-[9px] text-zinc-400">{initials}</span>
                  <div className="min-w-0 flex-1">
                    <p className="text-xs text-zinc-400">{name}</p>
                    <p className="mt-0.5 text-[9px] text-zinc-700">{status}</p>
                  </div>
                  {index === 0 && <CheckIcon className="size-3.5 text-accent" />}
                </div>
              ))}
            </div>
          </article>

          <article className="surface card-lift relative overflow-hidden p-7 lg:col-span-2 sm:p-9">
            <div className="relative z-10 max-w-md">
              <span className="font-mono text-[10px] text-zinc-700">04 / DELIVER</span>
              <h3 className="mt-4 text-xl font-semibold text-zinc-100">Keep every project visible</h3>
              <p className="mt-3 text-sm leading-6 text-zinc-500">
                Role-specific dashboards give clients and freelancers a clear view of every active commitment.
              </p>
            </div>
            <div className="mt-9 grid grid-cols-3 gap-2">
              {[['Open', '08'], ['In progress', '03'], ['Completed', '16']].map(([label, value], index) => (
                <div key={label} className="rounded-xl border border-line bg-[#111] p-4">
                  <span className={`mb-5 block h-0.5 rounded-full ${['bg-sky-700', 'bg-amber-700', 'bg-emerald-700'][index]}`} />
                  <p className="text-lg font-semibold text-zinc-300">{value}</p>
                  <p className="mt-1 text-[9px] text-zinc-700">{label}</p>
                </div>
              ))}
            </div>
          </article>
        </div>
      </section>

      <section className="border-y border-line bg-[#111]">
        <div className="page-shell relative py-24 sm:py-28">
          <div className="dot-field pointer-events-none absolute bottom-0 left-0 h-44 w-56 opacity-15" />
          <span className="cross-mark pointer-events-none right-8 top-12 hidden opacity-50 sm:block" />
          <div className="grid gap-12 lg:grid-cols-[0.8fr_1.2fr] lg:gap-24">
            <div>
              <p className="text-xs font-semibold uppercase tracking-[0.18em] text-zinc-600">{t('workflow')}</p>
              <h2 className="mt-4 text-3xl font-semibold tracking-[-0.035em] text-white sm:text-4xl">
                From brief to<br />breakthrough.
              </h2>
              <p className="mt-5 max-w-sm text-sm leading-6 text-zinc-500">
                One simple path for finding the person who can move your work forward.
              </p>
            </div>
            <div className="divide-y divide-line border-y border-line">
              {steps.map(([number, title, description]) => (
                <div key={number} className="group grid gap-3 py-7 sm:grid-cols-[64px_1fr_24px] sm:items-center">
                  <span className="font-mono text-xs text-zinc-700">{number}</span>
                  <div>
                    <h3 className="font-medium text-zinc-200">{title}</h3>
                    <p className="mt-2 text-sm leading-6 text-zinc-500">{description}</p>
                  </div>
                  <ArrowRightIcon className="hidden size-4 text-zinc-700 transition-transform group-hover:translate-x-1 group-hover:text-zinc-400 sm:block" />
                </div>
              ))}
            </div>
          </div>
        </div>
      </section>

      <section className="page-shell relative py-24 sm:py-32">
        <div className="pointer-events-none absolute left-1/2 top-0 h-16 w-px bg-line" />
        <span className="cross-mark pointer-events-none left-[12%] top-16 hidden opacity-40 md:block" />
        <span className="cross-mark pointer-events-none bottom-14 right-[10%] hidden opacity-40 md:block" />
        <div className="relative overflow-hidden rounded-2xl border border-zinc-700 bg-panel px-7 py-14 text-center sm:px-12 sm:py-20">
          <div className="dot-field pointer-events-none absolute -left-10 -top-10 h-48 w-48 opacity-20" />
          <div className="dot-field pointer-events-none absolute -bottom-10 -right-10 h-48 w-48 opacity-20" />
          <div className="pointer-events-none absolute inset-0 grid grid-cols-6 opacity-40">
            {Array.from({ length: 6 }).map((_, index) => <span key={index} className="border-l border-line last:border-r" />)}
          </div>
          <div className="relative mx-auto max-w-2xl">
            <span className="mx-auto mb-6 block size-2 rounded-full bg-accent" />
            <h2 className="text-3xl font-semibold tracking-[-0.04em] text-white sm:text-5xl">
              {t('nextCollab')}
            </h2>
            <p className="mx-auto mt-5 max-w-lg text-sm leading-7 text-zinc-500">
              Join the marketplace built to keep talented people and meaningful work moving in the same direction.
            </p>
            <div className="mt-8 flex flex-col justify-center gap-3 sm:flex-row">
              <Link to="/register" className="btn-primary px-5 py-3">{t('createAccount')} <ArrowRightIcon /></Link>
              <Link to="/projects" className="btn-secondary px-5 py-3">{t('browseOpportunities')}</Link>
            </div>
          </div>
        </div>
      </section>
    </div>
  )
}
