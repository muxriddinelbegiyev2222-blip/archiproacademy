from database.database import get_connection


LEVEL15_MODULE02_LESSONS = [
    ("L15_M02", "L15_M02_001", "Model setup challenge", "practice", "Stories, grid, layers va template asosida professional loyiha setup yaratish.", 1, 80, 25),
    ("L15_M02", "L15_M02_002", "Modeling challenge", "practice", "Wall, slab, roof, stair va boshqa elementlarni izchil BIM modelga aylantirish.", 2, 90, 25),
    ("L15_M02", "L15_M02_003", "Advanced BIM challenge", "practice", "Properties, Classification, Schedules va Graphic Overrides bilan ishlash.", 3, 95, 25),
    ("L15_M02", "L15_M02_004", "Documentation challenge", "practice", "Views, Layout Book va Publisher workflowini tekshirish.", 4, 100, 25),
    ("L15_M02", "L15_M02_005", "Archicad PRO final audit", "practice", "To'liq Archicad workflowini modeldan outputgacha tekshirish.", 5, 115, 30),
]


LEVEL15_MODULE02_CONTENT = {
    "L15_M02_001": [
        {"title": "Setup — testning bir qismi", "type": "highlight", "text": "Professional model tartibli loyiha bazasidan boshlanadi."},
        {"title": "Tekshiriladi", "type": "normal", "text": "Stories, grid, layers, attributes, Favorites va kerakli project structure."},
        {"title": "Xato", "type": "warning", "text": "Setup xatosini keyin yuzlab elementni qo'lda tuzatish bilan qoplashga suyanmang."},
        {"title": "Challenge", "type": "example", "text": "Bo'sh projectdan professional model setup yarating."},
    ],
    "L15_M02_002": [
        {"title": "BIM modeling", "type": "highlight", "text": "Elementlar 2D chizma emas, o'z vazifasiga mos BIM obyektlar sifatida ishlatiladi."},
        {"title": "Cross-view QA", "type": "normal", "text": "Plan, 3D va section orqali model doimiy tekshiriladi."},
        {"title": "Challenge", "type": "example", "text": "Berilgan residential brief asosida asosiy BIM modelni yarating."},
    ],
    "L15_M02_003": [
        {"title": "Advanced data", "type": "highlight", "text": "Model sifati faqat geometriyada emas; data va classification ham tekshiriladi."},
        {"title": "QA", "type": "normal", "text": "Schedules va Graphic Overrides model audit vositasi sifatida ishlatiladi."},
        {"title": "Challenge", "type": "example", "text": "Noto'g'ri classification va bo'sh propertiesni topadigan audit workflow tuzing."},
    ],
    "L15_M02_004": [
        {"title": "Documentation", "type": "highlight", "text": "Saved Views, Layouts va Publisher final hujjat sifatini belgilaydi."},
        {"title": "Output", "type": "normal", "text": "PDF yoki boshqa deliverable yaratilgach qayta QA qilinadi."},
        {"title": "Challenge", "type": "example", "text": "Plan, section, elevations va schedulesdan final album chiqaring."},
    ],
    "L15_M02_005": [
        {"title": "Archicad PRO audit", "type": "highlight", "text": "Setup → Modeling → BIM Data → Views → Schedules → Layouts → Publisher → QA."},
        {"title": "Professional checklist", "type": "example", "text": "1. Model structure tozami?<br><br>2. Elementlar to'g'rimi?<br><br>3. Duplicate yo'qmi?<br><br>4. Properties to'g'rimi?<br><br>5. Schedules ishlaydimi?<br><br>6. Views latestmi?<br><br>7. Layoutlar o'qiladimi?<br><br>8. Outputs tekshirilganmi?"},
        {"title": "Keyingi modul", "type": "highlight", "text": "Keyingi modul: XATONI TOP PRO."},
    ],
}


LEVEL15_MODULE02_QUIZ = {}

for i, lesson_code in enumerate(
    ["L15_M02_001", "L15_M02_002", "L15_M02_003", "L15_M02_004", "L15_M02_005"]
):
    start = 16 + i * 3

    LEVEL15_MODULE02_QUIZ[lesson_code] = [
        {
            "code": f"L15_Q{start:03d}",
            "question": "Professional Archicad workflow model setupdan boshlanadimi?",
            "explanation": "Project structure keyingi model sifatiga ta'sir qiladi.",
            "options": [("A", "Ha", True), ("B", "Yo'q", False)],
        },
        {
            "code": f"L15_Q{start + 1:03d}",
            "question": "BIM modelni faqat plan ko'rinishida tekshirish yetarlimi?",
            "explanation": "3D, section va boshqa views ham kerak.",
            "options": [("A", "Ha", False), ("B", "Yo'q", True)],
        },
        {
            "code": f"L15_Q{start + 2:03d}",
            "question": "Output yaratilgandan keyin ham QA qilish kerakmi?",
            "explanation": "Eksport natijasi alohida tekshiriladi.",
            "options": [("A", "Ha", True), ("B", "Yo'q", False)],
        },
    ]


def seed_level15_module02():
    connection = get_connection()
    try:
        cursor = connection.cursor()

        for row in LEVEL15_MODULE02_LESSONS:
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
