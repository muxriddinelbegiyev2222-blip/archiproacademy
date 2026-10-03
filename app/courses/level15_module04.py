from database.database import get_connection


LEVEL15_MODULE04_LESSONS = [
    ("L15_M04", "L15_M04_001", "Final briefni qabul qilish", "theory", "Final loyiha uchun mijoz va site ma'lumotlarini professional yig'ish.", 1, 30, 25),
    ("L15_M04", "L15_M04_002", "Talablarni klassifikatsiya qilish", "practice", "Funksiya, site, budjet va texnik talablarni tartiblash.", 2, 35, 25),
    ("L15_M04", "L15_M04_003", "Constraints va risklar", "practice", "Final loyiha cheklovlari va asosiy risklarni aniqlash.", 3, 35, 25),
    ("L15_M04", "L15_M04_004", "Deliverables va success criteria", "practice", "Final loyiha topshirish tarkibi va muvaffaqiyat mezonlarini belgilash.", 4, 40, 25),
    ("L15_M04", "L15_M04_005", "Final texnik topshiriq auditi", "practice", "Final briefni loyiha boshlashga tayyor holatga keltirish.", 5, 40, 30),
]


LEVEL15_MODULE04_CONTENT = {
    "L15_M04_001": [
        {"title": "Final loyiha shu yerdan boshlanadi", "type": "highlight", "text": "Endi sizga tayyor ideal masala emas, real loyihaga o'xshash brief kerak."},
        {"title": "Yig'iladi", "type": "normal", "text": "Client, family, site, lifestyle, rooms, style, budget, schedule va open questions."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Final client interview form tayyorlang."},
    ],
    "L15_M04_002": [
        {"title": "Requirements matrix", "type": "highlight", "text": "Har talab category va priority bilan qayd qilinadi."},
        {"title": "MUST / SHOULD / OPTIONAL", "type": "normal", "text": "Konflikt paydo bo'lganda qaysi talabni himoya qilish kerakligi aniq bo'ladi."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Final loyiha uchun requirement matrix tuzing."},
    ],
    "L15_M04_003": [
        {"title": "Risk register", "type": "highlight", "text": "Site, normativ, konstruksiya, budjet, MEP yoki vaqt bo'yicha asosiy risklar oldindan yoziladi."},
        {"title": "Xato", "type": "warning", "text": "Noma'lum yoki tekshirilmagan masalani yashirib loyiha boshlamang."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Top-10 project risk register yarating."},
    ],
    "L15_M04_004": [
        {"title": "Deliverables", "type": "highlight", "text": "Finalda aynan nima topshirilishi boshidan aniq bo'lishi kerak."},
        {"title": "Success criteria", "type": "normal", "text": "Funksiya, BIM, chizma, presentation va boshqa mezonlar oldindan belgilanadi."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Final submission checklist yozing."},
    ],
    "L15_M04_005": [
        {"title": "Final brief audit", "type": "highlight", "text": "Client → Site → Program → Priorities → Constraints → Risks → Deliverables → Confirmation."},
        {"title": "Keyingi modul", "type": "highlight", "text": "Keyingi modul: FINAL LOYIHA."},
    ],
}


LEVEL15_MODULE04_QUIZ = {}

for i, lesson_code in enumerate(
    ["L15_M04_001", "L15_M04_002", "L15_M04_003", "L15_M04_004", "L15_M04_005"]
):
    start = 46 + i * 3

    LEVEL15_MODULE04_QUIZ[lesson_code] = [
        {
            "code": f"L15_Q{start:03d}",
            "question": "Final loyiha aniq brief va talablar bilan boshlanishi kerakmi?",
            "explanation": "Final project maqsadi oldindan tushunarli bo'lishi kerak.",
            "options": [("A", "Ha", True), ("B", "Yo'q", False)],
        },
        {
            "code": f"L15_Q{start + 1:03d}",
            "question": "Risk va noma'lum masalalarni yashirib loyiha boshlash to'g'rimi?",
            "explanation": "Risklar oldindan qayd qilinishi kerak.",
            "options": [("A", "Ha", False), ("B", "Yo'q", True)],
        },
        {
            "code": f"L15_Q{start + 2:03d}",
            "question": "Final deliverables oldindan aniqlanishi foydalimi?",
            "explanation": "Loyiha scope va yakuniy natija tushunarli bo'ladi.",
            "options": [("A", "Ha", True), ("B", "Yo'q", False)],
        },
    ]


def seed_level15_module04():
    connection = get_connection()
    try:
        cursor = connection.cursor()

        for row in LEVEL15_MODULE04_LESSONS:
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
