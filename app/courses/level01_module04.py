from database.database import get_connection


# ============================================================
# LEVEL 1
# MODULE 04 - SIMMETRIYA VA ASIMMETRIYA
# ============================================================

LEVEL01_MODULE04_LESSONS = [
    (
        "L01_M04",
        "L01_M04_001",
        "Simmetriya nima?",
        "theory",
        "Fasaddagi elementlarning o'q bo'yicha muvofiqligini tushunish.",
        1,
        30,
        15,
    ),
    (
        "L01_M04",
        "L01_M04_002",
        "Simmetrik fasad",
        "theory",
        "Simmetrik kompozitsiyaning kuchli va zaif tomonlarini o'rganish.",
        2,
        30,
        15,
    ),
    (
        "L01_M04",
        "L01_M04_003",
        "Asimmetriya nima?",
        "theory",
        "Bir xil bo'lmagan elementlar bilan vizual muvozanat yaratish.",
        3,
        35,
        15,
    ),
    (
        "L01_M04",
        "L01_M04_004",
        "Asimmetrik balans",
        "practice",
        "Turli hajm va elementlar yordamida balansli kompozitsiya yaratish.",
        4,
        40,
        20,
    ),
    (
        "L01_M04",
        "L01_M04_005",
        "Simmetriya va asimmetriya xatolari",
        "practice",
        "Fasaddagi sun'iy, tasodifiy va muvozanatsiz yechimlarni aniqlash.",
        5,
        40,
        20,
    ),
]


# ============================================================
# LESSON CONTENT
# ============================================================

