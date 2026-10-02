from database.database import get_connection


# ============================================================
# LEVEL 2
# MODULE 09 - KORIDOR VA KIRISH
# ============================================================

LEVEL02_MODULE09_LESSONS = [
    (
        "L02_M09",
        "L02_M09_001",
        "Kirish zonasi va tambur",
        "theory",
        "Uyga kirish, tambur va birinchi o'tish zonasining vazifalarini tushunish.",
        1,
        35,
        20,
    ),
    (
        "L02_M09",
        "L02_M09_002",
        "Hallway va circulation",
        "theory",
        "Koridor va hallway orqali xonalar orasidagi harakatni mantiqiy tashkil qilish.",
        2,
        35,
        20,
    ),
    (
        "L02_M09",
        "L02_M09_003",
        "Kiyim va poyabzal saqlash",
        "practice",
        "Kirish zonasida coat, shoe va kundalik buyumlar uchun storage tashkil qilish.",
        3,
        35,
        20,
    ),
    (
        "L02_M09",
        "L02_M09_004",
        "Door conflict va o'tish yo'llari",
        "practice",
        "Koridor va kirishdagi eshiklar hamda harakat zonalari o'rtasidagi konfliktlarni aniqlash.",
        4,
        35,
        20,
    ),
    (
        "L02_M09",
        "L02_M09_005",
        "Kirish va koridor auditi",
        "practice",
        "Kirish, tambur, hallway, storage va circulationni kompleks tekshirish.",
        5,
        40,
        25,
    ),
]


# ============================================================
# CONTENT
# ============================================================

