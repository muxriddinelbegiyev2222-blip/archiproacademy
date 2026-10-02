from database.database import get_connection


# ============================================================
# LEVEL 3
# MODULE 06 - AVTOMOBIL ZONASI
# ============================================================

LEVEL03_MODULE06_LESSONS = [
    (
        "L03_M06",
        "L03_M06_001",
        "Parking zonasi qanday ishlaydi?",
        "theory",
        "Avtomobil kirishi, to'xtashi va chiqishini yagona tizim sifatida tushunish.",
        1,
        40,
        20,
    ),
    (
        "L03_M06",
        "L03_M06_002",
        "Bir va ikki avtomobil uchun parking",
        "theory",
        "Bir va ikki avtomobil uchun parking joylashuvlarini tahlil qilish.",
        2,
        40,
        20,
    ),
    (
        "L03_M06",
        "L03_M06_003",
        "Navес va carport",
        "theory",
        "Avtomobil soyaboni va uy arxitekturasi o'rtasidagi aloqani tushunish.",
        3,
        40,
        20,
    ),
    (
        "L03_M06",
        "L03_M06_004",
        "Mashina va piyoda xavfsizligi",
        "practice",
        "Avtomobil va piyoda yo'llari kesishuvini kamaytirish va xavfsiz circulation yaratish.",
        4,
        45,
        20,
    ),
    (
        "L03_M06",
        "L03_M06_005",
        "Parking xatolarini topish",
        "practice",
        "Avtomobil zonasidagi tipik rejalash va circulation xatolarini aniqlash.",
        5,
        55,
        25,
    ),
]


# ============================================================
# CONTENT
# ============================================================

