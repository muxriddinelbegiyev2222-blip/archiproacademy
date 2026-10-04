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
    ('PROJECT AUDIT', 'project_audit.py'),
    ('DATABASE AUDIT', 'database_audit.py'),
    ('RUNTIME SMOKE TEST', 'runtime_smoke_test.py'),
    ('CUSTOMER FEATURES SMOKE TEST', 'customer_features_smoke_test.py'),
    ('UI NAVIGATION SMOKE TEST', 'ui_navigation_smoke_test.py'),
    ('LEARNING FLOW SMOKE TEST', 'learning_flow_smoke_test.py'),
    ('RELEASE REGRESSION TEST', 'release_regression_test.py'),
]


def main():
    log_dir = PROJECT / 'audit_logs' / datetime.now().strftime('%Y%m%d_%H%M%S_%f')
    log_dir.mkdir(parents=True, exist_ok=True)
    results = []
    env = dict(os.environ, PYTHONIOENCODING='utf-8', PYTHONUNBUFFERED='1')
    for index, (title, filename) in enumerate(CHECKS, 1):
        print(f'\n{index}/{len(CHECKS)} - {title}', flush=True)
        log = log_dir / filename.replace('.py', '.log')
        try:
            with log.open('w', encoding='utf-8') as output:
                process = subprocess.run([sys.executable, str(TOOLS / filename)], cwd=PROJECT,
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
