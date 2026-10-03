from database.database import get_connection


LEVEL12_MODULE03_LESSONS = [
    ("L12_M03", "L12_M03_001", "Schedule va spetsifikatsiya", "theory", "Model elementlarini jadval ko'rinishida boshqarish mantig'ini tushunish.", 1, 60, 20),
    ("L12_M03", "L12_M03_002", "Criteria va fieldlar", "theory", "Spetsifikatsiyaga qaysi element va ma'lumotlar kirishini boshqarish.", 2, 70, 20),
    ("L12_M03", "L12_M03_003", "Door va window schedule", "practice", "Ochilishlar bo'yicha amaliy spetsifikatsiya mantiqini shakllantirish.", 3, 70, 20),
    ("L12_M03", "L12_M03_004", "Quantity va data audit", "practice", "Schedule orqali model xatolarini aniqlash.", 4, 75, 20),
    ("L12_M03", "L12_M03_005", "Spetsifikatsiya professional audit", "practice", "Jadvallarni model va loyiha maqsadi bilan kompleks tekshirish.", 5, 85, 25),
]


LEVEL12_MODULE03_CONTENT = {
    "L12_M03_001": [
        {"title": "Schedule — model oynasi", "type": "highlight", "text": "Spetsifikatsiya model elementlarini jadval orqali ko'rish va tekshirish imkonini beradi."},
        {"title": "Live data", "type": "normal", "text": "Jadval model elementlariga bog'liq bo'lsa o'zgarishlar koordinatsiyasi kuchayadi."},
        {"title": "Qo'lda qayta yozish", "type": "warning", "text": "Modeldagi ma'lumotni boshqa jadvalga qo'lda qayta yozish mismatch xavfini oshiradi."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Loyihada kerak bo'lishi mumkin bo'lgan 5 ta schedule turini yozing."},
    ],
    "L12_M03_002": [
        {"title": "Criteria", "type": "highlight", "text": "Criteria jadvalga qaysi elementlar kirishini belgilaydi."},
        {"title": "Fields", "type": "normal", "text": "Fields jadvalda qaysi ma'lumot ustun sifatida ko'rinishini belgilaydi."},
        {"title": "Keraksiz jadval", "type": "warning", "text": "Jadvalga hamma element va hamma fieldni qo'shish uni o'qilmas qilishi mumkin."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Door schedule uchun criteria va fields ro'yxatini tuzing."},
    ],
    "L12_M03_003": [
        {"title": "Door schedule", "type": "highlight", "text": "Eshiklar ID, type, o'lcham yoki boshqa kerakli ma'lumot bo'yicha boshqarilishi mumkin."},
        {"title": "Window schedule", "type": "normal", "text": "Window elementlar uchun ham izchil data talab qilinadi."},
        {"title": "Duplicate ID", "type": "warning", "text": "Noto'g'ri yoki dublikat ID schedule auditida aniqlanishi mumkin."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Door/window schedule uchun 8 ta audit savolini yozing."},
    ],
    "L12_M03_004": [
        {"title": "Schedule — QA vosita", "type": "highlight", "text": "Schedule faqat chiqarish uchun emas, model sifatini tekshirish uchun ham ishlatiladi."},
        {"title": "Topish mumkin", "type": "normal", "text": "Bo'sh property, noto'g'ri classification, dublikat ID yoki kutilmagan miqdor."},
        {"title": "Blind trust", "type": "warning", "text": "Schedule'dagi sonni kriteriya va modelni tekshirmasdan mutlaq to'g'ri deb qabul qilmang."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Schedule yordamida topilishi mumkin bo'lgan 6 ta xato yozing."},
    ],
    "L12_M03_005": [
        {"title": "Schedule audit", "type": "highlight", "text": "Purpose → criteria → fields → data → quantity → formatting → model cross-check."},
        {"title": "Professional checklist", "type": "example", "text": "1. Schedule maqsadi aniqmi?<br><br>2. Criteria to'g'rimi?<br><br>3. Fields keraklimi?<br><br>4. Bo'sh data bormi?<br><br>5. IDlar izchilmi?<br><br>6. Quantity mantiqiymi?<br><br>7. Model bilan cross-check qilindimi?"},
        {"title": "Keyingi modul", "type": "highlight", "text": "Keyingi modul: VIEW MAP PRO."},
    ],
}


LEVEL12_MODULE03_QUIZ = {}

for i, lesson_code in enumerate(
    ["L12_M03_001", "L12_M03_002", "L12_M03_003", "L12_M03_004", "L12_M03_005"]
):
    start = 31 + i * 3

    LEVEL12_MODULE03_QUIZ[lesson_code] = [
        {
            "code": f"L12_Q{start:03d}",
            "question": "Schedule model elementlarini jadvalda ko'rsatishi mumkinmi?",
            "explanation": "BIM element data jadvalga chiqarilishi mumkin.",
            "options": [("A", "Ha", True), ("B", "Yo'q", False)],
        },
        {
            "code": f"L12_Q{start + 1:03d}",
            "question": "Schedule orqali model xatolarini topish mumkinmi?",
            "explanation": "Data inconsistency va boshqa muammolar ko'rinishi mumkin.",
            "options": [("A", "Ha", True), ("B", "Yo'q", False)],
        },
        {
            "code": f"L12_Q{start + 2:03d}",
            "question": "Schedule kriteriyasini tekshirmasdan undagi miqdorga ko'r-ko'rona ishonish to'g'rimi?",
            "explanation": "Criteria va model holati tekshirilishi kerak.",
            "options": [("A", "Ha", False), ("B", "Yo'q", True)],
        },
    ]


def seed_level12_module03():
    connection = get_connection()
    try:
        cursor = connection.cursor()

        for row in LEVEL12_MODULE03_LESSONS:
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
