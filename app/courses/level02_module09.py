from database.database import get_connection


# ============================================================
# LEVEL 2
# MODULE 09 - BOLALAR XONASI VA OILAVIY MAKON
# ============================================================

LEVEL02_MODULE09_LESSONS = [
    (
        "L02_M09",
        "L02_M09_001",
        "Bolalar xonasi qanday ishlaydi?",
        "theory",
        "Bolalar xonasini uyqu, o'qish, o'yin va saqlash funksiyalari asosida loyihalash.",
        1,
        35,
        20,
    ),
    (
        "L02_M09",
        "L02_M09_002",
        "Yoshga qarab xona o'zgarishi",
        "theory",
        "Bola ulg'aygani sari xonaning funksional talablari qanday o'zgarishini tushunish.",
        2,
        35,
        20,
    ),
    (
        "L02_M09",
        "L02_M09_003",
        "Ikki bola bir xonada",
        "theory",
        "Ikki foydalanuvchi uchun uyqu, o'qish, saqlash va shaxsiy hududlarni tashkil qilish.",
        3,
        40,
        20,
    ),
    (
        "L02_M09",
        "L02_M09_004",
        "Xavfsizlik va oilaviy aloqa",
        "practice",
        "Bolalar xonasining ota-ona, sanuzel va umumiy makonlar bilan aloqasini tahlil qilish.",
        4,
        40,
        20,
    ),
    (
        "L02_M09",
        "L02_M09_005",
        "Bolalar xonasi xatolarini topish",
        "practice",
        "Real planlarda bolalar xonasi ergonomikasi, zonalash va kelajakdagi moslashuv xatolarini aniqlash.",
        5,
        45,
        25,
    ),
]


# ============================================================
# CONTENT
# ============================================================

