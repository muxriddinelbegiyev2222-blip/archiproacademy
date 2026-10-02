from database.database import get_connection


# ============================================================
# LEVEL 1
# MODULE 05 - FORMA VA HAJM
# ============================================================

LEVEL01_MODULE05_LESSONS = [
    (
        "L01_M05",
        "L01_M05_001",
        "Forma va hajm nima?",
        "theory",
        "Binoni ikki o'lchamli fasad emas, uch o'lchamli hajm sifatida tushunish.",
        1,
        30,
        15,
    ),
    (
        "L01_M05",
        "L01_M05_002",
        "Asosiy va yordamchi hajmlar",
        "theory",
        "Bino kompozitsiyasidagi asosiy va ikkilamchi hajmlarni ajratish.",
        2,
        30,
        15,
    ),
    (
        "L01_M05",
        "L01_M05_003",
        "Hajmni oldinga va orqaga siljitish",
        "theory",
        "Fasad chuqurligi va 3D kompozitsiya yaratishni tushunish.",
        3,
        35,
        20,
    ),
    (
        "L01_M05",
        "L01_M05_004",
        "Oddiy shakldan kuchli arxitektura",
        "practice",
        "Sodda geometrik hajmlar yordamida sifatli turar joy yaratish.",
        4,
        40,
        20,
    ),
    (
        "L01_M05",
        "L01_M05_005",
        "Hajm kompozitsiyasidagi xatolar",
        "practice",
        "Turar joylarda keraksiz, tartibsiz va asossiz hajmlarni aniqlash.",
        5,
        40,
        20,
    ),
]


# ============================================================
# LESSON CONTENT
# ============================================================

