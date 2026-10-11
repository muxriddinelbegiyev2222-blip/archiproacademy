import base64
import json
import os
import shutil
from datetime import datetime
from pathlib import Path

from cryptography.exceptions import (
    InvalidSignature,
)
from cryptography.hazmat.primitives.asymmetric.ed25519 import (
    Ed25519PublicKey,
)

from database.database import (
    get_connection,
)

from licensing.device_id import (
    get_device_id,
)


# ============================================================
# PRODUCT
# ============================================================

PRODUCT_NAME = "ARCHIPRO_UZ"
LICENSE_VERSION = 1


# ============================================================
# PUBLIC KEY
# ============================================================

# Current OWNER/ADMIN signing key: fingerprint F7AFC1C00E6D7DDE
# This is PUBLIC information (never add archipro_private.key here).
PUBLIC_KEY_B64 = (
    "uDSW12Lv5UvEtOFfypdKsy4JUdV1woihiqhegs70RoE="
)

# Legacy verification key: fingerprint 2BCB7109E86D65DD
# Keep it to verify already-issued, valid licenses from earlier releases.
# Retiring a legacy key requires an explicit customer migration process.
LEGACY_PUBLIC_KEY_B64 = (
    "TrPS3sdOCiD9wFd1CA4IyZQvCzBGyROPOt8S/2cjTWU="
)


# ============================================================
# LICENSE LOCATION
# ============================================================

def get_license_directory() -> Path:
    local_app_data = os.getenv(
        "LOCALAPPDATA"
    )

    if local_app_data:
        base_directory = Path(
            local_app_data
        )
    else:
        base_directory = Path.home()

    directory = (
        base_directory
        / "ARCHIPRO_UZ"
        / "license"
    )

    directory.mkdir(
        parents=True,
        exist_ok=True,
    )

    return directory


def get_installed_license_path() -> Path:
    return (
        get_license_directory()
        / "license.archiprolic"
    )


# ============================================================
# CANONICAL PAYLOAD
# ============================================================

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


# ============================================================
# LOAD PUBLIC KEY
# ============================================================

def _load_public_key():
    raw = base64.b64decode(
        PUBLIC_KEY_B64
    )

    return (
        Ed25519PublicKey
        .from_public_bytes(
            raw
        )
    )


def _load_legacy_public_key():
    """Previously trusted public key for already issued valid licenses."""
    return Ed25519PublicKey.from_public_bytes(
        base64.b64decode(LEGACY_PUBLIC_KEY_B64)
    )


def _verify_trusted_signature(signature: bytes, payload: dict) -> None:
    """Accept valid current or legacy signatures; never skip verification."""
    signed_bytes = _canonical_payload(payload)
    for public_key in (_load_public_key(), _load_legacy_public_key()):
        try:
            public_key.verify(signature, signed_bytes)
            return
        except InvalidSignature:
            continue
    raise InvalidSignature("No trusted ARCHIPRO public key verified this license.")


# ============================================================
# READ LICENSE FILE
# ============================================================

def read_license_file(
    license_path,
) -> dict:
    path = Path(
        license_path
    )

    text = path.read_text(
        encoding="utf-8"
    )

    data = json.loads(
        text
    )

    if not isinstance(
        data,
        dict,
    ):
        raise ValueError(
            "License fayli noto'g'ri."
        )

    return data


# ============================================================
# VERIFY LICENSE DATA
# ============================================================

def verify_license_data(
    data: dict,
) -> dict:
    if not isinstance(data, dict):
        return {
            "valid": False,
            "message": "Litsenziya faylining tuzilishi noto'g'ri.",
        }

    if (
        data.get("product")
        != PRODUCT_NAME
    ):
        return {
            "valid": False,
            "message": (
                "Bu litsenziya ARCHIPRO UZ uchun emas."
            ),
        }

    if (
        data.get("version")
        != LICENSE_VERSION
    ):
        return {
            "valid": False,
            "message": (
                "Litsenziya versiyasi mos emas."
            ),
        }

    payload = data.get(
        "payload"
    )

    signature_b64 = data.get(
        "signature"
    )

    if not isinstance(
        payload,
        dict,
    ):
        return {
            "valid": False,
            "message": (
                "Litsenziya tarkibi noto'g'ri."
            ),
        }

    if not signature_b64:
        return {
            "valid": False,
            "message": (
                "Litsenziya imzosi topilmadi."
            ),
        }

    try:
        if not isinstance(signature_b64, str):
            raise ValueError("Signature must be a Base64 string.")

        signature = base64.b64decode(signature_b64, validate=True)
        if len(signature) != 64:
            raise ValueError("Invalid Ed25519 signature length.")

        _verify_trusted_signature(signature, payload)

    except (
        InvalidSignature,
        ValueError,
        TypeError,
    ):
        return {
            "valid": False,
            "message": (
                "Litsenziya raqamli imzosi noto'g'ri."
            ),
        }

    except Exception:
        return {
            "valid": False,
            "message": (
                "Litsenziyani tekshirishda xato yuz berdi."
            ),
        }

    # ========================================================
    # DEVICE CHECK
    # ========================================================

    license_device_id = str(
        payload.get(
            "device_id",
            "",
        )
    ).strip().upper()

    current_device_id = (
        get_device_id()
        .strip()
        .upper()
    )

    if (
        not license_device_id
        or license_device_id
        != current_device_id
    ):
        return {
            "valid": False,
            "message": (
                "Bu litsenziya boshqa kompyuter uchun chiqarilgan."
            ),
            "device_id": (
                current_device_id
            ),
        }

    # ========================================================
    # REQUIRED DATA
    # ========================================================

    username = str(
        payload.get(
            "username",
            "",
        )
    ).strip().lower()

    password_hash = str(
        payload.get(
            "password_hash",
            "",
        )
    ).strip()

    password_salt = str(
        payload.get(
            "password_salt",
            "",
        )
    ).strip()

    if not username:
        return {
            "valid": False,
            "message": (
                "Litsenziyada login topilmadi."
            ),
        }

    if (
        not password_hash
        or not password_salt
    ):
        return {
            "valid": False,
            "message": (
                "Litsenziyada autentifikatsiya "
                "ma'lumotlari yetarli emas."
            ),
        }

    # ========================================================
    # EXPIRATION CHECK
    # ========================================================

    expires_at = payload.get(
        "expires_at"
    )

    if expires_at:

        try:
            expiry = (
                datetime.fromisoformat(
                    str(
                        expires_at
                    )
                )
            )

        except ValueError:
            return {
                "valid": False,
                "message": (
                    "Litsenziya muddati noto'g'ri yozilgan."
                ),
            }

        now = datetime.now(expiry.tzinfo) if expiry.tzinfo else datetime.now()
        if now > expiry:
            return {
                "valid": False,
                "message": (
                    "Litsenziya muddati tugagan."
                ),
                "expired": True,
            }

    return {
        "valid": True,
        "message": (
            "Litsenziya haqiqiy."
        ),
        "payload": payload,
    }


