from database.database import get_connection


# ============================================================
# LEVEL 2
# MODULE 10 - YORDAMCHI XONALAR
# ============================================================

LEVEL02_MODULE10_LESSONS = [
    (
        "L02_M10",
        "L02_M10_001",
        "Yordamchi xonalar vazifasi",
        "theory",
        "Garderob, laundry, ombor va texnik xonalarning uy rejasidagi rolini tushunish.",
        1,
        35,
        20,
    ),
    (
        "L02_M10",
        "L02_M10_002",
        "Garderob va storage",
        "theory",
        "Kiyim, kundalik buyumlar va mavsumiy predmetlar uchun saqlash tizimini tashkil qilish.",
        2,
        35,
        20,
    ),
    (
        "L02_M10",
        "L02_M10_003",
        "Laundry xonasi",
        "practice",
        "Kir yuvish, quritish, saralash va saqlash jarayonlarini mantiqiy rejalashtirish.",
        3,
        35,
        20,
    ),
    (
        "L02_M10",
        "L02_M10_004",
        "Ombor va texnik xona",
        "practice",
        "Ombor hamda texnik funksiyalarni yashash zonalariga xalaqit bermaydigan qilib joylashtirish.",
        4,
        35,
        20,
    ),
    (
        "L02_M10",
        "L02_M10_005",
        "Yordamchi xonalar auditi",
        "practice",
        "Yordamchi xonalarni joylashuv, circulation, storage va kundalik foydalanish bo'yicha tekshirish.",
        5,
        40,
        25,
    ),
]


# ============================================================
# CONTENT
# ============================================================

