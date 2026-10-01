export type Embed =
  | { provider: 'youtube'; id: string; src: string; poster: string }
  | { provider: 'vimeo'; id: string; src: string; poster: null }

/** Turns a YouTube or Vimeo watch URL into an embeddable player; other hosts return null and are linked instead. */
export function toEmbed(url: string): Embed | null {
  let u: URL
  try {
    u = new URL(url)
  } catch {
    return null
  }
  const host = u.hostname.replace(/^www\.|^m\./, '')
  let yt: string | null = null
  if (host === 'youtu.be') yt = u.pathname.slice(1)
  else if (host === 'youtube.com' || host === 'youtube-nocookie.com') {
    yt = u.searchParams.get('v') ?? u.pathname.match(/^\/(?:embed|shorts|live)\/([\w-]+)/)?.[1] ?? null
  }
  if (yt && /^[\w-]{6,}$/.test(yt)) {
    return {
      provider: 'youtube',
      id: yt,
      src: `https://www.youtube-nocookie.com/embed/${yt}?autoplay=1&rel=0`,
      poster: `https://i.ytimg.com/vi/${yt}/hqdefault.jpg`,
    }
  }
  const vimeo = host.endsWith('vimeo.com') ? u.pathname.match(/(\d{6,})/)?.[1] : undefined
  if (vimeo) return { provider: 'vimeo', id: vimeo, src: `https://player.vimeo.com/video/${vimeo}?dnt=1`, poster: null }
  return null
}
