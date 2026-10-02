from datetime import datetime

from database.database import get_connection


# ============================================================
# LEVELS
# ============================================================

def get_all_levels():
    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT *
            FROM course_levels
            ORDER BY sort_order ASC
            """
        )

        return [
            dict(row)
            for row in cursor.fetchall()
        ]

    finally:
        connection.close()


def get_current_level(
    user_id: int,
):
    """
    Foydalanuvchining hozirgi ochiq Level'ini qaytaradi.

    Agar barcha Level'lar tugagan bo'lsa,
    oxirgi tugallangan Level qaytariladi.
    """

    connection = get_connection()

    try:
        cursor = connection.cursor()

        # Avval AVAILABLE Level qidiramiz.
        cursor.execute(
            """
            SELECT
                course_levels.id,
                course_levels.code,
                course_levels.title,
                course_levels.subtitle,
                course_levels.sort_order,
                user_level_progress.status

            FROM user_level_progress

            INNER JOIN course_levels
                ON course_levels.id =
                   user_level_progress.level_id

            WHERE user_level_progress.user_id = ?
              AND user_level_progress.status = 'available'

            ORDER BY course_levels.sort_order ASC

            LIMIT 1
            """,
            (
                user_id,
            ),
        )

        row = cursor.fetchone()

        if row is not None:
            return dict(row)

        # Agar available yo'q bo'lsa,
        # oxirgi completed Level.
        cursor.execute(
            """
            SELECT
                course_levels.id,
                course_levels.code,
                course_levels.title,
                course_levels.subtitle,
                course_levels.sort_order,
                user_level_progress.status

            FROM user_level_progress

            INNER JOIN course_levels
                ON course_levels.id =
                   user_level_progress.level_id

            WHERE user_level_progress.user_id = ?
              AND user_level_progress.status = 'completed'

            ORDER BY course_levels.sort_order DESC

            LIMIT 1
            """,
            (
                user_id,
            ),
        )

        row = cursor.fetchone()

        if row is None:
            return None

        return dict(row)

    finally:
        connection.close()


# ============================================================
# MODULES
# ============================================================

def get_modules_for_level(
    level_id: int,
):
    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT *
            FROM course_modules
            WHERE level_id = ?
            ORDER BY sort_order ASC
            """,
            (
                level_id,
            ),
        )

        return [
            dict(row)
            for row in cursor.fetchall()
        ]

    finally:
        connection.close()


# ============================================================
# LESSONS
# ============================================================

def get_lessons_for_module(
    module_id: int,
):
    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT *
            FROM lessons
            WHERE module_id = ?
            ORDER BY sort_order ASC
            """,
            (
                module_id,
            ),
        )

        return [
            dict(row)
            for row in cursor.fetchall()
        ]

    finally:
        connection.close()


# ============================================================
# USER LESSON PROGRESS
# ============================================================

def initialize_user_progress(
    user_id: int,
):
    """
    Database'dagi barcha darslar uchun
    foydalanuvchi progress yozuvlarini yaratadi.

    Faqat birinchi dars boshida ochiq bo'ladi.
    """

    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT
                lessons.id

            FROM lessons

            INNER JOIN course_modules
                ON course_modules.id =
                   lessons.module_id

            INNER JOIN course_levels
                ON course_levels.id =
                   course_modules.level_id

            ORDER BY
                course_levels.sort_order ASC,
                course_modules.sort_order ASC,
                lessons.sort_order ASC
            """
        )

        lessons = cursor.fetchall()

        for index, lesson in enumerate(
            lessons
        ):
            status = (
                "available"
                if index == 0
                else "locked"
            )

            cursor.execute(
                """
                INSERT OR IGNORE INTO lesson_progress (
                    user_id,
                    lesson_id,
                    status
                )
                VALUES (?, ?, ?)
                """,
                (
                    user_id,
                    lesson["id"],
                    status,
                ),
            )

        connection.commit()

    finally:
        connection.close()


# ============================================================
# XP + STATISTICS
# ============================================================

