import { useEffect, useState } from 'react'
import { Link, useNavigate } from 'react-router-dom'
import Alert from '../components/Alert'
import { useAuth } from '../context/auth'
import { apiRequest } from '../lib/api'
import { useLanguage } from '../context/language'

const initialForm = {
  username: '',
  email: '',
  password: '',
  confirm_password: '',
  role: 'freelancer',
  country: '',
}

export default function Register() {
  const navigate = useNavigate()
  const { login } = useAuth()
  const { t } = useLanguage()
  const [form, setForm] = useState(initialForm)
  const [error, setError] = useState('')
  const [loading, setLoading] = useState(false)
  const [countries, setCountries] = useState([])
  const [countriesState, setCountriesState] = useState({ loading: true, error: '' })

  useEffect(() => {
    const controller = new AbortController()
    async function loadCountries() {
      try {
        const response = await apiRequest('/common/countries/', { signal: controller.signal })
        setCountries(Array.isArray(response.data) ? response.data : [])
      } catch (requestError) {
        if (requestError.name !== 'AbortError') {
          setCountriesState({ loading: false, error: requestError.message })
        }
        return
      }
      setCountriesState({ loading: false, error: '' })
    }
    loadCountries()
    return () => controller.abort()
  }, [])

  function update(event) {
    setForm((current) => ({ ...current, [event.target.name]: event.target.value }))
  }

  async function submit(event) {
    event.preventDefault()
    setLoading(true)
    setError('')
    try {
      await apiRequest('/auth/register/', {
        method: 'POST',
        body: JSON.stringify({ ...form, country: Number(form.country) }),
      })
      await login(form.username, form.password)
      const verification = await apiRequest('/auth/send_code/')
      navigate('/verify-email', {
        replace: true,
        state: { destination: '/dashboard', codeSent: true, message: verification.message },
      })
    } catch (requestError) {
      setError(requestError.message)
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="page-shell flex items-center justify-center">
      <div className="reveal w-full max-w-xl">
        <div className="reveal reveal-delay-1 mb-8 text-center">
          <p className="text-xs font-semibold uppercase tracking-[0.16em] text-zinc-600">{t('join')}</p>
          <h1 className="mt-3 text-3xl font-semibold tracking-tight text-white">{t('registerTitle')}</h1>
          <p className="mt-3 text-sm text-zinc-500">{t('registerText')}</p>
        </div>
        <form onSubmit={submit} className="surface reveal reveal-delay-2 space-y-5 p-6 sm:p-8">
          {error && <Alert>{error}</Alert>}
          <div className="grid grid-cols-2 gap-2 rounded-xl border border-line bg-[#111] p-1.5">
            {['freelancer', 'client'].map((option) => (
              <button
                key={option}
                type="button"
                onClick={() => setForm((current) => ({ ...current, role: option }))}
                className={`rounded-lg px-3 py-2.5 text-sm font-medium capitalize transition ${form.role === option ? 'bg-zinc-100 text-zinc-950' : 'text-zinc-500 hover:text-zinc-300'}`}
              >
                {t(option)}
              </button>
            ))}
          </div>
          <div className="grid gap-5 sm:grid-cols-2">
            <label className="block">
              <span className="mb-2 block text-sm text-zinc-400">{t('username')}</span>
              <input className="field" name="username" value={form.username} onChange={update} required />
            </label>
            <label className="block">
              <span className="mb-2 block text-sm text-zinc-400">{t('email')}</span>
              <input className="field" type="email" name="email" value={form.email} onChange={update} required />
            </label>
          </div>
          <label className="block">
            <span className="mb-2 block text-sm text-zinc-400">{t('country')}</span>
            <select className="field" name="country" value={form.country} onChange={update} disabled={countriesState.loading || Boolean(countriesState.error)} required>
              <option value="">{countriesState.loading ? t('loadingCountries') : t('selectCountry')}</option>
              {countries.map((country) => <option key={country.id} value={country.id}>{country.name}</option>)}
            </select>
            {countriesState.error && <span className="mt-2 block text-xs text-red-400">{t('countriesError')} {countriesState.error}</span>}
          </label>
          <div className="grid gap-5 sm:grid-cols-2">
            <label className="block">
              <span className="mb-2 block text-sm text-zinc-400">{t('password')}</span>
              <input className="field" type="password" name="password" value={form.password} onChange={update} autoComplete="new-password" required />
            </label>
            <label className="block">
              <span className="mb-2 block text-sm text-zinc-400">{t('confirm')}</span>
              <input className="field" type="password" name="confirm_password" value={form.confirm_password} onChange={update} autoComplete="new-password" required />
            </label>
          </div>
          <button className="btn-primary w-full py-3" disabled={loading}>
            {loading ? t('creating') : t('create')}
          </button>
        </form>
        <p className="mt-6 text-center text-sm text-zinc-600">
          {t('existing')} <Link to="/login" className="text-zinc-300 hover:text-white">{t('login')}</Link>
        </p>
      </div>
    </div>
  )
}
