import random
from datetime import datetime

from database.database import (
    get_connection,
)

from courses.content_registry import (
    get_all_quiz_data,
)


# ============================================================
# QUIZ SEED
# ============================================================

def seed_quizzes():
    """
    Registry ichidagi barcha testlarni
    SQLite database'ga joylashtiradi.
    """

    all_quizzes = (
        get_all_quiz_data()
    )

    connection = get_connection()

    try:
        cursor = connection.cursor()

        for (
            lesson_code,
            questions,
        ) in all_quizzes.items():

            cursor.execute(
                """
                SELECT id
                FROM lessons
                WHERE code = ?
                LIMIT 1
                """,
                (
                    lesson_code,
                ),
            )

            lesson = cursor.fetchone()

            if lesson is None:
                continue

            lesson_id = (
                lesson["id"]
            )

            for (
                question_index,
                question,
            ) in enumerate(
                questions,
                start=1,
            ):

                # Savol mavjud bo'lsa ham,
                # matni keyinchalik yangilanishi mumkin.
                cursor.execute(
                    """
                    INSERT INTO quiz_questions (
                        lesson_id,
                        code,
                        question_text,
                        explanation,
                        sort_order
                    )
                    VALUES (?, ?, ?, ?, ?)

                    ON CONFLICT(code)
                    DO UPDATE SET
                        lesson_id = excluded.lesson_id,
                        question_text = excluded.question_text,
                        explanation = excluded.explanation,
                        sort_order = excluded.sort_order
                    """,
                    (
                        lesson_id,
                        question["code"],
                        question["question"],
                        question["explanation"],
                        question_index,
                    ),
                )

                cursor.execute(
                    """
                    SELECT id
                    FROM quiz_questions
                    WHERE code = ?
                    LIMIT 1
                    """,
                    (
                        question["code"],
                    ),
                )

                question_row = (
                    cursor.fetchone()
                )

                if question_row is None:
                    continue

                question_id = (
                    question_row["id"]
                )

                # Variantlar eski bo'lsa,
                # tozalab qayta yaratamiz.
                cursor.execute(
                    """
                    DELETE FROM quiz_options
                    WHERE question_id = ?
                    """,
                    (
                        question_id,
                    ),
                )

                for (
                    option_key,
                    option_text,
                    is_correct,
                ) in question["options"]:

                    cursor.execute(
                        """
                        INSERT INTO quiz_options (
                            question_id,
                            option_key,
                            option_text,
                            is_correct
                        )
                        VALUES (?, ?, ?, ?)
                        """,
                        (
                            question_id,
                            option_key,
                            option_text,
                            1 if is_correct else 0,
                        ),
                    )

        connection.commit()

    finally:
        connection.close()


# ============================================================
# GET QUIZ
# ============================================================

def get_quiz_for_lesson(
    lesson_id: int,
    shuffle_questions: bool = True,
    shuffle_options: bool = True,
):
    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT *
            FROM quiz_questions

            WHERE lesson_id = ?

            ORDER BY
                sort_order ASC
            """,
            (
                lesson_id,
            ),
        )

        question_rows = (
            cursor.fetchall()
        )

        quiz = []

        for question_row in question_rows:

            question = dict(
                question_row
            )

            cursor.execute(
                """
                SELECT
                    id,
                    option_key,
                    option_text,
                    is_correct

                FROM quiz_options

                WHERE question_id = ?

                ORDER BY
                    option_key ASC
                """,
                (
                    question["id"],
                ),
            )

            options = [
                dict(row)
                for row in cursor.fetchall()
            ]

            if shuffle_options:
                random.shuffle(
                    options
                )

            question[
                "options"
            ] = options

            quiz.append(
                question
            )

        if shuffle_questions:
            random.shuffle(
                quiz
            )

        return quiz

    finally:
        connection.close()


# ============================================================
# SAVE ATTEMPT
# ============================================================

def save_quiz_attempt(
    user_id: int,
    lesson_id: int,
    score: int,
    passed: bool,
):
    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            INSERT INTO quiz_attempts (
                user_id,
                lesson_id,
                score,
                passed
            )
            VALUES (?, ?, ?, ?)
            """,
            (
                user_id,
                lesson_id,
                score,
                1 if passed else 0,
            ),
        )

        completed_at = (
            datetime.now().isoformat(
                timespec="seconds"
            )
            if passed
            else None
        )

        cursor.execute(
            """
            UPDATE lesson_progress

            SET
                attempts = attempts + 1,
                score = ?,

                best_score =
                    CASE
                        WHEN best_score < ?
                        THEN ?
                        ELSE best_score
                    END,

                status =
                    CASE
                        WHEN ? = 1
                        THEN 'completed'
                        ELSE status
                    END,

                completed_at =
                    CASE
                        WHEN ? = 1
                        THEN COALESCE(
                            completed_at,
                            ?
                        )
                        ELSE completed_at
                    END,

                last_opened_at =
                    COALESCE(
                        last_opened_at,
                        ?
                    )

            WHERE user_id = ?
              AND lesson_id = ?
            """,
            (
                score,
                score,
                score,
                1 if passed else 0,
                1 if passed else 0,
                completed_at,
                completed_at,
                user_id,
                lesson_id,
            ),
        )

        connection.commit()

    finally:
        connection.close()


# ============================================================
# QUIZ HISTORY
# ============================================================

def get_quiz_history(
    user_id: int,
    lesson_id: int,
):
    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT
                id,
                score,
                passed,
                created_at

            FROM quiz_attempts

            WHERE user_id = ?
              AND lesson_id = ?

            ORDER BY
                id DESC
            """,
            (
                user_id,
                lesson_id,
            ),
        )

        return [
            dict(row)
            for row in cursor.fetchall()
        ]

    finally:
        connection.close()


# ============================================================
# BEST SCORE
# ============================================================

def get_best_quiz_score(
    user_id: int,
    lesson_id: int,
) -> int:
    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT
                COALESCE(
                    MAX(score),
                    0
                ) AS best_score

            FROM quiz_attempts

            WHERE user_id = ?
              AND lesson_id = ?
            """,
            (
                user_id,
                lesson_id,
            ),
        )

        row = cursor.fetchone()

        if row is None:
            return 0

        return int(
            row["best_score"]
        )

    finally:
        connection.close()
