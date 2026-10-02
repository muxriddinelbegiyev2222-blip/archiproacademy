from database.database import get_connection


# ============================================================
# LEVEL 6
# MODULE 08 - RAILING
# ============================================================

LEVEL06_MODULE08_LESSONS = [
    (
        "L06_M08",
        "L06_M08_001",
        "Railing Tool asoslari",
        "theory",
        "Archicadda Railing Tool va to'siq tizimining asosiy komponentlarini tushunish.",
        1,
        40,
        20,
    ),
    (
        "L06_M08",
        "L06_M08_002",
        "Posts, Rails va Handrails",
        "theory",
        "Railing tizimidagi tayanch, gorizontal element va ushlagichlarning vazifasini tushunish.",
        2,
        45,
        20,
    ),
    (
        "L06_M08",
        "L06_M08_003",
        "Baluster va Panel tizimi",
        "practice",
        "Railing ichidagi vertikal elementlar va panel variantlarini boshqarish.",
        3,
        50,
        20,
    ),
    (
        "L06_M08",
        "L06_M08_004",
        "Stair va balkon bilan bog'lash",
        "practice",
        "Railingni zinapoya, landing, slab va balkon chetlari bilan mantiqiy bog'lash.",
        4,
        50,
        20,
    ),
    (
        "L06_M08",
        "L06_M08_005",
        "Railing professional audit",
        "practice",
        "Railing geometriyasi, komponentlari, bog'lanishi va 3D natijasini kompleks tekshirish.",
        5,
        55,
        25,
    ),
]


# ============================================================
# CONTENT
# ============================================================

