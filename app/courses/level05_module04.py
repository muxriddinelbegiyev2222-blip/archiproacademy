from database.database import get_connection


# ============================================================
# LEVEL 5
# MODULE 04 - SLAB TOOL
# ============================================================

LEVEL05_MODULE04_LESSONS = [
    (
        "L05_M04",
        "L05_M04_001",
        "Slab Tool asoslari",
        "theory",
        "Archicadda pol va gorizontal plita elementlarini yaratish mantig'ini tushunish.",
        1,
        40,
        20,
    ),
    (
        "L05_M04",
        "L05_M04_002",
        "Slab qalinligi va balandligi",
        "theory",
        "Slabning qalinligi, joylashuv balandligi va qavat bilan aloqasini tushunish.",
        2,
        40,
        20,
    ),
    (
        "L05_M04",
        "L05_M04_003",
        "Slab konturini yaratish",
        "practice",
        "Uy konturi bo'yicha aniq slab geometriyasini yaratish va tahrirlash.",
        3,
        45,
        20,
    ),
    (
        "L05_M04",
        "L05_M04_004",
        "Teshik va murakkab kontur",
        "practice",
        "Slab ichidagi teshiklar va murakkab polygon shakllar bilan ishlash.",
        4,
        50,
        20,
    ),
    (
        "L05_M04",
        "L05_M04_005",
        "Slab Tool mini-loyiha",
        "practice",
        "Oddiy turar joy uchun slab yaratish va uni 2D hamda 3Dda tekshirish.",
        5,
        60,
        25,
    ),
]


# ============================================================
# CONTENT
# ============================================================

