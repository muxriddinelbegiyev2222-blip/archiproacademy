from database.database import get_connection


# ============================================================
# LEVEL 3
# MODULE 07 - RELYEF
# ============================================================

LEVEL03_MODULE07_LESSONS = [
    (
        "L03_M07",
        "L03_M07_001",
        "Relyef nima?",
        "theory",
        "Uchastkadagi balandlik farqlari va nishabni tushunish.",
        1,
        40,
        20,
    ),
    (
        "L03_M07",
        "L03_M07_002",
        "Baland va past nuqtalarni o'qish",
        "theory",
        "Yerning baland va past qismlarini aniqlash va loyiha qaroriga bog'lash.",
        2,
        40,
        20,
    ),
    (
        "L03_M07",
        "L03_M07_003",
        "Uyni nishabga joylashtirish",
        "theory",
        "Nishabli uchastkada bino joylashuvini tahlil qilish.",
        3,
        45,
        20,
    ),
    (
        "L03_M07",
        "L03_M07_004",
        "Kesish, to'ldirish va suv oqimi",
        "practice",
        "Yer massasini o'zgartirish va yomg'ir suvining tabiiy oqimini boshlang'ich darajada tushunish.",
        4,
        45,
        20,
    ),
    (
        "L03_M07",
        "L03_M07_005",
        "Relyefdagi xatolarni topish",
        "practice",
        "Nishabli uchastkalardagi tipik bino va hovli rejalash xatolarini aniqlash.",
        5,
        55,
        25,
    ),
]


# ============================================================
# CONTENT
# ============================================================

