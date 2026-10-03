from database.database import get_connection


LEVEL09_MODULE03_LESSONS = [
    (
        "L09_M03",
        "L09_M03_001",
        "Uchastkani normativ o'qish",
        "theory",
        "Yer uchastkasini huquqiy va shaharsozlik cheklovlari bilan birga tahlil qilish.",
        1,
        50,
        20,
    ),
    (
        "L09_M03",
        "L09_M03_002",
        "Chegaralar, kirish va joylashtirish",
        "theory",
        "Uchastka chegaralari, ko'cha, kirishlar va bino joylashuvini tekshiruv savollari orqali baholash.",
        2,
        55,
        20,
    ),
    (
        "L09_M03",
        "L09_M03_003",
        "Qo'shni obyektlar va tashqi aloqalar",
        "practice",
        "Qo'shni bino, hovli va tashqi infratuzilma bilan aloqalarni normativ tahlil qilish.",
        3,
        60,
        20,
    ),
    (
        "L09_M03",
        "L09_M03_004",
        "Genplan koordinatsiyasi",
        "practice",
        "Uy, yo'l, yashil zona, xo'jalik va muhandislik elementlarini genplanda koordinatsiya qilish.",
        4,
        65,
        20,
    ),
    (
        "L09_M03",
        "L09_M03_005",
        "Uchastka professional audit",
        "practice",
        "Uchastkani joylashtirish bo'yicha kompleks normativ audit o'tkazish.",
        5,
        70,
        25,
    ),
]


