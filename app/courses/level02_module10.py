from database.database import get_connection


# ============================================================
# LEVEL 2
# MODULE 10 - YAKUNIY FAZOVIY TAHLIL
# ============================================================

LEVEL02_MODULE10_LESSONS = [
    (
        "L02_M10",
        "L02_M10_001",
        "Uy planini professional tahlil qilish",
        "theory",
        "Butun uy planini yagona algoritm asosida bosqichma-bosqich tahlil qilish.",
        1,
        40,
        25,
    ),
    (
        "L02_M10",
        "L02_M10_002",
        "Zonalar va aloqalarni tekshirish",
        "practice",
        "Public, private va service zonalar hamda xona qo'shnichiligini kompleks tahlil qilish.",
        2,
        40,
        25,
    ),
    (
        "L02_M10",
        "L02_M10_003",
        "Ergonomika va sirkulyatsiya auditi",
        "practice",
        "Mebel, eshik, yurish yo'llari va foydalanish zonalaridagi muammolarni aniqlash.",
        3,
        45,
        25,
    ),
    (
        "L02_M10",
        "L02_M10_004",
        "Xonalar bo'yicha professional audit",
        "practice",
        "Oshxona, living, yotoqxona, sanuzel va bolalar xonasini alohida tekshirish.",
        4,
        45,
        30,
    ),
    (
        "L02_M10",
        "L02_M10_005",
        "LEVEL 2 yakuniy case",
        "case",
        "Bitta turar joy planini to'liq tahlil qilish, xatolarni aniqlash va yechim taklif qilish.",
        5,
        60,
        40,
    ),
]


# ============================================================
# CONTENT
# ============================================================

