from database.database import get_connection


LEVEL15_EXAM = {
    "level_code": "LEVEL_15",
    "title": "LEVEL 15 — ARCHIPRO UZ PRO Final",
    "description": (
        "ARCHIPRO UZ dasturining yakuniy mastery imtihoni. "
        "Arxitektura nazariyasi, residential planning, site analysis, "
        "konstruktiv fikrlash, Archicad, BIM, hujjatlashtirish, "
        "mijoz bilan ishlash, murakkab case studies, final loyiha, "
        "loyihani himoya qilish va portfolio ko'nikmalarini qamrab oladi."
    ),
    "question_count": 80,
    "passing_score": 85,
    "xp_reward": 3000,
}


def seed_level15_exam():
    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT id
            FROM course_levels
            WHERE code = ?
            LIMIT 1
            """,
            (LEVEL15_EXAM["level_code"],),
        )

        level = cursor.fetchone()

        if level is None:
            return

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
                LEVEL15_EXAM["title"],
                LEVEL15_EXAM["description"],
                LEVEL15_EXAM["question_count"],
                LEVEL15_EXAM["passing_score"],
                LEVEL15_EXAM["xp_reward"],
            ),
        )

        connection.commit()

    finally:
        connection.close()
