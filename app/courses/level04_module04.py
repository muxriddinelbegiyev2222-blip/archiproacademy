from database.database import get_connection


# ============================================================
# LEVEL 4
# MODULE 04 - AYVON VA TERASSA
# ============================================================

LEVEL04_MODULE04_LESSONS = [
    (
        "L04_M04",
        "L04_M04_001",
        "Ayvon va terassa nima?",
        "theory",
        "Ochiq va yarim ochiq yashash makonlarining vazifasini tushunish.",
        1,
        40,
        20,
    ),
    (
        "L04_M04",
        "L04_M04_002",
        "Ichki va tashqi makon o'tishi",
        "theory",
        "Living, dining va hovlini ayvon yoki terassa orqali bog'lash.",
        2,
        40,
        20,
    ),
    (
        "L04_M04",
        "L04_M04_003",
        "Quyosh va soya",
        "theory",
        "Ayvon va terassadan quyoshdan himoyalanish uchun foydalanish.",
        3,
        45,
        20,
    ),
    (
        "L04_M04",
        "L04_M04_004",
        "Ayvon ergonomikasi va mebel",
        "practice",
        "O'tirish, ovqatlanish va harakat uchun qulay tashqi makon yaratish.",
        4,
        45,
        20,
    ),
    (
        "L04_M04",
        "L04_M04_005",
        "Ayvon va terassa auditi",
        "practice",
        "Ochiq va yarim ochiq makonlardagi tipik rejalash xatolarini aniqlash.",
        5,
        55,
        25,
    ),
]


# ============================================================
# CONTENT
# ============================================================

