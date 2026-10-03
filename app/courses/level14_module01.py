from database.database import get_connection


LEVEL14_MODULE01_LESSONS = [
    ("L14_M01", "L14_M01_001", "Tor uchastkani tahlil qilish", "theory", "Tor uchastkaning imkoniyat va cheklovlarini aniqlash.", 1, 60, 20),
    ("L14_M01", "L14_M01_002", "Uzunlamasına zonalash", "theory", "Funksiyalarni tor geometriyada izchil joylashtirish.", 2, 70, 20),
    ("L14_M01", "L14_M01_003", "Yorug'lik va ichki hovli", "practice", "Tor uyda tabiiy yorug'lik va ochiq makon strategiyalarini ishlab chiqish.", 3, 70, 20),
    ("L14_M01", "L14_M01_004", "Circulation va privacy", "practice", "Uzun plan ichida harakat va privacy'ni boshqarish.", 4, 75, 20),
    ("L14_M01", "L14_M01_005", "Tor uchastka professional audit", "practice", "Tor uchastka loyihasini kompleks tekshirish.", 5, 85, 25),
]


LEVEL14_MODULE01_CONTENT = {
    "L14_M01_001": [
        {"title": "Tor uchastka — faqat muammo emas", "type": "highlight", "text": "Cheklangan eni loyiha strategiyasini aniqroq qilishga majbur qiladi."},
        {"title": "Tahlil", "type": "normal", "text": "Ko'cha, kirish, uzunlik, orientatsiya, qo'shnilar, privacy va tabiiy yorug'lik birga ko'riladi."},
        {"title": "Xato", "type": "warning", "text": "Oddiy keng uy planini tor uchastkaga shunchaki siqib qo'ymang."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Tor uchastka uchun 10 bandli Site Analysis yozing."},
    ],
    "L14_M01_002": [
        {"title": "Uzunlamasına mantiq", "type": "highlight", "text": "Xonalar ketma-ketligi va courtyardlar tor uyda muhim rol o'ynashi mumkin."},
        {"title": "Zonalar", "type": "normal", "text": "Kirish, public, private va service zonalari uzun o'q bo'yicha boshqariladi."},
        {"title": "Koridor xavfi", "type": "warning", "text": "Tor uy avtomatik ravishda uzun va foydasiz koridorga aylanmasligi kerak."},
        {"title": "Mini-amaliyot", "type": "example", "text": "3 xil linear zoning variant yarating."},
    ],
    "L14_M01_003": [
        {"title": "Yorug'lik strategiyasi", "type": "highlight", "text": "Tor va chuqur plan ichkarisiga tabiiy yorug'lik kiritish alohida loyiha masalasi."},
        {"title": "Courtyard", "type": "normal", "text": "Ichki ochiq makon, light well yoki boshqa fazoviy usul loyiha konsepsiyasiga qarab yordam berishi mumkin."},
        {"title": "Kopiya qilmang", "type": "warning", "text": "Courtyard hajmi va joyi real site, iqlim va normativ talablar asosida tekshiriladi."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Plan chuqurligi bo'yicha natural light diagram chizing."},
    ],
    "L14_M01_004": [
        {"title": "Circulation", "type": "highlight", "text": "Uzun harakat yo'li xonalar bilan integratsiya qilinsa maydon samaraliroq ishlashi mumkin."},
        {"title": "Privacy", "type": "normal", "text": "Ko'chadan private zona tomon bosqichma-bosqich o'tish tashkil qilinadi."},
        {"title": "Xato", "type": "warning", "text": "Mehmon circulation'ini barcha private xonalar oldidan o'tkazmang."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Guest va family circulation'ni alohida tekshiring."},
    ],
    "L14_M01_005": [
        {"title": "Tor uchastka audit", "type": "highlight", "text": "Site → linear zoning → light → courtyard → circulation → privacy → structure → facade."},
        {"title": "Professional checklist", "type": "example", "text": "1. Kirish aniqmi?<br><br>2. Dead corridor kamayganmi?<br><br>3. Ichki zonalar yorug'mi?<br><br>4. Privacy ishlaydimi?<br><br>5. Courtyard maqsadlimi?<br><br>6. Konstruktsiya mantiqiymi?<br><br>7. Fasad site bilan mosmi?"},
        {"title": "Keyingi modul", "type": "highlight", "text": "Keyingi modul: NOTO'G'RI SHAKLDAGI UCHASTKA."},
    ],
}


LEVEL14_MODULE01_QUIZ = {}

for i, lesson_code in enumerate(
    ["L14_M01_001", "L14_M01_002", "L14_M01_003", "L14_M01_004", "L14_M01_005"]
):
    start = 1 + i * 3

    LEVEL14_MODULE01_QUIZ[lesson_code] = [
        {
            "code": f"L14_Q{start:03d}",
            "question": "Tor uchastka alohida rejalashtirish strategiyasini talab qilishi mumkinmi?",
            "explanation": "Cheklangan eni funksional va fazoviy qarorlarga ta'sir qiladi.",
            "options": [("A", "Ha", True), ("B", "Yo'q", False)],
        },
        {
            "code": f"L14_Q{start + 1:03d}",
            "question": "Oddiy keng uy planini tor uchastkaga shunchaki siqish yaxshi usulmi?",
            "explanation": "Site sharoitiga mos yangi yechim kerak bo'lishi mumkin.",
            "options": [("A", "Ha", False), ("B", "Yo'q", True)],
        },
        {
            "code": f"L14_Q{start + 2:03d}",
            "question": "Tor va chuqur planda tabiiy yorug'lik alohida tekshiriladimi?",
            "explanation": "Ichki zonalarga yorug'lik yetib borishi muhim.",
            "options": [("A", "Ha", True), ("B", "Yo'q", False)],
        },
    ]


def seed_level14_module01():
    connection = get_connection()
    try:
        cursor = connection.cursor()

        for row in LEVEL14_MODULE01_LESSONS:
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
