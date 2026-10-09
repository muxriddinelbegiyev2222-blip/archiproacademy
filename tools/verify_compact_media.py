"""Fail on broken/missing compact lesson assets without hiding known legacy repairs.

Usage:
    python tools/verify_compact_media.py
    python tools/verify_compact_media.py --require-complete
"""
import argparse
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "docs/MEDIA_COMPRESSION_2026_10_09.json"
LIMIT = 400_000


def verify(root=ROOT, require_complete=False):
    report_path = root / "docs/MEDIA_COMPRESSION_2026_10_09.json"
    report = json.loads(report_path.read_text(encoding="utf-8"))
    errors = []
    converted = report.get("records", [])
    blocked = report.get("blocked_records", [])
    used = set()

    for item in converted:
        relative = item["after"]
        if relative in used:
            errors.append(f"Duplicate recorded output: {relative}")
            continue
        used.add(relative)
        path = root / relative
        if not path.is_file():
            errors.append(f"Missing converted image: {relative}")
            continue
        data = path.read_bytes()
        if len(data) > LIMIT:
            errors.append(f"Image exceeds 400000 bytes: {relative} ({len(data)})")
        if len(data) != item["after_bytes"]:
            errors.append(f"Image length mismatch: {relative}")
        if hashlib.sha256(data).hexdigest() != item["after_sha256"]:
            errors.append(f"Image SHA-256 mismatch: {relative}")
        suffix = path.suffix.lower()
        if suffix in (".jpg", ".jpeg"):
            if not (data.startswith(b"\xff\xd8") and data.endswith(b"\xff\xd9")):
                errors.append(f"Invalid JPEG boundaries: {relative}")
        elif suffix == ".png":
            if not (data.startswith(b"\x89PNG\r\n\x1a\n") and data[-8:-4] == b"IEND"):
                errors.append(f"Invalid PNG boundaries: {relative}")
        else:
            errors.append(f"Unexpected converted image format: {relative}")

    for item in blocked:
        relative = item["before"]
        original = root / relative
        if not original.is_file():
            errors.append(f"Missing unresolved source (refresh repair registry): {relative}")
            continue
        if hashlib.sha256(original.read_bytes()).hexdigest() != item["before_sha256"]:
            errors.append(f"Unreviewed change to unresolved source: {relative}")

    if report.get("converted_count", len(converted)) != len(converted):
        errors.append("Converted image count differs from manifest")
    if report.get("blocked_count", len(blocked)) != len(blocked):
        errors.append("Unresolved image count differs from manifest")
    if bool(report.get("complete", not blocked)) != (not blocked):
        errors.append("Completion status differs from the remaining repair list")

    if require_complete and blocked:
        errors.append(f"{len(blocked)} legacy lesson sketches still require regeneration")

    print(f"ARCHIPRO media: checked {len(converted)} images, {len(blocked)} known repairs pending")
    for item in blocked:
        print(f"  PENDING: {item['before']}")
    for error in errors:
        print(f"  ERROR: {error}")
    print("MEDIA INTEGRITY: " + ("FAILED" if errors else "PASSED (known repairs listed)"))
    return 1 if errors else 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--require-complete", action="store_true")
    args = parser.parse_args()
    raise SystemExit(verify(require_complete=args.require_complete))
