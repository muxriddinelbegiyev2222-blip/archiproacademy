from database.database import get_connection


# ============================================================
# LEVEL 1
# MODULE 03 - RITM VA TAKRORLANISH
# ============================================================

LEVEL01_MODULE03_LESSONS = [
    (
        "L01_M03",
        "L01_M03_001",
        "Arxitekturada ritm nima?",
        "theory",
        "Elementlarning tartibli takrorlanishi orqali ritm hosil bo'lishini tushunish.",
        1,
        30,
        15,
    ),
    (
        "L01_M03",
        "L01_M03_002",
        "Derazalar ritmi",
        "theory",
        "Fasaddagi deraza joylashuvi va oralig'ini tahlil qilish.",
        2,
        30,
        15,
    ),
    (
        "L01_M03",
        "L01_M03_003",
        "Ustun va vertikal elementlar ritmi",
        "theory",
        "Ustunlar va vertikal elementlar fasad tartibiga qanday ta'sir qilishini tushunish.",
        3,
        30,
        15,
    ),
    (
        "L01_M03",
        "L01_M03_004",
        "Ritmni ataylab buzish",
        "theory",
        "Monoton kompozitsiyada aksent yaratish uchun ritmni ongli buzish.",
        4,
        35,
        20,
    ),
    (
        "L01_M03",
        "L01_M03_005",
        "Ritm xatolarini topish",
        "practice",
        "Turar joy fasadlaridagi tartibsiz va sababsiz takrorlanishlarni aniqlash.",
        5,
        40,
        20,
    ),
]


# ============================================================
# LESSON CONTENT
# ============================================================

