from database.database import get_connection


# ============================================================
# LEVEL 3
# MODULE 01 - UCHASTKANI O'QISH
# ============================================================

LEVEL03_MODULE01_LESSONS = [
    (
        "L03_M01",
        "L03_M01_001",
        "Uchastka nima va uni qanday o'qiymiz?",
        "theory",
        "Yer uchastkasini loyiha boshlanishidan oldin tizimli tahlil qilish.",
        1,
        35,
        20,
    ),
    (
        "L03_M01",
        "L03_M01_002",
        "Uchastka shakli va proporsiyasi",
        "theory",
        "To'g'ri, tor, uzun va murakkab shakldagi uchastkalarning imkoniyatlarini tushunish.",
        2,
        35,
        20,
    ),
    (
        "L03_M01",
        "L03_M01_003",
        "Chegaralar va mavjud obyektlar",
        "theory",
        "Uchastkadagi mavjud bino, daraxt, kommunikatsiya va boshqa elementlarni tahlil qilish.",
        3,
        40,
        20,
    ),
    (
        "L03_M01",
        "L03_M01_004",
        "Uchastkaning kuchli va zaif tomonlari",
        "practice",
        "Yerning loyiha imkoniyatlari va cheklovlarini professional tarzda ajratish.",
        4,
        40,
        20,
    ),
    (
        "L03_M01",
        "L03_M01_005",
        "Site Analysis — birinchi audit",
        "practice",
        "Real uchastka uchun boshlang'ich site analysis tayyorlash.",
        5,
        50,
        25,
    ),
]


# ============================================================
# CONTENT
# ============================================================

