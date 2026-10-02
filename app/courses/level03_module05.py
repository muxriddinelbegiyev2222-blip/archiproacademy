from database.database import get_connection


# ============================================================
# LEVEL 3
# MODULE 05 - HOVLI ZONALARI
# ============================================================

LEVEL03_MODULE05_LESSONS = [
    (
        "L03_M05",
        "L03_M05_001",
        "Hovlini funksional zonalash",
        "theory",
        "Hovlini dam olish, yashil, xo'jalik va harakat zonalariga ajratish.",
        1,
        40,
        20,
    ),
    (
        "L03_M05",
        "L03_M05_002",
        "Family va mehmon hovlisi",
        "theory",
        "Oilaviy kundalik foydalanish va mehmon kutish zonalarini tahlil qilish.",
        2,
        40,
        20,
    ),
    (
        "L03_M05",
        "L03_M05_003",
        "Yozgi ovqatlanish va dam olish zonasi",
        "theory",
        "Terassa, gazebo, mangal va tashqi ovqatlanish joylarini to'g'ri bog'lash.",
        3,
        45,
        20,
    ),
    (
        "L03_M05",
        "L03_M05_004",
        "Yashil va xo'jalik zonalari",
        "practice",
        "Landshaft, daraxtlar, ombor va xo'jalik funksiyalarini muvozanatli joylashtirish.",
        4,
        45,
        20,
    ),
    (
        "L03_M05",
        "L03_M05_005",
        "Hovli zonalaridagi xatolar",
        "practice",
        "Tashqi makondagi tipik funksional va circulation xatolarini aniqlash.",
        5,
        55,
        25,
    ),
]


# ============================================================
# CONTENT
# ============================================================

