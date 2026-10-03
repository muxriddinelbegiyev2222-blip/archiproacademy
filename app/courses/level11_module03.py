from database.database import get_connection


LEVEL11_MODULE03_LESSONS = [
    ("L11_M03", "L11_M03_001", "Zinapoya geometriyasi", "theory", "Zinapoyaning asosiy geometrik va fazoviy mantig'ini tushunish.", 1, 70, 20),
    ("L11_M03", "L11_M03_002", "Rise, tread va flight mantig'i", "theory", "Zinapoya elementlarini qulay foydalanish nuqtai nazaridan tushunish.", 2, 80, 20),
    ("L11_M03", "L11_M03_003", "Landing, headroom va opening", "practice", "Zinapoya bo'shlig'ini vertikal koordinatsiya qilish.", 3, 85, 20),
    ("L11_M03", "L11_M03_004", "Zinapoya va arxitektura", "practice", "Zinapoyani plan, void, fasad va interyer bilan integratsiya qilish.", 4, 90, 20),
    ("L11_M03", "L11_M03_005", "Zinapoya PRO audit", "practice", "Zinapoya modelini plan, kesim va 3D orqali kompleks tekshirish.", 5, 95, 25),
]


LEVEL11_MODULE03_CONTENT = {
    "L11_M03_001": [
        {"title": "Zinapoya — 3D obyekt", "type": "highlight", "text": "Zinapoyani faqat plan ko'rinishidagi chiziqlar sifatida tushunmang."},
        {"title": "Bog'langan", "type": "normal", "text": "Qavat balandligi, opening, landing, railing va konstruktsiya bir tizim."},
        {"title": "Aniq o'lcham", "type": "warning", "text": "Aniq riser, tread va boshqa talablar amaldagi tegishli normativdan tekshiriladi."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Zinapoyaning asosiy elementlarini yozing."},
    ],
    "L11_M03_002": [
        {"title": "Riser + tread", "type": "highlight", "text": "Zinapoya qulayligi vertikal va gorizontal qadam geometriyasining uyg'unligiga bog'liq."},
        {"title": "Bir xil qadam", "type": "normal", "text": "Flight ichida ritm va izchillik foydalanuvchi xavfsizligi uchun muhim."},
        {"title": "Taxmin", "type": "warning", "text": "Qavat balandligi bilan hisoblashni tekshirmasdan tasodifiy step soni qo'ymang."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Qavat balandligi o'zgarsa zinapoya geometriyasiga nima ta'sir qilishini yozing."},
    ],
    "L11_M03_003": [
        {"title": "Landing", "type": "normal", "text": "Yo'nalish o'zgarishi va dam olish nuqtasi sifatida ishlashi mumkin."},
        {"title": "Headroom", "type": "highlight", "text": "Foydalanuvchi zinapoyadan o'tayotganda yuqori konstruktsiya bilan konflikt bo'lmasligi kerak."},
        {"title": "Opening", "type": "normal", "text": "Slab opening zinapoya geometriyasi bilan aniq koordinatsiya qilinadi."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Section orqali stair opening va headroom konfliktini tekshiring."},
    ],
    "L11_M03_004": [
        {"title": "Arxitektura elementi", "type": "highlight", "text": "Zinapoya ichki makon kompozitsiyasining kuchli elementi bo'lishi mumkin."},
        {"title": "Void", "type": "normal", "text": "Zinapoya ikkinchi yorug'lik yoki double-height space bilan integratsiya qilinishi mumkin."},
        {"title": "Fasad", "type": "normal", "text": "Stair window fasadga vertikal ritm yoki aksent berishi mumkin."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Bitta zinapoya uchun plan, section va facade aloqasini tekshiring."},
    ],
    "L11_M03_005": [
        {"title": "Stair audit", "type": "highlight", "text": "Levels → geometry → flight → landing → opening → headroom → railing → structure → 3D audit."},
        {"title": "Professional checklist", "type": "example", "text": "1. Qavat balandligi to'g'rimi?<br><br>2. Step geometriyasi tekshirildimi?<br><br>3. Landing ishlaydimi?<br><br>4. Opening mosmi?<br><br>5. Headroom tekshirildimi?<br><br>6. Railing bormi?<br><br>7. Konstruktiv konflikt yo'qmi?<br><br>8. Plan/section/3D mosmi?"},
        {"title": "Keyingi modul", "type": "highlight", "text": "Keyingi modul: VERTIKAL KOMMUNIKATSIYALAR."},
    ],
}


LEVEL11_MODULE03_QUIZ = {}

for i, lesson_code in enumerate(
    ["L11_M03_001", "L11_M03_002", "L11_M03_003", "L11_M03_004", "L11_M03_005"]
):
    start = 31 + i * 3

    LEVEL11_MODULE03_QUIZ[lesson_code] = [
        {
            "code": f"L11_Q{start:03d}",
            "question": "Zinapoya qavat balandligi bilan koordinatsiya qilinadimi?",
            "explanation": "Zinapoya geometriyasi vertikal balandlikka bog'liq.",
            "options": [("A", "Ha", True), ("B", "Yo'q", False)],
        },
        {
            "code": f"L11_Q{start + 1:03d}",
            "question": "Zinapoyani faqat plan ko'rinishida tekshirish yetarlimi?",
            "explanation": "Section va 3D vertikal konfliktlarni ko'rsatadi.",
            "options": [("A", "Ha", False), ("B", "Yo'q", True)],
        },
        {
            "code": f"L11_Q{start + 2:03d}",
            "question": "Stair opening va headroom tekshirilishi kerakmi?",
            "explanation": "Xavfsiz va real foydalanish uchun muhim.",
            "options": [("A", "Ha", True), ("B", "Yo'q", False)],
        },
    ]


def seed_level11_module03():
    connection = get_connection()
    try:
        cursor = connection.cursor()

        for row in LEVEL11_MODULE03_LESSONS:
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
