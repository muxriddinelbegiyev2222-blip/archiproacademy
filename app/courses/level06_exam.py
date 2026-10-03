from database.database import get_connection


LEVEL06_EXAM = {
    "level_code": "LEVEL_06",
    "title": "LEVEL 6 — Archicad Intermediate Final",
    "description": (
        "Stories, Layers, Building Materials, Composite Structures, "
        "Complex Profiles, Roof, Stair, Railing, Mesh va Zones "
        "bo'yicha yakuniy imtihon."
    ),
    "question_count": 50,
    "passing_score": 85,
    "xp_reward": 700,
}


def seed_level06_exam():
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
            (LEVEL06_EXAM["level_code"],),
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
                LEVEL06_EXAM["title"],
                LEVEL06_EXAM["description"],
                LEVEL06_EXAM["question_count"],
                LEVEL06_EXAM["passing_score"],
                LEVEL06_EXAM["xp_reward"],
            ),
        )

        connection.commit()

    finally:
        connection.close()
