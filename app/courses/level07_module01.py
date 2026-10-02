from database.database import get_connection


# ============================================================
# LEVEL 7
# MODULE 01 - FAVORITES
# ============================================================

LEVEL07_MODULE01_LESSONS = [
    (
        "L07_M01",
        "L07_M01_001",
        "Favorites tushunchasi",
        "theory",
        "Archicadda tez-tez ishlatiladigan element sozlamalarini qayta ishlatish mantig'ini tushunish.",
        1,
        30,
        20,
    ),
    (
        "L07_M01",
        "L07_M01_002",
        "Favorite yaratish va qo'llash",
        "practice",
        "Standart element sozlamalaridan Favorite yaratish va uni yangi elementlarda qo'llash.",
        2,
        35,
        20,
    ),
    (
        "L07_M01",
        "L07_M01_003",
        "Professional Favorite kutubxonasi",
        "practice",
        "Devor, slab, roof, door va boshqa elementlar uchun tartibli Favorite tizimini tashkil qilish.",
        3,
        35,
        20,
    ),
    (
        "L07_M01",
        "L07_M01_004",
        "Favorites va standartlashtirish",
        "practice",
        "Loyiha bo'ylab bir xil element sozlamalarini saqlash va takroriy xatolarni kamaytirish.",
        4,
        40,
        20,
    ),
    (
        "L07_M01",
        "L07_M01_005",
        "Favorites professional audit",
        "practice",
        "Favorite nomlari, vazifalari, parametrlar va loyiha workflowidagi tartibini kompleks tekshirish.",
        5,
        40,
        25,
    ),
]


# ============================================================
# CONTENT
# ============================================================

