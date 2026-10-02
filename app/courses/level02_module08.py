from database.database import get_connection


# ============================================================
# LEVEL 2
# MODULE 08 - SANUZEL ERGONOMIKASI
# ============================================================

LEVEL02_MODULE08_LESSONS = [
    (
        "L02_M08",
        "L02_M08_001",
        "Sanuzel funksiyasi va jihozlari",
        "theory",
        "Sanuzeldagi asosiy sanitar jihozlar va ularning vazifalarini tushunish.",
        1,
        45,
        20,
    ),
    (
        "L02_M08",
        "L02_M08_002",
        "Foydalanish zonalari",
        "theory",
        "WC, rakovina, dush va boshqa jihozlar atrofidagi foydalanish hududlarini tushunish.",
        2,
        45,
        20,
    ),
    (
        "L02_M08",
        "L02_M08_003",
        "Wet va dry zoning",
        "practice",
        "Sanuzelda nam va quruq zonalarni mantiqiy tashkil qilish.",
        3,
        50,
        20,
    ),
    (
        "L02_M08",
        "L02_M08_004",
        "Eshik, privacy va circulation",
        "practice",
        "Sanuzel kirishi, eshik ochilishi va ichki harakatni qulay tashkil qilish.",
        4,
        50,
        20,
    ),
    (
        "L02_M08",
        "L02_M08_005",
        "Sanuzel auditi",
        "practice",
        "Sanuzel rejasini ergonomika, privacy, jihozlar va circulation bo'yicha tekshirish.",
        5,
        50,
        25,
    ),
]


# ============================================================
# CONTENT
# ============================================================

