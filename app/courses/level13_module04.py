from database.database import get_connection


LEVEL13_MODULE04_LESSONS = [
    ("L13_M04", "L13_M04_001", "Variant nima uchun kerak?", "theory", "Bir brief uchun turli arxitektura yechimlarini ishlab chiqish mantig'ini tushunish.", 1, 50, 20),
    ("L13_M04", "L13_M04_002", "Haqiqiy alternativalar", "theory", "Faqat kosmetik emas, strategik farqli variantlar yaratish.", 2, 55, 20),
    ("L13_M04", "L13_M04_003", "Variantlarni mezon bilan solishtirish", "practice", "Har bir yechimni aniq mezonlar bilan baholash.", 3, 60, 20),
    ("L13_M04", "L13_M04_004", "Mijozga variantlarni ko'rsatish", "practice", "Variantlarni tushunarli va boshqariladigan tarzda taqdim etish.", 4, 65, 20),
    ("L13_M04", "L13_M04_005", "Variantlar professional audit", "practice", "Final yo'nalishni tanlashdan oldin variantlarni kompleks tekshirish.", 5, 70, 25),
]


LEVEL13_MODULE04_CONTENT = {
    "L13_M04_001": [
        {"title": "Birinchi fikr final emas", "type": "highlight", "text": "Bir briefga bir nechta to'g'ri arxitektura javobi bo'lishi mumkin."},
        {"title": "Variant maqsadi", "type": "normal", "text": "Turli strategiyani sinab ko'rish va qarorni ongli tanlash."},
        {"title": "Keraksiz 10 variant", "type": "warning", "text": "Ko'p, lekin bir-biriga deyarli o'xshash variant mijozni faqat chalg'itishi mumkin."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Bir brief uchun 3 asosiy variant strategiyasini yozing."},
    ],
    "L13_M04_002": [
        {"title": "Strategik farq", "type": "highlight", "text": "Variantlar zonalash, bino joylashuvi, circulation yoki massing bo'yicha real farq qilishi mumkin."},
        {"title": "Kosmetik farq", "type": "normal", "text": "Faqat bitta deraza yoki rang o'zgarishi har doim alohida konsept variant hisoblanmaydi."},
        {"title": "Xato", "type": "warning", "text": "Bir variantni yaxshi, boshqalarini ataylab yomon tayyorlamang."},
        {"title": "Mini-amaliyot", "type": "example", "text": "A/B/C variantlar uchun asosiy farqni bir jumlada yozing."},
    ],
    "L13_M04_003": [
        {"title": "Mezon", "type": "highlight", "text": "Variantlar brief, site, circulation, privacy, budjet va arxitektura sifati bo'yicha solishtirilishi mumkin."},
        {"title": "Trade-off", "type": "normal", "text": "Bir variant privacy'da kuchli, boshqasi hovli aloqasida kuchli bo'lishi mumkin."},
        {"title": "Faqat did", "type": "warning", "text": "“Menga shu yoqdi”dan tashqari aniq loyiha sabablarini ko'rsating."},
        {"title": "Mini-amaliyot", "type": "example", "text": "6 mezonli variant comparison table yarating."},
    ],
    "L13_M04_004": [
        {"title": "Mijozga tushunarli", "type": "highlight", "text": "Har variantning asosiy g'oyasi, foydasi va trade-off'i sodda til bilan tushuntiriladi."},
        {"title": "Bir xil format", "type": "normal", "text": "Variantlarni bir xil scale va taqdimot darajasida ko'rsatish taqqoslashni osonlashtiradi."},
        {"title": "Bosim o'tkazmang", "type": "warning", "text": "Mijozga qaror uchun ma'lumot bering; tanlovni manipulyatsiya qilmang."},
        {"title": "Mini-amaliyot", "type": "example", "text": "A/B/C variant uchun 3 jumladan prezentatsiya matni yozing."},
    ],
    "L13_M04_005": [
        {"title": "Variant audit", "type": "highlight", "text": "Brief → 3 strategiya → bir xil detal darajasi → mezonlar → trade-offs → client feedback → direction."},
        {"title": "Professional checklist", "type": "example", "text": "1. Variantlar real farqlimi?<br><br>2. Hammasi briefga javob beradimi?<br><br>3. Bir xil detal darajasidami?<br><br>4. Mezonga solishtirildimi?<br><br>5. Trade-off aniqmi?<br><br>6. Mijoz feedbacki qayd qilindimi?"},
        {"title": "Keyingi modul", "type": "highlight", "text": "Keyingi modul: LOYIHA TAQDIMOTI."},
    ],
}


LEVEL13_MODULE04_QUIZ = {}

for i, lesson_code in enumerate(
    ["L13_M04_001", "L13_M04_002", "L13_M04_003", "L13_M04_004", "L13_M04_005"]
):
    start = 46 + i * 3

    LEVEL13_MODULE04_QUIZ[lesson_code] = [
        {
            "code": f"L13_Q{start:03d}",
            "question": "Bir brief uchun bir nechta asosli arxitektura varianti bo'lishi mumkinmi?",
            "explanation": "Bir muammoga turli strategiyalar mavjud bo'lishi mumkin.",
            "options": [("A", "Ha", True), ("B", "Yo'q", False)],
        },
        {
            "code": f"L13_Q{start + 1:03d}",
            "question": "Variantlarni aniq mezonlar bilan solishtirish foydalimi?",
            "explanation": "Trade-off va qaror sabablari ko'rinadi.",
            "options": [("A", "Ha", True), ("B", "Yo'q", False)],
        },
        {
            "code": f"L13_Q{start + 2:03d}",
            "question": "Mijozni ma'lum variantga bosim bilan yo'naltirish professional prezentatsiyaning maqsadimi?",
            "explanation": "Mijozga tushunarli ma'lumot berib qaroriga yordam beriladi.",
            "options": [("A", "Ha", False), ("B", "Yo'q", True)],
        },
    ]


def seed_level13_module04():
    connection = get_connection()
    try:
        cursor = connection.cursor()

        for row in LEVEL13_MODULE04_LESSONS:
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
