import os
import sqlite3
from pathlib import Path


# ============================================================
# DATABASE LOCATION
# ============================================================

def get_app_data_directory() -> Path:
    """
    Windows'da:
    %LOCALAPPDATA%/ARCHIPRO_UZ/data/

    LOCALAPPDATA topilmasa user home papkasidan foydalanadi.
    """

    local_app_data = os.getenv(
        "LOCALAPPDATA"
    )

    if local_app_data:
        base_directory = Path(
            local_app_data
        )
    else:
        base_directory = Path.home()

    app_directory = (
        base_directory
        / "ARCHIPRO_UZ"
        / "data"
    )

    app_directory.mkdir(
        parents=True,
        exist_ok=True,
    )

    return app_directory


_DATABASE_OVERRIDE = os.getenv(
    "ARCHIPRO_UZ_DATABASE_PATH"
)

if _DATABASE_OVERRIDE:
    DATABASE_PATH = Path(
        _DATABASE_OVERRIDE
    )

    DATABASE_PATH.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

else:
    DATABASE_PATH = (
        get_app_data_directory()
        / "archipro.db"
    )


# ============================================================
# CONNECTION
# ============================================================

def get_connection():
    connection = sqlite3.connect(
        DATABASE_PATH
    )

    connection.row_factory = (
        sqlite3.Row
    )

    connection.execute(
        "PRAGMA foreign_keys = ON"
    )

    return connection


# ============================================================
# MIGRATION HELPERS
# ============================================================

