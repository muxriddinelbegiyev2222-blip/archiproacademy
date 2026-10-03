from __future__ import annotations

from datetime import datetime

from database.database import (
    get_connection,
)


# ============================================================
# HELPERS
# ============================================================

def _row_to_dict(row) -> dict:
    if row is None:
        return {}

    return dict(row)


def _table_exists(
    cursor,
    table_name: str,
) -> bool:

    cursor.execute(
        """
        SELECT 1
        FROM sqlite_master
        WHERE type = 'table'
          AND name = ?
        LIMIT 1
        """,
        (table_name,),
    )

    return (
        cursor.fetchone()
        is not None
    )


def _ensure_progress_rows(
    cursor,
    user_id: int,
):
    """
    Foydalanuvchiga barcha Level va darslar
    uchun progress yozuvlarini yaratadi.

    Mavjud progress o'zgartirilmaydi.
    """

    if not _table_exists(
        cursor,
        "user_level_progress",
    ):
        return

    if not _table_exists(
        cursor,
        "lesson_progress",
    ):
        return

    # --------------------------------------------------------
    # LEVEL PROGRESS
    # --------------------------------------------------------

    cursor.execute(
        """
        INSERT OR IGNORE INTO user_level_progress (
            user_id,
            level_id,
            status,
            best_exam_score,
            exam_attempts
        )
        SELECT
            ?,
            id,
            'locked',
            0,
            0
        FROM course_levels
        WHERE is_active = 1
        """,
        (user_id,),
    )

    # --------------------------------------------------------
    # LESSON PROGRESS
    # --------------------------------------------------------

    cursor.execute(
        """
        INSERT OR IGNORE INTO lesson_progress (
            user_id,
            lesson_id,
            status,
            score,
            best_score,
            attempts
        )
        SELECT
            ?,
            id,
            'locked',
            0,
            0,
            0
        FROM lessons
        WHERE is_active = 1
        """,
        (user_id,),
    )


def _sync_user_access(
    cursor,
    user_id: int,
):
    """
    Progress asosida Level va darslarning
    locked / available / completed holatini
    yangilaydi.
    """

    _ensure_progress_rows(
        cursor,
        user_id,
    )

    cursor.execute(
        """
        SELECT
            l.id,
            l.code,
            l.sort_order,

            COALESCE(
                ulp.status,
                'locked'
            ) AS saved_status

        FROM course_levels l

        LEFT JOIN user_level_progress ulp
            ON ulp.level_id = l.id
           AND ulp.user_id = ?

        WHERE l.is_active = 1

        ORDER BY
            l.sort_order,
            l.id
        """,
        (user_id,),
    )

    levels = cursor.fetchall()

    first_open_level_id = None

    for level in levels:

        level_id = level["id"]

        # ----------------------------------------------------
        # EXAM PASSED?
        # ----------------------------------------------------

        cursor.execute(
            """
            SELECT 1

            FROM level_exam_attempts lea

            JOIN level_exams le
                ON le.id = lea.exam_id

            WHERE lea.user_id = ?
              AND le.level_id = ?
              AND lea.passed = 1

            LIMIT 1
            """,
            (
                user_id,
                level_id,
            ),
        )

        exam_passed = (
            cursor.fetchone()
            is not None
        )

        saved_status = (
            level["saved_status"]
        )

        # ----------------------------------------------------
        # LEVEL STATUS
        # ----------------------------------------------------

        if (
            exam_passed
            or saved_status == "completed"
        ):
            desired_status = (
                "completed"
            )

        elif first_open_level_id is None:

            desired_status = (
                "available"
            )

            first_open_level_id = (
                level_id
            )

        else:

            desired_status = (
                "locked"
            )

        cursor.execute(
            """
            UPDATE user_level_progress

            SET status = ?

            WHERE user_id = ?
              AND level_id = ?
            """,
            (
                desired_status,
                user_id,
                level_id,
            ),
        )

        # ----------------------------------------------------
        # LEVEL LESSONS
        # ----------------------------------------------------

        cursor.execute(
            """
            SELECT
                ls.id,

                COALESCE(
                    lp.status,
                    'locked'
                ) AS progress_status

            FROM lessons ls

            JOIN course_modules m
                ON m.id = ls.module_id

            LEFT JOIN lesson_progress lp
                ON lp.lesson_id = ls.id
               AND lp.user_id = ?

            WHERE m.level_id = ?
              AND ls.is_active = 1

            ORDER BY
                m.sort_order,
                m.id,
                ls.sort_order,
                ls.id
            """,
            (
                user_id,
                level_id,
            ),
        )

        lessons = cursor.fetchall()

        # ----------------------------------------------------
        # LOCKED LEVEL
        # ----------------------------------------------------

        if desired_status == "locked":

            for lesson in lessons:

                if (
                    lesson["progress_status"]
                    != "completed"
                ):

                    cursor.execute(
                        """
                        UPDATE lesson_progress

                        SET status = 'locked'

                        WHERE user_id = ?
                          AND lesson_id = ?
                        """,
                        (
                            user_id,
                            lesson["id"],
                        ),
                    )

            continue

        # ----------------------------------------------------
        # COMPLETED LEVEL
        # ----------------------------------------------------

        if desired_status == "completed":
            continue

        # ----------------------------------------------------
        # AVAILABLE LEVEL
        #
        # Birinchi tugallanmagan dars ochiladi.
        # ----------------------------------------------------

        open_lesson_found = False

        for lesson in lessons:

            lesson_id = (
                lesson["id"]
            )

            status = (
                lesson[
                    "progress_status"
                ]
            )

            if status == "completed":
                continue

            if not open_lesson_found:

                new_status = (
                    "available"
                )

                open_lesson_found = True

            else:

                new_status = (
                    "locked"
                )

            cursor.execute(
                """
                UPDATE lesson_progress

                SET status = ?

                WHERE user_id = ?
                  AND lesson_id = ?
                """,
                (
                    new_status,
                    user_id,
                    lesson_id,
                ),
            )


