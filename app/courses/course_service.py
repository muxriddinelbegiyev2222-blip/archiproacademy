from datetime import datetime

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

        return [dict(row) for row in cursor.fetchall()]

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

        return [dict(row) for row in cursor.fetchall()]

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

        return [dict(row) for row in cursor.fetchall()]

    finally:
        connection.close()


def initialize_user_progress(user_id: int):
    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT lessons.id
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
            status = "available" if index == 0 else "locked"

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

        cursor.execute(
            """
            SELECT COALESCE(SUM(lessons.xp_reward), 0) AS xp
            FROM lesson_progress
            INNER JOIN lessons
                ON lessons.id = lesson_progress.lesson_id
            WHERE lesson_progress.user_id = ?
              AND lesson_progress.status = 'completed'
            """,
            (user_id,),
        )

        xp = cursor.fetchone()["xp"]

        progress_percent = 0

        if total > 0:
            progress_percent = round(
                (completed / total) * 100
            )

        return {
            "total_lessons": total,
            "completed_lessons": completed,
            "progress_percent": progress_percent,
            "xp": xp,
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
                lessons.xp_reward,

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


def complete_lesson(
    user_id: int,
    lesson_id: int,
) -> dict:
    connection = get_connection()

    try:
        cursor = connection.cursor()

        now = datetime.now().isoformat(
            timespec="seconds"
        )

        cursor.execute(
            """
            SELECT *
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

        progress = cursor.fetchone()

        if progress is None:
            return {
                "success": False,
                "message": "Progress topilmadi.",
            }

        if progress["status"] == "completed":
            return {
                "success": True,
                "message": "Bu dars allaqachon tugatilgan.",
            }

        cursor.execute(
            """
            UPDATE lesson_progress
            SET
                status = 'completed',
                score = 100,
                best_score = CASE
                    WHEN best_score < 100 THEN 100
                    ELSE best_score
                END,
                attempts = attempts + 1,
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

        cursor.execute(
            """
            SELECT
                lessons.id
            FROM lessons

            INNER JOIN course_modules
                ON course_modules.id = lessons.module_id

            INNER JOIN course_levels
                ON course_levels.id = course_modules.level_id

            WHERE lessons.id != ?

            ORDER BY
                course_levels.sort_order ASC,
                course_modules.sort_order ASC,
                lessons.sort_order ASC
            """
            ,
            (lesson_id,),
        )

        all_other_lessons = cursor.fetchall()

        current_order_query = """
            SELECT
                course_levels.sort_order AS level_order,
                course_modules.sort_order AS module_order,
                lessons.sort_order AS lesson_order
            FROM lessons

            INNER JOIN course_modules
                ON course_modules.id = lessons.module_id

            INNER JOIN course_levels
                ON course_levels.id = course_modules.level_id

            WHERE lessons.id = ?
        """

        cursor.execute(
            current_order_query,
            (lesson_id,),
        )

        current_order = cursor.fetchone()

        cursor.execute(
            """
            SELECT
                lessons.id,
                course_levels.sort_order AS level_order,
                course_modules.sort_order AS module_order,
                lessons.sort_order AS lesson_order
            FROM lessons

            INNER JOIN course_modules
                ON course_modules.id = lessons.module_id

            INNER JOIN course_levels
                ON course_levels.id = course_modules.level_id

            ORDER BY
                level_order ASC,
                module_order ASC,
                lesson_order ASC
            """
        )

        ordered_lessons = cursor.fetchall()

        next_lesson_id = None

        found_current = False

        for row in ordered_lessons:
            if found_current:
                next_lesson_id = row["id"]
                break

            if row["id"] == lesson_id:
                found_current = True

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
