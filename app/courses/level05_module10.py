from database.database import get_connection


# ============================================================
# LEVEL 5
# MODULE 10 - BIRINCHI ARCHICAD LOYIHA
# ============================================================

LEVEL05_MODULE10_LESSONS = [
    (
        "L05_M10",
        "L05_M10_001",
        "Loyihani boshlash va reja",
        "theory",
        "Oddiy turar joy loyihasini boshlashdan oldin vazifa va ish ketma-ketligini tuzish.",
        1,
        60,
        25,
    ),
    (
        "L05_M10",
        "L05_M10_002",
        "Devor va slab modeli",
        "practice",
        "Uy konturi, ichki devorlar va slab elementlarini yaratish.",
        2,
        90,
        30,
    ),
    (
        "L05_M10",
        "L05_M10_003",
        "Door, Window va mebel",
        "practice",
        "Eshik, deraza va asosiy mebellarni funksional joylashtirish.",
        3,
        90,
        30,
    ),
    (
        "L05_M10",
        "L05_M10_004",
        "2D grafika va Dimension",
        "practice",
        "Plan chizmasini matn, label va o'lchamlar bilan tushunarli holatga keltirish.",
        4,
        90,
        30,
    ),
    (
        "L05_M10",
        "L05_M10_005",
        "Birinchi loyiha auditi",
        "practice",
        "Oddiy Archicad loyihasini Plan, 3D, Elevation va Section orqali tekshirish.",
        5,
        120,
        40,
    ),
]


# ============================================================
# CONTENT
# ============================================================

