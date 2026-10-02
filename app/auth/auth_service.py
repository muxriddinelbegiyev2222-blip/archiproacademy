from datetime import datetime

from auth.passwords import (
    generate_salt,
    hash_password,
    verify_password,
)
from database.database import get_connection


def create_user(
    username: str,
    password: str,
    full_name: str = "",
    license_type: str = "PRO",
) -> bool:
    username = username.strip().lower()

    if not username or not password:
        return False

    salt = generate_salt()
    password_hash = hash_password(password, salt)

    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            INSERT INTO users (
                username,
                password_hash,
                password_salt,
                full_name,
                license_type,
                is_active
            )
            VALUES (?, ?, ?, ?, ?, 1)
            """,
            (
                username,
                password_hash,
                salt,
                full_name,
                license_type,
            ),
        )

        connection.commit()

        return True

    except Exception:
        return False

    finally:
        connection.close()


def authenticate_user(
    username: str,
    password: str,
):
    username = username.strip().lower()

    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT *
            FROM users
            WHERE username = ?
            LIMIT 1
            """,
            (username,),
        )

        user = cursor.fetchone()

        if user is None:
            return None

        if user["is_active"] != 1:
            return None

        password_ok = verify_password(
            password,
            user["password_salt"],
            user["password_hash"],
        )

        if not password_ok:
            return None

        cursor.execute(
            """
            UPDATE users
            SET last_login = ?
            WHERE id = ?
            """,
            (
                datetime.now().isoformat(timespec="seconds"),
                user["id"],
            ),
        )

        connection.commit()

        return dict(user)

    finally:
        connection.close()
