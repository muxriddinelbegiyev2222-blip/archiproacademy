from database.database import get_connection


LEVEL11_MODULE09_LESSONS = [
    ("L11_M09", "L11_M09_001", "Ishchi loyiha tushunchasi", "theory", "Konseptual loyihadan qurilish uchun aniqroq hujjatga o'tish mantig'ini tushunish.", 1, 90, 20),
    ("L11_M09", "L11_M09_002", "Plan va o'lchamlar", "practice", "Qavat planlarini hujjatlashtirish va kerakli ma'lumotlarni tartibga solish.", 2, 100, 20),
    ("L11_M09", "L11_M09_003", "Fasad, kesim va detallar", "practice", "Vertikal chizmalar va kritik detail zonalarini tayyorlash.", 3, 105, 20),
    ("L11_M09", "L11_M09_004", "Koordinatsiya va revision", "practice", "Arxitektura, konstruktsiya va MEP o'zgarishlarini boshqarish.", 4, 110, 20),
    ("L11_M09", "L11_M09_005", "LEVEL 11 final ishchi loyiha auditi", "practice", "Ikki qavatli uy hujjatlarini kompleks tekshirish.", 5, 135, 25),
]


LEVEL11_MODULE09_CONTENT = {
    "L11_M09_001": [
        {"title": "Konseptdan hujjatga", "type": "highlight", "text": "Ishchi loyiha konsepsiyani aniqroq, koordinatsiyalangan va o'qiladigan qurilish ma'lumotiga aylantiradi."},
        {"title": "Maqsad", "type": "normal", "text": "Loyiha qarori chizmada tushunarli, izchil va tekshiriladigan bo'lishi kerak."},
        {"title": "Xato", "type": "warning", "text": "Render yoki umumiy plan qurilish uchun barcha kerakli ma'lumotni bermaydi."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Ishchi loyiha paketiga kirishi mumkin bo'lgan chizmalarni ro'yxat qiling."},
    ],
    "L11_M09_002": [
        {"title": "Plan hujjati", "type": "highlight", "text": "Plan faqat xona konturi emas; kerakli o'lcham, marker, nom va boshqa ma'lumotlar bilan o'qiladi."},
        {"title": "Dimension logic", "type": "normal", "text": "O'lchamlar qurilish va tekshiruv uchun tushunarli hierarxiyada beriladi."},
        {"title": "Ortiqcha o'lcham", "type": "warning", "text": "Hamma narsani bir xil darajada dimension qilish chizmani o'qilmas qilishi mumkin."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Plan uchun primary, secondary va detail dimensions guruhlarini tuzing."},
    ],
    "L11_M09_003": [
        {"title": "Fasad va kesim", "type": "highlight", "text": "Plan bilan tushunarsiz qolgan vertikal ma'lumot fasad va kesimda ochiladi."},
        {"title": "Critical details", "type": "normal", "text": "Tom, balkon, parapet, opening, stair va boshqa kritik zonalar alohida detail talab qilishi mumkin."},
        {"title": "Noto'g'ri detail", "type": "warning", "text": "Umumiy internet detailini o'z loyihangizga tekshirmasdan ko'chirmang."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Loyihangiz uchun 8 ta kritik detail zonasini yozing."},
    ],
    "L11_M09_004": [
        {"title": "Revision", "type": "highlight", "text": "Ishchi loyiha jarayonida o'zgarishlar nazorat bilan boshqariladi."},
        {"title": "Coordination", "type": "normal", "text": "Arxitektura o'zgarishi konstruktsiya va MEPga ta'sir qilsa tegishli mutaxassislar bilan qayta kelishiladi."},
        {"title": "Eski chizma", "type": "warning", "text": "Eski revision qurilishda ishlatilishi jiddiy xato tug'dirishi mumkin."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Revision log namunasi tuzing."},
    ],
    "L11_M09_005": [
        {"title": "LEVEL 11 audit", "type": "highlight", "text": "Brief → 2-floor zoning → stair → vertical systems → void → balcony → facade → BIM → working drawings → final audit."},
        {"title": "Professional checklist", "type": "example", "text": "1. Qavatlar mosmi?<br><br>2. Stair to'g'rimi?<br><br>3. Vertikal MEP koordinatsiya qilinganmi?<br><br>4. Void/balcony detallari ko'rilganmi?<br><br>5. Fasads va sections mosmi?<br><br>6. Plans dimension qilinganmi?<br><br>7. Critical details aniqlanganmi?<br><br>8. Revision nazoratdami?<br><br>9. Barcha hujjatlar bir versiyami?"},
        {"title": "LEVEL 11 yakuni", "type": "highlight", "text": "Siz endi 2 qavatli turar joyni konsepsiyadan koordinatsiyalangan ishchi loyiha bosqichigacha olib borish workflow'ini bilasiz."},
    ],
}


LEVEL11_MODULE09_QUIZ = {}

for i, lesson_code in enumerate(
    ["L11_M09_001", "L11_M09_002", "L11_M09_003", "L11_M09_004", "L11_M09_005"]
):
    start = 121 + i * 3

    LEVEL11_MODULE09_QUIZ[lesson_code] = [
        {
            "code": f"L11_Q{start:03d}",
            "question": "Ishchi loyiha konseptdan aniqroq va koordinatsiyalangan hujjatga o'tishni anglatadimi?",
            "explanation": "Qurilish va tekshiruv uchun loyiha ma'lumoti aniqroq bo'ladi.",
            "options": [("A", "Ha", True), ("B", "Yo'q", False)],
        },
        {
            "code": f"L11_Q{start + 1:03d}",
            "question": "Eski revisionni nazoratsiz ishlatish xavfsizmi?",
            "explanation": "Eski ma'lumot qurilish xatosiga olib kelishi mumkin.",
            "options": [("A", "Ha", False), ("B", "Yo'q", True)],
        },
        {
            "code": f"L11_Q{start + 2:03d}",
            "question": "Plan, fasad, kesim va detallar o'zaro koordinatsiya qilinadimi?",
            "explanation": "Barcha hujjatlar bitta loyiha holatini ko'rsatishi kerak.",
            "options": [("A", "Ha", True), ("B", "Yo'q", False)],
        },
    ]


def seed_level11_module09():
    connection = get_connection()
    try:
        cursor = connection.cursor()

        for row in LEVEL11_MODULE09_LESSONS:
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
