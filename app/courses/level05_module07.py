from database.database import get_connection


# ============================================================
# LEVEL 5
# MODULE 07 - OBJECT TOOL
# ============================================================

LEVEL05_MODULE07_LESSONS = [
    (
        "L05_M07",
        "L05_M07_001",
        "Object Tool asoslari",
        "theory",
        "Archicadda mebel va library obyektlarini joylashtirish mantig'ini tushunish.",
        1,
        40,
        20,
    ),
    (
        "L05_M07",
        "L05_M07_002",
        "Mebel joylashtirish",
        "practice",
        "Mebelni xona funksiyasi va ergonomikaga mos joylashtirish.",
        2,
        45,
        20,
    ),
    (
        "L05_M07",
        "L05_M07_003",
        "Rotation va elevation",
        "practice",
        "Obyektlarni burish, yo'naltirish va vertikal joylashuvini boshqarish.",
        3,
        45,
        20,
    ),
    (
        "L05_M07",
        "L05_M07_004",
        "Nusxalash va obyektlarni tahrirlash",
        "practice",
        "Bir xil obyektlarni samarali ko'paytirish va parametrlarini o'zgartirish.",
        4,
        50,
        20,
    ),
    (
        "L05_M07",
        "L05_M07_005",
        "Object Tool mini-loyiha",
        "practice",
        "Oddiy uy xonalarini mebel bilan jihozlash va ergonomik tekshiruv o'tkazish.",
        5,
        60,
        25,
    ),
]


# ============================================================
# CONTENT
# ============================================================

