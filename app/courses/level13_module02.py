from database.database import get_connection


LEVEL13_MODULE02_LESSONS = [
    ("L13_M02", "L13_M02_001", "Professional brief strukturasi", "theory", "Mijoz talablarini tartibli loyiha hujjatiga aylantirish.", 1, 50, 20),
    ("L13_M02", "L13_M02_002", "Room program va ustuvorlik", "theory", "Xonalar, funksiyalar va talablarni darajalash.", 2, 55, 20),
    ("L13_M02", "L13_M02_003", "Cheklovlar va assumptions", "practice", "Loyiha cheklovlari va hali tasdiqlanmagan taxminlarni qayd qilish.", 3, 60, 20),
    ("L13_M02", "L13_M02_004", "Briefni mijoz bilan tasdiqlash", "practice", "Yozilgan talablarni mijoz bilan qayta tekshirish.", 4, 65, 20),
    ("L13_M02", "L13_M02_005", "Professional brief audit", "practice", "Briefni loyiha boshlanishiga tayyor holatga keltirish.", 5, 70, 25),
]


LEVEL13_MODULE02_CONTENT = {
    "L13_M02_001": [
        {"title": "Suhbat → hujjat", "type": "highlight", "text": "Professional brief uchrashuvdagi tarqoq fikrlarni loyiha uchun ishlatiladigan tizimli ma'lumotga aylantiradi."},
        {"title": "Bo'limlar", "type": "normal", "text": "Client profile, site, room program, lifestyle, style, budget, priorities, constraints va open questions."},
        {"title": "Xato", "type": "warning", "text": "WhatsApp yozishmalarini o'z holicha technical brief deb qabul qilmang."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Professional brief uchun bo'limlar strukturasi tuzing."},
    ],
    "L13_M02_002": [
        {"title": "Room program", "type": "highlight", "text": "Har xona nomi bilan birga vazifasi, foydalanuvchisi va kerakli aloqasi yozilishi mumkin."},
        {"title": "Priorities", "type": "normal", "text": "MUST HAVE / SHOULD HAVE / OPTIONAL kabi guruhlash qaror qabul qilishni osonlashtiradi."},
        {"title": "Hammasi bir xil muhim emas", "type": "warning", "text": "Barcha istaklarni bir xil ustuvorlikda qoldirish keyinchalik konflikt keltiradi."},
        {"title": "Mini-amaliyot", "type": "example", "text": "20 ta talabni 3 ustuvorlik guruhiga ajrating."},
    ],
    "L13_M02_003": [
        {"title": "Constraints", "type": "highlight", "text": "Uchastka, normativ, budjet, vaqt va konstruktiv sharoitlar briefga ta'sir qiladi."},
        {"title": "Assumption", "type": "normal", "text": "Tasdiqlanmagan ma'lumot assumption sifatida alohida qayd qilinadi."},
        {"title": "Taxminni fakt deb yozmang", "type": "warning", "text": "Aniqlanmagan ma'lumotni tasdiqlangan talab sifatida hujjatlashtirish xato."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Brief uchun Constraints va Open Questions bo'limini yozing."},
    ],
    "L13_M02_004": [
        {"title": "Client confirmation", "type": "highlight", "text": "Brief tayyor bo'lgach mijoz bilan qayta ko'rib chiqiladi."},
        {"title": "Nega?", "type": "normal", "text": "Arxitektor bir gapni, mijoz boshqa ma'noda tushungan bo'lishi mumkin."},
        {"title": "Tasdiqsiz boshlash", "type": "warning", "text": "Katta loyiha bosqichiga noaniq brief bilan o'tish qayta ishlash xavfini oshiradi."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Mijozga yuboriladigan brief confirmation message yozing."},
    ],
    "L13_M02_005": [
        {"title": "Brief audit", "type": "highlight", "text": "Client → site → lifestyle → program → priorities → constraints → assumptions → confirmation."},
        {"title": "Professional checklist", "type": "example", "text": "1. Oila ma'lummi?<br><br>2. Site data bormi?<br><br>3. Room program to'liqmi?<br><br>4. Priorities belgilanganmi?<br><br>5. Constraints yozilganmi?<br><br>6. Assumptions alohidami?<br><br>7. Open questions bormi?<br><br>8. Client tasdiqladimi?"},
        {"title": "Keyingi modul", "type": "highlight", "text": "Keyingi modul: BUDJET."},
    ],
}


LEVEL13_MODULE02_QUIZ = {}

for i, lesson_code in enumerate(
    ["L13_M02_001", "L13_M02_002", "L13_M02_003", "L13_M02_004", "L13_M02_005"]
):
    start = 16 + i * 3

    LEVEL13_MODULE02_QUIZ[lesson_code] = [
        {
            "code": f"L13_Q{start:03d}",
            "question": "Professional brief mijoz talablarini strukturali hujjatga aylantiradimi?",
            "explanation": "Brief loyiha uchun umumiy yozma asos yaratadi.",
            "options": [("A", "Ha", True), ("B", "Yo'q", False)],
        },
        {
            "code": f"L13_Q{start + 1:03d}",
            "question": "Tasdiqlanmagan taxminni aniq fakt deb yozish to'g'rimi?",
            "explanation": "Assumption alohida qayd qilinishi kerak.",
            "options": [("A", "Ha", False), ("B", "Yo'q", True)],
        },
        {
            "code": f"L13_Q{start + 2:03d}",
            "question": "Briefni mijoz bilan tasdiqlash qayta ishlash xavfini kamaytirishi mumkinmi?",
            "explanation": "Talablar bir xil tushunilganini tekshirishga yordam beradi.",
            "options": [("A", "Ha", True), ("B", "Yo'q", False)],
        },
    ]


def seed_level13_module02():
    connection = get_connection()
    try:
        cursor = connection.cursor()

        for row in LEVEL13_MODULE02_LESSONS:
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
