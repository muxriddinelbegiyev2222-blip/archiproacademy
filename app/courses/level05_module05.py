from database.database import get_connection


# ============================================================
# LEVEL 5
# MODULE 05 - DOOR VA WINDOW
# ============================================================

LEVEL05_MODULE05_LESSONS = [
    (
        "L05_M05",
        "L05_M05_001",
        "Door va Window asoslari",
        "theory",
        "Eshik va derazalarni devorga joylashtirishning asosiy mantig'ini tushunish.",
        1,
        40,
        20,
    ),
    (
        "L05_M05",
        "L05_M05_002",
        "Eshik o'lchami va ochilish yo'nalishi",
        "theory",
        "Eshik o'lchamlari, joylashuvi va ochilish yo'nalishini boshqarish.",
        2,
        45,
        20,
    ),
    (
        "L05_M05",
        "L05_M05_003",
        "Deraza o'lchami va balandligi",
        "theory",
        "Deraza o'lchami, parapet balandligi va fasad bilan aloqasini tushunish.",
        3,
        45,
        20,
    ),
    (
        "L05_M05",
        "L05_M05_004",
        "Door va Window tahrirlash",
        "practice",
        "Eshik va derazalarni nusxalash, almashtirish va mavjud parametrlarini tahrirlash.",
        4,
        50,
        20,
    ),
    (
        "L05_M05",
        "L05_M05_005",
        "Door va Window mini-loyiha",
        "practice",
        "Oddiy uy modelida eshik va derazalarni joylashtirish va 2D hamda 3Dda tekshirish.",
        5,
        60,
        25,
    ),
]


# ============================================================
# CONTENT
# ============================================================