LEVEL02_MODULE09_CONTENT = {
    "L02_M09_001": [
        {
            "title": "Kirish — uy bilan birinchi aloqa",
            "type": "highlight",
            "text": """
            Uyga kirish zonasi —
            tashqi makondan ichki makonga
            o'tadigan birinchi nuqta.

            <br><br>

            Bu yerda odam:

            <br><br>

            • uyga kiradi;<br>
            • tashqi kiyimni yechadi;<br>
            • poyabzalni almashtiradi;<br>
            • sumka yoki buyumlarni qo'yadi;<br>
            • keyin uy ichiga o'tadi.
            """,
        },
        {
            "title": "Tambur nima uchun kerak?",
            "type": "normal",
            "text": """
            Tambur —
            tashqi eshik bilan
            asosiy ichki makon orasidagi
            o'tish zonasi.

            <br><br>

            U:

            <br><br>

            • kirishni tartibga solishi;<br>
            • tashqi va ichki makonni ajratishi;<br>
            • shamol va sovuq oqimini kamaytirishga yordam berishi;<br>
            • kiyim va poyabzal zonasiga joy berishi

            <br><br>

            mumkin.
            """,
        },
        {
            "title": "Kirish faqat eshik emas",
            "type": "highlight",
            "text": """
            Arxitektorda
            kirish nuqtasi

            <br><br>

            shunchaki eshik joyi emas.

            <br><br>

            Bu kichik funksional zona.
            """,
        },
        {
            "title": "Tasavvur qiling",
            "type": "example",
            "text": """
            Tashqi eshikdan kirganingizda
            darhol living markaziga tushasiz.

            <br><br>

            Poyabzal uchun joy yo'q.

            <br><br>

            Palto uchun shkaf yo'q.

            <br><br>

            Mehmon kirganda
            butun living birdan ko'rinadi.

            <br><br>

            Kirish ishlayapti,
            lekin entrance zone tashkil qilinmagan.
            """,
        },
        {
            "title": "Kirishdan keyingi savol",
            "type": "normal",
            "text": """
            Uyga kirgan odam
            keyin qayerga boradi?

            <br><br>

            • livinggami?<br>
            • hallwaygami?<br>
            • mehmon zonasigami?<br>
            • staircasegami?

            <br><br>

            Bu harakat
            birinchi qarashdayoq
            tushunarli bo'lishi foydali.
            """,
        },
        {
            "title": "Mini-vazifa",
            "type": "example",
            "text": """
            Uy entrance planini chizing.

            <br><br>

            Unda belgilang:

            <br><br>

            • tashqi eshik;<br>
            • tambur;<br>
            • shoe zone;<br>
            • coat storage;<br>
            • hallwayga o'tish.
            """,
        },
    ],

    "L02_M09_002": [
        {
            "title": "Koridorning vazifasi",
            "type": "highlight",
            "text": """
            Koridor va hallway
            uy ichidagi xonalarni
            bog'laydigan circulation makoni.

            <br><br>

            Uning asosiy vazifasi —
            odamni kerakli joyga
            qulay olib borish.
            """,
        },
        {
            "title": "Koridorning o'zi maqsad emas",
            "type": "normal",
            "text": """
            Koridor foydali funksiyani
            bog'lash uchun kerak.

            <br><br>

            Juda ko'p maydonni
            faqat yurish uchun sarflash
            reja samaradorligini pasaytirishi mumkin.
            """,
        },
        {
            "title": "Qisqa va tushunarli yo'l",
            "type": "highlight",
            "text": """
            Yaxshi circulationda
            odam:

            <br><br>

            • qayerga borishini tushunadi;<br>
            • keraksiz burilish qilmaydi;<br>
            • boshqa xonalarni kesib o'tmaydi.
            """,
        },
        {
            "title": "Private va public yo'llar",
            "type": "normal",
            "text": """
            Hallway orqali:

            <br><br>

            public zona,
            private zona
            va service zonalar

            <br><br>

            bir-biriga bog'lanishi mumkin.

            <br><br>

            Lekin mehmon
            bedroom orqali sanuzelga
            o'tmasligi kerak.
            """,
        },
        {
            "title": "Tasavvur qiling",
            "type": "example",
            "text": """
            Bedroomga kirish uchun
            avval livingdan,
            keyin diningdan,
            keyin kichik koridordan
            o'tish kerak.

            <br><br>

            Bu ortiqcha circulation
            va privacy muammosi
            yaratishi mumkin.
            """,
        },
        {
            "title": "Koridor geometriyasi",
            "type": "normal",
            "text": """
            Juda ko'p sinish,
            keraksiz burilish
            va murakkab shakl

            <br><br>

            harakatni tushunarsiz
            qilishi mumkin.

            <br><br>

            Har bir burilishning
            sababi bo'lishi kerak.
            """,
        },
        {
            "title": "Mini-vazifa",
            "type": "example",
            "text": """
            Uy planida
            entrance'dan:

            <br><br>

            • livingga;<br>
            • bedroomga;<br>
            • sanuzelga

            <br><br>

            yurish yo'llarini
            strelka bilan chizing.

            <br><br>

            Keraksiz kesishmalar bormi?
            """,
        },
    ],

    "L02_M09_003": [
        {
            "title": "Entrance storage",
            "type": "highlight",
            "text": """
            Kirish zonasida
            kundalik buyumlar uchun
            storage juda foydali.

            <br><br>

            Masalan:

            <br><br>

            • palto;<br>
            • kurtka;<br>
            • poyabzal;<br>
            • sumka;<br>
            • soyabon;<br>
            • kalitlar.
            """,
        },
        {
            "title": "Poyabzal zonasi",
            "type": "normal",
            "text": """
            Uyga kirgan odam
            qayerda poyabzal yechadi?

            <br><br>

            Shu oddiy savol
            entrance rejasini
            ancha o'zgartirishi mumkin.
            """,
        },
        {
            "title": "Coat storage",
            "type": "normal",
            "text": """
            Coat storage
            kirishga juda uzoq bo'lsa,

            <br><br>

            odam tashqi kiyim bilan
            uy ichiga ancha yurishga
            majbur bo'lishi mumkin.
            """,
        },
        {
            "title": "Storage circulationni to'smasin",
            "type": "warning",
            "text": """
            Katta shkaf
            entrance uchun foydali.

            <br><br>

            Lekin uning eshigi ochilganda
            asosiy yo'lni yopsa,

            <br><br>

            storage yaxshi joylashmagan.
            """,
        },
        {
            "title": "O'tirish joyi",
            "type": "example",
            "text": """
            Poyabzal almashtirish uchun
            kichik o'tirish joyi
            ayrim entrance'larda
            qulaylik yaratishi mumkin.

            <br><br>

            Lekin u circulationni
            to'smasligi kerak.
            """,
        },
        {
            "title": "Mehmon va oila storage'i",
            "type": "normal",
            "text": """
            Oilaning kundalik
            buyumlari ko'p bo'lishi mumkin.

            <br><br>

            Shu bilan birga
            mehmonning kiyimi uchun
            ham mantiqiy joy kerak bo'lishi mumkin.
            """,
        },
        {
            "title": "Mini-vazifa",
            "type": "example",
            "text": """
            Entrancega joylashtiring:

            <br><br>

            • shoe storage;<br>
            • coat storage;<br>
            • kichik bench;<br>
            • key shelf.

            <br><br>

            Keyin eshiklarni ochib,
            circulationni tekshiring.
            """,
        },
    ],

    "L02_M09_004": [
        {
            "title": "Koridorda ko'p eshik bo'lishi mumkin",
            "type": "highlight",
            "text": """
            Hallway va koridor
            ko'pincha bir nechta
            xonaning eshiklarini
            birlashtiradi.

            <br><br>

            Shu sabab door conflict
            muhim masala.
            """,
        },
        {
            "title": "Door swinglar to'qnashuvi",
            "type": "warning",
            "text": """
            Ikki xona eshigi
            bir vaqtda ochilganda
            bir-biriga urilsa,

            <br><br>

            circulation va foydalanish
            noqulaylashadi.
            """,
        },
        {
            "title": "Kirish eshigi va storage",
            "type": "example",
            "text": """
            Tashqi eshik ichkariga ochiladi.

            <br><br>

            Uning yonida wardrobe bor.

            <br><br>

            Wardrobe eshigi bilan
            tashqi eshik bir-birini bloklaydi.

            <br><br>

            Ikkala element alohida
            to'g'ri ko'rinadi,
            lekin birga ishlamaydi.
            """,
        },
        {
            "title": "Harakat yo'lini kesmang",
            "type": "normal",
            "text": """
            Eshik ochilganda
            hallway bo'ylab
            asosiy yurish yo'li
            butunlay yopilmasligi kerak.
            """,
        },
        {
            "title": "Ko'r zonalar",
            "type": "normal",
            "text": """
            Koridorda keskin burilish
            va bir-biriga yaqin eshiklar
            odamlar to'qnashuvini
            oshirishi mumkin.

            <br><br>

            Harakatni real holatda
            tasavvur qiling.
            """,
        },
        {
            "title": "Bir vaqtning o'zida foydalanish",
            "type": "highlight",
            "text": """
            Rejani tekshirayotganda
            bitta odamni emas,

            <br><br>

            bir vaqtning o'zida
            bir nechta odamni tasavvur qiling.
            """,
        },
        {
            "title": "Mini-vazifa",
            "type": "example",
            "text": """
            Koridorda 3 ta eshik chizing.

            <br><br>

            Ularning ochilish yoylarini
            ko'rsating.

            <br><br>

            Qaysi eshiklar
            bir-biri bilan konflikt
            qilayotganini aniqlang.
            """,
        },
    ],

    "L02_M09_005": [
        {
            "title": "Kirish va koridor auditi",
            "type": "highlight",
            "text": """
            Endi entrance va hallwayni
            faqat o'tish joyi sifatida emas,

            <br><br>

            butun uy circulation
            tizimining bir qismi sifatida
            tekshiramiz.
            """,
        },
        {
            "title": "1. Entrance",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • kirish aniqmi?<br>
            • tambur kerakli vazifani bajaryaptimi?<br>
            • uyga kirganda yo'nalish tushunarlimi?
            """,
        },
        {
            "title": "2. Storage",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • poyabzal uchun joy bormi?<br>
            • coat storage bormi?<br>
            • storage eshik bilan konflikt qilmayaptimi?<br>
            • kundalik buyumlar uchun joy bormi?
            """,
        },
        {
            "title": "3. Hallway",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • yo'llar qisqa va tushunarlimi?<br>
            • keraksiz burilishlar bormi?<br>
            • private xonalar himoyalanganmi?<br>
            • koridor ortiqcha maydon olmayaptimi?
            """,
        },
        {
            "title": "4. Door conflict",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • eshiklar bir-biriga urilmayaptimi?<br>
            • eshik asosiy yo'lni yopmayaptimi?<br>
            • wardrobe va door conflict yo'qmi?
            """,
        },
        {
            "title": "Xatoni toping",
            "type": "warning",
            "text": """
            Uyning entrance qismi
            juda chiroyli.

            <br><br>

            Ammo:

            <br><br>

            • tashqi eshik shkafga uriladi;<br>
            • poyabzal uchun joy yo'q;<br>
            • bedroomga borish uchun living kesib o'tiladi;<br>
            • koridorda 3 ta eshik bir joyda to'qnashadi.

            <br><br>

            Muammo:

            <br><br>

            entrance va hallway
            grafik ko'rinish sifatida ishlangan,
            circulation tizimi sifatida emas.
            """,
        },
        {
            "title": "Professional checklist",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            <b>1.</b> Kirish yo'nalishi aniqmi?<br><br>
            <b>2.</b> Tambur funksionalmi?<br><br>
            <b>3.</b> Shoe va coat storage bormi?<br><br>
            <b>4.</b> Hallway qisqa va tushunarlimi?<br><br>
            <b>5.</b> Public/private circulation mantiqiymi?<br><br>
            <b>6.</b> Door conflict yo'qmi?<br><br>
            <b>7.</b> Koridor ortiqcha maydon olmayaptimi?
            """,
        },
        {
            "title": "Modul yakuni",
            "type": "highlight",
            "text": """
            Siz endi:

            <br><br>

            ✓ entrance zonasini tushunasiz;<br>
            ✓ tamburni rejalashtirasiz;<br>
            ✓ hallway circulationni tahlil qilasiz;<br>
            ✓ coat va shoe storage tashkil qilasiz;<br>
            ✓ door conflictlarni topasiz;<br>
            ✓ public/private harakatni ajratasiz;<br>
            ✓ kirish va koridor auditini bajarasiz.

            <br><br>

            Keyingi modul:
            <b>Yordamchi xonalar.</b>
            """,
        },
    ],
}


# ============================================================
# QUIZ
# Q121-Q135 KODLARI SAQLANADI
# ============================================================

LEVEL02_MODULE09_QUIZ = {
    "L02_M09_001": [
        {
            "code": "L02_Q121",
            "question": "Kirish zonasi faqat tashqi eshikdan iboratmi?",
            "explanation": (
                "Kirish zonasida tambur, storage va uy ichiga o'tish kabi funksiyalar ham bo'lishi mumkin."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L02_Q122",
            "question": "Tambur tashqi va ichki makon orasidagi o'tish zonasi bo'lishi mumkinmi?",
            "explanation": (
                "Tambur entrance jarayonini tartibga soladigan oraliq makon bo'lishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L02_Q123",
            "question": "Uyga kirgandan keyingi harakat yo'nalishini rejalashtirish kerakmi?",
            "explanation": (
                "Entrance'dan keyin odamning qayerga borishi circulation tizimining bir qismidir."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L02_M09_002": [
        {
            "code": "L02_Q124",
            "question": "Koridorning asosiy vazifasi xonalar orasidagi harakatni tashkil qilishmi?",
            "explanation": (
                "Hallway va koridorlar uy ichidagi asosiy circulation elementlaridir."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L02_Q125",
            "question": "Juda uzun va keraksiz koridor reja samaradorligini pasaytirishi mumkinmi?",
            "explanation": (
                "Faqat yurishga sarflanadigan ortiqcha maydon reja samaradorligini kamaytirishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L02_Q126",
            "question": "Bedroomga borish uchun public xonalarni kesib o'tish har doim yaxshi yechimmi?",
            "explanation": (
                "Private circulation imkon qadar mantiqiy va himoyalangan bo'lishi kerak."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
    ],

    "L02_M09_003": [
        {
            "code": "L02_Q127",
            "question": "Kirish zonasida poyabzal va tashqi kiyim uchun storage foydalimi?",
            "explanation": (
                "Entrance storage kundalik foydalanishni tartibli va qulay qilishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L02_Q128",
            "question": "Storage eshigi asosiy circulationni to'sishi mumkinmi?",
            "explanation": (
                "Wardrobe yoki boshqa storage opening zonasi harakat yo'li bilan tekshiriladi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L02_Q129",
            "question": "Coat storage kirishdan juda uzoqda bo'lishi har doim qulaymi?",
            "explanation": (
                "Tashqi kiyimlar uchun storage entrancega mantiqan yaqin bo'lishi foydali."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
    ],

    "L02_M09_004": [
        {
            "code": "L02_Q130",
            "question": "Koridordagi eshiklar bir-biriga urilishi mumkinmi?",
            "explanation": (
                "Door swinglar noto'g'ri rejalashtirilsa bir-biri bilan konflikt qiladi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L02_Q131",
            "question": "Eshik ochilganda asosiy yurish yo'lini butunlay yopmasligi kerakmi?",
            "explanation": (
                "Door opening circulation bilan birga tekshirilishi kerak."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L02_Q132",
            "question": "Rejani faqat bitta odam harakatiga qarab tekshirish yetarlimi?",
            "explanation": (
                "Uyda bir vaqtning o'zida bir nechta odam harakatlanishi mumkin."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
    ],

    "L02_M09_005": [
        {
            "code": "L02_Q133",
            "question": "Entrance auditida storage va circulation birgalikda tekshiriladimi?",
            "explanation": (
                "Kirish zonasidagi barcha funksiyalar bir-biriga xalaqit bermasligi kerak."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L02_Q134",
            "question": "Chiroyli entrance avtomatik ravishda funksional entrance hisoblanadimi?",
            "explanation": (
                "Estetikadan tashqari tambur, storage, door va circulation ham tekshiriladi."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L02_Q135",
            "question": "Kirish va koridorni loyihalashdagi to'g'ri yondashuv qaysi?",
            "explanation": (
                "Entrance, storage, hallway va door conflictlar yagona circulation tizimi sifatida ko'riladi."
            ),
            "options": [
                (
                    "A",
                    "Entrance → storage → hallway → door conflict → audit",
                    True,
                ),
                (
                    "B",
                    "Faqat koridorni uzunroq qilish",
                    False,
                ),
            ],
        },
    ],
}


# ============================================================
# DATABASE SEED
# ============================================================

def seed_level02_module09():
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
        ) in LEVEL02_MODULE09_LESSONS:

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
