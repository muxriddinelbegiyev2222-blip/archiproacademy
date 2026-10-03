from database.database import get_connection


# ============================================================
# LEVEL 7
# MODULE 06 - PROPERTIES
# ============================================================

LEVEL07_MODULE06_LESSONS = [
    (
        "L07_M06",
        "L07_M06_001",
        "BIM Properties tushunchasi",
        "theory",
        "Model elementlariga faqat geometriya emas, mazmunli BIM ma'lumot biriktirish mantig'ini tushunish.",
        1,
        40,
        20,
    ),
    (
        "L07_M06",
        "L07_M06_002",
        "Property yaratish va tuzilishi",
        "theory",
        "Property nomi, maqsadi, qiymat turi va elementlarga tegishliligini mantiqan tashkil qilish.",
        2,
        45,
        20,
    ),
    (
        "L07_M06",
        "L07_M06_003",
        "Element ma'lumotlarini standartlashtirish",
        "practice",
        "Bir xil turdagi elementlarda BIM ma'lumotlarini izchil va tushunarli standartda yuritish.",
        3,
        50,
        20,
    ),
    (
        "L07_M06",
        "L07_M06_004",
        "Properties va Schedules",
        "practice",
        "Properties orqali model ma'lumotlarini Schedules, audit va hujjatlashtirish workflowida ishlatish.",
        4,
        50,
        20,
    ),
    (
        "L07_M06",
        "L07_M06_005",
        "Properties professional audit",
        "practice",
        "Property nomlari, qiymatlar, elementlarga qo'llanishi va Schedule natijalarini kompleks tekshirish.",
        5,
        55,
        25,
    ),
]


# ============================================================
# CONTENT
# ============================================================