LEVEL02_MODULE10_CONTENT = {
    "L02_M10_001": [
        {
            "title": "Endi butun uyga qaraymiz",
            "type": "highlight",
            "text": """
            Shu paytgacha biz alohida mavzularni o'rgandik.

            <br><br>

            Endi professional tahlilda
            ularning barchasini birlashtiramiz.

            <br><br>

            <b>
            Yaxshi plan — yaxshi ishlaydigan tizim.
            </b>
            """,
        },
        {
            "title": "1-bosqich — uy kim uchun?",
            "type": "normal",
            "text": """
            Plan tahlilini xonalardan emas,
            foydalanuvchidan boshlang.

            <br><br>

            Savollar:

            <br><br>

            • oilada nechta odam bor?<br>
            • bolalar bormi?<br>
            • mehmon ko'p keladimi?<br>
            • hovlida ko'p vaqt o'tkaziladimi?<br>
            • uyda ishlash kerakmi?<br>
            • bir yoki ikki avlod yashaydimi?
            """,
        },
        {
            "title": "2-bosqich — zonalar",
            "type": "normal",
            "text": """
            Keyin butun planni uch katta qatlamda ko'ring:

            <br><br>

            <b>PUBLIC</b><br>
            <b>PRIVATE</b><br>
            <b>SERVICE</b>

            <br><br>

            Ular mantiqiy joylashganmi?
            """,
        },
        {
            "title": "3-bosqich — harakat",
            "type": "normal",
            "text": """
            Keyin odamlarni plan ichida yurgizing.

            <br><br>

            Masalan:

            <br><br>

            kirish → living<br>
            kirish → oshxona<br>
            yotoqxona → sanuzel<br>
            oshxona → dining<br>
            living → hovli
            """,
        },
        {
            "title": "4-bosqich — xonalar",
            "type": "normal",
            "text": """
            Endi har bir asosiy xonani
            alohida tekshiring.

            <br><br>

            Faqat m² emas.

            <br><br>

            Uning:

            <br><br>

            • proporsiyasi;<br>
            • mebeli;<br>
            • foydali devorlari;<br>
            • eshiklari;<br>
            • derazalari;<br>
            • foydalanish zonalari

            <br><br>

            tekshiriladi.
            """,
        },
        {
            "title": "Professional odat",
            "type": "highlight",
            "text": """
            <b>
            Plan ko'rganda darhol
            “chiroyli” yoki “xunuk” demang.

            Avval nima ishlayotgani va
            nima ishlamayotganini aniqlang.
            </b>
            """,
        },
    ],

    "L02_M10_002": [
        {
            "title": "Zonalash auditi",
            "type": "highlight",
            "text": """
            Birinchi katta savol:

            <br><br>

            <b>
            Uy ichidagi funksiyalar
            to'g'ri guruhlanganmi?
            </b>
            """,
        },
        {
            "title": "Public zona",
            "type": "normal",
            "text": """
            Tekshiring:

            <br><br>

            • kirish tushunarlimi?<br>
            • mehmonxona oson topiladimi?<br>
            • mehmon sanuzeli qulaymi?<br>
            • dining oshxonaga yaqinmi?<br>
            • hovli bilan aloqa yaxshimi?
            """,
        },
        {
            "title": "Private zona",
            "type": "normal",
            "text": """
            Tekshiring:

            <br><br>

            • yotoqxonalar bir tizimmi?<br>
            • mehmonlar private zonani kesadimi?<br>
            • sanuzelga tungi yo'l qulaymi?<br>
            • bolalar va ota-onalar aloqasi mantiqiymi?
            """,
        },
        {
            "title": "Service zona",
            "type": "normal",
            "text": """
            Tekshiring:

            <br><br>

            • oshxona va pantry aloqasi;<br>
            • mahsulot olib kirish;<br>
            • laundry yoki xo'jalik zonasi;<br>
            • texnik xonalar;<br>
            • service chiqishlari.
            """,
        },
        {
            "title": "Qo'shnichilik xatosi",
            "type": "warning",
            "text": """
            Har bir xona alohida yaxshi bo'lishi mumkin.

            <br><br>

            Lekin noto'g'ri qo'shnichilik
            butun planni zaiflashtiradi.

            <br><br>

            Masalan:

            <br><br>

            shovqinli living ↔ bolalar yotoqxonasi.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Istalgan uy planini olib,
            faqat zonalash bo'yicha
            5 ta kuchli va 5 ta zaif nuqtani yozing.
            """,
        },
    ],

    "L02_M10_003": [
        {
            "title": "Ergonomika auditi",
            "type": "highlight",
            "text": """
            Endi plan ichidagi odamga qaytamiz.

            <br><br>

            Har bir xona real foydalanishda ishlaydimi?
            """,
        },
        {
            "title": "Eshiklar",
            "type": "normal",
            "text": """
            Tekshiring:

            <br><br>

            • eshik boshqa eshikka uriladimi;<br>
            • mebelga uriladimi;<br>
            • odamni tor burchakka yo'naltiradimi;<br>
            • foydali devorni keraksiz bo'lib tashlaganmi.
            """,
        },
        {
            "title": "Mebel",
            "type": "normal",
            "text": """
            Har bir mebel uchun:

            <br><br>

            • o'zi sig'dimi;<br>
            • undan foydalanish mumkinmi;<br>
            • oldida joy bormi;<br>
            • boshqa mebel bilan konflikt bormi

            <br><br>

            tekshiriladi.
            """,
        },
        {
            "title": "Sirkulyatsiya",
            "type": "normal",
            "text": """
            Asosiy yo'llarni xayolan chizing.

            <br><br>

            Qaysi yo'llar:

            <br><br>

            • kesishadi;<br>
            • juda uzun;<br>
            • keraksiz aylanadi;<br>
            • mebel orasidan o'tadi;<br>
            • private va public zonani aralashtiradi?
            """,
        },
        {
            "title": "O'lik maydon",
            "type": "warning",
            "text": """
            Plan maydoni katta bo'lishi mumkin.

            <br><br>

            Lekin diagonal devorlar,
            keraksiz koridorlar va
            foydalanilmaydigan burchaklar
            real foydali maydonni kamaytiradi.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Bitta plan uchun:

            <br><br>

            3 ta eshik konflikti,<br>
            3 ta sirkulyatsiya nuqtasi,<br>
            3 ta mebel ergonomikasi nuqtasini

            <br><br>

            tekshiring.
            """,
        },
    ],

    "L02_M10_004": [
        {
            "title": "Xonalarni navbat bilan audit qilamiz",
            "type": "highlight",
            "text": """
            Professional tahlilda
            har bir asosiy xona uchun
            alohida checklist ishlatish foydali.
            """,
        },
        {
            "title": "Oshxona",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • muzlatkich;<br>
            • moyka;<br>
            • tayyorlash yuzasi;<br>
            • plita;<br>
            • pantry;<br>
            • dining;<br>
            • hovli bilan aloqa.
            """,
        },
        {
            "title": "Living",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • TV joyi;<br>
            • suhbat zonasi;<br>
            • divanlar;<br>
            • asosiy yurish;<br>
            • hovliga chiqish;<br>
            • katta makon zonalanganmi.
            """,
        },
        {
            "title": "Master bedroom",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • krovat;<br>
            • yurish;<br>
            • garderob;<br>
            • private sanuzel;<br>
            • tungi circulation;<br>
            • maxfiylik.
            """,
        },
        {
            "title": "Bolalar xonasi",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • uyqu;<br>
            • o'qish;<br>
            • o'yin;<br>
            • saqlash;<br>
            • kelajakda transformatsiya;<br>
            • ota-onaga va sanuzelga aloqa.
            """,
        },
        {
            "title": "Sanuzel",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • eshik;<br>
            • rakovina;<br>
            • unitaz;<br>
            • dush/vanna;<br>
            • foydalanish zonalari;<br>
            • elementlar konflikti.
            """,
        },
        {
            "title": "Muhim qoida",
            "type": "highlight",
            "text": """
            <b>
            Xatoni ko'rish yetmaydi.

            Professional mutaxassis
            xatoning sababini va yechimini ham tushuntiradi.
            </b>
            """,
        },
    ],

    "L02_M10_005": [
        {
            "title": "LEVEL 2 YAKUNIY CASE",
            "type": "highlight",
            "text": """
            Endi sizga bitta turar joy planini
            to'liq tahlil qilish vazifasi beriladi.

            <br><br>

            Bu LEVEL 2 davomida o'rgangan
            bilimlaringizni birlashtiradi.
            """,
        },
        {
            "title": "1. Foydalanuvchini aniqlang",
            "type": "example",
            "text": """
            Tasavvur qiling:

            <br><br>

            • ota-ona;<br>
            • ikki bola;<br>
            • mehmonlar tez-tez keladi;<br>
            • oila hovlida ovqatlanishni yaxshi ko'radi.

            <br><br>

            Plan shu oilaga mos ishlashi kerak.
            """,
        },
        {
            "title": "2. Zonalashni tekshiring",
            "type": "example",
            "text": """
            Public, private va service zonalarni ajrating.

            <br><br>

            Kamida 3 ta savolga javob bering:

            <br><br>

            • mehmon qayergacha kiradi?<br>
            • bolalar private zonasi qayerda?<br>
            • oshxona va hovli aloqasi qanday?
            """,
        },
        {
            "title": "3. Sirkulyatsiyani tekshiring",
            "type": "example",
            "text": """
            Quyidagi yo'llarni tahlil qiling:

            <br><br>

            kirish → living<br>
            kirish → oshxona<br>
            oshxona → dining<br>
            living → hovli<br>
            yotoqxona → sanuzel
            """,
        },
        {
            "title": "4. Har bir xona",
            "type": "example",
            "text": """
            Kamida:

            <br><br>

            • oshxona;<br>
            • living;<br>
            • master bedroom;<br>
            • bolalar xonasi;<br>
            • sanuzel

            <br><br>

            bo'yicha alohida xulosa yozing.
            """,
        },
        {
            "title": "5. Xatolar",
            "type": "warning",
            "text": """
            Kamida 10 ta konkret nuqta toping.

            <br><br>

            “Plan yomon” deb yozmang.

            <br><br>

            Masalan:

            <br><br>

            “Mehmon sanuzelga borish uchun
            private yotoq koridoriga kiradi.”

            <br><br>

            Bu professional tahlil.
            """,
        },
        {
            "title": "6. Yechim taklif qiling",
            "type": "example",
            "text": """
            Har bir asosiy muammo uchun
            kamida bitta yechim bering.

            <br><br>

            Masalan:

            <br><br>

            MUAMMO:
            dining orqali hovliga asosiy yo'l o'tgan.

            <br><br>

            YECHIM:
            tashqi chiqishni sirkulyatsiya chetiga
            yaqinlashtirish yoki dining mebel sxemasini
            qayta tashkil qilish.
            """,
        },
        {
            "title": "Professional format",
            "type": "highlight",
            "text": """
            Har bir tahlilni:

            <br><br>

            <b>MUAMMO → SABAB → OQIBAT → YECHIM</b>

            <br><br>

            formatida yozishga odatlaning.
            """,
        },
        {
            "title": "LEVEL 2 yakuni",
            "type": "highlight",
            "text": """
            LEVEL 2 davomida siz:

            <br><br>

            ✓ ergonomika;<br>
            ✓ funksional zonalash;<br>
            ✓ sirkulyatsiya;<br>
            ✓ xona proporsiyasi;<br>
            ✓ public/private makon;<br>
            ✓ oshxona;<br>
            ✓ yotoqxona va sanuzel;<br>
            ✓ living;<br>
            ✓ bolalar xonasi;<br>
            ✓ kompleks plan auditi

            <br><br>

            bo'yicha fikrlashni o'rgandingiz.

            <br><br>

            Endi keyingi qadam:
            <b>LEVEL 2 FINAL EXAM.</b>
            """,
        },
    ],
}


# ============================================================
# QUIZ
# ============================================================

LEVEL02_MODULE10_QUIZ = {
    "L02_M10_001": [
        {
            "code": "L02_Q136",
            "question": "Professional plan tahlilini faqat xona maydonidan boshlash kerakmi?",
            "explanation": (
                "Avval foydalanuvchi va uning ehtiyojlarini tushunish muhim."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L02_Q137",
            "question": "Butun uy tahlilida public, private va service zonalar tekshiriladimi?",
            "explanation": (
                "Bu kompleks funksional tahlilning asosiy qismlaridan biridir."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L02_Q138",
            "question": "Plan haqida faqat 'chiroyli' yoki 'xunuk' deyish professional tahlilmi?",
            "explanation": (
                "Professional tahlil konkret funksional sabab va oqibatga asoslanadi."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
    ],

    "L02_M10_002": [
        {
            "code": "L02_Q139",
            "question": "Noto'g'ri xona qo'shnichiligi butun plan sifatiga ta'sir qilishi mumkinmi?",
            "explanation": (
                "Xonalar alohida yaxshi bo'lsa ham ularning noto'g'ri aloqasi muammo yaratishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L02_Q140",
            "question": "Mehmonning private zona ichidan o'tishi zonalash muammosi bo'lishi mumkinmi?",
            "explanation": (
                "Bu oilaning maxfiyligini zaiflashtirishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L02_Q141",
            "question": "Oshxona va pantry aloqasi service auditga kiradimi?",
            "explanation": (
                "Bu service zonaning kundalik ishlashiga ta'sir qiladi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L02_M10_003": [
        {
            "code": "L02_Q142",
            "question": "Eshik va mebel konflikti ergonomika auditiga kiradimi?",
            "explanation": (
                "Eshik va mebel foydalanish zonalari birgalikda tekshiriladi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L02_Q143",
            "question": "Keraksiz uzun koridor foydali maydonni kamaytirishi mumkinmi?",
            "explanation": (
                "Ortiqcha circulation maydon samaradorligini pasaytirishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L02_Q144",
            "question": "Asosiy harakat yo'lining mebel orasidan o'tishi tekshiriladimi?",
            "explanation": (
                "Sirkulyatsiya mebel va foydalanish zonalariga xalaqit bermasligi kerak."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L02_M10_004": [
        {
            "code": "L02_Q145",
            "question": "Oshxona auditida muzlatkich, moyka va plita aloqasi tekshiriladimi?",
            "explanation": (
                "Bu oshxona ish jarayonining muhim qismidir."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L02_Q146",
            "question": "Bolalar xonasida kelajakdagi transformatsiya ham tahlil qilinadimi?",
            "explanation": (
                "Bola ulg'aygani sari xona ehtiyojlari o'zgaradi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L02_Q147",
            "question": "Living auditida asosiy yurish yo'li muhimmi?",
            "explanation": (
                "Harakat TV va suhbat zonasini buzmasligi kerak."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L02_M10_005": [
        {
            "code": "L02_Q148",
            "question": "Professional xato tahlilida faqat muammoni aytish yetarlimi?",
            "explanation": (
                "Sabab, oqibat va yechimni ham tushuntirish professional tahlilni kuchaytiradi."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L02_Q149",
            "question": "MUAMMO → SABAB → OQIBAT → YECHIM formati foydalimi?",
            "explanation": (
                "Bu tahlilni aniq va mantiqiy shaklda ifodalashga yordam beradi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L02_Q150",
            "question": "LEVEL 2 yakuniy case nimani tekshiradi?",
            "explanation": (
                "Ergonomika, zonalash, sirkulyatsiya va xonalar sifatini bitta kompleks tahlilda birlashtiradi."
            ),
            "options": [
                ("A", "Butun uy planini kompleks tahlil qilishni", True),
                ("B", "Faqat fasad rangini", False),
            ],
        },
    ],
}


# ============================================================
# DATABASE SEED
# ============================================================

def seed_level02_module10():
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
        ) in LEVEL02_MODULE10_LESSONS:

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