LEVEL04_MODULE04_CONTENT = {
    "L04_M04_001": [
        {
            "title": "Ayvon — ichki va tashqi makon orasidagi ko'prik",
            "type": "highlight",
            "text": """
            Ayvon yoki terassa
            uy ichidan hovliga o'tishda
            oraliq makon yaratadi.

            <br><br>

            U to'liq yopiq xona ham emas,
            oddiy ochiq hovli ham emas.
            """,
        },
        {
            "title": "Asosiy vazifalar",
            "type": "normal",
            "text": """
            Ayvon yoki terassa:

            <br><br>

            • dam olish;<br>
            • mehmon kutish;<br>
            • tashqi ovqatlanish;<br>
            • soyalanish;<br>
            • yomg'irdan himoya;<br>
            • hovliga o'tish

            <br><br>

            uchun ishlatilishi mumkin.
            """,
        },
        {
            "title": "Tasavvur qiling",
            "type": "example",
            "text": """
            Livingning katta eshigi to'g'ridan-to'g'ri
            issiq ochiq hovliga chiqadi.

            <br><br>

            Oraliq soyali makon yo'q.

            <br><br>

            Ikkinchi variantda esa
            living oldida chuqur ayvon bor.

            <br><br>

            Ikki holatning foydalanish sifati
            juda farq qilishi mumkin.
            """,
        },
        {
            "title": "Ayvon uy rejasining bir qismi",
            "type": "highlight",
            "text": """
            Ayvonni loyiha oxirida
            tasodifiy qo'shiladigan element
            deb qabul qilish noto'g'ri.

            <br><br>

            U bino va hovli bilan
            birga rejalashtiriladi.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Bir uy rejasida
            ayvon uchun 3 ta joy tanlang.

            <br><br>

            Har birida:
            kim foydalanadi,
            qachon foydalanadi,
            nimaga yaqin bo'lishi kerak

            <br><br>

            deb yozing.
            """,
        },
    ],

    "L04_M04_002": [
        {
            "title": "Ichki makon tashqarida davom etadi",
            "type": "highlight",
            "text": """
            Kuchli terassa
            uy ichidagi funksiyani
            tashqariga davom ettirishi mumkin.
            """,
        },
        {
            "title": "Living → terassa",
            "type": "normal",
            "text": """
            Livingdan terassaga
            bevosita chiqish bo'lsa,

            <br><br>

            kundalik oilaviy foydalanish
            tabiiyroq bo'lishi mumkin.
            """,
        },
        {
            "title": "Dining → tashqi dining",
            "type": "normal",
            "text": """
            Ichki dining va
            tashqi ovqatlanish zonasi
            bir-biriga yaqin bo'lsa,

            <br><br>

            mavsumiy foydalanish qulaylashadi.
            """,
        },
        {
            "title": "Kitchen → terassa",
            "type": "example",
            "text": """
            Oshxona yaqin bo'lsa,
            ovqat va idishlarni
            tashqariga olib chiqish osonlashadi.
            """,
        },
        {
            "title": "Pol darajasi",
            "type": "normal",
            "text": """
            Ichki va tashqi makon orasidagi
            balandlik farqi ham muhim.

            <br><br>

            Keraksiz katta pog'ona
            circulationni noqulay qilishi mumkin.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Bir sxema chizing:

            <br><br>

            LIVING → TERASSA → HOVLI

            <br><br>

            va har bir o'tish nuqtasini tekshiring.
            """,
        },
    ],

    "L04_M04_003": [
        {
            "title": "Ayvon soyalanish vositasi",
            "type": "highlight",
            "text": """
            Issiq iqlimda
            yarim ochiq soyali makon
            juda muhim bo'lishi mumkin.
            """,
        },
        {
            "title": "Chuqurlik",
            "type": "normal",
            "text": """
            Ayvon chuqurligi
            uning soyalanish sifatiga ta'sir qiladi.

            <br><br>

            Juda sayoz ayvon
            kutilgan soyani bermasligi mumkin.
            """,
        },
        {
            "title": "Orientatsiya",
            "type": "normal",
            "text": """
            Bir xil ayvon
            turli yo'nalishlarda
            turlicha ishlashi mumkin.

            <br><br>

            Quyosh yo'nalishi
            albatta hisobga olinadi.
            """,
        },
        {
            "title": "G'arbiy quyosh",
            "type": "example",
            "text": """
            G'arb tomonda kechki quyosh
            pastroq burchakdan kelishi mumkin.

            <br><br>

            Faqat gorizontal soyabon
            har doim yetarli bo'lmasligi mumkin.
            """,
        },
        {
            "title": "Qo'shimcha himoya",
            "type": "normal",
            "text": """
            Zarur bo'lsa:

            <br><br>

            • pergola;<br>
            • vertikal lamel;<br>
            • yashil ekran;<br>
            • daraxt;<br>
            • chuqur ayvon

            <br><br>

            ishlatilishi mumkin.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Bir terassa tanlang.

            <br><br>

            Unda ertalab,
            tushda va kechqurun
            quyosh qayerdan kelishini belgilang.
            """,
        },
    ],

    "L04_M04_004": [
        {
            "title": "Ayvon ham ergonomik makon",
            "type": "highlight",
            "text": """
            Terassa katta bo'lishi yetarli emas.

            <br><br>

            Undagi mebel,
            o'tish yo'llari
            va foydalanish ssenariysi
            birga ishlashi kerak.
            """,
        },
        {
            "title": "Ovqatlanish zonasi",
            "type": "normal",
            "text": """
            Tashqi dining uchun:

            <br><br>

            • stol;<br>
            • stullar;<br>
            • stul orqasida yurish joyi;<br>
            • xizmat ko'rsatish yo'li

            <br><br>

            hisobga olinadi.
            """,
        },
        {
            "title": "Dam olish zonasi",
            "type": "normal",
            "text": """
            Sofa va kreslolar
            shunchaki devor bo'ylab terilmaydi.

            <br><br>

            Suhbat,
            manzara,
            hovli va harakat
            bilan bog'lanadi.
            """,
        },
        {
            "title": "Circulation",
            "type": "warning",
            "text": """
            Livingdan hovliga o'tish uchun
            odamlar doim stol orasidan
            siqilib o'tishga majbur bo'lsa,

            <br><br>

            mebel joylashuvi noto'g'ri.
            """,
        },
        {
            "title": "Mangalga yaqinlik",
            "type": "example",
            "text": """
            Dining mangalga yaqin bo'lishi mumkin,

            <br><br>

            lekin tutun va issiqlik
            o'tirish zonasiga xalaqit bermasligi kerak.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            4 × 6 metr terassa chizing.

            <br><br>

            Unda:

            <br><br>

            • 8 kishilik stol;<br>
            • dam olish zona;<br>
            • asosiy yurish yo'li

            <br><br>

            ni joylashtiring.
            """,
        },
    ],

    "L04_M04_005": [
        {
            "title": "Ayvon va terassa auditini boshlaymiz",
            "type": "highlight",
            "text": """
            Endi yarim ochiq makonni
            faqat fasad bezagi emas,

            <br><br>

            real kundalik yashash maydoni
            sifatida tekshiramiz.
            """,
        },
        {
            "title": "Xato 1 — terassa noto'g'ri xonaga ulangan",
            "type": "warning",
            "text": """
            Katta terassa mavjud.

            <br><br>

            Lekin unga faqat
            koridor yoki service xona orqali chiqiladi.
            """,
        },
        {
            "title": "Xato 2 — soyasi yetarli emas",
            "type": "warning",
            "text": """
            Terassa bor,
            lekin kunning asosiy vaqtida
            to'liq quyosh ostida qoladi.
            """,
        },
        {
            "title": "Xato 3 — mebel circulationni to'sadi",
            "type": "warning",
            "text": """
            Stol va sofa
            asosiy chiqish yo'lini band qilgan.
            """,
        },
        {
            "title": "Xato 4 — fasaddan uzilgan",
            "type": "warning",
            "text": """
            Ayvon materiali va proporsiyasi
            uy arxitekturasi bilan
            umuman bog'lanmagan.
            """,
        },
        {
            "title": "Xato 5 — funksiyasi noma'lum",
            "type": "warning",
            "text": """
            Katta terassa chizilgan,

            <br><br>

            lekin u yerda
            odamlar nima qilishi
            rejalashtirilmagan.
            """,
        },
        {
            "title": "Professional checklist",
            "type": "example",
            "text": """
            Ayvonni tekshiring:

            <br><br>

            <b>1.</b> Qaysi xonaga ulangan?<br><br>
            <b>2.</b> Kim foydalanadi?<br><br>
            <b>3.</b> Qachon foydalaniladi?<br><br>
            <b>4.</b> Soya yetarlimi?<br><br>
            <b>5.</b> Mebel sig'adimi?<br><br>
            <b>6.</b> Yurish yo'li ochiqmi?<br><br>
            <b>7.</b> Fasad bilan uyg'unmi?
            """,
        },
        {
            "title": "Mini-case",
            "type": "example",
            "text": """
            Talab:

            <br><br>

            • 1 qavatli uy;<br>
            • living hovliga qarasin;<br>
            • 8 kishilik outdoor dining;<br>
            • dam olish zonasi;<br>
            • yaxshi soya;<br>
            • mangal bilan aloqa.

            <br><br>

            Living + terassa + hovli
            sxemasini yarating.
            """,
        },
        {
            "title": "Modul yakuni",
            "type": "highlight",
            "text": """
            Siz endi:

            <br><br>

            ✓ ayvon va terassa vazifasini tushunish;<br>
            ✓ ichki-tashqi makonni bog'lash;<br>
            ✓ quyosh va soyani hisobga olish;<br>
            ✓ tashqi mebel ergonomikasi;<br>
            ✓ circulationni tekshirish;<br>
            ✓ ayvon xatolarini topish

            <br><br>

            ko'nikmalariga ega bo'ldingiz.

            <br><br>

            Keyingi modul:
            <b>Yozgi oshxona.</b>
            """,
        },
    ],
}


