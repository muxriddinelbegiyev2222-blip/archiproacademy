from database.database import get_connection


# ============================================================
# LEVEL 2
# MODULE 02 - FUNKSIONAL ZONALASH
# ============================================================

LEVEL02_MODULE02_LESSONS = [
    (
        "L02_M02",
        "L02_M02_001",
        "Funksional zonalash nima?",
        "theory",
        "Uy xonalarini vazifasi va foydalanish xarakteriga qarab guruhlash.",
        1,
        30,
        15,
    ),
    (
        "L02_M02",
        "L02_M02_002",
        "Public va private zonalar",
        "theory",
        "Mehmonlar zonasi bilan oilaning shaxsiy zonasini to'g'ri ajratish.",
        2,
        35,
        20,
    ),
    (
        "L02_M02",
        "L02_M02_003",
        "Service va xo'jalik zonasi",
        "theory",
        "Oshxona, kir yuvish, ombor va texnik xonalar o'rtasidagi aloqalarni tushunish.",
        3,
        35,
        20,
    ),
    (
        "L02_M02",
        "L02_M02_004",
        "Xonalar qo'shnichiligi",
        "practice",
        "Qaysi xonalar bir-biriga yaqin yoki uzoq bo'lishi kerakligini tahlil qilish.",
        4,
        40,
        20,
    ),
    (
        "L02_M02",
        "L02_M02_005",
        "Zonalashdagi tipik xatolar",
        "practice",
        "Real uy planlaridagi public, private va service zonalash xatolarini topish.",
        5,
        45,
        25,
    ),
]


# ============================================================
# LESSON CONTENT
# ============================================================

