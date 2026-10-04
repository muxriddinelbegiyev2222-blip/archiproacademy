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
        prefix="archipro_learning_flow_"
    )
)

DB_PATH = (
    TEMP_DIR
    / "learning_flow.db"
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

from courses.course_service import (
    complete_lesson,
    get_learning_overview,
)

from courses.quiz_service import (
    get_best_quiz_score,
    save_quiz_attempt,
)


def assert_true(
    condition,
    message: str,
) -> None:
    if not condition:
        raise AssertionError(
            message
        )


def seed_flow_data() -> tuple[int, int, int]:
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
                "flow_test",
                "dummy_hash",
                "dummy_salt",
                "Learning Flow Test",
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
                'Flow test',
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
                'Flow module',
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

        lesson_ids = []

        for index, title in enumerate(
            [
                "Birinchi dars",
                "Ikkinchi dars",
            ],
            start=1,
        ):
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
                VALUES (?, ?, ?, 'theory', '', ?, 10, 10, 80, 1, 1)
                """,
                (
                    module_id,
                    f"L00_M01_{index:03d}",
                    title,
                    index,
                ),
            )

            lesson_ids.append(
                int(
                    cursor.lastrowid
                )
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

        for index, lesson_id in enumerate(
            lesson_ids
        ):
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
                VALUES (?, ?, ?, 0, 0, 0)
                """,
                (
                    user_id,
                    lesson_id,
                    (
                        "available"
                        if index == 0
                        else "locked"
                    ),
                ),
            )

        connection.commit()

        return (
            user_id,
            lesson_ids[0],
            lesson_ids[1],
        )

    finally:
        connection.close()


def get_progress(
    user_id: int,
    lesson_id: int,
) -> dict:
    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT
                status,
                score,
                best_score,
                attempts,
                completed_at
            FROM lesson_progress
            WHERE user_id = ?
              AND lesson_id = ?
            LIMIT 1
            """,
            (
                user_id,
                lesson_id,
            ),
        )

        row = cursor.fetchone()

        return (
            dict(
                row
            )
            if row is not None
            else {}
        )

    finally:
        connection.close()


def main() -> int:
    print()
    print(
        "============================================================"
    )
    print(
        "ARCHIPRO UZ - LEARNING FLOW SMOKE TEST"
    )
    print(
        "============================================================"
    )
    print()

    try:
        user_id, first_id, second_id = (
            seed_flow_data()
        )

        # Failed quiz: birinchi dars ochiq qoladi,
        # ikkinchi dars ochilmasligi shart.
        save_quiz_attempt(
            user_id=user_id,
            lesson_id=first_id,
            score=60,
            passed=False,
        )

        failed_progress = get_progress(
            user_id,
            first_id,
        )

        assert_true(
            failed_progress.get(
                "status"
            )
            == "available",
            "Failed mini-test darsni noto'g'ri completed qildi.",
        )

        overview = get_learning_overview(
            user_id
        )

        lessons = (
            overview[0][
                "modules"
            ][0][
                "lessons"
            ]
        )

        assert_true(
            lessons[1][
                "status"
            ]
            == "locked",
            "Failed mini-testdan keyin keyingi dars ochilib ketdi.",
        )

        # Passed quiz: natija darhol saqlanishi shart.
        save_quiz_attempt(
            user_id=user_id,
            lesson_id=first_id,
            score=90,
            passed=True,
        )

        passed_progress = get_progress(
            user_id,
            first_id,
        )

        assert_true(
            passed_progress.get(
                "status"
            )
            == "completed",
            "Passed mini-test dars progressini darhol saqlamadi.",
        )

        assert_true(
            int(
                passed_progress.get(
                    "attempts",
                    0,
                )
            )
            == 2,
            "Quiz attempt soni noto'g'ri.",
        )

        assert_true(
            int(
                passed_progress.get(
                    "best_score",
                    0,
                )
            )
            == 90,
            "Best mini-test score noto'g'ri.",
        )

        # Access sync keyingi darsni ochishi kerak.
        overview = get_learning_overview(
            user_id
        )

        lessons = (
            overview[0][
                "modules"
            ][0][
                "lessons"
            ]
        )

        assert_true(
            lessons[1][
                "status"
            ]
            == "available",
            "Passed mini-testdan keyin keyingi dars ochilmadi.",
        )

        # UI continue yakunlash chaqirig'i attemptni yana oshirmasligi kerak.
        complete_lesson(
            user_id,
            first_id,
            score=get_best_quiz_score(
                user_id,
                first_id,
            ),
        )

        final_progress = get_progress(
            user_id,
            first_id,
        )

        assert_true(
            int(
                final_progress.get(
                    "attempts",
                    0,
                )
            )
            == 2,
            "Lesson completion quiz attemptni ikki marta sanadi.",
        )

        assert_true(
            int(
                final_progress.get(
                    "best_score",
                    0,
                )
            )
            == 90,
            "Lesson completion real quiz score'ni buzdi.",
        )

        print(
            "[PASS] Failed quiz keeps next lesson locked"
        )
        print(
            "[PASS] Passed quiz persists immediately"
        )
        print(
            "[PASS] Passed quiz unlocks next lesson"
        )
        print(
            "[PASS] Real score preserved"
        )
        print(
            "[PASS] Attempts are not double-counted"
        )
        print()
        print(
            "LEARNING FLOW SMOKE TEST: PASSED"
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
            "LEARNING FLOW SMOKE TEST: FAILED"
        )

        return 1


if __name__ == "__main__":
    raise SystemExit(
        main()
    )
