import os
import sqlite3
from pathlib import Path


APP_NAME = "ARCHIPRO_UZ"


def get_app_data_dir() -> Path:
    """
    ARCHIPRO UZ ma'lumotlari saqlanadigan lokal papkani qaytaradi.
    Windows'da LOCALAPPDATA ichida saqlanadi.
    """

    local_app_data = os.getenv("LOCALAPPDATA")

    if local_app_data:
        base_dir = Path(local_app_data)
    else:
        base_dir = Path.home()

    app_dir = base_dir / APP_NAME
    app_dir.mkdir(parents=True, exist_ok=True)

    return app_dir


def get_database_path() -> Path:
    data_dir = get_app_data_dir() / "data"
    data_dir.mkdir(parents=True, exist_ok=True)

    return data_dir / "archipro.db"


def get_connection() -> sqlite3.Connection:
    connection = sqlite3.connect(get_database_path())
    connection.row_factory = sqlite3.Row

    return connection


def initialize_database():
    """
    Dastur birinchi marta ishga tushganda kerakli jadvallarni yaratadi.
    """

    connection = get_connection()

    try:
        cursor = connection.cursor()

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

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS app_settings (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                setting_key TEXT NOT NULL UNIQUE,
                setting_value TEXT
            )
            """
        )

        connection.commit()

    finally:
        connection.close()