LEVEL01_MODULE04_CONTENT = {
    # ========================================================
    # 1-DARS
    # ========================================================

    "L01_M04_001": [
        {
            "title": "Simmetriya nima?",
            "type": "highlight",
            "text": """
            Simmetriya — kompozitsiyaning ikki tomoni
            ma'lum bir o'q bo'yicha
            <b>bir-biriga mos yoki juda yaqin</b>
            tashkil etilishi.

            <br><br>

            Eng sodda misol:
            inson yuzining chap va o'ng tomoni.
            """,
        },
        {
            "title": "Fasadni o'rtadan bo'lamiz",
            "type": "example",
            "text": """
            Uyning old fasadini xayolan
            vertikal chiziq bilan o'rtadan ikkiga bo'ling.

            <br><br>

            Agar:

            <br><br>

            • chapdagi deraza o'ngda ham bo'lsa;<br>
            • chapdagi ustun o'ngda ham takrorlansa;<br>
            • kirish markazda joylashsa;<br>
            • hajmlar bir-biriga mos kelsa

            <br><br>

            fasad kuchli simmetriyaga ega bo'lishi mumkin.
            """,
        },
        {
            "title": "Simmetriya qanday taassurot beradi?",
            "type": "normal",
            "text": """
            Simmetrik kompozitsiya ko'pincha:

            <br><br>

            • tartib;<br>
            • barqarorlik;<br>
            • rasmiylik;<br>
            • sokinlik;<br>
            • markazga yo'nalish

            <br><br>

            hissini berishi mumkin.
            """,
        },
        {
            "title": "Simmetriya faqat fasaddami?",
            "type": "normal",
            "text": """
            Yo'q.

            <br><br>

            Simmetriya:

            <br><br>

            • plan;<br>
            • fasad;<br>
            • interyer;<br>
            • hovli;<br>
            • landshaft

            <br><br>

            kompozitsiyasida ham uchrashi mumkin.
            """,
        },
        {
            "title": "Boshlovchi xatosi",
            "type": "warning",
            "text": """
            “Simmetrik bo'lsa, demak yaxshi loyiha.”

            <br><br>

            Bu noto'g'ri.

            <br><br>

            Simmetriya — shunchaki
            <b>kompozitsion vositalardan biri</b>.

            <br><br>

            Loyiha funksiyasi noto'g'ri bo'lsa,
            simmetriya uni avtomatik yaxshi qilmaydi.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Simmetrik uy fasadini toping.

            <br><br>

            Xayolan o'rtadan vertikal chiziq o'tkazing.

            <br><br>

            Chap va o'ng tomonda
            qaysi elementlar takrorlanganini yozing.
            """,
        },
    ],

    # ========================================================
    # 2-DARS
    # ========================================================

    "L01_M04_002": [
        {
            "title": "Simmetrik fasad qanday quriladi?",
            "type": "highlight",
            "text": """
            Simmetrik fasadda odatda
            aniq <b>markaziy o'q</b> mavjud.

            <br><br>

            Elementlar shu o'q atrofida
            tartiblanadi.
            """,
        },
        {
            "title": "Markaziy kirish",
            "type": "example",
            "text": """
            Tasavvur qiling:

            <br><br>

            uy eshigi aynan markazda.

            <br><br>

            Chap tomonda ikkita deraza.

            <br>
            O'ng tomonda ham xuddi shunday ikkita deraza.

            <br><br>

            Tomning asosiy cho'qqisi ham markazda.

            <br><br>

            Bu juda aniq simmetrik kompozitsiya.
            """,
        },
        {
            "title": "Simmetriyaning kuchli tomoni",
            "type": "normal",
            "text": """
            Simmetriya fasadni tez tushunarli qiladi.

            <br><br>

            Ko'z markazni oson topadi.

            <br><br>

            Shuning uchun klassik va rasmiy arxitekturada
            simmetriya ko'p ishlatiladi.
            """,
        },
        {
            "title": "Simmetriyaning cheklovi",
            "type": "warning",
            "text": """
            Plan funksiyasi simmetriyaga mos kelmasa,
            fasad uchun plan ichida sun'iy yechimlar
            paydo bo'lishi mumkin.

            <br><br>

            Masalan, faqat fasad simmetrik bo'lishi uchun
            xonaning derazasini noqulay joyga surish.

            <br><br>

            Bu professional yechim emas.
            """,
        },
        {
            "title": "Muhim fikr",
            "type": "highlight",
            "text": """
            <b>
            Fasad plan uchun ishlashi kerak.
            Plan fasadning quliga aylanmasligi kerak.
            </b>
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Simmetrik fasad toping va tekshiring:

            <br><br>

            1. Markaziy o'q qayerda?<br>
            2. Kirish shu o'qdamı?<br>
            3. Derazalar qanday takrorlangan?<br>
            4. Tom markazni kuchaytirganmi?
            """,
        },
    ],

    # ========================================================
    # 3-DARS
    # ========================================================

    "L01_M04_003": [
        {
            "title": "Asimmetriya nima?",
            "type": "highlight",
            "text": """
            Asimmetriya — kompozitsiyaning ikki tomoni
            bir-birining nusxasi bo'lmasa ham,
            umumiy ko'rinishda
            <b>muvozanat saqlanishi</b>.
            """,
        },
        {
            "title": "Oddiy misol",
            "type": "example",
            "text": """
            Fasadning chap tomonida katta
            ikki qavatli hajm bor.

            <br><br>

            O'ng tomonda esa pastroq,
            lekin kengroq hajm mavjud.

            <br><br>

            Ular shaklan bir xil emas.

            <br><br>

            Lekin vizual og'irliklari muvozanatli bo'lsa,
            kompozitsiya yaxshi ishlashi mumkin.
            """,
        },
        {
            "title": "Asimmetriya = tartibsizlik emas",
            "type": "warning",
            "text": """
            Bu juda muhim.

            <br><br>

            Asimmetriya:

            <br><br>

            <b>tasodifiy joylashtirish</b> degani emas.

            <br><br>

            Yaxshi asimmetriyada ham:

            <br><br>

            • balans;<br>
            • ierarxiya;<br>
            • ritm;<br>
            • proporsiya;<br>
            • markaz

            <br><br>

            mavjud bo'lishi mumkin.
            """,
        },
        {
            "title": "Zamonaviy turar joylarda",
            "type": "normal",
            "text": """
            Zamonaviy uylarda asimmetriya ko'p uchraydi.

            <br><br>

            Masalan:

            <br><br>

            • bir tomonda katta panoramali deraza;<br>
            • boshqa tomonda yopiq devor;<br>
            • siljigan kirish;<br>
            • turli balandlikdagi hajmlar;<br>
            • konsol elementlari.

            <br><br>

            Bularning barchasi baribir
            ongli kompozitsiya talab qiladi.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Asimmetrik zamonaviy uy toping.

            <br><br>

            Chap va o'ng tomon bir xil emasligini ko'ring.

            <br><br>

            Keyin savol bering:

            <br><br>

            <b>
            “Nega fasad baribir muvozanatli ko'rinyapti?”
            </b>
            """,
        },
    ],

    # ========================================================
    # 4-DARS
    # ========================================================

    "L01_M04_004": [
        {
            "title": "Asimmetrik balans",
            "type": "highlight",
            "text": """
            Asimmetrik kompozitsiyaning eng muhim qismi
            — <b>vizual balans</b>.
            """,
        },
        {
            "title": "Vizual tarozi",
            "type": "example",
            "text": """
            Fasadingizni xayolan tarozi deb tasavvur qiling.

            <br><br>

            Chap tomonda katta, lekin och rangli hajm.

            <br><br>

            O'ng tomonda kichikroq,
            lekin qora va kuchli teksturali hajm.

            <br><br>

            Hajmlari har xil bo'lsa ham,
            vizual og'irliklari bir-birini
            muvozanatlashi mumkin.
            """,
        },
        {
            "title": "Nima vizual og'irlik beradi?",
            "type": "normal",
            "text": """
            Vizual og'irlikka quyidagilar ta'sir qiladi:

            <br><br>

            • element kattaligi;<br>
            • rangning to'q yoki ochligi;<br>
            • tekstura;<br>
            • hajmning chuqurligi;<br>
            • deraza miqdori;<br>
            • material;<br>
            • elementning joylashuvi.
            """,
        },
        {
            "title": "Misol: katta deraza",
            "type": "example",
            "text": """
            Chap tomonda katta panoramali deraza bor.

            <br><br>

            U vizual jihatdan juda kuchli.

            <br><br>

            O'ng tomonda esa massiv devor hajmi
            unga qarshi balans yaratishi mumkin.

            <br><br>

            Ikki tomon bir xil emas,
            lekin bir-birini ushlab turadi.
            """,
        },
        {
            "title": "Boshlovchi xatosi",
            "type": "warning",
            "text": """
            Asimmetrik fasad qilish uchun
            elementlarni shunchaki turli joyga surish yetmaydi.

            <br><br>

            Natijada fasad bir tomonga
            “qulab ketayotgandek” ko'rinishi mumkin.
            """,
        },
        {
            "title": "Amaliy mashq",
            "type": "example",
            "text": """
            Asimmetrik fasadni o'rtadan ikkiga ajrating.

            <br><br>

            Chap taraf uchun vizual og'irlik berayotgan
            3 ta elementni yozing.

            <br><br>

            O'ng taraf uchun ham 3 ta element yozing.

            <br><br>

            Keyin ular qanday balans
            yaratayotganini tushuntiring.
            """,
        },
    ],

    # ========================================================
    # 5-DARS
    # ========================================================

    "L01_M04_005": [
        {
            "title": "Endi xatolarni topamiz",
            "type": "highlight",
            "text": """
            Simmetriya ham,
            asimmetriya ham noto'g'ri ishlatilishi mumkin.

            <br><br>

            Muhim narsa — qaysi uslub ishlatilgani emas,
            <b>qarorning mantiqi</b>.
            """,
        },
        {
            "title": "Xato 1 — majburiy simmetriya",
            "type": "warning",
            "text": """
            Fasad simmetrik chiqishi uchun
            ichki xonadagi deraza noqulay joyga qo'yildi.

            <br><br>

            Tashqaridan tartibli,
            ichkaridan esa noqulay.

            <br><br>

            Bu yaxshi arxitektura emas.
            """,
        },
        {
            "title": "Xato 2 — tasodifiy asimmetriya",
            "type": "warning",
            "text": """
            Deraza chapga surildi.

            <br>
            Balkon o'ngga surildi.

            <br>
            Kirish yana boshqa joyda.

            <br><br>

            Lekin hech qanday kompozitsion sabab yo'q.

            <br><br>

            Bu asimmetriya emas,
            shunchaki tartibsizlik bo'lishi mumkin.
            """,
        },
        {
            "title": "Xato 3 — bir tomon juda og'ir",
            "type": "warning",
            "text": """
            Chap tomonda:

            <br><br>

            • qora hajm;<br>
            • katta balkon;<br>
            • katta deraza;<br>
            • baland portal

            <br><br>

            jamlangan.

            <br><br>

            O'ng tomonda esa deyarli hech narsa yo'q.

            <br><br>

            Fasad balansini tekshirish kerak.
            """,
        },
        {
            "title": "Xato 4 — simmetriya yarim yo'lda buzilgan",
            "type": "warning",
            "text": """
            Fasadning deyarli hamma qismi simmetrik.

            <br><br>

            Lekin bitta deraza sababsiz
            30–40 sm boshqa joyga siljigan.

            <br><br>

            Ko'z buni xato sifatida sezishi mumkin.
            """,
        },
        {
            "title": "Professional tekshiruv",
            "type": "example",
            "text": """
            Har bir fasadga 5 savol:

            <br><br>

            <b>1.</b> Kompozitsiya simmetrikmi yoki asimmetrikmi?<br><br>
            <b>2.</b> Asosiy o'q bormi?<br><br>
            <b>3.</b> Chap va o'ng vizual og'irligi qanday?<br><br>
            <b>4.</b> Muvozanat bormi?<br><br>
            <b>5.</b> Bu qarorning funksional sababi bormi?
            """,
        },
        {
            "title": "Mini-loyiha",
            "type": "example",
            "text": """
            Ikkita uy fasadini tanlang.

            <br><br>

            Birinchisi — simmetrik.

            <br>
            Ikkinchisi — asimmetrik.

            <br><br>

            Har birining kamida:

            <br><br>

            • 2 ta kuchli tomoni;<br>
            • 1 ta zaif tomoni

            <br><br>

            ni professional terminlar bilan yozing.
            """,
        },
        {
            "title": "Modul yakuni",
            "type": "highlight",
            "text": """
            Siz endi:

            <br><br>

            ✓ simmetriya;<br>
            ✓ markaziy o'q;<br>
            ✓ simmetrik fasad;<br>
            ✓ asimmetriya;<br>
            ✓ asimmetrik balans;<br>
            ✓ vizual og'irlik

            <br><br>

            tushunchalarini farqlay olasiz.

            <br><br>

            Keyingi modul:
            <b>Forma va hajm.</b>
            """,
        },
    ],
}


