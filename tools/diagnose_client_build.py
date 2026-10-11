"""Safe Windows CLIENT EXE builder with a persistent, readable diagnostic log.

Does not modify source, licensing keys, OWNER/ADMIN outputs or current working
customer EXEs. Builds to a separate directory and verifies the actual EXE.
"""
from __future__ import annotations
import datetime
import importlib
import os
from pathlib import Path
import platform
import shutil
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[1]
LOG_DIR = ROOT / "build_logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)
STAMP = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
LOG = LOG_DIR / f"CLIENT_EXE_BUILD_{STAMP}.log"
DIST = ROOT / "dist_client_diagnostic"
WORK = ROOT / "build_client_diagnostic"
EXE = DIST / "ARCHIPRO UZ.exe"

class BuildFailure(Exception):
    pass

def say(message: str) -> None:
    text = str(message)
    print(text, flush=True)
    with LOG.open("a", encoding="utf-8") as f:
        f.write(text + "\n")

def run_step(label: str, command: list[str]) -> None:
    say("\n" + "=" * 68)
    say(label)
    say(" ".join(command))
    say("=" * 68)
    started = time.monotonic()
    try:
        child = subprocess.Popen(
            command, cwd=str(ROOT), stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT, text=True, encoding="utf-8",
            errors="replace", bufsize=1,
        )
    except OSError as exc:
        raise BuildFailure(f"{label}: Cannot start process: {exc}") from exc
    assert child.stdout is not None
    with LOG.open("a", encoding="utf-8") as f:
        for line in child.stdout:
            print(line, end="", flush=True)
            f.write(line)
    code = child.wait()
    say(f"[STEP EXIT CODE] {code}; duration {time.monotonic()-started:.0f} seconds")
    if code:
        raise BuildFailure(f"{label}: failed with exit code {code}. See {LOG}")

def main() -> int:
    say("ARCHIPRO UZ — ASOSIY MIJOZ DASTURI WINDOWS EXE BUILD")
    say(f"Project: {ROOT}")
    say(f"Python executable: {sys.executable}")
    say(f"Python version: {sys.version.split()[0]}; {platform.architecture()[0]}")
    say(f"OS: {platform.platform()}")
    say(f"LOG: {LOG}")
    if sys.platform != "win32":
        say("[ERROR] Windows EXE is built only under Windows, not this OS.")
        return 1
    source = ROOT / "app" / "main.py"
    builder = ROOT / "app" / "tools" / "build_client.py"
    verifier = ROOT / "app" / "tools" / "verify_built_exe.py"
    audit = ROOT / "app" / "tools" / "full_audit.py"
    figures = ROOT / "app" / "courses" / "visual_assets"
    for path in (source, builder, verifier, audit, figures, ROOT / "archipro.ico"):
        if not path.exists():
            say(f"[ERROR] Missing required project component: {path}")
            say("Download the newest full GitHub ZIP, extract ALL contents, and retry.")
            return 1
    usage = shutil.disk_usage(ROOT)
    say(f"Free disk space: {usage.free/1024**3:.2f} GiB")
    if usage.free < 3 * 1024**3:
        say("[WARNING] Free up 3-5 GB of disk space before building.")
    try:
        for package in ("PyInstaller", "PySide6", "cryptography"):
            try:
                mod = importlib.import_module(package)
                say(f"[DEPENDENCY] {package}: available ({getattr(mod, '__version__', 'installed')})")
            except (ImportError, OSError) as exc:
                say(f"[INFO] {package} unavailable: {exc}. Installing requirements.")
                run_step("INSTALL PYTHON DEPENDENCIES",
                    [sys.executable, "-m", "pip", "install", "-r", "requirements.txt", "pyinstaller"])
                break
        # NEVER skip the audits for software intended to be sold.
        run_step("STEP 1/3 — FULL SOURCE AND COURSE AUDIT",
                 [sys.executable, str(audit)])
        run_step("STEP 2/3 — BUILD ACTUAL CUSTOMER EXE",
                 [sys.executable, str(builder),
                  "--workpath", str(WORK), "--distpath", str(DIST),
                  "--specpath", str(ROOT)])
        if not EXE.is_file() or EXE.stat().st_size < 100000:
            raise BuildFailure(f"PyInstaller ended, but EXE is missing/too small: {EXE}")
        say(f"[EXE EXISTS] {EXE}; {EXE.stat().st_size/1024**2:.1f} MiB")
        run_step("STEP 3/3 — VERIFY ACTUAL 680-LESSON EXECUTABLE",
                 [sys.executable, str(verifier), str(EXE)])
        canonical = ROOT / "dist_client" / "ARCHIPRO UZ.exe"
        if canonical.is_file():
            say("[SAFE] Existing dist_client EXE was NOT overwritten.")
            say(f"[READY] New verified EXE: {EXE}")
        else:
            canonical.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(EXE, canonical)
            say(f"[READY] dist_client\\ARCHIPRO UZ.exe ({canonical.stat().st_size/1024**2:.1f} MiB)")
        say("[PASS] MAIN ARCHIPRO UZ EXECUTABLE CREATED AND VERIFIED.")
        say("[SECURITY] OWNER.exe, ADMIN.exe and private signing key were not packaged.")
        return 0
    except (BuildFailure, OSError, Exception) as exc:
        say(f"\n[FAILED] {type(exc).__name__}: {exc}")
        say(f"Share the last 25-40 lines of this log for exact diagnosis: {LOG}")
        say("PKG is an INTERMEDIATE build file — not the executable.")
        say("Existing OWNER, ADMIN, licensing and working customer executables were not modified.")
        return 1

if __name__ == "__main__":
    raise SystemExit(main())
