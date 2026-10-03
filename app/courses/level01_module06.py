from database.database import get_connection


# ============================================================
# LEVEL 1
# MODULE 06 - ARXITEKTURA USLUBLARI
# ============================================================

LEVEL01_MODULE06_LESSONS = [
    (
        "L01_M06",
        "L01_M06_001",
        "Arxitektura uslubi nima?",
        "theory",
        "Arxitektura uslubi, davr, shakl va vizual til tushunchalarini o'rganish.",
        1,
        40,
        20,
    ),
    (
        "L01_M06",
        "L01_M06_002",
        "Tarixiy uslublarni o'qish",
        "theory",
        "Tarixiy arxitekturadagi asosiy kompozitsion belgilarni ajratishni o'rganish.",
        2,
        45,
        20,
    ),
    (
        "L01_M06",
        "L01_M06_003",
        "Zamonaviy arxitektura",
        "theory",
        "Modern, minimalistik va zamonaviy turar joy arxitekturasining asosiy tamoyillarini tushunish.",
        3,
        45,
        20,
    ),
    (
        "L01_M06",
        "L01_M06_004",
        "Uslublarni aralashtirish",
        "practice",
        "Turli arxitektura tillarini uyg'unlashtirish va stilistik konfliktlarni aniqlash.",
        4,
        50,
        20,
    ),
    (
        "L01_M06",
        "L01_M06_005",
        "Arxitektura uslubi auditi",
        "practice",
        "Uy fasadi va hajmini stilistik yaxlitlik bo'yicha professional tahlil qilish.",
        5,
        60,
        25,
    ),
]


# ============================================================
# CONTENT
# ============================================================

