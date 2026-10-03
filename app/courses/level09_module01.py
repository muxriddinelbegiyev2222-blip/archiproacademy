from database.database import get_connection


LEVEL09_MODULE01_LESSONS = [
    (
        "L09_M01",
        "L09_M01_001",
        "Normativ hujjatni to'g'ri o'qish",
        "theory",
        "Normativ hujjatning tuzilishi, qo'llanish doirasi va talab turini to'g'ri tushunish.",
        1,
        40,
        20,
    ),
    (
        "L09_M01",
        "L09_M01_002",
        "Qo'llanish doirasi va obyekt turi",
        "theory",
        "Talab aynan qaysi bino, uchastka yoki loyiha holatiga tegishli ekanini aniqlash.",
        2,
        45,
        20,
    ),
    (
        "L09_M01",
        "L09_M01_003",
        "Tahrir, sana va hujjat holati",
        "practice",
        "Normativning amaldagi tahriri, sanasi va o'zgarishlarini tekshirish odatini shakllantirish.",
        3,
        50,
        20,
    ),
    (
        "L09_M01",
        "L09_M01_004",
        "Band, havola va dalil bilan ishlash",
        "practice",
        "Loyiha qarorini aniq band va hujjatga tayangan holda asoslash.",
        4,
        50,
        20,
    ),
    (
        "L09_M01",
        "L09_M01_005",
        "Normativ savodxonlik professional audit",
        "practice",
        "Normativdan foydalanishdagi asosiy xatolarni aniqlash va tekshiruv workflow'ini qo'llash.",
        5,
        55,
        25,
    ),
]


