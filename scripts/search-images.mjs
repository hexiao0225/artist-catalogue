// Round 2: image search for specific works. Writes discovery2/<slug>/ + manifest.json
import { mkdirSync, writeFileSync, readFileSync } from 'node:fs'
const UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128 Safari/537.36'
const queries = JSON.parse(readFileSync('scripts/queries.json', 'utf8'))
const sleep = (ms) => new Promise((r) => setTimeout(r, ms))
const unesc = (s) => s.replace(/&quot;/g, '"').replace(/&amp;/g, '&')
for (const [slug, qs] of Object.entries(queries)) {
  const dir = `discovery2/${slug}`; mkdirSync(dir, { recursive: true })
  const kept = []; let n = 0; const seen = new Set()
  for (const q of qs) {
    let html = ''
    try { const r = await fetch(`https://www.bing.com/images/search?q=${encodeURIComponent(q)}&form=HDRSC2&first=1`, { headers: { 'User-Agent': UA, 'Accept-Language': 'en-US' } }); html = await r.text() } catch {}
    const items = []
    for (const m of html.matchAll(/\sm="(\{[^"]+\})"/g)) {
      try { const o = JSON.parse(unesc(m[1])); if (o.murl) items.push(o) } catch {}
    }
    let got = 0
    for (const o of items) {
      if (got >= 5) break
      if (seen.has(o.murl)) continue
      seen.add(o.murl)
      try {
        const r = await fetch(o.murl, { headers: { 'User-Agent': UA, Referer: o.purl || '' }, signal: AbortSignal.timeout(15000) })
        if (!r.ok) continue
        const ct = r.headers.get('content-type') ?? ''
        if (!/image/.test(ct)) continue
        const buf = Buffer.from(await r.arrayBuffer())
        if (buf.length < 15000) continue
        const ext = /png/.test(ct) ? 'png' : /webp/.test(ct) ? 'webp' : 'jpg'
        const file = `s${String(++n).padStart(2, '0')}.${ext}`
        writeFileSync(`${dir}/${file}`, buf)
        kept.push({ file, query: q, title: o.t ?? '', image: o.murl, page: o.purl ?? '', bytes: buf.length })
        got++
      } catch {}
    }
    await sleep(1200)
  }
  writeFileSync(`${dir}/manifest.json`, JSON.stringify(kept, null, 2))
  console.log(slug, kept.length)
}
