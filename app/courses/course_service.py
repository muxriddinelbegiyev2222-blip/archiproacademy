from __future__ import annotations

from datetime import datetime
from typing import Any

from database.database import get_connection


# ============================================================
# HELPERS
# ============================================================

def _row_to_dict(row) -> dict:
    if row is None:
        return {}

    try:
        return dict(row)
    except Exception:
        return {}


def _table_exists(cursor, table_name: str) -> bool:
    cursor.execute(
        """
        SELECT name
        FROM sqlite_master
        WHERE type = 'table'
          AND name = ?
        LIMIT 1
        """,
        (table_name,),
    )

    return cursor.fetchone() is not None


def _table_columns(cursor, table_name: str) -> set[str]:
    cursor.execute(
        f"PRAGMA table_info({table_name})"
    )

    rows = cursor.fetchall()

    result = set()

    for row in rows:
        try:
            name = row["name"]
        except Exception:
            name = row[1]

        result.add(name)

    return result


def _find_lesson(
    cursor,
    lesson_id: int | None = None,
    lesson_code: str | None = None,
):
    if lesson_id is not None:
        cursor.execute(
            """
            SELECT *
            FROM lessons
            WHERE id = ?
            LIMIT 1
            """,
            (lesson_id,),
        )

        return cursor.fetchone()

    if lesson_code:
        cursor.execute(
            """
            SELECT *
            FROM lessons
            WHERE code = ?
            LIMIT 1
            """,
            (lesson_code,),
        )

        return cursor.fetchone()

    return None


# ============================================================
# CONTENT REGISTRY COMPATIBILITY
# ============================================================

def get_all_lesson_content():
    """
    Eski kodlarda course_service orqali chaqirilgan bo'lsa,
    yangi content_registry bilan moslikni saqlaydi.
    """
    from courses.content_registry import (
        get_all_lesson_content as registry_get_all_lesson_content,
    )

    return registry_get_all_lesson_content()


def get_lesson_content_by_code(lesson_code: str):
    from courses.content_registry import (
        get_lesson_content_by_code as registry_get_lesson_content_by_code,
    )

    return registry_get_lesson_content_by_code(
        lesson_code
    )


def get_all_quiz_data():
    from courses.content_registry import (
        get_all_quiz_data as registry_get_all_quiz_data,
    )

    return registry_get_all_quiz_data()


# ============================================================
# USER PROGRESS INITIALIZATION
# ============================================================

