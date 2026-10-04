"""Build the client with an explicit inventory of local dynamic Python modules."""
from pathlib import Path
import sys

APP = Path(__file__).resolve().parents[1]
PROJECT = APP.parent


def dynamic_modules():
    modules = set()
    for package in ("courses", "licensing", "ui"):
        for source in (APP / package).rglob("*.py"):
            parts = source.relative_to(APP).with_suffix("").parts
            if parts[-1] == "__init__":
                parts = parts[:-1]
            modules.add(".".join(parts))
    if "courses.lesson_content" not in modules or "courses.level15_module08" not in modules:
        raise RuntimeError("The source curriculum inventory is incomplete")
    return sorted(modules)


def main():
    import PyInstaller.__main__
    modules = dynamic_modules()
    print(f"[INFO] Explicit local dynamic modules: {len(modules)}", flush=True)
    args = ["--noconfirm", "--clean", "--onefile", "--windowed",
            "--name", "ARCHIPRO UZ", "--paths", str(APP),
            "--icon", str(PROJECT / "archipro.ico")]
    for module in modules:
        args.extend(["--hidden-import", module])
    args.extend(sys.argv[1:])
    args.append(str(APP / "main.py"))
    PyInstaller.__main__.run(args)


if __name__ == "__main__":
    main()
