from database.database import get_connection


# ============================================================
# LEVEL 8
# MODULE 09 - KONSTRUKTOR BILAN ISHLASH
# ============================================================

LEVEL08_MODULE09_LESSONS = [
    (
        "L08_M09",
        "L08_M09_001",
        "Arxitektor va konstruktor roli",
        "theory",
        "Arxitektor va konstruktorning vazifalari, javobgarligi va hamkorlik chegaralarini tushunish.",
        1,
        30,
        20,
    ),
    (
        "L08_M09",
        "L08_M09_002",
        "Konstruktorga ma'lumot tayyorlash",
        "theory",
        "Konstruktor ishlashi uchun kerak bo'ladigan plan, kesim, o'qlar, sathlar va loyiha ma'lumotlarini tartibli tayyorlash.",
        2,
        35,
        20,
    ),
    (
        "L08_M09",
        "L08_M09_003",
        "Koordinatsiya va savol-javob workflow",
        "practice",
        "Konstruktiv savollarni aniq shakllantirish, javoblarni loyiha qarorlariga kiritish va ochiq masalalarni boshqarish.",
        3,
        35,
        20,
    ),
    (
        "L08_M09",
        "L08_M09_004",
        "O'zgarishlar va versiyalarni boshqarish",
        "practice",
        "Arxitektura va konstruktiv o'zgarishlarni versiyalar, model va chizmalar orqali nazorat qilish.",
        4,
        40,
        20,
    ),
    (
        "L08_M09",
        "L08_M09_005",
        "Arxitektura-konstruktsiya professional audit",
        "practice",
        "Arxitektura va konstruktor modeli o'rtasidagi asosiy koordinatsiya nuqtalarini kompleks tekshirish.",
        5,
        40,
        25,
    ),
]


# ============================================================
# CONTENT
# ============================================================

