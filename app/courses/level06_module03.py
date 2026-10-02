from database.database import get_connection


# ============================================================
# LEVEL 6
# MODULE 03 - BUILDING MATERIALS
# ============================================================

LEVEL06_MODULE03_LESSONS = [
    (
        "L06_M03",
        "L06_M03_001",
        "Building Material tushunchasi",
        "theory",
        "Archicaddagi Building Material tushunchasi va uning BIM modeldagi rolini tushunish.",
        1,
        40,
        20,
    ),
    (
        "L06_M03",
        "L06_M03_002",
        "Building Material va Surface farqi",
        "theory",
        "Element materiali va tashqi ko'rinish tushunchalarini bir-biridan farqlash.",
        2,
        45,
        20,
    ),
    (
        "L06_M03",
        "L06_M03_003",
        "Cut Fill va kesim ko'rinishi",
        "practice",
        "Building Materialning plan va kesimdagi grafik ifodasini tushunish.",
        3,
        50,
        20,
    ),
    (
        "L06_M03",
        "L06_M03_004",
        "Intersection Priority va model tutashuvi",
        "practice",
        "Materiallarning element tutashuviga ta'siri va priority mantig'ini tushunish.",
        4,
        50,
        20,
    ),
    (
        "L06_M03",
        "L06_M03_005",
        "Building Materials professional audit",
        "practice",
        "Loyihadagi material nomlari, grafikasi, priority va elementlarga biriktirilishini tekshirish.",
        5,
        55,
        25,
    ),
]


# ============================================================
# CONTENT
# ============================================================