LEVEL05_MODULE05_CONTENT = {
    "L05_M05_001": [
        {
            "title": "Door va Window devor bilan ishlaydi",
            "type": "highlight",
            "text": """
            Archicadda Door va Window
            odatda devorga joylashtiriladigan
            BIM elementlaridir.

            <br><br>

            Ular oddiy 2D belgilar emas.

            <br><br>

            Eshik yoki deraza
            devorda real opening hosil qiladi.
            """,
        },
        {
            "title": "ToolBox",
            "type": "normal",
            "text": """
            ToolBox ichidan:

            <br><br>

            • Door Tool;<br>
            • Window Tool

            <br><br>

            ni toping.

            <br><br>

            Tool tanlanganda
            Info Boxdagi parametrlar ham
            shu elementga moslashadi.
            """,
        },
        {
            "title": "Devor bo'lmasa nima bo'ladi?",
            "type": "highlight",
            "text": """
            Boshlang'ich mashqda
            avval devor modeli yaratiladi.

            <br><br>

            Keyin eshik va derazalar
            shu devorlarga joylashtiriladi.
            """,
        },
        {
            "title": "Joylashtirish",
            "type": "normal",
            "text": """
            Eshik yoki derazani
            devorga qo'yishda:

            <br><br>

            • qaysi devor;<br>
            • qaysi nuqta;<br>
            • qaysi tomon;<br>
            • element o'lchami

            <br><br>

            nazorat qilinadi.
            """,
        },
        {
            "title": "Tasavvur qiling",
            "type": "example",
            "text": """
            Bedroom devori tayyor.

            <br><br>

            Siz derazani faqat
            “shu yer chiroyli ko'rinadi”
            deb qo'ydingiz.

            <br><br>

            Keyin fasadga o'tganda
            barcha oynalar turli balandlikda.

            <br><br>

            Demak faqat plan emas,
            fasad ham tekshirilishi kerak.
            """,
        },
        {
            "title": "BIM fikrlashi",
            "type": "highlight",
            "text": """
            Door va Window bilan ishlaganda:

            <br><br>

            <b>
            PLAN + FASAD + 3D
            </b>

            <br><br>

            birgalikda tekshiriladi.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            1. Oddiy devor yarating.<br><br>
            2. Door Toolni tanlang.<br><br>
            3. Bitta eshik qo'ying.<br><br>
            4. Window Toolni tanlang.<br><br>
            5. Bitta deraza qo'ying.<br><br>
            6. 3Dda tekshiring.
            """,
        },
    ],

    "L05_M05_002": [
        {
            "title": "Eshik o'lchami",
            "type": "highlight",
            "text": """
            Eshikni qo'yishdan oldin
            uning o'lchamlarini tekshiring.

            <br><br>

            Eshikning width va height
            parametrlarini
            tasodifiy qoldirmang.
            """,
        },
        {
            "title": "O'lcham nima uchun muhim?",
            "type": "normal",
            "text": """
            Eshik o'lchami:

            <br><br>

            • odam harakati;<br>
            • xona funksiyasi;<br>
            • mebel joylashuvi;<br>
            • fasad yoki interior ko'rinishi

            <br><br>

            bilan bog'liq.
            """,
        },
        {
            "title": "Ochilish yo'nalishi",
            "type": "highlight",
            "text": """
            Eshik qayerga ochilishi
            plan ergonomikasiga
            bevosita ta'sir qiladi.
            """,
        },
        {
            "title": "Noto'g'ri ochilish",
            "type": "warning",
            "text": """
            Eshik ochilganda:

            <br><br>

            • boshqa eshik bilan urishsa;<br>
            • mebelni to'ssa;<br>
            • tor koridorni yopsa;<br>
            • asosiy harakat yo'lini kesib qo'ysa

            <br><br>

            uning ochilish yo'nalishini
            qayta ko'rib chiqish kerak.
            """,
        },
        {
            "title": "Tasavvur qiling",
            "type": "example",
            "text": """
            Kichik sanuzel.

            <br><br>

            Eshik noto'g'ri tomonga ochilib,
            ichkaridagi jihoz bilan konfliktga kiryapti.

            <br><br>

            Plan grafik jihatdan to'g'ri,
            lekin foydalanish yomon.
            """,
        },
        {
            "title": "Door markerga emas, foydalanishga qarang",
            "type": "normal",
            "text": """
            Eshik belgisi
            chizmada chiroyli turishi
            yetarli emas.

            <br><br>

            Odam real hayotda
            eshikdan qanday foydalanishini
            tasavvur qiling.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Bitta xona yarating.

            <br><br>

            Bir xil eshikni
            ikki xil ochilish yo'nalishida
            sinab ko'ring.

            <br><br>

            Qaysi variant circulation uchun
            qulayroq ekanini yozing.
            """,
        },
    ],

    "L05_M05_003": [
        {
            "title": "Deraza faqat width va height emas",
            "type": "highlight",
            "text": """
            Window Toolda
            o'lchamdan tashqari
            vertikal joylashuv ham muhim.

            <br><br>

            Deraza polga nisbatan
            qayerda boshlanishini
            nazorat qilish kerak.
            """,
        },
        {
            "title": "Parapet / sill balandligi",
            "type": "normal",
            "text": """
            Derazaning pastki qismi
            polga nisbatan
            ma'lum balandlikda joylashadi.

            <br><br>

            Bu qiymat:

            <br><br>

            • xona funksiyasi;<br>
            • mebel;<br>
            • fasad;<br>
            • ko'rinish

            <br><br>

            bilan bog'liq bo'lishi mumkin.
            """,
        },
        {
            "title": "Bir xil fasad",
            "type": "example",
            "text": """
            Bir fasaddagi
            uchta bir xil bedroom oynasi
            turli balandlikda qo'yilgan.

            <br><br>

            Plan ichida bu
            darhol bilinmasligi mumkin.

            <br><br>

            Elevationda esa
            tartibsizlik juda aniq ko'rinadi.
            """,
        },
        {
            "title": "Deraza va mebel",
            "type": "normal",
            "text": """
            Deraza joylashuvida
            xona ichidagi mebelni ham
            hisobga oling.

            <br><br>

            Masalan:

            <br><br>

            shkaf oldiga
            katta deraza qo'yish

            <br><br>

            funksional konflikt yaratishi mumkin.
            """,
        },
        {
            "title": "Kitchen window",
            "type": "example",
            "text": """
            Oshxonada countertop,
            yuqori shkaflar,
            rakovina
            va deraza birgalikda
            tahlil qilinadi.

            <br><br>

            Faqat fasad uchun
            oynani joylashtirish yetarli emas.
            """,
        },
        {
            "title": "3D va Elevation",
            "type": "highlight",
            "text": """
            Derazani qo'ygandan keyin
            ikki joyni tekshiring:

            <br><br>

            <b>3D</b> —
            umumiy hajm uchun.

            <br><br>

            <b>Elevation</b> —
            fasad ritmi va balandlik uchun.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Bir devorga
            3 ta deraza qo'ying.

            <br><br>

            Ularning:

            <br><br>

            • width;<br>
            • height;<br>
            • sill/parapet balandligi

            <br><br>

            bir xil bo'lishini tekshiring.

            <br><br>

            Keyin Elevationda ko'ring.
            """,
        },
    ],

    "L05_M05_004": [
        {
            "title": "Bir elementni qayta-qayta yaratmang",
            "type": "highlight",
            "text": """
            Agar uyda
            bir xil turdagi
            8 ta deraza bo'lsa,

            <br><br>

            har safar parametrlarni
            noldan kiritish shart emas.
            """,
        },
        {
            "title": "Nusxalash",
            "type": "normal",
            "text": """
            Bir xil parametrdagi
            Door yoki Window
            mavjud bo'lsa,

            <br><br>

            undan nusxa olish
            ishni tezlashtirishi mumkin.
            """,
        },
        {
            "title": "Lekin tekshiring",
            "type": "warning",
            "text": """
            Nusxa olingan element
            yangi joyda ham
            aynan shu parametrda
            qolishi kerakmi?

            <br><br>

            Har safar shuni tekshiring.
            """,
        },
        {
            "title": "Existing elementni tahrirlash",
            "type": "normal",
            "text": """
            Mavjud Door yoki Window
            tanlanib,

            <br><br>

            uning:

            <br><br>

            • o'lchami;<br>
            • turi;<br>
            • joylashuvi;<br>
            • ayrim ko'rinish parametrlarini

            <br><br>

            tahrirlash mumkin.
            """,
        },
        {
            "title": "Bir turdagi elementlar",
            "type": "example",
            "text": """
            Masalan:

            <br><br>

            Bedroom Window Type A

            <br><br>

            degan mantiq bilan
            bir xil xonalarda
            bir xil deraza ishlatishingiz mumkin.

            <br><br>

            Bu modelni tartibli qiladi.
            """,
        },
        {
            "title": "Fasadni buzadigan nusxa",
            "type": "warning",
            "text": """
            O'quvchi bir derazani
            5 marta nusxaladi.

            <br><br>

            Lekin oxirgi deraza
            boshqa xona va boshqa fasadda.

            <br><br>

            Uning o'lchami va balandligi
            alohida tekshirilmagan.

            <br><br>

            Tezlik nazoratni almashtirmaydi.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Bitta Window yarating.

            <br><br>

            Undan 3 ta nusxa oling.

            <br><br>

            Keyin bittasining
            width parametrini o'zgartiring.

            <br><br>

            3D va Elevationda farqni ko'ring.
            """,
        },
    ],

    "L05_M05_005": [
        {
            "title": "Door va Window mini-loyiha",
            "type": "highlight",
            "text": """
            Endi oldingi darslarda
            yaratgan kichik uy modelini
            davom ettiramiz.

            <br><br>

            Devor va slab tayyor.

            <br><br>

            Endi uy real foydalanishga
            yaqinlasha boshlaydi.
            """,
        },
        {
            "title": "Vazifa",
            "type": "example",
            "text": """
            Modelda:

            <br><br>

            • asosiy kirish eshigi;<br>
            • bedroom eshiklari;<br>
            • sanuzel eshigi;<br>
            • living oynalari;<br>
            • bedroom oynalari;<br>
            • kitchen oynasi

            <br><br>

            joylashtiring.
            """,
        },
        {
            "title": "1-bosqich — eshiklar",
            "type": "normal",
            "text": """
            Avval barcha eshiklarni qo'ying.

            <br><br>

            Har birida tekshiring:

            <br><br>

            • o'lcham;<br>
            • joylashuv;<br>
            • ochilish yo'nalishi;<br>
            • mebel bilan konflikt.
            """,
        },
        {
            "title": "2-bosqich — derazalar",
            "type": "normal",
            "text": """
            Keyin derazalarni qo'ying.

            <br><br>

            Tekshiring:

            <br><br>

            • width;<br>
            • height;<br>
            • parapet/sill balandligi;<br>
            • xona funksiyasi.
            """,
        },
        {
            "title": "3-bosqich — Plan",
            "type": "normal",
            "text": """
            Floor Planda
            circulationni tekshiring.

            <br><br>

            Eshiklar bir-biri bilan
            urishmayaptimi?

            <br><br>

            Mebel uchun joy qolyaptimi?
            """,
        },
        {
            "title": "4-bosqich — Elevation",
            "type": "normal",
            "text": """
            Elevationda
            deraza ritmini tekshiring.

            <br><br>

            Bir xil turdagi oynalar
            tasodifiy balandliklarda
            turib qolmaganmi?
            """,
        },
        {
            "title": "5-bosqich — 3D",
            "type": "normal",
            "text": """
            3Dga o'ting.

            <br><br>

            Butun modelni
            tashqaridan va ichkaridan
            ko'rib chiqing.
            """,
        },
        {
            "title": "Xatoni toping",
            "type": "warning",
            "text": """
            Bedroom eshigi ochilganda
            shkaf oldini to'liq yopib qo'yyapti.

            <br><br>

            Eshik modeli texnik jihatdan mavjud.

            <br><br>

            Lekin arxitektura jihatdan
            yechim noto'g'ri.

            <br><br>

            Sabab:
            opening direction
            va mebel aloqasi tekshirilmagan.
            """,
        },
        {
            "title": "Professional checklist",
            "type": "example",
            "text": """
            Door va Windowlarni tekshiring:

            <br><br>

            <b>1.</b> To'g'ri devorga qo'yilganmi?<br><br>
            <b>2.</b> O'lchami mosmi?<br><br>
            <b>3.</b> Door opening direction to'g'rimi?<br><br>
            <b>4.</b> Window balandligi nazoratdami?<br><br>
            <b>5.</b> Mebel bilan konflikt yo'qmi?<br><br>
            <b>6.</b> Elevation ritmi to'g'rimi?<br><br>
            <b>7.</b> 3Dda tekshirildimi?
            """,
        },
        {
            "title": "Modul yakuni",
            "type": "highlight",
            "text": """
            Siz endi:

            <br><br>

            ✓ Door Toolni tushunasiz;<br>
            ✓ Window Toolni tushunasiz;<br>
            ✓ eshik o'lchamini boshqarasiz;<br>
            ✓ ochilish yo'nalishini tekshirasiz;<br>
            ✓ deraza balandligini boshqarasiz;<br>
            ✓ elementlarni nusxalaysiz;<br>
            ✓ Plan, Elevation va 3Dda nazorat qilasiz.

            <br><br>

            Keyingi modul:
            <b>Column va Beam.</b>
            """,
        },
    ],
}


