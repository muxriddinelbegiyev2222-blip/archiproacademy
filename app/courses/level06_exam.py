from database.database import get_connection


# ============================================================
# LEVEL 6 FINAL EXAM
# ============================================================

LEVEL06_EXAM_CONFIG = {
    "level_code": "LEVEL_06",
    "code": "L06_FINAL",
    "title": "LEVEL 6 — Archicad Intermediate yakuniy imtihoni",
    "description": (
        "Stories, Layers, Building Materials, Composite Structures, "
        "Complex Profiles, Roof Tool, Stair Tool, Railing, Mesh va "
        "Zones bo'yicha yakuniy bilim tekshiruvi."
    ),
    "question_count": 50,
    "passing_score": 85,
    "xp_reward": 700,
}


# ============================================================
# DATABASE SEED
# ============================================================

def seed_level06_exam():
    connection = get_connection()

    try:
        cursor = connection.cursor()

        # ----------------------------------------------------
        # LEVEL 6 ID
        # ----------------------------------------------------

        cursor.execute(
            """
            SELECT id
            FROM course_levels
            WHERE code = ?
            LIMIT 1
            """,
            (
                LEVEL06_EXAM_CONFIG[
                    "level_code"
                ],
            ),
        )

        level = cursor.fetchone()

        if level is None:
            return

        level_id = level["id"]

        # ----------------------------------------------------
        # FINAL EXAM
        # ----------------------------------------------------

        cursor.execute(
            """
            INSERT INTO level_exams (
                level_id,
                code,
                title,
                description,
                question_count,
                passing_score,
                xp_reward,
                is_active
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)

            ON CONFLICT(level_id)
            DO UPDATE SET
                code = excluded.code,
                title = excluded.title,
                description = excluded.description,
                question_count = excluded.question_count,
                passing_score = excluded.passing_score,
                xp_reward = excluded.xp_reward,
                is_active = excluded.is_active
            """,
            (
                level_id,
                LEVEL06_EXAM_CONFIG[
                    "code"
                ],
                LEVEL06_EXAM_CONFIG[
                    "title"
                ],
                LEVEL06_EXAM_CONFIG[
                    "description"
                ],
                LEVEL06_EXAM_CONFIG[
                    "question_count"
                ],
                LEVEL06_EXAM_CONFIG[
                    "passing_score"
                ],
                LEVEL06_EXAM_CONFIG[
                    "xp_reward"
                ],
                1,
            ),
        )

        connection.commit()

    finally:
        connection.close()
