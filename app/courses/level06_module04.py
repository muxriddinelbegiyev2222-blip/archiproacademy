from database.database import get_connection


# ============================================================
# LEVEL 6
# MODULE 04 - COMPOSITE STRUCTURES
# ============================================================

LEVEL06_MODULE04_LESSONS = [
    (
        "L06_M04",
        "L06_M04_001",
        "Composite Structure tushunchasi",
        "theory",
        "Bir nechta material qatlamidan tashkil topgan BIM konstruksiyani tushunish.",
        1,
        50,
        20,
    ),
    (
        "L06_M04",
        "L06_M04_002",
        "Skin va Building Material",
        "theory",
        "Composite tarkibidagi qatlamlar va ularning Building Material bilan aloqasini tushunish.",
        2,
        55,
        20,
    ),
    (
        "L06_M04",
        "L06_M04_003",
        "Qatlam qalinligi va tartibi",
        "practice",
        "Composite qatlamlarini to'g'ri ketma-ketlik va qalinlikda tashkil qilish.",
        3,
        60,
        20,
    ),
    (
        "L06_M04",
        "L06_M04_004",
        "Composite elementlar bilan ishlash",
        "practice",
        "Composite strukturani devor, slab va boshqa mos konstruktiv elementlarda qo'llash mantig'ini tushunish.",
        4,
        65,
        20,
    ),
    (
        "L06_M04",
        "L06_M04_005",
        "Composite professional audit",
        "practice",
        "Composite nomlari, qatlamlar, materiallar, qalinlik va kesim natijasini kompleks tekshirish.",
        5,
        70,
        25,
    ),
]


# ============================================================
# CONTENT
# ============================================================

