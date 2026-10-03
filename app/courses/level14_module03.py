from database.database import get_connection


LEVEL14_MODULE03_LESSONS = [
    ("L14_M03", "L14_M03_001", "Nishabli site analysis", "theory", "Yer balandliklari va nishab yo'nalishini o'qish.", 1, 70, 20),
    ("L14_M03", "L14_M03_002", "Bino sathi va terrain", "theory", "Bino level'larini mavjud relyef bilan bog'lash.", 2, 80, 20),
    ("L14_M03", "L14_M03_003", "Split-level va terracing", "practice", "Nishabga mos fazoviy strategiyalarni tushunish.", 3, 85, 20),
    ("L14_M03", "L14_M03_004", "Drenaj, retaining va access", "practice", "Nishabli uchastkadagi asosiy texnik risklarni koordinatsiya qilish.", 4, 90, 20),
    ("L14_M03", "L14_M03_005", "Nishabli yer professional audit", "practice", "Terrain, bino va tashqi harakatni kompleks tekshirish.", 5, 95, 25),
]


LEVEL14_MODULE03_CONTENT = {
    "L14_M03_001": [
        {"title": "Nishabni chiziq emas, 3D deb ko'ring", "type": "highlight", "text": "Contour va spot level ma'lumotlari uchastkaning real uch o'lchamli shaklini tushunishga yordam beradi."},
        {"title": "Tahlil", "type": "normal", "text": "High point, low point, nishab yo'nalishi, kirish, suv yo'li va ko'rinishlar aniqlanadi."},
        {"title": "Xato", "type": "warning", "text": "Nishabli uchastkani tekis deb qabul qilib loyiha boshlamang."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Site'da high/low points va asosiy slope directionni belgilang."},
    ],
    "L14_M03_002": [
        {"title": "Bino 0.000", "type": "highlight", "text": "Bino referens sathi mavjud yer bilan ongli bog'lanadi."},
        {"title": "Cut / fill", "type": "normal", "text": "Bino joylashuvi qazish va to'ldirish hajmiga ta'sir qilishi mumkin."},
        {"title": "Taxminiy sath", "type": "warning", "text": "Topografik ma'lumotsiz aniq earthwork yoki retaining yechimlarini taxmin qilish mumkin emas."},
        {"title": "Mini-amaliyot", "type": "example", "text": "3 bino level strategiyasini section orqali solishtiring."},
    ],
    "L14_M03_003": [
        {"title": "Split-level", "type": "highlight", "text": "Ba'zi nishabli uchastkalarda bino sathlari terrain bilan bosqichma-bosqich ishlashi mumkin."},
        {"title": "Terracing", "type": "normal", "text": "Tashqi maydon ham bir necha sathga bo'linishi mumkin."},
        {"title": "Murakkablik", "type": "warning", "text": "Ko'p level avtomatik ravishda yaxshi loyiha degani emas; circulation va accessibility tekshiriladi."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Flat platform va split-level konsepsiyalarini taqqoslang."},
    ],
    "L14_M03_004": [
        {"title": "Suv pastga harakat qiladi", "type": "highlight", "text": "Nishabli site'da surface water yo'li bino xavfsizligi bilan koordinatsiya qilinadi."},
        {"title": "Retaining", "type": "normal", "text": "Yer bosimini ushlab turuvchi konstruktiv elementlar konstruktor va geotexnik ma'lumot bilan loyihalanadi."},
        {"title": "Access", "type": "normal", "text": "Piyoda va avtomobil kirishlari terrain bilan real ishlashi kerak."},
        {"title": "Muhim", "type": "warning", "text": "Retaining wall o'lchami va armaturasi professional konstruktiv hisob talab qiladi."},
    ],
    "L14_M03_005": [
        {"title": "Slope audit", "type": "highlight", "text": "Survey → slope → building level → cut/fill → circulation → drainage → retaining → structure → landscape."},
        {"title": "Professional checklist", "type": "example", "text": "1. Survey ma'lumoti bormi?<br><br>2. Slope yo'nalishi aniqmi?<br><br>3. 0.000 mantiqiymi?<br><br>4. Access ishlaydimi?<br><br>5. Drainage ko'rildimi?<br><br>6. Retaining zonalar aniqlanganmi?<br><br>7. Konstruktor bilan koordinatsiya bormi?"},
        {"title": "Keyingi modul", "type": "highlight", "text": "Keyingi modul: KATTA VILLA."},
    ],
}


LEVEL14_MODULE03_QUIZ = {}

for i, lesson_code in enumerate(
    ["L14_M03_001", "L14_M03_002", "L14_M03_003", "L14_M03_004", "L14_M03_005"]
):
    start = 31 + i * 3

    LEVEL14_MODULE03_QUIZ[lesson_code] = [
        {
            "code": f"L14_Q{start:03d}",
            "question": "Nishabli uchastkada topografik ma'lumot muhimmi?",
            "explanation": "Yer balandliklari loyiha qaroriga ta'sir qiladi.",
            "options": [("A", "Ha", True), ("B", "Yo'q", False)],
        },
        {
            "code": f"L14_Q{start + 1:03d}",
            "question": "Retaining wall o'lchamini arxitektor taxmin bilan belgilashi to'g'rimi?",
            "explanation": "Konstruktiv va geotexnik hisob talab qilinadi.",
            "options": [("A", "Ha", False), ("B", "Yo'q", True)],
        },
        {
            "code": f"L14_Q{start + 2:03d}",
            "question": "Nishabli site'da drainage va access birga tekshiriladimi?",
            "explanation": "Terrain harakat va suv boshqaruviga ta'sir qiladi.",
            "options": [("A", "Ha", True), ("B", "Yo'q", False)],
        },
    ]


def seed_level14_module03():
    connection = get_connection()
    try:
        cursor = connection.cursor()

        for row in LEVEL14_MODULE03_LESSONS:
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
