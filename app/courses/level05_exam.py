from database.database import get_connection


# ============================================================
# LEVEL 5 FINAL EXAM
# ============================================================

LEVEL05_EXAM_CONFIG = {
    "level_code": "LEVEL_05",
    "question_count": 50,
    "passing_score": 85,
    "xp_reward": 600,
}


def seed_level05_exam():
    connection = get_connection()

    try:
        cursor = connection.cursor()

        # ====================================================
        # LEVEL 5 ID
        # ====================================================

        cursor.execute(
            """
            SELECT id
            FROM course_levels
            WHERE code = ?
            LIMIT 1
            """,
            (
                LEVEL05_EXAM_CONFIG[
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
                LEVEL05_EXAM_CONFIG[
                    "question_count"
                ],
                LEVEL05_EXAM_CONFIG[
                    "passing_score"
                ],
                LEVEL05_EXAM_CONFIG[
                    "xp_reward"
                ],
            ),
        )

        connection.commit()

    finally:
        connection.close()
