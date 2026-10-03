from database.database import get_connection


LEVEL15_MODULE07_LESSONS = [
    ("L15_M07", "L15_M07_001", "Portfolio strategiyasi", "theory", "Portfolio orqali professional kuchli tomonlarni ko'rsatish.", 1, 60, 25),
    ("L15_M07", "L15_M07_002", "Project selection", "practice", "Eng kuchli va turli ko'nikmalarni ko'rsatadigan loyihalarni tanlash.", 2, 70, 25),
    ("L15_M07", "L15_M07_003", "Project story", "practice", "Har loyiha uchun muammo, jarayon va natijani tushunarli ko'rsatish.", 3, 70, 25),
    ("L15_M07", "L15_M07_004", "Grafik va matn hierarxiyasi", "practice", "Portfolio sahifalarini professional o'qiladigan tizimga aylantirish.", 4, 75, 25),
    ("L15_M07", "L15_M07_005", "Portfolio professional audit", "practice", "Final portfolio sifatini kompleks tekshirish.", 5, 85, 30),
]


LEVEL15_MODULE07_CONTENT = {
    "L15_M07_001": [
        {"title": "Portfolio — rasm albomi emas", "type": "highlight", "text": "Portfolio siz qanday fikrlashingiz, muammoni qanday yechishingiz va qanday natija yaratishingizni ko'rsatadi."},
        {"title": "Target", "type": "normal", "text": "Portfolio maqsadi ish, mijoz, ta'lim yoki boshqa professional vazifaga qarab farq qilishi mumkin."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Portfolio maqsadingizni bir jumlada yozing."},
    ],
    "L15_M07_002": [
        {"title": "Kam, lekin kuchli", "type": "highlight", "text": "Har bir qilgan loyihani qo'shish shart emas."},
        {"title": "Selection", "type": "normal", "text": "Turli skilllarni ko'rsatadigan eng kuchli loyihalar tanlanadi."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Loyihalarni Strong / Maybe / Remove guruhlariga ajrating."},
    ],
    "L15_M07_003": [
        {"title": "Project story", "type": "highlight", "text": "Context → Problem → Process → Decision → Result."},
        {"title": "Jarayonni ko'rsating", "type": "normal", "text": "Faqat final render emas, diagram, plan va asosiy reasoning ham qiymatli."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Bitta loyiha uchun 5 bosqichli story yozing."},
    ],
    "L15_M07_004": [
        {"title": "Hierarchy", "type": "highlight", "text": "Har sahifada bitta asosiy message bo'lishi portfolio o'qilishini yaxshilaydi."},
        {"title": "Text", "type": "normal", "text": "Matn qisqa, konkret va vizual materialni tushuntiruvchi bo'lishi kerak."},
        {"title": "Xato", "type": "warning", "text": "Har sahifani maksimal rasm va matn bilan to'ldirmang."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Bir portfolio spreadini hierarchy bo'yicha qayta tuzing."},
    ],
    "L15_M07_005": [
        {"title": "Portfolio audit", "type": "highlight", "text": "Target → Selection → Story → Drawings → Visuals → Text → Hierarchy → Consistency → Final QA."},
        {"title": "Professional checklist", "type": "example", "text": "1. Maqsad aniqmi?<br><br>2. Kuchli loyihalar tanlanganmi?<br><br>3. Jarayon ko'rsatilganmi?<br><br>4. Plan/chizma o'qiladimi?<br><br>5. Final visual sifatlimi?<br><br>6. Matn qisqami?<br><br>7. Style izchilmi?<br><br>8. Keraksiz material olib tashlanganmi?"},
        {"title": "Keyingi modul", "type": "highlight", "text": "Keyingi modul: PRO FINAL."},
    ],
}


LEVEL15_MODULE07_QUIZ = {}

for i, lesson_code in enumerate(
    ["L15_M07_001", "L15_M07_002", "L15_M07_003", "L15_M07_004", "L15_M07_005"]
):
    start = 91 + i * 3

    LEVEL15_MODULE07_QUIZ[lesson_code] = [
        {
            "code": f"L15_Q{start:03d}",
            "question": "Portfolio faqat final renderlar to'plamimi?",
            "explanation": "U fikrlash, jarayon va natijani ko'rsatishi kerak.",
            "options": [("A", "Ha", False), ("B", "Yo'q", True)],
        },
        {
            "code": f"L15_Q{start + 1:03d}",
            "question": "Portfolio uchun eng kuchli loyihalarni tanlash foydalimi?",
            "explanation": "Sifat sonidan muhimroq bo'lishi mumkin.",
            "options": [("A", "Ha", True), ("B", "Yo'q", False)],
        },
        {
            "code": f"L15_Q{start + 2:03d}",
            "question": "Project story muammo, jarayon va natijani ko'rsatishi kerakmi?",
            "explanation": "Bu professional reasoningni ko'rsatadi.",
            "options": [("A", "Ha", True), ("B", "Yo'q", False)],
        },
    ]


def seed_level15_module07():
    connection = get_connection()
    try:
        cursor = connection.cursor()

        for row in LEVEL15_MODULE07_LESSONS:
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
