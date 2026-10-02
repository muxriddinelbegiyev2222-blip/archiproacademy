import random
from datetime import datetime

from database.database import (
    get_connection,
)


def seed_level_exams():
    """
    Har bir Level uchun yakuniy imtihon
    yozuvlarini yaratadi.

    Hozir LEVEL 0 faol ishlatiladi.
    Keyinchalik qolgan Level'lar ham
    shu tizimdan foydalanadi.
    """

    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT id
            FROM course_levels
            WHERE code = 'LEVEL_00'
            LIMIT 1
            """
        )

        level = cursor.fetchone()

        if level is None:
            return

        cursor.execute(
            """
            INSERT OR IGNORE INTO level_exams (
                level_id,
                title,
                description,
                question_count,
                passing_score,
                xp_reward,
                is_active
            )
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (
                level["id"],
                "LEVEL 0 YAKUNIY IMTIHON",
                (
                    "Arxitektura bo'yicha boshlang'ich "
                    "bilimlarni tekshiruvchi yakuniy imtihon."
                ),
                20,
                85,
                200,
                1,
            ),
        )

        connection.commit()

    finally:
        connection.close()


def initialize_user_levels(
    user_id: int,
):
    """
    Foydalanuvchi uchun barcha Level progressini yaratadi.

    LEVEL 0 ochiq.
    Qolganlari locked.
    """

    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT
                id,
                sort_order
            FROM course_levels
            ORDER BY sort_order ASC
            """
        )

        levels = cursor.fetchall()

        for index, level in enumerate(
            levels
        ):
            if index == 0:
                status = "available"
            else:
                status = "locked"

            cursor.execute(
                """
                INSERT OR IGNORE INTO user_level_progress (
                    user_id,
                    level_id,
                    status
                )
                VALUES (?, ?, ?)
                """,
                (
                    user_id,
                    level["id"],
                    status,
                ),
            )

        connection.commit()

    finally:
        connection.close()


def get_level_exam(
    level_code: str,
):
    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT
                level_exams.*,
                course_levels.code AS level_code,
                course_levels.title AS level_title

            FROM level_exams

            INNER JOIN course_levels
                ON course_levels.id = level_exams.level_id

            WHERE course_levels.code = ?
              AND level_exams.is_active = 1

            LIMIT 1
            """,
            (
                level_code,
            ),
        )

        row = cursor.fetchone()

        if row is None:
            return None

        return dict(
            row
        )

    finally:
        connection.close()


def are_all_level_lessons_completed(
    user_id: int,
    level_id: int,
) -> bool:
    """
    Level ichidagi barcha majburiy darslar
    tugatilganmi yoki yo'qmi tekshiradi.
    """

    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT COUNT(*) AS total

            FROM lessons

            INNER JOIN course_modules
                ON course_modules.id = lessons.module_id

            WHERE course_modules.level_id = ?
              AND lessons.is_required = 1
            """,
            (
                level_id,
            ),
        )

        total = cursor.fetchone()[
            "total"
        ]

        if total == 0:
            return False

        cursor.execute(
            """
            SELECT COUNT(*) AS completed

            FROM lesson_progress

            INNER JOIN lessons
                ON lessons.id = lesson_progress.lesson_id

            INNER JOIN course_modules
                ON course_modules.id = lessons.module_id

            WHERE lesson_progress.user_id = ?
              AND course_modules.level_id = ?
              AND lessons.is_required = 1
              AND lesson_progress.status = 'completed'
            """,
            (
                user_id,
                level_id,
            ),
        )

        completed = cursor.fetchone()[
            "completed"
        ]

        return completed == total

    finally:
        connection.close()


def get_exam_questions(
    exam_id: int,
):
    """
    Level ichidagi barcha mini-test savollaridan
    yakuniy imtihon savollarini tasodifiy tanlaydi.
    """

    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT
                level_exams.question_count,
                level_exams.level_id
            FROM level_exams
            WHERE id = ?
            LIMIT 1
            """,
            (
                exam_id,
            ),
        )

        exam = cursor.fetchone()

        if exam is None:
            return []

        question_count = exam[
            "question_count"
        ]

        level_id = exam[
            "level_id"
        ]

        cursor.execute(
            """
            SELECT
                quiz_questions.id,
                quiz_questions.code,
                quiz_questions.question_text,
                quiz_questions.explanation

            FROM quiz_questions

            INNER JOIN lessons
                ON lessons.id = quiz_questions.lesson_id

            INNER JOIN course_modules
                ON course_modules.id = lessons.module_id

            WHERE course_modules.level_id = ?
            """,
            (
                level_id,
            ),
        )

        question_rows = [
            dict(row)
            for row in cursor.fetchall()
        ]

        random.shuffle(
            question_rows
        )

        selected_questions = (
            question_rows[
                :question_count
            ]
        )

        result = []

        for question in selected_questions:

            cursor.execute(
                """
                SELECT
                    id,
                    option_text,
                    is_correct
                FROM quiz_options
                WHERE question_id = ?
                """,
                (
                    question["id"],
                ),
            )

            options = [
                dict(row)
                for row in cursor.fetchall()
            ]

            random.shuffle(
                options
            )

            question[
                "options"
            ] = options

            result.append(
                question
            )

        return result

    finally:
        connection.close()