# ============================================================
# QUIZ
# ============================================================

LEVEL04_MODULE04_QUIZ = {
    "L04_M04_001": [
        {
            "code": "L04_Q046",
            "question": "Ayvon faqat dekorativ elementmi?",
            "explanation": (
                "U dam olish, ovqatlanish, soyalanish va ichki-tashqi o'tish vazifalarini bajarishi mumkin."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L04_Q047",
            "question": "Ayvon uy va hovli orasidagi oraliq makon bo'lishi mumkinmi?",
            "explanation": (
                "Ayvon ichki va tashqi yashash makonlari o'rtasida bog'lovchi rol bajaradi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L04_Q048",
            "question": "Ayvonni loyiha oxirida tasodifiy qo'shish har doim to'g'rimi?",
            "explanation": (
                "Uni uy va hovli tizimi bilan birga rejalashtirish foydali."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
    ],

    "L04_M04_002": [
        {
            "code": "L04_Q049",
            "question": "Livingdan terassaga bevosita chiqish foydali bo'lishi mumkinmi?",
            "explanation": (
                "Bu ichki va tashqi family makonlarining aloqasini yaxshilaydi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L04_Q050",
            "question": "Kitchen va tashqi dining aloqasi kundalik foydalanishga ta'sir qiladimi?",
            "explanation": (
                "Ovqat va idishlarni tashish masofasi kamayishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L04_Q051",
            "question": "Ichki va tashqi pol orasidagi balandlik farqi circulationga ta'sir qiladimi?",
            "explanation": (
                "Keraksiz katta pog'ona yurishni noqulaylashtirishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L04_M04_003": [
        {
            "code": "L04_Q052",
            "question": "Ayvon chuqurligi soyalanishga ta'sir qiladimi?",
            "explanation": (
                "Ayvonning geometriyasi quyoshdan himoyalanish sifatiga ta'sir qiladi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L04_Q053",
            "question": "Bir xil ayvon barcha orientatsiyalarda bir xil ishlaydimi?",
            "explanation": (
                "Quyosh yo'nalishi va burchagi turli fasadlarda farq qiladi."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L04_Q054",
            "question": "Pergola va vertikal lamellar soyalanishga yordam berishi mumkinmi?",
            "explanation": (
                "Ular quyoshni boshqarish vositasi sifatida ishlatilishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L04_M04_004": [
        {
            "code": "L04_Q055",
            "question": "Terassada faqat mebel sig'ishi yetarlimi?",
            "explanation": (
                "Mebel bilan birga yurish va foydalanish zonalari ham kerak."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L04_Q056",
            "question": "Stul orqasida yurish joyi dining ergonomikasiga kiradimi?",
            "explanation": (
                "Stuldan foydalanish va uning orqasidan o'tish uchun joy talab qilinadi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L04_Q057",
            "question": "Mebel asosiy hovliga chiqish yo'lini to'sishi xatomi?",
            "explanation": (
                "Asosiy circulation ochiq va qulay bo'lishi kerak."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L04_M04_005": [
        {
            "code": "L04_Q058",
            "question": "Terassaga faqat service koridor orqali chiqish zaif yechim bo'lishi mumkinmi?",
            "explanation": (
                "Asosiy tashqi makon living yoki dining bilan qulay bog'langan bo'lishi foydali."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L04_Q059",
            "question": "Terassaning funksiyasi oldindan aniqlanishi kerakmi?",
            "explanation": (
                "Unda kim va qanday foydalanishi rejalash qarorlarini belgilaydi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L04_Q060",
            "question": "Ayvon auditidagi muhim savollardan biri qaysi?",
            "explanation": (
                "Ayvon qaysi xonaga ulanganligi va qanday ishlatilishi muhim."
            ),
            "options": [
                ("A", "Qaysi xonaga ulangan va kim foydalanadi?", True),
                ("B", "Faqat shift rangi qanday?", False),
            ],
        },
    ],
}


# ============================================================
# DATABASE SEED
# ============================================================

def seed_level04_module04():
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
        ) in LEVEL04_MODULE04_LESSONS:

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
