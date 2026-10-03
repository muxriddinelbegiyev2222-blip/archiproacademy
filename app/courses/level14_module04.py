from database.database import get_connection


LEVEL14_MODULE04_LESSONS = [
    ("L14_M04", "L14_M04_001", "Katta villa programmasi", "theory", "Katta hajmdagi turar joy funksiyalarini tizimli boshqarish.", 1, 80, 20),
    ("L14_M04", "L14_M04_002", "Functional clusters", "theory", "Ko'p xonali uyni mantiqiy bloklarga ajratish.", 2, 90, 20),
    ("L14_M04", "L14_M04_003", "Circulation va servis", "practice", "Katta uyda asosiy, private va service harakatlarini koordinatsiya qilish.", 3, 95, 20),
    ("L14_M04", "L14_M04_004", "Massing, courtyard va landscape", "practice", "Katta hajmni inson masshtabida va site bilan bog'liq tashkil qilish.", 4, 100, 20),
    ("L14_M04", "L14_M04_005", "Katta villa professional audit", "practice", "Murakkab turar joy loyihasini kompleks tekshirish.", 5, 115, 25),
]


LEVEL14_MODULE04_CONTENT = {
    "L14_M04_001": [
        {"title": "Katta uy = ko'p xona emas", "type": "highlight", "text": "Katta villa ko'p funksiyani yagona arxitektura tizimida boshqarishni talab qiladi."},
        {"title": "Program", "type": "normal", "text": "Family, guest, leisure, service, staff, wellness, outdoor va technical funksiyalar alohida tahlil qilinadi."},
        {"title": "Xato", "type": "warning", "text": "Maydon katta ekan deb keraksiz xonalar va foydalanilmaydigan zonalarni ko'paytirmang."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Villa uchun functional program matrix tuzing."},
    ],
    "L14_M04_002": [
        {"title": "Clusters", "type": "highlight", "text": "Katta programni bir nechta funksional blokka ajratish navigatsiya va privacy'ni yaxshilashi mumkin."},
        {"title": "Misol", "type": "normal", "text": "Guest wing, family wing, service core, entertainment zone kabi mantiqiy guruhlar bo'lishi mumkin."},
        {"title": "Uzun masofa", "type": "warning", "text": "Xonalar orasidagi kundalik yo'l haddan ortiq cho'zilib ketmasligi kerak."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Villa programmasini 5 functional clusterga ajrating."},
    ],
    "L14_M04_003": [
        {"title": "3 circulation", "type": "highlight", "text": "Guest, family va service circulation zarur joylarda bir-biridan farqlanishi mumkin."},
        {"title": "Service efficiency", "type": "normal", "text": "Oshxona, storage, laundry, technical va service access kundalik ishlash bilan bog'lanadi."},
        {"title": "Xato", "type": "warning", "text": "Service harakatini asosiy reprezentativ zonalar orqali keraksiz o'tkazmang."},
        {"title": "Mini-amaliyot", "type": "example", "text": "3 circulation diagram yarating."},
    ],
    "L14_M04_004": [
        {"title": "Katta massingni bo'ling", "type": "highlight", "text": "Katta bino hajmini courtyard, setback yoki bir necha volume orqali inson masshtabiga yaqinlashtirish mumkin."},
        {"title": "Landscape", "type": "normal", "text": "Villa tashqi hovli, terrace, pool yoki garden bilan yagona fazoviy tizim bo'lishi mumkin."},
        {"title": "Monolit blok", "type": "warning", "text": "Juda katta monolit massing ichki yorug'lik va inson masshtabida muammo tug'dirishi mumkin."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Villa uchun 3 massing strategy ishlab chiqing."},
    ],
    "L14_M04_005": [
        {"title": "Villa audit", "type": "highlight", "text": "Program → clusters → circulation → privacy → service → structure → MEP → massing → outdoor → BIM."},
        {"title": "Professional checklist", "type": "example", "text": "1. Program ortiqcha emasmi?<br><br>2. Clusters aniqmi?<br><br>3. Circulation samaralimi?<br><br>4. Privacy ishlaydimi?<br><br>5. Service logic bormi?<br><br>6. Structure/MEP koordinatsiya qilinganmi?<br><br>7. Massing inson masshtabidami?<br><br>8. Landscape bilan aloqa bormi?"},
        {"title": "Keyingi modul", "type": "highlight", "text": "Keyingi modul: KO'P AVLODLI OILA."},
    ],
}


LEVEL14_MODULE04_QUIZ = {}

for i, lesson_code in enumerate(
    ["L14_M04_001", "L14_M04_002", "L14_M04_003", "L14_M04_004", "L14_M04_005"]
):
    start = 46 + i * 3

    LEVEL14_MODULE04_QUIZ[lesson_code] = [
        {
            "code": f"L14_Q{start:03d}",
            "question": "Katta villa programmasini functional clusterlarga ajratish foydalimi?",
            "explanation": "Ko'p funksiyani boshqarishni osonlashtiradi.",
            "options": [("A", "Ha", True), ("B", "Yo'q", False)],
        },
        {
            "code": f"L14_Q{start + 1:03d}",
            "question": "Uy katta bo'lsa foydalanilmaydigan xonalarni ko'paytirish professional yondashuvmi?",
            "explanation": "Har maydonning real funksiyasi bo'lishi kerak.",
            "options": [("A", "Ha", False), ("B", "Yo'q", True)],
        },
        {
            "code": f"L14_Q{start + 2:03d}",
            "question": "Guest, family va service circulation alohida tahlil qilinishi mumkinmi?",
            "explanation": "Katta villa workflowida bu muhim bo'lishi mumkin.",
            "options": [("A", "Ha", True), ("B", "Yo'q", False)],
        },
    ]


def seed_level14_module04():
    connection = get_connection()
    try:
        cursor = connection.cursor()

        for row in LEVEL14_MODULE04_LESSONS:
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
