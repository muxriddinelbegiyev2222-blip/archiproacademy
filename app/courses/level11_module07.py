from database.database import get_connection


LEVEL11_MODULE07_LESSONS = [
    ("L11_M07", "L11_M07_001", "Ikki qavatli fasad proporsiyasi", "theory", "Balandroq bino hajmida fasad nisbatlarini boshqarish.", 1, 60, 20),
    ("L11_M07", "L11_M07_002", "Qavatlar orasidagi vizual aloqa", "theory", "Opening va massing orqali qavatlarni yagona kompozitsiyaga birlashtirish.", 2, 70, 20),
    ("L11_M07", "L11_M07_003", "Balkon, void va stair aksenti", "practice", "Vertikal elementlarni fasadga integratsiya qilish.", 3, 70, 20),
    ("L11_M07", "L11_M07_004", "Material va hajm PRO", "practice", "Materiallarni qavat va massing bilan professional boshqarish.", 4, 75, 20),
    ("L11_M07", "L11_M07_005", "2 qavatli fasad audit", "practice", "Barcha fasadlarni yagona kompozitsiya sifatida tekshirish.", 5, 85, 25),
]


LEVEL11_MODULE07_CONTENT = {
    "L11_M07_001": [
        {"title": "Balandlik proporsiyani o'zgartiradi", "type": "highlight", "text": "2 qavatli fasad bir qavatli fasaddan boshqa vertikal nisbatga ega."},
        {"title": "Base / middle / top", "type": "normal", "text": "Fasadni sokol, asosiy hajm va tom/siluet orqali o'qish mumkin."},
        {"title": "Xato", "type": "warning", "text": "1- va 2-qavat fasadini alohida-alohida bezab, umumiy kompozitsiyani yo'qotmang."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Old fasadni vertical proportion zonalariga ajrating."},
    ],
    "L11_M07_002": [
        {"title": "Opening alignment", "type": "highlight", "text": "Derazalarning qavatlar bo'yicha munosabati fasad ritmiga ta'sir qiladi."},
        {"title": "Alignment shart emas, mantiq kerak", "type": "normal", "text": "Barcha derazalar aynan bir chiziqda bo'lishi shart emas, lekin kompozitsion sabab bo'lishi kerak."},
        {"title": "Tasodif", "type": "warning", "text": "Har qavatdagi openinglarni mustaqil joylashtirish fasadni tartibsiz qilishi mumkin."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Opening rhythm uchun 3 variant solishtiring."},
    ],
    "L11_M07_003": [
        {"title": "Vertikal aksent", "type": "highlight", "text": "Stair window, void yoki kirish 2 qavatli fasadda vertikal aksent yaratishi mumkin."},
        {"title": "Balkon", "type": "normal", "text": "Balkon fasad hajmi va soya kompozitsiyasiga ta'sir qiladi."},
        {"title": "Ortiqcha effekt", "type": "warning", "text": "Har elementni aksentga aylantirsangiz hierarxiya yo'qoladi."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Dominant, secondary va neutral fasad elementlarini belgilang."},
    ],
    "L11_M07_004": [
        {"title": "Material bilan bo'lish", "type": "highlight", "text": "Material o'zgarishi bino hajmini tushunarli yoki aksincha parchalangan ko'rsatishi mumkin."},
        {"title": "Vertical / horizontal", "type": "normal", "text": "Material orqali vertikal yoki gorizontal kompozitsiya kuchaytirilishi mumkin."},
        {"title": "Ko'p material", "type": "warning", "text": "Material sonini ko'paytirish professional ko'rinishni kafolatlamaydi."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Primary, secondary va accent material strategiyasini yozing."},
    ],
    "L11_M07_005": [
        {"title": "Fasad audit", "type": "highlight", "text": "Plan → qavatlar → openings → stair/void → balcony → massing → material → roof → 4 elevations."},
        {"title": "Professional checklist", "type": "example", "text": "1. Qavatlar yagona kompozitsiyami?<br><br>2. Opening ritmi bormi?<br><br>3. Kirish aniqmi?<br><br>4. Stair/void mantiqan ko'rinadimi?<br><br>5. Balkon integratsiya qilinganmi?<br><br>6. Material strategiyasi sodda-mi?<br><br>7. Barcha fasadlar mosmi?"},
        {"title": "Keyingi modul", "type": "highlight", "text": "Keyingi modul: TO'LIQ ARCHICAD MODEL."},
    ],
}


LEVEL11_MODULE07_QUIZ = {}

for i, lesson_code in enumerate(
    ["L11_M07_001", "L11_M07_002", "L11_M07_003", "L11_M07_004", "L11_M07_005"]
):
    start = 91 + i * 3

    LEVEL11_MODULE07_QUIZ[lesson_code] = [
        {
            "code": f"L11_Q{start:03d}",
            "question": "2 qavatli fasadda qavatlar yagona kompozitsiya sifatida ko'riladimi?",
            "explanation": "Bino bitta umumiy massing va fasadga ega.",
            "options": [("A", "Ha", True), ("B", "Yo'q", False)],
        },
        {
            "code": f"L11_Q{start + 1:03d}",
            "question": "Opening va materiallarni tasodifiy joylashtirish professional fasad yaratadimi?",
            "explanation": "Kompozitsion mantiq kerak.",
            "options": [("A", "Ha", False), ("B", "Yo'q", True)],
        },
        {
            "code": f"L11_Q{start + 2:03d}",
            "question": "Balkon, stair va void fasad kompozitsiyasiga ta'sir qiladimi?",
            "explanation": "Ular tashqi hajm va ritmda ko'rinadi.",
            "options": [("A", "Ha", True), ("B", "Yo'q", False)],
        },
    ]


def seed_level11_module07():
    connection = get_connection()
    try:
        cursor = connection.cursor()

        for row in LEVEL11_MODULE07_LESSONS:
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
