from database.database import get_connection


# ============================================================
# LEVEL 3
# MODULE 04 - UY JOYLASHTIRISH
# ============================================================

LEVEL03_MODULE04_LESSONS = [
    (
        "L03_M04",
        "L03_M04_001",
        "Uyni uchastkaga joylashtirish prinsipi",
        "theory",
        "Uy konturini uchastka sharoitlari asosida joylashtirish.",
        1,
        40,
        20,
    ),
    (
        "L03_M04",
        "L03_M04_002",
        "Old hovli va orqa hovli",
        "theory",
        "Ko'cha tomoni va private hovli o'rtasidagi fazoviy balansni tushunish.",
        2,
        40,
        20,
    ),
    (
        "L03_M04",
        "L03_M04_003",
        "Uy, quyosh va privacy",
        "theory",
        "Binoni orientatsiya va maxfiylik bilan birga joylashtirish.",
        3,
        45,
        20,
    ),
    (
        "L03_M04",
        "L03_M04_004",
        "Uy va parking aloqasi",
        "practice",
        "Avtomobil zonasi, kirish va uy joylashuvini yagona sxemada tahlil qilish.",
        4,
        45,
        20,
    ),
    (
        "L03_M04",
        "L03_M04_005",
        "Uy joylashtirish xatolarini topish",
        "practice",
        "Uchastkada bino joylashtirishdagi tipik fazoviy xatolarni aniqlash.",
        5,
        55,
        25,
    ),
]


# ============================================================
# CONTENT
# ============================================================

