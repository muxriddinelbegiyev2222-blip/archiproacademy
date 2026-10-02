from database.database import get_connection


# ============================================================
# LEVEL 4
# MODULE 03 - ICHKI HOVLI
# ============================================================

LEVEL04_MODULE03_LESSONS = [
    (
        "L04_M03",
        "L04_M03_001",
        "Ichki hovli nima?",
        "theory",
        "Ichki hovlining turar joy arxitekturasidagi rolini tushunish.",
        1,
        40,
        20,
    ),
    (
        "L04_M03",
        "L04_M03_002",
        "Living va hovli aloqasi",
        "theory",
        "Ichki yashash makonlarini hovli bilan mantiqiy bog'lash.",
        2,
        40,
        20,
    ),
    (
        "L04_M03",
        "L04_M03_003",
        "Privacy va ichki hovli",
        "theory",
        "Ichki hovli orqali oilaviy maxfiylikni kuchaytirish.",
        3,
        40,
        20,
    ),
    (
        "L04_M03",
        "L04_M03_004",
        "Yorug'lik va shamollatish",
        "practice",
        "Ichki hovlidan tabiiy yorug'lik va shamollatish uchun foydalanish.",
        4,
        45,
        20,
    ),
    (
        "L04_M03",
        "L04_M03_005",
        "Ichki hovli auditi",
        "practice",
        "Ichki hovli va yashash makoni o'rtasidagi tipik xatolarni aniqlash.",
        5,
        55,
        25,
    ),
]


# ============================================================
# CONTENT
# ============================================================