LEVEL06_MODULE03_CONTENT = {
    "L06_M03_001": [
        {
            "title": "Building Material nima?",
            "type": "highlight",
            "text": """
            Building Material —
            Archicadda elementning
            qurilish materiali haqida
            BIM ma'lumot saqlashga
            xizmat qiladigan tushuncha.

            <br><br>

            Masalan:

            <br><br>

            • beton;<br>
            • g'isht;<br>
            • yog'och;<br>
            • issiqlik izolyatsiyasi;<br>
            • boshqa qurilish materiallari.
            """,
        },
        {
            "title": "Bu faqat rang emas",
            "type": "normal",
            "text": """
            Building Materialni
            oddiy rang yoki tekstura
            sifatida tushunish xato.

            <br><br>

            U modelning
            konstruktiv va grafik
            xususiyatlari bilan ham
            bog'liq bo'lishi mumkin.
            """,
        },
        {
            "title": "BIM fikrlash",
            "type": "highlight",
            "text": """
            Oddiy 3D modelda
            element faqat shakl bo'lishi mumkin.

            <br><br>

            BIM modelda esa
            elementning materiali
            ham ma'lumot sifatida
            boshqariladi.
            """,
        },
        {
            "title": "Tasavvur qiling",
            "type": "example",
            "text": """
            Ikki devor tashqi ko'rinishda
            bir xil.

            <br><br>

            Lekin biri beton,
            ikkinchisi g'isht.

            <br><br>

            Professional BIM modelda
            bu farq faqat nomda emas,
            material ma'lumotida ham
            aks etishi kerak.
            """,
        },
        {
            "title": "Qayerlarda ishlatiladi?",
            "type": "normal",
            "text": """
            Building Material
            turli model elementlarida
            ishlatilishi mumkin.

            <br><br>

            Masalan:

            <br><br>

            • Wall;<br>
            • Slab;<br>
            • Roof;<br>
            • Column;<br>
            • Beam;<br>
            • boshqa konstruktiv elementlar.
            """,
        },
        {
            "title": "Material nomlash",
            "type": "warning",
            "text": """
            Materiallarni:

            <br><br>

            Material 1<br>
            Material New<br>
            Test

            <br><br>

            kabi tasodifiy nomlash
            professional workflow emas.

            <br><br>

            Nom materialning
            mazmunini tushunarli
            ko'rsatishi kerak.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Kichik uy uchun
            kamida 5 ta
            Building Material ro'yxatini tuzing.

            <br><br>

            Masalan:

            • reinforced concrete;<br>
            • brick;<br>
            • insulation;<br>
            • wood;<br>
            • screed.

            <br><br>

            Har birini
            qayerda ishlatishingizni yozing.
            """,
        },
    ],

    "L06_M03_002": [
        {
            "title": "Building Material va Surface",
            "type": "highlight",
            "text": """
            Building Material
            va Surface
            bir xil tushuncha emas.

            <br><br>

            Bu farqni tushunish
            Archicadda juda muhim.
            """,
        },
        {
            "title": "Building Material",
            "type": "normal",
            "text": """
            Building Material
            elementning qurilish
            materialiga tegishli
            BIM xususiyatini ifodalaydi.
            """,
        },
        {
            "title": "Surface",
            "type": "normal",
            "text": """
            Surface esa
            elementning ko'rinadigan
            tashqi yuzasining

            <br><br>

            vizual ko'rinishi bilan
            ko'proq bog'liq.
            """,
        },
        {
            "title": "Oddiy misol",
            "type": "example",
            "text": """
            Devorning asosiy materiali —
            g'isht.

            <br><br>

            Lekin tashqi yuza
            dekorativ plaster
            ko'rinishida bo'lishi mumkin.

            <br><br>

            Demak:

            <br><br>

            konstruktiv material
            va ko'rinadigan surface
            bir xil narsa emas.
            """,
        },
        {
            "title": "3D ko'rinishga aldanmang",
            "type": "warning",
            "text": """
            Element 3Dda
            chiroyli tekstura bilan
            ko'rinishi

            <br><br>

            uning Building Materiali
            to'g'ri berilganini
            anglatmaydi.
            """,
        },
        {
            "title": "BIM modelning maqsadi",
            "type": "highlight",
            "text": """
            Professional modelda
            tashqi ko'rinish
            va material ma'lumoti

            <br><br>

            bir-biriga mos
            va tushunarli bo'lishi kerak.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Bitta devorni tasavvur qiling.

            <br><br>

            Yozing:

            Building Material:
            __________

            <br><br>

            Exterior Surface:
            __________

            <br><br>

            Interior Surface:
            __________

            <br><br>

            Uchtasining vazifasini
            alohida tushuntiring.
            """,
        },
    ],

    "L06_M03_003": [
        {
            "title": "Cut Fill nima?",
            "type": "highlight",
            "text": """
            Model elementi
            kesimda yoki planda
            kesilganda

            <br><br>

            uning materiali
            grafik pattern bilan
            ifodalanishi mumkin.

            <br><br>

            Bu Cut Fill
            tushunchasi bilan bog'liq.
            """,
        },
        {
            "title": "Materialni chizmada o'qish",
            "type": "normal",
            "text": """
            Professional chizmada
            turli materiallarni
            grafik jihatdan farqlash

            <br><br>

            modelni va hujjatni
            tushunishni osonlashtiradi.
            """,
        },
        {
            "title": "Section misoli",
            "type": "example",
            "text": """
            Sectionda:

            <br><br>

            beton devor
            bir grafik fill bilan,

            <br><br>

            izolyatsiya esa
            boshqa grafik fill bilan
            ko'rsatilishi mumkin.

            <br><br>

            Bu material qatlamlarini
            o'qishni osonlashtiradi.
            """,
        },
        {
            "title": "Tasodifiy Fill ishlatmang",
            "type": "warning",
            "text": """
            Har bir materialga
            tasodifiy grafik pattern
            berish

            <br><br>

            loyiha hujjatini
            chalkashtirishi mumkin.
            """,
        },
        {
            "title": "Model va Documentation aloqasi",
            "type": "highlight",
            "text": """
            Yaxshi BIM workflowda
            modeldagi material ma'lumoti

            <br><br>

            chizma grafikasi bilan
            mantiqiy bog'langan bo'ladi.
            """,
        },
        {
            "title": "Plan va Sectionni tekshiring",
            "type": "normal",
            "text": """
            Building Material yaratgandan
            yoki o'zgartirgandan so'ng

            <br><br>

            uni faqat 3Dda emas,

            <br><br>

            Plan va Sectionda
            ham tekshirish foydali.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Ikki xil materialli
            ikki element yarating.

            <br><br>

            Keyin:

            • Floor Plan;<br>
            • Section;<br>
            • 3D

            <br><br>

            ko'rinishlarida
            farqini tahlil qiling.
            """,
        },
    ],

    "L06_M03_004": [
        {
            "title": "Intersection Priority",
            "type": "highlight",
            "text": """
            Building Material
            model elementlari
            bir-biriga tutashganda

            <br><br>

            ularning qanday
            kesishishini boshqarishda
            ham rol o'ynashi mumkin.
            """,
        },
        {
            "title": "Priority mantig'i",
            "type": "normal",
            "text": """
            Materiallar
            turli kuchdagi
            intersection priorityga
            ega bo'lishi mumkin.

            <br><br>

            Bu tutashuvdagi
            qaysi material ustun
            ishlashiga ta'sir qiladi.
            """,
        },
        {
            "title": "Tasavvur qiling",
            "type": "example",
            "text": """
            Beton element
            issiqlik izolyatsiyasi
            bilan tutashdi.

            <br><br>

            Modeldagi priority
            noto'g'ri bo'lsa,

            <br><br>

            Sectiondagi tutashuv
            kutilmagan ko'rinish
            berishi mumkin.
            """,
        },
        {
            "title": "Faqat 3D shaklga qaramang",
            "type": "warning",
            "text": """
            Elementlar 3Dda
            bir-biriga tegib turgani

            <br><br>

            ularning BIM tutashuvi
            to'g'ri degani emas.
            """,
        },
        {
            "title": "Composite bilan aloqa",
            "type": "highlight",
            "text": """
            Keyingi modulda
            Composite Structures
            bilan ishlaganda

            <br><br>

            Building Material
            yanada muhimlashadi.

            <br><br>

            Chunki composite
            bir nechta material qatlamidan
            tashkil topishi mumkin.
            """,
        },
        {
            "title": "Muammo bo'lsa",
            "type": "normal",
            "text": """
            Noto'g'ri tutashuvni ko'rsangiz:

            <br><br>

            faqat element geometriyasini
            o'zgartirishga shoshilmang.

            <br><br>

            Material priority
            va element strukturasini
            ham tekshiring.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Ikki xil materialli
            element tutashuvini yarating.

            <br><br>

            Sectionda ko'ring.

            <br><br>

            Keyin material
            priority mantig'ini
            tahlil qiling.
            """,
        },
    ],

    "L06_M03_005": [
        {
            "title": "Building Materials audit",
            "type": "highlight",
            "text": """
            Endi Building Materials
            tizimini

            <br><br>

            faqat materiallar ro'yxati
            sifatida emas,

            <br><br>

            BIM modelning
            muhim ma'lumot qatlami
            sifatida tekshiramiz.
            """,
        },
        {
            "title": "1. Naming",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • material nomlari tushunarlimi?<br>
            • takroriy materiallar ko'p emasmi?<br>
            • Test, New Material kabi nomlar qolmaganmi?
            """,
        },
        {
            "title": "2. Element assignment",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • beton elementga beton material berilganmi?<br>
            • g'isht devor to'g'ri materialdami?<br>
            • slab va roof materiallari mantiqiymi?
            """,
        },
        {
            "title": "3. Cut Fill",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • Sectionda materiallar farqlanadimi?<br>
            • filllar tushunarlimi?<br>
            • tasodifiy grafik patternlar yo'qmi?
            """,
        },
        {
            "title": "4. Surface bilan aloqa",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • Building Material va Surface chalkashmaganmi?<br>
            • tashqi ko'rinish material ma'nosiga zid emasmi?
            """,
        },
        {
            "title": "5. Priority",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • element tutashuvlari to'g'rimi?<br>
            • kesimlarda materiallar noto'g'ri yutilib ketmaganmi?<br>
            • priority mantiqi ishlayaptimi?
            """,
        },
        {
            "title": "Xatoni toping",
            "type": "warning",
            "text": """
            Uy modeli 3Dda
            juda chiroyli.

            <br><br>

            Lekin:

            <br><br>

            • barcha devorlarga bir xil Building Material berilgan;<br>
            • beton va g'isht kesimda bir xil ko'rinadi;<br>
            • Surface to'g'ri, lekin material ma'lumoti noto'g'ri;<br>
            • element tutashuvlari priority sabab buzilgan.

            <br><br>

            Muammo:

            <br><br>

            model vizual jihatdan yaxshi,
            lekin BIM materiali
            professional boshqarilmagan.
            """,
        },
        {
            "title": "Professional checklist",
            "type": "example",
            "text": """
            Building Materialsni tekshiring:

            <br><br>

            <b>1.</b> Naming izchilmi?<br><br>
            <b>2.</b> Materiallar to'g'ri elementga biriktirilganmi?<br><br>
            <b>3.</b> Cut Filllar tushunarlimi?<br><br>
            <b>4.</b> Surface bilan farq tushunarlimi?<br><br>
            <b>5.</b> Intersection priority to'g'rimi?<br><br>
            <b>6.</b> Plan va Section yaxshi ishlayaptimi?<br><br>
            <b>7.</b> Takroriy va keraksiz materiallar yo'qmi?
            """,
        },
        {
            "title": "Modul yakuni",
            "type": "highlight",
            "text": """
            Siz endi:

            <br><br>

            ✓ Building Material tushunchasini bilasiz;<br>
            ✓ uni Surface'dan farqlaysiz;<br>
            ✓ Cut Fill mantig'ini tushunasiz;<br>
            ✓ material priority haqida bilasiz;<br>
            ✓ element tutashuvlarini tahlil qilasiz;<br>
            ✓ BIM material strukturasini boshqarasiz;<br>
            ✓ material auditini bajarasiz.

            <br><br>

            Keyingi modul:
            <b>Composite Structures.</b>
            """,
        },
    ],
}


# ============================================================
# QUIZ
# Q031-Q045
# ============================================================

LEVEL06_MODULE03_QUIZ = {
    "L06_M03_001": [
        {
            "code": "L06_Q031",
            "question": "Building Material Archicadda faqat rang vazifasini bajaradimi?",
            "explanation": (
                "Building Material BIM material ma'lumoti va boshqa model xususiyatlari bilan bog'liq."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L06_Q032",
            "question": "Building Material devor, slab va boshqa model elementlarida ishlatilishi mumkinmi?",
            "explanation": (
                "Building Material turli konstruktiv model elementlariga biriktirilishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L06_Q033",
            "question": "Material nomlarini tushunarli yuritish professional BIM workflow uchun foydalimi?",
            "explanation": (
                "Tushunarli naming modelni boshqarish va audit qilishni osonlashtiradi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L06_M03_002": [
        {
            "code": "L06_Q034",
            "question": "Building Material va Surface aynan bir xil tushunchami?",
            "explanation": (
                "Building Material BIM material xususiyatiga, Surface esa ko'rinadigan yuzaning vizual ifodasiga ko'proq bog'liq."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L06_Q035",
            "question": "Element 3Dda chiroyli teksturaga ega bo'lsa Building Material ham avtomatik to'g'ri bo'ladimi?",
            "explanation": (
                "Surface to'g'ri ko'rinsa ham Building Material noto'g'ri bo'lishi mumkin."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L06_Q036",
            "question": "Bir elementning Building Materiali va Surface'i turli maqsadlarni bajarishi mumkinmi?",
            "explanation": (
                "Ular BIM materiali va vizual yuzani alohida boshqarishga xizmat qiladi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L06_M03_003": [
        {
            "code": "L06_Q037",
            "question": "Cut Fill materialning kesimdagi grafik ifodasiga yordam beradimi?",
            "explanation": (
                "Cut Fill element kesilganda materialni grafik tarzda ifodalashda ishlatiladi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L06_Q038",
            "question": "Turli materiallarni Sectionda grafik jihatdan farqlash foydalimi?",
            "explanation": (
                "Bu konstruksiya va material qatlamlarini tushunishni osonlashtiradi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L06_Q039",
            "question": "Building Materialni faqat 3Dda tekshirish yetarlimi?",
            "explanation": (
                "Plan va Sectiondagi grafik natijani ham tekshirish kerak."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
    ],

    "L06_M03_004": [
        {
            "code": "L06_Q040",
            "question": "Building Material priority elementlarning tutashuviga ta'sir qilishi mumkinmi?",
            "explanation": (
                "Material priority kesishuvchi elementlarning bir-biriga qanday tutashishiga ta'sir qilishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L06_Q041",
            "question": "Noto'g'ri tutashuv ko'rilganda faqat geometriyani o'zgartirish kerakmi?",
            "explanation": (
                "Material priority va element strukturasi ham tekshirilishi kerak."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L06_Q042",
            "question": "Composite Structures Building Materials bilan bog'liq bo'lishi mumkinmi?",
            "explanation": (
                "Composite bir nechta qatlamdan tuziladi va qatlamlarda Building Material ishlatilishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L06_M03_005": [
        {
            "code": "L06_Q043",
            "question": "Building Materials auditida materiallarning to'g'ri elementga biriktirilishi tekshiriladimi?",
            "explanation": (
                "Element assignment BIM modelning material aniqligi uchun muhim."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L06_Q044",
            "question": "3D model chiroyli bo'lsa material auditini o'tkazmasa ham bo'ladimi?",
            "explanation": (
                "Vizual sifat BIM material ma'lumoti to'g'ri ekanini kafolatlamaydi."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L06_Q045",
            "question": "Building Materials bilan professional ishlashdagi to'g'ri workflow qaysi?",
            "explanation": (
                "Material aniqlanadi, elementlarga beriladi, grafik va priority natijalari tekshiriladi."
            ),
            "options": [
                (
                    "A",
                    "Naming → assignment → Cut Fill → priority → audit",
                    True,
                ),
                (
                    "B",
                    "Faqat 3D tekstura tanlash",
                    False,
                ),
            ],
        },
    ],
}


# ============================================================
# DATABASE SEED
# ============================================================

def seed_level06_module03():
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
        ) in LEVEL06_MODULE03_LESSONS:

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
