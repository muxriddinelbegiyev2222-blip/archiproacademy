from database.database import get_connection


LEVEL14_MODULE07_LESSONS = [
    ("L14_M07", "L14_M07_001", "Design Clinic metodikasi", "theory", "Tayyor yoki yarim tayyor loyihani professional diagnostika qilish.", 1, 80, 20),
    ("L14_M07", "L14_M07_002", "Plan diagnostikasi", "practice", "Funksiya, ergonomika va circulation muammolarini topish.", 2, 90, 20),
    ("L14_M07", "L14_M07_003", "Fasad va massing diagnostikasi", "practice", "Proporsiya, opening va kompozitsion muammolarni aniqlash.", 3, 95, 20),
    ("L14_M07", "L14_M07_004", "BIM va texnik diagnostika", "practice", "Model, konstruktsiya, MEP va hujjat konfliktlarini topish.", 4, 100, 20),
    ("L14_M07", "L14_M07_005", "Design Clinic final audit", "practice", "Muammoni topishdan yaxshilangan variantgacha bo'lgan jarayonni bajarish.", 5, 115, 25),
]


LEVEL14_MODULE07_CONTENT = {
    "L14_M07_001": [
        {"title": "Dizaynni davolash", "type": "highlight", "text": "Design Clinic — loyihani 'yoqdi/yoqmadi' deb baholash emas, muammoni aniqlash va sababini topish."},
        {"title": "4 savol", "type": "normal", "text": "Nima ishlamayapti? Nega? Ta'siri nima? Qanday yaxshilash mumkin?"},
        {"title": "Xato", "type": "warning", "text": "Muammo sababini tushunmasdan faqat elementlarni ko'chirish bilan cheklanib qolmang."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Bir eski loyihangiz uchun 10 ta diagnostic savol yozing."},
    ],
    "L14_M07_002": [
        {"title": "Plan clinic", "type": "highlight", "text": "Zonalar, room proportions, furniture, doors, circulation, privacy va dead space tekshiriladi."},
        {"title": "Symptom vs cause", "type": "normal", "text": "Uzun koridor simptom bo'lishi mumkin; asl sabab noto'g'ri zoning bo'lishi mumkin."},
        {"title": "Kosmetik tuzatish", "type": "warning", "text": "Asosiy funksional muammoni dekor bilan yashirmang."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Plan ichidan 5 symptom va ularning root cause'ini toping."},
    ],
    "L14_M07_003": [
        {"title": "Facade clinic", "type": "highlight", "text": "Massing, proportion, openings, entry, material va roof birgalikda tekshiriladi."},
        {"title": "Root cause", "type": "normal", "text": "Tartibsiz fasad muammosi aslida ichki plandagi opening joylashuvidan kelayotgan bo'lishi mumkin."},
        {"title": "Faqat materialni almashtirmang", "type": "warning", "text": "Kompozitsion muammoni faqat rang va tekstura bilan hal qilish har doim ishlamaydi."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Bir fasad uchun 5 root-cause tahlil yozing."},
    ],
    "L14_M07_004": [
        {"title": "Technical clinic", "type": "highlight", "text": "Stories, structure, stair, roof, MEP, shafts, openings va BIM consistency tekshiriladi."},
        {"title": "Cross-view", "type": "normal", "text": "Plan, section, elevation va 3D bir-biriga qarshi ma'lumot bermasligi kerak."},
        {"title": "Xato", "type": "warning", "text": "Grafik chiroyli bo'lsa texnik konflikt yo'q deb o'ylamang."},
        {"title": "Mini-amaliyot", "type": "example", "text": "15 bandli BIM/technical audit bajaring."},
    ],
    "L14_M07_005": [
        {"title": "Clinic workflow", "type": "highlight", "text": "Observe → identify symptom → find root cause → prioritize → propose alternatives → test → compare → fix → audit."},
        {"title": "Professional checklist", "type": "example", "text": "1. Muammo aniqmi?<br><br>2. Root cause topildimi?<br><br>3. Ta'siri tushunildimi?<br><br>4. Priority aniqmi?<br><br>5. Bir nechta yechim ko'rildimi?<br><br>6. Yangi konflikt yaratilmadimi?<br><br>7. Final variant qayta audit qilindimi?"},
        {"title": "Keyingi modul", "type": "highlight", "text": "Keyingi modul: ADVANCED CASE STUDIES."},
    ],
}


LEVEL14_MODULE07_QUIZ = {}

for i, lesson_code in enumerate(
    ["L14_M07_001", "L14_M07_002", "L14_M07_003", "L14_M07_004", "L14_M07_005"]
):
    start = 91 + i * 3

    LEVEL14_MODULE07_QUIZ[lesson_code] = [
        {
            "code": f"L14_Q{start:03d}",
            "question": "Design Clinic muammoning root cause'ini topishga qaratiladimi?",
            "explanation": "Faqat simptomni emas, sababni aniqlash kerak.",
            "options": [("A", "Ha", True), ("B", "Yo'q", False)],
        },
        {
            "code": f"L14_Q{start + 1:03d}",
            "question": "Funksional muammoni faqat dekor bilan yashirish professional yechimmi?",
            "explanation": "Asosiy sabab hal qilinishi kerak.",
            "options": [("A", "Ha", False), ("B", "Yo'q", True)],
        },
        {
            "code": f"L14_Q{start + 2:03d}",
            "question": "Fix kiritilgandan keyin loyiha qayta audit qilinadimi?",
            "explanation": "Yangi konflikt paydo bo'lmaganini tekshirish kerak.",
            "options": [("A", "Ha", True), ("B", "Yo'q", False)],
        },
    ]


def seed_level14_module07():
    connection = get_connection()
    try:
        cursor = connection.cursor()

        for row in LEVEL14_MODULE07_LESSONS:
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
