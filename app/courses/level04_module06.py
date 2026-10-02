from database.database import get_connection


# ============================================================
# LEVEL 4
# MODULE 06 - BANJA VA YORDAMCHI BINO
# ============================================================

LEVEL04_MODULE06_LESSONS = [
    (
        "L04_M06",
        "L04_M06_001",
        "Banja funksional sxemasi",
        "theory",
        "Banja tarkibidagi asosiy xonalar va ularning o'zaro aloqasini tushunish.",
        1,
        40,
        20,
    ),
    (
        "L04_M06",
        "L04_M06_002",
        "Banja va uy aloqasi",
        "theory",
        "Banjani uy, hovli va private dam olish zonasi bilan bog'lash.",
        2,
        40,
        20,
    ),
    (
        "L04_M06",
        "L04_M06_003",
        "Nam va quruq zonalar",
        "theory",
        "Dush, bug'li xona va dam olish zonasini funksional ajratish.",
        3,
        45,
        20,
    ),
    (
        "L04_M06",
        "L04_M06_004",
        "Ombor, texnik va service xonalari",
        "practice",
        "Yordamchi funksiyalarni asosiy yashash zonasiga xalaqit bermaydigan tarzda joylashtirish.",
        4,
        45,
        20,
    ),
    (
        "L04_M06",
        "L04_M06_005",
        "Banja va yordamchi bino auditi",
        "practice",
        "Banja, ombor va texnik zonalardagi tipik rejalash xatolarini aniqlash.",
        5,
        55,
        25,
    ),
]


# ============================================================
# CONTENT
# ============================================================

