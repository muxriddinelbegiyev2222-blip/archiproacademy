from database.database import get_connection


LEVEL05_EXAM = {
    "level_code": "LEVEL_05",
    "title": "BOSQICH 05 - Archicad: boshlang'ich bosqich: yakuniy imtihon",
    "description": (
        "Archicad interfeysi, Navigator, Wall, Slab, Door, Window, "
        "Column, Beam, Object, 2D instrumentlar, Dimension "
        "va birinchi Archicad loyihasi bo'yicha yakuniy imtihon."
    ),
    "question_count": 50,
    "passing_score": 85,
    "xp_reward": 600,
}


def seed_level05_exam():
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
            (LEVEL05_EXAM["level_code"],),
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
                LEVEL05_EXAM["title"],
                LEVEL05_EXAM["description"],
                LEVEL05_EXAM["question_count"],
                LEVEL05_EXAM["passing_score"],
                LEVEL05_EXAM["xp_reward"],
            ),
        )

        connection.commit()

    finally:
        connection.close()
