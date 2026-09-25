# Artist Catalogue

A museum-style catalogue of artists to study, built with React + TypeScript and deployed on Vercel.

**Live:** https://artist-catalogue.vercel.app/

## Add an artist

Each artist is one folder in `content/artists/`:

```
content/artists/maria-lassnig/
  artist.json        ← name, dates, bio, study notes, works
  01-expressive-self-portrait.jpg
  02-fat-green.jpg
  portrait.jpg       ← optional
```

1. `npm run new -- "Paula Rego"` creates `content/artists/paula-rego/artist.json` from a template.
   You can also create the file on github.com with *Add file → Create new file*.
2. Put the images next to it, about 1600px on the long edge. The first work in `works` becomes the cover.
3. Fill in the JSON. `status` is `to-study`, `studying` or `studied`. Your own observations go in `myNotes`.
4. Commit to `main`. Vercel validates the content, builds the site and deploys it. A broken entry fails the build and the live site stays as it was.

`npm run validate` checks every folder: required fields, date formats and that every referenced image exists.

## Views

- **Artists**: a grid or A–Z index, searchable by name, work, medium or theme, and filterable by study status.
- **Artist page**: a hero work, bio, facts, "What to look at" study notes, works with wall labels, and links.
- **Slides**: a full-screen deck with a title slide per artist followed by their works.
  Navigate with ← → or by swiping; Esc closes. `#/slides/<slug>` shows one artist.

## Develop

```
npm install
npm run dev
npm run lint && npm run build
```

## Images

Images are credited to their rights holders in each `artist.json` and reproduced for private study and reference.
Public-domain and CC-licensed images come from Wikimedia Commons where possible.
