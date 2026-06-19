import { useLanguage } from '../context/language'

export default function LanguageSelect() {
  const { language, setLanguage } = useLanguage()
  return (
    <select
      value={language}
      onChange={(event) => setLanguage(event.target.value)}
      className="rounded-lg border border-line bg-[#141414] px-2.5 py-2 text-xs text-zinc-400 outline-none"
      aria-label="Language"
    >
      <option value="en">EN</option>
      <option value="uz">UZ</option>
      <option value="ru">RU</option>
    </select>
  )
}
