from database.database import get_connection


# ============================================================
# LEVEL 2
# MODULE 06 - OSHXONA VA OVQATLANISH ERGONOMIKASI
# ============================================================

LEVEL02_MODULE06_LESSONS = [
    (
        "L02_M06",
        "L02_M06_001",
        "Oshxona ish jarayoni",
        "theory",
        "Oshxonani kundalik ish ketma-ketligi asosida rejalashtirish.",
        1,
        35,
        20,
    ),
    (
        "L02_M06",
        "L02_M06_002",
        "Muzlatkich, moyka va plita aloqasi",
        "theory",
        "Asosiy oshxona nuqtalari o'rtasidagi funksional aloqani tushunish.",
        2,
        35,
        20,
    ),
    (
        "L02_M06",
        "L02_M06_003",
        "Oshxona turlari va island",
        "theory",
        "Bir qatorli, L, U va island oshxonalarning ishlash prinsiplarini farqlash.",
        3,
        40,
        20,
    ),
    (
        "L02_M06",
        "L02_M06_004",
        "Ovqatlanish zonasi ergonomikasi",
        "practice",
        "Stol, stul va yurish zonalarini real foydalanish uchun to'g'ri tashkil qilish.",
        4,
        40,
        20,
    ),
    (
        "L02_M06",
        "L02_M06_005",
        "Oshxona planidagi xatolarni topish",
        "practice",
        "Real oshxona va ovqatlanish planlaridagi funksional xatolarni aniqlash.",
        5,
        45,
        25,
    ),
]


# ============================================================
# LESSON CONTENT
# ============================================================

