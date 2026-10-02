from database.database import get_connection


# ============================================================
# LEVEL 3
# MODULE 02 - SHIMOL VA QUYOSH
# ============================================================

LEVEL03_MODULE02_LESSONS = [
    (
        "L03_M02",
        "L03_M02_001",
        "Shimolni aniqlash va orientatsiya",
        "theory",
        "Uchastkaning shimol yo'nalishini aniqlash va loyihada to'g'ri ishlatish.",
        1,
        35,
        20,
    ),
    (
        "L03_M02",
        "L03_M02_002",
        "Quyosh kun davomida qanday harakat qiladi?",
        "theory",
        "Ertalab, kunduz va kechki quyoshning uchastka va xonalarga ta'sirini tushunish.",
        2,
        40,
        20,
    ),
    (
        "L03_M02",
        "L03_M02_003",
        "Xonalarni orientatsiya qilish",
        "theory",
        "Yotoqxona, living, oshxona va boshqa xonalarni quyoshga nisbatan tahlil qilish.",
        3,
        40,
        20,
    ),
    (
        "L03_M02",
        "L03_M02_004",
        "Issiq tomonlar va soya",
        "practice",
        "Quyosh issiqligi, tashqi soyalar va fasad ochilishlarini boshlang'ich darajada tahlil qilish.",
        4,
        45,
        20,
    ),
    (
        "L03_M02",
        "L03_M02_005",
        "Quyosh diagrammasi va site audit",
        "practice",
        "Uchastkada quyosh yo'nalishini oddiy diagramma orqali ko'rsatish va loyiha qaroriga aylantirish.",
        5,
        50,
        25,
    ),
]


# ============================================================
# CONTENT
# ============================================================