LEVEL05_MODULE07_CONTENT = {
    "L05_M07_001": [
        {
            "title": "Object Tool nima?",
            "type": "highlight",
            "text": """
            Object Tool
            tayyor library obyektlarini
            loyiha ichiga joylashtirish uchun ishlatiladi.

            <br><br>

            Masalan:

            <br><br>

            • stol;<br>
            • stul;<br>
            • divan;<br>
            • krovat;<br>
            • shkaf;<br>
            • sanitar jihoz;<br>
            • boshqa tayyor obyektlar.
            """,
        },
        {
            "title": "Object faqat dekor emas",
            "type": "highlight",
            "text": """
            Mebel faqat
            prezentatsiya uchun qo'yilmaydi.

            <br><br>

            U xona haqiqatan
            ishlaydimi yoki yo'qmi
            tekshirishga yordam beradi.
            """,
        },
        {
            "title": "Library tushunchasi",
            "type": "normal",
            "text": """
            Archicadda ko'plab tayyor obyektlar
            library orqali mavjud bo'lishi mumkin.

            <br><br>

            Siz kerakli obyektni tanlab,
            uning parametrlarini
            loyiha talabiga moslashtirasiz.
            """,
        },
        {
            "title": "Object Settings",
            "type": "normal",
            "text": """
            Obyektni joylashtirishdan oldin
            uning Settings oynasini ko'ring.

            <br><br>

            Obyektga qarab:

            <br><br>

            • o'lcham;<br>
            • turi;<br>
            • ko'rinishi;<br>
            • materialga oid parametrlar

            <br><br>

            mavjud bo'lishi mumkin.
            """,
        },
        {
            "title": "Tasavvur qiling",
            "type": "example",
            "text": """
            Bedroom planda katta ko'rinadi.

            <br><br>

            Krovat,
            shkaf
            va tumba qo'yilgandan keyin
            esa yurish uchun
            juda kam joy qoladi.

            <br><br>

            Demak mebel
            rejaning real sifatini ko'rsatdi.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            1. Object Toolni tanlang.<br><br>
            2. Bitta stol toping.<br><br>
            3. Uni plan ichiga joylashtiring.<br><br>
            4. O'lchamini kuzating.<br><br>
            5. 3Dda tekshiring.
            """,
        },
    ],

    "L05_M07_002": [
        {
            "title": "Mebel rejaning testi",
            "type": "highlight",
            "text": """
            Xona maydoni katta bo'lishi
            uning avtomatik ravishda
            qulay ekanini anglatmaydi.

            <br><br>

            Mebel joylashtirilganda
            real foydalanish boshlanadi.
            """,
        },
        {
            "title": "Living",
            "type": "normal",
            "text": """
            Livingda masalan:

            <br><br>

            • divan;<br>
            • kreslo;<br>
            • TV zona;<br>
            • coffee table

            <br><br>

            joylashtirilganda
            odam yuradigan yo'llarni ham
            tekshirish kerak.
            """,
        },
        {
            "title": "Bedroom",
            "type": "normal",
            "text": """
            Bedroomda:

            <br><br>

            • krovat;<br>
            • shkaf;<br>
            • tumba;<br>
            • ish stoli

            <br><br>

            bir-biriga xalaqit bermasligi kerak.
            """,
        },
        {
            "title": "Dining",
            "type": "example",
            "text": """
            Dining stolining o'zi
            xonaga sig'ishi mumkin.

            <br><br>

            Lekin stullar surilganda
            yurish yo'li yopilib qolishi mumkin.

            <br><br>

            Shuning uchun faqat
            stol konturiga qaramang.
            """,
        },
        {
            "title": "Circulation",
            "type": "highlight",
            "text": """
            Har bir mebel qo'yilgandan keyin
            quyidagini so'rang:

            <br><br>

            <b>
            odam bu xonada
            bemalol harakatlana oladimi?
            </b>
            """,
        },
        {
            "title": "Tipik xato",
            "type": "warning",
            "text": """
            Xona chiroyli ko'rinish uchun
            juda ko'p mebel bilan to'ldirilgan.

            <br><br>

            Lekin eshikdan kirish
            va derazaga borish yo'li
            torayib ketgan.

            <br><br>

            Bu yaxshi reja emas.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Bitta bedroomni jihozlang.

            <br><br>

            Joylashtiring:

            <br><br>

            • krovat;<br>
            • 2 ta tumba;<br>
            • shkaf;<br>
            • stol.

            <br><br>

            Keyin circulationni tekshiring.
            """,
        },
    ],

    "L05_M07_003": [
        {
            "title": "Rotation",
            "type": "highlight",
            "text": """
            Obyekt joylashtirilganda
            uning yo'nalishi ham muhim.

            <br><br>

            Rotation orqali
            obyektni kerakli tomonga
            burish mumkin.
            """,
        },
        {
            "title": "Yo'nalish va foydalanish",
            "type": "normal",
            "text": """
            Divan devorga qarab turadimi?

            <br><br>

            Dining stul stolga qaraganmi?

            <br><br>

            Krovatning bosh tomoni
            mantiqiy joylashganmi?

            <br><br>

            Rotation faqat grafik masala emas.
            """,
        },
        {
            "title": "Elevation",
            "type": "highlight",
            "text": """
            Ba'zi obyektlarning
            vertikal joylashuvi ham muhim.

            <br><br>

            Obyekt polga nisbatan
            noto'g'ri elevationda bo'lsa,
            3Dda havoda turib qolishi
            yoki pol ichiga kirib ketishi mumkin.
            """,
        },
        {
            "title": "3D nazorat",
            "type": "example",
            "text": """
            Floor Planda
            obyekt joylashuvi to'g'ri.

            <br><br>

            3Dga o'tilganda esa
            stol pol ustidan
            ancha baland turibdi.

            <br><br>

            Muammo:
            elevation.
            """,
        },
        {
            "title": "Plan va 3Dni bog'lang",
            "type": "normal",
            "text": """
            Plan sizga
            horizontal joylashuvni ko'rsatadi.

            <br><br>

            3D esa
            obyektning hajm va
            vertikal joylashuvini
            yaxshiroq ko'rsatadi.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Bitta stul joylashtiring.

            <br><br>

            Keyin:

            <br><br>

            • uni 90° buring;<br>
            • yana buring;<br>
            • elevationni o'zgartiring;<br>
            • 3Dda natijani kuzating.
            """,
        },
    ],

    "L05_M07_004": [
        {
            "title": "Bir xil obyektlarni qayta yaratmang",
            "type": "highlight",
            "text": """
            Diningda 8 ta bir xil stul kerak.

            <br><br>

            Har birini alohida
            librarydan qayta tanlash
            shart emas.

            <br><br>

            Mavjud obyektni
            nusxalash mumkin.
            """,
        },
        {
            "title": "Nusxalash",
            "type": "normal",
            "text": """
            Copy usuli
            bir xil parametrdagi
            obyektlarni tez yaratishga
            yordam beradi.
            """,
        },
        {
            "title": "Ritm",
            "type": "example",
            "text": """
            Dining stullari
            yoki ayvondagi bir xil obyektlar
            tartibli ritm asosida
            joylashtirilishi mumkin.
            """,
        },
        {
            "title": "Nusxa har doim final emas",
            "type": "warning",
            "text": """
            Copy qilingan obyekt
            yangi joyda ham
            aynan shu holatda
            qolishi kerak degani emas.

            <br><br>

            Rotation,
            o'lcham
            yoki boshqa parametr
            o'zgarishi mumkin.
            """,
        },
        {
            "title": "Mavjud obyektni tahrirlash",
            "type": "normal",
            "text": """
            Mavjud obyektni tanlab
            uning Settingsini ochish mumkin.

            <br><br>

            Shu orqali
            parametrlar qayta boshqariladi.
            """,
        },
        {
            "title": "Keraksiz dublikat",
            "type": "warning",
            "text": """
            O'quvchi stulni
            copy qilayotib
            bir joyga ikki nusxa qo'yib yubordi.

            <br><br>

            Floor Planda deyarli bilinmadi.

            <br><br>

            3Dda esa obyektlar
            bir-birining ichida turibdi.

            <br><br>

            Dublikatlarni tekshiring.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            1 ta dining stol qo'ying.

            <br><br>

            1 ta stul yarating.

            <br><br>

            Keyin undan
            5 ta nusxa oling.

            <br><br>

            Barcha stullarni
            stolga to'g'ri yo'naltiring.
            """,
        },
    ],

    "L05_M07_005": [
        {
            "title": "Object Tool mini-loyiha",
            "type": "highlight",
            "text": """
            Endi kichik uy modelidagi
            asosiy xonalarni
            mebel bilan jihozlaymiz.

            <br><br>

            Maqsad —
            chiroyli render emas.

            <br><br>

            Maqsad —
            plan haqiqatan ishlashini tekshirish.
            """,
        },
        {
            "title": "1-bosqich — Living",
            "type": "normal",
            "text": """
            Livingga:

            <br><br>

            • divan;<br>
            • kreslo;<br>
            • TV zona;<br>
            • coffee table

            <br><br>

            joylashtiring.

            <br><br>

            Kirish va hovliga chiqish
            yo'llarini ochiq qoldiring.
            """,
        },
        {
            "title": "2-bosqich — Dining",
            "type": "normal",
            "text": """
            Dining stol va stullarni
            joylashtiring.

            <br><br>

            Stul orqasida
            real foydalanish uchun
            yetarli harakat zonasi
            qolayotganini tekshiring.
            """,
        },
        {
            "title": "3-bosqich — Bedrooms",
            "type": "normal",
            "text": """
            Har bedroomga:

            <br><br>

            • krovat;<br>
            • shkaf;<br>
            • tumba

            <br><br>

            joylashtiring.

            <br><br>

            Eshik va derazalar bilan
            konfliktlarni tekshiring.
            """,
        },
        {
            "title": "4-bosqich — Plan auditi",
            "type": "normal",
            "text": """
            Floor Planda tekshiring:

            <br><br>

            • circulation;<br>
            • eshik opening;<br>
            • mebel intervali;<br>
            • derazaga kirish;<br>
            • bo'sh zonalar.
            """,
        },
        {
            "title": "5-bosqich — 3D auditi",
            "type": "normal",
            "text": """
            3Dga o'ting.

            <br><br>

            Tekshiring:

            <br><br>

            • obyektlar pol ustidami;<br>
            • bir-birining ichiga kirmaganmi;<br>
            • orientation to'g'rimi;<br>
            • xona haddan tashqari to'lib ketmaganmi.
            """,
        },
        {
            "title": "Xatoni toping",
            "type": "warning",
            "text": """
            Bedroomda:

            <br><br>

            krovat,
            shkaf,
            stol

            <br><br>

            hammasi sig'di.

            <br><br>

            Lekin shkaf eshigini ochish uchun
            joy qolmadi.

            <br><br>

            Muammo:
            faqat obyekt konturi tekshirilgan,
            foydalanish zonasi tekshirilmagan.
            """,
        },
        {
            "title": "Professional checklist",
            "type": "example",
            "text": """
            Objectlarni tekshiring:

            <br><br>

            <b>1.</b> Xona funksiyasiga mosmi?<br><br>
            <b>2.</b> O'lchami mantiqiymi?<br><br>
            <b>3.</b> Rotation to'g'rimi?<br><br>
            <b>4.</b> Elevation to'g'rimi?<br><br>
            <b>5.</b> Door bilan konflikt yo'qmi?<br><br>
            <b>6.</b> Circulation ochiqmi?<br><br>
            <b>7.</b> 3Dda dublikat yo'qmi?
            """,
        },
        {
            "title": "Modul yakuni",
            "type": "highlight",
            "text": """
            Siz endi:

            <br><br>

            ✓ Object Toolni tushunasiz;<br>
            ✓ library obyektini tanlaysiz;<br>
            ✓ mebel joylashtirasiz;<br>
            ✓ rotationni boshqarasiz;<br>
            ✓ elevationni tekshirasiz;<br>
            ✓ obyektlarni nusxalaysiz;<br>
            ✓ plan ergonomikasini mebel orqali tekshirasiz.

            <br><br>

            Keyingi modul:
            <b>2D instrumentlar.</b>
            """,
        },
    ],
}


