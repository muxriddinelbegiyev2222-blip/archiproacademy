from database.database import get_connection


LEVEL13_MODULE03_LESSONS = [
    ("L13_M03", "L13_M03_001", "Budjet va arxitektura", "theory", "Budjetning loyiha qarorlariga ta'sirini tushunish.", 1, 40, 20),
    ("L13_M03", "L13_M03_002", "Scope va budjet", "theory", "Loyiha hajmi va talablarni moliyaviy cheklov bilan bog'lash.", 2, 45, 20),
    ("L13_M03", "L13_M03_003", "Qimmat qarorlarni tanish", "practice", "Murakkab geometriya va boshqa qarorlarning xarajatga ta'sirini tushunish.", 3, 50, 20),
    ("L13_M03", "L13_M03_004", "Value engineering fikrlashi", "practice", "Asosiy g'oyani saqlab xarajatni optimallashtirish.", 4, 50, 20),
    ("L13_M03", "L13_M03_005", "Budjet professional audit", "practice", "Loyiha talablarini budjet bilan muntazam tekshirish.", 5, 55, 25),
]


LEVEL13_MODULE03_CONTENT = {
    "L13_M03_001": [
        {"title": "Budjetni boshida biling", "type": "highlight", "text": "Budjet loyiha oxirida paydo bo'ladigan muammo emas. U konsepsiyaga boshidan ta'sir qiladi."},
        {"title": "Arxitektor roli", "type": "normal", "text": "Arxitektor aniq qurilish narxini kafolatlamasdan, qarorlarning nisbiy murakkabligini tushuntirishi mumkin."},
        {"title": "Xato", "type": "warning", "text": "Tasdiqlanmagan bozor narxini aniq final smeta sifatida va'da qilmang."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Budjetga ta'sir qiluvchi 10 ta arxitektura qarorini yozing."},
    ],
    "L13_M03_002": [
        {"title": "Scope", "type": "highlight", "text": "Uy maydoni, funksiyalar soni, murakkablik va finish darajasi umumiy xarajatga ta'sir qilishi mumkin."},
        {"title": "Priorities", "type": "normal", "text": "Budjet cheklansa MUST HAVE funksiyalar birinchi himoya qilinadi."},
        {"title": "Hammasini saqlash", "type": "warning", "text": "Budjet kamayib, scope o'zgarmasa sifat yoki real bajarilishda konflikt paydo bo'lishi mumkin."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Budget cut bo'lsa qaysi talablar saqlanishini belgilab chiqing."},
    ],
    "L13_M03_003": [
        {"title": "Murakkablik narxi", "type": "highlight", "text": "Ko'p corner, murakkab tom, katta konsol yoki maxsus elementlar qurilish murakkabligini oshirishi mumkin."},
        {"title": "Oddiy = yomon emas", "type": "normal", "text": "Sodda va aniq geometriya ham kuchli arxitektura yaratishi mumkin."},
        {"title": "Faqat ko'rinish", "type": "warning", "text": "Bitta vizual effekt uchun katta konstruktiv yoki texnik murakkablik yaratishdan oldin qiymatini baholang."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Loyihangizdagi 5 ta high-cost-risk elementni toping."},
    ],
    "L13_M03_004": [
        {"title": "Value engineering", "type": "highlight", "text": "Maqsad arzonlashtirish emas, muhim qiymatni saqlab ortiqcha xarajatni kamaytirish."},
        {"title": "Savol", "type": "normal", "text": "Bu element loyiha sifatiga qancha real qiymat qo'shyapti?"},
        {"title": "Sifatni ko'r-ko'rona kesmang", "type": "warning", "text": "Faqat narx uchun kritik funksional yoki texnik sifatni yo'qotmang."},
        {"title": "Mini-amaliyot", "type": "example", "text": "3 ta qimmat qarorga soddaroq alternativ taklif qiling."},
    ],
    "L13_M03_005": [
        {"title": "Budjet audit", "type": "highlight", "text": "Budget → scope → priorities → complexity → alternatives → client decision → record."},
        {"title": "Professional checklist", "type": "example", "text": "1. Budget range gaplashildimi?<br><br>2. Scope mosmi?<br><br>3. MUST HAVE aniqmi?<br><br>4. High-cost risks topildimi?<br><br>5. Alternativlar bormi?<br><br>6. Mijoz qarori qayd qilindimi?"},
        {"title": "Keyingi modul", "type": "highlight", "text": "Keyingi modul: VARIANTLAR TAYYORLASH."},
    ],
}


LEVEL13_MODULE03_QUIZ = {}

for i, lesson_code in enumerate(
    ["L13_M03_001", "L13_M03_002", "L13_M03_003", "L13_M03_004", "L13_M03_005"]
):
    start = 31 + i * 3

    LEVEL13_MODULE03_QUIZ[lesson_code] = [
        {
            "code": f"L13_Q{start:03d}",
            "question": "Budjet loyiha konsepsiyasiga boshidan ta'sir qilishi mumkinmi?",
            "explanation": "Scope va murakkablik budjet bilan bog'liq.",
            "options": [("A", "Ha", True), ("B", "Yo'q", False)],
        },
        {
            "code": f"L13_Q{start + 1:03d}",
            "question": "Tasdiqlanmagan taxminiy narxni kafolatlangan final smeta sifatida aytish to'g'rimi?",
            "explanation": "Aniq smeta tegishli hisob va mutaxassislar bilan tasdiqlanishi kerak.",
            "options": [("A", "Ha", False), ("B", "Yo'q", True)],
        },
        {
            "code": f"L13_Q{start + 2:03d}",
            "question": "Value engineering muhim qiymatni saqlab ortiqcha xarajatni kamaytirishga intiladimi?",
            "explanation": "Maqsad shunchaki arzonlashtirish emas.",
            "options": [("A", "Ha", True), ("B", "Yo'q", False)],
        },
    ]


def seed_level13_module03():
    connection = get_connection()
    try:
        cursor = connection.cursor()

        for row in LEVEL13_MODULE03_LESSONS:
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
