from database.database import get_connection


# ============================================================
# LEVEL 5
# MODULE 01 - ARCHICAD INTERFEYSI
# ============================================================

LEVEL05_MODULE01_LESSONS = [
    (
        "L05_M01",
        "L05_M01_001",
        "Archicad ish muhiti",
        "theory",
        "Archicad oynasining asosiy qismlari va ish mantiqini tushunish.",
        1,
        35,
        20,
    ),
    (
        "L05_M01",
        "L05_M01_002",
        "ToolBox va Info Box",
        "theory",
        "Asboblarni tanlash va ularning asosiy parametrlarini boshqarish.",
        2,
        40,
        20,
    ),
    (
        "L05_M01",
        "L05_M01_003",
        "2D va 3D oynalar",
        "theory",
        "Plan, section, elevation va 3D ko'rinishlar o'rtasidagi farqni tushunish.",
        3,
        40,
        20,
    ),
    (
        "L05_M01",
        "L05_M01_004",
        "Zoom, Pan va tanlash",
        "practice",
        "Loyiha ichida tez harakatlanish va elementlarni to'g'ri tanlash.",
        4,
        40,
        20,
    ),
    (
        "L05_M01",
        "L05_M01_005",
        "Interfeys mini-amaliyoti",
        "practice",
        "Archicad interfeysida asosiy boshqaruvlarni mustaqil topish va ishlatish.",
        5,
        50,
        25,
    ),
]


# ============================================================
# CONTENT
# ============================================================

