from database.database import get_connection


LEVEL13_MODULE08_LESSONS = [
    ("L13_M08", "L13_M08_001", "Simulyatsiya: birinchi murojaat", "practice", "Real mijozga o'xshash boshlang'ich suhbat va ma'lumot yig'ish.", 1, 100, 20),
    ("L13_M08", "L13_M08_002", "Simulyatsiya: brief va variantlar", "practice", "Mijoz ma'lumotidan professional brief va konsept variantlar yaratish.", 2, 110, 20),
    ("L13_M08", "L13_M08_003", "Simulyatsiya: prezentatsiya", "practice", "Variantlarni mijozga taqdim etish va feedback olish.", 3, 120, 20),
    ("L13_M08", "L13_M08_004", "Simulyatsiya: revision va konflikt", "practice", "Mijoz tuzatishlari, budjet va texnik konfliktlarni boshqarish.", 4, 125, 20),
    ("L13_M08", "L13_M08_005", "LEVEL 13 real loyiha audit", "practice", "Mijoz bilan ishlash jarayonini boshidan oxirigacha professional tekshirish.", 5, 145, 25),
]


LEVEL13_MODULE08_CONTENT = {
    "L13_M08_001": [
        {"title": "Real ssenariy", "type": "highlight", "text": "Sizga to'liq tayyor brief berilmaydi. Mijoz tarqoq talablar bilan murojaat qiladi va siz kerakli ma'lumotni o'zingiz yig'asiz."},
        {"title": "Vazifa", "type": "normal", "text": "Savollar bering, missing information toping, assumptions yozing va keyingi qadamni belgilang."},
        {"title": "Shoshilmang", "type": "warning", "text": "Birinchi xabardanoq plan chizishga o'tmang."},
        {"title": "Mini loyiha", "type": "example", "text": "20 savollik client interview + meeting note tayyorlang."},
    ],
    "L13_M08_002": [
        {"title": "Brief", "type": "highlight", "text": "Yig'ilgan ma'lumot professional briefga aylantiriladi."},
        {"title": "Variant", "type": "normal", "text": "Kamida bir nechta real strategik variant tayyorlanadi va mezonlar bilan solishtiriladi."},
        {"title": "Client needs first", "type": "warning", "text": "O'zingiz yoqtirgan uslubni briefdan ustun qo'ymang."},
        {"title": "Mini loyiha", "type": "example", "text": "Brief + A/B/C variant comparison tayyorlang."},
    ],
    "L13_M08_003": [
        {"title": "Prezentatsiya", "type": "highlight", "text": "Mijozga brief, site, konsepsiya, plan va variant trade-offlari sodda ketma-ketlikda tushuntiriladi."},
        {"title": "Feedback", "type": "normal", "text": "Feedback yozib olinadi va aniqlashtiriladi."},
        {"title": "Faqat chiroyli render", "type": "warning", "text": "Mijoz qarorini faqat emotsional vizualga tayantirmang."},
        {"title": "Mini loyiha", "type": "example", "text": "10 daqiqalik presentation script + feedback form tayyorlang."},
    ],
    "L13_M08_004": [
        {"title": "Real konflikt", "type": "highlight", "text": "Mijoz yangi xona, pastroq budjet va o'zgarmas uy maydonini bir vaqtda talab qilishi mumkin."},
        {"title": "Trade-off boshqaruvi", "type": "normal", "text": "Muammoni yashirmasdan alternativ va oqibatlarni ko'rsating."},
        {"title": "Nazoratsiz revision", "type": "warning", "text": "Har yangi feedbackni approval va impact check'siz modelga kiritmang."},
        {"title": "Mini loyiha", "type": "example", "text": "3 ta konflikt ssenariysi uchun professional response va revision plan yozing."},
    ],
    "L13_M08_005": [
        {"title": "LEVEL 13 final workflow", "type": "highlight", "text": "First contact → interview → brief → budget → variants → presentation → feedback → revision → decision defense → final record."},
        {"title": "Professional checklist", "type": "example", "text": "1. Client needs tushunildimi?<br><br>2. Brief tasdiqlanganmi?<br><br>3. Budget/scope gaplashildimi?<br><br>4. Variantlar real farqlimi?<br><br>5. Prezentatsiya tushunarlimi?<br><br>6. Feedback qayd qilindimi?<br><br>7. Revision nazorat qilindimi?<br><br>8. Qarorlar dalil bilan himoya qilindimi?<br><br>9. Final client decisions qayd qilindimi?"},
        {"title": "LEVEL 13 yakuni", "type": "highlight", "text": "Siz endi mijoz bilan birinchi suhbatdan tasdiqlangan revision va loyiha qaroriga qadar professional workflow'ni boshqarish mantig'ini bilasiz."},
    ],
}


LEVEL13_MODULE08_QUIZ = {}

for i, lesson_code in enumerate(
    ["L13_M08_001", "L13_M08_002", "L13_M08_003", "L13_M08_004", "L13_M08_005"]
):
    start = 106 + i * 3

    LEVEL13_MODULE08_QUIZ[lesson_code] = [
        {
            "code": f"L13_Q{start:03d}",
            "question": "Real loyiha workflow'i mijozdan ma'lumot yig'ishdan boshlanadimi?",
            "explanation": "Loyiha maqsadi avval tushuniladi.",
            "options": [("A", "Ha", True), ("B", "Yo'q", False)],
        },
        {
            "code": f"L13_Q{start + 1:03d}",
            "question": "Mijoz feedbackini impact check va approval'siz darhol modelga kiritish idealmi?",
            "explanation": "Revision nazorat qilinishi kerak.",
            "options": [("A", "Ha", False), ("B", "Yo'q", True)],
        },
        {
            "code": f"L13_Q{start + 2:03d}",
            "question": "Real loyiha jarayonida qarorlar, feedback va revisionlarni hujjatlashtirish foydalimi?",
            "explanation": "Loyiha tarixi va qarorlar aniq bo'ladi.",
            "options": [("A", "Ha", True), ("B", "Yo'q", False)],
        },
    ]


def seed_level13_module08():
    connection = get_connection()
    try:
        cursor = connection.cursor()

        for row in LEVEL13_MODULE08_LESSONS:
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
