"""Offline, dependency-free integrity check for every shipped Python source."""
from __future__ import annotations

import os
import tokenize
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCAN_DIRS = ("app", "tools", "devtools")
REQUIRED = (
    "app/main.py",
    "app/tools/release_regression_test.py",
    "app/courses/level15_module08.py",
    "app/licensing/license_service.py",
    "tools/verify_course_visuals.py",
)


def main() -> int:
    failures = []
    paths = []
    for folder in SCAN_DIRS:
        directory = ROOT / folder
        if not directory.is_dir():
            failures.append(f"Missing source directory: {folder}")
            continue
        paths.extend(p for p in directory.rglob("*.py")
                     if "__pycache__" not in p.parts)

    for required in REQUIRED:
        if not (ROOT / required).is_file():
            failures.append(f"Missing required source: {required}")

    for path in sorted(set(paths)):
        try:
            with tokenize.open(path) as source:
                code = source.read()
            compile(code, str(path), "exec", dont_inherit=True)
        except (OSError, SyntaxError, UnicodeError, ValueError) as exc:
            failures.append(f"{path.relative_to(ROOT)}: {exc}")

    if len(set(paths)) < 100:
        failures.append(
            f"Suspiciously incomplete source inventory: {len(set(paths))} modules"
        )

    ignored = {".git", ".venv", "venv", "__pycache__", "build",
               "build_client", "dist", "dist_client", "release", "node_modules"}
    forbidden = {"archipro_private.key", "private_key.pem", ".env"}
    for folder, subdirs, files in os.walk(ROOT):
        subdirs[:] = [name for name in subdirs if name not in ignored]
        for filename in files:
            if filename.lower() in forbidden:
                path = Path(folder) / filename
                failures.append(f"Sensitive file present in project: {path.relative_to(ROOT)}")

    print(f"Source integrity: checked {len(set(paths))} Python files")
    for message in failures:
        print("ERROR: " + message)
    print("SOURCE INTEGRITY: " + ("FAILED" if failures else "PASSED"))
    return int(bool(failures))


if __name__ == "__main__":
    raise SystemExit(main())
