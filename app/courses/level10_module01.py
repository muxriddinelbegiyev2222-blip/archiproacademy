from database.database import get_connection


LEVEL10_MODULE01_LESSONS = [
    ("L10_M01", "L10_M01_001", "Texnik topshiriq nima?", "theory",
     "Uy loyihasini boshlashdan oldin mijoz ehtiyojlarini tizimli hujjatga aylantirish.", 1, 40, 20),

    ("L10_M01", "L10_M01_002", "Oila va yashash ssenariysi", "theory",
     "Oila tarkibi, kundalik hayot va mehmon qabul qilish odatlarini tahlil qilish.", 2, 45, 20),

    ("L10_M01", "L10_M01_003", "Xonalar dasturi", "practice",
     "Kerakli xonalar, zonalar va ularning funksional aloqalarini shakllantirish.", 3, 50, 20),

    ("L10_M01", "L10_M01_004", "Cheklovlar va ustuvorliklar", "practice",
     "Uchastka, budjet, konstruksiya va mijoz istaklarini ustuvorlik bo'yicha ajratish.", 4, 50, 20),

    ("L10_M01", "L10_M01_005", "Professional brief audit", "practice",
     "Texnik topshiriqni loyiha boshlanishidan oldin to'liq tekshirish.", 5, 55, 25),
]


LEVEL10_MODULE01_CONTENT = {
    "L10_M01_001": [
        {
            "title": "Loyiha chizishdan oldin savol bering",
            "type": "highlight",
            "text": """
            Professional loyiha
            qalam yoki Archicad'dan
            boshlanmaydi.

            <br><br>

            Avval mijozning
            real ehtiyoji
            tushuniladi.
            """,
        },
        {
            "title": "Texnik topshiriq",
            "type": "normal",
            "text": """
            Texnik topshiriq —

            <br><br>

            • kim yashaydi;<br>
            • qanday yashaydi;<br>
            • qanday xonalar kerak;<br>
            • qanday cheklovlar bor;<br>
            • asosiy ustuvorlik nima

            <br><br>

            degan savollarning
            tizimli javobi.
            """,
        },
        {
            "title": "Xato",
            "type": "warning",
            "text": """
            Mijoz:
            “3 ta yotoqxona kerak”

            <br><br>

            dedi.

            <br><br>

            Shu bilan
            topshiriq tayyor
            deb hisoblamang.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Bir mijoz bilan
            birinchi suhbat uchun

            <br><br>

            15 ta savol
            tayyorlang.
            """,
        },
    ],

    "L10_M01_002": [
        {
            "title": "Uy oila uchun ishlaydi",
            "type": "highlight",
            "text": """
            Bir xil maydondagi
            uy

            <br><br>

            turli oilalar uchun
            butunlay boshqacha
            rejalashtirilishi mumkin.
            """,
        },
        {
            "title": "O'rganing",
            "type": "normal",
            "text": """
            • oila a'zolari;<br>
            • bolalar yoshi;<br>
            • mehmonlar soni;<br>
            • ish/uy rejimi;<br>
            • ovqatlanish odati;<br>
            • privacy talabi.
            """,
        },
        {
            "title": "Tasavvur qiling",
            "type": "example",
            "text": """
            4 kishilik
            ikki oila bor.

            <br><br>

            Birinchisi tez-tez
            mehmon kutadi.

            <br><br>

            Ikkinchisi esa
            ko'proq private
            yashaydi.

            <br><br>

            Planlari bir xil
            bo'lishi shart emas.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Oila uchun
            “bir kunlik hayot”

            <br><br>

            ssenariysini
            yozib chiqing.
            """,
        },
    ],

    "L10_M01_003": [
        {
            "title": "Xonalar ro'yxati",
            "type": "highlight",
            "text": """
            Xonalar ro'yxati
            faqat nomlardan
            iborat bo'lmasligi kerak.
            """,
        },
        {
            "title": "Har xona uchun",
            "type": "normal",
            "text": """
            • vazifa;<br>
            • foydalanuvchi;<br>
            • taxminiy ustuvorlik;<br>
            • boshqa xona bilan aloqa;<br>
            • tabiiy yorug'lik ehtiyoji

            <br><br>

            yoziladi.
            """,
        },
        {
            "title": "Zonalash",
            "type": "normal",
            "text": """
            Xonalarni:

            <br><br>

            PUBLIC
            PRIVATE
            SERVICE

            <br><br>

            guruhlarga ajratish
            boshlang'ich
            tartib beradi.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            4 kishilik
            bir qavatli uy uchun

            <br><br>

            xona programmasini
            tuzing.
            """,
        },
    ],

    "L10_M01_004": [
        {
            "title": "Istak va cheklov",
            "type": "highlight",
            "text": """
            Mijoz istagi
            bilan real
            loyiha imkoniyati

            <br><br>

            har doim bir xil
            bo'lmasligi mumkin.
            """,
        },
        {
            "title": "Cheklovlar",
            "type": "normal",
            "text": """
            • uchastka;<br>
            • normativ;<br>
            • budjet;<br>
            • konstruksiya;<br>
            • iqlim;<br>
            • vaqt.
            """,
        },
        {
            "title": "Ustuvorlik",
            "type": "warning",
            "text": """
            “Hammasi muhim”
            degan topshiriq

            <br><br>

            qaror qabul qilishni
            qiyinlashtiradi.
            """,
        },
        {
            "title": "3 daraja",
            "type": "example",
            "text": """
            Talablarni:

            <br><br>

            MUST HAVE
            NICE TO HAVE
            OPTIONAL

            <br><br>

            guruhlarga ajrating.
            """,
        },
    ],

    "L10_M01_005": [
        {
            "title": "Brief audit",
            "type": "highlight",
            "text": """
            Mijoz
            → Oila
            → Hayot tarzi
            → Xonalar
            → Ustuvorlik
            → Cheklov
            → Tasdiqlash
            """,
        },
        {
            "title": "Professional checklist",
            "type": "example",
            "text": """
            <b>1.</b> Oila tarkibi aniqmi?<br><br>
            <b>2.</b> Kundalik ssenariy tushunarlimi?<br><br>
            <b>3.</b> Xonalar ro'yxati bormi?<br><br>
            <b>4.</b> Zonalash talabi aniqmi?<br><br>
            <b>5.</b> Uchastka cheklovlari ma'lummi?<br><br>
            <b>6.</b> Budjet haqida tushuncha bormi?<br><br>
            <b>7.</b> MUST/NICE/OPTIONAL ajratilganmi?<br><br>
            <b>8.</b> Mijoz briefni tasdiqlaganmi?
            """,
        },
        {
            "title": "Muhim qoida",
            "type": "warning",
            "text": """
            Texnik topshiriq
            tushunarsiz bo'lsa,

            <br><br>

            keyingi chizmalar
            tez-tez qayta
            ishlanishi mumkin.
            """,
        },
        {
            "title": "Keyingi modul",
            "type": "highlight",
            "text": """
            Keyingi bosqich:
            SITE ANALYSIS.
            """,
        },
    ],
}


