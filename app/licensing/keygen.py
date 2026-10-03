import base64
import os
from pathlib import Path

from cryptography.hazmat.primitives.asymmetric.ed25519 import (
    Ed25519PrivateKey,
)
from cryptography.hazmat.primitives.serialization import (
    Encoding,
    NoEncryption,
    PrivateFormat,
    PublicFormat,
)


# ============================================================
# ADMIN KEY DIRECTORY
# ============================================================

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

    key_directory = (
        base_directory
        / "ARCHIPRO_UZ_ADMIN"
        / "keys"
    )

    key_directory.mkdir(
        parents=True,
        exist_ok=True,
    )

    return key_directory


# ============================================================
# GENERATE KEYPAIR
# ============================================================

def generate_keypair():
    key_directory = (
        get_admin_key_directory()
    )

    private_path = (
        key_directory
        / "archipro_private.key"
    )

    public_path = (
        key_directory
        / "archipro_public.key"
    )

    if private_path.exists():
        print()
        print(
            "PRIVATE KEY ALLAQACHON MAVJUD."
        )
        print()
        print(
            f"Joylashuvi: {private_path}"
        )
        print()
        print(
            "Yangi key yaratilmadi."
        )
        print(
            "Eski private keyni yo'qotmang."
        )

        if public_path.exists():
            public_key_b64 = (
                public_path
                .read_text(
                    encoding="utf-8"
                )
                .strip()
            )

            print()
            print(
                "PUBLIC KEY:"
            )
            print()
            print(
                public_key_b64
            )

        return

    private_key = (
        Ed25519PrivateKey.generate()
    )

    public_key = (
        private_key.public_key()
    )

    private_bytes = (
        private_key.private_bytes(
            encoding=Encoding.Raw,
            format=PrivateFormat.Raw,
            encryption_algorithm=NoEncryption(),
        )
    )

    public_bytes = (
        public_key.public_bytes(
            encoding=Encoding.Raw,
            format=PublicFormat.Raw,
        )
    )

    private_b64 = (
        base64.b64encode(
            private_bytes
        )
        .decode("ascii")
    )

    public_b64 = (
        base64.b64encode(
            public_bytes
        )
        .decode("ascii")
    )

    private_path.write_text(
        private_b64,
        encoding="utf-8",
    )

    public_path.write_text(
        public_b64,
        encoding="utf-8",
    )

    print()
    print(
        "=============================================="
    )
    print(
        "ARCHIPRO UZ LICENSE KEY YARATILDI"
    )
    print(
        "=============================================="
    )

    print()
    print(
        "PRIVATE KEY:"
    )
    print(
        private_path
    )

    print()
    print(
        "PUBLIC KEY:"
    )
    print()
    print(
        public_b64
    )

    print()
    print(
        "MUHIM:"
    )
    print(
        "archipro_private.key faylini GitHub'ga "
        "yuklamang va mijozga bermang."
    )

    print()
    print(
        "Private key yo'qolsa, eski litsenziyalarni "
        "davom ettirish qiyinlashadi."
    )


if __name__ == "__main__":
    generate_keypair()
