from database.database import get_connection


LEVEL10_MODULE05_LESSONS = [
    ("L10_M05", "L10_M05_001", "Plan optimizatsiyasi tushunchasi", "theory", "Eskiz planni samaraliroq va aniqroq yechimga aylantirish.", 1, 60, 20),
    ("L10_M05", "L10_M05_002", "Foydali va yo'qotilgan maydon", "practice", "Koridor, burchak va dead space'larni tahlil qilish.", 2, 70, 20),
    ("L10_M05", "L10_M05_003", "Xonalararo konfliktlarni yechish", "practice", "Eshik, mebel, circulation va privacy konfliktlarini bartaraf etish.", 3, 70, 20),
    ("L10_M05", "L10_M05_004", "Konstruktiv va MEP mantiq", "practice", "Plan yechimini konstruktiv va muhandislik tizimlari bilan moslashtirish.", 4, 75, 20),
    ("L10_M05", "L10_M05_005", "Final plan audit", "practice", "Archicad modeliga o'tishdan oldin plan yechimini yakuniy tekshirish.", 5, 85, 25),
]


LEVEL10_MODULE05_CONTENT = {
    "L10_M05_001": [
        {"title": "Yaxshi plan birinchi urinishda tugamaydi", "type": "highlight", "text": "Optimizatsiya — ishlaydigan planni yanada sodda, aniq va samarali qilish jarayoni."},
        {"title": "Savol", "type": "normal", "text": "Har bir devor, koridor va burilishning vazifasi bormi?"},
        {"title": "Xato", "type": "warning", "text": "Faqat chiroyli geometriya uchun ortiqcha maydon yo'qotmang."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Eskiz plandagi 5 ta optimizatsiya nuqtasini toping."},
    ],
    "L10_M05_002": [
        {"title": "Dead space", "type": "highlight", "text": "Foydalanilmaydigan burchak, ortiqcha hall va uzun koridor maydon samaradorligini pasaytirishi mumkin."},
        {"title": "Foydali maydon", "type": "normal", "text": "Har bir kvadrat metrning real funksiyasi borligini tekshiring."},
        {"title": "Lekin haddan oshmang", "type": "warning", "text": "Faqat maydonni tejash uchun circulation yoki qulaylikni buzish ham noto'g'ri."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Plan ichidagi foydasiz yoki kam ishlatiladigan zonalarni belgilang."},
    ],
    "L10_M05_003": [
        {"title": "Conflict audit", "type": "highlight", "text": "Eshik, mebel, harakat, privacy va shovqin konfliktlari tekshiriladi."},
        {"title": "Privacy", "type": "normal", "text": "Private xonaga kirish public markaz orqali noqulay kesishmasligi kerak."},
        {"title": "Eshiklar", "type": "warning", "text": "Eshiklar bir-biriga, mebelga yoki circulation yo'liga urilmasligi kerak."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Plan bo'yicha 10 ta conflict-check bajaring."},
    ],
    "L10_M05_004": [
        {"title": "Plan faqat arxitektura emas", "type": "highlight", "text": "Konstruksiya va MEP talablarini erta hisobga olish keyingi qayta ishlashni kamaytiradi."},
        {"title": "Wet zones", "type": "normal", "text": "Sanuzel, oshxona va texnik zonalarning muhandislik aloqasi ko'riladi."},
        {"title": "Tayanch mantiqi", "type": "normal", "text": "Devor, ustun va katta ochilishlar konstruktiv tizim bilan koordinatsiya qilinadi."},
        {"title": "Xato", "type": "warning", "text": "Arxitektura planini konstruktor va MEPga umuman joy qoldirmasdan yakunlamang."},
    ],
    "L10_M05_005": [
        {"title": "Final plan audit", "type": "highlight", "text": "Brief → zonalash → xonalar → mebel → circulation → privacy → konstruktsiya → MEP → site → final plan."},
        {"title": "Professional checklist", "type": "example", "text": "1. Briefga javob beradimi?<br><br>2. Dead space kamayganmi?<br><br>3. Mebel ishlaydimi?<br><br>4. Eshiklar konflikt qilmayaptimi?<br><br>5. Privacy saqlanganmi?<br><br>6. Wet zones mantiqiymi?<br><br>7. Konstruktiv sxema mumkinmi?<br><br>8. Site bilan aloqa saqlanganmi?<br><br>9. Fasadga asos bor-mi?"},
        {"title": "Freeze point", "type": "normal", "text": "Plan yetarlicha audit qilingach keyingi BIM model bosqichiga o'tiladi."},
        {"title": "Keyingi modul", "type": "highlight", "text": "Keyingi bosqich: ARCHICAD MODELI."},
    ],
}


LEVEL10_MODULE05_QUIZ = {
    "L10_M05_001": [
        {"code": "L10_Q061", "question": "Plan optimizatsiyasi birinchi eskizni yaxshilash jarayonimi?", "explanation": "Eskiz tahlil va tuzatish orqali kuchaytiriladi.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
        {"code": "L10_Q062", "question": "Har bir devor va koridorning vazifasini tekshirish foydalimi?", "explanation": "Ortiqcha elementlarni aniqlashga yordam beradi.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
        {"code": "L10_Q063", "question": "Chiroyli geometriya uchun funksiyani buzish to'g'rimi?", "explanation": "Funksiya birlamchi tekshiruv mezonidir.", "options": [("A", "Ha", False), ("B", "Yo'q", True)]},
    ],
    "L10_M05_002": [
        {"code": "L10_Q064", "question": "Dead space maydon samaradorligini pasaytirishi mumkinmi?", "explanation": "Foydalanilmaydigan maydon ortadi.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
        {"code": "L10_Q065", "question": "Maydonni tejash uchun circulation'ni buzish to'g'rimi?", "explanation": "Samaradorlik qulaylik bilan muvozanatli bo'lishi kerak.", "options": [("A", "Ha", False), ("B", "Yo'q", True)]},
        {"code": "L10_Q066", "question": "Har kvadrat metrning real funksiyasini tekshirish foydalimi?", "explanation": "Bu plan samaradorligini oshiradi.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
    ],
    "L10_M05_003": [
        {"code": "L10_Q067", "question": "Eshik va mebel konfliktlari plan auditiga kiradimi?", "explanation": "Real foydalanishga ta'sir qiladi.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
        {"code": "L10_Q068", "question": "Privacy plan optimizatsiyasida muhimmi?", "explanation": "Public/private aloqalar tekshiriladi.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
        {"code": "L10_Q069", "question": "Faqat xona maydoni yaxshi bo'lsa barcha konfliktlar hal bo'ladimi?", "explanation": "Circulation va mebel konfliktlari qolishi mumkin.", "options": [("A", "Ha", False), ("B", "Yo'q", True)]},
    ],
    "L10_M05_004": [
        {"code": "L10_Q070", "question": "Wet zones MEP bilan koordinatsiya qilinadimi?", "explanation": "Muhandislik tarmoqlari bilan bog'liq.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
        {"code": "L10_Q071", "question": "Katta openinglar konstruktiv tizimga ta'sir qilishi mumkinmi?", "explanation": "Tayanch va yuk yo'li bilan bog'liq.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
        {"code": "L10_Q072", "question": "Arxitektura planini konstruktsiyani umuman o'ylamasdan yakunlash idealmi?", "explanation": "Keyingi bosqichlarda katta qayta ishlash bo'lishi mumkin.", "options": [("A", "Ha", False), ("B", "Yo'q", True)]},
    ],
    "L10_M05_005": [
        {"code": "L10_Q073", "question": "Final plan audit Archicad modelidan oldin bajariladimi?", "explanation": "Kuchli plan BIM model uchun baza bo'ladi.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
        {"code": "L10_Q074", "question": "Final plan brief bilan solishtiriladimi?", "explanation": "Loyiha texnik topshiriqqa javob berishi kerak.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
        {"code": "L10_Q075", "question": "Plan optimizatsiyasi workflow'i qaysi?", "explanation": "Funksiya, maydon, konflikt, konstruksiya va MEP tekshiriladi.", "options": [("A", "Eskiz → dead space → conflict → konstruktsiya/MEP → final audit", True), ("B", "Eskiz → darhol final", False)]},
    ],
}


def seed_level10_module05():
    connection = get_connection()
    try:
        cursor = connection.cursor()

        for row in LEVEL10_MODULE05_LESSONS:
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
