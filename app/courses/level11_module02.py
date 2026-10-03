from database.database import get_connection


LEVEL11_MODULE02_LESSONS = [
    ("L11_M02", "L11_M02_001", "Qavatlar bo'yicha zonalash", "theory", "Funksiyalarni ikki qavat bo'yicha tizimli taqsimlash.", 1, 50, 20),
    ("L11_M02", "L11_M02_002", "Public va private vertikal aloqa", "theory", "Qavatlar orasida privacy va foydalanish mantiqini boshqarish.", 2, 55, 20),
    ("L11_M02", "L11_M02_003", "Wet zones va service stack", "practice", "Muhandislik zonalarini qavatlar bo'yicha koordinatsiya qilish.", 3, 60, 20),
    ("L11_M02", "L11_M02_004", "Konstruktiv stacking", "practice", "Devor va tayanchlarni qavatlar bo'yicha mantiqan moslashtirish.", 4, 65, 20),
    ("L11_M02", "L11_M02_005", "Qavatlar zonalashi audit", "practice", "Ikki qavat funksional strukturasini kompleks tekshirish.", 5, 70, 25),
]


LEVEL11_MODULE02_CONTENT = {
    "L11_M02_001": [
        {"title": "Horizontal + vertical zoning", "type": "highlight", "text": "2 qavatli uyda zonalash faqat bir qavat ichida emas, qavatlar orasida ham ishlaydi."},
        {"title": "Savol", "type": "normal", "text": "Qaysi funksiya pastda, qaysi funksiya yuqorida va nima sababdan?"},
        {"title": "Xato", "type": "warning", "text": "Xonalarni faqat sig'gan qavatga joylashtirmang."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Room programni 1-qavat va 2-qavatga sabab bilan taqsimlang."},
    ],
    "L11_M02_002": [
        {"title": "Privacy gradient", "type": "highlight", "text": "Kirishdan private zonagacha privacy asta-sekin kuchayishi mumkin."},
        {"title": "Mehmon", "type": "normal", "text": "Mehmon harakati oilaning private zonasini keraksiz kesib o'tmasligi kerak."},
        {"title": "Night circulation", "type": "normal", "text": "Yotoqxona, sanuzel va zinapoya orasidagi tungi harakat ham tekshiriladi."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Guest / family / night circulation diagramlarini alohida yarating."},
    ],
    "L11_M02_003": [
        {"title": "Wet stack", "type": "highlight", "text": "Sanuzel va boshqa wet zonalarni qavatlar bo'yicha mantiqiy yaqinlashtirish MEPni soddalashtirishi mumkin."},
        {"title": "Shaft", "type": "normal", "text": "Vertikal muhandislik yo'llari uchun joy boshidan rejalashtiriladi."},
        {"title": "Xato", "type": "warning", "text": "Upper floor wet roomni pastdagi muhim xona ustiga sabab va koordinatsiyasiz joylashtirmang."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Wet zones va shaftlar uchun vertical stack diagram chizing."},
    ],
    "L11_M02_004": [
        {"title": "Konstruktiv stacking", "type": "highlight", "text": "Yuqoridagi tayanch va devorlar pastdagi konstruktiv tizim bilan mantiqiy aloqada bo'lishi kerak."},
        {"title": "Grid", "type": "normal", "text": "Qavatlar uchun umumiy o'qlar koordinatsiyani osonlashtiradi."},
        {"title": "Transfer", "type": "warning", "text": "Yuqoridagi tayanch pastda davom etmasa konstruktor bilan maxsus yechim talab qilinishi mumkin."},
        {"title": "Mini-amaliyot", "type": "example", "text": "1- va 2-qavat planlarini ustma-ust solishtirib tayanchlarni tekshiring."},
    ],
    "L11_M02_005": [
        {"title": "Zoning audit", "type": "highlight", "text": "Room program → qavat roli → privacy → circulation → wet stack → structure → audit."},
        {"title": "Professional checklist", "type": "example", "text": "1. Har qavat roli aniqmi?<br><br>2. Privacy ishlaydimi?<br><br>3. Guest circulation to'g'rimi?<br><br>4. Night circulation to'g'rimi?<br><br>5. Wet zones stack qilinganmi?<br><br>6. Shaft joylari bormi?<br><br>7. Tayanchlar mosmi?"},
        {"title": "Keyingi modul", "type": "highlight", "text": "Keyingi modul: ZINAPOYA PRO."},
    ],
}


LEVEL11_MODULE02_QUIZ = {}

for i, lesson_code in enumerate(
    [
        "L11_M02_001",
        "L11_M02_002",
        "L11_M02_003",
        "L11_M02_004",
        "L11_M02_005",
    ]
):
    start = 16 + i * 3

    LEVEL11_MODULE02_QUIZ[lesson_code] = [
        {
            "code": f"L11_Q{start:03d}",
            "question": "Ikki qavatli uyda qavatlar orasidagi funksional aloqa tekshiriladimi?",
            "explanation": "Qavatlar yagona uy tizimi sifatida ishlaydi.",
            "options": [("A", "Ha", True), ("B", "Yo'q", False)],
        },
        {
            "code": f"L11_Q{start + 1:03d}",
            "question": "Qavatlar orasidagi MEP va konstruktiv koordinatsiyani e'tiborsiz qoldirish to'g'rimi?",
            "explanation": "Vertikal tizimlar qavatlar orasida bog'liq.",
            "options": [("A", "Ha", False), ("B", "Yo'q", True)],
        },
        {
            "code": f"L11_Q{start + 2:03d}",
            "question": "Qavatlar zonalashida privacy va circulation muhimmi?",
            "explanation": "Real foydalanish sifati shu aloqalarga bog'liq.",
            "options": [("A", "Ha", True), ("B", "Yo'q", False)],
        },
    ]


def seed_level11_module02():
    connection = get_connection()
    try:
        cursor = connection.cursor()

        for row in LEVEL11_MODULE02_LESSONS:
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