LEVEL01_MODULE03_CONTENT = {
    "L01_M03_001": [
        {
            "title": "Ritm nima?",
            "type": "highlight",
            "text": """
            Ritm — elementlarning ma'lum tartib asosida
            <b>takrorlanishi</b>.

            <br><br>

            Arxitekturada ritm ko'zga tartib va davomiylik hissini beradi.
            """,
        },
        {
            "title": "Oddiy hayotiy misol",
            "type": "example",
            "text": """
            Tasavvur qiling:

            <br><br>

            ko'cha bo'ylab daraxtlar har 5 metrda bittadan ekilgan.

            <br><br>

            Siz yurayotganingizda:

            <br><br>

            daraxt — bo'shliq — daraxt — bo'shliq — daraxt

            <br><br>

            tartibini his qilasiz.

            <br><br>

            Bu ham ritmning sodda ko'rinishi.
            """,
        },
        {
            "title": "Fasadda ritm",
            "type": "normal",
            "text": """
            Fasadda ritm quyidagilar orqali paydo bo'lishi mumkin:

            <br><br>

            • derazalar;<br>
            • ustunlar;<br>
            • balkonlar;<br>
            • panellar;<br>
            • soyabonlar;<br>
            • vertikal yoki gorizontal chiziqlar;<br>
            • material bo'linmalari.
            """,
        },
        {
            "title": "Takrorlanishning o'zi yetadimi?",
            "type": "warning",
            "text": """
            Yo'q.

            <br><br>

            Bir xil elementlarni tasodifiy joylashtirish
            yaxshi ritm degani emas.

            <br><br>

            Ritmda <b>tartib va munosabat</b> bo'lishi kerak.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Bir uy fasadini tanlang.

            <br><br>

            Undagi takrorlanayotgan elementlarni toping.

            <br><br>

            Masalan:

            <br>
            deraza — deraza — deraza.

            <br><br>

            Keyin ularning oralig'i va o'lchami
            bir tizimga tushganmi, tekshiring.
            """,
        },
        {
            "title": "Eslab qoling",
            "type": "highlight",
            "text": """
            <b>
            Ritm — shunchaki takrorlanish emas.
            Ritm — tartibli takrorlanish.
            </b>
            """,
        },
    ],

    "L01_M03_002": [
        {
            "title": "Derazalar fasad ritmini kuchli o'zgartiradi",
            "type": "highlight",
            "text": """
            Bir qator derazalar fasadda eng tez seziladigan
            ritmlardan birini yaratadi.
            """,
        },
        {
            "title": "Tasavvur qiling",
            "type": "example",
            "text": """
            Fasadda 4 ta bir xil deraza bor.

            <br><br>

            Birinchi uchta deraza orasidagi masofa bir xil.

            <br><br>

            To'rtinchi deraza esa sababsiz juda uzoqqa surilgan.

            <br><br>

            Ko'z buni tez sezadi.

            <br><br>

            Ritm buzilganini his qilasiz.
            """,
        },
        {
            "title": "Nimalarni solishtiramiz?",
            "type": "normal",
            "text": """
            Derazalarda:

            <br><br>

            • eni;<br>
            • balandligi;<br>
            • pastki va yuqori sathi;<br>
            • derazalar orasidagi masofa;<br>
            • devor chetiga masofa

            <br><br>

            birgalikda tahlil qilinadi.
            """,
        },
        {
            "title": "Plan va fasad yana bog'liq",
            "type": "warning",
            "text": """
            Derazalarni tashqaridan chiroyli ritm qilish uchun
            ichkaridagi xonalarni buzib yuborish mumkin emas.

            <br><br>

            Fasad ritmi va xona funksiyasi
            <b>birgalikda hal qilinadi</b>.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            5 ta derazali fasad toping.

            <br><br>

            Har bir deraza orasidagi masofani
            ko'z bilan solishtiring.

            <br><br>

            Ritm:

            <br>
            • muntazammimi?<br>
            • ataylab o'zgartirilganmi?<br>
            • yoki shunchaki tasodifiymi?
            """,
        },
    ],

    "L01_M03_003": [
        {
            "title": "Ustunlar ham ritm yaratadi",
            "type": "highlight",
            "text": """
            Ayvon yoki terassada ketma-ket joylashgan ustunlar
            juda kuchli vizual ritm yaratishi mumkin.
            """,
        },
        {
            "title": "Oddiy misol",
            "type": "example",
            "text": """
            Tasavvur qiling, ayvonda 5 ta ustun bor.

            <br><br>

            Ularning oralig'i:

            <br><br>

            3 m — 3 m — 3 m — 3 m

            <br><br>

            bo'lsa, juda aniq ritm paydo bo'ladi.

            <br><br>

            Agar oxirgi oraliq sababsiz 1 metr bo'lsa,
            tizim buzilishi mumkin.
            """,
        },
        {
            "title": "Ritm faqat oralig'da emas",
            "type": "normal",
            "text": """
            Ustunlarda ritmga:

            <br><br>

            • qalinlik;<br>
            • balandlik;<br>
            • masofa;<br>
            • material;<br>
            • shakl

            <br><br>

            ham ta'sir qiladi.
            """,
        },
        {
            "title": "Konstruksiya bilan aloqa",
            "type": "warning",
            "text": """
            Ustunlarni faqat fasad chiroyli chiqishi uchun
            xohlagan joyga qo'yib bo'lmaydi.

            <br><br>

            Ularning konstruktiv vazifasi bo'lishi mumkin.

            <br><br>

            Arxitektura va konstruksiya birga ishlashi kerak.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Ustunli bitta zamonaviy uy toping.

            <br><br>

            Ustunlarni xayolan olib tashlang.

            <br><br>

            Fasadning ritmi va xarakteri qanchalik o'zgardi?
            """,
        },
    ],

    "L01_M03_004": [
        {
            "title": "Ritmni buzish ham mumkin",
            "type": "highlight",
            "text": """
            Professional arxitektura har doim
            hamma narsani bir xil takrorlash degani emas.

            <br><br>

            Ba'zan ritm <b>ataylab buziladi</b>.
            """,
        },
        {
            "title": "Nima uchun buziladi?",
            "type": "normal",
            "text": """
            Ritmni ongli ravishda o'zgartirish orqali:

            <br><br>

            • kirishni ajratish;<br>
            • aksent yaratish;<br>
            • monotonlikni kamaytirish;<br>
            • muhim zonani ko'rsatish

            <br><br>

            mumkin.
            """,
        },
        {
            "title": "Misol",
            "type": "example",
            "text": """
            Tasavvur qiling:

            <br><br>

            deraza — deraza — deraza — <b>KATTA KIRISH</b> — deraza.

            <br><br>

            Bu yerda ritm buzildi.

            <br><br>

            Lekin sabab bor:
            asosiy kirishga e'tibor qaratildi.
            """,
        },
        {
            "title": "Tasodifiy buzilish bilan farqi",
            "type": "warning",
            "text": """
            Professional ritm buzilishi:

            <br><br>

            <b>“Nega?”</b> savoliga javobga ega.

            <br><br>

            Tasodifiy buzilish esa ko'pincha
            loyiha tartibsizligidan paydo bo'ladi.
            """,
        },
        {
            "title": "Muhim qoida",
            "type": "highlight",
            "text": """
            <b>
            Qoidani buzish mumkin.

            Lekin avval qoidani tushunish kerak.
            </b>
            """,
        },
    ],

    "L01_M03_005": [
        {
            "title": "Endi xato ovlaymiz",
            "type": "highlight",
            "text": """
            Siz endi fasaddagi takrorlanishni
            professionalroq ko'z bilan tekshira olasiz.
            """,
        },
        {
            "title": "Xato 1 — sababsiz masofa",
            "type": "warning",
            "text": """
            To'rtta deraza orasidagi masofa:

            <br><br>

            1.5 m — 1.5 m — 2.2 m

            <br><br>

            Agar buning funksional yoki kompozitsion sababi bo'lmasa,
            oxirgi farq tasodifiy ko'rinishi mumkin.
            """,
        },
        {
            "title": "Xato 2 — turli balandlik",
            "type": "warning",
            "text": """
            Bir qavatdagi derazalarning tepasi
            sababsiz har xil balandlikda tugasa,
            fasadda tartibsizlik paydo bo'lishi mumkin.
            """,
        },
        {
            "title": "Xato 3 — ortiqcha bir xillik",
            "type": "warning",
            "text": """
            Juda uzoq fasadda bir xil element
            o'nlab marta o'zgarmasdan takrorlansa,
            fasad monoton bo'lib qolishi mumkin.

            <br><br>

            Demak, muammo faqat ritmning yo'qligi emas.

            <br><br>

            Ba'zida <b>haddan tashqari bir xil ritm</b>
            ham muammo.
            """,
        },
        {
            "title": "Xato 4 — konstruksiyadan uzilgan ritm",
            "type": "warning",
            "text": """
            Fasad uchun chiroyli ustunlar chizilgan,
            lekin ular binoning haqiqiy konstruktiv tizimi
            bilan umuman bog'lanmagan.

            <br><br>

            Bu yechim keyin loyiha davomida
            muammo tug'dirishi mumkin.
            """,
        },
        {
            "title": "5 savolli tekshiruv",
            "type": "example",
            "text": """
            Fasad ko'rsangiz:

            <br><br>

            <b>1.</b> Nima takrorlanyapti?<br><br>
            <b>2.</b> Oralig'i tartiblimi?<br><br>
            <b>3.</b> O'lchamlari tizimlimi?<br><br>
            <b>4.</b> Ritm qayerda buzilgan?<br><br>
            <b>5.</b> Buzilishning sababi bormi?
            """,
        },
        {
            "title": "Mini-loyiha",
            "type": "example",
            "text": """
            Internetdan ikkita fasad toping.

            <br><br>

            Birinchisi:
            yaxshi ritmga ega bo'lsin.

            <br><br>

            Ikkinchisi:
            sizningcha tartibsiz bo'lsin.

            <br><br>

            Har biri uchun kamida 3 ta sabab yozing.
            """,
        },
        {
            "title": "Modul yakuni",
            "type": "highlight",
            "text": """
            Siz endi:

            <br><br>

            ✓ ritm;<br>
            ✓ takrorlanish;<br>
            ✓ derazalar ritmi;<br>
            ✓ ustunlar ritmi;<br>
            ✓ ongli ritm buzilishi;<br>
            ✓ tasodifiy ritm xatosi

            <br><br>

            tushunchalarini farqlay olasiz.

            <br><br>

            Keyingi modul:
            <b>Simmetriya va asimmetriya.</b>
            """,
        },
    ],
}


