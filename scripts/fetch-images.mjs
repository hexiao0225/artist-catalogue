// Discovers candidate images for each artist from Wikipedia + Wikimedia Commons,
// plus og:image / large images from listed web pages. Writes discovery/<slug>/ + manifest.json
import { mkdirSync, writeFileSync, readFileSync } from 'node:fs'
const UA = 'ArtistCatalogueStudyBot/1.0 (https://github.com/hexiao0225; hexiao0225 study catalogue)'
const sources = JSON.parse(readFileSync('scripts/sources.json', 'utf8'))
const sleep = (ms) => new Promise((r) => setTimeout(r, ms))
async function j(url) {
  for (let i = 0; i < 3; i++) {
    try { const r = await fetch(url, { headers: { 'User-Agent': UA } }); if (r.ok) return await r.json() } catch {}
    await sleep(1500)
  }
  return null
}
const strip = (s) => (s ?? '').replace(/<[^>]+>/g, '').replace(/\s+/g, ' ').trim()
async function infoFor(titles, wiki) {
  const out = []
  for (let i = 0; i < titles.length; i += 40) {
    const t = titles.slice(i, i + 40).join('|')
    const d = await j(`https://${wiki}/w/api.php?action=query&format=json&prop=imageinfo&iiprop=url|size|mime|extmetadata&iiurlwidth=1600&titles=${encodeURIComponent(t)}`)
    for (const p of Object.values(d?.query?.pages ?? {})) {
      const ii = p.imageinfo?.[0]; if (!ii) continue
      const m = ii.extmetadata ?? {}
      out.push({ title: p.title, mime: ii.mime, w: ii.width, h: ii.height, thumb: ii.thumburl || ii.url, page: ii.descriptionurl,
        description: strip(m.ImageDescription?.value).slice(0, 300), author: strip(m.Artist?.value).slice(0, 200),
        license: m.LicenseShortName?.value ?? '', credit: strip(m.Credit?.value).slice(0, 200), date: strip(m.DateTimeOriginal?.value).slice(0, 60), wiki })
    }
  }
  return out
}
async function pageImages(article, wiki = 'en.wikipedia.org') {
  const d = await j(`https://${wiki}/w/api.php?action=query&format=json&prop=images&imlimit=200&redirects=1&titles=${encodeURIComponent(article)}`)
  const ims = Object.values(d?.query?.pages ?? {}).flatMap((p) => (p.images ?? []).map((i) => i.title))
  return ims.filter((t) => /\.(jpe?g|png|webp|gif|tiff?)$/i.test(t))
}
async function commonsSearch(q, n = 40) {
  const d = await j(`https://commons.wikimedia.org/w/api.php?action=query&format=json&list=search&srnamespace=6&srlimit=${n}&srsearch=${encodeURIComponent(q)}`)
  return (d?.query?.search ?? []).map((s) => s.title).filter((t) => /\.(jpe?g|png|webp|tiff?)$/i.test(t))
}
async function categoryFiles(cat, n = 60) {
  const d = await j(`https://commons.wikimedia.org/w/api.php?action=query&format=json&list=categorymembers&cmtype=file&cmlimit=${n}&cmtitle=${encodeURIComponent(cat)}`)
  return (d?.query?.categorymembers ?? []).map((s) => s.title).filter((t) => /\.(jpe?g|png|webp|tiff?)$/i.test(t))
}
async function ogImages(url) {
  try {
    const r = await fetch(url, { headers: { 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128 Safari/537.36' }, redirect: 'follow' })
    if (!r.ok) return []
    const html = await r.text()
    const found = new Set()
    for (const m of html.matchAll(/<meta[^>]+(?:property|name)=["'](?:og:image|twitter:image)(?::src)?["'][^>]*content=["']([^"']+)["']/gi)) found.add(m[1])
    for (const m of html.matchAll(/<meta[^>]+content=["']([^"']+)["'][^>]*(?:property|name)=["'](?:og:image|twitter:image)["']/gi)) found.add(m[1])
    return [...found].map((u) => new URL(u.replace(/&amp;/g, '&'), url).href).map((src) => ({ title: src.split('/').pop().slice(0, 80), thumb: src, page: url, description: '', author: '', license: 'web', credit: new URL(url).hostname }))
  } catch { return [] }
}
const skip = /(logo|icon|flag|signature|commons-|wiki|symbol|edit-|question_book|ambox|disambig|portal|crystal|nuvola|folder|locator|map_of|_map|\.svg)/i
const results = {}
for (const a of sources) {
  const titles = new Set()
  for (const art of a.articles ?? []) for (const t of await pageImages(art)) titles.add(t)
  for (const c of a.categories ?? []) for (const t of await categoryFiles(c)) titles.add(t)
  for (const q of a.search ?? [a.name]) for (const t of await commonsSearch(q)) titles.add(t)
  let list = (await infoFor([...titles].filter((t) => !skip.test(t)), 'commons.wikimedia.org'))
  const missing = [...titles].filter((t) => !skip.test(t) && !list.some((x) => x.title === t))
  if (missing.length) list = list.concat(await infoFor(missing, 'en.wikipedia.org'))
  list = list.filter((x) => (x.w ?? 9999) >= 400 && (x.h ?? 9999) >= 300)
  for (const u of a.pages ?? []) list = list.concat(await ogImages(u))
  const dir = `discovery/${a.slug}`; mkdirSync(dir, { recursive: true })
  const kept = []
  let n = 0
  for (const it of list.slice(0, a.max ?? 30)) {
    try {
      const r = await fetch(it.thumb, { headers: { 'User-Agent': UA } })
      if (!r.ok) { await sleep(500); continue }
      const buf = Buffer.from(await r.arrayBuffer())
      if (buf.length < 8000) continue
      const ext = /png/i.test(r.headers.get('content-type') ?? '') ? 'png' : /webp/.test(r.headers.get('content-type') ?? '') ? 'webp' : 'jpg'
      const file = `c${String(++n).padStart(2, '0')}.${ext}`
      writeFileSync(`${dir}/${file}`, buf)
      kept.push({ file, ...it, bytes: buf.length })
    } catch {}
    await sleep(250)
  }
  results[a.slug] = kept
  writeFileSync(`${dir}/manifest.json`, JSON.stringify(kept, null, 2))
  console.log(a.slug, kept.length)
}
writeFileSync('discovery/summary.json', JSON.stringify(Object.fromEntries(Object.entries(results).map(([k, v]) => [k, v.length])), null, 2))
