from database.database import get_connection


# ============================================================
# LEVEL 6
# MODULE 01 - STORIES
# ============================================================

LEVEL06_MODULE01_LESSONS = [
    (
        "L06_M01",
        "L06_M01_001",
        "Stories tushunchasi",
        "theory",
        "Archicaddagi Story tizimi va qavatlar o'rtasidagi vertikal struktura mantig'ini tushunish.",
        1,
        30,
        20,
    ),
    (
        "L06_M01",
        "L06_M01_002",
        "Story Settings va balandliklar",
        "theory",
        "Qavat nomlari, balandliklari va vertikal joylashuvini boshqarish.",
        2,
        35,
        20,
    ),
    (
        "L06_M01",
        "L06_M01_003",
        "Home Story va elementlar",
        "practice",
        "Elementlarning qaysi qavatga tegishli ekanini tushunish va to'g'ri boshqarish.",
        3,
        35,
        20,
    ),
    (
        "L06_M01",
        "L06_M01_004",
        "Ko'p qavatli model workflow",
        "practice",
        "Bir nechta qavatli modelda elementlar va qavatlar o'rtasidagi aloqani tashkil qilish.",
        4,
        40,
        20,
    ),
    (
        "L06_M01",
        "L06_M01_005",
        "Stories professional audit",
        "practice",
        "Qavat strukturasini nomlash, balandlik, element bog'lanishi va model barqarorligi bo'yicha tekshirish.",
        5,
        40,
        25,
    ),
]


# ============================================================
# CONTENT
# ============================================================