LEVEL03_MODULE06_CONTENT = {
    "L03_M06_001": [
        {
            "title": "Parking — faqat to'xtash joyi emas",
            "type": "highlight",
            "text": """
            Avtomobil zonasi bir nechta harakatdan iborat:

            <br><br>

            • kirish;<br>
            • burilish;<br>
            • to'xtash;<br>
            • odam tushishi;<br>
            • uyga o'tish;<br>
            • qayta chiqish.

            <br><br>

            Shuning uchun parking
            faqat mashina konturi bilan tugamaydi.
            """,
        },
        {
            "title": "Kirishdan boshlang",
            "type": "normal",
            "text": """
            Avval savol:

            <br><br>

            <b>Mashina uchastkaga qayerdan kiradi?</b>

            <br><br>

            Keyin:

            <br><br>

            qayerga buriladi,
            qayerga to'xtaydi,
            qayerdan chiqadi?
            """,
        },
        {
            "title": "Tasavvur qiling",
            "type": "example",
            "text": """
            Parking chizmada juda chiroyli ko'rinadi.

            <br><br>

            Lekin mashina unga kirish uchun
            bir necha marta oldinga-orqaga yurishi kerak.

            <br><br>

            Demak parking joyi bor,
            lekin circulation zaif.
            """,
        },
        {
            "title": "Uy bilan aloqa",
            "type": "normal",
            "text": """
            Mashinadan tushgan odam:

            <br><br>

            • qayerdan uyga kiradi;<br>
            • yomg'irda qancha yuradi;<br>
            • yukni qayerdan olib kiradi

            <br><br>

            ham tekshiriladi.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Bitta parking sxemasi chizing.

            <br><br>

            Mashina harakatini
            strelkalar bilan ko'rsating:

            <br><br>

            KIRISH → TO'XTASH → CHIQISH
            """,
        },
    ],

    "L03_M06_002": [
        {
            "title": "Bir mashina va ikki mashina — bir xil emas",
            "type": "highlight",
            "text": """
            Ikki avtomobil uchun parking
            shunchaki ikki marta katta joy degani emas.

            <br><br>

            Ularning bir-biriga bog'liqligi ham muhim.
            """,
        },
        {
            "title": "Yonma-yon parking",
            "type": "normal",
            "text": """
            Ikki mashina yonma-yon tursa,
            har bir avtomobil
            nisbatan mustaqil chiqishi mumkin.
            """,
        },
        {
            "title": "Ketma-ket parking",
            "type": "normal",
            "text": """
            Bir avtomobil ikkinchisining orqasida tursa,
            oldingi yoki orqadagi mashina
            chiqishda bir-biriga bog'liq bo'lishi mumkin.
            """,
        },
        {
            "title": "Kundalik hayotni o'ylang",
            "type": "example",
            "text": """
            Oilada ikki kishi har kuni
            turli vaqtda ishga ketadi.

            <br><br>

            Ketma-ket parking
            doim mashina almashtirishga majbur qilishi mumkin.

            <br><br>

            Demak faqat sig'ish emas,
            foydalanish ssenariysi ham muhim.
            """,
        },
        {
            "title": "Eshik ochilishi",
            "type": "warning",
            "text": """
            Mashina sig'di,
            lekin eshiklarni ochishga joy qolmadi.

            <br><br>

            Bu real foydalanishdagi xato.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Ikki variant chizing:

            <br><br>

            1. Yonma-yon parking<br>
            2. Ketma-ket parking

            <br><br>

            Har birining
            kundalik afzallik va kamchiligini yozing.
            """,
        },
    ],

    "L03_M06_003": [
        {
            "title": "Navес — uchastka arxitekturasining bir qismi",
            "type": "highlight",
            "text": """
            Carport yoki navес
            faqat metall tom qo'yilgan joy emas.

            <br><br>

            U uy fasadi va
            umumiy site compositionga ta'sir qiladi.
            """,
        },
        {
            "title": "Uyga yopishtirilgan navес",
            "type": "normal",
            "text": """
            Navес uyga yaqin bo'lsa:

            <br><br>

            • uyga kirish qisqarishi;<br>
            • yomg'irdan himoya;<br>
            • service aloqasi yaxshilanishi

            <br><br>

            mumkin.
            """,
        },
        {
            "title": "Alohida navес",
            "type": "normal",
            "text": """
            Alohida carport esa
            uy fasadini ochiqroq qoldirishi mumkin.

            <br><br>

            Lekin piyoda aloqasi
            alohida hal qilinadi.
            """,
        },
        {
            "title": "Fasadni yopib qo'ymaslik",
            "type": "warning",
            "text": """
            Navес juda katta yoki
            noto'g'ri joylashsa,

            <br><br>

            asosiy fasad va kirish
            avtomobil zonasining ortida qolishi mumkin.
            """,
        },
        {
            "title": "Kompozitsiya",
            "type": "example",
            "text": """
            Uy va carport
            bir xil arxitektura tilida ishlashi mumkin:

            <br><br>

            • tom;<br>
            • ustun;<br>
            • material;<br>
            • proporsiya;<br>
            • yoritish.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Uyingiz uchun ikki variant yarating:

            <br><br>

            • uyga biriktirilgan navес;<br>
            • alohida navес.

            <br><br>

            Qaysi biri hovlini yaxshiroq saqlaydi?
            """,
        },
    ],

    "L03_M06_004": [
        {
            "title": "Mashina va odam bir joydan foydalanadi",
            "type": "highlight",
            "text": """
            Avtomobil zonasida
            eng muhim masalalardan biri —
            piyoda xavfsizligi.
            """,
        },
        {
            "title": "Kesishuvlar",
            "type": "normal",
            "text": """
            Tekshiring:

            <br><br>

            • bolalar yo'li;<br>
            • asosiy piyoda kirishi;<br>
            • guest yo'li;<br>
            • mashina kirishi

            <br><br>

            qayerda kesishadi?
            """,
        },
        {
            "title": "Ko'rish",
            "type": "example",
            "text": """
            Mashina orqaga chiqayotganda
            haydovchi piyodani ko'ra oladimi?

            <br><br>

            Devor, daraxt yoki boshqa element
            ko'rishni to'smayaptimi?
            """,
        },
        {
            "title": "Bolalar zonasi",
            "type": "warning",
            "text": """
            Bolalar o'yin maydoni
            parking chiqishiga juda yaqin bo'lsa,

            <br><br>

            xavfsizlik nuqtai nazaridan
            zaif yechim bo'lishi mumkin.
            """,
        },
        {
            "title": "Alohida piyoda yo'li",
            "type": "normal",
            "text": """
            Imkoniyat bo'lsa,
            piyoda va avtomobil yo'llari
            to'liq yoki qisman ajratiladi.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Site planingizda:

            <br><br>

            qizil chiziq — mashina<br>
            ko'k chiziq — piyoda

            <br><br>

            qilib ikkala harakatni chizing.

            <br><br>

            Kesishgan nuqtalarni belgilang.
            """,
        },
    ],

    "L03_M06_005": [
        {
            "title": "Parking xatolarini ovlaymiz",
            "type": "highlight",
            "text": """
            Endi avtomobil zonasini
            real foydalanish bo'yicha audit qilamiz.
            """,
        },
        {
            "title": "Xato 1 — mashina sig'di, chiqolmaydi",
            "type": "warning",
            "text": """
            Parking joyi yetarli.

            <br><br>

            Lekin chiqish uchun
            juda ko'p manevr qilish kerak.
            """,
        },
        {
            "title": "Xato 2 — eshik ochilmaydi",
            "type": "warning",
            "text": """
            Mashinalar bir-biriga
            yoki devorga juda yaqin.

            <br><br>

            Odam qulay tusholmaydi.
            """,
        },
        {
            "title": "Xato 3 — parking private hovlini egallagan",
            "type": "warning",
            "text": """
            Avtomobillar uchun
            eng yaxshi hovli hududi berilgan.

            <br><br>

            Family dam olish zonasi esa
            kichik va noqulay qolgan.
            """,
        },
        {
            "title": "Xato 4 — piyoda kirishi mashina orasidan",
            "type": "warning",
            "text": """
            Mehmon uyga kirish uchun
            park qilingan avtomobillar orasidan o'tadi.
            """,
        },
        {
            "title": "Xato 5 — navес fasadni yopgan",
            "type": "warning",
            "text": """
            Uy fasadining asosiy qismi
            katta carport ortida qolgan.

            <br><br>

            Kirish kompozitsiyasi zaiflashgan.
            """,
        },
        {
            "title": "Professional checklist",
            "type": "example",
            "text": """
            Parkingni tekshirganda:

            <br><br>

            <b>1.</b> Mashina qanday kiradi?<br><br>
            <b>2.</b> Qayerda buriladi?<br><br>
            <b>3.</b> Eshik ochiladimi?<br><br>
            <b>4.</b> Uyga yo'l qulaymi?<br><br>
            <b>5.</b> Piyoda bilan konflikt bormi?<br><br>
            <b>6.</b> Private hovli saqlanganmi?<br><br>
            <b>7.</b> Mashina qanday chiqadi?
            """,
        },
        {
            "title": "Mini-loyiha",
            "type": "example",
            "text": """
            Ikki avtomobilli uchastka yarating.

            <br><br>

            Unda:

            <br><br>

            • darvoza;<br>
            • parking;<br>
            • navес;<br>
            • piyoda yo'li;<br>
            • uy kirishi;<br>
            • family hovli

            <br><br>

            ni birgalikda joylashtiring.

            <br><br>

            Mashina va piyoda yo'llarini
            alohida strelkalar bilan ko'rsating.
            """,
        },
        {
            "title": "Modul yakuni",
            "type": "highlight",
            "text": """
            Siz endi:

            <br><br>

            ✓ parking circulation;<br>
            ✓ bir va ikki mashina sxemasi;<br>
            ✓ navес joylashtirish;<br>
            ✓ uy-parking aloqasi;<br>
            ✓ piyoda xavfsizligi;<br>
            ✓ avtomobil zonasi xatolari

            <br><br>

            ni tahlil qila olasiz.

            <br><br>

            Keyingi modul:
            <b>Relyef.</b>
            """,
        },
    ],
}


