from database.database import get_connection


LEVEL12_MODULE01_LESSONS = [
    ("L12_M01", "L12_M01_001", "BIM nima?", "theory", "BIMni faqat 3D model emas, loyiha ma'lumotlarini boshqarish tizimi sifatida tushunish.", 1, 40, 20),
    ("L12_M01", "L12_M01_002", "Model va ma'lumot", "theory", "Geometriya bilan element ma'lumotlarining o'zaro aloqasini tushunish.", 2, 45, 20),
    ("L12_M01", "L12_M01_003", "BIM koordinatsiyasi", "practice", "Plan, kesim, fasad va ma'lumotlarning yagona modeldan boshqarilishini tushunish.", 3, 50, 20),
    ("L12_M01", "L12_M01_004", "BIM workflow", "practice", "Modeldan hujjat va spetsifikatsiyagacha bo'lgan ish jarayonini tushunish.", 4, 50, 20),
    ("L12_M01", "L12_M01_005", "BIM professional audit", "practice", "BIM modelning geometriya, ma'lumot va hujjat uyg'unligini tekshirish.", 5, 55, 25),
]


LEVEL12_MODULE01_CONTENT = {
    "L12_M01_001": [
        {"title": "BIM faqat 3D emas", "type": "highlight", "text": "3D geometriya BIMning bir qismi. BIM element, ma'lumot, hujjat va koordinatsiyani birlashtiradi."},
        {"title": "Element", "type": "normal", "text": "Devor shunchaki chiziq emas. U devor turi, material, o'lcham va boshqa ma'lumotlarni olib yurishi mumkin."},
        {"title": "Xato", "type": "warning", "text": "Chiroyli 3D modelni avtomatik ravishda professional BIM model deb qabul qilmang."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Bitta BIM element geometriyadan tashqari qanday ma'lumot olib yurishi mumkinligini yozing."},
    ],
    "L12_M01_002": [
        {"title": "Geometry + Data", "type": "highlight", "text": "BIM qiymati geometriya va ma'lumotning bir elementda bog'lanishidan keladi."},
        {"title": "Misol", "type": "normal", "text": "Eshik modelda joylashadi, chizmada ko'rinadi va kerak bo'lsa schedule ichida ham sanaladi."},
        {"title": "Dublikat ma'lumot", "type": "warning", "text": "Bir ma'lumotni turli joyda qo'lda takrorlash inconsistency xavfini oshiradi."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Door element uchun 8 ta foydali data field yozing."},
    ],
    "L12_M01_003": [
        {"title": "Yagona manba", "type": "highlight", "text": "Plan, section, elevation va schedule bir xil modeldan kelganda koordinatsiya kuchayadi."},
        {"title": "Change", "type": "normal", "text": "Modeldagi to'g'ri o'zgarish tegishli views va hujjatlarda nazorat qilinadi."},
        {"title": "Xato", "type": "warning", "text": "Plan bir versiyada, fasad boshqa versiyada qolib ketmasligi kerak."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Bitta window o'zgarishining plan, fasad, section va schedule'ga ta'sirini yozing."},
    ],
    "L12_M01_004": [
        {"title": "BIM workflow", "type": "highlight", "text": "Model → Views → Schedules → Layouts → Publisher → Exchange."},
        {"title": "Har bosqich bog'langan", "type": "normal", "text": "Model sifati keyingi hujjat va eksport sifatiga ta'sir qiladi."},
        {"title": "Oxirida tuzatish", "type": "warning", "text": "Yomon modelni faqat layout bosqichida qo'lda tuzatish BIM mantiqini buzishi mumkin."},
        {"title": "Mini-amaliyot", "type": "example", "text": "O'z loyihangiz uchun BIM deliverable chain yozing."},
    ],
    "L12_M01_005": [
        {"title": "BIM audit", "type": "highlight", "text": "Element → Geometry → Data → Views → Schedules → Layouts → Outputs → Consistency."},
        {"title": "Professional checklist", "type": "example", "text": "1. Elementlar BIM obyektmi?<br><br>2. Geometriya tozami?<br><br>3. Data to'g'rimi?<br><br>4. Views model bilan bog'liqmi?<br><br>5. Schedules ishlaydimi?<br><br>6. Layoutlar latestmi?<br><br>7. Exportlar nazorat qilinganmi?"},
        {"title": "Keyingi modul", "type": "highlight", "text": "Keyingi modul: ELEMENT INFORMATION."},
    ],
}


LEVEL12_MODULE01_QUIZ = {}

for i, lesson_code in enumerate(
    ["L12_M01_001", "L12_M01_002", "L12_M01_003", "L12_M01_004", "L12_M01_005"]
):
    start = 1 + i * 3

    LEVEL12_MODULE01_QUIZ[lesson_code] = [
        {
            "code": f"L12_Q{start:03d}",
            "question": "BIM faqat 3D geometriyadan iboratmi?",
            "explanation": "BIM geometriya, ma'lumot va hujjatlarni bog'laydi.",
            "options": [("A", "Ha", False), ("B", "Yo'q", True)],
        },
        {
            "code": f"L12_Q{start + 1:03d}",
            "question": "BIM element ma'lumot olib yurishi mumkinmi?",
            "explanation": "Elementlar geometrik va informatsion xususiyatlarga ega bo'lishi mumkin.",
            "options": [("A", "Ha", True), ("B", "Yo'q", False)],
        },
        {
            "code": f"L12_Q{start + 2:03d}",
            "question": "BIMda plan, section va schedule o'zaro koordinatsiya qilinadimi?",
            "explanation": "Yagona modeldan foydalanish koordinatsiyani kuchaytiradi.",
            "options": [("A", "Ha", True), ("B", "Yo'q", False)],
        },
    ]


def seed_level12_module01():
    connection = get_connection()
    try:
        cursor = connection.cursor()

        for row in LEVEL12_MODULE01_LESSONS:
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
