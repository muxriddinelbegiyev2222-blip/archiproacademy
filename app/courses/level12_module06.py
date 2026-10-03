from database.database import get_connection


LEVEL12_MODULE06_LESSONS = [
    ("L12_M06", "L12_M06_001", "Shtampning vazifasi", "theory", "Loyiha sahifasida asosiy identifikatsion ma'lumotlarni tartibli ko'rsatish.", 1, 40, 20),
    ("L12_M06", "L12_M06_002", "Sheet identity", "theory", "Sahifa raqami, nomi, loyiha va revision ma'lumotlarini boshqarish.", 2, 45, 20),
    ("L12_M06", "L12_M06_003", "Grafik standartlar", "practice", "Lineweight, text va annotation izchilligini saqlash.", 3, 50, 20),
    ("L12_M06", "L12_M06_004", "Template standard", "practice", "Shtamp va grafik standartlarni reusable template tizimiga bog'lash.", 4, 50, 20),
    ("L12_M06", "L12_M06_005", "Shtamp va standart audit", "practice", "Loyiha albomidagi sahifa identifikatsiyasi va grafik standartni tekshirish.", 5, 55, 25),
]


LEVEL12_MODULE06_CONTENT = {
    "L12_M06_001": [
        {"title": "Shtamp — identifikatsiya", "type": "highlight", "text": "Shtamp chizmaning qaysi loyiha va qaysi sahifaga tegishli ekanini tushunishga yordam beradi."},
        {"title": "Ma'lumot", "type": "normal", "text": "Loyiha nomi, sheet title, sheet number va kerakli boshqa identifikatsion ma'lumot."},
        {"title": "Dekor emas", "type": "warning", "text": "Shtamp faqat sahifa bezagi emas; u hujjat boshqaruvining bir qismi."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Minimal professional title block fieldlarini yozing."},
    ],
    "L12_M06_002": [
        {"title": "Sheet identity", "type": "highlight", "text": "Har bir sahifa aniq ID va nomga ega bo'lishi kerak."},
        {"title": "Revision", "type": "normal", "text": "Hujjat versiyasi va o'zgarish holati zarur workflowda qayd qilinadi."},
        {"title": "Duplicate sheet", "type": "warning", "text": "Bir xil ID bilan ikki xil sahifa yuritish chalkashlik tug'diradi."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Sheet numbering convention yarating."},
    ],
    "L12_M06_003": [
        {"title": "Grafik standart", "type": "highlight", "text": "Line, text, dimension va annotation yagona grafik tilga bo'ysunadi."},
        {"title": "Hierarchy", "type": "normal", "text": "Kesilgan element, background va annotation vizual darajalari farqlanishi mumkin."},
        {"title": "Har sahifada boshqa style", "type": "warning", "text": "Bir albom ichida tasodifiy font va grafik uslub professional ko'rinishni buzadi."},
        {"title": "Mini-amaliyot", "type": "example", "text": "5 bandli grafik standard yozing."},
    ],
    "L12_M06_004": [
        {"title": "Template bilan bog'lash", "type": "highlight", "text": "Master Layout va umumiy grafik standart template ichida tayyor turishi mumkin."},
        {"title": "Foyda", "type": "normal", "text": "Har yangi loyiha bir xil professional bazadan boshlanadi."},
        {"title": "Template ham audit qilinadi", "type": "warning", "text": "Eski yoki noto'g'ri standardni template orqali ko'paytirib yubormang."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Professional template ichida bo'lishi kerak bo'lgan documentation standartlarini yozing."},
    ],
    "L12_M06_005": [
        {"title": "Standard audit", "type": "highlight", "text": "Sheet ID → title → master → stamp → text → lines → dimensions → revision → consistency."},
        {"title": "Professional checklist", "type": "example", "text": "1. Sheet ID unique-mi?<br><br>2. Title aniqmi?<br><br>3. Stamp to'g'rimi?<br><br>4. Grafik style izchilmi?<br><br>5. Text o'qiladimi?<br><br>6. Revision boshqariladimi?<br><br>7. Template standard latestmi?"},
        {"title": "Keyingi modul", "type": "highlight", "text": "Keyingi modul: PUBLISHER."},
    ],
}


LEVEL12_MODULE06_QUIZ = {}

for i, lesson_code in enumerate(
    ["L12_M06_001", "L12_M06_002", "L12_M06_003", "L12_M06_004", "L12_M06_005"]
):
    start = 76 + i * 3

    LEVEL12_MODULE06_QUIZ[lesson_code] = [
        {
            "code": f"L12_Q{start:03d}",
            "question": "Shtamp loyiha hujjatini identifikatsiya qilishga yordam beradimi?",
            "explanation": "Sahifa va loyiha ma'lumotini ko'rsatadi.",
            "options": [("A", "Ha", True), ("B", "Yo'q", False)],
        },
        {
            "code": f"L12_Q{start + 1:03d}",
            "question": "Grafik standartlarni albom bo'ylab izchil saqlash foydalimi?",
            "explanation": "Hujjat o'qilishi va professional ko'rinishi yaxshilanadi.",
            "options": [("A", "Ha", True), ("B", "Yo'q", False)],
        },
        {
            "code": f"L12_Q{start + 2:03d}",
            "question": "Har sahifada tasodifiy boshqa grafik style ishlatish yaxshi standartmi?",
            "explanation": "Consistency buziladi.",
            "options": [("A", "Ha", False), ("B", "Yo'q", True)],
        },
    ]


def seed_level12_module06():
    connection = get_connection()
    try:
        cursor = connection.cursor()

        for row in LEVEL12_MODULE06_LESSONS:
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
