from database.database import get_connection


# ============================================================
# LEVEL 2
# MODULE 05 - PUBLIC VA PRIVATE MAKONLAR
# ============================================================

LEVEL02_MODULE05_LESSONS = [
    (
        "L02_M05",
        "L02_M05_001",
        "Public va private makonlarning chuqur tahlili",
        "theory",
        "Uy ichidagi umumiy va shaxsiy hududlarni professional darajada ajratish.",
        1,
        35,
        20,
    ),
    (
        "L02_M05",
        "L02_M05_002",
        "Mehmonlar oqimi va maxfiylik",
        "theory",
        "Mehmon harakatini oilaning private hayotidan ajratib tashkil qilish.",
        2,
        35,
        20,
    ),
    (
        "L02_M05",
        "L02_M05_003",
        "Ota-ona va bolalar zonasi",
        "theory",
        "Oilaviy private zonani yosh, qulaylik va tungi foydalanish asosida tashkil qilish.",
        3,
        40,
        20,
    ),
    (
        "L02_M05",
        "L02_M05_004",
        "Kunduzgi va tungi zonalar",
        "practice",
        "Uy funksiyalarini vaqt bo'yicha tahlil qilish va to'g'ri guruhlash.",
        4,
        40,
        20,
    ),
    (
        "L02_M05",
        "L02_M05_005",
        "Public-private xatolarini topish",
        "practice",
        "Bir qavatli uy planlarida maxfiylik va mehmon oqimi xatolarini aniqlash.",
        5,
        45,
        25,
    ),
]


# ============================================================
# LESSON CONTENT
# ============================================================

