import hashlib
import os
import platform
import subprocess

try:
    import winreg
except ImportError:
    winreg = None


DEVICE_PREFIX = "ARCHIPRO"
PRODUCT_SALT = "ARCHIPRO_UZ_HARDWARE_V3"


INVALID_HARDWARE_VALUES = {
    "",
    "none",
    "null",
    "unknown",
    "default string",
    "system serial number",
    "to be filled by o.e.m.",
    "to be filled by oem",
    "not specified",
    "not applicable",
    "n/a",
    "na",
    "00000000-0000-0000-0000-000000000000",
    "ffffffff-ffff-ffff-ffff-ffffffffffff",
}


def _normalize(value: str) -> str:
    if value is None:
        return ""

    value = str(value).strip()

    value = " ".join(
        value.split()
    )

    return value


def _is_valid_hardware_value(
    value: str,
) -> bool:
    value = _normalize(value)

    if not value:
        return False

    lowered = value.lower()

    if lowered in INVALID_HARDWARE_VALUES:
        return False

    if lowered.startswith(
        "to be filled"
    ):
        return False

    if len(value) < 4:
        return False

    return True


def _run_powershell(
    command: str,
) -> str:
    """
    PowerShell orqali Windows CIM/WMI ma'lumotini oladi.
    Konsol oynasi ko'rinmaydi.
    """

    try:
        creation_flags = 0

        if os.name == "nt":
            creation_flags = getattr(
                subprocess,
                "CREATE_NO_WINDOW",
                0,
            )

        result = subprocess.run(
            [
                "powershell.exe",
                "-NoProfile",
                "-NonInteractive",
                "-ExecutionPolicy",
                "Bypass",
                "-Command",
                command,
            ],
            capture_output=True,
            text=True,
            timeout=8,
            creationflags=creation_flags,
        )

        if result.returncode != 0:
            return ""

        output = _normalize(
            result.stdout
        )

        return output

    except Exception:
        return ""


def _get_system_uuid() -> str:
    """
    Kompyuter / motherboard bilan bog'liq SMBIOS UUID.

    Windows qayta o'rnatilganda odatda o'zgarmaydi.
    """

    value = _run_powershell(
        "(Get-CimInstance "
        "Win32_ComputerSystemProduct).UUID"
    )

    if _is_valid_hardware_value(
        value
    ):
        return value

    return ""


def _get_baseboard_serial() -> str:
    """
    Motherboard serial raqami.
    """

    value = _run_powershell(
        "(Get-CimInstance "
        "Win32_BaseBoard).SerialNumber"
    )

    if _is_valid_hardware_value(
        value
    ):
        return value

    return ""


def _get_bios_serial() -> str:
    """
    BIOS / ishlab chiqaruvchi bergan serial.
    """

    value = _run_powershell(
        "(Get-CimInstance "
        "Win32_BIOS).SerialNumber"
    )

    if _is_valid_hardware_value(
        value
    ):
        return value

    return ""


def _get_machine_guid() -> str:
    """
    Oxirgi fallback.

    Bu Windows qayta o'rnatilganda o'zgarishi mumkin,
    shuning uchun faqat hardware ID topilmasa ishlatiladi.
    """

    if winreg is None:
        return ""

    registry_path = (
        r"SOFTWARE\Microsoft\Cryptography"
    )

    access_modes = [
        winreg.KEY_READ
        | getattr(
            winreg,
            "KEY_WOW64_64KEY",
            0,
        ),

        winreg.KEY_READ
        | getattr(
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

                value, _ = (
                    winreg.QueryValueEx(
                        key,
                        "MachineGuid",
                    )
                )

                value = _normalize(
                    value
                )

                if value:
                    return value

        except Exception:
            continue

    return ""


def _get_hardware_source() -> str:
    """
    Muhim:

    Device ID uchun birinchi navbatda Windows'dan
    mustaqil hardware identifikator olinadi.

    PRIORITET:
    1. System UUID
    2. Motherboard serial
    3. BIOS serial
    4. Windows MachineGuid
    5. Juda oxirgi fallback
    """

    system_uuid = (
        _get_system_uuid()
    )

    if system_uuid:
        return (
            "SYSTEM_UUID|"
            + system_uuid.upper()
        )

    board_serial = (
        _get_baseboard_serial()
    )

    if board_serial:
        return (
            "BASEBOARD|"
            + board_serial.upper()
        )

    bios_serial = (
        _get_bios_serial()
    )

    if bios_serial:
        return (
            "BIOS|"
            + bios_serial.upper()
        )

    machine_guid = (
        _get_machine_guid()
    )

    if machine_guid:
        return (
            "MACHINE_GUID|"
            + machine_guid.upper()
        )

    # Juda kam uchraydigan fallback.
    return (
        "FALLBACK|"
        + platform.system()
        + "|"
        + platform.machine()
        + "|"
        + platform.processor()
    )


def get_device_id() -> str:
    """
    ARCHIPRO UZ Device ID.

    Format:
    ARCHIPRO-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX

    Agar System UUID yoki motherboard serial mavjud bo'lsa,
    Windows qayta o'rnatilganda Device ID o'zgarmaydi.
    """

    hardware_source = (
        _get_hardware_source()
    )

    source = (
        PRODUCT_SALT
        + "|"
        + hardware_source
    )

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