LEVEL09_MODULE01_CONTENT = {
    "L09_M01_001": [
        {
            "title": "Normativ matnni o'qish mantig'i",
            "type": "highlight",
            "text": """
            Normativ hujjatni
            faqat bitta jumla
            yoki jadval sifatida
            o'qimang.

            <br><br>

            Avval:

            • hujjat nomi;<br>
            • maqsadi;<br>
            • qo'llanish doirasi;<br>
            • atamalar;<br>
            • tegishli bo'limlar

            <br><br>

            tushuniladi.
            """,
        },
        {
            "title": "Kontekst",
            "type": "normal",
            "text": """
            Bitta band
            boshqa bandlar
            bilan bog'liq
            bo'lishi mumkin.

            <br><br>

            Shu sabab
            normativni
            kontekstdan uzib
            o'qish xavfli.
            """,
        },
        {
            "title": "Ehtiyot bo'ling",
            "type": "warning",
            "text": """
            Internetdagi
            bitta rasm,
            skrinshot
            yoki qisqa izoh

            <br><br>

            to'liq normativ
            manba o'rnini
            bosmaydi.
            """,
        },
        {
            "title": "Tasavvur qiling",
            "type": "example",
            "text": """
            Sizga:

            “Bu xonani
            shunday qilish
            mumkinmi?”

            <br><br>

            degan savol berildi.

            <br><br>

            Javobdan oldin
            obyekt turi,
            talab turi
            va tegishli hujjat
            aniqlanadi.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Bitta loyiha
            savolini tanlang.

            <br><br>

            Yozing:

            • qaysi hujjat kerak;<br>
            • qaysi bo'lim;<br>
            • qaysi band;<br>
            • qanday loyiha qaroriga ta'sir qiladi.
            """,
        },
    ],

    "L09_M01_002": [
        {
            "title": "Talab kimga tegishli?",
            "type": "highlight",
            "text": """
            Bir xil normativ
            talab barcha
            obyektlarga

            <br><br>

            avtomatik ravishda
            tatbiq etilmasligi
            mumkin.
            """,
        },
        {
            "title": "Tekshiriladigan omillar",
            "type": "normal",
            "text": """
            Masalan:

            • bino funksiyasi;<br>
            • qavatlar soni;<br>
            • obyekt turi;<br>
            • joylashuv;<br>
            • loyiha bosqichi

            <br><br>

            talab qo'llanishiga
            ta'sir qilishi mumkin.
            """,
        },
        {
            "title": "Eng katta xato",
            "type": "warning",
            "text": """
            Boshqa obyektga
            tegishli talabni

            <br><br>

            o'z loyihangizga
            tekshirmasdan
            ko'chirmang.
            """,
        },
        {
            "title": "Professional savol",
            "type": "example",
            "text": """
            “Bu talab
            mavjudmi?”

            <br><br>

            degan savoldan ko'ra:

            <br><br>

            “Bu talab
            aynan shu obyektga
            tatbiq etiladimi?”

            <br><br>

            degan savol
            kuchliroq.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            3 ta turli
            obyekt misolini yozing.

            <br><br>

            Har biri uchun
            bir xil talab
            tatbiq etiladimi

            <br><br>

            deb tekshirish uchun
            savollar tuzing.
            """,
        },
    ],

    "L09_M01_003": [
        {
            "title": "Amaldagi tahrir",
            "type": "highlight",
            "text": """
            Normativ bilan
            ishlaganda

            <br><br>

            hujjatning
            faqat nomini emas,

            <br><br>

            amaldagi holatini
            ham tekshiring.
            """,
        },
        {
            "title": "Nimalar tekshiriladi?",
            "type": "normal",
            "text": """
            • hujjat nomi;<br>
            • tahrir sanasi;<br>
            • o'zgarishlar;<br>
            • rasmiy manba;<br>
            • tekshirilgan sana.
            """,
        },
        {
            "title": "Eski PDF xavfi",
            "type": "warning",
            "text": """
            Kompyuterda
            saqlangan eski PDF

            <br><br>

            hozir ham
            amaldagi hujjat
            ekanini anglatmaydi.
            """,
        },
        {
            "title": "Normativ karta",
            "type": "example",
            "text": """
            Har bir muhim
            hujjat uchun:

            <br><br>

            Hujjat nomi<br>
            Tahrir<br>
            Manba<br>
            Sana<br>
            Tegishli band

            <br><br>

            formatida
            qayd yuriting.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            O'zingiz uchun
            “Normativ tekshiruv kartasi”
            shaklini tuzing.
            """,
        },
    ],

    "L09_M01_004": [
        {
            "title": "Dalil bilan gapirish",
            "type": "highlight",
            "text": """
            Professional javob:

            <br><br>

            “Shunday bo'lishi kerak”

            <br><br>

            degan gap bilan
            tugamasligi kerak.
            """,
        },
        {
            "title": "To'g'ri zanjir",
            "type": "normal",
            "text": """
            Talab
            → Manba
            → Band
            → Qo'llanish sharti
            → Loyiha yechimi
            """,
        },
        {
            "title": "Xotiradan raqam aytmang",
            "type": "warning",
            "text": """
            Aniq normativ
            qiymatlarni

            <br><br>

            bandni ko'rmasdan
            xotiradan aytish

            <br><br>

            xato xavfini
            oshiradi.
            """,
        },
        {
            "title": "Audit izi",
            "type": "normal",
            "text": """
            Keyinchalik
            boshqa mutaxassis

            <br><br>

            sizning qaroringiz
            nimaga asoslanganini
            tushuna olishi kerak.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Bitta loyiha
            qarorini:

            <br><br>

            talab
            → manba
            → band
            → loyiha yechimi

            <br><br>

            formatida yozing.
            """,
        },
    ],

    "L09_M01_005": [
        {
            "title": "Normativ audit workflow",
            "type": "highlight",
            "text": """
            Loyiha savoli
            → Obyekt tasnifi
            → Tegishli hujjat
            → Amaldagi tahrir
            → Band
            → Loyiha bilan solishtirish
            → Qayd
            """,
        },
        {
            "title": "Audit savollari",
            "type": "normal",
            "text": """
            • Qaysi talab tekshirilmoqda?<br>
            • Qaysi hujjat asos?<br>
            • Hujjat amaldami?<br>
            • Shu obyektga tegishlimi?<br>
            • Loyiha holati qanday?
            """,
        },
        {
            "title": "Bitta band yetmaydi",
            "type": "warning",
            "text": """
            Bitta talabga
            javob topish

            <br><br>

            butun loyiha
            normativga mos

            <br><br>

            degani emas.
            """,
        },
        {
            "title": "Status tizimi",
            "type": "example",
            "text": """
            Har bir masala uchun:

            <br><br>

            • OPEN<br>
            • TEKSHIRILDI<br>
            • MOS<br>
            • QAYTA ISHLASH KERAK

            <br><br>

            kabi status
            ishlatish mumkin.
            """,
        },
        {
            "title": "Professional checklist",
            "type": "example",
            "text": """
            <b>1.</b> Savol aniqmi?<br><br>
            <b>2.</b> Obyekt turi aniqmi?<br><br>
            <b>3.</b> Rasmiy manba topildimi?<br><br>
            <b>4.</b> Amaldagi tahrir tekshirildimi?<br><br>
            <b>5.</b> Qo'llanish doirasi mosmi?<br><br>
            <b>6.</b> Aniq band topildimi?<br><br>
            <b>7.</b> Loyiha bilan solishtirildimi?<br><br>
            <b>8.</b> Xulosa qayd qilindimi?
            """,
        },
    ],
}


