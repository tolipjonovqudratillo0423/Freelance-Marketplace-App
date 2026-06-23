import { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import Alert from '../components/Alert'
import SkillPicker from '../components/SkillPicker'
import { getNextRoute, useAuth } from '../context/auth'
import { apiRequest } from '../lib/api'

const profileInitial = { bio: '', phone: '', image: null }
const freelancerInitial = { skills: [], hourly_rate: '', resume: null }
const educationInitial = { level: 'bachelor', name: '', faculty: '', specialization: '', end_year: '' }
const experienceInitial = { company: '', position: '', start_date: '', end_date: '', details: '' }

function hasAnyValue(obj) {
  return Object.values(obj).some(Boolean)
}

export default function Onboarding() {
  const navigate = useNavigate()
  const { user, role, refreshUser } = useAuth()
  const currentRole = user?.role || role
  const [profile, setProfile] = useState(profileInitial)
  const [freelancer, setFreelancer] = useState(freelancerInitial)
  const [education, setEducation] = useState(educationInitial)
  const [experience, setExperience] = useState(experienceInitial)
  const [state, setState] = useState({ loading: false, error: '' })

  function update(setter) {
    return (event) => setter((current) => ({ ...current, [event.target.name]: event.target.value }))
  }

  function fileUpdate(setter) {
    return (event) => setter((current) => ({ ...current, [event.target.name]: event.target.files?.[0] || null }))
  }

  async function finish(skip = false) {
    if (skip) {
      localStorage.setItem('onboarding_skipped', 'true')
      navigate(getNextRoute({ ...user, is_onboarded: true }), { replace: true })
      return
    }

    setState({ loading: true, error: '' })
    try {
      const profileData = new FormData()
      profileData.append('bio', profile.bio)
      profileData.append('phone', profile.phone)
      if (profile.image) profileData.append('image', profile.image)
      await apiRequest('/onboard/profile/', { method: 'POST', body: profileData })

      if (currentRole === 'freelancer') {
        const freelancerData = new FormData()
        freelancer.skills.forEach((id) => freelancerData.append('skills', id))
        freelancerData.append('hourly_rate', freelancer.hourly_rate || 0)
        if (freelancer.resume) freelancerData.append('resume', freelancer.resume)
        await apiRequest('/onboard/freelancer-profile/', {
          method: 'POST',
          body: freelancerData,
        })
        if (hasAnyValue({ ...education, level: '' })) {
          await apiRequest('/onboard/education/', {
            method: 'POST',
            body: JSON.stringify({ ...education, end_year: Number(education.end_year) }),
          })
        }
        if (hasAnyValue(experience)) {
          await apiRequest('/onboard/experience/', { method: 'POST', body: JSON.stringify(experience) })
        }
      }

      localStorage.setItem('onboarding_done', 'true')
      const nextUser = await refreshUser()
      navigate(getNextRoute({ ...nextUser, is_onboarded: true }), { replace: true })
    } catch (error) {
      setState({ loading: false, error: error.message })
    }
  }

  return (
    <div className="page-shell">
      <div className="mx-auto max-w-3xl">
        <div className="mb-8">
          <p className="text-xs font-semibold uppercase tracking-[0.16em] text-zinc-600">Onboarding</p>
          <h1 className="mt-3 text-3xl font-semibold tracking-tight text-white">Complete your profile</h1>
          <p className="mt-3 text-sm text-zinc-500">Fill the basics now or skip and return later.</p>
        </div>

        <div className="surface space-y-7 p-6 sm:p-8">
          {state.error && <Alert>{state.error}</Alert>}

          <section className="space-y-4">
            <h2 className="font-semibold text-zinc-200">Basic profile</h2>
            <label className="block">
              <span className="mb-2 block text-sm text-zinc-400">Bio</span>
              <textarea className="field min-h-28" name="bio" value={profile.bio} onChange={update(setProfile)} required />
            </label>
            <label className="block">
              <span className="mb-2 block text-sm text-zinc-400">Phone</span>
              <input className="field" name="phone" value={profile.phone} onChange={update(setProfile)} placeholder="+998901234567" required />
            </label>
            <label className="block rounded-2xl border border-line bg-[#101010] p-4">
              <span className="mb-2 block text-sm text-zinc-400">Profile image</span>
              <input className="block w-full text-sm text-zinc-500 file:mr-4 file:rounded-full file:border-0 file:bg-zinc-100 file:px-4 file:py-2 file:text-sm file:font-medium file:text-zinc-950" type="file" name="image" accept="image/*" onChange={fileUpdate(setProfile)} />
              {profile.image && <span className="mt-2 block text-xs text-zinc-600">{profile.image.name}</span>}
            </label>
          </section>

          {currentRole === 'freelancer' && (
            <>
              <section className="space-y-4 border-t border-line pt-7">
                <h2 className="font-semibold text-zinc-200">Freelancer profile</h2>
                <SkillPicker value={freelancer.skills} onChange={(ids) => setFreelancer((current) => ({ ...current, skills: ids }))} />
                <label className="block">
                  <span className="mb-2 block text-sm text-zinc-400">Hourly rate</span>
                  <input className="field" type="number" min="0" step="0.01" name="hourly_rate" value={freelancer.hourly_rate} onChange={update(setFreelancer)} />
                </label>
                <label className="block rounded-2xl border border-line bg-[#101010] p-4">
                  <span className="mb-2 block text-sm text-zinc-400">Resume file</span>
                  <input className="block w-full text-sm text-zinc-500 file:mr-4 file:rounded-full file:border-0 file:bg-zinc-100 file:px-4 file:py-2 file:text-sm file:font-medium file:text-zinc-950" type="file" name="resume" accept=".pdf,.doc,.docx" onChange={fileUpdate(setFreelancer)} />
                  {freelancer.resume && <span className="mt-2 block text-xs text-zinc-600">{freelancer.resume.name}</span>}
                </label>
              </section>

              <section className="space-y-4 border-t border-line pt-7">
                <h2 className="font-semibold text-zinc-200">Education optional</h2>
                <div className="grid gap-4 sm:grid-cols-2">
                  <select className="field" name="level" value={education.level} onChange={update(setEducation)}>
                    <option value="bachelor">Bachelor</option>
                    <option value="master">Master</option>
                    <option value="phd">PhD</option>
                  </select>
                  <input className="field" name="end_year" value={education.end_year} onChange={update(setEducation)} placeholder="End year" />
                  <input className="field" name="name" value={education.name} onChange={update(setEducation)} placeholder="University" />
                  <input className="field" name="faculty" value={education.faculty} onChange={update(setEducation)} placeholder="Faculty" />
                </div>
                <input className="field" name="specialization" value={education.specialization} onChange={update(setEducation)} placeholder="Specialization" />
              </section>

              <section className="space-y-4 border-t border-line pt-7">
                <h2 className="font-semibold text-zinc-200">Experience optional</h2>
                <div className="grid gap-4 sm:grid-cols-2">
                  <input className="field" name="company" value={experience.company} onChange={update(setExperience)} placeholder="Company" />
                  <input className="field" name="position" value={experience.position} onChange={update(setExperience)} placeholder="Position" />
                  <input className="field" type="date" name="start_date" value={experience.start_date} onChange={update(setExperience)} />
                  <input className="field" type="date" name="end_date" value={experience.end_date} onChange={update(setExperience)} />
                </div>
                <textarea className="field min-h-24" name="details" value={experience.details} onChange={update(setExperience)} placeholder="Details" />
              </section>
            </>
          )}

          <div className="flex flex-col gap-3 border-t border-line pt-7 sm:flex-row">
            <button className="btn-primary" onClick={() => finish(false)} disabled={state.loading}>
              {state.loading ? 'Saving…' : 'Finish onboarding'}
            </button>
            <button className="btn-secondary" onClick={() => finish(true)} disabled={state.loading}>Skip for now</button>
          </div>
        </div>
      </div>
    </div>
  )
}
