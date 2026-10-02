from database.database import get_connection


# ============================================================
# LEVEL 2
# MODULE 07 - YOTOQXONA, GARDEROB VA SANUZEL ERGONOMIKASI
# ============================================================

LEVEL02_MODULE07_LESSONS = [
    (
        "L02_M07",
        "L02_M07_001",
        "Yotoqxona ergonomikasi",
        "theory",
        "Krovat, yurish zonasi va mebel aloqalari asosida qulay yotoqxona yaratish.",
        1,
        35,
        20,
    ),
    (
        "L02_M07",
        "L02_M07_002",
        "Garderob va kiyim saqlash",
        "theory",
        "Shkaf va garderobni real foydalanish zonasi bilan loyihalash.",
        2,
        35,
        20,
    ),
    (
        "L02_M07",
        "L02_M07_003",
        "Master bedroom tizimi",
        "theory",
        "Yotoqxona, garderob va private sanuzel o'rtasidagi aloqani tushunish.",
        3,
        40,
        20,
    ),
    (
        "L02_M07",
        "L02_M07_004",
        "Sanuzel ergonomikasi",
        "practice",
        "Unitaz, rakovina, dush yoki vanna atrofidagi foydalanish zonalarini tahlil qilish.",
        4,
        40,
        20,
    ),
    (
        "L02_M07",
        "L02_M07_005",
        "Yotoqxona va sanuzel xatolarini topish",
        "practice",
        "Real turar joy planlaridagi private zona ergonomik xatolarini aniqlash.",
        5,
        45,
        25,
    ),
]


# ============================================================
# CONTENT
# ============================================================