def initialize_user_progress(
    user_id: int | None = None,
) -> dict:
    """
    lesson_progress jadvalida foydalanuvchi uchun
    kerakli boshlang'ich yozuvlarni yaratadi.

    user_id berilmasa barcha foydalanuvchilar uchun ishlaydi.
    """

    connection = get_connection()

    try:
        cursor = connection.cursor()

        if not _table_exists(
            cursor,
            "users",
        ):
            return {
                "success": False,
                "message": "users jadvali mavjud emas.",
                "created": 0,
            }

        if not _table_exists(
            cursor,
            "lessons",
        ):
            return {
                "success": False,
                "message": "lessons jadvali mavjud emas.",
                "created": 0,
            }

        if not _table_exists(
            cursor,
            "lesson_progress",
        ):
            return {
                "success": False,
                "message": "lesson_progress jadvali mavjud emas.",
                "created": 0,
            }

        progress_columns = _table_columns(
            cursor,
            "lesson_progress",
        )

        if user_id is None:
            cursor.execute(
                """
                SELECT id
                FROM users
                WHERE COALESCE(is_active, 1) = 1
                ORDER BY id
                """
            )

            user_rows = cursor.fetchall()

            user_ids = []

            for row in user_rows:
                try:
                    user_ids.append(row["id"])
                except Exception:
                    user_ids.append(row[0])

        else:
            cursor.execute(
                """
                SELECT id
                FROM users
                WHERE id = ?
                LIMIT 1
                """,
                (user_id,),
            )

            row = cursor.fetchone()

            if row is None:
                return {
                    "success": False,
                    "message": "Foydalanuvchi topilmadi.",
                    "created": 0,
                }

            user_ids = [user_id]

        cursor.execute(
            """
            SELECT id
            FROM lessons
            ORDER BY id
            """
        )

        lesson_rows = cursor.fetchall()

        lesson_ids = []

        for row in lesson_rows:
            try:
                lesson_ids.append(row["id"])
            except Exception:
                lesson_ids.append(row[0])

        created = 0

        for current_user_id in user_ids:
            for lesson_id in lesson_ids:

                cursor.execute(
                    """
                    SELECT id
                    FROM lesson_progress
                    WHERE user_id = ?
                      AND lesson_id = ?
                    LIMIT 1
                    """,
                    (
                        current_user_id,
                        lesson_id,
                    ),
                )

                if cursor.fetchone() is not None:
                    continue

                insert_columns = [
                    "user_id",
                    "lesson_id",
                ]

                values: list[Any] = [
                    current_user_id,
                    lesson_id,
                ]

                defaults = {
                    "status": "locked",
                    "is_completed": 0,
                    "completed": 0,
                    "score": 0,
                    "best_score": 0,
                    "progress_percent": 0,
                    "attempts": 0,
                    "xp_earned": 0,
                    "is_unlocked": 0,
                    "unlocked": 0,
                }

                for column, value in defaults.items():
                    if column in progress_columns:
                        insert_columns.append(
                            column
                        )
                        values.append(
                            value
                        )

                placeholders = ", ".join(
                    "?"
                    for _ in insert_columns
                )

                columns_sql = ", ".join(
                    insert_columns
                )

                cursor.execute(
                    f"""
                    INSERT INTO lesson_progress (
                        {columns_sql}
                    )
                    VALUES (
                        {placeholders}
                    )
                    """,
                    values,
                )

                created += 1

        # Birinchi lesson foydalanuvchi uchun ochiq bo'lishi kerak.
        if lesson_ids:

            first_lesson_id = lesson_ids[0]

            for current_user_id in user_ids:

                updates = []
                values = []

                if "status" in progress_columns:
                    updates.append(
                        "status = ?"
                    )
                    values.append(
                        "available"
                    )

                if "is_unlocked" in progress_columns:
                    updates.append(
                        "is_unlocked = ?"
                    )
                    values.append(
                        1
                    )

                if "unlocked" in progress_columns:
                    updates.append(
                        "unlocked = ?"
                    )
                    values.append(
                        1
                    )

                if updates:
                    values.extend(
                        [
                            current_user_id,
                            first_lesson_id,
                        ]
                    )

                    cursor.execute(
                        f"""
                        UPDATE lesson_progress
                        SET {", ".join(updates)}
                        WHERE user_id = ?
                          AND lesson_id = ?
                        """,
                        values,
                    )

        connection.commit()

        return {
            "success": True,
            "message": "User progress initialize qilindi.",
            "created": created,
            "users": len(user_ids),
            "lessons": len(lesson_ids),
        }

    except Exception as exc:
        connection.rollback()

        return {
            "success": False,
            "message": str(exc),
            "created": 0,
        }

    finally:
        connection.close()


# ============================================================
# COMPLETE LESSON
# ============================================================

