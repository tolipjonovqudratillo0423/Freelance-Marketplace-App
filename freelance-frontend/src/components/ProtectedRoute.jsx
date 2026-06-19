import { Navigate, Outlet, useLocation } from 'react-router-dom'
import { useAuth } from '../context/auth'

export default function ProtectedRoute({ role }) {
  const { isAuthenticated, role: currentRole } = useAuth()
  const location = useLocation()

  if (!isAuthenticated) {
    return <Navigate to="/login" replace state={{ from: location.pathname }} />
  }
  if (role && currentRole && role !== currentRole) {
    return <Navigate to={`/dashboard/${currentRole}`} replace />
  }
  return <Outlet />
}