# ============================================================
# QUIZ
# ============================================================

LEVEL03_MODULE06_QUIZ = {
    "L03_M06_001": [
        {
            "code": "L03_Q076",
            "question": "Parking faqat mashina sig'adigan to'rtburchak joymi?",
            "explanation": (
                "Avtomobilning kirishi, burilishi, to'xtashi va chiqishi ham tahlil qilinadi."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L03_Q077",
            "question": "Parkingdan uyga piyoda yo'li muhimmi?",
            "explanation": (
                "Mashinadan tushgandan keyingi kundalik harakat ham site circulationga kiradi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L03_Q078",
            "question": "Mashina chiqish manevri ham oldindan tekshiriladimi?",
            "explanation": (
                "Parking ishlashi uchun kirish va chiqish real harakati tekshiriladi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L03_M06_002": [
        {
            "code": "L03_Q079",
            "question": "Ikki mashinani ketma-ket qo'yish ularni bir-biriga bog'lab qo'yishi mumkinmi?",
            "explanation": (
                "Bir mashina ikkinchisining chiqish yo'lini to'sishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L03_Q080",
            "question": "Mashina sig'ishi avtomatik ravishda parking qulayligini bildiradimi?",
            "explanation": (
                "Eshik ochilishi va real foydalanish zonasi ham muhim."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L03_Q081",
            "question": "Parking turi oilaning kundalik foydalanishiga bog'liqmi?",
            "explanation": (
                "Mashinalar qachon va kim tomonidan ishlatilishi parking sxemasiga ta'sir qiladi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L03_M06_003": [
        {
            "code": "L03_Q082",
            "question": "Navес uy arxitekturasiga ta'sir qiladimi?",
            "explanation": (
                "Carport fasad va site compositionning bir qismidir."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L03_Q083",
            "question": "Uyga yaqin navес yomg'irli paytda qulaylik berishi mumkinmi?",
            "explanation": (
                "Mashinadan uyga o'tish masofasi qisqarishi va himoyalanishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L03_Q084",
            "question": "Navес asosiy fasadni butunlay yopib qo'ysa bu kompozitsion muammo bo'lishi mumkinmi?",
            "explanation": (
                "Kirish va fasad avtomobil zonasining ortida qolishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L03_M06_004": [
        {
            "code": "L03_Q085",
            "question": "Piyoda va avtomobil yo'llarining kesishishi tekshiriladimi?",
            "explanation": (
                "Bu xavfsizlik va qulaylik uchun muhim."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L03_Q086",
            "question": "Bolalar zonasini mashina chiqishiga juda yaqin joylashtirish xavf tug'dirishi mumkinmi?",
            "explanation": (
                "Avtomobil va bolalar harakati ajratilishi foydali."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L03_Q087",
            "question": "Haydovchining ko'rish maydoni parking auditida muhimmi?",
            "explanation": (
                "Orqaga yurish va chiqishda piyodalarni ko'rish muhim."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L03_M06_005": [
        {
            "code": "L03_Q088",
            "question": "Parking joyi bor, lekin chiqish juda murakkab bo'lsa bu yaxshi yechimmi?",
            "explanation": (
                "Parking real harakatda ham qulay ishlashi kerak."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L03_Q089",
            "question": "Mehmonning park qilingan mashinalar orasidan yurishi zaif piyoda yechimi bo'lishi mumkinmi?",
            "explanation": (
                "Asosiy piyoda kirishi tushunarli va xavfsiz bo'lishi kerak."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L03_Q090",
            "question": "Parking auditida qaysi savol muhim?",
            "explanation": (
                "Kirish, burilish, to'xtash, piyoda va chiqish birgalikda tekshiriladi."
            ),
            "options": [
                ("A", "Mashina qanday kiradi va chiqadi?", True),
                ("B", "Faqat uy devori rangi qanday?", False),
            ],
        },
    ],
}


# ============================================================
# DATABASE SEED
# ============================================================

def seed_level03_module06():
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
        ) in LEVEL03_MODULE06_LESSONS:

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
