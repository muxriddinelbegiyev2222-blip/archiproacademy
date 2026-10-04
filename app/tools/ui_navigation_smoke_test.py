from __future__ import annotations

import atexit
import os
import shutil
import sys
import tempfile
import traceback
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
        prefix="archipro_ui_navigation_"
    )
)

DB_PATH = (
    TEMP_DIR
    / "ui_navigation.db"
)

os.environ[
    "ARCHIPRO_UZ_DATABASE_PATH"
] = str(
    DB_PATH
)

# GUI test real display talab qilmasin.
os.environ.setdefault(
    "QT_QPA_PLATFORM",
    "offscreen",
)


def _cleanup() -> None:
    shutil.rmtree(
        TEMP_DIR,
        ignore_errors=True,
    )


atexit.register(
    _cleanup
)


from PySide6.QtWidgets import (
    QApplication,
    QPushButton,
)

from database.database import (
    get_connection,
    initialize_database,
)

from ui.dashboard_window import (
    DashboardWindow,
)


def assert_true(
    condition,
    message: str,
) -> None:
    if not condition:
        raise AssertionError(
            message
        )


def seed_navigation_data() -> tuple[dict, int]:
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
                "ui_nav_test",
                "dummy_hash",
                "dummy_salt",
                "UI Navigation Test",
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
                sort_order,
                is_active
            )
            VALUES (
                'LEVEL_00',
                'Absolute Zero',
                'Arxitekturaga mutlaqo noldan kirish',
                0,
                1
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
                sort_order,
                is_active
            )
            VALUES (
                ?,
                'L00_M01',
                'Arxitektura bilan tanishuv',
                1,
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
                'Arxitektura nima?',
                'theory',
                'UI navigation test lesson',
                1,
                15,
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
            INSERT INTO user_level_progress (
                user_id,
                level_id,
                status,
                best_exam_score,
                exam_attempts
            )
            VALUES (?, ?, 'available', 0, 0)
            """,
            (
                user_id,
                level_id,
            ),
        )

        cursor.execute(
            """
            INSERT INTO lesson_progress (
                user_id,
                lesson_id,
                status,
                score,
                best_score,
                attempts
            )
            VALUES (?, ?, 'available', 0, 0, 0)
            """,
            (
                user_id,
                lesson_id,
            ),
        )

        connection.commit()

        return (
            {
                "id": user_id,
                "username": "ui_nav_test",
                "full_name": "UI Navigation Test",
                "license_type": "PRO",
            },
            lesson_id,
        )

    finally:
        connection.close()


def main() -> int:
    print()
    print(
        "============================================================"
    )
    print(
        "ARCHIPRO UZ - UI NAVIGATION SMOKE TEST"
    )
    print(
        "============================================================"
    )
    print()

    app = (
        QApplication.instance()
        or QApplication(
            []
        )
    )

    try:
        user, lesson_id = (
            seed_navigation_data()
        )

        shell = DashboardWindow(
            user
        )

        # Real widget event zanjirini tekshirish uchun shellni
        # offscreen platformda ham ko'rsatilgan holatga o'tkazamiz.
        shell.show()
        app.processEvents()

        shell.open_single_level(
            "LEVEL_00",
            "Absolute Zero",
            "Arxitekturaga mutlaqo noldan kirish",
            "home",
        )

        app.processEvents()

        assert_true(
            shell.current_page_key
            == "level::LEVEL_00",
            "Level sahifasi ochilmadi.",
        )

        level_page = shell.page_cache.get(
            "level::LEVEL_00"
        )

        assert_true(
            level_page
            is not None,
            "LearningPage cache'da topilmadi.",
        )

        open_button = level_page.findChild(
            QPushButton,
            "openLesson",
        )

        assert_true(
            open_button
            is not None,
            "OCHISH tugmasi topilmadi.",
        )

        assert_true(
            open_button.isEnabled(),
            "OCHISH tugmasi disabled.",
        )

        open_button.click()
        app.processEvents()
        QApplication.sendPostedEvents()
        app.processEvents()

        lesson_key = (
            "lesson::"
            + str(
                lesson_id
            )
        )

        assert_true(
            shell.current_page_key
            == lesson_key,
            (
                "OCHISH tugmasi LessonPage ga "
                "navigatsiya qilmadi."
            ),
        )

        lesson_page = shell.page_cache.get(
            lesson_key
        )

        assert_true(
            lesson_page
            is not None,
            "LessonPage cache'da topilmadi.",
        )

        assert_true(
            int(
                lesson_page.lesson[
                    "id"
                ]
            )
            == lesson_id,
            "Noto'g'ri dars ochildi.",
        )

        back_button = lesson_page.findChild(
            QPushButton,
            "backButton",
        )

        assert_true(
            back_button
            is not None,
            "Lesson back tugmasi topilmadi.",
        )

        back_button.click()
        app.processEvents()

        assert_true(
            shell.current_page_key
            == "level::LEVEL_00",
            "Darsdan Levelga qaytish ishlamadi.",
        )

        print(
            "[PASS] Level navigation"
        )
        print(
            "[PASS] OCHISH button signal"
        )
        print(
            "[PASS] LessonPage construction"
        )
        print(
            "[PASS] Lesson cache/navigation"
        )
        print(
            "[PASS] Back navigation"
        )
        print()
        print(
            "UI NAVIGATION SMOKE TEST: PASSED"
        )

        shell.close()

        return 0

    except Exception as exc:
        traceback.print_exc()

        print(
            "[FAIL] "
            + str(
                exc
            )
        )
        print()
        print(
            "UI NAVIGATION SMOKE TEST: FAILED"
        )

        return 1


if __name__ == "__main__":
    raise SystemExit(
        main()
    )
