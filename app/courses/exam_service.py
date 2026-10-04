import random
from datetime import datetime

from database.database import get_connection


# ============================================================
# FINAL EXAM CONFIGURATION
# ============================================================

LEVEL_EXAM_CONFIGS = [
    {
        "level_code": "LEVEL_00",
        "title": "BOSQICH 00 YAKUNIY IMTIHON",
        "description": (
            "Arxitektura bo'yicha boshlang'ich bilimlarni "
            "tekshiruvchi yakuniy imtihon."
        ),
        "question_count": 20,
        "passing_score": 85,
        "xp_reward": 200,
    },
    {
        "level_code": "LEVEL_01",
        "title": "BOSQICH 01 YAKUNIY IMTIHON",
        "description": (
            "Kompozitsiya, proporsiya, ritm, simmetriya, "
            "asimmetriya, forma, hajm va arxitektura "
            "uslublari bo'yicha yakuniy bilim nazorati."
        ),
        "question_count": 30,
        "passing_score": 85,
        "xp_reward": 300,
    },
]


# ============================================================
# EXAM SEED
# ============================================================

def seed_level_exams():
    """
    LEVEL_EXAM_CONFIGS ichidagi barcha
    Final Exam'larni database'ga yaratadi yoki yangilaydi.
    """

    connection = get_connection()

    try:
        cursor = connection.cursor()

        for config in LEVEL_EXAM_CONFIGS:

            cursor.execute(
                """
                SELECT id
                FROM course_levels
                WHERE code = ?
                LIMIT 1
                """,
                (
                    config["level_code"],
                ),
            )

            level = cursor.fetchone()

            if level is None:
                continue

            level_id = level["id"]

            cursor.execute(
                """
                INSERT INTO level_exams (
                    level_id,
                    title,
                    description,
                    question_count,
                    passing_score,
                    xp_reward,
                    is_active
                )
                VALUES (?, ?, ?, ?, ?, ?, 1)

                ON CONFLICT(level_id)
                DO UPDATE SET
                    title = excluded.title,
                    description = excluded.description,
                    question_count = excluded.question_count,
                    passing_score = excluded.passing_score,
                    xp_reward = excluded.xp_reward,
                    is_active = excluded.is_active
                """,
                (
                    level_id,
                    config["title"],
                    config["description"],
                    config["question_count"],
                    config["passing_score"],
                    config["xp_reward"],
                ),
            )

        connection.commit()

    finally:
        connection.close()


# ============================================================
# USER LEVEL PROGRESS
# ============================================================

def initialize_user_levels(
    user_id: int,
):
    """
    Foydalanuvchi uchun barcha Level progresslarini yaratadi.

    LEVEL 0 boshida available.
    Qolgan Level'lar locked.

    Mavjud progress yozuvlari o'zgartirilmaydi.
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
            status = (
                "available"
                if index == 0
                else "locked"
            )

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


# ============================================================
# GET LEVEL EXAM
# ============================================================

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
                ON course_levels.id =
                   level_exams.level_id

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


# ============================================================
# CHECK LEVEL LESSONS
# ============================================================

def are_all_level_lessons_completed(
    user_id: int,
    level_id: int,
) -> bool:
    """
    Level ichidagi barcha majburiy darslar
    tugallanganmi yoki yo'qmi tekshiradi.
    """

    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT
                COUNT(*) AS total

            FROM lessons

            INNER JOIN course_modules
                ON course_modules.id =
                   lessons.module_id

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
            SELECT
                COUNT(*) AS completed

            FROM lesson_progress

            INNER JOIN lessons
                ON lessons.id =
                   lesson_progress.lesson_id

            INNER JOIN course_modules
                ON course_modules.id =
                   lessons.module_id

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

        return (
            completed == total
        )

    finally:
        connection.close()


# ============================================================
# GET EXAM QUESTIONS
# ============================================================

def get_exam_questions(
    exam_id: int,
):
    """
    Shu Level ichidagi barcha mini-test savollaridan
    Final Exam uchun tasodifiy savollar tanlaydi.

    Har urinishda:
    - savollar aralashadi;
    - javob variantlari ham aralashadi.
    """

    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT
                question_count,
                level_id

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
                ON lessons.id =
                   quiz_questions.lesson_id

            INNER JOIN course_modules
                ON course_modules.id =
                   lessons.module_id

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


# ============================================================
# UNLOCK FIRST LESSON OF NEXT LEVEL
# ============================================================

def unlock_first_lesson_of_level(
    cursor,
    user_id: int,
    level_id: int,
):
    """
    Level ochilganda uning eng birinchi darsini
    ham available qiladi.
    """

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

        LIMIT 1
        """,
        (
            level_id,
        ),
    )

    first_lesson = (
        cursor.fetchone()
    )

    # LEVEL ichida hali dars yaratilmagan bo'lsa,
    # hech narsa qilmaymiz.
    if first_lesson is None:
        return

    lesson_id = (
        first_lesson["id"]
    )

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


# ============================================================
# SAVE FINAL EXAM ATTEMPT
# ============================================================

def save_level_exam_attempt(
    user_id: int,
    exam_id: int,
    score: int,
    correct_answers: int,
    total_questions: int,
    passed: bool,
):
    """
    Final Exam natijasini saqlaydi.

    O'tganda:
    1. Hozirgi Level completed.
    2. Keyingi Level available.
    3. Keyingi Level'ning birinchi darsi available.
    """

    connection = get_connection()

    try:
        cursor = connection.cursor()

        # ----------------------------------------------------
        # ATTEMPT HISTORY
        # ----------------------------------------------------

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

        # ----------------------------------------------------
        # GET CURRENT LEVEL
        # ----------------------------------------------------

        cursor.execute(
            """
            SELECT
                level_id

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

        level_id = (
            exam["level_id"]
        )

        # ----------------------------------------------------
        # UPDATE ATTEMPTS + BEST SCORE
        # ----------------------------------------------------

        cursor.execute(
            """
            UPDATE user_level_progress

            SET
                exam_attempts =
                    exam_attempts + 1,

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

        # ----------------------------------------------------
        # PASSED
        # ----------------------------------------------------

        if passed:

            now = datetime.now().isoformat(
                timespec="seconds"
            )

            # Current Level completed.
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

            # Current Level sort order.
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

                # Next Level.
                cursor.execute(
                    """
                    SELECT
                        id,
                        code,
                        title,
                        sort_order

                    FROM course_levels

                    WHERE sort_order > ?

                    ORDER BY
                        sort_order ASC

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

                    next_level_id = (
                        next_level["id"]
                    )

                    # Next Level status.
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
                            next_level_id,
                        ),
                    )

                    # Agar progress yozuvi qandaydir
                    # sabab bilan bo'lmasa, yaratamiz.
                    cursor.execute(
                        """
                        INSERT OR IGNORE INTO user_level_progress (
                            user_id,
                            level_id,
                            status
                        )
                        VALUES (?, ?, 'available')
                        """,
                        (
                            user_id,
                            next_level_id,
                        ),
                    )

                    # Next Level'da dars mavjud bo'lsa,
                    # birinchi darsni ochamiz.
                    unlock_first_lesson_of_level(
                        cursor=cursor,
                        user_id=user_id,
                        level_id=next_level_id,
                    )

        connection.commit()

    finally:
        connection.close()


# ============================================================
# EXAM STATS
# ============================================================

def get_level_exam_stats(
    user_id: int,
    level_code: str,
):
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
