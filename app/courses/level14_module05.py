from database.database import get_connection


LEVEL14_MODULE05_LESSONS = [
    ("L14_M05", "L14_M05_001", "Ko'p avlodli yashash ssenariysi", "theory", "Bir uyda turli avlod ehtiyojlarini tushunish.", 1, 60, 20),
    ("L14_M05", "L14_M05_002", "Birgalik va mustaqillik", "theory", "Shared va private funksiyalar muvozanatini yaratish.", 2, 70, 20),
    ("L14_M05", "L14_M05_003", "Accessibility va kelajak", "practice", "Turli yoshdagi foydalanuvchilar uchun moslashuvchan rejalashtirish.", 3, 70, 20),
    ("L14_M05", "L14_M05_004", "Kirish, oshxona va servis modeli", "practice", "Bir nechta household ssenariylarini koordinatsiya qilish.", 4, 75, 20),
    ("L14_M05", "L14_M05_005", "Ko'p avlodli uy professional audit", "practice", "Privacy, shared spaces va kelajak ehtiyojlarini kompleks tekshirish.", 5, 85, 25),
]


LEVEL14_MODULE05_CONTENT = {
    "L14_M05_001": [
        {"title": "Bir oila, turli hayot ritmi", "type": "highlight", "text": "Bolalar, ota-ona va katta yoshli avlodning kunlik tartibi va privacy ehtiyoji farq qiladi."},
        {"title": "Scenario", "type": "normal", "text": "Kim qachon uyda, kim mehmon qabul qiladi, kimga sokin zona kerak — bular plan qaroriga ta'sir qiladi."},
        {"title": "Xato", "type": "warning", "text": "Faqat xona sonini ko'paytirib ko'p avlodli uy muammosini hal qildim deb hisoblamang."},
        {"title": "Mini-amaliyot", "type": "example", "text": "3 avlod uchun daily routine jadvali tuzing."},
    ],
    "L14_M05_002": [
        {"title": "Shared + private", "type": "highlight", "text": "Family living va dining birlashtiruvchi zona, bedroom suite esa private zona bo'lishi mumkin."},
        {"title": "Independence", "type": "normal", "text": "Ba'zi householdlar uchun alohida living yoki kichik service zone kerak bo'lishi mumkin."},
        {"title": "Izolyatsiya emas", "type": "warning", "text": "Privacy yaratish oilani butunlay uzib qo'yish degani emas."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Shared / semi-private / private zonalash yarating."},
    ],
    "L14_M05_003": [
        {"title": "Kelajakni o'ylang", "type": "highlight", "text": "Uy uzoq muddat foydalanilgani uchun yosh va mobility o'zgarishi ehtimoli hisobga olinadi."},
        {"title": "Moslashuvchan xona", "type": "normal", "text": "Bir xona vaqt o'tishi bilan bedroom, study yoki caregiver room vazifasini olishi mumkin."},
        {"title": "Aniq accessibility talablari", "type": "warning", "text": "O'lcham va texnik talablar loyiha yurisdiksiyasidagi amaldagi normativlardan tekshiriladi."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Uy uchun 10 yillik adaptation scenario yozing."},
    ],
    "L14_M05_004": [
        {"title": "Household modeli", "type": "highlight", "text": "Birgalikda ovqatlanish, alohida oshxona ehtiyoji yoki mustaqil kirish oilaga qarab farq qiladi."},
        {"title": "Service", "type": "normal", "text": "Laundry, storage, pantry va boshqa kundalik funksiyalar household soni bilan bog'liq."},
        {"title": "Taxmin qilmang", "type": "warning", "text": "Ko'p avlodli oilalarning yashash odati bir xil deb qabul qilmang."},
        {"title": "Mini-amaliyot", "type": "example", "text": "2 xil family model uchun plan strategiyasini solishtiring."},
    ],
    "L14_M05_005": [
        {"title": "Multi-generation audit", "type": "highlight", "text": "Family profiles → routines → shared/private → accessibility → service → entrances → adaptability → audit."},
        {"title": "Professional checklist", "type": "example", "text": "1. Har avlod ehtiyoji tushunildimi?<br><br>2. Shared zona yetarlimi?<br><br>3. Privacy ishlaydimi?<br><br>4. Older users hisobga olinganmi?<br><br>5. Service zonalari yetarlimi?<br><br>6. Future adaptation mumkinmi?<br><br>7. Household conflict kamayganmi?"},
        {"title": "Keyingi modul", "type": "highlight", "text": "Keyingi modul: PREMIUM FASAD."},
    ],
}


LEVEL14_MODULE05_QUIZ = {}

for i, lesson_code in enumerate(
    ["L14_M05_001", "L14_M05_002", "L14_M05_003", "L14_M05_004", "L14_M05_005"]
):
    start = 61 + i * 3

    LEVEL14_MODULE05_QUIZ[lesson_code] = [
        {
            "code": f"L14_Q{start:03d}",
            "question": "Ko'p avlodli uyda turli yosh guruhlarining ehtiyoji alohida tahlil qilinadimi?",
            "explanation": "Hayot ritmi va privacy talabi farq qilishi mumkin.",
            "options": [("A", "Ha", True), ("B", "Yo'q", False)],
        },
        {
            "code": f"L14_Q{start + 1:03d}",
            "question": "Ko'p avlodli uy faqat ko'proq yotoqxona qo'shish bilan hal bo'ladimi?",
            "explanation": "Shared/private, circulation va service ham muhim.",
            "options": [("A", "Ha", False), ("B", "Yo'q", True)],
        },
        {
            "code": f"L14_Q{start + 2:03d}",
            "question": "Future adaptability ko'p avlodli uyda foydalimi?",
            "explanation": "Oila va mobility ehtiyojlari vaqt o'tishi bilan o'zgarishi mumkin.",
            "options": [("A", "Ha", True), ("B", "Yo'q", False)],
        },
    ]


def seed_level14_module05():
    connection = get_connection()
    try:
        cursor = connection.cursor()

        for row in LEVEL14_MODULE05_LESSONS:
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
