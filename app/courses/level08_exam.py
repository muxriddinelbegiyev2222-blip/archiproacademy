from database.database import get_connection


# ============================================================
# LEVEL 8 FINAL EXAM
# ============================================================

LEVEL08_EXAM = {
    "level_code": "LEVEL_08",
    "title": "LEVEL 8 — Konstruktsiya asoslari Final",
    "description": (
        "Fundament, devor konstruksiyasi, karkas, plitalar, "
        "tom konstruksiyasi, gidroizolyatsiya, issiqlik "
        "izolyatsiyasi, seysmika asoslari va konstruktor "
        "bilan ishlash bo'yicha yakuniy mastery imtihoni."
    ),
    "question_count": 50,
    "passing_score": 85,
    "xp_reward": 900,
}


# ============================================================
# DATABASE SEED
# ============================================================

def seed_level08_exam():
    connection = get_connection()

    try:
        cursor = connection.cursor()

        # ----------------------------------------------------
        # LEVEL 8 ni topamiz
        # ----------------------------------------------------

        cursor.execute(
            """
            SELECT id
            FROM course_levels
            WHERE code = ?
            LIMIT 1
            """,
            (
                LEVEL08_EXAM["level_code"],
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
                LEVEL08_EXAM["title"],
                LEVEL08_EXAM["description"],
                LEVEL08_EXAM["question_count"],
                LEVEL08_EXAM["passing_score"],
                LEVEL08_EXAM["xp_reward"],
            ),
        )

        connection.commit()

    finally:
        connection.close()
