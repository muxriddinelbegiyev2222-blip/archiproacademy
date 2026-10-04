from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path

from database.database import (
    get_connection,
)


BACKUP_PRODUCT = "ARCHIPRO_UZ"
BACKUP_VERSION = 1


def _now() -> str:
    return datetime.now().isoformat(
        timespec="seconds"
    )


# ============================================================
# RECENT LESSONS
# ============================================================


def mark_lesson_opened(
    user_id: int,
    lesson_id: int,
) -> None:
    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            INSERT INTO lesson_progress (
                user_id,
                lesson_id,
                status,
                started_at,
                last_opened_at
            )
            VALUES (?, ?, 'locked', ?, ?)

            ON CONFLICT(user_id, lesson_id)
            DO UPDATE SET
                started_at = COALESCE(
                    lesson_progress.started_at,
                    excluded.started_at
                ),
                last_opened_at = excluded.last_opened_at
            """,
            (
                user_id,
                lesson_id,
                _now(),
                _now(),
            ),
        )

        connection.commit()

    finally:
        connection.close()


def get_recent_lessons(
    user_id: int,
    limit: int = 5,
) -> list[dict]:
    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT
                ls.*,
                lp.status,
                lp.last_opened_at,
                m.title AS module_title,
                m.code AS module_code,
                l.title AS level_title,
                l.subtitle AS level_subtitle,
                l.code AS level_code

            FROM lesson_progress lp

            JOIN lessons ls
                ON ls.id = lp.lesson_id

            JOIN course_modules m
                ON m.id = ls.module_id

            JOIN course_levels l
                ON l.id = m.level_id

            WHERE lp.user_id = ?
              AND lp.last_opened_at IS NOT NULL
              AND ls.is_active = 1
              AND m.is_active = 1
              AND l.is_active = 1

            ORDER BY
                lp.last_opened_at DESC

            LIMIT ?
            """,
            (
                user_id,
                max(
                    1,
                    int(limit),
                ),
            ),
        )

        return [
            dict(row)
            for row in cursor.fetchall()
        ]

    finally:
        connection.close()


# ============================================================
# BOOKMARKS
# ============================================================


def is_lesson_bookmarked(
    user_id: int,
    lesson_id: int,
) -> bool:
    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT 1
            FROM lesson_bookmarks
            WHERE user_id = ?
              AND lesson_id = ?
            LIMIT 1
            """,
            (
                user_id,
                lesson_id,
            ),
        )

        return (
            cursor.fetchone()
            is not None
        )

    finally:
        connection.close()


def set_lesson_bookmark(
    user_id: int,
    lesson_id: int,
    enabled: bool,
) -> bool:
    connection = get_connection()

    try:
        cursor = connection.cursor()

        if enabled:
            cursor.execute(
                """
                INSERT INTO lesson_bookmarks (
                    user_id,
                    lesson_id,
                    created_at
                )
                VALUES (?, ?, ?)
                ON CONFLICT(user_id, lesson_id)
                DO NOTHING
                """,
                (
                    user_id,
                    lesson_id,
                    _now(),
                ),
            )

        else:
            cursor.execute(
                """
                DELETE FROM lesson_bookmarks
                WHERE user_id = ?
                  AND lesson_id = ?
                """,
                (
                    user_id,
                    lesson_id,
                ),
            )

        connection.commit()

        return bool(enabled)

    finally:
        connection.close()


def get_bookmarked_lesson_ids(
    user_id: int,
) -> set[int]:
    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT lesson_id
            FROM lesson_bookmarks
            WHERE user_id = ?
            """,
            (
                user_id,
            ),
        )

        return {
            int(row["lesson_id"])
            for row in cursor.fetchall()
        }

    finally:
        connection.close()


# ============================================================
# LESSON NOTES
# ============================================================


