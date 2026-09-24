import type { Artist, ArtistFile } from './types'

// Every artist lives in its own folder: content/artists/<slug>/artist.json plus images.
// Adding a folder is all it takes; nothing else needs to be registered.
const files = import.meta.glob<ArtistFile>('/content/artists/*/artist.json', {
  eager: true,
  import: 'default',
})
const images = import.meta.glob<string>('/content/artists/*/*.{jpg,jpeg,png,webp,gif,avif}', {
  eager: true,
  query: '?url',
  import: 'default',
})

function imageUrl(slug: string, file: string): string {
  const src = images[`/content/artists/${slug}/${file}`]
  if (!src) throw new Error(`Missing image "${file}" for artist "${slug}"`)
  return src
}

export const artists: Artist[] = Object.entries(files)
  .map(([path, data]) => {
    const slug = path.split('/').at(-2)!
    return {
      ...data,
      slug,
      works: data.works.map((work) => ({ ...work, src: imageUrl(slug, work.file) })),
      portrait: data.portrait
        ? { src: imageUrl(slug, data.portrait.file), credit: data.portrait.credit }
        : null,
    }
  })
  .sort((a, b) => sortName(a.name).localeCompare(sortName(b.name)))

/** Museum-style alphabetisation by surname. */
export function sortName(name: string): string {
  const parts = name.trim().split(/\s+/)
  return parts.length > 1 ? `${parts.at(-1)} ${parts.slice(0, -1).join(' ')}` : name
}

export function findArtist(slug: string | undefined): Artist | undefined {
  return artists.find((a) => a.slug === slug)
}

export function lifeDates(artist: Pick<Artist, 'born' | 'died'>): string {
  return artist.died ? `${artist.born}–${artist.died}` : `born ${artist.born}`
}

export const statusLabel: Record<Artist['status'], string> = {
  'to-study': 'To study',
  studying: 'Studying',
  studied: 'Studied',
}
