import hashlib
import hmac
import os


ITERATIONS = 310_000


def generate_salt() -> str:
    return os.urandom(32).hex()


def hash_password(password: str, salt_hex: str) -> str:
    salt = bytes.fromhex(salt_hex)

    password_hash = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode("utf-8"),
        salt,
        ITERATIONS,
    )

    return password_hash.hex()


def verify_password(
    password: str,
    salt_hex: str,
    expected_hash: str,
) -> bool:
    calculated_hash = hash_password(password, salt_hex)

    return hmac.compare_digest(
        calculated_hash,
        expected_hash,
    )
