from database.database import get_connection


LEVEL10_MODULE11_LESSONS = [
    ("L10_M11", "L10_M11_001", "Loyiha albomi strukturasi", "theory", "Bir qavatli uy loyiha albomini mantiqiy tartibda tashkil qilish.", 1, 80, 20),
    ("L10_M11", "L10_M11_002", "Plan, fasad va kesimlar", "practice", "Asosiy chizmalarni yagona grafik standartda tayyorlash.", 2, 90, 20),
    ("L10_M11", "L10_M11_003", "Genplan va yordamchi chizmalar", "practice", "Uchastka va loyiha haqidagi qo'shimcha ma'lumotlarni albomga integratsiya qilish.", 3, 95, 20),
    ("L10_M11", "L10_M11_004", "Layout va grafik sifat", "practice", "Chizmalarni professional sheet va layoutlarda joylashtirish.", 4, 100, 20),
    ("L10_M11", "L10_M11_005", "LEVEL 10 final loyiha audit", "practice", "Bir qavatli uy loyihasini texnik topshiriqdan albomgacha kompleks tekshirish.", 5, 115, 25),
]


LEVEL10_MODULE11_CONTENT = {
    "L10_M11_001": [
        {"title": "Albomi — hikoya", "type": "highlight", "text": "Loyiha albomi chizmalar to'plami emas, loyiha qarorini mantiqiy ketma-ketlikda tushuntiruvchi hujjat."},
        {"title": "Tartib", "type": "normal", "text": "Muqova → loyiha ma'lumoti → genplan → plan → fasad → kesim → kerakli qo'shimcha materiallar."},
        {"title": "Xato", "type": "warning", "text": "Chizmalarni tasodifiy tartibda joylashtirish o'quvchini chalg'itadi."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Bir qavatli uy albomi uchun sahifalar ro'yxatini tuzing."},
    ],
    "L10_M11_002": [
        {"title": "Bir xil standart", "type": "highlight", "text": "Plan, fasad va kesimlar o'zaro grafik va ma'lumot jihatdan izchil bo'lishi kerak."},
        {"title": "Annotation", "type": "normal", "text": "O'lcham, nom, level, marker va kerakli izohlar o'qilishi kerak."},
        {"title": "Mismatch", "type": "warning", "text": "Plan va fasadda bir xil deraza turli joyda ko'rinsa albom ishonchliligi pasayadi."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Plan/fasad/kesim o'rtasida 10 ta consistency check bajaring."},
    ],
    "L10_M11_003": [
        {"title": "Genplan", "type": "highlight", "text": "Uy loyiha albomida uchastka bilan aloqasi ham tushunarli bo'lishi kerak."},
        {"title": "Qo'shimcha material", "type": "normal", "text": "Kerak bo'lsa diagramma, 3D view, room schedule yoki boshqa tushuntiruvchi material qo'shilishi mumkin."},
        {"title": "Keraksiz sahifa", "type": "warning", "text": "Faqat sahifa sonini oshirish uchun foydasiz material qo'shmang."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Albomga qo'shiladigan materiallarni MUST / OPTIONAL guruhlariga ajrating."},
    ],
    "L10_M11_004": [
        {"title": "Layout hierarchy", "type": "highlight", "text": "Sahifada asosiy chizma, sarlavha va ikkilamchi ma'lumotlar vizual hierarxiyada joylashadi."},
        {"title": "Bir xil uslub", "type": "normal", "text": "Font, line weight, title va sheet strukturasini izchil saqlang."},
        {"title": "Crowded layout", "type": "warning", "text": "Bitta sahifaga juda ko'p chizma joylashtirish o'qilishni pasaytiradi."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Bitta layoutni hierarchy, alignment va readability bo'yicha audit qiling."},
    ],
    "L10_M11_005": [
        {"title": "LEVEL 10 final workflow", "type": "highlight", "text": "Brief → Site Analysis → Bubble → Eskiz → Optimization → BIM model → Fasad → Tom → Kesim → Genplan → Albom."},
        {"title": "Final professional checklist", "type": "example", "text": "1. Brief bajarilganmi?<br><br>2. Site bilan mosmi?<br><br>3. Plan professionalmi?<br><br>4. BIM model tozami?<br><br>5. Fasadlar izchilmi?<br><br>6. Tom ishlaydimi?<br><br>7. Kesimlar mosmi?<br><br>8. Genplan to'liqmi?<br><br>9. Layoutlar o'qiladimi?<br><br>10. Chizmalar bir-biriga mosmi?"},
        {"title": "Xato", "type": "warning", "text": "Albom chiroyli bo'lsa ham ichidagi chizmalar bir-biriga mos kelmasa loyiha professional emas."},
        {"title": "LEVEL 10 yakuni", "type": "highlight", "text": "Siz texnik topshiriqdan final loyiha albomigacha bir qavatli uy workflow'ini to'liq bosib o'tdingiz."},
    ],
}


LEVEL10_MODULE11_QUIZ = {
    "L10_M11_001": [
        {"code": "L10_Q151", "question": "Loyiha albomi faqat tasodifiy chizmalar to'plamimi?", "explanation": "U mantiqiy tartiblangan loyiha hujjati.", "options": [("A", "Ha", False), ("B", "Yo'q", True)]},
        {"code": "L10_Q152", "question": "Albom strukturasi o'quvchiga loyihani tushunishga yordam beradimi?", "explanation": "Ketma-ketlik loyiha hikoyasini tushunarli qiladi.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
        {"code": "L10_Q153", "question": "Genplan, plan, fasad va kesimlar mantiqiy ketma-ketlikda berilishi mumkinmi?", "explanation": "Bu professional prezentatsiya strukturasi.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
    ],
    "L10_M11_002": [
        {"code": "L10_Q154", "question": "Plan va fasad bir-biriga mos bo'lishi kerakmi?", "explanation": "Bir xil loyiha ma'lumotini ifodalaydi.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
        {"code": "L10_Q155", "question": "Annotation o'qilishi muhimmi?", "explanation": "Chizma ma'lumotini tushunishga yordam beradi.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
        {"code": "L10_Q156", "question": "Bir deraza plan va fasadda boshqa-boshqa joyda bo'lishi normalmi?", "explanation": "Bu koordinatsiya xatosi.", "options": [("A", "Ha", False), ("B", "Yo'q", True)]},
    ],
    "L10_M11_003": [
        {"code": "L10_Q157", "question": "Genplan uy albomining bir qismi bo'lishi mumkinmi?", "explanation": "Uy va uchastka aloqasini ko'rsatadi.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
        {"code": "L10_Q158", "question": "Foydasiz sahifalarni faqat son uchun qo'shish professionalmi?", "explanation": "Har sahifa maqsadga xizmat qilishi kerak.", "options": [("A", "Ha", False), ("B", "Yo'q", True)]},
        {"code": "L10_Q159", "question": "3D view tushuntiruvchi material bo'lishi mumkinmi?", "explanation": "Loyiha qarorini tushunishga yordam berishi mumkin.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
    ],
    "L10_M11_004": [
        {"code": "L10_Q160", "question": "Layout hierarchy o'qilishga ta'sir qiladimi?", "explanation": "Asosiy va ikkilamchi ma'lumotni ajratadi.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
        {"code": "L10_Q161", "question": "Bir sahifaga juda ko'p chizma joylashtirish o'qilishni pasaytirishi mumkinmi?", "explanation": "Crowded layout vizual shovqin yaratadi.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
        {"code": "L10_Q162", "question": "Layoutlar bir xil grafik standartda bo'lishi foydalimi?", "explanation": "Albomni professional va izchil qiladi.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
    ],
    "L10_M11_005": [
        {"code": "L10_Q163", "question": "LEVEL 10 final audit briefdan boshlanadimi?", "explanation": "Final loyiha boshlang'ich maqsadga javob berishi kerak.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
        {"code": "L10_Q164", "question": "Chiroyli albom ichidagi koordinatsiya xatolarini oqlaydimi?", "explanation": "Grafik sifat texnik moslikni almashtirmaydi.", "options": [("A", "Ha", False), ("B", "Yo'q", True)]},
        {"code": "L10_Q165", "question": "LEVEL 10 to'liq workflow'i qaysi?", "explanation": "Texnik topshiriqdan final albomgacha izchil loyiha jarayoni.", "options": [("A", "Brief → Site → Bubble → Eskiz → Optimization → BIM → Fasad/Tom/Kesim → Genplan → Albom", True), ("B", "Archicad → render → final", False)]},
    ],
}


def seed_level10_module11():
    connection = get_connection()
    try:
        cursor = connection.cursor()

        for row in LEVEL10_MODULE11_LESSONS:
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
