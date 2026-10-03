from database.database import get_connection


LEVEL09_MODULE04_LESSONS = [
    (
        "L09_M04",
        "L09_M04_001",
        "Tabiiy yorug'lik tushunchasi",
        "theory",
        "Xona funksiyasi, deraza va tashqi muhit orqali tabiiy yorug'likni tahlil qilish.",
        1,
        40,
        20,
    ),
    (
        "L09_M04",
        "L09_M04_002",
        "Orientatsiya va quyosh",
        "theory",
        "Bino orientatsiyasi va quyosh harakatining turar joyga ta'sirini tushunish.",
        2,
        45,
        20,
    ),
    (
        "L09_M04",
        "L09_M04_003",
        "Soyalanish va qo'shni obyektlar",
        "practice",
        "Qo'shni bino, ayvon va boshqa elementlarning yorug'lik va quyoshga ta'sirini baholash.",
        3,
        50,
        20,
    ),
    (
        "L09_M04",
        "L09_M04_004",
        "Plan, fasad va kesim koordinatsiyasi",
        "practice",
        "Yoritish qarorlarini plan, fasad va kesimda bir xil mantiqda tekshirish.",
        4,
        50,
        20,
    ),
    (
        "L09_M04",
        "L09_M04_005",
        "Yoritish va insolyatsiya audit",
        "practice",
        "Tabiiy yorug'lik va quyosh bo'yicha kompleks normativ audit workflow'ini qo'llash.",
        5,
        55,
        25,
    ),
]


