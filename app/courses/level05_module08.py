from database.database import get_connection


# ============================================================
# LEVEL 5
# MODULE 08 - 2D INSTRUMENTLAR
# ============================================================

LEVEL05_MODULE08_LESSONS = [
    (
        "L05_M08",
        "L05_M08_001",
        "Line va Polyline",
        "theory",
        "Archicadda yordamchi 2D chiziqlar va polyline bilan ishlashni o'rganish.",
        1,
        40,
        20,
    ),
    (
        "L05_M08",
        "L05_M08_002",
        "Fill Tool",
        "theory",
        "2D yuzalarni grafik tarzda ko'rsatish va fill bilan ishlash.",
        2,
        45,
        20,
    ),
    (
        "L05_M08",
        "L05_M08_003",
        "Text Tool",
        "practice",
        "Chizmalarga tushunarli va tartibli matn joylashtirish.",
        3,
        45,
        20,
    ),
    (
        "L05_M08",
        "L05_M08_004",
        "Label Tool",
        "practice",
        "Loyiha elementlariga tushuntiruvchi label va izohlar qo'yish.",
        4,
        50,
        20,
    ),
    (
        "L05_M08",
        "L05_M08_005",
        "2D grafik mini-loyiha",
        "practice",
        "Line, Polyline, Fill, Text va Label yordamida tartibli loyiha chizmasi tayyorlash.",
        5,
        60,
        25,
    ),
]


# ============================================================
# CONTENT
# ============================================================

