from database.database import get_connection


LEVEL12_MODULE05_LESSONS = [
    ("L12_M05", "L12_M05_001", "Layout Book tushunchasi", "theory", "Loyiha chizmalarini sheetlar ko'rinishida tashkil qilish.", 1, 60, 20),
    ("L12_M05", "L12_M05_002", "Master Layout mantig'i", "theory", "Takrorlanuvchi sahifa elementlarini standartlashtirish.", 2, 70, 20),
    ("L12_M05", "L12_M05_003", "Drawing placement", "practice", "Saved viewlarni layoutga izchil joylashtirish.", 3, 70, 20),
    ("L12_M05", "L12_M05_004", "Sheet hierarchy va readability", "practice", "Sahifada grafik hierarxiya va o'qilishni boshqarish.", 4, 75, 20),
    ("L12_M05", "L12_M05_005", "Layout Book professional audit", "practice", "Butun loyiha albomini layout darajasida tekshirish.", 5, 85, 25),
]


LEVEL12_MODULE05_CONTENT = {
    "L12_M05_001": [
        {"title": "Layout — yakuniy sahifa", "type": "highlight", "text": "Layout loyiha chizmasini topshiriladigan yoki chop etiladigan sheet ko'rinishida tashkil qiladi."},
        {"title": "Struktura", "type": "normal", "text": "Sheet number, title, drawinglar va kerakli umumiy ma'lumot bir tizimda ishlaydi."},
        {"title": "Xato", "type": "warning", "text": "Chizmalarni tasodifiy sheetlarga joylashtirish albom mantiqini buzadi."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Loyiha albomi uchun layoutlar ketma-ketligini yozing."},
    ],
    "L12_M05_002": [
        {"title": "Master Layout", "type": "highlight", "text": "Takroriy sahifa strukturasi master orqali standartlashtirilishi mumkin."},
        {"title": "Takroriy elementlar", "type": "normal", "text": "Border, shtamp, page identity va boshqa umumiy elementlar."},
        {"title": "Qo'lda har sahifada", "type": "warning", "text": "Bir xil elementni har layoutda qo'lda takrorlash xato va vaqt yo'qotishi mumkin."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Master Layoutda bo'lishi kerak bo'lgan elementlarni yozing."},
    ],
    "L12_M05_003": [
        {"title": "View → Drawing → Layout", "type": "highlight", "text": "Nazorat qilingan saved view layoutda drawing sifatida joylashtiriladi."},
        {"title": "Scale", "type": "normal", "text": "Drawing maqsadli o'qiladigan hajm va sahifa strukturasida bo'lishi kerak."},
        {"title": "Crop muammosi", "type": "warning", "text": "Drawing chegarasi muhim annotationni kesib tashlamasligi kerak."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Bir layoutdagi barcha drawinglarni source view bilan tekshiring."},
    ],
    "L12_M05_004": [
        {"title": "Hierarchy", "type": "highlight", "text": "Asosiy drawing vizual dominant, yordamchi ma'lumotlar secondary bo'lishi mumkin."},
        {"title": "Readability", "type": "normal", "text": "Text, linework va drawinglar chop/eksport holatida ham o'qilishi kerak."},
        {"title": "Crowded sheet", "type": "warning", "text": "Bitta sahifaga haddan ortiq drawing joylashtirish o'qilishni yomonlashtiradi."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Bir sheetni alignment, hierarchy va whitespace bo'yicha audit qiling."},
    ],
    "L12_M05_005": [
        {"title": "Layout audit", "type": "highlight", "text": "Sheet structure → master → drawing source → scale → title → alignment → readability → revision."},
        {"title": "Professional checklist", "type": "example", "text": "1. Sheet number to'g'rimi?<br><br>2. Title to'g'rimi?<br><br>3. Master to'g'rimi?<br><br>4. Drawing source latestmi?<br><br>5. Scale mosmi?<br><br>6. Annotation ko'rinadimi?<br><br>7. Sheet crowded emasmi?<br><br>8. Albom ketma-ketligi mantiqiymi?"},
        {"title": "Keyingi modul", "type": "highlight", "text": "Keyingi modul: SHTAMP VA STANDARTLAR."},
    ],
}


LEVEL12_MODULE05_QUIZ = {}

for i, lesson_code in enumerate(
    ["L12_M05_001", "L12_M05_002", "L12_M05_003", "L12_M05_004", "L12_M05_005"]
):
    start = 61 + i * 3

    LEVEL12_MODULE05_QUIZ[lesson_code] = [
        {
            "code": f"L12_Q{start:03d}",
            "question": "Layout loyiha chizmalarini sheet ko'rinishida tashkil qiladimi?",
            "explanation": "Layout topshiriladigan sahifa strukturasidir.",
            "options": [("A", "Ha", True), ("B", "Yo'q", False)],
        },
        {
            "code": f"L12_Q{start + 1:03d}",
            "question": "Master Layout takroriy elementlarni standartlashtirishga yordam beradimi?",
            "explanation": "Sahifa strukturasi izchil bo'ladi.",
            "options": [("A", "Ha", True), ("B", "Yo'q", False)],
        },
        {
            "code": f"L12_Q{start + 2:03d}",
            "question": "Bitta layoutga imkon qadar ko'p drawing joylashtirish har doim yaxshi yechimmi?",
            "explanation": "Readability pasayishi mumkin.",
            "options": [("A", "Ha", False), ("B", "Yo'q", True)],
        },
    ]


def seed_level12_module05():
    connection = get_connection()
    try:
        cursor = connection.cursor()

        for row in LEVEL12_MODULE05_LESSONS:
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
