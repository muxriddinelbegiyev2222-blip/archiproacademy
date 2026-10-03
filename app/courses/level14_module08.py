from database.database import get_connection


LEVEL14_MODULE08_LESSONS = [
    ("L14_M08", "L14_M08_001", "Case Study tahlil metodikasi", "theory", "Murakkab turar joy loyihalarini tizimli tahlil qilish.", 1, 100, 20),
    ("L14_M08", "L14_M08_002", "Case 1: murakkab site", "practice", "Tor, qiyshiq yoki nishabli uchastka muammolarini birlashtirib yechish.", 2, 110, 20),
    ("L14_M08", "L14_M08_003", "Case 2: murakkab oila programmasi", "practice", "Ko'p avlodli yoki katta programmani professional tashkil qilish.", 3, 120, 20),
    ("L14_M08", "L14_M08_004", "Case 3: dizayn va texnik konflikt", "practice", "Arxitektura sifati bilan konstruktsiya, MEP va budjetni muvozanatlash.", 4, 125, 20),
    ("L14_M08", "L14_M08_005", "LEVEL 14 Advanced Case audit", "practice", "Murakkab loyiha muammolarini mustaqil yechish va himoya qilish.", 5, 145, 25),
]


LEVEL14_MODULE08_CONTENT = {
    "L14_M08_001": [
        {"title": "Case Study — nusxa olish emas", "type": "highlight", "text": "Maqsad boshqa loyihaning formasini ko'chirish emas, qaror ortidagi sabab va trade-offlarni tushunish."},
        {"title": "Tahlil ketma-ketligi", "type": "normal", "text": "Context → brief → constraints → concept → decisions → conflicts → solutions → lessons."},
        {"title": "Xato", "type": "warning", "text": "Faqat final renderga qarab loyiha sifatini baholamang."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Case Study template yarating."},
    ],
    "L14_M08_002": [
        {"title": "Murakkab site case", "type": "highlight", "text": "Bitta site tor, qiyshiq va nishabli bo'lishi mumkin. Muammolar alohida emas, birgalikda ishlaydi."},
        {"title": "Prioritize", "type": "normal", "text": "Site constraintlarni ta'siri bo'yicha tartiblang va asosiy loyiha strategiyasini tanlang."},
        {"title": "Bir muammoni hal qilib boshqasini yaratmang", "type": "warning", "text": "Masalan, view'ni yaxshilab access yoki drainage'ni buzish mumkin."},
        {"title": "Mini loyiha", "type": "example", "text": "Murakkab site uchun concept + section + access/drainage diagram tayyorlang."},
    ],
    "L14_M08_003": [
        {"title": "Murakkab family case", "type": "highlight", "text": "Ko'p avlod, ko'p guest, staff yoki future adaptation bir loyihada to'qnashishi mumkin."},
        {"title": "Hierarchy", "type": "normal", "text": "Talablarni critical, important va optional guruhlariga ajratish qarorni boshqaradi."},
        {"title": "Faqat maydon qo'shmang", "type": "warning", "text": "Murakkab programning yechimi doim kattaroq uy emas."},
        {"title": "Mini loyiha", "type": "example", "text": "Complex family brief + zoning + circulation matrix tayyorlang."},
    ],
    "L14_M08_004": [
        {"title": "Design vs reality", "type": "highlight", "text": "Kuchli arxitektura konsepsiyasi konstruktsiya, MEP, envelope, budjet va qurilish mantig'i bilan tekshiriladi."},
        {"title": "Trade-off", "type": "normal", "text": "Har katta arxitektura gesture'ning texnik va moliyaviy oqibati bo'lishi mumkin."},
        {"title": "Hero element", "type": "warning", "text": "Bitta dramatik element butun loyiha tizimini asossiz murakkablashtirmasligi kerak."},
        {"title": "Mini loyiha", "type": "example", "text": "3 design gesture uchun architecture/structure/MEP/budget impact jadvali tuzing."},
    ],
    "L14_M08_005": [
        {"title": "LEVEL 14 final workflow", "type": "highlight", "text": "Read context → define problem → prioritize constraints → generate alternatives → test → coordinate → compare → defend → audit."},
        {"title": "Professional checklist", "type": "example", "text": "1. Muammo to'g'ri aniqlanganmi?<br><br>2. Constraints prioritetlanganmi?<br><br>3. Alternativlar ko'rildimi?<br><br>4. Site ishlaydimi?<br><br>5. Program ishlaydimi?<br><br>6. Structure/MEP mumkinmi?<br><br>7. Budget ta'siri ko'rildimi?<br><br>8. Qarorlar dalil bilan himoya qilinadimi?<br><br>9. Final loyiha qayta audit qilindimi?"},
        {"title": "LEVEL 14 yakuni", "type": "highlight", "text": "Siz endi oddiy ideal sharoit emas, real va murakkab turar joy vaziyatlarini tahlil qilish va yechish bosqichiga chiqdingiz."},
    ],
}


LEVEL14_MODULE08_QUIZ = {}

for i, lesson_code in enumerate(
    ["L14_M08_001", "L14_M08_002", "L14_M08_003", "L14_M08_004", "L14_M08_005"]
):
    start = 106 + i * 3

    LEVEL14_MODULE08_QUIZ[lesson_code] = [
        {
            "code": f"L14_Q{start:03d}",
            "question": "Case Study'da final formani ko'chirishdan ko'ra qaror sababini tushunish muhimmi?",
            "explanation": "Professional tahlil loyiha mantiqini o'rganadi.",
            "options": [("A", "Ha", True), ("B", "Yo'q", False)],
        },
        {
            "code": f"L14_Q{start + 1:03d}",
            "question": "Bitta muammoni hal qilib boshqa kritik muammoni yaratish yaxshi yechimmi?",
            "explanation": "Loyiha butun tizim sifatida tekshiriladi.",
            "options": [("A", "Ha", False), ("B", "Yo'q", True)],
        },
        {
            "code": f"L14_Q{start + 2:03d}",
            "question": "Murakkab loyihada alternative va trade-offlarni solishtirish kerakmi?",
            "explanation": "Qaror ongli va dalilli bo'ladi.",
            "options": [("A", "Ha", True), ("B", "Yo'q", False)],
        },
    ]


def seed_level14_module08():
    connection = get_connection()
    try:
        cursor = connection.cursor()

        for row in LEVEL14_MODULE08_LESSONS:
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
