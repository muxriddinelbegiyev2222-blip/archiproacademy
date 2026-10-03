from database.database import get_connection


LEVEL09_MODULE08_LESSONS = [
    ("L09_M08", "L09_M08_001", "Normativ xatolarni tanish", "theory", "Loyihada normativga oid xatolar qanday paydo bo'lishini va ularni tasniflashni o'rganish.", 1, 50, 20),
    ("L09_M08", "L09_M08_002", "Noto'g'ri manba va noto'g'ri talqin", "theory", "Eski, noto'g'ri yoki kontekstdan uzilgan manbalardan foydalanish xatolarini aniqlash.", 2, 55, 20),
    ("L09_M08", "L09_M08_003", "Plan va genplandagi xatolar", "practice", "Turar joy va uchastka yechimlarida normativ konfliktlarni topish.", 3, 60, 20),
    ("L09_M08", "L09_M08_004", "Koordinatsiya va hujjatlashtirish xatolari", "practice", "Arxitektura, konstruktsiya, MEP va normativ ma'lumotlar o'rtasidagi nomuvofiqliklarni aniqlash.", 4, 65, 20),
    ("L09_M08", "L09_M08_005", "LEVEL 9 professional normativ audit", "practice", "Barcha LEVEL 9 bilimlarini birlashtirib loyiha uchun yakuniy normativ audit o'tkazish.", 5, 70, 25),
]


