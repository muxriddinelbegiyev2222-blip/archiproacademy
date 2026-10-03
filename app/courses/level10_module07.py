from database.database import get_connection


LEVEL10_MODULE07_LESSONS = [
    ("L10_M07", "L10_M07_001", "Fasad konsepsiyasi", "theory", "Bir qavatli uy fasadini plan va hajm bilan bog'lash.", 1, 60, 20),
    ("L10_M07", "L10_M07_002", "Proporsiya va ritm", "theory", "Fasaddagi elementlar nisbatini va vizual tartibni boshqarish.", 2, 70, 20),
    ("L10_M07", "L10_M07_003", "Ochilishlar va kirish aksenti", "practice", "Deraza, eshik va asosiy kirishni fasad kompozitsiyasiga integratsiya qilish.", 3, 70, 20),
    ("L10_M07", "L10_M07_004", "Material va hajm", "practice", "Materiallar va hajm bo'linishini sodda va izchil ishlatish.", 4, 75, 20),
    ("L10_M07", "L10_M07_005", "Fasad professional audit", "practice", "To'rt fasadni plan, tom va umumiy konsepsiya bilan tekshirish.", 5, 85, 25),
]


LEVEL10_MODULE07_CONTENT = {
    "L10_M07_001": [
        {"title": "Fasad plan natijasi ham", "type": "highlight", "text": "Deraza, eshik va hajm ichki plan bilan bog'langan holda shakllanadi."},
        {"title": "Konsepsiya", "type": "normal", "text": "Fasadga bitta umumiy g'oya kerak: sokin, ritmik, kontrastli, gorizontal yoki boshqa boshqariladigan kompozitsiya."},
        {"title": "Xato", "type": "warning", "text": "Har bir joyga tasodifiy dekor qo'shish professional fasad yaratmaydi."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Uy fasadi uchun 3 ta kalit so'zdan iborat konsepsiya yozing."},
    ],
    "L10_M07_002": [
        {"title": "Proporsiya", "type": "highlight", "text": "Deraza, devor massasi, kirish va tom qismlari o'zaro nisbatda ko'riladi."},
        {"title": "Ritm", "type": "normal", "text": "Ochilishlar takrorlanishi fasadga tartib berishi mumkin."},
        {"title": "Hamma narsa teng emas", "type": "warning", "text": "Har elementga bir xil vizual urg'u berish fasadni tartibsiz qilishi mumkin."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Fasadda dominant, secondary va background elementlarni belgilang."},
    ],
    "L10_M07_003": [
        {"title": "Asosiy kirish", "type": "highlight", "text": "Kirish fasadda oson topiladigan va umumiy kompozitsiyaga mos bo'lishi kerak."},
        {"title": "Derazalar", "type": "normal", "text": "Deraza joyi xona funksiyasi va fasad ritmini birga qondiradi."},
        {"title": "Faqat tashqi ko'rinish uchun", "type": "warning", "text": "Ichki funksiyani buzib faqat fasad uchun derazani ko'chirish ehtiyotkorlik bilan bajariladi."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Asosiy fasaddagi kirish va ochilishlarni vizual hierarxiya bo'yicha tahlil qiling."},
    ],
    "L10_M07_004": [
        {"title": "Materiallar soni", "type": "highlight", "text": "Ko'p material avtomatik ravishda premium fasad yaratmaydi."},
        {"title": "Material + hajm", "type": "normal", "text": "Material o'zgarishi hajm, kirish yoki kompozitsion mantiq bilan bog'liq bo'lsa kuchliroq ishlaydi."},
        {"title": "Dekor ortig'i", "type": "warning", "text": "Mantiqsiz ko'p tekstura va bezak fasadni vizual shovqinli qilishi mumkin."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Fasad materiallarini primary / secondary / accent guruhlariga ajrating."},
    ],
    "L10_M07_005": [
        {"title": "Fasad audit", "type": "highlight", "text": "Plan → openings → massing → proportion → rhythm → entry → material → roof → 4 elevations."},
        {"title": "Professional checklist", "type": "example", "text": "1. Plan bilan mosmi?<br><br>2. Kirish aniqmi?<br><br>3. Derazalar ritmi bormi?<br><br>4. Proporsiyalar nazoratdami?<br><br>5. Material mantiqi bormi?<br><br>6. Tom fasadga mosmi?<br><br>7. Yon va orqa fasad ham ishlab chiqilganmi?"},
        {"title": "4 tomon", "type": "warning", "text": "Faqat ko'chaga qaragan fasadni loyihalab, boshqa tomonlarni tasodifiy qoldirmang."},
        {"title": "Keyingi modul", "type": "highlight", "text": "Keyingi bosqich: TOM."},
    ],
}


LEVEL10_MODULE07_QUIZ = {
    "L10_M07_001": [
        {"code": "L10_Q091", "question": "Fasad plan bilan bog'liqmi?", "explanation": "Ochilishlar va hajm ichki funksiyadan keladi.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
        {"code": "L10_Q092", "question": "Fasad konsepsiyasi foydalimi?", "explanation": "Kompozitsiyani izchil boshqarishga yordam beradi.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
        {"code": "L10_Q093", "question": "Tasodifiy dekor ko'paytirish professional fasadning asosiy usulimi?", "explanation": "Mantiq va kompozitsiya muhim.", "options": [("A", "Ha", False), ("B", "Yo'q", True)]},
    ],
    "L10_M07_002": [
        {"code": "L10_Q094", "question": "Proporsiya fasad sifatiga ta'sir qiladimi?", "explanation": "Elementlar nisbatini boshqaradi.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
        {"code": "L10_Q095", "question": "Ritm fasadga tartib bera oladimi?", "explanation": "Takrorlanish vizual struktura yaratadi.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
        {"code": "L10_Q096", "question": "Har element bir xil vizual dominant bo'lishi kerakmi?", "explanation": "Hierarxiya kompozitsiyani kuchaytiradi.", "options": [("A", "Ha", False), ("B", "Yo'q", True)]},
    ],
    "L10_M07_003": [
        {"code": "L10_Q097", "question": "Asosiy kirish fasadda oson o'qilishi foydalimi?", "explanation": "Foydalanuvchi orientatsiyasiga yordam beradi.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
        {"code": "L10_Q098", "question": "Deraza faqat fasad kompozitsiyasi uchun xizmat qiladimi?", "explanation": "Ichki xona funksiyasi ham muhim.", "options": [("A", "Ha", False), ("B", "Yo'q", True)]},
        {"code": "L10_Q099", "question": "Ochilishlar plan va fasad orasida koordinatsiya qilinadimi?", "explanation": "Bir xil elementlar turli ko'rinishlarda mos bo'lishi kerak.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
    ],
    "L10_M07_004": [
        {"code": "L10_Q100", "question": "Ko'p material har doim yaxshi fasad deganimi?", "explanation": "Materiallar sonidan ko'ra ularning mantiqi muhim.", "options": [("A", "Ha", False), ("B", "Yo'q", True)]},
        {"code": "L10_Q101", "question": "Material o'zgarishini hajm bilan bog'lash foydalimi?", "explanation": "Bu kompozitsion mantiq yaratishi mumkin.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
        {"code": "L10_Q102", "question": "Accent material maqsadli joyda ishlatilishi kerakmi?", "explanation": "Vizual hierarxiyani kuchaytiradi.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
    ],
    "L10_M07_005": [
        {"code": "L10_Q103", "question": "Fasad auditida tom ham tekshiriladimi?", "explanation": "Tom binoning umumiy siluetiga ta'sir qiladi.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
        {"code": "L10_Q104", "question": "Faqat old fasadni ishlab chiqish yetarlimi?", "explanation": "Barcha tomonlar yagona bino sifatida ishlaydi.", "options": [("A", "Ha", False), ("B", "Yo'q", True)]},
        {"code": "L10_Q105", "question": "Fasad workflow'i qaysi?", "explanation": "Plan va massing asosida proporsiya, ritm, kirish va materiallar ishlanadi.", "options": [("A", "Plan → massing → openings → proportion/rhythm → material → audit", True), ("B", "Tasodifiy dekor → final", False)]},
    ],
}


def seed_level10_module07():
    connection = get_connection()
    try:
        cursor = connection.cursor()

        for row in LEVEL10_MODULE07_LESSONS:
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
