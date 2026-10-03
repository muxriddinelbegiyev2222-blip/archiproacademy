from database.database import get_connection


LEVEL09_MODULE02_LESSONS = [
    (
        "L09_M02",
        "L09_M02_001",
        "Turar joy obyektini normativ nuqtai nazardan o'qish",
        "theory",
        "Turar joy loyihasini funksiyalar, xonalar va xavfsizlik nuqtai nazaridan normativ tahlil qilish.",
        1,
        60,
        20,
    ),
    (
        "L09_M02",
        "L09_M02_002",
        "Xona funksiyasi va o'zaro aloqalar",
        "theory",
        "Xonalar vazifasi, zonalash va kundalik foydalanish mantiqini normativ tekshiruv bilan bog'lash.",
        2,
        70,
        20,
    ),
    (
        "L09_M02",
        "L09_M02_003",
        "Sanitar va yordamchi zonalar",
        "practice",
        "Sanuzel, oshxona, texnik va yordamchi xonalarni normativ savollar orqali tekshirish.",
        3,
        70,
        20,
    ),
    (
        "L09_M02",
        "L09_M02_004",
        "Qavatlar va vertikal aloqa",
        "practice",
        "Bir va ikki qavatli turar joylarda qavatlar o'rtasidagi funksional va xavfsizlik aloqalarini tekshirish.",
        4,
        75,
        20,
    ),
    (
        "L09_M02",
        "L09_M02_005",
        "Turar joy professional audit",
        "practice",
        "Turar joy loyihasini kompleks normativ checklist asosida tekshirish.",
        5,
        85,
        25,
    ),
]


