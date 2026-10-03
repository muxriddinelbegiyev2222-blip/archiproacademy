from database.database import get_connection


LEVEL09_MODULE07_LESSONS = [
    ("L09_M07", "L09_M07_001", "Accessibility tushunchasi", "theory", "Turli foydalanuvchilar uchun muhitdan mustaqil va xavfsiz foydalanish prinsiplarini tushunish.", 1, 30, 20),
    ("L09_M07", "L09_M07_002", "Kirish va harakat zanjiri", "theory", "Uchastkadan bino ichigacha uzluksiz foydalanish yo'lini tahlil qilish.", 2, 35, 20),
    ("L09_M07", "L09_M07_003", "Eshik, sath va vertikal aloqa", "practice", "Kirishlar, sath farqlari va qavatlararo harakatni accessibility nuqtai nazaridan ko'rish.", 3, 35, 20),
    ("L09_M07", "L09_M07_004", "Sanitar va foydalanish zonalari", "practice", "Asosiy foydalanish va sanitar zonalarni accessibility savollari bilan tekshirish.", 4, 40, 20),
    ("L09_M07", "L09_M07_005", "Accessibility professional audit", "practice", "Loyihani uzluksiz foydalanish zanjiri asosida kompleks tekshirish.", 5, 40, 25),
]