# ============================================================
# INITIALIZE USER PROGRESS
# ============================================================

def initialize_user_progress(
    user_id: int | None = None,
) -> dict:
    """
    user_id berilsa bitta foydalanuvchi.

    user_id berilmasa barcha aktiv
    foydalanuvchilar uchun progress yaratiladi.
    """

    connection = get_connection()

    try:
        cursor = connection.cursor()

        if user_id is None:

            cursor.execute(
                """
                SELECT id

                FROM users

                WHERE is_active = 1

                ORDER BY id
                """
            )

            user_ids = [
                row["id"]
                for row
                in cursor.fetchall()
            ]

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

            user = cursor.fetchone()

            if user is None:

                return {
                    "success": False,
                    "message": (
                        "Foydalanuvchi topilmadi."
                    ),
                }

            user_ids = [
                user_id
            ]

        for current_user_id in user_ids:

            _sync_user_access(
                cursor,
                current_user_id,
            )

        connection.commit()

        return {
            "success": True,
            "users_processed": (
                len(user_ids)
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
# COMPLETE LESSON
# ============================================================

def complete_lesson(
    user_id: int,
    lesson_id: int,
    score: int = 100,
) -> dict:
    """
    Darsni tugallangan deb belgilaydi.

    DashboardWindow va LearningWindow
    shu funksiyani ishlatadi.
    """

    connection = get_connection()

    try:
        cursor = connection.cursor()

        _ensure_progress_rows(
            cursor,
            user_id,
        )

        cursor.execute(
            """
            SELECT
                id,
                xp_reward,
                passing_score

            FROM lessons

            WHERE id = ?
              AND is_active = 1

            LIMIT 1
            """,
            (lesson_id,),
        )

        lesson = cursor.fetchone()

        if lesson is None:

            return {
                "success": False,
                "message": (
                    "Dars topilmadi."
                ),
            }

        try:
            score = int(score)

        except (
            TypeError,
            ValueError,
        ):
            score = 100

        score = max(
            0,
            min(
                100,
                score,
            ),
        )

        now = (
            datetime.now().isoformat(
                timespec="seconds"
            )
        )

        cursor.execute(
            """
            SELECT
                best_score,
                attempts,
                started_at

            FROM lesson_progress

            WHERE user_id = ?
              AND lesson_id = ?

            LIMIT 1
            """,
            (
                user_id,
                lesson_id,
            ),
        )

        progress = cursor.fetchone()

        previous_best = (
            progress["best_score"]
            if progress
            else 0
        ) or 0

        previous_attempts = (
            progress["attempts"]
            if progress
            else 0
        ) or 0

        started_at = (
            progress["started_at"]
            if progress
            else None
        )

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

            ON CONFLICT(
                user_id,
                lesson_id
            )

            DO UPDATE SET
                status = excluded.status,

                score = excluded.score,

                best_score = excluded.best_score,

                attempts = excluded.attempts,

                started_at = COALESCE(
                    lesson_progress.started_at,
                    excluded.started_at
                ),

                completed_at =
                    excluded.completed_at,

                last_opened_at =
                    excluded.last_opened_at
            """,
            (
                user_id,
                lesson_id,
                "completed",
                score,
                max(
                    previous_best,
                    score,
                ),
                previous_attempts + 1,
                started_at or now,
                now,
                now,
            ),
        )

        _sync_user_access(
            cursor,
            user_id,
        )

        connection.commit()

        return {
            "success": True,
            "lesson_id": lesson_id,
            "score": score,
            "best_score": max(
                previous_best,
                score,
            ),
            "xp_reward": (
                lesson["xp_reward"]
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
# CURRENT LEVEL
# ============================================================

def get_current_level(
    user_id: int,
) -> dict | None:

    connection = get_connection()

    try:
        cursor = connection.cursor()

        _sync_user_access(
            cursor,
            user_id,
        )

        connection.commit()

        # ----------------------------------------------------
        # AVAILABLE LEVEL
        # ----------------------------------------------------

        cursor.execute(
            """
            SELECT
                l.*,

                ulp.status
                    AS level_status,

                ulp.best_exam_score,

                ulp.exam_attempts

            FROM course_levels l

            JOIN user_level_progress ulp
                ON ulp.level_id = l.id

            WHERE ulp.user_id = ?
              AND ulp.status = 'available'
              AND l.is_active = 1

            ORDER BY
                l.sort_order,
                l.id

            LIMIT 1
            """,
            (user_id,),
        )

        row = cursor.fetchone()

        if row is not None:

            return _row_to_dict(
                row
            )

        # ----------------------------------------------------
        # ALL COMPLETED BO'LSA OXIRGI LEVEL
        # ----------------------------------------------------

        cursor.execute(
            """
            SELECT
                l.*,

                ulp.status
                    AS level_status,

                ulp.best_exam_score,

                ulp.exam_attempts

            FROM course_levels l

            JOIN user_level_progress ulp
                ON ulp.level_id = l.id

            WHERE ulp.user_id = ?
              AND l.is_active = 1

            ORDER BY
                l.sort_order DESC,
                l.id DESC

            LIMIT 1
            """,
            (user_id,),
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
# NEXT AVAILABLE LESSON
# ============================================================

def get_next_available_lesson(
    user_id: int,
) -> dict | None:

    connection = get_connection()

    try:
        cursor = connection.cursor()

        _sync_user_access(
            cursor,
            user_id,
        )

        connection.commit()

        cursor.execute(
            """
            SELECT
                ls.*,

                lp.status,
                lp.score,
                lp.best_score,
                lp.attempts,

                m.title
                    AS module_title,

                m.code
                    AS module_code,

                l.title
                    AS level_title,

                l.code
                    AS level_code

            FROM lesson_progress lp

            JOIN lessons ls
                ON ls.id = lp.lesson_id

            JOIN course_modules m
                ON m.id = ls.module_id

            JOIN course_levels l
                ON l.id = m.level_id

            JOIN user_level_progress ulp
                ON ulp.level_id = l.id
               AND ulp.user_id = lp.user_id

            WHERE lp.user_id = ?
              AND lp.status = 'available'
              AND ulp.status = 'available'
              AND ls.is_active = 1
              AND m.is_active = 1
              AND l.is_active = 1

            ORDER BY
                l.sort_order,
                m.sort_order,
                ls.sort_order,
                ls.id

            LIMIT 1
            """,
            (user_id,),
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
# USER COURSE STATS
# ============================================================

def get_user_course_stats(
    user_id: int,
) -> dict:

    connection = get_connection()

    try:
        cursor = connection.cursor()

        _sync_user_access(
            cursor,
            user_id,
        )

        connection.commit()

        # ----------------------------------------------------
        # TOTAL LESSONS
        # ----------------------------------------------------

        cursor.execute(
            """
            SELECT COUNT(*) AS total

            FROM lessons

            WHERE is_active = 1
            """
        )

        total_lessons = (
            cursor.fetchone()[
                "total"
            ]
        )

        # ----------------------------------------------------
        # COMPLETED LESSONS
        # ----------------------------------------------------

        cursor.execute(
            """
            SELECT COUNT(*) AS completed

            FROM lesson_progress lp

            JOIN lessons ls
                ON ls.id = lp.lesson_id

            WHERE lp.user_id = ?
              AND lp.status = 'completed'
              AND ls.is_active = 1
            """,
            (user_id,),
        )

        completed_lessons = (
            cursor.fetchone()[
                "completed"
            ]
        )

        # ----------------------------------------------------
        # LESSON XP
        # ----------------------------------------------------

        cursor.execute(
            """
            SELECT
                COALESCE(
                    SUM(ls.xp_reward),
                    0
                ) AS lesson_xp

            FROM lesson_progress lp

            JOIN lessons ls
                ON ls.id = lp.lesson_id

            WHERE lp.user_id = ?
              AND lp.status = 'completed'
              AND ls.is_active = 1
            """,
            (user_id,),
        )

        lesson_xp = (
            cursor.fetchone()[
                "lesson_xp"
            ]
        )

        # ----------------------------------------------------
        # EXAM XP
        #
        # Bir exam bir necha marta topshirilsa ham
        # XP bir marta hisoblanadi.
        # ----------------------------------------------------

        cursor.execute(
            """
            SELECT
                COALESCE(
                    SUM(le.xp_reward),
                    0
                ) AS exam_xp

            FROM level_exams le

            WHERE EXISTS (
                SELECT 1

                FROM level_exam_attempts lea

                WHERE lea.exam_id = le.id
                  AND lea.user_id = ?
                  AND lea.passed = 1
            )
            """,
            (user_id,),
        )

        exam_xp = (
            cursor.fetchone()[
                "exam_xp"
            ]
        )

        # ----------------------------------------------------
        # PROGRESS
        # ----------------------------------------------------

        if total_lessons:

            progress_percent = round(
                (
                    completed_lessons
                    / total_lessons
                )
                * 100
            )

        else:

            progress_percent = 0

        return {
            "total_lessons": (
                total_lessons
            ),
            "completed_lessons": (
                completed_lessons
            ),
            "progress_percent": (
                progress_percent
            ),
            "lesson_xp": int(
                lesson_xp or 0
            ),
            "exam_xp": int(
                exam_xp or 0
            ),
            "xp": int(
                (lesson_xp or 0)
                + (exam_xp or 0)
            ),
        }

    finally:
        connection.close()


# ============================================================
# LEARNING OVERVIEW
# ============================================================

def get_learning_overview(
    user_id: int,
) -> list[dict]:
    """
    LearningWindow kutayotgan strukturani qaytaradi:

    LEVEL
      -> modules
          -> lessons
    """

    connection = get_connection()

    try:
        cursor = connection.cursor()

        _sync_user_access(
            cursor,
            user_id,
        )

        connection.commit()

        cursor.execute(
            """
            SELECT
                l.*,

                COALESCE(
                    ulp.status,
                    'locked'
                ) AS level_status,

                COALESCE(
                    ulp.best_exam_score,
                    0
                ) AS best_exam_score,

                COALESCE(
                    ulp.exam_attempts,
                    0
                ) AS exam_attempts

            FROM course_levels l

            LEFT JOIN user_level_progress ulp
                ON ulp.level_id = l.id
               AND ulp.user_id = ?

            WHERE l.is_active = 1

            ORDER BY
                l.sort_order,
                l.id
            """,
            (user_id,),
        )

        level_rows = (
            cursor.fetchall()
        )

        levels = []

        for level_row in level_rows:

            level = _row_to_dict(
                level_row
            )

            # ------------------------------------------------
            # MODULES
            # ------------------------------------------------

            cursor.execute(
                """
                SELECT *

                FROM course_modules

                WHERE level_id = ?
                  AND is_active = 1

                ORDER BY
                    sort_order,
                    id
                """,
                (
                    level["id"],
                ),
            )

            module_rows = (
                cursor.fetchall()
            )

            modules = []

            level_total_lessons = 0

            level_completed_lessons = 0

            for module_row in module_rows:

                module = _row_to_dict(
                    module_row
                )

                # --------------------------------------------
                # LESSONS
                # --------------------------------------------

                cursor.execute(
                    """
                    SELECT
                        ls.*,

                        COALESCE(
                            lp.status,
                            'locked'
                        ) AS status,

                        COALESCE(
                            lp.score,
                            0
                        ) AS score,

                        COALESCE(
                            lp.best_score,
                            0
                        ) AS best_score,

                        COALESCE(
                            lp.attempts,
                            0
                        ) AS attempts,

                        lp.started_at,

                        lp.completed_at,

                        lp.last_opened_at

                    FROM lessons ls

                    LEFT JOIN lesson_progress lp
                        ON lp.lesson_id = ls.id
                       AND lp.user_id = ?

                    WHERE ls.module_id = ?
                      AND ls.is_active = 1

                    ORDER BY
                        ls.sort_order,
                        ls.id
                    """,
                    (
                        user_id,
                        module["id"],
                    ),
                )

                lessons = [
                    _row_to_dict(
                        row
                    )
                    for row
                    in cursor.fetchall()
                ]

                total_lessons = (
                    len(lessons)
                )

                completed_lessons = sum(
                    1
                    for lesson in lessons
                    if (
                        lesson["status"]
                        == "completed"
                    )
                )

                module[
                    "total_lessons"
                ] = total_lessons

                module[
                    "completed_lessons"
                ] = completed_lessons

                if total_lessons:

                    module[
                        "progress_percent"
                    ] = round(
                        (
                            completed_lessons
                            / total_lessons
                        )
                        * 100
                    )

                else:

                    module[
                        "progress_percent"
                    ] = 0

                module[
                    "lessons"
                ] = lessons

                modules.append(
                    module
                )

                level_total_lessons += (
                    total_lessons
                )

                level_completed_lessons += (
                    completed_lessons
                )

            # ------------------------------------------------
            # LEVEL TOTALS
            # ------------------------------------------------

            level[
                "total_lessons"
            ] = level_total_lessons

            level[
                "completed_lessons"
            ] = level_completed_lessons

            if level_total_lessons:

                level[
                    "progress_percent"
                ] = round(
                    (
                        level_completed_lessons
                        / level_total_lessons
                    )
                    * 100
                )

            else:

                level[
                    "progress_percent"
                ] = 0

            level[
                "modules"
            ] = modules

            levels.append(
                level
            )

        return levels

    finally:
        connection.close()


# ============================================================
# LESSON PROGRESS READ
# ============================================================

def get_lesson_progress(
    user_id: int,
    lesson_id: int,
) -> dict | None:

    connection = get_connection()

    try:
        cursor = connection.cursor()

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
                lesson_id,
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

            WHERE is_active = 1

            ORDER BY
                sort_order,
                id
            """
        )

        return [
            _row_to_dict(
                row
            )
            for row
            in cursor.fetchall()
        ]

    finally:
        connection.close()


def get_level_modules(
    level_id: int,
) -> list[dict]:

    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT *

            FROM course_modules

            WHERE level_id = ?
              AND is_active = 1

            ORDER BY
                sort_order,
                id
            """,
            (level_id,),
        )

        return [
            _row_to_dict(
                row
            )
            for row
            in cursor.fetchall()
        ]

    finally:
        connection.close()


def get_module_lessons(
    module_id: int,
) -> list[dict]:

    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT *

            FROM lessons

            WHERE module_id = ?
              AND is_active = 1

            ORDER BY
                sort_order,
                id
            """,
            (module_id,),
        )

        return [
            _row_to_dict(
                row
            )
            for row
            in cursor.fetchall()
        ]

    finally:
        connection.close()


# ============================================================
# CONTENT REGISTRY COMPATIBILITY
# ============================================================

def get_all_lesson_content():

    from courses.content_registry import (
        get_all_lesson_content
        as registry_get_all_lesson_content,
    )

    return (
        registry_get_all_lesson_content()
    )


def get_lesson_content_by_code(
    lesson_code: str,
):

    from courses.content_registry import (
        get_lesson_content_by_code
        as registry_get_lesson_content_by_code,
    )

    return (
        registry_get_lesson_content_by_code(
            lesson_code
        )
    )


def get_all_quiz_data():

    from courses.content_registry import (
        get_all_quiz_data
        as registry_get_all_quiz_data,
    )

    return (
        registry_get_all_quiz_data()
    )