def get_lesson_note(
    user_id: int,
    lesson_id: int,
) -> str:
    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT note_text
            FROM lesson_notes
            WHERE user_id = ?
              AND lesson_id = ?
            LIMIT 1
            """,
            (
                user_id,
                lesson_id,
            ),
        )

        row = cursor.fetchone()

        if row is None:
            return ""

        return str(
            row["note_text"]
            or ""
        )

    finally:
        connection.close()


def save_lesson_note(
    user_id: int,
    lesson_id: int,
    note_text: str,
) -> None:
    note_text = str(
        note_text
        or ""
    ).strip()

    connection = get_connection()

    try:
        cursor = connection.cursor()

        if not note_text:
            cursor.execute(
                """
                DELETE FROM lesson_notes
                WHERE user_id = ?
                  AND lesson_id = ?
                """,
                (
                    user_id,
                    lesson_id,
                ),
            )

        else:
            cursor.execute(
                """
                INSERT INTO lesson_notes (
                    user_id,
                    lesson_id,
                    note_text,
                    updated_at
                )
                VALUES (?, ?, ?, ?)

                ON CONFLICT(user_id, lesson_id)
                DO UPDATE SET
                    note_text = CASE
                        WHEN excluded.updated_at >= lesson_notes.updated_at
                            THEN excluded.note_text
                        ELSE lesson_notes.note_text
                    END,
                    updated_at = CASE
                        WHEN excluded.updated_at >= lesson_notes.updated_at
                            THEN excluded.updated_at
                        ELSE lesson_notes.updated_at
                    END
                """,
                (
                    user_id,
                    lesson_id,
                    note_text,
                    _now(),
                ),
            )

        connection.commit()

    finally:
        connection.close()


# ============================================================
# PROGRESS BACKUP
# ============================================================


def _lesson_code_map(
    cursor,
) -> dict[int, str]:
    cursor.execute(
        """
        SELECT id, code
        FROM lessons
        """
    )

    return {
        int(row["id"]): str(row["code"])
        for row in cursor.fetchall()
    }


def _exam_level_code_map(
    cursor,
) -> dict[int, str]:
    cursor.execute(
        """
        SELECT
            level_exams.id AS exam_id,
            course_levels.code AS level_code

        FROM level_exams

        JOIN course_levels
            ON course_levels.id = level_exams.level_id
        """
    )

    return {
        int(row["exam_id"]): str(row["level_code"])
        for row in cursor.fetchall()
    }


def export_user_backup(
    user_id: int,
    destination,
) -> Path:
    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT username, full_name
            FROM users
            WHERE id = ?
            LIMIT 1
            """,
            (
                user_id,
            ),
        )

        user = cursor.fetchone()

        if user is None:
            raise ValueError(
                "Foydalanuvchi topilmadi."
            )

        lesson_codes = _lesson_code_map(
            cursor
        )

        exam_levels = _exam_level_code_map(
            cursor
        )

        cursor.execute(
            """
            SELECT *
            FROM lesson_progress
            WHERE user_id = ?
            """,
            (
                user_id,
            ),
        )

        lesson_progress = []

        for row in cursor.fetchall():
            lesson_code = lesson_codes.get(
                int(row["lesson_id"])
            )

            if not lesson_code:
                continue

            lesson_progress.append(
                {
                    "lesson_code": lesson_code,
                    "status": row["status"],
                    "score": row["score"],
                    "best_score": row["best_score"],
                    "attempts": row["attempts"],
                    "started_at": row["started_at"],
                    "completed_at": row["completed_at"],
                    "last_opened_at": row["last_opened_at"],
                }
            )

        cursor.execute(
            """
            SELECT
                course_levels.code AS level_code,
                user_level_progress.status,
                user_level_progress.best_exam_score,
                user_level_progress.exam_attempts,
                user_level_progress.completed_at

            FROM user_level_progress

            JOIN course_levels
                ON course_levels.id =
                   user_level_progress.level_id

            WHERE user_level_progress.user_id = ?
            """,
            (
                user_id,
            ),
        )

        level_progress = [
            dict(row)
            for row in cursor.fetchall()
        ]

        cursor.execute(
            """
            SELECT *
            FROM quiz_attempts
            WHERE user_id = ?
            ORDER BY id
            """,
            (
                user_id,
            ),
        )

        quiz_attempts = []

        for row in cursor.fetchall():
            lesson_code = lesson_codes.get(
                int(row["lesson_id"])
            )

            if lesson_code:
                quiz_attempts.append(
                    {
                        "lesson_code": lesson_code,
                        "score": row["score"],
                        "passed": row["passed"],
                        "created_at": row["created_at"],
                    }
                )

        cursor.execute(
            """
            SELECT *
            FROM level_exam_attempts
            WHERE user_id = ?
            ORDER BY id
            """,
            (
                user_id,
            ),
        )

        exam_attempts = []

        for row in cursor.fetchall():
            level_code = exam_levels.get(
                int(row["exam_id"])
            )

            if level_code:
                exam_attempts.append(
                    {
                        "level_code": level_code,
                        "score": row["score"],
                        "correct_answers": row["correct_answers"],
                        "total_questions": row["total_questions"],
                        "passed": row["passed"],
                        "created_at": row["created_at"],
                    }
                )

        cursor.execute(
            """
            SELECT lesson_id, created_at
            FROM lesson_bookmarks
            WHERE user_id = ?
            """,
            (
                user_id,
            ),
        )

        bookmarks = []

        for row in cursor.fetchall():
            lesson_code = lesson_codes.get(
                int(row["lesson_id"])
            )

            if lesson_code:
                bookmarks.append(
                    {
                        "lesson_code": lesson_code,
                        "created_at": row["created_at"],
                    }
                )

        cursor.execute(
            """
            SELECT lesson_id, note_text, updated_at
            FROM lesson_notes
            WHERE user_id = ?
            """,
            (
                user_id,
            ),
        )

        notes = []

        for row in cursor.fetchall():
            lesson_code = lesson_codes.get(
                int(row["lesson_id"])
            )

            if lesson_code:
                notes.append(
                    {
                        "lesson_code": lesson_code,
                        "note_text": row["note_text"],
                        "updated_at": row["updated_at"],
                    }
                )

        data = {
            "product": BACKUP_PRODUCT,
            "version": BACKUP_VERSION,
            "exported_at": _now(),
            "user": {
                "username": user["username"],
                "full_name": user["full_name"],
            },
            "lesson_progress": lesson_progress,
            "level_progress": level_progress,
            "quiz_attempts": quiz_attempts,
            "exam_attempts": exam_attempts,
            "bookmarks": bookmarks,
            "notes": notes,
        }

    finally:
        connection.close()

    path = Path(
        destination
    )

    if (
        path.suffix.lower()
        != ".archiprobackup"
    ):
        path = path.with_suffix(
            ".archiprobackup"
        )

    path.write_text(
        json.dumps(
            data,
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )

    return path


def import_user_backup(
    user_id: int,
    source,
) -> dict:
    path = Path(
        source
    )

    data = json.loads(
        path.read_text(
            encoding="utf-8"
        )
    )

    if (
        data.get("product")
        != BACKUP_PRODUCT
        or data.get("version")
        != BACKUP_VERSION
    ):
        raise ValueError(
            "Backup fayli ARCHIPRO UZ formatiga mos emas."
        )

    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT username
            FROM users
            WHERE id = ?
            LIMIT 1
            """,
            (
                user_id,
            ),
        )

        current_user = cursor.fetchone()

        if current_user is None:
            raise ValueError(
                "Foydalanuvchi topilmadi."
            )

        backup_username = str(
            data.get(
                "user",
                {},
            ).get(
                "username",
                "",
            )
        ).strip().lower()

        current_username = str(
            current_user["username"]
        ).strip().lower()

        if (
            backup_username
            and backup_username
            != current_username
        ):
            raise ValueError(
                "Bu backup boshqa login uchun yaratilgan."
            )

        cursor.execute(
            """
            SELECT id, code
            FROM lessons
            """
        )

        lesson_ids = {
            str(row["code"]): int(row["id"])
            for row in cursor.fetchall()
        }

        cursor.execute(
            """
            SELECT
                course_levels.id AS level_id,
                course_levels.code AS level_code,
                level_exams.id AS exam_id

            FROM course_levels

            LEFT JOIN level_exams
                ON level_exams.level_id =
                   course_levels.id
            """
        )

        levels = {
            str(row["level_code"]): {
                "level_id": int(row["level_id"]),
                "exam_id": (
                    int(row["exam_id"])
                    if row["exam_id"] is not None
                    else None
                ),
            }
            for row in cursor.fetchall()
        }

        for item in data.get(
            "lesson_progress",
            [],
        ):
            lesson_id = lesson_ids.get(
                str(
                    item.get(
                        "lesson_code",
                        "",
                    )
                )
            )

            if lesson_id is None:
                continue

            cursor.execute(
                """
                INSERT INTO lesson_progress (
                    user_id,
                    lesson_id,
                    status,
                    score,
                    best_score,
                    attempts,
                    started_at,
                    completed_at,
                    last_opened_at
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)

                ON CONFLICT(user_id, lesson_id)
                DO UPDATE SET
                    status = CASE
                        WHEN lesson_progress.status = 'completed'
                            THEN 'completed'
                        WHEN excluded.status = 'completed'
                            THEN 'completed'
                        WHEN lesson_progress.status = 'available'
                             OR excluded.status = 'available'
                            THEN 'available'
                        ELSE lesson_progress.status
                    END,
                    score = MAX(
                        lesson_progress.score,
                        excluded.score
                    ),
                    best_score = MAX(
                        lesson_progress.best_score,
                        excluded.best_score
                    ),
                    attempts = MAX(
                        lesson_progress.attempts,
                        excluded.attempts
                    ),
                    started_at = COALESCE(
                        lesson_progress.started_at,
                        excluded.started_at
                    ),
                    completed_at = COALESCE(
                        lesson_progress.completed_at,
                        excluded.completed_at
                    ),
                    last_opened_at = CASE
                        WHEN lesson_progress.last_opened_at IS NULL
                            THEN excluded.last_opened_at
                        WHEN excluded.last_opened_at IS NULL
                            THEN lesson_progress.last_opened_at
                        WHEN excluded.last_opened_at > lesson_progress.last_opened_at
                            THEN excluded.last_opened_at
                        ELSE lesson_progress.last_opened_at
                    END
                """,
                (
                    user_id,
                    lesson_id,
                    item.get(
                        "status",
                        "locked",
                    ),
                    int(
                        item.get(
                            "score",
                            0,
                        )
                        or 0
                    ),
                    int(
                        item.get(
                            "best_score",
                            0,
                        )
                        or 0
                    ),
                    int(
                        item.get(
                            "attempts",
                            0,
                        )
                        or 0
                    ),
                    item.get(
                        "started_at"
                    ),
                    item.get(
                        "completed_at"
                    ),
                    item.get(
                        "last_opened_at"
                    ),
                ),
            )

        for item in data.get(
            "level_progress",
            [],
        ):
            level_info = levels.get(
                str(
                    item.get(
                        "level_code",
                        "",
                    )
                )
            )

            if not level_info:
                continue

            cursor.execute(
                """
                INSERT INTO user_level_progress (
                    user_id,
                    level_id,
                    status,
                    best_exam_score,
                    exam_attempts,
                    completed_at
                )
                VALUES (?, ?, ?, ?, ?, ?)

                ON CONFLICT(user_id, level_id)
                DO UPDATE SET
                    status = CASE
                        WHEN user_level_progress.status = 'completed'
                            THEN 'completed'
                        WHEN excluded.status = 'completed'
                            THEN 'completed'
                        WHEN user_level_progress.status = 'available'
                             OR excluded.status = 'available'
                            THEN 'available'
                        ELSE user_level_progress.status
                    END,
                    best_exam_score = MAX(
                        user_level_progress.best_exam_score,
                        excluded.best_exam_score
                    ),
                    exam_attempts = MAX(
                        user_level_progress.exam_attempts,
                        excluded.exam_attempts
                    ),
                    completed_at = COALESCE(
                        user_level_progress.completed_at,
                        excluded.completed_at
                    )
                """,
                (
                    user_id,
                    level_info[
                        "level_id"
                    ],
                    item.get(
                        "status",
                        "locked",
                    ),
                    int(
                        item.get(
                            "best_exam_score",
                            0,
                        )
                        or 0
                    ),
                    int(
                        item.get(
                            "exam_attempts",
                            0,
                        )
                        or 0
                    ),
                    item.get(
                        "completed_at"
                    ),
                ),
            )

        # Attempts tarixini duplicate qilmaslik uchun importda
        # mavjud tarix o'chirilmaydi. Faqat backupdagi aniq
        # yozuv hali yo'q bo'lsa qo'shiladi.
        for item in data.get(
            "quiz_attempts",
            [],
        ):
            lesson_id = lesson_ids.get(
                str(
                    item.get(
                        "lesson_code",
                        "",
                    )
                )
            )

            if lesson_id is None:
                continue

            cursor.execute(
                """
                SELECT 1
                FROM quiz_attempts
                WHERE user_id = ?
                  AND lesson_id = ?
                  AND score = ?
                  AND passed = ?
                  AND created_at = ?
                LIMIT 1
                """,
                (
                    user_id,
                    lesson_id,
                    int(
                        item.get(
                            "score",
                            0,
                        )
                        or 0
                    ),
                    int(
                        item.get(
                            "passed",
                            0,
                        )
                        or 0
                    ),
                    item.get(
                        "created_at"
                    ),
                ),
            )

            if cursor.fetchone() is None:
                cursor.execute(
                    """
                    INSERT INTO quiz_attempts (
                        user_id,
                        lesson_id,
                        score,
                        passed,
                        created_at
                    )
                    VALUES (?, ?, ?, ?, ?)
                    """,
                    (
                        user_id,
                        lesson_id,
                        int(
                            item.get(
                                "score",
                                0,
                            )
                            or 0
                        ),
                        int(
                            item.get(
                                "passed",
                                0,
                            )
                            or 0
                        ),
                        item.get(
                            "created_at"
                        )
                        or _now(),
                    ),
                )

        for item in data.get(
            "exam_attempts",
            [],
        ):
            level_info = levels.get(
                str(
                    item.get(
                        "level_code",
                        "",
                    )
                )
            )

            if (
                not level_info
                or level_info[
                    "exam_id"
                ] is None
            ):
                continue

            exam_id = level_info[
                "exam_id"
            ]

            cursor.execute(
                """
                SELECT 1
                FROM level_exam_attempts
                WHERE user_id = ?
                  AND exam_id = ?
                  AND score = ?
                  AND created_at = ?
                LIMIT 1
                """,
                (
                    user_id,
                    exam_id,
                    int(
                        item.get(
                            "score",
                            0,
                        )
                        or 0
                    ),
                    item.get(
                        "created_at"
                    ),
                ),
            )

            if cursor.fetchone() is None:
                cursor.execute(
                    """
                    INSERT INTO level_exam_attempts (
                        user_id,
                        exam_id,
                        score,
                        correct_answers,
                        total_questions,
                        passed,
                        created_at
                    )
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                    """,
                    (
                        user_id,
                        exam_id,
                        int(
                            item.get(
                                "score",
                                0,
                            )
                            or 0
                        ),
                        int(
                            item.get(
                                "correct_answers",
                                0,
                            )
                            or 0
                        ),
                        int(
                            item.get(
                                "total_questions",
                                0,
                            )
                            or 0
                        ),
                        int(
                            item.get(
                                "passed",
                                0,
                            )
                            or 0
                        ),
                        item.get(
                            "created_at"
                        )
                        or _now(),
                    ),
                )

        for item in data.get(
            "bookmarks",
            [],
        ):
            lesson_id = lesson_ids.get(
                str(
                    item.get(
                        "lesson_code",
                        "",
                    )
                )
            )

            if lesson_id is None:
                continue

            cursor.execute(
                """
                INSERT INTO lesson_bookmarks (
                    user_id,
                    lesson_id,
                    created_at
                )
                VALUES (?, ?, ?)
                ON CONFLICT(user_id, lesson_id)
                DO NOTHING
                """,
                (
                    user_id,
                    lesson_id,
                    item.get(
                        "created_at"
                    )
                    or _now(),
                ),
            )

        for item in data.get(
            "notes",
            [],
        ):
            lesson_id = lesson_ids.get(
                str(
                    item.get(
                        "lesson_code",
                        "",
                    )
                )
            )

            if lesson_id is None:
                continue

            note_text = str(
                item.get(
                    "note_text",
                    "",
                )
                or ""
            ).strip()

            if not note_text:
                continue

            cursor.execute(
                """
                INSERT INTO lesson_notes (
                    user_id,
                    lesson_id,
                    note_text,
                    updated_at
                )
                VALUES (?, ?, ?, ?)

                ON CONFLICT(user_id, lesson_id)
                DO UPDATE SET
                    note_text = excluded.note_text,
                    updated_at = excluded.updated_at
                """,
                (
                    user_id,
                    lesson_id,
                    note_text,
                    item.get(
                        "updated_at"
                    )
                    or _now(),
                ),
            )

        connection.commit()

        return {
            "success": True,
            "message": (
                "Progress, bookmark va eslatmalar "
                "muvaffaqiyatli tiklandi."
            ),
        }

    except Exception:
        connection.rollback()
        raise

    finally:
        connection.close()
