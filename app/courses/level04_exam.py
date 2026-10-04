from database.database import get_connection


LEVEL04_EXAM = {
    "level_code": "LEVEL_04",
    "title": "BOSQICH 04 - O'zbekiston sharoitida turar joy loyihalash: yakuniy imtihon",
    "description": (
        "O'zbekiston sharoitidagi turar joy, oilaviy turmush tarzi, "
        "mehmon kutish, ichki hovli, ayvon, yozgi oshxona, "
        "yordamchi binolar, issiq iqlim va mahalliy fasad "
        "bo'yicha yakuniy imtihon."
    ),
    "question_count": 40,
    "passing_score": 85,
    "xp_reward": 500,
}


def seed_level04_exam():
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
            (LEVEL04_EXAM["level_code"],),
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
                LEVEL04_EXAM["title"],
                LEVEL04_EXAM["description"],
                LEVEL04_EXAM["question_count"],
                LEVEL04_EXAM["passing_score"],
                LEVEL04_EXAM["xp_reward"],
            ),
        )

        connection.commit()

    finally:
        connection.close()