LEVEL02_MODULE05_CONTENT = {
    "L02_M05_001": [
        {
            "title": "Public va private faqat nom emas",
            "type": "highlight",
            "text": """
            Public va private zonalarni ajratish
            faqat xonalarni ikki guruhga bo'lish emas.

            <br><br>

            Muhim savol:

            <br><br>

            <b>
            Kim qayergacha erkin kira oladi?
            </b>
            """,
        },
        {
            "title": "Public makon",
            "type": "normal",
            "text": """
            Public makonlar ko'pincha:

            <br><br>

            • kirish;<br>
            • mehmonxona;<br>
            • ovqatlanish zonasi;<br>
            • mehmonlar sanuzeli;<br>
            • umumiy zal

            <br><br>

            kabi xonalardan iborat bo'ladi.
            """,
        },
        {
            "title": "Private makon",
            "type": "normal",
            "text": """
            Private zona ko'pincha:

            <br><br>

            • ota-ona yotoqxonasi;<br>
            • bolalar xonalari;<br>
            • oilaviy sanuzel;<br>
            • garderob;<br>
            • private family lounge

            <br><br>

            kabi makonlardan tashkil topadi.
            """,
        },
        {
            "title": "Chegara qayerda?",
            "type": "example",
            "text": """
            Uyda ko'rinmas chegara bo'lishi mumkin.

            <br><br>

            Masalan:

            <br><br>

            kirish → mehmonxona → ovqatlanish

            <br><br>

            mehmon uchun ochiq.

            <br><br>

            Lekin undan keyingi koridor
            yotoq zonaga olib kirsa,
            bu private hudud hisoblanishi mumkin.
            """,
        },
        {
            "title": "Boshlovchi xatosi",
            "type": "warning",
            "text": """
            Yotoqxonalarni faqat bo'sh joy qolganiga qarab
            joylashtirish noto'g'ri.

            <br><br>

            Private zonaning yaxlitligi muhim.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Bir uy planida
            public va private zonalar orasidagi
            aniq chegarani topishga harakat qiling.

            <br><br>

            Bu chegara qayerda?
            """,
        },
    ],

    "L02_M05_002": [
        {
            "title": "Mehmon qanday yuradi?",
            "type": "highlight",
            "text": """
            Mehmonlar oqimi —
            public-private zonalashning
            eng muhim tekshiruvlaridan biri.
            """,
        },
        {
            "title": "Ideal savol",
            "type": "example",
            "text": """
            Tasavvur qiling:

            <br><br>

            uyga birinchi marta kelgan odam
            eshikdan kirdi.

            <br><br>

            U mehmonxonani osongina topa oladimi?

            <br><br>

            Yoki private xonalar ichiga adashib kiradimi?
            """,
        },
        {
            "title": "Mehmon sanuzeli",
            "type": "normal",
            "text": """
            Mehmon sanuzeli odatda
            public zonadan qulay yetib boriladigan
            joyda bo'lishi foydali.

            <br><br>

            Mehmon oilaning yotoq koridoriga
            kirishga majbur bo'lmasligi kerak.
            """,
        },
        {
            "title": "To'g'ridan-to'g'ri ko'rinish",
            "type": "warning",
            "text": """
            Kirish eshigidan turib
            ota-onalar yotoqxonasi ichini
            to'g'ridan-to'g'ri ko'rish mumkin bo'lsa,
            maxfiylik zaiflashadi.
            """,
        },
        {
            "title": "Mehmon yo'li",
            "type": "example",
            "text": """
            Yaxshi mehmon yo'li ko'pincha:

            <br><br>

            kirish → garderob → mehmonxona → mehmon sanuzeli

            <br><br>

            kabi qisqa va tushunarli tizim bo'lishi mumkin.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Bir plan toping.

            <br><br>

            Mehmonning 3 ta yo'lini chizing:

            <br><br>

            1. Kirish → mehmonxona<br>
            2. Mehmonxona → sanuzel<br>
            3. Mehmonxona → hovli

            <br><br>

            Private zonaga kirish talab qilinadimi?
            """,
        },
    ],

    "L02_M05_003": [
        {
            "title": "Private zonaning ichida ham zonalash bor",
            "type": "highlight",
            "text": """
            Private zona bitta blok bo'lsa ham,
            uning ichida ota-ona va bolalar ehtiyojlari
            turlicha bo'lishi mumkin.
            """,
        },
        {
            "title": "Ota-ona zonasi",
            "type": "normal",
            "text": """
            Master zona tarkibida:

            <br><br>

            • yotoqxona;<br>
            • garderob;<br>
            • private sanuzel;<br>
            • ba'zan ish yoki dam olish burchagi

            <br><br>

            bo'lishi mumkin.
            """,
        },
        {
            "title": "Bolalar zonasi",
            "type": "normal",
            "text": """
            Bolalar xonalari:

            <br><br>

            • ota-onaga yetarlicha yaqin;<br>
            • xavfsiz;<br>
            • sanuzelga qulay;<br>
            • shovqinli public zonadan himoyalangan

            <br><br>

            bo'lishi foydali.
            """,
        },
        {
            "title": "Yosh muhim",
            "type": "example",
            "text": """
            3 yoshli bola bilan
            16 yoshli bolaning private ehtiyoji bir xil emas.

            <br><br>

            Kichik bolaga ota-onaga yaqinlik muhim.

            <br><br>

            Katta bolaga esa ko'proq mustaqillik kerak bo'lishi mumkin.
            """,
        },
        {
            "title": "Xato",
            "type": "warning",
            "text": """
            Bolalar xonasi oshxona yoki mehmonxonaning
            eng shovqinli devoriga bevosita yopishgan bo'lsa,
            dam olish sifati pasayishi mumkin.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            4 kishilik oila uchun:

            <br><br>

            ota-ona + 2 bola

            <br><br>

            private zonani xayolan tuzing.

            <br><br>

            Qaysi xonalar bir-biriga yaqin bo'ladi?
            """,
        },
    ],

    "L02_M05_004": [
        {
            "title": "Uy vaqt bo'yicha ham ishlaydi",
            "type": "highlight",
            "text": """
            Uy faqat makon emas.

            <br><br>

            U ertalab, kunduz va kechasi
            turlicha ishlaydi.
            """,
        },
        {
            "title": "Kunduzgi zona",
            "type": "normal",
            "text": """
            Kunduz faol ishlatiladigan makonlar:

            <br><br>

            • oshxona;<br>
            • ovqatlanish;<br>
            • mehmonxona;<br>
            • hovli bilan aloqa;<br>
            • ish yoki o'qish zonasi

            <br><br>

            bo'lishi mumkin.
            """,
        },
        {
            "title": "Tungi zona",
            "type": "normal",
            "text": """
            Tungi foydalanishga ko'proq bog'liq:

            <br><br>

            • yotoqxonalar;<br>
            • oilaviy sanuzel;<br>
            • garderob;<br>
            • tungi private circulation.
            """,
        },
        {
            "title": "Shovqin masalasi",
            "type": "example",
            "text": """
            Kechasi bolalar uxlayapti.

            <br><br>

            Mehmonxonada esa mehmonlar bor.

            <br><br>

            Agar ikki zona orasida hech qanday
            masofa yoki tampon bo'lmasa,
            shovqin muammo bo'lishi mumkin.
            """,
        },
        {
            "title": "Buffer zona",
            "type": "highlight",
            "text": """
            Ba'zan ikki zona orasida
            garderob, koridor, sanuzel yoki boshqa
            yordamchi xona <b>tampon</b> vazifasini bajaradi.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Bir plan tanlang.

            <br><br>

            Kunduzgi va tungi zonalarni
            ikki rangga ajrating.

            <br><br>

            Ular qayerda to'qnashmoqda?
            """,
        },
    ],

    "L02_M05_005": [
        {
            "title": "Public-private xatolarini ovlaymiz",
            "type": "highlight",
            "text": """
            Endi uy planida
            maxfiylik va odamlar oqimini
            birgalikda tekshiramiz.
            """,
        },
        {
            "title": "Xato 1 — yotoq eshigi mehmonxonaga ochiladi",
            "type": "warning",
            "text": """
            Ota-onalar yotoqxonasining eshigi
            to'g'ridan-to'g'ri mehmonxonaga ochiladi.

            <br><br>

            Private va public chegarasi zaif.
            """,
        },
        {
            "title": "Xato 2 — mehmon sanuzeli private zonada",
            "type": "warning",
            "text": """
            Mehmon sanuzelga borish uchun
            barcha yotoqxona eshiklari oldidan o'tadi.

            <br><br>

            Maxfiylik kamayadi.
            """,
        },
        {
            "title": "Xato 3 — bolalar xonasi shovqin markazida",
            "type": "warning",
            "text": """
            Bolalar xonasi televizor devori,
            oshxona yoki asosiy mehmon zonasi bilan
            bevosita tutashgan.

            <br><br>

            Akustik qulaylik tekshiriladi.
            """,
        },
        {
            "title": "Xato 4 — kirishdan private zona ko'rinadi",
            "type": "warning",
            "text": """
            Uy eshigi ochilishi bilan
            private koridor yoki yotoqxona
            to'g'ridan-to'g'ri ko'rinadi.

            <br><br>

            Vizual maxfiylik zaif.
            """,
        },
        {
            "title": "Xato 5 — tungi yo'l public zonadan o'tadi",
            "type": "warning",
            "text": """
            Yotoqxonadan sanuzelga kechasi borish uchun
            mehmonxona yoki ovqatlanish zonasini
            kesib o'tish kerak.

            <br><br>

            Tungi circulation noto'g'ri bo'lishi mumkin.
            """,
        },
        {
            "title": "Professional tekshiruv",
            "type": "example",
            "text": """
            Plan oldingizda bo'lsa:

            <br><br>

            <b>1.</b> Mehmon qayergacha kiradi?<br><br>
            <b>2.</b> Private zona qayerdan boshlanadi?<br><br>
            <b>3.</b> Mehmon sanuzeli qayerda?<br><br>
            <b>4.</b> Yotoq zonasi shovqindan himoyalanganmi?<br><br>
            <b>5.</b> Tungi yo'llar qulaymi?<br><br>
            <b>6.</b> Kirishdan private makon ko'rinadimi?
            """,
        },
        {
            "title": "Mini-loyiha",
            "type": "example",
            "text": """
            4 kishilik oila uchun
            180–250 m² bir qavatli uy planini toping.

            <br><br>

            Tahlil qiling:

            <br><br>

            • public zona;<br>
            • ota-ona private zonasi;<br>
            • bolalar private zonasi;<br>
            • mehmonlar oqimi;<br>
            • tungi yo'llar.

            <br><br>

            Kamida 3 ta kuchli va
            2 ta zaif nuqtani yozing.
            """,
        },
        {
            "title": "Modul yakuni",
            "type": "highlight",
            "text": """
            Siz endi:

            <br><br>

            ✓ public-private chegarasi;<br>
            ✓ mehmonlar oqimi;<br>
            ✓ vizual maxfiylik;<br>
            ✓ ota-ona zonasi;<br>
            ✓ bolalar zonasi;<br>
            ✓ kunduzgi va tungi zonalar

            <br><br>

            bo'yicha plan tahlil qila olasiz.

            <br><br>

            Keyingi modul:
            <b>Oshxona va ovqatlanish ergonomikasi.</b>
            """,
        },
    ],
}


