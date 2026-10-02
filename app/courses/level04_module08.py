from database.database import get_connection


# ============================================================
# LEVEL 4
# MODULE 08 - MAHALLIY FASAD
# ============================================================

LEVEL04_MODULE08_LESSONS = [
    (
        "L04_M08",
        "L04_M08_001",
        "Fasad nimani ifodalaydi?",
        "theory",
        "Fasadni bino funksiyasi, kirish va kompozitsiya bilan bog'lab tushunish.",
        1,
        40,
        20,
    ),
    (
        "L04_M08",
        "L04_M08_002",
        "Mahalliy ruh va zamonaviy arxitektura",
        "theory",
        "Mahalliy elementlarni zamonaviy fasadga me'yorida integratsiya qilish.",
        2,
        45,
        20,
    ),
    (
        "L04_M08",
        "L04_M08_003",
        "Deraza, ayvon va soyalanish",
        "theory",
        "Fasad ochilishlari va soyalanish elementlarini kompozitsion boshqarish.",
        3,
        45,
        20,
    ),
    (
        "L04_M08",
        "L04_M08_004",
        "Material va proporsiya",
        "practice",
        "Materiallar, ranglar va fasad proporsiyalarini muvozanatli tashkil qilish.",
        4,
        50,
        20,
    ),
    (
        "L04_M08",
        "L04_M08_005",
        "Mahalliy fasad auditi",
        "practice",
        "Zamonaviy turar joy fasadidagi tipik kompozitsion xatolarni aniqlash.",
        5,
        60,
        25,
    ),
]


# ============================================================
# CONTENT
# ============================================================

