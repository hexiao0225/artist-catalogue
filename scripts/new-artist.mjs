// Scaffolds a new artist folder.
// Usage: npm run new -- "Paula Rego"
import { mkdirSync, writeFileSync, existsSync } from 'node:fs'

const name = process.argv.slice(2).join(' ').trim()
if (!name) {
  console.error('Usage: npm run new -- "Artist Name"')
  process.exit(1)
}
const slug = name
  .normalize('NFD')
  .replace(/[̀-ͯ]/g, '')
  .toLowerCase()
  .replace(/[^a-z0-9]+/g, '-')
  .replace(/^-|-$/g, '')
const dir = new URL(`../content/artists/${slug}/`, import.meta.url)
if (existsSync(dir)) {
  console.error(`content/artists/${slug} already exists`)
  process.exit(1)
}
mkdirSync(dir, { recursive: true })

const template = {
  name,
  nativeName: null,
  born: 1900,
  died: null,
  birthplace: '',
  basedIn: '',
  nationality: '',
  mediums: ['Painting'],
  tags: [],
  bio: '',
  studyNotes: [],
  myNotes: [],
  recommendedBy: null,
  status: 'to-study',
  addedOn: new Date().toISOString().slice(0, 10),
  links: [{ label: 'Wikipedia', url: '' }],
  portrait: null,
  works: [
    {
      title: '',
      year: '',
      medium: 'Oil on canvas',
      dimensions: null,
      collection: null,
      file: '01-title.jpg',
      credit: '',
      sourceUrl: null,
    },
  ],
}
writeFileSync(new URL('artist.json', dir), JSON.stringify(template, null, 2) + '\n')
console.log(`Created content/artists/${slug}/artist.json — fill it in and drop the images next to it.`)
