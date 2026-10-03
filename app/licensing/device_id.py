import hashlib
import platform
import uuid

try:
    import winreg
except ImportError:
    winreg = None


DEVICE_PREFIX = "ARCHIPRO"
PRODUCT_SALT = "ARCHIPRO_UZ_DEVICE_V2"


def _read_windows_machine_guid() -> str:
    """
    Windows MachineGuid ni registry'dan oladi.

    Bu qiymat:
    - kompyuter nomiga bog'liq emas
    - Wi-Fi / Ethernet adapteriga bog'liq emas
    - MAC address o'zgarsa o'zgarmaydi

    Windows qayta o'rnatilib MachineGuid yangilansa,
    Device ID ham yangilanadi.
    """

    if winreg is None:
        return ""

    registry_path = r"SOFTWARE\Microsoft\Cryptography"

    access_modes = [
        winreg.KEY_READ | getattr(
            winreg,
            "KEY_WOW64_64KEY",
            0,
        ),
        winreg.KEY_READ | getattr(
            winreg,
            "KEY_WOW64_32KEY",
            0,
        ),
        winreg.KEY_READ,
    ]

    for access in access_modes:
        try:
            with winreg.OpenKey(
                winreg.HKEY_LOCAL_MACHINE,
                registry_path,
                0,
                access,
            ) as key:
                value, _ = winreg.QueryValueEx(
                    key,
                    "MachineGuid",
                )

                machine_guid = str(
                    value
                ).strip()

                if machine_guid:
                    return machine_guid

        except (
            FileNotFoundError,
            OSError,
            PermissionError,
        ):
            continue

    return ""


def _fallback_device_source() -> str:
    """
    MachineGuid olinmasa fallback identifikator.

    Asosiy Windows mijozlarda odatda bu ishlatilmaydi.
    """

    parts = [
        PRODUCT_SALT,
        platform.system(),
        platform.machine(),
        platform.processor(),
        str(uuid.getnode()),
    ]

    cleaned = [
        str(part).strip().lower()
        for part in parts
        if str(part).strip()
    ]

    return "|".join(
        cleaned
    )


def _get_device_source() -> str:
    machine_guid = (
        _read_windows_machine_guid()
    )

    if machine_guid:
        return (
            f"{PRODUCT_SALT}"
            f"|WINDOWS"
            f"|{machine_guid.strip().lower()}"
        )

    return _fallback_device_source()


def get_device_id() -> str:
    """
    ARCHIPRO UZ uchun barqaror Device ID yaratadi.

    Ko'rinishi:
    ARCHIPRO-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX
    """

    source = _get_device_source()

    digest = hashlib.sha256(
        source.encode(
            "utf-8"
        )
    ).hexdigest().upper()

    short_hash = digest[:24]

    groups = [
        short_hash[i:i + 4]
        for i in range(
            0,
            24,
            4,
        )
    ]

    return (
        DEVICE_PREFIX
        + "-"
        + "-".join(groups)
    )


if __name__ == "__main__":
    print(
        get_device_id()
    )