# ============================================================
# VERIFY LICENSE FILE
# ============================================================

def verify_license_file(
    license_path,
) -> dict:
    try:
        data = read_license_file(
            license_path
        )

    except FileNotFoundError:
        return {
            "valid": False,
            "message": (
                "Litsenziya fayli topilmadi."
            ),
        }

    except json.JSONDecodeError:
        return {
            "valid": False,
            "message": (
                "Litsenziya fayli buzilgan yoki noto'g'ri."
            ),
        }

    except Exception as exc:
        return {
            "valid": False,
            "message": str(
                exc
            ),
        }

    return verify_license_data(
        data
    )


# ============================================================
# PROVISION USER FROM SIGNED LICENSE
# ============================================================

def provision_user_from_license(
    payload: dict,
):
    username = str(
        payload.get(
            "username",
            "",
        )
    ).strip().lower()

    full_name = str(
        payload.get(
            "full_name",
            "",
        )
    ).strip()

    license_type = str(
        payload.get(
            "license_type",
            "PRO",
        )
    ).strip().upper()

    password_hash = str(
        payload.get(
            "password_hash",
            "",
        )
    ).strip()

    password_salt = str(
        payload.get(
            "password_salt",
            "",
        )
    ).strip()

    if license_type not in (
        "PRO",
        "MASTER",
    ):
        license_type = "PRO"

    connection = (
        get_connection()
    )

    try:
        cursor = (
            connection.cursor()
        )

        cursor.execute(
            """
            SELECT id
            FROM users
            WHERE username = ?
            LIMIT 1
            """,
            (
                username,
            ),
        )

        existing = (
            cursor.fetchone()
        )

        if existing is None:

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
                    password_salt,
                    full_name,
                    license_type,
                ),
            )

        else:

            cursor.execute(
                """
                UPDATE users

                SET
                    password_hash = ?,
                    password_salt = ?,
                    full_name = ?,
                    license_type = ?,
                    is_active = 1

                WHERE username = ?
                """,
                (
                    password_hash,
                    password_salt,
                    full_name,
                    license_type,
                    username,
                ),
            )

        connection.commit()

        return True

    except Exception:
        connection.rollback()
        raise

    finally:
        connection.close()


# ============================================================
# INSTALL LICENSE
# ============================================================

def install_license(
    source_path,
) -> dict:
    result = verify_license_file(
        source_path
    )

    if not result.get(
        "valid"
    ):
        return result

    payload = result[
        "payload"
    ]

    destination = (
        get_installed_license_path()
    )

    try:
        source = Path(
            source_path
        )

        if (
            source.resolve()
            != destination.resolve()
        ):
            shutil.copy2(
                source,
                destination,
            )

        provision_user_from_license(
            payload
        )

    except Exception as exc:
        return {
            "valid": False,
            "message": (
                "Litsenziyani o'rnatib bo'lmadi.\n\n"
                + str(exc)
            ),
        }

    return {
        "valid": True,
        "message": (
            "Litsenziya muvaffaqiyatli faollashtirildi."
        ),
        "payload": payload,
        "license_path": str(
            destination
        ),
    }


# ============================================================
# CHECK INSTALLED LICENSE
# ============================================================

def validate_installed_license() -> dict:
    path = (
        get_installed_license_path()
    )

    if not path.exists():
        return {
            "valid": False,
            "message": (
                "ARCHIPRO UZ hali faollashtirilmagan."
            ),
            "device_id": (
                get_device_id()
            ),
        }

    result = (
        verify_license_file(
            path
        )
    )

    if result.get(
        "valid"
    ):
        try:
            provision_user_from_license(
                result[
                    "payload"
                ]
            )

        except Exception as exc:
            return {
                "valid": False,
                "message": (
                    "Litsenziya haqiqiy, lekin "
                    "foydalanuvchini tayyorlashda xato:\n\n"
                    + str(exc)
                ),
            }

    return result
