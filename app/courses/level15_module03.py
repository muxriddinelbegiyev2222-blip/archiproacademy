from database.database import get_connection


LEVEL15_MODULE03_LESSONS = [
    ("L15_M03", "L15_M03_001", "Plan xatolarini topish", "practice", "Funksiya, ergonomika va circulation xatolarini professional aniqlash.", 1, 60, 25),
    ("L15_M03", "L15_M03_002", "Fasad va kesim xatolari", "practice", "Proporsiya, opening, level va koordinatsiya muammolarini aniqlash.", 2, 70, 25),
    ("L15_M03", "L15_M03_003", "Konstruktiv va MEP konfliktlari", "practice", "Arxitektura bilan texnik tizimlar orasidagi muammolarni aniqlash.", 3, 70, 25),
    ("L15_M03", "L15_M03_004", "BIM va documentation xatolari", "practice", "Model data, views, schedules va layout xatolarini topish.", 4, 75, 25),
    ("L15_M03", "L15_M03_005", "Root Cause PRO audit", "practice", "Xatoni topishdan uning asosiy sababini va to'g'ri yechimini aniqlashgacha bo'lgan jarayon.", 5, 85, 30),
]


LEVEL15_MODULE03_CONTENT = {
    "L15_M03_001": [
        {"title": "Xatoni ko'rish — alohida skill", "type": "highlight", "text": "Professional faqat yangi loyiha chizmaydi; mavjud loyiha muammosini ham tez aniqlaydi."},
        {"title": "Plan scan", "type": "normal", "text": "Zoning → furniture → circulation → doors → privacy → daylight → dead space."},
        {"title": "Challenge", "type": "example", "text": "Bir plan ichidan kamida 10 ta potensial muammoni toping."},
    ],
    "L15_M03_002": [
        {"title": "Cross-view error", "type": "highlight", "text": "Plan, fasad va kesim bir-birini tasdiqlashi kerak."},
        {"title": "Tekshiriladi", "type": "normal", "text": "Opening, levels, roof, slab, facade rhythm va massing."},
        {"title": "Challenge", "type": "example", "text": "Plan-fasad-section orasidagi 8 ta mismatch ssenariysini yozing."},
    ],
    "L15_M03_003": [
        {"title": "Technical conflict", "type": "highlight", "text": "Arxitektura yechimi structure va MEP uchun real joy qoldirishi kerak."},
        {"title": "Xato", "type": "warning", "text": "Beam, shaft yoki slab opening muammosini qurilish paytida hal qilamiz deb qoldirmang."},
        {"title": "Challenge", "type": "example", "text": "10 ta architecture-structure-MEP conflict yozing."},
    ],
    "L15_M03_004": [
        {"title": "BIM error", "type": "highlight", "text": "Duplicate element, wrong classification, empty property, outdated view yoki missing drawing ham loyiha xatosi."},
        {"title": "Schedule test", "type": "normal", "text": "Jadval ko'p yashirin data xatolarini ko'rsatishi mumkin."},
        {"title": "Challenge", "type": "example", "text": "BIM QA checklist orqali modelni audit qiling."},
    ],
    "L15_M03_005": [
        {"title": "Root Cause workflow", "type": "highlight", "text": "Find → classify → impact → root cause → alternatives → fix → recheck."},
        {"title": "Muhim", "type": "warning", "text": "Simptomni tuzatib, asl sababni qoldirsangiz xato qaytishi mumkin."},
        {"title": "Keyingi modul", "type": "highlight", "text": "Keyingi modul: FINAL TEXNIK TOPSHIRIQ."},
    ],
}


LEVEL15_MODULE03_QUIZ = {}

for i, lesson_code in enumerate(
    ["L15_M03_001", "L15_M03_002", "L15_M03_003", "L15_M03_004", "L15_M03_005"]
):
    start = 31 + i * 3

    LEVEL15_MODULE03_QUIZ[lesson_code] = [
        {
            "code": f"L15_Q{start:03d}",
            "question": "Professional auditda faqat xatoni topish emas, sababini ham aniqlash kerakmi?",
            "explanation": "Root cause topilmasa muammo qaytishi mumkin.",
            "options": [("A", "Ha", True), ("B", "Yo'q", False)],
        },
        {
            "code": f"L15_Q{start + 1:03d}",
            "question": "Plan yaxshi ko'rinsa BIM data va sectionni tekshirmaslik mumkinmi?",
            "explanation": "Yashirin xatolar boshqa views va data ichida bo'lishi mumkin.",
            "options": [("A", "Ha", False), ("B", "Yo'q", True)],
        },
        {
            "code": f"L15_Q{start + 2:03d}",
            "question": "Fix kiritilgach loyiha qayta tekshiriladimi?",
            "explanation": "Yangi konflikt paydo bo'lmaganini tasdiqlash kerak.",
            "options": [("A", "Ha", True), ("B", "Yo'q", False)],
        },
    ]


def seed_level15_module03():
    connection = get_connection()
    try:
        cursor = connection.cursor()

        for row in LEVEL15_MODULE03_LESSONS:
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
