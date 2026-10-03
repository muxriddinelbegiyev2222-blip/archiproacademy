from database.database import get_connection


LEVEL12_MODULE02_LESSONS = [
    ("L12_M02", "L12_M02_001", "Element ma'lumoti tushunchasi", "theory", "BIM elementning geometrik va informatsion xususiyatlarini tushunish.", 1, 40, 20),
    ("L12_M02", "L12_M02_002", "ID, nom va klassifikatsiya", "theory", "Elementlarni tartibli identifikatsiya qilish.", 2, 45, 20),
    ("L12_M02", "L12_M02_003", "Properties va parametrlar", "practice", "Element ma'lumotlarini standart va foydali tarzda to'ldirish.", 3, 50, 20),
    ("L12_M02", "L12_M02_004", "Data consistency", "practice", "Bir xil turdagi elementlarda ma'lumot izchilligini ta'minlash.", 4, 50, 20),
    ("L12_M02", "L12_M02_005", "Element Information audit", "practice", "BIM element ma'lumotlarini kompleks tekshirish.", 5, 55, 25),
]


LEVEL12_MODULE02_CONTENT = {
    "L12_M02_001": [
        {"title": "Element faqat shakl emas", "type": "highlight", "text": "BIM elementning geometriyasi bilan birga uning identifikatsiyasi va xususiyatlari ham muhim."},
        {"title": "Data", "type": "normal", "text": "ID, type, material, classification, property va boshqa parametrlar loyiha maqsadiga qarab ishlatilishi mumkin."},
        {"title": "Xato", "type": "warning", "text": "Keraksiz data bilan modelni to'ldirish ham professional yondashuv emas."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Wall, door va window uchun zarur bo'lishi mumkin bo'lgan data ro'yxatini tuzing."},
    ],
    "L12_M02_002": [
        {"title": "Identifikatsiya", "type": "highlight", "text": "Elementni keyin topish, schedule qilish va tekshirish uchun izchil nomlash foydali."},
        {"title": "Classification", "type": "normal", "text": "Elementning loyiha tizimidagi roli classification orqali tartiblanishi mumkin."},
        {"title": "Noto'g'ri nomlash", "type": "warning", "text": "Bir xil elementlarni turli tasodifiy nom bilan yuritish keyingi auditni qiyinlashtiradi."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Door va window uchun sodda naming convention yarating."},
    ],
    "L12_M02_003": [
        {"title": "Properties", "type": "highlight", "text": "Properties loyiha elementiga qo'shimcha ma'lumot bog'lash imkonini beradi."},
        {"title": "Maqsad", "type": "normal", "text": "Data keyinchalik filtering, schedule yoki boshqa boshqaruv vazifasiga xizmat qilishi kerak."},
        {"title": "Data uchun data", "type": "warning", "text": "Hech qayerda ishlatilmaydigan yuzlab property kiritish modelni ortiqcha murakkablashtiradi."},
        {"title": "Mini-amaliyot", "type": "example", "text": "5 ta foydali project property va nima uchun kerakligini yozing."},
    ],
    "L12_M02_004": [
        {"title": "Consistency", "type": "highlight", "text": "Bir xil turdagi elementlar bir xil data qoidalariga amal qilishi kerak."},
        {"title": "Empty data", "type": "normal", "text": "Majburiy property bo'sh qolgan elementlar auditda topilishi kerak."},
        {"title": "Copy error", "type": "warning", "text": "Elementni copy qilganda eski yoki noto'g'ri data qolib ketishi mumkin."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Door data bo'yicha 5 ta consistency check yozing."},
    ],
    "L12_M02_005": [
        {"title": "Data audit", "type": "highlight", "text": "Element type → ID → classification → properties → completeness → consistency → schedule test."},
        {"title": "Professional checklist", "type": "example", "text": "1. ID mantiqiymi?<br><br>2. Nomlash izchilmi?<br><br>3. Classification to'g'rimi?<br><br>4. Majburiy properties to'lganmi?<br><br>5. Copy xatolari yo'qmi?<br><br>6. Schedule'da to'g'ri chiqadimi?"},
        {"title": "Keyingi modul", "type": "highlight", "text": "Keyingi modul: SPETSIFIKATSIYALAR."},
    ],
}


LEVEL12_MODULE02_QUIZ = {}

for i, lesson_code in enumerate(
    ["L12_M02_001", "L12_M02_002", "L12_M02_003", "L12_M02_004", "L12_M02_005"]
):
    start = 16 + i * 3

    LEVEL12_MODULE02_QUIZ[lesson_code] = [
        {
            "code": f"L12_Q{start:03d}",
            "question": "BIM element geometriyadan tashqari ma'lumot ham saqlashi mumkinmi?",
            "explanation": "Element properties va boshqa data bilan ishlashi mumkin.",
            "options": [("A", "Ha", True), ("B", "Yo'q", False)],
        },
        {
            "code": f"L12_Q{start + 1:03d}",
            "question": "Elementlarni izchil nomlash foydalimi?",
            "explanation": "Qidirish va audit osonlashadi.",
            "options": [("A", "Ha", True), ("B", "Yo'q", False)],
        },
        {
            "code": f"L12_Q{start + 2:03d}",
            "question": "Keraksiz ma'lumotni cheksiz ko'paytirish BIM sifatini avtomatik oshiradimi?",
            "explanation": "Data maqsadli va boshqariladigan bo'lishi kerak.",
            "options": [("A", "Ha", False), ("B", "Yo'q", True)],
        },
    ]


def seed_level12_module02():
    connection = get_connection()
    try:
        cursor = connection.cursor()

        for row in LEVEL12_MODULE02_LESSONS:
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
