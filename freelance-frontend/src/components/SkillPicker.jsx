import { useEffect, useMemo, useState } from 'react'
import { SearchIcon } from './Icons'
import { apiRequest } from '../lib/api'

export default function SkillPicker({ value = [], onChange, label = 'Skills' }) {
  const [skills, setSkills] = useState([])
  const [query, setQuery] = useState('')
  const [state, setState] = useState({ loading: true, error: '' })

  useEffect(() => {
    let active = true
    apiRequest('/common/skills/')
      .then((res) => {
        if (!active) return
        setSkills(Array.isArray(res.data) ? res.data : [])
        setState({ loading: false, error: '' })
      })
      .catch((error) => active && setState({ loading: false, error: error.message }))
    return () => { active = false }
  }, [])

  const selected = skills.filter((skill) => value.includes(skill.id))
  const filtered = useMemo(() => {
    const term = query.trim().toLowerCase()
    return skills
      .filter((skill) => !value.includes(skill.id))
      .filter((skill) => !term || skill.name.toLowerCase().includes(term))
      .slice(0, 10)
  }, [skills, query, value])
  const recommended = skills.filter((skill) => !value.includes(skill.id)).slice(0, 8)

  function add(id) {
    onChange([...value, id])
    setQuery('')
  }

  function remove(id) {
    onChange(value.filter((item) => item !== id))
  }

  return (
    <div>
      <span className="mb-2 block text-sm text-zinc-400">{label}</span>
      {state.error && <p className="mb-2 text-xs text-red-400">{state.error}</p>}

      <div className="rounded-2xl border border-line bg-[#101010] p-3 focus-within:border-zinc-600">
        <div className="mb-3 flex flex-wrap gap-2">
          {selected.map((skill) => (
            <button
              key={skill.id}
              type="button"
              onClick={() => remove(skill.id)}
              className="rounded-full border border-zinc-600 bg-zinc-100 px-3 py-1.5 text-xs font-medium text-zinc-950"
            >
              {skill.name} ×
            </button>
          ))}
          {!selected.length && <span className="px-1 py-1.5 text-xs text-zinc-700">No skills selected</span>}
        </div>

        <label className="relative block">
          <SearchIcon className="absolute left-3 top-1/2 size-4 -translate-y-1/2 text-zinc-600" />
          <input
            className="w-full rounded-xl border border-line bg-[#0c0c0c] py-3 pl-10 pr-3 text-sm text-zinc-200 outline-none placeholder:text-zinc-700"
            value={query}
            onChange={(event) => setQuery(event.target.value)}
            placeholder={state.loading ? 'Loading skills…' : 'Search skills'}
            disabled={state.loading}
          />
        </label>

        {(query ? filtered : recommended).length > 0 && (
          <div className="mt-4">
            <p className="mb-2 text-xs text-zinc-600">{query ? 'Search results' : 'Recommended skills'}</p>
            <div className="flex flex-wrap gap-2">
              {(query ? filtered : recommended).map((skill) => (
                <button
                  key={skill.id}
                  type="button"
                  onClick={() => add(skill.id)}
                  className="rounded-full border border-line bg-[#161616] px-3 py-2 text-xs text-zinc-400 transition hover:border-zinc-500 hover:text-white"
                >
                  + {skill.name}
                </button>
              ))}
            </div>
          </div>
        )}
      </div>
    </div>
  )
}