LEVEL09_MODULE03_CONTENT = {
    "L09_M03_001": [
        {
            "title": "Uchastka faqat o'lcham emas",
            "type": "highlight",
            "text": """
            Yer uchastkasini
            faqat uzunlik
            va kenglik bilan

            <br><br>

            baholash yetarli emas.
            """,
        },
        {
            "title": "Boshlang'ich ma'lumot",
            "type": "normal",
            "text": """
            Tekshiriladi:

            • chegaralar;<br>
            • ko'cha;<br>
            • kirish;<br>
            • mavjud bino;<br>
            • relyef;<br>
            • tarmoqlar;<br>
            • atrof kontekst.
            """,
        },
        {
            "title": "Taxmin qilmang",
            "type": "warning",
            "text": """
            Faqat umumiy
            uchastka o'lchamiga
            qarab

            <br><br>

            normativ xulosa
            bermang.
            """,
        },
        {
            "title": "Tasavvur qiling",
            "type": "example",
            "text": """
            Uchastka katta.

            <br><br>

            Lekin unda
            mavjud tarmoq,
            qo'shni bino
            yoki boshqa cheklov
            bo'lishi mumkin.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Uchastka uchun
            12 bandli
            boshlang'ich

            <br><br>

            ma'lumot checklist
            tuzing.
            """,
        },
    ],

    "L09_M03_002": [
        {
            "title": "Chegara va bino",
            "type": "highlight",
            "text": """
            Bino joyi
            uchastka chegarasi
            bilan

            <br><br>

            mantiqiy va
            normativ aloqada
            bo'lishi kerak.
            """,
        },
        {
            "title": "Kirish",
            "type": "normal",
            "text": """
            Piyoda va
            avtomobil kirishi

            <br><br>

            ko'cha,
            darvoza,
            bino kirishi
            va hovli

            <br><br>

            bilan koordinatsiya
            qilinadi.
            """,
        },
        {
            "title": "Aniq masofa",
            "type": "warning",
            "text": """
            Chegaradan
            aniq masofani

            <br><br>

            amaldagi
            tegishli normativni
            ko'rmasdan

            <br><br>

            yoddan kiritmang.
            """,
        },
        {
            "title": "Ko'cha tomoni",
            "type": "normal",
            "text": """
            Ko'chaga nisbatan
            joylashtirish

            <br><br>

            genplan
            va shaharsozlik
            qarorining bir qismi.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Genplanda:

            • barcha chegaralar;<br>
            • ko'cha;<br>
            • darvoza;<br>
            • asosiy kirish

            <br><br>

            nuqtalarini belgilang.
            """,
        },
    ],

    "L09_M03_003": [
        {
            "title": "Qo'shni ham loyiha konteksti",
            "type": "highlight",
            "text": """
            Faqat o'z
            uchastkangizni ko'rish

            <br><br>

            yetarli emas.
            """,
        },
        {
            "title": "Tashqi ta'sirlar",
            "type": "normal",
            "text": """
            Qo'shni obyekt:

            • soyalanish;<br>
            • ko'rinish;<br>
            • yong'in xavfsizligi;<br>
            • privacy;<br>
            • kirish

            <br><br>

            masalalariga
            ta'sir qilishi mumkin.
            """,
        },
        {
            "title": "Kontekstni unutish",
            "type": "warning",
            "text": """
            Atrofdagi
            mavjud qurilishni
            hisobga olmasdan

            <br><br>

            uy joylashtirish
            keyinchalik
            katta konflikt
            tug'dirishi mumkin.
            """,
        },
        {
            "title": "4 tomon tahlili",
            "type": "example",
            "text": """
            Uchastkaning:

            • shimoli;<br>
            • janubi;<br>
            • sharqi;<br>
            • g'arbi

            <br><br>

            bo'yicha
            alohida kontekst
            tahlili qiling.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Har bir tomon
            uchun:

            • qo'shni;<br>
            • ko'rinish;<br>
            • quyosh;<br>
            • kirish;<br>
            • xavf

            <br><br>

            yozing.
            """,
        },
    ],

    "L09_M03_004": [
        {
            "title": "Genplan tizim",
            "type": "highlight",
            "text": """
            Genplan
            faqat uy konturi
            va daraxtlardan

            <br><br>

            iborat emas.
            """,
        },
        {
            "title": "Asosiy zonalar",
            "type": "normal",
            "text": """
            • bino;<br>
            • piyoda yo'li;<br>
            • avtomobil yo'li;<br>
            • dam olish zonasi;<br>
            • xo'jalik zonasi;<br>
            • yashil zona;<br>
            • muhandislik kirishlari.
            """,
        },
        {
            "title": "Uy va uchastka",
            "type": "warning",
            "text": """
            Avval uy planini
            tugatib,

            <br><br>

            keyin uni
            tasodifiy uchastkaga
            qo'yish

            <br><br>

            yaxshi workflow
            emas.
            """,
        },
        {
            "title": "Aloqalar",
            "type": "normal",
            "text": """
            Har bir zona
            bir-biriga

            <br><br>

            xavfsiz va
            funksional
            bog'lanishi kerak.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Genplan uchun
            bubble diagram
            tayyorlang.

            <br><br>

            Zonalar orasidagi
            aloqalarni
            strelka bilan
            ko'rsating.
            """,
        },
    ],

    "L09_M03_005": [
        {
            "title": "Uchastka audit",
            "type": "highlight",
            "text": """
            Hujjatlar
            → Chegaralar
            → Kirish
            → Bino joyi
            → Qo'shnilar
            → Tarmoqlar
            → Zonalar
            → Normativ audit
            """,
        },
        {
            "title": "Audit status",
            "type": "example",
            "text": """
            Har bir masala:

            • TEKSHIRILDI<br>
            • OCHIQ SAVOL<br>
            • QAYTA ISHLASH

            <br><br>

            statusiga ega
            bo'lishi mumkin.
            """,
        },
        {
            "title": "Chiroyli = mos emas",
            "type": "warning",
            "text": """
            Vizual jihatdan
            chiroyli genplan

            <br><br>

            avtomatik ravishda
            normativga mos
            degani emas.
            """,
        },
        {
            "title": "Professional checklist",
            "type": "example",
            "text": """
            <b>1.</b> Uchastka hujjatlari aniqmi?<br><br>
            <b>2.</b> Chegaralar to'g'rimi?<br><br>
            <b>3.</b> Ko'cha va kirish aniqmi?<br><br>
            <b>4.</b> Qo'shni obyektlar tekshirilganmi?<br><br>
            <b>5.</b> Tarmoqlar ma'lummi?<br><br>
            <b>6.</b> Zonalar ishlaydimi?<br><br>
            <b>7.</b> Tegishli normativ bandlar tekshirilganmi?
            """,
        },
        {
            "title": "Modul yakuni",
            "type": "highlight",
            "text": """
            Siz endi
            uchastkani

            <br><br>

            faqat geometriya
            emas,

            <br><br>

            normativ va
            shaharsozlik konteksti
            bilan o'qiysiz.
            """,
        },
    ],
}


