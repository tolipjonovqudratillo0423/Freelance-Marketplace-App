import { Navigate, Route, Routes } from 'react-router-dom'
import { useAuth } from './context/auth'
import Layout from './components/Layout'
import ProtectedRoute from './components/ProtectedRoute'
import ClientDashboard from './pages/ClientDashboard'
import FreelancerDashboard from './pages/FreelancerDashboard'
import Landing from './pages/Landing'
import Login from './pages/Login'
import ProjectDetail from './pages/ProjectDetail'
import Projects from './pages/Projects'
import Register from './pages/Register'
import VerifyEmail from './pages/VerifyEmail'

function RoleDashboard() {
  const { role } = useAuth()

  if (role === 'client') return <Navigate to="/dashboard/client" replace />
  if (role === 'freelancer') return <Navigate to="/dashboard/freelancer" replace />
  return <Navigate to="/projects" replace />
}

export default function App() {
  return (
    <Routes>
      <Route element={<Layout />}>
        <Route index element={<Landing />} />
        <Route path="login" element={<Login />} />
        <Route path="register" element={<Register />} />
        <Route path="projects" element={<Projects />} />
        <Route path="projects/:id" element={<ProjectDetail />} />
        <Route element={<ProtectedRoute />}>
          <Route path="verify-email" element={<VerifyEmail />} />
          <Route path="dashboard" element={<RoleDashboard />} />
          <Route element={<ProtectedRoute role="client" />}>
            <Route path="dashboard/client" element={<ClientDashboard />} />
          </Route>
          <Route element={<ProtectedRoute role="freelancer" />}>
            <Route path="dashboard/freelancer" element={<FreelancerDashboard />} />
          </Route>
        </Route>
        <Route path="*" element={<Navigate to="/" replace />} />
      </Route>
    </Routes>
  )
}
