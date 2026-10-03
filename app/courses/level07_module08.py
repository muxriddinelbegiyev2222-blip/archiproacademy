from database.database import get_connection


# ============================================================
# LEVEL 7
# MODULE 08 - HOTLINK VA MODULES
# ============================================================

LEVEL07_MODULE08_LESSONS = [
    (
        "L07_M08",
        "L07_M08_001",
        "Hotlink va Module tushunchasi",
        "theory",
        "Katta yoki takrorlanuvchi BIM qismlarini alohida boshqarish va asosiy loyiha bilan bog'lash mantig'ini tushunish.",
        1,
        40,
        20,
    ),
    (
        "L07_M08",
        "L07_M08_002",
        "Module yaratish mantig'i",
        "theory",
        "Qaysi model qismlarini alohida modul sifatida tashkil qilish maqsadga muvofiqligini tushunish.",
        2,
        45,
        20,
    ),
    (
        "L07_M08",
        "L07_M08_003",
        "Hotlink orqali bog'lash",
        "practice",
        "Modul va asosiy loyiha o'rtasidagi bog'lanish, yangilanish va nazorat mantig'ini o'rganish.",
        3,
        50,
        20,
    ),
    (
        "L07_M08",
        "L07_M08_004",
        "Murakkab loyiha strukturasini boshqarish",
        "practice",
        "Takrorlanuvchi qismlar va yirik BIM loyihalarni tartibli modullar orqali boshqarish.",
        4,
        50,
        20,
    ),
    (
        "L07_M08",
        "L07_M08_005",
        "Hotlink va Modules professional audit",
        "practice",
        "Module tarkibi, bog'lanishlar, yangilanishlar va loyiha strukturasi bo'yicha kompleks audit bajarish.",
        5,
        55,
        25,
    ),
]


# ============================================================
# CONTENT
# ============================================================