def complete_lesson(
    user_id: int,
    lesson_id: int | None = None,
    score: int = 100,
    lesson_code: str | None = None,
    **kwargs,
) -> dict:
    """
    Lessonni tugallangan deb belgilaydi.

    lesson_id yoki lesson_code bilan ishlaydi.
    Qo'shimcha keyword argumentlar UI compatibility uchun qabul qilinadi.
    """

    connection = get_connection()

    try:
        cursor = connection.cursor()

        if not _table_exists(
            cursor,
            "lesson_progress",
        ):
            return {
                "success": False,
                "message": "lesson_progress jadvali mavjud emas.",
            }

        lesson = _find_lesson(
            cursor,
            lesson_id=lesson_id,
            lesson_code=lesson_code,
        )

        if lesson is None:
            return {
                "success": False,
                "message": "Lesson topilmadi.",
            }

        try:
            real_lesson_id = lesson["id"]
        except Exception:
            real_lesson_id = lesson[0]

        lesson_data = _row_to_dict(
            lesson
        )

        passing_score = lesson_data.get(
            "passing_score",
            80,
        )

        try:
            score = int(score)
        except (
            TypeError,
            ValueError,
        ):
            score = 0

        score = max(
            0,
            min(
                100,
                score,
            ),
        )

        passed = (
            score
            >= passing_score
        )

        progress_columns = _table_columns(
            cursor,
            "lesson_progress",
        )

        cursor.execute(
            """
            SELECT *
            FROM lesson_progress
            WHERE user_id = ?
              AND lesson_id = ?
            LIMIT 1
            """,
            (
                user_id,
                real_lesson_id,
            ),
        )

        existing = cursor.fetchone()

        now = datetime.now().isoformat(
            timespec="seconds"
        )

        values_by_column: dict[str, Any] = {}

        if "status" in progress_columns:
            values_by_column["status"] = (
                "completed"
                if passed
                else "available"
            )

        if "is_completed" in progress_columns:
            values_by_column["is_completed"] = (
                1
                if passed
                else 0
            )

        if "completed" in progress_columns:
            values_by_column["completed"] = (
                1
                if passed
                else 0
            )

        if "score" in progress_columns:
            values_by_column["score"] = score

        if "best_score" in progress_columns:
            previous_best = 0

            if existing is not None:
                try:
                    previous_best = (
                        existing["best_score"]
                        or 0
                    )
                except Exception:
                    previous_best = 0

            values_by_column["best_score"] = max(
                previous_best,
                score,
            )

        if "progress_percent" in progress_columns:
            values_by_column["progress_percent"] = (
                100
                if passed
                else score
            )

        if "completed_at" in progress_columns:
            values_by_column["completed_at"] = (
                now
                if passed
                else None
            )

        if "updated_at" in progress_columns:
            values_by_column["updated_at"] = now

        if "last_attempt_at" in progress_columns:
            values_by_column["last_attempt_at"] = now

        if "attempts" in progress_columns:
            previous_attempts = 0

            if existing is not None:
                try:
                    previous_attempts = (
                        existing["attempts"]
                        or 0
                    )
                except Exception:
                    previous_attempts = 0

            values_by_column["attempts"] = (
                previous_attempts + 1
            )

        xp_reward = lesson_data.get(
            "xp_reward",
            0,
        ) or 0

        if "xp_earned" in progress_columns:
            current_xp = 0

            if existing is not None:
                try:
                    current_xp = (
                        existing["xp_earned"]
                        or 0
                    )
                except Exception:
                    current_xp = 0

            if passed:
                values_by_column["xp_earned"] = max(
                    current_xp,
                    xp_reward,
                )
            else:
                values_by_column["xp_earned"] = (
                    current_xp
                )

        if existing is None:

            insert_columns = [
                "user_id",
                "lesson_id",
            ]

            insert_values: list[Any] = [
                user_id,
                real_lesson_id,
            ]

            for (
                column,
                value,
            ) in values_by_column.items():
                insert_columns.append(
                    column
                )
                insert_values.append(
                    value
                )

            placeholders = ", ".join(
                "?"
                for _ in insert_columns
            )

            columns_sql = ", ".join(
                insert_columns
            )

            cursor.execute(
                f"""
                INSERT INTO lesson_progress (
                    {columns_sql}
                )
                VALUES (
                    {placeholders}
                )
                """,
                insert_values,
            )

        else:

            if values_by_column:

                updates = [
                    f"{column} = ?"
                    for column
                    in values_by_column
                ]

                values = list(
                    values_by_column.values()
                )

                values.extend(
                    [
                        user_id,
                        real_lesson_id,
                    ]
                )

                cursor.execute(
                    f"""
                    UPDATE lesson_progress
                    SET {", ".join(updates)}
                    WHERE user_id = ?
                      AND lesson_id = ?
                    """,
                    values,
                )

        connection.commit()

        return {
            "success": True,
            "passed": passed,
            "lesson_id": real_lesson_id,
            "lesson_code": lesson_data.get(
                "code",
                lesson_code,
            ),
            "score": score,
            "passing_score": passing_score,
            "xp_reward": (
                xp_reward
                if passed
                else 0
            ),
        }

    except Exception as exc:
        connection.rollback()

        return {
            "success": False,
            "message": str(exc),
        }

    finally:
        connection.close()


# ============================================================
# LESSON PROGRESS READ
# ============================================================