# ============================================================
# QUIZ
# ============================================================

LEVEL05_MODULE05_QUIZ = {
    "L05_M05_001": [
        {
            "code": "L05_Q061",
            "question": "Door va Window odatda devorga joylashtiriladigan BIM elementlarimi?",
            "explanation": (
                "Ular devor bilan bog'langan holda real opening hosil qiladi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L05_Q062",
            "question": "Eshik va derazani faqat Floor Planda tekshirish yetarlimi?",
            "explanation": (
                "Plan bilan birga Elevation va 3D tekshiruvi ham muhim."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L05_Q063",
            "question": "Door yoki Window qo'yishda uning o'lchami nazorat qilinadimi?",
            "explanation": (
                "O'lcham elementning funksiyasi va modeldagi ko'rinishiga ta'sir qiladi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L05_M05_002": [
        {
            "code": "L05_Q064",
            "question": "Eshik ochilish yo'nalishi xona ergonomikasiga ta'sir qiladimi?",
            "explanation": (
                "Noto'g'ri ochilish mebel yoki harakat yo'li bilan konflikt yaratishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L05_Q065",
            "question": "Eshik ochilganda boshqa eshik bilan urilishi xato bo'lishi mumkinmi?",
            "explanation": (
                "Door swinglar bir-biri bilan va circulation bilan tekshiriladi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L05_Q066",
            "question": "Eshik grafik belgisi chiroyli bo'lsa foydalanish ergonomikasini tekshirish shart emasmi?",
            "explanation": (
                "Eshik real odam harakati va xona funksiyasi bilan baholanadi."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
    ],

    "L05_M05_003": [
        {
            "code": "L05_Q067",
            "question": "Window balandligi fasad ko'rinishiga ta'sir qiladimi?",
            "explanation": (
                "Derazalarning vertikal joylashuvi Elevationda fasad ritmiga ta'sir qiladi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L05_Q068",
            "question": "Deraza joylashuvida mebelni ham hisobga olish kerakmi?",
            "explanation": (
                "Deraza va mebel bir-biri bilan funksional konflikt yaratmasligi kerak."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L05_Q069",
            "question": "Bir fasaddagi bir xil derazalarni turli tasodifiy balandlikka qo'yish tartibsizlik yaratishi mumkinmi?",
            "explanation": (
                "Elevationda deraza ritmi va balandliklari nazorat qilinadi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L05_M05_004": [
        {
            "code": "L05_Q070",
            "question": "Bir xil derazadan nusxa olish workflow'ni tezlashtirishi mumkinmi?",
            "explanation": (
                "Bir xil parametrli elementlarni qayta ishlatish vaqtni tejashi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L05_Q071",
            "question": "Nusxa olingan element yangi joyda ham tekshirilishi kerakmi?",
            "explanation": (
                "Yangi xona yoki fasadda boshqa parametr talab qilinishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L05_Q072",
            "question": "Mavjud Door yoki Windowni tahrirlash mumkinmi?",
            "explanation": (
                "Tanlangan elementning o'lchami, turi va joylashuvi kabi parametrlar tahrirlanishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L05_M05_005": [
        {
            "code": "L05_Q073",
            "question": "Door va Window joylashtirgandan keyin Plan, Elevation va 3Dni tekshirish foydalimi?",
            "explanation": (
                "Har bir ko'rinish turli xatolarni aniqlashga yordam beradi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L05_Q074",
            "question": "Eshik mebel oldini to'sib qo'ysa opening direction qayta ko'rib chiqilishi mumkinmi?",
            "explanation": (
                "Eshik ochilishi xona ergonomikasi bilan bog'liq."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L05_Q075",
            "question": "Door va Window bilan ishlashdagi to'g'ri nazorat qaysi?",
            "explanation": (
                "O'lcham, joylashuv, ochilish va turli ko'rinishlarda tekshiruv birgalikda bajariladi."
            ),
            "options": [
                (
                    "A",
                    "O'lcham → joylashuv → Plan/Elevation/3D tekshiruv",
                    True,
                ),
                (
                    "B",
                    "Tasodifiy joylashtirish → tekshirmaslik",
                    False,
                ),
            ],
        },
    ],
}


# ============================================================
# DATABASE SEED
# ============================================================

def seed_level05_module05():
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
        ) in LEVEL05_MODULE05_LESSONS:

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