LEVEL06_MODULE01_CONTENT = {
    "L06_M01_001": [
        {
            "title": "Story nima?",
            "type": "highlight",
            "text": """
            Archicadda Story —
            binoning vertikal strukturasini
            tashkil qiluvchi qavat tizimi.

            <br><br>

            Masalan:

            <br><br>

            • Ground Floor;<br>
            • First Floor;<br>
            • Second Floor;<br>
            • Roof Level

            <br><br>

            alohida Story sifatida
            tashkil qilinishi mumkin.
            """,
        },
        {
            "title": "Story oddiy papka emas",
            "type": "normal",
            "text": """
            Story faqat
            chizmalarni ajratish uchun
            ishlatilmaydi.

            <br><br>

            U modeldagi elementlarning
            vertikal joylashuviga ham
            bog'liq.
            """,
        },
        {
            "title": "2D va 3D birga ishlaydi",
            "type": "highlight",
            "text": """
            Siz bir Storyda
            Floor Plan bilan ishlaysiz.

            <br><br>

            Lekin yaratgan elementlaringiz
            3D modelning
            vertikal qismiga aylanadi.
            """,
        },
        {
            "title": "Tasavvur qiling",
            "type": "example",
            "text": """
            Ikki qavatli uy yaratyapsiz.

            <br><br>

            1-qavat devorlari,
            2-qavat devorlari
            va tom elementlari

            <br><br>

            barchasi bitta
            mantiqsiz qavatga joylashtirilsa,

            <br><br>

            modelni boshqarish
            juda qiyinlashadi.
            """,
        },
        {
            "title": "Professional fikrlash",
            "type": "normal",
            "text": """
            Modelni boshlashdan oldin
            vertikal strukturani aniqlang.

            <br><br>

            Savollar:

            <br><br>

            • nechta qavat bor?<br>
            • qavatlar qanday nomlanadi?<br>
            • ularning sathlari qanday bog'langan?<br>
            • roof qaysi darajada?<br>
            • elementlar qaysi Storyga tegishli?
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            2 qavatli oddiy uy uchun
            Story strukturasi yozing.

            <br><br>

            Masalan:

            <br><br>

            Ground Floor<br>
            First Floor<br>
            Roof Level

            <br><br>

            Keyin har bir Storyda
            qanday elementlar bo'lishini yozing.
            """,
        },
    ],

    "L06_M01_002": [
        {
            "title": "Story Settings",
            "type": "highlight",
            "text": """
            Story Settings orqali
            qavatlar strukturasi
            boshqariladi.

            <br><br>

            Bu yerda qavatning:

            <br><br>

            • nomi;<br>
            • vertikal sathi;<br>
            • boshqa qavatlar bilan aloqasi

            <br><br>

            nazorat qilinadi.
            """,
        },
        {
            "title": "Qavat nomlari",
            "type": "normal",
            "text": """
            Qavatlarga tushunarli
            va bir xil tizimdagi
            nomlar bering.

            <br><br>

            Masalan:

            <br><br>

            Ground Floor<br>
            First Floor<br>
            Roof

            <br><br>

            yoki loyiha standartiga
            mos boshqa tizim.
            """,
        },
        {
            "title": "Nomlash tartibi",
            "type": "warning",
            "text": """
            Bir qavatni:

            <br><br>

            Floor 1

            <br><br>

            boshqasini:

            <br><br>

            Ikkinchi etaj

            <br><br>

            uchinchisini:

            <br><br>

            LEVEL_TOP

            <br><br>

            deb tasodifiy nomlash
            professional struktura emas.
            """,
        },
        {
            "title": "Story elevation",
            "type": "highlight",
            "text": """
            Har bir Story
            ma'lum vertikal sathda turadi.

            <br><br>

            Story balandliklarini
            o'zgartirganda

            <br><br>

            unga bog'langan elementlar
            qanday javob berishini
            tushunish juda muhim.
            """,
        },
        {
            "title": "Tasavvur qiling",
            "type": "example",
            "text": """
            Ikkinchi qavat balandligi
            loyiha davomida o'zgardi.

            <br><br>

            Agar model
            Story tizimiga mantiqiy
            bog'langan bo'lsa,

            <br><br>

            o'zgarishni boshqarish
            ancha osonlashadi.
            """,
        },
        {
            "title": "Qavat balandligini tasodifiy o'zgartirmang",
            "type": "warning",
            "text": """
            Story elevationni
            o'zgartirishdan oldin

            <br><br>

            qaysi elementlar
            unga bog'langanini
            tushunib oling.

            <br><br>

            Aks holda modelning
            vertikal strukturasi
            buzilishi mumkin.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Story Settingsni oching.

            <br><br>

            3 ta Story yarating:

            <br><br>

            Ground Floor<br>
            First Floor<br>
            Roof

            <br><br>

            Ularning tartibini
            Navigator orqali tekshiring.
            """,
        },
    ],

    "L06_M01_003": [
        {
            "title": "Home Story nima?",
            "type": "highlight",
            "text": """
            Model elementi
            ma'lum Story bilan
            bog'langan bo'lishi mumkin.

            <br><br>

            Elementning asosiy
            tegishli qavati
            Home Story tushunchasi bilan
            boshqariladi.
            """,
        },
        {
            "title": "Nega muhim?",
            "type": "normal",
            "text": """
            Home Story
            to'g'ri tashkil qilinsa:

            <br><br>

            • model strukturasi tushunarli bo'ladi;<br>
            • elementni topish osonlashadi;<br>
            • qavat o'zgarishlarini boshqarish yaxshilanadi;<br>
            • Floor Plan nazorati soddalashadi.
            """,
        },
        {
            "title": "Devor misoli",
            "type": "example",
            "text": """
            Ground Floorda
            tashqi devor yaratildi.

            <br><br>

            U aslida Ground Floor
            strukturasiga tegishli.

            <br><br>

            Uni sababsiz
            First Floor Home Storyga
            bog'lash modelni
            chalkashtirishi mumkin.
            """,
        },
        {
            "title": "Element qavatdan o'tishi mumkin",
            "type": "normal",
            "text": """
            Elementning Home Storysi
            uning faqat bitta qavat
            balandligida bo'lishi shart
            degani emas.

            <br><br>

            Ba'zi elementlar
            bir nechta qavat balandligini
            egallashi mumkin.

            <br><br>

            Muhim narsa —
            elementning modeldagi
            mantiqiy aloqasini tushunish.
            """,
        },
        {
            "title": "Floor Plan ko'rinishi",
            "type": "highlight",
            "text": """
            Elementning
            qaysi Storylarda
            qanday ko'rinishi

            <br><br>

            Home Storydan tashqari
            uning Floor Plan
            ko'rinish sozlamalariga ham
            bog'liq bo'lishi mumkin.
            """,
        },
        {
            "title": "Tipik xato",
            "type": "warning",
            "text": """
            Foydalanuvchi
            2-qavatda devor yaratmoqchi edi.

            <br><br>

            Lekin Navigator orqali
            Ground Floorda qolgan.

            <br><br>

            Natijada yangi elementlar
            noto'g'ri strukturaga tushdi.

            <br><br>

            Chizishdan oldin
            joriy Storyni tekshiring.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Ground Floorda
            bitta devor yarating.

            <br><br>

            Keyin uning:

            <br><br>

            • Home Storysi;<br>
            • elevationi;<br>
            • 3D joylashuvi

            <br><br>

            o'rtasidagi aloqani kuzating.
            """,
        },
    ],

    "L06_M01_004": [
        {
            "title": "Ko'p qavatli model",
            "type": "highlight",
            "text": """
            Ko'p qavatli loyiha
            oddiy bir qavatli modelning
            nusxalari to'plami emas.

            <br><br>

            Qavatlar o'zaro
            vertikal tizim sifatida
            ishlaydi.
            """,
        },
        {
            "title": "1-qavat va 2-qavat aloqasi",
            "type": "normal",
            "text": """
            Ikki qavatli uyda
            quyidagilarni birga tekshirish kerak:

            <br><br>

            • devorlar;<br>
            • slablar;<br>
            • ustunlar;<br>
            • zinapoya;<br>
            • openinglar;<br>
            • tom.
            """,
        },
        {
            "title": "Copy qilishdan oldin fikrlang",
            "type": "warning",
            "text": """
            1-qavatdagi barcha elementlarni
            shunchaki copy qilib
            2-qavatga qo'yish

            <br><br>

            har doim to'g'ri workflow emas.

            <br><br>

            Har bir qavatning
            funksiyasi va konstruktiv
            mantig'i tekshirilishi kerak.
            """,
        },
        {
            "title": "Vertikal moslashuv",
            "type": "highlight",
            "text": """
            Qavatlar orasida
            vertikal aloqalarni tekshiring.

            <br><br>

            Masalan:

            <br><br>

            • ustunlar bir-biriga mosmi?<br>
            • zinapoya kerakli qavatga chiqadimi?<br>
            • slab opening to'g'rimi?<br>
            • sanuzellar bir-biriga yaqinmi?
            """,
        },
        {
            "title": "3D orqali tekshiring",
            "type": "normal",
            "text": """
            Story bilan ishlaganda
            faqat Floor Planga
            ishonib qolmang.

            <br><br>

            3D modelda:

            <br><br>

            • qavatlar sathi;<br>
            • devorlar balandligi;<br>
            • slablar;<br>
            • vertikal elementlar

            <br><br>

            qanday tutashganini tekshiring.
            """,
        },
        {
            "title": "Section juda foydali",
            "type": "example",
            "text": """
            Qavatlararo muammoni
            ba'zan Plan yoki 3Ddan
            ko'rish qiyin.

            <br><br>

            Section orqali
            Story level va
            element balandliklarini
            aniqroq tahlil qilish mumkin.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            2 qavatli kichik model yarating.

            <br><br>

            Ground Floorda:
            tashqi devorlar.

            <br><br>

            First Floorda:
            boshqa konfiguratsiyadagi devorlar.

            <br><br>

            Keyin 3D va Sectionda
            qavatlar aloqasini tekshiring.
            """,
        },
    ],

    "L06_M01_005": [
        {
            "title": "Stories professional audit",
            "type": "highlight",
            "text": """
            Endi Story tizimini
            alohida qavatlar ro'yxati sifatida emas,

            <br><br>

            butun BIM modelning
            vertikal skeleti sifatida
            tekshiramiz.
            """,
        },
        {
            "title": "1. Story nomlari",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • nomlar tushunarlimi?<br>
            • bir xil naming standard ishlatilganmi?<br>
            • keraksiz Storylar yo'qmi?
            """,
        },
        {
            "title": "2. Story balandliklari",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • qavat sathlari mantiqiymi?<br>
            • tasodifiy elevation yo'qmi?<br>
            • qavatlar o'rtasida kerakli aloqa bormi?
            """,
        },
        {
            "title": "3. Home Story",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • elementlar mantiqiy Storyga tegishlimi?<br>
            • 2-qavat elementlari 1-qavatga tushib qolmaganmi?<br>
            • elementlar Navigator strukturasiga mosmi?
            """,
        },
        {
            "title": "4. 3D va Section",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • devorlar qavatlarga to'g'ri bog'langanmi?<br>
            • slablar kerakli sathdami?<br>
            • vertikal bo'shliqlar yo'qmi?<br>
            • elementlar bir-birini noto'g'ri kesmayaptimi?
            """,
        },
        {
            "title": "Xatoni toping",
            "type": "warning",
            "text": """
            Ikki qavatli uy
            Floor Planda yaxshi ko'rinadi.

            <br><br>

            Lekin Sectionda:

            <br><br>

            • 2-qavat slab noto'g'ri sathda;<br>
            • birinchi qavat devori slabdan o'tib ketgan;<br>
            • 2-qavat devorining Home Storysi Ground Floor.

            <br><br>

            Muammo:

            <br><br>

            qavatlar chizilgan,
            lekin Story tizimi
            professional boshqarilmagan.
            """,
        },
        {
            "title": "Professional checklist",
            "type": "example",
            "text": """
            Stories tizimini tekshiring:

            <br><br>

            <b>1.</b> Story nomlari tartiblimi?<br><br>
            <b>2.</b> Story elevationlar mantiqiymi?<br><br>
            <b>3.</b> Home Storylar to'g'rimi?<br><br>
            <b>4.</b> Qavatlararo elementlar to'g'ri ishlayaptimi?<br><br>
            <b>5.</b> 3D model to'g'rimi?<br><br>
            <b>6.</b> Sectionda vertikal aloqa to'g'rimi?<br><br>
            <b>7.</b> Keraksiz yoki tasodifiy Story yo'qmi?
            """,
        },
        {
            "title": "Modul yakuni",
            "type": "highlight",
            "text": """
            Siz endi:

            <br><br>

            ✓ Story tushunchasini bilasiz;<br>
            ✓ qavat strukturasini yaratasiz;<br>
            ✓ Story elevationlarni tushunasiz;<br>
            ✓ Home Storyni boshqarasiz;<br>
            ✓ ko'p qavatli modelni tashkil qilasiz;<br>
            ✓ 3D va Section orqali tekshirasiz;<br>
            ✓ Stories auditini bajarasiz.

            <br><br>

            Keyingi modul:
            <b>Layers.</b>
            """,
        },
    ],
}


