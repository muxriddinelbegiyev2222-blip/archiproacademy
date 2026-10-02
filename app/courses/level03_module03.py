from database.database import get_connection


# ============================================================
# LEVEL 3
# MODULE 03 - KO'CHA VA KIRISH
# ============================================================

LEVEL03_MODULE03_LESSONS = [
    (
        "L03_M03",
        "L03_M03_001",
        "Ko'cha va uchastka aloqasi",
        "theory",
        "Uchastkaning ko'cha bilan aloqasini loyiha boshlanishidan oldin tahlil qilish.",
        1,
        35,
        20,
    ),
    (
        "L03_M03",
        "L03_M03_002",
        "Piyoda kirishi",
        "theory",
        "Darvoza, kirish eshigi va piyoda yo'lini mantiqiy tashkil qilish.",
        2,
        35,
        20,
    ),
    (
        "L03_M03",
        "L03_M03_003",
        "Avtomobil kirishi",
        "theory",
        "Mashina kirishi, parking va uy kirishi o'rtasidagi aloqani tushunish.",
        3,
        40,
        20,
    ),
    (
        "L03_M03",
        "L03_M03_004",
        "Mehmon va xo'jalik harakati",
        "practice",
        "Mehmon, oila va service harakatlarini bir-biriga xalaqit bermaydigan tarzda rejalash.",
        4,
        40,
        20,
    ),
    (
        "L03_M03",
        "L03_M03_005",
        "Kirish sxemasidagi xatolar",
        "practice",
        "Uchastkadagi piyoda va avtomobil kirishlarining tipik rejalash xatolarini aniqlash.",
        5,
        50,
        25,
    ),
]


# ============================================================
# CONTENT
# ============================================================