LEVEL09_MODULE02_CONTENT = {
    "L09_M02_001": [
        {
            "title": "Turar joyni tizim sifatida ko'ring",
            "type": "highlight",
            "text": """
            Turar joy
            normativ tekshiruvi

            <br><br>

            faqat xona
            maydonini tekshirish
            emas.
            """,
        },
        {
            "title": "Nimalar birga tekshiriladi?",
            "type": "normal",
            "text": """
            • funksiya;<br>
            • zonalash;<br>
            • circulation;<br>
            • tabiiy yorug'lik;<br>
            • sanitar zonalar;<br>
            • xavfsizlik;<br>
            • tashqi muhit bilan aloqa.
            """,
        },
        {
            "title": "Aniq raqamlar",
            "type": "warning",
            "text": """
            Minimal maydon,
            kenglik
            yoki balandlikni

            <br><br>

            amaldagi normativ
            manbasiz
            kiritmang.
            """,
        },
        {
            "title": "Tasavvur qiling",
            "type": "example",
            "text": """
            Plan chiroyli.

            <br><br>

            Lekin:

            • xonalar noto'g'ri bog'langan;<br>
            • tabiiy yorug'lik muammoli;<br>
            • sanuzel koordinatsiyasi yomon.

            <br><br>

            Demak faqat
            kompozitsiya yetarli emas.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Bir uy planini
            tanlang.

            <br><br>

            U uchun
            10 ta normativ
            tekshiruv savolini
            tuzing.
            """,
        },
    ],

    "L09_M02_002": [
        {
            "title": "Xona nomidan ko'ra funksiya muhim",
            "type": "highlight",
            "text": """
            Normativ tekshiruvda
            xona faqat
            nomiga qarab emas,

            <br><br>

            real foydalanishiga
            qarab tahlil qilinadi.
            """,
        },
        {
            "title": "Zonalar",
            "type": "normal",
            "text": """
            Turar joyda:

            <br><br>

            • public;<br>
            • private;<br>
            • service

            <br><br>

            zonalar o'zaro
            mantiqiy ishlashi kerak.
            """,
        },
        {
            "title": "Xona nomini almashtirish",
            "type": "warning",
            "text": """
            Xona nomini
            hujjatda o'zgartirish

            <br><br>

            uning real
            funksiyasini
            avtomatik o'zgartirmaydi.
            """,
        },
        {
            "title": "Circulation",
            "type": "normal",
            "text": """
            Xonaga kirish,
            undan chiqish
            va boshqa zonalar
            bilan aloqa

            <br><br>

            normativ va
            funksional tekshiruvning
            bir qismi.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Public,
            private
            va service

            <br><br>

            zonalarni ajrating.

            <br><br>

            Ular orasidagi
            konfliktlarni yozing.
            """,
        },
    ],

    "L09_M02_003": [
        {
            "title": "Sanitar va texnik zonalar",
            "type": "highlight",
            "text": """
            Oshxona,
            sanuzel,
            laundry
            va texnik xonalar

            <br><br>

            arxitektura
            bilan birga
            MEP tizimlariga
            ham bog'liq.
            """,
        },
        {
            "title": "Faqat mebel emas",
            "type": "warning",
            "text": """
            Sanitar jihozni
            plan ichiga
            sig'dirishning o'zi

            <br><br>

            professional
            yechim emas.
            """,
        },
        {
            "title": "Koordinatsiya",
            "type": "normal",
            "text": """
            Tekshiriladi:

            • suv;<br>
            • kanalizatsiya;<br>
            • ventilyatsiya;<br>
            • konstruksiya;<br>
            • namlik himoyasi.
            """,
        },
        {
            "title": "Qavatlararo aloqa",
            "type": "example",
            "text": """
            Ikki qavatli uyda
            sanitar zonalarni

            <br><br>

            qavatlar bo'yicha
            mantiqiy koordinatsiya
            qilish

            <br><br>

            MEP yechimni
            soddalashtirishi mumkin.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Sanuzel va
            oshxona uchun

            <br><br>

            8 ta arxitektura
            + MEP

            <br><br>

            tekshiruv savolini
            yozing.
            """,
        },
    ],

    "L09_M02_004": [
        {
            "title": "Vertikal aloqa",
            "type": "highlight",
            "text": """
            Ikki qavatli uyda
            faqat har bir
            qavat planini

            <br><br>

            alohida tekshirish
            yetarli emas.
            """,
        },
        {
            "title": "Zinapoya",
            "type": "normal",
            "text": """
            Zinapoya:

            • circulation;<br>
            • xavfsizlik;<br>
            • opening;<br>
            • konstruksiya;<br>
            • qavat balandligi

            <br><br>

            bilan bog'liq.
            """,
        },
        {
            "title": "Faqat dizayn emas",
            "type": "warning",
            "text": """
            Zinapoyani
            faqat dekorativ
            element sifatida

            <br><br>

            loyihalash mumkin emas.
            """,
        },
        {
            "title": "Qavatlararo funksiyalar",
            "type": "normal",
            "text": """
            Yuqori va
            pastki qavatdagi

            <br><br>

            funksiyalar
            o'zaro mantiqiy
            bog'lanishi kerak.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Ikki qavatli uy uchun
            qavatlararo

            <br><br>

            8 ta tekshiruv
            savolini yozing.
            """,
        },
    ],

    "L09_M02_005": [
        {
            "title": "Turar joy audit",
            "type": "highlight",
            "text": """
            Obyekt turi
            → Xonalar
            → Zonalash
            → Circulation
            → Tabiiy sharoit
            → Sanitar zonalar
            → Vertikal aloqa
            → Xavfsizlik
            """,
        },
        {
            "title": "Audit jadvali",
            "type": "example",
            "text": """
            Har bir element uchun:

            • tekshiruv mavzusi;<br>
            • normativ manba;<br>
            • loyiha holati;<br>
            • status;<br>
            • izoh;<br>
            • yechim.
            """,
        },
        {
            "title": "Bir band yetmaydi",
            "type": "warning",
            "text": """
            Bitta xona
            talabga mos

            <br><br>

            ekanligi
            butun uy
            mos degani emas.
            """,
        },
        {
            "title": "Qayta tekshiruv",
            "type": "normal",
            "text": """
            Loyiha o'zgarsa
            tegishli normativ
            masalalar ham

            <br><br>

            qayta tekshiriladi.
            """,
        },
        {
            "title": "Professional checklist",
            "type": "example",
            "text": """
            <b>1.</b> Obyekt turi aniqmi?<br><br>
            <b>2.</b> Xonalar funksiyasi to'g'rimi?<br><br>
            <b>3.</b> Zonalash ishlaydimi?<br><br>
            <b>4.</b> Circulation tushunarlimi?<br><br>
            <b>5.</b> Sanitar zonalar koordinatsiya qilinganmi?<br><br>
            <b>6.</b> Qavatlararo aloqa tekshirilganmi?<br><br>
            <b>7.</b> Tegishli normativ manbalar qayd qilinganmi?
            """,
        },
    ],
}


