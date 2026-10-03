from database.database import get_connection


LEVEL12_MODULE07_LESSONS = [
    ("L12_M07", "L12_M07_001", "Publisher tushunchasi", "theory", "Loyiha outputlarini boshqariladigan to'plam sifatida chiqarish mantig'ini tushunish.", 1, 40, 20),
    ("L12_M07", "L12_M07_002", "Publisher Set", "theory", "Topshiriladigan chizma va fayllarni guruhlarga ajratish.", 2, 45, 20),
    ("L12_M07", "L12_M07_003", "Output naming", "practice", "Eksport fayllarini izchil nomlash.", 3, 50, 20),
    ("L12_M07", "L12_M07_004", "PDF va boshqa deliverable nazorati", "practice", "Eksportdan oldin va keyin output sifatini tekshirish.", 4, 50, 20),
    ("L12_M07", "L12_M07_005", "Publisher professional audit", "practice", "Topshirish paketini to'liq nazorat qilish.", 5, 55, 25),
]


LEVEL12_MODULE07_CONTENT = {
    "L12_M07_001": [
        {"title": "Output boshqaruvi", "type": "highlight", "text": "Publisher loyiha hujjatlarini qayta-qayta izchil chiqarish workflow'ini yaratishga yordam beradi."},
        {"title": "Maqsad", "type": "normal", "text": "Qaysi layoutlar, qanday formatda va qaysi nom bilan topshirilishi oldindan boshqariladi."},
        {"title": "Manual chaos", "type": "warning", "text": "Har safar alohida-alohida qo'lda export qilish noto'g'ri sheet yoki eski fayl chiqarish xavfini oshiradi."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Final loyiha uchun deliverable ro'yxatini yozing."},
    ],
    "L12_M07_002": [
        {"title": "Publisher Set", "type": "highlight", "text": "Turli topshirish maqsadlari uchun alohida output to'plamlari tashkil qilinishi mumkin."},
        {"title": "Misol", "type": "normal", "text": "Client PDF, working drawings va exchange files turli setlarda boshqarilishi mumkin."},
        {"title": "Keraksiz sheet", "type": "warning", "text": "Final setga test yoki eski layoutlar tasodifan kirib qolmasligi kerak."},
        {"title": "Mini-amaliyot", "type": "example", "text": "3 ta Publisher Set konsepsiyasini yozing."},
    ],
    "L12_M07_003": [
        {"title": "File naming", "type": "highlight", "text": "Eksport fayli nomidan loyiha, paket yoki versiyani tushunish foydali."},
        {"title": "Consistency", "type": "normal", "text": "Bir xil naming convention topshirish tartibini yaxshilaydi."},
        {"title": "final_final2", "type": "warning", "text": "Nazorat qilinmagan filename versiyalari chalkashlik tug'diradi."},
        {"title": "Mini-amaliyot", "type": "example", "text": "PDF va DWG output uchun naming convention yarating."},
    ],
    "L12_M07_004": [
        {"title": "Exportdan keyin ham audit", "type": "highlight", "text": "Fayl yaratilgani uning to'g'ri ekanini anglatmaydi."},
        {"title": "Tekshiruv", "type": "normal", "text": "Page count, orientation, scale, missing drawing, text va boshqa output sifati ko'riladi."},
        {"title": "Blind publish", "type": "warning", "text": "Publish bosib faylni ochib tekshirmasdan yubormang."},
        {"title": "Mini-amaliyot", "type": "example", "text": "PDF output uchun 10 bandli QA checklist tuzing."},
    ],
    "L12_M07_005": [
        {"title": "Publisher audit", "type": "highlight", "text": "Set → layouts → naming → format → destination → publish → open → QA → deliver."},
        {"title": "Professional checklist", "type": "example", "text": "1. To'g'ri set tanlandimi?<br><br>2. Eski layout yo'qmi?<br><br>3. Naming to'g'rimi?<br><br>4. Format mosmi?<br><br>5. Barcha sahifa chiqdidimi?<br><br>6. Export ochib tekshirildimi?<br><br>7. Faqat tekshirilgan paket yuborilyaptimi?"},
        {"title": "Keyingi modul", "type": "highlight", "text": "Keyingi modul: DWG ALMASHINUVI."},
    ],
}


LEVEL12_MODULE07_QUIZ = {}

for i, lesson_code in enumerate(
    ["L12_M07_001", "L12_M07_002", "L12_M07_003", "L12_M07_004", "L12_M07_005"]
):
    start = 91 + i * 3

    LEVEL12_MODULE07_QUIZ[lesson_code] = [
        {
            "code": f"L12_Q{start:03d}",
            "question": "Publisher loyiha outputlarini boshqarishga yordam beradimi?",
            "explanation": "Topshirish setlarini izchil chiqarish mumkin.",
            "options": [("A", "Ha", True), ("B", "Yo'q", False)],
        },
        {
            "code": f"L12_Q{start + 1:03d}",
            "question": "Export fayllarini izchil nomlash foydalimi?",
            "explanation": "Versiya va paketni tushunish osonlashadi.",
            "options": [("A", "Ha", True), ("B", "Yo'q", False)],
        },
        {
            "code": f"L12_Q{start + 2:03d}",
            "question": "Publish qilingandan keyin faylni tekshirmasdan yuborish idealmi?",
            "explanation": "Output QA zarur.",
            "options": [("A", "Ha", False), ("B", "Yo'q", True)],
        },
    ]


def seed_level12_module07():
    connection = get_connection()
    try:
        cursor = connection.cursor()

        for row in LEVEL12_MODULE07_LESSONS:
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
