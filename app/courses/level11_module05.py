from database.database import get_connection


LEVEL11_MODULE05_LESSONS = [
    ("L11_M05", "L11_M05_001", "Void tushunchasi", "theory", "Qavatlar orasidagi ochiq hajmning arxitektura rolini tushunish.", 1, 50, 20),
    ("L11_M05", "L11_M05_002", "Ikkinchi yorug'lik", "theory", "Double-height space va tabiiy yorug'lik aloqasini tushunish.", 2, 55, 20),
    ("L11_M05", "L11_M05_003", "Void va circulation", "practice", "Voidni zinapoya va qavatlararo harakat bilan integratsiya qilish.", 3, 60, 20),
    ("L11_M05", "L11_M05_004", "Void, konstruktsiya va xavfsizlik", "practice", "Plita openingi va himoya elementlarini koordinatsiya qilish.", 4, 65, 20),
    ("L11_M05", "L11_M05_005", "Void professional audit", "practice", "Double-height makonni kompleks tekshirish.", 5, 70, 25),
]


LEVEL11_MODULE05_CONTENT = {
    "L11_M05_001": [
        {"title": "Void — yo'qotilgan maydon emas", "type": "highlight", "text": "To'g'ri ishlatilgan void fazoviy sifat, aloqa va yorug'lik yaratishi mumkin."},
        {"title": "Lekin narxi bor", "type": "normal", "text": "Void qavat maydonini kamaytiradi va konstruktiv hamda iqlim masalalarini kuchaytirishi mumkin."},
        {"title": "Xato", "type": "warning", "text": "Faqat rasmda chiroyli ko'rinishi uchun keraksiz void yaratmang."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Void kerak bo'lishi mumkin bo'lgan 3 ssenariy yozing."},
    ],
    "L11_M05_002": [
        {"title": "Ikkinchi yorug'lik", "type": "highlight", "text": "Double-height space yuqori qavat yoki balandroq opening orqali makonga qo'shimcha yorug'lik olib kirishi mumkin."},
        {"title": "Section bilan ishlang", "type": "normal", "text": "Ikkinchi yorug'likni plan emas, section va 3D orqali ham loyihalash kerak."},
        {"title": "Energiya", "type": "warning", "text": "Katta hajm isitish/sovitish va akustika masalalariga ta'sir qilishi mumkin."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Double-height mehmonxona uchun foyda va kamchiliklarni yozing."},
    ],
    "L11_M05_003": [
        {"title": "Void + stair", "type": "highlight", "text": "Zinapoya void bilan birga kuchli vertikal markaz yaratishi mumkin."},
        {"title": "Visual connection", "type": "normal", "text": "Qavatlar orasidagi ko'rish va fazoviy aloqa boshqariladi."},
        {"title": "Privacy", "type": "warning", "text": "Ochiq void shovqin va privacy'ga ta'sir qilishi mumkin."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Void atrofidagi family/public/private aloqalarni tekshiring."},
    ],
    "L11_M05_004": [
        {"title": "Slab opening", "type": "highlight", "text": "Void plitada katta opening yaratadi va konstruktor bilan koordinatsiya talab qiladi."},
        {"title": "Railing", "type": "normal", "text": "Ochiq chekka xavfsizlik himoyasi bilan hal qilinadi."},
        {"title": "Aniq talab", "type": "warning", "text": "Railing va opening bo'yicha aniq o'lchamlar amaldagi normativlardan tekshiriladi."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Void uchun structure + safety checklist yozing."},
    ],
    "L11_M05_005": [
        {"title": "Void audit", "type": "highlight", "text": "Purpose → location → light → circulation → privacy → structure → safety → climate → section/3D."},
        {"title": "Professional checklist", "type": "example", "text": "1. Voidning maqsadi bormi?<br><br>2. Maydon yo'qotishi oqlanganmi?<br><br>3. Yorug'lik foydasi bormi?<br><br>4. Stair bilan aloqa to'g'rimi?<br><br>5. Privacy/shovqin ko'rildimi?<br><br>6. Konstruktsiya koordinatsiya qilinganmi?<br><br>7. Safety ko'rildimi?"},
        {"title": "Keyingi modul", "type": "highlight", "text": "Keyingi modul: BALKON VA TERASSA."},
    ],
}


LEVEL11_MODULE05_QUIZ = {}

for i, lesson_code in enumerate(
    ["L11_M05_001", "L11_M05_002", "L11_M05_003", "L11_M05_004", "L11_M05_005"]
):
    start = 61 + i * 3

    LEVEL11_MODULE05_QUIZ[lesson_code] = [
        {
            "code": f"L11_Q{start:03d}",
            "question": "Void fazoviy sifat yaratishi mumkinmi?",
            "explanation": "Qavatlar orasidagi ochiq hajm makon sifatiga ta'sir qilishi mumkin.",
            "options": [("A", "Ha", True), ("B", "Yo'q", False)],
        },
        {
            "code": f"L11_Q{start + 1:03d}",
            "question": "Void faqat chiroyli ko'rinish uchun qo'shilishi kerakmi?",
            "explanation": "Uning funksional va fazoviy maqsadi bo'lishi kerak.",
            "options": [("A", "Ha", False), ("B", "Yo'q", True)],
        },
        {
            "code": f"L11_Q{start + 2:03d}",
            "question": "Void konstruktsiya va xavfsizlik bilan koordinatsiya qilinadimi?",
            "explanation": "Plita openingi va ochiq chekka muhim.",
            "options": [("A", "Ha", True), ("B", "Yo'q", False)],
        },
    ]


def seed_level11_module05():
    connection = get_connection()
    try:
        cursor = connection.cursor()

        for row in LEVEL11_MODULE05_LESSONS:
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
