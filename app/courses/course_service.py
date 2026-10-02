from database.database import get_connection


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


def get_modules_for_level(level_id: int):
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
            (level_id,),
        )

        return [
            dict(row)
            for row in cursor.fetchall()
        ]

    finally:
        connection.close()


def get_lessons_for_module(module_id: int):
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
            (module_id,),
        )

        return [
            dict(row)
            for row in cursor.fetchall()
        ]

    finally:
        connection.close()


def initialize_user_progress(user_id: int):
    """
    Foydalanuvchi uchun barcha mavjud darslarning
    progress yozuvlarini yaratadi.

    Eng birinchi dars avtomatik ochiq bo'ladi.
    Qolganlari locked holatda turadi.
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
                ON course_modules.id = lessons.module_id

            INNER JOIN course_levels
                ON course_levels.id = course_modules.level_id

            ORDER BY
                course_levels.sort_order ASC,
                course_modules.sort_order ASC,
                lessons.sort_order ASC
            """
        )

        lessons = cursor.fetchall()

        for index, lesson in enumerate(lessons):

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


def get_user_course_stats(user_id: int):
    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT COUNT(*) AS total
            FROM lesson_progress
            WHERE user_id = ?
            """,
            (user_id,),
        )

        total = cursor.fetchone()["total"]

        cursor.execute(
            """
            SELECT COUNT(*) AS completed
            FROM lesson_progress
            WHERE user_id = ?
              AND status = 'completed'
            """,
            (user_id,),
        )

        completed = cursor.fetchone()["completed"]

        if total == 0:
            progress_percent = 0
        else:
            progress_percent = round(
                (completed / total) * 100
            )

        return {
            "total_lessons": total,
            "completed_lessons": completed,
            "progress_percent": progress_percent,
        }

    finally:
        connection.close()


def get_next_available_lesson(user_id: int):
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

                course_modules.title AS module_title,

                course_levels.title AS level_title

            FROM lesson_progress

            INNER JOIN lessons
                ON lessons.id = lesson_progress.lesson_id

            INNER JOIN course_modules
                ON course_modules.id = lessons.module_id

            INNER JOIN course_levels
                ON course_levels.id = course_modules.level_id

            WHERE lesson_progress.user_id = ?
              AND lesson_progress.status = 'available'

            ORDER BY
                course_levels.sort_order ASC,
                course_modules.sort_order ASC,
                lessons.sort_order ASC

            LIMIT 1
            """,
            (user_id,),
        )

        row = cursor.fetchone()

        if row is None:
            return None

        return dict(row)

    finally:
        connection.close()
