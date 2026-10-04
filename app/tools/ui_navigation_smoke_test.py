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

# Audit headless ishlaydi. Rendering emas, real Qt signal/callback
# va QStackedWidget navigation kontrakti tekshiriladi.
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

from courses.course_service import (
    get_learning_overview,
)

from ui.app_shell import (
    AppShell,
)

from ui.learning_page import (
    LearningPage,
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


def get_first_lesson(
    user_id: int,
) -> dict:
    overview = get_learning_overview(
        user_id
    )

    assert_true(
        bool(
            overview
        ),
        "Learning overview bo'sh.",
    )

    modules = overview[0].get(
        "modules",
        [],
    )

    assert_true(
        bool(
            modules
        ),
        "LEVEL_00 modullari topilmadi.",
    )

    lessons = modules[0].get(
        "lessons",
        [],
    )

    assert_true(
        bool(
            lessons
        ),
        "L00_M01 darslari topilmadi.",
    )

    lesson = dict(
        lessons[0]
    )

    lesson[
        "level_title"
    ] = overview[0].get(
        "title",
        "",
    )

    lesson[
        "module_title"
    ] = modules[0].get(
        "title",
        "",
    )

    return lesson


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

        # ====================================================
        # 1. REAL OCHISH BUTTON -> LEARNINGPAGE CALLBACK
        # ====================================================

        callback_calls = []

        def capture_open(
            lesson_data,
            source_page,
        ):
            callback_calls.append(
                (
                    dict(
                        lesson_data
                    ),
                    source_page,
                )
            )

        isolated_page = LearningPage(
            user=user,
            focus_level_codes=[
                "LEVEL_00"
            ],
            custom_title=(
                "LEVEL 00 • Absolute Zero"
            ),
            custom_subtitle=(
                "Arxitekturaga mutlaqo noldan kirish"
            ),
            open_lesson_callback=(
                capture_open
            ),
        )

        open_button = isolated_page.findChild(
            QPushButton,
            "openLesson",
        )

        assert_true(
            open_button is not None,
            "OCHISH tugmasi topilmadi.",
        )

        assert_true(
            open_button.isEnabled(),
            "OCHISH tugmasi disabled.",
        )

        open_button.click()
        app.processEvents()

        assert_true(
            len(
                callback_calls
            )
            == 1,
            (
                "OCHISH tugmasi LearningPage callback'ini "
                "aniq bir marta chaqirmadi."
            ),
        )

        captured_lesson, captured_source = (
            callback_calls[0]
        )

        assert_true(
            int(
                captured_lesson.get(
                    "id",
                    0,
                )
            )
            == lesson_id,
            "OCHISH noto'g'ri lesson ID uzatdi.",
        )

        assert_true(
            captured_source
            is isolated_page,
            "OCHISH noto'g'ri source page uzatdi.",
        )

        # ====================================================
        # 2. APPSHELL LEVEL -> LESSONPAGE
        # ====================================================

        shell = AppShell(
            user
        )

        shell.open_single_level(
            "LEVEL_00",
            "Absolute Zero",
            "Arxitekturaga mutlaqo noldan kirish",
            "home",
        )

        app.processEvents()

        level_key = (
            "level::LEVEL_00"
        )

        assert_true(
            shell.current_page_key
            == level_key,
            "Level sahifasi ochilmadi.",
        )

        level_page = shell.page_cache.get(
            level_key
        )

        assert_true(
            level_page is not None,
            "LearningPage cache'da topilmadi.",
        )

        shell_button = level_page.findChild(
            QPushButton,
            "openLesson",
        )

        assert_true(
            shell_button is not None,
            "Shell ichidagi OCHISH tugmasi topilmadi.",
        )

        shell_button.click()
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
                "Shell ichidagi OCHISH tugmasi "
                "LessonPage ga o'tmadi."
            ),
        )

        lesson_page = shell.page_cache.get(
            lesson_key
        )

        assert_true(
            lesson_page is not None,
            "LessonPage cache'da topilmadi.",
        )

        assert_true(
            int(
                lesson_page.lesson.get(
                    "id",
                    0,
                )
            )
            == lesson_id,
            "Shell noto'g'ri darsni ochdi.",
        )

        assert_true(
            shell.stack.currentWidget()
            is lesson_page,
            "QStackedWidget LessonPage ni active qilmadi.",
        )

        # ====================================================
        # 3. BACK CONTRACT
        # ====================================================

        assert_true(
            callable(
                lesson_page.back_callback
            ),
            "Lesson back callback ulanmagan.",
        )

        lesson_page.back_callback()
        app.processEvents()

        assert_true(
            shell.current_page_key
            == level_key,
            "Darsdan Levelga qaytish ishlamadi.",
        )

        assert_true(
            shell.stack.currentWidget()
            is level_page,
            "QStackedWidget LevelPage ga qaytmadi.",
        )

        # ====================================================
        # 4. SOURCE DATA CONTRACT
        # ====================================================

        lesson = get_first_lesson(
            user["id"]
        )

        assert_true(
            lesson.get(
                "status"
            )
            in {
                "available",
                "completed",
            },
            "Birinchi dars ochiq statusda emas.",
        )

        print(
            "[PASS] OCHISH button -> LearningPage callback"
        )
        print(
            "[PASS] Lesson payload/source contract"
        )
        print(
            "[PASS] AppShell Level -> LessonPage"
        )
        print(
            "[PASS] QStackedWidget active lesson"
        )
        print(
            "[PASS] Lesson -> Level back navigation"
        )
        print(
            "[PASS] First lesson unlock contract"
        )
        print()
        print(
            "UI NAVIGATION SMOKE TEST: PASSED"
        )

        isolated_page.deleteLater()
        shell.close()

        return 0

    except Exception as exc:
        traceback.print_exc()

        print()
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
