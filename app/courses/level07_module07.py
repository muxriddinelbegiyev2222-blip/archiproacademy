from database.database import get_connection


# ============================================================
# LEVEL 7
# MODULE 07 - CLASSIFICATION
# ============================================================

LEVEL07_MODULE07_LESSONS = [
    (
        "L07_M07",
        "L07_M07_001",
        "BIM Classification tushunchasi",
        "theory",
        "Model elementlarini ularning vazifasi va BIM ma'nosi bo'yicha tartibli klassifikatsiyalash mantig'ini tushunish.",
        1,
        30,
        20,
    ),
    (
        "L07_M07",
        "L07_M07_002",
        "Classification va element turi",
        "theory",
        "Geometrik element turi bilan BIM klassifikatsiyasi o'rtasidagi farqni tushunish.",
        2,
        35,
        20,
    ),
    (
        "L07_M07",
        "L07_M07_003",
        "Classification va Properties",
        "practice",
        "Classification orqali Properties va BIM ma'lumotlarini mantiqiy tashkil qilish.",
        3,
        35,
        20,
    ),
    (
        "L07_M07",
        "L07_M07_004",
        "Classification va Schedules",
        "practice",
        "Klassifikatsiyalangan elementlarni Schedule va audit workflowida boshqarish.",
        4,
        40,
        20,
    ),
    (
        "L07_M07",
        "L07_M07_005",
        "Classification professional audit",
        "practice",
        "Element klassifikatsiyasi, Properties va Schedule natijalarini kompleks tekshirish.",
        5,
        40,
        25,
    ),
]


# ============================================================
# CONTENT
# ============================================================