LEVEL08_MODULE09_CONTENT = {
    "L08_M09_001": [
        {
            "title": "Arxitektor va konstruktor",
            "type": "highlight",
            "text": """
            Arxitektor va
            konstruktor

            <br><br>

            bitta loyiha ustida
            ishlaydi,

            <br><br>

            lekin ularning
            vazifalari bir xil emas.
            """,
        },
        {
            "title": "Arxitektorning vazifasi",
            "type": "normal",
            "text": """
            Arxitektor:

            <br><br>

            • funksional reja;<br>
            • fazoviy yechim;<br>
            • fasad;<br>
            • bino shakli;<br>
            • foydalanish qulayligi;<br>
            • loyiha koordinatsiyasi

            <br><br>

            bilan ishlaydi.
            """,
        },
        {
            "title": "Konstruktorning vazifasi",
            "type": "normal",
            "text": """
            Konstruktor:

            <br><br>

            • yuk ko'taruvchi tizim;<br>
            • elementlar hisoblari;<br>
            • kesimlar;<br>
            • armatura;<br>
            • konstruktiv barqarorlik

            <br><br>

            bilan ishlaydi.
            """,
        },
        {
            "title": "Bir-birining o'rnini bosmaydi",
            "type": "warning",
            "text": """
            Arxitektor
            konstruktiv hisobni

            <br><br>

            taxmin bilan
            bajarmaydi.

            <br><br>

            Konstruktor esa
            arxitektura funksiyasini

            <br><br>

            mustaqil ravishda
            o'zgartirmasligi kerak.
            """,
        },
        {
            "title": "Hamkorlik",
            "type": "highlight",
            "text": """
            Kuchli loyiha:

            <br><br>

            Arxitektura
            +
            Konstruktsiya
            +
            MEP

            <br><br>

            koordinatsiyada
            ishlaganda yuzaga keladi.
            """,
        },
        {
            "title": "Tasavvur qiling",
            "type": "example",
            "text": """
            Arxitektor
            katta ochiq
            mehmonxona xohladi.

            <br><br>

            Konstruktor esa
            tayanch kerakligini
            aytdi.

            <br><br>

            Professional yechim —
            bir tomonning
            ikkinchisiga buyruq berishi
            emas,

            <br><br>

            balki ikkala talabni
            uyg'unlashtirish.
            """,
        },
        {
            "title": "Savol berish madaniyati",
            "type": "normal",
            "text": """
            “Bu bo'lmaydi”
            yoki
            “shunaqa qiling”

            <br><br>

            degan gapning o'zi
            yetarli emas.

            <br><br>

            Sabab,
            cheklov
            va alternativlar
            tushuniladi.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Ikki ustun yozing:

            <br><br>

            1. Arxitektor qarorlari.<br>
            2. Konstruktor qarorlari.

            <br><br>

            So'ng ular
            kesishadigan 5 ta
            koordinatsiya nuqtasini
            yozing.
            """,
        },
    ],

    "L08_M09_002": [
        {
            "title": "Konstruktorga nima beriladi?",
            "type": "highlight",
            "text": """
            Konstruktor
            taxmin bilan emas,

            <br><br>

            aniq loyiha
            ma'lumotlari bilan
            ishlashi kerak.
            """,
        },
        {
            "title": "Asosiy planlar",
            "type": "normal",
            "text": """
            Konstruktor uchun
            odatda muhim:

            <br><br>

            • qavat planlari;<br>
            • tom plani;<br>
            • fundament bilan bog'liq ma'lumotlar;<br>
            • kerakli kesimlar.
            """,
        },
        {
            "title": "O'qlar",
            "type": "highlight",
            "text": """
            Arxitektura va
            konstruktor bir xil

            <br><br>

            grid va o'qlar
            mantig'ida ishlashi

            <br><br>

            koordinatsiyani
            ancha osonlashtiradi.
            """,
        },
        {
            "title": "Sathlar",
            "type": "normal",
            "text": """
            Qavat balandliklari,
            asosiy level'lar
            va 0.000

            <br><br>

            ikkala loyiha
            uchun bir xil
            tushunilishi kerak.
            """,
        },
        {
            "title": "Ochilishlar",
            "type": "normal",
            "text": """
            Katta:

            <br><br>

            • derazalar;<br>
            • eshiklar;<br>
            • stair openings;<br>
            • shaftlar;<br>
            • fasad ochilishlari

            <br><br>

            konstruktor uchun
            muhim ma'lumot.
            """,
        },
        {
            "title": "Faqat PDF yetmasligi mumkin",
            "type": "warning",
            "text": """
            Murakkab loyihada
            faqat bitta

            <br><br>

            eski PDF yuborish
            yetarli bo'lmasligi mumkin.

            <br><br>

            Konstruktor
            qaysi versiya
            eng oxirgi ekanini
            bilishi kerak.
            """,
        },
        {
            "title": "Loyiha statusi",
            "type": "normal",
            "text": """
            Yuborilayotgan
            materialga:

            <br><br>

            • sana;<br>
            • versiya;<br>
            • o'zgarishlar;<br>
            • ochiq savollar

            <br><br>

            biriktirilsa,
            koordinatsiya
            ancha tushunarli bo'ladi.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Konstruktor uchun
            loyiha paketi
            tayyorlang deb tasavvur qiling.

            <br><br>

            Kamida 8 ta
            kerakli ma'lumot
            ro'yxatini yozing.
            """,
        },
    ],

    "L08_M09_003": [
        {
            "title": "Aniq savol",
            "type": "highlight",
            "text": """
            Professional
            koordinatsiyada

            <br><br>

            savol qisqa,
            aniq
            va tekshiriladigan
            bo'lishi kerak.
            """,
        },
        {
            "title": "Yomon savol",
            "type": "warning",
            "text": """
            “Bu joyni
            nima qilamiz?”

            <br><br>

            degan savol
            juda umumiy.
            """,
        },
        {
            "title": "Yaxshi savol",
            "type": "example",
            "text": """
            Masalan:

            <br><br>

            “A-3 o'q kesishmasidagi
            ustunni

            <br><br>

            eshik o'tishidan
            chetga siljitish
            imkoniyati bormi?

            <br><br>

            Arxitektura variantlari:
            1 yoki 2.”
            """,
        },
        {
            "title": "Issue tushunchasi",
            "type": "normal",
            "text": """
            Ochiq masalalar
            alohida

            <br><br>

            issue yoki
            savol sifatida
            boshqarilishi mumkin.
            """,
        },
        {
            "title": "Issue tarkibi",
            "type": "highlight",
            "text": """
            Yaxshi issue'da:

            <br><br>

            • joylashuv;<br>
            • muammo;<br>
            • sabab;<br>
            • rasm yoki view;<br>
            • taklif;<br>
            • mas'ul;<br>
            • status

            <br><br>

            bo'lishi mumkin.
            """,
        },
        {
            "title": "Javobni modelga kiritish",
            "type": "warning",
            "text": """
            Konstruktor javob
            berdi,

            <br><br>

            lekin arxitektura
            modeli yangilanmadi.

            <br><br>

            Bunda koordinatsiya
            hali tugamagan.
            """,
        },
        {
            "title": "Status",
            "type": "normal",
            "text": """
            Ochiq masala
            holati:

            <br><br>

            • open;<br>
            • in review;<br>
            • resolved

            <br><br>

            kabi mantiqda
            boshqarilishi mumkin.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Quyidagi muammo uchun
            professional issue yozing:

            <br><br>

            “Ustun eshik
            o'tishiga tushib qolgan.”

            <br><br>

            Joy,
            muammo,
            taklif
            va kerakli javobni
            ko'rsating.
            """,
        },
    ],

    "L08_M09_004": [
        {
            "title": "Eng xavfli holat",
            "type": "highlight",
            "text": """
            Arxitektor
            bir versiya bilan,

            <br><br>

            konstruktor esa
            boshqa versiya bilan
            ishlashi

            <br><br>

            katta koordinatsiya
            xatosiga olib kelishi mumkin.
            """,
        },
        {
            "title": "Versiya nima?",
            "type": "normal",
            "text": """
            Versiya —
            loyiha ma'lumotining

            <br><br>

            ma'lum vaqtga
            tegishli holati.
            """,
        },
        {
            "title": "O'zgarishlar ro'yxati",
            "type": "normal",
            "text": """
            Yangi versiya
            yuborilganda

            <br><br>

            nima o'zgargani
            aniq ko'rsatilishi
            kerak.
            """,
        },
        {
            "title": "Kritik o'zgarishlar",
            "type": "warning",
            "text": """
            Ayniqsa:

            <br><br>

            • ustun ko'chishi;<br>
            • konstruktiv devor o'zgarishi;<br>
            • katta opening;<br>
            • qavat balandligi;<br>
            • tom shakli;<br>
            • balkon/konsol

            <br><br>

            kabi o'zgarishlar
            konstruktor uchun
            muhim.
            """,
        },
        {
            "title": "Eski fayl xavfi",
            "type": "warning",
            "text": """
            Eski model
            yoki chizma

            <br><br>

            “FINAL”
            deb nomlangan bo'lsa ham

            <br><br>

            uning haqiqatan
            oxirgi versiya
            ekanligi kafolatlanmaydi.
            """,
        },
        {
            "title": "Naming",
            "type": "highlight",
            "text": """
            Fayl nomlari
            aniq va izchil
            bo'lishi kerak.

            <br><br>

            Masalan:

            PROJECT_A_ARC_V03

            <br><br>

            kabi versiya
            mantig'i ishlatilishi mumkin.
            """,
        },
        {
            "title": "Change log",
            "type": "normal",
            "text": """
            Change log
            o'zgarishlarni

            <br><br>

            qisqa tarix
            ko'rinishida
            saqlashga yordam beradi.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            V01 dan V02 ga
            loyiha o'zgardi.

            <br><br>

            Change log yozing:

            <br><br>

            • 2 ustun siljidi;<br>
            • stair opening kattalashdi;<br>
            • balkon qisqardi;<br>
            • tom ridge o'zgardi.
            """,
        },
    ],

    "L08_M09_005": [
        {
            "title": "Professional koordinatsiya auditi",
            "type": "highlight",
            "text": """
            Audit zanjiri:

            <br><br>

            Versiya
            → O'qlar
            → Sathlar
            → Tayanchlar
            → Openings
            → Konstruktsiya
            → MEP
            → Issue status
            """,
        },
        {
            "title": "1. Versiya",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • arxitektor oxirgi versiyadami?<br>
            • konstruktor oxirgi versiyadami?<br>
            • sana va versiya tushunarlimi?
            """,
        },
        {
            "title": "2. O'qlar",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • grid bir xilmi?<br>
            • o'q nomlari mosmi?<br>
            • ustun markazlari bir joydami?
            """,
        },
        {
            "title": "3. Sathlar",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • 0.000 bir xilmi?<br>
            • qavat balandliklari mosmi?<br>
            • slab level'lar mosmi?
            """,
        },
        {
            "title": "4. Ustun va devorlar",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • ustunlar joyi mosmi?<br>
            • konstruktiv devorlar mosmi?<br>
            • qavatlararo uzluksizlik saqlanganmi?
            """,
        },
        {
            "title": "5. Openings",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • stair opening;<br>
            • shaft;<br>
            • katta eshik va deraza;<br>
            • tom openings

            <br><br>

            ikki modelda ham
            mosmi?
            """,
        },
        {
            "title": "6. Fundament",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • tayanchlar fundament bilan mosmi?<br>
            • grid bir xilmi?<br>
            • yangi ustun eski fundamentga tushmaganmi?
            """,
        },
        {
            "title": "7. MEP",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • shaftlar mosmi?<br>
            • rigel bilan duct konflikt qilmayaptimi?<br>
            • penetratsiyalar kelishilganmi?
            """,
        },
        {
            "title": "8. Issue status",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • ochiq savollar nechta?<br>
            • kim javobgar?<br>
            • qaysi savol hal bo'lgan?<br>
            • modelga kiritilganmi?
            """,
        },
        {
            "title": "Xatoni toping",
            "type": "warning",
            "text": """
            Loyihada:

            <br><br>

            • arxitektor V05 bilan ishlayapti;<br>
            • konstruktor V03 bilan ishlayapti;<br>
            • bitta ustun joyi farq qiladi;<br>
            • stair opening konstruktiv modelda eski;<br>
            • yangi balcony konstruktor modelida yo'q;<br>
            • 4 ta issue javobsiz qolgan.

            <br><br>

            Bu loyiha
            koordinatsiya
            auditiga qaytariladi.
            """,
        },
        {
            "title": "Professional checklist",
            "type": "example",
            "text": """
            Arxitektura-konstruktsiya
            audit checklist:

            <br><br>

            <b>1.</b> Oxirgi versiyalar bir xilmi?<br><br>
            <b>2.</b> Grid va o'qlar mosmi?<br><br>
            <b>3.</b> Sathlar mosmi?<br><br>
            <b>4.</b> Ustun va devorlar mosmi?<br><br>
            <b>5.</b> Openings koordinatsiya qilinganmi?<br><br>
            <b>6.</b> Fundament bilan moslik bormi?<br><br>
            <b>7.</b> Tom va balkon o'zgarishlari kelishilganmi?<br><br>
            <b>8.</b> MEP konfliktlari tekshirilganmi?<br><br>
            <b>9.</b> Ochiq issue'lar nazoratdami?<br><br>
            <b>10.</b> Hal qilingan qarorlar modelga kiritilganmi?
            """,
        },
        {
            "title": "LEVEL 8 yakuni",
            "type": "highlight",
            "text": """
            LEVEL 8 davomida siz:

            <br><br>

            ✓ fundament mantig'ini;<br>
            ✓ devor konstruksiyasini;<br>
            ✓ karkas tizimini;<br>
            ✓ plitalarni;<br>
            ✓ tom konstruksiyasini;<br>
            ✓ gidroizolyatsiyani;<br>
            ✓ issiqlik izolyatsiyasini;<br>
            ✓ seysmika asoslarini;<br>
            ✓ konstruktor bilan professional ishlashni

            <br><br>

            o'rgandingiz.

            <br><br>

            Endi LEVEL 8
            final imtihoniga
            tayyorsiz.
            """,
        },
    ],
}