# ============================================================
# QUIZ DATA
# ============================================================

LEVEL02_MODULE05_QUIZ = {
    "L02_M05_001": [
        {
            "code": "L02_Q061",
            "question": "Public-private zonalashdagi asosiy savollardan biri qaysi?",
            "explanation": (
                "Kim qayergacha erkin kira olishini aniqlash maxfiylikni tashkil qiladi."
            ),
            "options": [
                ("A", "Kim qayergacha kira oladi?", True),
                ("B", "Faqat fasad rangi qanday?", False),
                ("C", "Faqat tom narxi qancha?", False),
            ],
        },
        {
            "code": "L02_Q062",
            "question": "Yotoqxona odatda private zonaga kiradimi?",
            "explanation": (
                "Yotoqxona oilaning shaxsiy makonlaridan biridir."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L02_Q063",
            "question": "Private zonaning yaxlitligi muhimmi?",
            "explanation": (
                "Private xonalarni mantiqiy guruhlash maxfiylik va qulaylikni oshiradi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L02_M05_002": [
        {
            "code": "L02_Q064",
            "question": "Mehmonlar oqimi nimani tekshiradi?",
            "explanation": (
                "Mehmonning uy ichida qayerlardan o'tishini va private zonaga aralashishini."
            ),
            "options": [
                ("A", "Mehmon harakatini", True),
                ("B", "Faqat material rangini", False),
            ],
        },
        {
            "code": "L02_Q065",
            "question": "Mehmon sanuzeli private yotoq koridorining oxirida bo'lishi har doim yaxshi yechimmi?",
            "explanation": (
                "Bu mehmonni private zona ichiga olib kirishi mumkin."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L02_Q066",
            "question": "Kirishdan yotoqxona ichi to'g'ridan-to'g'ri ko'rinishi maxfiylik muammosi bo'lishi mumkinmi?",
            "explanation": (
                "Vizual maxfiylik private zonaning muhim qismidir."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L02_M05_003": [
        {
            "code": "L02_Q067",
            "question": "Kichik bola xonasining ota-onaga yaqin bo'lishi foydali bo'lishi mumkinmi?",
            "explanation": (
                "Yosh bolalarda nazorat va tungi foydalanish nuqtai nazaridan yaqinlik foydali bo'lishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L02_Q068",
            "question": "Ota-ona va bolalar private ehtiyojlari har doim bir xilmi?",
            "explanation": (
                "Yosh, hayot tarzi va mustaqillik darajasiga qarab ehtiyojlar farq qiladi."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L02_Q069",
            "question": "Bolalar xonasini kuchli shovqin manbai yonida joylashtirishni tekshirish kerakmi?",
            "explanation": (
                "Dam olish va uyqu sifati uchun akustik aloqa muhim."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L02_M05_004": [
        {
            "code": "L02_Q070",
            "question": "Uy funksiyalarini kunduzgi va tungi foydalanish bo'yicha tahlil qilish mumkinmi?",
            "explanation": (
                "Uy vaqt davomida turlicha ishlaydi, shuning uchun bunday tahlil foydali."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L02_Q071",
            "question": "Yotoqxonalar tungi zonaga yaqinmi?",
            "explanation": (
                "Yotoqxonalar tungi dam olish funksiyasining asosiy qismidir."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L02_Q072",
            "question": "Koridor yoki garderob ikki shovqinli zona orasida tampon bo'lishi mumkinmi?",
            "explanation": (
                "Yordamchi makonlar ba'zan akustik va funksional tampon vazifasini bajarishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L02_M05_005": [
        {
            "code": "L02_Q073",
            "question": "Yotoqxona eshigining to'g'ridan-to'g'ri mehmonxonaga ochilishi maxfiylikni zaiflashtirishi mumkinmi?",
            "explanation": (
                "Public va private zonalar orasidagi chegara zaiflashadi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L02_Q074",
            "question": "Tungi harakat yo'li public zona ichidan o'tsa muammo bo'lishi mumkinmi?",
            "explanation": (
                "Bu private foydalanish va qulaylikni kamaytirishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L02_Q075",
            "question": "Professional tahlilda qaysi savol foydali?",
            "explanation": (
                "Mehmonning qayergacha kirishini aniqlash public-private chegarani tahlil qiladi."
            ),
            "options": [
                ("A", "Mehmon qayergacha kiradi?", True),
                ("B", "Faqat fasad materiali qaysi?", False),
            ],
        },
    ],
}


# ============================================================
# DATABASE SEED
# ============================================================

def seed_level02_module05():
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
        ) in LEVEL02_MODULE05_LESSONS:

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
