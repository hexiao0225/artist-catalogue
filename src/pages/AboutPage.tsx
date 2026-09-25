import { REPO_URL } from '../config'

const EXAMPLE = `{
  "name": "Paula Rego",
  "born": 1935,
  "died": 2022,
  "nationality": "Portuguese-British",
  "mediums": ["Painting", "Pastel", "Printmaking"],
  "tags": ["Figuration", "Storytelling"],
  "bio": "A short, museum-label style biography.",
  "studyNotes": ["What to look at when studying her work."],
  "myNotes": [],
  "recommendedBy": "Who suggested her",
  "status": "to-study",
  "addedOn": "2026-09-24",
  "links": [{ "label": "Tate", "url": "https://www.tate.org.uk/" }],
  "portrait": null,
  "works": [
    {
      "title": "The Dance",
      "year": "1988",
      "medium": "Acrylic on paper on canvas",
      "dimensions": "213.4 × 274 cm",
      "collection": "Tate",
      "file": "01-the-dance.jpg",
      "credit": "© Paula Rego. Photo: Tate",
      "sourceUrl": "https://www.tate.org.uk/art/artworks/rego-the-dance-t05535"
    }
  ]
}`

export default function AboutPage() {
  return (
    <div className="wrap">
      <section className="page-intro">
        <h1 className="display">How to add</h1>
        <p className="lede">
          Each artist is one folder. Add a folder and push, and the site rebuilds itself.
        </p>
      </section>

      <section className="section steps">
        <ol className="notes">
          <li>
            <strong>Make the folder.</strong> In the repository, run{' '}
            <code>npm run new -- "Paula Rego"</code>. Or, on github.com, choose{' '}
            <em>Add file → Create new file</em> and type{' '}
            <code>content/artists/paula-rego/artist.json</code>.
          </li>
          <li>
            <strong>Add images.</strong> Put JPEGs next to <code>artist.json</code> (about 1600px on
            the long edge is plenty) and name them <code>01-title.jpg</code>,{' '}
            <code>02-title.jpg</code>… The first work becomes the cover.
          </li>
          <li>
            <strong>Fill in the details.</strong> The fields are shown below. Set{' '}
            <code>status</code> to <code>to-study</code>, <code>studying</code> or{' '}
            <code>studied</code> as you go, and write your own observations in <code>myNotes</code>.
          </li>
          <li>
            <strong>Commit to main.</strong> Vercel checks the content, builds the site and
            publishes it in about a minute. If an image is missing or a field is
            wrong, the build fails and tells you which file to fix.
          </li>
        </ol>
      </section>

      <section className="section">
        <h2 className="section__title">artist.json</h2>
        <pre className="code">{EXAMPLE}</pre>
        <p className="prose prose--small">
          <a href={REPO_URL}>Open the repository ↗</a>
        </p>
      </section>
    </div>
  )
}
