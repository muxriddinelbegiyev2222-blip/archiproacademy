from database.database import get_connection


# ============================================================
# LEVEL 2
# MODULE 04 - MEHMONXONA LOYIHALASH
# ============================================================

LEVEL02_MODULE04_LESSONS = [
    (
        "L02_M04",
        "L02_M04_001",
        "Mehmonxona vazifasi",
        "theory",
        "Mehmonxonaning uy ichidagi roli va asosiy funksiyalarini tushunish.",
        1,
        40,
        20,
    ),
    (
        "L02_M04",
        "L02_M04_002",
        "Mehmonxona ergonomikasi",
        "theory",
        "Mebel, odam harakati va foydalanish zonalarini ergonomik tashkil qilish.",
        2,
        45,
        20,
    ),
    (
        "L02_M04",
        "L02_M04_003",
        "Mebel joylashuvi",
        "practice",
        "Divan, kreslo, stol va media zonani mantiqiy joylashtirish.",
        3,
        50,
        20,
    ),
    (
        "L02_M04",
        "L02_M04_004",
        "Circulation va mehmon oqimi",
        "practice",
        "Mehmonxona ichidagi kirish, o'tish va o'tirish yo'llarini to'g'ri tashkil qilish.",
        4,
        50,
        20,
    ),
    (
        "L02_M04",
        "L02_M04_005",
        "Mehmonxona auditi",
        "practice",
        "Mehmonxona rejasini ergonomika, mebel va circulation bo'yicha tekshirish.",
        5,
        55,
        25,
    ),
]


# ============================================================
# CONTENT
# ============================================================

