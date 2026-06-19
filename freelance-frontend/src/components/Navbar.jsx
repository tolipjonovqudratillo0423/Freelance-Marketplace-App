import { useState } from 'react'
import { NavLink } from 'react-router-dom'
import { useAuth } from '../context/auth'
import { CloseIcon, MenuIcon } from './Icons'
import Logo from './Logo'
import LanguageSelect from './LanguageSelect'
import { useLanguage } from '../context/language'

function navClass({ isActive }) {
  return `rounded-lg px-3 py-2 text-sm transition ${
    isActive ? 'bg-white/6 text-white' : 'text-zinc-400 hover:text-white'
  }`
}

export default function Navbar() {
  const [open, setOpen] = useState(false)
  const { isAuthenticated, role, logout } = useAuth()
  const { t } = useLanguage()
  const dashboardPath = role ? `/dashboard/${role}` : '/dashboard'

  return (
    <header className="sticky top-0 z-50 border-b border-line bg-ink/95 backdrop-blur">
      <div className="mx-auto flex h-16 max-w-[1180px] items-center justify-between px-5 md:px-8">
        <Logo />
        <nav className="hidden items-center gap-1 md:flex">
          <NavLink to="/projects" className={navClass}>{t('browse')}</NavLink>
          {isAuthenticated && <NavLink to={dashboardPath} className={navClass}>{t('dashboard')}</NavLink>}
        </nav>
        <div className="hidden items-center gap-2 md:flex">
          <LanguageSelect />
          {isAuthenticated ? (
            <>
              {role && <span className="mr-2 text-xs capitalize text-zinc-600">{role}</span>}
              <button className="btn-secondary" onClick={logout}>{t('logout')}</button>
            </>
          ) : (
            <>
              <NavLink to="/login" className="btn-ghost">{t('login')}</NavLink>
              <NavLink to="/register" className="btn-primary">{t('started')}</NavLink>
            </>
          )}
        </div>
        <button
          className="grid size-9 place-items-center rounded-lg border border-line text-zinc-300 md:hidden"
          onClick={() => setOpen((value) => !value)}
          aria-label="Toggle menu"
        >
          {open ? <CloseIcon /> : <MenuIcon />}
        </button>
      </div>
      {open && (
        <div className="border-t border-line px-5 py-4 md:hidden">
          <nav className="flex flex-col gap-1" onClick={() => setOpen(false)}>
            <div className="mb-2"><LanguageSelect /></div>
            <NavLink to="/projects" className={navClass}>{t('browse')}</NavLink>
            {isAuthenticated && <NavLink to={dashboardPath} className={navClass}>{t('dashboard')}</NavLink>}
            {isAuthenticated ? (
              <button className="mt-2 btn-secondary" onClick={logout}>{t('logout')}</button>
            ) : (
              <div className="mt-2 grid grid-cols-2 gap-2">
                <NavLink to="/login" className="btn-secondary">{t('login')}</NavLink>
                <NavLink to="/register" className="btn-primary">{t('started')}</NavLink>
              </div>
            )}
          </nav>
        </div>
      )}
    </header>
  )
}
