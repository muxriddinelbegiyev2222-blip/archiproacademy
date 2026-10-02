from database.database import get_connection


LEVEL02_MODULE04_LESSONS = [
    (
        "L02_M04",
        "L02_M04_001",
        "Xona maydoni va proporsiyasi",
        "theory",
        "Bir xil maydondagi xonalar nega turlicha qulay ishlashini tushunish.",
        1,
        30,
        15,
    ),
    (
        "L02_M04",
        "L02_M04_002",
        "Tor va uzun xonalar",
        "theory",
        "Xona geometriyasining mebel va harakatga ta'sirini tahlil qilish.",
        2,
        35,
        20,
    ),
    (
        "L02_M04",
        "L02_M04_003",
        "Foydali devorlar va o'lik burchaklar",
        "theory",
        "Mebel joylashtirish mumkin bo'lgan devorlar va samarasiz zonalarni aniqlash.",
        3,
        35,
        20,
    ),
    (
        "L02_M04",
        "L02_M04_004",
        "Deraza va eshik joylashuvining xona sifatiga ta'siri",
        "practice",
        "Ochilishlar xona ichidagi mebel va foydalanish imkoniyatini qanday o'zgartirishini tushunish.",
        4,
        40,
        20,
    ),
    (
        "L02_M04",
        "L02_M04_005",
        "Xona sifati xatolarini topish",
        "practice",
        "Real planlarda maydon, proporsiya va foydali geometriya xatolarini aniqlash.",
        5,
        45,
        25,
    ),
]