LEVEL04_MODULE03_CONTENT = {
    "L04_M03_001": [
        {
            "title": "Ichki hovli — uyning tashqi xonasi",
            "type": "highlight",
            "text": """
            Ichki hovli shunchaki
            ochiq qolgan maydon emas.

            <br><br>

            U:

            <br><br>

            • dam olish;<br>
            • yorug'lik;<br>
            • shamollatish;<br>
            • privacy;<br>
            • oilaviy aloqa

            <br><br>

            uchun ishlashi mumkin.
            """,
        },
        {
            "title": "Hovli markaziy element bo'lishi mumkin",
            "type": "normal",
            "text": """
            Ba'zi uy rejalarida
            xonalar ichki hovli atrofida
            tashkil qilinadi.

            <br><br>

            Natijada hovli
            uy kompozitsiyasining markaziga aylanadi.
            """,
        },
        {
            "title": "Tasavvur qiling",
            "type": "example",
            "text": """
            Living, dining va family room
            bitta ichki hovliga qaragan.

            <br><br>

            Oila ichkarida bo'lsa ham
            hovli bilan vizual aloqani saqlaydi.
            """,
        },
        {
            "title": "Ichki hovli va oddiy orqa hovli farqi",
            "type": "highlight",
            "text": """
            Oddiy orqa hovli
            uyning bir tomonida bo'lishi mumkin.

            <br><br>

            Ichki hovli esa
            uy massasi bilan qisman yoki
            to'liq o'ralgan bo'lishi mumkin.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            3 xil sxema chizing:

            <br><br>

            1. Uy oldida hovli<br>
            2. Uy orqasida hovli<br>
            3. Uy ichida / orasida hovli

            <br><br>

            Qaysi biri ko'proq privacy beradi?
            """,
        },
    ],

    "L04_M03_002": [
        {
            "title": "Living va hovli bir-birini davom ettirishi mumkin",
            "type": "highlight",
            "text": """
            Kuchli rejalarda
            livingdan hovliga chiqish
            tasodifiy emas.

            <br><br>

            Ichki va tashqi yashash makoni
            bir-biriga bog'lanadi.
            """,
        },
        {
            "title": "Vizual aloqa",
            "type": "normal",
            "text": """
            Hovliga chiqmasdan ham
            livingdan yashil zona,
            daraxt yoki terassani ko'rish

            <br><br>

            makon sifatini oshirishi mumkin.
            """,
        },
        {
            "title": "To'g'ridan-to'g'ri chiqish",
            "type": "example",
            "text": """
            Livingdan hovliga
            bevosita chiqish bo'lsa,

            <br><br>

            tashqi makon
            kundalik hayotning bir qismiga aylanadi.
            """,
        },
        {
            "title": "Dining bilan aloqa",
            "type": "normal",
            "text": """
            Dining hovliga yaqin bo'lsa,
            tashqi ovqatlanish va
            mehmon kutish qulaylashishi mumkin.
            """,
        },
        {
            "title": "Xato",
            "type": "warning",
            "text": """
            Chiroyli hovli bor,
            lekin unga faqat service koridor orqali chiqiladi.

            <br><br>

            Bu hovlining kundalik qiymatini pasaytiradi.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Plan ustida quyidagi aloqani chizing:

            <br><br>

            LIVING → TERRACE → HOVLI

            <br><br>

            Shu yo'l qancha sodda bo'lsa,
            foydalanish shuncha tabiiy bo'lishi mumkin.
            """,
        },
    ],

    "L04_M03_003": [
        {
            "title": "Ichki hovli privacy yaratadi",
            "type": "highlight",
            "text": """
            Hovli uyning ichki tomoniga
            qaragan bo'lsa,

            <br><br>

            ko'cha va tashqi qo'shnilardan
            himoyalangan family makon
            hosil bo'lishi mumkin.
            """,
        },
        {
            "title": "Ko'cha tomoni va ichki hovli",
            "type": "normal",
            "text": """
            Ko'cha tomonda
            nisbatan yopiqroq fasad,

            <br><br>

            ichki hovli tomonda esa
            kattaroq ochilishlar ishlatilishi mumkin.
            """,
        },
        {
            "title": "Qo'shni tomoni",
            "type": "normal",
            "text": """
            Qo'shni uy juda yaqin bo'lsa,
            asosiy derazalarni ichki hovliga
            yo'naltirish privacyga yordam berishi mumkin.
            """,
        },
        {
            "title": "Bolalar uchun xavfsiz makon",
            "type": "example",
            "text": """
            Ichki hovli
            ko'chadan va mashina zonasidan
            ajratilgan bo'lsa,

            <br><br>

            bolalar uchun nazorat qilinadigan
            tashqi makon bo'lishi mumkin.
            """,
        },
        {
            "title": "Privacy faqat devor emas",
            "type": "highlight",
            "text": """
            Privacy:

            <br><br>

            • devor;<br>
            • bino joylashuvi;<br>
            • hovli geometriyasi;<br>
            • yashil ekran;<br>
            • ko'rish yo'nalishi

            <br><br>

            orqali yaratilishi mumkin.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Bir plan chizing.

            <br><br>

            Ko'cha tomondan
            hovli ko'rinmasin,

            <br><br>

            lekin livingdan hovli
            to'liq ko'rinsin.
            """,
        },
    ],

    "L04_M03_004": [
        {
            "title": "Ichki hovli yorug'lik olib kirishi mumkin",
            "type": "highlight",
            "text": """
            Chuqur planlarda
            ichki hovli uy ichiga
            qo'shimcha tabiiy yorug'lik
            olib kirishi mumkin.
            """,
        },
        {
            "title": "Ichki xonalar",
            "type": "normal",
            "text": """
            Tashqi fasadga yetib bormaydigan
            ayrim xonalar

            <br><br>

            ichki hovli orqali
            tabiiy yorug'lik olishi mumkin.
            """,
        },
        {
            "title": "Shamollatish",
            "type": "normal",
            "text": """
            To'g'ri tashkil qilingan
            ochilishlar va hovli

            <br><br>

            havo harakatiga
            yordam berishi mumkin.
            """,
        },
        {
            "title": "Hovli juda tor bo'lsa",
            "type": "warning",
            "text": """
            Ichki hovli juda tor va baland devorlar orasida bo'lsa,

            <br><br>

            yorug'lik va ochiqlik
            kutilgan darajada bo'lmasligi mumkin.
            """,
        },
        {
            "title": "Quyosh",
            "type": "example",
            "text": """
            Ichki hovli orientatsiyasi
            quyosh bilan birga tahlil qilinadi.

            <br><br>

            Qaysi paytda quyosh kiradi?
            Qaysi fasad ko'proq soya oladi?
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Ichki hovli atrofida
            4 ta xona joylashtiring.

            <br><br>

            Har biri uchun:

            <br><br>

            • yorug'lik;<br>
            • ko'rinish;<br>
            • shamollatish

            <br><br>

            ni tekshiring.
            """,
        },
    ],

    "L04_M03_005": [
        {
            "title": "Ichki hovli auditini boshlaymiz",
            "type": "highlight",
            "text": """
            Endi ichki hovliga
            faqat chiroyli element sifatida emas,

            <br><br>

            butun uy hayotining bir qismi
            sifatida qaraymiz.
            """,
        },
        {
            "title": "Xato 1 — hovli mavjud, lekin foydalanilmaydi",
            "type": "warning",
            "text": """
            Hovli bor.

            <br><br>

            Lekin living,
            dining yoki family room
            u bilan bog'lanmagan.
            """,
        },
        {
            "title": "Xato 2 — privacy yo'q",
            "type": "warning",
            "text": """
            Ichki hovli deb ataladi,
            lekin ko'chadan to'liq ko'rinadi.
            """,
        },
        {
            "title": "Xato 3 — juda tor courtyard",
            "type": "warning",
            "text": """
            Hovli geometrik jihatdan mavjud,
            lekin juda tor.

            <br><br>

            Ochiq makon hissi yetarli emas.
            """,
        },
        {
            "title": "Xato 4 — mashina yo'li hovlini kesadi",
            "type": "warning",
            "text": """
            Family ichki hovlisidan
            avtomobil yo'li o'tadi.

            <br><br>

            Bu xavfsizlik va privacyga zarar beradi.
            """,
        },
        {
            "title": "Xato 5 — service dominant",
            "type": "warning",
            "text": """
            Hovlining eng yaxshi qismi
            chiqindi, ombor yoki
            service faoliyatiga berilgan.
            """,
        },
        {
            "title": "Professional checklist",
            "type": "example",
            "text": """
            Ichki hovlini tekshiring:

            <br><br>

            <b>1.</b> Kim foydalanadi?<br><br>
            <b>2.</b> Livingga aloqasi bormi?<br><br>
            <b>3.</b> Diningga aloqasi bormi?<br><br>
            <b>4.</b> Privacy bormi?<br><br>
            <b>5.</b> Yorug'lik yetarlimi?<br><br>
            <b>6.</b> Shamollatish imkoniyati bormi?<br><br>
            <b>7.</b> Mashina bilan konflikt yo'qmi?
            """,
        },
        {
            "title": "Mini-case",
            "type": "example",
            "text": """
            1 qavatli hovlili uy.

            <br><br>

            Talab:

            <br><br>

            • living ichki hovliga qarasin;<br>
            • dining hovliga chiqsin;<br>
            • bolalar hovlida o'ynasin;<br>
            • ko'chadan hovli ko'rinmasin;<br>
            • parking hovlini kesmasin.

            <br><br>

            Bubble diagram yarating.
            """,
        },
        {
            "title": "Modul yakuni",
            "type": "highlight",
            "text": """
            Siz endi:

            <br><br>

            ✓ ichki hovli rolini tushunish;<br>
            ✓ living-hovli aloqasini yaratish;<br>
            ✓ privacy kuchaytirish;<br>
            ✓ tabiiy yorug'likdan foydalanish;<br>
            ✓ shamollatishni hisobga olish;<br>
            ✓ courtyard xatolarini topish

            <br><br>

            ko'nikmalariga ega bo'ldingiz.

            <br><br>

            Keyingi modul:
            <b>Ayvon va terassa.</b>
            """,
        },
    ],
}