LEVEL09_MODULE08_CONTENT = {
    "L09_M08_001": [
        {"title": "Normativ xato faqat noto'g'ri raqam emas", "type": "highlight", "text": "Noto'g'ri hujjat, eski tahrir, noto'g'ri obyekt tasnifi, noto'g'ri talqin yoki koordinatsiya xatosi ham normativ xato bo'lishi mumkin."},
        {"title": "5 kategoriya", "type": "normal", "text": "1. Manba xatosi<br><br>2. Qo'llanish xatosi<br><br>3. Talqin xatosi<br><br>4. Loyiha xatosi<br><br>5. Koordinatsiya xatosi"},
        {"title": "Eshitganman", "type": "warning", "text": "Biror talabni faqat “eshitganman” yoki “hamma shunday qiladi” degan asos bilan qo'llamang."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Normativ xatolarni 5 kategoriyaga ajratib har biriga bittadan misol yozing."},
    ],

    "L09_M08_002": [
        {"title": "Manba xatosi", "type": "highlight", "text": "Eski PDF, noma'lum sayt, skrinshot yoki boshqa obyektga tegishli hujjat noto'g'ri qarorga olib kelishi mumkin."},
        {"title": "Source-check", "type": "normal", "text": "Hujjat nomi, manba, tahrir, sana, qo'llanish doirasi va kerakli band tekshiriladi."},
        {"title": "Kontekstdan uzmang", "type": "warning", "text": "Bitta jumlani to'liq bo'limdan uzib olib loyiha qarori sifatida ishlatmang."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Bitta talab uchun source-check kartasi tayyorlang."},
    ],

    "L09_M08_003": [
        {"title": "Plan va genplan xatolari", "type": "highlight", "text": "Ko'p normativ konfliktlar xona funksiyasi, circulation, uchastka joylashtirish, tashqi aloqalar va yoritish qarorlarida ko'rinadi."},
        {"title": "Chiroyli plan", "type": "warning", "text": "Chiroyli va zamonaviy ko'rinishdagi plan avtomatik ravishda normativga mos degani emas."},
        {"title": "Find the mistake", "type": "example", "text": "Plan va genplanda: noto'g'ri circulation, soyalanish, kirish konflikti, sanitar zona muammosi yoki uchastka cheklovi kabi xatolarni qidiring."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Bir uy planida topilishi mumkin bo'lgan 10 normativ xato ssenariysini yozing."},
    ],

    "L09_M08_004": [
        {"title": "Versiya xatosi", "type": "highlight", "text": "Normativ audit eski plan bo'yicha, arxitektura esa yangi plan bo'yicha bajarilsa xulosa ishonchsiz bo'ladi."},
        {"title": "Arxitektura + konstruktsiya + MEP", "type": "normal", "text": "Normativ tekshiruv oxirgi koordinatsiyalangan loyiha ma'lumotiga bog'lanishi kerak."},
        {"title": "Hujjatlashtirmaslik", "type": "warning", "text": "Qaysi versiya va qaysi normativ asosida xulosa berilgani qayd qilinmasa keyin tekshirish qiyinlashadi."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Versiya, sana, model va normativ auditni birlashtiradigan workflow yozing."},
    ],

    "L09_M08_005": [
        {"title": "LEVEL 9 yakuniy audit", "type": "highlight", "text": "Obyekt → amaldagi manba → qo'llanish doirasi → loyiha tekshiruvi → issue → yechim → qayta tekshiruv → hujjatlashtirish."},
        {"title": "Audit jadvali", "type": "example", "text": "Issue<br>Joy<br>Normativ manba<br>Band<br>Status<br>Yechim<br>Qayta tekshiruv"},
        {"title": "Dalilsiz MOS yozmang", "type": "warning", "text": "Tekshiruv natijasini aniq manba va loyiha dalilisiz “mos” deb belgilamang."},
        {"title": "Professional checklist", "type": "example", "text": "1. Obyekt tasnifi aniqmi?<br><br>2. Manbalar amaldami?<br><br>3. Qo'llanish doirasi tekshirildimi?<br><br>4. Plan audit qilindimi?<br><br>5. Genplan audit qilindimi?<br><br>6. Yoritish/insolyatsiya ko'rildimi?<br><br>7. Yong'in/evakuatsiya ko'rildimi?<br><br>8. Accessibility ko'rildimi?<br><br>9. Oxirgi loyiha versiyasi ishlatildimi?<br><br>10. Audit natijasi hujjatlashtirildimi?"},
        {"title": "LEVEL 9 yakuni", "type": "highlight", "text": "Siz endi normativni topishdan tashqari, uning amaldagi holati, qo'llanish doirasi, loyiha bilan aloqasi va audit izini professional tarzda boshqarish mantig'ini bilasiz."},
    ],
}


LEVEL09_MODULE08_QUIZ = {
    "L09_M08_001": [
        {"code": "L09_Q106", "question": "Normativ xato faqat noto'g'ri raqamdan iboratmi?", "explanation": "Manba, talqin va koordinatsiya xatolari ham bo'lishi mumkin.", "options": [("A", "Ha", False), ("B", "Yo'q", True)]},
        {"code": "L09_Q107", "question": "Noto'g'ri obyekt tasnifi normativ xatoga olib kelishi mumkinmi?", "explanation": "Noto'g'ri tasnif noto'g'ri talablar tanlanishiga sabab bo'lishi mumkin.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
        {"code": "L09_Q108", "question": "“Hamma shunday qiladi” normativ dalil hisoblanadimi?", "explanation": "Professional qaror amaldagi normativ manbaga tayanadi.", "options": [("A", "Ha", False), ("B", "Yo'q", True)]},
    ],
    "L09_M08_002": [
        {"code": "L09_Q109", "question": "Noma'lum manbadagi skrinshotni rasmiy normativ o'rnida ishlatish to'g'rimi?", "explanation": "Manba va hujjat holati tekshirilishi kerak.", "options": [("A", "Ha", False), ("B", "Yo'q", True)]},
        {"code": "L09_Q110", "question": "Normativ bandni kontekstdan uzib talqin qilish xato bo'lishi mumkinmi?", "explanation": "Bandning boshqa qoidalar va qo'llanish shartlari bilan aloqasi bo'lishi mumkin.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
        {"code": "L09_Q111", "question": "Source-check karta audit sifatini oshiradimi?", "explanation": "Manba va tahrirni nazorat qilish xato xavfini kamaytiradi.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
    ],
    "L09_M08_003": [
        {"code": "L09_Q112", "question": "Chiroyli plan avtomatik ravishda normativga mos deganimi?", "explanation": "Vizual sifat normativ moslikni isbotlamaydi.", "options": [("A", "Ha", False), ("B", "Yo'q", True)]},
        {"code": "L09_Q113", "question": "Genplan ham normativ xatolar manbai bo'lishi mumkinmi?", "explanation": "Joylashtirish, kirish va tashqi aloqalarda xatolar bo'lishi mumkin.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
        {"code": "L09_Q114", "question": "Find-the-mistake mashqlari normativ fikrlashni rivojlantiradimi?", "explanation": "Xatoni tanish professional audit ko'nikmasini kuchaytiradi.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
    ],
    "L09_M08_004": [
        {"code": "L09_Q115", "question": "Normativ audit eski loyiha versiyasida bajarilsa muammo bo'lishi mumkinmi?", "explanation": "Audit oxirgi koordinatsiyalangan loyiha holatiga asoslanishi kerak.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
        {"code": "L09_Q116", "question": "Arxitektura va konstruktor modeli turli versiyada bo'lsa audit ishonchliligi pasayadimi?", "explanation": "Koordinatsiya qilinmagan ma'lumot noto'g'ri xulosaga olib kelishi mumkin.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
        {"code": "L09_Q117", "question": "Auditda loyiha versiyasi va sana qayd qilinishi foydalimi?", "explanation": "Bu qaysi loyiha holati tekshirilganini aniq ko'rsatadi.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
    ],
    "L09_M08_005": [
        {"code": "L09_Q118", "question": "Yakuniy normativ audit amaldagi manbani tekshirishdan boshlanishi kerakmi?", "explanation": "Talabning ishonchliligi va qo'llanishi avval tekshiriladi.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
        {"code": "L09_Q119", "question": "Dalilsiz “MOS” statusi berish professional auditmi?", "explanation": "Status loyiha va normativ dalil bilan asoslanishi kerak.", "options": [("A", "Ha", False), ("B", "Yo'q", True)]},
        {"code": "L09_Q120", "question": "LEVEL 9 normativ auditining to'g'ri workflow'i qaysi?", "explanation": "Obyekt va amaldagi normativ aniqlanib loyiha tekshiriladi, issue va yechimlar qayta audit qilinadi.", "options": [("A", "Obyekt → amaldagi manba → qo'llanish → loyiha audit → issue → yechim → qayta tekshiruv", True), ("B", "Tasodifiy internet ma'lumoti → MOS deb yozish", False)]},
    ],
}


def seed_level09_module08():
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
        ) in LEVEL09_MODULE08_LESSONS:

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
