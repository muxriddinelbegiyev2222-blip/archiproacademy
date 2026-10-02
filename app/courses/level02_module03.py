from database.database import get_connection


# ============================================================
# LEVEL 2
# MODULE 03 - HARAKAT VA SIRKULYATSIYA
# ============================================================

LEVEL02_MODULE03_LESSONS = [
    (
        "L02_M03",
        "L02_M03_001",
        "Sirkulyatsiya nima?",
        "theory",
        "Uy ichidagi odamlar harakatini arxitektura elementi sifatida tushunish.",
        1,
        30,
        15,
    ),
    (
        "L02_M03",
        "L02_M03_002",
        "Asosiy va ikkilamchi harakat yo'llari",
        "theory",
        "Uy ichidagi muhim va kam ishlatiladigan yo'nalishlarni ajratish.",
        2,
        35,
        20,
    ),
    (
        "L02_M03",
        "L02_M03_003",
        "Koridor va o'tish zonalari",
        "theory",
        "Koridorning foydali va ortiqcha holatlarini farqlash.",
        3,
        35,
        20,
    ),
    (
        "L02_M03",
        "L02_M03_004",
        "Eshiklar va harakat to'qnashuvi",
        "practice",
        "Eshik ochilishi va yurish oqimlaridagi tipik xatolarni aniqlash.",
        4,
        40,
        20,
    ),
    (
        "L02_M03",
        "L02_M03_005",
        "Sirkulyatsiya xatolarini topish",
        "practice",
        "Real turar joy planidagi dead-end, kesishuvchi va keraksiz uzun yo'llarni tahlil qilish.",
        5,
        45,
        25,
    ),
]


# ============================================================
# LESSON CONTENT
# ============================================================