# ============================================================
# QUIZ DATA
# ============================================================

LEVEL01_MODULE03_QUIZ = {
    "L01_M03_001": [
        {
            "code": "L01_Q031",
            "question": "Arxitekturada ritm nima?",
            "explanation": (
                "Ritm elementlarning ma'lum tartibda takrorlanishidir."
            ),
            "options": [
                ("A", "Tartibli takrorlanish", True),
                ("B", "Faqat rang", False),
                ("C", "Tasodifiy elementlar", False),
            ],
        },
        {
            "code": "L01_Q032",
            "question": "Tasodifiy takrorlanish har doim yaxshi ritm yaratadimi?",
            "explanation": (
                "Yaxshi ritmda takrorlanish bilan birga tartib ham bo'lishi kerak."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L01_Q033",
            "question": "Qaysi element fasadda ritm yaratishi mumkin?",
            "explanation": (
                "Derazalar, ustunlar va boshqa takrorlanuvchi elementlar ritm yaratishi mumkin."
            ),
            "options": [
                ("A", "Derazalar", True),
                ("B", "Faqat yer maydoni", False),
            ],
        },
    ],

    "L01_M03_002": [
        {
            "code": "L01_Q034",
            "question": "Derazalar orasidagi masofa fasad ritmiga ta'sir qiladimi?",
            "explanation": (
                "Deraza oralig'i ritmning asosiy omillaridan biridir."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L01_Q035",
            "question": "Derazalarni faqat fasad uchun joylashtirish to'g'rimi?",
            "explanation": (
                "Ichki xona funksiyasi, yorug'lik va mebel ham hisobga olinadi."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L01_Q036",
            "question": "Bir qator derazalardan bittasi sababsiz boshqa balandlikda bo'lsa nima bo'lishi mumkin?",
            "explanation": (
                "Vizual ritm buzilishi mumkin."
            ),
            "options": [
                ("A", "Ritm buzilishi mumkin", True),
                ("B", "Hech qanday ta'siri yo'q", False),
            ],
        },
    ],

    "L01_M03_003": [
        {
            "code": "L01_Q037",
            "question": "Ustunlar fasadda ritm yaratishi mumkinmi?",
            "explanation": (
                "Takrorlanuvchi ustunlar kuchli vertikal ritm hosil qilishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L01_Q038",
            "question": "Ustunlar ritmida faqat masofa muhimmi?",
            "explanation": (
                "Qalinlik, balandlik, material va shakl ham ritmga ta'sir qiladi."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L01_Q039",
            "question": "Ustun joylashuvi konstruktiv tizim bilan bog'liq bo'lishi mumkinmi?",
            "explanation": (
                "Ustun konstruktiv element bo'lishi mumkin, shuning uchun arxitektura va konstruktsiya birgalikda hal qilinadi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L01_M03_004": [
        {
            "code": "L01_Q040",
            "question": "Arxitekturada ritmni ataylab buzish mumkinmi?",
            "explanation": (
                "Aksent yoki muhim zona yaratish uchun ritm ongli ravishda o'zgartirilishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Hech qachon", False),
            ],
        },
        {
            "code": "L01_Q041",
            "question": "Ritmni ongli buzishning sababi bo'lishi kerakmi?",
            "explanation": (
                "Professional qaror 'nega?' savoliga javob bera olishi kerak."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L01_Q042",
            "question": "Ritmni buzish kirishni ajratishda ishlatilishi mumkinmi?",
            "explanation": (
                "Asosiy kirishga e'tibor qaratish uchun ritm o'zgartirilishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L01_M03_005": [
        {
            "code": "L01_Q043",
            "question": "Haddan tashqari bir xil takrorlanish ham muammo bo'lishi mumkinmi?",
            "explanation": (
                "Juda uzoq va o'zgarmas ritm monotonlik yaratishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L01_Q044",
            "question": "Ritm xatosini tekshirganda qaysi savol foydali?",
            "explanation": (
                "Ritm qayerda buzilgan va buning sababi bor-yo'qligini tekshirish kerak."
            ),
            "options": [
                ("A", "Ritm qayerda va nima sabab buzilgan?", True),
                ("B", "Faqat bino narxi qancha?", False),
            ],
        },
        {
            "code": "L01_Q045",
            "question": "Bir xil qavatdagi deraza tepalari sababsiz turli balandlikda bo'lsa nima yuz berishi mumkin?",
            "explanation": (
                "Fasad vizual tartibsiz ko'rinishi mumkin."
            ),
            "options": [
                ("A", "Vizual tartibsizlik", True),
                ("B", "Har doim yaxshi kompozitsiya", False),
            ],
        },
    ],
}


# ============================================================
# DATABASE SEED
# ============================================================

def seed_level01_module03():
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
        ) in LEVEL01_MODULE03_LESSONS:

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
