import { useCallback, useEffect, useMemo, useRef } from 'react'
import { Link, useNavigate, useParams, useSearchParams } from 'react-router-dom'
import WorkLabel from '../components/WorkLabel'
import { artists, findArtist, lifeDates } from '../data'
import type { Artist, ResolvedWork } from '../types'

type Slide =
  | { kind: 'title'; artist: Artist }
  | { kind: 'work'; artist: Artist; work: ResolvedWork; n: number }

function buildSlides(list: Artist[]): Slide[] {
  return list.flatMap((artist) => [
    { kind: 'title' as const, artist },
    ...artist.works.map((work, n) => ({ kind: 'work' as const, artist, work, n })),
  ])
}

/** First two sentences of the bio, for the title slide. */
function summary(bio: string): string {
  return bio.match(/[^.!?]+[.!?]+/g)?.slice(0, 2).join('').trim() ?? bio
}

export default function SlidesPage() {
  const { slug } = useParams()
  const [params, setParams] = useSearchParams()
  const navigate = useNavigate()
  const single = findArtist(slug)

  const slides = useMemo(() => buildSlides(single ? [single] : artists), [single])
  const total = slides.length
  const raw = Number(params.get('i') ?? 0)
  const index = Number.isInteger(raw) ? Math.min(Math.max(raw, 0), total - 1) : 0
  const slide = slides[index]
  const closeHref = single ? `/artists/${single.slug}` : '/'

  const go = useCallback(
    (to: number) => {
      const clamped = Math.min(Math.max(to, 0), total - 1)
      setParams(clamped ? { i: String(clamped) } : {}, { replace: true })
    },
    [setParams, total],
  )

  useEffect(() => {
    const onKey = (e: KeyboardEvent) => {
      if (e.target instanceof HTMLSelectElement) return
      if (['ArrowRight', 'PageDown', ' '].includes(e.key)) go(index + 1)
      else if (['ArrowLeft', 'PageUp'].includes(e.key)) go(index - 1)
      else if (e.key === 'Home') go(0)
      else if (e.key === 'End') go(total - 1)
      else if (e.key === 'Escape') navigate(closeHref)
      else return
      e.preventDefault()
    }
    window.addEventListener('keydown', onKey)
    return () => window.removeEventListener('keydown', onKey)
  }, [go, index, total, navigate, closeHref])

  // Preload the next image so advancing feels instant.
  useEffect(() => {
    const upcoming = slides[index + 1]
    if (upcoming?.kind === 'work') new Image().src = upcoming.work.src
  }, [slides, index])

  const touchX = useRef<number | null>(null)
  const onTouchEnd = (e: React.TouchEvent) => {
    if (touchX.current === null) return
    const dx = e.changedTouches[0].clientX - touchX.current
    if (Math.abs(dx) > 50) go(index + (dx < 0 ? 1 : -1))
    touchX.current = null
  }

  if (!slide) return null
  const titleIndex = (a: Artist) => slides.findIndex((s) => s.kind === 'title' && s.artist === a)

  return (
    <div
      className="deck"
      onTouchStart={(e) => (touchX.current = e.touches[0].clientX)}
      onTouchEnd={onTouchEnd}
    >
      <div className="deck__progress" style={{ transform: `scaleX(${(index + 1) / total})` }} />

      <div className="deck__bar">
        <Link to={closeHref} className="deck__close">
          <span aria-hidden="true">×</span> Close
        </Link>
        {!single && artists.length > 1 && (
          <select
            className="deck__jump"
            aria-label="Jump to artist"
            value={slide.artist.slug}
            onChange={(e) => go(titleIndex(findArtist(e.target.value)!))}
          >
            {artists.map((a) => (
              <option key={a.slug} value={a.slug}>
                {a.name}
              </option>
            ))}
          </select>
        )}
        <span className="deck__count">
          {index + 1} / {total}
        </span>
      </div>

      {slide.kind === 'title' ? (
        <section className="deck__title" key={`t-${slide.artist.slug}`}>
          <p className="deck__eyebrow">
            {slide.artist.nationality}, {lifeDates(slide.artist)}
          </p>
          <h1 className="deck__name">{slide.artist.name}</h1>
          {slide.artist.nativeName && <p className="deck__native">{slide.artist.nativeName}</p>}
          <p className="deck__summary">{summary(slide.artist.bio)}</p>
          <p className="deck__eyebrow">{slide.artist.works.length} works</p>
        </section>
      ) : (
        <section className="deck__work" key={`w-${slide.artist.slug}-${slide.n}`}>
          <div className="deck__image">
            <img src={slide.work.src} alt={`${slide.work.title} by ${slide.artist.name}`} />
          </div>
          <div className="deck__label">
            <WorkLabel work={slide.work} artistName={slide.artist.name} />
            <p className="deck__index">
              {slide.n + 1} of {slide.artist.works.length}
            </p>
          </div>
        </section>
      )}

      <button
        type="button"
        className="deck__nav deck__nav--prev"
        onClick={() => go(index - 1)}
        disabled={index === 0}
        aria-label="Previous slide"
      />
      <button
        type="button"
        className="deck__nav deck__nav--next"
        onClick={() => go(index + 1)}
        disabled={index === total - 1}
        aria-label="Next slide"
      />
    </div>
  )
}