LEVEL02_MODULE07_CONTENT = {
    "L02_M07_001": [
        {
            "title": "Yotoqxona faqat krovat emas",
            "type": "highlight",
            "text": """
            Yotoqxonada krovat sig'ishi yetarli emas.

            <br><br>

            Odam:

            <br><br>

            • xonaga kiradi;<br>
            • krovatga yaqinlashadi;<br>
            • kiyim almashtiradi;<br>
            • shkaf ochadi;<br>
            • tumba ishlatadi;<br>
            • derazaga yaqinlashadi.

            <br><br>

            Bularning barchasi joy talab qiladi.
            """,
        },
        {
            "title": "Krovat markaziy element",
            "type": "example",
            "text": """
            Ko'p yotoqxonalarda krovat
            asosiy funksional element hisoblanadi.

            <br><br>

            Uni joylashtirganda faqat
            o'lchamiga emas,

            <br><br>

            atrofidagi yurish zonalariga ham qaraladi.
            """,
        },
        {
            "title": "Ikki tomondan foydalanish",
            "type": "normal",
            "text": """
            Ikki kishilik krovat bo'lsa,
            imkon qadar ikki tomondan foydalanish
            qulay bo'lishi mumkin.

            <br><br>

            Bu ayniqsa ota-ona yotoqxonasida muhim.
            """,
        },
        {
            "title": "Krovat va eshik",
            "type": "warning",
            "text": """
            Eshik ochilganda
            to'g'ridan-to'g'ri krovatga urilsa
            yoki yurish yo'lini to'ssa,

            <br><br>

            ergonomik muammo paydo bo'ladi.
            """,
        },
        {
            "title": "Krovat va deraza",
            "type": "normal",
            "text": """
            Deraza joylashuvi ham:

            <br><br>

            • krovat bosh qismi;<br>
            • pardalar;<br>
            • radiator;<br>
            • tabiiy yorug'lik;<br>
            • maxfiylik

            <br><br>

            bilan birga tekshiriladi.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Bir master bedroom planini toping.

            <br><br>

            Tekshiring:

            <br><br>

            1. Krovatga ikki tomondan borish mumkinmi?<br>
            2. Shkaf ochiladimi?<br>
            3. Eshik krovatga xalaqit beradimi?<br>
            4. Deraza bilan mebel to'qnashadimi?
            """,
        },
    ],

    "L02_M07_002": [
        {
            "title": "Shkafning o'zi yetmaydi",
            "type": "highlight",
            "text": """
            Shkaf xonaga sig'di degani
            undan qulay foydalanish mumkin degani emas.

            <br><br>

            Uning oldida odam turishi
            va eshigini ochishi uchun joy kerak.
            """,
        },
        {
            "title": "Oddiy shkaf",
            "type": "example",
            "text": """
            Devor bo'ylab shkaf qo'yildi.

            <br><br>

            Lekin krovat bilan shkaf orasida
            juda tor masofa qoldi.

            <br><br>

            Shkaf eshigi ochilganda
            yo'l butunlay yopiladi.

            <br><br>

            Bu noto'g'ri ergonomika.
            """,
        },
        {
            "title": "Walk-in garderob",
            "type": "normal",
            "text": """
            Walk-in garderobda:

            <br><br>

            • kiyim saqlash yuzasi;<br>
            • yurish yo'li;<br>
            • shkaf ochilishi;<br>
            • kiyim almashtirish

            <br><br>

            birgalikda ko'rib chiqiladi.
            """,
        },
        {
            "title": "Ko'p shkaf = yaxshi emas",
            "type": "warning",
            "text": """
            Juda ko'p shkaf qo'yib,
            odam yuradigan joyni qisqartirish
            yaxshi loyiha emas.

            <br><br>

            Saqlash sig'imi va qulaylik
            balansda bo'lishi kerak.
            """,
        },
        {
            "title": "Garderobning joylashuvi",
            "type": "example",
            "text": """
            Master bedroom ichida garderob
            sanuzel va yotoq qismi orasida
            tampon sifatida ishlashi mumkin.

            <br><br>

            Lekin bu yagona to'g'ri yechim emas.

            <br><br>

            Asosiy narsa — kundalik foydalanish mantiqi.
            """,
        },
    ],

    "L02_M07_003": [
        {
            "title": "Master suite",
            "type": "highlight",
            "text": """
            Master bedroom tizimi
            faqat katta yotoqxona emas.

            <br><br>

            U ko'pincha:

            <br><br>

            <b>
            yotoqxona + garderob + private sanuzel
            </b>

            <br><br>

            aloqasidan tashkil topadi.
            """,
        },
        {
            "title": "Aloqa variantlari",
            "type": "normal",
            "text": """
            Masalan:

            <br><br>

            yotoqxona → garderob → sanuzel

            <br><br>

            yoki

            <br><br>

            yotoqxona → alohida garderob<br>
            yotoqxona → alohida sanuzel

            <br><br>

            kabi sxemalar bo'lishi mumkin.
            """,
        },
        {
            "title": "Qaysi biri yaxshi?",
            "type": "example",
            "text": """
            Universal bitta javob yo'q.

            <br><br>

            Oilaning:

            <br><br>

            • odati;<br>
            • uyg'onish vaqti;<br>
            • kiyinish tartibi;<br>
            • maxfiylik talabi

            <br><br>

            yechimga ta'sir qiladi.
            """,
        },
        {
            "title": "Tungi foydalanish",
            "type": "normal",
            "text": """
            Kechasi sanuzelga borish uchun
            butun uy bo'ylab yurish kerak bo'lmasligi
            qulaylikni oshiradi.

            <br><br>

            Private circulation ayniqsa
            master zonada muhim.
            """,
        },
        {
            "title": "Xato",
            "type": "warning",
            "text": """
            Private sanuzel mavjud.

            <br><br>

            Lekin unga kirish uchun
            krovat atrofini aylanib,
            tor garderob yo'lidan o'tish kerak.

            <br><br>

            Xonalar mavjud,
            lekin aloqa yomon.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            3 xil master suite planini toping.

            <br><br>

            Har birida:

            <br><br>

            • yotoq;<br>
            • garderob;<br>
            • sanuzel

            <br><br>

            o'rtasidagi yo'lni solishtiring.
            """,
        },
    ],

    "L02_M07_004": [
        {
            "title": "Sanuzel — kichik, lekin murakkab makon",
            "type": "highlight",
            "text": """
            Sanuzel ko'pincha kichik maydonda
            ko'p funksiyani bajaradi.

            <br><br>

            Shu sababli har bir elementning
            foydalanish zonasi muhim.
            """,
        },
        {
            "title": "Asosiy elementlar",
            "type": "normal",
            "text": """
            Sanuzelda:

            <br><br>

            • unitaz;<br>
            • rakovina;<br>
            • dush;<br>
            • vanna;<br>
            • saqlash;<br>
            • kir yuvish jihozi

            <br><br>

            kabi elementlar bo'lishi mumkin.
            """,
        },
        {
            "title": "Eshik ochilishi",
            "type": "warning",
            "text": """
            Eshik ichkariga ochilib,
            unitaz yoki rakovinaga urilsa,
            real foydalanishda muammo bo'ladi.

            <br><br>

            Eshik radiusi doimo tekshiriladi.
            """,
        },
        {
            "title": "Dush oldidagi zona",
            "type": "example",
            "text": """
            Dush kabinasi planda sig'di.

            <br><br>

            Lekin eshigini ochish
            va undan chiqish uchun joy qolmadi.

            <br><br>

            Demak element konturi yetarli emas.
            """,
        },
        {
            "title": "Rakovina va harakat",
            "type": "normal",
            "text": """
            Rakovina oldida odam turadi.

            <br><br>

            Agar shu joy asosiy eshik
            yoki boshqa element bilan kesishsa,
            ikki odam bir vaqtda foydalana olmaydi.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Kichik sanuzel planini toping.

            <br><br>

            Har bir elementning oldida
            real foydalanish zonasini tasavvur qiling.

            <br><br>

            Qayerda to'qnashuv bor?
            """,
        },
    ],

    "L02_M07_005": [
        {
            "title": "Private zona xatolarini ovlaymiz",
            "type": "highlight",
            "text": """
            Endi yotoqxona, garderob va sanuzelni
            bitta tizim sifatida tekshiramiz.
            """,
        },
        {
            "title": "Xato 1 — krovat shkafni to'sadi",
            "type": "warning",
            "text": """
            Krovat xonaga yaxshi sig'gan.

            <br><br>

            Lekin shkaf eshiklari
            to'liq ochilmaydi.

            <br><br>

            Bu mebel zonalari to'qnashuvi.
            """,
        },
        {
            "title": "Xato 2 — eshik krovatga uriladi",
            "type": "warning",
            "text": """
            Yotoqxona eshigi ochilganda
            krovat burchagiga tegadi.

            <br><br>

            Eshik va mebel birgalikda
            tekshirilmagan.
            """,
        },
        {
            "title": "Xato 3 — garderob juda tor",
            "type": "warning",
            "text": """
            Ikki tomonda shkaf bor.

            <br><br>

            Lekin o'rtadagi yo'l juda tor.

            <br><br>

            Natijada bir odamning o'zi ham
            qulay foydalana olmaydi.
            """,
        },
        {
            "title": "Xato 4 — sanuzel eshigi konflikt yaratadi",
            "type": "warning",
            "text": """
            Sanuzel eshigi ichkariga ochilib,
            unitazga uriladi.

            <br><br>

            Planda barcha elementlar bor,
            lekin real foydalanish ishlamaydi.
            """,
        },
        {
            "title": "Xato 5 — private circulation uzun",
            "type": "warning",
            "text": """
            Krovatdan sanuzelga borish uchun
            garderobni aylanib,
            uzun yo'lakdan yurish kerak.

            <br><br>

            Private zonaning aloqasi
            qayta ko'rib chiqiladi.
            """,
        },
        {
            "title": "Professional tahlil",
            "type": "example",
            "text": """
            Master zonani tekshirganda:

            <br><br>

            <b>1.</b> Krovatga qanday boriladi?<br><br>
            <b>2.</b> Krovat atrofida yurish mumkinmi?<br><br>
            <b>3.</b> Shkaflar to'liq ochiladimi?<br><br>
            <b>4.</b> Garderob yo'li qulaymi?<br><br>
            <b>5.</b> Sanuzel eshigi to'qnashadimi?<br><br>
            <b>6.</b> Tungi yo'l qisqa va tushunarlimi?
            """,
        },
        {
            "title": "Mini-loyiha",
            "type": "example",
            "text": """
            20–30 m² umumiy master zona toping.

            <br><br>

            Yotoqxona + garderob + sanuzelni tahlil qiling.

            <br><br>

            Kamida:

            <br><br>

            • 3 ta yaxshi qaror;<br>
            • 2 ta ergonomik xato yoki yaxshilash nuqtasi

            <br><br>

            yozing.
            """,
        },
        {
            "title": "Modul yakuni",
            "type": "highlight",
            "text": """
            Siz endi:

            <br><br>

            ✓ yotoqxona ergonomikasi;<br>
            ✓ krovat atrofidagi yurish;<br>
            ✓ garderob foydalanish zonasi;<br>
            ✓ master suite aloqasi;<br>
            ✓ sanuzel ergonomikasi;<br>
            ✓ private circulation

            <br><br>

            bo'yicha plan tahlil qila olasiz.

            <br><br>

            Keyingi modul:
            <b>Mehmonxona va family room ergonomikasi.</b>
            """,
        },
    ],
}


