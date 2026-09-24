import type { ResolvedWork } from '../types'

interface Props {
  work: ResolvedWork
  artistName?: string
  compact?: boolean
}

/** A wall label: artist, title and date, then medium, size, collection and credit. */
export default function WorkLabel({ work, artistName, compact = false }: Props) {
  return (
    <div className={compact ? 'label label--compact' : 'label'}>
      {artistName && <p className="label__artist">{artistName}</p>}
      <p className="label__title">
        <cite>{work.title}</cite>, {work.year}
      </p>
      <p className="label__medium">{work.medium}</p>
      {!compact && work.dimensions && <p className="label__meta">{work.dimensions}</p>}
      {!compact && work.collection && <p className="label__meta">{work.collection}</p>}
      {!compact && (
        <p className="label__credit">
          {work.sourceUrl ? <a href={work.sourceUrl}>{work.credit}</a> : work.credit}
        </p>
      )}
    </div>
  )
}