LEVEL07_MODULE06_CONTENT = {
    "L07_M06_001": [
        {
            "title": "BIM faqat 3D emas",
            "type": "highlight",
            "text": """
            BIM model —
            faqat devor,
            eshik va tomlarning
            3D geometriyasi emas.

            <br><br>

            BIM element
            o'zi haqida
            ma'lumot ham
            saqlashi mumkin.
            """,
        },
        {
            "title": "Property nima?",
            "type": "normal",
            "text": """
            Property —
            elementga tegishli
            qo'shimcha ma'lumotni

            <br><br>

            tartibli shaklda
            saqlash uchun
            ishlatiladigan
            xususiyat.
            """,
        },
        {
            "title": "Tasavvur qiling",
            "type": "example",
            "text": """
            Modelda 30 ta eshik bor.

            <br><br>

            Geometriya orqali
            ularning o'lchamini
            ko'rish mumkin.

            <br><br>

            Lekin sizga
            qo'shimcha ravishda:

            • foydalanish turi;<br>
            • izoh;<br>
            • loyiha kodi;<br>
            • boshqa texnik ma'lumot

            <br><br>

            kerak bo'lishi mumkin.

            <br><br>

            Properties shu
            ma'lumotlarni boshqarishga
            yordam beradi.
            """,
        },
        {
            "title": "Ma'lumotning qiymati",
            "type": "highlight",
            "text": """
            Model qanchalik
            chiroyli bo'lishidan
            qat'i nazar,

            <br><br>

            BIM ma'lumotlari
            tartibsiz bo'lsa,

            <br><br>

            Schedule,
            audit va
            hujjatlashtirishda
            muammo paydo bo'ladi.
            """,
        },
        {
            "title": "Property va geometriya",
            "type": "normal",
            "text": """
            Property —
            elementning
            geometrik shakli emas.

            <br><br>

            U element haqidagi
            ma'lumot qatlamidir.
            """,
        },
        {
            "title": "Property va oddiy Text farqi",
            "type": "warning",
            "text": """
            Chizmaga Text bilan
            yozilgan ma'lumot

            <br><br>

            har doim ham
            BIM elementining
            strukturaviy ma'lumoti
            hisoblanmaydi.

            <br><br>

            Property esa
            element bilan
            bog'langan BIM
            ma'lumot bo'lishi mumkin.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Bitta Door elementini
            tasavvur qiling.

            <br><br>

            Uning geometriyasidan
            tashqari yana
            qaysi 5 ta ma'lumot

            <br><br>

            loyiha uchun
            foydali bo'lishi
            mumkinligini yozing.
            """,
        },
    ],

    "L07_M06_002": [
        {
            "title": "Property yaratishdan oldin",
            "type": "highlight",
            "text": """
            Har qanday Property
            yaratishdan oldin

            <br><br>

            bitta savol bering:

            <br><br>

            “Bu ma'lumot
            nimaga kerak?”
            """,
        },
        {
            "title": "Maqsadsiz Property",
            "type": "warning",
            "text": """
            Shunchaki ko'p
            Property yaratish

            <br><br>

            BIM modelni
            professional qilmaydi.

            <br><br>

            Keraksiz Properties
            ma'lumot bazasini
            chalkashtiradi.
            """,
        },
        {
            "title": "Property nomi",
            "type": "normal",
            "text": """
            Property nomi
            tushunarli va
            izchil bo'lishi kerak.

            <br><br>

            Masalan:

            “Info1”
            yoki
            “Data Final”

            <br><br>

            kabi nomlar
            kelajakda tushunarsiz
            bo'lib qolishi mumkin.
            """,
        },
        {
            "title": "Qiymat turi",
            "type": "highlight",
            "text": """
            Property saqlaydigan
            ma'lumot turi

            <br><br>

            uning maqsadiga
            mos bo'lishi kerak.

            <br><br>

            Masalan,
            matn,
            raqam,
            mantiqiy holat
            yoki boshqa turdagi
            qiymatlar ishlatilishi mumkin.
            """,
        },
        {
            "title": "Bir xil ma'lumot — bir xil format",
            "type": "normal",
            "text": """
            Agar bir xil Property
            100 ta elementda
            ishlatilsa,

            <br><br>

            qiymat yozish
            usuli ham
            izchil bo'lishi kerak.
            """,
        },
        {
            "title": "Tasavvur qiling",
            "type": "example",
            "text": """
            “Fire Rating”
            degan ma'lumot
            turli elementlarda:

            <br><br>

            Fire<br>
            fire<br>
            FIRE<br>
            F<br>
            Yes

            <br><br>

            kabi turlicha
            yozilgan.

            <br><br>

            Ma'lumot mavjud,
            lekin standart yo'q.
            """,
        },
        {
            "title": "Property elementga mos bo'lsin",
            "type": "warning",
            "text": """
            Har bir Property
            barcha elementlarga
            kerak bo'lishi shart emas.

            <br><br>

            Ma'lumotni
            faqat maqsadga
            mos elementlarda
            ishlatish kerak.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Bitta Property
            konsepsiyasini tuzing.

            <br><br>

            Yozing:

            1. Property nomi;<br>
            2. nima uchun kerak;<br>
            3. qaysi elementlarda ishlatiladi;<br>
            4. qanday qiymat saqlaydi.
            """,
        },
    ],

    "L07_M06_003": [
        {
            "title": "Standartlashtirish",
            "type": "highlight",
            "text": """
            BIM Properties'dagi
            eng katta kuch —

            <br><br>

            element ma'lumotlarini
            bir xil standartda
            boshqarish imkoniyati.
            """,
        },
        {
            "title": "Naming standard",
            "type": "normal",
            "text": """
            Property nomlari
            bitta umumiy
            naming tizimiga
            ega bo'lsa,

            <br><br>

            loyiha jamoasi
            ma'lumotni tezroq
            tushunadi.
            """,
        },
        {
            "title": "Qiymat standard",
            "type": "normal",
            "text": """
            Faqat Property nomi
            emas,

            <br><br>

            uning qiymatlari ham
            bir xil mantiqda
            yozilishi kerak.
            """,
        },
        {
            "title": "Bo'sh qiymatlar",
            "type": "warning",
            "text": """
            Property mavjud
            bo'lishi mumkin,

            <br><br>

            lekin kerakli
            elementlarda qiymat
            kiritilmagan bo'lsa,

            <br><br>

            BIM ma'lumot
            to'liq emas.
            """,
        },
        {
            "title": "Noto'g'ri qiymat",
            "type": "example",
            "text": """
            Door elementida
            kerakli Property
            mavjud.

            <br><br>

            Lekin qiymati
            boshqa eshikdan
            nusxa ko'chirilgan
            va noto'g'ri.

            <br><br>

            Property mavjudligi
            uning to'g'riligini
            kafolatlamaydi.
            """,
        },
        {
            "title": "Copy-Paste xavfi",
            "type": "warning",
            "text": """
            Elementni nusxalashda
            uning BIM ma'lumotlari
            ham ko'chishi mumkin.

            <br><br>

            Shu sabab yangi
            vazifaga mos bo'lmagan
            eski Property qiymati
            qolib ketmasligini
            tekshiring.
            """,
        },
        {
            "title": "Jamoaviy ishlash",
            "type": "normal",
            "text": """
            Bir loyihada
            bir nechta odam ishlasa,

            <br><br>

            Property nomi,
            qiymat formati
            va to'ldirish qoidalari

            <br><br>

            hammaga tushunarli
            bo'lishi kerak.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            10 ta eshikni
            tekshirayotganingizni
            tasavvur qiling.

            <br><br>

            Bitta Property
            uchun audit qiling:

            • bo'sh qiymat bormi?<br>
            • naming bir xilmi?<br>
            • noto'g'ri nusxa qolganmi?<br>
            • format izchilmi?
            """,
        },
    ],

    "L07_M06_004": [
        {
            "title": "Properties + Schedules",
            "type": "highlight",
            "text": """
            Properties
            Schedules bilan
            birga ishlaganda

            <br><br>

            BIM ma'lumot
            yanada foydali
            bo'ladi.
            """,
        },
        {
            "title": "Schedule'da Property",
            "type": "normal",
            "text": """
            Agar elementlarda
            tartibli Property
            ma'lumotlari mavjud bo'lsa,

            <br><br>

            ularni Schedule
            Fields sifatida
            ko'rsatish mumkin.
            """,
        },
        {
            "title": "Tasavvur qiling",
            "type": "example",
            "text": """
            Barcha eshiklarda
            “Door Function”
            Property mavjud.

            <br><br>

            Schedule orqali
            shu ma'lumotni
            bir jadvalda ko'rib,

            <br><br>

            qaysi eshikda
            qiymat yetishmasligini
            aniqlash mumkin.
            """,
        },
        {
            "title": "Audit aylanishi",
            "type": "highlight",
            "text": """
            Professional workflow:

            <br><br>

            Model
            → Property
            → Schedule
            → xatoni aniqlash
            → modelni tuzatish
            → qayta tekshirish.
            """,
        },
        {
            "title": "Property Schedule'ni kuchaytiradi",
            "type": "normal",
            "text": """
            Geometrik parametrlar
            yetarli bo'lmagan
            holatlarda

            <br><br>

            Properties
            jadvalga loyiha uchun
            kerakli qo'shimcha
            ma'lumot beradi.
            """,
        },
        {
            "title": "Schedule'da bo'sh katak",
            "type": "warning",
            "text": """
            Schedule'dagi
            bo'sh katakni
            shunchaki jadval
            muammosi deb o'ylamang.

            <br><br>

            Muammo elementdagi
            Property qiymati
            yetishmasligi
            bo'lishi mumkin.
            """,
        },
        {
            "title": "Properties + Graphic Overrides",
            "type": "normal",
            "text": """
            Ayrim workflowlarda
            Property ma'lumoti

            <br><br>

            elementlarni
            tahliliy grafik
            ko'rinishlarda
            ajratishga ham
            yordam berishi mumkin.

            <br><br>

            Bu imkoniyat
            qo'llanilayotgan
            Archicad versiyasi
            va konfiguratsiyaga
            bog'liq.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Door Schedule uchun
            3 ta custom Property
            konsepsiyasini yarating.

            <br><br>

            Har biri uchun:

            • nomi;<br>
            • maqsadi;<br>
            • Schedule'da nima uchun kerakligi

            <br><br>

            yozilsin.
            """,
        },
    ],

    "L07_M06_005": [
        {
            "title": "Properties professional audit",
            "type": "highlight",
            "text": """
            Properties auditini
            quyidagi zanjirda
            bajaramiz:

            <br><br>

            Maqsad
            → Property
            → Element
            → Qiymat
            → Schedule
            → Audit
            """,
        },
        {
            "title": "1. Property maqsadi",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • Property nima uchun kerak?<br>
            • undan qayerda foydalaniladi?<br>
            • keraksiz Property emasmi?
            """,
        },
        {
            "title": "2. Naming",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • nomlar tushunarlimi?<br>
            • bir xil naming usuli ishlatilganmi?<br>
            • Test, New, Copy kabi noma'lum nomlar qolmaganmi?
            """,
        },
        {
            "title": "3. Elementlarga qo'llanishi",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • Property kerakli elementlarda mavjudmi?<br>
            • keraksiz elementlarda chiqmayaptimi?<br>
            • model strukturasiga mosmi?
            """,
        },
        {
            "title": "4. Qiymatlar",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • bo'sh qiymatlar bormi?<br>
            • noto'g'ri qiymatlar bormi?<br>
            • bir xil ma'lumot turlicha yozilganmi?<br>
            • eski nusxa qiymati qolganmi?
            """,
        },
        {
            "title": "5. Schedule audit",
            "type": "example",
            "text": """
            Property'ni
            Schedule'da ko'ring.

            <br><br>

            Bu orqali:

            • bo'sh qiymatlar;<br>
            • noodatiy qiymatlar;<br>
            • naming farqlari;<br>
            • noto'g'ri elementlar

            <br><br>

            tezroq aniqlanishi mumkin.
            """,
        },
        {
            "title": "6. Keraksiz Properties",
            "type": "warning",
            "text": """
            Yillar davomida
            yig'ilgan eski
            va foydalanilmaydigan
            Properties

            <br><br>

            loyiha standartini
            murakkablashtirishi mumkin.

            <br><br>

            Ularni audit qilish
            kerak.
            """,
        },
        {
            "title": "Xatoni toping",
            "type": "warning",
            "text": """
            Loyihada 15 ta
            custom Property bor.

            <br><br>

            Lekin:

            • 4 tasining vazifasi noma'lum;<br>
            • 3 tasi bir xil ma'lumotni saqlaydi;<br>
            • ayrim elementlarda qiymat bo'sh;<br>
            • bir xil qiymat turli yozilgan;<br>
            • Schedule'da ko'p kataklar bo'sh.

            <br><br>

            Property ko'p,
            lekin BIM ma'lumot
            sifati past.
            """,
        },
        {
            "title": "Professional checklist",
            "type": "example",
            "text": """
            Properties tizimini tekshiring:

            <br><br>

            <b>1.</b> Har bir Property maqsadga egami?<br><br>
            <b>2.</b> Naming izchilmi?<br><br>
            <b>3.</b> Qiymat turi to'g'rimi?<br><br>
            <b>4.</b> Kerakli elementlarda qo'llanganmi?<br><br>
            <b>5.</b> Bo'sh qiymatlar yo'qmi?<br><br>
            <b>6.</b> Qiymatlar standart formatdami?<br><br>
            <b>7.</b> Schedule orqali audit qilinganmi?<br><br>
            <b>8.</b> Keraksiz eski Properties tozalanganmi?
            """,
        },
        {
            "title": "Modul yakuni",
            "type": "highlight",
            "text": """
            Siz endi:

            <br><br>

            ✓ BIM Property nima ekanini tushunasiz;<br>
            ✓ maqsadli Property tuzasiz;<br>
            ✓ naming va qiymatlarni standartlashtirasiz;<br>
            ✓ element ma'lumotlarini boshqarasiz;<br>
            ✓ Properties'ni Schedules bilan ishlatasiz;<br>
            ✓ BIM ma'lumotlarini professional audit qilasiz.

            <br><br>

            Keyingi modul:
            <b>Classification.</b>
            """,
        },
    ],
}


