from database.database import get_connection


# ============================================================
# LEVEL 5
# MODULE 06 - COLUMN VA BEAM
# ============================================================

LEVEL05_MODULE06_LESSONS = [
    (
        "L05_M06",
        "L05_M06_001",
        "Column Tool asoslari",
        "theory",
        "Archicadda ustun yaratish va uning asosiy parametrlarini tushunish.",
        1,
        40,
        20,
    ),
    (
        "L05_M06",
        "L05_M06_002",
        "Column joylashtirish",
        "practice",
        "Ustunlarni aniq nuqtalarda va mantiqiy tizim asosida joylashtirish.",
        2,
        45,
        20,
    ),
    (
        "L05_M06",
        "L05_M06_003",
        "Beam Tool asoslari",
        "theory",
        "Beam elementini yaratish va uning asosiy parametrlarini tushunish.",
        3,
        45,
        20,
    ),
    (
        "L05_M06",
        "L05_M06_004",
        "Column va Beam aloqasi",
        "practice",
        "Ustun va beam elementlarini yagona konstruktiv mantiqda bog'lash.",
        4,
        50,
        20,
    ),
    (
        "L05_M06",
        "L05_M06_005",
        "Column va Beam mini-loyiha",
        "practice",
        "Oddiy uy modelida ustun va beamlarni joylashtirish va 3Dda tekshirish.",
        5,
        60,
        25,
    ),
]


# ============================================================
# CONTENT
# ============================================================

