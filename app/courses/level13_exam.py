from database.database import get_connection


LEVEL13_EXAM = {
    "level_code": "LEVEL_13",
    "title": "LEVEL 13 — Mijoz bilan professional ishlash Final",
    "description": (
        "Mijoz bilan birinchi suhbat, professional brief, budjet, "
        "variantlar tayyorlash, loyiha taqdimoti, mijoz tuzatishlari, "
        "qarorni himoya qilish va real loyiha simulyatori "
        "bo'yicha yakuniy mastery imtihoni."
    ),
    "question_count": 60,
    "passing_score": 85,
    "xp_reward": 1800,
}


def seed_level13_exam():
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
            (LEVEL13_EXAM["level_code"],),
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
                LEVEL13_EXAM["title"],
                LEVEL13_EXAM["description"],
                LEVEL13_EXAM["question_count"],
                LEVEL13_EXAM["passing_score"],
                LEVEL13_EXAM["xp_reward"],
            ),
        )

        connection.commit()

    finally:
        connection.close()