# ============================================================
# QUIZ DATA
# ============================================================

LEVEL01_MODULE04_QUIZ = {
    "L01_M04_001": [
        {
            "code": "L01_Q046",
            "question": "Simmetriya nima?",
            "explanation": (
                "Simmetriyada kompozitsiyaning ikki tomoni ma'lum o'q bo'yicha mos tashkil etiladi."
            ),
            "options": [
                ("A", "O'q bo'yicha mos tashkil etilish", True),
                ("B", "Tasodifiy elementlar", False),
                ("C", "Faqat rang tanlash", False),
            ],
        },
        {
            "code": "L01_Q047",
            "question": "Simmetriya faqat fasadda uchraydimi?",
            "explanation": (
                "Simmetriya plan, interyer, landshaft va boshqa kompozitsiyalarda ham uchrashi mumkin."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L01_Q048",
            "question": "Simmetrik loyiha avtomatik ravishda yaxshi loyiha bo'ladimi?",
            "explanation": (
                "Simmetriya kompozitsion vosita, lekin funksional va boshqa talablar ham muhim."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
    ],

    "L01_M04_002": [
        {
            "code": "L01_Q049",
            "question": "Simmetrik fasadda markaziy o'q muhimmi?",
            "explanation": (
                "Simmetrik kompozitsiya ko'pincha aniq markaziy o'q atrofida quriladi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L01_Q050",
            "question": "Fasad simmetriyasi uchun ichki funksiyani buzish to'g'rimi?",
            "explanation": (
                "Fasad va plan birgalikda ishlashi kerak; simmetriya funksiyani buzmasligi kerak."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L01_Q051",
            "question": "Simmetriya ko'pincha qanday taassurot beradi?",
            "explanation": (
                "U tartib, barqarorlik va markazlashganlik hissini berishi mumkin."
            ),
            "options": [
                ("A", "Tartib va barqarorlik", True),
                ("B", "Faqat tartibsizlik", False),
            ],
        },
    ],

    "L01_M04_003": [
        {
            "code": "L01_Q052",
            "question": "Asimmetriya nimani anglatadi?",
            "explanation": (
                "Ikki tomon bir xil bo'lmasa ham umumiy vizual muvozanat saqlanishi mumkin."
            ),
            "options": [
                ("A", "Bir xil bo'lmagan, lekin balansli kompozitsiya", True),
                ("B", "Tasodifiy tartibsizlik", False),
            ],
        },
        {
            "code": "L01_Q053",
            "question": "Asimmetriya tartibsizlik bilan bir xilmi?",
            "explanation": (
                "Professional asimmetriyada ham balans, ritm va ierarxiya mavjud."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L01_Q054",
            "question": "Zamonaviy turar joylarda asimmetrik kompozitsiya ishlatilishi mumkinmi?",
            "explanation": (
                "Turli hajm, deraza va siljigan elementlar orqali asimmetrik kompozitsiya yaratilishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L01_M04_004": [
        {
            "code": "L01_Q055",
            "question": "Asimmetrik kompozitsiyada nima eng muhim?",
            "explanation": (
                "Ikki tomon bir xil bo'lmasa ham vizual balans saqlanishi muhim."
            ),
            "options": [
                ("A", "Vizual balans", True),
                ("B", "Hammasini bir xil qilish", False),
            ],
        },
        {
            "code": "L01_Q056",
            "question": "Rang elementning vizual og'irligiga ta'sir qilishi mumkinmi?",
            "explanation": (
                "To'q yoki kuchli ranglar ayrim elementlarni vizual jihatdan og'irroq ko'rsatishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L01_Q057",
            "question": "Asimmetrik fasad uchun elementlarni tasodifiy surish yetarlimi?",
            "explanation": (
                "Asimmetriya ham ongli balans va kompozitsion mantiq talab qiladi."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
    ],

    "L01_M04_005": [
        {
            "code": "L01_Q058",
            "question": "Fasad simmetrik bo'lishi uchun xona funksiyasini buzish yaxshi yechimmi?",
            "explanation": (
                "Arxitekturada tashqi kompozitsiya ichki funksiyani asossiz buzmasligi kerak."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L01_Q059",
            "question": "Bir tomonda juda ko'p kuchli element to'planishi nimaga olib kelishi mumkin?",
            "explanation": (
                "Fasad vizual jihatdan bir tomonga og'ir ko'rinishi mumkin."
            ),
            "options": [
                ("A", "Vizual balans buzilishiga", True),
                ("B", "Har doim yaxshi natijaga", False),
            ],
        },
        {
            "code": "L01_Q060",
            "question": "Professional tahlilda qaysi savol foydali?",
            "explanation": (
                "Chap va o'ng tomonning vizual og'irligini solishtirish balansni baholashga yordam beradi."
            ),
            "options": [
                ("A", "Chap va o'ng vizual og'irligi qanday?", True),
                ("B", "Faqat qurilish narxi qancha?", False),
            ],
        },
    ],
}


# ============================================================
# DATABASE SEED
# ============================================================

def seed_level01_module04():
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
        ) in LEVEL01_MODULE04_LESSONS:

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
