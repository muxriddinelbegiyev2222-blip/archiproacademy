from database.database import get_connection


# ============================================================
# LEVEL 5
# MODULE 02 - NAVIGATOR
# ============================================================

LEVEL05_MODULE02_LESSONS = [
    (
        "L05_M02",
        "L05_M02_001",
        "Navigator nima?",
        "theory",
        "Archicaddagi loyiha strukturasini Navigator orqali tushunish.",
        1,
        35,
        20,
    ),
    (
        "L05_M02",
        "L05_M02_002",
        "Project Map",
        "theory",
        "Floor Plan, Section, Elevation va boshqa model qismlarini boshqarish.",
        2,
        40,
        20,
    ),
    (
        "L05_M02",
        "L05_M02_003",
        "View Map",
        "theory",
        "Loyiha ko'rinishlarini saqlash va tartibli boshqarish.",
        3,
        40,
        20,
    ),
    (
        "L05_M02",
        "L05_M02_004",
        "Layout Book",
        "theory",
        "Chizmalarni listlarga joylashtirish va loyiha albomi mantiqini tushunish.",
        4,
        40,
        20,
    ),
    (
        "L05_M02",
        "L05_M02_005",
        "Navigator mini-amaliyoti",
        "practice",
        "Project Map, View Map va Layout Book o'rtasida mustaqil ishlash.",
        5,
        50,
        25,
    ),
]


# ============================================================
# CONTENT
# ============================================================

