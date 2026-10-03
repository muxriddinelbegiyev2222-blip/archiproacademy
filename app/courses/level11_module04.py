from database.database import get_connection


LEVEL11_MODULE04_LESSONS = [
    ("L11_M04", "L11_M04_001", "Vertikal kommunikatsiya tushunchasi", "theory", "Qavatlar orasidagi arxitektura va muhandislik aloqalarini tushunish.", 1, 50, 20),
    ("L11_M04", "L11_M04_002", "Shaft va riser", "theory", "Muhandislik tizimlari uchun vertikal zonalarni rejalashtirish.", 2, 55, 20),
    ("L11_M04", "L11_M04_003", "Wet stack koordinatsiyasi", "practice", "Sanitar va oshxona tizimlarini vertikal bog'lash.", 3, 60, 20),
    ("L11_M04", "L11_M04_004", "Konstruktsiya bilan koordinatsiya", "practice", "Vertikal penetratsiyalarni plita, beam va devorlar bilan muvofiqlashtirish.", 4, 65, 20),
    ("L11_M04", "L11_M04_005", "Vertikal kommunikatsiya audit", "practice", "Shaft, MEP va konstruktiv koordinatsiyani kompleks tekshirish.", 5, 70, 25),
]


LEVEL11_MODULE04_CONTENT = {
    "L11_M04_001": [
        {"title": "Qavatlar orasidagi yashirin tizim", "type": "highlight", "text": "2 qavatli uyda suv, kanalizatsiya, ventilyatsiya va boshqa tizimlar vertikal yo'l talab qilishi mumkin."},
        {"title": "Arxitektor roli", "type": "normal", "text": "Muhandislik uchun joy qoldirish arxitektura rejasining bir qismi."},
        {"title": "Xato", "type": "warning", "text": "Plan tugagach MEPni qolgan bo'shliqqa joylashtirish ko'p konflikt keltirishi mumkin."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Uyda vertikal o'tishi mumkin bo'lgan tizimlarni ro'yxat qiling."},
    ],
    "L11_M04_002": [
        {"title": "Shaft", "type": "highlight", "text": "Shaft bir yoki bir necha muhandislik tizimini qavatlar orasida olib o'tish uchun xizmat qilishi mumkin."},
        {"title": "Access", "type": "normal", "text": "Texnik xizmat va inspeksiya imkoniyati ham hisobga olinadi."},
        {"title": "Tasodifiy joy", "type": "warning", "text": "Shaftni mebel, opening yoki konstruktsiya bilan konflikt qiladigan joyga qo'ymang."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Shaft uchun 5 ta joylashuv mezonini yozing."},
    ],
    "L11_M04_003": [
        {"title": "Wet stack", "type": "highlight", "text": "Upper floor sanuzelni pastdagi wet/service zona bilan mantiqiy bog'lash ko'pincha foydali."},
        {"title": "Shortest logic", "type": "normal", "text": "Muhandislik yo'li imkon qadar tushunarli va koordinatsiyalangan bo'lishi kerak."},
        {"title": "Xato", "type": "warning", "text": "Muhandislik yo'lini konstruktiv elementni keyin kesish hisobiga hal qilishga suyanmang."},
        {"title": "Mini-amaliyot", "type": "example", "text": "1- va 2-qavat wet zonalarini overlay qilib tekshiring."},
    ],
    "L11_M04_004": [
        {"title": "Penetration", "type": "highlight", "text": "Plita yoki devordan o'tuvchi MEP elementlari konstruktor bilan oldindan koordinatsiya qilinadi."},
        {"title": "Beam conflict", "type": "warning", "text": "Duct yoki katta quvurni beam orqali o'zboshimchalik bilan o'tkazish mumkin emas."},
        {"title": "BIM", "type": "normal", "text": "Plan, section va 3D orqali vertical routing tekshiriladi."},
        {"title": "Mini-amaliyot", "type": "example", "text": "5 ta potensial MEP-structure conflict yozing."},
    ],
    "L11_M04_005": [
        {"title": "Vertical audit", "type": "highlight", "text": "Wet zones → shafts → risers → penetrations → structure → maintenance → BIM audit."},
        {"title": "Professional checklist", "type": "example", "text": "1. Shaftlar joyi aniqmi?<br><br>2. Wet stack ishlaydimi?<br><br>3. Plita penetratsiyalari ko'rilganmi?<br><br>4. Beam konflikt yo'qmi?<br><br>5. Access mavjudmi?<br><br>6. Plan/section/3D mosmi?"},
        {"title": "Keyingi modul", "type": "highlight", "text": "Keyingi modul: VOID VA IKKINCHI YORUG'LIK."},
    ],
}


LEVEL11_MODULE04_QUIZ = {}

for i, lesson_code in enumerate(
    ["L11_M04_001", "L11_M04_002", "L11_M04_003", "L11_M04_004", "L11_M04_005"]
):
    start = 46 + i * 3

    LEVEL11_MODULE04_QUIZ[lesson_code] = [
        {
            "code": f"L11_Q{start:03d}",
            "question": "Vertikal MEP yo'llari arxitektura bilan oldindan koordinatsiya qilinadimi?",
            "explanation": "Shaft va riserlar real joy talab qiladi.",
            "options": [("A", "Ha", True), ("B", "Yo'q", False)],
        },
        {
            "code": f"L11_Q{start + 1:03d}",
            "question": "MEP elementini konstruktiv beam orqali o'zboshimchalik bilan o'tkazish to'g'rimi?",
            "explanation": "Konstruktor bilan koordinatsiya kerak.",
            "options": [("A", "Ha", False), ("B", "Yo'q", True)],
        },
        {
            "code": f"L11_Q{start + 2:03d}",
            "question": "Wet stack MEP tizimini soddalashtirishi mumkinmi?",
            "explanation": "Vertikal routingni mantiqiy qiladi.",
            "options": [("A", "Ha", True), ("B", "Yo'q", False)],
        },
    ]


def seed_level11_module04():
    connection = get_connection()
    try:
        cursor = connection.cursor()

        for row in LEVEL11_MODULE04_LESSONS:
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
