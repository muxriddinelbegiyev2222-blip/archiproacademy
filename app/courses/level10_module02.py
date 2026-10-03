from database.database import get_connection


LEVEL10_MODULE02_LESSONS = [
    ("L10_M02", "L10_M02_001", "Site Analysis tushunchasi", "theory", "Uchastkani loyiha qaroridan oldin tizimli tahlil qilish.", 1, 50, 20),
    ("L10_M02", "L10_M02_002", "Kirish, ko'cha va orientatsiya", "theory", "Uchastkaning tashqi aloqalari va asosiy orientatsiyasini tahlil qilish.", 2, 55, 20),
    ("L10_M02", "L10_M02_003", "Quyosh, shamol va qo'shnilar", "practice", "Iqlim va atrof kontekstning uy joylashuviga ta'sirini tushunish.", 3, 60, 20),
    ("L10_M02", "L10_M02_004", "Relyef va mavjud elementlar", "practice", "Yer balandligi va mavjud obyektlarni loyiha qaroriga kiritish.", 4, 65, 20),
    ("L10_M02", "L10_M02_005", "Site Analysis professional audit", "practice", "Uchastka tahlilini yakuniy loyiha qaroriga aylantirish.", 5, 70, 25),
]


LEVEL10_MODULE02_CONTENT = {
    "L10_M02_001": [
        {"title": "Site Analysis", "type": "highlight", "text": "Uy planini chizishdan oldin uchastkaning imkoniyati va cheklovlari o'rganiladi."},
        {"title": "Tahlil", "type": "normal", "text": "Chegara, ko'cha, kirish, quyosh, shamol, qo'shnilar, relyef, mavjud obyektlar va tarmoqlar ko'riladi."},
        {"title": "Xato", "type": "warning", "text": "Avval ideal uy chizib, keyin uchastkaga joylashtirish ko'p konflikt keltirishi mumkin."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Bir uchastka uchun 12 bandli Site Analysis checklist tuzing."},
    ],
    "L10_M02_002": [
        {"title": "Ko'cha", "type": "highlight", "text": "Ko'cha uchastkaning tashqi aloqasi va asosiy kirish strategiyasiga ta'sir qiladi."},
        {"title": "Kirish", "type": "normal", "text": "Piyoda, avtomobil, xizmat va mehmon kirishlari alohida ko'rilishi mumkin."},
        {"title": "Orientatsiya", "type": "normal", "text": "Shimol yo'nalishi keyingi xona joylashuvi va quyosh tahlili uchun asos."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Uchastkada north, street, gate va asosiy kirishlarni belgilang."},
    ],
    "L10_M02_003": [
        {"title": "Quyosh", "type": "highlight", "text": "Xonalarni uchastkaga joylashtirishda quyosh harakati va soyalanish ko'rib chiqiladi."},
        {"title": "Shamol", "type": "normal", "text": "Mahalliy shamol va ochiq zonalar tashqi makon qulayligiga ta'sir qilishi mumkin."},
        {"title": "Qo'shni", "type": "warning", "text": "Qo'shni bino, baland devor yoki daraxt tabiiy yorug'lik va privacy'ga ta'sir qilishi mumkin."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Quyosh, shamol va qo'shnilar uchun alohida diagramma tuzing."},
    ],
    "L10_M02_004": [
        {"title": "Relyef", "type": "highlight", "text": "Yer balandligidagi farqlar kirish, drenaj va bino sathlariga ta'sir qiladi."},
        {"title": "Mavjud element", "type": "normal", "text": "Daraxt, eski bino, quduq, ustun, yo'l yoki tarmoq loyiha qaroriga ta'sir qilishi mumkin."},
        {"title": "Tekis deb taxmin qilmang", "type": "warning", "text": "Real o'lchovsiz uchastkani ideal tekis deb qabul qilish xato bo'lishi mumkin."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Mavjud elementlarni saqlash / olib tashlash / tekshirish guruhlariga ajrating."},
    ],
    "L10_M02_005": [
        {"title": "Site Analysis audit", "type": "highlight", "text": "Chegara → ko'cha → kirish → orientatsiya → quyosh → shamol → qo'shni → relyef → tarmoqlar → loyiha xulosasi."},
        {"title": "Xulosa", "type": "normal", "text": "Tahlil faqat diagramma emas. U keyingi bino joylashuvi bo'yicha konkret xulosaga olib kelishi kerak."},
        {"title": "Professional checklist", "type": "example", "text": "1. Chegaralar aniqmi?<br><br>2. Street/front aniqmi?<br><br>3. North bor-mi?<br><br>4. Kirishlar tahlil qilindimi?<br><br>5. Quyosh ko'rildimi?<br><br>6. Qo'shnilar tahlil qilindimi?<br><br>7. Relyef ma'lummi?<br><br>8. Mavjud elementlar qayd qilindimi?<br><br>9. Yakuniy site xulosasi bormi?"},
        {"title": "Keyingi modul", "type": "highlight", "text": "Keyingi bosqich: BUBBLE DIAGRAM."},
    ],
}


LEVEL10_MODULE02_QUIZ = {
    "L10_M02_001": [
        {"code": "L10_Q016", "question": "Site Analysis uy planidan oldin bajariladimi?", "explanation": "Uchastka sharoiti plan qarorlariga ta'sir qiladi.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
        {"code": "L10_Q017", "question": "Uchastka faqat o'lchamdan iboratmi?", "explanation": "Kontekst va tabiiy omillar ham muhim.", "options": [("A", "Ha", False), ("B", "Yo'q", True)]},
        {"code": "L10_Q018", "question": "Site Analysis keyingi bino joylashuviga ta'sir qiladimi?", "explanation": "Tahlil loyiha strategiyasini shakllantiradi.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
    ],
    "L10_M02_002": [
        {"code": "L10_Q019", "question": "Ko'cha tomoni kirish strategiyasiga ta'sir qiladimi?", "explanation": "Asosiy tashqi aloqa ko'cha bilan bog'liq.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
        {"code": "L10_Q020", "question": "North yo'nalishini bilish foydalimi?", "explanation": "Orientatsiya va quyosh tahliliga kerak.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
        {"code": "L10_Q021", "question": "Piyoda va avtomobil kirishlarini ajratish mumkinmi?", "explanation": "Ularning funksiyasi farq qilishi mumkin.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
    ],
    "L10_M02_003": [
        {"code": "L10_Q022", "question": "Qo'shni bino soyalanishga ta'sir qilishi mumkinmi?", "explanation": "Atrof kontekst quyosh va privacy'ga ta'sir qiladi.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
        {"code": "L10_Q023", "question": "Quyosh tahlili xona joylashuviga yordam beradimi?", "explanation": "Tabiiy yorug'lik va iqlim qarorlarini qo'llab-quvvatlaydi.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
        {"code": "L10_Q024", "question": "Atrof kontekstni e'tiborsiz qoldirish to'g'rimi?", "explanation": "Qo'shni va tabiiy omillar loyihaga ta'sir qiladi.", "options": [("A", "Ha", False), ("B", "Yo'q", True)]},
    ],
    "L10_M02_004": [
        {"code": "L10_Q025", "question": "Relyef bino sathlariga ta'sir qilishi mumkinmi?", "explanation": "Yer balandligi kirish va drenaj bilan bog'liq.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
        {"code": "L10_Q026", "question": "Real o'lchovsiz yer tekis deb qabul qilinishi kerakmi?", "explanation": "Mavjud holatni tekshirish kerak.", "options": [("A", "Ha", False), ("B", "Yo'q", True)]},
        {"code": "L10_Q027", "question": "Mavjud daraxt ham loyiha elementiga aylanishi mumkinmi?", "explanation": "Mavjud elementlarni saqlash qarori dizaynga ta'sir qilishi mumkin.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
    ],
    "L10_M02_005": [
        {"code": "L10_Q028", "question": "Site Analysis yakunida konkret loyiha xulosasi bo'lishi kerakmi?", "explanation": "Tahlil keyingi qarorga xizmat qilishi kerak.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
        {"code": "L10_Q029", "question": "Faqat chiroyli diagramma Site Analysis uchun yetarlimi?", "explanation": "Diagramma qaror va xulosaga olib kelishi kerak.", "options": [("A", "Ha", False), ("B", "Yo'q", True)]},
        {"code": "L10_Q030", "question": "Site Analysis workflow'i qaysi?", "explanation": "Uchastkaning tabiiy va kontekstual sharoiti tizimli tahlil qilinadi.", "options": [("A", "Chegara → kirish → orientatsiya → tabiiy omillar → kontekst → xulosa", True), ("B", "Darhol plan chizish", False)]},
    ],
}


def seed_level10_module02():
    connection = get_connection()
    try:
        cursor = connection.cursor()

        for row in LEVEL10_MODULE02_LESSONS:
            (
                module_code,
                lesson_code,
                title,
                lesson_type,
                summary,
                sort_order,
                estimated_minutes,
                xp_reward,
            ) = row

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
