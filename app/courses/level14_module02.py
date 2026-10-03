from database.database import get_connection


LEVEL14_MODULE02_LESSONS = [
    ("L14_M02", "L14_M02_001", "Murakkab uchastkani o'qish", "theory", "Noto'g'ri shakldagi chegaralarni loyiha ma'lumotiga aylantirish.", 1, 60, 20),
    ("L14_M02", "L14_M02_002", "Asosiy bino o'qini tanlash", "theory", "Murakkab chegara ichida sodda va mantiqiy bino geometriyasini tashkil qilish.", 2, 70, 20),
    ("L14_M02", "L14_M02_003", "Qolgan zonalardan foydalanish", "practice", "Noto'g'ri geometriyadagi qolgan maydonlarni hovli va yordamchi funksiyalarga aylantirish.", 3, 70, 20),
    ("L14_M02", "L14_M02_004", "Fasad va perspektiva nazorati", "practice", "Murakkab site ichida binoning ko'cha va hovli bilan vizual aloqasini boshqarish.", 4, 75, 20),
    ("L14_M02", "L14_M02_005", "Murakkab uchastka professional audit", "practice", "Noto'g'ri shakldagi uchastka loyihasini kompleks tekshirish.", 5, 85, 25),
]


LEVEL14_MODULE02_CONTENT = {
    "L14_M02_001": [
        {"title": "Chegara shakli bino shakli emas", "type": "highlight", "text": "Uchastka qiyshiq bo'lsa bino ham barcha chegarani takrorlashi shart emas."},
        {"title": "Tahlil", "type": "normal", "text": "Eng muhim chegaralar, ko'cha, orientatsiya, kirish va foydalanish mumkin bo'lgan zonalar aniqlanadi."},
        {"title": "Xato", "type": "warning", "text": "Har bir qiyshiq chegarani devor geometriyasiga aylantirish ortiqcha murakkablik yaratishi mumkin."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Murakkab uchastkada primary va secondary chegaralarni belgilang."},
    ],
    "L14_M02_002": [
        {"title": "Asosiy o'q", "type": "highlight", "text": "Bino geometriyasi uchun aniq referens o'q yoki grid tanlash loyiha boshqaruvini osonlashtiradi."},
        {"title": "Soddalik", "type": "normal", "text": "Murakkab site ichida sodda bino massing ko'pincha kuchli kontrast va tartib yaratishi mumkin."},
        {"title": "Ko'p burchak", "type": "warning", "text": "Foydasiz o'tkir burchaklar mebel, konstruktsiya va qurilishni qiyinlashtiradi."},
        {"title": "Mini-amaliyot", "type": "example", "text": "3 xil bino o'qi variantini solishtiring."},
    ],
    "L14_M02_003": [
        {"title": "Qolgan maydon — imkoniyat", "type": "highlight", "text": "Bino sig'magan geometriya courtyard, landscape, service yoki buffer zonaga aylanishi mumkin."},
        {"title": "Micro-zones", "type": "normal", "text": "Kichik uchburchak yoki qiyshiq hudud ham maqsadli tashqi funksiya olishi mumkin."},
        {"title": "Tasodifiy qoldiq", "type": "warning", "text": "Har bir qolgan zona uchun real foydalanish yoki landshaft mantiqi bo'lishi kerak."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Qolgan maydonlarni 4 funksional kategoriyaga ajrating."},
    ],
    "L14_M02_004": [
        {"title": "Perspective control", "type": "highlight", "text": "Qiyshiq street line yoki kirish binoni turli burchakdan ko'rsatishi mumkin."},
        {"title": "Facade response", "type": "normal", "text": "Asosiy kirish va fasad kompozitsiyasi ko'cha yo'nalishi bilan dialog quradi."},
        {"title": "Xato", "type": "warning", "text": "Faqat plan geometriyasini ko'rib, real ko'cha perspektivasini unutmaslik kerak."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Site'dagi 3 asosiy ko'rish nuqtasini belgilang."},
    ],
    "L14_M02_005": [
        {"title": "Audit", "type": "highlight", "text": "Boundary → primary axis → building geometry → residual zones → circulation → facade → structure → audit."},
        {"title": "Professional checklist", "type": "example", "text": "1. Asosiy o'q aniqmi?<br><br>2. Bino geometriyasi keraksiz murakkab emasmi?<br><br>3. Qoldiq zonalar ishlaydimi?<br><br>4. Kirish tushunarlimi?<br><br>5. Street perspective ko'rildimi?<br><br>6. Konstruktsiya mantiqiymi?"},
        {"title": "Keyingi modul", "type": "highlight", "text": "Keyingi modul: NISHABLI YER."},
    ],
}


LEVEL14_MODULE02_QUIZ = {}

for i, lesson_code in enumerate(
    ["L14_M02_001", "L14_M02_002", "L14_M02_003", "L14_M02_004", "L14_M02_005"]
):
    start = 16 + i * 3

    LEVEL14_MODULE02_QUIZ[lesson_code] = [
        {
            "code": f"L14_Q{start:03d}",
            "question": "Qiyshiq uchastka chegarasi bino devori ham aynan qiyshiq bo'lishini majbur qiladimi?",
            "explanation": "Bino uchun mustaqil, mantiqiy geometriya tanlanishi mumkin.",
            "options": [("A", "Ha", False), ("B", "Yo'q", True)],
        },
        {
            "code": f"L14_Q{start + 1:03d}",
            "question": "Murakkab uchastkada aniq bino o'qi yoki grid foydalimi?",
            "explanation": "Geometriya va koordinatsiya tartibli bo'ladi.",
            "options": [("A", "Ha", True), ("B", "Yo'q", False)],
        },
        {
            "code": f"L14_Q{start + 2:03d}",
            "question": "Qolgan noto'g'ri shakldagi zonalarga ham funksiya berish mumkinmi?",
            "explanation": "Landscape, courtyard yoki service zona bo'lishi mumkin.",
            "options": [("A", "Ha", True), ("B", "Yo'q", False)],
        },
    ]


def seed_level14_module02():
    connection = get_connection()
    try:
        cursor = connection.cursor()

        for row in LEVEL14_MODULE02_LESSONS:
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
