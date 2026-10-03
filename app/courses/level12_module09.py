from database.database import get_connection


LEVEL12_MODULE09_LESSONS = [
    ("L12_M09", "L12_M09_001", "IFC tushunchasi", "theory", "BIM modellar orasida ochiq ma'lumot almashinuvi mantig'ini tushunish.", 1, 40, 20),
    ("L12_M09", "L12_M09_002", "Classification va IFC data", "theory", "Element identifikatsiyasi va klassifikatsiyaning almashinuvdagi rolini tushunish.", 2, 45, 20),
    ("L12_M09", "L12_M09_003", "Model exchange scope", "practice", "Qaysi element va ma'lumotlar almashinuvga kirishini belgilash.", 3, 50, 20),
    ("L12_M09", "L12_M09_004", "IFC QA", "practice", "Eksport qilingan model geometriyasi va ma'lumotlarini tekshirish.", 4, 50, 20),
    ("L12_M09", "L12_M09_005", "IFC professional audit", "practice", "BIM exchange paketini kompleks nazorat qilish.", 5, 55, 25),
]


LEVEL12_MODULE09_CONTENT = {
    "L12_M09_001": [
        {"title": "Open BIM g'oyasi", "type": "highlight", "text": "IFC turli BIM dasturlari orasida model va ma'lumot almashish uchun ishlatiladigan ochiq formatlardan biridir."},
        {"title": "Native file emas", "type": "normal", "text": "IFC boshqa dasturga aynan native project faylning barcha ichki funksiyalarini ko'chirish degani emas."},
        {"title": "Xato kutish", "type": "warning", "text": "IFC exportdan keyin barcha native parametrlar bir xil ishlaydi deb taxmin qilmang."},
        {"title": "Mini-amaliyot", "type": "example", "text": "IFC exchange kerak bo'lishi mumkin bo'lgan 3 ta hamkorlik holatini yozing."},
    ],
    "L12_M09_002": [
        {"title": "Classification", "type": "highlight", "text": "Element qaysi turdagi obyekt ekanini to'g'ri aniqlash exchange sifatiga yordam beradi."},
        {"title": "Data", "type": "normal", "text": "Kerakli property va classificationlar exchange maqsadiga qarab tayyorlanadi."},
        {"title": "Garbage in → garbage out", "type": "warning", "text": "Model data noto'g'ri bo'lsa eksport formati uni avtomatik tuzatmaydi."},
        {"title": "Mini-amaliyot", "type": "example", "text": "IFC oldidan element data audit checklist tuzing."},
    ],
    "L12_M09_003": [
        {"title": "Scope", "type": "highlight", "text": "Har exchange'da butun model kerak bo'lmasligi mumkin. Topshirish maqsadi aniqlanadi."},
        {"title": "Recipient need", "type": "normal", "text": "Konstruktor, MEP yoki boshqa mutaxassisga kerakli model scope farq qilishi mumkin."},
        {"title": "Ortiqcha data", "type": "warning", "text": "Keraksiz yoki maxfiy loyiha ma'lumotini nazoratsiz topshirmang."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Structural coordination uchun kerakli IFC scope ro'yxatini yozing."},
    ],
    "L12_M09_004": [
        {"title": "IFC QA", "type": "highlight", "text": "Eksport modelni alohida viewer yoki boshqa muhitda tekshirish foydali."},
        {"title": "Tekshiriladi", "type": "normal", "text": "Element count, geometry, storeys, classification, property va location."},
        {"title": "Faqat fayl hajmiga qaramang", "type": "warning", "text": "Fayl ochilishi model ma'lumoti to'liq va to'g'ri ekanini anglatmaydi."},
        {"title": "Mini-amaliyot", "type": "example", "text": "IFC QA uchun 10 ta savol yozing."},
    ],
    "L12_M09_005": [
        {"title": "IFC audit", "type": "highlight", "text": "Purpose → scope → classification → properties → export settings → viewer QA → issue log → deliver."},
        {"title": "Professional checklist", "type": "example", "text": "1. Exchange maqsadi aniqmi?<br><br>2. Scope to'g'rimi?<br><br>3. Classification tekshirildimi?<br><br>4. Properties to'g'rimi?<br><br>5. Storeys mosmi?<br><br>6. Geometry buzilmaganmi?<br><br>7. Viewer'da tekshirildimi?<br><br>8. Issue log bormi?"},
        {"title": "Keyingi modul", "type": "highlight", "text": "Keyingi modul: FINAL LOYIHA ALBOMI."},
    ],
}


LEVEL12_MODULE09_QUIZ = {}

for i, lesson_code in enumerate(
    ["L12_M09_001", "L12_M09_002", "L12_M09_003", "L12_M09_004", "L12_M09_005"]
):
    start = 121 + i * 3

    LEVEL12_MODULE09_QUIZ[lesson_code] = [
        {
            "code": f"L12_Q{start:03d}",
            "question": "IFC turli BIM tizimlari orasida model almashishda ishlatilishi mumkinmi?",
            "explanation": "IFC Open BIM exchange formatlaridan biridir.",
            "options": [("A", "Ha", True), ("B", "Yo'q", False)],
        },
        {
            "code": f"L12_Q{start + 1:03d}",
            "question": "IFC export noto'g'ri model data'ni avtomatik to'g'rilaydimi?",
            "explanation": "Model data avvaldan to'g'ri tayyorlanishi kerak.",
            "options": [("A", "Ha", False), ("B", "Yo'q", True)],
        },
        {
            "code": f"L12_Q{start + 2:03d}",
            "question": "IFC eksport qilingandan keyin viewer orqali QA qilish foydalimi?",
            "explanation": "Geometry va data exchange natijasini tekshirish mumkin.",
            "options": [("A", "Ha", True), ("B", "Yo'q", False)],
        },
    ]


def seed_level12_module09():
    connection = get_connection()
    try:
        cursor = connection.cursor()

        for row in LEVEL12_MODULE09_LESSONS:
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