def get_lesson_progress(
    user_id: int,
    lesson_id: int | None = None,
    lesson_code: str | None = None,
) -> dict | None:

    connection = get_connection()

    try:
        cursor = connection.cursor()

        lesson = _find_lesson(
            cursor,
            lesson_id=lesson_id,
            lesson_code=lesson_code,
        )

        if lesson is None:
            return None

        try:
            real_lesson_id = lesson["id"]
        except Exception:
            real_lesson_id = lesson[0]

        cursor.execute(
            """
            SELECT *
            FROM lesson_progress
            WHERE user_id = ?
              AND lesson_id = ?
            LIMIT 1
            """,
            (
                user_id,
                real_lesson_id,
            ),
        )

        row = cursor.fetchone()

        if row is None:
            return None

        return _row_to_dict(
            row
        )

    finally:
        connection.close()


# ============================================================
# USER COURSE PROGRESS
# ============================================================

def get_user_progress_summary(
    user_id: int,
) -> dict:

    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT COUNT(*) AS total
            FROM lessons
            """
        )

        total_lessons = cursor.fetchone()

        try:
            total = total_lessons["total"]
        except Exception:
            total = total_lessons[0]

        progress_columns = _table_columns(
            cursor,
            "lesson_progress",
        )

        completed = 0

        if "is_completed" in progress_columns:

            cursor.execute(
                """
                SELECT COUNT(*) AS total
                FROM lesson_progress
                WHERE user_id = ?
                  AND is_completed = 1
                """,
                (user_id,),
            )

            row = cursor.fetchone()

            try:
                completed = row["total"]
            except Exception:
                completed = row[0]

        elif "completed" in progress_columns:

            cursor.execute(
                """
                SELECT COUNT(*) AS total
                FROM lesson_progress
                WHERE user_id = ?
                  AND completed = 1
                """,
                (user_id,),
            )

            row = cursor.fetchone()

            try:
                completed = row["total"]
            except Exception:
                completed = row[0]

        elif "status" in progress_columns:

            cursor.execute(
                """
                SELECT COUNT(*) AS total
                FROM lesson_progress
                WHERE user_id = ?
                  AND status = 'completed'
                """,
                (user_id,),
            )

            row = cursor.fetchone()

            try:
                completed = row["total"]
            except Exception:
                completed = row[0]

        percent = 0

        if total:
            percent = round(
                (
                    completed
                    / total
                )
                * 100
            )

        return {
            "success": True,
            "total_lessons": total,
            "completed_lessons": completed,
            "progress_percent": percent,
        }

    finally:
        connection.close()


# ============================================================
# COURSE STRUCTURE READERS
# ============================================================

def get_course_levels() -> list[dict]:

    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT *
            FROM course_levels
            ORDER BY sort_order, id
            """
        )

        return [
            _row_to_dict(row)
            for row in cursor.fetchall()
        ]

    finally:
        connection.close()


def get_level_modules(
    level_id: int | None = None,
    level_code: str | None = None,
) -> list[dict]:

    connection = get_connection()

    try:
        cursor = connection.cursor()

        if level_id is None and level_code:

            cursor.execute(
                """
                SELECT id
                FROM course_levels
                WHERE code = ?
                LIMIT 1
                """,
                (level_code,),
            )

            row = cursor.fetchone()

            if row is None:
                return []

            try:
                level_id = row["id"]
            except Exception:
                level_id = row[0]

        if level_id is None:
            return []

        cursor.execute(
            """
            SELECT *
            FROM course_modules
            WHERE level_id = ?
            ORDER BY sort_order, id
            """,
            (level_id,),
        )

        return [
            _row_to_dict(row)
            for row in cursor.fetchall()
        ]

    finally:
        connection.close()


def get_module_lessons(
    module_id: int | None = None,
    module_code: str | None = None,
) -> list[dict]:

    connection = get_connection()

    try:
        cursor = connection.cursor()

        if module_id is None and module_code:

            cursor.execute(
                """
                SELECT id
                FROM course_modules
                WHERE code = ?
                LIMIT 1
                """,
                (module_code,),
            )

            row = cursor.fetchone()

            if row is None:
                return []

            try:
                module_id = row["id"]
            except Exception:
                module_id = row[0]

        if module_id is None:
            return []

        cursor.execute(
            """
            SELECT *
            FROM lessons
            WHERE module_id = ?
            ORDER BY sort_order, id
            """,
            (module_id,),
        )

        return [
            _row_to_dict(row)
            for row in cursor.fetchall()
        ]

    finally:
        connection.close()
