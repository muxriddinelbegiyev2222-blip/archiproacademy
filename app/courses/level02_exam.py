from database.database import get_connection


LEVEL02_EXAM = {
    "level_code": "LEVEL_02",
    "title": "LEVEL 2 — Spatial Thinking Final",
    "description": (
        "Fazoviy fikrlash, ergonomika, funksional zonalash, "
        "circulation va turar joy xonalari bo'yicha yakuniy imtihon."
    ),
    "question_count": 40,
    "passing_score": 85,
    "xp_reward": 400,
}


def seed_level02_exam():
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
            (LEVEL02_EXAM["level_code"],),
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
                LEVEL02_EXAM["title"],
                LEVEL02_EXAM["description"],
                LEVEL02_EXAM["question_count"],
                LEVEL02_EXAM["passing_score"],
                LEVEL02_EXAM["xp_reward"],
            ),
        )

        connection.commit()

    finally:
        connection.close()
