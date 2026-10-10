"""Install seven reviewed legacy image replacements from the supplied ZIP.

From repository root, with archipro_7_repaired_images.zip alongside it:
    python tools/install_seven_repaired_media.py archipro_7_repaired_images.zip

Do not run git commit until integrity and functional audits pass.
"""
import hashlib
import json
import shutil
import sys
import tempfile
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "app/courses/visual_assets"
REPORT = ROOT / "docs/MEDIA_COMPRESSION_2026_10_09.json"
CODES = ("L07_M02_003", "L07_M04_001", "L07_M05_001", "L07_M05_002",
         "L07_M05_003", "L07_M05_004", "L07_M06_002")


def install(package):
    if not package.is_file():
        raise FileNotFoundError(f"ZIP not found: {package}")
    report = json.loads(REPORT.read_text(encoding="utf-8"))
    unresolved = report.get("blocked_records", [])
    if len(unresolved) == 0 and report.get("complete"):
        print("Seven-image recovery already completed; no files changed.")
        return
    if len(unresolved) != 7:
        raise ValueError(f"Expected 7 blocked assets; got {len(unresolved)}")
    by_stem = {Path(x["before"]).stem.upper(): x for x in unresolved}
    if set(by_stem) != set(CODES):
        raise ValueError("Repo repair list differs from the reviewed package")

    with zipfile.ZipFile(package) as archive:
        manifest = json.loads(archive.read("manifest.json").decode("utf-8"))
        if len(manifest) != 7 or {x["code"] for x in manifest} != set(CODES):
            raise ValueError("Wrong package manifest")
        plan = []
        for record in manifest:
            code = record["code"]
            name = f"sketch-{code.lower()}.jpg"
            if record["name"] != name:
                raise ValueError(f"Wrong image name: {record['name']}")
            data = archive.read(name)
            source = ROOT / by_stem[code]["before"]
            dest = ASSETS / name
            if len(data) > 400_000 or not data.startswith(bytes.fromhex("ffd8")) or not data.endswith(bytes.fromhex("ffd9")):
                raise ValueError(f"Invalid compact JPEG: {name}")
            if len(data) != record["bytes"] or hashlib.sha256(data).hexdigest() != record["sha256"]:
                raise ValueError(f"Incorrect image hash or length: {name}")
            if not source.is_file() or dest.exists():
                raise ValueError(f"Unexpected repository state: {code}")
            old_data = source.read_bytes()
            if hashlib.sha256(old_data).hexdigest() != by_stem[code]["before_sha256"]:
                raise ValueError(f"Old image changed unexpectedly: {source.name}")
            plan.append((record, by_stem[code], source, dest, data))

    changes = {}
    # Keep both runtime mappings and human-reviewed 680-lesson inventories
    # synchronized. Audit history itself must retain the old source names.
    inventory_paths = [
        ROOT / "docs/REALISTIC_LESSON_COVERAGE.csv",
        ROOT / "docs/VISUAL_LESSON_COVERAGE.csv",
        ROOT / "docs/ALL_LESSON_SKETCH_COVERAGE.csv",
    ]
    candidates = (
        list((ROOT / "app").rglob("*.py"))
        + list((ROOT / "app").rglob("*.json"))
        + [p for p in inventory_paths if p.is_file()]
    )
    for path in candidates:
        text = path.read_text(encoding="utf-8")
        changed = text
        for record, blocked, source, dest, data in plan:
            changed = changed.replace(source.name, dest.name)
        if changed != text:
            changes[path] = changed
    for record, blocked, source, dest, data in plan:
        if not any(dest.name in new for new in changes.values()):
            raise ValueError(f"Missing image reference: {record['code']}")

    with tempfile.TemporaryDirectory(prefix="archipro-repair-backup-") as staging:
        backup = Path(staging)
        originals = {p: p.read_bytes() for p in changes}
        original_report = REPORT.read_bytes()
        try:
            for record, blocked, source, dest, data in plan:
                shutil.copy2(source, backup / source.name)
                dest.write_bytes(data)
            for p, revised in changes.items():
                p.write_text(revised, encoding="utf-8")
            for record, blocked, source, dest, data in plan:
                report["records"].append(dict(
                    before=blocked["before"],
                    after=str(dest.relative_to(ROOT)).replace("\\", "/"),
                    before_bytes=blocked["before_bytes"],
                    after_bytes=len(data),
                    width=record["width"], height=record["height"],
                    quality=record["quality"],
                    before_sha256=blocked["before_sha256"],
                    after_sha256=record["sha256"],
                    recovery_source="Reviewed topic-specific image, compact JPEG",
                ))
                report.setdefault("renames", {})[source.name] = dest.name
                if blocked["before"] not in report.setdefault("deleted_paths", []):
                    report["deleted_paths"].append(blocked["before"])
            if len(report["records"]) != 278:
                raise ValueError("Repair count mismatch (expected 278)")
            report["blocked_records"] = []
            report["blocked_count"] = 0
            report["converted_count"] = len(report["records"])
            report["complete"] = True
            report["before_bytes"] = sum(x["before_bytes"] for x in report["records"])
            report["after_bytes"] = sum(x["after_bytes"] for x in report["records"])
            report["changed_paths"] = sorted(set(report.get("changed_paths", [])) |
                 {str(p.relative_to(ROOT)).replace("\\", "/") for p in changes} |
                 {str(dest.relative_to(ROOT)).replace("\\", "/") for _, _, _, dest, _ in plan})
            REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

            from verify_compact_media import verify
            if verify(root=ROOT, require_complete=True):
                raise ValueError("Integrity audit failed")
        except Exception:
            for p, old in originals.items():
                p.write_bytes(old)
            REPORT.write_bytes(original_report)
            for record, blocked, source, dest, data in plan:
                dest.unlink(missing_ok=True)
            raise
        for record, blocked, source, dest, data in plan:
            source.unlink()
    print("SUCCESS: 7/7 recovered, 278/278 image conversions recorded.")
    print("Run Python/CI audits before pushing or releasing.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("Usage: python tools/install_seven_repaired_media.py <package.zip>")
    install(Path(sys.argv[1]).resolve())
