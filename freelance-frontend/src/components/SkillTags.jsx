export default function SkillTags({ skills = [], limit }) {
  const items = limit ? skills.slice(0, limit) : skills

  return (
    <div className="flex flex-wrap gap-1.5">
      {items.map((skill) => (
        <span key={typeof skill === 'object' ? skill.id || skill.name : skill} className="rounded-md border border-line bg-[#111] px-2 py-1 text-xs text-zinc-400">
          {typeof skill === 'object' ? skill.name : skill}
        </span>
      ))}
      {limit && skills.length > limit && <span className="px-1 py-1 text-xs text-zinc-600">+{skills.length - limit}</span>}
    </div>
  )
}