# ============================================================
# QUIZ
# Q076-Q090
# ============================================================

LEVEL07_MODULE06_QUIZ = {
    "L07_M06_001": [
        {
            "code": "L07_Q076",
            "question": "BIM model faqat 3D geometriyadan iboratmi?",
            "explanation": (
                "BIM elementlari geometriya bilan birga mazmunli ma'lumotlarni ham saqlashi mumkin."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L07_Q077",
            "question": "Property element haqidagi qo'shimcha BIM ma'lumotini saqlashga yordam beradimi?",
            "explanation": (
                "Property elementlarga loyiha uchun zarur qo'shimcha ma'lumot biriktirishga yordam beradi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L07_Q078",
            "question": "Chizmaga oddiy Text bilan yozilgan ma'lumot har doim BIM Property bilan aynan bir xilmi?",
            "explanation": (
                "Oddiy grafik matn va element bilan bog'langan strukturaviy BIM Property bir xil tushuncha emas."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
    ],

    "L07_M06_002": [
        {
            "code": "L07_Q079",
            "question": "Property yaratishdan oldin uning maqsadini aniqlash kerakmi?",
            "explanation": (
                "Maqsadsiz Properties ma'lumot strukturasini keraksiz murakkablashtirishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L07_Q080",
            "question": "Ko'p Property yaratishning o'zi BIM modelni avtomatik ravishda professional qiladimi?",
            "explanation": (
                "Professional BIM uchun kerakli va sifatli ma'lumot muhim; keraksiz Properties aksincha chalkashlik yaratishi mumkin."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L07_Q081",
            "question": "Property nomi va qiymat turi uning vazifasiga mos bo'lishi kerakmi?",
            "explanation": (
                "Tushunarli naming va mos ma'lumot turi BIM ma'lumotining izchilligini oshiradi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L07_M06_003": [
        {
            "code": "L07_Q082",
            "question": "Bir xil ma'nodagi Property qiymatlarini turli usulda yozish auditni qiyinlashtirishi mumkinmi?",
            "explanation": (
                "Bir xil ma'lumot uchun izchil qiymat formati Schedule va audit natijalarini yaxshilaydi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L07_Q083",
            "question": "Property mavjud bo'lsa uning qiymati avtomatik ravishda to'g'ri deganimi?",
            "explanation": (
                "Property qiymati bo'sh, eski yoki noto'g'ri bo'lishi mumkin, shuning uchun tekshiruv kerak."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L07_Q084",
            "question": "Elementni nusxalashda eski BIM ma'lumotlari yangi vazifaga mos kelmasligi mumkinmi?",
            "explanation": (
                "Nusxalangan elementlarda oldingi Property qiymatlari qolishi mumkin, ularni tekshirish kerak."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L07_M06_004": [
        {
            "code": "L07_Q085",
            "question": "Properties Schedule Fields sifatida ishlatilishi mumkinmi?",
            "explanation": (
                "Tartibli Property ma'lumotlarini Schedule orqali chiqarish va tahlil qilish mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L07_Q086",
            "question": "Schedule'dagi bo'sh Property katagi model ma'lumotida yetishmovchilik borligini ko'rsatishi mumkinmi?",
            "explanation": (
                "Schedule modeldagi Property qiymatlarini ko'rsatadi, shuning uchun bo'sh qiymatlar BIM ma'lumotidagi bo'shliqni aniqlashi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L07_Q087",
            "question": "Properties va Schedules birgalikda BIM audit workflowini kuchaytirishi mumkinmi?",
            "explanation": (
                "Properties modelga ma'lumot beradi, Schedules esa bu ma'lumotlarni umumlashtirib tekshirishga yordam beradi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L07_M06_005": [
        {
            "code": "L07_Q088",
            "question": "Properties auditida naming, qiymatlar va elementlarga qo'llanishi tekshiriladimi?",
            "explanation": (
                "Professional audit Property strukturasini va modeldagi real qiymat sifatini birgalikda tekshiradi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L07_Q089",
            "question": "Foydalanilmaydigan eski Properties loyihada cheksiz saqlanishi har doim yaxshi amaliyotmi?",
            "explanation": (
                "Keraksiz Properties tizimni chalkashtirishi mumkin, shuning uchun ularni audit qilish foydali."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L07_Q090",
            "question": "Properties bilan professional ishlashdagi to'g'ri workflow qaysi?",
            "explanation": (
                "Avval maqsad aniqlanadi, Property yaratiladi, elementlarda izchil qiymatlar kiritiladi, Schedule orqali tekshiriladi va audit qilinadi."
            ),
            "options": [
                (
                    "A",
                    "Maqsad → Property → element → qiymat → Schedule → audit",
                    True,
                ),
                (
                    "B",
                    "Ko'p Property yaratish → tasodifiy qiymat → tekshirmaslik",
                    False,
                ),
            ],
        },
    ],
}


# ============================================================
# DATABASE SEED
# ============================================================

def seed_level07_module06():
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
        ) in LEVEL07_MODULE06_LESSONS:

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