LEVEL02_MODULE03_CONTENT = {
    "L02_M03_001": [
        {
            "title": "Sirkulyatsiya nima?",
            "type": "highlight",
            "text": """
            Sirkulyatsiya — odamlarning bino ichida
            <b>bir joydan ikkinchi joyga harakat qilish tizimi</b>.

            <br><br>

            Yaxshi plan faqat xonalardan iborat emas.

            <br><br>

            Ularning orasida qulay harakat ham bo'lishi kerak.
            """,
        },
        {
            "title": "Tasavvur qiling",
            "type": "example",
            "text": """
            Kirish eshigidan oshxonaga borish uchun:

            <br><br>

            • mehmonxonani kesib o'tasiz;<br>
            • televizor oldidan o'tasiz;<br>
            • stol atrofidan aylanasiz;<br>
            • keyin yana koridorga kirasiz.

            <br><br>

            Bu sirkulyatsiya yaxshi tashkil qilinmagan bo'lishi mumkin.
            """,
        },
        {
            "title": "Harakat ham loyihaning bir qismi",
            "type": "normal",
            "text": """
            Plan chizayotganda odamning kundalik yo'llari
            oldindan ko'rib chiqiladi.

            <br><br>

            Masalan:

            <br><br>

            • kirish → mehmonxona;<br>
            • kirish → oshxona;<br>
            • yotoqxona → sanuzel;<br>
            • oshxona → ovqatlanish zonasi;<br>
            • hovli → uy.
            """,
        },
        {
            "title": "Boshlovchi xatosi",
            "type": "warning",
            "text": """
            Xonalarni joylashtirib bo'lgandan keyin:

            <br><br>

            “Endi qayerdan yuramiz?”

            <br><br>

            deb o'ylash kech bo'lishi mumkin.

            <br><br>

            Harakat yo'llari plan bilan birga shakllanadi.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            O'z uyingizda ertalab uyg'ongandan
            eshikdan chiqib ketguningizgacha
            qaysi yo'llardan yurishingizni eslang.

            <br><br>

            Qaysi harakatlar eng ko'p takrorlanadi?
            """,
        },
    ],

    "L02_M03_002": [
        {
            "title": "Barcha yo'llar bir xil emas",
            "type": "highlight",
            "text": """
            Uyda ayrim yo'nalishlar
            kuniga o'nlab marta ishlatiladi.

            <br><br>

            Ayrimlari esa juda kam.

            <br><br>

            Shuning uchun asosiy va ikkilamchi
            harakat yo'llarini ajratish foydali.
            """,
        },
        {
            "title": "Asosiy harakat yo'li",
            "type": "normal",
            "text": """
            Asosiy yo'l ko'p ishlatiladigan
            kundalik yo'nalish.

            <br><br>

            Masalan:

            <br><br>

            kirish → yashash zonasi;<br>
            oshxona → ovqatlanish;<br>
            yotoqxona → sanuzel.
            """,
        },
        {
            "title": "Ikkilamchi yo'l",
            "type": "normal",
            "text": """
            Kamroq ishlatiladigan yo'nalishlar
            ikkilamchi bo'lishi mumkin.

            <br><br>

            Masalan:

            <br><br>

            • texnik xona;<br>
            • ombor;<br>
            • kam ishlatiladigan yordamchi chiqish.
            """,
        },
        {
            "title": "Muhim qoida",
            "type": "highlight",
            "text": """
            <b>
            Eng ko'p ishlatiladigan yo'llar
            eng murakkab bo'lmasligi kerak.
            </b>
            """,
        },
        {
            "title": "Xato",
            "type": "warning",
            "text": """
            Oshxona va ovqatlanish zonasi
            har kuni ishlatiladi.

            <br><br>

            Lekin ular orasida uzun va burilishli yo'l bor.

            <br><br>

            Bu asosiy harakat yo'lining
            keraksiz murakkablashtirilganini ko'rsatishi mumkin.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Bir uy planini tanlang.

            <br><br>

            Unda 3 ta eng ko'p ishlatiladigan
            yo'nalishni yozing.

            <br><br>

            Qaysi biri eng uzun?
            """,
        },
    ],

    "L02_M03_003": [
        {
            "title": "Koridor yomon narsa emas",
            "type": "highlight",
            "text": """
            Koridorning o'zi xato emas.

            <br><br>

            Muammo — uning
            <b>keraksiz uzun, keng yoki ko'p bo'lishi</b>.
            """,
        },
        {
            "title": "Koridorning vazifasi",
            "type": "normal",
            "text": """
            Koridor:

            <br><br>

            • xonalarni bog'laydi;<br>
            • private zonani ajratadi;<br>
            • odamlar harakatini tashkil qiladi;<br>
            • xonalarga mustaqil kirish beradi.
            """,
        },
        {
            "title": "Qachon muammo bo'ladi?",
            "type": "warning",
            "text": """
            200 m² uyda 35–40 m² faqat
            uzun yo'laklarga sarflansa,
            plan samaradorligini qayta tekshirish kerak.

            <br><br>

            Chunki koridor ko'pincha
            yashash funksiyasini bajarmaydigan maydon.
            """,
        },
        {
            "title": "Dead-end nima?",
            "type": "normal",
            "text": """
            Dead-end — yo'lning oxirida
            faqat bitta maqsadli nuqta bo'lgan
            berk yo'nalish.

            <br><br>

            Bu har doim xato emas.

            <br><br>

            Lekin juda uzun dead-end koridor
            foydasiz maydon yaratishi mumkin.
            """,
        },
        {
            "title": "Misol",
            "type": "example",
            "text": """
            8 metr uzun koridorning oxirida
            faqat bitta kichik ombor bor.

            <br><br>

            Demak, omborga yetish uchun
            katta maydon faqat yurish uchun ishlatilmoqda.

            <br><br>

            Buni boshqa usulda hal qilish mumkinmi?
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Bir plan toping.

            <br><br>

            Undagi barcha koridorlarni xayolan bo'yang.

            <br><br>

            Qaysi biri zarur?
            Qaysi biri qisqartirilishi mumkin?
            """,
        },
    ],

    "L02_M03_004": [
        {
            "title": "Eshik ham harakat tizimining qismi",
            "type": "highlight",
            "text": """
            Eshik faqat devordagi teshik emas.

            <br><br>

            Uning:

            <br><br>

            • joyi;<br>
            • ochilish tomoni;<br>
            • ochilish radiusi;<br>
            • boshqa eshiklar bilan aloqasi

            <br><br>

            sirkulyatsiyaga ta'sir qiladi.
            """,
        },
        {
            "title": "Ikki eshik to'qnashuvi",
            "type": "example",
            "text": """
            Koridorda ikki eshik bir-biriga qarama-qarshi.

            <br><br>

            Ikkalasi bir vaqtda ochilsa,
            bir-biriga uriladi.

            <br><br>

            Plan chizig'ida kichik detal.

            <br>
            Hayotda esa doimiy muammo.
            """,
        },
        {
            "title": "Eshik odamni devorga siqmasligi kerak",
            "type": "warning",
            "text": """
            Xonaga kirganda eshik ochilib,
            odamni tor burchakka yo'naltirsa,
            kirish noqulay bo'lishi mumkin.

            <br><br>

            Odamning keyingi harakati
            oldindan tasavvur qilinadi.
            """,
        },
        {
            "title": "Kirish eshigi va garderob",
            "type": "example",
            "text": """
            Uyga kirdingiz.

            <br><br>

            Kirish eshigi ochilganda
            garderob eshigini to'sadi.

            <br><br>

            Ikkala element mavjud,
            lekin bir vaqtda ishlamaydi.
            """,
        },
        {
            "title": "Professional tekshiruv",
            "type": "highlight",
            "text": """
            <b>
            Eshikni planda chizgandan keyin
            uni xayolan oching.
            </b>

            <br><br>

            Keyin odam qayerga qadam qo'yishini tekshiring.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Bir plan ichida barcha eshiklarni tekshiring.

            <br><br>

            Kamida 3 savol:

            <br><br>

            1. Eshik boshqa eshikka uriladimi?<br>
            2. Mebelga uriladimi?<br>
            3. Odamning yurish yo'lini to'sadimi?
            """,
        },
    ],

    "L02_M03_005": [
        {
            "title": "Sirkulyatsiya xatolarini ovlaymiz",
            "type": "highlight",
            "text": """
            Endi plan ichida xonalar emas,
            odamlarning butun harakat tizimini ko'ramiz.
            """,
        },
        {
            "title": "Xato 1 — asosiy yo'llar kesishadi",
            "type": "warning",
            "text": """
            Kirishdan oshxonaga,
            yotoqxonadan sanuzelga va
            mehmonxonadan hovliga yo'llar
            bitta tor nuqtada kesishadi.

            <br><br>

            Bu “tirbandlik” zonasi yaratishi mumkin.
            """,
        },
        {
            "title": "Xato 2 — keraksiz uzun koridor",
            "type": "warning",
            "text": """
            Koridor uzun.

            <br><br>

            Lekin uning ikkala tomonida
            deyarli hech qanday xona yo'q.

            <br><br>

            Maydon samaradorligi past.
            """,
        },
        {
            "title": "Xato 3 — private yo'l public zonadan o'tadi",
            "type": "warning",
            "text": """
            Yotoqxonadan sanuzelga borish uchun
            mehmonxona ichidan o'tish kerak.

            <br><br>

            Bu private circulation
            noto'g'ri tashkil qilinganini ko'rsatishi mumkin.
            """,
        },
        {
            "title": "Xato 4 — service harakati markazda",
            "type": "warning",
            "text": """
            Kir yuvish, chiqindi yoki mahsulot tashish
            yo'li doim asosiy mehmon zonasidan o'tadi.

            <br><br>

            Service circulation qayta ko'rilishi mumkin.
            """,
        },
        {
            "title": "Xato 5 — berk va foydasiz yo'l",
            "type": "warning",
            "text": """
            Uzoq koridorning oxirida
            faqat bitta kam ishlatiladigan xona bor.

            <br><br>

            Bu dead-end yo'lni
            boshqa usulda tashkil qilish mumkinligini ko'rsatishi mumkin.
            """,
        },
        {
            "title": "Professional tahlil algoritmi",
            "type": "example",
            "text": """
            Plan oldingizda bo'lsa:

            <br><br>

            <b>1.</b> Kirishdan odam qayerga yuradi?<br><br>
            <b>2.</b> Eng ko'p ishlatiladigan yo'llar qaysi?<br><br>
            <b>3.</b> Qaysi yo'llar kesishmoqda?<br><br>
            <b>4.</b> Qayerda dead-end bor?<br><br>
            <b>5.</b> Qayerda ortiqcha koridor bor?<br><br>
            <b>6.</b> Public/private/service oqimlar aralashganmi?
            """,
        },
        {
            "title": "Mini-loyiha",
            "type": "example",
            "text": """
            150–250 m² bir qavatli uy planini toping.

            <br><br>

            4 ta yo'nalishni belgilang:

            <br><br>

            • kirish → mehmonxona;<br>
            • kirish → oshxona;<br>
            • yotoqxona → sanuzel;<br>
            • oshxona → hovli.

            <br><br>

            Keyin kamida 2 ta
            sirkulyatsiya muammosini aniqlang.
            """,
        },
        {
            "title": "Modul yakuni",
            "type": "highlight",
            "text": """
            Siz endi:

            <br><br>

            ✓ sirkulyatsiya;<br>
            ✓ asosiy harakat yo'li;<br>
            ✓ ikkilamchi yo'l;<br>
            ✓ koridor samaradorligi;<br>
            ✓ dead-end;<br>
            ✓ eshik to'qnashuvi;<br>
            ✓ public/private/service circulation

            <br><br>

            tushunchalarini tahlil qila olasiz.

            <br><br>

            Keyingi modul:
            <b>Xona proporsiyasi va makon sifati.</b>
            """,
        },
    ],
}