LEVEL02_MODULE04_CONTENT = {
    "L02_M04_001": [
        {
            "title": "Kvadrat metrning o'zi yetmaydi",
            "type": "highlight",
            "text": """
            Xona maydoni muhim.

            <br><br>

            Lekin faqat m² raqamiga qarab
            xona sifatini baholab bo'lmaydi.

            <br><br>

            <b>Shakl va proporsiya</b> ham juda muhim.
            """,
        },
        {
            "title": "Misol",
            "type": "example",
            "text": """
            16 m² ikki xona:

            <br><br>

            4 × 4 m

            <br><br>

            va

            <br><br>

            2 × 8 m.

            <br><br>

            Maydon bir xil.

            <br><br>

            Lekin mebel joylashtirish va foydalanish
            butunlay boshqacha bo'lishi mumkin.
            """,
        },
        {
            "title": "Yaxshi proporsiya nima?",
            "type": "normal",
            "text": """
            Yaxshi proporsiya — xonaning vazifasiga mos
            ishlaydigan geometriya.

            <br><br>

            Masalan:

            <br><br>

            • yotoqxona uchun krovat va shkaf sig'adi;<br>
            • mehmonxonada o'tirish zonasi ishlaydi;<br>
            • oshxonada ish zonasi uzilmaydi.
            """,
        },
        {
            "title": "Boshlovchi xatosi",
            "type": "warning",
            "text": """
            “Xona 18 m² ekan, demak yaxshi.”

            <br><br>

            Bu xulosa yetarli emas.

            <br><br>

            18 m² xona noto'g'ri shakl yoki
            noto'g'ri eshik-deraza joylashuvi sabab
            12 m² qulay xonadan yomonroq ishlashi mumkin.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            12 m² va 16 m² ikkita xona toping.

            <br><br>

            Qaysi birida mebelni qulayroq joylashtirish mumkinligini
            faqat maydonga emas, shaklga qarab tahlil qiling.
            """,
        },
    ],

    "L02_M04_002": [
        {
            "title": "Tor va uzun xona",
            "type": "highlight",
            "text": """
            Xona juda tor va uzun bo'lsa,
            katta maydon bo'lsa ham
            foydalanish qiyinlashishi mumkin.
            """,
        },
        {
            "title": "Nima uchun?",
            "type": "normal",
            "text": """
            Tor xonada:

            <br><br>

            • mebel ikki tomonda to'qnashishi mumkin;<br>
            • yurish yo'li torayadi;<br>
            • markaziy zona foydasiz qoladi;<br>
            • katta mebel joylashtirish qiyinlashadi.
            """,
        },
        {
            "title": "Misol",
            "type": "example",
            "text": """
            2.2 × 7 metr xona tasavvur qiling.

            <br><br>

            Maydoni taxminan 15.4 m².

            <br><br>

            Lekin ikki tomonlama mebel qo'ysangiz,
            o'rtadagi yurish yo'li juda tor bo'lishi mumkin.
            """,
        },
        {
            "title": "Har bir tor xona yomonmi?",
            "type": "warning",
            "text": """
            Yo'q.

            <br><br>

            Masalan, garderob, galereya yoki
            maxsus funksional makon uchun
            uzun shakl foydali bo'lishi mumkin.

            <br><br>

            Muhim narsa — <b>funksiyaga moslik</b>.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Tor va uzun xonani tanlang.

            <br><br>

            3 ta savol:

            <br><br>

            1. Mebel qayerga tushadi?<br>
            2. Asosiy yurish yo'li qayerdan o'tadi?<br>
            3. Xonaning qaysi qismi foydasiz qolmoqda?
            """,
        },
    ],

    "L02_M04_003": [
        {
            "title": "Foydali devor nima?",
            "type": "highlight",
            "text": """
            Foydali devor — mebel, jihoz yoki
            funksional element joylashtirish mumkin bo'lgan
            amalda ishlatiladigan devor qismi.
            """,
        },
        {
            "title": "Eshik devorni bo'ladi",
            "type": "example",
            "text": """
            4 metrli devorda eshik o'rtada joylashgan.

            <br><br>

            Natijada bitta 4 metrlik foydali devor o'rniga
            ikkita kichik bo'lak paydo bo'ladi.

            <br><br>

            Katta shkaf yoki TV zona uchun
            bu noqulay bo'lishi mumkin.
            """,
        },
        {
            "title": "O'lik burchak",
            "type": "normal",
            "text": """
            O'lik burchak — xona ichida
            amalda foydalana olmaydigan
            yoki juda samarasiz ishlaydigan zona.

            <br><br>

            U:

            <br><br>

            • noto'g'ri eshik;<br>
            • diagonal devor;<br>
            • g'alati chiqinti;<br>
            • ikki ochilish orasidagi kichik bo'lak

            <br><br>

            sabab paydo bo'lishi mumkin.
            """,
        },
        {
            "title": "Xato",
            "type": "warning",
            "text": """
            Xonada 5 ta devor bor.

            <br><br>

            Lekin deraza, eshik va chiqintilar sabab
            ulardan faqat bittasi real mebel uchun ishlaydi.

            <br><br>

            Maydon katta bo'lsa ham xona sifati past bo'lishi mumkin.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Bir yotoqxona planini oling.

            <br><br>

            Har bir devorni tekshiring:

            <br><br>

            • krovat qo'yish mumkinmi?<br>
            • shkaf qo'yish mumkinmi?<br>
            • TV yoki stol qo'yish mumkinmi?

            <br><br>

            Nechta haqiqiy foydali devor qoldi?
            """,
        },
    ],

    "L02_M04_004": [
        {
            "title": "Deraza — faqat yorug'lik emas",
            "type": "highlight",
            "text": """
            Deraza xona ichidagi
            mebel joylashuvi va foydalanishiga ham ta'sir qiladi.
            """,
        },
        {
            "title": "Deraza o'rtada bo'lsa",
            "type": "example",
            "text": """
            Devorning o'rtasida katta deraza bo'lsa,
            shu devorga baland shkaf qo'yib bo'lmaydi.

            <br><br>

            Demak, deraza qarori
            mebel qarori bilan bog'liq.
            """,
        },
        {
            "title": "Eshikning joyi",
            "type": "example",
            "text": """
            Eshik devor markazida bo'lsa,
            ikki tomonda kichik-kichik devor bo'laklari qoladi.

            <br><br>

            Eshik burchakka yaqinroq joylashsa,
            katta uzluksiz devor saqlanishi mumkin.

            <br><br>

            Lekin bu ham harakat va ergonomika bilan tekshiriladi.
            """,
        },
        {
            "title": "Deraza va krovat",
            "type": "normal",
            "text": """
            Yotoqxonada deraza joylashuvi
            krovat, shkaf va ish stolining
            mantiqiy joylashuviga ta'sir qiladi.

            <br><br>

            Shuning uchun fasad va plan birgalikda ishlaydi.
            """,
        },
        {
            "title": "Boshlovchi xatosi",
            "type": "warning",
            "text": """
            Fasad chiroyli ko'rinsin deb
            barcha derazalarni tashqaridan bir xil joylashtirish,
            ichki mebelni qiyinlashtirishi mumkin.

            <br><br>

            Har bir ochilishning ikki tomoni bor:

            <br><br>

            tashqi fasad va ichki xona.
            """,
        },
    ],

    "L02_M04_005": [
        {
            "title": "Xona sifatini tekshiramiz",
            "type": "highlight",
            "text": """
            Endi xona maydoniga emas,
            uning haqiqiy ishlash sifatiga qaraymiz.
            """,
        },
        {
            "title": "Xato 1 — katta, lekin foydasiz",
            "type": "warning",
            "text": """
            Xona 22 m².

            <br><br>

            Lekin uchta eshik va ikkita deraza
            barcha asosiy devorlarni bo'lib tashlagan.

            <br><br>

            Mebel joylashtirish qiyin.
            """,
        },
        {
            "title": "Xato 2 — tor uzun geometriya",
            "type": "warning",
            "text": """
            Xona maydoni yetarli.

            <br><br>

            Lekin eni juda kichik.

            <br><br>

            Natijada mebel va harakat bir-biriga xalaqit beradi.
            """,
        },
        {
            "title": "Xato 3 — keraksiz burchak",
            "type": "warning",
            "text": """
            Xonaga dekorativ diagonal devor qo'shilgan.

            <br><br>

            Natijada g'alati uchburchak zona paydo bo'lgan.

            <br><br>

            Unga normal mebel joylashtirib bo'lmaydi.
            """,
        },
        {
            "title": "Xato 4 — eshik noto'g'ri joyda",
            "type": "warning",
            "text": """
            Eshik markazda.

            <br><br>

            Shu sababli katta shkaf uchun
            uzluksiz devor qolmagan.

            <br><br>

            Eshik joyini ozgina o'zgartirish
            xonani ancha samarali qilishi mumkin.
            """,
        },
        {
            "title": "Professional tekshiruv",
            "type": "example",
            "text": """
            Har bir xona uchun:

            <br><br>

            <b>1.</b> Maydoni qancha?<br><br>
            <b>2.</b> Proporsiyasi qanday?<br><br>
            <b>3.</b> Nechta foydali devor bor?<br><br>
            <b>4.</b> O'lik burchak bormi?<br><br>
            <b>5.</b> Eshik va derazalar mebelga xalaqit beradimi?<br><br>
            <b>6.</b> Kichikroq, lekin yaxshiroq yechim mumkinmi?
            """,
        },
        {
            "title": "Mini-loyiha",
            "type": "example",
            "text": """
            3 ta yotoqxona planini toping.

            <br><br>

            Faqat m² bo'yicha emas,
            quyidagicha solishtiring:

            <br><br>

            • proporsiya;<br>
            • foydali devor;<br>
            • krovat joylashuvi;<br>
            • shkaf joylashuvi;<br>
            • yurish yo'li.

            <br><br>

            Qaysi biri real hayotda eng yaxshi ishlashini asoslang.
            """,
        },
        {
            "title": "Modul yakuni",
            "type": "highlight",
            "text": """
            Siz endi:

            <br><br>

            ✓ xona maydoni;<br>
            ✓ proporsiya;<br>
            ✓ tor-uzun xona;<br>
            ✓ foydali devor;<br>
            ✓ o'lik burchak;<br>
            ✓ eshik va deraza ta'siri

            <br><br>

            orqali makon sifatini tahlil qila olasiz.

            <br><br>

            Keyingi modul:
            <b>Public va private makonlar chuqur tahlili.</b>
            """,
        },
    ],
}


