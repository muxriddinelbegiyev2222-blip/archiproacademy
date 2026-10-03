from database.database import get_connection


# ============================================================
# LEVEL 8
# MODULE 05 - TOM KONSTRUKSIYASI
# ============================================================

LEVEL08_MODULE05_LESSONS = [
    (
        "L08_M05",
        "L08_M05_001",
        "Tomning konstruktiv vazifasi",
        "theory",
        "Tomni faqat arxitektura shakli emas, balki yuklarni tayanchlarga uzatadigan konstruktiv tizim sifatida tushunish.",
        1,
        50,
        20,
    ),
    (
        "L08_M05",
        "L08_M05_002",
        "Tom yuk yo'li va tayanchlar",
        "theory",
        "Tom yuklarining rafters, beams, walls yoki boshqa tayanchlar orqali pastga uzatilish mantig'ini tushunish.",
        2,
        55,
        20,
    ),
    (
        "L08_M05",
        "L08_M05_003",
        "Nishab, ridge va eave mantig'i",
        "practice",
        "Tom geometriyasining ridge, eave va nishab zonalari bilan konstruktiv aloqasini tushunish.",
        3,
        60,
        20,
    ),
    (
        "L08_M05",
        "L08_M05_004",
        "Tom openings va arxitektura koordinatsiyasi",
        "practice",
        "Mansard oynalari, chimney, shaft va boshqa tom teshiklarini konstruktiv tizim bilan koordinatsiya qilish.",
        4,
        65,
        20,
    ),
    (
        "L08_M05",
        "L08_M05_005",
        "Tom konstruksiyasi professional audit",
        "practice",
        "Tom geometriyasi, tayanchlar, sathlar, openings va BIM modeldagi konstruktiv muvofiqliklarni kompleks tekshirish.",
        5,
        70,
        25,
    ),
]


# ============================================================
# CONTENT
# ============================================================

