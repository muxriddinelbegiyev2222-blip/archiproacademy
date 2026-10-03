from database.database import get_connection


LEVEL11_MODULE08_LESSONS = [
    ("L11_M08", "L11_M08_001", "Ikki qavatli BIM struktura", "theory", "Stories, grid va model strukturasini professional tashkil qilish.", 1, 100, 20),
    ("L11_M08", "L11_M08_002", "Qavatlar modeli", "practice", "1- va 2-qavat elementlarini izchil modellashtirish.", 2, 110, 20),
    ("L11_M08", "L11_M08_003", "Stair, void va vertical systems", "practice", "Qavatlararo murakkab elementlarni BIMda koordinatsiya qilish.", 3, 120, 20),
    ("L11_M08", "L11_M08_004", "Roof, facade va sections", "practice", "Modeldan asosiy loyiha ko'rinishlarini koordinatsiya qilish.", 4, 125, 20),
    ("L11_M08", "L11_M08_005", "To'liq BIM model audit", "practice", "Ikki qavatli uy modelini to'liq professional audit qilish.", 5, 145, 25),
]


LEVEL11_MODULE08_CONTENT = {
    "L11_M08_001": [
        {"title": "Stories birinchi", "type": "highlight", "text": "Ikki qavatli modelda qavat sathlari va umumiy grid boshidan to'g'ri quriladi."},
        {"title": "Common reference", "type": "normal", "text": "Plan, structure, sections va fasadlar bir xil model geometriyasiga tayangan bo'lishi kerak."},
        {"title": "Xato", "type": "warning", "text": "Qavatlarni mustaqil 2D chizmalar sifatida yuritmang."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Stories/grid setup uchun audit checklist yarating."},
    ],
    "L11_M08_002": [
        {"title": "Qavat overlay", "type": "highlight", "text": "Yuqori va pastki qavat geometriyasi doimiy ravishda solishtiriladi."},
        {"title": "Elements", "type": "normal", "text": "Wall, slab, column, openings va boshqa elementlar BIM obyektlari sifatida boshqariladi."},
        {"title": "Dublikat", "type": "warning", "text": "Elementlarni qavatlar orasida ko'r-ko'rona copy qilish xatolar tug'dirishi mumkin."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Upper/lower floor consistency audit bajaring."},
    ],
    "L11_M08_003": [
        {"title": "Vertical core", "type": "highlight", "text": "Stair, void, shaft va penetratsiyalar qavatlar orasida 3D koordinatsiya qilinadi."},
        {"title": "Section test", "type": "normal", "text": "Vertikal elementlar section orqali tekshiriladi."},
        {"title": "Xato", "type": "warning", "text": "Plan yaxshi ko'rinib, sectionda elementlar to'qnashsa model hali tayyor emas."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Vertical core bo'yicha 10 ta model-check bajaring."},
    ],
    "L11_M08_004": [
        {"title": "Roof + facade + section", "type": "highlight", "text": "Bir modeldagi o'zgarish barcha bog'liq loyiha ko'rinishlarida nazorat qilinadi."},
        {"title": "Views", "type": "normal", "text": "Kerakli plan, facade va sectionlar bir xil loyiha holatini ko'rsatishi kerak."},
        {"title": "Eski view", "type": "warning", "text": "Eski yoki noto'g'ri view setting bilan chiqarilgan chizma modelga mos kelmasligi mumkin."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Bitta o'zgarishni plan/fasad/section bo'yicha tekshiring."},
    ],
    "L11_M08_005": [
        {"title": "Full BIM audit", "type": "highlight", "text": "Stories → grid → floors → structure → stair → void → shafts → roof → facade → sections → 3D → cleanup."},
        {"title": "Professional checklist", "type": "example", "text": "1. Stories to'g'rimi?<br><br>2. Qavatlar mosmi?<br><br>3. Tayanchlar mosmi?<br><br>4. Stair/void to'g'rimi?<br><br>5. Shafts mosmi?<br><br>6. Roof tozami?<br><br>7. Fasads/sections mosmi?<br><br>8. Dublikat yo'qmi?<br><br>9. Keraksiz elementlar tozalanganmi?"},
        {"title": "Keyingi modul", "type": "highlight", "text": "Keyingi modul: ISHCHI LOYIHA."},
    ],
}


LEVEL11_MODULE08_QUIZ = {}

for i, lesson_code in enumerate(
    ["L11_M08_001", "L11_M08_002", "L11_M08_003", "L11_M08_004", "L11_M08_005"]
):
    start = 106 + i * 3

    LEVEL11_MODULE08_QUIZ[lesson_code] = [
        {
            "code": f"L11_Q{start:03d}",
            "question": "Ikki qavatli BIM modelda stories va grid muhimmi?",
            "explanation": "Modelning umumiy koordinatsion bazasi.",
            "options": [("A", "Ha", True), ("B", "Yo'q", False)],
        },
        {
            "code": f"L11_Q{start + 1:03d}",
            "question": "Plan yaxshi ko'rinsa section va 3D tekshiruvlari kerak emasmi?",
            "explanation": "Vertikal konfliktlar boshqa ko'rinishlarda aniqlanadi.",
            "options": [("A", "Ha", False), ("B", "Yo'q", True)],
        },
        {
            "code": f"L11_Q{start + 2:03d}",
            "question": "Qavatlararo stair, void va shaftlar 3D koordinatsiya qilinadimi?",
            "explanation": "Ular bir necha qavatni bog'laydi.",
            "options": [("A", "Ha", True), ("B", "Yo'q", False)],
        },
    ]


def seed_level11_module08():
    connection = get_connection()
    try:
        cursor = connection.cursor()

        for row in LEVEL11_MODULE08_LESSONS:
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
