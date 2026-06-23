import { useEffect, useState } from 'react'
import { apiRequest } from '../lib/api'
import { AuthContext } from './auth'

export function AuthProvider({ children }) {
  const [token, setToken] = useState(() => localStorage.getItem('access_token'))
  const [role, setRole] = useState(() => localStorage.getItem('user_role') || '')
  const [user, setUser] = useState(null)

  useEffect(() => {
    if (token && !user) refreshUser().catch(() => logout())
  }, [token, user])

  async function refreshUser() {
    const response = await apiRequest('/auth/about-me/')
    const nextUser = response.data
    setUser(nextUser)
    if (nextUser?.role) {
      localStorage.setItem('user_role', nextUser.role)
      setRole(nextUser.role)
    }
    return nextUser
  }

  async function login(username, password) {
    const response = await apiRequest('/auth/login/', {
      method: 'POST',
      body: JSON.stringify({ username, password }),
    })
    const accessToken = response?.data?.access_token
    const refreshToken = response?.data?.refresh_token

    if (!accessToken) throw new Error('The API did not return an access token.')

    localStorage.setItem('access_token', accessToken)
    if (refreshToken) localStorage.setItem('refresh_token', refreshToken)
    setToken(accessToken)
    return await refreshUser()
  }

  async function refreshSession(tokens) {
    if (tokens?.access_token) {
      localStorage.setItem('access_token', tokens.access_token)
      setToken(tokens.access_token)
    }
    if (tokens?.refresh_token) localStorage.setItem('refresh_token', tokens.refresh_token)
    return await refreshUser()
  }

  function logout() {
    localStorage.removeItem('access_token')
    localStorage.removeItem('refresh_token')
    localStorage.removeItem('user_role')
    localStorage.removeItem('onboarding_done')
    localStorage.removeItem('onboarding_skipped')
    setToken(null)
    setRole('')
    setUser(null)
  }

  const value = { isAuthenticated: Boolean(token), token, role, user, login, logout, refreshSession, refreshUser }

  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>
}
