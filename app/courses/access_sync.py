from database.database import get_connection


# ============================================================
# ACCESS SYNCHRONIZATION
# ============================================================

def synchronize_user_access(
    user_id: int,
):
    """
    Foydalanuvchining Level va dars access holatini
    database bilan sinxronlashtiradi.

    Bu ayniqsa yangi kontent keyinroq qo'shilganda kerak.

    Misol:

    User LEVEL 1 ni oldin tugatgan.
    LEVEL 2 available bo'lgan.
    Lekin o'sha paytda LEVEL 2 darslari hali database'da yo'q edi.

    Keyinchalik LEVEL 2 darslari qo'shilsa,
    ushbu funksiya LEVEL 2 ning birinchi tugallanmagan
    darsini avtomatik available qiladi.
    """

    connection = get_connection()

    try:
        cursor = connection.cursor()

        # ----------------------------------------------------
        # AVAILABLE LEVELS
        # ----------------------------------------------------

        cursor.execute(
            """
            SELECT
                course_levels.id AS level_id,
                course_levels.code,
                course_levels.sort_order,
                user_level_progress.status

            FROM user_level_progress

            INNER JOIN course_levels
                ON course_levels.id =
                   user_level_progress.level_id

            WHERE user_level_progress.user_id = ?
              AND user_level_progress.status = 'available'

            ORDER BY
                course_levels.sort_order ASC
            """,
            (
                user_id,
            ),
        )

        available_levels = (
            cursor.fetchall()
        )

        for level in available_levels:

            level_id = (
                level["level_id"]
            )

            # ------------------------------------------------
            # Shu Level ichida hozir available dars bormi?
            # ------------------------------------------------

            cursor.execute(
                """
                SELECT
                    lesson_progress.id

                FROM lesson_progress

                INNER JOIN lessons
                    ON lessons.id =
                       lesson_progress.lesson_id

                INNER JOIN course_modules
                    ON course_modules.id =
                       lessons.module_id

                WHERE lesson_progress.user_id = ?
                  AND course_modules.level_id = ?
                  AND lesson_progress.status = 'available'

                LIMIT 1
                """,
                (
                    user_id,
                    level_id,
                ),
            )

            already_available = (
                cursor.fetchone()
            )

            if already_available is not None:
                continue

            # ------------------------------------------------
            # Birinchi tugallanmagan darsni topamiz.
            # ------------------------------------------------

            cursor.execute(
                """
                SELECT
                    lessons.id

                FROM lessons

                INNER JOIN course_modules
                    ON course_modules.id =
                       lessons.module_id

                LEFT JOIN lesson_progress
                    ON lesson_progress.lesson_id =
                       lessons.id
                    AND lesson_progress.user_id = ?

                WHERE course_modules.level_id = ?
                  AND lessons.is_required = 1
                  AND (
                        lesson_progress.status IS NULL
                        OR lesson_progress.status != 'completed'
                      )

                ORDER BY
                    course_modules.sort_order ASC,
                    lessons.sort_order ASC

                LIMIT 1
                """,
                (
                    user_id,
                    level_id,
                ),
            )

            first_incomplete = (
                cursor.fetchone()
            )

            if first_incomplete is None:
                continue

            lesson_id = (
                first_incomplete["id"]
            )

            # Agar progress yozuvi bo'lmasa yaratamiz.
            cursor.execute(
                """
                INSERT OR IGNORE INTO lesson_progress (
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

            # Agar locked bo'lsa available qilamiz.
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
                    lesson_id,
                ),
            )

        connection.commit()

    finally:
        connection.close()