LEVEL05_MODULE02_CONTENT = {
    "L05_M02_001": [
        {
            "title": "Navigator — loyiha xaritasi",
            "type": "highlight",
            "text": """
            Archicad loyihasi kattalashgani sari
            ko'plab planlar,
            kesimlar,
            fasadlar,
            3D ko'rinishlar
            va listlar paydo bo'ladi.

            <br><br>

            Navigator shu strukturani
            boshqarishga yordam beradi.
            """,
        },
        {
            "title": "Navigatorning asosiy mantiqi",
            "type": "normal",
            "text": """
            Boshlang'ich bosqichda
            uchta asosiy tushunchani ajrating:

            <br><br>

            • Project Map;<br>
            • View Map;<br>
            • Layout Book.
            """,
        },
        {
            "title": "Oddiy taqqoslash",
            "type": "example",
            "text": """
            Project Map —
            binoning real loyiha strukturasi.

            <br><br>

            View Map —
            shu loyihadan tayyorlangan
            saqlangan ko'rinishlar.

            <br><br>

            Layout Book —
            chop etish va topshirish uchun
            yig'ilgan listlar.
            """,
        },
        {
            "title": "Nega bu muhim?",
            "type": "highlight",
            "text": """
            Professional loyihada
            barcha narsani bitta plan oynasidan
            boshqarish mumkin emas.

            <br><br>

            Tartib bo'lmasa,
            loyiha juda tez chalkashadi.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Navigatorni oching.

            <br><br>

            Quyidagilarni toping:

            <br><br>

            PROJECT MAP<br>
            VIEW MAP<br>
            LAYOUT BOOK

            <br><br>

            Hozircha hech narsani o'zgartirmang.
            """,
        },
    ],

    "L05_M02_002": [
        {
            "title": "Project Map nima?",
            "type": "highlight",
            "text": """
            Project Map —
            Archicad modelining
            asosiy strukturasi.

            <br><br>

            Bu yerda loyiha
            real qismlarga ajratilgan holda ko'rinadi.
            """,
        },
        {
            "title": "Project Map tarkibi",
            "type": "normal",
            "text": """
            Bu yerda odatda:

            <br><br>

            • Stories;<br>
            • Sections;<br>
            • Elevations;<br>
            • Interior Elevations;<br>
            • Worksheets;<br>
            • Details;<br>
            • 3D Documents

            <br><br>

            kabi bo'limlarni ko'rishingiz mumkin.
            """,
        },
        {
            "title": "Floor Plan",
            "type": "example",
            "text": """
            Stories bo'limida
            qavat rejalari joylashadi.

            <br><br>

            Masalan:

            <br><br>

            Ground Floor<br>
            First Floor<br>
            Roof Level
            """,
        },
        {
            "title": "Section va Elevation",
            "type": "normal",
            "text": """
            Section va Elevation
            alohida loyiha ko'rinishlari sifatida
            Project Map ichida mavjud bo'ladi.
            """,
        },
        {
            "title": "Muhim farq",
            "type": "warning",
            "text": """
            Project Mapdagi element —
            loyiha strukturasining o'zi.

            <br><br>

            Bu hali chop etishga tayyorlangan
            yakuniy view degani emas.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Project Map ichida toping:

            <br><br>

            • Floor Plan;<br>
            • Section;<br>
            • Elevation;<br>
            • 3D.

            <br><br>

            Har birini navbat bilan oching.
            """,
        },
    ],

    "L05_M02_003": [
        {
            "title": "View Map nima?",
            "type": "highlight",
            "text": """
            View Map —
            loyiha ko'rinishlarini
            kerakli sozlamalar bilan
            saqlash uchun ishlatiladi.
            """,
        },
        {
            "title": "View nima?",
            "type": "normal",
            "text": """
            View —
            modelning shunchaki tasviri emas.

            <br><br>

            U ma'lum ko'rinish sozlamalari bilan
            saqlangan holat bo'lishi mumkin.
            """,
        },
        {
            "title": "Nima uchun kerak?",
            "type": "example",
            "text": """
            Bitta Floor Plan mavjud.

            <br><br>

            Lekin undan:

            <br><br>

            • arxitektura plan;<br>
            • mebel plan;<br>
            • dimension plan;<br>
            • presentation plan

            <br><br>

            kabi turli viewlar tayyorlanishi mumkin.
            """,
        },
        {
            "title": "Bir model — bir nechta view",
            "type": "highlight",
            "text": """
            Bu Archicad workflowining
            juda muhim prinsipi:

            <br><br>

            <b>
            model bitta,
            ko'rinishlar ko'p.
            </b>
            """,
        },
        {
            "title": "Nomlash",
            "type": "normal",
            "text": """
            Viewlarni tartibli nomlash
            katta loyiha uchun juda muhim.

            <br><br>

            Masalan:

            <br><br>

            A-01 Ground Floor Plan<br>
            A-02 First Floor Plan<br>
            A-03 Roof Plan
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Bitta Floor Plan uchun
            ikki xil view yaratishni tasavvur qiling:

            <br><br>

            1. Working Plan<br>
            2. Presentation Plan

            <br><br>

            Ularning vazifasi nimada farq qilishini yozing.
            """,
        },
    ],

    "L05_M02_004": [
        {
            "title": "Layout Book nima?",
            "type": "highlight",
            "text": """
            Layout Book —
            loyiha chizmalarini
            topshiriladigan listlarga
            yig'ish joyi.
            """,
        },
        {
            "title": "Layout",
            "type": "normal",
            "text": """
            Layoutni qog'oz list deb tasavvur qiling.

            <br><br>

            Unga:

            <br><br>

            • plan;<br>
            • fasad;<br>
            • kesim;<br>
            • detal;<br>
            • matn

            <br><br>

            joylashtirilishi mumkin.
            """,
        },
        {
            "title": "View va Layout farqi",
            "type": "highlight",
            "text": """
            View —
            loyihaning saqlangan ko'rinishi.

            <br><br>

            Layout —
            shu ko'rinish joylashtirilgan
            yakuniy list.
            """,
        },
        {
            "title": "Misol",
            "type": "example",
            "text": """
            View Mapda:

            <br><br>

            Ground Floor Plan

            <br><br>

            mavjud.

            <br><br>

            Uni Layout Bookdagi:

            <br><br>

            A-101 Ground Floor

            <br><br>

            listiga joylashtirish mumkin.
            """,
        },
        {
            "title": "Loyiha albomi",
            "type": "normal",
            "text": """
            Bir nechta Layout
            birgalikda loyiha albomini
            tashkil qiladi.

            <br><br>

            Masalan:

            <br><br>

            • titul;<br>
            • genplan;<br>
            • planlar;<br>
            • fasadlar;<br>
            • kesimlar;<br>
            • detallar.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            1 qavatli uy uchun
            6 ta layout nomini yozing.

            <br><br>

            Ularni professional
            ketma-ketlikda joylashtiring.
            """,
        },
    ],

    "L05_M02_005": [
        {
            "title": "Navigator mini-amaliyoti",
            "type": "highlight",
            "text": """
            Endi uchta tushunchani
            aralashtirmasdan ishlaymiz:

            <br><br>

            PROJECT MAP<br>
            VIEW MAP<br>
            LAYOUT BOOK
            """,
        },
        {
            "title": "1-vazifa",
            "type": "example",
            "text": """
            Project Mapdan:

            <br><br>

            Ground Floor Plan
            ni toping va oching.
            """,
        },
        {
            "title": "2-vazifa",
            "type": "example",
            "text": """
            Section va Elevation
            bo'limlarini toping.

            <br><br>

            Ularning modeldagi
            real ko'rinish ekanini tushuning.
            """,
        },
        {
            "title": "3-vazifa",
            "type": "example",
            "text": """
            View Mapga o'ting.

            <br><br>

            Qaysi viewlar mavjudligini ko'ring.

            <br><br>

            Ularning nomlanish tartibiga e'tibor bering.
            """,
        },
        {
            "title": "4-vazifa",
            "type": "example",
            "text": """
            Layout Bookga o'ting.

            <br><br>

            Mavjud listlarni oching.

            <br><br>

            Bir list ichida
            nechta chizma joylashganini kuzating.
            """,
        },
        {
            "title": "Xatoni toping",
            "type": "warning",
            "text": """
            O'quvchi Project Mapdagi
            Floor Planni ochdi.

            <br><br>

            Uni yakuniy chop etish listi
            deb o'yladi.

            <br><br>

            Muammo nimada?

            <br><br>

            <b>
            Model ko'rinishi va Layout
            aralashtirib yuborilgan.
            </b>
            """,
        },
        {
            "title": "Professional fikrlash",
            "type": "highlight",
            "text": """
            Esda saqlang:

            <br><br>

            <b>
            PROJECT MAP = MODEL
            </b>

            <br><br>

            <b>
            VIEW MAP = SAQLANGAN KO'RINISH
            </b>

            <br><br>

            <b>
            LAYOUT BOOK = TOPSHIRILADIGAN LIST
            </b>
            """,
        },
        {
            "title": "Modul yakuni",
            "type": "highlight",
            "text": """
            Siz endi:

            <br><br>

            ✓ Navigator vazifasini tushunasiz;<br>
            ✓ Project Mapni taniysiz;<br>
            ✓ View Map vazifasini bilasiz;<br>
            ✓ Layout Bookni tushunasiz;<br>
            ✓ model, view va layoutni farqlaysiz.

            <br><br>

            Keyingi modul:
            <b>Wall Tool.</b>
            """,
        },
    ],
}


