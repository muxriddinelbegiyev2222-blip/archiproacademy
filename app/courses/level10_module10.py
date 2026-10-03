from database.database import get_connection


LEVEL10_MODULE10_LESSONS = [
    ("L10_M10", "L10_M10_001", "Final genplan strategiyasi", "theory", "Uy va uchastkani yagona loyiha sifatida yakunlash.", 1, 60, 20),
    ("L10_M10", "L10_M10_002", "Piyoda va avtomobil harakati", "practice", "Uchastkadagi kirish va harakat yo'llarini professional tashkil qilish.", 2, 70, 20),
    ("L10_M10", "L10_M10_003", "Hovli va tashqi funksiyalar", "practice", "Dam olish, BBQ, xizmat va yashil zonalarni joylashtirish.", 3, 70, 20),
    ("L10_M10", "L10_M10_004", "Sath, drenaj va tashqi koordinatsiya", "practice", "Relyef, suv va tashqi muhandislik aloqalarini tekshirish.", 4, 75, 20),
    ("L10_M10", "L10_M10_005", "Genplan professional audit", "practice", "Bir qavatli uy final genplanini kompleks tekshirish.", 5, 85, 25),
]


LEVEL10_MODULE10_CONTENT = {
    "L10_M10_001": [
        {"title": "Uy + hovli = bitta loyiha", "type": "highlight", "text": "Final genplan bino va uchastkaning barcha asosiy funksiyalarini yagona tizimda ko'rsatadi."},
        {"title": "Bazalar", "type": "normal", "text": "Site Analysis, final plan, tashqi kirish va hovli ehtiyojlari genplan uchun asos."},
        {"title": "Xato", "type": "warning", "text": "Uyni ideal qilib, hovlini qolgan bo'sh joyga tasodifiy joylashtirmang."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Final genplandagi barcha asosiy funksiyalar ro'yxatini tuzing."},
    ],
    "L10_M10_002": [
        {"title": "Harakat", "type": "highlight", "text": "Piyoda va avtomobil harakati xavfsiz va sodda bo'lishi kerak."},
        {"title": "Kirishlar", "type": "normal", "text": "Main entry, car entry, service access va guest movement kerak bo'lsa alohida ko'riladi."},
        {"title": "Conflict", "type": "warning", "text": "Avtomobil yo'li asosiy piyoda va dam olish zonasini keraksiz kesib o'tmasligi kerak."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Piyoda va car circulation'ni turli strelkalar bilan belgilang."},
    ],
    "L10_M10_003": [
        {"title": "Hovli zonalari", "type": "highlight", "text": "Dam olish, BBQ, bolalar, xo'jalik, parking va yashil zona bir-biriga ta'sir qiladi."},
        {"title": "Public-private outdoor", "type": "normal", "text": "Mehmonlar uchun tashqi zona va private oilaviy zona farqlanishi mumkin."},
        {"title": "Shovqin va hid", "type": "warning", "text": "BBQ, texnik yoki service zonalarini yotoqxona va tinch hududlar bilan ehtiyotkorlik bilan joylashtiring."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Tashqi funksiyalarni public/private/service guruhlariga ajrating."},
    ],
    "L10_M10_004": [
        {"title": "Sath", "type": "highlight", "text": "Uy 0.000 sathi va uchastka relyefi o'zaro bog'langan."},
        {"title": "Drenaj", "type": "normal", "text": "Yomg'ir suvi binoga yoki kirishga qarab emas, xavfsiz yo'nalishda boshqariladi."},
        {"title": "Tarmoqlar", "type": "normal", "text": "Tashqi MEP kirishlari genplan bilan koordinatsiya qilinadi."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Genplanda suv harakati va asosiy tashqi tarmoq kirishlarini belgilang."},
    ],
    "L10_M10_005": [
        {"title": "Genplan audit", "type": "highlight", "text": "Site data → building → access → circulation → outdoor zones → levels → drainage → services → landscape → audit."},
        {"title": "Professional checklist", "type": "example", "text": "1. Chegaralar aniqmi?<br><br>2. Uy joylashuvi finalmi?<br><br>3. Piyoda/car kirishlar ishlaydimi?<br><br>4. Hovli zonalari mantiqiymi?<br><br>5. Private/public tashqi zona ajratilganmi?<br><br>6. Relyef ko'rilganmi?<br><br>7. Drainage mantiqi bormi?<br><br>8. Tarmoqlar koordinatsiya qilinganmi?<br><br>9. Plan bilan mosmi?"},
        {"title": "Xato", "type": "warning", "text": "Genplan faqat chiroyli landshaft chizmasi emas. U real ishlaydigan uchastka tizimi."},
        {"title": "Keyingi modul", "type": "highlight", "text": "Keyingi bosqich: LOYIHA ALBOMI."},
    ],
}


LEVEL10_MODULE10_QUIZ = {
    "L10_M10_001": [
        {"code": "L10_Q136", "question": "Final genplan bino va uchastkani birgalikda ko'rsatadimi?", "explanation": "Uy tashqi makondan alohida emas.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
        {"code": "L10_Q137", "question": "Hovlini faqat qolgan bo'sh joyga joylashtirish idealmi?", "explanation": "Tashqi funksiyalar ham oldindan rejalashtiriladi.", "options": [("A", "Ha", False), ("B", "Yo'q", True)]},
        {"code": "L10_Q138", "question": "Site Analysis genplan uchun baza bo'ladimi?", "explanation": "Uchastka sharoiti asosiy ma'lumot beradi.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
    ],
    "L10_M10_002": [
        {"code": "L10_Q139", "question": "Piyoda va avtomobil circulation alohida tekshirilishi mumkinmi?", "explanation": "Xavfsiz va qulay harakat uchun foydali.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
        {"code": "L10_Q140", "question": "Car yo'li dam olish zonasini keraksiz kesib o'tishi yaxshi yechimmi?", "explanation": "Conflict va xavf yaratishi mumkin.", "options": [("A", "Ha", False), ("B", "Yo'q", True)]},
        {"code": "L10_Q141", "question": "Service access alohida ko'rib chiqilishi mumkinmi?", "explanation": "Funksional talablarga qarab.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
    ],
    "L10_M10_003": [
        {"code": "L10_Q142", "question": "BBQ va yotoqxona aloqasi shovqin/hid nuqtai nazaridan tekshiriladimi?", "explanation": "Tashqi funksiyalar ichki qulaylikka ta'sir qiladi.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
        {"code": "L10_Q143", "question": "Public va private outdoor zonalar ajratilishi mumkinmi?", "explanation": "Foydalanish ssenariysiga bog'liq.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
        {"code": "L10_Q144", "question": "Tashqi zonalash ham bubble mantiqida tahlil qilinishi mumkinmi?", "explanation": "Funksiyalar orasidagi aloqa foydali.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
    ],
    "L10_M10_004": [
        {"code": "L10_Q145", "question": "Bino 0.000 sathi relyef bilan bog'liqmi?", "explanation": "Kirish va suv yo'liga ta'sir qiladi.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
        {"code": "L10_Q146", "question": "Yomg'ir suvini bino tomon yo'naltirish yaxshi yechimmi?", "explanation": "Suv binodan xavfsiz uzoqlashtiriladi.", "options": [("A", "Ha", False), ("B", "Yo'q", True)]},
        {"code": "L10_Q147", "question": "Tashqi MEP kirishlari genplan bilan koordinatsiya qilinadimi?", "explanation": "Tarmoqlar uchastka geometriyasiga bog'liq.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
    ],
    "L10_M10_005": [
        {"code": "L10_Q148", "question": "Genplan auditida drainage tekshiriladimi?", "explanation": "Suv boshqaruvi uchastka dizaynining bir qismi.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
        {"code": "L10_Q149", "question": "Genplan faqat dekorativ landscape chizmasimi?", "explanation": "U real funksional uchastka tizimini ko'rsatadi.", "options": [("A", "Ha", False), ("B", "Yo'q", True)]},
        {"code": "L10_Q150", "question": "Genplan workflow'i qaysi?", "explanation": "Bino, harakat, zonalar, sath va tarmoqlar yagona tizim sifatida tekshiriladi.", "options": [("A", "Site → building → access → zones → levels/drainage → services → audit", True), ("B", "Faqat daraxt chizish → final", False)]},
    ],
}


def seed_level10_module10():
    connection = get_connection()
    try:
        cursor = connection.cursor()

        for row in LEVEL10_MODULE10_LESSONS:
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