LEVEL01_MODULE05_CONTENT = {
    "L01_M05_001": [
        {
            "title": "Uy faqat fasad emas",
            "type": "highlight",
            "text": """
            Uyga faqat old tomondan qarasangiz,
            uning faqat bitta qismini ko'rasiz.

            <br><br>

            Aslida bino:
            <b>eni + uzunligi + balandligi</b>
            bo'lgan uch o'lchamli obyekt.
            """,
        },
        {
            "title": "Forma nima?",
            "type": "normal",
            "text": """
            Forma — obyektning umumiy shakli.

            <br><br>

            Masalan:

            <br><br>

            • kubga yaqin;<br>
            • uzun to'rtburchak;<br>
            • L shakl;<br>
            • U shakl;<br>
            • murakkab birlashgan shakl.

            <br><br>

            Arxitekturada shakl tasodifan emas,
            funksiyaga va konsepsiyaga bog'liq bo'lishi kerak.
            """,
        },
        {
            "title": "Hajm nima?",
            "type": "normal",
            "text": """
            Hajm — binoning 3D ko'rinishdagi
            fazoviy massasini anglatadi.

            <br><br>

            Masalan, bir qavatli uyda:

            <br><br>

            asosiy yashash qismi,
            kirish qismi,
            ayvon,
            tom,
            terrasa

            <br><br>

            alohida hajmlar sifatida ko'rinishi mumkin.
            """,
        },
        {
            "title": "Oddiy misol",
            "type": "example",
            "text": """
            Qog'ozdan uchta quti yasaganingizni tasavvur qiling.

            <br><br>

            Birinchisi katta.

            <br>
            Ikkinchisi kichikroq.

            <br>
            Uchinchisi uzunroq.

            <br><br>

            Ularni turli joylashtirib,
            butunlay turli bino kompozitsiyalarini yaratish mumkin.

            <br><br>

            Arxitektura hajm bilan ishlashi ham shunga o'xshaydi.
            """,
        },
        {
            "title": "Boshlovchi xatosi",
            "type": "warning",
            "text": """
            Faqat old fasadni chiroyli qilish,
            yon va orqa tomonlarni unutish noto'g'ri.

            <br><br>

            Professional bino
            <b>360 darajada ishlashi</b> kerak.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Bir uy rasmini toping.

            <br><br>

            Uni xayolan faqat oddiy geometrik shakllarga ajrating.

            <br><br>

            Masalan:

            <br>
            katta quti + kichik quti + soyabon.

            <br><br>

            Nechta asosiy hajm ko'ryapsiz?
            """,
        },
    ],

    "L01_M05_002": [
        {
            "title": "Hamma hajm bir xil kuchli bo'lmasligi kerak",
            "type": "highlight",
            "text": """
            Yaxshi kompozitsiyada odatda
            <b>asosiy hajm</b> va
            <b>yordamchi hajmlar</b> mavjud.
            """,
        },
        {
            "title": "Asosiy hajm",
            "type": "normal",
            "text": """
            Asosiy hajm — binoning umumiy ko'rinishida
            eng kuchli seziladigan katta massa.

            <br><br>

            Masalan, bir qavatli uyda
            asosiy yashash bloki asosiy hajm bo'lishi mumkin.
            """,
        },
        {
            "title": "Yordamchi hajm",
            "type": "normal",
            "text": """
            Yordamchi hajm asosiy hajmni to'ldiradi.

            <br><br>

            Masalan:

            <br><br>

            • kirish soyaboni;<br>
            • terrasa;<br>
            • kichik yon blok;<br>
            • ayvon;<br>
            • garaj yoki carport qismi.
            """,
        },
        {
            "title": "Misol",
            "type": "example",
            "text": """
            Tasavvur qiling:

            <br><br>

            katta oq to'rtburchak hajm —
            uyning asosiy qismi.

            <br><br>

            Oldida kichik yog'och hajm —
            kirish.

            <br><br>

            Yon tomonda past soyabon —
            avtomobil uchun.

            <br><br>

            Ularning vazifasi va vizual kuchi bir xil emas.
            """,
        },
        {
            "title": "Xato",
            "type": "warning",
            "text": """
            Agar barcha hajmlar:

            <br><br>

            • bir xil katta;<br>
            • bir xil rangli;<br>
            • bir xil baland;<br>
            • bir xil kuchli

            <br><br>

            bo'lsa, ierarxiya yo'qolishi mumkin.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Bir uy tanlang.

            <br><br>

            1. Asosiy hajmni toping.<br>
            2. Ikki yordamchi hajmni toping.<br>
            3. Qaysi biri ko'zga birinchi tashlanishini yozing.
            """,
        },
    ],

    "L01_M05_003": [
        {
            "title": "Fasad tekis bo'lishi shart emas",
            "type": "highlight",
            "text": """
            Barcha devorlarni bitta tekis chiziqqa qo'yish
            har doim ham yaxshi yechim emas.

            <br><br>

            Hajmlarni oldinga yoki orqaga siljitish
            binoga chuqurlik beradi.
            """,
        },
        {
            "title": "Oldinga chiqarilgan hajm",
            "type": "example",
            "text": """
            Kirish qismini asosiy devordan
            1 metr oldinga chiqaring.

            <br><br>

            Endi kirish:

            <br><br>

            • kuchliroq ko'rinadi;<br>
            • soyaga ega bo'ladi;<br>
            • kompozitsion markazga aylanishi mumkin.
            """,
        },
        {
            "title": "Ichkariga olingan hajm",
            "type": "example",
            "text": """
            Terrasani asosiy hajmdan ichkariga kiriting.

            <br><br>

            Natijada:

            <br><br>

            • tabiiy soyali zona;<br>
            • chuqurlik;<br>
            • fasadga 3D effekt

            <br><br>

            hosil bo'lishi mumkin.
            """,
        },
        {
            "title": "Yorug'lik va soya",
            "type": "normal",
            "text": """
            Hajm oldinga yoki orqaga siljiganda
            faqat plan o'zgarmaydi.

            <br><br>

            Quyosh tushganda turli soyalar paydo bo'ladi.

            <br><br>

            Shuning uchun hajm kompozitsiyasi
            fasadni kun davomida turlicha ko'rsatadi.
            """,
        },
        {
            "title": "Boshlovchi xatosi",
            "type": "warning",
            "text": """
            Fasadni “zamonaviyroq” qilish uchun
            har bir devorni har xil chuqurlikka surish
            noto'g'ri.

            <br><br>

            Har bir siljishning sababi bo'lishi kerak.
            """,
        },
        {
            "title": "Professional savol",
            "type": "highlight",
            "text": """
            <b>
            “Bu hajm nima uchun oldinga chiqdi
            yoki nima uchun ichkariga kirdi?”
            </b>

            <br><br>

            Agar javob bo'lmasa,
            qarorni qayta tekshirish kerak.
            """,
        },
    ],

    "L01_M05_004": [
        {
            "title": "Murakkab = professional emas",
            "type": "highlight",
            "text": """
            Juda ko'p shakl ishlatish
            binoni avtomatik professional qilmaydi.

            <br><br>

            Ba'zan juda oddiy hajm
            kuchli arxitektura beradi.
            """,
        },
        {
            "title": "Oddiy kub",
            "type": "example",
            "text": """
            Oddiy to'rtburchak uy tasavvur qiling.

            <br><br>

            Fasad juda sodda.

            <br><br>

            Lekin:

            <br><br>

            • kirish chuqurlashtirilgan;<br>
            • katta deraza aniq joylashtirilgan;<br>
            • materiallar tartibli;<br>
            • tom proporsiyasi yaxshi;<br>
            • soyalar nazorat qilingan.

            <br><br>

            Natija juda kuchli bo'lishi mumkin.
            """,
        },
        {
            "title": "Kamroq element — ko'proq nazorat",
            "type": "normal",
            "text": """
            Elementlar kamaygan sari
            har bir elementning sifati muhimlashadi.

            <br><br>

            Sodda arxitektura:
            xato qilish oson emas degani emas.

            <br><br>

            Aksincha, xatolar ko'proq ko'rinadi.
            """,
        },
        {
            "title": "Keraksiz shakllar",
            "type": "warning",
            "text": """
            Fasadga:

            <br><br>

            • sababsiz uchburchak;<br>
            • tasodifiy quti;<br>
            • ortiqcha portal;<br>
            • keraksiz dekorativ ustun

            <br><br>

            qo'shish kompozitsiyani kuchaytirmasligi mumkin.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Juda sodda zamonaviy uy toping.

            <br><br>

            Nega u zerikarli emasligini yozing.

            <br><br>

            Kamida 3 sabab:

            <br><br>

            • proporsiya;<br>
            • material;<br>
            • chuqurlik;<br>
            • deraza joylashuvi;<br>
            • soya

            <br><br>

            kabi tushunchalardan foydalaning.
            """,
        },
    ],

    "L01_M05_005": [
        {
            "title": "Hajm xatolarini aniqlaymiz",
            "type": "highlight",
            "text": """
            Endi uyga 3D obyekt sifatida qarab,
            ortiqcha va tartibsiz hajmlarni topishni mashq qilamiz.
            """,
        },
        {
            "title": "Xato 1 — haddan tashqari ko'p hajm",
            "type": "warning",
            "text": """
            Bitta kichik uyda:

            <br><br>

            8–10 ta alohida quti,
            turli balandlik,
            turli chuqurlik,
            turli material.

            <br><br>

            Agar umumiy tizim bo'lmasa,
            bino parchalangan ko'rinishi mumkin.
            """,
        },
        {
            "title": "Xato 2 — yordamchi hajm asosiydan kuchli",
            "type": "warning",
            "text": """
            Kirish uchun yaratilgan kichik portal
            butun uy hajmidan ham kuchli ko'rinmoqda.

            <br><br>

            Natijada ierarxiya buzilishi mumkin.
            """,
        },
        {
            "title": "Xato 3 — sababsiz siljishlar",
            "type": "warning",
            "text": """
            Bir devor 30 sm oldinga.

            <br>
            Boshqasi 40 sm orqaga.

            <br>
            Yana biri 25 sm oldinga.

            <br><br>

            Agar bularning funksional yoki kompozitsion sababi bo'lmasa,
            fasad “tasodifan yig'ilgan” ko'rinishi mumkin.
            """,
        },
        {
            "title": "Xato 4 — plan bilan hajm uzilib ketgan",
            "type": "warning",
            "text": """
            Tashqaridan chiroyli hajm yaratildi.

            <br><br>

            Lekin uning ichida
            foydalanib bo'lmaydigan g'alati burchak yoki
            foydasiz maydon paydo bo'ldi.

            <br><br>

            Bu yaxshi yechim emas.
            """,
        },
        {
            "title": "Professional tekshiruv",
            "type": "example",
            "text": """
            Har bir hajm uchun so'rang:

            <br><br>

            <b>1.</b> Bu asosiy yoki yordamchi hajmmi?<br><br>
            <b>2.</b> Nega aynan shu o'lchamda?<br><br>
            <b>3.</b> Nega oldinga yoki orqaga siljigan?<br><br>
            <b>4.</b> Ichki funksiyaga mosmi?<br><br>
            <b>5.</b> Olib tashlasak loyiha yaxshilanadimi?
            """,
        },
        {
            "title": "Mini-loyiha",
            "type": "example",
            "text": """
            Bir murakkab uy tanlang.

            <br><br>

            Uni xayolan oddiy qutilarga ajrating.

            <br><br>

            Keyin kamida bitta hajmni
            olib tashlash mumkinmi, o'ylang.

            <br><br>

            Agar mumkin bo'lsa,
            nima uchunligini yozing.
            """,
        },
        {
            "title": "Modul yakuni",
            "type": "highlight",
            "text": """
            Siz endi:

            <br><br>

            ✓ forma;<br>
            ✓ hajm;<br>
            ✓ asosiy hajm;<br>
            ✓ yordamchi hajm;<br>
            ✓ hajm siljishi;<br>
            ✓ chuqurlik;<br>
            ✓ 3D kompozitsiya

            <br><br>

            tushunchalarini bilasiz.

            <br><br>

            LEVEL 1 da endi oxirgi katta modul qoldi:

            <br><br>

            <b>Arxitektura uslublari.</b>
            """,
        },
    ],
}


