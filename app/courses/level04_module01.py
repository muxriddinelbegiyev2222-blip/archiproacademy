from database.database import get_connection


# ============================================================
# LEVEL 4
# MODULE 01 - O'ZBEK OILASI UCHUN UY
# ============================================================

LEVEL04_MODULE01_LESSONS = [
    (
        "L04_M01",
        "L04_M01_001",
        "Oila hayoti va uy rejasi",
        "theory",
        "Oilaviy turmush tarzini loyiha rejasiga aylantirish.",
        1,
        40,
        20,
    ),
    (
        "L04_M01",
        "L04_M01_002",
        "Public va private hayot",
        "theory",
        "Mehmon va oilaviy kundalik zonalarni to'g'ri ajratish.",
        2,
        40,
        20,
    ),
    (
        "L04_M01",
        "L04_M01_003",
        "Oila tarkibi va xonalar",
        "theory",
        "Ota-ona, bolalar va boshqa oila a'zolari ehtiyojlarini rejalashtirish.",
        3,
        45,
        20,
    ),
    (
        "L04_M01",
        "L04_M01_004",
        "Uy va hovli aloqasi",
        "practice",
        "Ichki yashash zonalarini hovli bilan funksional bog'lash.",
        4,
        45,
        20,
    ),
    (
        "L04_M01",
        "L04_M01_005",
        "O'zbek oilasi uchun plan auditi",
        "practice",
        "Mahalliy oilaviy turmushga mos va nomos reja yechimlarini tahlil qilish.",
        5,
        55,
        25,
    ),
]


# ============================================================
# CONTENT
# ============================================================

