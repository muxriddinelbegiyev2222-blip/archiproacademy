from database.database import get_connection


LEVELS = [
    (
        "LEVEL_00",
        "Absolute Zero",
        "Arxitekturaga mutlaqo noldan kirish",
        "Arxitektura, loyiha va chizmalar haqida boshlang'ich bilim.",
        0,
    ),
    (
        "LEVEL_01",
        "Architecture Fundamentals",
        "Arxitektura asoslari",
        "Plan, fasad, kesim, masshtab va asosiy tushunchalar.",
        1,
    ),
    (
        "LEVEL_02",
        "Spatial Thinking",
        "Fazoviy fikrlash",
        "Ergonomika, proporsiya va funksional aloqalar.",
        2,
    ),
    (
        "LEVEL_03",
        "Site Planning",
        "Uchastka va genplan",
        "Uchastkani tahlil qilish va bino joylashtirish.",
        3,
    ),
    (
        "LEVEL_04",
        "Uzbekistan Residential Design",
        "O'zbekiston sharoitidagi uylar",
        "Mahalliy turmush tarzi va hovlili uylarni loyihalash.",
        4,
    ),
    (
        "LEVEL_05",
        "Archicad Beginner",
        "Archicad boshlang'ich",
        "Archicad interfeysi va asosiy instrumentlar.",
        5,
    ),
    (
        "LEVEL_06",
        "Archicad Intermediate",
        "Archicad o'rta daraja",
        "Murakkab modellashtirish va loyiha strukturasi.",
        6,
    ),
    (
        "LEVEL_07",
        "Archicad Advanced",
        "Archicad yuqori daraja",
        "Professional BIM workflow va hujjatlashtirish.",
        7,
    ),
    (
        "LEVEL_08",
        "Construction Fundamentals",
        "Konstruksiya asoslari",
        "Fundament, devor, karkas, tom va konstruktiv tushunchalar.",
        8,
    ),
    (
        "LEVEL_09",
        "SHNQ & Regulations",
        "SHNQ va normativlar",
        "O'zbekiston sharoitida me'yoriy savodxonlik.",
        9,
    ),
    (
        "LEVEL_10",
        "One-Storey House Professional",
        "1 qavatli uy PRO",
        "Bir qavatli turar joyni boshidan oxirigacha loyihalash.",
        10,
    ),
    (
        "LEVEL_11",
        "Two-Storey House Professional",
        "2 qavatli uy PRO",
        "Ikki qavatli turar joyni professional loyihalash.",
        11,
    ),
    (
        "LEVEL_12",
        "BIM & Documentation",
        "BIM va ishchi hujjatlar",
        "BIM model, spetsifikatsiya, layout va loyiha albomi.",
        12,
    ),
    (
        "LEVEL_13",
        "Client & Real Project Workflow",
        "Mijoz va real loyiha",
        "Texnik topshiriqdan loyiha himoyasigacha.",
        13,
    ),
    (
        "LEVEL_14",
        "Advanced Residential Designer",
        "Advanced Residential Designer",
        "Murakkab turar joy topshiriqlari va professional case study.",
        14,
    ),
    (
        "LEVEL_15",
        "PRO Final",
        "Professional final",
        "Mustaqil final loyiha, portfolio va yakuniy imtihon.",
        15,
    ),
]


STARTER_MODULES = [
    (
        "L00_M01",
        "Arxitektura bilan tanishuv",
        "Arxitektura nima va arxitektor qanday fikrlaydi.",
        1,
        90,
    ),
    (
        "L00_M02",
        "Chizmalarni tushunish",
        "Plan, fasad, kesim va genplan tushunchalari.",
        2,
        120,
    ),
    (
        "L00_M03",
        "Masshtab va o'lchamlar",
        "Arxitektura chizmalarida o'lcham va masshtab.",
        3,
        120,
    ),
    (
        "L00_M04",
        "Bino elementlari",
        "Uy va binoning asosiy konstruktiv qismlari.",
        4,
        150,
    ),
    (
        "L00_M05",
        "Birinchi arxitektura tahlili",
        "Tayyor uylarni arxitektor ko'zi bilan tahlil qilish.",
        5,
        180,
    ),
]


