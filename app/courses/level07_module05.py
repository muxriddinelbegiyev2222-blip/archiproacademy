from database.database import get_connection


# ============================================================
# LEVEL 7
# MODULE 05 - SCHEDULES
# ============================================================

LEVEL07_MODULE05_LESSONS = [
    (
        "L07_M05",
        "L07_M05_001",
        "Schedules tushunchasi",
        "theory",
        "BIM modeldagi element va xona ma'lumotlarini avtomatik jadvallar orqali boshqarish mantig'ini tushunish.",
        1,
        60,
        20,
    ),
    (
        "L07_M05",
        "L07_M05_002",
        "Criteria va Fields",
        "theory",
        "Schedule'ga qaysi elementlar kirishi va qaysi ma'lumotlar ustunlarda ko'rsatilishini boshqarish.",
        2,
        70,
        20,
    ),
    (
        "L07_M05",
        "L07_M05_003",
        "Sorting, Grouping va hisoblash",
        "practice",
        "Schedule ma'lumotlarini tartiblash, guruhlash va kerakli miqdorlarni tahlil qilish.",
        3,
        70,
        20,
    ),
    (
        "L07_M05",
        "L07_M05_004",
        "Door, Window va Zone Schedules",
        "practice",
        "Eshik, deraza va xonalar bo'yicha amaliy BIM jadvallarini tashkil qilish.",
        4,
        75,
        20,
    ),
    (
        "L07_M05",
        "L07_M05_005",
        "Schedules professional audit",
        "practice",
        "Schedule criteria, fields, model ma'lumotlari va jadval natijalarini kompleks tekshirish.",
        5,
        85,
        25,
    ),
]


# ============================================================
# CONTENT
# ============================================================