LEVEL03_MODULE03_CONTENT = {
    "L03_M03_001": [
        {
            "title": "Ko'cha — uchastkaning tashqi aloqasi",
            "type": "highlight",
            "text": """
            Uchastka alohida orol emas.

            <br><br>

            Uning tashqi dunyo bilan
            asosiy aloqasi ko'cha orqali amalga oshadi.

            <br><br>

            Shu sababli uy joylashuvidan oldin
            ko'chaning qayerdaligini tushunish kerak.
            """,
        },
        {
            "title": "Ko'chadan nima keladi?",
            "type": "normal",
            "text": """
            Ko'cha tomondan:

            <br><br>

            • piyoda;<br>
            • avtomobil;<br>
            • mehmon;<br>
            • yetkazib berish;<br>
            • servis;<br>
            • shovqin;<br>
            • chang;<br>
            • ko'rinish

            <br><br>

            kelishi mumkin.
            """,
        },
        {
            "title": "Tasavvur qiling",
            "type": "example",
            "text": """
            Uchastka juda chiroyli.

            <br><br>

            Uy ham yaxshi joylashtirilgan.

            <br><br>

            Lekin darvozadan uy eshigigacha
            aniq piyoda yo'li yo'q.

            <br><br>

            Mehmon qayerdan yurishini tushunmaydi.

            <br><br>

            Demak tashqi circulation zaif.
            """,
        },
        {
            "title": "Ko'cha tomoni fasadga ham ta'sir qiladi",
            "type": "normal",
            "text": """
            Ko'cha tomoni ko'pincha:

            <br><br>

            • asosiy kirish;<br>
            • darvoza;<br>
            • parking;<br>
            • reprezentativ fasad

            <br><br>

            bilan bog'lanadi.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Bir uchastka planini oling.

            <br><br>

            Belgilang:

            <br><br>

            • ko'cha;<br>
            • trotuar;<br>
            • piyoda kirishi;<br>
            • mashina kirishi;<br>
            • uy eshigi.
            """,
        },
    ],

    "L03_M03_002": [
        {
            "title": "Piyoda kirishi tushunarli bo'lishi kerak",
            "type": "highlight",
            "text": """
            Mehmon darvozadan kirganda
            uy eshigi qayerdaligini
            tabiiy ravishda tushunishi kerak.
            """,
        },
        {
            "title": "Kirish ketma-ketligi",
            "type": "normal",
            "text": """
            Oddiy sxema:

            <br><br>

            <b>
            ko'cha → darvoza →
            piyoda yo'li → ayvon →
            asosiy eshik
            </b>
            """,
        },
        {
            "title": "To'g'ridan-to'g'ri ko'rinish",
            "type": "example",
            "text": """
            Har doim eshik darvozadan
            to'g'ridan-to'g'ri ko'rinishi shart emas.

            <br><br>

            Lekin yo'nalish tushunarli bo'lishi kerak.
            """,
        },
        {
            "title": "Piyoda va mashina",
            "type": "warning",
            "text": """
            Piyoda yo'li faqat
            avtomobil yo'lining chetidan
            majburan o'tsa,

            <br><br>

            qulaylik va xavfsizlik pasayishi mumkin.
            """,
        },
        {
            "title": "Ayvon",
            "type": "normal",
            "text": """
            Kirish ayvoni:

            <br><br>

            • eshik oldida to'xtash;<br>
            • yomg'irdan himoya;<br>
            • kutish;<br>
            • kirish kompozitsiyasi

            <br><br>

            uchun ishlashi mumkin.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Darvozadan uy eshigigacha
            bo'lgan yo'lni chizing.

            <br><br>

            Mehmon hech qanday tushuntirishsiz
            to'g'ri eshikni topa oladimi?
            """,
        },
    ],

    "L03_M03_003": [
        {
            "title": "Mashina ham circulation yaratadi",
            "type": "highlight",
            "text": """
            Avtomobilni uchastkaga kiritish
            faqat parking joyi topish emas.

            <br><br>

            Mashina kiradi,
            buriladi,
            to'xtaydi
            va yana chiqadi.
            """,
        },
        {
            "title": "Kirishdan parkinggacha",
            "type": "normal",
            "text": """
            Tekshiring:

            <br><br>

            • darvoza qayerda;<br>
            • mashina qaysi yo'nalishda kiradi;<br>
            • qayerda to'xtaydi;<br>
            • odam mashinadan tushgach qayerga yuradi.
            """,
        },
        {
            "title": "Parking va uy kirishi",
            "type": "example",
            "text": """
            Oila har kuni avtomobildan foydalanadi.

            <br><br>

            Parking uy kirishidan
            juda uzoqda bo'lsa,

            <br><br>

            kundalik foydalanish noqulay bo'lishi mumkin.
            """,
        },
        {
            "title": "Hovlini kesib o'tish",
            "type": "warning",
            "text": """
            Mashina yo'li
            asosiy dam olish hovlisini
            o'rtadan kesib o'tsa,

            <br><br>

            yashash sifati pasayishi mumkin.
            """,
        },
        {
            "title": "Burilish haqida o'ylang",
            "type": "normal",
            "text": """
            Plan chizishda faqat
            mashina konturini qo'yish yetmaydi.

            <br><br>

            Uning real harakat yo'li ham
            tasavvur qilinadi.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Ikki avtomobil uchun
            uchastka sxemasini oling.

            <br><br>

            Har bir mashina:

            <br><br>

            • qanday kiradi;<br>
            • qayerga turadi;<br>
            • qanday chiqadi

            <br><br>

            deb tekshiring.
            """,
        },
    ],

    "L03_M03_004": [
        {
            "title": "Bir uchastkada bir nechta oqim",
            "type": "highlight",
            "text": """
            Hamma odam uchastkadan
            bir xil maqsadda foydalanmaydi.
            """,
        },
        {
            "title": "Oila oqimi",
            "type": "normal",
            "text": """
            Oila uchun:

            <br><br>

            • kundalik piyoda kirish;<br>
            • avtomobildan uyga kirish;<br>
            • bolalar harakati;<br>
            • hovliga chiqish

            <br><br>

            muhim.
            """,
        },
        {
            "title": "Mehmon oqimi",
            "type": "normal",
            "text": """
            Mehmon:

            <br><br>

            darvoza → asosiy kirish →
            mehmonxona

            <br><br>

            yo'lini tushunarli topishi foydali.
            """,
        },
        {
            "title": "Service oqimi",
            "type": "example",
            "text": """
            Masalan:

            <br><br>

            mahsulot olib kelish,
            chiqindi chiqarish,
            hovli servis ishlari

            <br><br>

            har doim asosiy mehmon yo'li bilan
            bir xil bo'lishi shart emas.
            """,
        },
        {
            "title": "To'qnashuv",
            "type": "warning",
            "text": """
            Mehmon kirishi,
            mashina kirishi va
            xo'jalik harakati

            <br><br>

            bitta tor nuqtada to'qnashsa,
            uchastka tartibsiz ishlashi mumkin.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Site plan ustida uchta yo'l chizing:

            <br><br>

            1. Oila<br>
            2. Mehmon<br>
            3. Service

            <br><br>

            Qayerda ular bir-birini kesadi?
            """,
        },
    ],

    "L03_M03_005": [
        {
            "title": "Kirish xatolarini ovlaymiz",
            "type": "highlight",
            "text": """
            Endi uchastkaning
            tashqi circulation tizimini
            professional tarzda tekshiramiz.
            """,
        },
        {
            "title": "Xato 1 — asosiy eshik yashirin",
            "type": "warning",
            "text": """
            Darvozadan kirganda
            uyda bir nechta eshik ko'rinadi.

            <br><br>

            Qaysi biri asosiy kirish
            ekanligi tushunarsiz.
            """,
        },
        {
            "title": "Xato 2 — piyoda yo'li yo'q",
            "type": "warning",
            "text": """
            Piyoda darvozadan kirgach
            avtomobil yo'li bo'ylab yurishga majbur.
            """,
        },
        {
            "title": "Xato 3 — parking hovlini egallagan",
            "type": "warning",
            "text": """
            Mashina uchun qulaylik yaratilib,
            butun yaxshi hovli maydoni
            avtomobil harakatiga berilgan.
            """,
        },
        {
            "title": "Xato 4 — mashina yo'li living oldidan o'tadi",
            "type": "warning",
            "text": """
            Livingning katta oynalari oldidan
            avtomobillar doim o'tadi.

            <br><br>

            Bu privacy va hovli sifatiga
            salbiy ta'sir qilishi mumkin.
            """,
        },
        {
            "title": "Xato 5 — service va mehmon bitta nuqtada",
            "type": "warning",
            "text": """
            Chiqindi chiqarish,
            mahsulot tushirish va
            mehmon kirishi

            <br><br>

            bir xil kichik ayvonda to'qnashadi.
            """,
        },
        {
            "title": "Professional checklist",
            "type": "example",
            "text": """
            Uchastkani tekshirganda:

            <br><br>

            <b>1.</b> Ko'cha qayerda?<br><br>
            <b>2.</b> Piyoda qayerdan kiradi?<br><br>
            <b>3.</b> Mashina qayerdan kiradi?<br><br>
            <b>4.</b> Parking qayerda?<br><br>
            <b>5.</b> Asosiy eshik tushunarlimi?<br><br>
            <b>6.</b> Service oqimi qayerda?<br><br>
            <b>7.</b> Oqimlar to'qnashyaptimi?
            """,
        },
        {
            "title": "Mini-loyiha",
            "type": "example",
            "text": """
            Oldingi site analysis uchastkangizga:

            <br><br>

            • piyoda darvozasi;<br>
            • avtomobil darvozasi;<br>
            • parking;<br>
            • asosiy kirish;<br>
            • service yo'li

            <br><br>

            ni joylashtiring.

            <br><br>

            Keyin uch xil rangli chiziq bilan:

            <br><br>

            OILA / MEHMON / SERVICE

            <br><br>

            harakatini ko'rsating.
            """,
        },
        {
            "title": "Modul yakuni",
            "type": "highlight",
            "text": """
            Siz endi:

            <br><br>

            ✓ ko'cha va uchastka aloqasi;<br>
            ✓ piyoda kirishi;<br>
            ✓ avtomobil kirishi;<br>
            ✓ parking aloqasi;<br>
            ✓ mehmon oqimi;<br>
            ✓ service harakati;<br>
            ✓ tashqi circulation xatolari

            <br><br>

            ni tahlil qila olasiz.

            <br><br>

            Keyingi modul:
            <b>Uy joylashtirish.</b>
            """,
        },
    ],
}


