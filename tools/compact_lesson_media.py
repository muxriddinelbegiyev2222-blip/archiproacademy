"""Prepare reviewable <=400000-byte lesson images without changing pixel dimensions."""
import base64
import hashlib
import io
import json
import os
from pathlib import Path
import re
import zipfile

os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')
from PIL import Image, ImageDraw, ImageStat
from PySide6.QtCore import QBuffer, QIODevice
from PySide6.QtGui import QImage, QPainter
from PySide6.QtSvg import QSvgRenderer
from PySide6.QtWidgets import QApplication

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / 'app/courses/visual_assets'
LIMIT = 400000


def jpeg_below_limit(im):
    # Full resolution and 4:4:4 preserve text and fine coloured strokes.
    im = im.convert('RGB')
    for quality in range(95, 29, -1):
        out = io.BytesIO()
        im.save(out, 'JPEG', quality=quality, subsampling=0, optimize=True)
        if len(out.getvalue()) <= LIMIT:
            return out.getvalue(), quality
    raise ValueError('Cannot meet the size cap at full resolution')


def svg_image(path):
    if b"bytes omitted" in path.read_bytes():
        raise ValueError(f"Truncated embedded image: {path}")
    renderer = QSvgRenderer(str(path))
    if not renderer.isValid():
        raise ValueError(f'Invalid SVG: {path}')
    size = renderer.defaultSize()
    image = QImage(size, QImage.Format.Format_RGB32)
    image.fill(0xFFFFFFFF)
    painter = QPainter(image)
    renderer.render(painter)
    painter.end()
    buf = QBuffer()
    buf.open(QIODevice.OpenModeFlag.WriteOnly)
    image.save(buf, 'PNG')
    result = Image.open(io.BytesIO(bytes(buf.data()))).convert('RGB')
    if max(ImageStat.Stat(result).stddev) < 3:
        raise ValueError(f'Blank SVG rendering requires manual recovery: {path}')
    return result