LEVEL06_MODULE08_CONTENT = {
    "L06_M08_001": [
        {
            "title": "Railing Tool nima?",
            "type": "highlight",
            "text": """
            Railing Tool —
            zinapoya,
            balkon,
            terassa
            va boshqa ochiq chetlarda

            <br><br>

            to'siq tizimini
            BIM element sifatida
            yaratish uchun ishlatiladi.
            """,
        },
        {
            "title": "Railing — bitta obyekt emas",
            "type": "normal",
            "text": """
            Railingni faqat
            bitta tayyor obyekt
            sifatida tushunmang.

            <br><br>

            U bir nechta
            komponentlardan tashkil topgan
            tizim bo'lishi mumkin.
            """,
        },
        {
            "title": "Asosiy komponentlar",
            "type": "highlight",
            "text": """
            Railing tarkibida
            quyidagi elementlar
            uchrashi mumkin:

            <br><br>

            • Posts;<br>
            • Rails;<br>
            • Handrails;<br>
            • Balusters;<br>
            • Panels.
            """,
        },
        {
            "title": "Railing va arxitektura",
            "type": "normal",
            "text": """
            Railing faqat
            texnik xavfsizlik elementi emas.

            <br><br>

            U:

            <br><br>

            • interyerga;<br>
            • fasadga;<br>
            • zinapoya obraziga;<br>
            • balkon dizayniga

            <br><br>

            ta'sir qiladi.
            """,
        },
        {
            "title": "Tasavvur qiling",
            "type": "example",
            "text": """
            Zamonaviy zinapoya
            juda sodda va yengil.

            <br><br>

            Lekin unga
            juda og'ir,
            murakkab railing
            qo'yildi.

            <br><br>

            Texnik jihatdan
            model mavjud,

            <br><br>

            lekin arxitektura
            kompozitsiyasi
            bir-biriga mos emas.
            """,
        },
        {
            "title": "Avval vazifani aniqlang",
            "type": "warning",
            "text": """
            Railing yaratishdan oldin
            uning vazifasini aniqlang:

            <br><br>

            • Stair uchunmi?<br>
            • Landing uchunmi?<br>
            • Balcony uchunmi?<br>
            • Terrace uchunmi?

            <br><br>

            So'ng geometriyani
            tanlang.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Bitta Stairni oling.

            <br><br>

            Unda railing
            qayerdan boshlanishi,
            qayerda burilishi
            va qayerda tugashini
            aniqlang.

            <br><br>

            Hali detal yaratmang —
            faqat railing yo'lini
            tahlil qiling.
            """,
        },
    ],

    "L06_M08_002": [
        {
            "title": "Post nima?",
            "type": "highlight",
            "text": """
            Post —
            Railing tizimidagi
            asosiy vertikal
            tayanch elementlaridan biri.
            """,
        },
        {
            "title": "Rail nima?",
            "type": "normal",
            "text": """
            Rail —
            Railing bo'ylab
            davom etadigan
            gorizontal yoki
            qiya elementlardan biri.
            """,
        },
        {
            "title": "Handrail",
            "type": "normal",
            "text": """
            Handrail —
            odam zinapoyadan
            yurayotganda

            <br><br>

            qo'l bilan ushlashi
            uchun mo'ljallangan
            element.
            """,
        },
        {
            "title": "Bir xil emas",
            "type": "highlight",
            "text": """
            Rail va Handrail
            tashqi ko'rinishda
            o'xshash bo'lishi mumkin.

            <br><br>

            Lekin ularning
            tizimdagi vazifasi
            bir xil bo'lishi shart emas.
            """,
        },
        {
            "title": "Elementlarni ko'paytirib yubormang",
            "type": "warning",
            "text": """
            Railingga juda ko'p
            rail yoki post qo'shish

            <br><br>

            avtomatik ravishda
            yaxshi yechim degani emas.

            <br><br>

            Har bir element
            aniq vazifa bajarishi kerak.
            """,
        },
        {
            "title": "Ritmik tartib",
            "type": "normal",
            "text": """
            Posts va boshqa
            vertikal elementlar

            <br><br>

            vizual ritm yaratadi.

            <br><br>

            Ularning joylashuvi
            tasodifiy ko'rinmasligi kerak.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Bitta Railing yarating.

            <br><br>

            Unda alohida toping:

            • Post;<br>
            • Rail;<br>
            • Handrail.

            <br><br>

            Har birining vazifasini
            bir jumlada yozing.
            """,
        },
    ],

    "L06_M08_003": [
        {
            "title": "Baluster",
            "type": "highlight",
            "text": """
            Baluster —
            Railing ichidagi
            takrorlanuvchi vertikal
            elementlardan biri.
            """,
        },
        {
            "title": "Baluster ritmi",
            "type": "normal",
            "text": """
            Balusterlar
            railing bo'ylab

            <br><br>

            ma'lum tartibda
            takrorlanadi.

            <br><br>

            Bu ham texnik,
            ham vizual natijaga
            ta'sir qiladi.
            """,
        },
        {
            "title": "Panel",
            "type": "highlight",
            "text": """
            Ayrim railinglarda
            ko'p baluster o'rniga

            <br><br>

            panel tipidagi
            to'ldiruvchi element
            ishlatilishi mumkin.
            """,
        },
        {
            "title": "Baluster yoki Panel?",
            "type": "normal",
            "text": """
            Tanlov:

            <br><br>

            • arxitektura uslubi;<br>
            • konstruksiya;<br>
            • vizual yengillik;<br>
            • loyiha talabi

            <br><br>

            bilan bog'liq bo'lishi mumkin.
            """,
        },
        {
            "title": "Tasavvur qiling",
            "type": "example",
            "text": """
            Minimalistik interyerda
            juda ko'p dekorativ
            baluster ishlatildi.

            <br><br>

            Railing texnik jihatdan
            mavjud,

            <br><br>

            lekin umumiy
            interyer tiliga
            mos kelmasligi mumkin.
            """,
        },
        {
            "title": "Takrorlanish xatolari",
            "type": "warning",
            "text": """
            Balusterlar
            railing burchaklarida,
            boshlanishida
            yoki tugashida

            <br><br>

            noodatiy zichlashib
            yoki bo'shashib qolishi mumkin.

            <br><br>

            Bunday joylarni
            3Dda tekshiring.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Bir xil Stair uchun:

            <br><br>

            1. Balusterli Railing;<br>
            2. Panelli Railing

            <br><br>

            variantini yarating.

            <br><br>

            3Dda qaysi biri
            arxitektura g'oyasiga
            yaxshiroq mos kelishini
            tahlil qiling.
            """,
        },
    ],

    "L06_M08_004": [
        {
            "title": "Railing va Stair",
            "type": "highlight",
            "text": """
            Railing Stair bilan
            bog'langan holda
            ishlashi mumkin.

            <br><br>

            Stair geometriyasi
            o'zgarganda

            <br><br>

            Railing natijasini
            ham qayta tekshirish kerak.
            """,
        },
        {
            "title": "Flight bo'ylab",
            "type": "normal",
            "text": """
            Zinapoya marshida
            Railing qiya yo'nalishda
            Stair bilan birga
            ko'tariladi.
            """,
        },
        {
            "title": "Landingda",
            "type": "normal",
            "text": """
            Landing zonasida
            Railing geometriyasi
            qiya holatdan

            <br><br>

            gorizontal holatga
            o'tishi mumkin.

            <br><br>

            Aynan shu o'tish joylarini
            diqqat bilan tekshiring.
            """,
        },
        {
            "title": "Balkonda",
            "type": "highlight",
            "text": """
            Balcony Railing
            Stairga bog'liq bo'lmasligi mumkin.

            <br><br>

            U slab yoki
            balkon chetining
            geometriyasiga mos
            tashkil qilinadi.
            """,
        },
        {
            "title": "Chegarani to'g'ri o'qing",
            "type": "warning",
            "text": """
            Railing path
            noto'g'ri tanlansa

            <br><br>

            railing:

            • noto'g'ri tomonga chiqishi;<br>
            • balkon ichiga kirishi;<br>
            • bo'shliqni kesib o'tishi;<br>
            • Stairning noto'g'ri tomonida qolishi

            <br><br>

            mumkin.
            """,
        },
        {
            "title": "Stair o'zgarsa",
            "type": "example",
            "text": """
            Stair flight uzunligi
            yoki landing geometriyasi
            o'zgartirildi.

            <br><br>

            Railing avtomatik
            moslashgan bo'lsa ham,

            <br><br>

            natijani tekshirmasdan
            qoldirmang.
            """,
        },
        {
            "title": "Plan + 3D + Section",
            "type": "highlight",
            "text": """
            Railingni:

            <br><br>

            • Plan;<br>
            • 3D;<br>
            • Section/Elevation

            <br><br>

            ko'rinishlarida
            birgalikda tekshiring.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Bitta Stair va
            bitta Balcony yarating.

            <br><br>

            Har ikkalasiga
            Railing qo'ying.

            <br><br>

            Keyin Stair Railing
            va Balcony Railing
            orasidagi workflow
            farqini yozing.
            """,
        },
    ],

    "L06_M08_005": [
        {
            "title": "Railing professional audit",
            "type": "highlight",
            "text": """
            Endi Railingni
            faqat to'siq sifatida emas,

            <br><br>

            arxitektura,
            circulation
            va BIM tizimining
            bir qismi sifatida
            tekshiramiz.
            """,
        },
        {
            "title": "1. Path",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • railing qayerdan boshlanadi?<br>
            • qayerda buriladi?<br>
            • qayerda tugaydi?<br>
            • Stair yoki balkon chegarasiga mosmi?
            """,
        },
        {
            "title": "2. Posts",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • postlar mantiqiy joylashganmi?<br>
            • burchaklarda xato yo'qmi?<br>
            • takrorlanish ritmi tartiblimi?
            """,
        },
        {
            "title": "3. Rails va Handrails",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • elementlar uzluksizmi?<br>
            • flight va landing o'tishi to'g'rimi?<br>
            • ortiqcha rail yo'qmi?
            """,
        },
        {
            "title": "4. Baluster va Panel",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • baluster ritmi to'g'rimi?<br>
            • burchaklarda g'alati takrorlanish yo'qmi?<br>
            • panellar geometriyaga mosmi?
            """,
        },
        {
            "title": "5. Stair bilan bog'lanish",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • Railing Stairni to'g'ri kuzatyaptimi?<br>
            • landingda o'tish to'g'rimi?<br>
            • Stair o'zgargandan keyin Railing tekshirildimi?
            """,
        },
        {
            "title": "6. Balkon va ochiq chetlar",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • balkon cheti to'liq himoyalanganmi?<br>
            • Railing path chet geometriyasiga mosmi?<br>
            • ochiq qolgan tasodifiy zona yo'qmi?
            """,
        },
        {
            "title": "Aniq normativ qiymatlar",
            "type": "normal",
            "text": """
            Railing balandligi,
            elementlar oralig'i
            va boshqa aniq
            xavfsizlik parametrlarini

            <br><br>

            loyiha turiga mos
            amaldagi normativ hujjatlar
            asosida tekshirish kerak.

            <br><br>

            Bu modulda
            Archicad workflow
            va BIM mantig'ini
            o'rganamiz.
            """,
        },
        {
            "title": "Xatoni toping",
            "type": "warning",
            "text": """
            Stair va Railing
            3Dda mavjud.

            <br><br>

            Lekin:

            <br><br>

            • handrail landingda uzilib qolgan;<br>
            • burchakda ikkita post bir-biriga juda yaqin;<br>
            • Stairning bir tomonida Railing noto'g'ri yo'nalgan;<br>
            • balcony railing konturdan tashqariga chiqib ketgan.

            <br><br>

            Muammo:

            <br><br>

            Railing yaratilgan,
            lekin geometriya
            va komponentlar
            professional audit qilinmagan.
            """,
        },
        {
            "title": "Professional checklist",
            "type": "example",
            "text": """
            Railingni tekshiring:

            <br><br>

            <b>1.</b> Path to'g'rimi?<br><br>
            <b>2.</b> Posts tartiblimi?<br><br>
            <b>3.</b> Rails va Handrails to'g'rimi?<br><br>
            <b>4.</b> Baluster yoki Panels mantiqiymi?<br><br>
            <b>5.</b> Stair bilan bog'lanish to'g'rimi?<br><br>
            <b>6.</b> Balcony geometriyasiga mosmi?<br><br>
            <b>7.</b> Plan, Section va 3D tekshirildimi?
            """,
        },
        {
            "title": "Modul yakuni",
            "type": "highlight",
            "text": """
            Siz endi:

            <br><br>

            ✓ Railing Tool mantig'ini tushunasiz;<br>
            ✓ Post, Rail va Handrailni farqlaysiz;<br>
            ✓ Baluster va Panel tizimini tushunasiz;<br>
            ✓ Railingni Stair bilan bog'laysiz;<br>
            ✓ Balcony Railing yaratasiz;<br>
            ✓ 3D va Section orqali tekshirasiz;<br>
            ✓ professional Railing auditini bajarasiz.

            <br><br>

            Keyingi modul:
            <b>Mesh.</b>
            """,
        },
    ],
}