LEVEL03_MODULE01_CONTENT = {
    "L03_M01_001": [
        {
            "title": "Loyiha uy chizishdan boshlanmaydi",
            "type": "highlight",
            "text": """
            Professional loyiha ko'pincha
            uy planini chizishdan oldin boshlanadi.

            <br><br>

            Avval arxitektor yer uchastkasini tushunadi.

            <br><br>

            <b>
            Yer qanday bo'lsa,
            loyiha qarorlarining katta qismi
            shunga bog'liq bo'ladi.
            </b>
            """,
        },
        {
            "title": "Site Analysis nima?",
            "type": "normal",
            "text": """
            Site Analysis — uchastkaning mavjud
            sharoitlarini loyiha oldidan tahlil qilish.

            <br><br>

            Masalan:

            <br><br>

            • shakli;<br>
            • o'lchami;<br>
            • ko'cha tomoni;<br>
            • kirish imkoniyati;<br>
            • mavjud bino;<br>
            • daraxtlar;<br>
            • relyef;<br>
            • atrofdagi qurilishlar.
            """,
        },
        {
            "title": "Tasavvur qiling",
            "type": "example",
            "text": """
            Sizga 20 × 40 metr uchastka berildi.

            <br><br>

            Darhol 250 m² uy chizishni boshladingiz.

            <br><br>

            Keyin ma'lum bo'ldiki:

            <br><br>

            asosiy kirish noto'g'ri tomonda,
            mavjud katta daraxt kesilmasligi kerak,
            uchastkaning bir qismida nishab bor.

            <br><br>

            Endi butun reja qayta ishlanishi mumkin.
            """,
        },
        {
            "title": "Arxitektorning birinchi savoli",
            "type": "highlight",
            "text": """
            <b>
            “Bu yerga qanday uy sig'adi?”
            emas.

            <br><br>

            “Bu yer qanday ishlaydi?”
            </b>

            <br><br>

            degan savol kuchliroq.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            O'zingiz biladigan bir uchastkani tanlang.

            <br><br>

            Uy chizmasdan turib,
            uchastka haqida kamida
            10 ta fakt yozing.
            """,
        },
    ],

    "L03_M01_002": [
        {
            "title": "Shakl loyiha imkoniyatini o'zgartiradi",
            "type": "highlight",
            "text": """
            Bir xil maydondagi ikki uchastka
            bir xil loyiha imkoniyatiga ega bo'lmasligi mumkin.

            <br><br>

            Sabab — shakl va proporsiya.
            """,
        },
        {
            "title": "To'g'ri to'rtburchak uchastka",
            "type": "normal",
            "text": """
            Oddiy to'g'ri to'rtburchak uchastka
            ko'pincha rejalashda tushunarliroq bo'ladi.

            <br><br>

            Lekin uning kengligi va uzunligi
            baribir loyiha xarakterini o'zgartiradi.
            """,
        },
        {
            "title": "Tor va uzun uchastka",
            "type": "example",
            "text": """
            Masalan:

            <br><br>

            10 × 50 metr uchastka.

            <br><br>

            Maydoni katta bo'lishi mumkin,
            lekin tor kenglik:

            <br><br>

            • kirish;<br>
            • avtomobil;<br>
            • hovli;<br>
            • uy eni

            <br><br>

            bo'yicha cheklov yaratadi.
            """,
        },
        {
            "title": "Murakkab shakl",
            "type": "normal",
            "text": """
            Trapetsiya, L shakl,
            uchburchakka yaqin yoki
            notekis chegara

            <br><br>

            muammo ham,
            imkoniyat ham bo'lishi mumkin.
            """,
        },
        {
            "title": "Xato fikr",
            "type": "warning",
            "text": """
            “Maydoni katta ekan,
            istalgan uy sig'adi.”

            <br><br>

            Bu noto'g'ri fikr.

            <br><br>

            Maydon bilan birga
            geometriyani ham o'qish kerak.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Bir xil 600 m² maydonga ega:

            <br><br>

            • keng;<br>
            • tor va uzun;<br>
            • murakkab shakldagi

            <br><br>

            uchta uchastkani tasavvur qiling.

            <br><br>

            Qaysi birida rejalash osonroq?
            Nima uchun?
            """,
        },
    ],

    "L03_M01_003": [
        {
            "title": "Bo'sh yer ham har doim bo'sh emas",
            "type": "highlight",
            "text": """
            Uchastkaga kirganingizda
            faqat chegarani ko'rmang.

            <br><br>

            Mavjud elementlar
            kelajak loyihasiga ta'sir qiladi.
            """,
        },
        {
            "title": "Nimalarni qayd qilamiz?",
            "type": "normal",
            "text": """
            Masalan:

            <br><br>

            • mavjud uy;<br>
            • yordamchi bino;<br>
            • daraxtlar;<br>
            • ustunlar;<br>
            • quduq;<br>
            • yo'l;<br>
            • devor;<br>
            • kommunikatsiya nuqtalari.
            """,
        },
        {
            "title": "Saqlanadigan elementlar",
            "type": "example",
            "text": """
            Uchastkada katta sog'lom daraxt bor.

            <br><br>

            Uni avtomatik ravishda
            “xalaqit beradi” deb qabul qilish shart emas.

            <br><br>

            U kelajakdagi hovli kompozitsiyasining
            kuchli elementi bo'lishi mumkin.
            """,
        },
        {
            "title": "Mavjud bino",
            "type": "normal",
            "text": """
            Agar uchastkada eski bino bo'lsa,
            loyiha boshlanishida aniqlanadi:

            <br><br>

            • saqlanadimi;<br>
            • buziladimi;<br>
            • vaqtincha foydalaniladimi;<br>
            • yangi uyga qanday ta'sir qiladi.
            """,
        },
        {
            "title": "Ko'rinmaydigan omillar",
            "type": "warning",
            "text": """
            Faqat ko'z bilan ko'rinadigan
            obyektlarga tayanish yetarli emas.

            <br><br>

            Keyingi professional bosqichlarda
            kommunikatsiyalar, huquqiy chegaralar
            va normativ cheklovlar ham tekshiriladi.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Bir uchastka rasmini oling.

            <br><br>

            Unda mavjud bo'lgan
            barcha elementlarni ro'yxatlang.

            <br><br>

            Har biriga:

            <br><br>

            SAQLASH / KO'CHIRISH / TEKSHIRISH

            <br><br>

            degan belgi qo'ying.
            """,
        },
    ],

    "L03_M01_004": [
        {
            "title": "Har uchastkaning kuchli tomoni bor",
            "type": "highlight",
            "text": """
            Site Analysis faqat muammolar
            ro'yxati emas.

            <br><br>

            Yaxshi arxitektor imkoniyatlarni ham topadi.
            """,
        },
        {
            "title": "Kuchli tomonlar",
            "type": "normal",
            "text": """
            Misollar:

            <br><br>

            • yaxshi ko'rinish;<br>
            • qulay ko'cha kirishi;<br>
            • katta yashil hudud;<br>
            • yaxshi orientatsiya imkoniyati;<br>
            • tinch qo'shni tomon;<br>
            • mavjud yetuk daraxtlar.
            """,
        },
        {
            "title": "Zaif tomonlar",
            "type": "normal",
            "text": """
            Misollar:

            <br><br>

            • tor uchastka;<br>
            • murakkab kirish;<br>
            • kuchli nishab;<br>
            • shovqinli ko'cha;<br>
            • noqulay qo'shni qurilish;<br>
            • foydalanish qiyin bo'lgan burchak.
            """,
        },
        {
            "title": "Muammo yechimga aylanadi",
            "type": "example",
            "text": """
            Ko'cha tomoni shovqinli.

            <br><br>

            Bu faqat minus emas.

            <br><br>

            Keyinchalik service,
            parking yoki buffer zonalarni
            shu tomonga joylashtirish
            imkoniyati tug'ilishi mumkin.
            """,
        },
        {
            "title": "SWOT usuli",
            "type": "highlight",
            "text": """
            Oddiy tahlilda uchastkani:

            <br><br>

            <b>Strengths</b> — kuchli tomonlar<br>
            <b>Weaknesses</b> — zaif tomonlar<br>
            <b>Opportunities</b> — imkoniyatlar<br>
            <b>Threats</b> — xavflar

            <br><br>

            sifatida ham tahlil qilish mumkin.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Bitta uchastka uchun:

            <br><br>

            3 ta kuchli tomon,<br>
            3 ta zaif tomon,<br>
            2 ta imkoniyat,<br>
            2 ta xavf

            <br><br>

            yozing.
            """,
        },
    ],

    "L03_M01_005": [
        {
            "title": "Birinchi Site Analysis",
            "type": "highlight",
            "text": """
            Endi uchastkani professional tartibda
            birinchi marta audit qilamiz.
            """,
        },
        {
            "title": "1. Geometriya",
            "type": "example",
            "text": """
            Belgilang:

            <br><br>

            • umumiy shakl;<br>
            • uzunlik;<br>
            • kenglik;<br>
            • torayadigan joylar;<br>
            • noto'g'ri burchaklar.
            """,
        },
        {
            "title": "2. Tashqi aloqa",
            "type": "example",
            "text": """
            Belgilang:

            <br><br>

            • ko'cha qayerda;<br>
            • asosiy kirish qayerdan;<br>
            • avtomobil qayerdan kirishi mumkin;<br>
            • piyoda qayerdan kiradi.
            """,
        },
        {
            "title": "3. Mavjud holat",
            "type": "example",
            "text": """
            Belgilang:

            <br><br>

            • mavjud bino;<br>
            • daraxt;<br>
            • devor;<br>
            • ustun;<br>
            • kommunikatsiya belgisi;<br>
            • relyef o'zgarishi.
            """,
        },
        {
            "title": "4. Atrof",
            "type": "example",
            "text": """
            Faqat o'z uchastkangizga qaramang.

            <br><br>

            Qo'shni tomonda:

            <br><br>

            • baland bino bormi?<br>
            • shovqin bormi?<br>
            • yaxshi manzara bormi?<br>
            • privacy muammosi bormi?
            """,
        },
        {
            "title": "5. Birinchi xulosa",
            "type": "highlight",
            "text": """
            Site Analysis yakunida
            darhol uy planini chizishdan oldin
            qisqa xulosa yozing:

            <br><br>

            <b>
            “Ushbu uchastkada loyiha uchun
            asosiy imkoniyat nima va
            asosiy cheklov nima?”
            </b>
            """,
        },
        {
            "title": "Mini-loyiha",
            "type": "example",
            "text": """
            20 × 30 yoki 25 × 40 metrga yaqin
            bir uchastka tanlang.

            <br><br>

            Bitta varaqda:

            <br><br>

            • uchastka konturi;<br>
            • ko'cha;<br>
            • kirish;<br>
            • mavjud elementlar;<br>
            • kuchli tomonlar;<br>
            • zaif tomonlar

            <br><br>

            ni belgilang.

            <br><br>

            Hali uy chizmang.
            Faqat yerning o'zini tushuning.
            """,
        },
        {
            "title": "Modul yakuni",
            "type": "highlight",
            "text": """
            Siz endi:

            <br><br>

            ✓ uchastkani o'qish;<br>
            ✓ shakl va proporsiyani tahlil qilish;<br>
            ✓ mavjud obyektlarni aniqlash;<br>
            ✓ kuchli va zaif tomonlarni ajratish;<br>
            ✓ boshlang'ich Site Analysis qilish

            <br><br>

            bo'yicha birinchi professional
            ko'nikmaga ega bo'ldingiz.

            <br><br>

            Keyingi modul:
            <b>Shimol va quyosh.</b>
            """,
        },
    ],
}