LEVEL02_MODULE10_CONTENT = {
    "L02_M10_001": [
        {
            "title": "Yordamchi xona nima?",
            "type": "highlight",
            "text": """
            Yordamchi xonalar
            uyda asosiy yashash funksiyasini
            bajarmaydi.

            <br><br>

            Lekin ular
            kundalik hayotni tartibli
            va qulay qilishda
            juda katta rol o'ynaydi.
            """,
        },
        {
            "title": "Asosiy turlari",
            "type": "normal",
            "text": """
            Yordamchi makonlarga
            loyiha vazifasiga qarab:

            <br><br>

            • garderob;<br>
            • laundry;<br>
            • pantry yoki ombor;<br>
            • texnik xona;<br>
            • cleaning storage;<br>
            • mavsumiy buyumlar storage'i

            <br><br>

            kirishi mumkin.
            """,
        },
        {
            "title": "Nega muhim?",
            "type": "highlight",
            "text": """
            Agar yordamchi funksiyalar
            oldindan rejalashtirilmasa,

            <br><br>

            kundalik buyumlar
            yashash xonalariga
            tarqalib ketishi mumkin.
            """,
        },
        {
            "title": "Tasavvur qiling",
            "type": "example",
            "text": """
            Uy katta.

            <br><br>

            Living,
            bedrooms
            va oshxona yaxshi.

            <br><br>

            Lekin changyutgich,
            dazmol,
            mavsumiy kiyim,
            maishiy buyumlar

            <br><br>

            uchun maxsus joy yo'q.

            <br><br>

            Natijada asosiy xonalar
            storage vazifasini ham
            bajarishga majbur bo'ladi.
            """,
        },
        {
            "title": "Arxitektor savoli",
            "type": "normal",
            "text": """
            Har bir uyda so'rang:

            <br><br>

            <b>
            Kundalik va kam ishlatiladigan
            buyumlar qayerda saqlanadi?
            </b>
            """,
        },
        {
            "title": "Mini-vazifa",
            "type": "example",
            "text": """
            Uy uchun yordamchi
            funksiyalar ro'yxatini tuzing.

            <br><br>

            Masalan:

            • kiyim;<br>
            • laundry;<br>
            • cleaning;<br>
            • oziq-ovqat zaxirasi;<br>
            • texnik jihozlar;<br>
            • mavsumiy buyumlar.
            """,
        },
    ],

    "L02_M10_002": [
        {
            "title": "Garderob va oddiy shkaf farqi",
            "type": "highlight",
            "text": """
            Garderob
            oddiy bitta shkafdan
            kengroq storage tizimi
            bo'lishi mumkin.

            <br><br>

            Unda kiyim,
            poyabzal
            va boshqa shaxsiy buyumlar
            tartibli saqlanadi.
            """,
        },
        {
            "title": "Joylashuv",
            "type": "normal",
            "text": """
            Garderobning joyi
            foydalanadigan odamga
            mantiqan yaqin bo'lishi kerak.

            <br><br>

            Masalan:

            bedroom bilan bog'langan
            garderob kundalik foydalanishda
            qulay bo'lishi mumkin.
            """,
        },
        {
            "title": "Kirish garderobi",
            "type": "normal",
            "text": """
            Entrance yaqinida
            alohida storage bo'lsa,

            <br><br>

            tashqi kiyim,
            poyabzal
            va mehmon buyumlarini
            tartibli joylashtirish mumkin.
            """,
        },
        {
            "title": "Faqat sig'im emas",
            "type": "warning",
            "text": """
            Garderobga juda ko'p
            shkaf sig'dirish

            <br><br>

            uning yaxshi ishlashini
            anglatmaydi.

            <br><br>

            Odam kirishi,
            buyumni olishi
            va qayta chiqishi ham
            qulay bo'lishi kerak.
            """,
        },
        {
            "title": "Mavsumiy storage",
            "type": "example",
            "text": """
            Har kuni ishlatilmaydigan:

            <br><br>

            • qishki kiyim;<br>
            • chamadon;<br>
            • qo'shimcha ko'rpa;<br>
            • katta qutilar

            <br><br>

            uchun alohida storage
            rejalashtirilishi mumkin.
            """,
        },
        {
            "title": "Mini-vazifa",
            "type": "example",
            "text": """
            Storage'ni 3 guruhga ajrating:

            <br><br>

            1. kundalik;<br>
            2. mavsumiy;<br>
            3. kam ishlatiladigan.

            <br><br>

            Har bir guruhni
            uyda qayerga joylashtirish
            ma'qul ekanini o'ylang.
            """,
        },
    ],

    "L02_M10_003": [
        {
            "title": "Laundry — jarayon xonasi",
            "type": "highlight",
            "text": """
            Laundry faqat
            kir yuvish mashinasi
            qo'yiladigan joy emas.

            <br><br>

            Bu yerda butun
            maishiy jarayon mavjud.
            """,
        },
        {
            "title": "Laundry jarayoni",
            "type": "normal",
            "text": """
            Jarayonni tasavvur qiling:

            <br><br>

            kir kiyim →
            saralash →
            yuvish →
            quritish →
            dazmollash yoki yig'ish →
            saqlash.
            """,
        },
        {
            "title": "Jihoz atrofida foydalanish",
            "type": "normal",
            "text": """
            Kir yuvish mashinasi
            yoki boshqa jihoz
            faqat o'z konturini
            egallamaydi.

            <br><br>

            Uning eshigi ochiladi,
            odam oldida turadi
            va kirlarni joylashtiradi.
            """,
        },
        {
            "title": "Storage",
            "type": "highlight",
            "text": """
            Laundryda:

            <br><br>

            • kir yuvish vositalari;<br>
            • kir savati;<br>
            • dazmol;<br>
            • cleaning buyumlari

            <br><br>

            uchun storage kerak bo'lishi mumkin.
            """,
        },
        {
            "title": "Laundry joylashuvi",
            "type": "example",
            "text": """
            Laundry bedroomlardan
            juda uzoqda bo'lsa,

            <br><br>

            kir kiyimlarni
            uy bo'ylab uzoq tashish
            talab qilinishi mumkin.

            <br><br>

            Juda public joyda bo'lsa esa
            kundalik maishiy jarayon
            ko'zga tashlanishi mumkin.
            """,
        },
        {
            "title": "Circulationni bloklamang",
            "type": "warning",
            "text": """
            Laundry eshigi
            yoki ochilgan jihoz

            <br><br>

            asosiy hallwayni
            butunlay bloklab qo'ymasligi kerak.
            """,
        },
        {
            "title": "Mini-vazifa",
            "type": "example",
            "text": """
            Laundry sxemasini chizing.

            <br><br>

            Belgilang:

            • washing;<br>
            • drying;<br>
            • basket;<br>
            • storage;<br>
            • ishchi sirt.

            <br><br>

            Jarayon ketma-ketligini
            strelka bilan ko'rsating.
            """,
        },
    ],

    "L02_M10_004": [
        {
            "title": "Ombor",
            "type": "highlight",
            "text": """
            Ombor
            kamroq ishlatiladigan
            yoki katta hajmdagi buyumlarni
            saqlash uchun xizmat qilishi mumkin.
            """,
        },
        {
            "title": "Omborni keraksiz bo'shliq qilmang",
            "type": "warning",
            "text": """
            Ombor borligi yetarli emas.

            <br><br>

            Ichida buyumlarga
            kirish mumkin bo'lmasa

            <br><br>

            yoki barcha predmetlar
            bir-birining oldini to'ssa,

            <br><br>

            storage samarali emas.
            """,
        },
        {
            "title": "Pantry",
            "type": "normal",
            "text": """
            Oshxona yaqinidagi
            oziq-ovqat ombori yoki pantry

            <br><br>

            oshxona bilan
            mantiqiy aloqada bo'lishi mumkin.

            <br><br>

            Uning joylashuvi
            kundalik foydalanishga mos
            bo'lishi kerak.
            """,
        },
        {
            "title": "Texnik xona",
            "type": "highlight",
            "text": """
            Texnik xonada
            uyga xizmat qiluvchi
            muhandislik jihozlari
            joylashtirilishi mumkin.

            <br><br>

            Bu xonaga xizmat ko'rsatish
            va nazorat uchun kirish
            imkonini oldindan o'ylash kerak.
            """,
        },
        {
            "title": "Texnik xonani tasodifiy qoldirmang",
            "type": "warning",
            "text": """
            Rejaning oxirida qolgan
            kichik bo'sh joyni

            <br><br>

            avtomatik ravishda
            texnik xona qilish

            <br><br>

            yaxshi usul emas.

            <br><br>

            Texnik funksiyaning
            real ehtiyojlari
            alohida aniqlanadi.
            """,
        },
        {
            "title": "Service circulation",
            "type": "normal",
            "text": """
            Texnik yoki ombor
            funksiyalaridan foydalanish

            <br><br>

            living yoki bedroomning
            asosiy dam olish zonasini
            keraksiz kesib o'tmasligi ma'qul.
            """,
        },
        {
            "title": "Mini-vazifa",
            "type": "example",
            "text": """
            Uy planida
            3 ta yordamchi xona joylashtiring:

            <br><br>

            • pantry;<br>
            • general storage;<br>
            • technical room.

            <br><br>

            Har birini
            unga eng bog'liq
            funksiyaga yaqinlashtiring.
            """,
        },
    ],

    "L02_M10_005": [
        {
            "title": "Yordamchi xonalar auditi",
            "type": "highlight",
            "text": """
            Endi yordamchi xonalarni
            alohida kichik xonalar sifatida emas,

            <br><br>

            butun uy funksional
            tizimining bir qismi sifatida
            tekshiramiz.
            """,
        },
        {
            "title": "1. Garderob",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • foydalanadigan odamga yaqinmi?<br>
            • shkaflardan foydalanish mumkinmi?<br>
            • circulation ochiqmi?<br>
            • kundalik va mavsumiy storage ajratilganmi?
            """,
        },
        {
            "title": "2. Laundry",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • kirlarni olib kelish qulaymi?<br>
            • yuvish jarayoni mantiqiymi?<br>
            • storage bormi?<br>
            • jihoz eshiklari ochiladimi?
            """,
        },
        {
            "title": "3. Ombor",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • buyumlarga kirish mumkinmi?<br>
            • kerakli joyga yaqinmi?<br>
            • ichki storage tartiblimi?<br>
            • keraksiz o'lik zona ko'p emasmi?
            """,
        },
        {
            "title": "4. Texnik xona",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • texnik funksiyaga mosmi?<br>
            • xizmat ko'rsatish uchun kirish bormi?<br>
            • yashash circulationiga xalaqit bermaydimi?
            """,
        },
        {
            "title": "Xatoni toping",
            "type": "warning",
            "text": """
            250 m² uyda
            katta living,
            katta bedrooms
            va katta dining mavjud.

            <br><br>

            Lekin:

            • coat storage yo'q;<br>
            • laundry yo'q;<br>
            • cleaning buyumlari uchun joy yo'q;<br>
            • texnik jihozlar koridorda turibdi.

            <br><br>

            Uy katta,
            lekin kundalik hayot
            yaxshi tashkil qilinmagan.
            """,
        },
        {
            "title": "Professional checklist",
            "type": "example",
            "text": """
            Yordamchi xonalarni tekshiring:

            <br><br>

            <b>1.</b> Kundalik storage yetarlimi?<br><br>
            <b>2.</b> Mavsumiy storage bormi?<br><br>
            <b>3.</b> Garderob mantiqiy joylashganmi?<br><br>
            <b>4.</b> Laundry workflow ishlaydimi?<br><br>
            <b>5.</b> Omborga kirish qulaymi?<br><br>
            <b>6.</b> Texnik xona xizmat ko'rsatishga mosmi?<br><br>
            <b>7.</b> Service circulation asosiy yashash zonasini buzmayaptimi?
            """,
        },
        {
            "title": "LEVEL 2 yakuni",
            "type": "highlight",
            "text": """
            Siz endi turar joyni
            faqat xonalar ro'yxati sifatida emas,

            <br><br>

            odam yashaydigan
            to'liq funksional tizim
            sifatida tahlil qila olasiz.

            <br><br>

            LEVEL 2 davomida siz:

            <br><br>

            ✓ inson ergonomikasini;<br>
            ✓ funksional zonalashni;<br>
            ✓ circulationni;<br>
            ✓ mehmonxonani;<br>
            ✓ oshxonani;<br>
            ✓ yotoqxonani;<br>
            ✓ bolalar xonasini;<br>
            ✓ sanuzelni;<br>
            ✓ entrance va hallwayni;<br>
            ✓ yordamchi xonalarni

            <br><br>

            o'rgandingiz.
            """,
        },
    ],
}