LEVEL09_MODULE07_CONTENT = {
    "L09_M07_001": [
        {"title": "Accessibility kim uchun?", "type": "highlight", "text": "Accessibility turli harakat, ko'rish va boshqa ehtiyojlarga ega foydalanuvchilarning muhitdan foydalanishini hisobga oladi."},
        {"title": "Faqat rampa emas", "type": "warning", "text": "Bino oldiga rampa qo'yishning o'zi accessibility masalasini to'liq hal qilmaydi."},
        {"title": "Uzluksiz foydalanish", "type": "normal", "text": "Foydalanuvchi uchastkadan asosiy funksional zonalargacha uzluksiz va xavfsiz harakat qila olishi kerak."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Uchastka kirishidan asosiy xonagacha bo'lgan foydalanuvchi yo'lini yozing."},
    ],

    "L09_M07_002": [
        {"title": "Accessibility chain", "type": "highlight", "text": "Ko'cha/uchastka → kirish yo'li → bino eshigi → hall → circulation → asosiy xona → kerakli xizmat zonasi."},
        {"title": "Bitta uzilish yetadi", "type": "warning", "text": "Yo'lning bitta joyida to'siq paydo bo'lsa butun foydalanish zanjiri buzilishi mumkin."},
        {"title": "Nazorat nuqtalari", "type": "normal", "text": "Har bir transition, eshik, burilish, sath farqi va asosiy xizmat nuqtasi alohida tekshiriladi."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Accessibility chain uchun 8 ta nazorat nuqtasini yozing."},
    ],

    "L09_M07_003": [
        {"title": "Sath farqi", "type": "highlight", "text": "Sath farqi foydalanuvchining mustaqil harakatiga ta'sir qilishi mumkin."},
        {"title": "Eshik", "type": "normal", "text": "Eshikning joylashuvi, ochilishi, threshold va yondashuv zonasi foydalanish bilan bog'liq."},
        {"title": "Aniq o'lcham", "type": "warning", "text": "Accessibility bo'yicha aniq o'lchamlar amaldagi tegishli normativdan tekshiriladi."},
        {"title": "Vertikal aloqa", "type": "normal", "text": "Bir necha qavatli binoda qavatlararo foydalanish zanjiri ham alohida ko'riladi."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Kirish eshigi va bitta ichki eshik uchun foydalanish ssenariysi yozing."},
    ],

    "L09_M07_004": [
        {"title": "Sanitar zona", "type": "highlight", "text": "Sanitar xonada faqat jihozlarni sig'dirish emas, foydalanish imkoniyati ham tahlil qilinadi."},
        {"title": "Yondashuv", "type": "normal", "text": "Jihozga yaqinlashish, burilish, o'tish va undan foydalanish ketma-ketligi ko'riladi."},
        {"title": "Faqat plan belgisi emas", "type": "warning", "text": "Sanitar jihozni plan ichiga chizish accessibility talabini avtomatik bajarmaydi."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Sanuzel uchun 6 ta accessibility audit savolini yozing."},
    ],

    "L09_M07_005": [
        {"title": "Accessibility audit", "type": "highlight", "text": "Uchastka kirishi → bino kirishi → sathlar → eshiklar → circulation → asosiy funksiya → sanitar zona → normativ tekshiruv."},
        {"title": "Status", "type": "normal", "text": "MOS / TEKSHIRISH KERAK / MOS EMAS kabi statuslar auditni boshqarishga yordam beradi."},
        {"title": "Bitta element yetmaydi", "type": "warning", "text": "Bitta mos element butun foydalanish zanjiri accessibility talabiga mos degani emas."},
        {"title": "Professional checklist", "type": "example", "text": "1. Uchastka kirishi tekshirildimi?<br><br>2. Bino kirishi ishlaydimi?<br><br>3. Sath farqlari ko'rildimi?<br><br>4. Eshiklar tekshirildimi?<br><br>5. Circulation uzluksizmi?<br><br>6. Asosiy funksiyalar accessiblemi?<br><br>7. Sanitar zona tekshirildimi?<br><br>8. Normativ manba qayd qilinganmi?"},
    ],
}


LEVEL09_MODULE07_QUIZ = {
    "L09_M07_001": [
        {"code": "L09_Q091", "question": "Accessibility faqat rampa masalasidan iboratmi?", "explanation": "Accessibility butun foydalanish zanjirini qamrab oladi.", "options": [("A", "Ha", False), ("B", "Yo'q", True)]},
        {"code": "L09_Q092", "question": "Turli foydalanuvchi ehtiyojlarini hisobga olish accessibility'ning bir qismimi?", "explanation": "Muhit turli foydalanuvchilar uchun ishlashi ko'rib chiqiladi.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
        {"code": "L09_Q093", "question": "Uchastkadan xonagacha uzluksiz foydalanish yo'li muhimmi?", "explanation": "Accessibility zanjiri faqat bitta element bilan tugamaydi.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
    ],
    "L09_M07_002": [
        {"code": "L09_Q094", "question": "Accessibility chain'dagi bitta to'siq butun yo'lga ta'sir qilishi mumkinmi?", "explanation": "Uzluksizlik accessibility'ning asosiy tamoyillaridan biridir.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
        {"code": "L09_Q095", "question": "Bino eshigigacha yetib borish ham accessibility auditiga kiradimi?", "explanation": "Uchastka va bino kirishi bir zanjirda ko'riladi.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
        {"code": "L09_Q096", "question": "Faqat ichki xonalarni tekshirish har doim yetarlimi?", "explanation": "Tashqi kirish va transitionlar ham tekshiriladi.", "options": [("A", "Ha", False), ("B", "Yo'q", True)]},
    ],
    "L09_M07_003": [
        {"code": "L09_Q097", "question": "Sath farqi accessibility'ga ta'sir qilishi mumkinmi?", "explanation": "Sath farqi mustaqil harakatni qiyinlashtirishi mumkin.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
        {"code": "L09_Q098", "question": "Eshikning ochilish holati foydalanishga ta'sir qilishi mumkinmi?", "explanation": "Eshik va yondashuv zonasi birgalikda ko'riladi.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
        {"code": "L09_Q099", "question": "Accessibility bo'yicha aniq o'lchamlarni normativdan tekshirish kerakmi?", "explanation": "Aniq qiymatlar amaldagi tegishli hujjatga asoslanadi.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
    ],
    "L09_M07_004": [
        {"code": "L09_Q100", "question": "Sanitar xonada jihozning faqat plan ichiga sig'ishi yetarlimi?", "explanation": "Foydalanish va yondashuv zonasi ham muhim.", "options": [("A", "Ha", False), ("B", "Yo'q", True)]},
        {"code": "L09_Q101", "question": "Sanitar jihozga yondashuv tekshiriladimi?", "explanation": "Accessibility real foydalanish imkoniyatini baholaydi.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
        {"code": "L09_Q102", "question": "Manevr va circulation zonalari accessibility bilan bog'liqmi?", "explanation": "Harakat uchun yetarli va to'siqsiz zona muhim bo'lishi mumkin.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
    ],
    "L09_M07_005": [
        {"code": "L09_Q103", "question": "Accessibility auditida uchastka kirishidan boshlash mumkinmi?", "explanation": "Audit to'liq foydalanish zanjirini ko'radi.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
        {"code": "L09_Q104", "question": "Bitta accessibility elementi mos bo'lsa butun bino avtomatik mosmi?", "explanation": "Barcha kerakli nazorat nuqtalari tekshirilishi kerak.", "options": [("A", "Ha", False), ("B", "Yo'q", True)]},
        {"code": "L09_Q105", "question": "Accessibility auditining to'g'ri workflow'i qaysi?", "explanation": "Tashqi kirishdan asosiy funksiyalar va sanitar zonagacha uzluksiz zanjir tekshiriladi.", "options": [("A", "Uchastka → bino kirishi → sath/eshik → circulation → funksiya → sanitar zona → normativ audit", True), ("B", "Faqat rampa → yakunlash", False)]},
    ],
}


def seed_level09_module07():
    connection = get_connection()
    try:
        cursor = connection.cursor()

        for (
            module_code,
            lesson_code,
            title,
            lesson_type,
            summary,
            sort_order,
            estimated_minutes,
            xp_reward,
        ) in LEVEL09_MODULE07_LESSONS:

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
                    module["id"],
                    lesson_code,
                    title,
                    lesson_type,
                    summary,
                    sort_order,
                    estimated_minutes,
                    xp_reward,
                    80,
                    1,
                ),
            )

        connection.commit()
    finally:
        connection.close()