LEVEL07_MODULE08_CONTENT = {
    "L07_M08_001": [
        {
            "title": "Module nima?",
            "type": "highlight",
            "text": """
            Module —
            asosiy loyihadan
            mantiqan ajratilgan

            <br><br>

            va alohida
            boshqarilishi mumkin
            bo'lgan model qismi.
            """,
        },
        {
            "title": "Hotlink nima?",
            "type": "normal",
            "text": """
            Hotlink —
            alohida model
            yoki modulni

            <br><br>

            boshqa loyiha
            ichida bog'langan
            holda ishlatish
            mantig'i.
            """,
        },
        {
            "title": "Nega kerak?",
            "type": "highlight",
            "text": """
            Hotlink va Modules:

            <br><br>

            • takrorlanuvchi qismlarni boshqarish;<br>
            • katta modelni qismlarga ajratish;<br>
            • jamoaviy workflowda tartib saqlash;<br>
            • bir xil model qismini ko'p joyda qayta ishlatish

            <br><br>

            uchun foydali bo'lishi mumkin.
            """,
        },
        {
            "title": "Tasavvur qiling",
            "type": "example",
            "text": """
            Katta turar joy
            loyihasida

            <br><br>

            bir xil blok
            bir necha marta
            takrorlanadi.

            <br><br>

            Har bir blokni
            alohida-alohida
            qayta chizish o'rniga,

            <br><br>

            bitta tartibli
            Module orqali
            boshqarish mumkin.
            """,
        },
        {
            "title": "Bitta xato — ko'p joy",
            "type": "warning",
            "text": """
            Modul noto'g'ri
            tuzilgan bo'lsa,

            <br><br>

            shu modul
            ishlatilgan barcha
            joylarda xato
            takrorlanishi mumkin.

            <br><br>

            Shuning uchun
            modul sifati
            juda muhim.
            """,
        },
        {
            "title": "Module hamma narsaga kerak emas",
            "type": "normal",
            "text": """
            Har bir kichik
            elementni Module
            qilish shart emas.

            <br><br>

            Module faqat
            loyiha strukturasini
            yaxshilaydigan holatda
            ishlatilishi kerak.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Bir loyiha misolini
            tasavvur qiling.

            <br><br>

            Qaysi qismni
            Module qilish
            foydali bo'lishi
            mumkinligini yozing.

            <br><br>

            Keyin sababini
            tushuntiring.
            """,
        },
    ],

    "L07_M08_002": [
        {
            "title": "Qachon Module yaratish kerak?",
            "type": "highlight",
            "text": """
            Module yaratish
            uchun asosiy savol:

            <br><br>

            “Bu model qismi
            alohida boshqarilsa
            loyiha yaxshilanadimi?”
            """,
        },
        {
            "title": "Takrorlanuvchi qism",
            "type": "normal",
            "text": """
            Agar bir xil
            model qismi

            <br><br>

            bir necha joyda
            takrorlansa,

            <br><br>

            Module konsepsiyasi
            foydali bo'lishi mumkin.
            """,
        },
        {
            "title": "Alohida jamoa",
            "type": "normal",
            "text": """
            Katta loyihada
            ayrim model qismlari

            <br><br>

            alohida jamoa
            yoki mas'ul shaxs
            tomonidan ishlab chiqilishi
            mumkin.

            <br><br>

            Module struktura
            bunday workflowga
            yordam berishi mumkin.
            """,
        },
        {
            "title": "Chegarasi aniq bo'lsin",
            "type": "highlight",
            "text": """
            Module ichiga
            nima kirishi

            <br><br>

            va nima
            asosiy modelda
            qolishi

            <br><br>

            oldindan aniq
            belgilanadi.
            """,
        },
        {
            "title": "Noaniq struktura",
            "type": "warning",
            "text": """
            Agar Module
            chegarasi noaniq bo'lsa,

            <br><br>

            bir elementning
            qayerda boshqarilishi
            tushunarsiz bo'lib qoladi.
            """,
        },
        {
            "title": "Naming",
            "type": "normal",
            "text": """
            Module nomlari
            tushunarli va
            izchil bo'lishi kerak.

            <br><br>

            Masalan:

            UNIT_A
            yoki
            BLOCK_01

            <br><br>

            kabi naming
            konsepsiyasi ishlatilishi
            mumkin.

            <br><br>

            Bu nomlar
            namuna xolos.
            """,
        },
        {
            "title": "Module hajmi",
            "type": "warning",
            "text": """
            Juda katta Module
            boshqarishni qiyinlashtirishi,

            <br><br>

            juda mayda Modules esa
            loyihani keraksiz
            murakkablashtirishi mumkin.

            <br><br>

            Balans kerak.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Katta loyiha uchun
            3 ta Module
            konsepsiyasini yozing.

            <br><br>

            Har biri uchun:

            • nomi;<br>
            • ichiga nima kiradi;<br>
            • nima uchun alohida boshqariladi

            <br><br>

            deb yozing.
            """,
        },
    ],

    "L07_M08_003": [
        {
            "title": "Hotlink bog'lanishi",
            "type": "highlight",
            "text": """
            Hotlink yordamida
            tashqi yoki alohida
            Module

            <br><br>

            asosiy loyiha ichida
            bog'langan holda
            ishlatiladi.
            """,
        },
        {
            "title": "Bog'langan, lekin mustaqil manba",
            "type": "normal",
            "text": """
            Hotlink'dagi
            model qismi

            <br><br>

            asosiy loyiha
            bilan bog'langan,

            <br><br>

            lekin uning
            manba modeli
            alohida boshqarilishi
            mumkin.
            """,
        },
        {
            "title": "Yangilanish mantig'i",
            "type": "highlight",
            "text": """
            Manba Module
            o'zgarsa,

            <br><br>

            bog'langan loyiha
            ham shu o'zgarishni
            yangilanish orqali
            qabul qilishi mumkin.
            """,
        },
        {
            "title": "Tasavvur qiling",
            "type": "example",
            "text": """
            UNIT_A
            Module loyihada
            5 marta ishlatilgan.

            <br><br>

            Modul ichidagi
            xatoni bitta joyda
            tuzatasiz.

            <br><br>

            Keyin bog'langan
            nusxalar yangilanadi.

            <br><br>

            Bu takroriy
            qo'lda tuzatishni
            kamaytiradi.
            """,
        },
        {
            "title": "Yangilashni unutish",
            "type": "warning",
            "text": """
            Manba Module
            o'zgargan,

            <br><br>

            lekin asosiy loyiha
            yangilanmagan bo'lsa,

            <br><br>

            eskirgan ma'lumot
            ishlatilishi mumkin.
            """,
        },
        {
            "title": "Manba fayl",
            "type": "normal",
            "text": """
            Hotlink workflowda
            manba fayl
            yoki Module

            <br><br>

            qayerda va
            qanday boshqarilayotganini
            loyiha jamoasi
            bilishi kerak.
            """,
        },
        {
            "title": "Bog'lanish uzilishi",
            "type": "warning",
            "text": """
            Manba topilmasa
            yoki loyiha
            strukturasi o'zgarsa,

            <br><br>

            Hotlink bog'lanishlari
            muammo berishi mumkin.

            <br><br>

            Shu sabab
            fayl strukturasini
            tartibli saqlash muhim.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Bitta Module
            va 3 ta Hotlink
            nusxadan iborat
            workflow chizing:

            <br><br>

            MODULE
            ↓
            HOTLINK 1
            HOTLINK 2
            HOTLINK 3

            <br><br>

            Manba o'zgarsa
            nima bo'lishini
            tushuntiring.
            """,
        },
    ],

    "L07_M08_004": [
        {
            "title": "Murakkab loyiha strukturasi",
            "type": "highlight",
            "text": """
            Katta loyiha
            bitta ulkan
            tartibsiz model

            <br><br>

            bo'lishi shart emas.

            <br><br>

            Uni mantiqiy
            qismlarga ajratish
            boshqaruvni yengillashtirishi
            mumkin.
            """,
        },
        {
            "title": "Struktura maqsadi",
            "type": "normal",
            "text": """
            Module struktura
            quyidagilarga
            xizmat qilishi kerak:

            <br><br>

            • aniqlik;<br>
            • tezlik;<br>
            • takroriy ishni kamaytirish;<br>
            • jamoaviy nazorat;<br>
            • xatolarni boshqarish.
            """,
        },
        {
            "title": "Takrorlanuvchi uy bloki",
            "type": "example",
            "text": """
            Masalan,
            bir xil turdagi
            uy bloki

            <br><br>

            bir nechta joyda
            takrorlanadi.

            <br><br>

            Shu blokni
            Module sifatida
            boshqarish

            <br><br>

            loyiha izchilligini
            oshirishi mumkin.
            """,
        },
        {
            "title": "Variantlar",
            "type": "normal",
            "text": """
            Agar bloklarning
            ayrimlari bir-biridan
            sezilarli farq qilsa,

            <br><br>

            ularni majburan
            bitta Module orqali
            boshqarish

            <br><br>

            noto'g'ri workflow
            bo'lishi mumkin.
            """,
        },
        {
            "title": "Jamoa bilan ishlash",
            "type": "highlight",
            "text": """
            Module struktura
            jamoada kim

            <br><br>

            qaysi qism uchun
            javobgar ekanini
            aniqroq qilishga
            yordam beradi.
            """,
        },
        {
            "title": "Koordinatsiya",
            "type": "normal",
            "text": """
            Modules o'rtasidagi:

            <br><br>

            • balandlik;<br>
            • joylashuv;<br>
            • grid;<br>
            • ulanish nuqtalari;<br>
            • boshqa koordinatsiya

            <br><br>

            tekshirilishi kerak.
            """,
        },
        {
            "title": "Noto'g'ri koordinatsiya",
            "type": "warning",
            "text": """
            Module geometriyasi
            o'zi to'g'ri bo'lishi mumkin,

            <br><br>

            lekin asosiy modelga
            noto'g'ri joylashtirilsa,

            <br><br>

            loyiha xato bo'ladi.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Murakkab loyiha uchun
            Module xaritasi tuzing.

            <br><br>

            Masalan:

            MAIN PROJECT

            <br><br>

            ├─ MODULE A<br>
            ├─ MODULE B<br>
            └─ MODULE C

            <br><br>

            Har bir Module
            vazifasini yozing.
            """,
        },
    ],

    "L07_M08_005": [
        {
            "title": "Hotlink va Modules professional audit",
            "type": "highlight",
            "text": """
            Audit zanjiri:

            <br><br>

            Module
            → Source
            → Hotlink
            → Position
            → Update
            → Project Audit
            """,
        },
        {
            "title": "1. Module maqsadi",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • nega Module yaratilgan?<br>
            • u haqiqatan ham kerakmi?<br>
            • loyiha strukturasini yaxshilayaptimi?
            """,
        },
        {
            "title": "2. Module tarkibi",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • kerakli elementlar ichidami?<br>
            • ortiqcha elementlar yo'qmi?<br>
            • Module chegarasi aniqmi?
            """,
        },
        {
            "title": "3. Naming",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • Module nomlari tushunarlimi?<br>
            • Copy, Final2 kabi noaniq nomlar yo'qmi?<br>
            • naming tizimi izchilmi?
            """,
        },
        {
            "title": "4. Hotlink source",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • to'g'ri manbaga bog'langanmi?<br>
            • eski source ishlatilmayaptimi?<br>
            • source joylashuvi jamoaga tushunarlimi?
            """,
        },
        {
            "title": "5. Position",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • Hotlink to'g'ri joydami?<br>
            • balandlik mosmi?<br>
            • orientatsiya to'g'rimi?<br>
            • boshqa qismlar bilan moslashganmi?
            """,
        },
        {
            "title": "6. Update",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • source yangilanganmi?<br>
            • Hotlink eskirib qolmaganmi?<br>
            • oxirgi o'zgarishlar asosiy modelga kirganmi?
            """,
        },
        {
            "title": "Xatoni toping",
            "type": "warning",
            "text": """
            Loyiha 4 ta
            Module'dan iborat.

            <br><br>

            Lekin:

            • Module nomlari tushunarsiz;<br>
            • bittasi eski source'ga bog'langan;<br>
            • bittasi noto'g'ri balandlikda;<br>
            • yangilanishlar tekshirilmagan;<br>
            • qaysi Module'ni kim boshqarishi noma'lum.

            <br><br>

            Hotlink ishlayapti,
            lekin loyiha
            boshqaruvi zaif.
            """,
        },
        {
            "title": "Professional checklist",
            "type": "example",
            "text": """
            Hotlink va Modules
            tizimini tekshiring:

            <br><br>

            <b>1.</b> Har bir Module aniq maqsadga egami?<br><br>
            <b>2.</b> Tarkibi to'g'rimi?<br><br>
            <b>3.</b> Naming izchilmi?<br><br>
            <b>4.</b> Source to'g'rimi?<br><br>
            <b>5.</b> Hotlink joylashuvi to'g'rimi?<br><br>
            <b>6.</b> Update qilinganmi?<br><br>
            <b>7.</b> Jamoa mas'uliyati aniqmi?<br><br>
            <b>8.</b> Modullar orasida koordinatsiya tekshirilganmi?
            """,
        },
        {
            "title": "Modul yakuni",
            "type": "highlight",
            "text": """
            Siz endi:

            <br><br>

            ✓ Module tushunchasini bilasiz;<br>
            ✓ qachon Module kerakligini tushunasiz;<br>
            ✓ Hotlink bog'lanish mantig'ini bilasiz;<br>
            ✓ katta BIM modelni qismlarga ajratasiz;<br>
            ✓ yangilanish va koordinatsiyani nazorat qilasiz;<br>
            ✓ Hotlink va Modules tizimini professional audit qilasiz.

            <br><br>

            Keyingi modul:
            <b>Professional Template.</b>
            """,
        },
    ],
}


