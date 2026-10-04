"""Restore the exact credited documentation assets from the committed manifest.

Developer maintenance only; the installed app never downloads lesson pictures.
"""
import json
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.parse import urlsplit

assets = Path(__file__).resolve().parents[1] / 'app/courses/visual_assets'
records = json.loads((assets / 'archicad_figures.json').read_text(encoding='utf-8'))
seen = set()
for row in records:
    filename, url = row['asset'], row['source_image_url']
    if filename in seen:
        continue
    seen.add(filename)
    if Path(filename).name != filename or urlsplit(url).hostname != 'help.graphisoft.com':
        raise ValueError('Unexpected documentation asset path or source')
    target = assets / filename
    if target.exists():
        continue
    with urlopen(Request(url, headers={'User-Agent': 'Mozilla/5.0'}), timeout=30) as response:
        data = response.read()
    target.write_bytes(data)
    print(filename)