LEVEL05_MODULE04_CONTENT = {
    "L05_M04_001": [
        {
            "title": "Slab Tool nima?",
            "type": "highlight",
            "text": """
            Archicaddagi Slab Tool
            gorizontal BIM elementlarini
            yaratish uchun ishlatiladi.

            <br><br>

            Boshlang'ich turar joy modelida
            undan pol yoki plita
            geometriyasini yaratishda foydalanamiz.
            """,
        },
        {
            "title": "Slab oddiy Fill emas",
            "type": "normal",
            "text": """
            Floor Planda slab
            yopiq 2D shaklga o'xshashi mumkin.

            <br><br>

            Lekin u aslida
            qalinlik va balandlikka ega
            3D model elementi.
            """,
        },
        {
            "title": "Toolni tanlash",
            "type": "normal",
            "text": """
            ToolBox ichidan
            <b>Slab Tool</b>ni tanlang.

            <br><br>

            So'ng Info Boxdagi
            slab parametrlariga e'tibor bering.
            """,
        },
        {
            "title": "Professional workflow",
            "type": "highlight",
            "text": """
            Slab yaratishda ham:

            <br><br>

            <b>
            TOOL → PARAMETER → CONTOUR →
            2D/3D TEKSHIRUV
            </b>

            <br><br>

            ketma-ketligini ishlatamiz.
            """,
        },
        {
            "title": "Tasavvur qiling",
            "type": "example",
            "text": """
            Uy devorlari tayyor.

            <br><br>

            Lekin Floor Plan ichida
            hech qanday pol plitasi yaratilmagan.

            <br><br>

            3Dga o'tganda devorlar turibdi,
            lekin bino gorizontal bazasi
            to'liq modellashtirilmagan.

            <br><br>

            Endi Slab Tool kerak.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            1. Slab Toolni toping.<br><br>
            2. Uni tanlang.<br><br>
            3. Info Boxni kuzating.<br><br>
            4. Oddiy to'rtburchak slab yarating.<br><br>
            5. 3Dga o'tib ko'ring.
            """,
        },
    ],

    "L05_M04_002": [
        {
            "title": "Slab qalinligi",
            "type": "highlight",
            "text": """
            Slabning eng muhim
            xususiyatlaridan biri —
            uning qalinligi.

            <br><br>

            Bu qiymat 3D modelga
            bevosita ta'sir qiladi.
            """,
        },
        {
            "title": "Qalinlikni taxmin bilan bermang",
            "type": "warning",
            "text": """
            O'quv bosqichida
            texnik konstruktsiya hali
            to'liq hisoblanmagan bo'lishi mumkin.

            <br><br>

            Shuning uchun real loyiha uchun
            konstruktor talab qiladigan
            qiymatlarni o'zboshimchalik bilan
            qabul qilmaslik kerak.
            """,
        },
        {
            "title": "Elevation",
            "type": "normal",
            "text": """
            Slabning vertikal joylashuvi
            ham muhim.

            <br><br>

            Agar elevation noto'g'ri bo'lsa,
            plan yaxshi ko'rinsa ham
            3D va sectionda xato chiqadi.
            """,
        },
        {
            "title": "Home Story bilan aloqa",
            "type": "normal",
            "text": """
            Slab qaysi qavatga tegishli
            ekanini tushunish kerak.

            <br><br>

            Bu ayniqsa
            ko'p qavatli modelga o'tganda
            muhimlashadi.
            """,
        },
        {
            "title": "Sectionda tekshiring",
            "type": "example",
            "text": """
            Floor Planda slabning
            vertikal joylashuvini
            to'liq tushunish qiyin.

            <br><br>

            Section oching.

            <br><br>

            Slabning devorga nisbatan
            qayerda turganini kuzating.
            """,
        },
        {
            "title": "3D tekshiruv",
            "type": "highlight",
            "text": """
            Slab yaratgandan keyin
            3Dga o'tish odatini hosil qiling.

            <br><br>

            Savollar:

            <br><br>

            • slab mavjudmi?<br>
            • balandligi to'g'rimi?<br>
            • konturi to'g'rimi?<br>
            • devorlar bilan aloqasi mantiqiymi?
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Bitta slab yarating.

            <br><br>

            So'ng uning:

            <br><br>

            • thickness;<br>
            • elevation

            <br><br>

            parametrlarini o'zgartiring.

            <br><br>

            Har bir o'zgarishni
            3D yoki Sectionda kuzating.
            """,
        },
    ],

    "L05_M04_003": [
        {
            "title": "Slab konturi yopiq shakl",
            "type": "highlight",
            "text": """
            Slab maydon hosil qilishi uchun
            uning konturi
            yopiq geometriya bo'lishi kerak.
            """,
        },
        {
            "title": "Oddiy to'rtburchak",
            "type": "normal",
            "text": """
            Eng oddiy slab —
            to'rtburchak shakl.

            <br><br>

            Bu Slab Toolni
            tushunish uchun
            eng yaxshi boshlang'ich mashq.
            """,
        },
        {
            "title": "Uy konturi bo'yicha",
            "type": "normal",
            "text": """
            Real uy har doim
            oddiy rectangle bo'lmaydi.

            <br><br>

            Slab konturi
            bino geometriyasini
            kuzatib borishi mumkin.
            """,
        },
        {
            "title": "Devor bilan tekshirish",
            "type": "example",
            "text": """
            Slab konturi
            tashqi devorlarga nisbatan
            qayerdan o'tayotganini tekshiring.

            <br><br>

            Uni shunchaki ko'z bilan
            devorga yaqin chizib qo'ymang.
            """,
        },
        {
            "title": "Node tahrirlash",
            "type": "normal",
            "text": """
            Kontur noto'g'ri chiqsa
            butun slabni o'chirib
            qayta chizish shart emas.

            <br><br>

            Kontur nuqtalarini
            tahrirlash orqali
            shaklni tuzatish mumkin.
            """,
        },
        {
            "title": "Xatoni toping",
            "type": "warning",
            "text": """
            Slab uy konturidan
            20–30 sm tasodifiy tashqariga chiqib ketgan.

            <br><br>

            Floor Planda sezilmagan.

            <br><br>

            3Dda esa bino tagida
            keraksiz chiqib turgan plita ko'rindi.

            <br><br>

            Sabab:
            kontur nazorat qilinmagan.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            L-shaklli slab yarating.

            <br><br>

            Keyin:

            <br><br>

            • bitta burchagini suring;<br>
            • bir tomonini uzaytiring;<br>
            • yana 3Dda tekshiring.
            """,
        },
    ],

    "L05_M04_004": [
        {
            "title": "Slab ichida teshik",
            "type": "highlight",
            "text": """
            Ba'zan slabning
            butun maydoni yopiq bo'lmaydi.

            <br><br>

            Uning ichida
            ochiq qoldiriladigan
            hudud kerak bo'lishi mumkin.
            """,
        },
        {
            "title": "Qayerda kerak bo'lishi mumkin?",
            "type": "normal",
            "text": """
            Keyingi murakkab loyihalarda
            slab opening masalasi:

            <br><br>

            • zina ochilishi;<br>
            • atrium;<br>
            • texnik opening;<br>
            • void

            <br><br>

            kabi holatlarda uchrashi mumkin.
            """,
        },
        {
            "title": "Teshik ham aniq geometriya",
            "type": "normal",
            "text": """
            Slab ichidagi teshikni ham
            tasodifiy chizish mumkin emas.

            <br><br>

            Uning konturi
            va joylashuvi
            alohida nazorat qilinadi.
            """,
        },
        {
            "title": "3Dda tekshirish",
            "type": "example",
            "text": """
            Floor Planda
            opening konturi ko'rinadi.

            <br><br>

            Lekin 3Dga o'tib,
            slab haqiqatan ochilganini
            ham tekshiring.
            """,
        },
        {
            "title": "Murakkab polygon",
            "type": "highlight",
            "text": """
            Slab to'rtburchak bo'lishi shart emas.

            <br><br>

            Bino shakliga qarab
            murakkab polygon konturdan
            tashkil topishi mumkin.
            """,
        },
        {
            "title": "Ortiqcha murakkablashtirmang",
            "type": "warning",
            "text": """
            Keraksiz ko'p node
            yaratish modelni
            boshqarishni qiyinlashtiradi.

            <br><br>

            Geometriya imkon qadar
            aniq va mantiqiy bo'lsin.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            To'rtburchak slab yarating.

            <br><br>

            Uning markazida
            kichik ochiq hudud yarating.

            <br><br>

            Keyin uni 3Dda
            turli burchakdan tekshiring.
            """,
        },
    ],

    "L05_M04_005": [
        {
            "title": "Slab Tool mini-loyiha",
            "type": "highlight",
            "text": """
            Endi Wall Toolda yaratilgan
            kichik uy modeliga
            slab qo'shamiz.

            <br><br>

            Maqsad:
            devor va slabni
            bir tizim sifatida ko'rish.
            """,
        },
        {
            "title": "1-bosqich — devorlarni tekshiring",
            "type": "normal",
            "text": """
            Floor Planda
            tashqi devor konturini tekshiring.

            <br><br>

            Slab geometriyasi uchun
            qaysi konturdan foydalanishingizni
            oldindan tushuning.
            """,
        },
        {
            "title": "2-bosqich — Slab Tool",
            "type": "normal",
            "text": """
            Slab Toolni tanlang.

            <br><br>

            Thickness va elevation
            parametrlarini tekshiring.
            """,
        },
        {
            "title": "3-bosqich — kontur",
            "type": "normal",
            "text": """
            Uy geometriyasiga mos
            slab konturini yarating.

            <br><br>

            Har bir burchakni
            aniq tekshiring.
            """,
        },
        {
            "title": "4-bosqich — 3D",
            "type": "normal",
            "text": """
            3D Windowga o'ting.

            <br><br>

            Tekshiring:

            <br><br>

            • slab mavjudmi;<br>
            • konturi devorlarga mosmi;<br>
            • tasodifiy chiqib ketgan joy bormi;<br>
            • balandligi to'g'rimi.
            """,
        },
        {
            "title": "5-bosqich — Section",
            "type": "normal",
            "text": """
            Section orqali
            slabning vertikal holatini tekshiring.

            <br><br>

            Floor Planda bilinmagan
            vertikal xatolar
            shu yerda ko'rinishi mumkin.
            """,
        },
        {
            "title": "Xatoni toping",
            "type": "warning",
            "text": """
            Uy Floor Planda
            mukammal ko'rinadi.

            <br><br>

            3Dda esa slab
            devorlardan ancha pastda turibdi.

            <br><br>

            Muammo qayerda?

            <br><br>

            <b>
            Slab elevation noto'g'ri.
            </b>
            """,
        },
        {
            "title": "Professional checklist",
            "type": "example",
            "text": """
            Slabni tekshiring:

            <br><br>

            <b>1.</b> To'g'ri qavatdami?<br><br>
            <b>2.</b> Thickness nazoratdami?<br><br>
            <b>3.</b> Elevation to'g'rimi?<br><br>
            <b>4.</b> Kontur yopiqmi?<br><br>
            <b>5.</b> Devorlarga mosmi?<br><br>
            <b>6.</b> Keraksiz opening yo'qmi?<br><br>
            <b>7.</b> 3D va Section tekshirildimi?
            """,
        },
        {
            "title": "Modul yakuni",
            "type": "highlight",
            "text": """
            Siz endi:

            <br><br>

            ✓ Slab Toolni tushunasiz;<br>
            ✓ thickness bilan ishlaysiz;<br>
            ✓ elevationni nazorat qilasiz;<br>
            ✓ slab konturini yaratasiz;<br>
            ✓ konturini tahrirlaysiz;<br>
            ✓ opening tushunchasini bilasiz;<br>
            ✓ slabni 2D va 3Dda tekshirasiz.

            <br><br>

            Keyingi modul:
            <b>Door va Window.</b>
            """,
        },
    ],
}


