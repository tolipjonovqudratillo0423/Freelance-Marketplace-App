import { useEffect, useRef, useState } from 'react'
import { useLocation, useNavigate } from 'react-router-dom'
import Alert from '../components/Alert'
import { CheckIcon } from '../components/Icons'
import { getNextRoute, useAuth } from '../context/auth'
import { apiRequest } from '../lib/api'
import { useLanguage } from '../context/language'

export default function VerifyEmail() {
  const navigate = useNavigate()
  const location = useLocation()
  const { refreshSession } = useAuth()
  const { t } = useLanguage()
  const codeRequested = useRef(false)
  const [code, setCode] = useState('')
  const [state, setState] = useState({
    loading: false,
    message: location.state?.message || '',
    error: '',
    alreadyVerified: false,
  })

  async function sendCode() {
    setState((current) => ({ ...current, loading: true, error: '' }))
    try {
      const response = await apiRequest('/verification/send_code/', { method: 'POST' })
      const alreadyVerified = response.message?.toLowerCase().includes('already verified')
      setState({ loading: false, message: response.message, error: '', alreadyVerified })
    } catch (error) {
      setState((current) => ({ ...current, loading: false, error: error.message }))
    }
  }

  useEffect(() => {
    if (location.state?.codeSent) return
    if (codeRequested.current) return
    codeRequested.current = true
    sendCode()
  }, [location.state?.codeSent])

  async function continueToApp(tokens) {
    const user = await refreshSession(tokens)
    navigate(getNextRoute(user, location.state?.destination || '/dashboard'), { replace: true })
  }

  async function verify(event) {
    event.preventDefault()
    setState((current) => ({ ...current, loading: true, error: '' }))
    try {
      const response = await apiRequest('/verification/verify_code/', {
        method: 'POST',
        body: JSON.stringify({ code }),
      })
      await continueToApp(response.data)
    } catch (error) {
      setState((current) => ({ ...current, loading: false, error: error.message }))
    }
  }

  return (
    <div className="page-shell flex min-h-[calc(100vh-129px)] items-center justify-center">
      <div className="reveal w-full max-w-md">
        <div className="reveal reveal-delay-1 mb-8 text-center">
          <span className="float-slow mx-auto grid size-12 place-items-center rounded-2xl border border-line bg-panel text-accent">
            <CheckIcon className="size-5" />
          </span>
          <h1 className="mt-5 text-3xl font-semibold tracking-tight text-white">{t('verifyTitle')}</h1>
          <p className="mt-3 text-sm leading-6 text-zinc-500">{t('verifyText')}</p>
        </div>

        <form onSubmit={verify} className="surface reveal reveal-delay-2 space-y-5 p-6 sm:p-8">
          {state.error && <Alert>{state.error}</Alert>}
          {state.message && <Alert tone="success">{state.message}</Alert>}

          {!state.alreadyVerified && (
            <>
              <input
                className="field text-center font-mono text-2xl tracking-[0.5em]"
                value={code}
                onChange={(event) => setCode(event.target.value.replace(/\D/g, '').slice(0, 6))}
                inputMode="numeric"
                placeholder="000000"
                autoFocus
                required
              />
              <button className="btn-primary w-full py-3" disabled={state.loading || code.length !== 6}>
                {state.loading ? t('verifying') : t('verify')}
              </button>
            </>
          )}

          {state.alreadyVerified && (
            <button type="button" className="btn-primary w-full py-3" onClick={() => continueToApp()}>
              {t('continue')}
            </button>
          )}

          <button type="button" className="btn-ghost w-full" onClick={sendCode} disabled={state.loading}>
            {t('resend')}
          </button>
        </form>
      </div>
    </div>
  )
}