def get_user_course_stats(
    user_id: int,
):
    """
    Umumiy progress va XP.

    XP tarkibi:
    1. Tugallangan darslar XP
    2. Muvaffaqiyatli tugallangan Level imtihonlari XP
    """

    connection = get_connection()

    try:
        cursor = connection.cursor()

        # ----------------------------------------------------
        # TOTAL LESSONS
        # ----------------------------------------------------

        cursor.execute(
            """
            SELECT COUNT(*) AS total
            FROM lesson_progress
            WHERE user_id = ?
            """,
            (
                user_id,
            ),
        )

        total = cursor.fetchone()[
            "total"
        ]

        # ----------------------------------------------------
        # COMPLETED LESSONS
        # ----------------------------------------------------

        cursor.execute(
            """
            SELECT COUNT(*) AS completed
            FROM lesson_progress
            WHERE user_id = ?
              AND status = 'completed'
            """,
            (
                user_id,
            ),
        )

        completed = cursor.fetchone()[
            "completed"
        ]

        # ----------------------------------------------------
        # LESSON XP
        # ----------------------------------------------------

        cursor.execute(
            """
            SELECT
                COALESCE(
                    SUM(lessons.xp_reward),
                    0
                ) AS lesson_xp

            FROM lesson_progress

            INNER JOIN lessons
                ON lessons.id =
                   lesson_progress.lesson_id

            WHERE lesson_progress.user_id = ?
              AND lesson_progress.status = 'completed'
            """,
            (
                user_id,
            ),
        )

        lesson_xp = cursor.fetchone()[
            "lesson_xp"
        ]

        # ----------------------------------------------------
        # EXAM XP
        #
        # user_level_progress completed bo'lsa,
        # shu Level imtihoni XP'si faqat bir marta hisoblanadi.
        # ----------------------------------------------------

        cursor.execute(
            """
            SELECT
                COALESCE(
                    SUM(level_exams.xp_reward),
                    0
                ) AS exam_xp

            FROM user_level_progress

            INNER JOIN level_exams
                ON level_exams.level_id =
                   user_level_progress.level_id

            WHERE user_level_progress.user_id = ?
              AND user_level_progress.status = 'completed'
              AND level_exams.is_active = 1
            """,
            (
                user_id,
            ),
        )

        exam_xp = cursor.fetchone()[
            "exam_xp"
        ]

        total_xp = (
            int(lesson_xp)
            + int(exam_xp)
        )

        if total == 0:
            progress_percent = 0

        else:
            progress_percent = round(
                (
                    completed
                    / total
                )
                * 100
            )

        return {
            "total_lessons": total,
            "completed_lessons": completed,
            "progress_percent": progress_percent,
            "lesson_xp": int(lesson_xp),
            "exam_xp": int(exam_xp),
            "xp": total_xp,
        }

    finally:
        connection.close()


# ============================================================
# NEXT LESSON
# ============================================================

