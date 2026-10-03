from database.database import get_connection


LEVEL13_MODULE05_LESSONS = [
    ("L13_M05", "L13_M05_001", "Taqdimot strukturasi", "theory", "Loyiha qarorini mijozga mantiqiy ketma-ketlikda tushuntirish.", 1, 40, 20),
    ("L13_M05", "L13_M05_002", "Plan va diagrammani tushuntirish", "theory", "Texnik chizmalarni mijoz uchun sodda tilda izohlash.", 2, 45, 20),
    ("L13_M05", "L13_M05_003", "3D va vizual material", "practice", "Vizual materialni loyiha qarorini tushuntirish uchun ishlatish.", 3, 50, 20),
    ("L13_M05", "L13_M05_004", "Savol va e'tirozlar", "practice", "Mijoz savollariga professional tarzda javob berish.", 4, 50, 20),
    ("L13_M05", "L13_M05_005", "Loyiha taqdimoti audit", "practice", "Prezentatsiyani mijozga ko'rsatishdan oldin kompleks tekshirish.", 5, 55, 25),
]


LEVEL13_MODULE05_CONTENT = {
    "L13_M05_001": [
        {"title": "Hikoya tartibi", "type": "highlight", "text": "Brief → site → concept → plan → facade/massing → key benefits → open decisions."},
        {"title": "Maqsad", "type": "normal", "text": "Mijoz nima uchun aynan shu qaror qabul qilinganini tushunishi kerak."},
        {"title": "Xato", "type": "warning", "text": "Darhol murakkab plan va texnik terminlardan boshlamang."},
        {"title": "Mini-amaliyot", "type": "example", "text": "10 daqiqalik loyiha prezentatsiyasi strukturasi tuzing."},
    ],
    "L13_M05_002": [
        {"title": "Sodda til", "type": "highlight", "text": "Mijoz arxitektura terminlarini bilmasligi mumkin. Qarorni kundalik foydalanish orqali tushuntiring."},
        {"title": "Diagramma", "type": "normal", "text": "Zonalash, circulation va site diagrammasi murakkab planni tez tushuntirishga yordam beradi."},
        {"title": "Faqat termin", "type": "warning", "text": "Professional ko'rinish uchun ortiqcha jargon ishlatmang."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Bir plan qarorini oddiy tilda 5 jumlada tushuntiring."},
    ],
    "L13_M05_003": [
        {"title": "3D yordam beradi", "type": "highlight", "text": "3D mijozga hajm va makonni tasavvur qilishda yordam beradi."},
        {"title": "Lekin 3D hamma narsa emas", "type": "normal", "text": "Yaxshi render yomon plan muammosini hal qilmaydi."},
        {"title": "Noto'g'ri expectation", "type": "warning", "text": "Konseptual vizualni qurilishdagi aynan yakuniy natija deb noto'g'ri tasavvur qildirmang."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Prezentatsiya uchun kerakli 5 ta visual viewni tanlang."},
    ],
    "L13_M05_004": [
        {"title": "Savol — qarshilik emas", "type": "highlight", "text": "Mijozning savoli yoki e'tirozi loyiha talabini yaxshiroq tushunish imkoniyati."},
        {"title": "Bilmasangiz", "type": "normal", "text": "Aniq bilmagan texnik savolga taxminiy javob berish o'rniga tekshirish kerakligini ayting."},
        {"title": "Himoya qilish ≠ tortishish", "type": "warning", "text": "Qarorni dalil bilan tushuntiring, suhbatni shaxsiy bahsga aylantirmang."},
        {"title": "Mini-amaliyot", "type": "example", "text": "5 ta qiyin mijoz savoliga professional javob ssenariysi yozing."},
    ],
    "L13_M05_005": [
        {"title": "Presentation audit", "type": "highlight", "text": "Goal → story → diagrams → plans → visuals → trade-offs → decisions → Q&A."},
        {"title": "Professional checklist", "type": "example", "text": "1. Prezentatsiya maqsadi aniqmi?<br><br>2. Brief eslatildimi?<br><br>3. Site qarori tushuntirildimi?<br><br>4. Plan sodda tushuntiriladimi?<br><br>5. 3D plan bilan mosmi?<br><br>6. Trade-off yashirilmaganmi?<br><br>7. Mijozdan qanday qaror kerakligi aniqmi?"},
        {"title": "Keyingi modul", "type": "highlight", "text": "Keyingi modul: MIJOZ TUZATISHLARI."},
    ],
}


LEVEL13_MODULE05_QUIZ = {}

for i, lesson_code in enumerate(
    ["L13_M05_001", "L13_M05_002", "L13_M05_003", "L13_M05_004", "L13_M05_005"]
):
    start = 61 + i * 3

    LEVEL13_MODULE05_QUIZ[lesson_code] = [
        {
            "code": f"L13_Q{start:03d}",
            "question": "Loyiha taqdimotida qarorlarning sababini tushuntirish muhimmi?",
            "explanation": "Mijoz faqat natijani emas, mantiqni ham tushunishi kerak.",
            "options": [("A", "Ha", True), ("B", "Yo'q", False)],
        },
        {
            "code": f"L13_Q{start + 1:03d}",
            "question": "Yaxshi render yomon plan muammosini avtomatik hal qiladimi?",
            "explanation": "Vizual sifat funksional sifatni almashtirmaydi.",
            "options": [("A", "Ha", False), ("B", "Yo'q", True)],
        },
        {
            "code": f"L13_Q{start + 2:03d}",
            "question": "Bilmagan texnik savolga taxmin qilish o'rniga tekshirib javob berish professionalmi?",
            "explanation": "Aniq bo'lmagan ma'lumotni ishonch bilan aytmaslik kerak.",
            "options": [("A", "Ha", True), ("B", "Yo'q", False)],
        },
    ]


def seed_level13_module05():
    connection = get_connection()
    try:
        cursor = connection.cursor()

        for row in LEVEL13_MODULE05_LESSONS:
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
