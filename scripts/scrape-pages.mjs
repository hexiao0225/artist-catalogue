// Round 3: fetch pages, pull out every large image with its alt text; also download listed direct URLs.
import { mkdirSync, writeFileSync, readFileSync } from 'node:fs'
const UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128 Safari/537.36'
const cfg = JSON.parse(readFileSync('scripts/pages.json', 'utf8'))
const sleep = (ms) => new Promise((r) => setTimeout(r, ms))
const dec = (s) => s.replace(/&amp;/g, '&').replace(/&quot;/g, '"').replace(/&#0?39;/g, "'")
const skip = /(logo|icon|favicon|sprite|avatar|placeholder|blank|pixel|spacer|badge|\.svg|\.gif)/i
async function get(url, asBuf = false) {
  const r = await fetch(url, { headers: { 'User-Agent': UA, 'Accept-Language': 'en-US,en', Accept: asBuf ? 'image/avif,image/webp,image/*,*/*' : 'text/html,*/*' }, redirect: 'follow', signal: AbortSignal.timeout(20000) })
  if (!r.ok) throw new Error(String(r.status))
  return asBuf ? { buf: Buffer.from(await r.arrayBuffer()), ct: r.headers.get('content-type') ?? '' } : await r.text()
}
const log = {}
for (const [slug, entry] of Object.entries(cfg)) {
  const dir = `discovery3/${slug}`; mkdirSync(dir, { recursive: true })
  const cands = []
  for (const d of entry.direct ?? []) cands.push({ src: d.url, alt: d.title, page: d.page ?? d.url })
  for (const page of entry.pages ?? []) {
    let html = ''
    try { html = await get(page) } catch (e) { log[page] = 'ERR ' + e.message; continue }
    const ptitle = dec((html.match(/<title>([^<]*)<\/title>/i) ?? [])[1] ?? '').trim()
    const found = []
    for (const m of html.matchAll(/<img\b[^>]*>/gi)) {
      const tag = m[0]
      const alt = dec((tag.match(/\balt=["']([^"']*)["']/i) ?? [])[1] ?? '')
      const srcs = []
      for (const a of ['data-src', 'data-lazy-src', 'data-original', 'src']) { const v = (tag.match(new RegExp(`\\b${a}=["']([^"']+)["']`, 'i')) ?? [])[1]; if (v) srcs.push(v) }
      const ss = (tag.match(/\b(?:data-)?srcset=["']([^"']+)["']/i) ?? [])[1]
      if (ss) { const parts = ss.split(',').map((p) => p.trim().split(/\s+/)); parts.sort((a, b) => parseInt(b[1] ?? '0') - parseInt(a[1] ?? '0')); if (parts[0]?.[0]) srcs.unshift(parts[0][0]) }
      if (srcs[0]) found.push({ src: srcs[0], alt })
    }
    for (const m of html.matchAll(/(?:property|name)=["'](?:og:image|twitter:image)["'][^>]*content=["']([^"']+)["']/gi)) found.push({ src: m[1], alt: 'og:image' })
    for (const m of html.matchAll(/https:\/\/freight\.cargo\.site\/[^"'\s)]+/g)) found.push({ src: m[0], alt: 'cargo' })
    for (const f of found) {
      let src = dec(f.src); if (src.startsWith('data:')) continue
      try { src = new URL(src, page).href } catch { continue }
      src = src.replace(/freight\.cargo\.site\/(t|w)\/[^/]+\/(?:[^/]+\/)?i\//, 'freight.cargo.site/w/1600/i/')
      if (skip.test(src)) continue
      cands.push({ src, alt: f.alt, page, ptitle })
    }
    log[page] = `ok ${found.length}`
    await sleep(800)
  }
  const seen = new Set(); const kept = []; let n = 0
  for (const c of cands) {
    if (seen.has(c.src) || kept.length >= (entry.max ?? 30)) continue
    seen.add(c.src)
    try {
      const { buf, ct } = await get(c.src, true)
      if (!/image/.test(ct) || buf.length < 25000) continue
      const ext = /png/.test(ct) ? 'png' : /webp/.test(ct) ? 'webp' : /avif/.test(ct) ? 'avif' : 'jpg'
      const file = `p${String(++n).padStart(2, '0')}.${ext}`
      writeFileSync(`${dir}/${file}`, buf)
      kept.push({ file, ...c, bytes: buf.length })
    } catch {}
    await sleep(200)
  }
  writeFileSync(`${dir}/manifest.json`, JSON.stringify(kept, null, 2))
  console.log(slug, kept.length)
}
writeFileSync('discovery3/log.json', JSON.stringify(log, null, 2))
