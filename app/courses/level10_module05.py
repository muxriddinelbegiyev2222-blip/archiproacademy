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
        {"title": "Bir qavatli uy misolida 3 qatlam", "type": "highlight", "text": "Bir xil reja ustida uch narsani alohida tekshiring: 1) tashqi va ichki tayanch tizimi; 2) suv va kanalizatsiya yo‘nalishlari; 3) elektr hamda shamollatish uchun zarur joylar. Bu qatlamlar bir-biriga xalaqit bermasligi kerak."},
        {"title": "Tayanch va katta ochilishlar", "type": "normal", "text": "Tashqi devor, ustun va katta deraza yoki eshik ochilishini rejada belgilang. Yuk qayerdan qayerga uzatilishi konstruktiv loyihada tekshiriladi. Katta ochilishni faqat fasad chiroyli ko‘rinsin deb tayanch sxemasidan mustaqil o‘zgartirmang."},
        {"title": "Oshxona va sanuzelning muhandislik aloqasi", "type": "normal", "text": "Oshxona, sanuzel va texnik xonani rejada toping. Suv kirishi, oqova chiqishi, quvurlarni olib borish va xizmat ko‘rsatish joyini muhokama qiling. Yaqin joylashuv qulay bo‘lishi mumkin, lekin aniq quvur yo‘li, nishab va quvvat muhandis tomonidan hisoblanadi."},
        {"title": "To‘qnashuv misoli", "type": "warning", "text": "Shamollatish kanali yirik to‘sin orqali o‘tishi yoki elektr jihozi xizmat ko‘rsatib bo‘lmaydigan burchakda qolishi mumkin. Buni rejaning dastlabki bosqichida aniqlash keyingi qimmat qayta ishlashdan saqlaydi."},
        {"title": "Mini-amaliyot: uch rang bilan tekshiring", "type": "example", "text": "O‘zingizning eskiz rejangiz nusxasida tayanchlarni qora, suv va kanalizatsiya ehtimoliy yo‘nalishlarini ko‘k, elektr va shamollatish uchun ajratilgan zonalarni to‘q sariq bilan ko‘rsating. Kamida ikkita ehtimoliy to‘qnashuvni aniqlang va 'tekshirish kerak' deb yozing."},
        {"title": "Muhim chegara", "type": "normal", "text": "Bu dars konstruktiv yoki muhandislik hisobining o‘rnini bosmaydi. O‘lcham, tayanch, quvur nishabi va xavfsizlik talablarini amaldagi me'yorlar hamda tegishli mutaxassis hisobiga tayangan holda tasdiqlash kerak."},
    ],
    "L10_M05_005": [
        {"title": "Yakuniy reja tekshiruvi", "type": "highlight", "text": "Dastlabki eskizni tasdiqlashdan oldin uni texnik topshiriq bilan qayta solishtiring. Chiroyli ko‘rinishning o‘zi yetarli emas: reja ishlashi, xonalar, harakat yo‘li va texnik imkoniyat dalil bilan tekshiriladi."},
        {"title": "To‘qqiz yo‘nalishdagi tekshiruv", "type": "example", "text": "1. Xonalar topshiriqqa mosmi?<br><br>2. Jamoat va shaxsiy zonalar ajratilganmi?<br><br>3. Mebel haqiqatan sig‘adimi?<br><br>4. Eshiklar ochilganda to‘qnashuv yo‘qmi?<br><br>5. Keraksiz uzun yo‘lak qolmaganmi?<br><br>6. Deraza, hovli va kirish o‘zaro mosmi?<br><br>7. Oshxona va sanuzelning muhandislik aloqasi ko‘rib chiqilganmi?<br><br>8. Tayanch va katta ochilishlar mutaxassis bilan kelishilishi belgilanganmi?<br><br>9. Xatolar va yechilmagan savollar ro‘yxati yozilganmi?"},
        {"title": "Audit jadvali: muammo → dalil → yechim", "type": "normal", "text": "Masalan: 'Yotoqxona eshigi shkafga tegadi' — buni eshik ochilish yoyi va mebel konturi bilan ko‘rsating. Eshik yoki shkaf joyini o‘zgartiring; keyin bir xil rejada qayta tekshiring. Har bir tuzatishga mas'ul va holat yozing."},
        {"title": "Mini-amaliyot: rejaning ikki nusxasi", "type": "example", "text": "A nusxada kamida uchta muammoni rang bilan belgilang. B nusxada aniq tuzatishlarni ko‘rsating. O‘zgarishdan keyin xona, eshik va yurish yo‘li bir-biriga mos qolganini qayta tekshiring."},
        {"title": "Yakuniy qaror", "type": "warning", "text": "Reja bo‘yicha ochiq savollar qolsa, uni 'to‘liq tasdiqlangan loyiha' deb belgilamang. Eskizni BIM modelga o‘tkazish mumkin bo‘lsa ham, qurilish me'yorlari, konstruksiya va muhandislik yechimlari keyingi mutaxassis tekshiruvini talab etadi."},
        {"title": "Keyingi bosqich", "type": "highlight", "text": "Tekshirilgan va tuzatilgan reja asosida Archicad modelini qurishni boshlang. Modellash davomida aniqlangan yangi konfliktlarni ham audit ro‘yxatiga qaytaring."},
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