# ============================================================
# QUIZ
# ============================================================

LEVEL03_MODULE01_QUIZ = {
    "L03_M01_001": [
        {
            "code": "L03_Q001",
            "question": "Professional loyiha har doim darhol uy planini chizishdan boshlanadimi?",
            "explanation": (
                "Avval uchastka sharoitini tushunish va site analysis qilish muhim."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L03_Q002",
            "question": "Site Analysis nimani o'rganadi?",
            "explanation": (
                "Uchastkaning shakli, o'lchami, mavjud sharoiti va loyiha imkoniyatlarini."
            ),
            "options": [
                ("A", "Uchastka sharoitini", True),
                ("B", "Faqat interyer rangini", False),
            ],
        },
        {
            "code": "L03_Q003",
            "question": "Uchastkadagi daraxtlar va mavjud binolar loyiha qaroriga ta'sir qilishi mumkinmi?",
            "explanation": (
                "Mavjud obyektlar yangi loyiha joylashuvi va hovli yechimlariga ta'sir qilishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L03_M01_002": [
        {
            "code": "L03_Q004",
            "question": "Bir xil maydondagi ikki uchastkaning loyiha imkoniyati doim bir xilmi?",
            "explanation": (
                "Shakl va proporsiya loyiha imkoniyatlarini keskin o'zgartirishi mumkin."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L03_Q005",
            "question": "Tor va uzun uchastka rejalashga ta'sir qiladimi?",
            "explanation": (
                "Kenglik uy eni, parking, kirish va hovli tashkiliga ta'sir qilishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L03_Q006",
            "question": "Uchastka maydoni katta bo'lsa geometriyasini tekshirish shart emasmi?",
            "explanation": (
                "Maydon katta bo'lsa ham shakl va proporsiya albatta tekshiriladi."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
    ],

    "L03_M01_003": [
        {
            "code": "L03_Q007",
            "question": "Mavjud katta daraxt har doim xalaqit beruvchi elementmi?",
            "explanation": (
                "U loyiha va hovli kompozitsiyasining foydali elementi bo'lishi mumkin."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L03_Q008",
            "question": "Uchastkadagi eski bino holati loyiha oldidan aniqlanadimi?",
            "explanation": (
                "U saqlanishi, buzilishi yoki boshqa tarzda foydalanilishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L03_Q009",
            "question": "Site Analysis faqat ko'z bilan ko'rinadigan narsalardan iboratmi?",
            "explanation": (
                "Keyingi bosqichlarda kommunikatsiya, chegaralar va boshqa cheklovlar ham tekshiriladi."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
    ],

    "L03_M01_004": [
        {
            "code": "L03_Q010",
            "question": "Site Analysis faqat kamchiliklarni topish uchun qilinadimi?",
            "explanation": (
                "U imkoniyatlar va kuchli tomonlarni ham aniqlaydi."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L03_Q011",
            "question": "Shovqinli ko'cha loyiha zonalashiga ta'sir qilishi mumkinmi?",
            "explanation": (
                "Shovqinli tomon buffer yoki service zonalarni joylashtirish qaroriga ta'sir qilishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L03_Q012",
            "question": "SWOT tahlilida Strengths nimani bildiradi?",
            "explanation": (
                "Strengths — uchastkaning kuchli tomonlari."
            ),
            "options": [
                ("A", "Kuchli tomonlar", True),
                ("B", "Faqat xavflar", False),
            ],
        },
    ],

    "L03_M01_005": [
        {
            "code": "L03_Q013",
            "question": "Birinchi site auditda ko'cha va kirish yo'nalishi tekshiriladimi?",
            "explanation": (
                "Tashqi aloqa uchastka tahlilining asosiy qismlaridan biridir."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L03_Q014",
            "question": "Site Analysisda qo'shni qurilishlarni ham o'rganish kerakmi?",
            "explanation": (
                "Qo'shni binolar privacy, shovqin, ko'rinish va boshqa qarorlarga ta'sir qiladi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L03_Q015",
            "question": "Site Analysis yakunidagi eng foydali savollardan biri qaysi?",
            "explanation": (
                "Asosiy imkoniyat va asosiy cheklovni aniqlash keyingi loyiha qarorlariga asos yaratadi."
            ),
            "options": [
                ("A", "Asosiy imkoniyat va cheklov nima?", True),
                ("B", "Faqat fasad qaysi rangda bo'ladi?", False),
            ],
        },
    ],
}


# ============================================================
# DATABASE SEED
# ============================================================

def seed_level03_module01():
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
        ) in LEVEL03_MODULE01_LESSONS:

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
