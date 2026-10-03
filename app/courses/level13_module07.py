from database.database import get_connection


LEVEL13_MODULE07_LESSONS = [
    ("L13_M07", "L13_M07_001", "Arxitektura qarorini asoslash", "theory", "Loyiha qarorini shaxsiy did emas, dalil va mantiq bilan tushuntirish.", 1, 40, 20),
    ("L13_M07", "L13_M07_002", "Brief va site bilan dalillash", "theory", "Qarorlarni mijoz talabi va uchastka tahliliga bog'lash.", 2, 45, 20),
    ("L13_M07", "L13_M07_003", "Trade-offni tushuntirish", "practice", "Har qarorning foyda va cheklovlarini ochiq ko'rsatish.", 3, 50, 20),
    ("L13_M07", "L13_M07_004", "Kelishmovchilikni boshqarish", "practice", "Mijoz bilan qarama-qarshi fikrlarni professional muhokama qilish.", 4, 50, 20),
    ("L13_M07", "L13_M07_005", "Qarorni himoya qilish audit", "practice", "Arxitektura qarorini dalil, alternativ va ta'sir bilan tushuntirish.", 5, 55, 25),
]


LEVEL13_MODULE07_CONTENT = {
    "L13_M07_001": [
        {"title": "“Menga yoqadi” yetmaydi", "type": "highlight", "text": "Professional qaror funksional, site, texnik yoki kompozitsion sabab bilan izohlanadi."},
        {"title": "Dalil", "type": "normal", "text": "Brief, circulation, privacy, daylight, site, structure yoki boshqa loyiha omili dalil bo'lishi mumkin."},
        {"title": "Avtoritet bilan bosmang", "type": "warning", "text": "“Men arxitektorman, shuning uchun shunday” degan yondashuv mijozga qaror mantig'ini tushuntirmaydi."},
        {"title": "Mini-amaliyot", "type": "example", "text": "3 ta loyiha qarorini sabab bilan asoslab yozing."},
    ],
    "L13_M07_002": [
        {"title": "Briefga qayting", "type": "highlight", "text": "Mijoz bilan kelishmovchilikda boshlang'ich maqsad va prioritylarga qaytish foydali."},
        {"title": "Site evidence", "type": "normal", "text": "Orientatsiya, kirish, qo'shni yoki relyef kabi obyektiv omillar qarorni asoslaydi."},
        {"title": "Briefni o'zgartirish mumkin", "type": "warning", "text": "Mijoz priorityni o'zgartirsa qaror ham o'zgarishi mumkin. Eski briefni mutlaq qoida deb ushlamang."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Bir qarorni brief + site dalili bilan tushuntiring."},
    ],
    "L13_M07_003": [
        {"title": "Trade-off", "type": "highlight", "text": "Ko'p loyiha qarorida bir afzallik boshqa cheklov bilan keladi."},
        {"title": "Misol", "type": "normal", "text": "Katta glazing ko'rinishni kuchaytirishi mumkin, lekin boshqa iqlim, privacy yoki konstruktiv masalalarni ham ko'rishni talab qiladi."},
        {"title": "Faqat plusni aytmang", "type": "warning", "text": "Mijoz qaror qilishi uchun muhim minus va risklarni ham tushuntiring."},
        {"title": "Mini-amaliyot", "type": "example", "text": "3 qaror uchun Benefit / Trade-off jadvali yarating."},
    ],
    "L13_M07_004": [
        {"title": "Kelishmovchilik", "type": "highlight", "text": "Mijoz bilan fikr farqi loyiha jarayonining normal qismi bo'lishi mumkin."},
        {"title": "Alternativ", "type": "normal", "text": "Muammo → sabab → alternativ → ta'sir formatida suhbatni davom ettiring."},
        {"title": "Shaxsiy bahsga aylantirmang", "type": "warning", "text": "Mijozning didini yoki fikrini kamsitmang."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Qiyin mijoz e'tiroziga 3 bosqichli professional javob yozing."},
    ],
    "L13_M07_005": [
        {"title": "Decision defense audit", "type": "highlight", "text": "Decision → reason → brief/site evidence → trade-off → alternative → impact → client decision."},
        {"title": "Professional checklist", "type": "example", "text": "1. Qaror sababi aniqmi?<br><br>2. Brief bilan bog'langanmi?<br><br>3. Site dalili bormi?<br><br>4. Trade-off aytildimi?<br><br>5. Alternativ ko'rildimi?<br><br>6. Texnik risk yashirilmaganmi?<br><br>7. Client qarori qayd qilindimi?"},
        {"title": "Keyingi modul", "type": "highlight", "text": "Keyingi modul: REAL LOYIHA SIMULYATORI."},
    ],
}


LEVEL13_MODULE07_QUIZ = {}

for i, lesson_code in enumerate(
    ["L13_M07_001", "L13_M07_002", "L13_M07_003", "L13_M07_004", "L13_M07_005"]
):
    start = 91 + i * 3

    LEVEL13_MODULE07_QUIZ[lesson_code] = [
        {
            "code": f"L13_Q{start:03d}",
            "question": "Arxitektura qarorini dalil va mantiq bilan tushuntirish kerakmi?",
            "explanation": "Professional qaror shaxsiy diddan kengroq asosga ega.",
            "options": [("A", "Ha", True), ("B", "Yo'q", False)],
        },
        {
            "code": f"L13_Q{start + 1:03d}",
            "question": "Trade-off va risklarni mijozdan yashirish to'g'rimi?",
            "explanation": "Mijoz qaror uchun muhim oqibatlarni tushunishi kerak.",
            "options": [("A", "Ha", False), ("B", "Yo'q", True)],
        },
        {
            "code": f"L13_Q{start + 2:03d}",
            "question": "Kelishmovchilikda alternativ va uning ta'sirini tushuntirish foydalimi?",
            "explanation": "Suhbatni konstruktiv qiladi.",
            "options": [("A", "Ha", True), ("B", "Yo'q", False)],
        },
    ]


def seed_level13_module07():
    connection = get_connection()
    try:
        cursor = connection.cursor()

        for row in LEVEL13_MODULE07_LESSONS:
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
