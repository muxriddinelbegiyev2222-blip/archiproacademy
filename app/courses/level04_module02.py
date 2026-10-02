from database.database import get_connection


# ============================================================
# LEVEL 4
# MODULE 02 - MEHMON KUTISH MADANIYATI
# ============================================================

LEVEL04_MODULE02_LESSONS = [
    (
        "L04_M02",
        "L04_M02_001",
        "Mehmon oqimini tushunish",
        "theory",
        "Mehmonning darvozadan mehmonxonagacha bo'lgan harakatini rejalashtirish.",
        1,
        40,
        20,
    ),
    (
        "L04_M02",
        "L04_M02_002",
        "Mehmonxona joylashuvi",
        "theory",
        "Mehmonxonani kirish, dining va private zonalarga nisbatan to'g'ri joylashtirish.",
        2,
        40,
        20,
    ),
    (
        "L04_M02",
        "L04_M02_003",
        "Guest WC va dining aloqasi",
        "theory",
        "Mehmon sanuzeli va ovqatlanish zonasini qulay tashkil qilish.",
        3,
        40,
        20,
    ),
    (
        "L04_M02",
        "L04_M02_004",
        "Mehmon va family privacy",
        "practice",
        "Mehmon circulationini oilaning private hayotidan ajratish.",
        4,
        45,
        20,
    ),
    (
        "L04_M02",
        "L04_M02_005",
        "Mehmon zonasi auditi",
        "practice",
        "Mehmon kutish bilan bog'liq tipik rejalash xatolarini aniqlash.",
        5,
        55,
        25,
    ),
]


# ============================================================
# CONTENT
# ============================================================

