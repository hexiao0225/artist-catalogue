import type { ResolvedWork, WorkKind } from '../types'

/** Ephemeral and time-based works get a tag, since the image is only documentation. */
const TAGGED: Partial<Record<WorkKind, string>> = { film: 'Film', performance: 'Performance', installation: 'Installation' }

interface Props {
  work: ResolvedWork
  artistName?: string
  compact?: boolean
}

/** A wall label: artist, title and date, then medium, size, collection and credit. */
export default function WorkLabel({ work, artistName, compact = false }: Props) {
  return (
    <div className={compact ? 'label label--compact' : 'label'}>
      {work.kind && TAGGED[work.kind] && <p className="kind">{TAGGED[work.kind]}</p>}
      {artistName && <p className="label__artist">{artistName}</p>}
      <p className="label__title">
        <cite>{work.title}</cite>, {work.year}
      </p>
      <p className="label__medium">{work.medium}</p>
      {!compact && work.note && <p className="label__note">{work.note}</p>}
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