LEVEL05_MODULE10_CONTENT = {
    "L05_M10_001": [
        {
            "title": "Endi hamma instrumentlarni birlashtiramiz",
            "type": "highlight",
            "text": """
            Shu paytgacha siz:

            <br><br>

            • interfeys;<br>
            • Navigator;<br>
            • Wall;<br>
            • Slab;<br>
            • Door va Window;<br>
            • Column va Beam;<br>
            • Object;<br>
            • 2D instrumentlar;<br>
            • Dimension

            <br><br>

            bilan alohida ishladingiz.

            <br><br>

            Endi ularni bitta
            kichik loyiha ichida birlashtiramiz.
            """,
        },
        {
            "title": "Loyiha vazifasi",
            "type": "example",
            "text": """
            Oddiy bir qavatli uy.

            <br><br>

            Shartli tarkib:

            <br><br>

            • living;<br>
            • oshxona/dining;<br>
            • 2 ta bedroom;<br>
            • sanuzel;<br>
            • koridor;<br>
            • kirish zonasi.
            """,
        },
        {
            "title": "Avval plan haqida o'ylang",
            "type": "highlight",
            "text": """
            Archicadni ochishdan oldin
            ham arxitektura fikri kerak.

            <br><br>

            Savollar:

            <br><br>

            • kirish qayerda?<br>
            • living qayerda?<br>
            • private zona qayerda?<br>
            • oshxona bilan dining qanday bog'lanadi?<br>
            • sanuzel qayerda qulay?
            """,
        },
        {
            "title": "Ish ketma-ketligi",
            "type": "normal",
            "text": """
            Ushbu mini-loyihada:

            <br><br>

            1. Plan sxemasi<br>
            2. Wall<br>
            3. Slab<br>
            4. Door va Window<br>
            5. Object<br>
            6. 2D grafika<br>
            7. Dimension<br>
            8. Audit

            <br><br>

            ketma-ketligida ishlaymiz.
            """,
        },
        {
            "title": "Tezlik emas, to'g'rilik",
            "type": "warning",
            "text": """
            Birinchi loyihada
            tez ishlashga urinmang.

            <br><br>

            Har bir bosqichdan keyin
            modelni tekshiring.

            <br><br>

            Noto'g'ri modelni
            tez yaratish foyda bermaydi.
            """,
        },
        {
            "title": "Mini-vazifa",
            "type": "example",
            "text": """
            Archicadga kirmasdan
            qog'ozda yoki sxemada
            xonalar aloqasini chizing.

            <br><br>

            Keyin nima uchun
            aynan shu joylashuvni
            tanlaganingizni yozing.
            """,
        },
    ],

    "L05_M10_002": [
        {
            "title": "1-bosqich — tashqi devorlar",
            "type": "highlight",
            "text": """
            Wall Tool bilan
            avval bino tashqi konturini yarating.

            <br><br>

            Reference line tizimini
            bir xil mantiqda ishlating.
            """,
        },
        {
            "title": "2-bosqich — ichki devorlar",
            "type": "normal",
            "text": """
            Keyin xonalarni ajratuvchi
            ichki devorlarni yarating.

            <br><br>

            Plan funksiyasini
            Archicad instrumentidan ustun qo'ying.
            """,
        },
        {
            "title": "Xona aloqalarini tekshiring",
            "type": "example",
            "text": """
            Livingga kirish
            koridordan mantiqiymi?

            <br><br>

            Bedroomlar private zonadami?

            <br><br>

            Oshxona dining bilan
            qulay bog'langanmi?
            """,
        },
        {
            "title": "3-bosqich — Slab",
            "type": "highlight",
            "text": """
            Uy konturiga mos
            Slab yarating.

            <br><br>

            Thickness,
            elevation
            va konturini tekshiring.
            """,
        },
        {
            "title": "Burchak va connectionlar",
            "type": "normal",
            "text": """
            Plan bo'ylab yaqinlashtirib
            barcha burchaklarni tekshiring.

            <br><br>

            • devorlar tutashganmi;<br>
            • kichik gap yo'qmi;<br>
            • tasodifiy devor qolmaganmi.
            """,
        },
        {
            "title": "3D tekshiruv",
            "type": "highlight",
            "text": """
            Endi 3Dga o'ting.

            <br><br>

            Tekshiring:

            <br><br>

            • tashqi hajm;<br>
            • devor balandliklari;<br>
            • Slab joylashuvi;<br>
            • ortiqcha elementlar.
            """,
        },
        {
            "title": "Xatoni toping",
            "type": "warning",
            "text": """
            Floor Planda uy to'g'ri.

            <br><br>

            3Dda esa bitta ichki devor
            boshqa devorlardan ancha past.

            <br><br>

            Muammo:
            devor height parametri
            boshqalardan farq qilgan.
            """,
        },
    ],

    "L05_M10_003": [
        {
            "title": "Doorlarni joylashtiring",
            "type": "highlight",
            "text": """
            Har bir xona uchun
            Door Tooldan foydalaning.

            <br><br>

            Lekin eshikni
            shunchaki devorga qo'ymang.

            <br><br>

            Opening directionni
            ham tekshiring.
            """,
        },
        {
            "title": "Eshik audit savollari",
            "type": "normal",
            "text": """
            Har bir eshikda so'rang:

            <br><br>

            • ochilganda mebelga uriladimi?<br>
            • boshqa eshik bilan konflikt bormi?<br>
            • circulationni to'sadimi?<br>
            • xona ichiga kirish qulaymi?
            """,
        },
        {
            "title": "Windowlarni joylashtiring",
            "type": "highlight",
            "text": """
            Window Tool yordamida
            asosiy xonalarga
            derazalar joylashtiring.

            <br><br>

            Plan bilan birga
            Elevationni ham kuzating.
            """,
        },
        {
            "title": "Fasad ritmi",
            "type": "example",
            "text": """
            Bedroomlarning
            bir xil turdagi derazalari
            tasodifiy turli balandlikda
            qolib ketmasin.

            <br><br>

            Elevation orqali tekshiring.
            """,
        },
        {
            "title": "Object Tool",
            "type": "normal",
            "text": """
            Endi asosiy mebellarni qo'ying:

            <br><br>

            • living — divan va TV;<br>
            • dining — stol va stullar;<br>
            • bedroom — krovat va shkaf;<br>
            • oshxona — asosiy mebel sxemasi.
            """,
        },
        {
            "title": "Mebel plan auditi",
            "type": "highlight",
            "text": """
            Mebel qo'yilgandan keyin
            plan qayta baholanadi.

            <br><br>

            Xona katta ko'rinishi
            yetarli emas.

            <br><br>

            U real foydalanishda
            qulay bo'lishi kerak.
            """,
        },
        {
            "title": "Xatoni toping",
            "type": "warning",
            "text": """
            Bedroomda krovat va
            katta shkaf sig'di.

            <br><br>

            Lekin eshik ochilganda
            shkaf oldini yopib qo'ydi.

            <br><br>

            Model xatosiz,
            lekin rejalashtirish noto'g'ri.
            """,
        },
    ],

    "L05_M10_004": [
        {
            "title": "Modeldan chizmaga",
            "type": "highlight",
            "text": """
            Yaxshi BIM modelning o'zi
            hali topshiriladigan chizma emas.

            <br><br>

            Endi grafikani
            tushunarli holatga keltiramiz.
            """,
        },
        {
            "title": "Xona nomlari",
            "type": "normal",
            "text": """
            Text Tool yordamida
            xonalarga tushunarli nomlar qo'ying.

            <br><br>

            Masalan:

            <br><br>

            LIVING<br>
            KITCHEN<br>
            BEDROOM 01<br>
            BEDROOM 02<br>
            BATHROOM
            """,
        },
        {
            "title": "Kerakli Label",
            "type": "normal",
            "text": """
            Faqat tushuntirish zarur bo'lgan
            elementlarga Label qo'ying.

            <br><br>

            Chizmani ortiqcha
            izoh bilan to'ldirmang.
            """,
        },
        {
            "title": "Dimension",
            "type": "highlight",
            "text": """
            Endi plan uchun:

            <br><br>

            • umumiy gabarit;<br>
            • muhim tashqi segmentlar;<br>
            • kerakli ichki o'lchamlar

            <br><br>

            qo'yiladi.
            """,
        },
        {
            "title": "2D grafikani nazorat qiling",
            "type": "warning",
            "text": """
            Wall yoki boshqa BIM elementni
            Line Tool bilan
            keraksiz qayta chizmang.

            <br><br>

            Model va 2D grafika
            bir-biridan ajralib ketishi mumkin.
            """,
        },
        {
            "title": "Grafik ierarxiya",
            "type": "normal",
            "text": """
            Plan qaralganda:

            <br><br>

            1. bino geometriyasi;<br>
            2. asosiy xonalar;<br>
            3. dimensionlar;<br>
            4. yordamchi izohlar

            <br><br>

            tushunarli o'qilishi kerak.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Planni 30 soniya davomida
            uzoqdan ko'ring.

            <br><br>

            O'zingizdan so'rang:

            <br><br>

            • plan tushunarlimi?<br>
            • matn o'qiladimi?<br>
            • dimensionlar ortiqcha emasmi?<br>
            • grafik shovqin bormi?
            """,
        },
    ],

    "L05_M10_005": [
        {
            "title": "FINAL AUDIT",
            "type": "highlight",
            "text": """
            Birinchi Archicad loyihangiz
            tayyor bo'lishidan oldin
            uni to'liq tekshiramiz.

            <br><br>

            Maqsad —
            xatolarni yashirish emas,
            ularni topish.
            """,
        },
        {
            "title": "1. Floor Plan audit",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • xonalar funksiyasi;<br>
            • circulation;<br>
            • devor connections;<br>
            • Door opening;<br>
            • Window joylashuvi;<br>
            • mebel ergonomikasi;<br>
            • dimensionlar.
            """,
        },
        {
            "title": "2. 3D audit",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • devor balandligi;<br>
            • slab joylashuvi;<br>
            • eshik/derazalar;<br>
            • obyekt elevationlari;<br>
            • dublikatlar;<br>
            • tasodifiy elementlar.
            """,
        },
        {
            "title": "3. Elevation audit",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • deraza ritmi;<br>
            • eshik balandliklari;<br>
            • fasad kompozitsiyasi;<br>
            • tasodifiy openinglar.
            """,
        },
        {
            "title": "4. Section audit",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • slab sathi;<br>
            • devor balandligi;<br>
            • vertikal aloqalar;<br>
            • modeldagi g'alati kesishmalar.
            """,
        },
        {
            "title": "5. Navigator audit",
            "type": "example",
            "text": """
            Navigator orqali
            loyiha qismlarini ko'ring.

            <br><br>

            Kerakli plan,
            section,
            elevation
            va 3D ko'rinishlar
            tartibli ochiladimi?
            """,
        },
        {
            "title": "Xatoni toping",
            "type": "warning",
            "text": """
            O'quvchi Floor Planni
            tekshirib loyiha tayyor dedi.

            <br><br>

            3Dda esa bitta stol havoda,
            derazalardan biri boshqa balandlikda,
            Slab esa devordan tashqariga chiqib turibdi.

            <br><br>

            Xulosa:

            <br><br>

            <b>
            bitta ko'rinishda tekshirish yetarli emas.
            </b>
            """,
        },
        {
            "title": "Birinchi loyiha yakuniy checklist",
            "type": "example",
            "text": """
            <b>PLAN</b><br>
            ✓ xona aloqalari to'g'rimi?<br>
            ✓ circulation ishlaydimi?<br>
            ✓ eshiklar konflikt qilmayaptimi?<br><br>

            <b>MODEL</b><br>
            ✓ Wall to'g'rimi?<br>
            ✓ Slab to'g'rimi?<br>
            ✓ Door/Window to'g'rimi?<br>
            ✓ Objectlar to'g'rimi?<br><br>

            <b>DOCUMENTATION</b><br>
            ✓ xona nomlari bormi?<br>
            ✓ dimensionlar tushunarlimi?<br>
            ✓ ortiqcha 2D element yo'qmi?<br><br>

            <b>CONTROL</b><br>
            ✓ Floor Plan tekshirildi;<br>
            ✓ 3D tekshirildi;<br>
            ✓ Elevation tekshirildi;<br>
            ✓ Section tekshirildi.
            """,
        },
        {
            "title": "LEVEL 5 yakuni",
            "type": "highlight",
            "text": """
            Siz endi Archicadda
            mutlaqo noldan:

            <br><br>

            ✓ loyiha boshlash;<br>
            ✓ devor yaratish;<br>
            ✓ slab yaratish;<br>
            ✓ Door va Window qo'yish;<br>
            ✓ Column va Beam ishlatish;<br>
            ✓ mebel joylashtirish;<br>
            ✓ 2D grafikalar qo'shish;<br>
            ✓ dimension qo'yish;<br>
            ✓ modelni turli ko'rinishlarda tekshirish

            <br><br>

            jarayonini bajara olasiz.

            <br><br>

            Keyingi qadam:
            <b>LEVEL 5 FINAL EXAM.</b>
            """,
        },
    ],
}