LEVEL02_MODULE08_CONTENT = {
    "L02_M08_001": [
        {
            "title": "Sanuzel — kichik, lekin murakkab makon",
            "type": "highlight",
            "text": """
            Sanuzel ko'pincha
            uy ichidagi kichik xonalardan biri.

            <br><br>

            Lekin unda ko'p
            funksiyalar juda yaqin
            joylashadi.

            <br><br>

            Shu sabab sanuzel
            aniq rejalashtirishni talab qiladi.
            """,
        },
        {
            "title": "Asosiy jihozlar",
            "type": "normal",
            "text": """
            Sanuzelda loyiha vazifasiga qarab:

            <br><br>

            • WC;<br>
            • rakovina;<br>
            • dush;<br>
            • vanna;<br>
            • bidet;<br>
            • storage;<br>
            • kir yuvish jihozi

            <br><br>

            mavjud bo'lishi mumkin.
            """,
        },
        {
            "title": "Har bir jihozning o'z funksiyasi bor",
            "type": "highlight",
            "text": """
            Jihozlarni faqat
            devor bo'ylab ketma-ket
            qo'yish yetarli emas.

            <br><br>

            Har bir jihozdan
            odam real foydalanishini
            tasavvur qilish kerak.
            """,
        },
        {
            "title": "Tasavvur qiling",
            "type": "example",
            "text": """
            WC,
            rakovina
            va dush

            <br><br>

            kichik xonaga sig'di.

            <br><br>

            Lekin dushdan chiqqanda
            WC oldida harakat qilish
            juda qiyin.

            <br><br>

            Jihozlar sig'di,
            ammo ergonomika yomon.
            """,
        },
        {
            "title": "Mini-vazifa",
            "type": "example",
            "text": """
            Oddiy sanuzel sxemasini chizing.

            <br><br>

            Unda belgilang:

            <br><br>

            • WC;<br>
            • lavabo;<br>
            • dush;<br>
            • eshik.

            <br><br>

            Keyin odam harakatini
            strelka bilan ko'rsating.
            """,
        },
    ],

    "L02_M08_002": [
        {
            "title": "Jihoz konturi yetarli emas",
            "type": "highlight",
            "text": """
            Sanitar jihoz
            faqat o'z fizik o'lchamini
            egallamaydi.

            <br><br>

            Odam undan foydalanishi uchun
            oldida yoki yonida
            kerakli bo'sh zona bo'ladi.
            """,
        },
        {
            "title": "WC foydalanish zonasi",
            "type": "normal",
            "text": """
            WC joylashtirilganda
            odamning o'tirishi,
            turishi
            va oldinga harakat qilishi
            hisobga olinadi.
            """,
        },
        {
            "title": "Rakovina zonasi",
            "type": "normal",
            "text": """
            Rakovina oldida
            odam turadi.

            <br><br>

            Shu sabab rakovina
            boshqa jihoz yoki eshik bilan
            haddan tashqari yaqin bo'lmasligi kerak.
            """,
        },
        {
            "title": "Dush va vanna",
            "type": "normal",
            "text": """
            Dush yoki vannaga:

            <br><br>

            • kirish;<br>
            • chiqish;<br>
            • foydalanish;<br>
            • qurinish

            <br><br>

            uchun real harakat zonasi kerak.
            """,
        },
        {
            "title": "Jihozlar bir-biriga xalaqit bermasin",
            "type": "warning",
            "text": """
            Rakovina oldida turgan odam
            eshik ochilishiga to'sqinlik qilsa

            <br><br>

            yoki dush eshigi
            WCga urilsa,

            <br><br>

            reja ergonomik emas.
            """,
        },
        {
            "title": "Qulay masofa tushunchasi",
            "type": "highlight",
            "text": """
            Bu bosqichda maqsad
            raqamlarni yodlash emas.

            <br><br>

            Maqsad —
            har bir jihoz atrofida
            odam harakati va foydalanish
            uchun yetarli joy kerakligini
            tushunish.
            """,
        },
        {
            "title": "Mini-vazifa",
            "type": "example",
            "text": """
            WC,
            rakovina
            va dush atrofida

            <br><br>

            shartli foydalanish zonalarini
            alohida kontur bilan chizing.

            <br><br>

            Ular bir-biriga
            juda kuchli kirib ketayaptimi?
            """,
        },
    ],

    "L02_M08_003": [
        {
            "title": "Wet va dry zona",
            "type": "highlight",
            "text": """
            Sanuzelda
            namlik darajasi
            hamma joyda bir xil emas.

            <br><br>

            Shu sabab makonni
            shartli ravishda:

            <br><br>

            <b>WET</b>

            <br><br>

            va

            <br><br>

            <b>DRY</b>

            <br><br>

            zonalarga ajratib
            fikrlash mumkin.
            """,
        },
        {
            "title": "Wet zona",
            "type": "normal",
            "text": """
            Dush va vanna atrofida
            suv bilan bevosita aloqa
            ko'proq bo'ladi.

            <br><br>

            Bu zona nam zona
            sifatida ko'rib chiqiladi.
            """,
        },
        {
            "title": "Dry zona",
            "type": "normal",
            "text": """
            Kirish,
            storage
            yoki ayrim rakovina atrofi

            <br><br>

            nisbatan quruq
            foydalanish zonasi bo'lishi mumkin.
            """,
        },
        {
            "title": "Dushdan chiqish yo'li",
            "type": "example",
            "text": """
            Dushdan chiqayotgan odam
            to'g'ridan-to'g'ri
            WC yoki shkafga urilmasligi kerak.

            <br><br>

            Dush oldida
            real foydalanish va chiqish
            zonasi bo'lishi kerak.
            """,
        },
        {
            "title": "Namlikni tarqatmang",
            "type": "warning",
            "text": """
            Dush zonasi
            sanuzel ichidagi
            barcha harakat yo'lini
            nam qiladigan holatda bo'lsa,

            <br><br>

            foydalanish noqulaylashishi mumkin.
            """,
        },
        {
            "title": "Storage joylashuvi",
            "type": "normal",
            "text": """
            Sochiq,
            gigiyena buyumlari
            va boshqa storage

            <br><br>

            suv bilan bevosita
            to'qnashmaydigan
            mantiqiy joyda bo'lishi foydali.
            """,
        },
        {
            "title": "Mini-vazifa",
            "type": "example",
            "text": """
            Sanuzel planida:

            <br><br>

            qizil bilan WET zonani,
            boshqa rang bilan DRY zonani
            belgilang.

            <br><br>

            Ularning orasidagi
            harakatni tahlil qiling.
            """,
        },
    ],

    "L02_M08_004": [
        {
            "title": "Sanuzel kirishi",
            "type": "highlight",
            "text": """
            Sanuzelga kirish
            faqat eshik joylashtirish
            masalasi emas.

            <br><br>

            Privacy,
            foydalanish
            va circulation ham
            hisobga olinadi.
            """,
        },
        {
            "title": "Eshik ochilishi",
            "type": "normal",
            "text": """
            Door swing:

            <br><br>

            • WCga urilmasin;<br>
            • rakovinani yopmasin;<br>
            • dushga kirishni to'smasin;<br>
            • odam harakatini buzmasin.
            """,
        },
        {
            "title": "Privacy",
            "type": "highlight",
            "text": """
            Sanuzel eshigi
            public makonga ochilganda
            ichki qism to'g'ridan-to'g'ri
            ko'rinib qolmasligi ma'qul.
            """,
        },
        {
            "title": "Tasavvur qiling",
            "type": "example",
            "text": """
            Sanuzel eshigi
            livingga ochiladi.

            <br><br>

            Eshik ochilishi bilan
            WC to'g'ridan-to'g'ri ko'rinadi.

            <br><br>

            Bu privacy
            nuqtai nazaridan
            yaxshi yechim emas.
            """,
        },
        {
            "title": "Ichki circulation",
            "type": "normal",
            "text": """
            Sanuzel kichik bo'lsa ham,
            odam:

            <br><br>

            kirish →
            rakovina →
            WC →
            dush

            <br><br>

            kabi harakatlarni
            ortiqcha to'qnashuvsiz
            bajara olishi kerak.
            """,
        },
        {
            "title": "Ikki kishi foydalanishi",
            "type": "normal",
            "text": """
            Kattaroq sanuzelda
            bir vaqtning o'zida
            ikki kishi foydalanishi mumkin.

            <br><br>

            Masalan biri rakovinada,
            boshqasi dush zonasida.

            <br><br>

            Bunday holatni ham
            tasavvur qilib ko'ring.
            """,
        },
        {
            "title": "Mini-vazifa",
            "type": "example",
            "text": """
            Sanuzel planida
            eshikning 2 xil ochilish
            variantini chizing.

            <br><br>

            Qaysi variant
            jihozlar bilan kamroq
            konflikt qilayotganini
            solishtiring.
            """,
        },
    ],

    "L02_M08_005": [
        {
            "title": "Sanuzel auditi",
            "type": "highlight",
            "text": """
            Endi sanuzelni
            jihozlar sig'ishi bo'yicha emas,

            <br><br>

            real foydalanish
            va ergonomika bo'yicha
            tekshiramiz.
            """,
        },
        {
            "title": "1. Jihozlar",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • WC mantiqiy joydami?<br>
            • rakovinadan foydalanish qulaymi?<br>
            • dush/vannaga kirish mumkinmi?<br>
            • storage kerakli joydami?
            """,
        },
        {
            "title": "2. Foydalanish zonalari",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • jihozlar oldida joy bormi?<br>
            • odam erkin tura oladimi?<br>
            • jihozlar bir-biriga urilmayaptimi?
            """,
        },
        {
            "title": "3. Wet / dry zoning",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • dush zonasi mantiqiymi?<br>
            • kirish doim nam bo'lib qolmayaptimi?<br>
            • storage wet zonaga kirib ketmaganmi?
            """,
        },
        {
            "title": "4. Privacy va eshik",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • eshik jihozlarga urilmayaptimi?<br>
            • ichki qism public zonadan ochiq ko'rinmayaptimi?<br>
            • kirish va chiqish qulaymi?
            """,
        },
        {
            "title": "Xatoni toping",
            "type": "warning",
            "text": """
            Sanuzelda:

            <br><br>

            WC,
            rakovina,
            dush,
            kir yuvish mashinasi

            <br><br>

            hammasi sig'di.

            <br><br>

            Lekin eshik ochilganda
            rakovinaga uriladi.

            <br><br>

            Dushdan chiqqanda esa
            odam to'g'ridan-to'g'ri
            WCga yaqin tushadi.

            <br><br>

            Xulosa:

            <br><br>

            <b>
            Jihozlar sig'ishi
            yaxshi ergonomika degani emas.
            </b>
            """,
        },
        {
            "title": "Professional checklist",
            "type": "example",
            "text": """
            Sanuzelni tekshiring:

            <br><br>

            <b>1.</b> Jihozlar mantiqiy joylashganmi?<br><br>
            <b>2.</b> Foydalanish zonalari yetarlimi?<br><br>
            <b>3.</b> Door conflict yo'qmi?<br><br>
            <b>4.</b> Wet va dry zonalar tushunarlimi?<br><br>
            <b>5.</b> Circulation ochiqmi?<br><br>
            <b>6.</b> Privacy saqlanganmi?<br><br>
            <b>7.</b> Storage mantiqiy joydami?
            """,
        },
        {
            "title": "Modul yakuni",
            "type": "highlight",
            "text": """
            Siz endi:

            <br><br>

            ✓ asosiy sanitar jihozlarni tushunasiz;<br>
            ✓ foydalanish zonalarini hisobga olasiz;<br>
            ✓ wet va dry zoningni tushunasiz;<br>
            ✓ eshik conflictlarini tekshirasiz;<br>
            ✓ privacy haqida o'ylaysiz;<br>
            ✓ circulationni tahlil qilasiz;<br>
            ✓ sanuzel auditini bajarasiz.

            <br><br>

            Keyingi modul:
            <b>Koridor va kirish.</b>
            """,
        },
    ],
}