LEVEL06_MODULE04_CONTENT = {
    "L06_M04_001": [
        {
            "title": "Composite Structure nima?",
            "type": "highlight",
            "text": """
            Composite Structure —
            bir nechta material qatlamini
            bitta BIM konstruksiya
            sifatida boshqarish usuli.

            <br><br>

            Masalan devorda:

            <br><br>

            • tashqi finish;<br>
            • asosiy konstruktiv qatlam;<br>
            • issiqlik izolyatsiyasi;<br>
            • ichki finish

            <br><br>

            birgalikda ishlashi mumkin.
            """,
        },
        {
            "title": "Oddiy devor va Composite farqi",
            "type": "normal",
            "text": """
            Oddiy element
            bitta material bilan
            ifodalanishi mumkin.

            <br><br>

            Composite esa
            bir nechta qatlamni

            <br><br>

            bitta konstruksiya sifatida
            boshqarishga yordam beradi.
            """,
        },
        {
            "title": "Nega kerak?",
            "type": "highlight",
            "text": """
            Real bino konstruksiyasi
            ko'pincha bitta materialdan
            iborat bo'lmaydi.

            <br><br>

            Composite orqali
            shu qatlamli struktura
            BIM modelda ham
            aniqroq ifodalanadi.
            """,
        },
        {
            "title": "Tasavvur qiling",
            "type": "example",
            "text": """
            Tashqi devor:

            <br><br>

            g'isht +
            izolyatsiya +
            tashqi qoplama +
            ichki pardoz

            <br><br>

            dan tashkil topgan.

            <br><br>

            Agar bularning hammasi
            faqat bitta oddiy material
            sifatida ko'rsatilsa,

            <br><br>

            BIM ma'lumotining
            bir qismi yo'qoladi.
            """,
        },
        {
            "title": "Composite — dekor emas",
            "type": "warning",
            "text": """
            Composite Structure
            faqat Sectionni
            chiroyli ko'rsatish uchun
            ishlatilmaydi.

            <br><br>

            Uning asosida
            konstruktiv qatlamlar
            mantig'i turadi.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Bitta tashqi devorni
            real qatlamlarga ajrating.

            <br><br>

            Masalan:

            1. tashqi finish<br>
            2. asosiy material<br>
            3. insulation<br>
            4. ichki finish

            <br><br>

            Har bir qatlam
            nima vazifa bajarishini yozing.
            """,
        },
    ],

    "L06_M04_002": [
        {
            "title": "Skin nima?",
            "type": "highlight",
            "text": """
            Composite tarkibidagi
            har bir alohida qatlamni

            <br><br>

            skin sifatida
            tasavvur qilish mumkin.
            """,
        },
        {
            "title": "Har bir Skinning materiali",
            "type": "normal",
            "text": """
            Har bir skin
            tegishli Building Material
            bilan bog'lanadi.

            <br><br>

            Masalan:

            <br><br>

            • brick skin → Brick;<br>
            • insulation skin → Insulation;<br>
            • concrete skin → Concrete.
            """,
        },
        {
            "title": "Building Material muhim",
            "type": "highlight",
            "text": """
            Oldingi moduldagi
            Building Materials

            <br><br>

            Composite ichida
            amalda ishlay boshlaydi.

            <br><br>

            Shuning uchun noto'g'ri
            Building Material tanlovi
            composite natijasiga ham
            ta'sir qiladi.
            """,
        },
        {
            "title": "Qatlam vazifasi",
            "type": "normal",
            "text": """
            Composite ichidagi
            qatlamlar bir xil rol
            bajarmaydi.

            <br><br>

            Ular:

            <br><br>

            • konstruktiv;<br>
            • izolyatsion;<br>
            • finish

            <br><br>

            vazifalarida bo'lishi mumkin.
            """,
        },
        {
            "title": "Tasavvur qiling",
            "type": "example",
            "text": """
            Tashqi finish
            tasodifan asosiy
            konstruktiv qatlam sifatida
            tashkil qilindi.

            <br><br>

            Section grafikasi
            va element tutashuvlarida
            kutilmagan natijalar
            paydo bo'lishi mumkin.
            """,
        },
        {
            "title": "Nomga aldanmang",
            "type": "warning",
            "text": """
            Qatlam nomi
            “Concrete” bo'lishi

            <br><br>

            uning Building Materiali
            ham beton ekanini
            avtomatik anglatmaydi.

            <br><br>

            Sozlamani real tekshiring.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Bitta composite uchun
            4 ta skin yarating.

            <br><br>

            Har biriga:

            • vazifa;<br>
            • Building Material;<br>
            • tartib

            <br><br>

            belgilang.
            """,
        },
    ],

    "L06_M04_003": [
        {
            "title": "Qatlam qalinligi",
            "type": "highlight",
            "text": """
            Composite Structureda
            har bir qatlamning
            o'z qalinligi mavjud.

            <br><br>

            Umumiy element qalinligi
            shu qatlamlar yig'indisidan
            hosil bo'ladi.
            """,
        },
        {
            "title": "Real konstruksiyani ifodalang",
            "type": "normal",
            "text": """
            Qatlam qalinliklarini
            faqat grafik ko'rinish uchun
            tasodifiy tanlamang.

            <br><br>

            Composite real loyiha
            mantig'iga mos bo'lishi kerak.
            """,
        },
        {
            "title": "Qatlam tartibi",
            "type": "highlight",
            "text": """
            Faqat qalinlik emas,
            qatlamlarning ketma-ketligi ham
            muhim.

            <br><br>

            Tashqi va ichki tomonlarni
            aralashtirib yubormang.
            """,
        },
        {
            "title": "Reference Side",
            "type": "normal",
            "text": """
            Composite element bilan
            ishlaganda elementning
            reference tomoni

            <br><br>

            qatlamlar qaysi yo'nalishda
            joylashishini tushunishda
            muhim bo'lishi mumkin.
            """,
        },
        {
            "title": "Tasavvur qiling",
            "type": "example",
            "text": """
            Tashqi devor
            teskari yo'nalishda chizildi.

            <br><br>

            Natijada insulation
            ichki tomonga,

            <br><br>

            interior finish esa
            tashqi tomonga chiqib qoldi.

            <br><br>

            Composite to'g'ri,
            lekin element yo'nalishi noto'g'ri.
            """,
        },
        {
            "title": "Section bilan nazorat",
            "type": "highlight",
            "text": """
            Composite yaratgandan keyin
            Section oching.

            <br><br>

            Qatlamlarning:

            <br><br>

            • tartibi;<br>
            • qalinligi;<br>
            • material grafikasi

            <br><br>

            to'g'ri ekanini tekshiring.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Ikki xil composite yarating:

            <br><br>

            1. Exterior Wall<br>
            2. Interior Wall

            <br><br>

            Ularning skin soni,
            materiali va qalinligi
            qanday farq qilishini
            tahlil qiling.
            """,
        },
    ],

    "L06_M04_004": [
        {
            "title": "Composite elementda ishlaydi",
            "type": "highlight",
            "text": """
            Composite Structure
            model elementining
            fizik qatlamli strukturasi
            sifatida ishlatiladi.

            <br><br>

            Uning natijasini
            plan,
            section
            va 3Dda ko'rish mumkin.
            """,
        },
        {
            "title": "Composite Wall",
            "type": "normal",
            "text": """
            Tashqi yoki ichki devorda
            bir nechta real qatlam mavjud bo'lsa,

            <br><br>

            Composite Wall
            shu strukturani
            tartibli boshqarishga yordam beradi.
            """,
        },
        {
            "title": "Composite Slab",
            "type": "normal",
            "text": """
            Pol yoki yopma
            ham bir nechta qatlamdan
            tashkil topishi mumkin.

            <br><br>

            Masalan:

            konstruktiv qatlam +
            screed +
            finish.

            <br><br>

            Bunday holatda
            qatlamli struktura
            BIM modelda ham muhim.
            """,
        },
        {
            "title": "Bitta Composite hamma joyga mos emas",
            "type": "warning",
            "text": """
            Bitta exterior wall
            Composite'ini

            <br><br>

            barcha devor,
            slab
            va boshqa elementlarga
            berish yaxshi workflow emas.

            <br><br>

            Har konstruksiyaning
            real tarkibini tekshiring.
            """,
        },
        {
            "title": "Tutashuvlarni tekshiring",
            "type": "highlight",
            "text": """
            Composite elementlar
            bir-biriga tutashganda

            <br><br>

            Building Material priority
            va skin strukturasi
            natijaga ta'sir qilishi mumkin.
            """,
        },
        {
            "title": "Corner misoli",
            "type": "example",
            "text": """
            Ikki tashqi devor
            burchakda tutashdi.

            <br><br>

            Section yoki Plan'da
            qatlamlar noto'g'ri
            kesishayotgan bo'lsa,

            <br><br>

            faqat devorni siljitish
            bilan cheklanib qolmang.

            <br><br>

            Composite va
            Building Materiallarni
            ham tekshiring.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Kichik xona yarating.

            <br><br>

            Tashqi devorlarga
            Exterior Composite,

            <br><br>

            ichki devorga
            Interior Composite bering.

            <br><br>

            Keyin Plan va Sectionda
            tutashuvlarni tekshiring.
            """,
        },
    ],

    "L06_M04_005": [
        {
            "title": "Composite audit",
            "type": "highlight",
            "text": """
            Endi Composite Structuresni
            oddiy tayyor preset sifatida emas,

            <br><br>

            professional BIM konstruksiya
            sifatida tekshiramiz.
            """,
        },
        {
            "title": "1. Naming",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • nom tushunarlimi?<br>
            • qaysi konstruksiya uchun ekanligi bilinadimi?<br>
            • Test yoki Copy kabi nomlar qolmaganmi?
            """,
        },
        {
            "title": "2. Skinlar",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • barcha kerakli qatlamlar bormi?<br>
            • ortiqcha qatlam yo'qmi?<br>
            • tartib tashqi-ichki tomonga mosmi?
            """,
        },
        {
            "title": "3. Building Materials",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • har skin to'g'ri materialdami?<br>
            • material priority mantiqiymi?<br>
            • section grafikasi tushunarlimi?
            """,
        },
        {
            "title": "4. Qalinlik",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • skin qalinliklari mantiqiymi?<br>
            • umumiy qalinlik kutilgan natijani beryaptimi?<br>
            • tasodifiy sonlar qolmaganmi?
            """,
        },
        {
            "title": "5. Element yo'nalishi",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • exterior va interior tomonlar to'g'rimi?<br>
            • teskari chizilgan elementlar yo'qmi?<br>
            • reference side mantiqiy ishlayaptimi?
            """,
        },
        {
            "title": "Xatoni toping",
            "type": "warning",
            "text": """
            Tashqi devor
            4 qatlamli Composite.

            <br><br>

            Lekin:

            <br><br>

            • insulation ichki tomonda;<br>
            • brick skinga noto'g'ri material berilgan;<br>
            • finish qatlam juda qalin;<br>
            • burchak tutashuvi buzilgan.

            <br><br>

            Composite mavjud,
            lekin BIM konstruksiya
            professional tashkil qilinmagan.
            """,
        },
        {
            "title": "Professional checklist",
            "type": "example",
            "text": """
            Composite'ni tekshiring:

            <br><br>

            <b>1.</b> Naming tushunarlimi?<br><br>
            <b>2.</b> Skinlar to'g'ri tartibdami?<br><br>
            <b>3.</b> Building Materials to'g'rimi?<br><br>
            <b>4.</b> Qalinliklar mantiqiymi?<br><br>
            <b>5.</b> Exterior/interior yo'nalish to'g'rimi?<br><br>
            <b>6.</b> Plan va Section grafikasi to'g'rimi?<br><br>
            <b>7.</b> Tutashuvlar yaxshi ishlayaptimi?
            """,
        },
        {
            "title": "Modul yakuni",
            "type": "highlight",
            "text": """
            Siz endi:

            <br><br>

            ✓ Composite Structure tushunchasini bilasiz;<br>
            ✓ skinlarni boshqarasiz;<br>
            ✓ Building Materiallarni biriktirasiz;<br>
            ✓ qatlam qalinligini tushunasiz;<br>
            ✓ qatlam tartibini boshqarasiz;<br>
            ✓ element tutashuvini tekshirasiz;<br>
            ✓ Composite auditini bajarasiz.

            <br><br>

            Keyingi modul:
            <b>Complex Profiles.</b>
            """,
        },
    ],
}


# ============================================================
# QUIZ
# Q046-Q060
# ============================================================

LEVEL06_MODULE04_QUIZ = {
    "L06_M04_001": [
        {
            "code": "L06_Q046",
            "question": "Composite Structure bir nechta material qatlamini bitta konstruksiya sifatida boshqarishga yordam beradimi?",
            "explanation": (
                "Composite ko'p qatlamli konstruksiyani BIM modelda bir struktura sifatida ifodalashga yordam beradi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L06_Q047",
            "question": "Composite faqat chiroyli Section grafikasi uchun ishlatiladimi?",
            "explanation": (
                "Composite real qatlamli konstruksiya va BIM material strukturasini ham ifodalaydi."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L06_Q048",
            "question": "Real tashqi devor bir nechta material qatlamidan iborat bo'lishi mumkinmi?",
            "explanation": (
                "Tashqi devorda konstruktiv material, izolyatsiya va finish qatlamlari bo'lishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L06_M04_002": [
        {
            "code": "L06_Q049",
            "question": "Composite ichidagi har bir qatlam alohida Building Material bilan bog'lanishi mumkinmi?",
            "explanation": (
                "Har bir skin o'z material xususiyatiga ega bo'lishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L06_Q050",
            "question": "Skinning nomi to'g'ri bo'lsa uning Building Materialini tekshirmasa ham bo'ladimi?",
            "explanation": (
                "Nom va real Building Material sozlamasi bir-biridan alohida tekshiriladi."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L06_Q051",
            "question": "Building Materials Composite Structures uchun muhimmi?",
            "explanation": (
                "Composite skinlarining material xususiyatlari Building Materials orqali boshqariladi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L06_M04_003": [
        {
            "code": "L06_Q052",
            "question": "Composite qatlamlarining qalinligi umumiy konstruksiya qalinligiga ta'sir qiladimi?",
            "explanation": (
                "Skin qalinliklari birgalikda umumiy element strukturasini tashkil qiladi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L06_Q053",
            "question": "Composite'da tashqi va ichki qatlam tartibini tekshirish kerakmi?",
            "explanation": (
                "Qatlam yo'nalishi real konstruksiya mantig'iga mos bo'lishi kerak."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L06_Q054",
            "question": "Composite yaratgandan keyin Sectionda tekshirish foydalimi?",
            "explanation": (
                "Sectionda qatlam tartibi, qalinlik va material grafikasi aniqroq ko'rinadi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L06_M04_004": [
        {
            "code": "L06_Q055",
            "question": "Bitta Composite barcha konstruksiyalar uchun avtomatik mos keladimi?",
            "explanation": (
                "Turli konstruksiyalar turli qatlam va material tarkibiga ega bo'lishi mumkin."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L06_Q056",
            "question": "Composite devorlar tutashganda Building Material priority natijaga ta'sir qilishi mumkinmi?",
            "explanation": (
                "Material priority element tutashuvi va kesim grafikasiga ta'sir qilishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L06_Q057",
            "question": "Composite elementlarni Plan va Sectionda tekshirish kerakmi?",
            "explanation": (
                "Turli ko'rinishlarda qatlamlar va tutashuvlar nazorat qilinadi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L06_M04_005": [
        {
            "code": "L06_Q058",
            "question": "Composite auditida skinlar va Building Materials tekshiriladimi?",
            "explanation": (
                "Qatlamlar va ularning materiallari Composite sifatining asosiy qismlaridir."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L06_Q059",
            "question": "Composite mavjud bo'lsa uning orientation va qatlam tartibini tekshirmasa ham bo'ladimi?",
            "explanation": (
                "Element teskari yo'nalgan bo'lsa tashqi va ichki qatlamlar noto'g'ri joylashishi mumkin."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L06_Q060",
            "question": "Composite Structures bilan professional ishlashdagi to'g'ri workflow qaysi?",
            "explanation": (
                "Avval qatlamlar va materiallar tuziladi, so'ng qalinlik, yo'nalish va tutashuvlar tekshiriladi."
            ),
            "options": [
                (
                    "A",
                    "Skinlar → materiallar → qalinlik → orientation → audit",
                    True,
                ),
                (
                    "B",
                    "Faqat umumiy devor qalinligini tanlash",
                    False,
                ),
            ],
        },
    ],
}


# ============================================================
# DATABASE SEED
# ============================================================

def seed_level06_module04():
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
        ) in LEVEL06_MODULE04_LESSONS:

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