# ============================================================
# QUIZ
# Q136-Q150 KODLARI SAQLANADI
# ============================================================

LEVEL02_MODULE10_QUIZ = {
    "L02_M10_001": [
        {
            "code": "L02_Q136",
            "question": "Yordamchi xonalar uy kundalik foydalanishiga ta'sir qiladimi?",
            "explanation": (
                "Storage, laundry va texnik funksiyalar kundalik hayotni tartibli tashkil qilishga yordam beradi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L02_Q137",
            "question": "Yordamchi xonalar faqat keraksiz qolgan maydonga joylashtirilishi kerakmi?",
            "explanation": (
                "Ularning joylashuvi real funksional ehtiyoj va boshqa xonalar bilan aloqaga qarab belgilanadi."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L02_Q138",
            "question": "Uyda cleaning va mavsumiy buyumlar uchun storage kerak bo'lishi mumkinmi?",
            "explanation": (
                "Kundalik yashashda turli turdagi buyumlar uchun saqlash joyi kerak bo'lishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L02_M10_002": [
        {
            "code": "L02_Q139",
            "question": "Garderob foydalanadigan bedroomga yaqin joylashishi qulay bo'lishi mumkinmi?",
            "explanation": (
                "Funksional yaqinlik kundalik foydalanishni soddalashtirishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L02_Q140",
            "question": "Garderobga ko'p shkaf sig'ishi uning avtomatik ravishda qulay ekanini anglatadimi?",
            "explanation": (
                "Shkaflardan foydalanish va ichki circulation ham tekshirilishi kerak."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L02_Q141",
            "question": "Kundalik va mavsumiy storage'ni alohida o'ylash foydalimi?",
            "explanation": (
                "Turli foydalanish chastotasidagi buyumlarni tartibli joylashtirish mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L02_M10_003": [
        {
            "code": "L02_Q142",
            "question": "Laundry faqat kir yuvish mashinasi uchun joymi?",
            "explanation": (
                "Laundry saralash, yuvish, quritish, yig'ish va storage jarayonlarini ham o'z ichiga olishi mumkin."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L02_Q143",
            "question": "Laundry rejasida jihoz eshigi ochilish zonasini tekshirish kerakmi?",
            "explanation": (
                "Jihozdan foydalanish uchun uning oldida real ish maydoni kerak."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L02_Q144",
            "question": "Laundry uchun storage foydali bo'lishi mumkinmi?",
            "explanation": (
                "Kir vositalari, savatlar va boshqa maishiy buyumlarni saqlash uchun joy kerak bo'lishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L02_M10_004": [
        {
            "code": "L02_Q145",
            "question": "Omborda saqlanayotgan buyumlarga real kirish imkonini tekshirish kerakmi?",
            "explanation": (
                "Buyumlarni faqat joylashtirish emas, ulardan foydalanish ham mumkin bo'lishi kerak."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L02_Q146",
            "question": "Pantryni oshxona bilan funksional bog'lash foydali bo'lishi mumkinmi?",
            "explanation": (
                "Oziq-ovqat saqlash zonasining oshxonaga mantiqan yaqinligi kundalik foydalanishga yordam beradi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L02_Q147",
            "question": "Texnik xona faqat planda qolib ketgan tasodifiy bo'sh joyga joylashtirilishi kerakmi?",
            "explanation": (
                "Texnik makonning real jihozlari, kirish va xizmat ko'rsatish ehtiyojlari alohida tahlil qilinadi."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
    ],

    "L02_M10_005": [
        {
            "code": "L02_Q148",
            "question": "Yordamchi xonalar auditida joylashuv va circulation tekshiriladimi?",
            "explanation": (
                "Yordamchi funksiyalar boshqa xonalarga qulay bog'lanishi va asosiy harakatga xalaqit bermasligi kerak."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L02_Q149",
            "question": "Katta uyda yordamchi xonalar bo'lmasa kundalik foydalanish noqulaylashishi mumkinmi?",
            "explanation": (
                "Storage, laundry va texnik funksiyalarning yo'qligi asosiy yashash xonalarini ortiqcha yuklashi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L02_Q150",
            "question": "Yordamchi xonalarni rejalashtirishdagi to'g'ri yondashuv qaysi?",
            "explanation": (
                "Ehtiyoj aniqlanadi, tegishli joy tanlanadi, storage va circulation tekshiriladi."
            ),
            "options": [
                (
                    "A",
                    "Ehtiyoj → joylashuv → storage/workflow → circulation → audit",
                    True,
                ),
                (
                    "B",
                    "Qolgan bo'sh joyga tasodifiy xonalar qo'shish",
                    False,
                ),
            ],
        },
    ],
}


# ============================================================
# DATABASE SEED
# ============================================================

def seed_level02_module10():
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
        ) in LEVEL02_MODULE10_LESSONS:

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
