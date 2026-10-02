from database.database import get_connection


# ============================================================
# LEVEL 4 FINAL EXAM
# ============================================================

LEVEL04_EXAM_CONFIG = {
    "level_code": "LEVEL_04",
    "question_count": 40,
    "passing_score": 85,
    "xp_reward": 500,
}


def seed_level04_exam():
    connection = get_connection()

    try:
        cursor = connection.cursor()

        # ====================================================
        # LEVEL 4 ID
        # ====================================================

        cursor.execute(
            """
            SELECT id
            FROM course_levels
            WHERE code = ?
            LIMIT 1
            """,
            (
                LEVEL04_EXAM_CONFIG[
                    "level_code"
                ],
            ),
        )

        level = cursor.fetchone()

        if level is None:
            return

        level_id = level["id"]

        # ====================================================
        # FINAL EXAM
        # ====================================================

        cursor.execute(
            """
            INSERT INTO level_exams (
                level_id,
                question_count,
                passing_score,
                xp_reward,
                is_active
            )
            VALUES (?, ?, ?, ?, 1)

            ON CONFLICT(level_id)
            DO UPDATE SET
                question_count = excluded.question_count,
                passing_score = excluded.passing_score,
                xp_reward = excluded.xp_reward,
                is_active = 1
            """,
            (
                level_id,
                LEVEL04_EXAM_CONFIG[
                    "question_count"
                ],
                LEVEL04_EXAM_CONFIG[
                    "passing_score"
                ],
                LEVEL04_EXAM_CONFIG[
                    "xp_reward"
                ],
            ),
        )

        connection.commit()

    finally:
        connection.close()
