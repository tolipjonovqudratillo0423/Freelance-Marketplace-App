import { useState } from 'react'
import Alert from './Alert'
import { apiRequest } from '../lib/api'
import { useLanguage } from '../context/language'

const initialForm = {
  title: '',
  description: '',
  min_price: '',
  max_price: '',
  required_skills: '',
}

export default function CreateProjectForm({ onCreated, onCancel }) {
  const [form, setForm] = useState(initialForm)
  const [state, setState] = useState({ loading: false, error: '' })
  const { t } = useLanguage()

  function update(event) {
    setForm((current) => ({ ...current, [event.target.name]: event.target.value }))
  }

  async function submit(event) {
    event.preventDefault()
    setState({ loading: true, error: '' })
    const skills = form.required_skills
      .split(',')
      .map((value) => Number(value.trim()))
      .filter(Number.isInteger)

    try {
      await apiRequest('/client/projects/create', {
        method: 'POST',
        body: JSON.stringify({
          title: form.title,
          description: form.description,
          min_price: Number(form.min_price),
          max_price: Number(form.max_price),
          required_skills: skills,
        }),
      })
      setForm(initialForm)
      onCreated?.()
    } catch (error) {
      setState({ loading: false, error: error.message })
    }
  }

  return (
    <form onSubmit={submit} className="surface mb-6 space-y-5 p-6 sm:p-8">
      <div className="flex items-start justify-between">
        <div>
          <h2 className="text-lg font-semibold text-white">{t('createProject')}</h2>
          <p className="mt-1 text-sm text-zinc-600">{t('createIntro')}</p>
        </div>
        <button type="button" onClick={onCancel} className="btn-ghost -mr-2 -mt-2">{t('close')}</button>
      </div>
      {state.error && <Alert>{state.error}</Alert>}
      <label className="block">
        <span className="mb-2 block text-sm text-zinc-400">{t('projectTitle')}</span>
        <input className="field" name="title" value={form.title} onChange={update} placeholder={t('projectTitleExample')} required />
      </label>
      <label className="block">
        <span className="mb-2 block text-sm text-zinc-400">{t('description')}</span>
        <textarea className="field min-h-36 resize-y" name="description" value={form.description} onChange={update} placeholder={t('descriptionPlaceholder')} required />
      </label>
      <div className="grid gap-5 sm:grid-cols-2">
        <label className="block">
          <span className="mb-2 block text-sm text-zinc-400">{t('minBudget')}</span>
          <input className="field" type="number" min="0" step="0.01" name="min_price" value={form.min_price} onChange={update} required />
        </label>
        <label className="block">
          <span className="mb-2 block text-sm text-zinc-400">{t('maxBudget')}</span>
          <input className="field" type="number" min="0" step="0.01" name="max_price" value={form.max_price} onChange={update} required />
        </label>
      </div>
      <label className="block">
        <span className="mb-2 block text-sm text-zinc-400">{t('skillIds')}</span>
        <input className="field" name="required_skills" value={form.required_skills} onChange={update} placeholder="1, 4, 7" />
        <span className="mt-2 block text-xs text-zinc-700">{t('skillIdsHint')}</span>
      </label>
      <button className="btn-primary" disabled={state.loading}>{state.loading ? t('publishing') : t('publish')}</button>
    </form>
  )
}