LEVEL02_MODULE04_CONTENT = {
    "L02_M04_001": [
        {
            "title": "Mehmonxona nima uchun kerak?",
            "type": "highlight",
            "text": """
            Mehmonxona —
            uy ichidagi eng faol
            umumiy makonlardan biri.

            <br><br>

            Bu yerda:

            <br><br>

            • oila yig'iladi;<br>
            • mehmon kutish mumkin;<br>
            • suhbat qilinadi;<br>
            • dam olinadi;<br>
            • ba'zan TV yoki media zona ishlatiladi.
            """,
        },
        {
            "title": "Faqat katta xona yetarli emas",
            "type": "normal",
            "text": """
            Mehmonxona katta bo'lishi
            uning avtomatik ravishda
            qulay ekanini anglatmaydi.

            <br><br>

            Asosiy savol:

            <br><br>

            <b>
            odam bu xonadan
            qanday foydalanadi?
            </b>
            """,
        },
        {
            "title": "Funksiya birinchi o'rinda",
            "type": "highlight",
            "text": """
            Mebelni joylashtirishdan oldin
            xonaning asosiy funksiyasini aniqlang.

            <br><br>

            Masalan:

            <br><br>

            • oilaviy dam olish;<br>
            • mehmon qabul qilish;<br>
            • TV ko'rish;<br>
            • suhbat zonasi;<br>
            • dining bilan bog'lanish.
            """,
        },
        {
            "title": "Tasavvur qiling",
            "type": "example",
            "text": """
            30 m² mehmonxona bor.

            <br><br>

            Lekin divan kirish eshigini to'sgan,
            TVga qarash noqulay,
            o'tish yo'li esa
            xona o'rtasidan kesib o'tadi.

            <br><br>

            Maydon katta,
            lekin reja yomon.
            """,
        },
        {
            "title": "Arxitektor savollari",
            "type": "normal",
            "text": """
            Mehmonxonani loyihalashda so'rang:

            <br><br>

            • kirish qayerdan?<br>
            • odam qayerga o'tiradi?<br>
            • asosiy fokus nuqtasi qayerda?<br>
            • hovli yoki terassa bilan aloqa bormi?<br>
            • dining bilan aloqa kerakmi?<br>
            • o'tish yo'li mebelni kesib o'tmayaptimi?
            """,
        },
        {
            "title": "Mini-vazifa",
            "type": "example",
            "text": """
            Qog'ozda oddiy mehmonxona chizing.

            <br><br>

            Unda belgilang:

            <br><br>

            • kirish;<br>
            • asosiy o'tirish zonasi;<br>
            • TV/media zona;<br>
            • deraza;<br>
            • asosiy circulation yo'li.
            """,
        },
    ],

    "L02_M04_002": [
        {
            "title": "Ergonomika — odam uchun loyiha",
            "type": "highlight",
            "text": """
            Mehmonxona ergonomikasi —
            mebelni shunchaki sig'dirish emas.

            <br><br>

            Odamning:

            <br><br>

            • o'tirishi;<br>
            • turishi;<br>
            • yurishi;<br>
            • suhbat qilishi;<br>
            • eshik va derazadan foydalanishi

            <br><br>

            hisobga olinadi.
            """,
        },
        {
            "title": "Mebel atrofidagi bo'sh zona",
            "type": "normal",
            "text": """
            Divan,
            stol
            yoki kreslo
            faqat o'z konturi bilan
            joy egallamaydi.

            <br><br>

            Ularning atrofida
            foydalanish va yurish uchun
            bo'sh zona ham kerak.
            """,
        },
        {
            "title": "Suhbat zonasi",
            "type": "example",
            "text": """
            Ikki divan
            bir-biridan juda uzoq
            joylashtirilsa,

            <br><br>

            odamlar suhbat qilishi
            noqulaylashishi mumkin.

            <br><br>

            Juda yaqin joylashtirilsa esa
            circulation yomonlashadi.
            """,
        },
        {
            "title": "TV/media zona",
            "type": "normal",
            "text": """
            Agar xonada TV bo'lsa,
            faqat TV devorini emas,
            unga qaragan seatingni ham
            birgalikda rejalashtiring.

            <br><br>

            Xona faqat bitta element
            atrofida qurilib qolmasin.
            """,
        },
        {
            "title": "Deraza oldini to'smang",
            "type": "warning",
            "text": """
            Katta divan yoki shkaf
            deraza oldini to'liq to'sib qo'ysa,

            <br><br>

            yorug'lik,
            ko'rinish
            va derazadan foydalanish
            yomonlashishi mumkin.
            """,
        },
        {
            "title": "Eshik swingini tekshiring",
            "type": "normal",
            "text": """
            Eshik ochilganda:

            <br><br>

            • divanga urilmasin;<br>
            • kresloni to'smasin;<br>
            • odam o'tadigan yo'lni yopmasin.
            """,
        },
        {
            "title": "Mini-vazifa",
            "type": "example",
            "text": """
            Bitta mehmonxona sxemasini oling.

            <br><br>

            Unda 3 ta joyni belgilang:

            <br><br>

            1. o'tirish zonasi;<br>
            2. yurish zonasi;<br>
            3. erkin foydalanish zonasi.
            """,
        },
    ],

    "L02_M04_003": [
        {
            "title": "Mebel plan tuzilmani ko'rsatadi",
            "type": "highlight",
            "text": """
            Mehmonxona planini
            mebelsiz baholash yetarli emas.

            <br><br>

            Mebel joylashtirilganda
            xonaning real qulayligi
            ko'rina boshlaydi.
            """,
        },
        {
            "title": "Asosiy elementlar",
            "type": "normal",
            "text": """
            Mehmonxonada
            loyiha vazifasiga qarab:

            <br><br>

            • divan;<br>
            • kreslo;<br>
            • coffee table;<br>
            • TV/media elementi;<br>
            • konsol;<br>
            • yordamchi stol

            <br><br>

            ishlatilishi mumkin.
            """,
        },
        {
            "title": "Fokus nuqtasi",
            "type": "highlight",
            "text": """
            Mehmonxonada
            asosiy vizual yoki
            funksional fokus bo'lishi mumkin.

            <br><br>

            Masalan:

            <br><br>

            • TV devori;<br>
            • hovliga katta deraza;<br>
            • dekorativ devor;<br>
            • kamin;<br>
            • suhbat markazi.
            """,
        },
        {
            "title": "Mebelni devorga yopishtirish shart emas",
            "type": "normal",
            "text": """
            Barcha mebelni
            xona perimetri bo'ylab
            devorga yopishtirib chiqish

            <br><br>

            har doim eng yaxshi
            kompozitsiya bermaydi.

            <br><br>

            Xona markazi va
            odam harakatini ham o'ylang.
            """,
        },
        {
            "title": "Dining bilan aloqa",
            "type": "example",
            "text": """
            Agar living va dining
            bir-biriga yaqin bo'lsa,

            <br><br>

            mebel joylashuvi
            ular orasidagi yurish yo'lini
            to'smasligi kerak.
            """,
        },
        {
            "title": "Tipik xato",
            "type": "warning",
            "text": """
            Katta L-shaped divan
            plan chiroyli ko'rinishi uchun qo'yildi.

            <br><br>

            Lekin u diningga
            asosiy o'tish yo'lini yopdi.

            <br><br>

            Mebel xonaga sig'di,
            lekin circulation buzildi.
            """,
        },
        {
            "title": "Mini-vazifa",
            "type": "example",
            "text": """
            Bir xil mehmonxona uchun
            2 xil mebel variantini chizing.

            <br><br>

            Variant A:
            TVga yo'naltirilgan.

            <br><br>

            Variant B:
            suhbatga yo'naltirilgan.

            <br><br>

            Qaysi biri qaysi oilaga
            mos kelishini tushuntiring.
            """,
        },
    ],

    "L02_M04_004": [
        {
            "title": "Circulation xonani kesib o'tishi mumkin",
            "type": "highlight",
            "text": """
            Mehmonxona ko'pincha
            boshqa xonalarga yoki
            hovliga olib boradigan
            harakat yo'llariga yaqin bo'ladi.

            <br><br>

            Shuning uchun circulation
            alohida tekshiriladi.
            """,
        },
        {
            "title": "Kirgan odam qayerga boradi?",
            "type": "normal",
            "text": """
            Mehmonxonaga kirgan odam
            darhol mebelga urilmasligi kerak.

            <br><br>

            Kirishdan keyin
            tabiiy harakat yo'li
            tushunarli bo'lishi foydali.
            """,
        },
        {
            "title": "Seating zonani kesmang",
            "type": "warning",
            "text": """
            Hovliga chiqish uchun
            odamlar doim
            divan va TV orasidan o'tsa,

            <br><br>

            sitting zona tinchligi buziladi.
            """,
        },
        {
            "title": "Mehmon va oila oqimi",
            "type": "normal",
            "text": """
            Mehmonxona faqat
            bitta odam uchun emas.

            <br><br>

            Bir vaqtning o'zida
            bir nechta odam harakatlanishini
            tasavvur qiling.
            """,
        },
        {
            "title": "Hovli bilan aloqa",
            "type": "example",
            "text": """
            Mehmonxonadan terassaga chiqish bor.

            <br><br>

            Divan shu eshik oldiga
            juda yaqin qo'yilgan.

            <br><br>

            Natijada tashqi makonga
            chiqish noqulaylashadi.
            """,
        },
        {
            "title": "Ko'rinmas yo'l",
            "type": "highlight",
            "text": """
            Plan chizayotganda
            pol ustida odamlar yuradigan
            “ko'rinmas yo'llar”ni tasavvur qiling.

            <br><br>

            Yaxshi reja —
            shu yo'llar bilan mebel
            konflikt qilmaydigan reja.
            """,
        },
        {
            "title": "Mini-vazifa",
            "type": "example",
            "text": """
            Mehmonxona planida
            strelka bilan belgilang:

            <br><br>

            • kirish → sofa;<br>
            • kirish → dining;<br>
            • kirish → hovli.

            <br><br>

            Strelkalar mebelni
            kesib o'tayotgan bo'lsa,
            reja ustida qayta ishlang.
            """,
        },
    ],

    "L02_M04_005": [
        {
            "title": "Mehmonxona auditi",
            "type": "highlight",
            "text": """
            Endi mehmonxonani
            faqat chiroyli plan sifatida emas,

            <br><br>

            real ishlaydigan makon sifatida
            tekshiramiz.
            """,
        },
        {
            "title": "1. Funksiya",
            "type": "example",
            "text": """
            Savollar:

            <br><br>

            • xona kim uchun?<br>
            • asosiy faoliyat nima?<br>
            • mehmon qabul qilinadimi?<br>
            • TV kerakmi?<br>
            • dining bilan bog'lanadimi?
            """,
        },
        {
            "title": "2. Mebel",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • divan mantiqiy joydami?<br>
            • kreslolar konflikt qilmayaptimi?<br>
            • stol foydalanishga qulaymi?<br>
            • mebel xonani ortiqcha to'ldirmaganmi?
            """,
        },
        {
            "title": "3. Circulation",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • kirish ochiqmi?<br>
            • asosiy yo'l tushunarlimi?<br>
            • hovliga chiqish yopilmaganmi?<br>
            • seating zona doim kesib o'tilmayaptimi?
            """,
        },
        {
            "title": "4. Eshik va deraza",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • eshik mebelga urilmayaptimi?<br>
            • deraza to'silmaganmi?<br>
            • yorug'likdan foydalanish mantiqiymi?<br>
            • tashqi ko'rinish bilan aloqa bormi?
            """,
        },
        {
            "title": "Xatoni toping",
            "type": "warning",
            "text": """
            Mehmonxona 28 m².

            <br><br>

            Unda katta divan,
            2 ta kreslo,
            katta stol
            va TV bor.

            <br><br>

            Barcha mebel sig'gan.

            <br><br>

            Lekin hovliga chiqadigan eshik
            oldida faqat tor yo'l qolgan.

            <br><br>

            Savol:
            loyiha yaxshi ishlayaptimi?

            <br><br>

            <b>
            Yo'q.
            Mebel sig'ishi ergonomika
            va circulation yaxshi degani emas.
            </b>
            """,
        },
        {
            "title": "Professional checklist",
            "type": "example",
            "text": """
            Mehmonxonani tekshiring:

            <br><br>

            <b>1.</b> Xona funksiyasi aniqmi?<br><br>
            <b>2.</b> Mebel real foydalanishga mosmi?<br><br>
            <b>3.</b> O'tirish zonasi qulaymi?<br><br>
            <b>4.</b> Circulation ochiqmi?<br><br>
            <b>5.</b> Eshiklar konflikt qilmayaptimi?<br><br>
            <b>6.</b> Deraza oldi ochiqmi?<br><br>
            <b>7.</b> Dining/hovli aloqasi mantiqiymi?
            """,
        },
        {
            "title": "Modul yakuni",
            "type": "highlight",
            "text": """
            Siz endi:

            <br><br>

            ✓ mehmonxona funksiyasini tahlil qilasiz;<br>
            ✓ ergonomikani hisobga olasiz;<br>
            ✓ mebelni mantiqiy joylashtirasiz;<br>
            ✓ circulationni tekshirasiz;<br>
            ✓ eshik va deraza konfliktlarini ko'rasiz;<br>
            ✓ mehmonxona planini audit qilasiz.

            <br><br>

            Keyingi modul:
            <b>Oshxona loyihalash.</b>
            """,
        },
    ],
}


# ============================================================
# QUIZ
# Q046-Q060 KODLARI SAQLAB QOLINDI
# ============================================================

LEVEL02_MODULE04_QUIZ = {
    "L02_M04_001": [
        {
            "code": "L02_Q046",
            "question": "Mehmonxona katta bo'lsa avtomatik ravishda qulay bo'ladimi?",
            "explanation": (
                "Maydondan tashqari funksiya, mebel va circulation ham muhim."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L02_Q047",
            "question": "Mehmonxona loyihalashda uning asosiy funksiyasini aniqlash kerakmi?",
            "explanation": (
                "Mebel va rejalashtirish xonaning qanday ishlatilishiga bog'liq."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L02_Q048",
            "question": "Mehmonxonada circulationni ham tahlil qilish kerakmi?",
            "explanation": (
                "Odam harakati mebel va xonaning real foydalanishiga bevosita ta'sir qiladi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L02_M04_002": [
        {
            "code": "L02_Q049",
            "question": "Mebel faqat o'z fizik konturi bilan joy egallaydimi?",
            "explanation": (
                "Mebel atrofida undan foydalanish va yurish uchun ham joy kerak."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L02_Q050",
            "question": "Eshik ochilish zonasi mebel bilan tekshirilishi kerakmi?",
            "explanation": (
                "Eshikning mebel yoki circulation bilan konflikti bo'lmasligi kerak."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L02_Q051",
            "question": "Deraza oldini katta mebel bilan to'liq to'sish har doim yaxshi yechimmi?",
            "explanation": (
                "Bu yorug'lik, ko'rinish va derazadan foydalanishni yomonlashtirishi mumkin."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
    ],

    "L02_M04_003": [
        {
            "code": "L02_Q052",
            "question": "Mehmonxona planini mebel bilan tekshirish foydalimi?",
            "explanation": (
                "Mebel real ergonomika va circulationni ko'rsatishga yordam beradi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L02_Q053",
            "question": "Barcha mebelni majburiy ravishda devorga yopishtirish kerakmi?",
            "explanation": (
                "Mebel joylashuvi xona funksiyasi, kompozitsiyasi va circulationga qarab belgilanadi."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L02_Q054",
            "question": "Living va dining orasidagi o'tish yo'li mebel bilan to'silmasligi kerakmi?",
            "explanation": (
                "Funksional zonalar orasidagi circulation ochiq bo'lishi muhim."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L02_M04_004": [
        {
            "code": "L02_Q055",
            "question": "Asosiy circulation seating zonani doim kesib o'tsa bu noqulaylik yaratishi mumkinmi?",
            "explanation": (
                "O'tish oqimi dam olish va suhbat zonasini bezovta qilishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L02_Q056",
            "question": "Mehmonxonaga kirganda tabiiy harakat yo'li tushunarli bo'lishi foydalimi?",
            "explanation": (
                "Kirish va circulation mantiqi xonadan foydalanishni yaxshilaydi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L02_Q057",
            "question": "Hovliga chiqadigan eshik oldini mebel bilan to'sib qo'yish yaxshi rejalashtirishmi?",
            "explanation": (
                "Tashqi makonga chiqish yo'li ochiq va qulay bo'lishi kerak."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
    ],

    "L02_M04_005": [
        {
            "code": "L02_Q058",
            "question": "Mebelning hammasi sig'ishi mehmonxona ergonomikasi yaxshi degani bo'ladimi?",
            "explanation": (
                "Mebel sig'ishi bilan birga circulation va foydalanish zonalari ham tekshiriladi."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L02_Q059",
            "question": "Mehmonxona auditida eshik, deraza va mebel aloqasi tekshiriladimi?",
            "explanation": (
                "Bu elementlar xonaning ergonomik va funksional ishlashiga ta'sir qiladi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L02_Q060",
            "question": "Mehmonxonani baholashdagi to'g'ri yondashuv qaysi?",
            "explanation": (
                "Funksiya, mebel va circulation birgalikda tahlil qilinadi."
            ),
            "options": [
                (
                    "A",
                    "Funksiya → mebel → circulation → audit",
                    True,
                ),
                (
                    "B",
                    "Faqat xona maydoniga qarash",
                    False,
                ),
            ],
        },
    ],
}


# ============================================================
# DATABASE SEED
# ============================================================

def seed_level02_module04():
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
        ) in LEVEL02_MODULE04_LESSONS:

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