LEVEL05_MODULE01_CONTENT = {
    "L05_M01_001": [
        {
            "title": "Archicadni birinchi marta ochganda",
            "type": "highlight",
            "text": """
            Boshlovchi uchun Archicad
            juda ko'p tugma va oynalardan
            iboratdek ko'rinadi.

            <br><br>

            Lekin interfeysni
            bir nechta asosiy hududga ajratsak,
            hammasi ancha tushunarli bo'ladi.
            """,
        },
        {
            "title": "Asosiy hududlar",
            "type": "normal",
            "text": """
            Archicad ish muhitida odatda:

            <br><br>

            • ishchi maydon;<br>
            • ToolBox;<br>
            • Info Box;<br>
            • Navigator;<br>
            • menyular;<br>
            • toolbarlar;<br>
            • palette oynalari

            <br><br>

            bilan ishlaysiz.
            """,
        },
        {
            "title": "Ishchi maydon",
            "type": "normal",
            "text": """
            Ishchi maydon —
            loyiha chiziladigan va
            ko'riladigan asosiy hudud.

            <br><br>

            Plan, kesim, fasad
            yoki 3D shu yerda ochiladi.
            """,
        },
        {
            "title": "Tasavvur qiling",
            "type": "example",
            "text": """
            Archicadni avtomobil kabinasi deb tasavvur qiling.

            <br><br>

            Ishchi maydon — old oynangiz.

            <br><br>

            ToolBox — boshqaruv asboblari.

            <br><br>

            Navigator — qayerda turganingizni
            ko'rsatadigan xarita.
            """,
        },
        {
            "title": "Birinchi maqsad",
            "type": "highlight",
            "text": """
            Hozir barcha tugmalarni
            yodlash shart emas.

            <br><br>

            Birinchi maqsad:

            <br><br>

            <b>
            qaysi vazifa qayerdan boshqarilishini
            tushunish.
            </b>
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Archicadni oching.

            <br><br>

            Quyidagilarni toping:

            <br><br>

            • ToolBox;<br>
            • Info Box;<br>
            • Navigator;<br>
            • asosiy ishchi maydon.

            <br><br>

            Hech narsani chizish shart emas.
            """,
        },
    ],

    "L05_M01_002": [
        {
            "title": "ToolBox nima?",
            "type": "highlight",
            "text": """
            ToolBox —
            Archicaddagi asosiy
            chizish va modellashtirish asboblari joylashgan panel.
            """,
        },
        {
            "title": "Tool turlari",
            "type": "normal",
            "text": """
            ToolBox orqali masalan:

            <br><br>

            • Wall;<br>
            • Slab;<br>
            • Door;<br>
            • Window;<br>
            • Column;<br>
            • Beam;<br>
            • Object;<br>
            • Line;<br>
            • Fill;<br>
            • Text

            <br><br>

            kabi instrumentlar tanlanadi.
            """,
        },
        {
            "title": "Info Box nima?",
            "type": "highlight",
            "text": """
            Tool tanlanganidan keyin
            uning tezkor asosiy parametrlarini
            Info Box orqali ko'rish va o'zgartirish mumkin.
            """,
        },
        {
            "title": "Misol",
            "type": "example",
            "text": """
            Wall Tool tanlandi.

            <br><br>

            Endi devorning:

            <br><br>

            • turini;<br>
            • geometriyasini;<br>
            • ayrim o'lchamlarini;<br>
            • reference parametrlarini

            <br><br>

            boshqarishingiz mumkin.
            """,
        },
        {
            "title": "Settings oynasi",
            "type": "normal",
            "text": """
            Info Box tezkor sozlama beradi.

            <br><br>

            Lekin elementning
            batafsil parametrlariga kirish uchun
            uning Settings oynasi ishlatiladi.
            """,
        },
        {
            "title": "Muhim fikr",
            "type": "warning",
            "text": """
            Asbobni tanlab darhol chizishga shoshilmang.

            <br><br>

            Avval:

            <br><br>

            <b>
            TOOL → PARAMETER → CHIZISH
            </b>

            <br><br>

            ketma-ketligiga odatlaning.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Wall Toolni tanlang.

            <br><br>

            Info Boxda kamida
            5 ta parametrni toping.

            <br><br>

            Hozircha ularni o'zgartirmang.
            """,
        },
    ],

    "L05_M01_003": [
        {
            "title": "Archicad faqat plan emas",
            "type": "highlight",
            "text": """
            Archicadda bitta BIM model
            turli ko'rinishlarda ishlatiladi.

            <br><br>

            Siz bir xil bino bilan
            2D va 3D muhitlarda ishlaysiz.
            """,
        },
        {
            "title": "Floor Plan",
            "type": "normal",
            "text": """
            Floor Plan —
            qavat rejasini ko'radigan
            asosiy 2D ish muhiti.

            <br><br>

            Devor,
            eshik,
            deraza
            va boshqa elementlar
            shu yerda boshqarilishi mumkin.
            """,
        },
        {
            "title": "3D Window",
            "type": "normal",
            "text": """
            3D Window orqali
            loyihani hajmli ko'rinishda
            tekshirishingiz mumkin.

            <br><br>

            Bu faqat prezentatsiya uchun emas.

            <br><br>

            Modeldagi xatolarni
            tushunishda ham foydali.
            """,
        },
        {
            "title": "Section",
            "type": "normal",
            "text": """
            Section —
            binoni vertikal kesib ko'rish imkonini beradi.

            <br><br>

            Qavat balandligi,
            tom,
            pol,
            shift
            va vertikal aloqalarni
            tahlil qilishda muhim.
            """,
        },
        {
            "title": "Elevation",
            "type": "normal",
            "text": """
            Elevation —
            binoning tashqi fasadini
            to'g'ri proyeksiyada ko'rsatadi.
            """,
        },
        {
            "title": "BIM fikrlashi",
            "type": "highlight",
            "text": """
            Muhim farq:

            <br><br>

            siz har safar
            boshqa bino chizmayapsiz.

            <br><br>

            Siz bitta modelni
            turli nuqtai nazardan ko'ryapsiz.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Loyihada navbat bilan oching:

            <br><br>

            FLOOR PLAN<br>
            3D<br>
            SECTION<br>
            ELEVATION

            <br><br>

            va ularning farqini kuzating.
            """,
        },
    ],

    "L05_M01_004": [
        {
            "title": "Tez ishlash chizishdan oldin boshlanadi",
            "type": "highlight",
            "text": """
            Archicadda professional tezlik
            faqat tez chizish degani emas.

            <br><br>

            Loyiha ichida
            tez va aniq harakatlanish ham muhim.
            """,
        },
        {
            "title": "Zoom",
            "type": "normal",
            "text": """
            Zoom orqali
            loyihaning kerakli qismiga
            yaqinlashasiz yoki uzoqlashasiz.

            <br><br>

            Juda uzoq zoomda
            aniqlik kamayadi.

            <br><br>

            Juda yaqin zoomda esa
            umumiy kontekst yo'qoladi.
            """,
        },
        {
            "title": "Pan",
            "type": "normal",
            "text": """
            Pan —
            ko'rinishni siljitish.

            <br><br>

            Model joyidan ko'chmaydi.

            <br><br>

            Faqat sizning ko'rish oynangiz
            boshqa qismga o'tadi.
            """,
        },
        {
            "title": "Elementni tanlash",
            "type": "normal",
            "text": """
            Elementni o'zgartirishdan oldin
            qaysi obyekt tanlanganini
            aniq tekshiring.

            <br><br>

            Noto'g'ri elementni tanlab
            tahrirlash boshlovchilarda
            ko'p uchraydigan xato.
            """,
        },
        {
            "title": "Selection va tool farqi",
            "type": "example",
            "text": """
            Wall Tool faol bo'lishi mumkin.

            <br><br>

            Lekin bu ekrandagi har bir
            tanlangan element devor degani emas.

            <br><br>

            Faol asbob va tanlangan elementni
            bir-biridan farqlashni o'rganing.
            """,
        },
        {
            "title": "Esc odati",
            "type": "normal",
            "text": """
            Noto'g'ri buyruq yoki
            faol jarayondan chiqish uchun
            Escape tugmasidan foydalanish
            ko'p vaziyatlarda foydali.

            <br><br>

            Har bir holatda aynan bir xil
            natija bo'lishi shart emas,
            lekin boshlovchi uchun
            bu muhim boshqaruv odatlaridan biri.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Bitta mavjud loyiha ichida:

            <br><br>

            • zoom qiling;<br>
            • pan qiling;<br>
            • devorni tanlang;<br>
            • tanlovni bekor qiling;<br>
            • boshqa elementni tanlang.

            <br><br>

            Hech narsani o'chirmang.
            """,
        },
    ],

    "L05_M01_005": [
        {
            "title": "Interfeys mini-amaliyoti",
            "type": "highlight",
            "text": """
            Endi maqsad —
            Archicad oynasida
            o'zingizni yo'qotmaslik.

            <br><br>

            Hali uy qurmaymiz.

            <br><br>

            Avval boshqaruvni mustahkamlaymiz.
            """,
        },
        {
            "title": "1-vazifa",
            "type": "example",
            "text": """
            Quyidagilarni toping:

            <br><br>

            • ToolBox;<br>
            • Info Box;<br>
            • Navigator;<br>
            • ishchi maydon.
            """,
        },
        {
            "title": "2-vazifa",
            "type": "example",
            "text": """
            ToolBoxdan quyidagilarni toping:

            <br><br>

            • Wall;<br>
            • Slab;<br>
            • Door;<br>
            • Window;<br>
            • Object;<br>
            • Line.

            <br><br>

            Hali element yaratishingiz shart emas.
            """,
        },
        {
            "title": "3-vazifa",
            "type": "example",
            "text": """
            Wall Toolni tanlang.

            <br><br>

            Keyin Info Boxga qarang.

            <br><br>

            Tool almashganda
            Info Box tarkibi qanday o'zgarishini kuzating.
            """,
        },
        {
            "title": "4-vazifa",
            "type": "example",
            "text": """
            Floor Plan va 3D Window
            orasida o'ting.

            <br><br>

            Bitta loyiha ikki xil
            ko'rinishda qanday aks etishini tushuning.
            """,
        },
        {
            "title": "5-vazifa",
            "type": "example",
            "text": """
            3 daqiqa davomida
            faqat navigation mashqi qiling:

            <br><br>

            ZOOM → PAN → SELECT →
            DESELECT → ZOOM OUT.
            """,
        },
        {
            "title": "Xatoni toping",
            "type": "warning",
            "text": """
            O'quvchi kerakli devorni o'zgartirmoqchi.

            <br><br>

            Lekin boshqa element tanlanganini
            tekshirmasdan parametrni o'zgartirdi.

            <br><br>

            Natija:
            noto'g'ri obyekt o'zgardi.

            <br><br>

            Muammo nimada?

            <br><br>

            <b>
            Amal qilishdan oldin
            selection tekshirilmagan.
            </b>
            """,
        },
        {
            "title": "Modul yakuni",
            "type": "highlight",
            "text": """
            Siz endi:

            <br><br>

            ✓ Archicad ish muhitini tushunasiz;<br>
            ✓ ToolBoxni taniysiz;<br>
            ✓ Info Box vazifasini bilasiz;<br>
            ✓ 2D va 3D farqini tushunasiz;<br>
            ✓ zoom va pan bilan ishlaysiz;<br>
            ✓ element tanlash mantiqini tushunasiz.

            <br><br>

            Keyingi modul:
            <b>Navigator.</b>
            """,
        },
    ],
}