# ============================================================
# QUIZ
# Q001-Q015
# ============================================================

LEVEL06_MODULE01_QUIZ = {
    "L06_M01_001": [
        {
            "code": "L06_Q001",
            "question": "Story Archicadda binoning vertikal qavat strukturasini tashkil qilish uchun ishlatiladimi?",
            "explanation": (
                "Story tizimi binoning qavatlarini vertikal struktura sifatida boshqarishga yordam beradi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L06_Q002",
            "question": "Story faqat oddiy papka vazifasini bajaradimi?",
            "explanation": (
                "Story model elementlarining vertikal joylashuvi va qavat strukturasiga ham bog'liq."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L06_Q003",
            "question": "Ko'p qavatli loyihani boshlashdan oldin Story strukturasini rejalashtirish foydalimi?",
            "explanation": (
                "Oldindan tuzilgan qavat tizimi modelni boshqarishni ancha tartibli qiladi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L06_M01_002": [
        {
            "code": "L06_Q004",
            "question": "Story Settings orqali qavat nomi va vertikal sathini boshqarish mumkinmi?",
            "explanation": (
                "Story Settings qavat strukturasining asosiy parametrlarini boshqarish uchun ishlatiladi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L06_Q005",
            "question": "Qavatlarni tasodifiy va turli nomlash tizimida yuritish professional workflowmi?",
            "explanation": (
                "Bir xil va tushunarli naming system loyiha strukturasini boshqarishni yaxshilaydi."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L06_Q006",
            "question": "Story elevation o'zgarsa unga bog'langan elementlarni tekshirish kerakmi?",
            "explanation": (
                "Qavat sathi o'zgarishi elementlarning vertikal joylashuviga ta'sir qilishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L06_M01_003": [
        {
            "code": "L06_Q007",
            "question": "Home Story elementning qaysi qavat strukturasiga tegishli ekanini boshqarishga yordam beradimi?",
            "explanation": (
                "Home Story elementning asosiy qavat aloqasini belgilashda muhim."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L06_Q008",
            "question": "2-qavat uchun yaratilgan elementlarni tasodifan Ground Floorga bog'lash modelni chalkashtirishi mumkinmi?",
            "explanation": (
                "Noto'g'ri Home Story model strukturasini boshqarishni qiyinlashtiradi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L06_Q009",
            "question": "Element Home Storysi uning hech qachon boshqa qavat balandligiga chiqolmasligini anglatadimi?",
            "explanation": (
                "Element bir nechta qavat balandligini egallashi mumkin; Home Story uning mantiqiy qavat aloqasini bildiradi."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
    ],

    "L06_M01_004": [
        {
            "code": "L06_Q010",
            "question": "Ko'p qavatli modelda qavatlar o'rtasidagi vertikal aloqani tekshirish kerakmi?",
            "explanation": (
                "Slab, wall, column, stair va boshqa elementlar qavatlararo birgalikda ishlaydi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L06_Q011",
            "question": "1-qavatdagi barcha elementlarni o'ylamasdan 2-qavatga copy qilish har doim to'g'ri workflowmi?",
            "explanation": (
                "Har bir qavatning funksional va konstruktiv strukturasi alohida tekshirilishi kerak."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L06_Q012",
            "question": "Story muammolarini Section orqali tekshirish foydalimi?",
            "explanation": (
                "Section qavat sathlari va elementlarning vertikal aloqasini ko'rishga yordam beradi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L06_M01_005": [
        {
            "code": "L06_Q013",
            "question": "Stories auditida Story nomlari va elevationlari tekshiriladimi?",
            "explanation": (
                "Professional qavat strukturasi nomlash va vertikal sathlarni ham nazorat qiladi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L06_Q014",
            "question": "Floor Plan yaxshi ko'rinsa 3D va Sectionni tekshirmaslik mumkinmi?",
            "explanation": (
                "Vertikal xatolar Floor Planda ko'rinmasligi mumkin, shuning uchun 3D va Section nazorati kerak."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L06_Q015",
            "question": "Stories bilan professional ishlashdagi to'g'ri workflow qaysi?",
            "explanation": (
                "Avval qavat strukturasi tuziladi, elementlar to'g'ri Storyga bog'lanadi va model bir nechta ko'rinishda tekshiriladi."
            ),
            "options": [
                (
                    "A",
                    "Story struktura → elevation → Home Story → model → audit",
                    True,
                ),
                (
                    "B",
                    "Barcha elementni bitta qavatda chizish",
                    False,
                ),
            ],
        },
    ],
}


# ============================================================
# DATABASE SEED
# ============================================================

def seed_level06_module01():
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
        ) in LEVEL06_MODULE01_LESSONS:

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
