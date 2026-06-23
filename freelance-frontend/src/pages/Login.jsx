import { useState } from 'react'
import { Link, Navigate, useLocation, useNavigate } from 'react-router-dom'
import Alert from '../components/Alert'
import { getNextRoute, useAuth } from '../context/auth'
import { apiRequest } from '../lib/api'
import { useLanguage } from '../context/language'

export default function Login() {
  const { isAuthenticated, login } = useAuth()
  const navigate = useNavigate()
  const location = useLocation()
  const [form, setForm] = useState({ username: '', password: '' })
  const [error, setError] = useState('')
  const [loading, setLoading] = useState(false)
  const { t } = useLanguage()

  if (isAuthenticated) return <Navigate to="/dashboard" replace />

  function update(event) {
    setForm((current) => ({ ...current, [event.target.name]: event.target.value }))
  }

  async function submit(event) {
    event.preventDefault()
    setLoading(true)
    setError('')
    try {
      const user = await login(form.username, form.password)
      const destination = location.state?.from || '/dashboard'
      if (!user.is_verified) {
        const verification = await apiRequest('/verification/send_code/', { method: 'POST' })
        navigate('/verify-email', {
          replace: true,
          state: { destination, codeSent: true, message: verification.message },
        })
      } else {
        navigate(getNextRoute(user, destination), { replace: true })
      }
    } catch (requestError) {
      setError(requestError.message)
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="page-shell flex min-h-[calc(100vh-129px)] items-center justify-center">
      <div className="reveal w-full max-w-md">
        <div className="reveal reveal-delay-1 mb-8 text-center">
          <p className="text-xs font-semibold uppercase tracking-[0.16em] text-zinc-600">{t('welcome')}</p>
          <h1 className="mt-3 text-3xl font-semibold tracking-tight text-white">{t('loginTitle')}</h1>
          <p className="mt-3 text-sm text-zinc-500">{t('loginText')}</p>
        </div>
        <form onSubmit={submit} className="surface reveal reveal-delay-2 space-y-5 p-6 sm:p-8">
          {error && <Alert>{error}</Alert>}
          <label className="block">
            <span className="mb-2 block text-sm text-zinc-400">{t('username')}</span>
            <input className="field" name="username" value={form.username} onChange={update} autoComplete="username" required />
          </label>
          <label className="block">
            <span className="mb-2 block text-sm text-zinc-400">{t('password')}</span>
            <input className="field" type="password" name="password" value={form.password} onChange={update} autoComplete="current-password" required />
          </label>
          <button className="btn-primary w-full py-3" disabled={loading}>
            {loading ? t('logging') : t('login')}
          </button>
        </form>
        <p className="mt-6 text-center text-sm text-zinc-600">
          {t('newHere')} <Link to="/register" className="text-zinc-300 hover:text-white">{t('createAccount')}</Link>
        </p>
      </div>
    </div>
  )
}
