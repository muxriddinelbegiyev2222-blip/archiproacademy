from database.database import get_connection


LEVEL10_MODULE04_LESSONS = [
    ("L10_M04", "L10_M04_001", "Bubble'dan planga o'tish", "theory", "Funksional sxemani real xona geometriyasiga aylantirish.", 1, 60, 20),
    ("L10_M04", "L10_M04_002", "Xona proporsiyasi va mebel", "practice", "Xona shaklini real foydalanish bilan tekshirish.", 2, 70, 20),
    ("L10_M04", "L10_M04_003", "Devor, eshik va circulation", "practice", "Eskiz planda harakat va ochilishlarni koordinatsiya qilish.", 3, 70, 20),
    ("L10_M04", "L10_M04_004", "Fasad va hovli bilan aloqa", "practice", "Plan qarorini tashqi makon va fasad bilan bog'lash.", 4, 75, 20),
    ("L10_M04", "L10_M04_005", "Eskiz plan professional audit", "practice", "Eskiz plan funksiyasi va geometriyasini kompleks tekshirish.", 5, 85, 25),
]


LEVEL10_MODULE04_CONTENT = {
    "L10_M04_001": [
        {"title": "Bubble endi geometriyaga aylanadi", "type": "highlight", "text": "Eskiz plan bosqichida funksional bloklar real devor va xona shakliga aylantiriladi."},
        {"title": "Maqsad", "type": "normal", "text": "Hali ishchi loyiha emas, lekin xonalar real foydalanishga yaqin geometriyada ko'riladi."},
        {"title": "Xato", "type": "warning", "text": "Bubble aloqalarini unutib faqat chiroyli kontur chizmang."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Tanlangan bubble variantni oddiy devor konturlariga aylantiring."},
    ],
    "L10_M04_002": [
        {"title": "Xona ishlashi kerak", "type": "highlight", "text": "Xona faqat maydon emas. Uning proporsiyasi va mebel joylashuvi real foydalanishni belgilaydi."},
        {"title": "Mebel test", "type": "normal", "text": "Asosiy mebelni joylashtirib o'tish va foydalanish zonasini tekshiring."},
        {"title": "Noto'g'ri proporsiya", "type": "warning", "text": "Maydoni katta, lekin juda tor yoki noqulay xona amalda yomon ishlashi mumkin."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Mehmonxona, oshxona va yotoqxonaga asosiy mebellarni joylashtiring."},
    ],
    "L10_M04_003": [
        {"title": "Eshik + circulation", "type": "highlight", "text": "Eshik qayerda ochilishi xonadagi harakat va mebelga ta'sir qiladi."},
        {"title": "Dead space", "type": "normal", "text": "Keraksiz uzun koridor, burchak yoki foydalanilmaydigan o'tish zonalarini kamaytiring."},
        {"title": "Conflict", "type": "warning", "text": "Ikki eshikning bir-biriga urilishi yoki mebel yo'lni to'sishi eskiz bosqichida aniqlanishi kerak."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Plan ichidagi barcha asosiy circulation yo'llarini strelka bilan ko'rsating."},
    ],
    "L10_M04_004": [
        {"title": "Plan tashqi dunyo bilan bog'liq", "type": "highlight", "text": "Deraza, terassa, hovli va kirish plan qarorining davomi."},
        {"title": "Hovli bilan aloqa", "type": "normal", "text": "Mehmonxona, oshxona yoki boshqa public zona tashqi dam olish hududi bilan bog'lanishi mumkin."},
        {"title": "Fasadni unutish", "type": "warning", "text": "Ichkarida ishlaydigan plan fasadda tartibsiz ochilishlar yaratishi mumkin. Ikkalasi parallel tekshiriladi."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Har bir tashqi devor bo'yicha deraza va hovli aloqasini tahlil qiling."},
    ],
    "L10_M04_005": [
        {"title": "Eskiz plan audit", "type": "highlight", "text": "Brief → Bubble → xona proporsiyasi → mebel → circulation → openings → hovli/fasad → audit."},
        {"title": "Professional checklist", "type": "example", "text": "1. Briefga javob beradimi?<br><br>2. Zonalar to'g'rimi?<br><br>3. Xonalar ishlaydimi?<br><br>4. Mebel sig'adimi?<br><br>5. Circulation sodda-mi?<br><br>6. Eshik konfliktlari yo'qmi?<br><br>7. Deraza mantig'i bormi?<br><br>8. Hovli bilan aloqa bormi?<br><br>9. Fasadga ta'siri ko'rildimi?"},
        {"title": "Yakun", "type": "normal", "text": "Eskiz plan keyingi optimizatsiya uchun kuchli bazaga aylanishi kerak."},
        {"title": "Keyingi modul", "type": "highlight", "text": "Keyingi bosqich: PLAN OPTIMIZATSIYASI."},
    ],
}


LEVEL10_MODULE04_QUIZ = {
    "L10_M04_001": [
        {"code": "L10_Q046", "question": "Eskiz plan bubble diagramdan keyin keladimi?", "explanation": "Funksional sxema real geometriyaga aylantiriladi.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
        {"code": "L10_Q047", "question": "Eskiz plan darhol to'liq ishchi loyiha hisoblanadimi?", "explanation": "U hali konseptual va optimizatsiya bosqichidadir.", "options": [("A", "Ha", False), ("B", "Yo'q", True)]},
        {"code": "L10_Q048", "question": "Bubble aloqalarini eskiz planda saqlash muhimmi?", "explanation": "Funksional mantiq yo'qolmasligi kerak.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
    ],
    "L10_M04_002": [
        {"code": "L10_Q049", "question": "Xona maydoni yaxshi bo'lsa proporsiya ahamiyatsizmi?", "explanation": "Xona shakli real foydalanishga ta'sir qiladi.", "options": [("A", "Ha", False), ("B", "Yo'q", True)]},
        {"code": "L10_Q050", "question": "Mebel test xona ishlashini tekshirishga yordam beradimi?", "explanation": "Real foydalanish uchun yaxshi test.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
        {"code": "L10_Q051", "question": "Juda tor xona katta maydonga ega bo'lsa ham noqulay bo'lishi mumkinmi?", "explanation": "Proporsiya foydalanishga ta'sir qiladi.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
    ],
    "L10_M04_003": [
        {"code": "L10_Q052", "question": "Eshik ochilishi circulation'ga ta'sir qiladimi?", "explanation": "Harakat va mebel zonalari bilan konflikt bo'lishi mumkin.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
        {"code": "L10_Q053", "question": "Keraksiz uzun koridor foydali maydonni kamaytirishi mumkinmi?", "explanation": "Circulation optimizatsiyasi muhim.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
        {"code": "L10_Q054", "question": "Eshik konfliktini final bosqichgacha qoldirish kerakmi?", "explanation": "Eskizda erta aniqlash osonroq.", "options": [("A", "Ha", False), ("B", "Yo'q", True)]},
    ],
    "L10_M04_004": [
        {"code": "L10_Q055", "question": "Plan hovli bilan bog'lanishi mumkinmi?", "explanation": "Ichki va tashqi makonlar o'zaro ishlashi mumkin.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
        {"code": "L10_Q056", "question": "Plan fasadga ta'sir qiladimi?", "explanation": "Ochilishlar va hajm fasadda ko'rinadi.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
        {"code": "L10_Q057", "question": "Fasadni faqat plan tugagandan keyin o'ylash shartmi?", "explanation": "Plan va fasad parallel tekshirilishi mumkin.", "options": [("A", "Ha", False), ("B", "Yo'q", True)]},
    ],
    "L10_M04_005": [
        {"code": "L10_Q058", "question": "Eskiz plan auditida mebel va circulation tekshiriladimi?", "explanation": "Real funksional ishlash uchun muhim.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
        {"code": "L10_Q059", "question": "Eskiz plan briefga javob berishi kerakmi?", "explanation": "Plan texnik topshiriqni yechishi kerak.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
        {"code": "L10_Q060", "question": "Eskiz plan workflow'i qaysi?", "explanation": "Bubble funksiyasi real geometriya va mebel/circulation orqali tekshiriladi.", "options": [("A", "Bubble → xona geometriyasi → mebel → circulation → openings → audit", True), ("B", "Tasodifiy devor → final", False)]},
    ],
}


def seed_level10_module04():
    connection = get_connection()
    try:
        cursor = connection.cursor()

        for row in LEVEL10_MODULE04_LESSONS:
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
