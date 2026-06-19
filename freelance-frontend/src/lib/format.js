export function formatMoney(value) {
  const amount = Number(value)
  if (!Number.isFinite(amount)) return '$0'
  return new Intl.NumberFormat('en-US', {
    style: 'currency',
    currency: 'USD',
    maximumFractionDigits: amount % 1 ? 2 : 0,
  }).format(amount)
}

export function humanize(value = '') {
  return String(value)
    .replaceAll('_', ' ')
    .toLowerCase()
    .replace(/\b\w/g, (letter) => letter.toUpperCase())
}

export function projectName(project) {
  if (typeof project === 'string') {
    const marker = 'Project - '
    return project.includes(marker) ? project.split(marker)[1].replace(/\s*#$/, '') : project
  }
  return project?.title || 'Untitled project'
}