# ============================================================
# QUIZ DATA
# ============================================================

LEVEL02_MODULE03_QUIZ = {
    "L02_M03_001": [
        {
            "code": "L02_Q031",
            "question": "Sirkulyatsiya nima?",
            "explanation": (
                "Sirkulyatsiya odamlarning bino ichida bir joydan boshqa joyga harakat qilish tizimidir."
            ),
            "options": [
                ("A", "Odamlarning harakat tizimi", True),
                ("B", "Faqat fasad materiali", False),
                ("C", "Faqat tom shakli", False),
            ],
        },
        {
            "code": "L02_Q032",
            "question": "Harakat yo'llari plan tugagandan keyingina o'ylanadimi?",
            "explanation": (
                "Harakat tizimi plan bilan birga shakllantiriladi."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L02_Q033",
            "question": "Kirishdan oshxonaga yo'l ham sirkulyatsiya tahliliga kiradimi?",
            "explanation": (
                "Kundalik yo'nalishlarning barchasi sirkulyatsiya tizimining bir qismi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L02_M03_002": [
        {
            "code": "L02_Q034",
            "question": "Asosiy harakat yo'li qanday yo'l?",
            "explanation": (
                "Ko'p ishlatiladigan kundalik yo'nalish asosiy harakat yo'li hisoblanadi."
            ),
            "options": [
                ("A", "Ko'p ishlatiladigan yo'l", True),
                ("B", "Faqat kam ishlatiladigan yo'l", False),
            ],
        },
        {
            "code": "L02_Q035",
            "question": "Eng ko'p ishlatiladigan yo'lni murakkab qilish foydalimi?",
            "explanation": (
                "Ko'p ishlatiladigan yo'llar imkon qadar sodda va qulay bo'lishi kerak."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L02_Q036",
            "question": "Texnik xonaga yo'l ikkilamchi harakat bo'lishi mumkinmi?",
            "explanation": (
                "Kam ishlatiladigan service yo'nalishlari ikkilamchi bo'lishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L02_M03_003": [
        {
            "code": "L02_Q037",
            "question": "Koridorning o'zi har doim xatomi?",
            "explanation": (
                "Koridor zarur harakat va xonalarni bog'lash uchun foydali bo'lishi mumkin."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L02_Q038",
            "question": "Juda uzun va kam foydalaniladigan koridor nimani kamaytirishi mumkin?",
            "explanation": (
                "U foydali maydon samaradorligini kamaytirishi mumkin."
            ),
            "options": [
                ("A", "Maydon samaradorligini", True),
                ("B", "Faqat deraza sonini", False),
            ],
        },
        {
            "code": "L02_Q039",
            "question": "Dead-end nima?",
            "explanation": (
                "Berk tugaydigan yoki oxirida cheklangan maqsadga olib boradigan harakat yo'li."
            ),
            "options": [
                ("A", "Berk tugaydigan yo'nalish", True),
                ("B", "Faqat fasad turi", False),
            ],
        },
    ],

    "L02_M03_004": [
        {
            "code": "L02_Q040",
            "question": "Eshik ochilish yo'nalishi sirkulyatsiyaga ta'sir qiladimi?",
            "explanation": (
                "Eshik ochilishi odam yurishi va boshqa elementlardan foydalanishga ta'sir qiladi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L02_Q041",
            "question": "Ikki eshik bir-biriga urilsa bu qanday muammo?",
            "explanation": (
                "Bu eshik ochilishi va harakat tashkilotidagi xato."
            ),
            "options": [
                ("A", "Harakat va ergonomika xatosi", True),
                ("B", "Har doim yaxshi yechim", False),
            ],
        },
        {
            "code": "L02_Q042",
            "question": "Eshikni chizgandan keyin uni xayolan ochib ko'rish foydalimi?",
            "explanation": (
                "Bu ochilish radiusi va keyingi harakatni tekshirishga yordam beradi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L02_M03_005": [
        {
            "code": "L02_Q043",
            "question": "Bir nechta asosiy yo'l bitta tor nuqtada kesishsa nima paydo bo'lishi mumkin?",
            "explanation": (
                "Harakat tirbandligi va to'qnashuvi paydo bo'lishi mumkin."
            ),
            "options": [
                ("A", "Tirbandlik zonasi", True),
                ("B", "Har doim yaxshi kompozitsiya", False),
            ],
        },
        {
            "code": "L02_Q044",
            "question": "Private harakat yo'li public zona ichidan majburan o'tishi muammo bo'lishi mumkinmi?",
            "explanation": (
                "Bu maxfiylik va zonalashni zaiflashtirishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L02_Q045",
            "question": "Sirkulyatsiya tahlilida qaysi savol foydali?",
            "explanation": (
                "Eng ko'p ishlatiladigan va kesishadigan yo'llarni aniqlash muhim."
            ),
            "options": [
                ("A", "Qaysi yo'llar eng ko'p ishlatiladi?", True),
                ("B", "Faqat fasad rangi qanday?", False),
            ],
        },
    ],
}


# ============================================================
# DATABASE SEED
# ============================================================

def seed_level02_module03():
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
        ) in LEVEL02_MODULE03_LESSONS:

            cursor.execute(
                """
                SELECT id
                FROM course_modules
                WHERE code = ?
                LIMIT 1
                """,
                (
                    module_code,
                ),
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
