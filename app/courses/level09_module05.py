from database.database import get_connection


LEVEL09_MODULE05_LESSONS = [
    (
        "L09_M05",
        "L09_M05_001",
        "Yong'in xavfsizligi fikrlashi",
        "theory",
        "Arxitektor uchun yong'in xavfsizligini tizimli ravishda tushunish.",
        1,
        40,
        20,
    ),
    (
        "L09_M05",
        "L09_M05_002",
        "Odamlar, yo'llar va chiqishlar",
        "theory",
        "Odamlarning xavfsiz chiqishi va harakat yo'llarining umumiy mantig'ini tushunish.",
        2,
        45,
        20,
    ),
    (
        "L09_M05",
        "L09_M05_003",
        "Konstruksiya va materiallar bilan aloqa",
        "practice",
        "Yong'in xavfsizligi qarorlarining devor, eshik, konstruksiya va materiallar bilan aloqasini tushunish.",
        3,
        50,
        20,
    ),
    (
        "L09_M05",
        "L09_M05_004",
        "Uchastka va tashqi kirish",
        "practice",
        "Tashqi kirish, xizmat ko'rsatish va qo'shni obyektlar bilan yong'in xavfsizligi aloqalarini tahlil qilish.",
        4,
        50,
        20,
    ),
    (
        "L09_M05",
        "L09_M05_005",
        "Yong'in xavfsizligi professional audit",
        "practice",
        "Arxitektura loyihasini yong'in xavfsizligi nuqtai nazaridan kompleks tekshirish.",
        5,
        55,
        25,
    ),
]


LEVEL09_MODULE05_CONTENT = {
    "L09_M05_001": [
        {
            "title": "Yong'in xavfsizligi tizim",
            "type": "highlight",
            "text": """
            Yong'in xavfsizligi
            faqat bitta

            <br><br>

            eshik,
            devor
            yoki materialdan
            iborat emas.
            """,
        },
        {
            "title": "Birgalikda ishlaydigan qismlar",
            "type": "normal",
            "text": """
            • odamlar;<br>
            • chiqish yo'llari;<br>
            • bo'linishlar;<br>
            • konstruksiya;<br>
            • materiallar;<br>
            • tashqi kirish.
            """,
        },
        {
            "title": "Aniq qiymatlar",
            "type": "warning",
            "text": """
            Aniq yong'inga
            chidamlilik qiymati

            <br><br>

            yoki masofalarni
            amaldagi normativsiz
            kiritmang.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Bir uy uchun
            yong'in xavfsizligi
            bo'yicha

            <br><br>

            10 ta audit
            savolini yozing.
            """,
        },
    ],

    "L09_M05_002": [
        {
            "title": "Xavfsiz chiqish",
            "type": "highlight",
            "text": """
            Favqulodda holatda
            foydalanuvchi

            <br><br>

            xavfli zonadan
            xavfsiz yo'nalishda
            chiqishi kerak.
            """,
        },
        {
            "title": "Yo'l",
            "type": "normal",
            "text": """
            Yo'l:

            • tushunarli;<br>
            • uzluksiz;<br>
            • to'siqsiz

            <br><br>

            bo'lishi kerak.
            """,
        },
        {
            "title": "Kundalik yo'l bilan bir xil emas",
            "type": "warning",
            "text": """
            Kundalik circulation
            ishlayotgani

            <br><br>

            favqulodda holatda
            ham hamma narsa
            xavfsiz

            <br><br>

            degani emas.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Bir xonadan
            tashqarigacha

            <br><br>

            odamning chiqish
            yo'lini bosqichma-bosqich
            yozing.
            """,
        },
    ],

    "L09_M05_003": [
        {
            "title": "Material va konstruksiya",
            "type": "highlight",
            "text": """
            Yong'in xavfsizligi
            material,

            <br><br>

            devor,
            eshik,
            shaft
            va konstruktiv

            <br><br>

            elementlar bilan
            bog'liq.
            """,
        },
        {
            "title": "Taxmin qilmang",
            "type": "warning",
            "text": """
            Material nomiga
            qarab

            <br><br>

            uning yong'in
            xususiyatlarini

            <br><br>

            taxmin qilmang.
            """,
        },
        {
            "title": "Hujjat bilan ishlash",
            "type": "normal",
            "text": """
            Elementning
            kerakli xususiyati

            <br><br>

            tegishli normativ,
            sertifikat
            yoki texnik

            <br><br>

            ma'lumot bilan
            tekshiriladi.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Devor,
            eshik
            va qoplama uchun

            <br><br>

            tekshiriladigan
            xususiyatlar
            ro'yxatini yozing.
            """,
        },
    ],

    "L09_M05_004": [
        {
            "title": "Genplan ham muhim",
            "type": "highlight",
            "text": """
            Yong'in xavfsizligi
            faqat bino
            ichida tugamaydi.
            """,
        },
        {
            "title": "Tashqi kirish",
            "type": "normal",
            "text": """
            Uchastkadagi:

            • kirish;<br>
            • yo'llar;<br>
            • darvoza;<br>
            • bino atrofi

            <br><br>

            ham tekshirilishi
            mumkin.
            """,
        },
        {
            "title": "Landshaft bilan konflikt",
            "type": "warning",
            "text": """
            Landshaft,
            dekorativ element
            yoki parkovka

            <br><br>

            zarur tashqi
            harakat yo'lini

            <br><br>

            to'sib qo'ymasligi
            kerak.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Genplanda
            favqulodda kirish

            <br><br>

            nuqtai nazaridan
            6 ta savol
            yozing.
            """,
        },
    ],

    "L09_M05_005": [
        {
            "title": "Yong'in audit",
            "type": "highlight",
            "text": """
            Obyekt
            → Odamlar
            → Chiqish yo'li
            → Bo'linish
            → Konstruksiya/material
            → Tashqi kirish
            → Normativ dalil
            """,
        },
        {
            "title": "Issue-list",
            "type": "example",
            "text": """
            Joy<br>
            Xavf<br>
            Manba<br>
            Band<br>
            Status<br>
            Yechim
            """,
        },
        {
            "title": "Bir talab yetmaydi",
            "type": "warning",
            "text": """
            Bitta yong'in
            talabi bajarilgani

            <br><br>

            barcha masalalar
            hal bo'lganini
            anglatmaydi.
            """,
        },
        {
            "title": "Professional checklist",
            "type": "example",
            "text": """
            <b>1.</b> Obyekt turi aniqmi?<br><br>
            <b>2.</b> Foydalanuvchilar tushunarlimi?<br><br>
            <b>3.</b> Chiqish yo'li tekshirilganmi?<br><br>
            <b>4.</b> Eshik va bo'linishlar ko'rilganmi?<br><br>
            <b>5.</b> Material/konstruksiya tekshirilganmi?<br><br>
            <b>6.</b> Tashqi kirishlar ko'rilganmi?<br><br>
            <b>7.</b> Normativ dalil qayd qilinganmi?
            """,
        },
    ],
}