LEVEL03_MODULE04_CONTENT = {
    "L03_M04_001": [
        {
            "title": "Uy konturi — eng katta qarorlardan biri",
            "type": "highlight",
            "text": """
            Uyni uchastkaga qayerga qo'yish
            keyingi deyarli barcha qarorlarga ta'sir qiladi.

            <br><br>

            Bino joylashuvi:

            <br><br>

            • hovli hajmi;<br>
            • kirish;<br>
            • parking;<br>
            • quyosh;<br>
            • privacy;<br>
            • manzara;<br>
            • service

            <br><br>

            bilan bog'liq.
            """,
        },
        {
            "title": "Uy markazda bo'lishi shart emas",
            "type": "normal",
            "text": """
            Boshlovchi ko'pincha
            uyni uchastkaning markaziga qo'yadi.

            <br><br>

            Chunki qog'ozda bu balansli ko'rinadi.

            <br><br>

            Lekin real hayotda
            markaziy joylashuv hovlini
            mayda bo'laklarga bo'lib yuborishi mumkin.
            """,
        },
        {
            "title": "Tasavvur qiling",
            "type": "example",
            "text": """
            25 × 40 metr uchastka.

            <br><br>

            Uy aynan markazga qo'yildi.

            <br><br>

            Natijada:

            <br><br>

            old tomonda kichik hovli,
            orqada kichik hovli,
            ikki yon tomonda tor bo'shliqlar paydo bo'ldi.

            <br><br>

            Maydon bor,
            lekin kuchli tashqi makon yo'q.
            """,
        },
        {
            "title": "Uy joylashuvi nimadan boshlanadi?",
            "type": "highlight",
            "text": """
            Avval:

            <br><br>

            <b>
            uchastka → ko'cha → quyosh →
            kirish → hovli → privacy
            </b>

            <br><br>

            keyin bino konturi.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Bir uchastkada uyni
            uch xil variantda joylashtiring:

            <br><br>

            • markazga;<br>
            • old tomonga;<br>
            • yon tomonga yaqin.

            <br><br>

            Har variantda hovli qanday o'zgarishini solishtiring.
            """,
        },
    ],

    "L03_M04_002": [
        {
            "title": "Old hovli va orqa hovli bir xil vazifa emas",
            "type": "highlight",
            "text": """
            Ko'cha tomoni bilan
            private hovli tomoni
            bir xil ishlashi shart emas.
            """,
        },
        {
            "title": "Old hovli",
            "type": "normal",
            "text": """
            Old hovli ko'pincha:

            <br><br>

            • kirish;<br>
            • mehmon kelishi;<br>
            • avtomobil;<br>
            • reprezentativ ko'rinish

            <br><br>

            bilan bog'liq.
            """,
        },
        {
            "title": "Orqa yoki private hovli",
            "type": "normal",
            "text": """
            Private hovli ko'pincha:

            <br><br>

            • dam olish;<br>
            • bolalar o'yini;<br>
            • terassa;<br>
            • family room aloqasi;<br>
            • yozgi ovqatlanish

            <br><br>

            uchun ishlatiladi.
            """,
        },
        {
            "title": "Bino hovlini himoya qilishi mumkin",
            "type": "example",
            "text": """
            Uy ko'cha tomondagi shovqin va ko'rinishni
            qisman to'sib,

            <br><br>

            orqa tomonda tinchroq
            private hovli yaratishi mumkin.
            """,
        },
        {
            "title": "Xato",
            "type": "warning",
            "text": """
            Barcha yaxshi hovli maydoni
            avtomobil va kirish zonasiga berilib,

            <br><br>

            family foydalanish uchun
            juda kam sifatli tashqi makon qolishi mumkin.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Uchastkangizda:

            <br><br>

            FRONT / PUBLIC HOVLI

            va

            PRIVATE / FAMILY HOVLI

            <br><br>

            zonalarini ajrating.
            """,
        },
    ],

    "L03_M04_003": [
        {
            "title": "Uy joylashuvi quyosh bilan birga qaraladi",
            "type": "highlight",
            "text": """
            Bino konturini
            site analysisdan ajratib bo'lmaydi.

            <br><br>

            Oldingi moduldagi
            shimol va quyosh tahlili
            endi real bino joylashuviga ta'sir qiladi.
            """,
        },
        {
            "title": "Living va hovli",
            "type": "example",
            "text": """
            Agar living private hovli bilan
            yaxshi bog'lanishi kerak bo'lsa,

            <br><br>

            bino joylashuvi bu aloqani
            oldindan yaratishi kerak.
            """,
        },
        {
            "title": "Privacy",
            "type": "normal",
            "text": """
            Tekshiring:

            <br><br>

            • qo'shni derazalari qayerda;<br>
            • ko'cha qayerda;<br>
            • private xona oynalari qayerga qaraydi;<br>
            • hovli tashqaridan qanchalik ko'rinadi.
            """,
        },
        {
            "title": "Uy devori buffer sifatida",
            "type": "example",
            "text": """
            Ba'zan uyning o'zi
            noqulay tashqi tomonga
            himoya devori kabi ishlashi mumkin.

            <br><br>

            Service xonalar
            shovqinli yoki kamroq jozibali tomonga,
            living va private xonalar esa
            kuchliroq tomonga yo'naltirilishi mumkin.
            """,
        },
        {
            "title": "Xato",
            "type": "warning",
            "text": """
            Chiroyli katta deraza qo'yildi.

            <br><br>

            Lekin u to'g'ridan-to'g'ri
            qo'shni hovliga yoki ko'chaga ochiladi.

            <br><br>

            Fasad chiroyli,
            privacy esa zaif.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Bitta bino konturi uchun belgilang:

            <br><br>

            • eng yaxshi hovli tomoni;<br>
            • noqulay tashqi tomon;<br>
            • public fasad;<br>
            • private fasad.
            """,
        },
    ],

    "L03_M04_004": [
        {
            "title": "Parking va uy alohida emas",
            "type": "highlight",
            "text": """
            Parking qayerda joylashsa,
            oilaning kundalik kirish yo'li ham
            shunga bog'liq bo'ladi.
            """,
        },
        {
            "title": "Mashina → uy",
            "type": "normal",
            "text": """
            Oila mashinadan tushgach:

            <br><br>

            • asosiy eshikka;<br>
            • side entrance'ga;<br>
            • oshxonaga yaqin kirishga

            <br><br>

            qanday yetishini tahlil qiling.
            """,
        },
        {
            "title": "Mahsulot olib kirish",
            "type": "example",
            "text": """
            Bozordan ko'p mahsulot olib kelindi.

            <br><br>

            Parkingdan oshxonagacha
            butun uy atrofi bo'ylab yurish kerak.

            <br><br>

            Bu kundalik noqulaylik bo'lishi mumkin.
            """,
        },
        {
            "title": "Parking fasadni egallamasin",
            "type": "warning",
            "text": """
            Ba'zi uchastkalarda
            barcha ko'cha fasadi
            mashina va darvozaga aylanib ketadi.

            <br><br>

            Natijada piyoda kirishi va
            uy arxitekturasi ikkinchi darajaga tushadi.
            """,
        },
        {
            "title": "Carport",
            "type": "normal",
            "text": """
            Navес yoki carport
            alohida bino emas,
            umumiy site compositionning
            bir qismi sifatida ko'riladi.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            2 ta avtomobil uchun parking joylashtiring.

            <br><br>

            Keyin:

            <br><br>

            parking → uy kirishi<br>
            parking → oshxona<br>
            parking → ko'cha

            <br><br>

            yo'llarini chizing.
            """,
        },
    ],

    "L03_M04_005": [
        {
            "title": "Uy joylashtirish xatolarini ovlaymiz",
            "type": "highlight",
            "text": """
            Endi bino konturiga
            faqat shakl sifatida emas,
            butun uchastkani boshqaruvchi element
            sifatida qaraymiz.
            """,
        },
        {
            "title": "Xato 1 — uy uchastkani bo'lib tashlagan",
            "type": "warning",
            "text": """
            Uy markazga qo'yilib,
            to'rtta kichik tashqi zona paydo bo'lgan.

            <br><br>

            Hech biri haqiqiy katta hovli sifatida ishlamaydi.
            """,
        },
        {
            "title": "Xato 2 — private hovli ko'chaga ochiq",
            "type": "warning",
            "text": """
            Family terassa va dam olish zonasi
            to'g'ridan-to'g'ri ko'cha tomonda.

            <br><br>

            Privacy zaif.
            """,
        },
        {
            "title": "Xato 3 — living hovlidan uzilgan",
            "type": "warning",
            "text": """
            Eng yaxshi hovli mavjud.

            <br><br>

            Lekin living undan
            uzun koridor va boshqa xona orqali ajralgan.
            """,
        },
        {
            "title": "Xato 4 — parking butun fasadni egallagan",
            "type": "warning",
            "text": """
            Ko'chadan qaralganda
            birinchi ko'rinadigan narsa
            faqat avtomobil va darvoza.

            <br><br>

            Piyoda kirishi va asosiy fasad zaiflashgan.
            """,
        },
        {
            "title": "Xato 5 — orientatsiya unutildi",
            "type": "warning",
            "text": """
            Bino plan jihatdan qulay.

            <br><br>

            Lekin barcha asosiy tashqi makon
            noqulay quyosh tomonga tushib qolgan.
            """,
        },
        {
            "title": "Professional algoritm",
            "type": "example",
            "text": """
            Uy konturini qo'yishda:

            <br><br>

            <b>1.</b> Ko'cha qayerda?<br><br>
            <b>2.</b> Shimol qayerda?<br><br>
            <b>3.</b> Eng yaxshi hovli qayerda?<br><br>
            <b>4.</b> Privacy qayerda kerak?<br><br>
            <b>5.</b> Parking qayerda?<br><br>
            <b>6.</b> Living qaysi hovliga qaraydi?<br><br>
            <b>7.</b> Service qayerda?
            """,
        },
        {
            "title": "Mini-loyiha",
            "type": "example",
            "text": """
            Oldingi uchastkangizda
            uyni 3 xil variantda joylashtiring.

            <br><br>

            Har variant uchun:

            <br><br>

            • public hovli;<br>
            • private hovli;<br>
            • parking;<br>
            • living-hovli aloqasi;<br>
            • quyosh;<br>
            • privacy

            <br><br>

            bo'yicha baholang.

            <br><br>

            Keyin eng mantiqiy variantni tanlang
            va nima uchunligini yozing.
            """,
        },
        {
            "title": "Modul yakuni",
            "type": "highlight",
            "text": """
            Siz endi:

            <br><br>

            ✓ bino konturini uchastkaga joylashtirish;<br>
            ✓ old va private hovlini ajratish;<br>
            ✓ quyoshni hisobga olish;<br>
            ✓ privacy yaratish;<br>
            ✓ parkingni uy bilan bog'lash;<br>
            ✓ noto'g'ri joylashtirishni aniqlash

            <br><br>

            ko'nikmalariga ega bo'ldingiz.

            <br><br>

            Keyingi modul:
            <b>Hovli zonalari.</b>
            """,
        },
    ],
}