LEVEL02_MODULE04_QUIZ = {
    "L02_M04_001": [
        {
            "code": "L02_Q046",
            "question": "Bir xil maydondagi ikki xona qulayligi bir xil bo'lishi shartmi?",
            "explanation": (
                "Xona shakli, proporsiyasi va ochilishlari foydalanish sifatini o'zgartiradi."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L02_Q047",
            "question": "4×4 m va 2×8 m xonalarning maydoni bir xil bo'lishi mumkinmi?",
            "explanation": (
                "Ikkalasi ham 16 m², lekin proporsiyasi boshqacha."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L02_Q048",
            "question": "Xona sifatini faqat m² bilan baholash yetarlimi?",
            "explanation": (
                "Proporsiya, mebel va foydalanish imkoniyati ham muhim."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
    ],

    "L02_M04_002": [
        {
            "code": "L02_Q049",
            "question": "Tor va uzun xona katta maydon bo'lsa ham noqulay bo'lishi mumkinmi?",
            "explanation": (
                "Tor eni mebel va yurish zonalarini cheklashi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L02_Q050",
            "question": "Har qanday uzun xona yomonmi?",
            "explanation": (
                "Ayrim funksiyalar uchun uzun shakl foydali bo'lishi mumkin."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L02_Q051",
            "question": "Xona geometriyasi nimaga ta'sir qiladi?",
            "explanation": (
                "Mebel joylashuvi va harakatga."
            ),
            "options": [
                ("A", "Mebel va harakatga", True),
                ("B", "Faqat fasad rangiga", False),
            ],
        },
    ],

    "L02_M04_003": [
        {
            "code": "L02_Q052",
            "question": "Foydali devor nima?",
            "explanation": (
                "Mebel yoki funksional element joylashtirish mumkin bo'lgan amalda ishlatiladigan devor."
            ),
            "options": [
                ("A", "Amalda ishlatiladigan devor qismi", True),
                ("B", "Faqat tashqi devor", False),
            ],
        },
        {
            "code": "L02_Q053",
            "question": "Eshik devorning foydali uzunligini kamaytirishi mumkinmi?",
            "explanation": (
                "Ochilish devorni kichik bo'laklarga ajratishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L02_Q054",
            "question": "O'lik burchak nima?",
            "explanation": (
                "Amalda juda samarasiz yoki foydalana olmaydigan zona."
            ),
            "options": [
                ("A", "Samarasiz zona", True),
                ("B", "Faqat tashqi fasad burchagi", False),
            ],
        },
    ],

    "L02_M04_004": [
        {
            "code": "L02_Q055",
            "question": "Deraza joylashuvi mebelga ta'sir qiladimi?",
            "explanation": (
                "Deraza ayrim devorlardan baland mebel uchun foydalanishni cheklashi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L02_Q056",
            "question": "Eshikni devor markaziga qo'yish har doim eng yaxshi yechimmi?",
            "explanation": (
                "Eshik joyi foydali devor va harakat bilan birga tahlil qilinadi."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L02_Q057",
            "question": "Fasad derazasi va ichki xona birgalikda hal qilinadimi?",
            "explanation": (
                "Deraza tashqi kompozitsiya va ichki foydalanishga bir vaqtning o'zida ta'sir qiladi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L02_M04_005": [
        {
            "code": "L02_Q058",
            "question": "Katta xona ko'p ochilish sabab mebel uchun noqulay bo'lishi mumkinmi?",
            "explanation": (
                "Ko'p eshik va deraza foydali devorlarni kamaytirishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L02_Q059",
            "question": "Diagonal devor o'lik burchak yaratishi mumkinmi?",
            "explanation": (
                "Asossiz diagonal geometriya mebel uchun foydasiz zonalar yaratishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L02_Q060",
            "question": "Professional xona tahlilida qaysi savol foydali?",
            "explanation": (
                "Foydali devorlar va mebel imkoniyatini tekshirish xona sifatini baholashga yordam beradi."
            ),
            "options": [
                ("A", "Nechta foydali devor bor?", True),
                ("B", "Faqat fasad rangi qanday?", False),
            ],
        },
    ],
}


def seed_level02_module04():
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
        ) in LEVEL02_MODULE04_LESSONS:

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
