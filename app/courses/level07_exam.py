from database.database import get_connection


# ============================================================
# LEVEL 7 FINAL EXAM
# ============================================================

LEVEL07_EXAM = {
    "level_code": "LEVEL_07",
    "title": "LEVEL 7 — Archicad Advanced Final",
    "description": (
        "Favorites, Graphic Overrides, Model View Options, "
        "Renovation, Schedules, Properties, Classification, "
        "Hotlink va Modules hamda Professional Template "
        "bo'yicha yakuniy mastery imtihoni."
    ),
    "question_count": 50,
    "passing_score": 85,
    "xp_reward": 800,
}


# ============================================================
# DATABASE SEED
# ============================================================

def seed_level07_exam():
    connection = get_connection()

    try:
        cursor = connection.cursor()

        # ----------------------------------------------------
        # LEVEL 7 ni topamiz
        # ----------------------------------------------------

        cursor.execute(
            """
            SELECT id
            FROM course_levels
            WHERE code = ?
            LIMIT 1
            """,
            (
                LEVEL07_EXAM["level_code"],
            ),
        )

        level = cursor.fetchone()

        if level is None:
            return

        # ----------------------------------------------------
        # FINAL EXAM
        # ----------------------------------------------------

        cursor.execute(
            """
            INSERT INTO level_exams (
                level_id,
                title,
                description,
                question_count,
                passing_score,
                xp_reward
            )
            VALUES (?, ?, ?, ?, ?, ?)

            ON CONFLICT(level_id)
            DO UPDATE SET
                title = excluded.title,
                description = excluded.description,
                question_count = excluded.question_count,
                passing_score = excluded.passing_score,
                xp_reward = excluded.xp_reward
            """,
            (
                level["id"],
                LEVEL07_EXAM["title"],
                LEVEL07_EXAM["description"],
                LEVEL07_EXAM["question_count"],
                LEVEL07_EXAM["passing_score"],
                LEVEL07_EXAM["xp_reward"],
            ),
        )

        connection.commit()

    finally:
        connection.close()