def save_level_exam_attempt(
    user_id: int,
    exam_id: int,
    score: int,
    correct_answers: int,
    total_questions: int,
    passed: bool,
):
    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            INSERT INTO level_exam_attempts (
                user_id,
                exam_id,
                score,
                correct_answers,
                total_questions,
                passed
            )
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (
                user_id,
                exam_id,
                score,
                correct_answers,
                total_questions,
                1 if passed else 0,
            ),
        )

        cursor.execute(
            """
            SELECT level_id
            FROM level_exams
            WHERE id = ?
            LIMIT 1
            """,
            (
                exam_id,
            ),
        )

        exam = cursor.fetchone()

        if exam is None:
            connection.commit()
            return

        level_id = exam[
            "level_id"
        ]

        cursor.execute(
            """
            UPDATE user_level_progress

            SET
                exam_attempts = exam_attempts + 1,

                best_exam_score =
                    CASE
                        WHEN best_exam_score < ?
                        THEN ?
                        ELSE best_exam_score
                    END

            WHERE user_id = ?
              AND level_id = ?
            """,
            (
                score,
                score,
                user_id,
                level_id,
            ),
        )

        if passed:
            now = datetime.now().isoformat(
                timespec="seconds"
            )

            cursor.execute(
                """
                UPDATE user_level_progress
                SET
                    status = 'completed',
                    completed_at = ?
                WHERE user_id = ?
                  AND level_id = ?
                """,
                (
                    now,
                    user_id,
                    level_id,
                ),
            )

            cursor.execute(
                """
                SELECT
                    id,
                    sort_order
                FROM course_levels
                WHERE id = ?
                LIMIT 1
                """,
                (
                    level_id,
                ),
            )

            current_level = (
                cursor.fetchone()
            )

            if current_level is not None:

                cursor.execute(
                    """
                    SELECT id
                    FROM course_levels
                    WHERE sort_order > ?
                    ORDER BY sort_order ASC
                    LIMIT 1
                    """,
                    (
                        current_level[
                            "sort_order"
                        ],
                    ),
                )

                next_level = (
                    cursor.fetchone()
                )

                if next_level is not None:
                    cursor.execute(
                        """
                        UPDATE user_level_progress
                        SET status = 'available'
                        WHERE user_id = ?
                          AND level_id = ?
                          AND status = 'locked'
                        """,
                        (
                            user_id,
                            next_level["id"],
                        ),
                    )

        connection.commit()

    finally:
        connection.close()


def get_level_exam_stats(
    user_id: int,
    level_code: str,
):
    """
    Level imtihoni bo'yicha foydalanuvchining
    eng yaxshi natijasini qaytaradi.
    """

    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT
                user_level_progress.status,
                user_level_progress.best_exam_score,
                user_level_progress.exam_attempts

            FROM user_level_progress

            INNER JOIN course_levels
                ON course_levels.id =
                   user_level_progress.level_id

            WHERE user_level_progress.user_id = ?
              AND course_levels.code = ?

            LIMIT 1
            """,
            (
                user_id,
                level_code,
            ),
        )

        row = cursor.fetchone()

        if row is None:
            return {
                "status": "locked",
                "best_exam_score": 0,
                "exam_attempts": 0,
            }

        return dict(
            row
        )

    finally:
        connection.close()