# ============================================================
# QUIZ
# ============================================================

LEVEL05_MODULE07_QUIZ = {
    "L05_M07_001": [
        {
            "code": "L05_Q091",
            "question": "Object Tool tayyor library obyektlarini joylashtirish uchun ishlatiladimi?",
            "explanation": (
                "Object Tool mebel va boshqa tayyor obyektlarni modelga qo'shishga yordam beradi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L05_Q092",
            "question": "Mebel faqat chiroyli 3D ko'rinish uchun kerakmi?",
            "explanation": (
                "Mebel xona ergonomikasi va real foydalanishni tekshirishda ham muhim."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L05_Q093",
            "question": "Object Settings orqali obyekt parametrlarini boshqarish mumkinmi?",
            "explanation": (
                "Obyektga qarab o'lcham va boshqa parametrlar mavjud bo'lishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L05_M07_002": [
        {
            "code": "L05_Q094",
            "question": "Mebel joylashtirish xona ergonomikasini tekshirishga yordam beradimi?",
            "explanation": (
                "Mebel real foydalanish va circulationni ko'rsatadi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L05_Q095",
            "question": "Dining stol sig'sa stullar uchun joyni tekshirish shart emasmi?",
            "explanation": (
                "Stul foydalanishi va odam harakati uchun qo'shimcha joy kerak bo'lishi mumkin."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L05_Q096",
            "question": "Mebel asosiy circulationni to'sib qo'yishi mumkinmi?",
            "explanation": (
                "Noto'g'ri joylashtirilgan mebel harakat yo'lini yomonlashtirishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L05_M07_003": [
        {
            "code": "L05_Q097",
            "question": "Rotation obyekt yo'nalishini boshqaradimi?",
            "explanation": (
                "Rotation orqali obyekt kerakli tomonga buriladi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L05_Q098",
            "question": "Noto'g'ri elevation obyektni havoda qoldirishi mumkinmi?",
            "explanation": (
                "Obyektning vertikal joylashuvi noto'g'ri bo'lsa 3Dda xato ko'rinadi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L05_Q099",
            "question": "Objectlarni faqat Floor Planda tekshirish yetarlimi?",
            "explanation": (
                "3D obyektning hajm va vertikal joylashuvini tekshirishga yordam beradi."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
    ],

    "L05_M07_004": [
        {
            "code": "L05_Q100",
            "question": "Bir xil obyektlarni nusxalash vaqtni tejashi mumkinmi?",
            "explanation": (
                "Bir xil parametrli obyektlarni qayta ishlatish workflow'ni tezlashtiradi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L05_Q101",
            "question": "Copy qilingan obyektni yangi joyda qayta tekshirish kerakmi?",
            "explanation": (
                "Yangi joyda rotation yoki boshqa parametr o'zgarishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L05_Q102",
            "question": "Bir joyda ikki obyekt tasodifan ustma-ust qolishi mumkinmi?",
            "explanation": (
                "Nusxalashda dublikatlar yuz berishi mumkin, shuning uchun 2D va 3D tekshiruv kerak."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L05_M07_005": [
        {
            "code": "L05_Q103",
            "question": "Mebel joylashtirgandan keyin Door openingni qayta tekshirish kerakmi?",
            "explanation": (
                "Mebel va eshik ochilishi o'rtasida konflikt paydo bo'lishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L05_Q104",
            "question": "Mebel sig'ishi xonaning to'liq qulay ekanini avtomatik anglatadimi?",
            "explanation": (
                "Circulation, foydalanish zonasi va eshiklar ham tekshirilishi kerak."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L05_Q105",
            "question": "Object Tool bilan ishlashdagi to'g'ri workflow qaysi?",
            "explanation": (
                "Obyekt tanlash, parametr, joylashtirish va ergonomik nazorat birgalikda bajariladi."
            ),
            "options": [
                (
                    "A",
                    "Object → parametr → joylashtirish → Plan/3D tekshiruv",
                    True,
                ),
                (
                    "B",
                    "Tasodifiy mebel → xonani to'ldirish",
                    False,
                ),
            ],
        },
    ],
}


# ============================================================
# DATABASE SEED
# ============================================================

def seed_level05_module07():
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
        ) in LEVEL05_MODULE07_LESSONS:

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
