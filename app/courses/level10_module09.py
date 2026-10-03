from database.database import get_connection


LEVEL10_MODULE09_LESSONS = [
    ("L10_M09", "L10_M09_001", "Professional kesim tushunchasi", "theory", "Kesim orqali binoning vertikal mantig'ini tushunish.", 1, 50, 20),
    ("L10_M09", "L10_M09_002", "Sathlar va balandliklar", "theory", "Asosiy qavat, pol, shift va tom sathlarini koordinatsiya qilish.", 2, 55, 20),
    ("L10_M09", "L10_M09_003", "Konstruksiya va openinglar", "practice", "Kesimda plita, devor, tom, deraza va eshik aloqalarini tekshirish.", 3, 60, 20),
    ("L10_M09", "L10_M09_004", "Kesim orqali dizayn tekshiruvi", "practice", "Hajm, yorug'lik va ichki makonni kesim yordamida tahlil qilish.", 4, 65, 20),
    ("L10_M09", "L10_M09_005", "Kesim professional audit", "practice", "Bir qavatli uy kesimlarini kompleks tekshirish.", 5, 70, 25),
]


LEVEL10_MODULE09_CONTENT = {
    "L10_M09_001": [
        {"title": "Kesim — vertikal plan", "type": "highlight", "text": "Plan gorizontal aloqani ko'rsatsa, kesim binoning vertikal aloqalarini ko'rsatadi."},
        {"title": "Ko'rinadi", "type": "normal", "text": "Pol, shift, tom, opening, sath va konstruktiv aloqalar."},
        {"title": "Xato", "type": "warning", "text": "Kesimni faqat avtomatik generated drawing deb qaramang. U loyiha tekshiruv vositasi."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Uy uchun eng informativ 2 ta kesim joyini tanlang."},
    ],
    "L10_M09_002": [
        {"title": "0.000", "type": "highlight", "text": "Asosiy referens sath boshqa balandliklar bilan izchil ishlashi kerak."},
        {"title": "Floor/ceiling/roof", "type": "normal", "text": "Ichki balandlik va tom geometriyasi bir kesimda tushunarli ko'rinadi."},
        {"title": "Mismatch", "type": "warning", "text": "Plan va sectiondagi sathlar farq qilsa loyiha koordinatsiyasi tekshiriladi."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Kesimdagi barcha asosiy level'larni ro'yxat qiling."},
    ],
    "L10_M09_003": [
        {"title": "Konstruktiv qatlamlar", "type": "highlight", "text": "Devor, plita va tom kesimda real tutashuv mantig'ini ko'rsatadi."},
        {"title": "Openings", "type": "normal", "text": "Deraza sill/head, eshik balandligi va boshqa openinglar vertikal koordinatsiyada tekshiriladi."},
        {"title": "Conflict", "type": "warning", "text": "Opening tom, beam yoki boshqa element bilan konflikt qilishi mumkin."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Kesim orqali 5 ta konstruktiv/architectural conflict tekshiring."},
    ],
    "L10_M09_004": [
        {"title": "Kesim dizayn vositasi", "type": "highlight", "text": "Ichki hajm, shift, yorug'lik va tashqi siluet kesim orqali yaxshiroq tushuniladi."},
        {"title": "Window + light", "type": "normal", "text": "Deraza balandligi va xona chuqurligi vertikal munosabatda ko'riladi."},
        {"title": "Faqat hujjat emas", "type": "warning", "text": "Kesimni faqat album oxirida qo'shiladigan chizma deb hisoblamang."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Kesim orqali xona hajmini yaxshilaydigan 3 ta dizayn qarorini toping."},
    ],
    "L10_M09_005": [
        {"title": "Kesim audit", "type": "highlight", "text": "Cut location → levels → floor → walls → openings → roof → structure → annotation → plan consistency."},
        {"title": "Professional checklist", "type": "example", "text": "1. Kesim joyi informativmi?<br><br>2. Level'lar to'g'rimi?<br><br>3. Pol/tom qatlamlari tushunarlimi?<br><br>4. Openinglar mosmi?<br><br>5. Konstruktiv konflikt yo'qmi?<br><br>6. Plan bilan mosmi?<br><br>7. Kerakli annotation bormi?"},
        {"title": "Muhim qoida", "type": "warning", "text": "Plan, fasad va kesim bir-biriga qarama-qarshi loyiha ma'lumotini ko'rsatmasligi kerak."},
        {"title": "Keyingi modul", "type": "highlight", "text": "Keyingi bosqich: GENPLAN."},
    ],
}


LEVEL10_MODULE09_QUIZ = {
    "L10_M09_001": [
        {"code": "L10_Q121", "question": "Kesim binoning vertikal aloqalarini ko'rsatadimi?", "explanation": "Bu uning asosiy vazifalaridan.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
        {"code": "L10_Q122", "question": "Kesim faqat avtomatik chizma sifatida ko'rilishi kerakmi?", "explanation": "U dizayn va koordinatsiya vositasi hamdir.", "options": [("A", "Ha", False), ("B", "Yo'q", True)]},
        {"code": "L10_Q123", "question": "Kesim joyini ongli tanlash muhimmi?", "explanation": "Informativ zonalarni kesish kerak.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
    ],
    "L10_M09_002": [
        {"code": "L10_Q124", "question": "0.000 boshqa sathlar uchun referens bo'lishi mumkinmi?", "explanation": "Loyiha balandliklari tartibli tizimda ishlaydi.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
        {"code": "L10_Q125", "question": "Plan va kesimdagi sathlar mos bo'lishi kerakmi?", "explanation": "Bitta loyiha ma'lumotini ko'rsatadi.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
        {"code": "L10_Q126", "question": "Tom balandligi kesimda tekshiriladimi?", "explanation": "Vertikal geometriya kesimda aniq ko'rinadi.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
    ],
    "L10_M09_003": [
        {"code": "L10_Q127", "question": "Deraza head/sill kesimda tekshiriladimi?", "explanation": "Ochilishlar vertikal koordinatsiya talab qiladi.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
        {"code": "L10_Q128", "question": "Opening konstruktiv element bilan konflikt qilishi mumkinmi?", "explanation": "Beam, roof yoki boshqa element bilan to'qnashishi mumkin.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
        {"code": "L10_Q129", "question": "Kesim konstruktiv tutashuvni tushunishga yordam beradimi?", "explanation": "Qatlam va elementlar vertikal ko'rinadi.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
    ],
    "L10_M09_004": [
        {"code": "L10_Q130", "question": "Kesim ichki makon dizaynini tekshirishga yordam beradimi?", "explanation": "Hajm va balandliklar ko'rinadi.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
        {"code": "L10_Q131", "question": "Kesim faqat albumning oxirida kerakmi?", "explanation": "U loyiha rivojlanishida ham ishlatiladi.", "options": [("A", "Ha", False), ("B", "Yo'q", True)]},
        {"code": "L10_Q132", "question": "Deraza va yorug'lik aloqasini section orqali tahlil qilish mumkinmi?", "explanation": "Vertikal joylashuv ko'rinadi.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
    ],
    "L10_M09_005": [
        {"code": "L10_Q133", "question": "Kesim auditida plan bilan moslik tekshiriladimi?", "explanation": "Chizmalar bir-biriga mos bo'lishi kerak.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
        {"code": "L10_Q134", "question": "Kesimda konstruktiv konfliktlar aniqlanishi mumkinmi?", "explanation": "Vertikal kesishuvlar ko'rinadi.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
        {"code": "L10_Q135", "question": "Kesim audit workflow'i qaysi?", "explanation": "Kesim joyidan level va elementlar orqali koordinatsiya tekshiriladi.", "options": [("A", "Cut → levels → elements/openings → roof/structure → annotation → audit", True), ("B", "Auto section → tekshirmasdan final", False)]},
    ],
}


def seed_level10_module09():
    connection = get_connection()
    try:
        cursor = connection.cursor()

        for row in LEVEL10_MODULE09_LESSONS:
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
