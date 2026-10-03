from database.database import get_connection


LEVEL13_MODULE06_LESSONS = [
    ("L13_M06", "L13_M06_001", "Tuzatishlarni qabul qilish", "theory", "Mijoz feedbackini professional tarzda yig'ish va tushunish.", 1, 50, 20),
    ("L13_M06", "L13_M06_002", "Feedbackni klassifikatsiya qilish", "theory", "Tuzatishlarni funksiya, estetika, budjet va texnik toifalarga ajratish.", 2, 55, 20),
    ("L13_M06", "L13_M06_003", "Revision boshqaruvi", "practice", "O'zgarishlarni nazorat qilinadigan versiya jarayonida yuritish.", 3, 60, 20),
    ("L13_M06", "L13_M06_004", "O'zgarish ta'siri", "practice", "Bitta tuzatishning boshqa loyiha qismlariga ta'sirini aniqlash.", 4, 65, 20),
    ("L13_M06", "L13_M06_005", "Mijoz tuzatishlari audit", "practice", "Feedbackdan tasdiqlangan revisiongacha bo'lgan jarayonni tekshirish.", 5, 70, 25),
]


LEVEL13_MODULE06_CONTENT = {
    "L13_M06_001": [
        {"title": "Feedbackni himoyasiz tinglang", "type": "highlight", "text": "Mijoz tuzatish so'rashi loyiha yomon degani emas. Avval nima o'zgartirmoqchi ekanini aniq tushuning."},
        {"title": "Aniqlashtirish", "type": "normal", "text": "“Oshxonani kattalashtiring” talabining sababini so'rash keyingi yechimni yaxshilaydi."},
        {"title": "Darhol o'zgartirmang", "type": "warning", "text": "Noaniq feedbackni tushunmasdan modelga kiritish yangi muammo yaratishi mumkin."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Feedback clarification uchun 8 ta savol yozing."},
    ],
    "L13_M06_002": [
        {"title": "Feedback turlari", "type": "highlight", "text": "Function / aesthetic / budget / technical / preference / new requirement."},
        {"title": "Priority", "type": "normal", "text": "Har feedback bir xil shoshilinch yoki muhim bo'lmasligi mumkin."},
        {"title": "Bir jumlada aralashtirmang", "type": "warning", "text": "Ko'p tuzatishni bitta noaniq taskga aylantirish nazoratni qiyinlashtiradi."},
        {"title": "Mini-amaliyot", "type": "example", "text": "10 ta feedbackni kategoriya va priority bo'yicha ajrating."},
    ],
    "L13_M06_003": [
        {"title": "Revision control", "type": "highlight", "text": "O'zgarish qachon, nima sababdan va qaysi versiyada kiritilgani qayd qilinadi."},
        {"title": "Status", "type": "normal", "text": "Requested / reviewed / approved / implemented / checked kabi statuslar ishlatilishi mumkin."},
        {"title": "Eski fayl", "type": "warning", "text": "Mijozga eski revision yuborish katta chalkashlik keltirishi mumkin."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Revision log uchun ustunlar ro'yxatini tuzing."},
    ],
    "L13_M06_004": [
        {"title": "Domino effect", "type": "highlight", "text": "Bitta devorni ko'chirish mebel, fasad, roof, structure, MEP va area'ga ta'sir qilishi mumkin."},
        {"title": "Impact check", "type": "normal", "text": "Har katta revisiondan oldin qaysi chizma va tizim o'zgarishini tekshiring."},
        {"title": "Faqat planni tuzatish", "type": "warning", "text": "Plan o'zgargach fasad, kesim va schedule eski qolib ketmasligi kerak."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Bitta devor ko'chirilganda tekshiriladigan 8 ta loyiha qismni yozing."},
    ],
    "L13_M06_005": [
        {"title": "Revision audit", "type": "highlight", "text": "Feedback → clarify → classify → impact → approve → implement → cross-check → issue."},
        {"title": "Professional checklist", "type": "example", "text": "1. Feedback aniqmi?<br><br>2. Category ma'lummi?<br><br>3. Priority aniqmi?<br><br>4. Impact tekshirildimi?<br><br>5. Client approval bormi?<br><br>6. Revision qayd qilindimi?<br><br>7. Barcha views yangilandimi?<br><br>8. Final QA qilindimi?"},
        {"title": "Keyingi modul", "type": "highlight", "text": "Keyingi modul: QARORNI HIMOYA QILISH."},
    ],
}


LEVEL13_MODULE06_QUIZ = {}

for i, lesson_code in enumerate(
    ["L13_M06_001", "L13_M06_002", "L13_M06_003", "L13_M06_004", "L13_M06_005"]
):
    start = 76 + i * 3

    LEVEL13_MODULE06_QUIZ[lesson_code] = [
        {
            "code": f"L13_Q{start:03d}",
            "question": "Noaniq feedbackni avval aniqlashtirish kerakmi?",
            "explanation": "Noto'g'ri tushunilgan tuzatish yangi muammo keltirishi mumkin.",
            "options": [("A", "Ha", True), ("B", "Yo'q", False)],
        },
        {
            "code": f"L13_Q{start + 1:03d}",
            "question": "Revisionlarni status va versiya bilan boshqarish foydalimi?",
            "explanation": "O'zgarishlar nazorati kuchayadi.",
            "options": [("A", "Ha", True), ("B", "Yo'q", False)],
        },
        {
            "code": f"L13_Q{start + 2:03d}",
            "question": "Plan o'zgarsa boshqa views va hujjatlarni tekshirmaslik to'g'rimi?",
            "explanation": "O'zgarish boshqa chizmalarga ham ta'sir qilishi mumkin.",
            "options": [("A", "Ha", False), ("B", "Yo'q", True)],
        },
    ]


def seed_level13_module06():
    connection = get_connection()
    try:
        cursor = connection.cursor()

        for row in LEVEL13_MODULE06_LESSONS:
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