LEVEL09_MODULE04_CONTENT = {
    "L09_M04_001": [
        {
            "title": "Deraza borligi yetarlimi?",
            "type": "highlight",
            "text": """
            Xonada deraza
            mavjudligi

            <br><br>

            avtomatik ravishda
            tabiiy yorug'lik
            yetarli

            <br><br>

            degani emas.
            """,
        },
        {
            "title": "Ta'sir qiluvchi omillar",
            "type": "normal",
            "text": """
            • xona funksiyasi;<br>
            • deraza joyi;<br>
            • xona chuqurligi;<br>
            • tashqi to'siqlar;<br>
            • orientatsiya;<br>
            • soyalanish.
            """,
        },
        {
            "title": "Aniq hisob",
            "type": "warning",
            "text": """
            Aniq koeffitsiyent
            yoki talab

            <br><br>

            tegishli
            amaldagi normativ
            va hisob usuli

            <br><br>

            bilan tekshiriladi.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Bitta xonani
            tanlang.

            <br><br>

            Tabiiy yorug'likka
            ta'sir qiladigan

            <br><br>

            6 ta omilni
            yozing.
            """,
        },
    ],

    "L09_M04_002": [
        {
            "title": "Orientatsiya",
            "type": "highlight",
            "text": """
            Xonaning
            qaysi tomonga
            qaragani

            <br><br>

            quyosh tushish
            vaqtiga ta'sir qiladi.
            """,
        },
        {
            "title": "Universal yo'nalish yo'q",
            "type": "warning",
            "text": """
            Bitta orientatsiyani
            barcha xonalar uchun

            <br><br>

            universal
            “eng yaxshi”

            <br><br>

            deb qabul qilmang.
            """,
        },
        {
            "title": "Funksiya + iqlim",
            "type": "normal",
            "text": """
            Orientatsiya:

            • xona funksiyasi;<br>
            • mahalliy iqlim;<br>
            • tashqi to'siqlar;<br>
            • foydalanuvchi rejimi

            <br><br>

            bilan birga
            ko'riladi.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Uy xonalarini
            orientatsiya bo'yicha

            <br><br>

            tahlil qiling
            va har biri
            uchun sabab yozing.
            """,
        },
    ],

    "L09_M04_003": [
        {
            "title": "Soyalanish",
            "type": "highlight",
            "text": """
            Xonaga tushadigan
            yorug'likka

            <br><br>

            faqat deraza
            emas,

            <br><br>

            tashqi obyektlar
            ham ta'sir qiladi.
            """,
        },
        {
            "title": "Soya manbalari",
            "type": "normal",
            "text": """
            • qo'shni bino;<br>
            • daraxt;<br>
            • balkon;<br>
            • ayvon;<br>
            • tom chiqishi;<br>
            • rel'ef.
            """,
        },
        {
            "title": "Faqat fasadni ko'rmang",
            "type": "warning",
            "text": """
            O'z fasadingiz
            yaxshi bo'lsa ham

            <br><br>

            qo'shni obyekt
            xonani kuchli
            soyalashi mumkin.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Uchastkadagi
            barcha potensial

            <br><br>

            soyalanish
            manbalarini yozing.
            """,
        },
    ],

    "L09_M04_004": [
        {
            "title": "Plan",
            "type": "normal",
            "text": """
            Plan orqali:

            • deraza joyi;<br>
            • xona chuqurligi;<br>
            • orientatsiya

            <br><br>

            ko'riladi.
            """,
        },
        {
            "title": "Fasad",
            "type": "normal",
            "text": """
            Fasad orqali:

            • deraza balandligi;<br>
            • proporsiya;<br>
            • tashqi shading

            <br><br>

            ko'riladi.
            """,
        },
        {
            "title": "Kesim",
            "type": "highlight",
            "text": """
            Kesim:

            • xona balandligi;<br>
            • ayvon;<br>
            • balkon;<br>
            • tom chiqishi;<br>
            • tashqi to'siq

            <br><br>

            ta'sirini
            tushunishga yordam beradi.
            """,
        },
        {
            "title": "Faqat plan yetmaydi",
            "type": "warning",
            "text": """
            Tabiiy yorug'lik
            bo'yicha

            <br><br>

            faqat plan
            asosida yakuniy

            <br><br>

            xulosa berish
            yetarli emas.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Bitta xona uchun:

            plan,
            fasad,
            kesim

            <br><br>

            bo'yicha
            alohida tekshiruv
            savollari yozing.
            """,
        },
    ],

    "L09_M04_005": [
        {
            "title": "Yoritish audit",
            "type": "highlight",
            "text": """
            Xona funksiyasi
            → Orientatsiya
            → Deraza
            → Tashqi to'siqlar
            → Soyalanish
            → Normativ/hisob
            → Qayd
            """,
        },
        {
            "title": "Vizual baho",
            "type": "warning",
            "text": """
            Xona ko'zga
            yorug' ko'ringani

            <br><br>

            normativ hisob
            o'rnini bosmaydi.
            """,
        },
        {
            "title": "Natija kartasi",
            "type": "example",
            "text": """
            Xona<br>
            Muammo<br>
            Tekshiruv usuli<br>
            Manba<br>
            Natija<br>
            Yechim
            """,
        },
        {
            "title": "Professional checklist",
            "type": "example",
            "text": """
            <b>1.</b> Xona funksiyasi aniqmi?<br><br>
            <b>2.</b> Orientatsiya tekshirildimi?<br><br>
            <b>3.</b> Deraza holati aniqmi?<br><br>
            <b>4.</b> Tashqi soyalanish bormi?<br><br>
            <b>5.</b> Plan/fasad/kesim mosmi?<br><br>
            <b>6.</b> Tegishli normativ yoki hisob qo'llanildimi?
            """,
        },
    ],
}


