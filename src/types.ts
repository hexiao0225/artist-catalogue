export type StudyStatus = 'to-study' | 'studying' | 'studied'

export interface Link {
  label: string
  url: string
}

export interface Work {
  title: string
  year: string
  medium: string
  dimensions?: string | null
  collection?: string | null
  /** Image filename inside the artist's folder. */
  file: string
  credit: string
  sourceUrl?: string | null
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
  status: StudyStatus
  addedOn: string
  links: Link[]
  portrait?: { file: string; credit: string } | null
  works: Work[]
}

export interface ResolvedWork extends Work {
  src: string
}

export interface Artist extends Omit<ArtistFile, 'works' | 'portrait'> {
  slug: string
  works: ResolvedWork[]
  portrait: { src: string; credit: string } | null
}