LEVEL03_MODULE02_CONTENT = {
    "L03_M02_001": [
        {
            "title": "Shimol — genplandagi asosiy belgilardan biri",
            "type": "highlight",
            "text": """
            Uchastkani professional o'qishda
            birinchi savollardan biri:

            <br><br>

            <b>Shimol qayerda?</b>

            <br><br>

            Chunki orientatsiya
            quyosh, soya, hovli va
            xona joylashuviga ta'sir qiladi.
            """,
        },
        {
            "title": "Orientatsiya nima?",
            "type": "normal",
            "text": """
            Orientatsiya — bino va uning
            xonalarining asosiy yo'nalishlarga
            nisbatan joylashuvi.

            <br><br>

            Masalan:

            <br><br>

            • shimol;<br>
            • janub;<br>
            • sharq;<br>
            • g'arb.
            """,
        },
        {
            "title": "Nega bu muhim?",
            "type": "example",
            "text": """
            Tasavvur qiling:

            <br><br>

            ikkita bir xil uy bor.

            <br><br>

            Birinchisida living ertalab va kunduz
            ko'proq tabiiy yorug'lik oladi.

            <br><br>

            Ikkinchisida esa asosiy oynalar
            noqulay yo'nalishga qaragan.

            <br><br>

            Plan bir xil,
            yashash sifati esa farq qilishi mumkin.
            """,
        },
        {
            "title": "Shimol strelkasi",
            "type": "normal",
            "text": """
            Genplan va site analysis diagrammalarida
            odatda shimol yo'nalishi
            alohida belgi bilan ko'rsatiladi.

            <br><br>

            Bu boshqa barcha yo'nalishlarni
            tushunishga yordam beradi.
            """,
        },
        {
            "title": "Boshlovchi xatosi",
            "type": "warning",
            "text": """
            Uchastkani qog'ozda qulay ko'ringani uchun
            aylantirib chizib,

            <br><br>

            haqiqiy shimolni unutish mumkin.

            <br><br>

            Bu keyinchalik orientatsiya tahlilini
            noto'g'ri qiladi.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Bir uchastka planini tanlang.

            <br><br>

            Unda:

            <br><br>

            • shimol;<br>
            • janub;<br>
            • sharq;<br>
            • g'arb

            <br><br>

            yo'nalishlarini belgilang.
            """,
        },
    ],

    "L03_M02_002": [
        {
            "title": "Quyosh bir joyda turmaydi",
            "type": "highlight",
            "text": """
            Binoni faqat bitta vaqtdagi
            quyosh bo'yicha baholab bo'lmaydi.

            <br><br>

            Quyosh kun davomida
            osmondagi holatini o'zgartiradi.
            """,
        },
        {
            "title": "Ertalabki quyosh",
            "type": "normal",
            "text": """
            Ertalab quyosh
            sharq tomondan keladi.

            <br><br>

            Shu sababli sharqqa qaragan ochilishlar
            ertalabki yorug'likni ko'proq qabul qilishi mumkin.
            """,
        },
        {
            "title": "Kechki quyosh",
            "type": "normal",
            "text": """
            Kechga yaqin quyosh
            g'arb tomonda bo'ladi.

            <br><br>

            G'arb tomondagi fasadlar
            kechki kuchli quyoshni qabul qilishi mumkin.
            """,
        },
        {
            "title": "Kun davomida farq",
            "type": "example",
            "text": """
            Bir xona ertalab salqin va yorug' bo'lishi mumkin.

            <br><br>

            Xuddi shu xona boshqa orientatsiyada
            kechga yaqin ko'proq qizishi mumkin.

            <br><br>

            Shuning uchun faqat
            “deraza katta” degan qaror yetmaydi.
            """,
        },
        {
            "title": "Mavsum ham muhim",
            "type": "normal",
            "text": """
            Quyoshning balandligi va yo'li
            yil davomida bir xil bo'lmaydi.

            <br><br>

            Bu mavzu keyingi professional bosqichlarda
            yanada chuqurroq o'rganiladi.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            O'zingiz yashaydigan uyni kuzating.

            <br><br>

            Qaysi xona:

            <br><br>

            • ertalab yorug'?<br>
            • tushda yorug'?<br>
            • kechga yaqin ko'proq quyosh oladi?

            <br><br>

            Uchta kuzatuv yozing.
            """,
        },
    ],

    "L03_M02_003": [
        {
            "title": "Har bir xona bir xil orientatsiyani talab qilmaydi",
            "type": "highlight",
            "text": """
            Xonalarni quyoshga nisbatan
            joylashtirishda ularning
            qanday ishlatilishi muhim.
            """,
        },
        {
            "title": "Yotoqxona",
            "type": "normal",
            "text": """
            Yotoqxona uchun:

            <br><br>

            • ertalabki yorug'lik;<br>
            • kechki issiqlik;<br>
            • maxfiylik;<br>
            • tashqi shovqin

            <br><br>

            birgalikda ko'rib chiqiladi.
            """,
        },
        {
            "title": "Living",
            "type": "normal",
            "text": """
            Living room uchun
            faqat quyosh emas,

            <br><br>

            • hovli bilan aloqa;<br>
            • manzara;<br>
            • tashqi terassa;<br>
            • oilaning foydalanish vaqti

            <br><br>

            ham muhim.
            """,
        },
        {
            "title": "Oshxona",
            "type": "normal",
            "text": """
            Oshxonaning orientatsiyasi
            uning:

            <br><br>

            • kunduzgi foydalanishi;<br>
            • deraza joyi;<br>
            • dining bilan aloqasi;<br>
            • hovliga chiqishi

            <br><br>

            bilan birga ko'rib chiqiladi.
            """,
        },
        {
            "title": "Bitta formula yo'q",
            "type": "warning",
            "text": """
            “Barcha yotoqxona faqat shu tomonga qarashi kerak”
            degan universal formulaga yopishib olish noto'g'ri.

            <br><br>

            Real uchastka,
            iqlim,
            qo'shnilar,
            ko'cha va oila hayoti
            birga tahlil qilinadi.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            4 xonani oling:

            <br><br>

            • living;<br>
            • oshxona;<br>
            • master bedroom;<br>
            • bolalar xonasi.

            <br><br>

            Har biri uchun:
            “Qachon quyosh kerak?”
            degan savolga javob yozing.
            """,
        },
    ],

    "L03_M02_004": [
        {
            "title": "Quyosh faqat yorug'lik emas",
            "type": "highlight",
            "text": """
            Quyosh xonaga:

            <br><br>

            • yorug'lik;<br>
            • issiqlik;<br>
            • soya;<br>
            • vizual qulaylik

            <br><br>

            orqali ta'sir qiladi.
            """,
        },
        {
            "title": "G'arb tomoni",
            "type": "example",
            "text": """
            Kechki paytda g'arb tomondagi
            katta oynalar ko'p quyosh olishi mumkin.

            <br><br>

            Bu ayrim holatlarda
            xona qizishini kuchaytirishi mumkin.
            """,
        },
        {
            "title": "Soya vositalari",
            "type": "normal",
            "text": """
            Quyoshni boshqarishda:

            <br><br>

            • ayvon;<br>
            • soyabon;<br>
            • pergola;<br>
            • chuqur deraza;<br>
            • daraxt;<br>
            • fasad elementlari

            <br><br>

            yordam berishi mumkin.
            """,
        },
        {
            "title": "Daraxt ham arxitektura vositasi",
            "type": "example",
            "text": """
            Mavjud daraxt
            faqat landshaft elementi emas.

            <br><br>

            U:

            <br><br>

            • soya;<br>
            • privacy;<br>
            • shamol filtri;<br>
            • hovli markazi

            <br><br>

            vazifasini bajarishi mumkin.
            """,
        },
        {
            "title": "Boshlovchi xatosi",
            "type": "warning",
            "text": """
            Fasadni chiroyli qilish uchun
            juda katta shisha ochilishlar qo'yilib,

            <br><br>

            quyosh va qizish masalasi
            umuman tekshirilmasa,

            <br><br>

            loyiha real hayotda noqulay bo'lishi mumkin.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Bitta fasad tanlang.

            <br><br>

            Unda:

            <br><br>

            • quyosh ko'p tushadigan qism;<br>
            • mavjud soya;<br>
            • qo'shimcha soya kerak bo'lishi mumkin bo'lgan qism

            <br><br>

            ni belgilang.
            """,
        },
    ],

    "L03_M02_005": [
        {
            "title": "Quyosh diagrammasi",
            "type": "highlight",
            "text": """
            Site Analysis varag'ida
            quyosh yo'nalishini oddiy grafik
            bilan ko'rsatish mumkin.

            <br><br>

            Maqsad ilmiy murakkab diagramma emas.

            <br><br>

            Maqsad — loyiha qarorini tushunarli qilish.
            """,
        },
        {
            "title": "1. Shimolni belgilang",
            "type": "example",
            "text": """
            Uchastka konturiga
            shimol strelkasini qo'ying.

            <br><br>

            Shundan keyin qolgan yo'nalishlar
            aniq bo'ladi.
            """,
        },
        {
            "title": "2. Ertalabki yo'nalish",
            "type": "example",
            "text": """
            Sharq tomonni belgilang.

            <br><br>

            Ertalabki quyosh qaysi xonalar
            va hovli qismlariga tushishini
            xayolan tekshiring.
            """,
        },
        {
            "title": "3. Kechki yo'nalish",
            "type": "example",
            "text": """
            G'arb tomonni belgilang.

            <br><br>

            Kechki quyoshning
            qaysi fasad va ochiq zonalarga
            kuchliroq ta'sir qilishini ko'ring.
            """,
        },
        {
            "title": "4. Qarorga aylantiring",
            "type": "highlight",
            "text": """
            Tahlil faqat diagramma bilan tugamaydi.

            <br><br>

            Masalan:

            <br><br>

            “G'arb tomonda katta shisha ochilish bo'lsa,
            qo'shimcha soya yechimi kerak bo'lishi mumkin.”

            <br><br>

            Mana shu — tahlildan loyiha qaroriga o'tish.
            """,
        },
        {
            "title": "Mini-loyiha",
            "type": "example",
            "text": """
            Oldingi modulda tanlagan uchastkangizni oling.

            <br><br>

            Bitta varaqda:

            <br><br>

            • shimol strelkasi;<br>
            • sharq;<br>
            • g'arb;<br>
            • ertalabki quyosh;<br>
            • kechki quyosh;<br>
            • yaxshi yorug'lik olish mumkin bo'lgan zona;<br>
            • soya talab qilishi mumkin bo'lgan zona

            <br><br>

            ni belgilang.
            """,
        },
        {
            "title": "Modul yakuni",
            "type": "highlight",
            "text": """
            Siz endi:

            <br><br>

            ✓ shimolni aniqlash;<br>
            ✓ orientatsiyani tushunish;<br>
            ✓ ertalab va kechki quyoshni farqlash;<br>
            ✓ xonalarni quyoshga nisbatan tahlil qilish;<br>
            ✓ soya ehtiyojini ko'rish;<br>
            ✓ oddiy sun diagram tayyorlash

            <br><br>

            bo'yicha boshlang'ich professional
            fikrlashga ega bo'ldingiz.

            <br><br>

            Keyingi modul:
            <b>Ko'cha va kirish.</b>
            """,
        },
    ],
}