LEVEL10_MODULE01_QUIZ = {
    "L10_M01_001": [
        {"code": "L10_Q001", "question": "Professional uy loyihasi mijoz ehtiyojini tushunishdan boshlanadimi?", "explanation": "Texnik topshiriq keyingi loyiha qarorlari uchun asos bo'ladi.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
        {"code": "L10_Q002", "question": "Faqat xonalar sonini bilish to'liq brief uchun yetarlimi?", "explanation": "Hayot tarzi, ustuvorlik va cheklovlar ham muhim.", "options": [("A", "Ha", False), ("B", "Yo'q", True)]},
        {"code": "L10_Q003", "question": "Texnik topshiriq keyingi loyiha qarorlariga ta'sir qiladimi?", "explanation": "Brief loyiha maqsadi va cheklovlarini belgilaydi.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
    ],
    "L10_M01_002": [
        {"code": "L10_Q004", "question": "Bir xil tarkibli ikki oila uchun plan har doim bir xil bo'lishi kerakmi?", "explanation": "Hayot tarzi va odatlar farq qilishi mumkin.", "options": [("A", "Ha", False), ("B", "Yo'q", True)]},
        {"code": "L10_Q005", "question": "Mehmon kutish odati plan yechimiga ta'sir qiladimi?", "explanation": "Public va private zonalarning aloqasi o'zgarishi mumkin.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
        {"code": "L10_Q006", "question": "Bolalar yoshi xona programmasiga ta'sir qilishi mumkinmi?", "explanation": "Foydalanish ssenariysi vaqt o'tishi bilan ham o'zgaradi.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
    ],
    "L10_M01_003": [
        {"code": "L10_Q007", "question": "Xona dasturida faqat xona nomi yetarlimi?", "explanation": "Funksiya va aloqalar ham yozilishi kerak.", "options": [("A", "Ha", False), ("B", "Yo'q", True)]},
        {"code": "L10_Q008", "question": "Public, private va service zonalash foydalimi?", "explanation": "Bu uy funksional strukturasini tushunishga yordam beradi.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
        {"code": "L10_Q009", "question": "Xonalar orasidagi aloqa texnik topshiriqda muhimmi?", "explanation": "Aloqalar keyingi bubble diagram va plan uchun asos bo'ladi.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
    ],
    "L10_M01_004": [
        {"code": "L10_Q010", "question": "Mijozning barcha istaklari real cheklovlardan mustaqilmi?", "explanation": "Uchastka, budjet va boshqa omillar yechimga ta'sir qiladi.", "options": [("A", "Ha", False), ("B", "Yo'q", True)]},
        {"code": "L10_Q011", "question": "Talablarni ustuvorlikka ajratish foydalimi?", "explanation": "Bu qaror qabul qilishni osonlashtiradi.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
        {"code": "L10_Q012", "question": "MUST HAVE va OPTIONAL bir xil darajami?", "explanation": "Ularning loyiha ustuvorligi farq qiladi.", "options": [("A", "Ha", False), ("B", "Yo'q", True)]},
    ],
    "L10_M01_005": [
        {"code": "L10_Q013", "question": "Brief mijoz bilan tasdiqlanishi kerakmi?", "explanation": "Bu keyingi loyiha bosqichlari uchun umumiy asos yaratadi.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
        {"code": "L10_Q014", "question": "Tushunarsiz brief ko'p qayta ishlashga olib kelishi mumkinmi?", "explanation": "Boshlang'ich talablar noaniq bo'lsa qarorlar tez-tez o'zgaradi.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
        {"code": "L10_Q015", "question": "Texnik topshiriq workflow'ining to'g'ri ketma-ketligi qaysi?", "explanation": "Oila va ehtiyojlar tushunilib, xona programmasi va cheklovlar shakllantiriladi.", "options": [("A", "Oila → hayot tarzi → xonalar → ustuvorlik → cheklov → tasdiqlash", True), ("B", "Darhol Archicad → keyin mijozdan so'rash", False)]},
    ],
}


def seed_level10_module01():
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
        ) in LEVEL10_MODULE01_LESSONS:

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