LEVEL03_MODULE05_CONTENT = {
    "L03_M05_001": [
        {
            "title": "Hovli — qolgan bo'sh joy emas",
            "type": "highlight",
            "text": """
            Uy joylashtirilgandan keyin
            qolgan maydon avtomatik ravishda
            yaxshi hovli bo'lib qolmaydi.

            <br><br>

            Hovli ham ichki plan kabi
            funksional tizim sifatida loyihalanadi.
            """,
        },
        {
            "title": "Asosiy zonalar",
            "type": "normal",
            "text": """
            Hovlida quyidagi zonalar bo'lishi mumkin:

            <br><br>

            • family dam olish;<br>
            • mehmon zonasi;<br>
            • yashil hudud;<br>
            • bolalar o'yin zonasi;<br>
            • yozgi ovqatlanish;<br>
            • xo'jalik zonasi;<br>
            • parking;<br>
            • piyoda yo'llari.
            """,
        },
        {
            "title": "Tasavvur qiling",
            "type": "example",
            "text": """
            Uchastka katta.

            <br><br>

            Lekin:

            <br><br>

            mangal bir burchakda,
            stol boshqa burchakda,
            bolalar zonasi mashina yo'liga yaqin,
            xo'jalik zonasi living oynasi oldida.

            <br><br>

            Maydon katta,
            ammo tizim yo'q.
            """,
        },
        {
            "title": "Zonalash prinsipi",
            "type": "highlight",
            "text": """
            <b>
            Har bir tashqi zona
            qayerda joylashishi kerakligini
            uning funksiyasi belgilaydi.
            </b>
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Oldingi uchastkangizda
            kamida 5 ta tashqi zona belgilang.

            <br><br>

            Hali detallarni chizmang.

            <br><br>

            Faqat:
            “qaysi zona qayerda bo'ladi?”
            degan savolga javob bering.
            """,
        },
    ],

    "L03_M05_002": [
        {
            "title": "Family va guest foydalanishi bir xil emas",
            "type": "highlight",
            "text": """
            Oilaning har kuni foydalanadigan hovlisi bilan
            mehmon uchun ishlatiladigan hovli
            bir xil xarakterda bo'lishi shart emas.
            """,
        },
        {
            "title": "Family hovli",
            "type": "normal",
            "text": """
            Family hovli ko'pincha:

            <br><br>

            • livingga yaqin;<br>
            • private;<br>
            • bolalar uchun qulay;<br>
            • kundalik foydalanishga mos

            <br><br>

            bo'lishi kerak.
            """,
        },
        {
            "title": "Mehmon hovlisi",
            "type": "normal",
            "text": """
            Mehmon zonasi:

            <br><br>

            • asosiy kirishga;<br>
            • mehmonxonaga;<br>
            • tashqi diningga

            <br><br>

            mantiqiy bog'lanishi mumkin.
            """,
        },
        {
            "title": "Privacy",
            "type": "example",
            "text": """
            Mehmon kelganda
            oilaning kundalik private hovlisidan
            o'tishga majbur bo'lsa,

            <br><br>

            family privacy zaiflashadi.
            """,
        },
        {
            "title": "Bitta hovli ham bo'lishi mumkin",
            "type": "normal",
            "text": """
            Kichik uchastkada
            family va guest zona bitta makonda
            ishlashi mumkin.

            <br><br>

            Muhimi — foydalanish konfliktini kamaytirish.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Uchastkangizda:

            <br><br>

            FAMILY

            va

            GUEST

            <br><br>

            zonalarni belgilang.

            <br><br>

            Agar ular bitta bo'lsa,
            nima uchun bitta ekanini yozing.
            """,
        },
    ],

    "L03_M05_003": [
        {
            "title": "Yozgi yashash makoni",
            "type": "highlight",
            "text": """
            Tashqi ovqatlanish va dam olish zonasi
            hovlining eng faol qismlaridan biri bo'lishi mumkin.
            """,
        },
        {
            "title": "Oshxona bilan aloqa",
            "type": "normal",
            "text": """
            Tashqi dining yoki mangal zonasi
            oshxona bilan juda uzoq bo'lsa,

            <br><br>

            mahsulot, idish va ovqat tashish
            noqulaylashadi.
            """,
        },
        {
            "title": "Living bilan aloqa",
            "type": "example",
            "text": """
            Living → terassa → hovli

            <br><br>

            ketma-ketligi
            ichki va tashqi yashash makonini
            birlashtirishi mumkin.
            """,
        },
        {
            "title": "Gazebo",
            "type": "normal",
            "text": """
            Gazebo yoki yopiq ayvon:

            <br><br>

            • quyoshdan himoya;<br>
            • yomg'irdan himoya;<br>
            • mehmon kutish;<br>
            • tashqi ovqatlanish

            <br><br>

            vazifalarini bajarishi mumkin.
            """,
        },
        {
            "title": "Mangal zonasi",
            "type": "warning",
            "text": """
            Mangalni joylashtirganda
            faqat chiroyli ko'rinishni emas,

            <br><br>

            tutun,
            xavfsizlik,
            ovqat tayyorlash
            va o'tirish zonasiga aloqani
            ham hisobga olish kerak.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Uchastkangizda quyidagilarni joylashtiring:

            <br><br>

            • terassa;<br>
            • tashqi stol;<br>
            • mangal;<br>
            • gazebo.

            <br><br>

            Oshxonadan ulargacha bo'lgan
            yo'lni ham chizing.
            """,
        },
    ],

    "L03_M05_004": [
        {
            "title": "Yashil hudud — faqat dekor emas",
            "type": "highlight",
            "text": """
            Daraxt, maysa va o'simliklar
            hovli sifatiga funksional ta'sir qiladi.
            """,
        },
        {
            "title": "Daraxtlarning vazifasi",
            "type": "normal",
            "text": """
            Daraxtlar:

            <br><br>

            • soya;<br>
            • privacy;<br>
            • vizual ekran;<br>
            • mikroiqlim;<br>
            • kompozitsion markaz

            <br><br>

            yaratishi mumkin.
            """,
        },
        {
            "title": "Xo'jalik zonasi",
            "type": "normal",
            "text": """
            Xo'jalik zonasi:

            <br><br>

            • ombor;<br>
            • inventar;<br>
            • laundry bilan bog'liq tashqi joy;<br>
            • chiqindi;<br>
            • servis elementlari

            <br><br>

            uchun ishlatilishi mumkin.
            """,
        },
        {
            "title": "Xo'jalikni yashirish",
            "type": "example",
            "text": """
            Xo'jalik zonasi
            asosiy mehmon hovlisining markazida bo'lmasligi mumkin.

            <br><br>

            Uni service yo'liga yaqinroq,
            lekin foydalanishga qulay joylashtirish mumkin.
            """,
        },
        {
            "title": "Bolalar zonasi",
            "type": "warning",
            "text": """
            Bolalar o'yin joyi
            mashina harakati yoki
            service zonasiga juda yaqin bo'lmasligi kerak.

            <br><br>

            Ko'rish va nazorat ham muhim.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Uchastkangizda belgilang:

            <br><br>

            • katta daraxtlar;<br>
            • yashil zona;<br>
            • bolalar zona;<br>
            • xo'jalik zona;<br>
            • chiqindi/service nuqtasi.
            """,
        },
    ],

    "L03_M05_005": [
        {
            "title": "Hovli xatolarini ovlaymiz",
            "type": "highlight",
            "text": """
            Endi butun tashqi makonni
            foydalanuvchi ko'zi bilan tekshiramiz.
            """,
        },
        {
            "title": "Xato 1 — hovli qoldiq maydon",
            "type": "warning",
            "text": """
            Avval uy va parking joylashtirilgan.

            <br><br>

            Qolgan tasodifiy joy
            “hovli” deb qabul qilingan.

            <br><br>

            Natijada aniq tashqi markaz yo'q.
            """,
        },
        {
            "title": "Xato 2 — mangal oshxonadan juda uzoqda",
            "type": "warning",
            "text": """
            Tashqi ovqatlanish chiroyli joyda.

            <br><br>

            Lekin idish va mahsulotlarni
            har safar uzoq masofaga tashish kerak.
            """,
        },
        {
            "title": "Xato 3 — bolalar va mashina konflikti",
            "type": "warning",
            "text": """
            Bolalar o'yin zonasi
            avtomobil kirish yo'li bilan kesishadi.
            """,
        },
        {
            "title": "Xato 4 — service zona living oldida",
            "type": "warning",
            "text": """
            Livingning asosiy oynasi oldida
            chiqindi, ombor yoki xo'jalik faoliyati joylashgan.
            """,
        },
        {
            "title": "Xato 5 — barcha joy qoplama",
            "type": "warning",
            "text": """
            Hovli deyarli to'liq
            beton yoki tosh qoplama bilan to'ldirilgan.

            <br><br>

            Yashil, soya va yumshoq landshaft
            juda kam.
            """,
        },
        {
            "title": "Professional checklist",
            "type": "example",
            "text": """
            Hovlini tekshirganda:

            <br><br>

            <b>1.</b> Family zona qayerda?<br><br>
            <b>2.</b> Guest zona qayerda?<br><br>
            <b>3.</b> Tashqi dining qayerda?<br><br>
            <b>4.</b> Bolalar qayerda o'ynaydi?<br><br>
            <b>5.</b> Yashil va daraxtlar qayerda?<br><br>
            <b>6.</b> Xo'jalik zona qayerda?<br><br>
            <b>7.</b> Parking bilan konflikt bormi?
            """,
        },
        {
            "title": "Mini-loyiha",
            "type": "example",
            "text": """
            Oldingi genplaningizni oling.

            <br><br>

            Unda kamida:

            <br><br>

            • family hovli;<br>
            • guest zona;<br>
            • tashqi dining;<br>
            • yashil zona;<br>
            • bolalar zona;<br>
            • service/xo'jalik zona

            <br><br>

            ni belgilang.

            <br><br>

            Har bir zona nima uchun
            aynan shu joyda ekanini
            bir jumla bilan tushuntiring.
            """,
        },
        {
            "title": "Modul yakuni",
            "type": "highlight",
            "text": """
            Siz endi:

            <br><br>

            ✓ hovlini funksional zonalash;<br>
            ✓ family va guest hududlarini ajratish;<br>
            ✓ tashqi ovqatlanish zonasini joylashtirish;<br>
            ✓ yashil hududlardan foydalanish;<br>
            ✓ xo'jalik zonasini boshqarish;<br>
            ✓ tashqi circulation konfliktlarini ko'rish

            <br><br>

            ko'nikmalariga ega bo'ldingiz.

            <br><br>

            Keyingi modul:
            <b>Avtomobil zonasi.</b>
            """,
        },
    ],
}


