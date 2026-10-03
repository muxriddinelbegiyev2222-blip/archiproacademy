from database.database import get_connection


LEVEL13_MODULE01_LESSONS = [
    ("L13_M01", "L13_M01_001", "Birinchi suhbatning maqsadi", "theory", "Mijozning loyiha ehtiyoji va muammosini to'g'ri tushunish.", 1, 40, 20),
    ("L13_M01", "L13_M01_002", "To'g'ri savol berish", "theory", "Mijozdan kerakli loyiha ma'lumotlarini tizimli olish.", 2, 45, 20),
    ("L13_M01", "L13_M01_003", "Tinglash va qayd qilish", "practice", "Mijoz fikrini yo'qotmasdan strukturali qaydga aylantirish.", 3, 50, 20),
    ("L13_M01", "L13_M01_004", "Istak va real ehtiyoj", "practice", "Mijoz aytgan yechim ortidagi real maqsadni aniqlash.", 4, 50, 20),
    ("L13_M01", "L13_M01_005", "Birinchi suhbat professional audit", "practice", "Birinchi uchrashuvni yakuniy briefga tayyor holatga keltirish.", 5, 55, 25),
]


LEVEL13_MODULE01_CONTENT = {
    "L13_M01_001": [
        {"title": "Darhol chizma boshlamang", "type": "highlight", "text": "Birinchi suhbatning maqsadi mijoz nimani xohlayotganini emas, nima uchun xohlayotganini ham tushunish."},
        {"title": "Natija", "type": "normal", "text": "Uchrashuvdan keyin loyiha turi, oila, uchastka, asosiy funksiyalar va ustuvorliklar haqida aniqroq tasavvur bo'lishi kerak."},
        {"title": "Xato", "type": "warning", "text": "Mijoz bir rasm ko'rsatgani uchun aynan o'sha uyni nusxalashga o'tmang."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Birinchi uchrashuvning 10 ta maqsadini yozing."},
    ],
    "L13_M01_002": [
        {"title": "Savol tizimi", "type": "highlight", "text": "Savollar oila, hayot tarzi, uchastka, funksiyalar, uslub, budjet va vaqt bo'yicha guruhlanishi mumkin."},
        {"title": "Ochiq savol", "type": "normal", "text": "“Uyda mehmonlarni qanday qabul qilasiz?” kabi savol real ssenariyni ochishi mumkin."},
        {"title": "Faqat ha/yo'q", "type": "warning", "text": "Faqat yopiq savollar bilan mijoz ehtiyojini chuqur tushunish qiyin."},
        {"title": "Mini-amaliyot", "type": "example", "text": "20 ta professional mijoz savolini tayyorlang."},
    ],
    "L13_M01_003": [
        {"title": "Tinglash", "type": "highlight", "text": "Mijoz gapirayotgan paytda darhol yechim taklif qilishdan oldin ma'lumotni to'liq tushunish foydali."},
        {"title": "Qayd", "type": "normal", "text": "Talab, sabab, ustuvorlik va ochiq savol alohida yozilishi mumkin."},
        {"title": "Xotiraga suyanmang", "type": "warning", "text": "Uchrashuvdagi muhim talablarni faqat eslab qolishga suyanmang."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Meeting notes uchun sodda template yarating."},
    ],
    "L13_M01_004": [
        {"title": "Istak ortidagi ehtiyoj", "type": "highlight", "text": "Mijoz “katta mehmonxona” deydi. Real ehtiyoj esa 20 kishilik mehmon kutish bo'lishi mumkin."},
        {"title": "Why?", "type": "normal", "text": "Talabning sababini bilish boshqa, kuchliroq arxitektura yechimini topishga yordam beradi."},
        {"title": "Bahslashish emas", "type": "warning", "text": "Mijoz istagini rad etishdan oldin uning maqsadini tushuning."},
        {"title": "Mini-amaliyot", "type": "example", "text": "5 ta mijoz istagini yozing va har biri ortidagi ehtimoliy real ehtiyojni aniqlang."},
    ],
    "L13_M01_005": [
        {"title": "Suhbat audit", "type": "highlight", "text": "Maqsad → savollar → tinglash → qayd → aniqlashtirish → ustuvorlik → keyingi qadam."},
        {"title": "Professional checklist", "type": "example", "text": "1. Oila tarkibi aniqmi?<br><br>2. Uchastka haqida ma'lumot bormi?<br><br>3. Funksiyalar ma'lummi?<br><br>4. Hayot ssenariysi tushunarlimi?<br><br>5. Uslub istagi qayd qilindimi?<br><br>6. Budjet savoli berildimi?<br><br>7. Ochiq savollar yozildimi?<br><br>8. Keyingi qadam kelishildimi?"},
        {"title": "Keyingi modul", "type": "highlight", "text": "Keyingi modul: PROFESSIONAL BRIEF."},
    ],
}


LEVEL13_MODULE01_QUIZ = {}

for i, lesson_code in enumerate(
    ["L13_M01_001", "L13_M01_002", "L13_M01_003", "L13_M01_004", "L13_M01_005"]
):
    start = 1 + i * 3

    LEVEL13_MODULE01_QUIZ[lesson_code] = [
        {
            "code": f"L13_Q{start:03d}",
            "question": "Birinchi suhbatda mijoz ehtiyojining sababini ham tushunish foydalimi?",
            "explanation": "Real ehtiyojni tushunish kuchliroq loyiha qaroriga yordam beradi.",
            "options": [("A", "Ha", True), ("B", "Yo'q", False)],
        },
        {
            "code": f"L13_Q{start + 1:03d}",
            "question": "Uchrashuv ma'lumotlarini faqat xotirada saqlash professional usulmi?",
            "explanation": "Muhim talablar strukturali qayd qilinishi kerak.",
            "options": [("A", "Ha", False), ("B", "Yo'q", True)],
        },
        {
            "code": f"L13_Q{start + 2:03d}",
            "question": "Ochiq savollar mijozning real hayot ssenariysini tushunishga yordam beradimi?",
            "explanation": "Batafsil javob olish imkonini beradi.",
            "options": [("A", "Ha", True), ("B", "Yo'q", False)],
        },
    ]


def seed_level13_module01():
    connection = get_connection()
    try:
        cursor = connection.cursor()

        for row in LEVEL13_MODULE01_LESSONS:
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
                    module["id"],
                    lesson_code,
                    title,
                    lesson_type,
                    summary,
                    sort_order,
                    estimated_minutes,
                    xp_reward,
                    80,
                    1,
                ),
            )

        connection.commit()
    finally:
        connection.close()
