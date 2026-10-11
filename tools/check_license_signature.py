"""Read-only offline diagnosis for the ARCHIPRO UZ Ed25519 license error.

Never send or print the signing private key, password hashes, usernames or Device ID.
No credentials or signed licenses are modified by this tool.
"""
from __future__ import annotations

import ast
import base64
import binascii
import hashlib
import json
import os
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
CODE = ROOT / "app" / "licensing" / "license_service.py"
ADMIN_DIR = Path(os.environ.get("LOCALAPPDATA") or Path.home()) / "ARCHIPRO_UZ_ADMIN" / "keys"
PRIVATE_FILE = ADMIN_DIR / "archipro_private.key"
PUBLIC_FILE = ADMIN_DIR / "archipro_public.key"


def fingerprint(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()[:16]


def decode(value: str, size: int) -> bytes:
    raw = base64.b64decode(value.strip(), validate=True)
    if len(raw) != size:
        raise ValueError("kalit yoki imzo uzunligi xato")
    return raw


def program_public() -> bytes:
    # Do not import license_service: its database/device initialization is not needed.
    tree = ast.parse(CODE.read_text(encoding="utf-8"))
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(
            isinstance(t, ast.Name) and t.id == "PUBLIC_KEY_B64" for t in node.targets
        ):
            return decode(ast.literal_eval(node.value), 32)
    raise ValueError("PUBLIC_KEY_B64 kodda topilmadi")


def load_signer_public() -> bytes:
    from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
    from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat

    # Load only in memory. Never print or upload the private key.
    private = decode(PRIVATE_FILE.read_text(encoding="utf-8"), 32)
    signer = Ed25519PrivateKey.from_private_bytes(private)
    return signer.public_key().public_bytes(Encoding.Raw, PublicFormat.Raw)


def check_signature(public_bytes: bytes, signature: bytes, payload: bytes) -> bool:
    from cryptography.exceptions import InvalidSignature
    from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PublicKey

    try:
        Ed25519PublicKey.from_public_bytes(public_bytes).verify(signature, payload)
        return True
    except (InvalidSignature, ValueError):
        return False


def choose_file() -> Path | None:
    if len(sys.argv) > 1:
        f = Path(sys.argv[1].strip('"'))
        return f if f.is_file() else None

    try:
        import tkinter
        from tkinter import filedialog
        root = tkinter.Tk()
        root.withdraw()
        selected = filedialog.askopenfilename(
            title="Imzo xatosi bergan .archiprolic litsenziyani tanlang",
            filetypes=[("ARCHIPRO litsenziya", "*.archiprolic"), ("Barcha fayllar", "*.*")]
        )
        root.destroy()
        return Path(selected) if selected else None
    except Exception:
        return None


def main() -> int:
    print("=" * 64)
    print("ARCHIPRO UZ — RAQAMLI IMZO MOSLIGINI TEKSHIRISH")
    print("MAXFIY KALIT, PAROL VA DEVICE ID KO'RSATILMAYDI")
    print("=" * 64)
    try:
        program = program_public()
    except (OSError, ValueError, SyntaxError, binascii.Error) as exc:
        print("[XATO] Dasturdagi PUBLIC KEYni o'qish:", type(exc).__name__, str(exc))
        return 2

    print("Asosiy dastur uchun PUBLIC KEY fingerprint:", fingerprint(program))
    signer = None
    if not PRIVATE_FILE.is_file():
        print("[XATO] ADMIN/OWNER uchun private key topilmadi.")
        print("Eski kalit nusxasini toping; YANGI KALIT YARATMANG.")
    else:
        try:
            signer = load_signer_public()
            print("ADMIN/OWNER private key jufti fingerprint:  ", fingerprint(signer))
            print("PRIVATE KEY VA ASOSIY DASTUR:", "MOS [OK]" if signer == program else "MOS EMAS [XATO]")
            if signer != program:
                print("Tuzatish uchun FAQAT PUBLIC KEY (ulashish mumkin):")
                print(base64.b64encode(signer).decode("ascii"))
                print("Ushbu OCHIQ kalit private key emas.")
        except (ImportError, OSError, ValueError, binascii.Error) as exc:
            print("[XATO] Private keyni xavfsiz tekshirib bo'lmadi:", type(exc).__name__)

    if PUBLIC_FILE.is_file():
        try:
            stored = decode(PUBLIC_FILE.read_text(encoding="utf-8"), 32)
            print("Saqlangan PUBLIC KEY fingerprint:         ", fingerprint(stored))
            if signer is not None:
                print("SAQLANGAN PUBLIC KEY / PRIVATE KEY:",
                      "MOS [OK]" if signer == stored else "MOS EMAS [XATO]")
        except (OSError, ValueError, binascii.Error):
            print("[XATO] Saqlangan public key formati noto'g'ri.")
    else:
        print("[INFO] Saqlangan public key fayli yo'q (bu imzo uchun shart emas).")

    lic = choose_file()
    if lic is None:
        print("[INFO] Litsenziya tanlanmadi, faqat kalit jufti solishtirildi.")
    else:
        try:
            data = json.loads(lic.read_text(encoding="utf-8"))
            payload = data["payload"]
            if not isinstance(payload, dict):
                raise ValueError("payload dict emas")
            signature = decode(data["signature"], 64)
            signed = json.dumps(
                payload, ensure_ascii=False, sort_keys=True, separators=(",", ":")
            ).encode("utf-8")
            print("Litsenziya formati:", "MOS" if (data.get("product") == "ARCHIPRO_UZ" and data.get("version") == 1) else "MOS EMAS")
            print("Litsenziya imzosi / ASOSIY DASTUR:", "TO'G'RI" if check_signature(program, signature, signed) else "NOTO'G'RI")
            if signer is not None:
                print("Litsenziya imzosi / ADMIN PRIVATE KEY:",
                      "TO'G'RI" if check_signature(signer, signature, signed) else "NOTO'G'RI")
        except (OSError, UnicodeError, ValueError, TypeError, KeyError, json.JSONDecodeError, binascii.Error) as exc:
            print("[XATO] Tanlangan litsenziya fayli formati noto'g'ri:", type(exc).__name__)

    print("-" * 64)
    print("Agar kalitlar mos bo'lmasa: public keyni yangilashdan")
    print("oldin OLDINGI MIJOZLAR LITSENZIYALARINI saqlash kerak.")
    print("Agar mos bo'lsa, lekin EXE rad etsa: eski EXE ishlatilayotgan")
    print("yoki litsenziya boshqa kalit bilan imzolangan bo'lishi mumkin.")
    print("USHBU DASTUR HECH QANDAY KALITNI O'ZGARTIRMADI.")
    print("Faqat yuqoridagi tekshiruv natijalarini yuboring.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