LEVEL01_MODULE06_CONTENT = {
    "L01_M06_001": [
        {
            "title": "Arxitektura uslubi nima?",
            "type": "highlight",
            "text": """
            Arxitektura uslubi —
            binoning tashqi ko'rinishi,
            proporsiyasi,
            materiali,
            detali va kompozitsiyasida
            takrorlanadigan umumiy vizual til.

            <br><br>

            Uslub faqat bezak emas.
            U binoning qanday fikr bilan
            yaratilganini ham ko'rsatadi.
            """,
        },
        {
            "title": "Uslubni qanday taniymiz?",
            "type": "normal",
            "text": """
            Binoni ko'rganda quyidagilarga qarang:

            <br><br>

            • umumiy hajm;<br>
            • tom shakli;<br>
            • deraza va eshik ritmi;<br>
            • materiallar;<br>
            • ranglar;<br>
            • dekor miqdori;<br>
            • proporsiya;<br>
            • detal xarakteri.
            """,
        },
        {
            "title": "Uslub va moda bir xil emas",
            "type": "warning",
            "text": """
            Trenddagi bitta material yoki
            bezakni ishlatish
            binoni avtomatik ravishda
            ma'lum uslubga kiritmaydi.

            <br><br>

            Uslub butun bino bo'ylab
            izchil ishlashi kerak.
            """,
        },
        {
            "title": "Tasavvur qiling",
            "type": "example",
            "text": """
            Bir uyda:

            <br><br>

            • klassik ustunlar;<br>
            • juda minimalistik derazalar;<br>
            • loft g'isht;<br>
            • sharqona ornament;<br>
            • futuristik tom

            <br><br>

            bir vaqtning o'zida
            ishlatilgan.

            <br><br>

            Har bir element alohida
            chiroyli bo'lishi mumkin,
            lekin umumiy arxitektura
            tartibsiz ko'rinishi mumkin.
            """,
        },
        {
            "title": "Mini-vazifa",
            "type": "example",
            "text": """
            O'zingiz yoqtirgan
            3 ta uy rasmini tanlang.

            <br><br>

            Har biri uchun yozing:

            <br><br>

            • hajm qanday?<br>
            • tom qanday?<br>
            • materiallar qanday?<br>
            • deraza ritmi qanday?<br>
            • dekor ko'pmi yoki kammi?
            """,
        },
    ],

    "L01_M06_002": [
        {
            "title": "Tarixiy arxitekturani ko'chirish emas",
            "type": "highlight",
            "text": """
            Tarixiy uslublarni o'rganishning maqsadi
            eski binoni aynan nusxalash emas.

            <br><br>

            Maqsad —
            proporsiya,
            ritm,
            simmetriya,
            masshtab
            va detal mantiqini tushunish.
            """,
        },
        {
            "title": "Klassik kompozitsiya",
            "type": "normal",
            "text": """
            Ko'plab klassik binolarda:

            <br><br>

            • aniq markaz;<br>
            • simmetriya;<br>
            • kuchli vertikal yoki gorizontal o'qlar;<br>
            • takroriy ritm;<br>
            • qatlamli fasad

            <br><br>

            kuzatiladi.
            """,
        },
        {
            "title": "Mahalliy arxitektura",
            "type": "normal",
            "text": """
            Mahalliy tarixiy arxitekturada
            faqat ornament emas,
            makon tashkiloti ham muhim.

            <br><br>

            Masalan:

            <br><br>

            • hovli;<br>
            • ayvon;<br>
            • soyali o'tish;<br>
            • ichki va tashqi makon aloqasi.
            """,
        },
        {
            "title": "Xato",
            "type": "warning",
            "text": """
            Faqat tarixiy ornament qo'shib,
            qolgan bino kompozitsiyasini
            umuman boshqa tilda qilish

            <br><br>

            ko'pincha yuzaki stilizatsiyaga olib keladi.
            """,
        },
        {
            "title": "Mini-vazifa",
            "type": "example",
            "text": """
            Bitta tarixiy bino tanlang.

            <br><br>

            Unda:

            <br><br>

            • markaz;<br>
            • ritm;<br>
            • simmetriya;<br>
            • proporsiya;<br>
            • asosiy detal

            <br><br>

            qayerda ekanini belgilang.
            """,
        },
    ],

    "L01_M06_003": [
        {
            "title": "Zamonaviy arxitektura",
            "type": "highlight",
            "text": """
            Zamonaviy arxitekturada
            ko'pincha shakl,
            funksiya,
            material
            va texnologiya o'rtasidagi
            bog'lanish muhim.
            """,
        },
        {
            "title": "Minimalizm",
            "type": "normal",
            "text": """
            Minimalizm —
            shunchaki oq rang
            yoki bezaksiz fasad emas.

            <br><br>

            Unda keraksiz element kamayadi,
            lekin proporsiya,
            detal
            va material sifati
            yanada muhimlashadi.
            """,
        },
        {
            "title": "Modern residential",
            "type": "normal",
            "text": """
            Zamonaviy turar joylarda:

            <br><br>

            • sodda hajmlar;<br>
            • katta openinglar;<br>
            • indoor-outdoor aloqa;<br>
            • material kontrasti;<br>
            • aniq kompozitsiya

            <br><br>

            ko'p uchrashi mumkin.
            """,
        },
        {
            "title": "Loft elementlari",
            "type": "normal",
            "text": """
            Loft vizual tilida
            g'isht,
            beton,
            metall,
            ochiq konstruktiv xarakter
            kabi elementlar ishlatilishi mumkin.

            <br><br>

            Lekin bitta g'isht devor
            butun binoni loft qilib qo'ymaydi.
            """,
        },
        {
            "title": "Xato",
            "type": "warning",
            "text": """
            Zamonaviy arxitekturani
            faqat katta oynalar
            va tekis tom bilan
            tenglashtirmang.

            <br><br>

            Asosiy mezon —
            umumiy dizayn mantiqi.
            """,
        },
        {
            "title": "Mini-vazifa",
            "type": "example",
            "text": """
            Bir zamonaviy uy fasadini tanlang.

            <br><br>

            Undagi:

            • asosiy hajm;<br>
            • dominant element;<br>
            • materiallar;<br>
            • opening ritmi;<br>
            • bo'sh va to'liq yuzalar

            <br><br>

            nisbatini tahlil qiling.
            """,
        },
    ],

    "L01_M06_004": [
        {
            "title": "Uslublarni aralashtirish mumkinmi?",
            "type": "highlight",
            "text": """
            Ha, mumkin.

            <br><br>

            Lekin turli uslublar
            tasodifiy yig'ilmasligi kerak.

            <br><br>

            Ularni birlashtiruvchi
            umumiy kompozitsion qoida bo'lishi kerak.
            """,
        },
        {
            "title": "Asosiy va ikkilamchi til",
            "type": "normal",
            "text": """
            Kuchli yechimda
            odatda bitta asosiy dizayn tili bo'ladi.

            <br><br>

            Ikkinchi uslub
            detal,
            material
            yoki aksent sifatida ishlashi mumkin.
            """,
        },
        {
            "title": "Masalan",
            "type": "example",
            "text": """
            Zamonaviy uy:

            <br><br>

            • sodda massing;<br>
            • zamonaviy openinglar;<br>
            • neytral materiallar

            <br><br>

            bilan qurilgan.

            <br><br>

            Mahalliy xarakter esa
            ayvon,
            yog'och detal
            yoki ornament aksenti
            orqali berilishi mumkin.
            """,
        },
        {
            "title": "Stilistik konflikt",
            "type": "warning",
            "text": """
            Har bir fasad qismida
            boshqa dizayn tili ishlatilsa,
            bino yaxlitligini yo'qotishi mumkin.

            <br><br>

            Savol:

            <br><br>

            “Bu element umumiy konsepsiyani
            kuchaytirayaptimi yoki buzayaptimi?”
            """,
        },
        {
            "title": "Mini-vazifa",
            "type": "example",
            "text": """
            Zamonaviy + mahalliy elementli
            bitta uy konsepsiyasi tuzing.

            <br><br>

            Asosiy uslubni belgilang.

            <br><br>

            Keyin faqat 2–3 ta
            ikkilamchi element bilan
            mahalliy xarakter qo'shing.
            """,
        },
    ],

    "L01_M06_005": [
        {
            "title": "Uslub auditi",
            "type": "highlight",
            "text": """
            Endi fasadni
            “yoqdi / yoqmadi”
            darajasida emas,

            <br><br>

            aniq mezonlar bilan
            tahlil qilamiz.
            """,
        },
        {
            "title": "1. Massing",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • asosiy hajm tushunarlimi?<br>
            • kompozitsiya tartiblimi?<br>
            • ortiqcha shakllar bormi?
            """,
        },
        {
            "title": "2. Proporsiya",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • fasad qismlari bir-biriga mosmi?<br>
            • openinglar juda katta yoki kichik ko'rinmayaptimi?<br>
            • bino odam masshtabiga mos seziladimi?
            """,
        },
        {
            "title": "3. Ritm",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • derazalar tartibli ritm beradimi?<br>
            • takrorlanish mantiqiymi?<br>
            • tasodifiy openinglar bormi?
            """,
        },
        {
            "title": "4. Material",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • materiallar soni boshqarilganmi?<br>
            • ular bir-birini qo'llab-quvvatlayaptimi?<br>
            • bitta material ortiqcha dominant bo'lib qolmaganmi?
            """,
        },
        {
            "title": "5. Detal",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • dekor umumiy uslubga mosmi?<br>
            • detal haddan tashqari ko'p emasmi?<br>
            • barcha elementlar bir xil vizual tilda gapiryaptimi?
            """,
        },
        {
            "title": "Professional checklist",
            "type": "example",
            "text": """
            <b>1.</b> Asosiy uslub tushunarlimi?<br><br>
            <b>2.</b> Massing yaxlitmi?<br><br>
            <b>3.</b> Proporsiya ishlaydimi?<br><br>
            <b>4.</b> Ritm tartiblimi?<br><br>
            <b>5.</b> Materiallar uyg'unmi?<br><br>
            <b>6.</b> Detallar bir xil tildami?<br><br>
            <b>7.</b> Keraksiz stilistik konflikt yo'qmi?
            """,
        },
        {
            "title": "LEVEL 1 yakuni",
            "type": "highlight",
            "text": """
            Siz endi:

            <br><br>

            ✓ kompozitsiyani tushunasiz;<br>
            ✓ proporsiyani tahlil qilasiz;<br>
            ✓ ritmni ko'rasiz;<br>
            ✓ simmetriya va asimmetriyani farqlaysiz;<br>
            ✓ forma va hajmni 3D fikrlaysiz;<br>
            ✓ asosiy arxitektura uslublarini tahlil qilasiz.

            <br><br>

            Keyingi bosqich:
            <b>LEVEL 2 — Spatial Thinking.</b>
            """,
        },
    ],
}


# ============================================================
# QUIZ
# Q076-Q090
# ============================================================

LEVEL01_MODULE06_QUIZ = {
    "L01_M06_001": [
        {
            "code": "L01_Q076",
            "question": "Arxitektura uslubi faqat bezakdan iboratmi?",
            "explanation": "Uslub hajm, proporsiya, material, opening va detallarni ham qamrab oladi.",
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L01_Q077",
            "question": "Binoning tomi, derazalari va materiallari uslubni aniqlashga yordam beradimi?",
            "explanation": "Bu elementlar binoning umumiy vizual tilini shakllantiradi.",
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L01_Q078",
            "question": "Bitta trend material ishlatilsa bino avtomatik ravishda ma'lum uslubga kiradimi?",
            "explanation": "Uslub butun kompozitsiya bo'ylab izchil ishlashi kerak.",
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
    ],

    "L01_M06_002": [
        {
            "code": "L01_Q079",
            "question": "Tarixiy arxitekturani o'rganishda proporsiya va ritm muhimmi?",
            "explanation": "Tarixiy arxitekturaning kompozitsion mantiqini tushunish muhim.",
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L01_Q080",
            "question": "Mahalliy arxitektura faqat ornamentdan iboratmi?",
            "explanation": "Hovli, ayvon va makon tashkiloti ham muhim.",
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L01_Q081",
            "question": "Tarixiy elementni zamonaviy loyihaga qo'shganda umumiy kompozitsiya tekshirilishi kerakmi?",
            "explanation": "Element umumiy dizayn tiliga mos bo'lishi kerak.",
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L01_M06_003": [
        {
            "code": "L01_Q082",
            "question": "Minimalizm faqat oq rang va bezaksiz fasad deganimi?",
            "explanation": "Minimalizmda proporsiya, detal va material sifati juda muhim.",
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L01_Q083",
            "question": "Zamonaviy turar joyda indoor-outdoor aloqa muhim dizayn elementi bo'lishi mumkinmi?",
            "explanation": "Ichki va tashqi makon aloqasi zamonaviy uylarning muhim jihatlaridan biri bo'lishi mumkin.",
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L01_Q084",
            "question": "Bitta g'isht devor ishlatilsa bino avtomatik loft uslubiga aylanadimi?",
            "explanation": "Uslub bitta material emas, umumiy dizayn tizimidir.",
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
    ],

    "L01_M06_004": [
        {
            "code": "L01_Q085",
            "question": "Turli arxitektura uslublarini uyg'unlashtirish mumkinmi?",
            "explanation": "Mumkin, lekin asosiy konsepsiya va umumiy kompozitsion qoida saqlanishi kerak.",
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L01_Q086",
            "question": "Har bir fasad qismiga alohida uslub berish har doim yaxlit kompozitsiya yaratadimi?",
            "explanation": "Tasodifiy aralashma stilistik konflikt keltirib chiqarishi mumkin.",
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L01_Q087",
            "question": "Asosiy dizayn tili va ikkilamchi aksentlarni ajratish foydalimi?",
            "explanation": "Bu stilistik yaxlitlikni saqlashga yordam beradi.",
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L01_M06_005": [
        {
            "code": "L01_Q088",
            "question": "Arxitektura uslubi auditida massing, proporsiya va ritm tekshiriladimi?",
            "explanation": "Ular fasadning asosiy kompozitsion mezonlari.",
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L01_Q089",
            "question": "Ko'p material ishlatish avtomatik ravishda fasadni professional qiladimi?",
            "explanation": "Materiallar boshqarilgan va umumiy konsepsiyaga mos bo'lishi kerak.",
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L01_Q090",
            "question": "Professional stilistik auditning to'g'ri ketma-ketligi qaysi?",
            "explanation": "Umumiy uslub massing, proporsiya, ritm, material va detallar bilan birga tekshiriladi.",
            "options": [
                (
                    "A",
                    "Uslub → massing → proporsiya → ritm → material → detal → audit",
                    True,
                ),
                (
                    "B",
                    "Faqat dekorni ko'paytirish",
                    False,
                ),
            ],
        },
    ],
}


# ============================================================
# DATABASE SEED
# ============================================================

def seed_level01_module06():
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
        ) in LEVEL01_MODULE06_LESSONS:

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
