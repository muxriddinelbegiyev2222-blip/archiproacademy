from database.database import get_connection


# ============================================================
# LEVEL 4
# MODULE 05 - YOZGI OSHXONA
# ============================================================

LEVEL04_MODULE05_LESSONS = [
    (
        "L04_M05",
        "L04_M05_001",
        "Yozgi oshxona nima?",
        "theory",
        "Yozgi oshxonaning turar joy va hovli tizimidagi vazifasini tushunish.",
        1,
        40,
        20,
    ),
    (
        "L04_M05",
        "L04_M05_002",
        "Asosiy oshxona bilan aloqa",
        "theory",
        "Ichki oshxona va yozgi oshxona o'rtasidagi funksional bog'lanishni rejalashtirish.",
        2,
        40,
        20,
    ),
    (
        "L04_M05",
        "L04_M05_003",
        "Mangal, tutun va tashqi dining",
        "theory",
        "Ovqat tayyorlash, mangal va tashqi ovqatlanish zonalarini to'g'ri tashkil qilish.",
        3,
        45,
        20,
    ),
    (
        "L04_M05",
        "L04_M05_004",
        "Suv, saqlash va service",
        "practice",
        "Yozgi oshxonadagi suv, mahsulot saqlash va xo'jalik harakatlarini rejalashtirish.",
        4,
        45,
        20,
    ),
    (
        "L04_M05",
        "L04_M05_005",
        "Yozgi oshxona auditi",
        "practice",
        "Yozgi oshxonadagi tipik funksional va circulation xatolarini aniqlash.",
        5,
        55,
        25,
    ),
]


# ============================================================
# CONTENT
# ============================================================