LEVEL04_MODULE08_CONTENT = {
    "L04_M08_001": [
        {
            "title": "Fasad — uyning yuzi",
            "type": "highlight",
            "text": """
            Fasad binoning tashqi ko'rinishi,
            lekin u faqat bezak emas.

            <br><br>

            Fasad orqali:

            <br><br>

            • asosiy kirish;<br>
            • bino massasi;<br>
            • qavatlar;<br>
            • derazalar;<br>
            • soyalanish;<br>
            • materiallar

            <br><br>

            o'qiladi.
            """,
        },
        {
            "title": "Fasad ichki reja bilan bog'liq",
            "type": "normal",
            "text": """
            Deraza va eshiklar
            fasadga tasodifiy qo'yilmaydi.

            <br><br>

            Ular ichki xonalar bilan
            bevosita bog'liq.
            """,
        },
        {
            "title": "Tasavvur qiling",
            "type": "example",
            "text": """
            Ichkarida katta living bor.

            <br><br>

            Fasad esa mayda,
            tartibsiz oynalardan iborat.

            <br><br>

            Ichki makon va tashqi ko'rinish
            bir-birini tushuntirmaydi.
            """,
        },
        {
            "title": "Asosiy kirish o'qilishi kerak",
            "type": "highlight",
            "text": """
            Odam uyga qaraganda:

            <br><br>

            <b>
            asosiy kirish qayerda ekanini
            tushunishi kerak.
            </b>
            """,
        },
        {
            "title": "Kompozitsion ierarxiya",
            "type": "normal",
            "text": """
            Fasadning barcha elementlari
            bir xil darajada kuchli bo'lmasligi kerak.

            <br><br>

            Asosiy kirish,
            katta living oynasi
            yoki markaziy element

            <br><br>

            kompozitsion dominant bo'lishi mumkin.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Bitta uy fasadini oling.

            <br><br>

            Belgilang:

            <br><br>

            • asosiy kirish;<br>
            • dominant;<br>
            • ikkilamchi elementlar;<br>
            • deraza ritmi.
            """,
        },
    ],

    "L04_M08_002": [
        {
            "title": "Mahalliy ruh — nusxa ko'chirish emas",
            "type": "highlight",
            "text": """
            Mahalliy arxitektura elementini ishlatish
            eski binoni to'liq ko'chirish degani emas.

            <br><br>

            Maqsad —
            zamonaviy uyga mos
            mahalliy xarakter yaratish.
            """,
        },
        {
            "title": "Mahalliy elementlar qayerda ko'rinishi mumkin?",
            "type": "normal",
            "text": """
            Mahalliy ruh:

            <br><br>

            • kirish portali;<br>
            • ayvon;<br>
            • ustun ritmi;<br>
            • dekorativ ekran;<br>
            • tekstura;<br>
            • material;<br>
            • geometrik naqsh

            <br><br>

            orqali ifodalanishi mumkin.
            """,
        },
        {
            "title": "Me'yor muhim",
            "type": "warning",
            "text": """
            Har bir devorga
            naqsh, ustun, bezak va
            dekor qo'shilsa,

            <br><br>

            fasad vizual shovqinga
            aylanishi mumkin.
            """,
        },
        {
            "title": "Zamonaviy + mahalliy",
            "type": "example",
            "text": """
            Oddiy zamonaviy fasad.

            <br><br>

            Lekin:

            <br><br>

            kirishda chuqur ayvon,
            ritmik ustunlar,
            tabiiy material teksturasi
            va nozik geometrik ekran mavjud.

            <br><br>

            Natija zamonaviy,
            lekin mahalliy ruhga ega.
            """,
        },
        {
            "title": "Forma emas, prinsip",
            "type": "highlight",
            "text": """
            Mahalliy arxitekturadan
            faqat dekor emas,

            <br><br>

            <b>
            soya,
            hovli,
            ayvon,
            ritm,
            privacy
            </b>

            <br><br>

            kabi prinsiplarni ham o'rganish mumkin.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Bitta zamonaviy fasad yarating.

            <br><br>

            Unda faqat 2 ta
            mahalliy element ishlating.

            <br><br>

            Nega aynan shu elementlarni
            tanlaganingizni yozing.
            """,
        },
    ],

    "L04_M08_003": [
        {
            "title": "Deraza fasad kompozitsiyasining bir qismi",
            "type": "highlight",
            "text": """
            Deraza faqat ichkariga
            yorug'lik kirituvchi teshik emas.

            <br><br>

            Uning:

            <br><br>

            • o'lchami;<br>
            • proporsiyasi;<br>
            • ritmi;<br>
            • chuqurligi;<br>
            • soyalanishi

            <br><br>

            fasad xarakteriga ta'sir qiladi.
            """,
        },
        {
            "title": "Deraza ritmi",
            "type": "normal",
            "text": """
            Oynalar orasida
            ma'lum ritm va tartib bo'lsa,

            <br><br>

            fasad bir butun ko'rinishi mumkin.
            """,
        },
        {
            "title": "Tartibsiz ochilish",
            "type": "warning",
            "text": """
            Har bir xona derazasi
            faqat ichki reja bo'yicha
            tashqariga chiqarilib,

            <br><br>

            umumiy fasad kompozitsiyasi
            tekshirilmasa,

            <br><br>

            tashqi ko'rinish tartibsiz bo'lishi mumkin.
            """,
        },
        {
            "title": "Ayvon va soyalanish",
            "type": "normal",
            "text": """
            Ayvon yoki soyabon
            bir vaqtning o'zida:

            <br><br>

            • funksional;<br>
            • iqlimiy;<br>
            • kompozitsion

            <br><br>

            element bo'lishi mumkin.
            """,
        },
        {
            "title": "Chuqurlik",
            "type": "example",
            "text": """
            Deraza fasad tekisligidan
            biroz ichkarida joylashsa,

            <br><br>

            soya va chuqurlik
            fasadga kuchliroq plastika berishi mumkin.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Bir fasad chizing.

            <br><br>

            Unda:

            <br><br>

            • 3 ta deraza turi;<br>
            • kirish soyaboni;<br>
            • ayvon;<br>
            • bir xil ritm

            <br><br>

            yaratishga harakat qiling.
            """,
        },
    ],

    "L04_M08_004": [
        {
            "title": "Material ko'p bo'lsa fasad kuchli bo'ladimi?",
            "type": "highlight",
            "text": """
            Yo'q.

            <br><br>

            Ko'p material
            avtomatik ravishda
            sifatli fasad yaratmaydi.
            """,
        },
        {
            "title": "Asosiy material",
            "type": "normal",
            "text": """
            Fasad uchun
            bitta asosiy material yoki rang
            dominant bo'lishi mumkin.

            <br><br>

            Qolganlari esa
            aksent sifatida ishlaydi.
            """,
        },
        {
            "title": "Material ierarxiyasi",
            "type": "example",
            "text": """
            Masalan:

            <br><br>

            70% — asosiy silliq fasad<br>
            20% — teksturali material<br>
            10% — aksent

            <br><br>

            Bu qat'iy formula emas.

            <br><br>

            Maqsad — vizual ierarxiyani tushunish.
            """,
        },
        {
            "title": "Proporsiya",
            "type": "normal",
            "text": """
            Fasad elementlari:

            <br><br>

            • kirish;<br>
            • oynalar;<br>
            • ustunlar;<br>
            • tom;<br>
            • sokol

            <br><br>

            bir-biriga nisbatan
            proporsional ko'rinishi kerak.
            """,
        },
        {
            "title": "Bir qavatli uyda masshtab",
            "type": "warning",
            "text": """
            Bir qavatli uyga
            haddan tashqari katta portal
            yoki juda baland dekor qo'yilsa,

            <br><br>

            bino tabiiy proporsiyasini
            yo'qotishi mumkin.
            """,
        },
        {
            "title": "Rang",
            "type": "normal",
            "text": """
            Rang materialdan ajralgan holda
            emas, birgalikda qaraladi.

            <br><br>

            Juda ko'p rang
            fasadni parchalashi mumkin.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Bir fasad uchun:

            <br><br>

            • 1 asosiy material;<br>
            • 1 ikkilamchi material;<br>
            • 1 aksent material

            <br><br>

            tanlang.

            <br><br>

            Har birining qayerda
            ishlatilishini belgilang.
            """,
        },
    ],

    "L04_M08_005": [
        {
            "title": "Fasad auditini boshlaymiz",
            "type": "highlight",
            "text": """
            Endi fasadni
            “menga yoqdi / yoqmadi”
            bilan emas,

            <br><br>

            professional savollar bilan
            tekshiramiz.
            """,
        },
        {
            "title": "Xato 1 — asosiy kirish yo'qolgan",
            "type": "warning",
            "text": """
            Fasad chiroyli,

            <br><br>

            lekin odam
            qaysi eshik asosiy ekanini
            tushunmaydi.
            """,
        },
        {
            "title": "Xato 2 — juda ko'p material",
            "type": "warning",
            "text": """
            Tosh,
            g'isht,
            yog'och,
            metall,
            dekor,
            rangli panel

            <br><br>

            barchasi bir fasadda
            raqobat qiladi.
            """,
        },
        {
            "title": "Xato 3 — derazalar tartibsiz",
            "type": "warning",
            "text": """
            Ichki plan yaxshi,

            <br><br>

            lekin tashqi deraza ritmi
            umuman tekshirilmagan.
            """,
        },
        {
            "title": "Xato 4 — mahalliy dekor ortiqcha",
            "type": "warning",
            "text": """
            Mahalliy ruh yaratish o'rniga
            fasad juda ko'p dekor bilan
            to'ldirilgan.
            """,
        },
        {
            "title": "Xato 5 — iqlim unutildi",
            "type": "warning",
            "text": """
            Katta oynalar mavjud,

            <br><br>

            lekin quyosh va
            soyalanish umuman hisobga olinmagan.
            """,
        },
        {
            "title": "Xato 6 — proporsiya buzilgan",
            "type": "warning",
            "text": """
            Bir qavatli kichik uyda
            haddan tashqari ulkan kirish portali
            bino masshtabini buzgan.
            """,
        },
        {
            "title": "Professional checklist",
            "type": "example",
            "text": """
            Fasadni tekshiring:

            <br><br>

            <b>1.</b> Asosiy kirish o'qiladimi?<br><br>
            <b>2.</b> Fasad ichki plan bilan bog'liqmi?<br><br>
            <b>3.</b> Derazalarda ritm bormi?<br><br>
            <b>4.</b> Soyalanish ishlaydimi?<br><br>
            <b>5.</b> Materiallar soni nazoratdami?<br><br>
            <b>6.</b> Mahalliy element me'yoridami?<br><br>
            <b>7.</b> Umumiy proporsiya uyg'unmi?
            """,
        },
        {
            "title": "LEVEL 4 yakuniy mini-case",
            "type": "example",
            "text": """
            1 qavatli oilaviy uy uchun
            asosiy fasad konsepsiyasini yarating.

            <br><br>

            Talab:

            <br><br>

            • zamonaviy ko'rinish;<br>
            • aniq asosiy kirish;<br>
            • katta living oynasi;<br>
            • ayvon;<br>
            • quyoshdan himoya;<br>
            • 2 ta mahalliy element;<br>
            • 3 tadan ko'p asosiy material ishlatmaslik.

            <br><br>

            Har bir qaroringizga
            “nega?” deb javob yozing.
            """,
        },
        {
            "title": "LEVEL 4 yakuni",
            "type": "highlight",
            "text": """
            LEVEL 4 davomida siz:

            <br><br>

            ✓ O'zbek oilasi uchun uy;<br>
            ✓ mehmon kutish;<br>
            ✓ ichki hovli;<br>
            ✓ ayvon va terassa;<br>
            ✓ yozgi oshxona;<br>
            ✓ banja va yordamchi bino;<br>
            ✓ issiq iqlim;<br>
            ✓ mahalliy fasad

            <br><br>

            mavzularini bir tizim sifatida o'rgandingiz.

            <br><br>

            Keyingi qadam:
            <b>LEVEL 4 FINAL EXAM.</b>
            """,
        },
    ],
}


