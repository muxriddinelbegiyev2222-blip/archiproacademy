from database.database import get_connection


LEVEL10_MODULE03_LESSONS = [
    ("L10_M03", "L10_M03_001", "Bubble Diagram tushunchasi", "theory", "Xonalarni devorsiz funksional bloklar sifatida rejalashtirish.", 1, 40, 20),
    ("L10_M03", "L10_M03_002", "Zonalar va aloqalar", "theory", "Public, private va service zonalar orasidagi aloqalarni tashkil qilish.", 2, 45, 20),
    ("L10_M03", "L10_M03_003", "Kirish va circulation", "practice", "Harakat yo'llarini bubble diagram bosqichida tekshirish.", 3, 50, 20),
    ("L10_M03", "L10_M03_004", "Variantlar yaratish", "practice", "Bir brief uchun bir nechta funksional sxema tayyorlash.", 4, 50, 20),
    ("L10_M03", "L10_M03_005", "Bubble Diagram professional audit", "practice", "Eng kuchli funksional sxemani tanlash va audit qilish.", 5, 55, 25),
]


LEVEL10_MODULE03_CONTENT = {
    "L10_M03_001": [
        {"title": "Hali devor chizmang", "type": "highlight", "text": "Bubble Diagram bosqichida xonalar devor emas, funksional blok sifatida ko'riladi."},
        {"title": "Maqsad", "type": "normal", "text": "Xonalar qayerda va bir-biriga qanday bog'lanishi kerakligini tez tekshirish."},
        {"title": "Xato", "type": "warning", "text": "Juda erta aniq devor va o'lchamga o'tish variant qidirishni cheklaydi."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Briefdagi barcha xonalarni alohida bubble sifatida yozing."},
    ],
    "L10_M03_002": [
        {"title": "3 asosiy zona", "type": "highlight", "text": "PUBLIC / PRIVATE / SERVICE."},
        {"title": "Aloqa", "type": "normal", "text": "Mehmonxona-oshxona, master-sanuzel, kirish-garderob kabi kerakli yaqinliklar belgilanadi."},
        {"title": "Keraksiz aloqa", "type": "warning", "text": "Har xona ham har bir xona bilan to'g'ridan-to'g'ri bog'lanishi shart emas."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Required / Preferred / Avoid aloqalar jadvalini tuzing."},
    ],
    "L10_M03_003": [
        {"title": "Circulation diagram", "type": "highlight", "text": "Bubble diagram ichida foydalanuvchi harakatini strelkalar bilan ko'rsatish mumkin."},
        {"title": "Yo'l", "type": "normal", "text": "Kirish → public zona → private zona → service aloqalari tushunarli bo'lishi kerak."},
        {"title": "Koridorni kamaytirish", "type": "warning", "text": "Ko'p bubble'ni ulash uchun avtomatik uzun koridor yaratish yaxshi yechim bo'lmasligi mumkin."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Mehmon, oila va service harakati uchun 3 xil circulation strelkasi chizing."},
    ],
    "L10_M03_004": [
        {"title": "Bitta variant yetmaydi", "type": "highlight", "text": "Professional loyiha birinchi g'oyani darhol yakuniy plan deb qabul qilmaydi."},
        {"title": "Variant A/B/C", "type": "normal", "text": "Bir xil brief uchun turli zonalash va kirish strategiyasini sinab ko'ring."},
        {"title": "Baholash", "type": "normal", "text": "Har variant: funksionallik, privacy, circulation, site bilan aloqa bo'yicha solishtiriladi."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Bitta brief uchun 3 bubble variant yarating."},
    ],
    "L10_M03_005": [
        {"title": "Bubble audit", "type": "highlight", "text": "Brief → zonalar → aloqalar → circulation → site → variantlar → tanlov."},
        {"title": "Professional checklist", "type": "example", "text": "1. Barcha xonalar bormi?<br><br>2. Public/private/service aniqmi?<br><br>3. Kerakli xonalar yaqinmi?<br><br>4. Privacy saqlanganmi?<br><br>5. Circulation tushunarlimi?<br><br>6. Site bilan aloqa bormi?<br><br>7. Kamida 2-3 variant ko'rildimi?"},
        {"title": "Xato", "type": "warning", "text": "Bubble yaxshi bo'lmasa aniq plan bosqichida ko'p geometriya bilan yomon funksiyani yashirish mumkin."},
        {"title": "Keyingi modul", "type": "highlight", "text": "Keyingi bosqich: ESKIZ PLAN."},
    ],
}


LEVEL10_MODULE03_QUIZ = {
    "L10_M03_001": [
        {"code": "L10_Q031", "question": "Bubble Diagram bosqichida devor detallarini to'liq ishlab chiqish shartmi?", "explanation": "Bu bosqich funksional aloqalarni tekshiradi.", "options": [("A", "Ha", False), ("B", "Yo'q", True)]},
        {"code": "L10_Q032", "question": "Bubble Diagram xonalar aloqasini tekshirishga yordam beradimi?", "explanation": "Bu uning asosiy maqsadlaridan biri.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
        {"code": "L10_Q033", "question": "Juda erta aniq geometriyaga o'tish variant qidirishni cheklashi mumkinmi?", "explanation": "Erkin funksional izlanish kamayadi.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
    ],
    "L10_M03_002": [
        {"code": "L10_Q034", "question": "Public/private/service zonalash bubble diagramda ishlatiladimi?", "explanation": "Funksional guruhlash muhim.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
        {"code": "L10_Q035", "question": "Har xona barcha xonalar bilan bevosita bog'lanishi shartmi?", "explanation": "Kerakli va keraksiz aloqalar farqlanadi.", "options": [("A", "Ha", False), ("B", "Yo'q", True)]},
        {"code": "L10_Q036", "question": "Xonalar orasidagi yaqinlikni oldindan belgilash foydalimi?", "explanation": "Bu plan funksiyasini kuchaytiradi.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
    ],
    "L10_M03_003": [
        {"code": "L10_Q037", "question": "Circulation bubble diagramda tekshirilishi mumkinmi?", "explanation": "Strelkalar orqali harakat yo'llari ko'rsatiladi.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
        {"code": "L10_Q038", "question": "Har bir aloqani uzun koridor bilan hal qilish eng yaxshi yechimmi?", "explanation": "Bu foydali maydonni kamaytirishi mumkin.", "options": [("A", "Ha", False), ("B", "Yo'q", True)]},
        {"code": "L10_Q039", "question": "Mehmon va private circulation alohida tahlil qilinishi mumkinmi?", "explanation": "Privacy va funksional qulaylik uchun foydali.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
    ],
    "L10_M03_004": [
        {"code": "L10_Q040", "question": "Birinchi bubble variantni darhol final deb olish kerakmi?", "explanation": "Variantlar solishtirilsa kuchliroq yechim topilishi mumkin.", "options": [("A", "Ha", False), ("B", "Yo'q", True)]},
        {"code": "L10_Q041", "question": "Bir brief uchun bir nechta funksional variant bo'lishi mumkinmi?", "explanation": "Bir muammoga turli arxitektura yechimlari mavjud.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
        {"code": "L10_Q042", "question": "Variantlarni mezonlar bilan solishtirish foydalimi?", "explanation": "Qaror subyektiv tasodifga kamroq bog'lanadi.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
    ],
    "L10_M03_005": [
        {"code": "L10_Q043", "question": "Bubble audit brief bilan boshlanadimi?", "explanation": "Funksional sxema texnik topshiriqqa javob berishi kerak.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
        {"code": "L10_Q044", "question": "Site bilan aloqa bubble auditning bir qismi bo'lishi mumkinmi?", "explanation": "Kirish, hovli va orientatsiya funksional sxemaga ta'sir qiladi.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
        {"code": "L10_Q045", "question": "Bubble Diagram workflow'i qaysi?", "explanation": "Briefdan zonalar, aloqalar va variantlar orqali kuchli sxema tanlanadi.", "options": [("A", "Brief → zonalar → aloqalar → circulation → variantlar → audit", True), ("B", "Darhol devor → keyin funksiya", False)]},
    ],
}


def seed_level10_module03():
    connection = get_connection()
    try:
        cursor = connection.cursor()

        for row in LEVEL10_MODULE03_LESSONS:
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
