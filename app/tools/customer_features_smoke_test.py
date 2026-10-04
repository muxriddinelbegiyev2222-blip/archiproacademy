from __future__ import annotations

import atexit
import os
import shutil
import sys
import tempfile
from pathlib import Path


CURRENT_FILE = Path(__file__).resolve()
TOOLS_DIR = CURRENT_FILE.parent
APP_DIR = TOOLS_DIR.parent

if str(APP_DIR) not in sys.path:
    sys.path.insert(
        0,
        str(APP_DIR),
    )


TEMP_DIR = Path(
    tempfile.mkdtemp(
        prefix="archipro_customer_features_"
    )
)

DB_PATH = (
    TEMP_DIR
    / "features_test.db"
)

os.environ[
    "ARCHIPRO_UZ_DATABASE_PATH"
] = str(
    DB_PATH
)


def _cleanup() -> None:
    shutil.rmtree(
        TEMP_DIR,
        ignore_errors=True,
    )


atexit.register(
    _cleanup
)


from database.database import (
    get_connection,
    initialize_database,
)

from courses.user_features import (
    export_user_backup,
    get_bookmarked_lesson_ids,
    get_lesson_note,
    get_recent_lessons,
    get_user_notes_map,
    import_user_backup,
    mark_lesson_opened,
    save_lesson_note,
    set_lesson_bookmark,
)


def seed_minimal_data() -> tuple[int, int]:
    initialize_database()

    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            INSERT INTO users (
                username,
                password_hash,
                password_salt,
                full_name,
                license_type,
                is_active
            )
            VALUES (?, ?, ?, ?, 'PRO', 1)
            """,
            (
                "feature_test",
                "dummy_hash",
                "dummy_salt",
                "Feature Test",
            ),
        )

        user_id = int(
            cursor.lastrowid
        )

        cursor.execute(
            """
            INSERT INTO course_levels (
                code,
                title,
                subtitle,
                sort_order
            )
            VALUES (
                'LEVEL_00',
                'Test Level',
                'Test subtitle',
                0
            )
            """
        )

        level_id = int(
            cursor.lastrowid
        )

        cursor.execute(
            """
            INSERT INTO course_modules (
                level_id,
                code,
                title,
                sort_order
            )
            VALUES (
                ?,
                'L00_M01',
                'Test Module',
                1
            )
            """,
            (
                level_id,
            ),
        )

        module_id = int(
            cursor.lastrowid
        )

        cursor.execute(
            """
            INSERT INTO lessons (
                module_id,
                code,
                title,
                lesson_type,
                summary,
                sort_order,
                estimated_minutes,
                xp_reward,
                passing_score,
                is_required,
                is_active
            )
            VALUES (
                ?,
                'L00_M01_001',
                'Test Lesson',
                'theory',
                'Test summary',
                1,
                10,
                10,
                80,
                1,
                1
            )
            """,
            (
                module_id,
            ),
        )

        lesson_id = int(
            cursor.lastrowid
        )

        cursor.execute(
            """
            INSERT INTO lesson_progress (
                user_id,
                lesson_id,
                status
            )
            VALUES (?, ?, 'available')
            """,
            (
                user_id,
                lesson_id,
            ),
        )

        cursor.execute(
            """
            INSERT INTO user_level_progress (
                user_id,
                level_id,
                status
            )
            VALUES (?, ?, 'available')
            """,
            (
                user_id,
                level_id,
            ),
        )

        connection.commit()

        return (
            user_id,
            lesson_id,
        )

    finally:
        connection.close()


def assert_true(
    condition,
    message: str,
) -> None:
    if not condition:
        raise AssertionError(
            message
        )


def main() -> int:
    print()
    print(
        "============================================================"
    )
    print(
        "ARCHIPRO UZ - CUSTOMER FEATURES SMOKE TEST"
    )
    print(
        "============================================================"
    )
    print()

    try:
        user_id, lesson_id = (
            seed_minimal_data()
        )

        mark_lesson_opened(
            user_id,
            lesson_id,
        )

        recent = get_recent_lessons(
            user_id,
            limit=5,
        )

        assert_true(
            len(
                recent
            )
            == 1,
            "Recent lesson ishlamadi.",
        )

        set_lesson_bookmark(
            user_id,
            lesson_id,
            True,
        )

        bookmarks = (
            get_bookmarked_lesson_ids(
                user_id
            )
        )

        assert_true(
            lesson_id
            in bookmarks,
            "Bookmark saqlanmadi.",
        )

        save_lesson_note(
            user_id,
            lesson_id,
            "Test shaxsiy eslatma",
        )

        assert_true(
            get_lesson_note(
                user_id,
                lesson_id,
            )
            == "Test shaxsiy eslatma",
            "Lesson note saqlanmadi.",
        )

        notes = get_user_notes_map(
            user_id
        )

        assert_true(
            notes.get(
                lesson_id
            )
            == "Test shaxsiy eslatma",
            "Notes index ishlamadi.",
        )

        backup_path = (
            TEMP_DIR
            / "test.archiprobackup"
        )

        export_user_backup(
            user_id,
            backup_path,
        )

        assert_true(
            backup_path.exists(),
            "Backup yaratilmagan.",
        )

        backup_text = (
            backup_path.read_text(
                encoding="utf-8"
            )
        )

        assert_true(
            "password_hash"
            not in backup_text,
            "Backup ichiga password hash tushib qolgan.",
        )

        assert_true(
            "password_salt"
            not in backup_text,
            "Backup ichiga password salt tushib qolgan.",
        )

        connection = get_connection()

        try:
            cursor = connection.cursor()

            cursor.execute(
                """
                DELETE FROM lesson_bookmarks
                WHERE user_id = ?
                """,
                (
                    user_id,
                ),
            )

            cursor.execute(
                """
                DELETE FROM lesson_notes
                WHERE user_id = ?
                """,
                (
                    user_id,
                ),
            )

            connection.commit()

        finally:
            connection.close()

        import_user_backup(
            user_id,
            backup_path,
        )

        assert_true(
            lesson_id
            in get_bookmarked_lesson_ids(
                user_id
            ),
            "Backup bookmarkni tiklamadi.",
        )

        assert_true(
            get_lesson_note(
                user_id,
                lesson_id,
            )
            == "Test shaxsiy eslatma",
            "Backup eslatmani tiklamadi.",
        )

        print(
            "[PASS] Recent lessons"
        )
        print(
            "[PASS] Bookmark"
        )
        print(
            "[PASS] Personal notes"
        )
        print(
            "[PASS] Backup export"
        )
        print(
            "[PASS] Backup restore"
        )
        print(
            "[PASS] Credential exclusion"
        )
        print()
        print(
            "CUSTOMER FEATURES SMOKE TEST: PASSED"
        )

        return 0

    except Exception as exc:
        print(
            "[FAIL] "
            + str(
                exc
            )
        )
        print()
        print(
            "CUSTOMER FEATURES SMOKE TEST: FAILED"
        )

        return 1


if __name__ == "__main__":
    raise SystemExit(
        main()
    )
