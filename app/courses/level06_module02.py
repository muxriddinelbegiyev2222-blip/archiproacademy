from database.database import get_connection


# ============================================================
# LEVEL 6
# MODULE 02 - LAYERS
# ============================================================

LEVEL06_MODULE02_LESSONS = [
    (
        "L06_M02",
        "L06_M02_001",
        "Layer tushunchasi",
        "theory",
        "Archicaddagi Layer tizimi va elementlarni tartibli guruhlash mantig'ini tushunish.",
        1,
        40,
        20,
    ),
    (
        "L06_M02",
        "L06_M02_002",
        "Layer Settings",
        "theory",
        "Layer nomlari, ko'rinish holati, lock va boshqa asosiy boshqaruvlarni tushunish.",
        2,
        45,
        20,
    ),
    (
        "L06_M02",
        "L06_M02_003",
        "Layer Combination",
        "practice",
        "Turli loyiha ko'rinishlari uchun Layer Combination yaratish va boshqarish.",
        3,
        50,
        20,
    ),
    (
        "L06_M02",
        "L06_M02_004",
        "Professional layer struktura",
        "practice",
        "Arxitektura modelini devor, mebel, annotation va boshqa kategoriyalar bo'yicha tartibli tashkil qilish.",
        4,
        50,
        20,
    ),
    (
        "L06_M02",
        "L06_M02_005",
        "Layers professional audit",
        "practice",
        "Layer nomlari, element biriktirilishi, kombinatsiyalar va ko'rinishlarni kompleks tekshirish.",
        5,
        55,
        25,
    ),
]


# ============================================================
# CONTENT
# ============================================================

