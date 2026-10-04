from database.database import get_connection


LEVEL09_EXAM = {
    "level_code": "LEVEL_09",
    "title": "BOSQICH 09 - SHNQ va me'yoriy talablar: yakuniy imtihon",
    "description": (
        "Normativ savodxonlik, turar joy talablari, uchastka talablari, "
        "yoritish va insolyatsiya, yong'in xavfsizligi, evakuatsiya, "
        "accessibility va normativ xatolar bo'yicha yakuniy mastery imtihoni."
    ),
    "question_count": 50,
    "passing_score": 85,
    "xp_reward": 1000,
}


def seed_level09_exam():
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
            (LEVEL09_EXAM["level_code"],),
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
                LEVEL09_EXAM["title"],
                LEVEL09_EXAM["description"],
                LEVEL09_EXAM["question_count"],
                LEVEL09_EXAM["passing_score"],
                LEVEL09_EXAM["xp_reward"],
            ),
        )

        connection.commit()

    finally:
        connection.close()