LEVEL09_MODULE02_QUIZ = {
    "L09_M02_001": [
        {
            "code": "L09_Q016",
            "question": "Turar joy normativ tekshiruvi faqat xona maydonidan iboratmi?",
            "explanation": "Funksiya, circulation, tabiiy sharoit va xavfsizlik kabi boshqa masalalar ham tekshiriladi.",
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L09_Q017",
            "question": "Aniq minimal o'lchamni amaldagi normativ manbasiz kiritish to'g'rimi?",
            "explanation": "Aniq talab amaldagi tegishli hujjatdan olinishi kerak.",
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L09_Q018",
            "question": "Turar joyni tizim sifatida audit qilish kerakmi?",
            "explanation": "Uy ichidagi funksiyalar va xavfsizlik masalalari o'zaro bog'langan.",
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L09_M02_002": [
        {
            "code": "L09_Q019",
            "question": "Xonaning real funksiyasi normativ tekshiruvda muhimmi?",
            "explanation": "Talablar ko'pincha xonaning real foydalanish turiga bog'liq.",
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L09_Q020",
            "question": "Xona nomini o'zgartirish uning real funksiyasini avtomatik o'zgartiradimi?",
            "explanation": "Nom emas, real foydalanish va loyiha sharoiti muhim.",
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L09_Q021",
            "question": "Public, private va service zonalar o'zaro koordinatsiya qilinadimi?",
            "explanation": "Zonalash foydalanuvchi harakati va qulayligiga ta'sir qiladi.",
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L09_M02_003": [
        {
            "code": "L09_Q022",
            "question": "Sanuzel va oshxona MEP tizimlari bilan bog'liqmi?",
            "explanation": "Suv, kanalizatsiya va ventilyatsiya kabi tizimlar bilan koordinatsiya kerak.",
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L09_Q023",
            "question": "Sanitar jihozni plan ichiga sig'dirishning o'zi yetarlimi?",
            "explanation": "Foydalanish, MEP va boshqa loyiha masalalari ham tekshiriladi.",
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L09_Q024",
            "question": "Sanitar zonalarni qavatlar bo'yicha koordinatsiya qilish foydalimi?",
            "explanation": "Bu muhandislik tizimlarini mantiqiy tashkil qilishga yordam beradi.",
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L09_M02_004": [
        {
            "code": "L09_Q025",
            "question": "Ikki qavatli uyda qavatlar o'zaro alohida-alohida ko'rilib qolmasligi kerakmi?",
            "explanation": "Vertikal circulation va muhandislik aloqalari qavatlarni birlashtiradi.",
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L09_Q026",
            "question": "Zinapoya faqat dekorativ elementmi?",
            "explanation": "Zinapoya circulation, xavfsizlik va konstruktsiya bilan bog'liq.",
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L09_Q027",
            "question": "Qavat balandligi zinapoya yechimiga ta'sir qiladimi?",
            "explanation": "Zinapoya geometriyasi qavatlar orasidagi balandlik bilan bog'liq.",
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L09_M02_005": [
        {
            "code": "L09_Q028",
            "question": "Turar joy professional auditida funksional zonalash tekshiriladimi?",
            "explanation": "Zonalash turar joyning asosiy loyiha masalalaridan biridir.",
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L09_Q029",
            "question": "Bitta xona talabga mos bo'lsa butun loyiha avtomatik mos bo'ladimi?",
            "explanation": "Loyihaning boshqa qismlarida alohida talablar bo'lishi mumkin.",
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L09_Q030",
            "question": "Turar joy auditining to'g'ri workflow'i qaysi?",
            "explanation": "Obyekt va funksiyalar aniqlanib, turli loyiha masalalari amaldagi normativ manbalar bilan tekshiriladi.",
            "options": [
                (
                    "A",
                    "Obyekt → funksiyalar → zonalash → circulation → sanitar/vertikal aloqa → normativ audit",
                    True,
                ),
                (
                    "B",
                    "Faqat xona nomlari → tekshirmasdan yakunlash",
                    False,
                ),
            ],
        },
    ],
}


def seed_level09_module02():
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
        ) in LEVEL09_MODULE02_LESSONS:

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
