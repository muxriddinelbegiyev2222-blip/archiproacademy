from database.database import get_connection


LEVEL11_MODULE06_LESSONS = [
    ("L11_M06", "L11_M06_001", "Balkon va terassa funksiyasi", "theory", "Tashqi yashash zonalarining real vazifasini aniqlash.", 1, 40, 20),
    ("L11_M06", "L11_M06_002", "Ichki-tashqi aloqa", "theory", "Balkon va terassani xona funksiyasi bilan bog'lash.", 2, 45, 20),
    ("L11_M06", "L11_M06_003", "Konstruktiv va thermal bridge mantig'i", "practice", "Tashqi plita va bino qobig'i aloqasini tushunish.", 3, 50, 20),
    ("L11_M06", "L11_M06_004", "Gidroizolyatsiya va drainage", "practice", "Tashqi ochiq zonalarda suvni boshqarish.", 4, 50, 20),
    ("L11_M06", "L11_M06_005", "Balkon va terassa audit", "practice", "Funksiya, konstruktsiya va suv himoyasini kompleks tekshirish.", 5, 55, 25),
]


LEVEL11_MODULE06_CONTENT = {
    "L11_M06_001": [
        {"title": "Nima uchun kerak?", "type": "highlight", "text": "Balkon yoki terassa faqat fasad bezagi emas. Uning real foydalanish ssenariysi bo'lishi kerak."},
        {"title": "Savol", "type": "normal", "text": "Kim foydalanadi, qachon foydalanadi va qaysi xona bilan bog'lanadi?"},
        {"title": "Xato", "type": "warning", "text": "Juda tor yoki real foydalanilmaydigan balkon faqat maydon va xarajat qo'shishi mumkin."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Har bir tashqi zonaning real ssenariysini yozing."},
    ],
    "L11_M06_002": [
        {"title": "Ichki-tashqi aloqa", "type": "highlight", "text": "Bedroom balcony, family terrace yoki guest terrace turli aloqa talab qiladi."},
        {"title": "Privacy", "type": "normal", "text": "Balkon joyi qo'shni va boshqa xonalar bilan ko'rish aloqasiga ta'sir qiladi."},
        {"title": "Access", "type": "normal", "text": "Eshik va ichki circulation tashqi zonaga qulay kirishni ta'minlaydi."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Balkon uchun room-access-privacy diagram yarating."},
    ],
    "L11_M06_003": [
        {"title": "Cantilever", "type": "highlight", "text": "Konsol balkon konstruktiv hisob va detail talab qiladi."},
        {"title": "Thermal bridge", "type": "normal", "text": "Ichki plitaning tashqariga davom etishi bino qobig'iga ta'sir qilishi mumkin."},
        {"title": "Taxmin qilmang", "type": "warning", "text": "Konsol uzunligi yoki armaturani arxitektura taxmini bilan belgilamang."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Balkon uchun architect-structure-envelope koordinatsiya savollarini yozing."},
    ],
    "L11_M06_004": [
        {"title": "Suv", "type": "highlight", "text": "Ochiq balkon va terassada nishab, drainage va waterproofing bir tizim."},
        {"title": "Threshold", "type": "normal", "text": "Ichki xona bilan tashqi sath tutashuvi kritik detail."},
        {"title": "Xato", "type": "warning", "text": "Suvni eshik oldiga yoki bino tomon yo'naltirmang."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Balkonda suv yo'lini strelka bilan tasvirlang."},
    ],
    "L11_M06_005": [
        {"title": "Balkon audit", "type": "highlight", "text": "Purpose → access → privacy → structure → thermal bridge → waterproofing → drainage → railing."},
        {"title": "Professional checklist", "type": "example", "text": "1. Real funksiya bormi?<br><br>2. Access qulaymi?<br><br>3. Privacy ko'rildimi?<br><br>4. Konstruktor bilan kelishildimi?<br><br>5. Thermal bridge ko'rildimi?<br><br>6. Drainage ishlaydimi?<br><br>7. Threshold detaili bormi?<br><br>8. Safety tekshirildimi?"},
        {"title": "Keyingi modul", "type": "highlight", "text": "Keyingi modul: 2 QAVATLI FASAD."},
    ],
}


LEVEL11_MODULE06_QUIZ = {}

for i, lesson_code in enumerate(
    ["L11_M06_001", "L11_M06_002", "L11_M06_003", "L11_M06_004", "L11_M06_005"]
):
    start = 76 + i * 3

    LEVEL11_MODULE06_QUIZ[lesson_code] = [
        {
            "code": f"L11_Q{start:03d}",
            "question": "Balkon yoki terassaning real foydalanish maqsadi bo'lishi kerakmi?",
            "explanation": "Tashqi zona faqat dekor emas.",
            "options": [("A", "Ha", True), ("B", "Yo'q", False)],
        },
        {
            "code": f"L11_Q{start + 1:03d}",
            "question": "Balkon konstruktsiya va thermal envelope bilan bog'liqmi?",
            "explanation": "Plita va bino qobig'i tutashadi.",
            "options": [("A", "Ha", True), ("B", "Yo'q", False)],
        },
        {
            "code": f"L11_Q{start + 2:03d}",
            "question": "Balkonda drainage va waterproofingni e'tiborsiz qoldirish to'g'rimi?",
            "explanation": "Suv himoyasi kritik.",
            "options": [("A", "Ha", False), ("B", "Yo'q", True)],
        },
    ]


def seed_level11_module06():
    connection = get_connection()
    try:
        cursor = connection.cursor()

        for row in LEVEL11_MODULE06_LESSONS:
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
