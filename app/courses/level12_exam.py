from database.database import get_connection


LEVEL12_EXAM = {
    "level_code": "LEVEL_12",
    "title": "LEVEL 12 — BIM va hujjatlashtirish Final",
    "description": (
        "BIM tushunchasi, Element Information, spetsifikatsiyalar, "
        "View Map PRO, Layout Book, shtamp va standartlar, Publisher, "
        "DWG almashinuvi, IFC asoslari va final loyiha albomi "
        "bo'yicha yakuniy mastery imtihoni."
    ),
    "question_count": 60,
    "passing_score": 85,
    "xp_reward": 1600,
}


def seed_level12_exam():
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
            (LEVEL12_EXAM["level_code"],),
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
                LEVEL12_EXAM["title"],
                LEVEL12_EXAM["description"],
                LEVEL12_EXAM["question_count"],
                LEVEL12_EXAM["passing_score"],
                LEVEL12_EXAM["xp_reward"],
            ),
        )

        connection.commit()

    finally:
        connection.close()