LEVEL04_MODULE06_CONTENT = {
    "L04_M06_001": [
        {
            "title": "Banja — bitta xona emas",
            "type": "highlight",
            "text": """
            Banja loyihalashda
            faqat issiq xona haqida o'ylash yetarli emas.

            <br><br>

            Foydalanish ssenariysi bir nechta
            ketma-ket makondan tashkil topishi mumkin.
            """,
        },
        {
            "title": "Asosiy funksiyalar",
            "type": "normal",
            "text": """
            Banja tarkibida loyiha talabiga qarab:

            <br><br>

            • kirish yoki tambur;<br>
            • kiyim almashtirish joyi;<br>
            • dush;<br>
            • bug'li yoki issiq xona;<br>
            • dam olish xonasi;<br>
            • sanuzel;<br>
            • texnik zona;<br>
            • tashqi dam olish maydoni

            <br><br>

            bo'lishi mumkin.
            """,
        },
        {
            "title": "Foydalanuvchi yo'lini o'ylang",
            "type": "highlight",
            "text": """
            Banja planini xonalar ro'yxatidan emas,

            <br><br>

            <b>
            odamning qanday foydalanishidan
            </b>

            <br><br>

            boshlash foydali.
            """,
        },
        {
            "title": "Tasavvur qiling",
            "type": "example",
            "text": """
            Odam banjaga kirdi.

            <br><br>

            Kiyim almashtirdi,
            dushga o'tdi,
            issiq xonadan foydalandi,
            keyin dam olish zonasiga chiqdi.

            <br><br>

            Shu harakat plan ichida
            tushunarli va qulay bo'lishi kerak.
            """,
        },
        {
            "title": "Xato",
            "type": "warning",
            "text": """
            Dam olish xonasiga borish uchun
            har safar nam dush zonasidan
            o'tish kerak bo'lsa,

            <br><br>

            quruq va nam circulation
            bir-biriga xalaqit berishi mumkin.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Quyidagi funksiyalar uchun
            bubble diagram yarating:

            <br><br>

            KIRISH<br>
            KIYIM ALMASHTIRISH<br>
            DUSH<br>
            BUG'LI XONA<br>
            DAM OLISH
            """,
        },
    ],

    "L04_M06_002": [
        {
            "title": "Banja uchastkaning qayerida bo'ladi?",
            "type": "highlight",
            "text": """
            Banja uchun yaxshi xona rejasining o'zi yetarli emas.

            <br><br>

            Uning uchastkadagi joylashuvi ham muhim.
            """,
        },
        {
            "title": "Uyga biriktirilgan variant",
            "type": "normal",
            "text": """
            Banja uyga biriktirilsa:

            <br><br>

            • kirish qisqarishi;<br>
            • kommunikatsiyalarni birlashtirish imkoniyati;<br>
            • qishda foydalanish qulayligi

            <br><br>

            kabi afzalliklar bo'lishi mumkin.
            """,
        },
        {
            "title": "Alohida bino varianti",
            "type": "normal",
            "text": """
            Banja alohida bino bo'lsa:

            <br><br>

            • asosiy uydan funksional ajralishi;<br>
            • alohida dam olish muhiti;<br>
            • hovli bilan kuchliroq aloqa

            <br><br>

            yaratish mumkin.
            """,
        },
        {
            "title": "Private hovli bilan aloqa",
            "type": "example",
            "text": """
            Banjadan chiqqan odam
            private dam olish hovlisi,
            ayvon yoki terassaga o'tishi mumkin.

            <br><br>

            Shunda ichki va tashqi
            dam olish funksiyalari birlashadi.
            """,
        },
        {
            "title": "Guest circulation",
            "type": "normal",
            "text": """
            Agar banjadan mehmonlar ham foydalansa,

            <br><br>

            ular asosiy family yotoqxona zonasidan
            o'tmasdan yetib borishi foydali.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Banjani uch xil joylashtiring:

            <br><br>

            1. Uyga biriktirilgan<br>
            2. Hovlida alohida<br>
            3. Ayvon orqali ulangan

            <br><br>

            Har variantning
            afzallik va kamchiligini yozing.
            """,
        },
    ],

    "L04_M06_003": [
        {
            "title": "Nam va quruq zona",
            "type": "highlight",
            "text": """
            Banjada makonlarni
            namlik darajasi bo'yicha ham
            fikrlash kerak.

            <br><br>

            Bu funksional zonalashning
            muhim qismi.
            """,
        },
        {
            "title": "Nam zona",
            "type": "normal",
            "text": """
            Nam zonaga:

            <br><br>

            • dush;<br>
            • yuvinish;<br>
            • suv bilan bog'liq funksiyalar

            <br><br>

            kirishi mumkin.
            """,
        },
        {
            "title": "Quruq zona",
            "type": "normal",
            "text": """
            Quruq zona:

            <br><br>

            • kiyim almashtirish;<br>
            • dam olish;<br>
            • o'tirish;<br>
            • saqlash

            <br><br>

            bilan bog'liq bo'lishi mumkin.
            """,
        },
        {
            "title": "Nam yo'lni kamaytirish",
            "type": "example",
            "text": """
            Dushdan chiqqan odam
            butun dam olish xonasini
            kesib o'tishi kerak bo'lsa,

            <br><br>

            nam va quruq circulation
            noto'g'ri tashkil qilingan bo'lishi mumkin.
            """,
        },
        {
            "title": "Shamollatish haqida fikrlash",
            "type": "warning",
            "text": """
            Namlik yuqori bo'lgan makonlarda
            shamollatish masalasini
            loyiha boshidanoq hisobga olish kerak.

            <br><br>

            Aniq texnik yechimlar esa
            keyingi muhandislik bosqichida
            mutaxassislar bilan belgilanadi.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Banja planida:

            <br><br>

            NAM ZONA

            va

            QURUQ ZONA

            <br><br>

            ni ikki xil rang bilan belgilang.

            <br><br>

            Ular qayerda kesishadi?
            """,
        },
    ],

    "L04_M06_004": [
        {
            "title": "Yordamchi xona ham arxitekturaning bir qismi",
            "type": "highlight",
            "text": """
            Ombor va texnik xonalar
            fasadda kam ko'rinishi mumkin,

            <br><br>

            lekin uy qulayligiga
            juda katta ta'sir qiladi.
            """,
        },
        {
            "title": "Ombor",
            "type": "normal",
            "text": """
            Omborda:

            <br><br>

            • hovli inventari;<br>
            • mavsumiy buyumlar;<br>
            • asboblar;<br>
            • tashqi mebel;<br>
            • xo'jalik buyumlari

            <br><br>

            saqlanishi mumkin.
            """,
        },
        {
            "title": "Texnik xona",
            "type": "normal",
            "text": """
            Texnik xona
            uy muhandislik tizimlariga
            xizmat qiluvchi hudud bo'lishi mumkin.

            <br><br>

            Uning aniq jihozlanishi
            loyiha muhandislik yechimlariga bog'liq.
            """,
        },
        {
            "title": "Service kirish",
            "type": "example",
            "text": """
            Texnik yoki ombor xonasiga
            tashqaridan qulay kirish bo'lsa,

            <br><br>

            ustalar va service xodimlari
            asosiy family living orqali
            yurishga majbur bo'lmasligi mumkin.
            """,
        },
        {
            "title": "To'g'ri joyga qo'ying",
            "type": "normal",
            "text": """
            Yordamchi funksiyalarni
            livingning eng yaxshi hovli tomoniga
            joylashtirish shart emas.

            <br><br>

            Ular noqulayroq yoki service tomonlardan
            oqilona foydalanishi mumkin.
            """,
        },
        {
            "title": "Omborga borish yo'li",
            "type": "warning",
            "text": """
            Bog' asbobini olish uchun
            odam butun uy ichidan o'tishi kerak bo'lsa,

            <br><br>

            omborning joylashuvi
            qayta ko'rib chiqilishi mumkin.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Uchastkangizda belgilang:

            <br><br>

            • ombor;<br>
            • texnik xona;<br>
            • chiqindi nuqtasi;<br>
            • service kirish;<br>
            • hovli inventari yo'li.

            <br><br>

            Family va guest oqimlari bilan
            konfliktlarni toping.
            """,
        },
    ],

    "L04_M06_005": [
        {
            "title": "Banja va service auditini boshlaymiz",
            "type": "highlight",
            "text": """
            Endi yordamchi makonlarni
            “qolgan joyga qo'yiladigan xonalar”
            sifatida emas,

            <br><br>

            professional loyiha tizimining
            muhim qismi sifatida tekshiramiz.
            """,
        },
        {
            "title": "Xato 1 — banja family bedroom orqali",
            "type": "warning",
            "text": """
            Mehmon banjaga borish uchun
            private yotoqxona koridoridan o'tadi.

            <br><br>

            Privacy zaiflashadi.
            """,
        },
        {
            "title": "Xato 2 — nam va quruq oqim aralashgan",
            "type": "warning",
            "text": """
            Dushdan chiqish yo'li
            asosiy quruq dam olish zonasini
            doim kesib o'tadi.
            """,
        },
        {
            "title": "Xato 3 — texnik xona livingdan kiriladi",
            "type": "warning",
            "text": """
            Har qanday texnik xizmat uchun
            ishchi family living orqali
            o'tishga majbur.
            """,
        },
        {
            "title": "Xato 4 — ombor hovlidan uzoq",
            "type": "warning",
            "text": """
            Bog' va hovli buyumlari omborda,

            <br><br>

            lekin omborga kirish
            hovlining qarama-qarshi tomonida.
            """,
        },
        {
            "title": "Xato 5 — service eng yaxshi hovlini egallagan",
            "type": "warning",
            "text": """
            Living va family hovli uchun
            eng yaxshi zona mavjud,

            <br><br>

            lekin u ombor va
            texnik funksiyalarga berilgan.
            """,
        },
        {
            "title": "Professional checklist",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            <b>1.</b> Banjaga kirish qayerdan?<br><br>
            <b>2.</b> Guest privacy to'g'rimi?<br><br>
            <b>3.</b> Nam va quruq zona ajralganmi?<br><br>
            <b>4.</b> Dam olish hovliga ulanganmi?<br><br>
            <b>5.</b> Ombor nimaga xizmat qiladi?<br><br>
            <b>6.</b> Texnik xona uchun service kirish bormi?<br><br>
            <b>7.</b> Yordamchi zona livingga xalaqit bermayaptimi?
            """,
        },
        {
            "title": "Mini-case",
            "type": "example",
            "text": """
            Uchastkada quyidagilar kerak:

            <br><br>

            • banja;<br>
            • dush;<br>
            • kiyim almashtirish;<br>
            • dam olish xona;<br>
            • private tashqi terassa;<br>
            • ombor;<br>
            • texnik xona.

            <br><br>

            Talab:

            <br><br>

            banjadan mehmon ham foydalana olsin,
            lekin asosiy family bedroom zonasi
            buzilmasin.

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

            ✓ banja funksional sxemasini tuzish;<br>
            ✓ uy va hovli bilan bog'lash;<br>
            ✓ nam va quruq zonalarni ajratish;<br>
            ✓ omborni rejalashtirish;<br>
            ✓ texnik xonani joylashtirish;<br>
            ✓ service circulationni boshqarish

            <br><br>

            ko'nikmalariga ega bo'ldingiz.

            <br><br>

            Keyingi modul:
            <b>Issiq iqlimda loyiha.</b>
            """,
        },
    ],
}


# ============================================================
# QUIZ
# ============================================================

LEVEL04_MODULE06_QUIZ = {
    "L04_M06_001": [
        {
            "code": "L04_Q076",
            "question": "Banja faqat bitta issiq xonadan iborat bo'lishi shartmi?",
            "explanation": (
                "Loyiha ehtiyojiga qarab dush, kiyim almashtirish va dam olish kabi funksiyalar ham bo'lishi mumkin."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L04_Q077",
            "question": "Banja rejasida foydalanuvchining harakat ketma-ketligi muhimmi?",
            "explanation": (
                "Xonalar odamning real foydalanish ssenariysi asosida bog'lanadi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L04_Q078",
            "question": "Dam olish zonasiga faqat nam dush orqali o'tish noqulay bo'lishi mumkinmi?",
            "explanation": (
                "Nam va quruq harakatning ortiqcha kesishishi foydalanishni yomonlashtirishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L04_M06_002": [
        {
            "code": "L04_Q079",
            "question": "Banjaning uchastkadagi joylashuvi ham muhimmi?",
            "explanation": (
                "Uy, hovli, private zona va mehmon circulationi bilan aloqasi hisobga olinadi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L04_Q080",
            "question": "Banja alohida bino sifatida ham loyihalanishi mumkinmi?",
            "explanation": (
                "U alohida yoki asosiy uyga bog'langan yechimda tashkil qilinishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L04_Q081",
            "question": "Mehmon banjaga borishda family bedroom zonasidan o'tishi shartmi?",
            "explanation": (
                "Guest circulationni private zonadan ajratish foydali."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
    ],

    "L04_M06_003": [
        {
            "code": "L04_Q082",
            "question": "Banjada nam va quruq zonalarni farqlash foydalimi?",
            "explanation": (
                "Bu circulation va foydalanish sifatini yaxshilashga yordam beradi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L04_Q083",
            "question": "Dush odatda nam zona sifatida qaraladimi?",
            "explanation": (
                "Dush suv bilan faol ishlatiladigan makon hisoblanadi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L04_Q084",
            "question": "Namlik yuqori makonlarda shamollatishni loyiha boshida hisobga olish kerakmi?",
            "explanation": (
                "Namlikni boshqarish uchun shamollatish masalasi muhim, aniq texnik yechim esa mutaxassislar bilan belgilanadi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L04_M06_004": [
        {
            "code": "L04_Q085",
            "question": "Ombor uy qulayligiga ta'sir qiladimi?",
            "explanation": (
                "To'g'ri saqlash tizimi hovli va xo'jalik buyumlarini tartibli boshqarishga yordam beradi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L04_Q086",
            "question": "Texnik xona uchun tashqi service kirish foydali bo'lishi mumkinmi?",
            "explanation": (
                "Texnik xizmat paytida family living orqali yurishni kamaytirishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L04_Q087",
            "question": "Hovli asboblari ombori hovlidan juda uzoqda bo'lsa bu noqulaylik yaratishi mumkinmi?",
            "explanation": (
                "Omborning vazifasi va undan foydalaniladigan hudud orasidagi aloqa muhim."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L04_M06_005": [
        {
            "code": "L04_Q088",
            "question": "Banjaga guest circulationni private bedroom orqali tashkil qilish zaif yechim bo'lishi mumkinmi?",
            "explanation": (
                "Bu oilaviy privacyga xalaqit berishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L04_Q089",
            "question": "Yordamchi binolarni uchastkaning qolgan tasodifiy joyiga qo'yish har doim to'g'rimi?",
            "explanation": (
                "Ularning vazifasi, service yo'li va asosiy yashash zonalari bilan aloqasi tahlil qilinadi."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L04_Q090",
            "question": "Banja va yordamchi bino auditidagi muhim savollardan biri qaysi?",
            "explanation": (
                "Kirish, privacy, nam-quruq zonalar va service circulation birgalikda tekshiriladi."
            ),
            "options": [
                ("A", "Service kirish qayerda va kim foydalanadi?", True),
                ("B", "Faqat fasad rangi qanday?", False),
            ],
        },
    ],
}


# ============================================================
# DATABASE SEED
# ============================================================

def seed_level04_module06():
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
        ) in LEVEL04_MODULE06_LESSONS:

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
