"""ARCHIPRO UZ UI curriculum map.

Bu fayl course content yoki unlock qoidalarini o'zgartirmaydi.
Faqat mavjud LEVEL_00 ... LEVEL_15 ni UI bo'limlariga guruhlaydi.
"""


CURRICULUM_SECTIONS = {
    "Arxitektura": {
        "title": "Arxitektura",
        "subtitle": (
            "Arxitekturani mutlaqo noldan turar joy "
            "rejalashtirishigacha o'rganish."
        ),
        "levels": [
            "LEVEL_00",
            "LEVEL_01",
            "LEVEL_02",
            "LEVEL_03",
            "LEVEL_04",
        ],
    },

    "Archicad": {
        "title": "Archicad",
        "subtitle": (
            "Archicad'ni boshlang'ichdan professional "
            "BIM workflow darajasigacha o'rganish."
        ),
        "levels": [
            "LEVEL_05",
            "LEVEL_06",
            "LEVEL_07",
        ],
    },

    "Qurilish konstruksiyalari": {
        "title": "Qurilish konstruksiyalari",
        "subtitle": (
            "Arxitektor bilishi kerak bo'lgan "
            "asosiy konstruktiv bilimlar."
        ),
        "levels": [
            "LEVEL_08",
        ],
    },

    "SHNQ va normativlar": {
        "title": "SHNQ va normativlar",
        "subtitle": (
            "O'zbekiston sharoitida normativ savodxonlik "
            "va loyiha tekshiruvi."
        ),
        "levels": [
            "LEVEL_09",
        ],
    },

    "Amaliyot": {
        "title": "Amaliyot",
        "subtitle": (
            "Bir va ikki qavatli turar joylarni "
            "professional darajada loyihalash."
        ),
        "levels": [
            "LEVEL_10",
            "LEVEL_11",
        ],
    },

    "BIM va real loyiha": {
        "title": "BIM va real loyiha",
        "subtitle": (
            "Ishchi hujjatlar, real mijoz workflow'i "
            "va murakkab residential design."
        ),
        "levels": [
            "LEVEL_12",
            "LEVEL_13",
            "LEVEL_14",
        ],
    },

    "Portfolio / PRO Final": {
        "title": "Portfolio / PRO Final",
        "subtitle": (
            "Yakuniy loyiha, loyiha himoyasi, "
            "professional portfolio va PRO Final."
        ),
        "levels": [
            "LEVEL_15",
        ],
    },
}


EXPECTED_LEVEL_CODES = [
    f"LEVEL_{number:02d}"
    for number in range(16)
]


def get_section(
    name: str,
):
    return CURRICULUM_SECTIONS.get(
        name
    )


def validate_curriculum_map():
    mapped = []

    for section in CURRICULUM_SECTIONS.values():
        mapped.extend(
            section["levels"]
        )

    missing = [
        code
        for code in EXPECTED_LEVEL_CODES
        if code not in mapped
    ]

    duplicates = [
        code
        for code in EXPECTED_LEVEL_CODES
        if mapped.count(code) > 1
    ]

    unknown = [
        code
        for code in mapped
        if code not in EXPECTED_LEVEL_CODES
    ]

    return {
        "ok": (
            not missing
            and not duplicates
            and not unknown
        ),
        "missing": missing,
        "duplicates": duplicates,
        "unknown": unknown,
    }