LEVEL04_MODULE01_CONTENT = {
    "L04_M01_001": [
        {
            "title": "Uy odamlar uchun loyihalanadi",
            "type": "highlight",
            "text": """
            Bir xil maydondagi uy
            turli oilalar uchun
            butunlay boshqacha ishlashi mumkin.

            <br><br>

            Shuning uchun professional loyiha
            xonalar sonidan emas,
            <b>oila hayotini tushunishdan</b> boshlanadi.
            """,
        },
        {
            "title": "Birinchi savollar",
            "type": "normal",
            "text": """
            Loyiha boshida aniqlanadi:

            <br><br>

            • oilada nechta odam bor;<br>
            • bolalar yoshi;<br>
            • mehmonlar tez-tez keladimi;<br>
            • katta avlod yashaydimi;<br>
            • oilaning kundalik odatlari qanday;<br>
            • hovlidan qanday foydalaniladi.
            """,
        },
        {
            "title": "Tasavvur qiling",
            "type": "example",
            "text": """
            Ikki oilada ham 4 kishi yashaydi.

            <br><br>

            Birinchi oilada mehmonlar kam keladi.

            <br><br>

            Ikkinchi oilada esa
            har hafta katta mehmon yig'ilishi bo'ladi.

            <br><br>

            Odam soni bir xil,
            lekin uy rejasi bir xil bo'lishi shart emas.
            """,
        },
        {
            "title": "Xona emas — ssenariy",
            "type": "highlight",
            "text": """
            Arxitektor:

            <br><br>

            “Mehmonxona nechchi m²?”

            <br><br>

            savolidan oldin:

            <br><br>

            <b>
            “Bu xonada odamlar qanday yashaydi?”
            </b>

            <br><br>

            deb o'ylashi kerak.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Bir oila uchun 10 ta savol tuzing.

            <br><br>

            Bu savollar
            xonalar sonidan tashqari
            real turmush tarzini aniqlashi kerak.
            """,
        },
    ],

    "L04_M01_002": [
        {
            "title": "Public va private hayot",
            "type": "highlight",
            "text": """
            Uyda barcha zonalar
            bir xil darajada ochiq bo'lmaydi.

            <br><br>

            Mehmon foydalanadigan zonalar bilan
            oilaning private zonalari
            o'rtasida mantiqiy chegara bo'lishi mumkin.
            """,
        },
        {
            "title": "Public zona",
            "type": "normal",
            "text": """
            Public zona tarkibiga:

            <br><br>

            • kirish;<br>
            • mehmonxona;<br>
            • guest sanuzel;<br>
            • ayrim hollarda dining

            <br><br>

            kirishi mumkin.
            """,
        },
        {
            "title": "Private zona",
            "type": "normal",
            "text": """
            Private zona odatda:

            <br><br>

            • yotoqxona;<br>
            • bolalar xonasi;<br>
            • family room;<br>
            • private sanuzel

            <br><br>

            bilan bog'lanadi.
            """,
        },
        {
            "title": "Mehmon yo'li",
            "type": "example",
            "text": """
            Mehmon kirib,
            yotoqxona koridori orqali
            mehmonxonaga o'tsa,

            <br><br>

            private zona buzilishi mumkin.
            """,
        },
        {
            "title": "Guest sanuzel",
            "type": "example",
            "text": """
            Mehmon sanuzelga borish uchun
            master bedroom yonidan o'tishi kerak bo'lsa,

            <br><br>

            zonalash zaif.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Bir uy rejasini oling.

            <br><br>

            Ikki rang bilan:

            <br><br>

            PUBLIC

            va

            PRIVATE

            <br><br>

            zonalarni belgilang.

            <br><br>

            Ular qayerda kesishayotganini toping.
            """,
        },
    ],

    "L04_M01_003": [
        {
            "title": "Oila tarkibi rejani o'zgartiradi",
            "type": "highlight",
            "text": """
            Oilada kim yashashi
            xona soni va aloqalariga
            bevosita ta'sir qiladi.
            """,
        },
        {
            "title": "Ota-ona",
            "type": "normal",
            "text": """
            Master bedroom uchun:

            <br><br>

            • privacy;<br>
            • garderob;<br>
            • sanuzel bilan aloqa;<br>
            • shovqindan himoya

            <br><br>

            ko'rib chiqilishi mumkin.
            """,
        },
        {
            "title": "Bolalar",
            "type": "normal",
            "text": """
            Bolalar xonasi:

            <br><br>

            • uyqu;<br>
            • o'qish;<br>
            • saqlash;<br>
            • o'yin

            <br><br>

            funksiyalarini birlashtirishi mumkin.
            """,
        },
        {
            "title": "Katta avlod",
            "type": "example",
            "text": """
            Agar uyda katta yoshli ota-ona yashasa,

            <br><br>

            zinapoya,
            sanuzel masofasi,
            kirish qulayligi
            va privacy alohida ahamiyatga ega bo'ladi.
            """,
        },
        {
            "title": "Kelajakni o'ylash",
            "type": "highlight",
            "text": """
            Bolalar ulg'ayadi.

            <br><br>

            Oila tarkibi o'zgarishi mumkin.

            <br><br>

            Kuchli reja faqat bugungi kun emas,
            ma'lum darajada kelajakni ham hisobga oladi.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            4 kishilik oila uchun
            xona ro'yxati tuzing.

            <br><br>

            Keyin shu oilaga
            katta yoshli bitta ota-ona
            qo'shilsa,

            <br><br>

            rejada nima o'zgarishini yozing.
            """,
        },
    ],

    "L04_M01_004": [
        {
            "title": "O'zbekistonda hovli muhim yashash makoni",
            "type": "highlight",
            "text": """
            Hovlili uyda
            tashqi makon ko'pincha
            kundalik hayotning faol qismi bo'ladi.

            <br><br>

            Shu sababli uy va hovli
            bir-biridan ajralgan tizim emas.
            """,
        },
        {
            "title": "Living → hovli",
            "type": "normal",
            "text": """
            Living yoki family room
            private hovliga yaxshi ulangan bo'lsa,

            <br><br>

            ichki va tashqi hayot
            bir-birini davom ettiradi.
            """,
        },
        {
            "title": "Oshxona → tashqi dining",
            "type": "example",
            "text": """
            Yozgi ovqatlanish tez-tez ishlatilsa,

            <br><br>

            oshxona bilan
            tashqi dining orasidagi
            aloqa qisqa va tushunarli bo'lishi foydali.
            """,
        },
        {
            "title": "Bolalar va hovli",
            "type": "normal",
            "text": """
            Bolalar hovlida o'ynaganda
            ularni living yoki oshxonadan
            kuzatish imkoniyati foydali bo'lishi mumkin.
            """,
        },
        {
            "title": "Privacy",
            "type": "warning",
            "text": """
            Hovli oilaviy foydalanish uchun yaratilgan,
            lekin ko'chadan to'liq ko'rinib tursa,

            <br><br>

            uning private xarakteri zaiflashadi.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Plan va genplanni birga oling.

            <br><br>

            Quyidagi aloqalarni chizing:

            <br><br>

            living → hovli<br>
            kitchen → outdoor dining<br>
            bolalar xonasi → family hovli
            """,
        },
    ],

    "L04_M01_005": [
        {
            "title": "Plan auditini boshlaymiz",
            "type": "highlight",
            "text": """
            Endi uyga
            faqat chiroyli plan sifatida emas,

            <br><br>

            real O'zbek oilasi yashaydigan
            tizim sifatida qaraymiz.
            """,
        },
        {
            "title": "Xato 1 — mehmon private zonada",
            "type": "warning",
            "text": """
            Mehmonxonaga borish uchun
            yotoqxona koridoridan o'tish kerak.
            """,
        },
        {
            "title": "Xato 2 — guest sanuzel uzoqda",
            "type": "warning",
            "text": """
            Mehmonlar private sanuzeldan
            foydalanishga majbur.
            """,
        },
        {
            "title": "Xato 3 — oshxona hovlidan uzilgan",
            "type": "warning",
            "text": """
            Yozgi ovqatlanish mavjud.

            <br><br>

            Lekin oshxonadan u yerga
            uzoq yo'l orqali chiqiladi.
            """,
        },
        {
            "title": "Xato 4 — family hovli parking bilan aralashgan",
            "type": "warning",
            "text": """
            Bolalar va oilaviy dam olish zonasi
            avtomobil yo'li bilan bir xil maydonda.
            """,
        },
        {
            "title": "Xato 5 — oila ehtiyoji noto'g'ri tushunilgan",
            "type": "warning",
            "text": """
            Uyda 5 kishi yashaydi,
            lekin saqlash joylari,
            sanuzel yoki kundalik family zona
            yetarli emas.
            """,
        },
        {
            "title": "Professional checklist",
            "type": "example",
            "text": """
            Rejani tekshiring:

            <br><br>

            <b>1.</b> Oilada kim yashaydi?<br><br>
            <b>2.</b> Mehmon qayerdan kiradi?<br><br>
            <b>3.</b> Private zona himoyalanganmi?<br><br>
            <b>4.</b> Guest sanuzel qulaymi?<br><br>
            <b>5.</b> Living hovliga ulanganmi?<br><br>
            <b>6.</b> Kitchen tashqi diningga qulaymi?<br><br>
            <b>7.</b> Bolalar zonasi xavfsizmi?
            """,
        },
        {
            "title": "Mini-case",
            "type": "example",
            "text": """
            Oila:

            <br><br>

            ota + ona + 2 bola.

            <br><br>

            Talablar:

            <br><br>

            • alohida mehmonxona;<br>
            • family living;<br>
            • 2 bolalar xonasi;<br>
            • master bedroom;<br>
            • guest sanuzel;<br>
            • private hovli;<br>
            • tashqi dining.

            <br><br>

            Bubble diagram yarating.

            <br><br>

            Har bir zona nega
            aynan shu joyda ekanini yozing.
            """,
        },
        {
            "title": "Modul yakuni",
            "type": "highlight",
            "text": """
            Siz endi:

            <br><br>

            ✓ oila turmush tarzini tahlil qilish;<br>
            ✓ public/private zonalarni ajratish;<br>
            ✓ oila tarkibiga mos xona yaratish;<br>
            ✓ uy-hovli aloqasini qurish;<br>
            ✓ mahalliy turmushga mos plan auditini qilish

            <br><br>

            ko'nikmalariga ega bo'ldingiz.

            <br><br>

            Keyingi modul:
            <b>Mehmon kutish madaniyati.</b>
            """,
        },
    ],
}


