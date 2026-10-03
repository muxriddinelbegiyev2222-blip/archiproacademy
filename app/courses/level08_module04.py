from database.database import get_connection


# ============================================================
# LEVEL 8
# MODULE 04 - PLITALAR
# ============================================================

LEVEL08_MODULE04_LESSONS = [
    (
        "L08_M04",
        "L08_M04_001",
        "Plita va qavatlararo yopma tushunchasi",
        "theory",
        "Qavatlararo plitaning bino ichidagi vazifasi va umumiy yuk uzatish mantig'ini tushunish.",
        1,
        40,
        20,
    ),
    (
        "L08_M04",
        "L08_M04_002",
        "Plita tayanch sxemasi",
        "theory",
        "Plitaning devor, rigel va ustunlarga qanday tayanishi mumkinligini tushunish.",
        2,
        45,
        20,
    ),
    (
        "L08_M04",
        "L08_M04_003",
        "Ochilishlar va zinapoya bo'shligi",
        "practice",
        "Plitadagi zinapoya, shaft va boshqa ochilishlarni konstruktiv tizim bilan koordinatsiya qilish.",
        3,
        50,
        20,
    ),
    (
        "L08_M04",
        "L08_M04_004",
        "Balkon, konsol va chekka zonalar",
        "practice",
        "Plitaning balkon, konsol va fasad chekkalaridagi konstruktiv mantig'ini tushunish.",
        4,
        50,
        20,
    ),
    (
        "L08_M04",
        "L08_M04_005",
        "Plitalar professional audit",
        "practice",
        "Plita geometriyasi, tayanchlar, ochilishlar, sathlar va BIM koordinatsiyasini kompleks tekshirish.",
        5,
        55,
        25,
    ),
]


# ============================================================
# CONTENT
# ============================================================

