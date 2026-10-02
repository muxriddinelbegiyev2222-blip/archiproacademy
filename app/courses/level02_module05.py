from database.database import get_connection


# ============================================================
# LEVEL 2
# MODULE 05 - OSHXONA LOYIHALASH
# ============================================================

LEVEL02_MODULE05_LESSONS = [
    (
        "L02_M05",
        "L02_M05_001",
        "Oshxona funksiyasi va zonalari",
        "theory",
        "Oshxonadagi asosiy funksional zonalar va ularning o'zaro aloqasini tushunish.",
        1,
        50,
        20,
    ),
    (
        "L02_M05",
        "L02_M05_002",
        "Ishchi uchburchak",
        "theory",
        "Muzlatkich, rakovina va pishirish zonasi o'rtasidagi ishchi aloqani tushunish.",
        2,
        55,
        20,
    ),
    (
        "L02_M05",
        "L02_M05_003",
        "Countertop va saqlash",
        "practice",
        "Ishchi sirt, shkaflar va mahsulot saqlash tizimini mantiqiy tashkil qilish.",
        3,
        60,
        20,
    ),
    (
        "L02_M05",
        "L02_M05_004",
        "Circulation va dining aloqasi",
        "practice",
        "Oshxona ichidagi harakat va dining bilan funksional bog'lanishni tashkil qilish.",
        4,
        60,
        20,
    ),
    (
        "L02_M05",
        "L02_M05_005",
        "Oshxona auditi",
        "practice",
        "Oshxona rejasini ergonomika, ish jarayoni va circulation bo'yicha tekshirish.",
        5,
        75,
        25,
    ),
]


# ============================================================
# CONTENT
# ============================================================