# ============================================================
# QUIZ
# Q106-Q120
# ============================================================

LEVEL07_MODULE08_QUIZ = {
    "L07_M08_001": [
        {
            "code": "L07_Q106",
            "question": "Module modelning alohida boshqarilishi mumkin bo'lgan mantiqiy qismi bo'lishi mumkinmi?",
            "explanation": (
                "Module katta yoki takrorlanuvchi model qismlarini alohida boshqarishga yordam beradi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L07_Q107",
            "question": "Hotlink alohida Module yoki model qismini boshqa loyiha bilan bog'lash mantig'imi?",
            "explanation": (
                "Hotlink manba model qismini asosiy loyiha ichida bog'langan holda ishlatishga yordam beradi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L07_Q108",
            "question": "Har bir kichik elementni albatta alohida Module qilish kerakmi?",
            "explanation": (
                "Module faqat loyiha strukturasini yaxshilaydigan holatlarda ishlatilishi kerak."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
    ],

    "L07_M08_002": [
        {
            "code": "L07_Q109",
            "question": "Takrorlanuvchi model qismi Module sifatida boshqarish uchun yaxshi nomzod bo'lishi mumkinmi?",
            "explanation": (
                "Takroriy qismlarni bitta manba orqali boshqarish qayta ishlashni kamaytirishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L07_Q110",
            "question": "Module chegarasi noaniq bo'lishi boshqaruv muammolarini keltirib chiqarishi mumkinmi?",
            "explanation": (
                "Qaysi element qayerda boshqarilishi aniq bo'lmasa loyiha strukturasida chalkashlik paydo bo'ladi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L07_Q111",
            "question": "Juda ko'p mayda Modules loyiha strukturasini keraksiz murakkablashtirishi mumkinmi?",
            "explanation": (
                "Module soni va hajmi loyiha ehtiyojiga mos va boshqariladigan bo'lishi kerak."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L07_M08_003": [
        {
            "code": "L07_Q112",
            "question": "Manba Module o'zgarsa Hotlink nusxalarni yangilash zarur bo'lishi mumkinmi?",
            "explanation": (
                "Hotlink'dagi bog'langan ma'lumot manba o'zgarishlaridan keyin yangilanishi kerak bo'lishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L07_Q113",
            "question": "Hotlink yangilanmasa asosiy loyiha eskirgan ma'lumotni ko'rsatishi mumkinmi?",
            "explanation": (
                "Manba o'zgargan bo'lsa, yangilanmagan Hotlink eski holatda qolishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L07_Q114",
            "question": "Hotlink source fayl yoki modulining qayerda boshqarilishini bilish muhim emasmi?",
            "explanation": (
                "Manba strukturasini bilish yangilash, audit va jamoaviy boshqaruv uchun muhim."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
    ],

    "L07_M08_004": [
        {
            "code": "L07_Q115",
            "question": "Katta BIM loyihani mantiqiy Modules orqali bo'lish boshqaruvni yengillashtirishi mumkinmi?",
            "explanation": (
                "To'g'ri Module struktura katta modeldagi javobgarlik, takroriy ish va koordinatsiyani yaxshilashi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L07_Q116",
            "question": "Module geometriyasi to'g'ri bo'lsa uning asosiy loyihadagi joylashuvini tekshirish shart emasmi?",
            "explanation": (
                "Module to'g'ri bo'lsa ham noto'g'ri balandlik, orientatsiya yoki pozitsiya loyiha xatosiga olib kelishi mumkin."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L07_Q117",
            "question": "Modules orasidagi koordinatsiya katta loyihada muhimmi?",
            "explanation": (
                "Joylashuv, balandlik va ulanishlar modullar o'rtasida tekshirilishi kerak."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L07_M08_005": [
        {
            "code": "L07_Q118",
            "question": "Hotlink auditida source, joylashuv va update holati tekshiriladimi?",
            "explanation": (
                "Professional audit manba, bog'lanish, pozitsiya va yangilanish holatini birgalikda tekshiradi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L07_Q119",
            "question": "Tushunarsiz Module naming jamoaviy ishlashni qiyinlashtirishi mumkinmi?",
            "explanation": (
                "Izchil naming qaysi modul nima uchun kerakligini tez tushunishga yordam beradi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L07_Q120",
            "question": "Hotlink va Modules bilan professional ishlashdagi to'g'ri workflow qaysi?",
            "explanation": (
                "Module maqsadi aniqlanadi, source tartibli yaratiladi, Hotlink joylashtiriladi, update va koordinatsiya tekshiriladi."
            ),
            "options": [
                (
                    "A",
                    "Maqsad → Module → Source → Hotlink → Position → Update → audit",
                    True,
                ),
                (
                    "B",
                    "Ko'p Module yaratish → source'ni unutish → update qilmaslik",
                    False,
                ),
            ],
        },
    ],
}


# ============================================================
# DATABASE SEED
# ============================================================

def seed_level07_module08():
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
        ) in LEVEL07_MODULE08_LESSONS:

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
