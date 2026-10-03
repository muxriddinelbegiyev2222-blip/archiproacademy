from database.database import get_connection


LEVEL11_MODULE01_LESSONS = [
    ("L11_M01", "L11_M01_001", "2 qavatli uy mantig'i", "theory", "Ikki qavatli uyni bitta vertikal tizim sifatida tushunish.", 1, 50, 20),
    ("L11_M01", "L11_M01_002", "Qavatlar orasidagi funksiya", "theory", "Funksiyalarni ikki qavatga mantiqiy taqsimlash.", 2, 55, 20),
    ("L11_M01", "L11_M01_003", "Vertikal yadro", "practice", "Zinapoya va asosiy vertikal aloqani konsepsiyaga integratsiya qilish.", 3, 60, 20),
    ("L11_M01", "L11_M01_004", "Massing va fasad", "practice", "Ikki qavatli hajmning tashqi kompozitsiyasini shakllantirish.", 4, 65, 20),
    ("L11_M01", "L11_M01_005", "2 qavatli konsepsiya auditi", "practice", "Funksiya, vertikal aloqa va hajmni kompleks tekshirish.", 5, 70, 25),
]


LEVEL11_MODULE01_CONTENT = {
    "L11_M01_001": [
        {"title": "Ikki plan emas", "type": "highlight", "text": "2 qavatli uy — bir-biriga qo'yilgan ikkita mustaqil plan emas. U bitta vertikal arxitektura tizimi."},
        {"title": "Birgalikda ishlaydi", "type": "normal", "text": "Qavat funksiyasi, zinapoya, konstruktsiya, MEP, fasad va tom bir-biriga bog'liq."},
        {"title": "Xato", "type": "warning", "text": "Avval 1-qavatni to'liq tugatib, 2-qavatni qolgan geometriyaga tasodifiy joylashtirmang."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Ikki qavatli uy uchun 8 ta vertikal koordinatsiya savolini yozing."},
    ],

    "L11_M01_002": [
        {"title": "Qavat funksiyasi", "type": "highlight", "text": "Har qavatning asosiy roli aniqlanadi."},
        {"title": "Misol", "type": "normal", "text": "Public/service funksiyalar pastda, private funksiyalar yuqorida bo'lishi mumkin, lekin bu universal qoida emas."},
        {"title": "Foydalanuvchi", "type": "normal", "text": "Yosh, mobility, kunlik hayot va kelajak ehtiyojlari qavat taqsimotiga ta'sir qiladi."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Bir oila uchun qavatlar bo'yicha room program tuzing."},
    ],

    "L11_M01_003": [
        {"title": "Vertikal yadro", "type": "highlight", "text": "Zinapoya ikki qavat orasidagi eng muhim arxitektura bog'lanishlaridan biri."},
        {"title": "Markaziy qaror", "type": "normal", "text": "Zinapoya joyi circulation, plan, void, fasad va konstruktsiyaga ta'sir qiladi."},
        {"title": "Keyin joylashtirmang", "type": "warning", "text": "Zinapoyani plan tugagach qolgan bo'sh joyga qo'yish ko'p muammo tug'dirishi mumkin."},
        {"title": "Mini-amaliyot", "type": "example", "text": "3 xil zinapoya joylashuv konsepsiyasini solishtiring."},
    ],

    "L11_M01_004": [
        {"title": "Massing", "type": "highlight", "text": "Ikki qavat bino balandligini oshiradi va fasad proporsiyasi o'zgaradi."},
        {"title": "Hajm", "type": "normal", "text": "Upper floor setback, terrace, balcony yoki void kabi qarorlar umumiy massing bilan bog'lanadi."},
        {"title": "Tasodifiy shakl", "type": "warning", "text": "Faqat fasadni qiziqarli qilish uchun konstruktsiya va plan mantiqini buzadigan hajm yaratilmasligi kerak."},
        {"title": "Mini-amaliyot", "type": "example", "text": "2 qavatli uy uchun 3 massing variant tayyorlang."},
    ],

    "L11_M01_005": [
        {"title": "Konsepsiya audit", "type": "highlight", "text": "Brief → qavat roli → vertikal yadro → strukturaviy mantiq → MEP → massing → fasad → audit."},
        {"title": "Professional checklist", "type": "example", "text": "1. Qavatlar roli aniqmi?<br><br>2. Zinapoya joyi mantiqiymi?<br><br>3. Circulation ishlaydimi?<br><br>4. Qavatlar konstruktiv mosmi?<br><br>5. Wet zones koordinatsiya qilinganmi?<br><br>6. Massing tushunarlimi?<br><br>7. Fasad konsepsiyasi bormi?"},
        {"title": "Keyingi modul", "type": "highlight", "text": "Keyingi modul: QAVATLAR ZONALASHI."},
    ],
}


LEVEL11_MODULE01_QUIZ = {
    "L11_M01_001": [
        {"code": "L11_Q001", "question": "2 qavatli uy ikkita butunlay mustaqil planmi?", "explanation": "Qavatlar vertikal va konstruktiv tizim orqali bog'langan.", "options": [("A", "Ha", False), ("B", "Yo'q", True)]},
        {"code": "L11_Q002", "question": "Qavatlar orasidagi koordinatsiya muhimmi?", "explanation": "Zinapoya, konstruktsiya va MEP bir-biriga bog'liq.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
        {"code": "L11_Q003", "question": "Ikkinchi qavatni tasodifiy joylashtirish yaxshi workflow'mi?", "explanation": "Ikki qavat boshidan bir tizim sifatida rejalashtiriladi.", "options": [("A", "Ha", False), ("B", "Yo'q", True)]},
    ],
    "L11_M01_002": [
        {"code": "L11_Q004", "question": "Qavatlar turli funksional rolga ega bo'lishi mumkinmi?", "explanation": "Funksiyalar oila ehtiyojiga qarab taqsimlanadi.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
        {"code": "L11_Q005", "question": "Public pastda, private yuqorida bo'lishi doim majburiymi?", "explanation": "Bu mumkin bo'lgan strategiya, universal qoida emas.", "options": [("A", "Ha", False), ("B", "Yo'q", True)]},
        {"code": "L11_Q006", "question": "Foydalanuvchi mobility qavat taqsimotiga ta'sir qilishi mumkinmi?", "explanation": "Qulay foydalanish uchun muhim.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
    ],
    "L11_M01_003": [
        {"code": "L11_Q007", "question": "Zinapoya qavatlararo asosiy aloqa elementimi?", "explanation": "Vertikal circulation uchun markaziy rol o'ynaydi.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
        {"code": "L11_Q008", "question": "Zinapoya joyi fasadga ham ta'sir qilishi mumkinmi?", "explanation": "Opening va hajm qarorlariga ta'sir qilishi mumkin.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
        {"code": "L11_Q009", "question": "Zinapoyani qolgan bo'shliqqa oxirida joylashtirish eng yaxshi usulmi?", "explanation": "Uni konsepsiyada erta hal qilish yaxshiroq.", "options": [("A", "Ha", False), ("B", "Yo'q", True)]},
    ],
    "L11_M01_004": [
        {"code": "L11_Q010", "question": "Ikkinchi qavat fasad proporsiyasiga ta'sir qiladimi?", "explanation": "Bino balandligi va massing o'zgaradi.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
        {"code": "L11_Q011", "question": "Massing plan va konstruktsiya bilan koordinatsiya qilinadimi?", "explanation": "Hajm loyiha tizimining bir qismi.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
        {"code": "L11_Q012", "question": "Faqat qiziqarli tashqi shakl uchun ichki funksiyani buzish to'g'rimi?", "explanation": "Forma va funksiya birga ishlaydi.", "options": [("A", "Ha", False), ("B", "Yo'q", True)]},
    ],
    "L11_M01_005": [
        {"code": "L11_Q013", "question": "2 qavatli konsepsiya auditida MEP ham ko'riladimi?", "explanation": "Vertikal shaft va wet zones muhim.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
        {"code": "L11_Q014", "question": "Qavatlarning konstruktiv mosligi muhimmi?", "explanation": "Tayanch va yuk yo'li qavatlar bo'yicha ishlaydi.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
        {"code": "L11_Q015", "question": "2 qavatli konsepsiya workflow'i qaysi?", "explanation": "Qavatlar roli va vertikal aloqa massing bilan birga rivojlanadi.", "options": [("A", "Brief → qavat roli → zinapoya → konstruktsiya/MEP → massing → audit", True), ("B", "1-qavat → tasodifiy 2-qavat → final", False)]},
    ],
}


def seed_level11_module01():
    connection = get_connection()
    try:
        cursor = connection.cursor()

        for row in LEVEL11_MODULE01_LESSONS:
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