def table_exists(
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


def column_exists(
    cursor,
    table_name: str,
    column_name: str,
) -> bool:

    if not table_exists(
        cursor,
        table_name,
    ):
        return False

    cursor.execute(
        f"PRAGMA table_info({table_name})"
    )

    for column in cursor.fetchall():

        if (
            column["name"]
            == column_name
        ):
            return True

    return False


def ensure_column(
    cursor,
    table_name: str,
    column_name: str,
    column_definition: str,
):
    """
    Eski database'da yangi ustun bo'lmasa,
    ALTER TABLE orqali avtomatik qo'shadi.
    """

    if not column_exists(
        cursor,
        table_name,
        column_name,
    ):

        cursor.execute(
            f"""
            ALTER TABLE {table_name}
            ADD COLUMN {column_name}
            {column_definition}
            """
        )


# ============================================================
# INITIALIZE DATABASE
# ============================================================

def initialize_database():

    connection = get_connection()

    try:
        cursor = connection.cursor()

        # ====================================================
        # USERS
        # ====================================================

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,

                username TEXT NOT NULL UNIQUE,

                password_hash TEXT NOT NULL,

                password_salt TEXT NOT NULL,

                full_name TEXT DEFAULT '',

                license_type TEXT NOT NULL DEFAULT 'PRO',

                is_active INTEGER NOT NULL DEFAULT 1,

                created_at TEXT NOT NULL
                    DEFAULT CURRENT_TIMESTAMP,

                last_login TEXT
            )
            """
        )

        # ====================================================
        # APP SETTINGS
        # ====================================================

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS app_settings (
                id INTEGER PRIMARY KEY AUTOINCREMENT,

                setting_key TEXT NOT NULL UNIQUE,

                setting_value TEXT
            )
            """
        )

        # ====================================================
        # COURSE LEVELS
        # ====================================================

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS course_levels (
                id INTEGER PRIMARY KEY AUTOINCREMENT,

                code TEXT NOT NULL UNIQUE,

                title TEXT NOT NULL,

                subtitle TEXT DEFAULT '',

                description TEXT DEFAULT '',

                sort_order INTEGER NOT NULL DEFAULT 0,

                minimum_mastery_score
                    INTEGER NOT NULL DEFAULT 85,

                is_active INTEGER NOT NULL DEFAULT 1
            )
            """
        )

        # ====================================================
        # COURSE MODULES
        # ====================================================

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS course_modules (
                id INTEGER PRIMARY KEY AUTOINCREMENT,

                level_id INTEGER NOT NULL,

                code TEXT NOT NULL UNIQUE,

                title TEXT NOT NULL,

                description TEXT DEFAULT '',

                sort_order INTEGER NOT NULL DEFAULT 0,

                estimated_minutes
                    INTEGER NOT NULL DEFAULT 0,

                minimum_mastery_score
                    INTEGER NOT NULL DEFAULT 85,

                is_active INTEGER NOT NULL DEFAULT 1,

                FOREIGN KEY(level_id)
                    REFERENCES course_levels(id)
                    ON DELETE CASCADE
            )
            """
        )

        # ====================================================
        # LESSONS
        # ====================================================

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS lessons (
                id INTEGER PRIMARY KEY AUTOINCREMENT,

                module_id INTEGER NOT NULL,

                code TEXT NOT NULL UNIQUE,

                title TEXT NOT NULL,

                lesson_type TEXT NOT NULL DEFAULT 'theory',

                summary TEXT DEFAULT '',

                sort_order INTEGER NOT NULL DEFAULT 0,

                estimated_minutes
                    INTEGER NOT NULL DEFAULT 10,

                xp_reward
                    INTEGER NOT NULL DEFAULT 10,

                passing_score
                    INTEGER NOT NULL DEFAULT 80,

                is_required
                    INTEGER NOT NULL DEFAULT 1,

                is_active
                    INTEGER NOT NULL DEFAULT 1,

                FOREIGN KEY(module_id)
                    REFERENCES course_modules(id)
                    ON DELETE CASCADE
            )
            """
        )

        # ====================================================
        # LESSON PROGRESS
        # ====================================================

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS lesson_progress (
                id INTEGER PRIMARY KEY AUTOINCREMENT,

                user_id INTEGER NOT NULL,

                lesson_id INTEGER NOT NULL,

                status TEXT NOT NULL DEFAULT 'locked',

                score INTEGER NOT NULL DEFAULT 0,

                best_score INTEGER NOT NULL DEFAULT 0,

                attempts INTEGER NOT NULL DEFAULT 0,

                started_at TEXT,

                completed_at TEXT,

                last_opened_at TEXT,

                UNIQUE(
                    user_id,
                    lesson_id
                ),

                FOREIGN KEY(user_id)
                    REFERENCES users(id)
                    ON DELETE CASCADE,

                FOREIGN KEY(lesson_id)
                    REFERENCES lessons(id)
                    ON DELETE CASCADE
            )
            """
        )

        # ====================================================
        # CUSTOMER CONVENIENCE
        # ====================================================

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS lesson_bookmarks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,

                user_id INTEGER NOT NULL,

                lesson_id INTEGER NOT NULL,

                created_at TEXT NOT NULL
                    DEFAULT CURRENT_TIMESTAMP,

                UNIQUE(
                    user_id,
                    lesson_id
                ),

                FOREIGN KEY(user_id)
                    REFERENCES users(id)
                    ON DELETE CASCADE,

                FOREIGN KEY(lesson_id)
                    REFERENCES lessons(id)
                    ON DELETE CASCADE
            )
            """
        )

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS lesson_notes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,

                user_id INTEGER NOT NULL,

                lesson_id INTEGER NOT NULL,

                note_text TEXT NOT NULL DEFAULT '',

                updated_at TEXT NOT NULL
                    DEFAULT CURRENT_TIMESTAMP,

                UNIQUE(
                    user_id,
                    lesson_id
                ),

                FOREIGN KEY(user_id)
                    REFERENCES users(id)
                    ON DELETE CASCADE,

                FOREIGN KEY(lesson_id)
                    REFERENCES lessons(id)
                    ON DELETE CASCADE
            )
            """
        )

        # ====================================================
        # QUIZ QUESTIONS
        # ====================================================

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS quiz_questions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,

                lesson_id INTEGER NOT NULL,

                code TEXT NOT NULL UNIQUE,

                question_text TEXT NOT NULL,

                explanation TEXT DEFAULT '',

                sort_order INTEGER NOT NULL DEFAULT 0,

                FOREIGN KEY(lesson_id)
                    REFERENCES lessons(id)
                    ON DELETE CASCADE
            )
            """
        )

        # ====================================================
        # QUIZ OPTIONS
        # ====================================================

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS quiz_options (
                id INTEGER PRIMARY KEY AUTOINCREMENT,

                question_id INTEGER NOT NULL,

                option_key TEXT NOT NULL,

                option_text TEXT NOT NULL,

                is_correct
                    INTEGER NOT NULL DEFAULT 0,

                FOREIGN KEY(question_id)
                    REFERENCES quiz_questions(id)
                    ON DELETE CASCADE
            )
            """
        )

        # ====================================================
        # QUIZ ATTEMPTS
        # ====================================================

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS quiz_attempts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,

                user_id INTEGER NOT NULL,

                lesson_id INTEGER NOT NULL,

                score INTEGER NOT NULL,

                passed INTEGER NOT NULL DEFAULT 0,

                created_at TEXT NOT NULL
                    DEFAULT CURRENT_TIMESTAMP,

                FOREIGN KEY(user_id)
                    REFERENCES users(id)
                    ON DELETE CASCADE,

                FOREIGN KEY(lesson_id)
                    REFERENCES lessons(id)
                    ON DELETE CASCADE
            )
            """
        )

        # ====================================================
        # LEVEL EXAMS
        # ====================================================

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS level_exams (
                id INTEGER PRIMARY KEY AUTOINCREMENT,

                level_id INTEGER NOT NULL UNIQUE,

                title TEXT NOT NULL,

                description TEXT DEFAULT '',

                question_count
                    INTEGER NOT NULL DEFAULT 20,

                passing_score
                    INTEGER NOT NULL DEFAULT 85,

                xp_reward
                    INTEGER NOT NULL DEFAULT 200,

                is_active
                    INTEGER NOT NULL DEFAULT 1,

                FOREIGN KEY(level_id)
                    REFERENCES course_levels(id)
                    ON DELETE CASCADE
            )
            """
        )

        # ====================================================
        # LEVEL EXAM ATTEMPTS
        # ====================================================

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS level_exam_attempts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,

                user_id INTEGER NOT NULL,

                exam_id INTEGER NOT NULL,

                score INTEGER NOT NULL,

                correct_answers INTEGER NOT NULL,

                total_questions INTEGER NOT NULL,

                passed INTEGER NOT NULL DEFAULT 0,

                created_at TEXT NOT NULL
                    DEFAULT CURRENT_TIMESTAMP,

                FOREIGN KEY(user_id)
                    REFERENCES users(id)
                    ON DELETE CASCADE,

                FOREIGN KEY(exam_id)
                    REFERENCES level_exams(id)
                    ON DELETE CASCADE
            )
            """
        )

        # ====================================================
        # USER LEVEL PROGRESS
        # ====================================================

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS user_level_progress (
                id INTEGER PRIMARY KEY AUTOINCREMENT,

                user_id INTEGER NOT NULL,

                level_id INTEGER NOT NULL,

                status TEXT NOT NULL DEFAULT 'locked',

                best_exam_score
                    INTEGER NOT NULL DEFAULT 0,

                exam_attempts
                    INTEGER NOT NULL DEFAULT 0,

                completed_at TEXT,

                UNIQUE(
                    user_id,
                    level_id
                ),

                FOREIGN KEY(user_id)
                    REFERENCES users(id)
                    ON DELETE CASCADE,

                FOREIGN KEY(level_id)
                    REFERENCES course_levels(id)
                    ON DELETE CASCADE
            )
            """
        )

        # ====================================================
        # SAFE MIGRATIONS
        # ====================================================

        ensure_column(
            cursor,
            "course_levels",
            "minimum_mastery_score",
            "INTEGER NOT NULL DEFAULT 85",
        )

        ensure_column(
            cursor,
            "course_levels",
            "is_active",
            "INTEGER NOT NULL DEFAULT 1",
        )

        # ----------------------------------------------------
        # COURSE MODULES
        # ----------------------------------------------------

        ensure_column(
            cursor,
            "course_modules",
            "estimated_minutes",
            "INTEGER NOT NULL DEFAULT 0",
        )

        ensure_column(
            cursor,
            "course_modules",
            "minimum_mastery_score",
            "INTEGER NOT NULL DEFAULT 85",
        )

        ensure_column(
            cursor,
            "course_modules",
            "is_active",
            "INTEGER NOT NULL DEFAULT 1",
        )

        # ----------------------------------------------------
        # LESSONS
        # ----------------------------------------------------

        ensure_column(
            cursor,
            "lessons",
            "estimated_minutes",
            "INTEGER NOT NULL DEFAULT 10",
        )

        ensure_column(
            cursor,
            "lessons",
            "xp_reward",
            "INTEGER NOT NULL DEFAULT 10",
        )

        ensure_column(
            cursor,
            "lessons",
            "passing_score",
            "INTEGER NOT NULL DEFAULT 80",
        )

        ensure_column(
            cursor,
            "lessons",
            "is_required",
            "INTEGER NOT NULL DEFAULT 1",
        )

        ensure_column(
            cursor,
            "lessons",
            "is_active",
            "INTEGER NOT NULL DEFAULT 1",
        )

        # ----------------------------------------------------
        # LESSON PROGRESS
        # ----------------------------------------------------

        ensure_column(
            cursor,
            "lesson_progress",
            "status",
            "TEXT NOT NULL DEFAULT 'locked'",
        )

        ensure_column(
            cursor,
            "lesson_progress",
            "score",
            "INTEGER NOT NULL DEFAULT 0",
        )

        ensure_column(
            cursor,
            "lesson_progress",
            "best_score",
            "INTEGER NOT NULL DEFAULT 0",
        )

        ensure_column(
            cursor,
            "lesson_progress",
            "attempts",
            "INTEGER NOT NULL DEFAULT 0",
        )

        ensure_column(
            cursor,
            "lesson_progress",
            "started_at",
            "TEXT",
        )

        ensure_column(
            cursor,
            "lesson_progress",
            "completed_at",
            "TEXT",
        )

        ensure_column(
            cursor,
            "lesson_progress",
            "last_opened_at",
            "TEXT",
        )

        # ----------------------------------------------------
        # LEVEL EXAMS
        # ----------------------------------------------------

        ensure_column(
            cursor,
            "level_exams",
            "description",
            "TEXT DEFAULT ''",
        )

        ensure_column(
            cursor,
            "level_exams",
            "question_count",
            "INTEGER NOT NULL DEFAULT 20",
        )

        ensure_column(
            cursor,
            "level_exams",
            "passing_score",
            "INTEGER NOT NULL DEFAULT 85",
        )

        ensure_column(
            cursor,
            "level_exams",
            "xp_reward",
            "INTEGER NOT NULL DEFAULT 200",
        )

        ensure_column(
            cursor,
            "level_exams",
            "is_active",
            "INTEGER NOT NULL DEFAULT 1",
        )

        # ----------------------------------------------------
        # USER LEVEL PROGRESS
        # ----------------------------------------------------

        ensure_column(
            cursor,
            "user_level_progress",
            "status",
            "TEXT NOT NULL DEFAULT 'locked'",
        )

        ensure_column(
            cursor,
            "user_level_progress",
            "best_exam_score",
            "INTEGER NOT NULL DEFAULT 0",
        )

        ensure_column(
            cursor,
            "user_level_progress",
            "exam_attempts",
            "INTEGER NOT NULL DEFAULT 0",
        )

        ensure_column(
            cursor,
            "user_level_progress",
            "completed_at",
            "TEXT",
        )

        # ====================================================
        # INDEXES
        # ====================================================

        cursor.execute(
            """
            CREATE INDEX IF NOT EXISTS
            idx_modules_level
            ON course_modules(level_id)
            """
        )

        cursor.execute(
            """
            CREATE INDEX IF NOT EXISTS
            idx_lessons_module
            ON lessons(module_id)
            """
        )

        cursor.execute(
            """
            CREATE INDEX IF NOT EXISTS
            idx_lesson_progress_user
            ON lesson_progress(user_id)
            """
        )

        cursor.execute(
            """
            CREATE INDEX IF NOT EXISTS
            idx_bookmarks_user
            ON lesson_bookmarks(user_id)
            """
        )

        cursor.execute(
            """
            CREATE INDEX IF NOT EXISTS
            idx_notes_user
            ON lesson_notes(user_id)
            """
        )

        cursor.execute(
            """
            CREATE INDEX IF NOT EXISTS
            idx_quiz_questions_lesson
            ON quiz_questions(lesson_id)
            """
        )

        cursor.execute(
            """
            CREATE INDEX IF NOT EXISTS
            idx_quiz_attempts_user_lesson
            ON quiz_attempts(
                user_id,
                lesson_id
            )
            """
        )

        cursor.execute(
            """
            CREATE INDEX IF NOT EXISTS
            idx_level_progress_user
            ON user_level_progress(user_id)
            """
        )

        cursor.execute(
            """
            CREATE INDEX IF NOT EXISTS
            idx_exam_attempts_user_exam
            ON level_exam_attempts(
                user_id,
                exam_id
            )
            """
        )

        connection.commit()

    except Exception:
        connection.rollback()
        raise

    finally:
        connection.close()