# ============================================================
# QUIZ
# ============================================================

LEVEL03_MODULE03_QUIZ = {
    "L03_M03_001": [
        {
            "code": "L03_Q031",
            "question": "Uchastkaning ko'cha bilan aloqasi loyiha qarorlariga ta'sir qiladimi?",
            "explanation": (
                "Ko'cha piyoda, avtomobil, mehmon, shovqin va boshqa tashqi aloqalarning asosiy manbai."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L03_Q032",
            "question": "Darvozadan uyga aniq yo'l bo'lmasa bu circulation muammosimi?",
            "explanation": (
                "Kirish yo'nalishi foydalanuvchiga tushunarli bo'lishi kerak."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L03_Q033",
            "question": "Ko'cha tomoni asosiy fasadga ta'sir qilishi mumkinmi?",
            "explanation": (
                "Darvoza va asosiy kirish ko'pincha ko'cha tomoni bilan bog'lanadi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L03_M03_002": [
        {
            "code": "L03_Q034",
            "question": "Piyoda kirish yo'li tushunarli bo'lishi kerakmi?",
            "explanation": (
                "Mehmon darvozadan asosiy eshikkacha yo'nalishni oson tushunishi kerak."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L03_Q035",
            "question": "Piyoda va avtomobil yo'li doim aynan bir xil bo'lishi shartmi?",
            "explanation": (
                "Ularni qulaylik va xavfsizlik uchun ajratish mumkin."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L03_Q036",
            "question": "Kirish ayvoni faqat dekorativ elementmi?",
            "explanation": (
                "U himoya, kutish va kirish kompozitsiyasi vazifasini ham bajaradi."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
    ],

    "L03_M03_003": [
        {
            "code": "L03_Q037",
            "question": "Parkingni loyihalashda mashinaning real harakati ham hisobga olinadimi?",
            "explanation": (
                "Mashina kirishi, burilishi, to'xtashi va chiqishi tahlil qilinadi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L03_Q038",
            "question": "Parkingning uy kirishiga aloqasi kundalik qulaylikka ta'sir qiladimi?",
            "explanation": (
                "Oilada avtomobil doim ishlatilsa bu aloqa muhim."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L03_Q039",
            "question": "Mashina yo'lining dam olish hovlisini kesib o'tishi muammo bo'lishi mumkinmi?",
            "explanation": (
                "Avtomobil harakati hovli qulayligi va xavfsizligiga ta'sir qilishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L03_M03_004": [
        {
            "code": "L03_Q040",
            "question": "Mehmon va service oqimlari har doim bir xil bo'lishi shartmi?",
            "explanation": (
                "Turli funksiyalar uchun alohida yoki nazoratli yo'nalishlar bo'lishi mumkin."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L03_Q041",
            "question": "Mehmonning asosiy kirishni oson topishi foydalimi?",
            "explanation": (
                "Bu tashqi circulationni tushunarli qiladi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L03_Q042",
            "question": "Service harakati genplanda ham hisobga olinadimi?",
            "explanation": (
                "Mahsulot, chiqindi va xo'jalik ishlari ham uchastka circulationining bir qismi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L03_M03_005": [
        {
            "code": "L03_Q043",
            "question": "Piyoda darvozasi bo'lib, piyoda yo'li bo'lmasa bu rejalash xatosi bo'lishi mumkinmi?",
            "explanation": (
                "Darvozadan uy eshigigacha davomiy va qulay yo'l bo'lishi kerak."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L03_Q044",
            "question": "Parking butun dam olish hovlisini egallashi yaxshi yechimmi?",
            "explanation": (
                "Avtomobil va yashash zonalari o'rtasida balans kerak."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L03_Q045",
            "question": "Site kirish auditida qaysi savol muhim?",
            "explanation": (
                "Piyoda, avtomobil va service oqimlarining to'qnashishi tekshiriladi."
            ),
            "options": [
                ("A", "Oqimlar qayerda to'qnashadi?", True),
                ("B", "Faqat tom rangi qanday?", False),
            ],
        },
    ],
}


# ============================================================
# DATABASE SEED
# ============================================================

def seed_level03_module03():
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
        ) in LEVEL03_MODULE03_LESSONS:

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
