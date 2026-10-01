export type StudyStatus = 'to-study' | 'studying' | 'studied'

export interface Link {
  label: string
  url: string
}

export type WorkKind = 'painting' | 'sculpture' | 'drawing' | 'photograph' | 'performance' | 'film' | 'installation'

export interface Work {
  title: string
  /** What kind of work it is; film and performance get a tag on the label. */
  kind?: WorkKind | null
  year: string
  medium: string
  /** What happened, for performances and films where the image is only a trace. */
  note?: string | null
  dimensions?: string | null
  collection?: string | null
  /** Image filename inside the artist's folder. */
  file: string
  credit: string
  sourceUrl?: string | null
}

/** A film by or about the artist. YouTube and Vimeo links play inline; anything else is linked. */
export interface Video {
  title: string
  year?: string | null
  /** Who published it, e.g. "Tate". */
  source: string
  url: string
}

/** Where you saw the work in person. */
export interface Viewing {
  title: string
  venue: string
  dates?: string | null
  url?: string | null
}

/** Shape of content/artists/<slug>/artist.json */
export interface ArtistFile {
  name: string
  nativeName?: string | null
  born: number
  died?: number | null
  birthplace?: string | null
  basedIn?: string | null
  nationality: string
  mediums: string[]
  tags: string[]
  bio: string
  studyNotes: string[]
  /** Your own notes: what you took away, what to try next. */
  myNotes?: string[]
  recommendedBy?: string | null
  seenAt?: Viewing | null
  status: StudyStatus
  addedOn: string
  links: Link[]
  portrait?: { file: string; credit: string } | null
  videos?: Video[]
  works: Work[]
}

export interface ResolvedWork extends Work {
  src: string
}

export interface Artist extends Omit<ArtistFile, 'works' | 'portrait' | 'videos'> {
  slug: string
  videos: Video[]
  works: ResolvedWork[]
  portrait: { src: string; credit: string } | null
}
