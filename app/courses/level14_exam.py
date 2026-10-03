from database.database import get_connection


LEVEL14_EXAM = {
    "level_code": "LEVEL_14",
    "title": "LEVEL 14 — Advanced Case Projects Final",
    "description": (
        "Tor uchastka, noto'g'ri shakldagi uchastka, nishabli yer, "
        "katta villa, ko'p avlodli oila, premium fasad, Design Clinic "
        "va Advanced Case Studies bo'yicha yakuniy mastery imtihoni."
    ),
    "question_count": 60,
    "passing_score": 85,
    "xp_reward": 2000,
}


def seed_level14_exam():
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
            (LEVEL14_EXAM["level_code"],),
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
                LEVEL14_EXAM["title"],
                LEVEL14_EXAM["description"],
                LEVEL14_EXAM["question_count"],
                LEVEL14_EXAM["passing_score"],
                LEVEL14_EXAM["xp_reward"],
            ),
        )

        connection.commit()

    finally:
        connection.close()