LEVEL09_MODULE01_QUIZ = {
    "L09_M01_001": [
        {
            "code": "L09_Q001",
            "question": "Normativ bandni kontekstdan uzib o'qish to'g'rimi?",
            "explanation": "Normativ bandlar boshqa bo'limlar, atamalar va qo'llanish doirasi bilan bog'liq bo'lishi mumkin.",
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L09_Q002",
            "question": "Normativ hujjatning qo'llanish doirasini o'qish kerakmi?",
            "explanation": "Talab aynan qaysi obyekt yoki holatga tegishli ekanini shu orqali tushunamiz.",
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L09_Q003",
            "question": "Internetdagi bitta skrinshot to'liq normativ manba o'rnini bosadimi?",
            "explanation": "Skrinshot hujjatning tahriri, konteksti va qo'llanish shartlarini ko'rsatmasligi mumkin.",
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
    ],

    "L09_M01_002": [
        {
            "code": "L09_Q004",
            "question": "Bir xil talab barcha obyektlarga avtomatik qo'llanadimi?",
            "explanation": "Talabning qo'llanishi obyekt turi va loyiha sharoitiga bog'liq bo'lishi mumkin.",
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L09_Q005",
            "question": "Obyekt funksiyasi normativ talab tanlashga ta'sir qilishi mumkinmi?",
            "explanation": "Turli funksiyadagi binolar uchun turli talablar amal qilishi mumkin.",
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L09_Q006",
            "question": "Boshqa loyiha talabini tekshirmasdan ko'chirish professional usulmi?",
            "explanation": "Har bir loyiha uchun qo'llanish doirasi qayta tekshiriladi.",
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
    ],

    "L09_M01_003": [
        {
            "code": "L09_Q007",
            "question": "Normativ hujjatning amaldagi tahririni tekshirish kerakmi?",
            "explanation": "Eski tahrir bilan ishlash noto'g'ri loyiha qaroriga olib kelishi mumkin.",
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L09_Q008",
            "question": "Kompyuterdagi eski PDF avtomatik ravishda amaldagi hujjat hisoblanadimi?",
            "explanation": "Hujjat holati rasmiy yoki ishonchli manbadan tekshiriladi.",
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L09_Q009",
            "question": "Normativ tekshiruvda manba va sana qayd qilinishi foydalimi?",
            "explanation": "Bu keyingi tekshiruv va audit uchun aniq iz qoldiradi.",
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L09_M01_004": [
        {
            "code": "L09_Q010",
            "question": "Professional normativ xulosa aniq manbaga tayanishi kerakmi?",
            "explanation": "Qarorning qaysi hujjat va bandga asoslanganini ko'rsatish kerak.",
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L09_Q011",
            "question": "Aniq normativ raqamni bandni ko'rmasdan xotiradan aytish xavfsizmi?",
            "explanation": "Xotiradagi qiymat eski yoki boshqa holatga tegishli bo'lishi mumkin.",
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L09_Q012",
            "question": "Talab → manba → band → loyiha yechimi zanjiri foydalimi?",
            "explanation": "Bu loyiha qarorini dalil bilan asoslashga yordam beradi.",
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L09_M01_005": [
        {
            "code": "L09_Q013",
            "question": "Normativ audit loyiha savolini aniq belgilashdan boshlanishi kerakmi?",
            "explanation": "Savol aniq bo'lmasa qaysi normativ talabni izlash ham noaniq bo'ladi.",
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L09_Q014",
            "question": "Bitta normativ bandga moslik butun loyihaning to'liq mosligini isbotlaydimi?",
            "explanation": "Loyihada ko'plab mustaqil normativ masalalar bo'lishi mumkin.",
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L09_Q015",
            "question": "Normativ bilan professional ishlashdagi to'g'ri workflow qaysi?",
            "explanation": "Avval obyekt va savol aniqlanadi, so'ng amaldagi manba va band topilib loyiha bilan solishtiriladi.",
            "options": [
                (
                    "A",
                    "Savol → obyekt → amaldagi manba → band → loyiha tekshiruvi → qayd",
                    True,
                ),
                (
                    "B",
                    "Internetdan tasodifiy raqam → loyihaga ko'chirish → tekshirmaslik",
                    False,
                ),
            ],
        },
    ],
}


def seed_level09_module01():
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
        ) in LEVEL09_MODULE01_LESSONS:

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