# ============================================================
# QUIZ
# ============================================================

LEVEL03_MODULE02_QUIZ = {
    "L03_M02_001": [
        {
            "code": "L03_Q016",
            "question": "Genplanda shimol yo'nalishini bilish muhimmi?",
            "explanation": (
                "Orientatsiya quyosh, soya va bino joylashuvi tahliliga ta'sir qiladi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L03_Q017",
            "question": "Orientatsiya nimani bildiradi?",
            "explanation": (
                "Bino va xonalarning asosiy geografik yo'nalishlarga nisbatan joylashuvini."
            ),
            "options": [
                ("A", "Yo'nalishlarga nisbatan joylashuvni", True),
                ("B", "Faqat xona rangini", False),
            ],
        },
        {
            "code": "L03_Q018",
            "question": "Uchastka chizmasini aylantirganda haqiqiy shimolni unutish mumkinmi?",
            "explanation": (
                "Shuning uchun shimol belgisi aniq saqlanishi kerak."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L03_M02_002": [
        {
            "code": "L03_Q019",
            "question": "Ertalab quyosh asosan qaysi tomondan keladi?",
            "explanation": (
                "Quyosh sharq tomondan chiqadi."
            ),
            "options": [
                ("A", "Sharq", True),
                ("B", "G'arb", False),
            ],
        },
        {
            "code": "L03_Q020",
            "question": "Kechki quyosh asosan qaysi tomonga bog'liq?",
            "explanation": (
                "Kechga yaqin quyosh g'arb tomonda bo'ladi."
            ),
            "options": [
                ("A", "G'arb", True),
                ("B", "Sharq", False),
            ],
        },
        {
            "code": "L03_Q021",
            "question": "Quyoshning holati kun davomida o'zgaradimi?",
            "explanation": (
                "Shu sababli xonaning yorug'lik va issiqlik sharoiti vaqt bo'yicha o'zgaradi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L03_M02_003": [
        {
            "code": "L03_Q022",
            "question": "Barcha xonalarni bir xil orientatsiya qilish shartmi?",
            "explanation": (
                "Har bir xona funksiyasi va foydalanish vaqti turlicha."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L03_Q023",
            "question": "Living orientatsiyasida hovli bilan aloqa ham muhimmi?",
            "explanation": (
                "Living uchun quyosh bilan birga manzara va hovli aloqasi ham muhim."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L03_Q024",
            "question": "Xona orientatsiyasida oilaning foydalanish vaqti hisobga olinadimi?",
            "explanation": (
                "Xona qachon ko'p ishlatilishi orientatsiya qaroriga ta'sir qilishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L03_M02_004": [
        {
            "code": "L03_Q025",
            "question": "Quyosh faqat yorug'lik beradimi?",
            "explanation": (
                "U issiqlik, soya va vizual qulaylikka ham ta'sir qiladi."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L03_Q026",
            "question": "Ayvon va pergola quyoshni boshqarishda yordam berishi mumkinmi?",
            "explanation": (
                "Bunday elementlar tashqi soya yaratishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L03_Q027",
            "question": "Mavjud daraxt ham soya vositasi bo'lishi mumkinmi?",
            "explanation": (
                "Daraxtlar soya va privacy yaratishda foydali bo'lishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L03_M02_005": [
        {
            "code": "L03_Q028",
            "question": "Quyosh diagrammasida shimolni ko'rsatish kerakmi?",
            "explanation": (
                "Shimol boshqa yo'nalishlarni to'g'ri tushunish uchun asos bo'ladi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L03_Q029",
            "question": "Site Analysis faqat diagramma chizish bilan tugaydimi?",
            "explanation": (
                "Tahlil loyiha qaroriga aylanishi kerak."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L03_Q030",
            "question": "Quyosh tahlilining asosiy maqsadi nima?",
            "explanation": (
                "Yorug'lik, issiqlik va soya sharoitini tushunib, yaxshiroq loyiha qarori qabul qilish."
            ),
            "options": [
                ("A", "Loyiha qarorini yaxshilash", True),
                ("B", "Faqat chizmaga belgi qo'shish", False),
            ],
        },
    ],
}


# ============================================================
# DATABASE SEED
# ============================================================

def seed_level03_module02():
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
        ) in LEVEL03_MODULE02_LESSONS:

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
