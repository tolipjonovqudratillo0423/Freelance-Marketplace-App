import { Link } from 'react-router-dom'

export default function Logo() {
  return (
    <Link to="/" className="flex items-center gap-2.5 text-sm font-semibold tracking-tight text-white">
      <span className="grid size-7 place-items-center rounded-md bg-white text-xs font-black text-black">F</span>
      <span>Freeform</span>
    </Link>
  )
}
