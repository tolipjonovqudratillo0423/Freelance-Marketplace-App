import { createContext, useContext } from 'react'

export const AuthContext = createContext(null)

export function useAuth() {
  return useContext(AuthContext)
}

export function getNextRoute(user, fallback = '/dashboard') {
  if (!user?.is_verified) return '/verify-email'
  const bypass = localStorage.getItem('onboarding_done') === 'true' || localStorage.getItem('onboarding_skipped') === 'true'
  if (!user?.is_onboarded && !bypass) return '/onboarding'
  if (fallback !== '/dashboard') return fallback
  return user?.role ? `/dashboard/${user.role}` : '/projects'
}