LEVEL06_MODULE02_CONTENT = {
    "L06_M02_001": [
        {
            "title": "Layer nima?",
            "type": "highlight",
            "text": """
            Layer —
            Archicaddagi elementlarni
            mantiqiy guruhlarga ajratish
            vositalaridan biri.

            <br><br>

            Masalan:

            <br><br>

            • devorlar;<br>
            • mebel;<br>
            • o'lchamlar;<br>
            • tekstlar;<br>
            • yordamchi grafikalar

            <br><br>

            turli layerlarda
            tashkil qilinishi mumkin.
            """,
        },
        {
            "title": "Layer papka emas",
            "type": "normal",
            "text": """
            Layerni oddiy
            fayl papkasi kabi
            tasavvur qilmang.

            <br><br>

            U model elementining
            ko'rinish va boshqaruv
            tizimiga ta'sir qiladi.
            """,
        },
        {
            "title": "Nega Layer kerak?",
            "type": "highlight",
            "text": """
            Katta loyihada
            yuzlab yoki minglab
            elementlar bo'lishi mumkin.

            <br><br>

            Layer tizimi
            kerakli elementlarni
            boshqarishni osonlashtiradi.
            """,
        },
        {
            "title": "Tasavvur qiling",
            "type": "example",
            "text": """
            Butun loyiha:

            <br><br>

            devor,
            furniture,
            dimensions,
            text,
            detail lines

            <br><br>

            bitta layerda turibdi.

            <br><br>

            Endi faqat furniture'ni
            vaqtincha yashirmoqchisiz.

            <br><br>

            Buni boshqarish
            juda noqulay bo'ladi.
            """,
        },
        {
            "title": "Element yaratishdan oldin",
            "type": "normal",
            "text": """
            Archicadda element yaratganda
            uning qaysi Layerga
            tushayotganini tekshiring.

            <br><br>

            Noto'g'ri layer
            keyinchalik View va
            Documentationda muammo
            yaratishi mumkin.
            """,
        },
        {
            "title": "Layer va element turi",
            "type": "normal",
            "text": """
            Layer nomi
            elementning maqsadini
            tushunarli ko'rsatishi kerak.

            <br><br>

            Masalan,
            tasodifiy:

            <br><br>

            Layer 1<br>
            Layer 2<br>
            Layer New

            <br><br>

            kabi nomlardan
            qochish ma'qul.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Kichik uy loyihasi uchun
            kamida 5 ta layer
            kategoriyasini o'ylang.

            <br><br>

            Masalan:

            • Walls;<br>
            • Furniture;<br>
            • Dimensions;<br>
            • Text;<br>
            • 2D Helpers.

            <br><br>

            Har biriga
            qanday elementlar tushishini
            yozib chiqing.
            """,
        },
    ],

    "L06_M02_002": [
        {
            "title": "Layer Settings",
            "type": "highlight",
            "text": """
            Layer Settings orqali
            loyiha layerlari
            boshqariladi.

            <br><br>

            Bu yerda layerlarni:

            <br><br>

            • ko'rish;<br>
            • yashirish;<br>
            • lock qilish;<br>
            • nomlash;<br>
            • tartiblash

            <br><br>

            mumkin.
            """,
        },
        {
            "title": "Visible / Hidden",
            "type": "normal",
            "text": """
            Layer ko'rinadigan
            yoki yashirilgan
            holatda bo'lishi mumkin.

            <br><br>

            Bu elementni
            modeldan o'chirmaydi.

            <br><br>

            Faqat uning
            ko'rinishini boshqaradi.
            """,
        },
        {
            "title": "Hide va Delete farqi",
            "type": "warning",
            "text": """
            Layerni yashirish bilan
            elementni o'chirish
            bir xil emas.

            <br><br>

            Hidden element
            loyiha ichida mavjud
            bo'lib qoladi.
            """,
        },
        {
            "title": "Locked Layer",
            "type": "highlight",
            "text": """
            Layerni lock qilish
            undagi elementlarni
            tasodifiy o'zgartirishdan
            himoya qilishga yordam beradi.
            """,
        },
        {
            "title": "Tasavvur qiling",
            "type": "example",
            "text": """
            Tayyor 2D reference
            chiziqlar bor.

            <br><br>

            Siz ularni
            tasodifan siljitib yubormaslik
            uchun tegishli layerni
            lock qilishingiz mumkin.
            """,
        },
        {
            "title": "Lock xavfsizlik vositasi",
            "type": "normal",
            "text": """
            Professional workflowda
            ba'zi elementlarni
            vaqtincha himoyalash

            <br><br>

            modelda tasodifiy
            xatolarni kamaytirishi mumkin.
            """,
        },
        {
            "title": "Layer nomlash",
            "type": "normal",
            "text": """
            Layer nomlari
            qisqa,
            tushunarli
            va izchil bo'lishi kerak.

            <br><br>

            Bir loyiha ichida
            bir xil naming principle
            ishlating.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Layer Settingsni oching.

            <br><br>

            Bitta layerni:

            1. visible;<br>
            2. hidden;<br>
            3. locked

            <br><br>

            holatlarida sinab ko'ring.

            <br><br>

            Model elementiga
            nima bo'lishini kuzating.
            """,
        },
    ],

    "L06_M02_003": [
        {
            "title": "Layer Combination nima?",
            "type": "highlight",
            "text": """
            Layer Combination —
            layerlarning ma'lum
            ko'rinish holatini

            <br><br>

            bitta tayyor konfiguratsiya
            sifatida saqlash imkonini beradi.
            """,
        },
        {
            "title": "Nega kerak?",
            "type": "normal",
            "text": """
            Har safar
            o'nlab layerni
            qo'lda yoqib-o'chirish
            noqulay.

            <br><br>

            Layer Combination
            tayyor ish holatini
            tez chaqirishga yordam beradi.
            """,
        },
        {
            "title": "Plan uchun kombinatsiya",
            "type": "example",
            "text": """
            Architectural Plan
            ko'rinishida:

            <br><br>

            • Walls — ON<br>
            • Doors — ON<br>
            • Furniture — ON<br>
            • Dimensions — ON<br>
            • Helper Graphics — OFF

            <br><br>

            kabi konfiguratsiya
            ishlatilishi mumkin.
            """,
        },
        {
            "title": "Furniture Plan",
            "type": "example",
            "text": """
            Furniture Plan uchun
            boshqa kombinatsiya
            yaratish mumkin.

            <br><br>

            Masalan:

            furniture va room elements
            ko'rinadi,

            <br><br>

            ayrim keraksiz
            texnik grafikalar
            yashiriladi.
            """,
        },
        {
            "title": "Structure View",
            "type": "example",
            "text": """
            Konstruktiv tahlilga
            yaqin ko'rinishda

            <br><br>

            dekorativ yoki
            furniture layerlarini
            vaqtincha yashirish
            foydali bo'lishi mumkin.
            """,
        },
        {
            "title": "Combinationni tasodifiy o'zgartirmang",
            "type": "warning",
            "text": """
            Mavjud Layer Combination
            ichidagi layer holatini
            tushunmasdan o'zgartirsangiz,

            <br><br>

            unga bog'langan Viewlar
            kutilmagan ko'rinishga
            o'tishi mumkin.
            """,
        },
        {
            "title": "View bilan aloqa",
            "type": "highlight",
            "text": """
            Professional Archicad workflowda
            Layer Combination

            <br><br>

            ko'pincha View sozlamalarining
            muhim qismi bo'ladi.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            3 ta Layer Combination yarating:

            <br><br>

            1. Working Plan<br>
            2. Furniture Plan<br>
            3. Clean Presentation

            <br><br>

            Har birida
            qaysi layerlar ko'rinishini
            alohida belgilang.
            """,
        },
    ],

    "L06_M02_004": [
        {
            "title": "Professional layer struktura",
            "type": "highlight",
            "text": """
            Professional loyihada
            layerlar tasodifiy
            yaratilmaydi.

            <br><br>

            Ular loyiha
            strukturasi bo'yicha
            tartiblanadi.
            """,
        },
        {
            "title": "Asosiy kategoriyalar",
            "type": "normal",
            "text": """
            Loyiha talabiga qarab
            layerlarni quyidagicha
            kategoriyalash mumkin:

            <br><br>

            • model elements;<br>
            • furniture;<br>
            • annotation;<br>
            • dimensions;<br>
            • site elements;<br>
            • helper graphics.
            """,
        },
        {
            "title": "Bitta element — mantiqiy layer",
            "type": "highlight",
            "text": """
            Har bir element
            unga mos mantiqiy
            layerda bo'lishi kerak.

            <br><br>

            Masalan,
            dimensionni furniture
            layeriga tashlash

            <br><br>

            kelajakda boshqaruvni
            qiyinlashtiradi.
            """,
        },
        {
            "title": "Over-layering",
            "type": "warning",
            "text": """
            Juda kam layer
            muammo.

            <br><br>

            Lekin har bir
            kichik detal uchun
            alohida layer yaratish ham

            <br><br>

            ortiqcha murakkablik
            keltirib chiqarishi mumkin.
            """,
        },
        {
            "title": "Balans",
            "type": "normal",
            "text": """
            Layer strukturasida
            ikki maqsad orasida
            balans kerak:

            <br><br>

            • yetarlicha nazorat;<br>
            • ortiqcha murakkabliksiz boshqaruv.
            """,
        },
        {
            "title": "Naming standard",
            "type": "example",
            "text": """
            Loyiha ichida:

            <br><br>

            A-Wall<br>
            A-Furniture<br>
            A-Dimension<br>
            A-Text

            <br><br>

            kabi izchil naming
            ishlatilishi mumkin.

            <br><br>

            Bu faqat misol.

            <br><br>

            Muhim narsa —
            butun loyiha bo'ylab
            bir xil tizim.
            """,
        },
        {
            "title": "Team workflow",
            "type": "highlight",
            "text": """
            Layer nomlari
            faqat siz uchun emas.

            <br><br>

            Boshqa loyiha ishtirokchisi
            faylni ochganda ham
            struktura tushunarli bo'lishi kerak.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            O'zingiz uchun
            kichik residential template
            layer strukturasi tuzing.

            <br><br>

            Kamida:

            • Wall<br>
            • Slab<br>
            • Furniture<br>
            • Dimension<br>
            • Text<br>
            • Site<br>
            • Helper

            <br><br>

            kategoriyalarini
            tartib bilan yozing.
            """,
        },
    ],

    "L06_M02_005": [
        {
            "title": "Layers professional audit",
            "type": "highlight",
            "text": """
            Endi Layer tizimini
            faqat ON/OFF vositasi sifatida emas,

            <br><br>

            butun loyiha boshqaruv
            sistemasi sifatida
            tekshiramiz.
            """,
        },
        {
            "title": "1. Naming",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • layer nomlari tushunarlimi?<br>
            • naming standard bir xilmi?<br>
            • Layer 1, New Layer kabi nomlar qolmaganmi?
            """,
        },
        {
            "title": "2. Element assignment",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • wall to'g'ri layerdami?<br>
            • furniture to'g'ri layerdami?<br>
            • annotation alohidami?<br>
            • dimensions mantiqiy layerdami?
            """,
        },
        {
            "title": "3. Visibility",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • keraksiz layerlar ko'rinib qolmaganmi?<br>
            • muhim layer tasodifan hidden emasmi?<br>
            • ishlash vaqtida kerakli layerlar ko'rinadimi?
            """,
        },
        {
            "title": "4. Lock",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • himoyalanishi kerak bo'lgan layerlar lock qilinganmi?<br>
            • tasodifan kerakli layer lock bo'lib qolmaganmi?
            """,
        },
        {
            "title": "5. Layer Combinations",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • Working Plan kombinatsiyasi bormi?<br>
            • Presentation uchun kombinatsiya bormi?<br>
            • kombinatsiyalar Viewlar bilan mantiqan ishlayaptimi?
            """,
        },
        {
            "title": "Xatoni toping",
            "type": "warning",
            "text": """
            Loyiha chiroyli ko'rinadi.

            <br><br>

            Lekin:

            <br><br>

            • dimensions Furniture layerda;<br>
            • devorlarning bir qismi Layer 1 da;<br>
            • keraksiz helper lines barcha Viewlarda ko'rinadi;<br>
            • hech qanday Layer Combination yo'q.

            <br><br>

            Muammo:

            <br><br>

            model mavjud,
            lekin layer struktura
            professional tashkil qilinmagan.
            """,
        },
        {
            "title": "Professional checklist",
            "type": "example",
            "text": """
            Layers tizimini tekshiring:

            <br><br>

            <b>1.</b> Naming izchilmi?<br><br>
            <b>2.</b> Elementlar to'g'ri layerdami?<br><br>
            <b>3.</b> Visibility boshqariladimi?<br><br>
            <b>4.</b> Lock to'g'ri ishlatilganmi?<br><br>
            <b>5.</b> Layer Combinationlar mavjudmi?<br><br>
            <b>6.</b> Viewlar bilan aloqa mantiqiymi?<br><br>
            <b>7.</b> Ortiqcha layerlar yo'qmi?
            """,
        },
        {
            "title": "Modul yakuni",
            "type": "highlight",
            "text": """
            Siz endi:

            <br><br>

            ✓ Layer tushunchasini bilasiz;<br>
            ✓ elementlarni layerlarga ajratasiz;<br>
            ✓ visibilityni boshqarasiz;<br>
            ✓ layerlarni lock qilasiz;<br>
            ✓ Layer Combination yaratasiz;<br>
            ✓ professional naming tizimini tushunasiz;<br>
            ✓ loyiha layer auditini bajarasiz.

            <br><br>

            Keyingi modul:
            <b>Building Materials.</b>
            """,
        },
    ],
}


# ============================================================
# QUIZ
# Q016-Q030
# ============================================================

LEVEL06_MODULE02_QUIZ = {
    "L06_M02_001": [
        {
            "code": "L06_Q016",
            "question": "Layer model elementlarini mantiqiy guruhlashga yordam beradimi?",
            "explanation": (
                "Layer tizimi elementlarni boshqariladigan kategoriyalarga ajratishga yordam beradi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L06_Q017",
            "question": "Butun loyihadagi barcha elementlarni bitta layerga joylashtirish professional workflowmi?",
            "explanation": (
                "Turli elementlarni mantiqiy layerlarga ajratish loyiha boshqaruvini osonlashtiradi."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L06_Q018",
            "question": "Element yaratganda uning qaysi Layerga tushayotganini tekshirish foydalimi?",
            "explanation": (
                "Noto'g'ri layer keyinchalik View va Documentationda muammo yaratishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L06_M02_002": [
        {
            "code": "L06_Q019",
            "question": "Layerni yashirish undagi elementlarni o'chirib yuboradimi?",
            "explanation": (
                "Hidden layerdagi elementlar modelda qoladi, faqat ko'rinmaydi."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L06_Q020",
            "question": "Layerni lock qilish tasodifiy tahrirlashdan himoya qilishga yordam beradimi?",
            "explanation": (
                "Locked layerdagi elementlar tasodifiy o'zgartirishdan himoyalanishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L06_Q021",
            "question": "Layer nomlari tushunarli va izchil bo'lishi kerakmi?",
            "explanation": (
                "Professional naming modelni siz va boshqa loyiha ishtirokchilari uchun tushunarli qiladi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L06_M02_003": [
        {
            "code": "L06_Q022",
            "question": "Layer Combination bir nechta layerning ko'rinish holatini saqlashi mumkinmi?",
            "explanation": (
                "Layer Combination ma'lum View uchun layer konfiguratsiyasini qayta ishlatishga yordam beradi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L06_Q023",
            "question": "Har safar barcha layerlarni qo'lda yoqib-o'chirish yagona professional usulmi?",
            "explanation": (
                "Layer Combination takroriy ko'rinish konfiguratsiyalarini tez boshqarishga yordam beradi."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L06_Q024",
            "question": "Turli Viewlar uchun turli Layer Combination ishlatilishi mumkinmi?",
            "explanation": (
                "Working Plan, Furniture Plan yoki boshqa Viewlar turli layer ko'rinishiga ega bo'lishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L06_M02_004": [
        {
            "code": "L06_Q025",
            "question": "Professional loyihada layerlar mantiqiy struktura bo'yicha tashkil qilinadimi?",
            "explanation": (
                "Model, furniture, annotation va boshqa kategoriyalarni mantiqan ajratish boshqaruvni yaxshilaydi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L06_Q026",
            "question": "Dimensionni tasodifan Furniture layerga joylashtirish yaxshi layer strukturami?",
            "explanation": (
                "Element o'z maqsadiga mos layerga biriktirilishi kerak."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L06_Q027",
            "question": "Haddan tashqari ko'p va keraksiz layer ham boshqaruvni qiyinlashtirishi mumkinmi?",
            "explanation": (
                "Layer strukturasida nazorat va soddalik o'rtasida balans kerak."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L06_M02_005": [
        {
            "code": "L06_Q028",
            "question": "Layers auditida elementlarning to'g'ri layerga tegishliligi tekshiriladimi?",
            "explanation": (
                "Element assignment professional layer strukturasi uchun asosiy nazorat nuqtalaridan biridir."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L06_Q029",
            "question": "Viewda keraksiz helper layerlar ko'rinib qolishi professional hujjat sifatiga ta'sir qilishi mumkinmi?",
            "explanation": (
                "Layer visibility noto'g'ri bo'lsa Viewda keraksiz elementlar chiqishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L06_Q030",
            "question": "Layers bilan professional ishlashdagi to'g'ri workflow qaysi?",
            "explanation": (
                "Avval layer strukturasi tuziladi, elementlar to'g'ri biriktiriladi, kombinatsiyalar va Viewlar tekshiriladi."
            ),
            "options": [
                (
                    "A",
                    "Naming → element assignment → visibility → combinations → audit",
                    True,
                ),
                (
                    "B",
                    "Barcha elementni Layer 1 ga joylashtirish",
                    False,
                ),
            ],
        },
    ],
}


# ============================================================
# DATABASE SEED
# ============================================================

def seed_level06_module02():
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
        ) in LEVEL06_MODULE02_LESSONS:

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
