from database.database import get_connection


LEVEL15_MODULE01_LESSONS = [
    ("L15_M01", "L15_M01_001", "Arxitektura nazariyasi integratsiyasi", "theory", "Oldingi levellardagi arxitektura bilimlarini yagona tizimga birlashtirish.", 1, 60, 25),
    ("L15_M01", "L15_M01_002", "Site, planning va ergonomika nazorati", "practice", "Uchastka va rejalashtirish bo'yicha kompleks nazariy tekshiruv.", 2, 70, 25),
    ("L15_M01", "L15_M01_003", "Konstruktsiya va normativ fikrlash", "practice", "Arxitektura qarorining texnik va normativ oqibatlarini tahlil qilish.", 3, 70, 25),
    ("L15_M01", "L15_M01_004", "BIM va hujjatlashtirish nazariyasi", "practice", "Model, data va hujjatlar orasidagi bog'lanishni tekshirish.", 4, 75, 25),
    ("L15_M01", "L15_M01_005", "PRO nazariya mastery audit", "practice", "Nazariy bilimlarni case-based savollar orqali yakuniy tekshirish.", 5, 85, 30),
]


LEVEL15_MODULE01_CONTENT = {
    "L15_M01_001": [
        {"title": "Endi mavzular alohida emas", "type": "highlight", "text": "Professional qarorda site, plan, ergonomika, konstruksiya, BIM va mijoz talabi bir vaqtning o'zida ishlaydi."},
        {"title": "Maqsad", "type": "normal", "text": "Faqat terminni eslash emas, real loyiha vaziyatida qaysi bilimni qachon qo'llashni bilish."},
        {"title": "Xato", "type": "warning", "text": "Nazariyani yodlangan ta'riflar to'plami sifatida qabul qilmang."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Bir uy loyihasida bir-biriga bog'liq 10 ta qarorni yozing."},
    ],
    "L15_M01_002": [
        {"title": "Site + plan", "type": "highlight", "text": "Kirish, quyosh, qo'shni, privacy, hovli va room program bir-biridan ajralmaydi."},
        {"title": "Ergonomika", "type": "normal", "text": "Xona faqat maydon emas; mebel, harakat va real foydalanish bilan tekshiriladi."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Bitta plan uchun 15 bandli functional audit yozing."},
    ],
    "L15_M01_003": [
        {"title": "Arxitektor chegarani biladi", "type": "highlight", "text": "Arxitektor konstruktiv mantiqni tushunadi, lekin professional hisob talab qiladigan qarorni taxmin bilan almashtirmaydi."},
        {"title": "Normativ fikrlash", "type": "normal", "text": "Aniq talab va o'lchamlar amaldagi tegishli normativ manbalardan tekshiriladi."},
        {"title": "Xato", "type": "warning", "text": "Eski yoki tekshirilmagan raqamni universal norma sifatida ishlatmang."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Architect / structural engineer / MEP / normative check vazifalarini ajrating."},
    ],
    "L15_M01_004": [
        {"title": "BIM chain", "type": "highlight", "text": "Model → Data → Views → Schedules → Layouts → Publisher → Exchange."},
        {"title": "Consistency", "type": "normal", "text": "Professional BIM workflowda bir o'zgarish tegishli loyiha hujjatlarida nazorat qilinadi."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Final BIM deliverable uchun QA chain tuzing."},
    ],
    "L15_M01_005": [
        {"title": "PRO Theory audit", "type": "highlight", "text": "Architecture → Site → Planning → Ergonomics → Structure → Regulations → BIM → Documentation → Client."},
        {"title": "Mastery", "type": "normal", "text": "Savolga javobni bilishdan tashqari, noto'g'ri variant nega noto'g'ri ekanini ham tushuntira olish kerak."},
        {"title": "Keyingi modul", "type": "highlight", "text": "Keyingi modul: ARCHICAD PRO IMTIHONI."},
    ],
}


LEVEL15_MODULE01_QUIZ = {}

for i, lesson_code in enumerate(
    ["L15_M01_001", "L15_M01_002", "L15_M01_003", "L15_M01_004", "L15_M01_005"]
):
    start = 1 + i * 3

    LEVEL15_MODULE01_QUIZ[lesson_code] = [
        {
            "code": f"L15_Q{start:03d}",
            "question": "Professional loyiha qarorlari bir nechta fan va omilni birlashtiradimi?",
            "explanation": "Arxitektura qarori site, funksiya, texnika va boshqa omillar bilan bog'liq.",
            "options": [("A", "Ha", True), ("B", "Yo'q", False)],
        },
        {
            "code": f"L15_Q{start + 1:03d}",
            "question": "Aniq konstruktiv hisobni taxmin bilan almashtirish to'g'rimi?",
            "explanation": "Hisob talab qiladigan masala tegishli mutaxassis tomonidan tekshiriladi.",
            "options": [("A", "Ha", False), ("B", "Yo'q", True)],
        },
        {
            "code": f"L15_Q{start + 2:03d}",
            "question": "PRO nazariya faqat terminlarni yodlashdan iboratmi?",
            "explanation": "Bilim real loyiha vaziyatida qo'llanilishi kerak.",
            "options": [("A", "Ha", False), ("B", "Yo'q", True)],
        },
    ]


def seed_level15_module01():
    connection = get_connection()
    try:
        cursor = connection.cursor()

        for row in LEVEL15_MODULE01_LESSONS:
            module_code, lesson_code, title, lesson_type, summary, sort_order, estimated_minutes, xp_reward = row

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
                    module["id"], lesson_code, title, lesson_type,
                    summary, sort_order, estimated_minutes,
                    xp_reward, 80, 1,
                ),
            )

        connection.commit()
    finally:
        connection.close()
