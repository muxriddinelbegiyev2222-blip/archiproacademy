from database.database import get_connection


LEVEL14_MODULE06_LESSONS = [
    ("L14_M06", "L14_M06_001", "Premium fasad tushunchasi", "theory", "Premium ko'rinishni bezak emas, kompozitsion sifat sifatida tushunish.", 1, 70, 20),
    ("L14_M06", "L14_M06_002", "Proporsiya va massing PRO", "theory", "Hajm, bo'shliq va opening nisbatlarini yuqori darajada boshqarish.", 2, 80, 20),
    ("L14_M06", "L14_M06_003", "Material va detal hierarxiyasi", "practice", "Material va detailni maqsadli kompozitsion tizimga aylantirish.", 3, 85, 20),
    ("L14_M06", "L14_M06_004", "Yorug'lik, soya va landscape", "practice", "Fasadni kun davomida va tashqi makon bilan birga o'qish.", 4, 90, 20),
    ("L14_M06", "L14_M06_005", "Premium fasad professional audit", "practice", "Fasadni plan, massing, material va detal bo'yicha kompleks tekshirish.", 5, 95, 25),
]


LEVEL14_MODULE06_CONTENT = {
    "L14_M06_001": [
        {"title": "Premium ≠ ko'p dekor", "type": "highlight", "text": "Premium taassurot ko'pincha proporsiya, material sifati, detal va kompozitsion intizomdan keladi."},
        {"title": "Kamroq, lekin aniq", "type": "normal", "text": "Har fasad elementi maqsadli va umumiy g'oyaga xizmat qilishi kerak."},
        {"title": "Xato", "type": "warning", "text": "Ko'p qimmat material va bezak avtomatik ravishda kuchli fasad yaratmaydi."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Premium fasad uchun 5 ta sifat mezonini yozing."},
    ],
    "L14_M06_002": [
        {"title": "Massing birinchi", "type": "highlight", "text": "Materialdan oldin bino hajmi va proporsiyasi ishlashi kerak."},
        {"title": "Solid / void", "type": "normal", "text": "Devor massasi va openinglar o'rtasidagi nisbat fasad xarakterini belgilaydi."},
        {"title": "Material bilan yashirmang", "type": "warning", "text": "Yomon massingni qimmat material bilan qutqarishga suyanmang."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Fasadni materialsiz oq massa sifatida audit qiling."},
    ],
    "L14_M06_003": [
        {"title": "Material hierarchy", "type": "highlight", "text": "Primary, secondary va accent materiallar aniq rolda ishlaydi."},
        {"title": "Detail", "type": "normal", "text": "Material tutashuvi, reveal, corner va opening atrofi umumiy sifatga kuchli ta'sir qiladi."},
        {"title": "Detailni keyinga qoldirmang", "type": "warning", "text": "Fasad konsepsiyasi quriladigan detailga aylanishi kerak."},
        {"title": "Mini-amaliyot", "type": "example", "text": "5 ta kritik facade detail zonasini belgilang."},
    ],
    "L14_M06_004": [
        {"title": "Soya ham material", "type": "highlight", "text": "Recess, canopy, fins va volume shift kun davomida fasad xarakterini o'zgartiradi."},
        {"title": "Landscape", "type": "normal", "text": "Fasad yer, daraxt, approach va outdoor lighting bilan birgalikda qabul qilinadi."},
        {"title": "Faqat tungi render", "type": "warning", "text": "Kuchli artificial lighting yomon kunduzgi fasadni professional yechimga aylantirmaydi."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Morning / noon / evening facade perceptionni tahlil qiling."},
    ],
    "L14_M06_005": [
        {"title": "Premium facade audit", "type": "highlight", "text": "Massing → proportion → solid/void → hierarchy → material → details → shadow → landscape → constructability."},
        {"title": "Professional checklist", "type": "example", "text": "1. Massing materialsiz ishlaydimi?<br><br>2. Proporsiya kuchlimi?<br><br>3. Opening hierarchy bormi?<br><br>4. Material soni nazoratdami?<br><br>5. Detail zonalari yechilganmi?<br><br>6. Shadow strategy bormi?<br><br>7. Barcha fasadlar bir tildami?<br><br>8. Qurilish mantig'i bormi?"},
        {"title": "Keyingi modul", "type": "highlight", "text": "Keyingi modul: DESIGN CLINIC."},
    ],
}


LEVEL14_MODULE06_QUIZ = {}

for i, lesson_code in enumerate(
    ["L14_M06_001", "L14_M06_002", "L14_M06_003", "L14_M06_004", "L14_M06_005"]
):
    start = 76 + i * 3

    LEVEL14_MODULE06_QUIZ[lesson_code] = [
        {
            "code": f"L14_Q{start:03d}",
            "question": "Premium fasad sifati faqat qimmat material soniga bog'liqmi?",
            "explanation": "Proporsiya, massing, detail va kompozitsiya muhim.",
            "options": [("A", "Ha", False), ("B", "Yo'q", True)],
        },
        {
            "code": f"L14_Q{start + 1:03d}",
            "question": "Materialdan oldin massing va proporsiyani tekshirish foydalimi?",
            "explanation": "Fasadning asosiy kompozitsion bazasi shu.",
            "options": [("A", "Ha", True), ("B", "Yo'q", False)],
        },
        {
            "code": f"L14_Q{start + 2:03d}",
            "question": "Material tutashuv detallari final fasad sifatiga ta'sir qiladimi?",
            "explanation": "Kritik detail zonalari muhim.",
            "options": [("A", "Ha", True), ("B", "Yo'q", False)],
        },
    ]


def seed_level14_module06():
    connection = get_connection()
    try:
        cursor = connection.cursor()

        for row in LEVEL14_MODULE06_LESSONS:
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
