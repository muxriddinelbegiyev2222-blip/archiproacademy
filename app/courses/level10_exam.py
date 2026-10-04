from database.database import get_connection


LEVEL10_EXAM = {
    "level_code": "LEVEL_10",
    "title": "BOSQICH 10 - Bir qavatli uy loyihalash: yakuniy imtihon",
    "description": (
        "Texnik topshiriq, Site Analysis, Bubble Diagram, "
        "eskiz plan, plan optimizatsiyasi, Archicad modeli, "
        "fasad, tom, kesim, genplan va loyiha albomi "
        "bo'yicha yakuniy mastery imtihoni."
    ),
    "question_count": 60,
    "passing_score": 85,
    "xp_reward": 1200,
}


def seed_level10_exam():
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
            (LEVEL10_EXAM["level_code"],),
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
                LEVEL10_EXAM["title"],
                LEVEL10_EXAM["description"],
                LEVEL10_EXAM["question_count"],
                LEVEL10_EXAM["passing_score"],
                LEVEL10_EXAM["xp_reward"],
            ),
        )

        connection.commit()

    finally:
        connection.close()
