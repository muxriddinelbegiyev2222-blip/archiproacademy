from database.database import get_connection


LEVEL15_MODULE05_LESSONS = [
    ("L15_M05", "L15_M05_001", "Final loyiha: konsepsiya", "project", "Final brief va site asosida mustaqil arxitektura konsepsiyasini ishlab chiqish.", 1, 220, 30),
    ("L15_M05", "L15_M05_002", "Final loyiha: plan va site", "project", "Plan, circulation, ergonomika va genplanni professional darajaga olib chiqish.", 2, 230, 30),
    ("L15_M05", "L15_M05_003", "Final loyiha: BIM va texnik koordinatsiya", "project", "Model, konstruktsiya, MEP va vertikal tizimlarni koordinatsiya qilish.", 3, 240, 30),
    ("L15_M05", "L15_M05_004", "Final loyiha: fasad va hujjatlar", "project", "Fasad, tom, kesim, schedules va layoutlarni yakunlash.", 4, 250, 30),
    ("L15_M05", "L15_M05_005", "Final loyiha: professional audit", "project", "Loyihani barcha mezonlar bo'yicha to'liq audit va finalizatsiya qilish.", 5, 260, 40),
]


LEVEL15_MODULE05_CONTENT = {
    "L15_M05_001": [
        {"title": "Final project boshlanishi", "type": "highlight", "text": "Brief → Site Analysis → Problems → Opportunities → Concept → Alternatives → Direction."},
        {"title": "Talab", "type": "normal", "text": "Kamida bir nechta konseptual yo'nalish ishlab chiqilib, final yo'nalish sabab bilan tanlanadi."},
        {"title": "Xato", "type": "warning", "text": "Birinchi sketchni avtomatik final concept deb qabul qilmang."},
        {"title": "Project task", "type": "example", "text": "Site diagrams + bubble diagrams + massing variants + concept statement tayyorlang."},
    ],
    "L15_M05_002": [
        {"title": "Plan mastery", "type": "highlight", "text": "Final plan brief, ergonomika, circulation, privacy, daylight va site bilan bir vaqtda ishlashi kerak."},
        {"title": "Genplan", "type": "normal", "text": "Uy va uchastka yagona loyiha sifatida yechiladi."},
        {"title": "Project task", "type": "example", "text": "Furniture bilan final plans + circulation diagrams + final genplan tayyorlang."},
    ],
    "L15_M05_003": [
        {"title": "BIM mastery", "type": "highlight", "text": "Final loyiha toza BIM model va professional koordinatsiya talab qiladi."},
        {"title": "Structure + MEP", "type": "normal", "text": "Tayanch, stairs, openings, shafts, wet zones va boshqa kritik elementlar tegishli mutaxassislik mantiqi bilan koordinatsiya qilinadi."},
        {"title": "Project task", "type": "example", "text": "Full BIM model + coordination views + issue checklist tayyorlang."},
    ],
    "L15_M05_004": [
        {"title": "Architecture package", "type": "highlight", "text": "Fasad, roof, sections va material strategiyasi konsepsiyani davom ettiradi."},
        {"title": "Documentation", "type": "normal", "text": "Views, schedules, layouts va publisher package final holatga keltiriladi."},
        {"title": "Project task", "type": "example", "text": "Final elevations + sections + schedules + layout album tayyorlang."},
    ],
    "L15_M05_005": [
        {"title": "Final Project audit", "type": "highlight", "text": "Brief → Site → Plan → Structure → MEP → BIM → Facade → Roof → Sections → Genplan → Data → Layout → Output → QA."},
        {"title": "Professional checklist", "type": "example", "text": "1. Brief bajarilganmi?<br><br>2. Site bilan mosmi?<br><br>3. Plan ishlaydimi?<br><br>4. Ergonomika to'g'rimi?<br><br>5. Structure/MEP koordinatsiya qilinganmi?<br><br>6. BIM model tozami?<br><br>7. Facades kuchlimi?<br><br>8. Roof ishlaydimi?<br><br>9. Sections mosmi?<br><br>10. Genplan ishlaydimi?<br><br>11. Schedules to'g'rimi?<br><br>12. Layoutlar professionalmi?<br><br>13. Final output QA qilinganmi?"},
        {"title": "Keyingi modul", "type": "highlight", "text": "Keyingi modul: LOYIHANI HIMOYA QILISH."},
    ],
}


LEVEL15_MODULE05_QUIZ = {}

for i, lesson_code in enumerate(
    ["L15_M05_001", "L15_M05_002", "L15_M05_003", "L15_M05_004", "L15_M05_005"]
):
    start = 61 + i * 3

    LEVEL15_MODULE05_QUIZ[lesson_code] = [
        {
            "code": f"L15_Q{start:03d}",
            "question": "Final loyiha brief va site analysis asosida rivojlanishi kerakmi?",
            "explanation": "Final qarorlar boshlang'ich talab va real site bilan bog'liq bo'lishi kerak.",
            "options": [("A", "Ha", True), ("B", "Yo'q", False)],
        },
        {
            "code": f"L15_Q{start + 1:03d}",
            "question": "Final loyiha faqat chiroyli render bilan tugaydimi?",
            "explanation": "Plan, BIM, texnik koordinatsiya va hujjatlar ham talab qilinadi.",
            "options": [("A", "Ha", False), ("B", "Yo'q", True)],
        },
        {
            "code": f"L15_Q{start + 2:03d}",
            "question": "Final project barcha asosiy chizma va outputlar bo'yicha QA qilinadimi?",
            "explanation": "Topshirishdan oldin kompleks audit zarur.",
            "options": [("A", "Ha", True), ("B", "Yo'q", False)],
        },
    ]


def seed_level15_module05():
    connection = get_connection()
    try:
        cursor = connection.cursor()

        for row in LEVEL15_MODULE05_LESSONS:
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
