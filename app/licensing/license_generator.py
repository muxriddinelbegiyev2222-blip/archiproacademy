import base64
import json
import os
import uuid
from datetime import datetime, timedelta
from pathlib import Path

from cryptography.hazmat.primitives.asymmetric.ed25519 import (
    Ed25519PrivateKey,
)

from auth.passwords import (
    generate_salt,
    hash_password,
)


PRODUCT_NAME = "ARCHIPRO_UZ"
LICENSE_VERSION = 1


def get_admin_key_directory() -> Path:
    local_app_data = os.getenv(
        "LOCALAPPDATA"
    )

    if local_app_data:
        base_directory = Path(
            local_app_data
        )
    else:
        base_directory = Path.home()

    return (
        base_directory
        / "ARCHIPRO_UZ_ADMIN"
        / "keys"
    )


def get_private_key_path() -> Path:
    return (
        get_admin_key_directory()
        / "archipro_private.key"
    )


def private_key_exists() -> bool:
    return (
        get_private_key_path()
        .exists()
    )


def _load_private_key():
    private_path = (
        get_private_key_path()
    )

    if not private_path.exists():
        raise FileNotFoundError(
            "ARCHIPRO private key topilmadi."
        )

    private_b64 = (
        private_path.read_text(
            encoding="utf-8"
        )
        .strip()
    )

    raw = base64.b64decode(
        private_b64
    )

    if len(raw) != 32:
        raise ValueError(
            "Private key formati noto'g'ri."
        )

    return (
        Ed25519PrivateKey
        .from_private_bytes(
            raw
        )
    )


def _canonical_payload(
    payload: dict,
) -> bytes:
    text = json.dumps(
        payload,
        ensure_ascii=False,
        sort_keys=True,
        separators=(
            ",",
            ":",
        ),
    )

    return text.encode(
        "utf-8"
    )


def calculate_expiry(
    duration_code: str,
):
    now = datetime.now()

    duration_code = str(
        duration_code
    ).strip().upper()

    if duration_code == "30":
        expiry = now + timedelta(
            days=30
        )

    elif duration_code == "90":
        expiry = now + timedelta(
            days=90
        )

    elif duration_code == "180":
        expiry = now + timedelta(
            days=180
        )

    elif duration_code == "365":
        expiry = now + timedelta(
            days=365
        )

    else:
        return None

    return expiry.isoformat(
        timespec="seconds"
    )


def generate_license(
    device_id: str,
    username: str,
    password: str,
    full_name: str = "",
    license_type: str = "PRO",
    duration_code: str = "PERMANENT",
) -> dict:

    device_id = (
        device_id
        .strip()
        .upper()
    )

    username = (
        username
        .strip()
        .lower()
    )

    full_name = (
        full_name
        .strip()
    )

    license_type = (
        license_type
        .strip()
        .upper()
    )

    if not device_id:
        raise ValueError(
            "Device ID kiritilmagan."
        )

    if not device_id.startswith(
        "ARCHIPRO-"
    ):
        raise ValueError(
            "Device ID formati noto'g'ri."
        )

    if not username:
        raise ValueError(
            "Login kiritilmagan."
        )

    if len(username) < 3:
        raise ValueError(
            "Login kamida 3 ta belgidan iborat bo'lsin."
        )

    if len(password) < 8:
        raise ValueError(
            "Parol kamida 8 ta belgidan iborat bo'lsin."
        )

    if license_type not in (
        "PRO",
        "MASTER",
    ):
        raise ValueError(
            "Litsenziya turi noto'g'ri."
        )

    private_key = (
        _load_private_key()
    )

    salt = generate_salt()

    password_hash = (
        hash_password(
            password,
            salt,
        )
    )

    issued_at = (
        datetime.now()
        .isoformat(
            timespec="seconds"
        )
    )

    expires_at = (
        calculate_expiry(
            duration_code
        )
    )

    payload = {
        "license_id": str(
            uuid.uuid4()
        ),
        "device_id": device_id,
        "username": username,
        "full_name": full_name,
        "license_type": license_type,
        "password_hash": password_hash,
        "password_salt": salt,
        "issued_at": issued_at,
        "expires_at": expires_at,
    }

    signature = private_key.sign(
        _canonical_payload(
            payload
        )
    )

    signature_b64 = (
        base64.b64encode(
            signature
        )
        .decode(
            "ascii"
        )
    )

    return {
        "product": PRODUCT_NAME,
        "version": LICENSE_VERSION,
        "payload": payload,
        "signature": signature_b64,
    }


def save_license(
    license_data: dict,
    file_path,
):
    path = Path(
        file_path
    )

    if (
        path.suffix.lower()
        != ".archiprolic"
    ):
        path = path.with_suffix(
            ".archiprolic"
        )

    text = json.dumps(
        license_data,
        ensure_ascii=False,
        indent=2,
    )

    path.write_text(
        text,
        encoding="utf-8",
    )

    return path
