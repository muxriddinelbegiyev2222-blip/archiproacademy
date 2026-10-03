from database.database import get_connection


LEVEL10_MODULE06_LESSONS = [
    ("L10_M06", "L10_M06_001", "Modelni boshlash strategiyasi", "theory", "Final plan asosida toza BIM modelni boshlash.", 1, 80, 20),
    ("L10_M06", "L10_M06_002", "Stories, grid va asosiy elementlar", "practice", "Modelning bazaviy strukturasi va o'qlarini to'g'ri tashkil qilish.", 2, 90, 20),
    ("L10_M06", "L10_M06_003", "Wall, slab, column va openings", "practice", "Asosiy bino elementlarini izchil modellashtirish.", 3, 95, 20),
    ("L10_M06", "L10_M06_004", "Model koordinatsiyasi", "practice", "Plan, 3D, kesim va boshqa ko'rinishlarda konfliktlarni aniqlash.", 4, 100, 20),
    ("L10_M06", "L10_M06_005", "Archicad modeli professional audit", "practice", "Bir qavatli uy modelini professional BIM checklist bilan tekshirish.", 5, 115, 25),
]


LEVEL10_MODULE06_CONTENT = {
    "L10_M06_001": [
        {"title": "Final plan — model bazasi", "type": "highlight", "text": "Archicad modeliga o'tishda eskiz emas, audit qilingan final plan asos bo'ladi."},
        {"title": "Model tartibi", "type": "normal", "text": "Stories, units, grid, layers va asosiy element strategiyasi boshidan tushunarli bo'lishi kerak."},
        {"title": "Xato", "type": "warning", "text": "Har narsani default holatda tasodifiy chizib ketish keyin modelni boshqarishni qiyinlashtiradi."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Model boshlashdan oldingi 10 bandli setup checklist tuzing."},
    ],
    "L10_M06_002": [
        {"title": "Stories", "type": "highlight", "text": "Qavatlar va asosiy sathlar model strukturasi uchun tayanch."},
        {"title": "Grid", "type": "normal", "text": "Konstruktiv va arxitektura o'qlari mantiqli bo'lsa keyingi koordinatsiya osonlashadi."},
        {"title": "Model origin", "type": "normal", "text": "Loyiha joylashuvi va grid bir xil tizimda boshqariladi."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Bir qavatli uy uchun stories va asosiy grid sxemasini tayyorlang."},
    ],
    "L10_M06_003": [
        {"title": "Asosiy elementlar", "type": "highlight", "text": "Wall, Slab, Column, Beam, Door va Window elementlari BIM mantiqida yaratiladi."},
        {"title": "Duplicate geometriya", "type": "warning", "text": "Bir elementni bir necha marta ustma-ust qo'yish model xatosidir."},
        {"title": "Ochilishlar", "type": "normal", "text": "Eshik va derazalar plan, fasad va 3D bilan birga tekshiriladi."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Modeldagi asosiy element kategoriyalarini checklist qilib chiqing."},
    ],
    "L10_M06_004": [
        {"title": "Modelni faqat plan orqali tekshirmang", "type": "highlight", "text": "3D, section va elevation ko'rinishlari boshqa turdagi xatolarni ko'rsatadi."},
        {"title": "Conflict", "type": "normal", "text": "Wall/slab, opening, roof, column va boshqa elementlarning kesishuvlari tekshiriladi."},
        {"title": "Consistency", "type": "warning", "text": "Plan to'g'ri ko'rinib, 3D noto'g'ri bo'lsa model hali toza emas."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Plan + 3D + section bo'yicha 15 ta model audit savolini yozing."},
    ],
    "L10_M06_005": [
        {"title": "BIM audit", "type": "highlight", "text": "Stories → grid → walls → slabs → openings → structure → views → 3D → sections → cleanup."},
        {"title": "Professional checklist", "type": "example", "text": "1. Stories to'g'rimi?<br><br>2. Grid mosmi?<br><br>3. Dublikatlar yo'qmi?<br><br>4. Wall/slab tutashuvi to'g'rimi?<br><br>5. Doors/windows mosmi?<br><br>6. 3D tozami?<br><br>7. Sectionlar mantiqiymi?<br><br>8. Keraksiz elementlar yo'qmi?<br><br>9. Model final plan bilan mosmi?"},
        {"title": "Muhim qoida", "type": "warning", "text": "BIM model chiroyli 3D emas. U koordinatsiyalangan loyiha ma'lumoti."},
        {"title": "Keyingi modul", "type": "highlight", "text": "Keyingi bosqich: FASAD."},
    ],
}


LEVEL10_MODULE06_QUIZ = {
    "L10_M06_001": [
        {"code": "L10_Q076", "question": "Archicad modeli audit qilingan plan asosida boshlanishi kerakmi?", "explanation": "Bu qayta ishlashni kamaytiradi.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
        {"code": "L10_Q077", "question": "Model strukturasi boshidan rejalashtirilishi foydalimi?", "explanation": "Keyingi boshqaruv osonlashadi.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
        {"code": "L10_Q078", "question": "Tasodifiy default sozlamalarda model qurish eng yaxshi workflow'mi?", "explanation": "Standart va struktura kerak.", "options": [("A", "Ha", False), ("B", "Yo'q", True)]},
    ],
    "L10_M06_002": [
        {"code": "L10_Q079", "question": "Stories model strukturasiga ta'sir qiladimi?", "explanation": "Qavat va sathlar bilan bog'liq.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
        {"code": "L10_Q080", "question": "Grid konstruktor bilan koordinatsiyada foydalimi?", "explanation": "O'qlar umumiy referens beradi.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
        {"code": "L10_Q081", "question": "Grid va model joylashuvi tartibli bo'lishi kerakmi?", "explanation": "Koordinatsiya uchun muhim.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
    ],
    "L10_M06_003": [
        {"code": "L10_Q082", "question": "Dublikat element model xatosimi?", "explanation": "Bu miqdor va grafik natijalarni buzishi mumkin.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
        {"code": "L10_Q083", "question": "Door va Window fasadga ham ta'sir qiladimi?", "explanation": "Ochilishlar ko'p ko'rinishda aks etadi.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
        {"code": "L10_Q084", "question": "BIM elementlarni faqat 2D chiziqlar bilan almashtirish har doim to'g'rimi?", "explanation": "BIM element ma'lumot va 3D geometriyani ham olib yuradi.", "options": [("A", "Ha", False), ("B", "Yo'q", True)]},
    ],
    "L10_M06_004": [
        {"code": "L10_Q085", "question": "Modelni section orqali tekshirish foydalimi?", "explanation": "Vertikal konfliktlar ko'rinadi.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
        {"code": "L10_Q086", "question": "Plan yaxshi ko'rinsa 3D'ni tekshirish shart emasmi?", "explanation": "3D boshqa xatolarni ko'rsatishi mumkin.", "options": [("A", "Ha", False), ("B", "Yo'q", True)]},
        {"code": "L10_Q087", "question": "Element kesishuvlarini tekshirish koordinatsiyaning bir qismimi?", "explanation": "Model tozaligi uchun muhim.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
    ],
    "L10_M06_005": [
        {"code": "L10_Q088", "question": "BIM model faqat chiroyli 3D'mi?", "explanation": "BIM koordinatsiyalangan geometriya va ma'lumotni o'z ichiga oladi.", "options": [("A", "Ha", False), ("B", "Yo'q", True)]},
        {"code": "L10_Q089", "question": "Final model final plan bilan mos bo'lishi kerakmi?", "explanation": "Turli loyiha versiyalari konflikt yaratadi.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
        {"code": "L10_Q090", "question": "Model audit workflow'i qaysi?", "explanation": "Strukturadan element va views'largacha ketma-ket tekshiriladi.", "options": [("A", "Stories/grid → elements → openings → 3D/section → cleanup", True), ("B", "Faqat render → final", False)]},
    ],
}


def seed_level10_module06():
    connection = get_connection()
    try:
        cursor = connection.cursor()

        for row in LEVEL10_MODULE06_LESSONS:
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
