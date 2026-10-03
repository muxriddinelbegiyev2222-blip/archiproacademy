from database.database import get_connection


LEVEL15_MODULE08_LESSONS = [
    ("L15_M08", "L15_M08_001", "PRO readiness self-audit", "practice", "Barcha asosiy ko'nikmalarni yakuniy self-audit qilish.", 1, 50, 30),
    ("L15_M08", "L15_M08_002", "Weak skill audit", "practice", "Zaif qolgan ko'nikmalarni aniqlash va qayta mustahkamlash.", 2, 55, 30),
    ("L15_M08", "L15_M08_003", "Integrated case challenge", "practice", "Arxitektura, BIM va professional workflow'ni bitta case'da birlashtirish.", 3, 60, 30),
    ("L15_M08", "L15_M08_004", "Final submission readiness", "practice", "Loyiha, himoya va portfolio materiallarini final tekshirish.", 4, 65, 30),
    ("L15_M08", "L15_M08_005", "ARCHIPRO UZ yakuniy audit", "practice", "Butun o'quv dasturini mastery tamoyili asosida yakunlash.", 5, 70, 40),
]


LEVEL15_MODULE08_CONTENT = {
    "L15_M08_001": [
        {"title": "PRO — yakun emas, standart", "type": "highlight", "text": "Bu bosqich siz har bir loyihada mustaqil fikrlash, tekshirish va o'rganishni davom ettirishingiz uchun professional workflow beradi."},
        {"title": "Self-audit", "type": "normal", "text": "Architecture / Planning / Site / Construction / Archicad / BIM / Documentation / Client / Presentation."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Har skill bo'yicha Strong / Medium / Weak self-assessment qiling."},
    ],
    "L15_M08_002": [
        {"title": "Weaknessni yashirmang", "type": "highlight", "text": "Zaif skill aniqlansa tegishli oldingi modulga qaytib refresh qilish professional rivojlanishning bir qismi."},
        {"title": "Mastery", "type": "normal", "text": "Faqat kursni tugatish emas, asosiy ko'nikmani amalda bajara olish muhim."},
        {"title": "Mini-amaliyot", "type": "example", "text": "3 zaif skill uchun 30 kunlik improvement plan yozing."},
    ],
    "L15_M08_003": [
        {"title": "Integrated challenge", "type": "highlight", "text": "Bir case ichida site, brief, planning, structure, BIM va client decisionlarni boshqaring."},
        {"title": "No isolated skill", "type": "normal", "text": "Real ishda alohida darslar emas, integratsiyalangan qarorlar kerak bo'ladi."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Bitta murakkab residential case'ni boshidan yakuniy decisiongacha yeching."},
    ],
    "L15_M08_004": [
        {"title": "Submission readiness", "type": "highlight", "text": "Final project, defense va portfolio bitta professional profilni ko'rsatishi kerak."},
        {"title": "QA", "type": "normal", "text": "Missing file, wrong revision, unreadable drawing yoki inconsistent visual qolmasligi kerak."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Final submission uchun master checklist tuzing."},
    ],
    "L15_M08_005": [
        {"title": "ARCHIPRO UZ mastery chain", "type": "highlight", "text": "Learn → Practice → Test → Project → Audit → Find Weakness → Improve → Repeat."},
        {"title": "Yakuniy tamoyil", "type": "normal", "text": "Professional arxitektura — faqat dastur tugmalarini bilish emas. Muammoni tushunish, qaror qilish, tekshirish, koordinatsiya va aniq tushuntirishdir."},
        {"title": "Final", "type": "highlight", "text": "Endi yakuniy LEVEL 15 imtihoniga o'tish mumkin."},
    ],
}


LEVEL15_MODULE08_QUIZ = {}

for i, lesson_code in enumerate(
    ["L15_M08_001", "L15_M08_002", "L15_M08_003", "L15_M08_004", "L15_M08_005"]
):
    start = 106 + i * 3

    LEVEL15_MODULE08_QUIZ[lesson_code] = [
        {
            "code": f"L15_Q{start:03d}",
            "question": "Professional rivojlanishda weak skilllarni aniqlash foydalimi?",
            "explanation": "Zaif ko'nikmalarni maqsadli mustahkamlash mumkin.",
            "options": [("A", "Ha", True), ("B", "Yo'q", False)],
        },
        {
            "code": f"L15_Q{start + 1:03d}",
            "question": "Kursni tugatishning o'zi barcha skilllar mastery bo'lganini avtomatik anglatadimi?",
            "explanation": "Amaliy ko'nikma alohida tekshirilishi kerak.",
            "options": [("A", "Ha", False), ("B", "Yo'q", True)],
        },
        {
            "code": f"L15_Q{start + 2:03d}",
            "question": "Real professional workflow bir nechta ko'nikmani integratsiya qiladimi?",
            "explanation": "Site, planning, BIM va boshqa skilllar birgalikda ishlaydi.",
            "options": [("A", "Ha", True), ("B", "Yo'q", False)],
        },
    ]


def seed_level15_module08():
    connection = get_connection()
    try:
        cursor = connection.cursor()

        for row in LEVEL15_MODULE08_LESSONS:
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