# ============================================================
# QUIZ
# ============================================================

LEVEL05_MODULE01_QUIZ = {
    "L05_M01_001": [
        {
            "code": "L05_Q001",
            "question": "Archicadni o'rganishda barcha tugmalarni birdan yodlash shartmi?",
            "explanation": (
                "Avval interfeysning asosiy mantiqi va vazifalar qayerda joylashganini tushunish muhim."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L05_Q002",
            "question": "Archicadning asosiy ishchi maydonida loyiha ko'rinishlari ochiladimi?",
            "explanation": (
                "Plan, section, elevation va 3D kabi ko'rinishlar ishchi maydonda ishlatiladi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L05_Q003",
            "question": "Navigator loyihadagi turli ko'rinish va qismlarga o'tishda yordam beradimi?",
            "explanation": (
                "Navigator loyiha strukturasi bo'ylab harakatlanish uchun ishlatiladi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L05_M01_002": [
        {
            "code": "L05_Q004",
            "question": "ToolBox orqali Wall va Slab kabi asboblar tanlanadimi?",
            "explanation": (
                "ToolBox asosiy modellashtirish va chizish asboblarini o'z ichiga oladi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L05_Q005",
            "question": "Info Box tanlangan toolning tezkor parametrlarini ko'rsatadimi?",
            "explanation": (
                "Info Box faol tool yoki elementga tegishli asosiy parametrlarni tez boshqarish imkonini beradi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L05_Q006",
            "question": "Professional odat sifatida parametrlarni tekshirmasdan darhol chizishni boshlash yaxshimi?",
            "explanation": (
                "Tool va uning parametrlarini tekshirib keyin element yaratish xatolarni kamaytiradi."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
    ],

    "L05_M01_003": [
        {
            "code": "L05_Q007",
            "question": "Floor Plan va 3D Window bitta loyiha modelining turli ko'rinishlari bo'lishi mumkinmi?",
            "explanation": (
                "BIM model bir nechta ko'rinish orqali ko'riladi va boshqariladi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L05_Q008",
            "question": "Section binoning vertikal aloqalarini ko'rishda foydalimi?",
            "explanation": (
                "Kesim qavatlar, balandliklar va vertikal konstruktiv munosabatlarni ko'rsatadi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L05_Q009",
            "question": "3D Window faqat chiroyli rasm olish uchun ishlatiladimi?",
            "explanation": (
                "3D modelni tekshirish va xatolarni tushunishda ham muhim."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
    ],

    "L05_M01_004": [
        {
            "code": "L05_Q010",
            "question": "Pan ishlatilganda modelning o'zi joyidan ko'chadimi?",
            "explanation": (
                "Pan faqat ekrandagi ko'rish hududini siljitadi."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L05_Q011",
            "question": "Elementni tahrirlashdan oldin qaysi obyekt tanlanganini tekshirish kerakmi?",
            "explanation": (
                "Noto'g'ri selection noto'g'ri elementni o'zgartirishga olib kelishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L05_Q012",
            "question": "Zoom va Pan loyiha ichida navigatsiya qilishga yordam beradimi?",
            "explanation": (
                "Bu asosiy ko'rish va harakatlanish boshqaruvlaridir."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L05_M01_005": [
        {
            "code": "L05_Q013",
            "question": "Tool almashganda Info Box tarkibi o'zgarishi mumkinmi?",
            "explanation": (
                "Info Box faol instrumentga mos parametrlarni ko'rsatadi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L05_Q014",
            "question": "Boshlang'ich Archicad mashqida navigationni alohida mashq qilish foydalimi?",
            "explanation": (
                "Zoom, pan va selectionni yaxshi o'zlashtirish keyingi modellashtirishni tezlashtiradi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L05_Q015",
            "question": "Archicad interfeysini o'rganishdagi asosiy maqsad qaysi?",
            "explanation": (
                "Asosiy maqsad vazifa uchun kerakli boshqaruv qayerda ekanini tushunish."
            ),
            "options": [
                ("A", "Qaysi vazifa qayerdan boshqarilishini tushunish", True),
                ("B", "Barcha ikonalarni bir kunda yodlash", False),
            ],
        },
    ],
}


# ============================================================
# DATABASE SEED
# ============================================================

def seed_level05_module01():
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
        ) in LEVEL05_MODULE01_LESSONS:

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