# ============================================================
# QUIZ
# ============================================================

LEVEL05_MODULE10_QUIZ = {
    "L05_M10_001": [
        {
            "code": "L05_Q136",
            "question": "Archicad loyihasini boshlashdan oldin xona aloqalarini o'ylash kerakmi?",
            "explanation": (
                "Dastur instrumentlari arxitektura qarorini almashtirmaydi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L05_Q137",
            "question": "Birinchi loyihada asosiy maqsad faqat tez ishlashmi?",
            "explanation": (
                "Boshlang'ich loyiha uchun to'g'ri workflow va nazorat tezlikdan muhimroq."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L05_Q138",
            "question": "Wall, Slab, Door va boshqa instrumentlar bitta loyiha ichida birgalikda ishlatiladimi?",
            "explanation": (
                "Mini-loyiha oldingi instrumentlarni yagona workflowga birlashtiradi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L05_M10_002": [
        {
            "code": "L05_Q139",
            "question": "Tashqi devorlardan keyin ichki zoningni yaratish mumkinmi?",
            "explanation": (
                "Ichki devorlar xonalar va funksional zonalarni shakllantiradi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L05_Q140",
            "question": "Slab yaratgandan keyin 3D tekshiruvi kerakmi?",
            "explanation": (
                "3D kontur va vertikal joylashuvdagi xatolarni ko'rsatishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L05_Q141",
            "question": "Planda to'g'ri ko'ringan modelda 3D xato bo'lishi mumkinmi?",
            "explanation": (
                "Masalan element balandligi yoki elevationi noto'g'ri bo'lishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L05_M10_003": [
        {
            "code": "L05_Q142",
            "question": "Door opening direction ergonomikaga ta'sir qiladimi?",
            "explanation": (
                "Eshik mebel yoki circulation bilan konflikt yaratishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L05_Q143",
            "question": "Windowlarni Elevationda tekshirish foydalimi?",
            "explanation": (
                "Elevation fasaddagi balandlik va ritmni ko'rishga yordam beradi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L05_Q144",
            "question": "Mebel sig'ishi xonaning avtomatik qulayligini anglatadimi?",
            "explanation": (
                "Circulation va foydalanish zonalari ham tekshirilishi kerak."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
    ],

    "L05_M10_004": [
        {
            "code": "L05_Q145",
            "question": "Yaxshi BIM model avtomatik ravishda yakuniy tushunarli chizma bo'ladimi?",
            "explanation": (
                "Documentation uchun matn, dimension va grafik tartib ham kerak bo'lishi mumkin."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L05_Q146",
            "question": "Dimensionlarni grafik jihatdan tartibli joylashtirish kerakmi?",
            "explanation": (
                "Dimensionlar chizmani tushuntirishi, uni to'sib qo'ymasligi kerak."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L05_Q147",
            "question": "BIM devorlarni Line Tool bilan keraksiz qayta chizish yaxshi odatmi?",
            "explanation": (
                "Model va qo'shimcha 2D grafik keyinchalik bir-biriga mos kelmay qolishi mumkin."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
    ],

    "L05_M10_005": [
        {
            "code": "L05_Q148",
            "question": "Final auditda Floor Plan bilan birga 3D, Elevation va Section ham tekshiriladimi?",
            "explanation": (
                "Turli ko'rinishlar turli turdagi xatolarni ko'rsatadi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L05_Q149",
            "question": "Modelni faqat bitta ko'rinishda tekshirish yetarlimi?",
            "explanation": (
                "Faqat bitta view orqali barcha geometrik va vertikal xatolarni aniqlash qiyin."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L05_Q150",
            "question": "Birinchi Archicad loyiha uchun to'g'ri yakuniy workflow qaysi?",
            "explanation": (
                "Model yaratishdan keyin hujjatlashtirish va ko'p ko'rinishli audit bajariladi."
            ),
            "options": [
                (
                    "A",
                    "Plan → Model → Door/Window/Object → Documentation → Audit",
                    True,
                ),
                (
                    "B",
                    "Tasodifiy chizish → 3D ko'rish → tugatish",
                    False,
                ),
            ],
        },
    ],
}


# ============================================================
# DATABASE SEED
# ============================================================

def seed_level05_module10():
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
        ) in LEVEL05_MODULE10_LESSONS:

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