# ============================================================
# QUIZ
# ============================================================

LEVEL04_MODULE08_QUIZ = {
    "L04_M08_001": [
        {
            "code": "L04_Q106",
            "question": "Fasad faqat dekorativ tashqi ko'rinishmi?",
            "explanation": (
                "Fasad kirish, deraza, bino massasi, soyalanish va ichki reja bilan bog'liq."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L04_Q107",
            "question": "Fasaddagi deraza va eshiklar ichki reja bilan bog'liqmi?",
            "explanation": (
                "Ochilishlar ichki xonalar va tashqi kompozitsiya bilan birgalikda ishlaydi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L04_Q108",
            "question": "Asosiy kirish fasadda tushunarli o'qilishi foydalimi?",
            "explanation": (
                "Kirish fasad ierarxiyasining asosiy elementlaridan biri bo'lishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L04_M08_002": [
        {
            "code": "L04_Q109",
            "question": "Mahalliy ruh yaratish uchun eski fasadni to'liq nusxalash shartmi?",
            "explanation": (
                "Mahalliy prinsip va elementlarni zamonaviy tarzda talqin qilish mumkin."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L04_Q110",
            "question": "Ayvon va privacy ham mahalliy arxitektura prinsiplaridan ilhom olishi mumkinmi?",
            "explanation": (
                "Mahalliylik faqat dekor emas, fazoviy va iqlimiy prinsiplarni ham o'z ichiga oladi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L04_Q111",
            "question": "Har bir fasad elementiga juda ko'p dekor qo'shish doim yaxshi yechimmi?",
            "explanation": (
                "Ortiqcha bezak vizual shovqin yaratishi mumkin."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
    ],

    "L04_M08_003": [
        {
            "code": "L04_Q112",
            "question": "Deraza ritmi fasad kompozitsiyasiga ta'sir qiladimi?",
            "explanation": (
                "Deraza o'lchami, tartibi va ritmi fasadning bir butun ko'rinishiga ta'sir qiladi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L04_Q113",
            "question": "Ayvon bir vaqtning o'zida funksional va kompozitsion element bo'lishi mumkinmi?",
            "explanation": (
                "Ayvon soya yaratishi va fasad xarakterini shakllantirishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L04_Q114",
            "question": "Ichki reja yaxshi bo'lsa fasaddagi deraza tartibini tekshirish shart emasmi?",
            "explanation": (
                "Ichki reja va tashqi kompozitsiya birgalikda tekshiriladi."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
    ],

    "L04_M08_004": [
        {
            "code": "L04_Q115",
            "question": "Ko'p material ishlatish avtomatik ravishda kuchli fasad yaratadimi?",
            "explanation": (
                "Materiallar sonidan ko'ra ularning ierarxiyasi va uyg'unligi muhim."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L04_Q116",
            "question": "Fasad elementlarining proporsiyasi muhimmi?",
            "explanation": (
                "Kirish, deraza, ustun va boshqa elementlarning o'zaro masshtabi fasad sifatiga ta'sir qiladi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L04_Q117",
            "question": "Bir qavatli kichik uyda juda ulkan portal proporsiyani buzishi mumkinmi?",
            "explanation": (
                "Element masshtabi umumiy bino hajmiga mos bo'lishi kerak."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L04_M08_005": [
        {
            "code": "L04_Q118",
            "question": "Asosiy kirish fasadda yo'qolib qolishi kompozitsion xato bo'lishi mumkinmi?",
            "explanation": (
                "Kirishning vizual ierarxiyasi foydalanuvchiga yo'nalish beradi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L04_Q119",
            "question": "Mahalliy elementlarni me'yorida ishlatish muhimmi?",
            "explanation": (
                "Mahalliy xarakter yaratish va ortiqcha dekor o'rtasida balans kerak."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L04_Q120",
            "question": "Mahalliy fasad auditidagi muhim savollardan biri qaysi?",
            "explanation": (
                "Kirish, deraza, soya, material, mahalliy element va proporsiya birgalikda tekshiriladi."
            ),
            "options": [
                ("A", "Asosiy kirish o'qiladimi va fasad mantiqiymi?", True),
                ("B", "Faqat bitta bezak chiroylimi?", False),
            ],
        },
    ],
}


# ============================================================
# DATABASE SEED
# ============================================================

def seed_level04_module08():
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
        ) in LEVEL04_MODULE08_LESSONS:

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