LEVEL04_MODULE05_CONTENT = {
    "L04_M05_001": [
        {
            "title": "Yozgi oshxona — hovlining faol funksiyasi",
            "type": "highlight",
            "text": """
            Yozgi oshxona
            shunchaki tashqaridagi plita emas.

            <br><br>

            U:

            <br><br>

            • ovqat tayyorlash;<br>
            • katta mehmon uchun xizmat;<br>
            • mangal;<br>
            • tashqi dining;<br>
            • mahsulot tayyorlash;<br>
            • kundalik yozgi foydalanish

            <br><br>

            bilan bog'liq bo'lishi mumkin.
            """,
        },
        {
            "title": "Nega alohida yozgi oshxona kerak bo'lishi mumkin?",
            "type": "normal",
            "text": """
            Issiq mavsumda:

            <br><br>

            • ichki uyga kamroq issiqlik kirishi;<br>
            • kuchli hidlarni tashqarida ushlash;<br>
            • katta hajmda ovqat tayyorlash;<br>
            • mehmon kutishni osonlashtirish

            <br><br>

            uchun yozgi oshxona foydali bo'lishi mumkin.
            """,
        },
        {
            "title": "Tasavvur qiling",
            "type": "example",
            "text": """
            Oilada katta mehmon yig'ildi.

            <br><br>

            Mangal tashqarida,
            dining boshqa burchakda,
            suv esa faqat ichki oshxonada.

            <br><br>

            Har safar idish va mahsulot
            uy ichidan tashqariga olib chiqiladi.

            <br><br>

            Bu ishlaydi,
            lekin qulay emas.
            """,
        },
        {
            "title": "Asosiy prinsip",
            "type": "highlight",
            "text": """
            Yozgi oshxona
            alohida obyekt emas.

            <br><br>

            U:

            <br><br>

            <b>
            uy + hovli + dining + service
            </b>

            <br><br>

            tizimining bir qismi.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Bir yozgi oshxona uchun
            kamida 8 ta funksiyani yozing.

            <br><br>

            Faqat plita bilan cheklanib qolmang.
            """,
        },
    ],

    "L04_M05_002": [
        {
            "title": "Ikki oshxona bir-biridan uzilmasin",
            "type": "highlight",
            "text": """
            Ichki oshxona va yozgi oshxona
            bir-biriga nisbatan
            mantiqiy joylashishi kerak.
            """,
        },
        {
            "title": "Qisqa aloqa",
            "type": "normal",
            "text": """
            Tekshiring:

            <br><br>

            • mahsulot qayerdan keladi;<br>
            • idish qayerdan olinadi;<br>
            • suv qayerda;<br>
            • dining qayerda;<br>
            • chiqindi qayerga olib chiqiladi.
            """,
        },
        {
            "title": "Noto'g'ri aloqa",
            "type": "warning",
            "text": """
            Ichki oshxona uyning bir tomonida,
            yozgi oshxona esa uchastkaning
            eng uzoq burchagida.

            <br><br>

            Har bir mahsulot uchun
            uzun yo'l bosiladi.
            """,
        },
        {
            "title": "Service door",
            "type": "example",
            "text": """
            Ba'zi loyihalarda
            oshxonadan hovliga alohida
            service chiqish foydali bo'lishi mumkin.

            <br><br>

            Bu tashqi ovqatlanish bilan
            aloqani qisqartiradi.
            """,
        },
        {
            "title": "Yozgi oshxona living yo'lini to'smasin",
            "type": "normal",
            "text": """
            Service harakati
            family living va
            dam olish zonasini
            doim kesib o'tmasligi foydali.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Chizing:

            <br><br>

            ICHKI OSHXONA → YOZGI OSHXONA → DINING

            <br><br>

            Keyin alohida:

            <br><br>

            STORAGE → YOZGI OSHXONA → CHIQINDI

            <br><br>

            yo'lini ko'rsating.
            """,
        },
    ],

    "L04_M05_003": [
        {
            "title": "Mangal zonasi alohida tahlil qilinadi",
            "type": "highlight",
            "text": """
            Mangal yoki grill zonasi
            faqat chiroyli dekor emas.

            <br><br>

            Unda issiqlik,
            tutun,
            ishchi joy
            va xavfsizlik bor.
            """,
        },
        {
            "title": "Tutun yo'nalishi",
            "type": "normal",
            "text": """
            Mangal tutuni:

            <br><br>

            • living oynasiga;<br>
            • terassaga;<br>
            • qo'shni tomonga;<br>
            • asosiy kirishga

            <br><br>

            doimiy tushib qolmasligi kerak.
            """,
        },
        {
            "title": "Mangal va dining",
            "type": "example",
            "text": """
            Mangal diningga yaqin bo'lsa,
            ovqat uzatish qulay.

            <br><br>

            Lekin juda yaqin bo'lsa,
            issiqlik va tutun noqulaylik tug'dirishi mumkin.
            """,
        },
        {
            "title": "Ishchi zona",
            "type": "normal",
            "text": """
            Ovqat tayyorlash uchun:

            <br><br>

            • stol yoki countertop;<br>
            • suv;<br>
            • mahsulot qo'yish joyi;<br>
            • idish;<br>
            • chiqindi

            <br><br>

            kerak bo'lishi mumkin.
            """,
        },
        {
            "title": "Xavfsizlik",
            "type": "warning",
            "text": """
            Ochiq olovli zona
            odamlarning asosiy yurish yo'liga
            juda yaqin joylashtirilmasligi kerak.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Mangal zonasida:

            <br><br>

            • grill;<br>
            • ishchi stol;<br>
            • suv;<br>
            • dining;<br>
            • odam harakati

            <br><br>

            ni joylashtiring.
            """,
        },
    ],

    "L04_M05_004": [
        {
            "title": "Yozgi oshxona service tizimidir",
            "type": "highlight",
            "text": """
            Yozgi oshxona
            yaxshi ishlashi uchun
            faqat pishirish uskunasi yetarli emas.
            """,
        },
        {
            "title": "Suv",
            "type": "normal",
            "text": """
            Suv nuqtasi:

            <br><br>

            • mahsulot yuvish;<br>
            • idish yuvish;<br>
            • tozalash

            <br><br>

            uchun muhim bo'lishi mumkin.
            """,
        },
        {
            "title": "Saqlash",
            "type": "normal",
            "text": """
            Yozgi oshxonada:

            <br><br>

            • idish;<br>
            • ziravor;<br>
            • servis buyumlari;<br>
            • quruq mahsulot

            <br><br>

            uchun saqlash joyi kerak bo'lishi mumkin.
            """,
        },
        {
            "title": "Chiqindi yo'li",
            "type": "example",
            "text": """
            Ovqat tayyorlash ko'p chiqindi yaratadi.

            <br><br>

            Chiqindi tashish yo'li
            dining va mehmonlar orasidan
            o'tmasligi foydali.
            """,
        },
        {
            "title": "Mahsulot kirishi",
            "type": "normal",
            "text": """
            Parking yoki service kirishidan
            mahsulotni yozgi oshxonaga
            olib kirish yo'li ham tahlil qilinadi.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            4 ta service oqim chizing:

            <br><br>

            • mahsulot;<br>
            • suv;<br>
            • idish;<br>
            • chiqindi.

            <br><br>

            Qayerda ular mehmon oqimi bilan kesishadi?
            """,
        },
    ],

    "L04_M05_005": [
        {
            "title": "Yozgi oshxona auditini boshlaymiz",
            "type": "highlight",
            "text": """
            Endi yozgi oshxonani
            real foydalanish ssenariysi bilan
            tekshiramiz.
            """,
        },
        {
            "title": "Xato 1 — asosiy oshxonadan juda uzoq",
            "type": "warning",
            "text": """
            Har bir mahsulot,
            idish yoki servis buyumi uchun
            uzoq masofa bosiladi.
            """,
        },
        {
            "title": "Xato 2 — tutun livingga ketadi",
            "type": "warning",
            "text": """
            Mangal tutuni
            living va terassa tomon
            doimiy yo'naladi.
            """,
        },
        {
            "title": "Xato 3 — suv yo'q",
            "type": "warning",
            "text": """
            Pishirish joyi tashqarida,
            lekin barcha yuvish ishlari
            ichki oshxonada bajariladi.
            """,
        },
        {
            "title": "Xato 4 — chiqindi mehmonlar orasidan o'tadi",
            "type": "warning",
            "text": """
            Service harakati
            guest diningni doim kesib o'tadi.
            """,
        },
        {
            "title": "Xato 5 — mangal asosiy yurish yo'lida",
            "type": "warning",
            "text": """
            Ochiq olov zonasi
            odamlar ko'p yuradigan yo'lga
            juda yaqin joylashtirilgan.
            """,
        },
        {
            "title": "Professional checklist",
            "type": "example",
            "text": """
            Yozgi oshxonani tekshiring:

            <br><br>

            <b>1.</b> Asosiy oshxonaga aloqasi qanday?<br><br>
            <b>2.</b> Diningga aloqasi qulaymi?<br><br>
            <b>3.</b> Suv bormi?<br><br>
            <b>4.</b> Ishchi stol bormi?<br><br>
            <b>5.</b> Saqlash joyi bormi?<br><br>
            <b>6.</b> Tutun qayerga ketadi?<br><br>
            <b>7.</b> Chiqindi qanday chiqariladi?
            """,
        },
        {
            "title": "Mini-case",
            "type": "example",
            "text": """
            Talab:

            <br><br>

            • 10 kishilik tashqi dining;<br>
            • mangal;<br>
            • ishchi stol;<br>
            • rakovina;<br>
            • saqlash;<br>
            • ichki oshxona bilan qisqa aloqa;<br>
            • service yo'li.

            <br><br>

            Yozgi oshxona + dining
            sxemasini yarating.
            """,
        },
        {
            "title": "Modul yakuni",
            "type": "highlight",
            "text": """
            Siz endi:

            <br><br>

            ✓ yozgi oshxona funksiyasini tushunish;<br>
            ✓ ichki oshxona bilan bog'lash;<br>
            ✓ mangal va diningni rejalash;<br>
            ✓ tutunni hisobga olish;<br>
            ✓ suv va saqlashni rejalash;<br>
            ✓ service circulationni boshqarish

            <br><br>

            ko'nikmalariga ega bo'ldingiz.

            <br><br>

            Keyingi modul:
            <b>Banja va yordamchi bino.</b>
            """,
        },
    ],
}