# ============================================================
# QUIZ
# ============================================================

LEVEL02_MODULE07_QUIZ = {
    "L02_M07_001": [
        {
            "code": "L02_Q091",
            "question": "Yotoqxonada krovatning faqat sig'ishi yetarlimi?",
            "explanation": (
                "Krovat atrofida yurish va boshqa mebellardan foydalanish uchun ham joy kerak."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L02_Q092",
            "question": "Ikki kishilik krovatga ikki tomondan kirish qulay bo'lishi mumkinmi?",
            "explanation": (
                "Bu ikki foydalanuvchi uchun qulay harakat yaratishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L02_Q093",
            "question": "Yotoqxona eshigi krovatga urilishi ergonomik muammomi?",
            "explanation": (
                "Eshik va mebelning foydalanish zonalari to'qnashmoqda."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L02_M07_002": [
        {
            "code": "L02_Q094",
            "question": "Shkaf oldida foydalanish zonasi kerakmi?",
            "explanation": (
                "Shkaf eshigini ochish va kiyim olish uchun oldida makon kerak."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L02_Q095",
            "question": "Ko'p shkaf har doim yaxshi garderob deganimi?",
            "explanation": (
                "Saqlash sig'imi bilan yurish va foydalanish qulayligi balansda bo'lishi kerak."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L02_Q096",
            "question": "Walk-in garderobda yurish yo'li ham hisobga olinadimi?",
            "explanation": (
                "Garderob faqat shkaflardan emas, foydalanish va harakat zonasidan ham iborat."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L02_M07_003": [
        {
            "code": "L02_Q097",
            "question": "Master suite tarkibiga nimalar kirishi mumkin?",
            "explanation": (
                "Yotoqxona, garderob va private sanuzel master tizimining qismlari bo'lishi mumkin."
            ),
            "options": [
                ("A", "Yotoqxona, garderob, sanuzel", True),
                ("B", "Faqat mehmonxona", False),
            ],
        },
        {
            "code": "L02_Q098",
            "question": "Master suite uchun faqat bitta universal sxema bormi?",
            "explanation": (
                "Yechim oilaning hayot tarzi va ehtiyojiga qarab o'zgaradi."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L02_Q099",
            "question": "Tungi private circulation muhimmi?",
            "explanation": (
                "Yotoqxona va sanuzel o'rtasidagi qisqa va qulay aloqa tungi foydalanishda muhim."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L02_M07_004": [
        {
            "code": "L02_Q100",
            "question": "Sanuzel eshigi unitazga urilsa bu xatomi?",
            "explanation": (
                "Eshik radiusi va jihozlarning foydalanish zonasi to'qnashmoqda."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L02_Q101",
            "question": "Dushning faqat planga sig'ishi yetarlimi?",
            "explanation": (
                "Dushga kirish, chiqish va eshik ochilishi uchun ham joy kerak."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L02_Q102",
            "question": "Rakovina oldida odam turadigan zona hisobga olinadimi?",
            "explanation": (
                "Sanuzeldagi har bir elementning foydalanish zonasi mavjud."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L02_M07_005": [
        {
            "code": "L02_Q103",
            "question": "Krovat shkaf eshiklarini to'ssa bu qanday muammo?",
            "explanation": (
                "Mebel foydalanish zonalari bir-biriga to'qnashgan."
            ),
            "options": [
                ("A", "Ergonomik muammo", True),
                ("B", "Har doim yaxshi yechim", False),
            ],
        },
        {
            "code": "L02_Q104",
            "question": "Garderobdagi juda tor yurish yo'li foydalanishni qiyinlashtirishi mumkinmi?",
            "explanation": (
                "Shkaflardan foydalanish va odam harakati uchun yetarli joy kerak."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L02_Q105",
            "question": "Master zona tahlilida qaysi savol foydali?",
            "explanation": (
                "Yotoq, garderob va sanuzel orasidagi real harakatni tekshirish kerak."
            ),
            "options": [
                ("A", "Tungi harakat yo'li qulaymi?", True),
                ("B", "Faqat fasad qaysi rangda?", False),
            ],
        },
    ],
}


# ============================================================
# DATABASE SEED
# ============================================================

def seed_level02_module07():
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
        ) in LEVEL02_MODULE07_LESSONS:

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