# ============================================================
# QUIZ
# ============================================================

LEVEL04_MODULE03_QUIZ = {
    "L04_M03_001": [
        {
            "code": "L04_Q031",
            "question": "Ichki hovli faqat dekorativ ochiq maydonmi?",
            "explanation": (
                "U dam olish, yorug'lik, shamollatish va privacy uchun ishlashi mumkin."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L04_Q032",
            "question": "Ichki hovli uy kompozitsiyasining markazi bo'lishi mumkinmi?",
            "explanation": (
                "Xonalar hovli atrofida tashkil qilinishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L04_Q033",
            "question": "Ichki hovli oddiy orqa hovlidan fazoviy jihatdan farq qilishi mumkinmi?",
            "explanation": (
                "Ichki hovli ko'pincha bino massasi bilan qisman yoki to'liq o'raladi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L04_M03_002": [
        {
            "code": "L04_Q034",
            "question": "Living va hovli o'rtasidagi bevosita aloqa foydalimi?",
            "explanation": (
                "Ichki va tashqi yashash makonlarini birlashtirish mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L04_Q035",
            "question": "Chiroyli hovliga faqat service koridor orqali chiqish kuchli yechimmi?",
            "explanation": (
                "Asosiy yashash xonalari bilan aloqa zaif bo'lsa hovli kam ishlatilishi mumkin."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L04_Q036",
            "question": "Dining va hovli aloqasi tashqi ovqatlanishga yordam beradimi?",
            "explanation": (
                "Diningdan hovliga qulay chiqish tashqi foydalanishni osonlashtiradi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L04_M03_003": [
        {
            "code": "L04_Q037",
            "question": "Ichki hovli family privacyga yordam berishi mumkinmi?",
            "explanation": (
                "Uy massasi ko'cha va qo'shnilardan himoyalangan tashqi makon yaratishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L04_Q038",
            "question": "Ko'cha tomonda yopiqroq, hovli tomonda ochiqroq fasad ishlatilishi mumkinmi?",
            "explanation": (
                "Bu privacy va ichki-tashqi aloqani boshqarish usullaridan biri."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L04_Q039",
            "question": "Privacy faqat baland devor orqali yaratiladimi?",
            "explanation": (
                "Bino joylashuvi, ko'rish yo'nalishi va landshaft ham privacy yaratadi."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
    ],

    "L04_M03_004": [
        {
            "code": "L04_Q040",
            "question": "Ichki hovli uy ichiga qo'shimcha tabiiy yorug'lik olib kirishi mumkinmi?",
            "explanation": (
                "Chuqur planlarda hovli ichki fasadlar orqali yorug'lik manbai bo'lishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L04_Q041",
            "question": "Ichki hovli shamollatishga yordam berishi mumkinmi?",
            "explanation": (
                "To'g'ri tashkil qilingan ochilishlar havo harakatiga yordam berishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L04_Q042",
            "question": "Juda tor va baland courtyard yorug'lik sifatini pasaytirishi mumkinmi?",
            "explanation": (
                "Hovli proporsiyasi uning yorug'lik va ochiqlik sifatiga ta'sir qiladi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L04_M03_005": [
        {
            "code": "L04_Q043",
            "question": "Ichki hovli living bilan umuman bog'lanmagan bo'lsa bu zaif yechim bo'lishi mumkinmi?",
            "explanation": (
                "Hovli kundalik yashash makoni bilan bog'lanmasa kam foydalanilishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L04_Q044",
            "question": "Family ichki hovlisidan avtomobil yo'li o'tishi muammo bo'lishi mumkinmi?",
            "explanation": (
                "Bu xavfsizlik, shovqin va privacyga salbiy ta'sir qilishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L04_Q045",
            "question": "Ichki hovli auditidagi asosiy savollardan biri qaysi?",
            "explanation": (
                "Hovli kim tomonidan va qanday ishlatilishini tushunish muhim."
            ),
            "options": [
                ("A", "Kim foydalanadi va living bilan aloqasi bormi?", True),
                ("B", "Faqat tom rangi qanday?", False),
            ],
        },
    ],
}


# ============================================================
# DATABASE SEED
# ============================================================

def seed_level04_module03():
    connection = get_connection()

    try:
        cursor = connection.cursor()

        for (
            module_code,
            lesson_code,
            title,
            lesson_type,
            summary,
            sort_order,
            estimated_minutes,
            xp_reward,
        ) in LEVEL04_MODULE03_LESSONS:

            cursor.execute(
                """
                SELECT id
                FROM course_modules
                WHERE code = ?
                LIMIT 1
                """,
                (module_code,),
            )

            module = cursor.fetchone()

            if module is None:
                continue

            cursor.execute(
                """
                INSERT INTO lessons (
                    module_id,
                    code,
                    title,
                    lesson_type,
                    summary,
                    sort_order,
                    estimated_minutes,
                    xp_reward,
                    passing_score,
                    is_required
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
                    module["id"],
                    lesson_code,
                    title,
                    lesson_type,
                    summary,
                    sort_order,
                    estimated_minutes,
                    xp_reward,
                    80,
                    1,
                ),
            )

        connection.commit()

    finally:
        connection.close()
