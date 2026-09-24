import { Link, useParams } from 'react-router-dom'
import WorkLabel from '../components/WorkLabel'
import { artists, findArtist, lifeDates, statusLabel } from '../data'
import NotFound from './NotFound'

export default function ArtistPage() {
  const { slug } = useParams()
  const artist = findArtist(slug)
  if (!artist) return <NotFound />

  const i = artists.indexOf(artist)
  const prev = artists[(i - 1 + artists.length) % artists.length]
  const next = artists[(i + 1) % artists.length]
  const [hero, ...rest] = artist.works
  const slideHref = (n: number) => `/slides/${artist.slug}?i=${n + 1}`

  return (
    <article>
      <div className="wrap">
        <nav className="crumbs" aria-label="Breadcrumb">
          <Link to="/">Artists</Link> <span aria-hidden="true">/</span> {artist.name}
        </nav>
        <header className="artist-head">
          <h1 className="display display--artist">{artist.name}</h1>
          {artist.nativeName && <p className="artist-head__native">{artist.nativeName}</p>}
          <p className="artist-head__meta">
            {artist.nationality}, {lifeDates(artist)}
            {artist.birthplace && <> · Born {artist.birthplace}</>}
          </p>
          <div className="artist-head__actions">
            <Link to={`/slides/${artist.slug}`} className="button">
              View as slides <span aria-hidden="true">→</span>
            </Link>
            <span className={`status status--${artist.status}`}>{statusLabel[artist.status]}</span>
          </div>
        </header>
      </div>

      {hero && (
        <figure className="hero">
          <Link to={slideHref(0)} className="hero__frame" aria-label={`Open ${hero.title} full screen`}>
            <img src={hero.src} alt={`${hero.title} by ${artist.name}`} />
          </Link>
          <figcaption className="wrap">
            <WorkLabel work={hero} />
          </figcaption>
        </figure>
      )}

      <div className="wrap">
        <section className="section about">
          <h2 className="section__title">About the artist</h2>
          <div className="about__body">
            <p className="prose">{artist.bio}</p>
            <aside className="facts">
              {artist.portrait && (
                <figure className="facts__portrait">
                  <img src={artist.portrait.src} alt={`Portrait of ${artist.name}`} loading="lazy" />
                  <figcaption>{artist.portrait.credit}</figcaption>
                </figure>
              )}
              <dl>
                <dt>Born</dt>
                <dd>
                  {artist.born}
                  {artist.birthplace && `, ${artist.birthplace}`}
                </dd>
                {artist.died && (
                  <>
                    <dt>Died</dt>
                    <dd>{artist.died}</dd>
                  </>
                )}
                {artist.basedIn && (
                  <>
                    <dt>{artist.died ? 'Worked in' : 'Lives in'}</dt>
                    <dd>{artist.basedIn}</dd>
                  </>
                )}
                <dt>Media</dt>
                <dd>{artist.mediums.join(', ')}</dd>
                {artist.recommendedBy && (
                  <>
                    <dt>Recommended by</dt>
                    <dd>{artist.recommendedBy}</dd>
                  </>
                )}
                <dt>Added</dt>
                <dd>{artist.addedOn}</dd>
              </dl>
              <ul className="tags">
                {artist.tags.map((t) => (
                  <li key={t}>{t}</li>
                ))}
              </ul>
            </aside>
          </div>
        </section>

        {artist.studyNotes.length > 0 && (
          <section className="section">
            <h2 className="section__title">What to look at</h2>
            <ol className="notes">
              {artist.studyNotes.map((note) => (
                <li key={note}>{note}</li>
              ))}
            </ol>
          </section>
        )}

        {artist.myNotes && artist.myNotes.length > 0 && (
          <section className="section">
            <h2 className="section__title">My notes</h2>
            <ul className="notes notes--mine">
              {artist.myNotes.map((note) => (
                <li key={note}>{note}</li>
              ))}
            </ul>
          </section>
        )}

        {rest.length > 0 && (
          <section className="section">
            <h2 className="section__title">
              Works <span className="count">{artist.works.length}</span>
            </h2>
            <div className="works">
              {rest.map((work, n) => (
                <figure key={work.file} className="work">
                  <Link to={slideHref(n + 1)} aria-label={`Open ${work.title} full screen`}>
                    <img src={work.src} alt={`${work.title} by ${artist.name}`} loading="lazy" />
                  </Link>
                  <figcaption>
                    <WorkLabel work={work} />
                  </figcaption>
                </figure>
              ))}
            </div>
          </section>
        )}

        {artist.links.length > 0 && (
          <section className="section">
            <h2 className="section__title">Further looking</h2>
            <ul className="links">
              {artist.links.map((l) => (
                <li key={l.url}>
                  <a href={l.url}>
                    {l.label} <span aria-hidden="true">↗</span>
                  </a>
                </li>
              ))}
            </ul>
          </section>
        )}
      </div>

      {artists.length > 1 && (
        <nav className="pager" aria-label="More artists">
          <Link to={`/artists/${prev.slug}`} className="pager__link">
            <span className="pager__dir">← Previous</span>
            <span className="pager__name">{prev.name}</span>
          </Link>
          <Link to={`/artists/${next.slug}`} className="pager__link pager__link--next">
            <span className="pager__dir">Next →</span>
            <span className="pager__name">{next.name}</span>
          </Link>
        </nav>
      )}
    </article>
  )
}
