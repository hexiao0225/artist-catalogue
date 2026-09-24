import { useMemo, useState } from 'react'
import { Link, useSearchParams } from 'react-router-dom'
import ArtistCard from '../components/ArtistCard'
import { artists, lifeDates, sortName, statusLabel } from '../data'
import type { Artist, StudyStatus } from '../types'

type View = 'grid' | 'index'
const FILTERS: Array<StudyStatus | 'all'> = ['all', 'to-study', 'studying', 'studied']

function matches(artist: Artist, query: string): boolean {
  if (!query) return true
  const haystack = [
    artist.name,
    artist.nativeName,
    artist.nationality,
    ...artist.tags,
    ...artist.mediums,
    ...artist.works.map((w) => w.title),
  ]
    .join(' ')
    .toLowerCase()
  return query
    .toLowerCase()
    .split(/\s+/)
    .every((term) => haystack.includes(term))
}

export default function IndexPage() {
  const [params, setParams] = useSearchParams()
  const [query, setQuery] = useState('')
  const view: View = params.get('view') === 'index' ? 'index' : 'grid'
  const filter = (params.get('status') as StudyStatus | null) ?? 'all'

  const update = (key: string, value: string, fallback: string) => {
    const next = new URLSearchParams(params)
    if (value === fallback) next.delete(key)
    else next.set(key, value)
    setParams(next, { replace: true })
  }

  const visible = useMemo(
    () => artists.filter((a) => (filter === 'all' || a.status === filter) && matches(a, query)),
    [filter, query],
  )
  const workCount = artists.reduce((n, a) => n + a.works.length, 0)

  return (
    <div className="wrap">
      <section className="page-intro">
        <h1 className="display">
          Artists<sup>{artists.length}</sup>
        </h1>
        <p className="lede">
          {artists.length} artists and {workCount} works, collected as a reference to learn from:
          how they handle surface, colour, composition and subject.
        </p>
      </section>

      <div className="toolbar" role="search">
        <input
          className="search"
          type="search"
          placeholder="Search artists, works, themes"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          aria-label="Search the catalogue"
        />
        <div className="segmented" aria-label="Filter by status">
          {FILTERS.map((f) => (
            <button
              key={f}
              type="button"
              aria-pressed={filter === f}
              onClick={() => update('status', f, 'all')}
            >
              {f === 'all' ? 'All' : statusLabel[f]}
            </button>
          ))}
        </div>
        <div className="segmented" aria-label="Layout">
          {(['grid', 'index'] as const).map((v) => (
            <button
              key={v}
              type="button"
              aria-pressed={view === v}
              onClick={() => update('view', v, 'grid')}
            >
              {v === 'grid' ? 'Grid' : 'A–Z'}
            </button>
          ))}
        </div>
      </div>

      {visible.length === 0 && <p className="empty">No artists match that search.</p>}

      {view === 'grid' ? (
        <div className="grid">
          {visible.map((a) => (
            <ArtistCard key={a.slug} artist={a} />
          ))}
        </div>
      ) : (
        <AlphaIndex artists={visible} />
      )}
    </div>
  )
}

function AlphaIndex({ artists: list }: { artists: Artist[] }) {
  const groups = new Map<string, Artist[]>()
  for (const a of list) {
    const letter = sortName(a.name)[0].toUpperCase()
    groups.set(letter, [...(groups.get(letter) ?? []), a])
  }
  return (
    <div className="alpha">
      {[...groups].map(([letter, group]) => (
        <section key={letter} className="alpha__group">
          <h2 className="alpha__letter">{letter}</h2>
          <ul>
            {group.map((a) => (
              <li key={a.slug}>
                <Link to={`/artists/${a.slug}`} className="alpha__row">
                  <span className="alpha__name">{a.name}</span>
                  <span className="alpha__meta">
                    {a.nationality}, {lifeDates(a)}
                  </span>
                  <span className="alpha__thumbs" aria-hidden="true">
                    {a.works.slice(0, 3).map((w) => (
                      <img key={w.file} src={w.src} alt="" loading="lazy" />
                    ))}
                  </span>
                </Link>
              </li>
            ))}
          </ul>
        </section>
      ))}
    </div>
  )
}
