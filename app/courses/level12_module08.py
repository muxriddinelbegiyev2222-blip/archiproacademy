from database.database import get_connection


LEVEL12_MODULE08_LESSONS = [
    ("L12_M08", "L12_M08_001", "DWG exchange tushunchasi", "theory", "BIM va CAD workflowlari orasida ma'lumot almashish mantig'ini tushunish.", 1, 40, 20),
    ("L12_M08", "L12_M08_002", "Layer va mapping mantig'i", "theory", "Eksport/importda grafik struktura qanday boshqarilishini tushunish.", 2, 45, 20),
    ("L12_M08", "L12_M08_003", "Scale, units va origin", "practice", "DWG almashinuvda koordinata va birlik muammolarini oldini olish.", 3, 50, 20),
    ("L12_M08", "L12_M08_004", "DWG QA va round-trip", "practice", "Eksport qilingan faylni qayta tekshirish.", 4, 50, 20),
    ("L12_M08", "L12_M08_005", "DWG professional audit", "practice", "CAD almashinuv paketini kompleks nazorat qilish.", 5, 55, 25),
]


LEVEL12_MODULE08_CONTENT = {
    "L12_M08_001": [
        {"title": "BIM ↔ CAD", "type": "highlight", "text": "DWG boshqa mutaxassis yoki tizim bilan 2D/3D CAD ma'lumot almashish vositasi bo'lishi mumkin."},
        {"title": "Maqsadni aniqlang", "type": "normal", "text": "Eksport kim uchun va nima uchun kerakligi translator sozlamasiga ta'sir qiladi."},
        {"title": "Default export", "type": "warning", "text": "Har loyihaga bir xil tekshirilmagan default export ishlatish muammo keltirishi mumkin."},
        {"title": "Mini-amaliyot", "type": "example", "text": "DWG kerak bo'lishi mumkin bo'lgan 4 ta hamkorlik ssenariysini yozing."},
    ],
    "L12_M08_002": [
        {"title": "Layer mapping", "type": "highlight", "text": "BIMdagi element va layer strukturasi DWG'da qanday aks etishi oldindan boshqariladi."},
        {"title": "Recipient", "type": "normal", "text": "Qabul qiluvchi mutaxassis uchun tushunarli CAD struktura kerak."},
        {"title": "Layer chaos", "type": "warning", "text": "Eksportdan keyin yuzlab tushunarsiz layerlar hamkorlikni qiyinlashtiradi."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Architectural DWG uchun layer naming prinsiplarini yozing."},
    ],
    "L12_M08_003": [
        {"title": "Units", "type": "highlight", "text": "Import/exportda birliklar noto'g'ri bo'lsa geometriya noto'g'ri scale'da kelishi mumkin."},
        {"title": "Origin", "type": "normal", "text": "Koordinata va referens nuqta hamkorlikda kritik bo'lishi mumkin."},
        {"title": "Ko'z bilan to'g'rilash", "type": "warning", "text": "Noto'g'ri joylashgan faylni taxminan surib moslashtirish koordinatsiya sifatini pasaytiradi."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Units/origin bo'yicha exchange checklist yozing."},
    ],
    "L12_M08_004": [
        {"title": "Round-trip QA", "type": "highlight", "text": "Eksport qilingan DWGni boshqa viewer yoki qayta ochish orqali tekshirish foydali."},
        {"title": "Tekshiriladi", "type": "normal", "text": "Geometry, text, dimensions, layers, units va file completeness."},
        {"title": "Fayl yaratildi = to'g'ri emas", "type": "warning", "text": "Eksport jarayoni xatosiz tugagani output to'g'ri ekanini kafolatlamaydi."},
        {"title": "Mini-amaliyot", "type": "example", "text": "DWG QA uchun 8 ta savol yozing."},
    ],
    "L12_M08_005": [
        {"title": "DWG audit", "type": "highlight", "text": "Purpose → translator → layers → units → origin → export → reopen → QA → deliver."},
        {"title": "Professional checklist", "type": "example", "text": "1. Recipient ma'lummi?<br><br>2. Translator mosmi?<br><br>3. Layer mapping tekshirildimi?<br><br>4. Units to'g'rimi?<br><br>5. Origin to'g'rimi?<br><br>6. Text/dimensions saqlanganmi?<br><br>7. Fayl qayta ochildimi?"},
        {"title": "Keyingi modul", "type": "highlight", "text": "Keyingi modul: IFC ASOSLARI."},
    ],
}


LEVEL12_MODULE08_QUIZ = {}

for i, lesson_code in enumerate(
    ["L12_M08_001", "L12_M08_002", "L12_M08_003", "L12_M08_004", "L12_M08_005"]
):
    start = 106 + i * 3

    LEVEL12_MODULE08_QUIZ[lesson_code] = [
        {
            "code": f"L12_Q{start:03d}",
            "question": "DWG BIM va CAD workflowlari orasida ma'lumot almashishda ishlatilishi mumkinmi?",
            "explanation": "CAD formatlari hamkorlikda ishlatilishi mumkin.",
            "options": [("A", "Ha", True), ("B", "Yo'q", False)],
        },
        {
            "code": f"L12_Q{start + 1:03d}",
            "question": "Units va origin DWG almashinuvda muhimmi?",
            "explanation": "Scale va koordinata xatolarini oldini olish uchun muhim.",
            "options": [("A", "Ha", True), ("B", "Yo'q", False)],
        },
        {
            "code": f"L12_Q{start + 2:03d}",
            "question": "Eksport qilingan DWGni qayta tekshirish shart emasmi?",
            "explanation": "Output QA tavsiya etiladi.",
            "options": [("A", "Ha", False), ("B", "Yo'q", True)],
        },
    ]


def seed_level12_module08():
    connection = get_connection()
    try:
        cursor = connection.cursor()

        for row in LEVEL12_MODULE08_LESSONS:
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