LEVEL05_MODULE06_CONTENT = {
    "L05_M06_001": [
        {
            "title": "Column Tool nima?",
            "type": "highlight",
            "text": """
            Column Tool
            vertikal BIM elementlarini
            yaratish uchun ishlatiladi.

            <br><br>

            Ustun faqat plandagi
            to'rtburchak belgi emas.

            <br><br>

            U balandlik,
            kesim va joylashuvga ega
            3D element.
            """,
        },
        {
            "title": "Column parametrlarini tekshiring",
            "type": "normal",
            "text": """
            Column yaratishdan oldin:

            <br><br>

            • balandlik;<br>
            • kesim;<br>
            • qavat;<br>
            • joylashuv nuqtasi

            <br><br>

            kabi parametrlarni tekshiring.
            """,
        },
        {
            "title": "Reference nuqta",
            "type": "normal",
            "text": """
            Columnni aniq joylashtirishda
            uning reference nuqtasi
            muhim bo'lishi mumkin.

            <br><br>

            Ustunni ko'z bilan
            taxminiy markazga qo'ymang.
            """,
        },
        {
            "title": "Tasavvur qiling",
            "type": "example",
            "text": """
            Ayvon uchun 4 ta ustun kerak.

            <br><br>

            O'quvchi ularni
            ko'z bilan teng masofaga qo'ydi.

            <br><br>

            3D chiroyli ko'rinadi,
            lekin planda ular
            aniq bir o'qda emas.

            <br><br>

            Bu professional model emas.
            """,
        },
        {
            "title": "2D va 3D",
            "type": "highlight",
            "text": """
            Columnni:

            <br><br>

            <b>PLAN + 3D + SECTION</b>

            <br><br>

            orqali tekshiring.

            <br><br>

            Har bir ko'rinish
            boshqa turdagi xatoni ko'rsatadi.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            1. Column Toolni tanlang.<br><br>
            2. Bitta ustun yarating.<br><br>
            3. Kesimini o'zgartiring.<br><br>
            4. Balandligini tekshiring.<br><br>
            5. 3Dda ko'ring.
            """,
        },
    ],

    "L05_M06_002": [
        {
            "title": "Ustun joyi tasodifiy bo'lmaydi",
            "type": "highlight",
            "text": """
            Column joylashtirishda
            arxitektura va konstruktiv
            mantiq birga ko'riladi.

            <br><br>

            Ustun faqat bo'sh joy topilgan
            nuqtaga qo'yilmaydi.
            """,
        },
        {
            "title": "O'qlar bilan fikrlash",
            "type": "normal",
            "text": """
            Ustunlar ko'pincha
            ma'lum o'qlar va
            tartib asosida joylashtiriladi.

            <br><br>

            Bu modelni tushunarli
            va boshqariladigan qiladi.
            """,
        },
        {
            "title": "Ayvon misoli",
            "type": "example",
            "text": """
            Ayvonda 4 ta ustun bor.

            <br><br>

            Ular:

            <br><br>

            • bir chiziqda;<br>
            • bir xil ritmda;<br>
            • ayvon geometriyasiga mos

            <br><br>

            bo'lishi kerak.
            """,
        },
        {
            "title": "Ustun va devor",
            "type": "normal",
            "text": """
            Column devor bilan
            yonma-yon yoki ichida
            ishlashi mumkin.

            <br><br>

            Bunday joylarda
            plan va 3D aloqani tekshirish kerak.
            """,
        },
        {
            "title": "Mebel va circulation",
            "type": "warning",
            "text": """
            Konstruktiv element
            xona funksiyasini buzmasligi kerak.

            <br><br>

            Masalan:

            <br><br>

            ustun eshik oldida,
            koridor markazida
            yoki mebelning asosiy joyida
            qolib ketmasligi kerak.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            4 ta Column yarating.

            <br><br>

            Ularni:

            <br><br>

            • bir o'qda;<br>
            • teng ritmda;<br>
            • ayvon chegarasiga mos

            <br><br>

            joylashtiring.

            <br><br>

            Keyin 3Dda tekshiring.
            """,
        },
    ],

    "L05_M06_003": [
        {
            "title": "Beam Tool nima?",
            "type": "highlight",
            "text": """
            Beam Tool
            gorizontal yoki
            ma'lum yo'nalishdagi
            konstruktiv elementlarni
            modellashtirish uchun ishlatiladi.

            <br><br>

            Turar joy modelida
            beam yoki rigel sifatida
            foydalanilishi mumkin.
            """,
        },
        {
            "title": "Beam parametrlari",
            "type": "normal",
            "text": """
            Beam yaratishda:

            <br><br>

            • kesim;<br>
            • balandlik;<br>
            • elevation;<br>
            • boshlanish va tugash nuqtasi

            <br><br>

            nazorat qilinadi.
            """,
        },
        {
            "title": "Beam faqat chiziq emas",
            "type": "highlight",
            "text": """
            Floor Planda beam
            chiziqqa o'xshashi mumkin.

            <br><br>

            Lekin 3Dda
            u real hajmga ega element.
            """,
        },
        {
            "title": "Ustundan ustungacha",
            "type": "example",
            "text": """
            Ikki Column orasiga
            Beam joylashtirilmoqda.

            <br><br>

            Beamning boshlanish
            va tugash nuqtalari
            ustunlar bilan
            mantiqan bog'lanishi kerak.
            """,
        },
        {
            "title": "Elevation xatosi",
            "type": "warning",
            "text": """
            Planda beam
            ustunlar orasida to'g'ri.

            <br><br>

            Lekin 3Dda u
            ustunlarning o'rtasidan o'tib ketgan.

            <br><br>

            Sabab:
            vertikal joylashuv tekshirilmagan.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            1. Ikki Column yarating.<br><br>
            2. Beam Toolni tanlang.<br><br>
            3. Ikki ustun orasiga beam yarating.<br><br>
            4. 3Dga o'ting.<br><br>
            5. Vertikal joylashuvni tekshiring.
            """,
        },
    ],

    "L05_M06_004": [
        {
            "title": "Column va Beam tizim sifatida ishlaydi",
            "type": "highlight",
            "text": """
            Ustun va beamni
            alohida-alohida element sifatida
            emas,

            <br><br>

            yagona tizim sifatida
            ko'rish muhim.
            """,
        },
        {
            "title": "O'q mosligi",
            "type": "normal",
            "text": """
            Beam va Columnlar
            bir-biriga yaqin turishi yetarli emas.

            <br><br>

            Ularning markaziy
            yoki reference aloqasi
            mantiqan to'g'ri bo'lishi kerak.
            """,
        },
        {
            "title": "Plan nazorati",
            "type": "normal",
            "text": """
            Floor Planda tekshiring:

            <br><br>

            • beam qaysi ustunlarga ulangan;<br>
            • ustunlar bir o'qdami;<br>
            • tasodifiy siljish bormi.
            """,
        },
        {
            "title": "3D nazorati",
            "type": "normal",
            "text": """
            3Dda tekshiring:

            <br><br>

            • beam balandligi;<br>
            • beam va column tutashuvi;<br>
            • noto'g'ri kesishmalar;<br>
            • modelning umumiy tartibi.
            """,
        },
        {
            "title": "Section nazorati",
            "type": "example",
            "text": """
            Section oching.

            <br><br>

            Columnning
            pol va yuqori konstruksiyaga
            nisbatan balandligini kuzating.

            <br><br>

            Beamning qaysi sathda
            joylashganini ham tekshiring.
            """,
        },
        {
            "title": "Tipik xato",
            "type": "warning",
            "text": """
            Columnlar bir o'qda.

            <br><br>

            Lekin Beam
            ulardan 10 sm yon tomonda.

            <br><br>

            3D uzoqdan qaraganda
            bilinmaydi.

            <br><br>

            Yaqin tekshiruvda
            ulanish xatosi ko'rinadi.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            4 ta Column va
            3 ta Beamdan iborat
            oddiy tizim yarating.

            <br><br>

            Plan,
            3D
            va Sectionda tekshiring.
            """,
        },
    ],

    "L05_M06_005": [
        {
            "title": "Column va Beam mini-loyiha",
            "type": "highlight",
            "text": """
            Endi kichik uy modelida
            ustun va beamlarni
            real arxitektura vazifasi bilan
            qo'llaymiz.
            """,
        },
        {
            "title": "Vazifa",
            "type": "example",
            "text": """
            Uyda hovliga qaragan
            yopiq ayvon bor.

            <br><br>

            Ayvon oldida:

            <br><br>

            • 4 ta Column;<br>
            • ularni bog'lovchi Beam

            <br><br>

            yarating.
            """,
        },
        {
            "title": "1-bosqich — Columnlar",
            "type": "normal",
            "text": """
            Avval 4 ta ustunni
            bir xil ritmda joylashtiring.

            <br><br>

            Plan bo'yicha
            bir o'qda ekanini tekshiring.
            """,
        },
        {
            "title": "2-bosqich — Beam",
            "type": "normal",
            "text": """
            Columnlar orasiga
            Beamlarni joylashtiring.

            <br><br>

            Boshlanish va tugash
            nuqtalarini aniq tutashtiring.
            """,
        },
        {
            "title": "3-bosqich — 3D",
            "type": "normal",
            "text": """
            3Dda tekshiring:

            <br><br>

            • barcha Columnlar bir xilmi;<br>
            • beamlar to'g'ri sathdami;<br>
            • elementlar bir-biriga ulanganmi;<br>
            • ayvon kompozitsiyasi tartiblimi.
            """,
        },
        {
            "title": "4-bosqich — Section",
            "type": "normal",
            "text": """
            Sectionda:

            <br><br>

            Column balandligi
            va Beam elevationini
            tekshiring.
            """,
        },
        {
            "title": "5-bosqich — arxitektura nazorati",
            "type": "normal",
            "text": """
            Faqat konstruktiv ko'rinishga qaramang.

            <br><br>

            Ustunlar:

            <br><br>

            • kirishni to'smayaptimi;<br>
            • oynalarni yopmayaptimi;<br>
            • circulationni buzmayaptimi;<br>
            • fasad ritmiga mosmi

            <br><br>

            deb tekshiring.
            """,
        },
        {
            "title": "Xatoni toping",
            "type": "warning",
            "text": """
            Ayvondagi 4 ta ustun
            tashqi ko'rinishda
            deyarli teng masofada.

            <br><br>

            Lekin plan o'lchaganda
            ularning intervali har xil.

            <br><br>

            Sabab:
            ko'z bilan joylashtirilgan.
            """,
        },
        {
            "title": "Professional checklist",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            <b>1.</b> Column kesimi to'g'rimi?<br><br>
            <b>2.</b> Columnlar aniq joylashganmi?<br><br>
            <b>3.</b> Beam kesimi to'g'rimi?<br><br>
            <b>4.</b> Beam elevation to'g'rimi?<br><br>
            <b>5.</b> Beam va Column tutashganmi?<br><br>
            <b>6.</b> Plan va 3D tekshirildimi?<br><br>
            <b>7.</b> Arxitektura bilan konflikt yo'qmi?
            """,
        },
        {
            "title": "Modul yakuni",
            "type": "highlight",
            "text": """
            Siz endi:

            <br><br>

            ✓ Column Toolni tushunasiz;<br>
            ✓ ustunlarni aniq joylashtirasiz;<br>
            ✓ Beam Toolni tushunasiz;<br>
            ✓ beam balandligini boshqarasiz;<br>
            ✓ Column va Beamni bog'laysiz;<br>
            ✓ Plan, 3D va Sectionda tekshirasiz.

            <br><br>

            Keyingi modul:
            <b>Object Tool.</b>
            """,
        },
    ],
}


# ============================================================
# QUIZ
# ============================================================

LEVEL05_MODULE06_QUIZ = {
    "L05_M06_001": [
        {
            "code": "L05_Q076",
            "question": "Column Archicadda 3D BIM elementi hisoblanadimi?",
            "explanation": (
                "Column balandlik, kesim va joylashuv parametrlariga ega."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L05_Q077",
            "question": "Columnni faqat ko'z bilan taxminiy joylashtirish professional usulmi?",
            "explanation": (
                "Ustun joylashuvi aniq nuqta va tizim asosida nazorat qilinadi."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L05_Q078",
            "question": "Columnni 3D va Sectionda tekshirish foydalimi?",
            "explanation": (
                "Bu balandlik va vertikal joylashuvni tushunishga yordam beradi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L05_M06_002": [
        {
            "code": "L05_Q079",
            "question": "Ustunlarni bir xil o'q va ritmda joylashtirish muhim bo'lishi mumkinmi?",
            "explanation": (
                "Tartibli joylashuv model va arxitektura sifatini yaxshilaydi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L05_Q080",
            "question": "Column circulation bilan konflikt yaratishi mumkinmi?",
            "explanation": (
                "Noto'g'ri joylashgan ustun harakat va xona funksiyasini buzishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L05_Q081",
            "question": "Ayvon ustunlarini ko'z bilan teng masofaga qo'yish yetarlimi?",
            "explanation": (
                "Ularning haqiqiy o'lcham va intervallari tekshirilishi kerak."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
    ],

    "L05_M06_003": [
        {
            "code": "L05_Q082",
            "question": "Beam gorizontal konstruktiv BIM elementi sifatida ishlatilishi mumkinmi?",
            "explanation": (
                "Beam Tool rigel va boshqa beam elementlarini modellashtirish uchun ishlatiladi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L05_Q083",
            "question": "Beam elevation 3D modelga ta'sir qiladimi?",
            "explanation": (
                "Beamning vertikal joylashuvi elevation bilan bog'liq."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L05_Q084",
            "question": "Beamni faqat planda tekshirish yetarlimi?",
            "explanation": (
                "3D va Section beamning balandlik va ulanishini tekshirishga yordam beradi."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
    ],

    "L05_M06_004": [
        {
            "code": "L05_Q085",
            "question": "Column va Beam yagona tizim sifatida ko'rilishi kerakmi?",
            "explanation": (
                "Ularning o'zaro joylashuvi va ulanishi birgalikda tekshiriladi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L05_Q086",
            "question": "Beam Column yonida turishi, lekin unga aniq tutashmasligi xato bo'lishi mumkinmi?",
            "explanation": (
                "Elementlarning o'zaro reference va ulanishi nazorat qilinadi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L05_Q087",
            "question": "Section Column va Beamning vertikal aloqasini tekshirishga yordam beradimi?",
            "explanation": (
                "Section balandlik va sathlarni ko'rish uchun muhim."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L05_M06_005": [
        {
            "code": "L05_Q088",
            "question": "Columnlar fasad ritmiga ta'sir qilishi mumkinmi?",
            "explanation": (
                "Ayvon va fasaddagi ustunlar kompozitsiyaning bir qismi bo'lishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L05_Q089",
            "question": "Column va Beamni 3D tekshirish kerakmi?",
            "explanation": (
                "3D elementlarning umumiy geometriya va tutashuvini ko'rishga yordam beradi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L05_Q090",
            "question": "Column va Beam bilan ishlashdagi to'g'ri workflow qaysi?",
            "explanation": (
                "Joylashuv, parametr va turli ko'rinishlarda nazorat birgalikda bajariladi."
            ),
            "options": [
                (
                    "A",
                    "Parametr → joylashtirish → ulash → Plan/3D/Section tekshiruv",
                    True,
                ),
                (
                    "B",
                    "Ko'z bilan joylashtirish → tekshirmaslik",
                    False,
                ),
            ],
        },
    ],
}


# ============================================================
# DATABASE SEED
# ============================================================

def seed_level05_module06():
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
        ) in LEVEL05_MODULE06_LESSONS:

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