LEVEL08_MODULE05_CONTENT = {
    "L08_M05_001": [
        {
            "title": "Tom faqat ko'rinish emas",
            "type": "highlight",
            "text": """
            Tom —
            binoning yuqori
            himoya qatlami
            bo'lish bilan birga

            <br><br>

            konstruktiv tizimning
            muhim qismi.
            """,
        },
        {
            "title": "Tom nimalarni qabul qiladi?",
            "type": "normal",
            "text": """
            Tom tizimiga
            turli yuklar
            ta'sir qilishi mumkin.

            <br><br>

            Ular konstruktiv
            elementlar orqali
            tayanchlarga uzatiladi.
            """,
        },
        {
            "title": "Tom shakli va konstruksiya",
            "type": "highlight",
            "text": """
            Arxitektura tom shakli
            konstruktiv yechimdan
            alohida emas.

            <br><br>

            Tom murakkablashgan sari
            yuk yo'li ham
            murakkablashishi mumkin.
            """,
        },
        {
            "title": "Tasavvur qiling",
            "type": "example",
            "text": """
            Oddiy ikki nishabli tom
            bor.

            <br><br>

            Keyin mijoz
            bir nechta chiqindi,
            mansard oyna
            va katta konsol so'radi.

            <br><br>

            Bu faqat tashqi
            ko'rinish o'zgarishi emas.
            """,
        },
        {
            "title": "Tom konstruksiyasi turi",
            "type": "warning",
            "text": """
            Tomning aniq:

            <br><br>

            • konstruktiv turi;<br>
            • element kesimi;<br>
            • materiallari;<br>
            • birikmalari

            <br><br>

            konstruktiv hisob
            va loyiha asosida
            belgilanadi.
            """,
        },
        {
            "title": "Arxitektor nimani bilishi kerak?",
            "type": "normal",
            "text": """
            Arxitektor:

            <br><br>

            • tom qaerga tayanishini;<br>
            • ridge qayerda ekanini;<br>
            • eave qayerda tugashini;<br>
            • openings qayerda ekanini;<br>
            • tom va devor aloqasini

            <br><br>

            tushunishi kerak.
            """,
        },
        {
            "title": "Tom va devor",
            "type": "normal",
            "text": """
            Tom yuklari
            devor,
            beam,
            ustun
            yoki boshqa tayanchlarga

            <br><br>

            uzatilishi mumkin.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Oddiy pitched roof
            sxemasini tasavvur qiling.

            <br><br>

            Belgilang:

            • ridge;<br>
            • eave;<br>
            • asosiy tayanchlar;<br>
            • yukning pastga yo'li.
            """,
        },
    ],

    "L08_M05_002": [
        {
            "title": "Tom yuk yo'li",
            "type": "highlight",
            "text": """
            Professional tom
            loyihasida

            <br><br>

            yuk qayerdan
            qayerga uzatilishi
            tushunarli bo'lishi kerak.
            """,
        },
        {
            "title": "Rafter yoki asosiy element",
            "type": "normal",
            "text": """
            Tom qoplamasi
            yoki tom yuzasidagi yuklar

            <br><br>

            asosiy tom
            konstruktiv elementlariga
            uzatiladi.
            """,
        },
        {
            "title": "Keyingi tayanch",
            "type": "normal",
            "text": """
            Keyin yuklar
            beam,
            devor,
            ustun
            yoki boshqa

            <br><br>

            konstruktiv tayanchlarga
            o'tishi mumkin.
            """,
        },
        {
            "title": "Tayanch chizig'i",
            "type": "highlight",
            "text": """
            Tom geometriyasi
            bilan tayanch chizig'i

            <br><br>

            bir-biriga
            mantiqan mos
            bo'lishi kerak.
            """,
        },
        {
            "title": "Katta span",
            "type": "warning",
            "text": """
            Katta ustunsiz
            tom osti makoni

            <br><br>

            konstruktiv yechimga
            jiddiy ta'sir
            qilishi mumkin.

            <br><br>

            Aniq yechim
            hisob bilan belgilanadi.
            """,
        },
        {
            "title": "Ichki tayanch",
            "type": "example",
            "text": """
            Bir uyda
            ridge ostida

            <br><br>

            ichki tayanch
            yoki beam
            ishlashi mumkin.

            <br><br>

            Boshqa uyda esa
            boshqa konstruktiv
            tizim tanlanishi mumkin.
            """,
        },
        {
            "title": "Pastdagi tayanch",
            "type": "warning",
            "text": """
            Tom tayanchi
            pastdagi qavatda

            <br><br>

            hech qanday
            konstruktiv elementga
            mos kelmasa,

            <br><br>

            yuk uzatish
            qayta tekshiriladi.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Bir tom kesimini
            tasavvur qiling.

            <br><br>

            Yuk yo'lini yozing:

            tom yuzasi
            → asosiy tom elementi
            → tayanch
            → pastki konstruksiya
            → fundament.
            """,
        },
    ],

    "L08_M05_003": [
        {
            "title": "Nishab",
            "type": "highlight",
            "text": """
            Tom nishabi
            faqat tashqi
            ko'rinish emas.

            <br><br>

            U tom geometriyasi
            va konstruktiv
            tizimiga ta'sir qiladi.
            """,
        },
        {
            "title": "Ridge",
            "type": "normal",
            "text": """
            Ridge —
            tom yuzalarining
            yuqori tutashuv
            zonasi.

            <br><br>

            Uning joylashuvi
            tom umumiy
            geometriyasini belgilaydi.
            """,
        },
        {
            "title": "Eave",
            "type": "normal",
            "text": """
            Eave —
            tomning pastki
            chekka zonasi.

            <br><br>

            U fasad,
            suv chiqarish
            va tom chiqishi
            bilan bog'liq.
            """,
        },
        {
            "title": "Nishablar uchrashuvi",
            "type": "normal",
            "text": """
            Murakkab tomlarda
            bir nechta
            tom yuzalari

            <br><br>

            turli chiziqlarda
            bir-biri bilan
            tutashadi.
            """,
        },
        {
            "title": "Murakkab geometriya",
            "type": "warning",
            "text": """
            Tomga ko'p
            mayda nishablar
            qo'shish

            <br><br>

            loyihani avtomatik
            yaxshi qilmaydi.

            <br><br>

            Konstruksiya,
            suv chiqarish
            va qurilish
            murakkablashishi mumkin.
            """,
        },
        {
            "title": "Tom chiqishi",
            "type": "normal",
            "text": """
            Eave yoki
            tom chiqishi

            <br><br>

            fasadni himoya qilish,
            soyalanish
            va kompozitsiyaga

            <br><br>

            ta'sir qilishi mumkin.
            """,
        },
        {
            "title": "Ridge joyi o'zgarsa",
            "type": "example",
            "text": """
            Ridge joyi
            keyin o'zgartirildi.

            <br><br>

            Natijada:

            • nishablar;<br>
            • tom balandligi;<br>
            • fasad;<br>
            • konstruktiv tayanchlar

            <br><br>

            qayta tekshiriladi.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Oddiy gable roof
            uchun yozing:

            <br><br>

            • ridge qayerda;<br>
            • eave qayerda;<br>
            • nishab yo'nalishi;<br>
            • asosiy tayanchlar qayerda.
            """,
        },
    ],

    "L08_M05_004": [
        {
            "title": "Tomdagi opening",
            "type": "highlight",
            "text": """
            Tomdagi
            har qanday teshik

            <br><br>

            tom konstruktiv
            tizimining
            uzluksizligini
            o'zgartiradi.
            """,
        },
        {
            "title": "Mansard oynasi",
            "type": "normal",
            "text": """
            Mansard yoki
            roof window

            <br><br>

            tom geometriyasi
            va konstruktiv
            elementlar bilan
            koordinatsiya qilinadi.
            """,
        },
        {
            "title": "Chimney",
            "type": "normal",
            "text": """
            Mo'ri yoki
            chimney

            <br><br>

            tomdan o'tganda
            uning konstruktiv
            va tom qatlamlari

            <br><br>

            bilan tutashuvi
            hal qilinadi.
            """,
        },
        {
            "title": "Vent shaft",
            "type": "normal",
            "text": """
            Ventilyatsiya shaftlari
            tom orqali chiqishi
            mumkin.

            <br><br>

            Ularning joyi
            konstruktiv elementlar
            bilan to'qnashmasligi kerak.
            """,
        },
        {
            "title": "Openingni keyin qo'shish",
            "type": "warning",
            "text": """
            Tayyor tomda
            katta opening

            <br><br>

            keyin qo'shilsa,

            <br><br>

            faqat model
            kesib qo'yilmaydi.

            <br><br>

            Konstruktiv tizim
            qayta tekshiriladi.
            """,
        },
        {
            "title": "Dormer",
            "type": "example",
            "text": """
            Dormer
            tomning oddiy
            dekorativ elementi
            emas.

            <br><br>

            U:

            • geometriya;<br>
            • konstruksiya;<br>
            • gidroizolyatsiya;<br>
            • fasad

            <br><br>

            bilan bog'liq.
            """,
        },
        {
            "title": "MEP koordinatsiyasi",
            "type": "warning",
            "text": """
            Duct yoki shaft
            tomning asosiy
            konstruktiv elementi
            bilan to'qnashsa,

            <br><br>

            yechim mutaxassislar
            bilan kelishiladi.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Tomdagi 4 ta
            opening turini yozing.

            <br><br>

            Har biri uchun:

            • arxitektura;<br>
            • konstruktor;<br>
            • MEP

            <br><br>

            koordinatsiyasi
            kerakmi, belgilang.
            """,
        },
    ],

    "L08_M05_005": [
        {
            "title": "Tom konstruksiyasi auditi",
            "type": "highlight",
            "text": """
            Audit zanjiri:

            <br><br>

            Tom geometriyasi
            → Nishab
            → Ridge/Eave
            → Tayanch
            → Yuk yo'li
            → Openings
            → BIM audit
            """,
        },
        {
            "title": "1. Tom geometriyasi",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • tom shakli aniqmi?<br>
            • keraksiz murakkablik yo'qmi?<br>
            • tom yuzalari to'g'ri tutashyaptimi?
            """,
        },
        {
            "title": "2. Nishablar",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • nishab yo'nalishi to'g'rimi?<br>
            • tom yuzalari o'zaro mosmi?<br>
            • fasad bilan moslik bormi?
            """,
        },
        {
            "title": "3. Ridge va eave",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • ridge joyi aniqmi?<br>
            • eave sathlari mosmi?<br>
            • tom chiqishlari bir xil mantiqdami?
            """,
        },
        {
            "title": "4. Tayanchlar",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • tom qaerga tayanadi?<br>
            • tayanch ostida konstruktiv element bormi?<br>
            • yuk yo'li tushunarlimi?
            """,
        },
        {
            "title": "5. Openings",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • roof windowlar to'g'rimi?<br>
            • chimney joylari mosmi?<br>
            • vent shaftlar konflikt qilmayaptimi?
            """,
        },
        {
            "title": "6. Fasad koordinatsiyasi",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • tom fasad bilan mosmi?<br>
            • eave balandliklari to'g'rimi?<br>
            • ridge fasad kompozitsiyasiga mosmi?
            """,
        },
        {
            "title": "7. BIM model",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • plan va 3D mosmi?<br>
            • kesimda tom to'g'rimi?<br>
            • dublikat roof elementlar yo'qmi?<br>
            • noto'g'ri story'da elementlar yo'qmi?
            """,
        },
        {
            "title": "8. Konstruktor bilan koordinatsiya",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • oxirgi tom geometriyasi yuborilganmi?<br>
            • konstruktiv model bilan mosmi?<br>
            • keyingi o'zgarishlar qayta tekshirilganmi?
            """,
        },
        {
            "title": "Xatoni toping",
            "type": "warning",
            "text": """
            Tom modelida:

            <br><br>

            • ridge joyi plan va kesimda farq qiladi;<br>
            • bir roof window asosiy konstruktiv elementni kesadi;<br>
            • eave balandligi fasadda boshqa;<br>
            • chimney eski joyda qolgan;<br>
            • konstruktor eski tom modeli bilan ishlayapti.

            <br><br>

            Bu model
            qayta koordinatsiya
            qilinishi kerak.
            """,
        },
        {
            "title": "Professional checklist",
            "type": "example",
            "text": """
            Tom konstruksiyasi
            audit checklist:

            <br><br>

            <b>1.</b> Tom geometriyasi tushunarlimi?<br><br>
            <b>2.</b> Nishablar mantiqi to'g'rimi?<br><br>
            <b>3.</b> Ridge va eave mosmi?<br><br>
            <b>4.</b> Tayanch sxemasi tushunarlimi?<br><br>
            <b>5.</b> Yuk yo'li pastgacha davom etadimi?<br><br>
            <b>6.</b> Roof openings koordinatsiya qilinganmi?<br><br>
            <b>7.</b> MEP konfliktlari tekshirilganmi?<br><br>
            <b>8.</b> Fasad va tom modeli mosmi?<br><br>
            <b>9.</b> Plan, kesim va 3D bir xilmi?<br><br>
            <b>10.</b> Konstruktor oxirgi versiya bilan ishlayaptimi?
            """,
        },
        {
            "title": "Modul yakuni",
            "type": "highlight",
            "text": """
            Siz endi:

            <br><br>

            ✓ tomning konstruktiv vazifasini tushunasiz;<br>
            ✓ tom yuk yo'lini o'qiysiz;<br>
            ✓ tayanchlarni tekshirasiz;<br>
            ✓ ridge, eave va nishab mantig'ini bilasiz;<br>
            ✓ openings va MEP elementlarni koordinatsiya qilasiz;<br>
            ✓ tom konstruktiv modelini audit qilasiz.

            <br><br>

            Keyingi modul:
            <b>Gidroizolyatsiya.</b>
            """,
        },
    ],
}