LEVEL03_MODULE07_CONTENT = {
    "L03_M07_001": [
        {
            "title": "Yer har doim tekis emas",
            "type": "highlight",
            "text": """
            Uchastka planda tekis ko'rinishi mumkin.

            <br><br>

            Lekin real hayotda yerning
            bir tomoni baland,
            ikkinchi tomoni past bo'lishi mumkin.

            <br><br>

            Bu — relyef.
            """,
        },
        {
            "title": "Relyef nimaga ta'sir qiladi?",
            "type": "normal",
            "text": """
            Relyef:

            <br><br>

            • bino otmetkasiga;<br>
            • kirishga;<br>
            • zinapoyaga;<br>
            • hovliga;<br>
            • parkingga;<br>
            • suv oqimiga;<br>
            • fundamentga

            <br><br>

            ta'sir qilishi mumkin.
            """,
        },
        {
            "title": "Tasavvur qiling",
            "type": "example",
            "text": """
            Uchastkaning ko'cha tomoni past.

            <br><br>

            Orqa qismi esa ancha baland.

            <br><br>

            Agar uyni yerga moslashtirmasdan
            tekis platforma sifatida qo'ysak,

            <br><br>

            katta yer ishlari kerak bo'lishi mumkin.
            """,
        },
        {
            "title": "Arxitektor relyef bilan kurashmaydi",
            "type": "highlight",
            "text": """
            <b>
            Kuchli yechim ko'pincha
            relyefni butunlay yo'q qilish emas,
            undan foydalanishdir.
            </b>
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Bir nishabli uchastkani tasavvur qiling.

            <br><br>

            Belgilang:

            <br><br>

            • eng baland nuqta;<br>
            • eng past nuqta;<br>
            • nishab yo'nalishi.
            """,
        },
    ],

    "L03_M07_002": [
        {
            "title": "Balandlikni o'qish",
            "type": "highlight",
            "text": """
            Relyef tahlilida
            eng asosiy savollardan biri:

            <br><br>

            <b>
            Suv va odam tabiiy ravishda
            qaysi tomonga harakat qiladi?
            </b>
            """,
        },
        {
            "title": "Baland nuqta",
            "type": "normal",
            "text": """
            Baland nuqta:

            <br><br>

            • yaxshi manzara;<br>
            • yuqori pozitsiya;<br>
            • suv oqimidan nisbatan yuqori turish

            <br><br>

            imkoniyatini berishi mumkin.
            """,
        },
        {
            "title": "Past nuqta",
            "type": "normal",
            "text": """
            Past nuqtada:

            <br><br>

            • suv yig'ilishi;<br>
            • namlik;<br>
            • kirish qiyinlashishi

            <br><br>

            kabi masalalar paydo bo'lishi mumkin.
            """,
        },
        {
            "title": "Faqat bir nuqtaga qaramang",
            "type": "warning",
            "text": """
            Uchastkaning faqat
            eng baland va eng past nuqtasini bilish yetmaydi.

            <br><br>

            Ularning orasidagi
            umumiy yer harakati ham muhim.
            """,
        },
        {
            "title": "Relyef diagrammasi",
            "type": "example",
            "text": """
            Oddiy diagrammada:

            <br><br>

            ↑ BALAND

            <br>

            ↓ PAST

            <br><br>

            belgilar bilan
            umumiy nishab yo'nalishini ko'rsatish mumkin.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Uchastkangizga 3 ta zona qo'ying:

            <br><br>

            BALAND<br>
            O'RTA<br>
            PAST

            <br><br>

            va ularning loyiha imkoniyatini yozing.
            """,
        },
    ],

    "L03_M07_003": [
        {
            "title": "Uy nishabga qanday o'tiradi?",
            "type": "highlight",
            "text": """
            Nishabli uchastkada
            uy joylashuvi oddiy tekis yerga qaraganda
            ko'proq tahlil talab qiladi.
            """,
        },
        {
            "title": "Variant 1 — yuqori qism",
            "type": "normal",
            "text": """
            Bino uchastkaning yuqori qismida bo'lsa:

            <br><br>

            • manzara yaxshiroq bo'lishi mumkin;<br>
            • kirish murakkablashishi mumkin;<br>
            • platforma ishlari kerak bo'lishi mumkin.
            """,
        },
        {
            "title": "Variant 2 — past qism",
            "type": "normal",
            "text": """
            Bino past qismda bo'lsa:

            <br><br>

            • ko'chaga yaqinlashishi mumkin;<br>
            • suv masalasi kuchayishi mumkin;<br>
            • yuqori hovli bilan vertikal aloqa kerak bo'lishi mumkin.
            """,
        },
        {
            "title": "Variant 3 — relyefga ergashish",
            "type": "example",
            "text": """
            Ba'zan bino qisman
            relyefga moslashtiriladi.

            <br><br>

            Masalan:

            <br><br>

            turli platformalar,
            terrasa,
            pog'onali hovli
            yoki yarim darajali yechimlar.
            """,
        },
        {
            "title": "Muhim ogohlantirish",
            "type": "warning",
            "text": """
            Relyefli loyiha
            konstruktiv va geologik masalalarni ham keltirib chiqaradi.

            <br><br>

            Arxitektor buni yolg'iz hal qilmaydi.

            <br><br>

            Keyingi bosqichlarda
            konstruktor va boshqa mutaxassislar
            bilan ishlash muhim bo'ladi.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Nishabli uchastkada
            uyni 3 joyga qo'ying:

            <br><br>

            • yuqori;<br>
            • o'rta;<br>
            • past.

            <br><br>

            Har bir variantning
            2 ta afzallik va 2 ta kamchiligini yozing.
            """,
        },
    ],

    "L03_M07_004": [
        {
            "title": "Kesish va to'ldirish",
            "type": "highlight",
            "text": """
            Nishabli yerda
            tekis platforma yaratish uchun
            yerning bir qismi olinishi,
            boshqa qismi to'ldirilishi mumkin.

            <br><br>

            Bu tushuncha ko'pincha
            cut & fill deb yuritiladi.
            """,
        },
        {
            "title": "Ortiqcha yer ishidan qochish",
            "type": "normal",
            "text": """
            Uy relyefga mos kelmasa,
            juda ko'p yer qazish yoki
            to'ldirish kerak bo'lishi mumkin.

            <br><br>

            Bu loyiha murakkabligini oshiradi.
            """,
        },
        {
            "title": "Suv pastga oqadi",
            "type": "highlight",
            "text": """
            Juda oddiy,
            lekin juda muhim qoida:

            <br><br>

            <b>Suv tabiiy ravishda past tomonga harakat qiladi.</b>

            <br><br>

            Shuning uchun suv oqimini
            bino va kirish bilan birga tahlil qilish kerak.
            """,
        },
        {
            "title": "Bino tomon oqim",
            "type": "warning",
            "text": """
            Agar tashqi yer sathi
            suvni to'g'ridan-to'g'ri
            uy tomonga yo'naltirsa,

            <br><br>

            namlik va drenaj muammolari
            paydo bo'lishi mumkin.
            """,
        },
        {
            "title": "Hovli platformalari",
            "type": "example",
            "text": """
            Nishabli hovlida:

            <br><br>

            • terassa;<br>
            • zinapoya;<br>
            • kichik platformalar;<br>
            • yashil nishablar

            <br><br>

            orqali makon bosqichma-bosqich
            tashkil qilinishi mumkin.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Bitta nishabli kesim chizing.

            <br><br>

            Unda:

            <br><br>

            • tabiiy yer;<br>
            • uy platformasi;<br>
            • yuqori qism;<br>
            • past qism;<br>
            • suv oqimi

            <br><br>

            ni ko'rsating.
            """,
        },
    ],

    "L03_M07_005": [
        {
            "title": "Relyef xatolarini ovlaymiz",
            "type": "highlight",
            "text": """
            Endi uchastkani
            faqat plan emas,
            vertikal makon sifatida ham ko'ramiz.
            """,
        },
        {
            "title": "Xato 1 — relyef umuman hisobga olinmagan",
            "type": "warning",
            "text": """
            Genplanda hamma narsa yaxshi.

            <br><br>

            Lekin real yerda
            katta balandlik farqi mavjud.
            """,
        },
        {
            "title": "Xato 2 — suv uyga oqadi",
            "type": "warning",
            "text": """
            Eng past nuqta
            aynan bino kirishi yoki
            fundament atrofiga to'g'ri kelgan.
            """,
        },
        {
            "title": "Xato 3 — parking juda tik nishabda",
            "type": "warning",
            "text": """
            Mashina parkingga kirishda
            noqulay balandlik farqini yengishi kerak.
            """,
        },
        {
            "title": "Xato 4 — hovli foydalanib bo'lmaydi",
            "type": "warning",
            "text": """
            Hovlining katta qismi
            juda tik nishabda qolgan.

            <br><br>

            Dam olish uchun
            qulay tekis zona yaratilmagan.
            """,
        },
        {
            "title": "Xato 5 — ortiqcha yer ishlari",
            "type": "warning",
            "text": """
            Tabiiy relyefdan foydalanish o'rniga
            butun uchastkani majburan tekislash
            rejalashtirilgan.
            """,
        },
        {
            "title": "Professional checklist",
            "type": "example",
            "text": """
            Relyef auditida:

            <br><br>

            <b>1.</b> Eng baland nuqta qayerda?<br><br>
            <b>2.</b> Eng past nuqta qayerda?<br><br>
            <b>3.</b> Suv qayerga oqadi?<br><br>
            <b>4.</b> Uy qaysi otmetkada?<br><br>
            <b>5.</b> Parking qayerda?<br><br>
            <b>6.</b> Family hovli foydalaniladimi?<br><br>
            <b>7.</b> Ortiqcha cut & fill bormi?
            """,
        },
        {
            "title": "Mini-loyiha",
            "type": "example",
            "text": """
            Bir nishabli uchastka yarating.

            <br><br>

            Belgilang:

            <br><br>

            • yuqori tomon;<br>
            • past tomon;<br>
            • uy;<br>
            • parking;<br>
            • private hovli;<br>
            • terassa;<br>
            • suv oqimi.

            <br><br>

            Keyin nima uchun
            uyni aynan shu joyga qo'yganingizni
            5 ta punkt bilan tushuntiring.
            """,
        },
        {
            "title": "Modul yakuni",
            "type": "highlight",
            "text": """
            Siz endi:

            <br><br>

            ✓ relyefni o'qish;<br>
            ✓ baland va past nuqtalarni aniqlash;<br>
            ✓ nishab yo'nalishini tushunish;<br>
            ✓ uyni relyefga moslashtirish;<br>
            ✓ cut & fill tushunchasi;<br>
            ✓ suv oqimini boshlang'ich tahlil qilish

            <br><br>

            ko'nikmalariga ega bo'ldingiz.

            <br><br>

            Keyingi modul:
            <b>Genplan yaratish.</b>
            """,
        },
    ],
}