LEVEL04_MODULE02_CONTENT = {
    "L04_M02_001": [
        {
            "title": "Mehmon oqimi darvozadan boshlanadi",
            "type": "highlight",
            "text": """
            Mehmon kutish faqat
            mehmonxona ichida boshlanmaydi.

            <br><br>

            Mehmonning tajribasi:

            <br><br>

            <b>
            ko'cha → darvoza → kirish →
            foyye → mehmonxona
            </b>

            <br><br>

            ketma-ketligidan boshlanadi.
            """,
        },
        {
            "title": "Mehmon nimani tushunishi kerak?",
            "type": "normal",
            "text": """
            Mehmon:

            <br><br>

            • qayerdan kirishni;<br>
            • qaysi eshik asosiy ekanini;<br>
            • qayerda kutishni;<br>
            • qayerga o'tishni

            <br><br>

            osongina tushunishi kerak.
            """,
        },
        {
            "title": "Tasavvur qiling",
            "type": "example",
            "text": """
            Mehmon uyga kirdi.

            <br><br>

            Oldida uchta yo'lak:

            <br><br>

            biri yotoqxonalarga,
            biri oshxonaga,
            biri mehmonxonaga.

            <br><br>

            Qaysi yo'nalish asosiy ekani
            tushunarsiz.

            <br><br>

            Bu circulation muammosi.
            """,
        },
        {
            "title": "Kirish va mehmonxona aloqasi",
            "type": "highlight",
            "text": """
            Mehmonxona
            asosiy kirishga nisbatan
            mantiqiy va tushunarli joylashishi foydali.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Bir uy planini oling.

            <br><br>

            Mehmonning yo'lini chizing:

            <br><br>

            DARVOZA → ESHIK → MEHMONXONA

            <br><br>

            Yo'l qayerda ortiqcha uzayadi?
            """,
        },
    ],

    "L04_M02_002": [
        {
            "title": "Mehmonxona public zonaning yuragi",
            "type": "highlight",
            "text": """
            Mehmonxona
            tashqi mehmon oqimi bilan
            oilaning ichki hayoti o'rtasidagi
            asosiy public makon bo'lishi mumkin.
            """,
        },
        {
            "title": "Kirishga yaqinlik",
            "type": "normal",
            "text": """
            Mehmonxona kirishga nisbatan
            tushunarli joylashsa,

            <br><br>

            mehmon private zonaga
            chuqur kirishga majbur bo'lmaydi.
            """,
        },
        {
            "title": "Dining bilan aloqa",
            "type": "normal",
            "text": """
            Mehmon kutishda ovqatlanish muhim bo'lsa,

            <br><br>

            mehmonxona va dining
            o'rtasidagi aloqa ham
            oldindan o'ylanishi kerak.
            """,
        },
        {
            "title": "Mehmonxona va hovli",
            "type": "example",
            "text": """
            Ba'zi loyihalarda
            mehmonxona tashqi guest hovli,
            terassa yoki ayvon bilan bog'lanishi mumkin.

            <br><br>

            Bu ichki va tashqi mehmon makonini
            birlashtiradi.
            """,
        },
        {
            "title": "Family living bilan bir xilmi?",
            "type": "warning",
            "text": """
            Mehmonxona va family living
            har doim bir xil xona bo'lishi shart emas.

            <br><br>

            Oilaning turmush tarziga qarab
            ular alohida yoki birlashtirilgan bo'lishi mumkin.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Ikki variant tuzing:

            <br><br>

            1. Alohida mehmonxona<br>
            2. Mehmon + family living birga

            <br><br>

            Har birining
            afzallik va kamchiligini yozing.
            """,
        },
    ],

    "L04_M02_003": [
        {
            "title": "Guest WC kichik, lekin muhim",
            "type": "highlight",
            "text": """
            Mehmon uchun sanuzel
            rejaning kichik qismi bo'lishi mumkin,

            <br><br>

            lekin noto'g'ri joylashsa
            private zonani buzishi mumkin.
            """,
        },
        {
            "title": "Guest WC qayerda?",
            "type": "normal",
            "text": """
            Guest WC odatda:

            <br><br>

            • public zonaga yaqin;<br>
            • tushunarli;<br>
            • private yotoqxonalardan ajratilgan

            <br><br>

            bo'lishi foydali.
            """,
        },
        {
            "title": "Noto'g'ri misol",
            "type": "warning",
            "text": """
            Mehmon sanuzelga borish uchun
            bolalar xonasi va master bedroom
            oldidan o'tadi.

            <br><br>

            Bu public-private zonalashni zaiflashtiradi.
            """,
        },
        {
            "title": "Dining",
            "type": "normal",
            "text": """
            Dining mehmonxona bilan
            juda uzoq bo'lsa,

            <br><br>

            mehmon kutish jarayonida
            keraksiz circulation paydo bo'lishi mumkin.
            """,
        },
        {
            "title": "Kitchen va dining",
            "type": "example",
            "text": """
            Dining oshxonaga yaqin,
            lekin oshxonaning barcha ishchi jarayoni
            mehmon ko'z o'ngida bo'lishi shart emas.

            <br><br>

            Funksiya va vizual nazorat
            muvozanatda bo'lishi mumkin.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Plan ustida uchta nuqta belgilang:

            <br><br>

            MEHMONXONA<br>
            DINING<br>
            GUEST WC

            <br><br>

            Ular orasidagi yo'llarni chizing.
            """,
        },
    ],

    "L04_M02_004": [
        {
            "title": "Mehmon va oila bir uyda, lekin bir xil hududda emas",
            "type": "highlight",
            "text": """
            Kuchli reja
            mehmon kutishga imkon beradi,

            <br><br>

            shu bilan birga
            oilaning kundalik hayotini ham himoya qiladi.
            """,
        },
        {
            "title": "Private koridor",
            "type": "normal",
            "text": """
            Yotoqxona koridori
            mehmon circulationining
            asosiy qismiga aylanmasligi kerak.
            """,
        },
        {
            "title": "Family room",
            "type": "example",
            "text": """
            Mehmonlar mehmonxonada o'tirganda
            oila boshqa family room yoki
            private livingdan foydalanishi mumkin.

            <br><br>

            Bu katta oilalarda qulay bo'lishi mumkin.
            """,
        },
        {
            "title": "Bolalar privacy",
            "type": "normal",
            "text": """
            Mehmonlar kelganda
            bolalar xonasi oldidan
            doimiy o'tish bo'lsa,

            <br><br>

            bolalarning private zonasi zaiflashadi.
            """,
        },
        {
            "title": "Vizual privacy",
            "type": "warning",
            "text": """
            Mehmon kirish eshigidan
            to'g'ridan-to'g'ri
            private family zonasini ko'rsa,

            <br><br>

            vizual privacy yo'qolishi mumkin.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Planda:

            <br><br>

            qizil rang — GUEST<br>
            ko'k rang — FAMILY

            <br><br>

            circulation chizing.

            <br><br>

            Kesishgan joylarni belgilang.
            """,
        },
    ],

    "L04_M02_005": [
        {
            "title": "Mehmon zonasini audit qilamiz",
            "type": "highlight",
            "text": """
            Endi mehmon kutish tizimini
            bitta xona sifatida emas,
            to'liq ssenariy sifatida tekshiramiz.
            """,
        },
        {
            "title": "Xato 1 — mehmon yo'li private zonada",
            "type": "warning",
            "text": """
            Mehmonxona yaxshi.

            <br><br>

            Lekin unga borish uchun
            yotoqxona koridoridan o'tish kerak.
            """,
        },
        {
            "title": "Xato 2 — guest WC yo'q",
            "type": "warning",
            "text": """
            Mehmonlar family bathroomdan
            foydalanishga majbur.

            <br><br>

            Bu private zonaga keraksiz kirishni oshiradi.
            """,
        },
        {
            "title": "Xato 3 — dining juda uzoq",
            "type": "warning",
            "text": """
            Mehmonxonadan dininggacha
            uzoq va murakkab yo'l mavjud.
            """,
        },
        {
            "title": "Xato 4 — kirish tushunarsiz",
            "type": "warning",
            "text": """
            Mehmon asosiy eshikdan kirgach
            qaysi tomonga yurishni
            tushunmaydi.
            """,
        },
        {
            "title": "Xato 5 — family hayoti ochilib qolgan",
            "type": "warning",
            "text": """
            Mehmonxona yoki foyyedan
            oilaning private living,
            oshxona ishchi qismi
            yoki yotoqxona zonasi
            to'liq ko'rinadi.
            """,
        },
        {
            "title": "Professional checklist",
            "type": "example",
            "text": """
            Mehmon zonasini tekshiring:

            <br><br>

            <b>1.</b> Darvozadan kirish tushunarlimi?<br><br>
            <b>2.</b> Mehmonxona qayerda?<br><br>
            <b>3.</b> Guest WC qulaymi?<br><br>
            <b>4.</b> Diningga yo'l qisqami?<br><br>
            <b>5.</b> Private zona himoyalanganmi?<br><br>
            <b>6.</b> Family circulation buzilmayaptimi?<br><br>
            <b>7.</b> Mehmon chiqishi tushunarlimi?
            """,
        },
        {
            "title": "Mini-case",
            "type": "example",
            "text": """
            Oila haftada bir marta
            8–10 kishilik mehmon qabul qiladi.

            <br><br>

            Talab:

            <br><br>

            • alohida mehmonxona;<br>
            • 8–10 kishilik dining;<br>
            • guest WC;<br>
            • tashqi ayvon bilan aloqa;<br>
            • family private zonasi.

            <br><br>

            Bubble diagram yarating.

            <br><br>

            GUEST va FAMILY oqimlarini
            alohida ko'rsating.
            """,
        },
        {
            "title": "Modul yakuni",
            "type": "highlight",
            "text": """
            Siz endi:

            <br><br>

            ✓ mehmon oqimini yaratish;<br>
            ✓ mehmonxonani joylashtirish;<br>
            ✓ guest WC aloqasi;<br>
            ✓ dining circulation;<br>
            ✓ family privacy;<br>
            ✓ guest zone audit

            <br><br>

            ko'nikmalariga ega bo'ldingiz.

            <br><br>

            Keyingi modul:
            <b>Ichki hovli.</b>
            """,
        },
    ],
}


