from database.database import get_connection


LEVEL11_EXAM = {
    "level_code": "LEVEL_11",
    "title": "LEVEL 11 — 2 qavatli uy PRO Final",
    "description": (
        "2 qavatli uy konsepsiyasi, qavatlar zonalashi, Zinapoya PRO, "
        "vertikal kommunikatsiyalar, void va ikkinchi yorug'lik, "
        "balkon va terassa, 2 qavatli fasad, to'liq Archicad model "
        "hamda ishchi loyiha bo'yicha yakuniy mastery imtihoni."
    ),
    "question_count": 60,
    "passing_score": 85,
    "xp_reward": 1400,
}


def seed_level11_exam():
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
            (LEVEL11_EXAM["level_code"],),
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
                LEVEL11_EXAM["title"],
                LEVEL11_EXAM["description"],
                LEVEL11_EXAM["question_count"],
                LEVEL11_EXAM["passing_score"],
                LEVEL11_EXAM["xp_reward"],
            ),
        )

        connection.commit()

    finally:
        connection.close()