# ============================================================
# QUIZ
# Q121-Q135
# ============================================================

LEVEL08_MODULE09_QUIZ = {
    "L08_M09_001": [
        {
            "code": "L08_Q121",
            "question": "Arxitektor va konstruktorning vazifalari bir xilmi?",
            "explanation": (
                "Ular bitta loyiha ustida ishlaydi, lekin arxitektura va konstruktiv javobgarliklari farq qiladi."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L08_Q122",
            "question": "Arxitektor konstruktiv hisobni taxmin bilan konstruktor o'rniga bajarishi kerakmi?",
            "explanation": (
                "Aniq konstruktiv hisob konstruktor va tegishli me'yorlar asosida amalga oshiriladi."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L08_Q123",
            "question": "Kuchli loyiha arxitektura, konstruktsiya va MEP koordinatsiyasini talab qiladimi?",
            "explanation": (
                "Tizimlar bir-biriga ta'sir qilgani uchun ular o'zaro koordinatsiyada rivojlantiriladi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L08_M09_002": [
        {
            "code": "L08_Q124",
            "question": "Konstruktor uchun qavat planlari, o'qlar va sathlar muhim ma'lumotmi?",
            "explanation": (
                "Konstruktiv model arxitektura geometriyasi, grid va sathlar bilan koordinatsiyada ishlaydi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L08_Q125",
            "question": "Konstruktor qaysi fayl eng oxirgi versiya ekanini bilishi kerakmi?",
            "explanation": (
                "Versiya nazorati eski ma'lumot asosida ishlash xavfini kamaytiradi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L08_Q126",
            "question": "Katta openings va stair opening konstruktor uchun ahamiyatsizmi?",
            "explanation": (
                "Ochilishlar plita, devor va boshqa konstruktiv elementlarga ta'sir qilishi mumkin."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
    ],

    "L08_M09_003": [
        {
            "code": "L08_Q127",
            "question": "Professional koordinatsiya savoli aniq joylashuv va muammoni ko'rsatishi kerakmi?",
            "explanation": (
                "Aniq savol konstruktorning muammoni tez va to'g'ri tushunishiga yordam beradi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L08_Q128",
            "question": "Konstruktor javob bergach arxitektura modelini yangilash shart emasmi?",
            "explanation": (
                "Qaror modelga kiritilmaguncha koordinatsiya amalda yakunlanmagan bo'ladi."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L08_Q129",
            "question": "Issue'larda mas'ul va statusni ko'rsatish foydalimi?",
            "explanation": (
                "Bu ochiq masalalarni kim hal qilishi va qaysi bosqichda ekanini kuzatishga yordam beradi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L08_M09_004": [
        {
            "code": "L08_Q130",
            "question": "Arxitektor va konstruktor turli loyiha versiyalari bilan ishlasa koordinatsiya xatosi yuzaga kelishi mumkinmi?",
            "explanation": (
                "Eski va yangi geometriya o'rtasidagi farqlar konstruktiv va arxitektura konfliktlarini keltirib chiqarishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L08_Q131",
            "question": "Ustun ko'chishi va katta opening kabi o'zgarishlar konstruktorga alohida bildirilishi kerakmi?",
            "explanation": (
                "Bunday o'zgarishlar konstruktiv sxema va hisobga ta'sir qilishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L08_Q132",
            "question": "Fayl nomida FINAL yozuvi bo'lsa u avtomatik ravishda eng yangi versiya hisoblanadimi?",
            "explanation": (
                "Versiya aniq boshqarilmasa FINAL nomli bir nechta eski fayl ham paydo bo'lishi mumkin."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
    ],

    "L08_M09_005": [
        {
            "code": "L08_Q133",
            "question": "Arxitektura-konstruktsiya auditida grid, sath va tayanchlar tekshiriladimi?",
            "explanation": (
                "Bular ikki loyiha orasidagi asosiy koordinatsiya nuqtalaridir."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L08_Q134",
            "question": "Hal qilingan issue modelga kiritilmagan bo'lsa koordinatsiya hali to'liq tugamaganmi?",
            "explanation": (
                "Qabul qilingan qaror loyiha hujjati va modelida aks etishi kerak."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L08_Q135",
            "question": "Arxitektor-konstruktor bilan professional ishlashdagi to'g'ri umumiy workflow qaysi?",
            "explanation": (
                "Aniq ma'lumot almashinadi, savollar boshqariladi, javoblar modelga kiritiladi, versiyalar nazorat qilinadi va yakunda koordinatsiya auditi o'tkaziladi."
            ),
            "options": [
                (
                    "A",
                    "Aniq loyiha ma'lumoti → savol/issue → konstruktor javobi → modelni yangilash → versiya nazorati → audit",
                    True,
                ),
                (
                    "B",
                    "Eski fayl yuborish → og'zaki kelishuv → modelni yangilamaslik → audit qilmaslik",
                    False,
                ),
            ],
        },
    ],
}


# ============================================================
# DATABASE SEED
# ============================================================

def seed_level08_module09():
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
        ) in LEVEL08_MODULE09_LESSONS:

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