LEVEL02_MODULE02_CONTENT = {
    # ========================================================
    # 1-DARS
    # ========================================================

    "L02_M02_001": [
        {
            "title": "Funksional zonalash nima?",
            "type": "highlight",
            "text": """
            Funksional zonalash — uy ichidagi xonalarni
            ularning vazifasiga qarab
            <b>mantiqiy guruhlarga ajratish</b>.

            <br><br>

            Bu yaxshi plan yaratishning asosiy bosqichlaridan biridir.
            """,
        },
        {
            "title": "Nega kerak?",
            "type": "normal",
            "text": """
            Uyda barcha xonalar bir xil vazifani bajarmaydi.

            <br><br>

            Masalan:

            <br><br>

            • mehmonxona — mehmon va oilaviy muloqot uchun;<br>
            • yotoqxona — dam olish va maxfiylik uchun;<br>
            • oshxona — ovqat tayyorlash uchun;<br>
            • sanuzel — gigiyena uchun;<br>
            • texnik xona — uskunalar uchun.

            <br><br>

            Shuning uchun ularni tasodifiy joylashtirib bo'lmaydi.
            """,
        },
        {
            "title": "Tasavvur qiling",
            "type": "example",
            "text": """
            Mehmon uyga kirdi.

            <br><br>

            Mehmonxonaga borish uchun avval
            ota-onalar yotoqxonasidan o'tishi kerak.

            <br><br>

            Xonalar mavjud.

            <br>
            Maydon yetarli.

            <br><br>

            Lekin zonalash noto'g'ri.
            """,
        },
        {
            "title": "Asosiy zonalar",
            "type": "normal",
            "text": """
            Turar joyda ko'pincha uchta katta guruhni ko'ramiz:

            <br><br>

            <b>PUBLIC</b> — umumiy va mehmonlar zonasi.<br><br>

            <b>PRIVATE</b> — oilaning shaxsiy zonasi.<br><br>

            <b>SERVICE</b> — xizmat va xo'jalik zonasi.

            <br><br>

            Keyingi darslarda ularning har birini alohida o'rganamiz.
            """,
        },
        {
            "title": "Boshlovchi xatosi",
            "type": "warning",
            "text": """
            “Barcha xonalarni uchastkaga sig'dirdim,
            demak plan tayyor.”

            <br><br>

            Yo'q.

            <br><br>

            Professional plan faqat xonalar ro'yxati emas.

            <br><br>

            <b>Xonalar orasidagi aloqa ham loyihaning bir qismi.</b>
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            O'zingiz yashaydigan uyni xayolan uch rangga ajrating:

            <br><br>

            • Public<br>
            • Private<br>
            • Service

            <br><br>

            Qaysi zonalar bir-biriga aralashib ketganini kuzating.
            """,
        },
    ],

    # ========================================================
    # 2-DARS
    # ========================================================

    "L02_M02_002": [
        {
            "title": "Public zona",
            "type": "highlight",
            "text": """
            Public zona — mehmon va oila a'zolari
            birgalikda foydalanadigan makonlar.

            <br><br>

            Masalan:

            <br><br>

            • kirish;<br>
            • mehmonxona;<br>
            • umumiy zal;<br>
            • ovqatlanish zonasi;<br>
            • mehmonlar sanuzeli.
            """,
        },
        {
            "title": "Private zona",
            "type": "normal",
            "text": """
            Private zona — oilaning shaxsiy hayoti
            bilan bog'liq xonalar.

            <br><br>

            Masalan:

            <br><br>

            • ota-ona yotoqxonasi;<br>
            • bolalar xonalari;<br>
            • oilaviy sanuzel;<br>
            • garderob;<br>
            • ba'zan private family lounge.
            """,
        },
        {
            "title": "Nega ajratamiz?",
            "type": "example",
            "text": """
            Tasavvur qiling:

            <br><br>

            uyga 8 ta mehmon keldi.

            <br><br>

            Ular mehmonxonaga o'tish uchun
            bolalar yotoqxonasi oldidan,
            garderob oldidan va oilaviy sanuzel oldidan o'tadi.

            <br><br>

            Oila uchun maxfiylik kamayadi.
            """,
        },
        {
            "title": "Yaxshi prinsip",
            "type": "highlight",
            "text": """
            <b>
            Mehmon uyga kirganda private zonaga
            majburan chuqur kirib bormasligi kerak.
            </b>
            """,
        },
        {
            "title": "Lekin butunlay uzib tashlaymizmi?",
            "type": "normal",
            "text": """
            Yo'q.

            <br><br>

            Public va private zonalar orasida aloqa bo'ladi.

            <br><br>

            Masala — bu aloqani
            mantiqiy va nazorat qilinadigan qilish.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Bir uy planini toping.

            <br><br>

            Mehmon kirish eshigidan mehmonxonaga
            qanday yo'l bilan borishini kuzating.

            <br><br>

            U private zonani kesib o'tadimi?
            """,
        },
    ],

    # ========================================================
    # 3-DARS
    # ========================================================

    "L02_M02_003": [
        {
            "title": "Service zona nima?",
            "type": "highlight",
            "text": """
            Service zona uy hayotini qo'llab-quvvatlaydigan
            xizmat va xo'jalik makonlaridir.
            """,
        },
        {
            "title": "Nimalar kirishi mumkin?",
            "type": "normal",
            "text": """
            Uy dasturiga qarab:

            <br><br>

            • oshxona;<br>
            • pantry yoki ombor;<br>
            • kir yuvish xonasi;<br>
            • texnik xona;<br>
            • xo'jalik ombori;<br>
            • yordamchi kirish;<br>
            • ayrim sanuzellar

            <br><br>

            service tizimining bir qismi bo'lishi mumkin.
            """,
        },
        {
            "title": "Oshxona va ovqatlanish zonasi",
            "type": "example",
            "text": """
            Oshxona bilan ovqatlanish zonasi
            bir-biridan juda uzoq bo'lsa,
            har kuni ortiqcha yurish paydo bo'ladi.

            <br><br>

            Funksional qo'shnichilik
            kundalik hayotga bevosita ta'sir qiladi.
            """,
        },
        {
            "title": "Mahsulot olib kirish",
            "type": "example",
            "text": """
            Tasavvur qiling:

            <br><br>

            avtomobildan oziq-ovqat olib tushirdingiz.

            <br><br>

            Oshxonaga borish uchun
            butun mehmonxona va uzun koridordan o'tishingiz kerak.

            <br><br>

            Bu xizmat yo'nalishini qayta ko'rib chiqish uchun signal.
            """,
        },
        {
            "title": "Service zona ko'rinmas bo'lishi shartmi?",
            "type": "normal",
            "text": """
            Har doim emas.

            <br><br>

            Masalan, zamonaviy open-plan uyda
            oshxona public zonaning muhim qismiga aylanishi mumkin.

            <br><br>

            Muhim narsa — loyiha konsepsiyasi
            va oilaning yashash odati.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Bir uy planida quyidagi yo'lni tekshiring:

            <br><br>

            tashqi kirish → oshxona → pantry

            <br><br>

            Bu aloqa qanchalik qulay?
            """,
        },
    ],

    # ========================================================
    # 4-DARS
    # ========================================================

    "L02_M02_004": [
        {
            "title": "Xonalar qo'shnichiligi",
            "type": "highlight",
            "text": """
            Yaxshi planda faqat har bir xonaning
            o'lchami emas,

            <br><br>

            <b>qaysi xona qaysi xonaga yaqin joylashgani</b>
            ham muhim.
            """,
        },
        {
            "title": "Yaqin bo'lishi foydali bo'lgan aloqalar",
            "type": "normal",
            "text": """
            Masalan:

            <br><br>

            • oshxona ↔ ovqatlanish;<br>
            • master bedroom ↔ garderob;<br>
            • master bedroom ↔ private sanuzel;<br>
            • kirish ↔ garderob;<br>
            • bolalar xonalari ↔ oilaviy sanuzel.
            """,
        },
        {
            "title": "Uzoqroq bo'lishi kerak bo'lishi mumkin",
            "type": "normal",
            "text": """
            Ayrim kombinatsiyalarni ehtiyotkor hal qilish kerak.

            <br><br>

            Masalan:

            <br><br>

            • shovqinli mehmonxona ↔ chaqaloq yotoqxonasi;<br>
            • texnik xona ↔ jim dam olish xonasi;<br>
            • asosiy mehmon yo'li ↔ private garderob.
            """,
        },
        {
            "title": "Bubble diagram",
            "type": "example",
            "text": """
            Professional plan boshlashdan oldin
            xonalarni darhol devor bilan chizish shart emas.

            <br><br>

            Avval doiralar bilan:

            <br><br>

            OSHXONA ↔ OVQATLANISH ↔ MEHMONXONA

            <br><br>

            kabi aloqalarni ko'rsatish mumkin.

            <br><br>

            Bu <b>bubble diagram</b> fikrlash usulidir.
            """,
        },
        {
            "title": "Boshlovchi xatosi",
            "type": "warning",
            "text": """
            Chiroyli to'rtburchak xonalarni
            birma-bir joylashtirib chiqish,
            lekin ular orasidagi aloqani
            oxirida o'ylash katta xato.

            <br><br>

            Aloqalar boshidan o'ylanadi.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Quyidagi 6 xona uchun
            qaysilari bir-biriga yaqin bo'lishini yozing:

            <br><br>

            • kirish<br>
            • mehmonxona<br>
            • oshxona<br>
            • ota-ona yotoqxonasi<br>
            • garderob<br>
            • sanuzel

            <br><br>

            Keyin oddiy bubble diagram tasavvur qiling.
            """,
        },
    ],

    # ========================================================
    # 5-DARS
    # ========================================================

    "L02_M02_005": [
        {
            "title": "Zonalash xatolarini ovlaymiz",
            "type": "highlight",
            "text": """
            Endi plan ichidagi xonalarni emas,
            butun uy hayotini tahlil qilamiz.
            """,
        },
        {
            "title": "Xato 1 — mehmon private zonada",
            "type": "warning",
            "text": """
            Mehmonxona uyning eng ichkarisida.

            <br><br>

            Unga borish uchun barcha yotoqxonalardan o'tiladi.

            <br><br>

            Public va private zonalar
            bir-biriga aralashib ketgan.
            """,
        },
        {
            "title": "Xato 2 — oshxona uzoqda",
            "type": "warning",
            "text": """
            Oshxona ovqatlanish zonasidan juda uzoq.

            <br><br>

            Har bir taom uchun uzun yo'l bosiladi.

            <br><br>

            Kundalik harakat keraksiz ko'payadi.
            """,
        },
        {
            "title": "Xato 3 — mehmon sanuzeli noto'g'ri joyda",
            "type": "warning",
            "text": """
            Mehmon sanuzelga borishi uchun
            oilaning yotoq zonasi ichiga kiradi.

            <br><br>

            Bu maxfiylikni buzishi mumkin.
            """,
        },
        {
            "title": "Xato 4 — service yo'li public markazdan o'tadi",
            "type": "warning",
            "text": """
            Xo'jalik chiqindisi yoki kir yuvish
            harakati doim asosiy mehmon zonasidan o'tadi.

            <br><br>

            Service oqimi qayta tashkil qilinishi mumkin.
            """,
        },
        {
            "title": "Xato 5 — koridor hamma narsani hal qilmoqda",
            "type": "warning",
            "text": """
            Xonalar orasidagi har bir muammo
            yana bitta uzun koridor bilan hal qilingan.

            <br><br>

            Natijada foydali maydon kamayadi
            va uy parchalanib ketadi.
            """,
        },
        {
            "title": "Professional tekshiruv",
            "type": "example",
            "text": """
            Plan oldingizda bo'lsa:

            <br><br>

            <b>1.</b> Public zona qayerda?<br><br>
            <b>2.</b> Private zona qayerda?<br><br>
            <b>3.</b> Service zona qayerda?<br><br>
            <b>4.</b> Mehmon qayerlargacha kiradi?<br><br>
            <b>5.</b> Kundalik service yo'llari qanday?<br><br>
            <b>6.</b> Qaysi xonalar noto'g'ri qo'shni?
            """,
        },
        {
            "title": "Mini-loyiha",
            "type": "example",
            "text": """
            Internetdan 150–250 m²
            bir qavatli uy planini toping.

            <br><br>

            Uch rang bilan xayolan ajrating:

            <br><br>

            PUBLIC<br>
            PRIVATE<br>
            SERVICE

            <br><br>

            Keyin kamida 3 ta yaxshi aloqa
            va 2 ta yaxshilash mumkin bo'lgan aloqani yozing.
            """,
        },
        {
            "title": "Modul yakuni",
            "type": "highlight",
            "text": """
            Siz endi:

            <br><br>

            ✓ funksional zonalash;<br>
            ✓ public zona;<br>
            ✓ private zona;<br>
            ✓ service zona;<br>
            ✓ xonalar qo'shnichiligi;<br>
            ✓ bubble diagram

            <br><br>

            tushunchalari asosida plan haqida
            professionalroq fikrlay olasiz.

            <br><br>

            Keyingi modul:
            <b>Harakat va sirkulyatsiya.</b>
            """,
        },
    ],
}