LEVEL05_MODULE08_CONTENT = {
    "L05_M08_001": [
        {
            "title": "2D instrumentlar nima uchun kerak?",
            "type": "highlight",
            "text": """
            Archicad BIM dasturi bo'lsa ham,
            2D instrumentlar juda muhim.

            <br><br>

            Ular:

            <br><br>

            • yordamchi chiziqlar;<br>
            • sxemalar;<br>
            • grafik tushuntirish;<br>
            • detallash;<br>
            • prezentatsion chizmalar

            <br><br>

            uchun ishlatiladi.
            """,
        },
        {
            "title": "Line Tool",
            "type": "normal",
            "text": """
            Line Tool —
            oddiy 2D chiziq yaratadi.

            <br><br>

            U BIM modeli emas.

            <br><br>

            Ya'ni Line Tool bilan
            chizilgan chiziq
            devor yoki beamga aylanmaydi.
            """,
        },
        {
            "title": "Polyline",
            "type": "normal",
            "text": """
            Polyline bir nechta
            segmentni bitta
            bog'langan 2D element sifatida
            yaratishga yordam beradi.
            """,
        },
        {
            "title": "Qachon ishlatiladi?",
            "type": "example",
            "text": """
            Masalan:

            <br><br>

            • uchastka chegarasi;<br>
            • yordamchi sxema;<br>
            • grafik yo'nalish;<br>
            • zoning konturi

            <br><br>

            uchun Line yoki Polyline
            foydali bo'lishi mumkin.
            """,
        },
        {
            "title": "Model va 2Dni aralashtirmang",
            "type": "warning",
            "text": """
            Boshlovchilarning katta xatosi:

            <br><br>

            devorni Wall Tool o'rniga
            Line Tool bilan chizish.

            <br><br>

            Plan ko'rinishda o'xshashi mumkin,
            lekin 3D modelda devor yo'q.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            1. Line Tool bilan 4 ta chiziq chizing.<br><br>
            2. Polyline bilan yopiq kontur yarating.<br><br>
            3. Keyin 3Dga o'ting.<br><br>
            4. Nega ular 3D modelda yo'qligini tushuning.
            """,
        },
    ],

    "L05_M08_002": [
        {
            "title": "Fill Tool nima?",
            "type": "highlight",
            "text": """
            Fill Tool
            2D yuzani grafik tarzda
            ko'rsatish uchun ishlatiladi.

            <br><br>

            U ma'lum hududni
            rang, pattern yoki
            grafik ko'rinish bilan
            ajratishga yordam beradi.
            """,
        },
        {
            "title": "Fill qayerda foydali?",
            "type": "normal",
            "text": """
            Filldan masalan:

            <br><br>

            • zoning diagram;<br>
            • material ko'rsatish;<br>
            • kesim grafikasi;<br>
            • prezentatsion plan;<br>
            • hududlarni ajratish

            <br><br>

            uchun foydalanish mumkin.
            """,
        },
        {
            "title": "Fill va Slab farqi",
            "type": "highlight",
            "text": """
            Fill va Slab
            planda o'xshab ko'rinishi mumkin.

            <br><br>

            Lekin:

            <br><br>

            <b>Fill = 2D grafik element</b>

            <br><br>

            <b>Slab = 3D BIM element</b>
            """,
        },
        {
            "title": "Kontur",
            "type": "normal",
            "text": """
            Fill ham
            yopiq kontur asosida
            maydon hosil qiladi.

            <br><br>

            Uning shakli
            chizma maqsadiga mos
            va toza bo'lishi kerak.
            """,
        },
        {
            "title": "Ortiqcha fill",
            "type": "warning",
            "text": """
            Har bir joyga
            turli hatch yoki rang qo'yish
            chizmani professional qilmaydi.

            <br><br>

            Aksincha,
            grafik shovqin yaratishi mumkin.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Plan ichida 3 ta zona yarating:

            <br><br>

            PUBLIC<br>
            PRIVATE<br>
            SERVICE

            <br><br>

            Har biri uchun
            Fill yordamida
            alohida grafik zona yarating.
            """,
        },
    ],

    "L05_M08_003": [
        {
            "title": "Text Tool",
            "type": "highlight",
            "text": """
            Chizma tushunarli bo'lishi uchun
            grafikadan tashqari
            matn ham kerak.

            <br><br>

            Text Tool
            erkin yozuv joylashtirishga
            yordam beradi.
            """,
        },
        {
            "title": "Matnning vazifasi",
            "type": "normal",
            "text": """
            Text orqali:

            <br><br>

            • xona nomi;<br>
            • izoh;<br>
            • sarlavha;<br>
            • tushuntirish;<br>
            • eslatma

            <br><br>

            berilishi mumkin.
            """,
        },
        {
            "title": "Matn ierarxiyasi",
            "type": "highlight",
            "text": """
            Barcha matnlar
            bir xil katta va bir xil kuchli
            bo'lishi shart emas.

            <br><br>

            Sarlavha,
            asosiy yozuv
            va izoh

            <br><br>

            grafik ierarxiyaga ega bo'lishi kerak.
            """,
        },
        {
            "title": "Juda ko'p matn",
            "type": "warning",
            "text": """
            Chizmada uzun paragraf
            va ortiqcha izohlar ko'p bo'lsa,
            asosiy grafik axborot yo'qolishi mumkin.

            <br><br>

            Matn qisqa,
            aniq
            va kerakli joyda bo'lsin.
            """,
        },
        {
            "title": "Joylashuv",
            "type": "normal",
            "text": """
            Text:

            <br><br>

            • devor ustiga chiqib ketmasin;<br>
            • dimension bilan to'qnashmasin;<br>
            • boshqa yozuvni yopmasin;<br>
            • kerakli obyektga yaqin bo'lsin.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Plandagi 5 ta xonaga
            nom yozing.

            <br><br>

            Keyin alohida:

            <br><br>

            1 ta sarlavha<br>
            1 ta izoh

            <br><br>

            qo'shing.

            <br><br>

            Ularning o'lcham ierarxiyasini tekshiring.
            """,
        },
    ],

    "L05_M08_004": [
        {
            "title": "Label Tool nima?",
            "type": "highlight",
            "text": """
            Label Tool
            ma'lum element yoki
            loyiha obyektini
            tushuntirish uchun ishlatiladi.
            """,
        },
        {
            "title": "Text va Label farqi",
            "type": "normal",
            "text": """
            Oddiy tushuncha:

            <br><br>

            <b>Text</b> —
            erkin matn.

            <br><br>

            <b>Label</b> —
            ma'lum element yoki
            chizma qismiga bog'langan
            tushuntiruvchi belgi bo'lishi mumkin.
            """,
        },
        {
            "title": "Label qayerda foydali?",
            "type": "example",
            "text": """
            Label orqali:

            <br><br>

            • devor turi;<br>
            • element nomi;<br>
            • material izohi;<br>
            • detal chaqirig'i;<br>
            • obyekt haqida ma'lumot

            <br><br>

            ko'rsatilishi mumkin.
            """,
        },
        {
            "title": "Leader",
            "type": "normal",
            "text": """
            Labeldagi ko'rsatkich
            aynan qaysi elementga
            tegishli ekanini
            aniq ko'rsatishi kerak.
            """,
        },
        {
            "title": "Noto'g'ri label",
            "type": "warning",
            "text": """
            Label matni
            bir element haqida,

            <br><br>

            leader esa
            boshqa elementga qarab turibdi.

            <br><br>

            Bu xavfli grafik xato.
            """,
        },
        {
            "title": "Ortiqcha label",
            "type": "warning",
            "text": """
            Chizmaning har bir elementiga
            alohida label qo'yish shart emas.

            <br><br>

            Faqat o'quvchiga yoki loyiha
            foydalanuvchisiga kerakli
            axborotni bering.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Planda 3 ta elementga
            label qo'ying.

            <br><br>

            Tekshiring:

            <br><br>

            • matn aniqmi;<br>
            • leader to'g'ri elementga qaraganmi;<br>
            • boshqa grafikani to'smayaptimi.
            """,
        },
    ],

    "L05_M08_005": [
        {
            "title": "2D grafik mini-loyiha",
            "type": "highlight",
            "text": """
            Endi bitta oddiy Floor Planni
            grafik jihatdan
            tushunarli ko'rinishga keltiramiz.

            <br><br>

            Maqsad —
            bezak emas.

            <br><br>

            Maqsad —
            axborotni aniq yetkazish.
            """,
        },
        {
            "title": "1-bosqich — Line",
            "type": "normal",
            "text": """
            Zarur yordamchi
            grafik chiziqlarni qo'shing.

            <br><br>

            Lekin BIM elementni
            Line bilan almashtirmang.
            """,
        },
        {
            "title": "2-bosqich — Fill",
            "type": "normal",
            "text": """
            Public,
            private
            va service zonalarini
            Fill yordamida ajrating.

            <br><br>

            Grafikani juda kuchli qilmang.
            """,
        },
        {
            "title": "3-bosqich — Text",
            "type": "normal",
            "text": """
            Xonalarga nom qo'ying.

            <br><br>

            Plan uchun
            tushunarli sarlavha yarating.
            """,
        },
        {
            "title": "4-bosqich — Label",
            "type": "normal",
            "text": """
            Zarur elementlarga
            tushuntiruvchi Label qo'shing.

            <br><br>

            Har bir leader
            to'g'ri obyektga
            qaraganini tekshiring.
            """,
        },
        {
            "title": "5-bosqich — grafik tozalash",
            "type": "normal",
            "text": """
            Chizmani uzoqdan ko'ring.

            <br><br>

            Tekshiring:

            <br><br>

            • nimani birinchi ko'ryapsiz?<br>
            • matnlar o'qiladimi?<br>
            • ortiqcha chiziqlar bormi?<br>
            • grafik shovqin bormi?<br>
            • asosiy plan aniq ko'rinadimi?
            """,
        },
        {
            "title": "Xatoni toping",
            "type": "warning",
            "text": """
            O'quvchi devorlarni
            qalin Line Tool bilan
            qayta ustidan chizib chiqdi.

            <br><br>

            Plan chiroyliroq ko'rindi.

            <br><br>

            Lekin keyin devor siljitildi,
            2D chiziqlar esa eski joyda qoldi.

            <br><br>

            Natija:
            model va 2D grafika
            bir-biriga mos emas.

            <br><br>

            Keraksiz 2D dublikatlardan qoching.
            """,
        },
        {
            "title": "Professional checklist",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            <b>1.</b> BIM elementlar Line bilan almashtirilmaganmi?<br><br>
            <b>2.</b> Polyline vazifasi aniqmi?<br><br>
            <b>3.</b> Fill ortiqcha emasmi?<br><br>
            <b>4.</b> Text o'qiladimi?<br><br>
            <b>5.</b> Matn ierarxiyasi bormi?<br><br>
            <b>6.</b> Label to'g'ri obyektga qaraganmi?<br><br>
            <b>7.</b> Grafik toza va tushunarlimi?
            """,
        },
        {
            "title": "Modul yakuni",
            "type": "highlight",
            "text": """
            Siz endi:

            <br><br>

            ✓ Line Toolni tushunasiz;<br>
            ✓ Polyline bilan ishlaysiz;<br>
            ✓ Fill yaratishingiz mumkin;<br>
            ✓ Text joylashtirasiz;<br>
            ✓ Label qo'yasiz;<br>
            ✓ model va 2D grafikani farqlaysiz;<br>
            ✓ chizmani grafik jihatdan tartibga keltirasiz.

            <br><br>

            Keyingi modul:
            <b>Dimension.</b>
            """,
        },
    ],
}


# ============================================================
# QUIZ
# ============================================================

LEVEL05_MODULE08_QUIZ = {
    "L05_M08_001": [
        {
            "code": "L05_Q106",
            "question": "Line Tool bilan chizilgan chiziq avtomatik ravishda 3D devorga aylanadimi?",
            "explanation": (
                "Line Tool 2D grafik element yaratadi, Wall Tool esa BIM devor elementini yaratadi."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L05_Q107",
            "question": "Polyline bir nechta segmentni bitta bog'langan 2D element sifatida yaratishga yordam beradimi?",
            "explanation": (
                "Polyline ketma-ket segmentlardan tashkil topgan 2D geometriya uchun qulay."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L05_Q108",
            "question": "BIM devorni Line Tool bilan almashtirish yaxshi workflow hisoblanadimi?",
            "explanation": (
                "2D Line model elementi emas va 3D hamda BIM ma'lumotini bermaydi."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
    ],

    "L05_M08_002": [
        {
            "code": "L05_Q109",
            "question": "Fill 2D grafik yuzani ko'rsatish uchun ishlatiladimi?",
            "explanation": (
                "Fill ma'lum hududni grafik pattern yoki boshqa 2D ko'rinish bilan ajratishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L05_Q110",
            "question": "Fill va Slab bir xil turdagi elementmi?",
            "explanation": (
                "Fill 2D grafik element, Slab esa 3D BIM elementi."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L05_Q111",
            "question": "Juda ko'p turli fill ishlatish grafik shovqin yaratishi mumkinmi?",
            "explanation": (
                "Grafik elementlar axborotni tushunarli qilish uchun me'yorida ishlatiladi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L05_M08_003": [
        {
            "code": "L05_Q112",
            "question": "Text Tool yordamida xona nomlari va izohlar yozish mumkinmi?",
            "explanation": (
                "Text Tool erkin matn joylashtirish uchun ishlatiladi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L05_Q113",
            "question": "Barcha matnlarni bir xil vizual kuchda berish har doim yaxshi yechimmi?",
            "explanation": (
                "Sarlavha va izohlar orasida grafik ierarxiya bo'lishi chizmani o'qishni yengillashtiradi."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L05_Q114",
            "question": "Text dimension va boshqa grafikani to'sib qo'ymasligi kerakmi?",
            "explanation": (
                "Matn joylashuvi chizma o'qiluvchanligiga ta'sir qiladi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L05_M08_004": [
        {
            "code": "L05_Q115",
            "question": "Label ma'lum loyiha elementini tushuntirish uchun ishlatilishi mumkinmi?",
            "explanation": (
                "Label element yoki chizma qismiga bog'liq tushuntiruvchi belgi sifatida ishlatilishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L05_Q116",
            "question": "Label leaderi noto'g'ri elementga qarasa bu grafik xato hisoblanadimi?",
            "explanation": (
                "Label qaysi obyektga tegishli ekanini aniq ko'rsatishi kerak."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L05_Q117",
            "question": "Har bir elementga majburiy ravishda label qo'yish kerakmi?",
            "explanation": (
                "Faqat kerakli va foydali ma'lumotlarni ko'rsatish maqsadga muvofiq."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
    ],

    "L05_M08_005": [
        {
            "code": "L05_Q118",
            "question": "Model elementini 2D Line bilan qayta ustidan chizish keyinchalik nomuvofiqlik yaratishi mumkinmi?",
            "explanation": (
                "Model o'zgarsa qo'shimcha 2D grafik avtomatik moslashmasligi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L05_Q119",
            "question": "2D grafikadagi asosiy maqsad axborotni tushunarli yetkazishmi?",
            "explanation": (
                "Line, Fill, Text va Label chizmani o'qishni osonlashtirish uchun ishlatiladi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L05_Q120",
            "question": "2D instrumentlar bilan ishlashdagi to'g'ri prinsip qaysi?",
            "explanation": (
                "2D grafika modelni tushuntirishi kerak, uni keraksiz takrorlamasligi kerak."
            ),
            "options": [
                (
                    "A",
                    "Modelni saqlash → kerakli 2D grafika → o'qiluvchanlik tekshiruvi",
                    True,
                ),
                (
                    "B",
                    "Hammasini Line bilan qayta chizish",
                    False,
                ),
            ],
        },
    ],
}


# ============================================================
# DATABASE SEED
# ============================================================

def seed_level05_module08():
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
        ) in LEVEL05_MODULE08_LESSONS:

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
