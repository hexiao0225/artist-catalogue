export const REPO_URL = 'https://github.com/hexiao0225/artist-catalogue'

/** Broad categories used to group and filter the catalogue. An artist can belong to several. */
export const CATEGORIES: Array<{ id: string; title: string; blurb: string }> = [
  {
    id: 'painting',
    title: 'Painting',
    blurb: 'Surface, colour, composition and subject, worked out on canvas and paper.',
  },
  {
    id: 'bio-science',
    title: 'Bio & science',
    blurb: 'Living systems, labs, genetics and biomaterials as material and subject.',
  },
  {
    id: 'code',
    title: 'Code & computation',
    blurb: 'Rules, algorithms, software and data as the way the work gets made.',
  },
  {
    id: 'fibre',
    title: 'Thread & fabric',
    blurb: 'Fibre, weaving and soft structure at the scale of sculpture and architecture.',
  },
  {
    id: 'light',
    title: 'Light & perception',
    blurb: 'Light, colour and space as the material, with perception as the subject.',
  },
  {
    id: 'concept',
    title: 'Concept across media',
    blurb: 'One idea carried through performance, film, objects, photography and text.',
  },
]

export function categoryTitle(id: string): string {
  return CATEGORIES.find((c) => c.id === id)?.title ?? id
}
