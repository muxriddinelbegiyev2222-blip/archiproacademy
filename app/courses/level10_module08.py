from database.database import get_connection


LEVEL10_MODULE08_LESSONS = [
    ("L10_M08", "L10_M08_001", "Tom konsepsiyasi", "theory", "Bir qavatli uy tomini bino shakli va iqlim bilan bog'lash.", 1, 50, 20),
    ("L10_M08", "L10_M08_002", "Nishab va suv yo'li", "theory", "Tom geometriyasi va suv chiqarish mantig'ini tushunish.", 2, 55, 20),
    ("L10_M08", "L10_M08_003", "Ridge, eave va tutashuvlar", "practice", "Tomning asosiy geometrik zonalarini koordinatsiya qilish.", 3, 60, 20),
    ("L10_M08", "L10_M08_004", "Tom va fasad koordinatsiyasi", "practice", "Tom silueti, fasad va ichki reja aloqasini tekshirish.", 4, 65, 20),
    ("L10_M08", "L10_M08_005", "Tom professional audit", "practice", "Bir qavatli uy tomini kompleks tekshirish.", 5, 70, 25),
]


LEVEL10_MODULE08_CONTENT = {
    "L10_M08_001": [
        {"title": "Tom alohida obyekt emas", "type": "highlight", "text": "Tom bino hajmi, fasad, suv chiqarish va konstruksiya bilan birga ishlaydi."},
        {"title": "Konsepsiya", "type": "normal", "text": "Tom turi bino shakli va loyiha maqsadiga mos tanlanadi."},
        {"title": "Xato", "type": "warning", "text": "Faqat chiroyli silhouette uchun ortiqcha murakkab tom yaratish qurilishni qiyinlashtirishi mumkin."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Uy uchun 2-3 tom konsepsiyasini solishtiring."},
    ],
    "L10_M08_002": [
        {"title": "Suv yo'li", "type": "highlight", "text": "Tomdagi har bir nishab suv qayerga ketishini belgilaydi."},
        {"title": "Drainage", "type": "normal", "text": "Suv bino kirishi, terassa yoki noqulay zonaga tashlanmasligi kerak."},
        {"title": "Aniq nishab", "type": "warning", "text": "Aniq nishab qiymati tom materiali va texnik talablar asosida belgilanadi."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Tom planida suv oqim yo'nalishlarini strelka bilan ko'rsating."},
    ],
    "L10_M08_003": [
        {"title": "Ridge", "type": "normal", "text": "Ridge tomning yuqori tutashuv zonasini belgilaydi."},
        {"title": "Eave", "type": "normal", "text": "Eave fasad va suv chiqarish bilan bog'liq."},
        {"title": "Tutashuv", "type": "highlight", "text": "Murakkab tomlarda turli yuzalar uchrashadigan joylar alohida nazorat qilinadi."},
        {"title": "Xato", "type": "warning", "text": "Keraksiz ko'p ridge va valley tomni murakkablashtirishi mumkin."},
    ],
    "L10_M08_004": [
        {"title": "Tom + fasad", "type": "highlight", "text": "Tom balandligi, eave va ridge fasad proporsiyasiga kuchli ta'sir qiladi."},
        {"title": "Kirish", "type": "normal", "text": "Asosiy kirish ustidagi tom yechimi foydalanuvchi orientatsiyasiga ta'sir qilishi mumkin."},
        {"title": "Plan", "type": "normal", "text": "Ichki hajm va shift strategiyasi tom shakli bilan koordinatsiyada bo'lishi mumkin."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Tom o'zgarishining old, yon va orqa fasadga ta'sirini tekshiring."},
    ],
    "L10_M08_005": [
        {"title": "Tom audit", "type": "highlight", "text": "Massing → nishab → ridge/eave → drainage → openings → fasad → konstruktsiya → BIM audit."},
        {"title": "Professional checklist", "type": "example", "text": "1. Tom konsepsiyasi sodda-mi?<br><br>2. Suv yo'li tushunarlimi?<br><br>3. Ridge/eave mantiqi to'g'rimi?<br><br>4. Fasadlar bilan mosmi?<br><br>5. Openings koordinatsiya qilinganmi?<br><br>6. Konstruktiv mantiq tekshirilganmi?<br><br>7. 3D va section mosmi?"},
        {"title": "Xato", "type": "warning", "text": "Tom plan, fasad va sectionda har xil ko'rinsa model koordinatsiyasi buzilgan."},
        {"title": "Keyingi modul", "type": "highlight", "text": "Keyingi bosqich: KESIM."},
    ],
}


LEVEL10_MODULE08_QUIZ = {
    "L10_M08_001": [
        {"code": "L10_Q106", "question": "Tom bino hajmi va fasad bilan bog'liqmi?", "explanation": "Tom umumiy arxitektura kompozitsiyasining bir qismi.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
        {"code": "L10_Q107", "question": "Murakkab tom har doim yaxshiroqmi?", "explanation": "Keraksiz murakkablik qurilish va suv chiqarishni qiyinlashtirishi mumkin.", "options": [("A", "Ha", False), ("B", "Yo'q", True)]},
        {"code": "L10_Q108", "question": "Tom konsepsiyasi loyiha maqsadiga mos bo'lishi kerakmi?", "explanation": "Forma va funksiya birga ishlaydi.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
    ],
    "L10_M08_002": [
        {"code": "L10_Q109", "question": "Tom nishabi suv yo'liga ta'sir qiladimi?", "explanation": "Suv nishab bo'yicha harakat qiladi.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
        {"code": "L10_Q110", "question": "Suvning kirish oldiga oqishi yaxshi yechimmi?", "explanation": "Drainage odamlar va bino himoyasi bilan koordinatsiya qilinadi.", "options": [("A", "Ha", False), ("B", "Yo'q", True)]},
        {"code": "L10_Q111", "question": "Aniq tom nishabi material talabiga bog'liq bo'lishi mumkinmi?", "explanation": "Texnik talablarga qarab belgilanadi.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
    ],
    "L10_M08_003": [
        {"code": "L10_Q112", "question": "Ridge tom geometriyasining yuqori zonasimi?", "explanation": "Tom yuzalari yuqorida tutashishi mumkin.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
        {"code": "L10_Q113", "question": "Eave fasad bilan bog'liqmi?", "explanation": "Tomning pastki chekkasi fasadda ko'rinadi.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
        {"code": "L10_Q114", "question": "Keraksiz ko'p tom tutashuvlari riskni oshirishi mumkinmi?", "explanation": "Detal va drainage murakkablashadi.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
    ],
    "L10_M08_004": [
        {"code": "L10_Q115", "question": "Tom balandligi fasad proporsiyasiga ta'sir qiladimi?", "explanation": "Siluet va umumiy massing o'zgaradi.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
        {"code": "L10_Q116", "question": "Tom faqat plan ko'rinishida tekshiriladimi?", "explanation": "Fasad, 3D va sectionda ham ko'riladi.", "options": [("A", "Ha", False), ("B", "Yo'q", True)]},
        {"code": "L10_Q117", "question": "Kirish ustidagi tom yechimi foydalanuvchi orientatsiyasiga yordam berishi mumkinmi?", "explanation": "Kirishni vizual va funksional ta'kidlashi mumkin.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
    ],
    "L10_M08_005": [
        {"code": "L10_Q118", "question": "Tom auditida drainage tekshiriladimi?", "explanation": "Suv chiqarish tomning asosiy vazifalaridan.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
        {"code": "L10_Q119", "question": "Tom plan va section mos bo'lishi kerakmi?", "explanation": "Bitta loyiha holatini aks ettiradi.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
        {"code": "L10_Q120", "question": "Tom workflow'i qaysi?", "explanation": "Forma, suv yo'li va koordinatsiya birgalikda tekshiriladi.", "options": [("A", "Massing → nishab → ridge/eave → drainage → fasad/section → audit", True), ("B", "Faqat 3D ko'rinish → final", False)]},
    ],
}


def seed_level10_module08():
    connection = get_connection()
    try:
        cursor = connection.cursor()

        for row in LEVEL10_MODULE08_LESSONS:
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