# ============================================================
# QUIZ
# ============================================================

LEVEL03_MODULE05_QUIZ = {
    "L03_M05_001": [
        {
            "code": "L03_Q061",
            "question": "Hovli faqat uy qurilgandan keyin qolgan bo'sh maydonmi?",
            "explanation": (
                "Hovli ham alohida funksional tizim sifatida loyihalanadi."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L03_Q062",
            "question": "Hovlida bir nechta funksional zona bo'lishi mumkinmi?",
            "explanation": (
                "Family, guest, yashil, bolalar va xo'jalik kabi zonalar bo'lishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L03_Q063",
            "question": "Tashqi zonalarni ham circulation bilan bog'lash kerakmi?",
            "explanation": (
                "Ular o'rtasidagi real harakat hovli qulayligiga ta'sir qiladi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L03_M05_002": [
        {
            "code": "L03_Q064",
            "question": "Family va guest hovli doim bir xil vazifani bajarishi shartmi?",
            "explanation": (
                "Oilaviy kundalik foydalanish va mehmon foydalanishi farq qilishi mumkin."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L03_Q065",
            "question": "Mehmon private family hovlisini kesib o'tishi privacy muammosi bo'lishi mumkinmi?",
            "explanation": (
                "Bu oilaning kundalik private hududiga ta'sir qilishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L03_Q066",
            "question": "Kichik uchastkada family va guest zona birlashishi mumkinmi?",
            "explanation": (
                "Makon cheklangan bo'lsa funksiyalar birlashtirilishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L03_M05_003": [
        {
            "code": "L03_Q067",
            "question": "Tashqi diningning oshxona bilan aloqasi muhimmi?",
            "explanation": (
                "Ovqat, mahsulot va idish tashish qulayligi uchun bu muhim."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L03_Q068",
            "question": "Gazebo faqat dekorativ elementmi?",
            "explanation": (
                "U soya, himoya, mehmon kutish va tashqi ovqatlanish vazifalarini bajarishi mumkin."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L03_Q069",
            "question": "Mangal joylashuvida tutun va xavfsizlik hisobga olinadimi?",
            "explanation": (
                "Mangal zonasi faqat ko'rinish bilan emas, real foydalanish bilan tahlil qilinadi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L03_M05_004": [
        {
            "code": "L03_Q070",
            "question": "Daraxtlar faqat bezak uchun ishlatiladimi?",
            "explanation": (
                "Ular soya, privacy va mikroiqlimga ham ta'sir qiladi."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L03_Q071",
            "question": "Xo'jalik zonasi service harakati bilan bog'liqmi?",
            "explanation": (
                "Ombor, chiqindi va xo'jalik ishlari service circulationiga kiradi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L03_Q072",
            "question": "Bolalar o'yin zonasini mashina yo'liga yaqin joylashtirish xavf tug'dirishi mumkinmi?",
            "explanation": (
                "Bolalar zonasi xavfsiz va nazorat qilinadigan joyda bo'lishi kerak."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L03_M05_005": [
        {
            "code": "L03_Q073",
            "question": "Avval uy va parkingni joylashtirib, qolgan maydonni avtomatik hovli deb qabul qilish to'g'rimi?",
            "explanation": (
                "Hovli ham oldindan funksional rejalashtirilishi kerak."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L03_Q074",
            "question": "Living oynasi oldidagi xo'jalik zonasi fazoviy muammo bo'lishi mumkinmi?",
            "explanation": (
                "Asosiy yashash ko'rinishi va service funksiyalari bir-biriga xalaqit berishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L03_Q075",
            "question": "Hovli auditida qaysi savol muhim?",
            "explanation": (
                "Har bir tashqi zonaning vazifasi va o'zaro aloqasi tekshiriladi."
            ),
            "options": [
                ("A", "Family zona qayerda?", True),
                ("B", "Faqat tom materiali nima?", False),
            ],
        },
    ],
}


# ============================================================
# DATABASE SEED
# ============================================================

def seed_level03_module05():
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
        ) in LEVEL03_MODULE05_LESSONS:

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
