export const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://127.0.0.1:8000'

function flattenErrors(value) {
  if (!value) return ''
  if (typeof value === 'string') return value
  if (Array.isArray(value)) return value.map(flattenErrors).filter(Boolean).join(' ')
  if (typeof value === 'object') {
    return Object.entries(value)
      .map(([key, messages]) => {
        const text = flattenErrors(messages)
        return key === 'non_field_errors' ? text : `${key}: ${text}`
      })
      .filter(Boolean)
      .join(' ')
  }
  return String(value)
}

export class ApiError extends Error {
  constructor(message, status, data) {
    super(message)
    this.name = 'ApiError'
    this.status = status
    this.data = data
  }
}

export async function apiRequest(path, options = {}) {
  const token = localStorage.getItem('access_token')
  const url = path.startsWith('http') ? path : `${API_BASE_URL}${path}`
  const headers = new Headers(options.headers)

  if (options.body && !(options.body instanceof FormData)) {
    headers.set('Content-Type', 'application/json')
  }
  if (token) headers.set('Authorization', `Bearer ${token}`)

  let response
  try {
    response = await fetch(url, { ...options, headers })
  } catch (error) {
    if (error.name === 'AbortError') throw error
    throw new ApiError('Unable to reach the API. Make sure the backend is running on port 8000.', 0, null)
  }

  const contentType = response.headers.get('content-type') || ''
  const payload = contentType.includes('application/json') ? await response.json() : null

  if (!response.ok) {
    const message =
      payload?.message ||
      flattenErrors(payload) ||
      `Request failed with status ${response.status}.`
    throw new ApiError(message, response.status, payload?.data ?? payload)
  }

  return payload
}

export function getResults(payload) {
  const data = payload?.data
  if (Array.isArray(data)) return data
  if (Array.isArray(data?.results)) return data.results
  return []
}

export function decodeToken(token) {
  try {
    const payload = token.split('.')[1]
    const normalized = payload.replace(/-/g, '+').replace(/_/g, '/')
    return JSON.parse(decodeURIComponent(escape(atob(normalized))))
  } catch {
    return {}
  }
}
