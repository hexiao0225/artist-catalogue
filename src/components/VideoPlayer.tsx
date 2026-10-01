import { useState } from 'react'
import type { Video } from '../types'
import { toEmbed } from '../video'

interface Props {
  video: Video
  /** Load the player straight away instead of showing a poster first. */
  eager?: boolean
}

/** YouTube shows its poster until clicked (no player loads before that); Vimeo embeds lazily; other hosts become a link. */
export default function VideoPlayer({ video, eager = false }: Props) {
  const embed = toEmbed(video.url)
  const [playing, setPlaying] = useState(eager)
  const label = `${video.title}${video.year ? `, ${video.year}` : ''}`

  if (!embed) {
    return (
      <a className="video video--link" href={video.url}>
        <span className="video__play" aria-hidden="true" />
        <span className="video__watch">Watch on {video.source} ↗</span>
      </a>
    )
  }

  if (embed.provider === 'youtube' && !playing) {
    return (
      <button type="button" className="video video--poster" onClick={() => setPlaying(true)} aria-label={`Play ${label}`}>
        <img src={embed.poster} alt="" loading="lazy" />
        <span className="video__play" aria-hidden="true" />
      </button>
    )
  }

  return (
    <div className="video">
      <iframe
        src={embed.provider === 'youtube' && !eager ? embed.src : embed.src.replace('autoplay=1&', '')}
        title={label}
        loading="lazy"
        allow="autoplay; encrypted-media; picture-in-picture; fullscreen"
        allowFullScreen
      />
    </div>
  )
}
