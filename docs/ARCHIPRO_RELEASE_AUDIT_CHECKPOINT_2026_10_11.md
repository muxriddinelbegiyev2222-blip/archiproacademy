# ARCHIPRO UZ — release audit checkpoint (2026-10-11)

## Scope and evidence
- Checked GitHub `main` source tree and recent GitHub Actions run/job metadata.
- Static metadata checks: 680 unique lesson IDs in each of the three coverage CSVs; image names in those CSVs and all three figure JSON registries resolve to tracked assets.
- 125 previously selected lessons reference their named replacement JPEGs. Rework manifest: 125 replaced, 31 image-optional, 0 pending out of the 156 reviewed subset.
- GitHub tree contains 449 JPEGs and no JPEG exceeds 400000 bytes.
- Compression registry: 278 converted records, 0 blocked, `complete=true`. The registry itself was inspected, but its full on-disk hash validation still needs a working runner.
- The 31-image local backup ZIP was independently decoded: 31/31 JPEGs opened successfully, matched its SHA-256/size/dimension manifest, and were under 400000 bytes.
- No tracked `archipro_private.key`, `.env`, `private_key.pem`, or user SQLite DB detected in the GitHub tree.

## Changes committed
1. Added `tools/verify_source_integrity.py`: Python compilation/syntax inventory (no execution), checks required files and accidental key/environment files.
2. `app/tools/full_audit.py` now runs **11 checks**, including source integrity, compact media with `--require-complete`, image metadata, content guard, project/database/runtime/customer/UI/learning and full curriculum release regression. Logs and exit codes are preserved.
3. `app/licensing/license_service.py` rejects non-object JSON input safely. `app/tools/release_regression_test.py` adds invalid-input cases.
4. GitHub Actions now checks source compilation and content guard, enforces repaired media completeness, and makes the package job depend on the audit job succeeding.
5. `BUILD_RELEASE.bat` now invokes the full 11-check audit instead of its narrower set of individual smoke tests. Its existing content guard and post-build EXE verification remain.

## Important limitation — NOT production certified
At the latest inspected GitHub Actions runs the audit job fails in approximately 4 seconds **with no steps or job logs**, while packaging is skipped. A successful 2026-10-09 run executed audit/package steps, but it predates recent changes. This points to a runner/account/scheduling problem that cannot be diagnosed from repository source alone. **The exact GitHub-side reason is not confirmed.**

Consequently:
- The 11 checks were **not executed on the updated commit** in a Windows environment.
- Full 680-lesson interactive flow, login/activation, local data upgrade/backup, and Windows GUI smoke checks are **not yet certified** for the current HEAD.
- The current Windows EXE and installer have **not** been rebuilt and verified from the latest commit.
- Static file existence and hashes do not prove image pedagogical correctness or full release reliability.
- No claim of zero remaining bugs is made.

## Required release sign-off
1. In GitHub Actions inspect the failed `ARCHIPRO CI` run message/banner and account Actions usage/billing/quota/settings; restore execution of hosted jobs. The repository connector does not expose the account billing/error banner.
2. Run the updated `ARCHIPRO CI` audit to a real green result (all steps, not merely a status or skipped job).
3. On Windows run `AUDIT_ARCHIPRO.bat` and inspect each log under `audit_logs/`; fix any reported regression and repeat.
4. Trigger the CI workflow manually only after audit is functional; its package job now depends on audit. Verify `dist/ARCHIPRO UZ.exe` against `verify_built_exe.py`.
5. Verify real customer license activation, login, full quiz progression, backups/recovery, offline display, installer/upgrade/uninstall in a clean Windows user account. Never bundle the private signing key.
6. Release only when checks and user acceptance pass; retain the last known-good version and do not overwrite it blindly.

**Status: STATIC INSPECTION IMPROVED; WINDOWS RELEASE VERIFICATION BLOCKED.**