# ============================================================
# QUIZ
# ============================================================

LEVEL04_MODULE01_QUIZ = {
    "L04_M01_001": [
        {
            "code": "L04_Q001",
            "question": "Bir xil odam soniga ega ikki oilaning uy rejasi doim bir xil bo'lishi kerakmi?",
            "explanation": (
                "Oilalarning mehmon, kundalik hayot va boshqa ehtiyojlari turlicha bo'lishi mumkin."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L04_Q002",
            "question": "Loyiha boshida oilaning kundalik turmush tarzi o'rganiladimi?",
            "explanation": (
                "Uy rejasining asosiy qarorlari foydalanuvchi hayotiga bog'liq."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L04_Q003",
            "question": "Arxitektorda faqat xona maydonini bilish yetarlimi?",
            "explanation": (
                "Xonaning qanday ishlatilishini ham tushunish kerak."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
    ],

    "L04_M01_002": [
        {
            "code": "L04_Q004",
            "question": "Mehmon yo'li private yotoqxona zonasidan o'tishi yaxshi zonalashmi?",
            "explanation": (
                "Public va private oqimlarni imkon qadar mantiqiy ajratish foydali."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L04_Q005",
            "question": "Guest sanuzel public zonaga qulay bog'langan bo'lishi foydalimi?",
            "explanation": (
                "Mehmon private oilaviy zonaga chuqur kirmasdan undan foydalana oladi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L04_Q006",
            "question": "Public va private zonalar uy rejasida farqlanishi mumkinmi?",
            "explanation": (
                "Ular turli foydalanuvchi va privacy darajalariga ega."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L04_M01_003": [
        {
            "code": "L04_Q007",
            "question": "Oila tarkibi xona rejasiga ta'sir qiladimi?",
            "explanation": (
                "Bolalar, ota-ona va katta avlodning ehtiyojlari turlicha."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L04_Q008",
            "question": "Katta yoshli oila a'zosi uchun kirish va sanuzel qulayligi muhim bo'lishi mumkinmi?",
            "explanation": (
                "Yosh va harakat imkoniyati rejalash qarorlariga ta'sir qiladi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L04_Q009",
            "question": "Uy rejasi faqat bugungi oilaviy holatni hisobga olishi kerakmi?",
            "explanation": (
                "Ma'lum darajada kelajakdagi o'zgarishlarni ham hisobga olish foydali."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
    ],

    "L04_M01_004": [
        {
            "code": "L04_Q010",
            "question": "Living va private hovli o'rtasidagi aloqa muhimmi?",
            "explanation": (
                "Ichki va tashqi family makonlari bir-birini davom ettirishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L04_Q011",
            "question": "Oshxona bilan tashqi dining orasidagi aloqa kundalik qulaylikka ta'sir qiladimi?",
            "explanation": (
                "Ovqat va idishlarni tashish yo'li qisqa va mantiqiy bo'lishi foydali."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L04_Q012",
            "question": "Family hovli ko'chadan to'liq ochiq bo'lsa privacy zaiflashishi mumkinmi?",
            "explanation": (
                "Private tashqi makonning tashqi ko'rinishdan himoyasi muhim bo'lishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L04_M01_005": [
        {
            "code": "L04_Q013",
            "question": "Mehmon private zona orqali yurishi plan auditi xatosi bo'lishi mumkinmi?",
            "explanation": (
                "Public circulation private oilaviy zonani buzmasligi kerak."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L04_Q014",
            "question": "Family hovli va avtomobil yo'li bir-biriga xalaqit berishi mumkinmi?",
            "explanation": (
                "Bolalar va oilaviy dam olish zonasi avtomobil harakatidan xavfsiz ajratilishi foydali."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L04_Q015",
            "question": "O'zbek oilasi uchun uy rejasining boshlang'ich asosiy savoli qaysi?",
            "explanation": (
                "Avval oilaning real turmush tarzi va ehtiyojlari tushuniladi."
            ),
            "options": [
                ("A", "Bu oila qanday yashaydi?", True),
                ("B", "Faqat fasad qaysi rangda bo'ladi?", False),
            ],
        },
    ],
}


# ============================================================
# DATABASE SEED
# ============================================================

def seed_level04_module01():
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
        ) in LEVEL04_MODULE01_LESSONS:

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
