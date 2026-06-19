import { Outlet } from 'react-router-dom'
import Logo from './Logo'
import Navbar from './Navbar'
import { useLanguage } from '../context/language'

export default function Layout() {
  const { t } = useLanguage()
  return (
    <div className="flex min-h-screen flex-col bg-ink">
      <Navbar />
      <main className="flex-1"><Outlet /></main>
      <footer className="border-t border-line">
        <div className="mx-auto flex max-w-[1180px] flex-col gap-4 px-5 py-8 text-xs text-zinc-600 sm:flex-row sm:items-center sm:justify-between md:px-8">
          <Logo />
          <p>{t('footer')}</p>
        </div>
      </footer>
    </div>
  )
}