LEVEL07_MODULE07_CONTENT = {
    "L07_M07_001": [
        {
            "title": "Classification nima?",
            "type": "highlight",
            "text": """
            Classification —
            BIM elementni

            <br><br>

            uning ma'nosi,
            vazifasi yoki
            tizimdagi o'rni bo'yicha

            <br><br>

            ma'lum sinfga
            ajratish usuli.
            """,
        },
        {
            "title": "Nega kerak?",
            "type": "normal",
            "text": """
            Katta BIM modelda
            yuzlab yoki minglab
            elementlar bo'lishi mumkin.

            <br><br>

            Faqat geometriyaga
            qarab ishlash

            <br><br>

            ma'lumot boshqaruvini
            qiyinlashtiradi.
            """,
        },
        {
            "title": "Tasavvur qiling",
            "type": "example",
            "text": """
            Modelda:

            • devorlar;<br>
            • eshiklar;<br>
            • derazalar;<br>
            • ustunlar;<br>
            • mebel;<br>
            • boshqa elementlar

            <br><br>

            mavjud.

            <br><br>

            Classification
            ularni BIM ma'nosi
            bo'yicha tartibga
            solishga yordam beradi.
            """,
        },
        {
            "title": "Classification — nom emas",
            "type": "warning",
            "text": """
            Element nomini
            o'zgartirishning o'zi

            <br><br>

            uni to'g'ri
            klassifikatsiyalash
            degani emas.

            <br><br>

            Classification
            strukturaviy BIM
            ma'lumotidir.
            """,
        },
        {
            "title": "BIM ma'lumot strukturasi",
            "type": "highlight",
            "text": """
            Tartibli Classification
            keyinchalik:

            <br><br>

            • Properties;<br>
            • Schedules;<br>
            • audit;<br>
            • ma'lumot almashinuvi

            <br><br>

            kabi jarayonlarni
            boshqarishga yordam beradi.
            """,
        },
        {
            "title": "Noto'g'ri klassifikatsiya",
            "type": "warning",
            "text": """
            Element geometriyasi
            to'g'ri bo'lishi mumkin,

            <br><br>

            lekin Classification
            noto'g'ri bo'lsa,

            <br><br>

            keyingi BIM
            ma'lumot jarayonlarida
            xato paydo bo'lishi mumkin.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Kichik uy modelidagi
            10 ta elementni
            yozing.

            <br><br>

            Har biri uchun:

            • bu nima?<br>
            • BIM ma'nosi nima?<br>
            • qaysi umumiy guruhga kiradi?

            <br><br>

            degan savollarga
            javob bering.
            """,
        },
    ],

    "L07_M07_002": [
        {
            "title": "Element Type va Classification",
            "type": "highlight",
            "text": """
            Element Type —
            element qaysi
            Archicad vositasi
            orqali yaratilganini
            bildirishi mumkin.

            <br><br>

            Classification esa
            elementning BIM
            ma'nosini ifodalaydi.
            """,
        },
        {
            "title": "Bir xil emas",
            "type": "warning",
            "text": """
            Geometrik tool
            va BIM ma'nosi

            <br><br>

            har doim aynan
            bir xil tushuncha emas.
            """,
        },
        {
            "title": "Tasavvur qiling",
            "type": "example",
            "text": """
            Bir element
            geometrik jihatdan
            ma'lum tool orqali
            yaratilgan.

            <br><br>

            Lekin loyiha
            ma'nosida uning
            vazifasi boshqacha
            bo'lishi mumkin.

            <br><br>

            Shu sabab
            Classification
            alohida ahamiyatga ega.
            """,
        },
        {
            "title": "Geometriya boshqa, ma'no boshqa",
            "type": "normal",
            "text": """
            BIM workflowda
            elementning:

            <br><br>

            • geometriyasi;<br>
            • materiali;<br>
            • Property qiymatlari;<br>
            • Classification

            <br><br>

            turli ma'lumot
            qatlamlari hisoblanadi.
            """,
        },
        {
            "title": "Noto'g'ri yondashuv",
            "type": "warning",
            "text": """
            “Bu devor toolida
            chizilgan ekan,
            demak BIM ma'nosi
            avtomatik to'g'ri”

            <br><br>

            deb o'ylash
            xavfli.

            <br><br>

            Classification
            alohida tekshiriladi.
            """,
        },
        {
            "title": "Tizimlilik",
            "type": "highlight",
            "text": """
            Professional modelda
            bir xil vazifadagi
            elementlar

            <br><br>

            izchil BIM
            klassifikatsiyasiga
            ega bo'lishi kerak.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            5 ta model elementi
            tanlang.

            <br><br>

            Har biri uchun:

            1. qaysi tool bilan yaratilgan?<br>
            2. BIM vazifasi nima?<br>
            3. Classification qanday bo'lishi kerak?

            <br><br>

            deb yozing.
            """,
        },
    ],

    "L07_M07_003": [
        {
            "title": "Classification + Properties",
            "type": "highlight",
            "text": """
            Classification
            va Properties
            birgalikda

            <br><br>

            BIM ma'lumot
            strukturasini
            kuchaytiradi.
            """,
        },
        {
            "title": "Nega bog'liq?",
            "type": "normal",
            "text": """
            Ayrim Properties
            faqat ma'lum
            turdagi elementlar uchun
            ma'noli bo'lishi mumkin.

            <br><br>

            Classification
            qaysi elementga
            qaysi ma'lumot
            tegishli ekanini
            tartibga solishga
            yordam beradi.
            """,
        },
        {
            "title": "Tasavvur qiling",
            "type": "example",
            "text": """
            Door elementlarida
            eshikka tegishli
            Properties bor.

            <br><br>

            Wall elementlarda esa
            boshqa ma'lumotlar
            kerak bo'lishi mumkin.

            <br><br>

            Classification
            BIM ma'lumotlarini
            mantiqan ajratishga
            yordam beradi.
            """,
        },
        {
            "title": "Keraksiz Property",
            "type": "warning",
            "text": """
            Har bir Property
            barcha elementlarda
            ko'rinishi

            <br><br>

            ma'lumot tizimini
            ortiqcha murakkablashtirishi
            mumkin.
            """,
        },
        {
            "title": "Classification xatosi",
            "type": "warning",
            "text": """
            Element noto'g'ri
            klassifikatsiyalansa,

            <br><br>

            unga noto'g'ri
            Property to'plami
            tegishli bo'lishi
            mumkin.
            """,
        },
        {
            "title": "Ma'lumot sifati",
            "type": "highlight",
            "text": """
            To'g'ri BIM ma'lumot:

            <br><br>

            element
            + Classification
            + Properties
            + qiymatlar

            <br><br>

            birgalikda
            to'g'ri bo'lganda
            hosil bo'ladi.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Door va Wall
            uchun alohida:

            <br><br>

            • Classification;<br>
            • 3 tadan Property

            <br><br>

            konsepsiyasini yozing.

            <br><br>

            Nima uchun
            bu Properties aynan
            shu elementga
            tegishli ekanini
            tushuntiring.
            """,
        },
    ],

    "L07_M07_004": [
        {
            "title": "Classification + Schedules",
            "type": "highlight",
            "text": """
            Klassifikatsiyalangan
            BIM elementlarni

            <br><br>

            Schedule orqali
            guruhlash,
            filtrlash
            va audit qilish
            osonlashadi.
            """,
        },
        {
            "title": "Schedule Criteria",
            "type": "normal",
            "text": """
            Schedule Criteria
            modeldan kerakli
            elementlarni

            <br><br>

            ma'lum shartlar
            orqali tanlaydi.

            <br><br>

            Classification
            bu tanlovda
            foydali BIM
            ma'lumot bo'lishi mumkin.
            """,
        },
        {
            "title": "Tasavvur qiling",
            "type": "example",
            "text": """
            Siz faqat
            ma'lum BIM sinfiga
            kiradigan elementlarni

            <br><br>

            bitta Schedule'da
            tekshirmoqchisiz.

            <br><br>

            Classification
            elementlarni mantiqiy
            ajratishga yordam beradi.
            """,
        },
        {
            "title": "Audit uchun foydasi",
            "type": "highlight",
            "text": """
            Schedule orqali
            quyidagilarni aniqlash
            mumkin:

            <br><br>

            • Classification bo'sh elementlar;<br>
            • noto'g'ri sinfdagi elementlar;<br>
            • bir xil vazifada turli klassifikatsiya;<br>
            • ma'lumotdagi izchillik muammolari.
            """,
        },
        {
            "title": "Faqat Schedule'ga ishonmang",
            "type": "warning",
            "text": """
            Schedule natijasi
            model ma'lumotiga
            bog'liq.

            <br><br>

            Model noto'g'ri
            klassifikatsiyalangan bo'lsa,

            <br><br>

            Schedule ham
            noto'g'ri natija
            berishi mumkin.
            """,
        },
        {
            "title": "Audit aylanishi",
            "type": "normal",
            "text": """
            Professional workflow:

            <br><br>

            Model
            → Classification
            → Properties
            → Schedule
            → xatoni topish
            → modelni tuzatish
            → qayta audit.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Classification audit
            Schedule konsepsiyasini
            tuzing.

            <br><br>

            Unda kamida:

            • element ID;<br>
            • element turi;<br>
            • Classification;<br>
            • bitta muhim Property

            <br><br>

            ko'rsatilishini rejalashtiring.
            """,
        },
    ],

    "L07_M07_005": [
        {
            "title": "Classification professional audit",
            "type": "highlight",
            "text": """
            Audit zanjiri:

            <br><br>

            Element
            → Classification
            → Properties
            → Schedule
            → tekshiruv.
            """,
        },
        {
            "title": "1. Classification mavjudmi?",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • kerakli elementlar klassifikatsiyalanganmi?<br>
            • bo'sh Classification qolmaganmi?
            """,
        },
        {
            "title": "2. Classification to'g'rimi?",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • element vazifasiga mosmi?<br>
            • tasodifiy sinf tanlanmaganmi?<br>
            • bir xil elementlarda izchillik bormi?
            """,
        },
        {
            "title": "3. Properties",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • tegishli Properties mavjudmi?<br>
            • keraksiz Properties chiqmayaptimi?<br>
            • qiymatlar to'ldirilganmi?
            """,
        },
        {
            "title": "4. Schedule audit",
            "type": "example",
            "text": """
            Schedule'da tekshiring:

            <br><br>

            • noodatiy Classification qiymatlari bormi?<br>
            • bo'sh satrlar bormi?<br>
            • bir xil elementlar turlicha klassifikatsiyalanganmi?
            """,
        },
        {
            "title": "5. Naming va standart",
            "type": "normal",
            "text": """
            BIM klassifikatsiya
            tizimi loyiha
            jamoasiga tushunarli

            <br><br>

            va izchil
            qo'llanilishi kerak.
            """,
        },
        {
            "title": "Xatoni toping",
            "type": "warning",
            "text": """
            Modeldagi
            30 ta elementdan:

            <br><br>

            • 5 tasida Classification yo'q;<br>
            • 4 tasi noto'g'ri sinfda;<br>
            • bir xil eshiklar ikki xil klassifikatsiyada;<br>
            • ayrim Properties chiqmayapti;<br>
            • Schedule'da natijalar aralash.

            <br><br>

            Geometriya yaxshi,
            lekin BIM ma'lumot
            strukturasi noto'g'ri.
            """,
        },
        {
            "title": "Professional checklist",
            "type": "example",
            "text": """
            Classification tizimini
            tekshiring:

            <br><br>

            <b>1.</b> Barcha kerakli elementlarda Classification bormi?<br><br>
            <b>2.</b> Classification element vazifasiga mosmi?<br><br>
            <b>3.</b> Bir xil turdagi elementlarda izchillik bormi?<br><br>
            <b>4.</b> Properties to'g'ri ishlayaptimi?<br><br>
            <b>5.</b> Schedule audit qilinganmi?<br><br>
            <b>6.</b> Noto'g'ri va bo'sh qiymatlar tuzatilganmi?
            """,
        },
        {
            "title": "Modul yakuni",
            "type": "highlight",
            "text": """
            Siz endi:

            <br><br>

            ✓ BIM Classification tushunchasini bilasiz;<br>
            ✓ element turi va Classification farqini tushunasiz;<br>
            ✓ Classification va Properties aloqasini bilasiz;<br>
            ✓ Classification'ni Schedules bilan ishlatasiz;<br>
            ✓ BIM ma'lumot strukturasini audit qilasiz.

            <br><br>

            Keyingi modul:
            <b>Hotlink va Modules.</b>
            """,
        },
    ],
}


# ============================================================
# QUIZ
# Q091-Q105
# ============================================================

LEVEL07_MODULE07_QUIZ = {
    "L07_M07_001": [
        {
            "code": "L07_Q091",
            "question": "Classification BIM elementlarni ma'nosi va vazifasi bo'yicha tartiblashga yordam beradimi?",
            "explanation": (
                "Classification elementlarni BIM ma'nosi bo'yicha ma'lum sinflarga ajratishga yordam beradi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L07_Q092",
            "question": "Element nomini o'zgartirishning o'zi to'g'ri BIM Classification hisoblanadimi?",
            "explanation": (
                "Classification oddiy nom emas, u strukturaviy BIM ma'lumotidir."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L07_Q093",
            "question": "Noto'g'ri Classification keyingi BIM ma'lumot jarayonlariga ta'sir qilishi mumkinmi?",
            "explanation": (
                "Properties, Schedules va audit natijalari Classification ma'lumotiga bog'liq bo'lishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L07_M07_002": [
        {
            "code": "L07_Q094",
            "question": "Element Tool va BIM Classification har doim aynan bir xil tushunchami?",
            "explanation": (
                "Tool element qanday yaratilganini, Classification esa uning BIM ma'nosini ifodalashi mumkin."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L07_Q095",
            "question": "Bir xil vazifadagi elementlarda Classification izchil bo'lishi kerakmi?",
            "explanation": (
                "Izchil Classification model ma'lumotining tartibli bo'lishiga yordam beradi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L07_Q096",
            "question": "Element geometriyasi to'g'ri bo'lsa Classification'ni tekshirish shart emasmi?",
            "explanation": (
                "Geometriya va BIM klassifikatsiyasi alohida ma'lumot qatlamlari bo'lib, ikkalasi ham tekshiriladi."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
    ],

    "L07_M07_003": [
        {
            "code": "L07_Q097",
            "question": "Classification qaysi Properties ma'lum elementlarga tegishli bo'lishini tashkil qilishda yordam berishi mumkinmi?",
            "explanation": (
                "Classification va Properties birgalikda BIM ma'lumot strukturasini mantiqiy tashkil qilishga yordam beradi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L07_Q098",
            "question": "Har bir Property barcha elementlarda ko'rinishi shartmi?",
            "explanation": (
                "Properties maqsadiga qarab faqat tegishli elementlarda ishlatilishi mumkin."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L07_Q099",
            "question": "Noto'g'ri Classification noto'g'ri BIM ma'lumot strukturasiga olib kelishi mumkinmi?",
            "explanation": (
                "Element noto'g'ri sinfga kiritilsa tegishli Properties va boshqa BIM jarayonlari ham noto'g'ri ishlashi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L07_M07_004": [
        {
            "code": "L07_Q100",
            "question": "Classification Schedule Criteria va auditda foydalanilishi mumkinmi?",
            "explanation": (
                "Classification model elementlarini mantiqiy filtrlash va tahlil qilishda ishlatilishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L07_Q101",
            "question": "Schedule orqali Classification bo'sh yoki noodatiy elementlarni aniqlash mumkinmi?",
            "explanation": (
                "Schedule Classification ma'lumotlarini bir joyda ko'rsatib auditni osonlashtirishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L07_Q102",
            "question": "Model noto'g'ri klassifikatsiyalangan bo'lsa Schedule har doim avtomatik to'g'ri natija beradimi?",
            "explanation": (
                "Schedule modeldagi ma'lumotga tayanadi, shuning uchun noto'g'ri Classification noto'g'ri natijaga olib kelishi mumkin."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
    ],

    "L07_M07_005": [
        {
            "code": "L07_Q103",
            "question": "Classification auditida bo'sh va noto'g'ri klassifikatsiyalar tekshiriladimi?",
            "explanation": (
                "Professional audit elementlarning Classification mavjudligi va to'g'riligini tekshiradi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L07_Q104",
            "question": "Geometriya yaxshi bo'lsa BIM ma'lumot strukturasidagi xatolar ahamiyatsizmi?",
            "explanation": (
                "BIM model sifati geometriya bilan birga ma'lumot strukturasining to'g'riligiga ham bog'liq."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L07_Q105",
            "question": "Classification bilan professional ishlashdagi to'g'ri workflow qaysi?",
            "explanation": (
                "Element klassifikatsiyalanadi, tegishli Properties tekshiriladi, Schedule orqali audit qilinadi va xatolar modelda tuzatiladi."
            ),
            "options": [
                (
                    "A",
                    "Element → Classification → Properties → Schedule → audit",
                    True,
                ),
                (
                    "B",
                    "Element chizish → Classification bermaslik → jadvalni tekshirmaslik",
                    False,
                ),
            ],
        },
    ],
}


# ============================================================
# DATABASE SEED
# ============================================================

def seed_level07_module07():
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
        ) in LEVEL07_MODULE07_LESSONS:

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
