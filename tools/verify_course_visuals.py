"""Verify the 680-lesson image map and on-disk media integrity.

This is a static integrity check, NOT a visual-quality review or a substitute
for the interactive UI / Windows EXE test.
Usage: python tools/verify_course_visuals.py
"""
import csv
import json
import xml.etree.ElementTree as ET
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "app" / "courses" / "visual_assets"
DOCS = ROOT / "docs"
IMAGE_LIMIT = 400_000
COVERAGE_CSVS = {
    "sketch": ("ALL_LESSON_SKETCH_COVERAGE.csv", "sketch_asset"),
    "visual": ("VISUAL_LESSON_COVERAGE.csv", "assets"),
    "reviewed": ("REALISTIC_LESSON_COVERAGE.csv", "realistic_asset"),
}
FIGURE_JSONS = ("lesson_figures.json", "realistic_figures.json", "archicad_figures.json")


def read_csv(filename):
    with (DOCS / filename).open(encoding="utf-8-sig", newline="") as stream:
        return list(csv.DictReader(stream))


def check():
    problems = []
    coverage = {}
    checked_assets = set()

    def add(problem):
        problems.append(problem)

    def check_asset(name, where):
        if not name:
            return
        # Asset registry names must be basenames; no filesystem traversal.
        if Path(name).name != name or name in (".", ".."):
            add(f"{where}: unsafe asset name {name!r}")
            return
        p = ASSETS / name
        checked_assets.add(name)
        if not p.is_file():
            add(f"{where}: missing {name}")
            return
        if p.suffix.lower() not in (".jpg", ".jpeg", ".png", ".svg", ".webp"):
            add(f"{where}: unsupported asset type {name}")
            return
        if p.suffix.lower() in (".jpg", ".jpeg"):
            data = p.read_bytes()
            if len(data) > IMAGE_LIMIT:
                add(f"{where}: JPEG exceeds 400 KB ({len(data)} bytes): {name}")
            if not (data.startswith(bytes.fromhex("ffd8")) and data.endswith(bytes.fromhex("ffd9"))):
                add(f"{where}: damaged JPEG file: {name}")
        elif p.suffix.lower() == ".svg":
            try:
                ET.parse(p)
            except ET.ParseError as exc:
                add(f"{where}: malformed SVG {name}: {exc}")
        elif p.suffix.lower() == ".png":
            if p.open("rb").read(8) != bytes.fromhex("89504e470d0a1a0a"):
                add(f"{where}: invalid PNG signature: {name}")

    for kind, (filename, column) in COVERAGE_CSVS.items():
        rows = read_csv(filename)
        codes = [row.get("code", "") for row in rows]
        if len(codes) != 680 or len(set(codes)) != 680:
            add(f"{filename}: expected exactly 680 unique lesson codes, got {len(codes)} rows / {len(set(codes))} unique")
        coverage[kind] = set(codes)
        for row in rows:
            code = row.get("code") or "unknown"
            raw = row.get(column) or ""
            for name in raw.split("|"):
                check_asset(name.strip(), f"{filename}:{code}")

    if not (coverage["sketch"] == coverage["visual"] == coverage["reviewed"]):
        add("Three coverage CSVs have different lesson-code sets")

    figure_codes = set()
    for filename in FIGURE_JSONS:
        source = json.loads((ASSETS / filename).read_text(encoding="utf-8"))
        if not isinstance(source, list):
            add(f"{filename}: expected JSON list")
            continue
        for item in source:
            code = item.get("code", "")
            figure_codes.add(code)
            if code not in coverage["visual"]:
                add(f"{filename}: figure for unknown lesson {code}")
            check_asset(item.get("asset", ""), f"{filename}:{code}")

    if figure_codes != coverage["visual"]:
        add(f"JSON figures do not cover exactly the 680 lessons (missing {len(coverage['visual']-figure_codes)}, extra {len(figure_codes-coverage['visual'])})")

    state_path = DOCS / "ARCHIPRO_IMAGE_REWORK_STATUS_2026_10_10.json"
    if state_path.is_file():
        state = json.loads(state_path.read_text(encoding="utf-8"))
        completed = state.get("completed_new_codes", [])
        if len(set(completed)) != len(completed):
            add("Rework status has duplicate completed lesson codes")
        if state.get("individually_replaced_on_main") != len(completed):
            add("Completed lesson count disagrees with the rework status")
        if state.get("still_to_replace", 0) + len(completed) != state.get("review_pending_initial", -1):
            add("Rework status total does not match its completed and pending counts")
        by_code = {item.get("code"): item.get("asset") for item in json.loads((ASSETS / "lesson_figures.json").read_text(encoding="utf-8"))}
        for code in completed:
            expected = f"sketch-{code.lower()}.jpg"
            if by_code.get(code) != expected:
                add(f"Completed {code} not connected to expected JPEG: {by_code.get(code)}")

    print(f"Lesson visual integrity: {len(coverage['visual'])} lessons, {len(figure_codes)} codes with figures, {len(checked_assets)} unique assets referenced")
    for problem in problems:
        print("ERROR: " + problem)
    print("VISUAL INTEGRITY: " + ("FAILED" if problems else "PASSED (static references and file structure only)"))
    return int(bool(problems))


if __name__ == "__main__":
    raise SystemExit(check())