# ============================================================
# QUIZ
# Q061-Q075
# ============================================================

LEVEL08_MODULE05_QUIZ = {
    "L08_M05_001": [
        {
            "code": "L08_Q061",
            "question": "Tom konstruktiv yuk uzatish tizimining bir qismi bo'lishi mumkinmi?",
            "explanation": (
                "Tom elementlari yuklarni pastdagi tayanch va konstruktiv tizimlarga uzatishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L08_Q062",
            "question": "Tom shakli konstruktiv yechimga umuman ta'sir qilmaydimi?",
            "explanation": (
                "Tom geometriyasi murakkablashsa, tayanch va yuk uzatish sxemasi ham o'zgarishi mumkin."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L08_Q063",
            "question": "Arxitektor tom qayerga tayanishini tushunishi kerakmi?",
            "explanation": (
                "Tayanch va yuk yo'lini tushunish arxitektura-konstruksiya koordinatsiyasi uchun muhim."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L08_M05_002": [
        {
            "code": "L08_Q064",
            "question": "Tom yuklari konstruktiv elementlar orqali devor, beam yoki ustunlarga uzatilishi mumkinmi?",
            "explanation": (
                "Tom yuk yo'li konstruktiv sxemaga qarab turli tayanchlar orqali pastga davom etadi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L08_Q065",
            "question": "Tom tayanchi pastdagi konstruktiv tizim bilan mos bo'lmasa bu tekshiruv talab qiladimi?",
            "explanation": (
                "Yuk yo'li uzluksiz va tushunarli bo'lishi kerak."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L08_Q066",
            "question": "Katta ustunsiz tom osti makoni konstruktiv yechimga ta'sir qilmasligi kafolatlanganmi?",
            "explanation": (
                "Katta spanlar konstruktiv elementlar va tizim tanloviga ta'sir qilishi mumkin."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
    ],

    "L08_M05_003": [
        {
            "code": "L08_Q067",
            "question": "Ridge tom yuzalarining yuqori tutashuv zonasi hisoblanadimi?",
            "explanation": (
                "Ridge tom geometriyasidagi asosiy yuqori tutashuv chizig'idir."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L08_Q068",
            "question": "Eave tomning pastki chekka zonasi bilan bog'liqmi?",
            "explanation": (
                "Eave tomning pastki chekka qismi bo'lib, fasad va suv chiqarish bilan ham bog'liq."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L08_Q069",
            "question": "Ridge joyini o'zgartirish faqat grafik ko'rinishga ta'sir qiladimi?",
            "explanation": (
                "Ridge o'zgarishi nishab, balandlik, fasad va tayanch sxemasiga ham ta'sir qilishi mumkin."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
    ],

    "L08_M05_004": [
        {
            "code": "L08_Q070",
            "question": "Roof window va chimney tom konstruktiv tizimi bilan koordinatsiya qilinadimi?",
            "explanation": (
                "Tomdagi openings va chiqish elementlari konstruktiv elementlar bilan to'qnashmasligi kerak."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L08_Q071",
            "question": "Tayyor tomda katta opening yaratish faqat BIM modelni kesish bilan tugaydimi?",
            "explanation": (
                "Katta opening tomning konstruktiv ishlashiga ta'sir qilishi mumkin va qayta tekshiriladi."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L08_Q072",
            "question": "Vent shaft joyi tom konstruktiv elementlari bilan to'qnashmasligi kerakmi?",
            "explanation": (
                "MEP va konstruktiv elementlar oldindan koordinatsiya qilinishi kerak."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L08_M05_005": [
        {
            "code": "L08_Q073",
            "question": "Tom auditida geometriya, tayanch, ridge/eave va openings tekshiriladimi?",
            "explanation": (
                "Professional tom auditi arxitektura va konstruktiv tizimni kompleks tekshiradi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L08_Q074",
            "question": "Plan va kesimda ridge joyi farq qilsa bu koordinatsiya xatosi bo'lishi mumkinmi?",
            "explanation": (
                "Turli ko'rinishlardagi tom geometriyasi bir xil loyiha holatini ko'rsatishi kerak."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L08_Q075",
            "question": "Tom konstruksiyasi bilan professional ishlashdagi to'g'ri umumiy workflow qaysi?",
            "explanation": (
                "Tom geometriyasi va tayanchlar aniqlanadi, yuk yo'li tushuniladi, openings va MEP koordinatsiya qilinadi va yakunda BIM audit bajariladi."
            ),
            "options": [
                (
                    "A",
                    "Tom geometriyasi → tayanchlar → yuk yo'li → ridge/eave → openings/MEP → BIM audit",
                    True,
                ),
                (
                    "B",
                    "Tom shaklini tasodifiy murakkablashtirish → tayanchlarni tekshirmaslik → openinglarni keyin kesish",
                    False,
                ),
            ],
        },
    ],
}


# ============================================================
# DATABASE SEED
# ============================================================

def seed_level08_module05():
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
        ) in LEVEL08_MODULE05_LESSONS:

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