# ============================================================
# QUIZ DATA
# ============================================================

LEVEL02_MODULE02_QUIZ = {
    "L02_M02_001": [
        {
            "code": "L02_Q016",
            "question": "Funksional zonalash nima?",
            "explanation": (
                "Xonalarni ularning vazifasi va foydalanish xarakteriga qarab mantiqiy guruhlash."
            ),
            "options": [
                ("A", "Xonalarni vazifasiga qarab guruhlash", True),
                ("B", "Faqat devor rangini tanlash", False),
                ("C", "Faqat fasad chizish", False),
            ],
        },
        {
            "code": "L02_Q017",
            "question": "Barcha xonalarni uchastkaga sig'dirishning o'zi yaxshi plan uchun yetarlimi?",
            "explanation": (
                "Xonalar orasidagi aloqa va zonalash ham muhim."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L02_Q018",
            "question": "Turar joyda public, private va service zonalar bo'lishi mumkinmi?",
            "explanation": (
                "Bu turar joyni funksional guruhlarga ajratishning keng tarqalgan usullaridan biridir."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L02_M02_002": [
        {
            "code": "L02_Q019",
            "question": "Yotoqxona odatda qaysi zonaga yaqin?",
            "explanation": (
                "Yotoqxona odatda oilaning private zonasiga kiradi."
            ),
            "options": [
                ("A", "Private", True),
                ("B", "Public", False),
                ("C", "Faqat service", False),
            ],
        },
        {
            "code": "L02_Q020",
            "question": "Mehmon private zona ichidan majburan o'tishi yaxshi yechimmi?",
            "explanation": (
                "Bu oilaning maxfiyligini kamaytirishi mumkin."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Ko'pincha yo'q", True),
            ],
        },
        {
            "code": "L02_Q021",
            "question": "Mehmonxona odatda public zonaga kiradimi?",
            "explanation": (
                "Mehmonxona umumiy va mehmonlar foydalanadigan makon hisoblanadi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L02_M02_003": [
        {
            "code": "L02_Q022",
            "question": "Pantry oshxonaga yaqin bo'lishi foydalimi?",
            "explanation": (
                "Oziq-ovqat saqlash va tayyorlash funksiyalari o'zaro bog'liq."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L02_Q023",
            "question": "Service zona faqat bitta xona deganimi?",
            "explanation": (
                "Service zona bir nechta xizmat va xo'jalik xonalaridan iborat bo'lishi mumkin."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L02_Q024",
            "question": "Open-plan oshxona public zona bilan birlashishi mumkinmi?",
            "explanation": (
                "Loyiha konsepsiyasi va oilaning yashash odatiga qarab mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Hech qachon", False),
            ],
        },
    ],

    "L02_M02_004": [
        {
            "code": "L02_Q025",
            "question": "Master bedroom va garderobning yaqin joylashishi foydali bo'lishi mumkinmi?",
            "explanation": (
                "Bu ikki funksiya kundalik foydalanishda bir-biri bilan bevosita bog'liq."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L02_Q026",
            "question": "Bubble diagram nima uchun foydali?",
            "explanation": (
                "Xonalarni devor chizishdan oldin ularning funksional aloqalarini ko'rishga yordam beradi."
            ),
            "options": [
                ("A", "Xonalar aloqasini rejalash uchun", True),
                ("B", "Faqat fasad rangini tanlash uchun", False),
            ],
        },
        {
            "code": "L02_Q027",
            "question": "Xonalar aloqasini faqat plan oxirida o'ylash to'g'rimi?",
            "explanation": (
                "Funksional aloqalar loyiha boshidan shakllantiriladi."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
    ],

    "L02_M02_005": [
        {
            "code": "L02_Q028",
            "question": "Mehmon sanuzelga borish uchun private yotoq zonasi ichidan o'tsa muammo bo'lishi mumkinmi?",
            "explanation": (
                "Bu maxfiylik va funksional zonalashni buzishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L02_Q029",
            "question": "Har bir funksional muammoni uzun koridor bilan hal qilish yaxshi yechimmi?",
            "explanation": (
                "Ortiqcha koridor foydali maydonni kamaytirishi va plan aloqalarini zaiflashtirishi mumkin."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L02_Q030",
            "question": "Professional zonalash tahlilida qaysi savol muhim?",
            "explanation": (
                "Public, private va service zonalarning joylashuvi plan funksiyasini tushunishga yordam beradi."
            ),
            "options": [
                ("A", "Public va private zonalar qayerda?", True),
                ("B", "Faqat fasad materiali qancha turadi?", False),
            ],
        },
    ],
}


# ============================================================
# DATABASE SEED
# ============================================================

def seed_level02_module02():
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
        ) in LEVEL02_MODULE02_LESSONS:

            cursor.execute(
                """
                SELECT id
                FROM course_modules
                WHERE code = ?
                LIMIT 1
                """,
                (
                    module_code,
                ),
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
