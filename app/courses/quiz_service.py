from database.database import get_connection
from courses.quiz_data import QUIZ_DATA


def seed_quizzes():
    connection = get_connection()

    try:
        cursor = connection.cursor()

        for lesson_code, questions in QUIZ_DATA.items():
            cursor.execute(
                """
                SELECT id
                FROM lessons
                WHERE code = ?
                """,
                (lesson_code,),
            )

            lesson = cursor.fetchone()

            if lesson is None:
                continue

            lesson_id = lesson["id"]

            for question_index, question in enumerate(
                questions,
                start=1,
            ):
                cursor.execute(
                    """
                    INSERT OR IGNORE INTO quiz_questions (
                        lesson_id,
                        code,
                        question_text,
                        explanation,
                        sort_order
                    )
                    VALUES (?, ?, ?, ?, ?)
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
                    """,
                    (question["code"],),
                )

                question_row = cursor.fetchone()

                if question_row is None:
                    continue

                question_id = question_row["id"]

                for option_key, option_text, is_correct in question["options"]:
                    cursor.execute(
                        """
                        INSERT OR IGNORE INTO quiz_options (
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


def get_quiz_for_lesson(lesson_id: int):
    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT *
            FROM quiz_questions
            WHERE lesson_id = ?
            ORDER BY sort_order ASC
            """,
            (lesson_id,),
        )

        question_rows = cursor.fetchall()

        quiz = []

        for question_row in question_rows:
            question = dict(question_row)

            cursor.execute(
                """
                SELECT
                    id,
                    option_key,
                    option_text,
                    is_correct
                FROM quiz_options
                WHERE question_id = ?
                ORDER BY option_key ASC
                """,
                (question["id"],),
            )

            question["options"] = [
                dict(row)
                for row in cursor.fetchall()
            ]

            quiz.append(question)

        return quiz

    finally:
        connection.close()


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

        cursor.execute(
            """
            UPDATE lesson_progress
            SET
                attempts = attempts + 1,
                score = ?,
                best_score = CASE
                    WHEN best_score < ? THEN ?
                    ELSE best_score
                END
            WHERE user_id = ?
              AND lesson_id = ?
            """,
            (
                score,
                score,
                score,
                user_id,
                lesson_id,
            ),
        )

        connection.commit()

    finally:
        connection.close()