# ============================================================
# QUIZ
# ============================================================

LEVEL03_MODULE04_QUIZ = {
    "L03_M04_001": [
        {
            "code": "L03_Q046",
            "question": "Uyni uchastkaning markaziga qo'yish har doim eng yaxshi yechimmi?",
            "explanation": (
                "Markaziy joylashuv hovlini bir nechta kichik va samarasiz qismlarga bo'lishi mumkin."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L03_Q047",
            "question": "Uy joylashuvi hovli va parkingga ta'sir qiladimi?",
            "explanation": (
                "Bino konturi uchastkadagi barcha asosiy funksional zonalar bilan bog'liq."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L03_Q048",
            "question": "Bino konturidan oldin site sharoitini tahlil qilish foydalimi?",
            "explanation": (
                "Ko'cha, quyosh, hovli va privacy keyingi bino joylashuviga asos bo'ladi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L03_M04_002": [
        {
            "code": "L03_Q049",
            "question": "Old hovli va private hovli bir xil vazifani bajarishi shartmi?",
            "explanation": (
                "Old hovli ko'proq kirish va public funksiyalar bilan, private hovli esa oilaviy dam olish bilan bog'liq bo'lishi mumkin."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L03_Q050",
            "question": "Uy ko'cha shovqinidan private hovlini qisman himoya qilishi mumkinmi?",
            "explanation": (
                "Binoning o'zi tashqi noqulay tomonga buffer bo'lib xizmat qilishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L03_Q051",
            "question": "Family hovli uchun living bilan yaxshi aloqa foydalimi?",
            "explanation": (
                "Ichki va tashqi oilaviy makonlar orasidagi qulay aloqa yashash sifatini oshiradi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L03_M04_003": [
        {
            "code": "L03_Q052",
            "question": "Uy joylashuvida privacy ham tahlil qilinadimi?",
            "explanation": (
                "Ko'cha va qo'shnilardan ko'rinish private xona va hovliga ta'sir qiladi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L03_Q053",
            "question": "Service xonalar noqulay tashqi tomonga buffer sifatida joylashtirilishi mumkinmi?",
            "explanation": (
                "Bu ayrim loyihalarda asosiy yashash zonalarini himoya qilishga yordam beradi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L03_Q054",
            "question": "Katta deraza doim privacy uchun yaxshi yechimmi?",
            "explanation": (
                "Ochilish yo'nalishi va tashqi ko'rinish sharoiti tekshirilishi kerak."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
    ],

    "L03_M04_004": [
        {
            "code": "L03_Q055",
            "question": "Parkingning uy kirishiga yaqinligi kundalik foydalanishga ta'sir qiladimi?",
            "explanation": (
                "Avtomobildan uyga o'tish oilaning kundalik circulationiga kiradi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L03_Q056",
            "question": "Parking butun ko'cha fasadini egallashi har doim yaxshi yechimmi?",
            "explanation": (
                "Bu piyoda kirishi va uy fasadining sifatini zaiflashtirishi mumkin."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L03_Q057",
            "question": "Mahsulotni parkingdan oshxonaga olib kirish yo'li tahlil qilinadimi?",
            "explanation": (
                "Bu kundalik service va household circulationning bir qismi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L03_M04_005": [
        {
            "code": "L03_Q058",
            "question": "Uy uchastkani bir nechta kichik foydasiz hovliga bo'lib yuborishi mumkinmi?",
            "explanation": (
                "Bino konturining noto'g'ri joylashuvi tashqi makon sifatini pasaytirishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L03_Q059",
            "question": "Livingning eng yaxshi hovlidan uzilishi fazoviy muammomi?",
            "explanation": (
                "Living va asosiy oilaviy tashqi zona o'rtasidagi aloqa muhim."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L03_Q060",
            "question": "Uy joylashtirish tahlilida qaysi savol muhim?",
            "explanation": (
                "Eng yaxshi hovli, ko'cha, quyosh, privacy va parking birgalikda tahlil qilinadi."
            ),
            "options": [
                ("A", "Eng yaxshi private hovli qayerda?", True),
                ("B", "Faqat tom materiali nima?", False),
            ],
        },
    ],
}


# ============================================================
# DATABASE SEED
# ============================================================

def seed_level03_module04():
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
        ) in LEVEL03_MODULE04_LESSONS:

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
