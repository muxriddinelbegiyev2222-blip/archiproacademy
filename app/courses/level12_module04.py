from database.database import get_connection


LEVEL12_MODULE04_LESSONS = [
    ("L12_M04", "L12_M04_001", "View tushunchasi", "theory", "Model ko'rinishi va saqlangan view orasidagi farqni tushunish.", 1, 50, 20),
    ("L12_M04", "L12_M04_002", "View settings mantig'i", "theory", "Scale, layer, graphic va boshqa ko'rinish sozlamalarini boshqarish.", 2, 55, 20),
    ("L12_M04", "L12_M04_003", "View naming va folders", "practice", "View Map strukturasini loyiha hujjatlariga mos tashkil qilish.", 3, 60, 20),
    ("L12_M04", "L12_M04_004", "Documentation views", "practice", "Plan, section, elevation va schedule viewlarini izchil tayyorlash.", 4, 65, 20),
    ("L12_M04", "L12_M04_005", "View Map PRO audit", "practice", "Viewlar struktura va output consistency'sini tekshirish.", 5, 70, 25),
]


LEVEL12_MODULE04_CONTENT = {
    "L12_M04_001": [
        {"title": "Model view vs saved view", "type": "highlight", "text": "Saqlangan view ma'lum loyiha ko'rinishini va kerakli sozlamalarni qayta chaqirishga xizmat qiladi."},
        {"title": "Maqsad", "type": "normal", "text": "Bir xil chizmani har safar qo'lda sozlamasdan izchil olish."},
        {"title": "Xato", "type": "warning", "text": "Har safar layer va scale'ni qo'lda o'zgartirib chiqarish inconsistency yaratishi mumkin."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Loyihadagi kerakli saved view turlarini yozing."},
    ],
    "L12_M04_002": [
        {"title": "View settings", "type": "highlight", "text": "View kerakli grafik va ko'rinish konfiguratsiyasi bilan saqlanishi kerak."},
        {"title": "Consistency", "type": "normal", "text": "Bir turdagi hujjatlar bir xil standartga yaqin sozlamalarda ishlashi kerak."},
        {"title": "Noto'g'ri view", "type": "warning", "text": "Layoutga modeldagi tasodifiy current view emas, nazorat qilingan saved view qo'yish ma'qul."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Floor Plan documentation view uchun kerakli sozlamalar checklistini yozing."},
    ],
    "L12_M04_003": [
        {"title": "View Map tartibi", "type": "highlight", "text": "Viewlar plan, section, elevation, schedule va boshqa guruhlarga ajratilishi mumkin."},
        {"title": "Naming", "type": "normal", "text": "Nomdan view maqsadi va qaysi hujjatga tegishli ekanini tushunish foydali."},
        {"title": "View chaos", "type": "warning", "text": "Yuzlab 'Copy of...' kabi views loyiha boshqaruvini yomonlashtiradi."},
        {"title": "Mini-amaliyot", "type": "example", "text": "LEVEL 10/11 loyihangiz uchun View Map folder strukturasini yozing."},
    ],
    "L12_M04_004": [
        {"title": "Documentation set", "type": "highlight", "text": "Plans, sections, elevations, schedules va boshqa outputlar uchun alohida nazorat qilingan views yaratiladi."},
        {"title": "Bir model, ko'p maqsad", "type": "normal", "text": "Bir modeldan turli scale va grafik maqsaddagi views olinishi mumkin."},
        {"title": "Xato", "type": "warning", "text": "Presentation view bilan working drawing viewni chalkashtirmang."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Presentation va working documentation viewlari orasidagi farqlarni yozing."},
    ],
    "L12_M04_005": [
        {"title": "View audit", "type": "highlight", "text": "Purpose → name → folder → settings → graphic standard → layout link → output test."},
        {"title": "Professional checklist", "type": "example", "text": "1. View nomi tushunarlimi?<br><br>2. Folder to'g'rimi?<br><br>3. Scale mosmi?<br><br>4. Layer holati to'g'rimi?<br><br>5. Grafik sozlama to'g'rimi?<br><br>6. Layout bilan bog'langanmi?<br><br>7. Dublikat views tozalanganmi?"},
        {"title": "Keyingi modul", "type": "highlight", "text": "Keyingi modul: LAYOUT BOOK."},
    ],
}


LEVEL12_MODULE04_QUIZ = {}

for i, lesson_code in enumerate(
    ["L12_M04_001", "L12_M04_002", "L12_M04_003", "L12_M04_004", "L12_M04_005"]
):
    start = 46 + i * 3

    LEVEL12_MODULE04_QUIZ[lesson_code] = [
        {
            "code": f"L12_Q{start:03d}",
            "question": "Saved view hujjat ko'rinishi sozlamalarini izchil boshqarishga yordam beradimi?",
            "explanation": "View kerakli ko'rinish konfiguratsiyasini saqlaydi.",
            "options": [("A", "Ha", True), ("B", "Yo'q", False)],
        },
        {
            "code": f"L12_Q{start + 1:03d}",
            "question": "View Map'ni tartibli folder va naming bilan boshqarish foydalimi?",
            "explanation": "Loyiha navigatsiyasi va hujjatlashtirish osonlashadi.",
            "options": [("A", "Ha", True), ("B", "Yo'q", False)],
        },
        {
            "code": f"L12_Q{start + 2:03d}",
            "question": "Har safar tasodifiy current viewni layoutga qo'yish ideal workflow'mi?",
            "explanation": "Nazorat qilingan saved views izchilroq.",
            "options": [("A", "Ha", False), ("B", "Yo'q", True)],
        },
    ]


def seed_level12_module04():
    connection = get_connection()
    try:
        cursor = connection.cursor()

        for row in LEVEL12_MODULE04_LESSONS:
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