LEVEL09_MODULE04_QUIZ = {
    "L09_M04_001": [
        {
            "code": "L09_Q046",
            "question": "Xonada deraza mavjudligi avtomatik ravishda yetarli tabiiy yorug'lik deganimi?",
            "explanation": "Deraza joyi, xona geometriyasi va tashqi to'siqlar ham ta'sir qiladi.",
            "options": [("A", "Ha", False), ("B", "Yo'q", True)],
        },
        {
            "code": "L09_Q047",
            "question": "Xona funksiyasi tabiiy yorug'lik tekshiruviga ta'sir qilishi mumkinmi?",
            "explanation": "Turli funksiyadagi xonalar uchun turli talablar bo'lishi mumkin.",
            "options": [("A", "Ha", True), ("B", "Yo'q", False)],
        },
        {
            "code": "L09_Q048",
            "question": "Aniq yoritish talablarini amaldagi manbadan tekshirish kerakmi?",
            "explanation": "Aniq qiymatlar tegishli normativ va hisob metodiga tayanadi.",
            "options": [("A", "Ha", True), ("B", "Yo'q", False)],
        },
    ],

    "L09_M04_002": [
        {
            "code": "L09_Q049",
            "question": "Orientatsiya xonaga tushadigan quyoshga ta'sir qiladimi?",
            "explanation": "Xonaning yo'nalishi quyosh tushish vaqtiga ta'sir qiladi.",
            "options": [("A", "Ha", True), ("B", "Yo'q", False)],
        },
        {
            "code": "L09_Q050",
            "question": "Bitta orientatsiya barcha xonalar uchun universal eng yaxshi yechimmi?",
            "explanation": "Funksiya va iqlim sharoiti ham muhim.",
            "options": [("A", "Ha", False), ("B", "Yo'q", True)],
        },
        {
            "code": "L09_Q051",
            "question": "Mahalliy iqlim orientatsiya qaroriga ta'sir qilishi mumkinmi?",
            "explanation": "Quyosh va issiqlik sharoiti hududga bog'liq.",
            "options": [("A", "Ha", True), ("B", "Yo'q", False)],
        },
    ],

    "L09_M04_003": [
        {
            "code": "L09_Q052",
            "question": "Qo'shni bino xonaning tabiiy yorug'ligiga ta'sir qilishi mumkinmi?",
            "explanation": "Qo'shni bino soyalanish yaratishi mumkin.",
            "options": [("A", "Ha", True), ("B", "Yo'q", False)],
        },
        {
            "code": "L09_Q053",
            "question": "Ayvon yoki balkon soyalanishga ta'sir qiladimi?",
            "explanation": "Tashqi elementlar derazaga tushadigan quyoshni kamaytirishi mumkin.",
            "options": [("A", "Ha", True), ("B", "Yo'q", False)],
        },
        {
            "code": "L09_Q054",
            "question": "Faqat o'z fasadingizni ko'rish yoritish auditi uchun har doim yetarlimi?",
            "explanation": "Atrof kontekst va tashqi to'siqlar ham tekshiriladi.",
            "options": [("A", "Ha", False), ("B", "Yo'q", True)],
        },
    ],

    "L09_M04_004": [
        {
            "code": "L09_Q055",
            "question": "Yoritish masalasini plan, fasad va kesimda tekshirish foydalimi?",
            "explanation": "Har bir ko'rinish turli geometrik ma'lumot beradi.",
            "options": [("A", "Ha", True), ("B", "Yo'q", False)],
        },
        {
            "code": "L09_Q056",
            "question": "Faqat plan asosida yakuniy yoritish xulosasi berish har doim yetarlimi?",
            "explanation": "Kesim va fasad tashqi soyalanish va balandliklarni ko'rsatadi.",
            "options": [("A", "Ha", False), ("B", "Yo'q", True)],
        },
        {
            "code": "L09_Q057",
            "question": "Kesim tom chiqishi yoki balkonning soyalanish ta'sirini ko'rsatishi mumkinmi?",
            "explanation": "Vertikal geometriya kesimda yaxshiroq ko'rinadi.",
            "options": [("A", "Ha", True), ("B", "Yo'q", False)],
        },
    ],

    "L09_M04_005": [
        {
            "code": "L09_Q058",
            "question": "Vizual ravishda yorug' xona normativ hisobning o'rnini bosadimi?",
            "explanation": "Vizual baho texnik yoki normativ tekshiruvni almashtirmaydi.",
            "options": [("A", "Ha", False), ("B", "Yo'q", True)],
        },
        {
            "code": "L09_Q059",
            "question": "Yoritish auditida tashqi soyalanish tekshiriladimi?",
            "explanation": "Tashqi obyektlar yorug'lik sharoitiga ta'sir qiladi.",
            "options": [("A", "Ha", True), ("B", "Yo'q", False)],
        },
        {
            "code": "L09_Q060",
            "question": "Yoritish auditining to'g'ri workflow'i qaysi?",
            "explanation": "Xona, orientatsiya, deraza va tashqi kontekst tekshirilgach tegishli normativ/hisob qo'llaniladi.",
            "options": [
                (
                    "A",
                    "Funksiya → orientatsiya → deraza → tashqi to'siqlar → normativ/hisob → audit",
                    True,
                ),
                (
                    "B",
                    "Deraza bor → avtomatik mos",
                    False,
                ),
            ],
        },
    ],
}


def seed_level09_module04():
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
        ) in LEVEL09_MODULE04_LESSONS:

            cursor.execute(
                "SELECT id FROM course_modules WHERE code = ? LIMIT 1",
                (module_code,),
            )

            module = cursor.fetchone()

            if module is None:
                continue

            cursor.execute(
                """
                INSERT INTO lessons (
                    module_id, code, title, lesson_type, summary,
                    sort_order, estimated_minutes, xp_reward,
                    passing_score, is_required
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