LEVEL02_MODULE06_CONTENT = {
    # ========================================================
    # 1-DARS
    # ========================================================

    "L02_M06_001": [
        {
            "title": "Oshxona — faqat mebel emas",
            "type": "highlight",
            "text": """
            Oshxona — uy ichidagi eng faol
            ishlatiladigan funksional zonalardan biri.

            <br><br>

            Bu yerda odam bir nechta ishni
            ketma-ket bajaradi.

            <br><br>

            Shuning uchun oshxonani faqat
            shkaflarni devorga terish orqali
            loyihalab bo'lmaydi.
            """,
        },
        {
            "title": "Oddiy ish jarayoni",
            "type": "example",
            "text": """
            Tasavvur qiling:

            <br><br>

            siz bozordan mahsulot olib keldingiz.

            <br><br>

            Jarayon taxminan:

            <br><br>

            <b>
            olib kelish → saqlash → yuvish →
            tayyorlash → pishirish → servis
            </b>

            <br><br>

            ketma-ketligida ishlaydi.
            """,
        },
        {
            "title": "Saqlash",
            "type": "normal",
            "text": """
            Mahsulotlar:

            <br><br>

            • muzlatkich;<br>
            • pantry;<br>
            • yuqori shkaf;<br>
            • pastki shkaf

            <br><br>

            kabi joylarda saqlanadi.

            <br><br>

            Saqlash zonasiga mahsulotni
            uyga olib kirish yo'li ham muhim.
            """,
        },
        {
            "title": "Tayyorlash zonasi",
            "type": "normal",
            "text": """
            Mahsulot yuvilgandan keyin
            uni kesish, tayyorlash va
            pishirishga tayyorlash uchun
            ish yuzasi kerak.

            <br><br>

            Faqat moyka va plita bo'lishi yetmaydi.
            """,
        },
        {
            "title": "Boshlovchi xatosi",
            "type": "warning",
            "text": """
            Oshxonada barcha texnika mavjud.

            <br><br>

            Lekin ular orasida normal
            ish yuzasi yo'q.

            <br><br>

            Natijada katta oshxona ham
            noqulay ishlashi mumkin.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            O'z oshxonangizda bir taom
            tayyorlash jarayonini kuzating.

            <br><br>

            Qayerdan boshlaysiz?

            <br>
            Necha marta u yoqdan bu yoqqa yurasiz?

            <br><br>

            Eng ko'p ishlatiladigan 5 nuqtani yozing.
            """,
        },
    ],

    # ========================================================
    # 2-DARS
    # ========================================================

    "L02_M06_002": [
        {
            "title": "Uch asosiy nuqta",
            "type": "highlight",
            "text": """
            Oshxonada ko'p ishlatiladigan
            uchta muhim element:

            <br><br>

            <b>muzlatkich — moyka — plita</b>.

            <br><br>

            Ularning o'zaro joylashuvi
            kundalik ishga katta ta'sir qiladi.
            """,
        },
        {
            "title": "Work triangle tushunchasi",
            "type": "normal",
            "text": """
            Klassik rejalashda
            muzlatkich, moyka va plita orasidagi
            aloqaga ko'pincha
            <b>ish uchburchagi</b> sifatida qaraladi.

            <br><br>

            Bu qat'iy universal formula emas,
            balki harakatni tahlil qilish usuli.
            """,
        },
        {
            "title": "Nega moyka markaziy bo'lishi mumkin?",
            "type": "example",
            "text": """
            Ko'p jarayonlarda:

            <br><br>

            muzlatkichdan mahsulot olinadi,

            <br>
            keyin yuviladi,

            <br>
            keyin tayyorlanadi,

            <br>
            keyin pishiriladi.

            <br><br>

            Shu sababli moyka va
            tayyorlash yuzasi muhim markazga aylanishi mumkin.
            """,
        },
        {
            "title": "Juda uzoq masofa",
            "type": "warning",
            "text": """
            Muzlatkich oshxonaning bir chetida.

            <br><br>

            Moyka qarama-qarshi uzoq burchakda.

            <br><br>

            Plita yana boshqa tomonda.

            <br><br>

            Har bir ovqat tayyorlashda
            keraksiz yurish ko'payadi.
            """,
        },
        {
            "title": "Juda yaqin ham muammo",
            "type": "warning",
            "text": """
            Hammasini bir-biriga
            haddan tashqari zich joylashtirish ham
            yaxshi emas.

            <br><br>

            Texnika eshiklari,
            odamlarning turish zonasi va
            ish yuzalari bir-biriga xalaqit berishi mumkin.
            """,
        },
        {
            "title": "Professional fikr",
            "type": "highlight",
            "text": """
            <b>
            Maqsad mukammal geometrik uchburchak emas.

            Maqsad — ish jarayonini qulay qilish.
            </b>
            """,
        },
    ],

    # ========================================================
    # 3-DARS
    # ========================================================

    "L02_M06_003": [
        {
            "title": "Oshxona shakli",
            "type": "highlight",
            "text": """
            Oshxona mebellari turli
            konfiguratsiyada tashkil qilinishi mumkin.

            <br><br>

            Eng ko'p uchraydiganlari:

            <br><br>

            • bir qatorli;<br>
            • parallel;<br>
            • L shakl;<br>
            • U shakl;<br>
            • island bilan.
            """,
        },
        {
            "title": "Bir qatorli oshxona",
            "type": "normal",
            "text": """
            Barcha asosiy elementlar
            bitta devor bo'ylab joylashadi.

            <br><br>

            Kichik makonda qulay bo'lishi mumkin.

            <br><br>

            Lekin juda uzun bo'lsa,
            ish masofasi ortib ketishi mumkin.
            """,
        },
        {
            "title": "L shaklli oshxona",
            "type": "normal",
            "text": """
            Ikki tutash devor ishlatiladi.

            <br><br>

            Bu ko'p hollarda:

            <br><br>

            • ish zonasini ixcham qilish;<br>
            • markazda bo'sh joy qoldirish;<br>
            • dining bilan yaxshi aloqa qilish

            <br><br>

            imkonini beradi.
            """,
        },
        {
            "title": "U shaklli oshxona",
            "type": "normal",
            "text": """
            Uch tomon ish yuzasi sifatida ishlatiladi.

            <br><br>

            Saqlash va ish yuzasi ko'p bo'lishi mumkin.

            <br><br>

            Lekin ichki harakat zonasi
            yetarlicha qulay bo'lishi kerak.
            """,
        },
        {
            "title": "Island nima?",
            "type": "example",
            "text": """
            Island — oshxona markazida joylashgan
            alohida ish yoki servis bloki.

            <br><br>

            Unda:

            <br><br>

            • ish yuzasi;<br>
            • saqlash;<br>
            • moyka;<br>
            • plita;<br>
            • o'tirish zonasi

            <br><br>

            bo'lishi mumkin.
            """,
        },
        {
            "title": "Island uchun joy yetarlimi?",
            "type": "warning",
            "text": """
            Island chiroyli ko'ringani uchun
            har qanday oshxonaga qo'yilmaydi.

            <br><br>

            Uning atrofida:

            <br><br>

            • yurish;<br>
            • shkaf ochish;<br>
            • texnika ochish;<br>
            • ikki odam ishlashi

            <br><br>

            uchun real makon qolishi kerak.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Bir qatorli, L va islandli
            uchta oshxona toping.

            <br><br>

            Har biri uchun:

            <br><br>

            • kuchli tomoni;<br>
            • zaif tomoni;<br>
            • qaysi xona uchun mosligini

            <br><br>

            yozing.
            """,
        },
    ],

    # ========================================================
    # 4-DARS
    # ========================================================

    "L02_M06_004": [
        {
            "title": "Stol sig'di — masala tugamadi",
            "type": "highlight",
            "text": """
            Ovqat stoli plan ichiga sig'ishi
            uning ergonomik ishlashini anglatmaydi.

            <br><br>

            Stul va odam uchun ham joy kerak.
            """,
        },
        {
            "title": "Stul ortidagi zona",
            "type": "example",
            "text": """
            Odam stulni orqaga suradi.

            <br><br>

            O'tiradi.

            <br><br>

            Uning orqasidan boshqa odam
            o'tishi ham mumkin.

            <br><br>

            Demak stol konturidan tashqarida
            qo'shimcha makon talab qilinadi.
            """,
        },
        {
            "title": "Dining va oshxona aloqasi",
            "type": "normal",
            "text": """
            Ovqatlanish zonasi oshxonaga
            mantiqiy yaqin bo'lishi foydali.

            <br><br>

            Tayyor taomni uzoq masofaga
            tashish kundalik noqulaylik yaratadi.
            """,
        },
        {
            "title": "Yurish yo'li stol orasidan o'tmasin",
            "type": "warning",
            "text": """
            Asosiy uy sirkulyatsiyasi
            ovqat stolining stullari orasidan o'tsa,
            odamlar bir-biriga xalaqit beradi.

            <br><br>

            Dining zona harakat yo'liga aylanib qolmasligi kerak.
            """,
        },
        {
            "title": "Katta stol — har doim yaxshi emas",
            "type": "warning",
            "text": """
            8 kishilik stol xona ichiga zo'rg'a sig'di.

            <br><br>

            Lekin stullarni surishning iloji yo'q.

            <br><br>

            Bu holatda kichikroq stol
            real hayotda yaxshiroq ishlashi mumkin.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Bir oshxona + dining planini toping.

            <br><br>

            Tekshiring:

            <br><br>

            1. Stol atrofida odam o'tira oladimi?<br>
            2. Stul orqasidan yurish mumkinmi?<br>
            3. Oshxonadan stolga yo'l qisqami?<br>
            4. Dining asosiy koridorga aylanmaganmi?
            """,
        },
    ],

    # ========================================================
    # 5-DARS
    # ========================================================

    "L02_M06_005": [
        {
            "title": "Oshxona xatolarini ovlaymiz",
            "type": "highlight",
            "text": """
            Endi oshxonaning tashqi ko'rinishini emas,
            uning real ishlashini tahlil qilamiz.
            """,
        },
        {
            "title": "Xato 1 — muzlatkich eshigi to'sadi",
            "type": "warning",
            "text": """
            Muzlatkich eshigi ochilganda
            asosiy yurish yo'lini butunlay yopadi.

            <br><br>

            Texnika o'lchami emas,
            uning ochilishi ham hisobga olinishi kerak.
            """,
        },
        {
            "title": "Xato 2 — moyka va plita orasida ish yuzasi yo'q",
            "type": "warning",
            "text": """
            Moyka plitaga juda yaqin.

            <br><br>

            Mahsulotni yuvib,
            xavfsiz tayyorlash uchun
            normal ish yuzasi qolmagan.
            """,
        },
        {
            "title": "Xato 3 — island yo'lni toraytirgan",
            "type": "warning",
            "text": """
            Oshxona katta ko'rinsin deb
            markazga island qo'yilgan.

            <br><br>

            Lekin island bilan asosiy shkaflar orasida
            odamlar bemalol harakat qila olmaydi.
            """,
        },
        {
            "title": "Xato 4 — stol asosiy yo'l ustida",
            "type": "warning",
            "text": """
            Hovliga chiqish uchun
            odam har safar dining stolini aylanadi.

            <br><br>

            Stullar chiqarilganda yo'l butunlay torayadi.
            """,
        },
        {
            "title": "Xato 5 — pantry juda uzoqda",
            "type": "warning",
            "text": """
            Pantry mavjud.

            <br><br>

            Lekin u oshxonadan boshqa tomonda.

            <br><br>

            Har bir mahsulot uchun uzoq yurish kerak.

            <br><br>

            Xona mavjudligi emas,
            uning aloqasi muhim.
            """,
        },
        {
            "title": "Xato 6 — oshxona hovlidan uzilgan",
            "type": "warning",
            "text": """
            Oilada hovlida tez-tez ovqatlanish odati bor.

            <br><br>

            Lekin oshxonadan hovliga chiqish uchun
            butun uyni aylanib o'tish kerak.

            <br><br>

            Loyiha oilaning hayot tarziga moslashmagan.
            """,
        },
        {
            "title": "Professional tahlil algoritmi",
            "type": "example",
            "text": """
            Oshxona planini ko'rsangiz:

            <br><br>

            <b>1.</b> Mahsulot qayerdan kiradi?<br><br>
            <b>2.</b> Qayerda saqlanadi?<br><br>
            <b>3.</b> Qayerda yuviladi?<br><br>
            <b>4.</b> Qayerda tayyorlanadi?<br><br>
            <b>5.</b> Qayerda pishiriladi?<br><br>
            <b>6.</b> Diningga qanday yetkaziladi?<br><br>
            <b>7.</b> Eshik va texnika ochilishlari to'qnashadimi?
            """,
        },
        {
            "title": "Mini-loyiha",
            "type": "example",
            "text": """
            4 kishilik oila uchun
            oshxona + dining planini tahlil qiling.

            <br><br>

            Quyidagilarni belgilang:

            <br><br>

            • muzlatkich;<br>
            • moyka;<br>
            • plita;<br>
            • tayyorlash yuzasi;<br>
            • pantry;<br>
            • dining;<br>
            • hovliga chiqish.

            <br><br>

            Kamida 3 ta yaxshi qaror va
            2 ta yaxshilash mumkin bo'lgan nuqtani yozing.
            """,
        },
        {
            "title": "Modul yakuni",
            "type": "highlight",
            "text": """
            Siz endi:

            <br><br>

            ✓ oshxona workflow;<br>
            ✓ muzlatkich-moyka-plita aloqasi;<br>
            ✓ work triangle;<br>
            ✓ L va U shaklli oshxona;<br>
            ✓ island;<br>
            ✓ dining ergonomikasi;<br>
            ✓ pantry va hovli aloqasi

            <br><br>

            bo'yicha plan tahlil qila olasiz.

            <br><br>

            Keyingi modul:
            <b>Yotoqxona, garderob va sanuzel ergonomikasi.</b>
            """,
        },
    ],
}


