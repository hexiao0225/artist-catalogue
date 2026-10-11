"""Copy chosen images into content/artists/<slug>/ (JPEG, 1600px long edge) and write artist.json."""
import json
import re
import sys
from pathlib import Path

from PIL import Image

sys.path.insert(0, str(Path(__file__).parent))
from artists_b import ARTISTS  # noqa: E402  (artists_b extends artists_a)

FETCH = Path('/home/claude/fetch')
OUT = Path('/home/claude/artist-catalogue/content/artists')
ADDED = '2026-10-11'

_manifests: dict[str, dict] = {}


def commons_meta(src: str) -> dict:
    slug, file = src.split('/')[1:]
    folder = src.split('/')[0]
    key = f'{folder}/{slug}'
    if key not in _manifests:
        _manifests[key] = {m['file']: m for m in json.load(open(FETCH / folder / slug / 'manifest.json'))}
    return _manifests[key][file]


def commons_credit(meta: dict, holder: str | None, artist: str = '') -> tuple[str, str]:
    author = re.sub(r'\s+', ' ', meta.get('author') or '').strip() or 'Unknown photographer'
    lic0 = meta.get('license') or ''
    if artist and artist.split()[-1].lower() in author.lower():
        lic_t = 'public domain' if lic0.lower().startswith(('public domain', 'cc0')) else lic0
        return f'© {artist}, {lic_t}, via Wikimedia Commons', meta['page']
    author = re.sub(r'\b(from|talk)\b.*$', '', author).strip(' -,(') or author
    lic = meta.get('license') or ''
    lic_text = 'public domain' if lic.lower().startswith(('public domain', 'no restrictions', 'cc0')) else lic
    photo = f'Photo: {author}, {lic_text}, via Wikimedia Commons'
    return (f'{holder}. {photo}' if holder else photo), meta['page']


def kebab(s: str) -> str:
    s = s.lower().replace('&', 'and')
    s = re.sub(r"[\"'’().,:;!?]", '', s)
    s = re.sub(r'[^a-z0-9]+', '-', s).strip('-')
    return s[:48].rstrip('-')


def save_image(src: str, dest: Path) -> None:
    im = Image.open(FETCH / src)
    if im.mode in ('RGBA', 'LA', 'P'):
        im = im.convert('RGBA')
        bg = Image.new('RGB', im.size, (255, 255, 255))
        bg.paste(im, mask=im.split()[-1])
        im = bg
    else:
        im = im.convert('RGB')
    im.thumbnail((1600, 1600), Image.LANCZOS)
    im.save(dest, 'JPEG', quality=86, optimize=True, progressive=True)


def holder_for(a: dict) -> str | None:
    # Works by artists who died more than 70 years ago are out of copyright; none of these are.
    return f'© {a["name"]}' if a['died'] is None else f'© Estate of {a["name"]}'


def build(slug: str, a: dict) -> None:
    d = OUT / slug
    d.mkdir(parents=True, exist_ok=True)
    for old in d.glob('*.jpg'):
        old.unlink()
    works = []
    for i, w in enumerate(a['works'], 1):
        src, title, kind, year, medium, note, collection = w[:7]
        if len(w) > 7:
            credit, source_url = w[7], w[8]
        else:
            credit, source_url = commons_credit(commons_meta(src), holder_for(a), a['name'])
        file = f'{i:02d}-{kebab(title)}.jpg'
        save_image(src, d / file)
        works.append({
            'title': title, 'kind': kind, 'year': year, 'medium': medium, 'note': note,
            'dimensions': None, 'collection': collection, 'file': file,
            'credit': credit, 'sourceUrl': source_url,
        })
    portrait = None
    if a.get('portrait'):
        p = a['portrait']
        if isinstance(p, tuple):
            src, credit = p
        else:
            src = p
            credit, _ = commons_credit(commons_meta(src), None)
        save_image(src, d / 'portrait.jpg')
        portrait = {'file': 'portrait.jpg', 'credit': credit}
    data = {
        'name': a['name'], 'nativeName': None, 'born': a['born'], 'died': a['died'],
        'birthplace': a['birthplace'], 'basedIn': a['basedIn'], 'nationality': a['nationality'],
        'categories': a['categories'], 'mediums': a['mediums'], 'tags': a['tags'],
        'bio': a['bio'], 'studyNotes': a['studyNotes'], 'myNotes': [], 'recommendedBy': None,
        'seenAt': None, 'status': 'to-study', 'addedOn': ADDED,
        'links': [{'label': l, 'url': u} for l, u in a['links']],
        'portrait': portrait, 'videos': [], 'works': works,
    }
    (d / 'artist.json').write_text(json.dumps(data, indent=2, ensure_ascii=False) + '\n')
    print(f'{slug}: {len(works)} works{", portrait" if portrait else ""}')


if __name__ == '__main__':
    only = sys.argv[1:]
    for slug, a in ARTISTS.items():
        if not only or slug in only:
            build(slug, a)
