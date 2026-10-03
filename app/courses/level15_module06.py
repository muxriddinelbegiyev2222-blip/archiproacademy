from database.database import get_connection


LEVEL15_MODULE06_LESSONS = [
    ("L15_M06", "L15_M06_001", "Himoya strukturasi", "theory", "Final loyihani professional hikoya va dalillar bilan taqdim etish.", 1, 60, 25),
    ("L15_M06", "L15_M06_002", "Konsept va qarorlarni asoslash", "practice", "Asosiy loyiha qarorlarini brief va site bilan bog'lab tushuntirish.", 2, 70, 25),
    ("L15_M06", "L15_M06_003", "Texnik qarorlarni himoya qilish", "practice", "Konstruktsiya, MEP va BIM koordinatsiyasini tushuntirish.", 3, 70, 25),
    ("L15_M06", "L15_M06_004", "Savol-javob va tanqid", "practice", "Murakkab savol va professional kritikaga javob berish.", 4, 75, 25),
    ("L15_M06", "L15_M06_005", "Final defense audit", "practice", "Himoya taqdimotini boshidan oxirigacha tekshirish.", 5, 85, 30),
]


LEVEL15_MODULE06_CONTENT = {
    "L15_M06_001": [
        {"title": "Himoya — loyiha hikoyasi", "type": "highlight", "text": "Problem → Brief → Site → Concept → Plan → Technical coordination → Final result."},
        {"title": "Maqsad", "type": "normal", "text": "Ko'ruvchi qarorlarning ketma-ketligini va nima uchun shunday yechim tanlanganini tushunishi kerak."},
        {"title": "Mini-amaliyot", "type": "example", "text": "15 daqiqalik final defense structure tayyorlang."},
    ],
    "L15_M06_002": [
        {"title": "Dalil", "type": "highlight", "text": "Har katta qaror brief, site yoki loyiha mezoni bilan bog'lanadi."},
        {"title": "Xato", "type": "warning", "text": "“Chiroyli ko'ringani uchun” yagona asos bo'lib qolmasligi kerak."},
        {"title": "Mini-amaliyot", "type": "example", "text": "5 asosiy qarorni Evidence → Decision → Benefit formatida yozing."},
    ],
    "L15_M06_003": [
        {"title": "Technical confidence", "type": "highlight", "text": "Arxitektor o'z modelidagi strukturaviy va muhandislik koordinatsiya mantig'ini tushuntira olishi kerak."},
        {"title": "Chegara", "type": "normal", "text": "Aniq muhandislik hisoblarini tegishli mutaxassis tasdiqlashi kerakligini ochiq aytish professional yondashuvdir."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Structure/MEP/BIM bo'yicha 10 savolga javob tayyorlang."},
    ],
    "L15_M06_004": [
        {"title": "Tanqid — hujum emas", "type": "highlight", "text": "Professional kritikani qarorni qayta tekshirish imkoniyati sifatida qabul qiling."},
        {"title": "Bilmasangiz", "type": "normal", "text": "Aniq bilmagan savolga taxminiy javob bermasdan tekshirish kerakligini ayting."},
        {"title": "Mini-amaliyot", "type": "example", "text": "10 ta qiyin jury savoli va professional javob yozing."},
    ],
    "L15_M06_005": [
        {"title": "Defense audit", "type": "highlight", "text": "Story → Evidence → Diagrams → Drawings → Technical logic → Trade-offs → Q&A → Closing."},
        {"title": "Keyingi modul", "type": "highlight", "text": "Keyingi modul: PORTFOLIO."},
    ],
}


LEVEL15_MODULE06_QUIZ = {}

for i, lesson_code in enumerate(
    ["L15_M06_001", "L15_M06_002", "L15_M06_003", "L15_M06_004", "L15_M06_005"]
):
    start = 76 + i * 3

    LEVEL15_MODULE06_QUIZ[lesson_code] = [
        {
            "code": f"L15_Q{start:03d}",
            "question": "Final himoyada loyiha qarorlari dalil bilan tushuntiriladimi?",
            "explanation": "Brief, site va boshqa mezonlar qarorni asoslaydi.",
            "options": [("A", "Ha", True), ("B", "Yo'q", False)],
        },
        {
            "code": f"L15_Q{start + 1:03d}",
            "question": "Bilmagan texnik savolga ishonch bilan taxminiy javob berish professionalmi?",
            "explanation": "Tekshirish zarurligini ochiq aytish yaxshiroq.",
            "options": [("A", "Ha", False), ("B", "Yo'q", True)],
        },
        {
            "code": f"L15_Q{start + 2:03d}",
            "question": "Tanqid loyiha qarorini qayta tekshirish imkoniyati bo'lishi mumkinmi?",
            "explanation": "Professional feedback loyiha sifatini oshirishi mumkin.",
            "options": [("A", "Ha", True), ("B", "Yo'q", False)],
        },
    ]


def seed_level15_module06():
    connection = get_connection()
    try:
        cursor = connection.cursor()

        for row in LEVEL15_MODULE06_LESSONS:
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