# ============================================================
# QUIZ DATA
# ============================================================

LEVEL02_MODULE06_QUIZ = {
    "L02_M06_001": [
        {
            "code": "L02_Q076",
            "question": "Oshxonani rejalashda faqat mebelni joylashtirish yetarlimi?",
            "explanation": (
                "Oshxonada saqlash, yuvish, tayyorlash, pishirish va servis jarayonlari ham tahlil qilinadi."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L02_Q077",
            "question": "Mahsulotni tayyorlash uchun ish yuzasi kerakmi?",
            "explanation": (
                "Yuvish va pishirish orasida mahsulotni tayyorlash uchun ish yuzasi zarur bo'lishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L02_Q078",
            "question": "Mahsulotni uyga olib kirish yo'li oshxona rejasiga ta'sir qilishi mumkinmi?",
            "explanation": (
                "Saqlash va pantry bilan qulay aloqa kundalik foydalanishni yaxshilaydi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L02_M06_002": [
        {
            "code": "L02_Q079",
            "question": "Oshxonadagi uch muhim ish nuqtasi qaysilar?",
            "explanation": (
                "Muzlatkich, moyka va plita oshxona ish jarayonining muhim nuqtalaridir."
            ),
            "options": [
                ("A", "Muzlatkich, moyka, plita", True),
                ("B", "TV, divan, krovat", False),
                ("C", "Shkaf, eshik, deraza", False),
            ],
        },
        {
            "code": "L02_Q080",
            "question": "Work triangle qat'iy universal formula hisoblanadimi?",
            "explanation": (
                "U harakatni tahlil qilish prinsipi; real reja va foydalanuvchi ehtiyojiga moslashtiriladi."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L02_Q081",
            "question": "Muzlatkich, moyka va plita haddan tashqari uzoq bo'lsa nima ko'payadi?",
            "explanation": (
                "Kundalik ovqat tayyorlashdagi keraksiz yurish ko'payishi mumkin."
            ),
            "options": [
                ("A", "Keraksiz yurish", True),
                ("B", "Faqat fasad sifati", False),
            ],
        },
    ],

    "L02_M06_003": [
        {
            "code": "L02_Q082",
            "question": "Island har qanday kichik oshxonaga qo'yilishi kerakmi?",
            "explanation": (
                "Island faqat atrofida yetarli harakat va foydalanish zonasi bo'lsa maqsadga muvofiq."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L02_Q083",
            "question": "L shaklli oshxona nechta tutash devordan foydalanadi?",
            "explanation": (
                "L shaklli oshxona odatda ikki tutash devor bo'ylab tashkil qilinadi."
            ),
            "options": [
                ("A", "Ikki", True),
                ("B", "Faqat bitta", False),
            ],
        },
        {
            "code": "L02_Q084",
            "question": "U shaklli oshxonada ko'p ish yuzasi bo'lishi mumkinmi?",
            "explanation": (
                "U shakli uch tomonlama ish va saqlash yuzasi yaratishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L02_M06_004": [
        {
            "code": "L02_Q085",
            "question": "Ovqat stolining plan ichiga sig'ishi uning ergonomik ishlashi uchun yetarlimi?",
            "explanation": (
                "Stullarni surish, o'tirish va yurish zonasi ham hisobga olinadi."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L02_Q086",
            "question": "Dining va oshxonaning mantiqiy yaqinligi foydalimi?",
            "explanation": (
                "Taomni servis qilish va kundalik harakatni qisqartirishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L02_Q087",
            "question": "Asosiy yurish yo'lining stol stullari orasidan o'tishi muammo bo'lishi mumkinmi?",
            "explanation": (
                "Stullar chiqarilganda asosiy sirkulyatsiya to'silishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L02_M06_005": [
        {
            "code": "L02_Q088",
            "question": "Muzlatkich eshigi asosiy yurish yo'lini yopishi ergonomik muammomi?",
            "explanation": (
                "Texnika ochilishi sirkulyatsiyani to'smasligi kerak."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L02_Q089",
            "question": "Island qo'yilganda uning atrofidagi harakat zonasi tekshiriladimi?",
            "explanation": (
                "Island va boshqa oshxona elementlari orasida foydalanish uchun real makon qolishi kerak."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L02_Q090",
            "question": "Oshxona tahlilida qaysi savol professionalroq?",
            "explanation": (
                "Mahsulotning saqlashdan pishirish va servisgacha bo'lgan yo'lini tahlil qilish funksional sifatni ko'rsatadi."
            ),
            "options": [
                ("A", "Mahsulot qanday yo'l bosadi?", True),
                ("B", "Faqat fasad qaysi rangda?", False),
            ],
        },
    ],
}


# ============================================================
# DATABASE SEED
# ============================================================

def seed_level02_module06():
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
        ) in LEVEL02_MODULE06_LESSONS:

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