def run():
    app = QApplication.instance() or QApplication([])
    destination = ROOT / 'docs/MEDIA_COMPRESSION_2026_10_09.json'
    previous = json.loads(destination.read_text(encoding='utf-8')) if destination.exists() else {}
    known_blocked = {item['before']: item for item in previous.get('blocked_records', [])}
    report = {'limit_bytes': LIMIT, 'pixel_dimensions_preserved': True,
              'records': list(previous.get('records', [])),
              'renames': dict(previous.get('renames', {})),
              'deleted_paths': list(previous.get('deleted_paths', [])),
              'blocked_records': []}
    new_records = []
    changed = set()
    comparisons = []
    for path in sorted(ASSETS.iterdir()):
        if path.suffix.lower() not in ('.svg', '.jpg', '.jpeg', '.png'):
            continue
        original = path.read_bytes()
        if len(original) <= LIMIT:
            continue
        if path.suffix == '.svg':
            try:
                im = svg_image(path)
            except ValueError as exc:
                rel = str(path.relative_to(ROOT))
                if rel not in known_blocked:
                    raise  # Do not silently accept a newly corrupted asset.
                report['blocked_records'].append({
                    **known_blocked[rel],
                    'error': str(exc),
                })
                print('NEEDS IMAGE REPAIR:', rel, str(exc), flush=True)
                continue
            target = path.with_name('sketch-' + path.stem + '.jpg')
            encoded, quality = jpeg_below_limit(im)
        else:
            im = Image.open(io.BytesIO(original)).convert('RGB')
            if path.suffix == '.png' and path.name.startswith('ac28-'):
                # Real UI captures retain sharp pixel boundaries and PNG encoding.
                encoded = None
                for colors in (256, 128, 64):
                    b = io.BytesIO()
                    im.quantize(colors=colors, method=Image.Quantize.MEDIANCUT).save(b, 'PNG', optimize=True)
                    if len(b.getvalue()) <= LIMIT:
                        encoded, quality = b.getvalue(), f'PNG palette {colors}'
                        break
                if encoded is None:
                    raise ValueError(f'UI screenshot needs manual review: {path.name}')
                target = path
            else:
                encoded, quality = jpeg_below_limit(im)
                target = path.with_suffix('.jpg')
        assert len(encoded) <= LIMIT
        after = Image.open(io.BytesIO(encoded)).convert('RGB')
        assert after.size == im.size
        target.write_bytes(encoded)
        old_rel, new_rel = str(path.relative_to(ROOT)), str(target.relative_to(ROOT))
        if target != path:
            report['renames'][path.name] = target.name
            report['deleted_paths'].append(old_rel)
            path.unlink()
        changed.add(new_rel)
        record = {'before': old_rel, 'after': new_rel, 'before_bytes': len(original),
                  'after_bytes': len(encoded), 'width': im.width, 'height': im.height,
                  'quality': quality, 'before_sha256': hashlib.sha256(original).hexdigest(),
                  'after_sha256': hashlib.sha256(encoded).hexdigest()}
        report['records'] = [old for old in report['records'] if old['before'] != old_rel]
        report['records'].append(record)
        new_records.append(record)
        # Review samples include the most demanding encodings and all UI captures.
        if isinstance(quality, str) or quality < 70 or len(comparisons) < 8:
            comparisons.append((path.name, im.copy(), after.copy()))
        print(path.name, len(original), '->', target.name, len(encoded), quality, flush=True)

    # Update only exact asset filename references, not lesson prose or questions.
    for path in list((ROOT / 'app').rglob('*.py')) + list(ASSETS.glob('*.json')):
        text = path.read_text(encoding='utf-8')
        updated = text
        for old, new in report['renames'].items():
            updated = updated.replace("'" + old + "'", "'" + new + "'")
            updated = updated.replace('"' + old + '"', '"' + new + '"')
        if updated != text:
            path.write_text(updated, encoding='utf-8')
            changed.add(str(path.relative_to(ROOT)))

    registry = ROOT / 'docs/VISUAL_REWORK_2026_10_08.json'
    if registry.exists() and new_records:
        data = json.loads(registry.read_text())
        by_old = {x['before']: x for x in new_records}
        for item in data['accepted']:
            if item['asset'] in by_old:
                r = by_old[item['asset']]
                item['original_asset'] = item['asset']
                item['asset'] = r['after']
                item['file_sha256'] = r['after_sha256']
                item['file_bytes'] = r['after_bytes']
                item['encoding'] = f"JPEG quality {r['quality']}, 4:4:4; <=400000 bytes; original dimensions"
                if 'svg_sha256' in item:
                    item['original_svg_sha256'] = item.pop('svg_sha256')
        registry.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')
        changed.add(str(registry.relative_to(ROOT)))
    # Re-run safety: prior completed conversions must still exist and match.
    for item in report['records']:
        finished = ROOT / item['after']
        if not finished.is_file():
            raise FileNotFoundError(f"Previously converted asset missing: {finished}")
        if hashlib.sha256(finished.read_bytes()).hexdigest() != item['after_sha256']:
            raise ValueError(f"Previously converted asset hash mismatch: {finished}")
        if finished.stat().st_size > LIMIT:
            raise ValueError(f"Previously converted asset exceeds 400 KB: {finished}")

    report['before_bytes'] = sum(x['before_bytes'] for x in report['records'])
    report['after_bytes'] = sum(x['after_bytes'] for x in report['records'])
    report['changed_paths'] = sorted(set(previous.get('changed_paths', [])) | changed)
    report['converted_count'] = len(report['records'])
    report['blocked_count'] = len(report['blocked_records'])
    report['complete'] = not report['blocked_records']
    destination.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    changed.add(str(destination.relative_to(ROOT)))
    review_dir = ROOT / 'media-review'
    review_dir.mkdir(exist_ok=True)
    for index, (name, before, after) in enumerate(comparisons):
        sheet = Image.new('RGB', (1536, 1064), 'white')
        draw = ImageDraw.Draw(sheet)
        before.thumbnail((768, 1024)); after.thumbnail((768, 1024))
        sheet.paste(before, (0, 40)); sheet.paste(after, (768, 40))
        draw.text((8, 8), name + ' BEFORE / AFTER', fill='black')
        sheet.save(review_dir / f'{index:03}.jpg', quality=95)
    with zipfile.ZipFile(ROOT / 'compact-media-review.zip', 'w', zipfile.ZIP_DEFLATED) as archive:
        for name in sorted(changed):
            archive.write(ROOT / name, name)
        for path in review_dir.glob('*.jpg'):
            archive.write(path, str(path.relative_to(ROOT)))
    print(json.dumps({'converted_this_run': len(new_records),
                      'converted_total': report['converted_count'],
                      'blocked': report['blocked_count'],
                      'complete': report['complete'],
                      'before_bytes': report['before_bytes'],
                      'after_bytes': report['after_bytes'],
                      'review_samples': len(comparisons)}))


if __name__ == '__main__':
    run()