# ============================================================
# QUIZ
# ============================================================

LEVEL05_MODULE02_QUIZ = {
    "L05_M02_001": [
        {
            "code": "L05_Q016",
            "question": "Navigator loyiha strukturasini boshqarishga yordam beradimi?",
            "explanation": (
                "Navigator planlar, kesimlar, viewlar va layoutlar orasida tartibli ishlashga yordam beradi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L05_Q017",
            "question": "Project Map, View Map va Layout Book bir xil narsa hisoblanadimi?",
            "explanation": (
                "Ularning vazifalari turlicha: model, saqlangan ko'rinish va list."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L05_Q018",
            "question": "Katta loyihada Navigator tartibni saqlashga yordam beradimi?",
            "explanation": (
                "Ko'p ko'rinish va listlar bilan ishlaganda loyiha strukturasi muhim."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L05_M02_002": [
        {
            "code": "L05_Q019",
            "question": "Project Map loyiha modelining asosiy strukturasini ko'rsatadimi?",
            "explanation": (
                "Stories, Sections, Elevations va boshqa model qismlari shu yerda ko'rinadi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L05_Q020",
            "question": "Section Project Map tarkibida bo'lishi mumkinmi?",
            "explanation": (
                "Section loyiha modelining asosiy ko'rinishlaridan biri."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L05_Q021",
            "question": "Project Mapdagi Floor Plan avtomatik ravishda yakuniy chop etish listimi?",
            "explanation": (
                "Floor Plan model ko'rinishi, Layout esa yakuniy list hisoblanadi."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
    ],

    "L05_M02_003": [
        {
            "code": "L05_Q022",
            "question": "View Map saqlangan loyiha ko'rinishlarini boshqaradimi?",
            "explanation": (
                "Viewlar ma'lum ko'rinish va sozlamalar bilan saqlanishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L05_Q023",
            "question": "Bitta modeldan bir nechta turli view tayyorlash mumkinmi?",
            "explanation": (
                "Bitta modeldan turli maqsad uchun bir nechta saqlangan ko'rinish olinishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L05_Q024",
            "question": "Viewlarni tartibli nomlash katta loyihada foydalimi?",
            "explanation": (
                "Tartibli nomlash viewlarni tez topish va boshqarishga yordam beradi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L05_M02_004": [
        {
            "code": "L05_Q025",
            "question": "Layout Book topshiriladigan listlarni boshqaradimi?",
            "explanation": (
                "Layout Book chizmalarni loyiha albomi formatida joylashtirish uchun ishlatiladi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L05_Q026",
            "question": "View va Layout bir xil narsa hisoblanadimi?",
            "explanation": (
                "View saqlangan ko'rinish, Layout esa shu ko'rinish joylashtiriladigan list."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L05_Q027",
            "question": "Bitta Layout ichida bir nechta chizma joylashtirilishi mumkinmi?",
            "explanation": (
                "Plan, fasad, kesim yoki detallar bitta listda birgalikda joylashtirilishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L05_M02_005": [
        {
            "code": "L05_Q028",
            "question": "Project Mapni MODEL deb eslab qolish mumkinmi?",
            "explanation": (
                "Project Map loyiha modelining asosiy strukturasini ifodalaydi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L05_Q029",
            "question": "View Mapni saqlangan ko'rinishlar tizimi deb tushunish to'g'rimi?",
            "explanation": (
                "View Map turli maqsad uchun tayyorlangan ko'rinishlarni boshqaradi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L05_Q030",
            "question": "Navigator bo'yicha asosiy uchlik qaysi?",
            "explanation": (
                "Boshlang'ich workflow uchun Project Map, View Map va Layout Bookni farqlash muhim."
            ),
            "options": [
                ("A", "Project Map + View Map + Layout Book", True),
                ("B", "Wall + Door + Roof", False),
            ],
        },
    ],
}


# ============================================================
# DATABASE SEED
# ============================================================

def seed_level05_module02():
    connection = get_connection()

    try:
        cursor = connection.cursor()

        for (
            module_code,
            lesson_code,
            title,
            lesson_type,
            summary,
            sort_order,
            estimated_minutes,
            xp_reward,
        ) in LEVEL05_MODULE02_LESSONS:

            cursor.execute(
                """
                SELECT id
                FROM course_modules
                WHERE code = ?
                LIMIT 1
                """,
                (module_code,),
            )

            module = cursor.fetchone()

            if module is None:
                continue

            cursor.execute(
                """
                INSERT INTO lessons (
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

                ON CONFLICT(code)
                DO UPDATE SET
                    module_id = excluded.module_id,
                    title = excluded.title,
                    lesson_type = excluded.lesson_type,
                    summary = excluded.summary,
                    sort_order = excluded.sort_order,
                    estimated_minutes = excluded.estimated_minutes,
                    xp_reward = excluded.xp_reward,
                    passing_score = excluded.passing_score,
                    is_required = excluded.is_required
                """,
                (
                    module["id"],
                    lesson_code,
                    title,
                    lesson_type,
                    summary,
                    sort_order,
                    estimated_minutes,
                    xp_reward,
                    80,
                    1,
                ),
            )

        connection.commit()

    finally:
        connection.close()