STARTER_LESSONS = [
    (
        "L00_M01_001",
        "Arxitektura nima?",
        "theory",
        "Arxitekturaning mohiyati va vazifasi.",
        1,
        15,
    ),
    (
        "L00_M01_002",
        "Arxitektor kim?",
        "theory",
        "Arxitektorning real loyihadagi roli.",
        2,
        15,
    ),
    (
        "L00_M01_003",
        "Loyiha nima?",
        "theory",
        "Loyiha tushunchasi va loyiha tarkibi.",
        3,
        20,
    ),
    (
        "L00_M02_001",
        "Plan nima?",
        "theory",
        "Qavat rejasini o'qishning boshlang'ich qoidalari.",
        1,
        20,
    ),
    (
        "L00_M02_002",
        "Fasad nima?",
        "theory",
        "Binoning tashqi ko'rinish chizmalarini tushunish.",
        2,
        20,
    ),
    (
        "L00_M02_003",
        "Kesim nima?",
        "theory",
        "Binoning vertikal kesimini o'qish.",
        3,
        20,
    ),
    (
        "L00_M02_004",
        "Genplan nima?",
        "theory",
        "Uy va uchastka munosabatini tushunish.",
        4,
        20,
    ),
    (
        "L00_M03_001",
        "Masshtab tushunchasi",
        "theory",
        "1:50, 1:100 va boshqa masshtablarni tushunish.",
        1,
        25,
    ),
    (
        "L00_M03_002",
        "O'lchamlarni o'qish",
        "practice",
        "Arxitektura chizmalaridagi o'lchamlarni aniqlash.",
        2,
        25,
    ),
    (
        "L00_M03_003",
        "Otmetka va balandlik",
        "theory",
        "0.000 va boshqa balandlik belgilarini tushunish.",
        3,
        25,
    ),
]


def seed_course_structure():
    connection = get_connection()

    try:
        cursor = connection.cursor()

        # =========================
        # LEVELS
        # =========================

        for (
            code,
            title,
            subtitle,
            description,
            sort_order,
        ) in LEVELS:

            cursor.execute(
                """
                INSERT OR IGNORE INTO course_levels (
                    code,
                    title,
                    subtitle,
                    description,
                    sort_order
                )
                VALUES (?, ?, ?, ?, ?)
                """,
                (
                    code,
                    title,
                    subtitle,
                    description,
                    sort_order,
                ),
            )

        # Level 0 ID
        cursor.execute(
            """
            SELECT id
            FROM course_levels
            WHERE code = 'LEVEL_00'
            """
        )

        level_row = cursor.fetchone()

        if level_row is None:
            return

        level_id = level_row["id"]

        # =========================
        # MODULES
        # =========================

        for (
            code,
            title,
            description,
            sort_order,
            estimated_minutes,
        ) in STARTER_MODULES:

            cursor.execute(
                """
                INSERT OR IGNORE INTO course_modules (
                    level_id,
                    code,
                    title,
                    description,
                    sort_order,
                    estimated_minutes
                )
                VALUES (?, ?, ?, ?, ?, ?)
                """,
                (
                    level_id,
                    code,
                    title,
                    description,
                    sort_order,
                    estimated_minutes,
                ),
            )

        # =========================
        # LESSONS
        # =========================

        for (
            lesson_code,
            title,
            lesson_type,
            summary,
            sort_order,
            estimated_minutes,
        ) in STARTER_LESSONS:

            module_code = lesson_code.rsplit("_", 1)[0]

            cursor.execute(
                """
                SELECT id
                FROM course_modules
                WHERE code = ?
                """,
                (module_code,),
            )

            module_row = cursor.fetchone()

            if module_row is None:
                continue

            module_id = module_row["id"]

            cursor.execute(
                """
                INSERT OR IGNORE INTO lessons (
                    module_id,
                    code,
                    title,
                    lesson_type,
                    summary,
                    sort_order,
                    estimated_minutes,
                    xp_reward,
                    passing_score,
                    is_required
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    module_id,
                    lesson_code,
                    title,
                    lesson_type,
                    summary,
                    sort_order,
                    estimated_minutes,
                    10,
                    85,
                    1,
                ),
            )

        connection.commit()

    finally:
        connection.close()