LEVEL02_MODULE05_CONTENT = {
    "L02_M05_001": [
        {
            "title": "Oshxona — faqat mebel qatori emas",
            "type": "highlight",
            "text": """
            Oshxona —
            uy ichidagi eng ko'p
            funksional harakat sodir bo'ladigan
            makonlardan biri.

            <br><br>

            Bu yerda:

            <br><br>

            • mahsulot olinadi;<br>
            • yuviladi;<br>
            • tayyorlanadi;<br>
            • pishiriladi;<br>
            • saqlanadi;<br>
            • ba'zan ovqatlaniladi.
            """,
        },
        {
            "title": "Asosiy zonalar",
            "type": "normal",
            "text": """
            Oshxonani bir nechta
            funksional zonaga ajratib
            fikrlash foydali:

            <br><br>

            • mahsulot saqlash;<br>
            • yuvish;<br>
            • tayyorlash;<br>
            • pishirish;<br>
            • idish saqlash;<br>
            • chiqindi bilan ishlash.
            """,
        },
        {
            "title": "Jarayon ketma-ketligi",
            "type": "highlight",
            "text": """
            Tasavvur qiling:

            <br><br>

            mahsulotni oldingiz →
            yuvdingiz →
            tayyorladingiz →
            pishirdingiz →
            ovqatni uzatdingiz.

            <br><br>

            Yaxshi oshxona
            shu jarayonni ortiqcha
            yurishsiz tashkil qiladi.
            """,
        },
        {
            "title": "Tasavvur qiling",
            "type": "example",
            "text": """
            Muzlatkich
            oshxonaning bir chetida.

            <br><br>

            Rakovina qarama-qarshi tomonda.

            <br><br>

            Pishirish zonasi esa
            ularning orasidagi
            asosiy circulation yo'lini kesib o'tadi.

            <br><br>

            Barcha jihozlar bor,
            lekin workflow yomon.
            """,
        },
        {
            "title": "Arxitektor savollari",
            "type": "normal",
            "text": """
            Oshxona rejasida so'rang:

            <br><br>

            • muzlatkich qayerda?<br>
            • rakovina qayerda?<br>
            • pishirish zonasi qayerda?<br>
            • tayyorlash uchun ishchi sirt bormi?<br>
            • diningga chiqish qulaymi?<br>
            • odamlar bir-biriga xalaqit bermaydimi?
            """,
        },
        {
            "title": "Mini-vazifa",
            "type": "example",
            "text": """
            Oddiy oshxona sxemasini chizing.

            <br><br>

            Unda belgilang:

            <br><br>

            F — Fridge<br>
            S — Sink<br>
            C — Cooking

            <br><br>

            Keyin ular orasidagi
            odam harakatini strelka bilan ko'rsating.
            """,
        },
    ],

    "L02_M05_002": [
        {
            "title": "Ishchi uchburchak nima?",
            "type": "highlight",
            "text": """
            Oshxona rejalashtirishda
            klassik tushunchalardan biri —
            ishchi uchburchak.

            <br><br>

            U uchta asosiy nuqtani
            bog'laydi:

            <br><br>

            <b>
            MUZLATKICH → RAKOVINA → PISHIRISH
            </b>
            """,
        },
        {
            "title": "Nega uchta nuqta?",
            "type": "normal",
            "text": """
            Kundalik ovqat tayyorlashda
            odam ko'p marta
            shu uch zona orasida yuradi.

            <br><br>

            Shuning uchun ularning
            o'zaro joylashuvi
            ish qulayligiga ta'sir qiladi.
            """,
        },
        {
            "title": "Uchburchak — qat'iy dekorativ shakl emas",
            "type": "warning",
            "text": """
            Ishchi uchburchak
            planda albatta chiroyli
            geometrik uchburchak chiqishi kerak
            degani emas.

            <br><br>

            Asosiy maqsad —
            ish jarayonini qulay tashkil qilish.
            """,
        },
        {
            "title": "Circulation bilan konflikt",
            "type": "example",
            "text": """
            Muzlatkichdan rakovinaga
            boradigan yo'l

            <br><br>

            diningga o'tadigan
            asosiy yo'l bilan kesishadi.

            <br><br>

            Ovqat tayyorlayotgan odam
            doim boshqa odamlar bilan
            to'qnashadi.

            <br><br>

            Bu yaxshi workflow emas.
            """,
        },
        {
            "title": "Island bo'lsa",
            "type": "normal",
            "text": """
            Kitchen island mavjud bo'lsa,
            u ham ish jarayoniga
            qo'shiladi.

            <br><br>

            Lekin island
            asosiy yurish yo'llarini
            toraytirib yubormasligi kerak.
            """,
        },
        {
            "title": "Bir tomonlama oshxona",
            "type": "normal",
            "text": """
            Har bir oshxonada
            an'anaviy uchburchak shakl
            hosil bo'lavermaydi.

            <br><br>

            Masalan,
            bir tomonlama kitchen line'da
            asosiy zonalar ketma-ket
            joylashishi mumkin.

            <br><br>

            Muhim narsa —
            workflow.
            """,
        },
        {
            "title": "Mini-vazifa",
            "type": "example",
            "text": """
            3 xil variant chizing:

            <br><br>

            1. L-shaped kitchen;<br>
            2. U-shaped kitchen;<br>
            3. Linear kitchen.

            <br><br>

            Har birida Fridge,
            Sink va Cooking joyini belgilang.
            """,
        },
    ],

    "L02_M05_003": [
        {
            "title": "Countertop — ishchi zona",
            "type": "highlight",
            "text": """
            Oshxonada jihozlarning
            o'zi yetarli emas.

            <br><br>

            Mahsulotni:

            <br><br>

            • qo'yish;<br>
            • tozalash;<br>
            • kesish;<br>
            • tayyorlash

            <br><br>

            uchun ishchi sirt kerak.
            """,
        },
        {
            "title": "Sink va cooking orasidagi ishchi sirt",
            "type": "example",
            "text": """
            Rakovinadan keyin
            mahsulot tayyorlanadi.

            <br><br>

            Keyin pishirish zonasiga o'tadi.

            <br><br>

            Shu sabab
            bu jarayon orasidagi
            countertop juda muhim.
            """,
        },
        {
            "title": "Saqlashni foydalanishga yaqinlashtiring",
            "type": "normal",
            "text": """
            Idishlar,
            mahsulotlar
            va oshxona anjomlari

            <br><br>

            ishlatiladigan zonaga
            mantiqan yaqin bo'lsa,
            ortiqcha yurish kamayadi.
            """,
        },
        {
            "title": "Pastki va yuqori saqlash",
            "type": "normal",
            "text": """
            Oshxona storage tizimi
            faqat bitta katta shkafdan iborat emas.

            <br><br>

            Turli predmetlar
            foydalanish tezligiga qarab
            turli joylarda saqlanishi mumkin.
            """,
        },
        {
            "title": "Corner muammosi",
            "type": "warning",
            "text": """
            L yoki U shaklli oshxonada
            burchak zonalari
            noto'g'ri rejalashtirilsa,

            <br><br>

            shkaf eshiklari
            yoki tortmalar
            bir-biri bilan konflikt qilishi mumkin.
            """,
        },
        {
            "title": "Jihoz eshigini ham tasavvur qiling",
            "type": "highlight",
            "text": """
            Muzlatkich,
            idish yuvish mashinasi
            yoki boshqa jihoz

            <br><br>

            faqat yopiq kontur holatida
            tekshirilmaydi.

            <br><br>

            Uning eshigi ochilganda
            qancha joy egallashini ham
            tasavvur qiling.
            """,
        },
        {
            "title": "Mini-vazifa",
            "type": "example",
            "text": """
            Oshxona sxemasida belgilang:

            <br><br>

            • food storage;<br>
            • dishes;<br>
            • preparation area;<br>
            • cleaning area;<br>
            • cooking area.

            <br><br>

            Ularning joylashuvi
            workflowga mos keladimi?
            """,
        },
    ],

    "L02_M05_004": [
        {
            "title": "Oshxona ichidagi circulation",
            "type": "highlight",
            "text": """
            Oshxonada bir vaqtning o'zida
            ovqat tayyorlash
            va boshqa odamlarning yurishi
            sodir bo'lishi mumkin.

            <br><br>

            Shu sabab circulation
            alohida tahlil qilinadi.
            """,
        },
        {
            "title": "Transit yo'lni ish zonasidan ajrating",
            "type": "normal",
            "text": """
            Agar hovliga,
            diningga
            yoki boshqa xonaga o'tadigan
            asosiy yo'l

            <br><br>

            doim cooking zonadan o'tsa,
            foydalanish noqulaylashishi mumkin.
            """,
        },
        {
            "title": "Dining bilan aloqa",
            "type": "highlight",
            "text": """
            Oshxona va dining
            ko'pincha bir-biriga
            kuchli funksional bog'langan.

            <br><br>

            Tayyor ovqatni
            diningga olib borish
            qulay bo'lishi kerak.
            """,
        },
        {
            "title": "Dining juda uzoqda",
            "type": "example",
            "text": """
            Oshxona bir tomonda,
            dining esa boshqa tomonda.

            <br><br>

            Ularning orasida
            koridor,
            living
            va asosiy circulation bor.

            <br><br>

            Har bir ovqatda
            uzoq yo'l bosiladi.

            <br><br>

            Funksional aloqa zaif.
            """,
        },
        {
            "title": "Bir nechta odam",
            "type": "normal",
            "text": """
            Faqat bitta odamni emas,
            oiladagi bir nechta odamni
            tasavvur qiling.

            <br><br>

            Biri muzlatkichni ochyapti,
            biri rakovinada,
            boshqasi diningga o'tmoqda.

            <br><br>

            Ular bir-biriga xalaqit bermasligi kerak.
            """,
        },
        {
            "title": "Door opening",
            "type": "warning",
            "text": """
            Oshxona eshigi ochilganda
            muzlatkich,
            shkaf
            yoki ishchi zonaga
            to'qnashmasligi kerak.
            """,
        },
        {
            "title": "Mini-vazifa",
            "type": "example",
            "text": """
            Oshxona planida 3 ta yo'l chizing:

            <br><br>

            1. Kirish → fridge<br>
            2. Kitchen → dining<br>
            3. Kitchen → hovli yoki boshqa xona

            <br><br>

            Ular asosiy ish zonasini
            keraksiz kesib o'tayaptimi?
            """,
        },
    ],

    "L02_M05_005": [
        {
            "title": "Oshxona auditi",
            "type": "highlight",
            "text": """
            Endi oshxonani
            faqat shkaflar chizig'i sifatida emas,

            <br><br>

            real kundalik ish tizimi
            sifatida tekshiramiz.
            """,
        },
        {
            "title": "1. Funksional zonalar",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • fridge mavjudmi?<br>
            • sink mantiqiy joydami?<br>
            • cooking zona qulaymi?<br>
            • preparation area bormi?<br>
            • storage yetarlimi?
            """,
        },
        {
            "title": "2. Workflow",
            "type": "example",
            "text": """
            Mahsulotning yo'lini kuzating:

            <br><br>

            saqlash →
            yuvish →
            tayyorlash →
            pishirish →
            dining.

            <br><br>

            Keraksiz ortiqcha yurish bormi?
            """,
        },
        {
            "title": "3. Circulation",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • boshqa odamlar ish zonasini kesadimi?<br>
            • jihoz eshiklari yo'lni to'sadimi?<br>
            • island o'tishni toraytirganmi?<br>
            • diningga chiqish qulaymi?
            """,
        },
        {
            "title": "4. Storage",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • kundalik idishlar qulay joydami?<br>
            • oziq-ovqat saqlash mantiqiymi?<br>
            • og'ir predmetlar uchun joy bormi?<br>
            • burchaklar foydalanishga yaroqlimi?
            """,
        },
        {
            "title": "Xatoni toping",
            "type": "warning",
            "text": """
            Oshxona juda katta.

            <br><br>

            Muzlatkich,
            sink
            va cooking zona
            hammasi mavjud.

            <br><br>

            Lekin ular
            uch xil uzoq burchakda.

            <br><br>

            Ovqat tayyorlashda
            odam xona bo'ylab
            qayta-qayta yuradi.

            <br><br>

            Muammo:
            maydon yetarli,
            lekin workflow samarasiz.
            """,
        },
        {
            "title": "Professional checklist",
            "type": "example",
            "text": """
            Oshxonani tekshiring:

            <br><br>

            <b>1.</b> Funksional zonalar aniqmi?<br><br>
            <b>2.</b> Fridge–Sink–Cooking aloqasi mantiqiymi?<br><br>
            <b>3.</b> Preparation surface bormi?<br><br>
            <b>4.</b> Storage foydalanishga yaqinmi?<br><br>
            <b>5.</b> Jihoz eshiklari konflikt qilmayaptimi?<br><br>
            <b>6.</b> Circulation ish zonasini buzmayaptimi?<br><br>
            <b>7.</b> Dining bilan aloqa qulaymi?
            """,
        },
        {
            "title": "Modul yakuni",
            "type": "highlight",
            "text": """
            Siz endi:

            <br><br>

            ✓ oshxona funksional zonalarini ajratasiz;<br>
            ✓ ishchi uchburchakni tushunasiz;<br>
            ✓ countertopni rejalashtirasiz;<br>
            ✓ storage mantiqini tuzasiz;<br>
            ✓ circulationni tekshirasiz;<br>
            ✓ dining bilan aloqani tahlil qilasiz;<br>
            ✓ oshxona rejasini audit qilasiz.

            <br><br>

            Keyingi modul:
            <b>Yotoqxona loyihalash.</b>
            """,
        },
    ],
}


# ============================================================
# QUIZ
# Q061-Q075 KODLARI SAQLANADI
# ============================================================

LEVEL02_MODULE05_QUIZ = {
    "L02_M05_001": [
        {
            "code": "L02_Q061",
            "question": "Oshxona faqat shkaflar joylashtiriladigan makonmi?",
            "explanation": (
                "Oshxona mahsulot saqlash, yuvish, tayyorlash va pishirish kabi ko'plab funksiyalarni bajaradi."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L02_Q062",
            "question": "Oshxona loyihalashda ish jarayonini hisobga olish kerakmi?",
            "explanation": (
                "Mahsulotning saqlashdan pishirishgacha bo'lgan yo'li ergonomikaga ta'sir qiladi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L02_Q063",
            "question": "Preparation area oshxonada foydali funksional zona hisoblanadimi?",
            "explanation": (
                "Mahsulotni kesish va tayyorlash uchun ishchi sirt zarur bo'lishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L02_M05_002": [
        {
            "code": "L02_Q064",
            "question": "Klassik ishchi uchburchakning asosiy nuqtalari qaysilar?",
            "explanation": (
                "Asosiy nuqtalar muzlatkich, rakovina va pishirish zonasidir."
            ),
            "options": [
                (
                    "A",
                    "Muzlatkich + Rakovina + Pishirish",
                    True,
                ),
                (
                    "B",
                    "Divan + TV + Stol",
                    False,
                ),
            ],
        },
        {
            "code": "L02_Q065",
            "question": "Ishchi uchburchakning asosiy maqsadi ish jarayonini qulay qilishmi?",
            "explanation": (
                "Uch asosiy zona orasidagi aloqani mantiqiy tashkil qilish nazarda tutiladi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L02_Q066",
            "question": "Har qanday oshxonada uchta zona geometrik jihatdan ideal uchburchak hosil qilishi shartmi?",
            "explanation": (
                "Oshxona turi va geometriyasi farq qiladi; asosiy narsa qulay workflow."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
    ],

    "L02_M05_003": [
        {
            "code": "L02_Q067",
            "question": "Oshxonada countertop ishchi sirt sifatida muhimmi?",
            "explanation": (
                "Mahsulotni qo'yish, kesish va tayyorlash uchun ishchi sirt kerak."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L02_Q068",
            "question": "Storage joylashuvi ish jarayoniga ta'sir qiladimi?",
            "explanation": (
                "Ko'p ishlatiladigan narsalarning qulay joyda bo'lishi ortiqcha harakatni kamaytirishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L02_Q069",
            "question": "Jihozning faqat yopiq holatini tekshirish yetarlimi?",
            "explanation": (
                "Jihoz eshigi ochilganda circulation va boshqa elementlar bilan konflikt yuzaga kelishi mumkin."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
    ],

    "L02_M05_004": [
        {
            "code": "L02_Q070",
            "question": "Diningga o'tadigan asosiy yo'l cooking zonani keraksiz kesib o'tmasligi foydalimi?",
            "explanation": (
                "Transit circulation va ish zonasi o'rtasidagi konflikt foydalanishni yomonlashtirishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L02_Q071",
            "question": "Oshxona va dining o'rtasidagi funksional aloqa muhimmi?",
            "explanation": (
                "Tayyor ovqat va idishlarni ikki zona orasida qulay tashish kundalik foydalanishga ta'sir qiladi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L02_Q072",
            "question": "Oshxona circulationini faqat bitta odam uchun tekshirish yetarlimi?",
            "explanation": (
                "Uyda bir vaqtning o'zida bir nechta odam oshxonadan foydalanishi mumkin."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
    ],

    "L02_M05_005": [
        {
            "code": "L02_Q073",
            "question": "Katta oshxona avtomatik ravishda ergonomik oshxona bo'ladimi?",
            "explanation": (
                "Maydondan tashqari zonalar aloqasi, workflow, storage va circulation ham muhim."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L02_Q074",
            "question": "Oshxona auditida Fridge–Sink–Cooking aloqasi tekshiriladimi?",
            "explanation": (
                "Bu asosiy ish jarayonining muhim qismi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L02_Q075",
            "question": "Oshxona rejasini baholashdagi to'g'ri yondashuv qaysi?",
            "explanation": (
                "Funksional zonalar, workflow, storage va circulation birgalikda tekshiriladi."
            ),
            "options": [
                (
                    "A",
                    "Zonalar → workflow → storage → circulation → audit",
                    True,
                ),
                (
                    "B",
                    "Faqat shkaflar sonini ko'paytirish",
                    False,
                ),
            ],
        },
    ],
}


# ============================================================
# DATABASE SEED
# ============================================================

def seed_level02_module05():
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
        ) in LEVEL02_MODULE05_LESSONS:

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