# ============================================================
# QUIZ
# ============================================================

LEVEL04_MODULE05_QUIZ = {
    "L04_M05_001": [
        {
            "code": "L04_Q061",
            "question": "Yozgi oshxona faqat tashqaridagi plitadan iboratmi?",
            "explanation": (
                "U pishirish, dining, service va hovli bilan bog'liq to'liq funksional zona bo'lishi mumkin."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L04_Q062",
            "question": "Yozgi oshxona katta mehmon kutishda foydali bo'lishi mumkinmi?",
            "explanation": (
                "Katta hajmda ovqat tayyorlash va tashqi diningni qo'llab-quvvatlashi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L04_Q063",
            "question": "Yozgi oshxona hovli va service tizimidan ajratib rejalashtiriladimi?",
            "explanation": (
                "U uy, hovli, dining va service bilan birga ishlashi kerak."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
    ],

    "L04_M05_002": [
        {
            "code": "L04_Q064",
            "question": "Ichki va yozgi oshxona orasidagi masofa kundalik qulaylikka ta'sir qiladimi?",
            "explanation": (
                "Mahsulot, idish va servis harakati uchun qisqa aloqa foydali."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L04_Q065",
            "question": "Service chiqish yozgi oshxona bilan aloqani yaxshilashi mumkinmi?",
            "explanation": (
                "U ichki oshxonadan tashqi ovqatlanish zonasiga to'g'ridan-to'g'ri xizmat qilishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L04_Q066",
            "question": "Service oqimi doim family livingni kesib o'tishi kerakmi?",
            "explanation": (
                "Imkon qadar service harakati yashash zonasini bezovta qilmasligi foydali."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
    ],

    "L04_M05_003": [
        {
            "code": "L04_Q067",
            "question": "Mangal joylashuvida tutun yo'nalishi hisobga olinadimi?",
            "explanation": (
                "Tutun living, dining yoki qo'shni zonaga doimiy tushmasligi kerak."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L04_Q068",
            "question": "Mangal diningga qanchalik yaqinligi muhimmi?",
            "explanation": (
                "Juda uzoq joy xizmatni qiyinlashtiradi, juda yaqin joy esa issiqlik va tutun muammosi yaratishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L04_Q069",
            "question": "Ochiq olov zonasi asosiy yurish yo'liga juda yaqin bo'lishi xavf tug'dirishi mumkinmi?",
            "explanation": (
                "Mangal va grill zonalarida harakat va xavfsizlik alohida tekshiriladi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L04_M05_004": [
        {
            "code": "L04_Q070",
            "question": "Yozgi oshxonada suv nuqtasi foydalimi?",
            "explanation": (
                "Mahsulot, idish va tozalash ishlari uchun suv muhim."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L04_Q071",
            "question": "Saqlash joyi yozgi oshxona funksiyasiga kiradimi?",
            "explanation": (
                "Idish va servis buyumlarini joyida saqlash foydalanishni yengillashtiradi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L04_Q072",
            "question": "Chiqindi yo'lining guest dining orqali o'tishi yaxshi service yechimimi?",
            "explanation": (
                "Service harakati mehmon zonasini kamroq bezovta qilishi kerak."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
    ],

    "L04_M05_005": [
        {
            "code": "L04_Q073",
            "question": "Yozgi oshxona asosiy oshxonadan juda uzoq bo'lsa bu muammo bo'lishi mumkinmi?",
            "explanation": (
                "Mahsulot va idish tashish masofasi ortadi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L04_Q074",
            "question": "Tutunning living tomon ketishi yozgi oshxona xatosi bo'lishi mumkinmi?",
            "explanation": (
                "Tutun yashash sifatiga salbiy ta'sir qilishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L04_Q075",
            "question": "Yozgi oshxona auditidagi muhim savollardan biri qaysi?",
            "explanation": (
                "Asosiy oshxona, dining, suv, tutun va service harakati birgalikda tekshiriladi."
            ),
            "options": [
                ("A", "Asosiy oshxona bilan aloqasi qanday?", True),
                ("B", "Faqat tom rangi qanday?", False),
            ],
        },
    ],
}


# ============================================================
# DATABASE SEED
# ============================================================

def seed_level04_module05():
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
        ) in LEVEL04_MODULE05_LESSONS:

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