LEVEL02_MODULE09_CONTENT = {
    "L02_M09_001": [
        {
            "title": "Bolalar xonasi — bir nechta xona vazifasi",
            "type": "highlight",
            "text": """
            Bolalar xonasi ko'pincha bir vaqtning o'zida:

            <br><br>

            • yotoqxona;<br>
            • o'qish joyi;<br>
            • o'yin maydoni;<br>
            • kiyim saqlash joyi;<br>
            • shaxsiy hudud

            <br><br>

            vazifasini bajaradi.
            """,
        },
        {
            "title": "To'rtta asosiy zona",
            "type": "normal",
            "text": """
            Bolalar xonasini tahlil qilganda
            kamida to'rtta zonani tekshiramiz:

            <br><br>

            <b>1. Uyqu</b><br>
            <b>2. O'qish</b><br>
            <b>3. O'yin yoki bo'sh faoliyat</b><br>
            <b>4. Saqlash</b>
            """,
        },
        {
            "title": "Tasavvur qiling",
            "type": "example",
            "text": """
            Xona 14 m².

            <br><br>

            Krovat, shkaf va stol sig'di.

            <br><br>

            Lekin stolga o'tirish uchun
            stulni orqaga surib bo'lmaydi.

            <br><br>

            Demak mebel sig'di,
            ammo xona to'liq ishlamayapti.
            """,
        },
        {
            "title": "O'yin uchun bo'sh makon",
            "type": "normal",
            "text": """
            Ayniqsa kichik yoshdagi bolalarda
            xonaning markaziy bo'sh maydoni
            juda foydali bo'lishi mumkin.

            <br><br>

            Har bir devorni mebel bilan to'ldirish
            shart emas.
            """,
        },
        {
            "title": "Boshlovchi xatosi",
            "type": "warning",
            "text": """
            Xonaga maksimal miqdorda mebel joylashtirish
            bolalar xonasini yaxshi qilmaydi.

            <br><br>

            Bola harakati uchun bo'sh makon ham
            funksiyaning bir qismidir.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Bir bolalar xonasi planini oling.

            <br><br>

            Unda belgilang:

            <br><br>

            • uyqu;<br>
            • o'qish;<br>
            • o'yin;<br>
            • saqlash.

            <br><br>

            To'rttalasi bir-biriga xalaqit bermayaptimi?
            """,
        },
    ],

    "L02_M09_002": [
        {
            "title": "Bola ulg'ayadi — xona ham o'zgaradi",
            "type": "highlight",
            "text": """
            4 yoshli bola uchun qulay xona
            14 yoshli bola uchun aynan shu holatda
            qulay bo'lishi shart emas.

            <br><br>

            Professional loyiha
            kelajakdagi o'zgarishni ham o'ylaydi.
            """,
        },
        {
            "title": "Kichik yosh",
            "type": "normal",
            "text": """
            Kichik yoshdagi bola uchun:

            <br><br>

            • ota-onaga yaqinlik;<br>
            • xavfsiz harakat;<br>
            • o'yin maydoni;<br>
            • oddiy saqlash

            <br><br>

            muhim bo'lishi mumkin.
            """,
        },
        {
            "title": "Maktab yoshi",
            "type": "normal",
            "text": """
            Keyinchalik:

            <br><br>

            • normal ish stoli;<br>
            • kitoblar uchun saqlash;<br>
            • kompyuter;<br>
            • yaxshiroq yoritish;<br>
            • ko'proq shaxsiy hudud

            <br><br>

            kerak bo'lishi mumkin.
            """,
        },
        {
            "title": "O'smirlik davri",
            "type": "example",
            "text": """
            O'smir uchun xonaning
            private xarakteri kuchayadi.

            <br><br>

            Do'st bilan o'tirish,
            katta ish stoli,
            kiyim saqlash va
            texnika uchun joy talab qilinishi mumkin.
            """,
        },
        {
            "title": "Transformatsiya",
            "type": "highlight",
            "text": """
            <b>
            Yaxshi bolalar xonasi
            qimmat rekonstruksiyasiz
            yoshga mos o'zgarishi mumkin.
            </b>
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Bitta xona uchun
            ikki variant o'ylang:

            <br><br>

            • 6 yoshli bola;<br>
            • 16 yoshli bola.

            <br><br>

            Qaysi mebellar o'zgaradi?
            Qaysi elementlar o'z joyida qoladi?
            """,
        },
    ],

    "L02_M09_003": [
        {
            "title": "Ikki bola — ikki foydalanuvchi",
            "type": "highlight",
            "text": """
            Bitta xonada ikki bola yashasa,
            masala faqat ikkita krovat sig'dirish emas.
            """,
        },
        {
            "title": "Har birining o'z joyi",
            "type": "normal",
            "text": """
            Imkon qadar har bir bola uchun:

            <br><br>

            • uyqu joyi;<br>
            • saqlash joyi;<br>
            • o'qish joyi;<br>
            • shaxsiy buyum zonasi

            <br><br>

            aniqlanishi foydali.
            """,
        },
        {
            "title": "Ikki ish stoli",
            "type": "example",
            "text": """
            Ikki bola bir vaqtda dars qilsa,
            bitta kichik stol yetmasligi mumkin.

            <br><br>

            Ish zonasi real kundalik hayotga
            mos bo'lishi kerak.
            """,
        },
        {
            "title": "Krovatlarni qanday qo'yamiz?",
            "type": "normal",
            "text": """
            Variantlar ko'p:

            <br><br>

            • parallel;<br>
            • qarama-qarshi;<br>
            • burchak shaklida;<br>
            • ikki qavatli krovat.

            <br><br>

            Tanlov xona shakli va
            bolalarning yoshiga bog'liq.
            """,
        },
        {
            "title": "Shaxsiylik",
            "type": "warning",
            "text": """
            Bolalar ulg'aygani sari
            har birining shaxsiy hududga
            bo'lgan ehtiyoji ortishi mumkin.

            <br><br>

            Buni rejalashda oldindan hisobga olish foydali.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Ikki bola uchun xona chizing.

            <br><br>

            Quyidagilarni tekshiring:

            <br><br>

            • ikki uyqu joyi;<br>
            • ikki o'qish joyi;<br>
            • yetarli saqlash;<br>
            • umumiy yurish maydoni.
            """,
        },
    ],

    "L02_M09_004": [
        {
            "title": "Bolalar xonasi uyning qayerida?",
            "type": "highlight",
            "text": """
            Xonaning ichki ergonomikasi yaxshi bo'lishi yetmaydi.

            <br><br>

            U butun uy bilan ham
            to'g'ri bog'lanishi kerak.
            """,
        },
        {
            "title": "Ota-onaga yaqinlik",
            "type": "normal",
            "text": """
            Kichik bolalar xonalarini
            ota-onalar zonasidan haddan tashqari
            uzoqlashtirmaslik foydali bo'lishi mumkin.

            <br><br>

            Ayniqsa tungi foydalanishda.
            """,
        },
        {
            "title": "Sanuzelga yo'l",
            "type": "example",
            "text": """
            Bola kechasi uyg'ondi.

            <br><br>

            Sanuzelga borish uchun
            qorong'i holda mehmonxona va oshxonani
            kesib o'tishi kerak.

            <br><br>

            Bu tungi circulation'ni qayta ko'rish uchun signal.
            """,
        },
        {
            "title": "Zinapoya",
            "type": "warning",
            "text": """
            Ikki qavatli uyda kichik bolalar xonasi
            zinapoya bilan qanday bog'langanini
            alohida tahlil qilish kerak.

            <br><br>

            Xavfsizlik faqat xonaning ichida emas.
            """,
        },
        {
            "title": "Shovqin",
            "type": "normal",
            "text": """
            Bolalar yotoqxonasi:

            <br><br>

            • TV devori;<br>
            • katta mehmonxona;<br>
            • texnik xona

            <br><br>

            kabi shovqinli zonalar bilan
            qanday tutashgani tekshiriladi.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Bir uy planida bolalar xonasidan:

            <br><br>

            • ota-onalar xonasiga;<br>
            • sanuzelga;<br>
            • umumiy family room'ga

            <br><br>

            bo'lgan yo'llarni tekshiring.
            """,
        },
    ],

    "L02_M09_005": [
        {
            "title": "Bolalar xonasi xatolarini ovlaymiz",
            "type": "highlight",
            "text": """
            Endi xonani faqat bugungi kun uchun emas,
            bola ulg'ayishi bilan birga tahlil qilamiz.
            """,
        },
        {
            "title": "Xato 1 — ish stoli uchun joy yo'q",
            "type": "warning",
            "text": """
            Kichik bola uchun xona chiroyli.

            <br><br>

            Lekin keyinchalik normal ish stolini
            qo'yish uchun foydali devor qolmagan.
            """,
        },
        {
            "title": "Xato 2 — barcha maydon mebel bilan to'lgan",
            "type": "warning",
            "text": """
            Krovat, shkaf, javon va stol
            xonaning deyarli barcha qismini egallagan.

            <br><br>

            Erkin harakat va o'yin maydoni qolmagan.
            """,
        },
        {
            "title": "Xato 3 — ikkita krovat, bitta normal yo'l",
            "type": "warning",
            "text": """
            Ikki bola xonasida
            krovatlar sig'gan.

            <br><br>

            Lekin biri krovatiga borish uchun
            ikkinchisining zonasidan o'tadi.
            """,
        },
        {
            "title": "Xato 4 — tungi sanuzel uzoqda",
            "type": "warning",
            "text": """
            Bolalar xonasidan sanuzelga
            juda uzun va murakkab yo'l mavjud.

            <br><br>

            Ayniqsa kichik yoshda bu
            qulaylikni pasaytirishi mumkin.
            """,
        },
        {
            "title": "Xato 5 — kelajak hisobga olinmagan",
            "type": "warning",
            "text": """
            Xona faqat hozirgi kichik mebelga mos.

            <br><br>

            Bola ulg'ayganda
            krovat, shkaf va stolni kattalashtirish
            deyarli imkonsiz.
            """,
        },
        {
            "title": "Professional tahlil",
            "type": "example",
            "text": """
            Bolalar xonasini tekshirganda:

            <br><br>

            <b>1.</b> Uyqu zonasi qayerda?<br><br>
            <b>2.</b> O'qish zonasi qayerda?<br><br>
            <b>3.</b> O'yin uchun makon bormi?<br><br>
            <b>4.</b> Saqlash yetarlimi?<br><br>
            <b>5.</b> Bola ulg'aysa xona moslashadimi?<br><br>
            <b>6.</b> Sanuzel va ota-onaga yo'l qulaymi?
            """,
        },
        {
            "title": "Mini-loyiha",
            "type": "example",
            "text": """
            Bir xonani uch bosqich uchun tahlil qiling:

            <br><br>

            • 5 yosh;<br>
            • 10 yosh;<br>
            • 16 yosh.

            <br><br>

            Har bosqichda:

            <br><br>

            krovat, stol, saqlash va
            bo'sh maydon qanday o'zgarishini yozing.
            """,
        },
        {
            "title": "Modul yakuni",
            "type": "highlight",
            "text": """
            Siz endi:

            <br><br>

            ✓ bolalar xonasi zonalari;<br>
            ✓ yoshga mos transformatsiya;<br>
            ✓ ikki bola xonasi;<br>
            ✓ shaxsiy hudud;<br>
            ✓ xavfsiz circulation;<br>
            ✓ oilaviy aloqalar

            <br><br>

            bo'yicha plan tahlil qila olasiz.

            <br><br>

            Keyingi modul:
            <b>LEVEL 2 yakuniy fazoviy tahlil.</b>
            """,
        },
    ],
}


