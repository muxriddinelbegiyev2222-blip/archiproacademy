from database.database import get_connection


LEVEL12_MODULE10_LESSONS = [
    ("L12_M10", "L12_M10_001", "Final BIM deliverable strategiyasi", "theory", "Modeldan yakuniy loyiha paketigacha bo'lgan deliverable tizimini tashkil qilish.", 1, 80, 20),
    ("L12_M10", "L12_M10_002", "Views va schedules finalizatsiyasi", "practice", "Final loyiha views va jadvallarini audit qilish.", 2, 90, 20),
    ("L12_M10", "L12_M10_003", "Layout Book finalizatsiyasi", "practice", "Sahifalar, shtamp va drawinglarni yakuniy holatga keltirish.", 3, 95, 20),
    ("L12_M10", "L12_M10_004", "Publisher va exchange paketi", "practice", "PDF, DWG va IFC deliverable paketlarini nazorat qilish.", 4, 100, 20),
    ("L12_M10", "L12_M10_005", "LEVEL 12 final BIM audit", "practice", "Model, data, views, layouts va outputlarni kompleks tekshirish.", 5, 115, 25),
]


LEVEL12_MODULE10_CONTENT = {
    "L12_M10_001": [
        {"title": "Final deliverable", "type": "highlight", "text": "Professional BIM loyiha model bilan tugamaydi. Modeldan nazorat qilingan hujjat va exchange paketlari olinadi."},
        {"title": "Chain", "type": "normal", "text": "Model → Data → Views → Schedules → Layouts → Publisher → PDF/DWG/IFC → QA."},
        {"title": "Oxirgi kun chaos", "type": "warning", "text": "Topshirish kuni barcha layout va exportlarni boshidan yig'ishga qolib ketmang."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Final deliverable matrix tuzing: kimga / nima / format / versiya."},
    ],
    "L12_M10_002": [
        {"title": "View audit", "type": "highlight", "text": "Faqat final va nazorat qilingan views deliverable uchun ishlatiladi."},
        {"title": "Schedule audit", "type": "normal", "text": "Data completeness va quantitylar model bilan tekshiriladi."},
        {"title": "Old view", "type": "warning", "text": "Eski saved view yoki test schedule final paketga kirib qolmasligi kerak."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Final views va schedules uchun status jadvali yarating."},
    ],
    "L12_M10_003": [
        {"title": "Layout final", "type": "highlight", "text": "Sheet number, title, drawing, scale, annotation va revision holati tekshiriladi."},
        {"title": "Consistency", "type": "normal", "text": "Barcha sahifalar yagona grafik va title-block standartiga mos bo'lishi kerak."},
        {"title": "Missing drawing", "type": "warning", "text": "Empty frame, missing source yoki outdated drawing final QA'da aniqlanishi kerak."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Final album uchun 12 bandli layout QA checklist tuzing."},
    ],
    "L12_M10_004": [
        {"title": "Multi-format delivery", "type": "highlight", "text": "Bir loyiha turli maqsad uchun PDF, DWG yoki IFC kabi formatlarda topshirilishi mumkin."},
        {"title": "Har format alohida QA", "type": "normal", "text": "PDF to'g'ri bo'lishi DWG yoki IFC ham to'g'ri degani emas."},
        {"title": "Version control", "type": "warning", "text": "Turli formatlarda turli loyiha versiyasini yubormang."},
        {"title": "Mini-amaliyot", "type": "example", "text": "PDF/DWG/IFC uchun alohida final QA ustunlari yarating."},
    ],
    "L12_M10_005": [
        {"title": "LEVEL 12 final audit", "type": "highlight", "text": "BIM → Element Data → Schedules → Views → Layouts → Standards → Publisher → DWG → IFC → Final QA."},
        {"title": "Professional checklist", "type": "example", "text": "1. Model cleanmi?<br><br>2. Element data to'g'rimi?<br><br>3. Schedules auditdan o'tdimi?<br><br>4. Views latestmi?<br><br>5. Layoutlar to'g'rimi?<br><br>6. Shtamp va grafik standard izchilmi?<br><br>7. Publisher Set to'g'rimi?<br><br>8. PDF tekshirildimi?<br><br>9. DWG tekshirildimi?<br><br>10. IFC tekshirildimi?<br><br>11. Barcha format bir revisionmi?"},
        {"title": "LEVEL 12 yakuni", "type": "highlight", "text": "Siz endi BIM modelni ma'lumot, schedules, views, layouts va professional topshirish paketigacha olib borish workflow'ini bilasiz."},
    ],
}


LEVEL12_MODULE10_QUIZ = {}

for i, lesson_code in enumerate(
    ["L12_M10_001", "L12_M10_002", "L12_M10_003", "L12_M10_004", "L12_M10_005"]
):
    start = 136 + i * 3

    LEVEL12_MODULE10_QUIZ[lesson_code] = [
        {
            "code": f"L12_Q{start:03d}",
            "question": "Professional BIM deliverable faqat model faylidan iboratmi?",
            "explanation": "Hujjat, data va kerakli exchange paketlari ham bo'lishi mumkin.",
            "options": [("A", "Ha", False), ("B", "Yo'q", True)],
        },
        {
            "code": f"L12_Q{start + 1:03d}",
            "question": "Final layout va exportlar topshirishdan oldin QA qilinadimi?",
            "explanation": "Topshirish sifati nazorat qilinadi.",
            "options": [("A", "Ha", True), ("B", "Yo'q", False)],
        },
        {
            "code": f"L12_Q{start + 2:03d}",
            "question": "PDF, DWG va IFC bir xil loyiha revisioniga tegishli bo'lishi kerakmi?",
            "explanation": "Turli formatlarda versiya mismatch bo'lmasligi kerak.",
            "options": [("A", "Ha", True), ("B", "Yo'q", False)],
        },
    ]


def seed_level12_module10():
    connection = get_connection()
    try:
        cursor = connection.cursor()

        for row in LEVEL12_MODULE10_LESSONS:
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