LEVEL08_MODULE04_CONTENT = {
    "L08_M04_001": [
        {
            "title": "Plita nima?",
            "type": "highlight",
            "text": """
            Plita —
            qavatlar orasini
            ajratadigan

            <br><br>

            va yuklarni
            tayanchlarga uzatadigan
            konstruktiv element.
            """,
        },
        {
            "title": "Plita faqat pol emas",
            "type": "warning",
            "text": """
            Qavat planida
            pol ko'rinishi

            <br><br>

            bilan konstruktiv
            plita bir xil
            tushuncha emas.

            <br><br>

            Plita yuk ko'taruvchi
            tizimning bir qismi.
            """,
        },
        {
            "title": "Yuk yo'li",
            "type": "normal",
            "text": """
            Plitadagi yuklar
            konstruktiv sxemaga qarab

            <br><br>

            devor,
            rigel,
            ustun
            yoki boshqa tayanchlarga

            <br><br>

            uzatilishi mumkin.
            """,
        },
        {
            "title": "Arxitektura uchun ahamiyati",
            "type": "highlight",
            "text": """
            Plita:

            <br><br>

            • qavat sathlariga;<br>
            • zinapoyaga;<br>
            • balkonlarga;<br>
            • ochilishlarga;<br>
            • shift balandligiga;<br>
            • MEP o'tishlariga

            <br><br>

            ta'sir qiladi.
            """,
        },
        {
            "title": "Qalinlikni taxmin qilmang",
            "type": "warning",
            "text": """
            Plitaning aniq:

            <br><br>

            • qalinligi;<br>
            • armaturasi;<br>
            • tayanch sxemasi;<br>
            • konstruktiv turi

            <br><br>

            hisob va loyiha
            asosida aniqlanadi.
            """,
        },
        {
            "title": "Tasavvur qiling",
            "type": "example",
            "text": """
            Ikkinchi qavatda
            katta xona bor.

            <br><br>

            Pastdagi qavatda esa
            tayanchlar boshqa
            joylashgan.

            <br><br>

            Plita bu yuklarni
            qanday uzatishi
            konstruktiv jihatdan
            hal qilinadi.
            """,
        },
        {
            "title": "Plita va sath",
            "type": "normal",
            "text": """
            Arxitektura
            floor level
            bilan

            <br><br>

            konstruktiv plita
            sathi

            <br><br>

            bir xil mantiqda
            koordinatsiya qilinishi kerak.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Oddiy ikki qavatli
            uy uchun yozing:

            <br><br>

            • plita qayerda;<br>
            • qaysi tayanchlarga tayanadi;<br>
            • yuk qayerga uzatiladi.
            """,
        },
    ],

    "L08_M04_002": [
        {
            "title": "Tayanch sxemasi",
            "type": "highlight",
            "text": """
            Plita havoda
            mustaqil turmaydi.

            <br><br>

            U ma'lum
            konstruktiv tayanch
            sxemasida ishlaydi.
            """,
        },
        {
            "title": "Devorlarga tayangan plita",
            "type": "normal",
            "text": """
            Ayrim tizimlarda
            plita yuklari

            <br><br>

            yuk ko'taruvchi
            devorlarga
            uzatilishi mumkin.
            """,
        },
        {
            "title": "Rigellarga tayangan plita",
            "type": "normal",
            "text": """
            Karkasli tizimda
            plita

            <br><br>

            rigel yoki beamlar
            orqali

            <br><br>

            ustunlarga
            yuk uzatishi mumkin.
            """,
        },
        {
            "title": "Ustunlarga bevosita tayanch",
            "type": "normal",
            "text": """
            Ayrim konstruktiv
            tizimlarda

            <br><br>

            plita ustunlar
            bilan bevosita
            ishlashi ham mumkin.

            <br><br>

            Aniq tizim
            konstruktor tomonidan
            belgilanadi.
            """,
        },
        {
            "title": "Tayanch qaerda?",
            "type": "highlight",
            "text": """
            Arxitektor
            har bir katta
            plita zonasi uchun

            <br><br>

            “Bu plita
            nimaga tayanadi?”

            <br><br>

            degan savolni
            bera olishi kerak.
            """,
        },
        {
            "title": "Tayanchsiz tasavvur",
            "type": "warning",
            "text": """
            Plan chiroyli
            ko'rinadi,

            <br><br>

            lekin katta
            ochiq zona ostida
            tayanch tizimi yo'q.

            <br><br>

            Bu konstruktiv
            yechimni alohida
            hal qilishni talab qiladi.
            """,
        },
        {
            "title": "Span bilan aloqa",
            "type": "normal",
            "text": """
            Plitaning
            tayanchlar orasidagi
            ishlash masofasi

            <br><br>

            konstruktiv yechimga
            ta'sir qiladi.

            <br><br>

            Aniq qiymatlar
            hisob bilan belgilanadi.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Bitta qavat planini
            tasavvur qiling.

            <br><br>

            Har bir plita zonasi uchun:

            • tayanch turi;<br>
            • yuk qayerga uzatiladi;<br>
            • katta span bormi

            <br><br>

            deb yozing.
            """,
        },
    ],

    "L08_M04_003": [
        {
            "title": "Plitadagi ochilish",
            "type": "highlight",
            "text": """
            Zinapoya,
            lift shaft,
            vent shaft
            yoki boshqa teshik

            <br><br>

            plitaning uzluksizligini
            o'zgartiradi.
            """,
        },
        {
            "title": "Zinapoya bo'shligi",
            "type": "normal",
            "text": """
            Zinapoya uchun
            kerakli bo'shliq

            <br><br>

            plita,
            rigel
            va qavat balandligi
            bilan

            <br><br>

            boshidan koordinatsiya
            qilinadi.
            """,
        },
        {
            "title": "Ochilishni keyin qo'shish",
            "type": "warning",
            "text": """
            Tayyor konstruktiv
            plitada

            <br><br>

            katta yangi
            ochilish yaratish

            <br><br>

            oddiy BIM tahriri
            emas.

            <br><br>

            Konstruktiv yechim
            qayta tekshirilishi kerak.
            """,
        },
        {
            "title": "Shaftlar",
            "type": "normal",
            "text": """
            Ventilyatsiya,
            kanalizatsiya
            va boshqa shaftlar

            <br><br>

            qavatlar bo'yicha
            mantiqiy davom etishi

            <br><br>

            va plitalar bilan
            koordinatsiyada bo'lishi kerak.
            """,
        },
        {
            "title": "Kichik teshik ham muhim",
            "type": "warning",
            "text": """
            Teshik kichik
            ko'ringani bilan

            <br><br>

            uning joylashuvi
            konstruktiv elementga
            yaqin bo'lishi mumkin.

            <br><br>

            Shu sabab
            MEP penetratsiyalar
            nazorat qilinadi.
            """,
        },
        {
            "title": "Tasavvur qiling",
            "type": "example",
            "text": """
            Zinapoya modeli
            tayyor.

            <br><br>

            Lekin plitada
            unga mos
            opening yo'q.

            <br><br>

            3D modelda
            elementlar bir-birini
            kesib o'tadi.

            <br><br>

            Bu koordinatsiya xatosi.
            """,
        },
        {
            "title": "Qavatlararo moslik",
            "type": "normal",
            "text": """
            Vertikal shaftlar
            bir qavatda bir joyda,

            <br><br>

            boshqa qavatda
            boshqa joyda bo'lsa,

            <br><br>

            muhandislik va
            konstruktiv yechim
            murakkablashadi.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Plitadagi
            4 xil opening
            misolini yozing.

            <br><br>

            Har biri uchun
            kim bilan koordinatsiya
            kerakligini belgilang:

            <br><br>

            arxitektor,
            konstruktor,
            MEP.
            """,
        },
    ],

    "L08_M04_004": [
        {
            "title": "Balkon va plita",
            "type": "highlight",
            "text": """
            Balkon
            plitaning oddiy
            dekorativ davomi emas.

            <br><br>

            U alohida
            konstruktiv va
            fizik masalalarga ega.
            """,
        },
        {
            "title": "Konsol tushunchasi",
            "type": "normal",
            "text": """
            Konsol —
            bir tomondan
            tayangan

            <br><br>

            va boshqa tomonga
            chiqib turuvchi
            konstruktiv element
            konsepsiyasi.
            """,
        },
        {
            "title": "Balkon uzunligini taxmin qilmang",
            "type": "warning",
            "text": """
            Balkon yoki
            konsol chiqishini

            <br><br>

            faqat fasad
            ko'rinishi uchun

            <br><br>

            tasodifiy kattalashtirish
            mumkin emas.

            <br><br>

            Konstruktiv hisob
            talab qilinadi.
            """,
        },
        {
            "title": "Issiqlik ko'prigi",
            "type": "highlight",
            "text": """
            Tashqi balkon
            va ichki plita
            tutashuvi

            <br><br>

            issiqlik texnikasi
            nuqtai nazaridan ham
            muhim bo'lishi mumkin.
            """,
        },
        {
            "title": "Suv va nishab",
            "type": "normal",
            "text": """
            Tashqi balkon
            faqat konstruktsiya emas.

            <br><br>

            Unda:

            • suv chiqarish;<br>
            • nishab;<br>
            • gidroizolyatsiya;<br>
            • tashqi qatlamlar

            <br><br>

            ham koordinatsiya qilinadi.
            """,
        },
        {
            "title": "Fasad chekkasi",
            "type": "normal",
            "text": """
            Plita chekkasi
            fasad tizimi bilan

            <br><br>

            to'g'ri tutashishi
            kerak.

            <br><br>

            Konstruktiv model
            va fasad modeli
            bir-biridan uzilib
            qolmasligi kerak.
            """,
        },
        {
            "title": "Tasavvur qiling",
            "type": "example",
            "text": """
            Mijoz balkon
            chuqurligini
            keyin kattalashtirdi.

            <br><br>

            Arxitektura planini
            o'zgartirishning o'zi
            yetarli emas.

            <br><br>

            Konstruktor,
            fasad
            va suv chiqarish
            yechimi qayta tekshiriladi.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Balkon uchun
            koordinatsiya checklist
            yozing.

            <br><br>

            Kamida:

            • konstruktsiya;<br>
            • sath;<br>
            • fasad;<br>
            • gidroizolyatsiya;<br>
            • suv chiqarish

            <br><br>

            bo'lsin.
            """,
        },
    ],

    "L08_M04_005": [
        {
            "title": "Plitalar professional audit",
            "type": "highlight",
            "text": """
            Audit zanjiri:

            <br><br>

            Plita geometriyasi
            → Tayanchlar
            → Sathlar
            → Openings
            → Balkonlar
            → MEP
            → BIM audit
            """,
        },
        {
            "title": "1. Plita konturi",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • plita konturi to'g'rimi?<br>
            • devor va fasad bilan mosmi?<br>
            • keraksiz chiqishlar yo'qmi?
            """,
        },
        {
            "title": "2. Tayanchlar",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • plita nimaga tayanadi?<br>
            • rigel yoki devorlar mosmi?<br>
            • tayanchsiz katta zona bormi?
            """,
        },
        {
            "title": "3. Sathlar",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • konstruktiv sath to'g'rimi?<br>
            • finish floor bilan farq tushunarlimi?<br>
            • kesim va plan mosmi?
            """,
        },
        {
            "title": "4. Openings",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • zinapoya opening'i bormi?<br>
            • shaftlar qavatlar bo'yicha mosmi?<br>
            • MEP teshiklari koordinatsiya qilinganmi?
            """,
        },
        {
            "title": "5. Balkon va konsol",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • balkon geometriyasi konstruktiv loyiha bilan mosmi?<br>
            • sath va nishablar tushunarlimi?<br>
            • tashqi qatlamlar koordinatsiya qilinganmi?
            """,
        },
        {
            "title": "6. Zinapoya bilan aloqa",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • stair opening yetarlimi?<br>
            • zinapoya plitani kesib o'tmayaptimi?<br>
            • qavat balandliklari mosmi?
            """,
        },
        {
            "title": "7. MEP koordinatsiyasi",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • duct va quvurlar qayerdan o'tadi?<br>
            • keraksiz kesishuvlar bormi?<br>
            • penetratsiyalar oldindan belgilanganmi?
            """,
        },
        {
            "title": "8. BIM model",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • plita noto'g'ri story'da emasmi?<br>
            • dublikat slab yo'qmi?<br>
            • konturlar yopiq va to'g'rimi?<br>
            • plan, kesim va 3D mosmi?
            """,
        },
        {
            "title": "Xatoni toping",
            "type": "warning",
            "text": """
            Modelda:

            <br><br>

            • zinapoya plitani kesib o'tadi;<br>
            • shaft opening'i bir qavatda yo'q;<br>
            • balkon eski o'lchamda qolgan;<br>
            • plita sathi kesimda boshqa;<br>
            • MEP teshiklari konstruktor chizmasida yo'q.

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
            Plita audit checklist:

            <br><br>

            <b>1.</b> Plita konturi to'g'rimi?<br><br>
            <b>2.</b> Tayanch sxemasi tushunarlimi?<br><br>
            <b>3.</b> Sathlar mosmi?<br><br>
            <b>4.</b> Zinapoya opening'i to'g'rimi?<br><br>
            <b>5.</b> Shaftlar koordinatsiya qilinganmi?<br><br>
            <b>6.</b> Balkon va konsollar tekshirilganmi?<br><br>
            <b>7.</b> MEP penetratsiyalar mosmi?<br><br>
            <b>8.</b> Plan, kesim va 3D bir xilmi?<br><br>
            <b>9.</b> Konstruktor oxirgi model bilan ishlayaptimi?
            """,
        },
        {
            "title": "Modul yakuni",
            "type": "highlight",
            "text": """
            Siz endi:

            <br><br>

            ✓ plitaning vazifasini tushunasiz;<br>
            ✓ tayanch sxemasini o'qiysiz;<br>
            ✓ openings bilan ishlash mantig'ini bilasiz;<br>
            ✓ zinapoya va shaftlarni koordinatsiya qilasiz;<br>
            ✓ balkon va konsol zonasini tushunasiz;<br>
            ✓ plita BIM modelini audit qilasiz.

            <br><br>

            Keyingi modul:
            <b>Tom konstruksiyasi.</b>
            """,
        },
    ],
}