LEVEL07_MODULE05_CONTENT = {
    "L07_M05_001": [
        {
            "title": "Schedule nima?",
            "type": "highlight",
            "text": """
            Schedule —
            BIM model ichidagi
            elementlar va ularning
            ma'lumotlarini

            <br><br>

            tartibli jadval
            ko'rinishida chiqarishga
            yordam beradigan vosita.
            """,
        },
        {
            "title": "Oddiy jadvaldan farqi",
            "type": "normal",
            "text": """
            Oddiy qo'lda yozilgan
            jadval modeldan
            mustaqil bo'lishi mumkin.

            <br><br>

            BIM Schedule esa
            model elementlari
            haqidagi ma'lumotlarga
            tayanadi.
            """,
        },
        {
            "title": "Nima uchun muhim?",
            "type": "highlight",
            "text": """
            Schedule yordamida:

            <br><br>

            • elementlarni ro'yxatlash;<br>
            • kerakli parametrlarni ko'rish;<br>
            • miqdorlarni nazorat qilish;<br>
            • xatolarni aniqlash;<br>
            • hujjat tayyorlash

            <br><br>

            osonlashadi.
            """,
        },
        {
            "title": "Tasavvur qiling",
            "type": "example",
            "text": """
            Uy modelida
            25 ta eshik bor.

            <br><br>

            Sizga kerak:

            • eshik turi;<br>
            • o'lchami;<br>
            • ID yoki raqami;<br>
            • boshqa kerakli ma'lumotlar.

            <br><br>

            Har birini qo'lda
            jadvalga yozish o'rniga,

            <br><br>

            Schedule modeldagi
            ma'lumotlarni yig'ishga
            yordam beradi.
            """,
        },
        {
            "title": "Schedule modeli o'qiydi",
            "type": "normal",
            "text": """
            Schedule natijasining
            sifati modeldagi
            ma'lumot sifatiga bog'liq.

            <br><br>

            Modelda parametr
            noto'g'ri bo'lsa,

            <br><br>

            jadval ham noto'g'ri
            ma'lumot ko'rsatishi mumkin.
            """,
        },
        {
            "title": "Schedule — audit vositasi",
            "type": "highlight",
            "text": """
            Schedule faqat
            yakuniy spetsifikatsiya emas.

            <br><br>

            U modelni
            tekshirish uchun
            juda kuchli
            BIM audit vositasi ham.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Bitta kichik uy
            modelini tasavvur qiling.

            <br><br>

            Qaysi 3 ta jadval
            sizga foydali bo'lishini
            yozing.

            <br><br>

            Masalan:

            • Door Schedule;<br>
            • Window Schedule;<br>
            • Room Schedule.
            """,
        },
    ],

    "L07_M05_002": [
        {
            "title": "Criteria nima?",
            "type": "highlight",
            "text": """
            Criteria —
            Schedule ichiga
            qaysi elementlar
            kirishini aniqlaydigan
            shartlar tizimi.
            """,
        },
        {
            "title": "Misol",
            "type": "example",
            "text": """
            Door Schedule
            yaratmoqchisiz.

            <br><br>

            Criteria
            aynan eshik
            elementlarini tanlashga
            yordam beradi.

            <br><br>

            Keraksiz boshqa
            elementlar jadvalga
            tushmasligi kerak.
            """,
        },
        {
            "title": "Criteria juda keng bo'lsa",
            "type": "warning",
            "text": """
            Criteria noto'g'ri
            tuzilsa,

            <br><br>

            Schedule ichiga
            kerak bo'lmagan
            elementlar ham
            kirib qolishi mumkin.
            """,
        },
        {
            "title": "Criteria juda tor bo'lsa",
            "type": "warning",
            "text": """
            Criteria haddan
            tashqari tor bo'lsa,

            <br><br>

            kerakli ayrim
            elementlar jadvaldan
            tashqarida qolishi mumkin.
            """,
        },
        {
            "title": "Fields nima?",
            "type": "highlight",
            "text": """
            Fields —
            Schedule ustunlarida
            qaysi ma'lumotlar
            ko'rsatilishini
            belgilaydi.
            """,
        },
        {
            "title": "Door Schedule Fields",
            "type": "example",
            "text": """
            Eshik jadvalida
            loyiha maqsadiga qarab:

            <br><br>

            • ID;<br>
            • turi;<br>
            • o'lchami;<br>
            • joylashuvga oid ma'lumot;<br>
            • boshqa kerakli parametrlar

            <br><br>

            ko'rsatilishi mumkin.
            """,
        },
        {
            "title": "Keraksiz ustunlar",
            "type": "warning",
            "text": """
            Schedule'ga
            barcha mavjud
            parametrlarni chiqarish

            <br><br>

            uni professional
            qilmaydi.

            <br><br>

            Faqat jadval maqsadi
            uchun kerakli
            Fields tanlang.
            """,
        },
        {
            "title": "Criteria va Fields farqi",
            "type": "highlight",
            "text": """
            Esda tuting:

            <br><br>

            <b>Criteria</b> —
            qaysi elementlar?

            <br><br>

            <b>Fields</b> —
            ular haqida
            qaysi ma'lumotlar?
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Window Schedule uchun:

            <br><br>

            1. Criteria yozing.<br>
            2. Kamida 5 ta Field tanlang.<br>
            3. Har bir Field nima uchun kerakligini tushuntiring.
            """,
        },
    ],

    "L07_M05_003": [
        {
            "title": "Sorting",
            "type": "highlight",
            "text": """
            Sorting —
            Schedule'dagi
            ma'lumotlarni

            <br><br>

            ma'lum tartibda
            joylashtirish.
            """,
        },
        {
            "title": "Nega tartib kerak?",
            "type": "normal",
            "text": """
            50 ta element
            tasodifiy ketma-ketlikda
            tursa,

            <br><br>

            jadvalni tushunish
            qiyinlashadi.

            <br><br>

            Tartibli jadval
            auditni ham
            osonlashtiradi.
            """,
        },
        {
            "title": "Grouping",
            "type": "highlight",
            "text": """
            Grouping —
            o'xshash elementlarni
            ma'lum mantiq asosida
            guruhlash.
            """,
        },
        {
            "title": "Tasavvur qiling",
            "type": "example",
            "text": """
            Modelda 20 ta
            bir xil turdagi
            deraza bor.

            <br><br>

            Har birini alohida
            qatorda ko'rsatish
            kerak bo'lishi mumkin,

            <br><br>

            yoki loyiha maqsadiga qarab
            ularni tur bo'yicha
            guruhlab tahlil qilish
            foydali bo'lishi mumkin.
            """,
        },
        {
            "title": "Miqdor",
            "type": "normal",
            "text": """
            Schedule elementlarning
            miqdorini nazorat qilishda
            yordam berishi mumkin.

            <br><br>

            Lekin natija
            faqat model
            to'g'ri bo'lsa
            ishonchli bo'ladi.
            """,
        },
        {
            "title": "Dublikat muammosi",
            "type": "warning",
            "text": """
            Modelda tasodifan
            ikki marta qo'yilgan
            element

            <br><br>

            Schedule'da ham
            ortiqcha miqdor
            sifatida chiqishi mumkin.

            <br><br>

            Shuning uchun
            Schedule modelni
            audit qilishda
            juda foydali.
            """,
        },
        {
            "title": "Bir xil nom, boshqa parametr",
            "type": "example",
            "text": """
            Ikki elementning
            nomi bir xil,

            <br><br>

            lekin o'lchami
            boshqacha bo'lishi mumkin.

            <br><br>

            Schedule bunday
            farqlarni ko'rishga
            yordam beradi.
            """,
        },
        {
            "title": "Hisoblashga ehtiyotkorlik",
            "type": "warning",
            "text": """
            Schedule ko'rsatgan
            son yoki miqdorni

            <br><br>

            avtomatik ravishda
            qurilish smetasi
            deb qabul qilmang.

            <br><br>

            Miqdor,
            loyiha ma'lumoti
            va iqtisodiy hisob
            turli vazifalar.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            10 ta eshikdan iborat
            jadval tasavvur qiling.

            <br><br>

            Ularni:

            • turi;<br>
            • ID;<br>
            • o'lchami

            <br><br>

            bo'yicha qanday
            tartiblash foydali
            bo'lishini belgilang.
            """,
        },
    ],

    "L07_M05_004": [
        {
            "title": "Door Schedule",
            "type": "highlight",
            "text": """
            Door Schedule —
            loyihadagi eshiklar
            haqidagi ma'lumotlarni

            <br><br>

            tartibli nazorat
            qilishga yordam beradi.
            """,
        },
        {
            "title": "Eshiklarni audit qilish",
            "type": "normal",
            "text": """
            Door Schedule orqali
            quyidagi muammolarni
            ko'rish osonlashishi mumkin:

            <br><br>

            • ID takrorlanishi;<br>
            • noto'g'ri tur;<br>
            • noodatiy o'lcham;<br>
            • ma'lumot yetishmasligi.
            """,
        },
        {
            "title": "Window Schedule",
            "type": "highlight",
            "text": """
            Window Schedule
            derazalarni

            <br><br>

            tur,
            o'lcham,
            identifikatsiya
            va boshqa kerakli
            parametrlar bo'yicha
            nazorat qilishga
            yordam beradi.
            """,
        },
        {
            "title": "Zone Schedule",
            "type": "highlight",
            "text": """
            Zone Schedule
            xonalar haqidagi
            BIM ma'lumotlarini

            <br><br>

            jadval ko'rinishida
            tahlil qilishga
            yordam beradi.
            """,
        },
        {
            "title": "Room data",
            "type": "normal",
            "text": """
            Zone Schedule'da
            loyiha talabiga qarab:

            <br><br>

            • xona nomi;<br>
            • xona raqami;<br>
            • maydon;<br>
            • kategoriya;<br>
            • boshqa parametrlar

            <br><br>

            chiqarilishi mumkin.
            """,
        },
        {
            "title": "Area audit",
            "type": "example",
            "text": """
            Room Schedule
            orqali barcha
            xona maydonlarini
            bir joyda ko'rish mumkin.

            <br><br>

            Bu rejalashtirishdagi
            noodatiy katta
            yoki kichik xonalarni
            aniqlashga yordam beradi.
            """,
        },
        {
            "title": "Model bilan aloqa",
            "type": "warning",
            "text": """
            Jadvaldagi noto'g'ri
            xona maydonini

            <br><br>

            shunchaki yozuv sifatida
            tuzatishdan oldin

            <br><br>

            muammo modelda
            yoki Zone chegarasida
            emasligini tekshiring.
            """,
        },
        {
            "title": "Bitta loyiha — bir nechta Schedule",
            "type": "normal",
            "text": """
            Professional loyihada
            vazifaga qarab
            bir nechta jadvallar
            bo'lishi mumkin.

            <br><br>

            Masalan:

            • Door Schedule;<br>
            • Window Schedule;<br>
            • Room Schedule;<br>
            • boshqa element schedules.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Kichik uy loyihasi uchun
            3 ta jadval rejalashtiring:

            <br><br>

            1. Door Schedule<br>
            2. Window Schedule<br>
            3. Zone Schedule

            <br><br>

            Har birida
            kamida 5 ta Field
            bo'lishini yozing.
            """,
        },
    ],

    "L07_M05_005": [
        {
            "title": "Schedules professional audit",
            "type": "highlight",
            "text": """
            Schedule auditini
            quyidagi zanjirda
            bajaramiz:

            <br><br>

            Model
            → Criteria
            → Fields
            → Sorting
            → Schedule
            → Audit
            """,
        },
        {
            "title": "1. Criteria audit",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • kerakli elementlar jadvalga tushganmi?<br>
            • ortiqcha elementlar yo'qmi?<br>
            • kerakli elementlar tashqarida qolmaganmi?
            """,
        },
        {
            "title": "2. Fields audit",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • kerakli ustunlar bormi?<br>
            • muhim ma'lumot yetishmayaptimi?<br>
            • keraksiz ustunlar haddan tashqari ko'p emasmi?
            """,
        },
        {
            "title": "3. Ma'lumot sifati",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • bo'sh qiymatlar bormi?<br>
            • noto'g'ri ID bormi?<br>
            • bir xil elementlarda turli naming ishlatilganmi?<br>
            • kerakli BIM parametrlar to'ldirilganmi?
            """,
        },
        {
            "title": "4. Sorting va Grouping",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • jadval mantiqiy tartibdami?<br>
            • o'xshash elementlar boshqariladimi?<br>
            • foydalanuvchi kerakli ma'lumotni tez topa oladimi?
            """,
        },
        {
            "title": "5. Miqdor audit",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • sonlar mantiqiymi?<br>
            • tasodifiy dublikat element yo'qmi?<br>
            • modelda yetishmayotgan element bo'lishi mumkinmi?
            """,
        },
        {
            "title": "6. Modelga qayting",
            "type": "highlight",
            "text": """
            Schedule'dagi xato
            ko'pincha

            <br><br>

            jadvalning o'zida emas,
            model ma'lumotida
            bo'lishi mumkin.

            <br><br>

            Muammo manbasini
            toping.
            """,
        },
        {
            "title": "Xatoni toping",
            "type": "warning",
            "text": """
            Door Schedule tayyor.

            <br><br>

            Lekin:

            • 2 ta eshikning ID'si bir xil;<br>
            • 3 ta eshikda o'lcham ma'lumoti noto'g'ri;<br>
            • 1 ta eshik jadvalga umuman tushmagan;<br>
            • bir xil turdagi eshiklar turli nomlangan;<br>
            • bitta tasodifiy dublikat eshik modelda qolgan.

            <br><br>

            Schedule muammoni
            yaratmadi.

            <br><br>

            Schedule modeldagi
            muammolarni ko'rsatdi.
            """,
        },
        {
            "title": "Professional checklist",
            "type": "example",
            "text": """
            Schedule'ni tekshiring:

            <br><br>

            <b>1.</b> Maqsadi aniqmi?<br><br>
            <b>2.</b> Criteria to'g'rimi?<br><br>
            <b>3.</b> Fields yetarlimi?<br><br>
            <b>4.</b> Naming izchilmi?<br><br>
            <b>5.</b> Sorting tushunarlimi?<br><br>
            <b>6.</b> Miqdorlar mantiqiymi?<br><br>
            <b>7.</b> Bo'sh yoki noto'g'ri ma'lumot bormi?<br><br>
            <b>8.</b> Xato aniqlansa model ham tekshirildimi?
            """,
        },
        {
            "title": "Modul yakuni",
            "type": "highlight",
            "text": """
            Siz endi:

            <br><br>

            ✓ Schedule mantig'ini tushunasiz;<br>
            ✓ Criteria va Fields farqini bilasiz;<br>
            ✓ Sorting va Grouping'dan foydalanasiz;<br>
            ✓ Door Schedule tuzasiz;<br>
            ✓ Window Schedule tuzasiz;<br>
            ✓ Zone Schedule tuzasiz;<br>
            ✓ Schedule orqali BIM modelni audit qilasiz.

            <br><br>

            Keyingi modul:
            <b>Properties.</b>
            """,
        },
    ],
}


# ============================================================
# QUIZ
# Q061-Q075
# ============================================================

LEVEL07_MODULE05_QUIZ = {
    "L07_M05_001": [
        {
            "code": "L07_Q061",
            "question": "Schedule BIM modeldagi element ma'lumotlarini jadval ko'rinishida boshqarishga yordam beradimi?",
            "explanation": (
                "Schedule modeldagi element va parametrlarni tartibli jadvalda ko'rish va tahlil qilishga yordam beradi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L07_Q062",
            "question": "BIM Schedule oddiy qo'lda yozilgan, modeldan uzilgan jadval bilan aynan bir xilmi?",
            "explanation": (
                "BIM Schedule model elementlari va ularning ma'lumotlariga tayanadi."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L07_Q063",
            "question": "Schedule model auditida ham foydalanilishi mumkinmi?",
            "explanation": (
                "Jadvaldagi noodatiy yoki yetishmayotgan ma'lumot modeldagi xatolarni aniqlashga yordam beradi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L07_M05_002": [
        {
            "code": "L07_Q064",
            "question": "Criteria Schedule'ga qaysi elementlar kirishini belgilashga yordam beradimi?",
            "explanation": (
                "Criteria kerakli elementlarni shartlar asosida tanlaydi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L07_Q065",
            "question": "Fields Schedule ustunlarida qaysi ma'lumotlar ko'rsatilishini belgilaydimi?",
            "explanation": (
                "Fields elementlar haqidagi kerakli parametrlarni jadval ustunlariga chiqaradi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L07_Q066",
            "question": "Criteria va Fields aynan bir xil vazifani bajaradimi?",
            "explanation": (
                "Criteria qaysi elementlarni tanlaydi, Fields esa ular haqida qaysi ma'lumot ko'rsatilishini belgilaydi."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
    ],

    "L07_M05_003": [
        {
            "code": "L07_Q067",
            "question": "Sorting Schedule ma'lumotlarini mantiqiy tartibga keltirishga yordam beradimi?",
            "explanation": (
                "Sorting jadvalni o'qish va tekshirishni osonlashtiradi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L07_Q068",
            "question": "Modeldagi dublikat element Schedule miqdoriga ta'sir qilishi mumkinmi?",
            "explanation": (
                "Modeldagi ortiqcha element jadvalda ham ortiqcha element yoki miqdor sifatida ko'rinishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L07_Q069",
            "question": "Schedule'dagi har qanday miqdorni tekshirmasdan yakuniy qurilish smetasi sifatida qabul qilish kerakmi?",
            "explanation": (
                "Schedule BIM miqdorlarini ko'rsatishi mumkin, ammo smeta alohida metodologiya va tekshiruvni talab qiladi."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
    ],

    "L07_M05_004": [
        {
            "code": "L07_Q070",
            "question": "Door Schedule eshik ID va boshqa parametrlarni nazorat qilishga yordam berishi mumkinmi?",
            "explanation": (
                "Door Schedule eshiklar haqidagi kerakli BIM ma'lumotlarini bir joyda tahlil qilish imkonini beradi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L07_Q071",
            "question": "Zone Schedule xona nomlari va maydonlarini tahlil qilishda foydalanilishi mumkinmi?",
            "explanation": (
                "Zone ma'lumotlari xona jadvalida ko'rsatilishi va tekshirilishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L07_Q072",
            "question": "Schedule'da xona maydoni noto'g'ri ko'rinsa faqat jadval yozuvini o'zgartirish yetarlimi?",
            "explanation": (
                "Muammo Zone chegarasi yoki model ma'lumotida bo'lishi mumkin, shuning uchun manba tekshirilishi kerak."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
    ],

    "L07_M05_005": [
        {
            "code": "L07_Q073",
            "question": "Schedule auditida Criteria, Fields va model ma'lumotlari tekshiriladimi?",
            "explanation": (
                "Professional audit jadvalning tanlov mezonlari, ustunlari va modeldan kelgan ma'lumot sifatini tekshiradi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L07_Q074",
            "question": "Schedule'dagi xato har doim Schedule vositasining o'zidan kelib chiqadimi?",
            "explanation": (
                "Ko'p holatda jadval modeldagi noto'g'ri yoki yetishmayotgan BIM ma'lumotni shunchaki ko'rsatadi."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L07_Q075",
            "question": "Schedules bilan professional ishlashdagi to'g'ri workflow qaysi?",
            "explanation": (
                "Avval jadval maqsadi aniqlanadi, Criteria va Fields tuziladi, ma'lumot tartiblanadi va natija model bilan birga audit qilinadi."
            ),
            "options": [
                (
                    "A",
                    "Maqsad → Criteria → Fields → Sorting/Grouping → Schedule → model audit",
                    True,
                ),
                (
                    "B",
                    "Tasodifiy jadval → barcha parametrlarni chiqarish → natijani tekshirmaslik",
                    False,
                ),
            ],
        },
    ],
}


# ============================================================
# DATABASE SEED
# ============================================================

def seed_level07_module05():
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
        ) in LEVEL07_MODULE05_LESSONS:

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
