from database.database import get_connection


LEVEL03_EXAM = {
    "level_code": "LEVEL_03",
    "title": "BOSQICH 03 - Uchastkani rejalashtirish: yakuniy imtihon",
    "description": (
        "Uchastkani o'qish, quyosh va orientatsiya, kirish, "
        "uy joylashtirish, hovli zonalari, avtomobil zonasi, "
        "relyef va genplan bo'yicha yakuniy imtihon."
    ),
    "question_count": 40,
    "passing_score": 85,
    "xp_reward": 500,
}


def seed_level03_exam():
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
            (LEVEL03_EXAM["level_code"],),
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
                LEVEL03_EXAM["title"],
                LEVEL03_EXAM["description"],
                LEVEL03_EXAM["question_count"],
                LEVEL03_EXAM["passing_score"],
                LEVEL03_EXAM["xp_reward"],
            ),
        )

        connection.commit()

    finally:
        connection.close()