LEVEL07_MODULE01_CONTENT = {
    "L07_M01_001": [
        {
            "title": "Favorite nima?",
            "type": "highlight",
            "text": """
            Favorite —
            oldindan sozlangan
            element parametrlarini

            <br><br>

            keyinchalik tez
            qayta ishlatishga
            yordam beradigan vosita.
            """,
        },
        {
            "title": "Nima uchun kerak?",
            "type": "normal",
            "text": """
            Tasavvur qiling:

            <br><br>

            har safar yangi devor
            chizayotganingizda

            <br><br>

            uning:

            • structure;<br>
            • thickness;<br>
            • Building Material;<br>
            • Layer;<br>
            • boshqa sozlamalarini

            <br><br>

            boshidan kiritishingiz kerak.

            <br><br>

            Bu vaqt oladi
            va xato xavfini oshiradi.
            """,
        },
        {
            "title": "Favorite — tezlik + tartib",
            "type": "highlight",
            "text": """
            Favorite'ning asosiy foydasi:

            <br><br>

            • tez ishlash;<br>
            • bir xil standartni saqlash;<br>
            • tasodifiy sozlamalarni kamaytirish;<br>
            • takrorlanuvchi elementlarni boshqarish.
            """,
        },
        {
            "title": "Tasavvur qiling",
            "type": "example",
            "text": """
            Loyihada
            20 ta bir xil
            tashqi devor kerak.

            <br><br>

            Birinchi devorni
            to'g'ri sozlaysiz.

            <br><br>

            So'ng shu sozlamani
            Favorite sifatida saqlab,

            <br><br>

            boshqa devorlarda
            bir xil standartni
            tez qo'llaysiz.
            """,
        },
        {
            "title": "Favorite elementning o'zi emas",
            "type": "warning",
            "text": """
            Favorite —
            tayyor chizilgan
            model elementi emas.

            <br><br>

            U element sozlamalarini
            qayta ishlatish uchun
            saqlangan konfiguratsiya.
            """,
        },
        {
            "title": "Qayerda foydali?",
            "type": "normal",
            "text": """
            Favorites
            turli elementlarda
            workflowga yordam beradi.

            <br><br>

            Masalan:

            • Walls;<br>
            • Slabs;<br>
            • Roofs;<br>
            • Columns;<br>
            • Beams;<br>
            • Doors;<br>
            • Windows;<br>
            • Objects.

            <br><br>

            Aniq imkoniyatlar
            element turi va
            Archicad versiyasiga
            qarab farqlanishi mumkin.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Bitta Wall elementini
            kerakli sozlamalar bilan
            tayyorlang.

            <br><br>

            Keyin o'zingizga savol bering:

            <br><br>

            “Men shu devorni
            yana 30 marta ishlatsam,
            har safar qo'lda
            qayta sozlashim kerakmi?”

            <br><br>

            Favorites mantig'i
            aynan shu yerda boshlanadi.
            """,
        },
    ],

    "L07_M01_002": [
        {
            "title": "Favorite yaratish",
            "type": "highlight",
            "text": """
            Professional workflow:

            <br><br>

            1. elementni to'g'ri sozlash;<br>
            2. natijani tekshirish;<br>
            3. Favorite sifatida saqlash;<br>
            4. keyin qayta ishlatish.
            """,
        },
        {
            "title": "Avval sozlama to'g'ri bo'lsin",
            "type": "warning",
            "text": """
            Xato sozlangan elementni
            Favorite sifatida saqlasangiz,

            <br><br>

            shu xatoni
            tezroq ko'paytirasiz.

            <br><br>

            Shuning uchun
            Favorite yaratishdan oldin
            elementni audit qiling.
            """,
        },
        {
            "title": "Wall misoli",
            "type": "example",
            "text": """
            Masalan,
            tashqi devor uchun:

            <br><br>

            • kerakli structure;<br>
            • to'g'ri layer;<br>
            • to'g'ri material;<br>
            • to'g'ri geometry

            <br><br>

            tayyor bo'lgach
            uni Favorite sifatida
            saqlash mumkin.
            """,
        },
        {
            "title": "Favorite qo'llash",
            "type": "normal",
            "text": """
            Favorite tanlanganda
            saqlangan sozlamalar

            <br><br>

            mos yangi elementga
            qo'llanishi mumkin.

            <br><br>

            Bu qo'lda
            ko'p parametr kiritishni
            kamaytiradi.
            """,
        },
        {
            "title": "Qo'llagandan keyin ham tekshiring",
            "type": "highlight",
            "text": """
            Favorite ishlatildi
            degani element
            avtomatik ravishda

            <br><br>

            aynan shu joy uchun
            to'g'ri degani emas.

            <br><br>

            Kontekstni baribir
            tekshirish kerak.
            """,
        },
        {
            "title": "Tasavvur qiling",
            "type": "example",
            "text": """
            Bedroom Door Favorite
            mavjud.

            <br><br>

            Lekin yangi joyda
            ochilish yo'nalishi
            boshqacha bo'lishi kerak.

            <br><br>

            Favorite boshlang'ich
            standartni beradi,

            <br><br>

            loyiha konteksti esa
            keyingi qarorni belgilaydi.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            3 ta Favorite yarating:

            <br><br>

            1. Exterior Wall;<br>
            2. Interior Wall;<br>
            3. Standard Slab.

            <br><br>

            Har birini
            yangi elementda qo'llang

            <br><br>

            va sozlamalar
            saqlanganini tekshiring.
            """,
        },
    ],

    "L07_M01_003": [
        {
            "title": "Favorite kutubxonasi",
            "type": "highlight",
            "text": """
            Favorites soni oshganda
            ularni shunchaki
            yig'ib borish yetarli emas.

            <br><br>

            Tartibli naming
            va struktura kerak.
            """,
        },
        {
            "title": "Yomon naming",
            "type": "warning",
            "text": """
            Masalan:

            <br><br>

            Wall 1<br>
            Wall 2<br>
            New Wall<br>
            Good Wall<br>
            Final Wall

            <br><br>

            kabi nomlar
            professional kutubxona
            uchun tushunarsiz.
            """,
        },
        {
            "title": "Tushunarli naming",
            "type": "example",
            "text": """
            Masalan:

            <br><br>

            WALL_EXT_STANDARD<br>
            WALL_INT_STANDARD<br>
            SLAB_GROUND_STANDARD<br>
            ROOF_MAIN_STANDARD

            <br><br>

            kabi izchil naming
            element vazifasini
            tez tushunishga yordam beradi.

            <br><br>

            Bu nomlar
            universal standart emas —
            muhim jihat izchillik.
            """,
        },
        {
            "title": "Element turi bo'yicha tartib",
            "type": "normal",
            "text": """
            Kutubxonani
            element turi bo'yicha
            mantiqan tashkil qilish mumkin.

            <br><br>

            Masalan:

            • Walls;<br>
            • Slabs;<br>
            • Roofs;<br>
            • Doors;<br>
            • Windows;<br>
            • Objects.
            """,
        },
        {
            "title": "Faqat kerakli Favorite",
            "type": "warning",
            "text": """
            Har bir kichik variantni
            Favorite sifatida
            saqlash shart emas.

            <br><br>

            Juda ko'p
            o'xshash Favorite

            <br><br>

            tanlashni qiyinlashtiradi
            va kutubxonani
            chalkashtiradi.
            """,
        },
        {
            "title": "Standard va project-specific",
            "type": "normal",
            "text": """
            Ayrim Favorites
            ko'p loyihada
            qayta ishlatiladigan
            standart bo'lishi mumkin.

            <br><br>

            Ayrimlari esa
            faqat bitta loyiha
            uchun kerak bo'lishi mumkin.

            <br><br>

            Bu farqni
            naming va struktura
            bilan ajratish foydali.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            10 ta Favorite uchun
            naming tizimi tuzing.

            <br><br>

            Kamida:

            • 3 Wall;<br>
            • 2 Slab;<br>
            • 2 Door;<br>
            • 2 Window;<br>
            • 1 Roof

            <br><br>

            bo'lsin.

            <br><br>

            Nomiga qarab
            uning vazifasi
            tushunilishi kerak.
            """,
        },
    ],

    "L07_M01_004": [
        {
            "title": "Standartlashtirish",
            "type": "highlight",
            "text": """
            Favorites —
            shunchaki tezlik vositasi emas.

            <br><br>

            U loyiha ichida
            standart elementlardan
            foydalanishga yordam beradi.
            """,
        },
        {
            "title": "Bir xil devor — bir xil sozlama",
            "type": "example",
            "text": """
            Agar loyihada
            bir xil turdagi
            tashqi devorlar mavjud bo'lsa,

            <br><br>

            ularning parametrlarini
            tasodifiy farqlantirish
            kerak emas.

            <br><br>

            Favorite
            bir xil bazaviy
            sozlamani saqlashga
            yordam beradi.
            """,
        },
        {
            "title": "Xatolar kamayadi",
            "type": "normal",
            "text": """
            Qo'lda qayta-qayta
            sozlash jarayonida:

            <br><br>

            • noto'g'ri Layer;<br>
            • noto'g'ri Material;<br>
            • noto'g'ri thickness;<br>
            • noto'g'ri parameter

            <br><br>

            tanlanishi mumkin.

            <br><br>

            To'g'ri Favorite
            bu riskni kamaytiradi.
            """,
        },
        {
            "title": "Lekin audit baribir kerak",
            "type": "warning",
            "text": """
            Favorite —
            sifat nazoratini
            almashtirmaydi.

            <br><br>

            Favorite'dagi
            eski yoki noto'g'ri
            parametr

            <br><br>

            butun loyihaga
            tarqalishi mumkin.
            """,
        },
        {
            "title": "Team workflow",
            "type": "normal",
            "text": """
            Bir nechta odam
            bitta loyiha standartlari
            bilan ishlaganda,

            <br><br>

            umumiy tushunarli
            Favorite tizimi

            <br><br>

            element sozlamalaridagi
            tasodifiy farqlarni
            kamaytirishga yordam beradi.
            """,
        },
        {
            "title": "Favorite va Template",
            "type": "highlight",
            "text": """
            Professional workflowda
            Favorites

            <br><br>

            keyinchalik
            Template tizimining
            muhim qismlaridan biri
            bo'lishi mumkin.

            <br><br>

            LEVEL 7 oxirida
            Professional Template
            mavzusiga qaytamiz.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Kichik uy loyihasidagi
            barcha tashqi devorlarni
            tekshiring.

            <br><br>

            Savol:

            <br><br>

            bir xil vazifadagi devorlar
            bir xil standart
            sozlamaga egami?

            <br><br>

            Agar yo'q bo'lsa,
            bitta to'g'ri Favorite
            standartini tayyorlang.
            """,
        },
    ],

    "L07_M01_005": [
        {
            "title": "Favorites professional audit",
            "type": "highlight",
            "text": """
            Endi Favorites'ni
            faqat tez ishlash vositasi
            sifatida emas,

            <br><br>

            loyiha standartlari
            tizimi sifatida tekshiramiz.
            """,
        },
        {
            "title": "1. Naming",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • Favorite nomi tushunarlimi?<br>
            • vazifasi nomidan bilinadimi?<br>
            • Copy, Test, Final kabi nomlar qolmaganmi?
            """,
        },
        {
            "title": "2. Parametrlar",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • element turi to'g'rimi?<br>
            • Layer to'g'rimi?<br>
            • material/structure mantiqiymi?<br>
            • kerakli bazaviy parametrlar saqlanganmi?
            """,
        },
        {
            "title": "3. Dublikatlar",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • bir xil vazifali Favorite bir necha marta yaratilmaganmi?<br>
            • eski variantlar qolmaganmi?<br>
            • foydasiz elementlar o'chirilishi kerakmi?
            """,
        },
        {
            "title": "4. Loyiha standarti",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • bir xil vazifadagi elementlar bir xil bazaviy Favorite'dan chiqyaptimi?<br>
            • tasodifiy parametr farqlari kamayganmi?
            """,
        },
        {
            "title": "5. Kontekst",
            "type": "normal",
            "text": """
            Favorite qo'llangandan keyin
            ham tekshiring:

            <br><br>

            • aynan shu joy uchun mosmi?<br>
            • yo'nalish to'g'rimi?<br>
            • geometriya to'g'rimi?<br>
            • boshqa elementlar bilan konflikt yo'qmi?
            """,
        },
        {
            "title": "Xatoni toping",
            "type": "warning",
            "text": """
            Loyiha jamoasida
            25 ta Wall Favorite bor.

            <br><br>

            Lekin:

            • 8 tasi bir-birining nusxasi;<br>
            • nomlari Wall1, Wall2, FinalWall;<br>
            • ayrimlarida eski Layer;<br>
            • ayrimlarida noto'g'ri material;<br>
            • qaysi biri standart ekanini hech kim bilmaydi.

            <br><br>

            Favorites mavjud,
            lekin tizim mavjud emas.
            """,
        },
        {
            "title": "Professional checklist",
            "type": "example",
            "text": """
            Favorites kutubxonasini tekshiring:

            <br><br>

            <b>1.</b> Naming izchilmi?<br><br>
            <b>2.</b> Parametrlar to'g'rimi?<br><br>
            <b>3.</b> Keraksiz dublikatlar yo'qmi?<br><br>
            <b>4.</b> Standart va project-specific Favorites ajratilganmi?<br><br>
            <b>5.</b> Elementlarda qo'llangandan keyin audit qilinadimi?<br><br>
            <b>6.</b> Jamoa qaysi Favorite'ni ishlatishni tushunadimi?
            """,
        },
        {
            "title": "Modul yakuni",
            "type": "highlight",
            "text": """
            Siz endi:

            <br><br>

            ✓ Favorites mantig'ini tushunasiz;<br>
            ✓ Favorite yaratish va qo'llashni bilasiz;<br>
            ✓ professional naming tuzasiz;<br>
            ✓ Favorite kutubxonasini tartibga solasiz;<br>
            ✓ loyiha standartlarini izchil boshqarasiz;<br>
            ✓ Favorites auditini bajarasiz.

            <br><br>

            Keyingi modul:
            <b>Graphic Overrides.</b>
            """,
        },
    ],
}