# ============================================================
# QUIZ
# Q106-Q120
# ============================================================

LEVEL06_MODULE08_QUIZ = {
    "L06_M08_001": [
        {
            "code": "L06_Q106",
            "question": "Railing Tool zinapoya va balkon to'siqlarini BIM element sifatida yaratish uchun ishlatiladimi?",
            "explanation": (
                "Railing Tool Stair, balkon va boshqa chetlarda to'siq tizimi yaratishga yordam beradi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L06_Q107",
            "question": "Railing faqat bitta oddiy obyekt bo'lishi shartmi?",
            "explanation": (
                "Railing bir nechta komponentlardan tashkil topgan tizim bo'lishi mumkin."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L06_Q108",
            "question": "Railing arxitektura ko'rinishiga ham ta'sir qiladimi?",
            "explanation": (
                "Railing interyer, fasad, Stair va balkon obrazining muhim qismi bo'lishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L06_M08_002": [
        {
            "code": "L06_Q109",
            "question": "Post Railing tizimidagi vertikal tayanch elementlardan biri bo'lishi mumkinmi?",
            "explanation": (
                "Post Railingning asosiy vertikal tayanch komponentlaridan biri."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L06_Q110",
            "question": "Handrail odam qo'l bilan ushlashi uchun ishlatiladigan element bo'lishi mumkinmi?",
            "explanation": (
                "Handrail Stair bo'ylab ushlash vazifasini bajaradigan komponentdir."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L06_Q111",
            "question": "Railingga imkon qadar ko'p Rail va Post qo'shish har doim yaxshi yechimmi?",
            "explanation": (
                "Har bir komponent aniq vazifa bajarishi kerak; ortiqcha elementlar model va dizaynni murakkablashtirishi mumkin."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
    ],

    "L06_M08_003": [
        {
            "code": "L06_Q112",
            "question": "Baluster Railing ichidagi takrorlanuvchi vertikal element bo'lishi mumkinmi?",
            "explanation": (
                "Balusterlar Railing bo'ylab takrorlanadigan vertikal komponentlar sifatida ishlatilishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L06_Q113",
            "question": "Railingda Panel balusterlarga alternativ to'ldiruvchi yechim bo'lishi mumkinmi?",
            "explanation": (
                "Ayrim Railing tizimlarida panel tipidagi to'ldiruvchi elementlardan foydalanish mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L06_Q114",
            "question": "Balusterlarning burchak va tugash joylaridagi takrorlanishini 3Dda tekshirish foydalimi?",
            "explanation": (
                "Takrorlanish qoidalari burchaklarda kutilmagan geometriya berishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L06_M08_004": [
        {
            "code": "L06_Q115",
            "question": "Stair geometriyasi o'zgarsa unga bog'langan Railingni ham tekshirish kerakmi?",
            "explanation": (
                "Stair o'zgarishi Railingning flight, landing va tugash geometriyasiga ta'sir qilishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L06_Q116",
            "question": "Balcony Railing balkon cheti geometriyasiga mos bo'lishi kerakmi?",
            "explanation": (
                "Railing path balkon yoki ochiq chet konturini mantiqan kuzatishi kerak."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L06_Q117",
            "question": "Railingni faqat Plan'da tekshirish yetarlimi?",
            "explanation": (
                "Plan, Section/Elevation va 3D turli geometriya xatolarini ko'rsatadi."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
    ],

    "L06_M08_005": [
        {
            "code": "L06_Q118",
            "question": "Railing auditida path, posts va rail komponentlari tekshiriladimi?",
            "explanation": (
                "Railingning yo'li va komponentlari professional auditning asosiy qismlaridir."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L06_Q119",
            "question": "Railing 3Dda ko'rinsa uning Stair yoki balkon bilan bog'lanishini tekshirmasa ham bo'ladimi?",
            "explanation": (
                "Railing geometriyasi asosiy element bilan to'g'ri bog'langanini alohida tekshirish kerak."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L06_Q120",
            "question": "Railing bilan professional ishlashdagi to'g'ri workflow qaysi?",
            "explanation": (
                "Avval Railing yo'li aniqlanadi, so'ng komponentlar sozlanadi va Stair/balkon bilan bog'lanishi tekshiriladi."
            ),
            "options": [
                (
                    "A",
                    "Path → komponentlar → Stair/Balcony aloqasi → Plan/Section/3D audit",
                    True,
                ),
                (
                    "B",
                    "Tasodifiy Railing presetini qo'yib tekshirmaslik",
                    False,
                ),
            ],
        },
    ],
}


# ============================================================
# DATABASE SEED
# ============================================================

def seed_level06_module08():
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
        ) in LEVEL06_MODULE08_LESSONS:

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