# ============================================================
# QUIZ
# Q046-Q060
# ============================================================

LEVEL08_MODULE04_QUIZ = {
    "L08_M04_001": [
        {
            "code": "L08_Q046",
            "question": "Qavatlararo plita bino yuklarini tayanchlarga uzatadigan konstruktiv element bo'lishi mumkinmi?",
            "explanation": (
                "Plita qavatni tashkil qilish bilan birga konstruktiv yuk uzatish tizimida ham ishlaydi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L08_Q047",
            "question": "Pol finishi va konstruktiv plita har doim aynan bir xil tushunchami?",
            "explanation": (
                "Finish floor qatlamlari bilan konstruktiv plita alohida loyiha qatlamlari hisoblanadi."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L08_Q048",
            "question": "Plitaning aniq qalinligi konstruktiv hisob va loyiha bilan belgilanadimi?",
            "explanation": (
                "Plita parametrlari yuklar, span va konstruktiv tizim asosida mutaxassis tomonidan aniqlanadi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L08_M04_002": [
        {
            "code": "L08_Q049",
            "question": "Arxitektor plita qaysi tayanchlarga tayanishini tushunishi kerakmi?",
            "explanation": (
                "Tayanch sxemasini tushunish arxitektura va konstruksiya koordinatsiyasi uchun muhim."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L08_Q050",
            "question": "Plita hech qanday tayanchsiz istalgan katta masofani avtomatik yopib bera oladimi?",
            "explanation": (
                "Span va tayanchlar konstruktiv hisobga bog'liq; cheksiz tayanchsiz zona mavjud emas."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L08_Q051",
            "question": "Plita devor, rigel yoki ustun tizimi bilan ishlashi mumkinmi?",
            "explanation": (
                "Plitaning tayanch sxemasi loyiha konstruktiv tizimiga qarab turlicha bo'lishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L08_M04_003": [
        {
            "code": "L08_Q052",
            "question": "Zinapoya bo'shligi plita bilan oldindan koordinatsiya qilinishi kerakmi?",
            "explanation": (
                "Zinapoya opening'i qavatlararo plita, balandlik va tayanchlar bilan birgalikda hal qilinadi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L08_Q053",
            "question": "Tayyor konstruktiv plitada katta yangi opening yaratish faqat grafik tahrir hisoblanadimi?",
            "explanation": (
                "Katta opening plitaning konstruktiv ishlashiga ta'sir qilishi mumkin va konstruktor bilan tekshiriladi."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L08_Q054",
            "question": "Shaftlarning qavatlar bo'yicha mos joylashuvi koordinatsiya uchun muhimmi?",
            "explanation": (
                "Vertikal kommunikatsiyalar qavatlar bo'yicha izchil bo'lsa konstruktiv va MEP koordinatsiyasi osonlashadi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L08_M04_004": [
        {
            "code": "L08_Q055",
            "question": "Balkon chiqishini faqat fasad ko'rinishiga qarab istalgancha kattalashtirish mumkinmi?",
            "explanation": (
                "Balkon va konsol o'lchamlari konstruktiv hisob va boshqa loyiha talablariga bog'liq."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L08_Q056",
            "question": "Balkon zonasida konstruktsiya bilan birga gidroizolyatsiya va suv chiqarish ham koordinatsiya qilinadimi?",
            "explanation": (
                "Tashqi balkon konstruktiv va qurilish-fizik masalalarni birgalikda talab qiladi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L08_Q057",
            "question": "Konsol bir tomondan tayangan va boshqa tomonga chiqib turuvchi konstruktiv sxema bo'lishi mumkinmi?",
            "explanation": (
                "Bu konsolning asosiy konstruktiv tushunchasidir."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L08_M04_005": [
        {
            "code": "L08_Q058",
            "question": "Plita auditida sath, tayanch, opening va MEP koordinatsiyasi tekshiriladimi?",
            "explanation": (
                "Professional audit plitaning geometriyasi va boshqa tizimlar bilan aloqasini kompleks tekshiradi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L08_Q059",
            "question": "Plan va kesimda plita sathi bir-biridan farq qilsa bu koordinatsiya muammosi bo'lishi mumkinmi?",
            "explanation": (
                "Turli ko'rinishlarda konstruktiv sathlar bir xil loyiha ma'lumotini ifodalashi kerak."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L08_Q060",
            "question": "Plitalar bilan professional ishlashdagi to'g'ri umumiy workflow qaysi?",
            "explanation": (
                "Avval tayanch va sathlar tushuniladi, openings va balkonlar koordinatsiya qilinadi, MEP konfliktlari tekshiriladi va BIM audit bajariladi."
            ),
            "options": [
                (
                    "A",
                    "Tayanchlar → plita → sathlar → openings/balkon → MEP koordinatsiya → BIM audit",
                    True,
                ),
                (
                    "B",
                    "Slab chizish → openinglarni keyin tasodifiy kesish → koordinatsiya qilmaslik",
                    False,
                ),
            ],
        },
    ],
}


# ============================================================
# DATABASE SEED
# ============================================================

def seed_level08_module04():
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
        ) in LEVEL08_MODULE04_LESSONS:

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
