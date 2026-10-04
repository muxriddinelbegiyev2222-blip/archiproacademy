"""Run the actual Windows EXE and fail packaging if embedded lessons are missing."""
import json
from pathlib import Path
import subprocess
import sys
import tempfile


def main():
    executable = Path(sys.argv[1]).resolve()
    with tempfile.TemporaryDirectory(prefix="archipro_exe_check_") as directory:
        report_path = Path(directory) / "curriculum.json"
        result = subprocess.run([str(executable), "--verify-curriculum", str(report_path)],
                                timeout=180, check=False)
        if result.returncode != 0 or not report_path.is_file():
            raise RuntimeError("Built EXE could not load its curriculum")
        report = json.loads(report_path.read_text(encoding="utf-8"))
        if not (report.get("success") and report.get("frozen") and
                report.get("lessons") == 680 and report.get("quizzes") == 680 and
                report.get("first_lesson_blocks") == 7):
            raise RuntimeError("Built EXE curriculum verification failed: " + str(report))
        print("[PASS] Built EXE: 680 lessons, 680 quizzes, first lesson 7 blocks; v" + report["version"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