def get_next_available_lesson(
    user_id: int,
):
    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT
                lessons.id,
                lessons.code,
                lessons.title,
                lessons.lesson_type,
                lessons.summary,
                lessons.estimated_minutes,
                lessons.xp_reward,
                lessons.passing_score,

                course_modules.id AS module_id,
                course_modules.title AS module_title,

                course_levels.id AS level_id,
                course_levels.code AS level_code,
                course_levels.title AS level_title

            FROM lesson_progress

            INNER JOIN lessons
                ON lessons.id =
                   lesson_progress.lesson_id

            INNER JOIN course_modules
                ON course_modules.id =
                   lessons.module_id

            INNER JOIN course_levels
                ON course_levels.id =
                   course_modules.level_id

            LEFT JOIN user_level_progress
                ON user_level_progress.level_id =
                   course_levels.id
                AND user_level_progress.user_id = ?

            WHERE lesson_progress.user_id = ?
              AND lesson_progress.status = 'available'

              AND (
                    user_level_progress.status = 'available'
                    OR course_levels.sort_order = 0
                  )

            ORDER BY
                course_levels.sort_order ASC,
                course_modules.sort_order ASC,
                lessons.sort_order ASC

            LIMIT 1
            """,
            (
                user_id,
                user_id,
            ),
        )

        row = cursor.fetchone()

        if row is None:
            return None

        return dict(row)

    finally:
        connection.close()


# ============================================================
# COMPLETE LESSON
# ============================================================

def complete_lesson(
    user_id: int,
    lesson_id: int,
) -> dict:
    """
    Darsni completed qiladi va shu Level ichidagi
    keyingi darsni ochadi.

    Level tugagandan keyin keyingi Level darsi
    avtomatik ochilmaydi.

    Keyingi Level faqat Final Exam orqali ochiladi.
    """

    connection = get_connection()

    try:
        cursor = connection.cursor()

        now = datetime.now().isoformat(
            timespec="seconds"
        )

        # ----------------------------------------------------
        # CURRENT LESSON
        # ----------------------------------------------------

        cursor.execute(
            """
            SELECT
                lesson_progress.status,
                course_modules.level_id

            FROM lesson_progress

            INNER JOIN lessons
                ON lessons.id =
                   lesson_progress.lesson_id

            INNER JOIN course_modules
                ON course_modules.id =
                   lessons.module_id

            WHERE lesson_progress.user_id = ?
              AND lesson_progress.lesson_id = ?

            LIMIT 1
            """,
            (
                user_id,
                lesson_id,
            ),
        )

        current = cursor.fetchone()

        if current is None:
            return {
                "success": False,
                "message": "Dars progressi topilmadi.",
            }

        if current["status"] == "completed":
            return {
                "success": True,
                "message": "Dars allaqachon tugatilgan.",
            }

        current_level_id = (
            current["level_id"]
        )

        # ----------------------------------------------------
        # COMPLETE CURRENT LESSON
        # ----------------------------------------------------

        cursor.execute(
            """
            UPDATE lesson_progress

            SET
                status = 'completed',
                completed_at = ?,
                last_opened_at = ?

            WHERE user_id = ?
              AND lesson_id = ?
            """,
            (
                now,
                now,
                user_id,
                lesson_id,
            ),
        )

        # ----------------------------------------------------
        # CURRENT LEVEL LESSON ORDER
        # ----------------------------------------------------

        cursor.execute(
            """
            SELECT
                lessons.id

            FROM lessons

            INNER JOIN course_modules
                ON course_modules.id =
                   lessons.module_id

            WHERE course_modules.level_id = ?

            ORDER BY
                course_modules.sort_order ASC,
                lessons.sort_order ASC
            """,
            (
                current_level_id,
            ),
        )

        level_lessons = (
            cursor.fetchall()
        )

        next_lesson_id = None
        found_current = False

        for row in level_lessons:

            if found_current:
                next_lesson_id = (
                    row["id"]
                )
                break

            if row["id"] == lesson_id:
                found_current = True

        # ----------------------------------------------------
        # FAQAT SHU LEVEL ICHIDAGI KEYINGI DARS OCHILADI
        # ----------------------------------------------------

        if next_lesson_id is not None:

            cursor.execute(
                """
                UPDATE lesson_progress
                SET status = 'available'

                WHERE user_id = ?
                  AND lesson_id = ?
                  AND status = 'locked'
                """,
                (
                    user_id,
                    next_lesson_id,
                ),
            )

        connection.commit()

        return {
            "success": True,
            "message": "Dars muvaffaqiyatli tugatildi.",
            "next_lesson_id": next_lesson_id,
        }

    finally:
        connection.close()


# ============================================================
# LEARNING OVERVIEW
# ============================================================

def get_learning_overview(
    user_id: int,
):
    """
    LEVEL
      -> MODULE
          -> LESSON

    strukturasini foydalanuvchi progressi bilan qaytaradi.
    """

    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT
                course_levels.*,

                COALESCE(
                    user_level_progress.status,
                    'locked'
                ) AS level_status,

                COALESCE(
                    user_level_progress.best_exam_score,
                    0
                ) AS best_exam_score,

                COALESCE(
                    user_level_progress.exam_attempts,
                    0
                ) AS exam_attempts

            FROM course_levels

            LEFT JOIN user_level_progress
                ON user_level_progress.level_id =
                   course_levels.id
                AND user_level_progress.user_id = ?

            ORDER BY
                course_levels.sort_order ASC
            """,
            (
                user_id,
            ),
        )

        levels = []

        for level_row in cursor.fetchall():

            level = dict(
                level_row
            )

            cursor.execute(
                """
                SELECT *
                FROM course_modules
                WHERE level_id = ?
                ORDER BY sort_order ASC
                """,
                (
                    level["id"],
                ),
            )

            modules = []

            for module_row in cursor.fetchall():

                module = dict(
                    module_row
                )

                cursor.execute(
                    """
                    SELECT
                        lessons.id,
                        lessons.code,
                        lessons.title,
                        lessons.lesson_type,
                        lessons.summary,
                        lessons.estimated_minutes,
                        lessons.xp_reward,
                        lessons.passing_score,

                        COALESCE(
                            lesson_progress.status,
                            'locked'
                        ) AS status,

                        COALESCE(
                            lesson_progress.best_score,
                            0
                        ) AS best_score

                    FROM lessons

                    LEFT JOIN lesson_progress
                        ON lesson_progress.lesson_id =
                           lessons.id
                        AND lesson_progress.user_id = ?

                    WHERE lessons.module_id = ?

                    ORDER BY
                        lessons.sort_order ASC
                    """,
                    (
                        user_id,
                        module["id"],
                    ),
                )

                lessons = [
                    dict(row)
                    for row in cursor.fetchall()
                ]

                # Agar Level locked bo'lsa,
                # uning barcha darslarini UI uchun
                # locked qilib ko'rsatamiz.
                if (
                    level["level_status"]
                    == "locked"
                ):
                    for lesson in lessons:
                        lesson["status"] = (
                            "locked"
                        )

                module[
                    "lessons"
                ] = lessons

                total_lessons = len(
                    lessons
                )

                completed_lessons = sum(
                    1
                    for lesson in lessons
                    if (
                        lesson["status"]
                        == "completed"
                    )
                )

                if total_lessons > 0:

                    module[
                        "progress_percent"
                    ] = round(
                        (
                            completed_lessons
                            / total_lessons
                        )
                        * 100
                    )

                else:
                    module[
                        "progress_percent"
                    ] = 0

                module[
                    "completed_lessons"
                ] = completed_lessons

                module[
                    "total_lessons"
                ] = total_lessons

                modules.append(
                    module
                )

            level[
                "modules"
            ] = modules

            level_total = sum(
                module[
                    "total_lessons"
                ]
                for module in modules
            )

            level_completed = sum(
                module[
                    "completed_lessons"
                ]
                for module in modules
            )

            if level_total > 0:

                level[
                    "progress_percent"
                ] = round(
                    (
                        level_completed
                        / level_total
                    )
                    * 100
                )

            else:
                level[
                    "progress_percent"
                ] = 0

            level[
                "completed_lessons"
            ] = level_completed

            level[
                "total_lessons"
            ] = level_total

            levels.append(
                level
            )

        return levels

    finally:
        connection.close()