# ============================================================
# QUIZ
# ============================================================

LEVEL05_MODULE04_QUIZ = {
    "L05_M04_001": [
        {
            "code": "L05_Q046",
            "question": "Archicaddagi Slab faqat 2D Fill hisoblanadimi?",
            "explanation": (
                "Slab qalinlik va balandlikka ega BIM model elementi."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L05_Q047",
            "question": "Slab yaratgandan keyin uni 3Dda tekshirish foydalimi?",
            "explanation": (
                "3D kontur, balandlik va modeldagi joylashuvni tekshirishga yordam beradi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L05_Q048",
            "question": "Slab Tool pol va gorizontal plita geometriyasini yaratishda ishlatilishi mumkinmi?",
            "explanation": (
                "Slab Tool gorizontal BIM elementlarini modellashtirish uchun ishlatiladi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L05_M04_002": [
        {
            "code": "L05_Q049",
            "question": "Slab thickness 3D modelga ta'sir qiladimi?",
            "explanation": (
                "Qalinlik slabning vertikal geometriyasini belgilovchi asosiy parametrlardan biridir."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L05_Q050",
            "question": "Slab elevation noto'g'ri bo'lsa Sectionda xato ko'rinishi mumkinmi?",
            "explanation": (
                "Elevation elementning vertikal joylashuviga ta'sir qiladi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L05_Q051",
            "question": "Real konstruktiv qalinlikni mutaxassis talabisiz tasodifiy tanlash to'g'rimi?",
            "explanation": (
                "Real loyiha konstruktsion qiymatlari tegishli hisob va loyiha talablariga asoslanishi kerak."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
    ],

    "L05_M04_003": [
        {
            "code": "L05_Q052",
            "question": "Slab konturi yopiq geometriya bo'lishi kerakmi?",
            "explanation": (
                "Slab yuzasi yopiq polygon kontur asosida hosil qilinadi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L05_Q053",
            "question": "Slab shakli faqat to'rtburchak bo'lishi shartmi?",
            "explanation": (
                "Bino geometriyasiga qarab murakkab polygon shakllar ham ishlatilishi mumkin."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L05_Q054",
            "question": "Slab konturidagi xatoda butun elementni har safar qayta chizish shartmi?",
            "explanation": (
                "Ko'p holatda kontur nuqtalarini tahrirlash mumkin."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
    ],

    "L05_M04_004": [
        {
            "code": "L05_Q055",
            "question": "Slab ichida opening kerak bo'lishi mumkinmi?",
            "explanation": (
                "Zina, atrium yoki boshqa void kabi vaziyatlarda ochiq hudud talab qilinishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L05_Q056",
            "question": "Slab openingni ham 3Dda tekshirish foydalimi?",
            "explanation": (
                "3D opening haqiqatan modelda hosil bo'lganini tushunishga yordam beradi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L05_Q057",
            "question": "Keraksiz juda ko'p polygon node yaratish model boshqaruvini qiyinlashtirishi mumkinmi?",
            "explanation": (
                "Aniq va soddaroq geometriya odatda boshqarishni osonlashtiradi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L05_M04_005": [
        {
            "code": "L05_Q058",
            "question": "Slabni Floor Plan bilan birga Sectionda ham tekshirish kerakmi?",
            "explanation": (
                "Section vertikal joylashuv va qalinlikni tushunishga yordam beradi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L05_Q059",
            "question": "Slab konturi devorlar bilan mantiqiy mos kelishi muhimmi?",
            "explanation": (
                "Uy modelida slab va devor geometriyasi birgalikda nazorat qilinadi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L05_Q060",
            "question": "Slab Tool bilan ishlashdagi to'g'ri workflow qaysi?",
            "explanation": (
                "Parametr, kontur va 2D/3D nazorat birgalikda ishlatiladi."
            ),
            "options": [
                (
                    "A",
                    "Tool → parametr → kontur → 2D/3D tekshiruv",
                    True,
                ),
                (
                    "B",
                    "Tasodifiy polygon → tekshirmaslik",
                    False,
                ),
            ],
        },
    ],
}


# ============================================================
# DATABASE SEED
# ============================================================

def seed_level05_module04():
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
        ) in LEVEL05_MODULE04_LESSONS:

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