# ============================================================
# QUIZ
# ============================================================

LEVEL03_MODULE07_QUIZ = {
    "L03_M07_001": [
        {
            "code": "L03_Q091",
            "question": "Uchastka planda tekis ko'rinsa, real hayotda ham albatta tekismi?",
            "explanation": (
                "Real uchastkada balandlik farqlari va nishab mavjud bo'lishi mumkin."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L03_Q092",
            "question": "Relyef parking va hovliga ta'sir qiladimi?",
            "explanation": (
                "Balandlik farqlari kirish, parking va tashqi makonlarga ta'sir qiladi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L03_Q093",
            "question": "Relyefni butunlay yo'q qilish har doim eng yaxshi yechimmi?",
            "explanation": (
                "Ko'pincha tabiiy relyefdan oqilona foydalanish yaxshiroq bo'lishi mumkin."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
    ],

    "L03_M07_002": [
        {
            "code": "L03_Q094",
            "question": "Past nuqtalarda suv yig'ilishi ehtimoli bo'lishi mumkinmi?",
            "explanation": (
                "Suv tabiiy ravishda past tomonlarga harakat qiladi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L03_Q095",
            "question": "Faqat eng baland nuqtani bilish relyefni to'liq tushunish uchun yetarlimi?",
            "explanation": (
                "Butun uchastka bo'ylab umumiy nishab yo'nalishi ham muhim."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L03_Q096",
            "question": "Baland va past zonalarni diagrammada ko'rsatish foydalimi?",
            "explanation": (
                "Bu relyefni vizual tushunishga yordam beradi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L03_M07_003": [
        {
            "code": "L03_Q097",
            "question": "Nishabli uchastkada uy joylashuvi ko'proq tahlil talab qiladimi?",
            "explanation": (
                "Kirish, platforma, hovli va suv masalalari birga ko'rib chiqiladi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L03_Q098",
            "question": "Bino relyefga qisman moslashtirilishi mumkinmi?",
            "explanation": (
                "Terrasa, pog'onali yechim va turli platformalar ishlatilishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L03_Q099",
            "question": "Relyefli loyiha konstruktiv masalalarni ham keltirib chiqarishi mumkinmi?",
            "explanation": (
                "Relyef fundament va konstruktiv qarorlarga ta'sir qilishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L03_M07_004": [
        {
            "code": "L03_Q100",
            "question": "Cut & fill nimaga bog'liq?",
            "explanation": (
                "Yerning bir qismini kesish va boshqa qismini to'ldirish orqali platforma hosil qilishga."
            ),
            "options": [
                ("A", "Yer massasini o'zgartirishga", True),
                ("B", "Faqat fasad rangiga", False),
            ],
        },
        {
            "code": "L03_Q101",
            "question": "Suv odatda qaysi tomonga harakat qiladi?",
            "explanation": (
                "Suv tabiiy ravishda past tomonga oqadi."
            ),
            "options": [
                ("A", "Past tomonga", True),
                ("B", "Har doim yuqoriga", False),
            ],
        },
        {
            "code": "L03_Q102",
            "question": "Suvning bino tomon oqishi muammo bo'lishi mumkinmi?",
            "explanation": (
                "Namlik va drenaj muammolari paydo bo'lishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L03_M07_005": [
        {
            "code": "L03_Q103",
            "question": "Parking juda tik nishabda bo'lsa bu muammo bo'lishi mumkinmi?",
            "explanation": (
                "Avtomobil kirishi va to'xtashi noqulaylashishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L03_Q104",
            "question": "Hovlining katta qismi foydalanib bo'lmaydigan nishabda qolishi fazoviy xatomi?",
            "explanation": (
                "Family foydalanishi uchun qulay tashqi platformalar kerak bo'lishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L03_Q105",
            "question": "Relyef auditida qaysi savol muhim?",
            "explanation": (
                "Eng baland, past nuqta va suv yo'nalishini tushunish asosiy tahlil hisoblanadi."
            ),
            "options": [
                ("A", "Suv qayerga oqadi?", True),
                ("B", "Faqat devor rangi qanday?", False),
            ],
        },
    ],
}


# ============================================================
# DATABASE SEED
# ============================================================

def seed_level03_module07():
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
        ) in LEVEL03_MODULE07_LESSONS:

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
