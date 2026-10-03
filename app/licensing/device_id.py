import hashlib
import os
import platform
import uuid


# ============================================================
# WINDOWS MACHINE GUID
# ============================================================

def _get_windows_machine_guid() -> str:
    if os.name != "nt":
        return ""

    try:
        import winreg

        key = winreg.OpenKey(
            winreg.HKEY_LOCAL_MACHINE,
            r"SOFTWARE\Microsoft\Cryptography",
        )

        value, _ = winreg.QueryValueEx(
            key,
            "MachineGuid",
        )

        winreg.CloseKey(
            key
        )

        return str(
            value
        ).strip()

    except Exception:
        return ""


# ============================================================
# RAW DEVICE FINGERPRINT
# ============================================================

def _get_raw_fingerprint() -> str:
    parts = []

    machine_guid = (
        _get_windows_machine_guid()
    )

    if machine_guid:
        parts.append(
            machine_guid
        )

    parts.append(
        platform.system()
    )

    parts.append(
        platform.machine()
    )

    parts.append(
        platform.node()
    )

    parts.append(
        str(
            uuid.getnode()
        )
    )

    computer_name = os.getenv(
        "COMPUTERNAME",
        "",
    )

    if computer_name:
        parts.append(
            computer_name
        )

    return "|".join(
        str(part).strip().lower()
        for part in parts
        if str(part).strip()
    )


# ============================================================
# DEVICE ID
# ============================================================

def get_device_id() -> str:
    raw = (
        _get_raw_fingerprint()
    )

    digest = hashlib.sha256(
        raw.encode(
            "utf-8"
        )
    ).hexdigest().upper()

    chunks = [
        digest[index:index + 4]
        for index in range(
            0,
            24,
            4,
        )
    ]

    return (
        "ARCHIPRO-"
        + "-".join(chunks)
    )


if __name__ == "__main__":
    print(
        get_device_id()
    )
