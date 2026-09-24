import { Link } from 'react-router-dom'
import { lifeDates, statusLabel } from '../data'
import type { Artist } from '../types'

export default function ArtistCard({ artist }: { artist: Artist }) {
  const cover = artist.works[0]
  return (
    <Link to={`/artists/${artist.slug}`} className="card">
      <div className="card__image">
        {cover && <img src={cover.src} alt={`${cover.title} by ${artist.name}`} loading="lazy" />}
      </div>
      <h2 className="card__name">{artist.name}</h2>
      <p className="card__meta">
        {artist.nationality}, {lifeDates(artist)}
      </p>
      <p className="card__foot">
        <span>{artist.works.length} works</span>
        <span className={`status status--${artist.status}`}>{statusLabel[artist.status]}</span>
      </p>
    </Link>
  )
}
