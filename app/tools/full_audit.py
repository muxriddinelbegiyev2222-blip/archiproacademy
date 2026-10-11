"""Run all release checks with persistent logs, timeouts and real exit codes."""
from __future__ import annotations
import os
from pathlib import Path
import subprocess
import sys
from datetime import datetime

TOOLS = Path(__file__).resolve().parent
PROJECT = TOOLS.parents[1]
CHECKS = [
    ('SOURCE INTEGRITY', 'tools/verify_source_integrity.py'),
    ('COMPACT MEDIA INTEGRITY', 'tools/verify_compact_media.py'),
    ('LESSON IMAGE INTEGRITY', 'tools/verify_course_visuals.py'),
    ('CONTENT GUARD', 'app/tools/content_guard.py'),
    ('PROJECT AUDIT', 'app/tools/project_audit.py'),
    ('DATABASE AUDIT', 'app/tools/database_audit.py'),
    ('RUNTIME SMOKE TEST', 'app/tools/runtime_smoke_test.py'),
    ('CUSTOMER FEATURES SMOKE TEST', 'app/tools/customer_features_smoke_test.py'),
    ('UI NAVIGATION SMOKE TEST', 'app/tools/ui_navigation_smoke_test.py'),
    ('LEARNING FLOW SMOKE TEST', 'app/tools/learning_flow_smoke_test.py'),
    ('RELEASE REGRESSION TEST', 'app/tools/release_regression_test.py'),
]


def main():
    log_dir = PROJECT / 'audit_logs' / datetime.now().strftime('%Y%m%d_%H%M%S_%f')
    log_dir.mkdir(parents=True, exist_ok=True)
    results = []
    env = dict(os.environ, PYTHONIOENCODING='utf-8', PYTHONUNBUFFERED='1')
    env.setdefault('QT_QPA_PLATFORM', 'offscreen')  # automated UI smoke checks
    for index, (title, filename) in enumerate(CHECKS, 1):
        print(f'\n{index}/{len(CHECKS)} - {title}', flush=True)
        log = log_dir / Path(filename).name.replace('.py', '.log')
        try:
            with log.open('w', encoding='utf-8') as output:
                command = [sys.executable, str(PROJECT / filename)]
                if filename == 'tools/verify_compact_media.py':
                    command.append('--require-complete')
                process = subprocess.run(command, cwd=PROJECT,
                                         env=env, stdout=output, stderr=subprocess.STDOUT, timeout=600)
            code = process.returncode
        except (OSError, subprocess.TimeoutExpired) as exc:
            code = 1
            with log.open('a', encoding='utf-8') as output:
                output.write(f'\n[ERROR] {exc}\n')
        results.append((title, code))
        print(log.read_text(encoding='utf-8', errors='replace'), flush=True)
    print('\nFINAL AUDIT RESULT')
    for title, code in results:
        print(f"[{'PASS' if code == 0 else 'FAIL'}] {title} (exit code: {code})")
    success = all(code == 0 for _, code in results)
    print('ARCHIPRO UZ FULL AUDIT ' + ('MUVAFFAQIYATLI YAKUNLANDI' if success else 'XATOLAR BILAN YAKUNLANDI'))
    print(f'Audit logs: {log_dir}')
    return 0 if success else 1


if __name__ == '__main__':
    raise SystemExit(main())
