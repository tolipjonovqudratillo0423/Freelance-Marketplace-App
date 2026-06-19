import { useState } from 'react'
import { apiRequest, decodeToken } from '../lib/api'
import { AuthContext } from './auth'

async function detectRole(accessToken) {
  const claims = decodeToken(accessToken)
  if (claims.role === 'client' || claims.role === 'freelancer') return claims.role

  try {
    await apiRequest('/client/projects/all')
    return 'client'
  } catch (error) {
    if (error.status === 401) throw error
  }

  try {
    await apiRequest('/freelancer/bid/')
    return 'freelancer'
  } catch (error) {
    if (error.status === 401) throw error
  }

  return ''
}

export function AuthProvider({ children }) {
  const [token, setToken] = useState(() => localStorage.getItem('access_token'))
  const [role, setRole] = useState(() => localStorage.getItem('user_role') || '')

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

    const resolvedRole = await detectRole(accessToken)
    if (resolvedRole) localStorage.setItem('user_role', resolvedRole)
    setRole(resolvedRole)
    return resolvedRole
  }

  async function refreshSession(tokens) {
    const accessToken = tokens?.access_token || token
    if (tokens?.access_token) {
      localStorage.setItem('access_token', tokens.access_token)
      setToken(tokens.access_token)
    }
    if (tokens?.refresh_token) localStorage.setItem('refresh_token', tokens.refresh_token)

    const resolvedRole = await detectRole(accessToken)
    if (resolvedRole) localStorage.setItem('user_role', resolvedRole)
    setRole(resolvedRole)
    return resolvedRole
  }

  function logout() {
    localStorage.removeItem('access_token')
    localStorage.removeItem('refresh_token')
    localStorage.removeItem('user_role')
    setToken(null)
    setRole('')
  }

  const value = { isAuthenticated: Boolean(token), token, role, login, logout, refreshSession }

  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>
}