LEVEL09_MODULE03_QUIZ = {
    "L09_M03_001": [
        {
            "code": "L09_Q031",
            "question": "Uchastka tahlili faqat uning uzunligi va kengligidan iboratmi?",
            "explanation": "Chegaralar, atrof kontekst, kirish, tarmoqlar va boshqa omillar ham muhim.",
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L09_Q032",
            "question": "Mavjud muhandislik tarmoqlari uchastka loyihasiga ta'sir qilishi mumkinmi?",
            "explanation": "Tarmoqlar bino va genplan qarorlariga ta'sir qilishi mumkin.",
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L09_Q033",
            "question": "Atrofdagi mavjud qurilishni tahlil qilish foydalimi?",
            "explanation": "Qo'shni kontekst joylashtirish va boshqa loyiha qarorlariga ta'sir qiladi.",
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L09_M03_002": [
        {
            "code": "L09_Q034",
            "question": "Bino joylashuvi uchastka chegaralari bilan koordinatsiya qilinadimi?",
            "explanation": "Chegaralar genplan qarorining asosiy elementlaridan biridir.",
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L09_Q035",
            "question": "Chegaradan aniq masofani normativ manbasiz yoddan belgilash to'g'rimi?",
            "explanation": "Aniq qiymatlar tegishli amaldagi manbadan tekshirilishi kerak.",
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L09_Q036",
            "question": "Piyoda va avtomobil kirishlarini alohida tahlil qilish foydalimi?",
            "explanation": "Ularning funksiyasi va harakat talablari farq qilishi mumkin.",
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L09_M03_003": [
        {
            "code": "L09_Q037",
            "question": "Qo'shni bino soyalanishga ta'sir qilishi mumkinmi?",
            "explanation": "Qo'shni obyekt tabiiy yorug'lik va quyoshga ta'sir qilishi mumkin.",
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L09_Q038",
            "question": "Faqat o'z uchastkangizni ko'rish har doim yetarlimi?",
            "explanation": "Atrof kontekst ham loyiha qarorlariga ta'sir qiladi.",
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L09_Q039",
            "question": "Qo'shni obyekt bilan yong'in xavfsizligi aloqasi bo'lishi mumkinmi?",
            "explanation": "Bino joylashuvi va qo'shni kontekst yong'in xavfsizligi tekshiruviga ta'sir qilishi mumkin.",
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L09_M03_004": [
        {
            "code": "L09_Q040",
            "question": "Genplan faqat bino konturi va landshaftdan iboratmi?",
            "explanation": "Harakat, xo'jalik, tarmoqlar va boshqa zonalar ham genplanning bir qismi.",
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L09_Q041",
            "question": "Uy va uchastkani parallel rivojlantirish foydalimi?",
            "explanation": "Bu bino va tashqi makon o'rtasidagi konfliktlarni erta aniqlashga yordam beradi.",
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L09_Q042",
            "question": "Muhandislik kirishlari genplan bilan koordinatsiya qilinadimi?",
            "explanation": "Tashqi tarmoqlar bino va uchastka qarorlariga bog'liq.",
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L09_M03_005": [
        {
            "code": "L09_Q043",
            "question": "Uchastka auditida hujjatlar va chegaralar tekshiriladimi?",
            "explanation": "Ular genplan uchun asosiy boshlang'ich ma'lumot.",
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L09_Q044",
            "question": "Chiroyli genplan avtomatik ravishda normativga mos deganimi?",
            "explanation": "Vizual sifat va normativ moslik alohida tekshiriladi.",
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L09_Q045",
            "question": "Uchastka auditining to'g'ri workflow'i qaysi?",
            "explanation": "Hujjat va chegaralardan boshlanib, joylashtirish, kontekst va normativ tekshiruv bilan yakunlanadi.",
            "options": [
                (
                    "A",
                    "Hujjatlar → chegaralar → kirish → joylashtirish → kontekst → normativ audit",
                    True,
                ),
                (
                    "B",
                    "Faqat uy konturi → tasodifiy joylashtirish",
                    False,
                ),
            ],
        },
    ],
}


def seed_level09_module03():
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
        ) in LEVEL09_MODULE03_LESSONS:

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