# ============================================================
# QUIZ DATA
# ============================================================

LEVEL01_MODULE05_QUIZ = {
    "L01_M05_001": [
        {
            "code": "L01_Q061",
            "question": "Bino faqat fasaddan iboratmi?",
            "explanation": (
                "Bino eni, uzunligi va balandligi bo'lgan uch o'lchamli obyekt."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L01_Q062",
            "question": "Arxitekturada hajm nimani anglatadi?",
            "explanation": (
                "Hajm binoning uch o'lchamli fazoviy massasini anglatadi."
            ),
            "options": [
                ("A", "3D fazoviy massa", True),
                ("B", "Faqat rang", False),
                ("C", "Faqat plan chizig'i", False),
            ],
        },
        {
            "code": "L01_Q063",
            "question": "Professional bino faqat old fasaddan yaxshi ko'rinishi kifoyami?",
            "explanation": (
                "Binoning barcha tomonlari va umumiy 3D kompozitsiyasi muhim."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
    ],

    "L01_M05_002": [
        {
            "code": "L01_Q064",
            "question": "Asosiy hajm nima?",
            "explanation": (
                "Asosiy hajm kompozitsiyada eng kuchli seziladigan katta massa."
            ),
            "options": [
                ("A", "Kompozitsiyaning asosiy massasi", True),
                ("B", "Har qanday kichik detal", False),
            ],
        },
        {
            "code": "L01_Q065",
            "question": "Yordamchi hajmning vazifasi nima?",
            "explanation": (
                "Yordamchi hajm asosiy hajmni to'ldiradi va muayyan funksiyani bajaradi."
            ),
            "options": [
                ("A", "Asosiy hajmni to'ldirish", True),
                ("B", "Har doim asosiydan kuchli bo'lish", False),
            ],
        },
        {
            "code": "L01_Q066",
            "question": "Barcha hajmlar bir xil vizual kuchga ega bo'lishi shartmi?",
            "explanation": (
                "Kompozitsiyada ierarxiya bo'lishi foydali."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
    ],

    "L01_M05_003": [
        {
            "code": "L01_Q067",
            "question": "Hajmni oldinga chiqarish fasadga nima berishi mumkin?",
            "explanation": (
                "U chuqurlik, soya va kompozitsion urg'u yaratishi mumkin."
            ),
            "options": [
                ("A", "Chuqurlik va urg'u", True),
                ("B", "Hech qanday ta'sir qilmaydi", False),
            ],
        },
        {
            "code": "L01_Q068",
            "question": "Terrasani ichkariga olish tabiiy soyali zona yaratishi mumkinmi?",
            "explanation": (
                "Ichkariga olingan hajm quyoshdan himoyalangan chuqur zona yaratishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L01_Q069",
            "question": "Har bir devorni turli chuqurlikka surish professional yechimmi?",
            "explanation": (
                "Har bir siljishning funksional yoki kompozitsion sababi bo'lishi kerak."
            ),
            "options": [
                ("A", "Har doim", False),
                ("B", "Faqat asosli bo'lsa", True),
            ],
        },
    ],

    "L01_M05_004": [
        {
            "code": "L01_Q070",
            "question": "Murakkab shakl har doim professional arxitektura deganimi?",
            "explanation": (
                "Sodda shakl ham yaxshi proporsiya va kompozitsiya bilan kuchli natija berishi mumkin."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L01_Q071",
            "question": "Sodda arxitekturada xatolar kamroq ko'rinadimi?",
            "explanation": (
                "Sodda kompozitsiyada har bir detal kuchli ko'rinadi, shuning uchun xatolar ham sezilarli."
            ),
            "options": [
                ("A", "Har doim kamroq", False),
                ("B", "Yo'q, xatolar aniq ko'rinishi mumkin", True),
            ],
        },
        {
            "code": "L01_Q072",
            "question": "Keraksiz dekorativ hajmlar kompozitsiyani buzishi mumkinmi?",
            "explanation": (
                "Asossiz elementlar umumiy shaklni parchalashi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L01_M05_005": [
        {
            "code": "L01_Q073",
            "question": "Juda ko'p alohida hajm nimaga olib kelishi mumkin?",
            "explanation": (
                "Tizim bo'lmasa bino parchalangan va tartibsiz ko'rinishi mumkin."
            ),
            "options": [
                ("A", "Parchalangan kompozitsiyaga", True),
                ("B", "Har doim yaxshi natijaga", False),
            ],
        },
        {
            "code": "L01_Q074",
            "question": "Yordamchi hajm asosiy hajmdan kuchliroq bo'lsa nima buzilishi mumkin?",
            "explanation": (
                "Kompozitsion ierarxiya buzilishi mumkin."
            ),
            "options": [
                ("A", "Ierarxiya", True),
                ("B", "Faqat material narxi", False),
            ],
        },
        {
            "code": "L01_Q075",
            "question": "Professional tekshiruvda qaysi savol foydali?",
            "explanation": (
                "Har bir hajmning nima sababdan mavjudligini tushunish muhim."
            ),
            "options": [
                ("A", "Bu hajm nima uchun kerak?", True),
                ("B", "Faqat necha rang bor?", False),
            ],
        },
    ],
}


# ============================================================
# DATABASE SEED
# ============================================================

def seed_level01_module05():
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
        ) in LEVEL01_MODULE05_LESSONS:

            cursor.execute(
                """
                SELECT id
                FROM course_modules
                WHERE code = ?
                LIMIT 1
                """,
                (
                    module_code,
                ),
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