# ============================================================
# QUIZ
# Q001-Q015
# ============================================================

LEVEL07_MODULE01_QUIZ = {
    "L07_M01_001": [
        {
            "code": "L07_Q001",
            "question": "Favorite oldindan sozlangan element parametrlarini qayta ishlatishga yordam beradimi?",
            "explanation": (
                "Favorites tez-tez ishlatiladigan element sozlamalarini saqlab, qayta qo'llashga yordam beradi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L07_Q002",
            "question": "Favorite tayyor chizilgan model elementi bilan aynan bir xilmi?",
            "explanation": (
                "Favorite elementning o'zi emas, uning qayta ishlatiladigan sozlamalar konfiguratsiyasidir."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L07_Q003",
            "question": "Favorites takroriy element sozlamalaridagi tasodifiy farqlarni kamaytirishga yordam berishi mumkinmi?",
            "explanation": (
                "Bir xil Favorite'dan foydalanish standart bazaviy parametrlarni saqlashga yordam beradi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L07_M01_002": [
        {
            "code": "L07_Q004",
            "question": "Favorite yaratishdan oldin element sozlamalarini tekshirish kerakmi?",
            "explanation": (
                "Xato sozlamani Favorite sifatida saqlash xatoni ko'p elementga tarqatishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L07_Q005",
            "question": "Favorite qo'llangandan keyin loyiha kontekstini tekshirish kerak emasmi?",
            "explanation": (
                "Favorite bazaviy sozlamani beradi, lekin elementning aniq joydagi geometriya va vazifasi baribir tekshiriladi."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L07_Q006",
            "question": "Favorites ko'p parametrni har safar qo'lda qayta kiritishni kamaytirishi mumkinmi?",
            "explanation": (
                "Favorite oldindan sozlangan parametrlarni qayta ishlatish orqali takroriy qo'lda sozlashni kamaytiradi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L07_M01_003": [
        {
            "code": "L07_Q007",
            "question": "Favorite nomlari izchil va tushunarli bo'lishi kerakmi?",
            "explanation": (
                "Professional naming kutubxonada kerakli Favorite'ni tez topish va tushunishga yordam beradi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L07_Q008",
            "question": "Wall 1, Wall 2, Final Wall kabi nomlar katta Favorite kutubxonasi uchun qulaymi?",
            "explanation": (
                "Bunday nomlar element vazifasini aniq ko'rsatmaydi va kutubxonani chalkashtiradi."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L07_Q009",
            "question": "Har bir kichik parametr farqi uchun alohida Favorite yaratish har doim kerakmi?",
            "explanation": (
                "Keraksiz ko'p Favorite dublikatlar va boshqaruv muammosini keltirib chiqarishi mumkin."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
    ],

    "L07_M01_004": [
        {
            "code": "L07_Q010",
            "question": "Favorites loyiha standartlashtirishiga yordam berishi mumkinmi?",
            "explanation": (
                "Favorites takroriy elementlarda bir xil bazaviy sozlamalardan foydalanishga yordam beradi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L07_Q011",
            "question": "Favorite ishlatilsa sifat auditi umuman kerak bo'lmaydimi?",
            "explanation": (
                "Favorite ham xato yoki eskirgan parametrga ega bo'lishi mumkin, shuning uchun audit saqlanadi."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L07_Q012",
            "question": "Tartibli Favorite tizimi jamoaviy workflowda tasodifiy parametr farqlarini kamaytirishi mumkinmi?",
            "explanation": (
                "Umumiy standart Favorites jamoa a'zolarining bir xil bazaviy sozlamalardan foydalanishiga yordam beradi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L07_M01_005": [
        {
            "code": "L07_Q013",
            "question": "Favorites auditida naming va parametrlar tekshiriladimi?",
            "explanation": (
                "Professional auditda Favorite nomi, vazifasi va saqlangan sozlamalari tekshiriladi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L07_Q014",
            "question": "Bir xil vazifali ko'plab dublikat Favorites kutubxonani boshqarishni qiyinlashtirishi mumkinmi?",
            "explanation": (
                "Dublikatlar qaysi Favorite standart ekanini aniqlashni qiyinlashtiradi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L07_Q015",
            "question": "Favorites bilan professional ishlashdagi to'g'ri workflow qaysi?",
            "explanation": (
                "Element avval to'g'ri sozlanadi va tekshiriladi, keyin Favorite sifatida tartibli saqlanib, qo'llangandan keyin ham audit qilinadi."
            ),
            "options": [
                (
                    "A",
                    "Elementni sozlash → tekshirish → Favorite yaratish → tartibli naming → qo'llash → audit",
                    True,
                ),
                (
                    "B",
                    "Tasodifiy elementdan Favorite yaratib hamma joyda tekshirmasdan ishlatish",
                    False,
                ),
            ],
        },
    ],
}


# ============================================================
# DATABASE SEED
# ============================================================

def seed_level07_module01():
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
        ) in LEVEL07_MODULE01_LESSONS:

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