# ============================================================
# QUIZ
# ============================================================

LEVEL02_MODULE09_QUIZ = {
    "L02_M09_001": [
        {
            "code": "L02_Q121",
            "question": "Bolalar xonasi faqat uyqu uchun xizmat qiladimi?",
            "explanation": (
                "U ko'pincha uyqu, o'qish, o'yin va saqlash funksiyalarini birlashtiradi."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L02_Q122",
            "question": "Kichik bolalar xonasida bo'sh o'yin maydoni foydali bo'lishi mumkinmi?",
            "explanation": (
                "Erkin harakat va o'yin ham xona funksiyasining bir qismidir."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L02_Q123",
            "question": "Mebelning sig'ishi xonaning to'liq ishlashini kafolatlaydimi?",
            "explanation": (
                "Mebel atrofidagi foydalanish va harakat zonasi ham muhim."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
    ],

    "L02_M09_002": [
        {
            "code": "L02_Q124",
            "question": "Bolalar xonasining ehtiyojlari yosh bilan o'zgaradimi?",
            "explanation": (
                "Bola ulg'aygani sari o'qish, saqlash va shaxsiy hudud talablari o'zgaradi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L02_Q125",
            "question": "16 yoshli bola uchun 5 yoshdagi xona sxemasi o'zgarmasdan qolishi shartmi?",
            "explanation": (
                "Xona yoshga moslashishi kerak."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L02_Q126",
            "question": "Transformatsiyaga mos xona nima beradi?",
            "explanation": (
                "Xonani bola ulg'ayganda katta rekonstruksiyasiz moslashtirish imkonini beradi."
            ),
            "options": [
                ("A", "Kelajakda moslashuv", True),
                ("B", "Faqat fasad bezagi", False),
            ],
        },
    ],

    "L02_M09_003": [
        {
            "code": "L02_Q127",
            "question": "Ikki bola xonasida faqat ikkita krovat sig'ishi yetarlimi?",
            "explanation": (
                "O'qish, saqlash, yurish va shaxsiy hududlar ham hisobga olinadi."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L02_Q128",
            "question": "Ikki bola uchun alohida o'qish joylari foydali bo'lishi mumkinmi?",
            "explanation": (
                "Bolalar bir vaqtda o'qishi va mustaqil foydalanishi uchun foydali."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L02_Q129",
            "question": "Bolalar ulg'aygani sari shaxsiy hudud ehtiyoji ortishi mumkinmi?",
            "explanation": (
                "Yosh ortishi bilan mustaqillik va maxfiylik talabi kuchayishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L02_M09_004": [
        {
            "code": "L02_Q130",
            "question": "Bolalar xonasining ota-onalar zonasiga aloqasi muhimmi?",
            "explanation": (
                "Ayniqsa kichik yoshda nazorat va tungi foydalanishda bu muhim bo'lishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L02_Q131",
            "question": "Bolalar xonasidan sanuzelga tungi yo'lni tekshirish kerakmi?",
            "explanation": (
                "Qisqa va tushunarli tungi circulation qulaylik va xavfsizlikka yordam beradi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L02_Q132",
            "question": "Shovqinli xona bilan bolalar yotoqxonasining qo'shnichiligini tahlil qilish kerakmi?",
            "explanation": (
                "Akustik qulaylik uyqu va dam olish sifatiga ta'sir qiladi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L02_M09_005": [
        {
            "code": "L02_Q133",
            "question": "Kelajakda kattaroq ish stoliga joy qolmasligi rejalash muammosi bo'lishi mumkinmi?",
            "explanation": (
                "Bolalar xonasida yoshga moslashuv ham rejalashning bir qismidir."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L02_Q134",
            "question": "Xonaning barcha qismini mebel bilan to'ldirish har doim yaxshi yechimmi?",
            "explanation": (
                "Erkin harakat va foydalanish uchun bo'sh makon ham kerak."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L02_Q135",
            "question": "Bolalar xonasi tahlilida qaysi savol foydali?",
            "explanation": (
                "Xonaning bola ulg'ayganda moslashishi professional tahlilning muhim qismidir."
            ),
            "options": [
                ("A", "Bola ulg'aysa xona moslashadimi?", True),
                ("B", "Faqat fasad rangi qanday?", False),
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