# ============================================================
# QUIZ
# Q106-Q120 KODLARI SAQLANADI
# ============================================================

LEVEL02_MODULE08_QUIZ = {
    "L02_M08_001": [
        {
            "code": "L02_Q106",
            "question": "Sanuzelda jihozlarning faqat xonaga sig'ishi yetarlimi?",
            "explanation": (
                "Jihozlardan real foydalanish va circulation ham tekshirilishi kerak."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L02_Q107",
            "question": "WC, rakovina va dush sanuzeldagi asosiy jihozlar bo'lishi mumkinmi?",
            "explanation": (
                "Sanuzel tarkibi loyiha vazifasiga qarab shu kabi sanitar jihozlardan iborat bo'lishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L02_Q108",
            "question": "Sanuzel kichik bo'lsa ham ergonomika muhimmi?",
            "explanation": (
                "Kichik makonda jihozlar yaqin joylashgani sabab ergonomik rejalashtirish ayniqsa muhim."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L02_M08_002": [
        {
            "code": "L02_Q109",
            "question": "Sanitar jihoz atrofida foydalanish zonasi kerakmi?",
            "explanation": (
                "Odam jihozdan foydalanishi uchun uning atrofida bo'sh joy kerak."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L02_Q110",
            "question": "Rakovina oldida odam turadigan joy hisobga olinadimi?",
            "explanation": (
                "Rakovinadan real foydalanish uchun oldida foydalanish hududi kerak."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L02_Q111",
            "question": "Jihozlarning konturlari bir-biriga sig'sa foydalanish zonalarini tekshirmasa ham bo'ladimi?",
            "explanation": (
                "Jihoz konturi va real foydalanish maydoni bir xil tushuncha emas."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
    ],

    "L02_M08_003": [
        {
            "code": "L02_Q112",
            "question": "Dush atrofi wet zona hisoblanishi mumkinmi?",
            "explanation": (
                "Dush atrofida suv bilan to'g'ridan-to'g'ri aloqa ko'proq bo'ladi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L02_Q113",
            "question": "Wet va dry zoning sanuzel funksiyasini tushunishga yordam beradimi?",
            "explanation": (
                "Nam va quruq faoliyatlarni ajratib fikrlash rejalashtirishni yaxshilaydi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L02_Q114",
            "question": "Storage doim dushning eng nam qismida joylashishi kerakmi?",
            "explanation": (
                "Storage suv bilan bevosita konflikt qilmaydigan mantiqiy joyda bo'lishi ma'qul."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
    ],

    "L02_M08_004": [
        {
            "code": "L02_Q115",
            "question": "Sanuzel eshigi sanitar jihoz bilan konflikt qilishi mumkinmi?",
            "explanation": (
                "Door swing rakovina, WC yoki boshqa element bilan to'qnashishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L02_Q116",
            "question": "Sanuzel kirishida privacy hisobga olinadimi?",
            "explanation": (
                "Eshik ochilganda ichki private zona public makondan qanday ko'rinishi ham tahlil qilinadi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L02_Q117",
            "question": "Kichik sanuzelda circulationni tekshirish shart emasmi?",
            "explanation": (
                "Kichik makonda ham odam jihozlar orasida qulay harakatlana olishi kerak."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
    ],

    "L02_M08_005": [
        {
            "code": "L02_Q118",
            "question": "Sanuzel auditida eshik, jihozlar va circulation birgalikda tekshiriladimi?",
            "explanation": (
                "Ularning o'zaro aloqasi sanuzel ergonomikasiga bevosita ta'sir qiladi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L02_Q119",
            "question": "Barcha jihozlar sig'gan sanuzel avtomatik ravishda qulay bo'ladimi?",
            "explanation": (
                "Foydalanish zonalari, privacy, eshik va circulation ham tekshiriladi."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L02_Q120",
            "question": "Sanuzel loyihalashdagi to'g'ri yondashuv qaysi?",
            "explanation": (
                "Jihozlar, foydalanish zonalari, wet/dry zoning, privacy va circulation birgalikda ko'riladi."
            ),
            "options": [
                (
                    "A",
                    "Jihozlar → foydalanish zonasi → wet/dry → circulation → audit",
                    True,
                ),
                (
                    "B",
                    "Faqat barcha jihozlarni xonaga sig'dirish",
                    False,
                ),
            ],
        },
    ],
}


# ============================================================
# DATABASE SEED
# ============================================================

def seed_level02_module08():
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
        ) in LEVEL02_MODULE08_LESSONS:

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