# ============================================================
# QUIZ
# ============================================================

LEVEL04_MODULE02_QUIZ = {
    "L04_M02_001": [
        {
            "code": "L04_Q016",
            "question": "Mehmon circulationi faqat mehmonxona ichidan boshlanadimi?",
            "explanation": (
                "Mehmon tajribasi ko'cha va darvozadan boshlab shakllanadi."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L04_Q017",
            "question": "Mehmon asosiy kirishni oson topishi kerakmi?",
            "explanation": (
                "Tushunarli entrance sequence mehmon circulationining muhim qismidir."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L04_Q018",
            "question": "Mehmon yo'li private zonadan o'tmasa yaxshi bo'lishi mumkinmi?",
            "explanation": (
                "Bu family privacyni himoya qilishga yordam beradi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L04_M02_002": [
        {
            "code": "L04_Q019",
            "question": "Mehmonxonaning kirishga aloqasi muhimmi?",
            "explanation": (
                "Mehmon private zonaga chuqur kirmasdan public zonaga o'tishi foydali."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L04_Q020",
            "question": "Mehmonxona va dining o'rtasidagi aloqa mehmon kutishda muhim bo'lishi mumkinmi?",
            "explanation": (
                "Ovqatlanish va mehmon kutish funksiyalari ko'pincha bog'liq."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L04_Q021",
            "question": "Mehmonxona va family living har doim alohida bo'lishi shartmi?",
            "explanation": (
                "Bu oilaning ehtiyoji va uy maydoniga bog'liq."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
    ],

    "L04_M02_003": [
        {
            "code": "L04_Q022",
            "question": "Guest WC public zonaga qulay joylashishi foydalimi?",
            "explanation": (
                "Mehmon private zonaga kirmasdan foydalanishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L04_Q023",
            "question": "Mehmon sanuzelga borishda master bedroom oldidan o'tishi yaxshi zonalashmi?",
            "explanation": (
                "Bu private zonani buzishi mumkin."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L04_Q024",
            "question": "Diningning oshxona bilan aloqasi ham muhimmi?",
            "explanation": (
                "Ovqat tayyorlash va xizmat ko'rsatish jarayoni uchun bu muhim."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L04_M02_004": [
        {
            "code": "L04_Q025",
            "question": "Mehmon va family circulationi bir-biriga ta'sir qiladimi?",
            "explanation": (
                "Oqimlarning kesishishi privacy va kundalik qulaylikka ta'sir qiladi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L04_Q026",
            "question": "Mehmon kirishidan private family zona to'liq ko'rinishi privacy muammosi bo'lishi mumkinmi?",
            "explanation": (
                "Vizual privacy ham rejalashning bir qismi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L04_Q027",
            "question": "Yotoqxona koridori guest circulationning asosiy yo'li bo'lishi kerakmi?",
            "explanation": (
                "Yotoqxona koridori private zona sifatida himoyalanishi foydali."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
    ],

    "L04_M02_005": [
        {
            "code": "L04_Q028",
            "question": "Mehmon zonasini faqat mehmonxona maydoni bilan baholash yetarlimi?",
            "explanation": (
                "Kirish, WC, dining, privacy va circulation ham birgalikda tekshiriladi."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L04_Q029",
            "question": "Guest WC yo'qligi private circulationni oshirishi mumkinmi?",
            "explanation": (
                "Mehmon family bathroomga o'tishi kerak bo'lishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L04_Q030",
            "question": "Mehmon zonasi auditidagi asosiy savollardan biri qaysi?",
            "explanation": (
                "Mehmon oqimi va family privacy o'rtasidagi munosabat tekshiriladi."
            ),
            "options": [
                ("A", "Private zona himoyalanganmi?", True),
                ("B", "Faqat tomning rangi qanday?", False),
            ],
        },
    ],
}


# ============================================================
# DATABASE SEED
# ============================================================

def seed_level04_module02():
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
        ) in LEVEL04_MODULE02_LESSONS:

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
