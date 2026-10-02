import os
import sqlite3
from pathlib import Path


APP_NAME = "ARCHIPRO_UZ"


def get_app_data_dir() -> Path:
    local_app_data = os.getenv("LOCALAPPDATA")

    if local_app_data:
        base_dir = Path(local_app_data)
    else:
        base_dir = Path.home()

    app_dir = base_dir / APP_NAME

    app_dir.mkdir(
        parents=True,
        exist_ok=True,
    )

    return app_dir


def get_database_path() -> Path:
    data_dir = (
        get_app_data_dir()
        / "data"
    )

    data_dir.mkdir(
        parents=True,
        exist_ok=True,
    )

    return (
        data_dir
        / "archipro.db"
    )


def get_connection() -> sqlite3.Connection:
    connection = sqlite3.connect(
        get_database_path()
    )

    connection.row_factory = (
        sqlite3.Row
    )

    connection.execute(
        "PRAGMA foreign_keys = ON"
    )

    return connection


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
                full_name TEXT,
                license_type TEXT DEFAULT 'PRO',
                is_active INTEGER NOT NULL DEFAULT 1,
                created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
                last_login TEXT
            )
            """
        )

        # ====================================================
        # SETTINGS
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
                subtitle TEXT,
                description TEXT,
                sort_order INTEGER NOT NULL,
                minimum_mastery_score INTEGER NOT NULL DEFAULT 85,
                created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
            )
            """
        )

        # ====================================================
        # MODULES
        # ====================================================

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS course_modules (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                level_id INTEGER NOT NULL,
                code TEXT NOT NULL UNIQUE,
                title TEXT NOT NULL,
                description TEXT,
                sort_order INTEGER NOT NULL,
                estimated_minutes INTEGER NOT NULL DEFAULT 0,
                minimum_mastery_score INTEGER NOT NULL DEFAULT 85,

                FOREIGN KEY (level_id)
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
                summary TEXT,
                content_text TEXT,
                sort_order INTEGER NOT NULL,
                estimated_minutes INTEGER NOT NULL DEFAULT 10,
                xp_reward INTEGER NOT NULL DEFAULT 10,
                passing_score INTEGER NOT NULL DEFAULT 80,
                is_required INTEGER NOT NULL DEFAULT 1,

                FOREIGN KEY (module_id)
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
                last_opened_at TEXT,
                completed_at TEXT,

                UNIQUE(user_id, lesson_id),

                FOREIGN KEY (user_id)
                    REFERENCES users(id)
                    ON DELETE CASCADE,

                FOREIGN KEY (lesson_id)
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
                explanation TEXT,
                sort_order INTEGER NOT NULL,

                FOREIGN KEY (lesson_id)
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
                is_correct INTEGER NOT NULL DEFAULT 0,

                UNIQUE(
                    question_id,
                    option_key
                ),

                FOREIGN KEY (question_id)
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
                created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,

                FOREIGN KEY (user_id)
                    REFERENCES users(id)
                    ON DELETE CASCADE,

                FOREIGN KEY (lesson_id)
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
                description TEXT,
                question_count INTEGER NOT NULL DEFAULT 20,
                passing_score INTEGER NOT NULL DEFAULT 85,
                xp_reward INTEGER NOT NULL DEFAULT 200,
                is_active INTEGER NOT NULL DEFAULT 1,

                FOREIGN KEY (level_id)
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
                correct_answers INTEGER NOT NULL DEFAULT 0,
                total_questions INTEGER NOT NULL DEFAULT 0,

                passed INTEGER NOT NULL DEFAULT 0,

                created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,

                FOREIGN KEY (user_id)
                    REFERENCES users(id)
                    ON DELETE CASCADE,

                FOREIGN KEY (exam_id)
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

                best_exam_score INTEGER NOT NULL DEFAULT 0,
                exam_attempts INTEGER NOT NULL DEFAULT 0,

                completed_at TEXT,

                UNIQUE(
                    user_id,
                    level_id
                ),

                FOREIGN KEY (user_id)
                    REFERENCES users(id)
                    ON DELETE CASCADE,

                FOREIGN KEY (level_id)
                    REFERENCES course_levels(id)
                    ON DELETE CASCADE
            )
            """
        )

        connection.commit()

    finally:
        connection.close()