LEVEL09_MODULE05_QUIZ = {
    "L09_M05_001": [
        {"code": "L09_Q061", "question": "Yong'in xavfsizligi faqat bitta eshik bilan hal bo'ladimi?", "explanation": "Yong'in xavfsizligi ko'p elementli tizimdir.", "options": [("A", "Ha", False), ("B", "Yo'q", True)]},
        {"code": "L09_Q062", "question": "Yong'in xavfsizligida odamlarning harakat yo'li muhimmi?", "explanation": "Favqulodda holatda xavfsiz chiqish asosiy masalalardan biridir.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
        {"code": "L09_Q063", "question": "Aniq yong'in qiymatlarini normativsiz taxmin qilish to'g'rimi?", "explanation": "Aniq talablar amaldagi tegishli normativga tayanadi.", "options": [("A", "Ha", False), ("B", "Yo'q", True)]},
    ],
    "L09_M05_002": [
        {"code": "L09_Q064", "question": "Favqulodda chiqish yo'li uzluksiz bo'lishi kerakmi?", "explanation": "Yo'l xavfsiz chiqishga olib borishi kerak.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
        {"code": "L09_Q065", "question": "Kundalik circulation ishlasa favqulodda holat ham avtomatik xavfsizmi?", "explanation": "Favqulodda vaziyat alohida tekshiruv talab qiladi.", "options": [("A", "Ha", False), ("B", "Yo'q", True)]},
        {"code": "L09_Q066", "question": "Chiqish yo'lidagi to'siqlar xavf tug'dirishi mumkinmi?", "explanation": "To'siqlar odamlarning chiqishini qiyinlashtirishi mumkin.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
    ],
    "L09_M05_003": [
        {"code": "L09_Q067", "question": "Devor va eshiklar yong'in xavfsizligi bilan bog'liq bo'lishi mumkinmi?", "explanation": "Ularning xususiyatlari yong'in xavfsizligi tizimining bir qismi bo'lishi mumkin.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
        {"code": "L09_Q068", "question": "Materialning yong'in xususiyatini faqat nomidan bilish mumkinmi?", "explanation": "Texnik va normativ ma'lumot tekshirilishi kerak.", "options": [("A", "Ha", False), ("B", "Yo'q", True)]},
        {"code": "L09_Q069", "question": "Material xususiyatlarini hujjat bilan tekshirish foydalimi?", "explanation": "Bu qarorni dalil bilan asoslashga yordam beradi.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
    ],
    "L09_M05_004": [
        {"code": "L09_Q070", "question": "Yong'in xavfsizligi genplanga ham ta'sir qilishi mumkinmi?", "explanation": "Tashqi kirish va yo'llar ham muhim bo'lishi mumkin.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
        {"code": "L09_Q071", "question": "Landshaft elementi zarur kirish yo'lini to'sishi mumkinmi?", "explanation": "Tashqi harakat yo'llari ham koordinatsiya qilinadi.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
        {"code": "L09_Q072", "question": "Yong'in xavfsizligi faqat bino ichida tekshiriladimi?", "explanation": "Uchastka va tashqi aloqalar ham muhim bo'lishi mumkin.", "options": [("A", "Ha", False), ("B", "Yo'q", True)]},
    ],
    "L09_M05_005": [
        {"code": "L09_Q073", "question": "Yong'in auditida obyekt turi aniqlanadimi?", "explanation": "Talablar obyekt turiga bog'liq bo'lishi mumkin.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
        {"code": "L09_Q074", "question": "Bitta yong'in talabi bajarilsa butun loyiha avtomatik mosmi?", "explanation": "Ko'plab mustaqil tekshiruvlar mavjud bo'lishi mumkin.", "options": [("A", "Ha", False), ("B", "Yo'q", True)]},
        {"code": "L09_Q075", "question": "Yong'in xavfsizligi auditining to'g'ri workflow'i qaysi?", "explanation": "Obyekt, odamlar, chiqish, konstruksiya va tashqi kirishlar tegishli normativ bilan tekshiriladi.", "options": [("A", "Obyekt → odamlar → chiqish → konstruksiya/material → tashqi kirish → normativ audit", True), ("B", "Faqat eshik qo'yish → yakunlash", False)]},
    ],
}


def seed_level09_module05():
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
        ) in LEVEL09_MODULE05_LESSONS:

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
