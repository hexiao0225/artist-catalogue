// Checks every content/artists/<slug>/artist.json before a build.
// Run with: npm run validate
import { readdirSync, readFileSync, existsSync, statSync } from 'node:fs'
import { join } from 'node:path'

const root = new URL('../content/artists/', import.meta.url).pathname
const STATUSES = ['to-study', 'studying', 'studied']
const KINDS = ['painting', 'sculpture', 'drawing', 'photograph', 'performance', 'film', 'installation']
const errors = []

for (const slug of readdirSync(root)) {
  const dir = join(root, slug)
  if (!statSync(dir).isDirectory()) continue
  const where = `content/artists/${slug}/artist.json`
  if (!/^[a-z0-9]+(-[a-z0-9]+)*$/.test(slug)) errors.push(`${slug}: folder name must be kebab-case`)
  if (!existsSync(join(dir, 'artist.json'))) {
    errors.push(`${where}: missing`)
    continue
  }
  let a
  try {
    a = JSON.parse(readFileSync(join(dir, 'artist.json'), 'utf8'))
  } catch (e) {
    errors.push(`${where}: invalid JSON (${e.message})`)
    continue
  }
  const need = (cond, msg) => cond || errors.push(`${where}: ${msg}`)
  need(typeof a.name === 'string' && a.name, '"name" is required')
  need(Number.isInteger(a.born), '"born" must be a year number')
  need(a.died == null || Number.isInteger(a.died), '"died" must be a year number or null')
  need(typeof a.nationality === 'string', '"nationality" is required')
  need(typeof a.bio === 'string', '"bio" is required')
  need(STATUSES.includes(a.status), `"status" must be one of ${STATUSES.join(', ')}`)
  need(/^\d{4}-\d{2}-\d{2}$/.test(a.addedOn ?? ''), '"addedOn" must be YYYY-MM-DD')
  for (const key of ['mediums', 'tags', 'studyNotes', 'links', 'works']) {
    need(Array.isArray(a[key]), `"${key}" must be a list`)
  }
  const files = [...(a.works ?? []).map((w) => w.file), a.portrait?.file].filter(Boolean)
  for (const f of files) need(existsSync(join(dir, f)), `image "${f}" not found in the folder`)
  ;(a.works ?? []).forEach((w, i) => {
    for (const key of ['title', 'year', 'medium', 'file', 'credit']) {
      need(typeof w[key] === 'string' && w[key], `works[${i}] needs "${key}"`)
    }
    need(w.kind == null || KINDS.includes(w.kind), `works[${i}].kind must be one of ${KINDS.join(', ')}`)
  })
  need(a.videos == null || Array.isArray(a.videos), '"videos" must be a list')
  ;(a.videos ?? []).forEach((v, i) => {
    need(typeof v.title === 'string' && v.title, `videos[${i}] needs "title"`)
    need(typeof v.source === 'string' && v.source, `videos[${i}] needs "source"`)
    need(/^https?:\/\//.test(v.url ?? ''), `videos[${i}].url must be a web address`)
  })
  if (a.seenAt != null) {
    need(typeof a.seenAt.title === 'string' && typeof a.seenAt.venue === 'string', '"seenAt" needs "title" and "venue"')
  }
}

if (errors.length) {
  console.error(`✗ ${errors.length} problem(s) in the catalogue:\n  ` + errors.join('\n  '))
  process.exit(1)
}
console.log('✓ catalogue content is valid')
