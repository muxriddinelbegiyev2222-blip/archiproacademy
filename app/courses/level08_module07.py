from database.database import get_connection


# ============================================================
# LEVEL 8
# MODULE 07 - ISSIQLIK IZOLYATSIYASI
# ============================================================

LEVEL08_MODULE07_LESSONS = [
    (
        "L08_M07",
        "L08_M07_001",
        "Issiqlik izolyatsiyasi tushunchasi",
        "theory",
        "Binoning tashqi qobig'i orqali issiqlik almashinuvi va izolyatsiyaning umumiy vazifasini tushunish.",
        1,
        30,
        20,
    ),
    (
        "L08_M07",
        "L08_M07_002",
        "Building envelope va uzluksizlik",
        "theory",
        "Devor, tom, pol va ochilishlar atrofida issiqlik himoyasi uzluksiz ishlashi kerakligini tushunish.",
        2,
        35,
        20,
    ),
    (
        "L08_M07",
        "L08_M07_003",
        "Thermal bridge tushunchasi",
        "practice",
        "Issiqlik ko'priklari qayerda paydo bo'lishi va ularni loyiha bosqichida aniqlash mantig'ini tushunish.",
        3,
        35,
        20,
    ),
    (
        "L08_M07",
        "L08_M07_004",
        "Deraza, balkon va tutashuvlar",
        "practice",
        "Deraza, balkon, plita chekkasi va boshqa tutashuvlarda issiqlik himoyasini koordinatsiya qilish.",
        4,
        40,
        20,
    ),
    (
        "L08_M07",
        "L08_M07_005",
        "Issiqlik izolyatsiyasi professional audit",
        "practice",
        "Building envelope uzluksizligi, thermal bridge zonalari va BIM detallarini kompleks tekshirish.",
        5,
        40,
        25,
    ),
]


# ============================================================
# CONTENT
# ============================================================

LEVEL08_MODULE07_CONTENT = {
    "L08_M07_001": [
        {
            "title": "Issiqlik izolyatsiyasi nima?",
            "type": "highlight",
            "text": """
            Issiqlik izolyatsiyasi —
            bino ichki muhitini

            <br><br>

            tashqi harorat
            ta'siridan

            <br><br>

            himoya qilishga
            yordam beradigan
            qatlam va yechimlar tizimi.
            """,
        },
        {
            "title": "Bino qobig'i",
            "type": "normal",
            "text": """
            Building envelope
            tarkibiga odatda:

            <br><br>

            • tashqi devorlar;<br>
            • tom;<br>
            • yer yoki tashqi muhit bilan tutashuvchi pol;<br>
            • deraza va eshiklar

            <br><br>

            kiradi.
            """,
        },
        {
            "title": "Issiqlik qayerdan chiqadi?",
            "type": "normal",
            "text": """
            Issiqlik
            bino qobig'idagi

            <br><br>

            turli elementlar
            orqali almashinadi.

            <br><br>

            Shu sabab
            faqat bitta devorni
            izolyatsiya qilish
            yetarli bo'lmasligi mumkin.
            """,
        },
        {
            "title": "Izolyatsiya faqat qalinlik emas",
            "type": "warning",
            "text": """
            Issiqlik himoyasi
            faqat izolyatsiya
            qalinligini oshirishdan

            <br><br>

            iborat emas.

            <br><br>

            Material,
            uzluksizlik,
            tutashuv
            va umumiy detail
            muhim.
            """,
        },
        {
            "title": "Arxitektorning vazifasi",
            "type": "highlight",
            "text": """
            Arxitektor
            bino qobig'ini

            <br><br>

            bitta uzluksiz
            himoya tizimi
            sifatida ko'ra olishi kerak.
            """,
        },
        {
            "title": "Tasavvur qiling",
            "type": "example",
            "text": """
            Devor yaxshi
            izolyatsiyalangan.

            <br><br>

            Lekin balkon
            plitasi ichkaridan
            tashqariga uzluksiz chiqadi

            <br><br>

            va tutashuv
            hal qilinmagan.

            <br><br>

            Muammo devorning
            o'zida emas,
            detailda bo'lishi mumkin.
            """,
        },
        {
            "title": "Aniq hisob",
            "type": "warning",
            "text": """
            Izolyatsiyaning aniq:

            <br><br>

            • turi;<br>
            • qalinligi;<br>
            • qatlamlari;<br>
            • issiqlik ko'rsatkichlari

            <br><br>

            normativ va
            texnik hisoblar
            asosida belgilanadi.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Oddiy uy uchun
            building envelope'ni
            yozib chiqing:

            <br><br>

            • tashqi devor;<br>
            • tom;<br>
            • pol;<br>
            • deraza;<br>
            • eshik.
            """,
        },
    ],

    "L08_M07_002": [
        {
            "title": "Uzluksiz himoya",
            "type": "highlight",
            "text": """
            Professional
            issiqlik himoyasi

            <br><br>

            elementlar orasida
            uzilib qolmasligi kerak.
            """,
        },
        {
            "title": "Devor → tom",
            "type": "normal",
            "text": """
            Tashqi devordagi
            izolyatsiya

            <br><br>

            tomdagi issiqlik
            himoyasi bilan

            <br><br>

            mantiqan tutashishi
            kerak.
            """,
        },
        {
            "title": "Devor → pol",
            "type": "normal",
            "text": """
            Devorning pastki
            qismi bilan

            <br><br>

            pol yoki fundament
            zonasi orasidagi

            <br><br>

            tutashuv ham
            muhim.
            """,
        },
        {
            "title": "Deraza atrofi",
            "type": "warning",
            "text": """
            Deraza o'rnatilgan
            joyda

            <br><br>

            devor izolyatsiyasi
            uzilib qolishi mumkin.

            <br><br>

            Shu sabab
            reveal va frame
            atrofidagi detail
            muhim.
            """,
        },
        {
            "title": "Burchaklar",
            "type": "normal",
            "text": """
            Tashqi burchaklar,
            ichki burchaklar
            va boshqa

            <br><br>

            geometriya o'zgaradigan
            joylar

            <br><br>

            alohida tekshiriladi.
            """,
        },
        {
            "title": "Continuity line",
            "type": "highlight",
            "text": """
            Kesimni ko'rib,
            izolyatsiya qatlamini

            <br><br>

            uzluksiz chiziq
            sifatida kuzata
            olishingiz kerak.
            """,
        },
        {
            "title": "Xatoni toping",
            "type": "warning",
            "text": """
            Devor izolyatsiyasi bor.

            <br><br>

            Tom izolyatsiyasi ham bor.

            <br><br>

            Lekin parapet
            zonasida ular
            bir-biriga ulanmagan.

            <br><br>

            Bu detail
            qayta ko'rib chiqiladi.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Uy kesimini
            tasavvur qiling.

            <br><br>

            Izolyatsiya chizig'ini
            quyidagilar orqali
            kuzating:

            <br><br>

            pol
            → devor
            → tom.
            """,
        },
    ],

    "L08_M07_003": [
        {
            "title": "Thermal bridge nima?",
            "type": "highlight",
            "text": """
            Thermal bridge —
            bino qobig'ida

            <br><br>

            issiqlik oqimi
            kuchayishi mumkin bo'lgan
            lokal zona.
            """,
        },
        {
            "title": "Qayerda paydo bo'lishi mumkin?",
            "type": "normal",
            "text": """
            Thermal bridge
            ko'pincha:

            <br><br>

            • balkon tutashuvida;<br>
            • plita chekkasida;<br>
            • ustun va devor tutashuvida;<br>
            • deraza atrofida;<br>
            • tom-devor tutashuvida

            <br><br>

            paydo bo'lishi mumkin.
            """,
        },
        {
            "title": "Faqat energiya masalasi emas",
            "type": "warning",
            "text": """
            Sovuq lokal
            yuzalar

            <br><br>

            ichki komfort
            va namlik
            bilan bog'liq

            <br><br>

            qo'shimcha muammolar
            yaratishi mumkin.
            """,
        },
        {
            "title": "Konstruktiv element",
            "type": "normal",
            "text": """
            Beton ustun,
            beam
            yoki plita

            <br><br>

            tashqi qobiqni
            kesib o'tganda

            <br><br>

            detail alohida
            tekshiriladi.
            """,
        },
        {
            "title": "Balkon misoli",
            "type": "example",
            "text": """
            Ichki plita
            tashqi balkonga

            <br><br>

            to'g'ridan-to'g'ri
            davom etmoqda.

            <br><br>

            Bu zona
            issiqlik ko'prigi
            nuqtai nazaridan
            tekshirilishi kerak.
            """,
        },
        {
            "title": "Arxitektor nimani qiladi?",
            "type": "highlight",
            "text": """
            Arxitektor
            thermal bridge
            xavfi bo'lishi mumkin bo'lgan

            <br><br>

            zonalarni
            loyiha bosqichida
            aniqlaydi

            <br><br>

            va mutaxassislar
            bilan koordinatsiya qiladi.
            """,
        },
        {
            "title": "Aniq baholash",
            "type": "warning",
            "text": """
            Thermal bridge'ning
            aniq ta'siri

            <br><br>

            texnik hisob
            va tegishli
            loyiha tahlili
            bilan baholanadi.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Oddiy ikki qavatli
            uyda

            <br><br>

            5 ta potensial
            thermal bridge
            zonasini yozing.
            """,
        },
    ],

    "L08_M07_004": [
        {
            "title": "Deraza — zaif zona",
            "type": "highlight",
            "text": """
            Deraza
            bino qobig'idagi

            <br><br>

            muhim tutashuv
            zonalaridan biri.
            """,
        },
        {
            "title": "Frame va devor",
            "type": "normal",
            "text": """
            Deraza frame'i
            va devor qatlamlari

            <br><br>

            o'zaro to'g'ri
            koordinatsiya qilinishi kerak.
            """,
        },
        {
            "title": "Reveal",
            "type": "normal",
            "text": """
            Deraza ochilishining
            yon,
            yuqori
            va pastki

            <br><br>

            qismlari
            issiqlik himoyasi
            nuqtai nazaridan
            tekshiriladi.
            """,
        },
        {
            "title": "Balkon",
            "type": "warning",
            "text": """
            Balkon-plita
            tutashuvi

            <br><br>

            konstruktiv,
            gidroizolyatsiya
            va issiqlik

            <br><br>

            masalalarini
            birlashtiradi.
            """,
        },
        {
            "title": "Parapet",
            "type": "normal",
            "text": """
            Parapetda
            tom izolyatsiyasi
            va devor izolyatsiyasi

            <br><br>

            bir-biriga
            to'g'ri ulanishi
            kerak.
            """,
        },
        {
            "title": "Plita chekkasi",
            "type": "warning",
            "text": """
            Tashqi fasad
            zonasidagi

            <br><br>

            plita chekkasi
            himoya qatlamini
            kesib yubormasligi kerak.
            """,
        },
        {
            "title": "BIM detail",
            "type": "highlight",
            "text": """
            BIM modelda
            faqat umumiy
            devor qalinligi emas,

            <br><br>

            kritik tutashuv
            detallarining mantig'i
            ham tushunarli
            bo'lishi kerak.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Quyidagi zonalar uchun
            bitta-bittadan
            audit savoli yozing:

            <br><br>

            • deraza;<br>
            • balkon;<br>
            • parapet;<br>
            • plita chekkasi.
            """,
        },
    ],

    "L08_M07_005": [
        {
            "title": "Issiqlik izolyatsiyasi auditi",
            "type": "highlight",
            "text": """
            Audit zanjiri:

            <br><br>

            Envelope
            → Continuity
            → Thermal bridge
            → Openings
            → Tutashuv
            → BIM detail
            """,
        },
        {
            "title": "1. Building envelope",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • tashqi qobiq aniqmi?<br>
            • ichki va tashqi zona farqlanganmi?<br>
            • barcha asosiy yuzalar ko'rilganmi?
            """,
        },
        {
            "title": "2. Continuity",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • devordan tomga o'tish uzluksizmi?<br>
            • devordan polga o'tish uzluksizmi?<br>
            • parapetda uzilish yo'qmi?
            """,
        },
        {
            "title": "3. Thermal bridge zonalari",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • balkon tutashuvi;<br>
            • ustun-devor zonasi;<br>
            • plita chekkasi;<br>
            • deraza atrofi

            <br><br>

            nazorat qilinganmi?
            """,
        },
        {
            "title": "4. Deraza va eshik",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • frame joylashuvi tushunarlimi?<br>
            • reveal detali hal qilinganmi?<br>
            • izolyatsiya uzilib qolmaganmi?
            """,
        },
        {
            "title": "5. Tom va parapet",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • tom izolyatsiyasi devorga ulanyaptimi?<br>
            • parapet tepasi hal qilinganmi?<br>
            • qatlamlar mantiqan davom etadimi?
            """,
        },
        {
            "title": "6. Balkon",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • konstruktiv tutashuv tushunarlimi?<br>
            • waterproofing va insulation bir-biriga mosmi?<br>
            • ichki-tashqi sathlar koordinatsiya qilinganmi?
            """,
        },
        {
            "title": "7. BIM model",
            "type": "normal",
            "text": """
            Tekshiring:

            <br><br>

            • wall build-up to'g'rimi?<br>
            • roof build-up mosmi?<br>
            • slab edge tushunarlimi?<br>
            • sectionlarda qatlamlar mantiqi ko'rinadimi?
            """,
        },
        {
            "title": "Xatoni toping",
            "type": "warning",
            "text": """
            Loyihada:

            <br><br>

            • devor izolyatsiyasi tomga yetmaydi;<br>
            • balkon plitasi himoya qatlamini kesadi;<br>
            • deraza reveal'i izolyatsiyasiz;<br>
            • parapet detaili yo'q;<br>
            • plan va kesimdagi wall build-up farq qiladi.

            <br><br>

            Bu loyiha
            thermal envelope
            auditiga qaytariladi.
            """,
        },
        {
            "title": "Professional checklist",
            "type": "example",
            "text": """
            Issiqlik izolyatsiyasi audit:

            <br><br>

            <b>1.</b> Building envelope aniqmi?<br><br>
            <b>2.</b> Izolyatsiya uzluksizmi?<br><br>
            <b>3.</b> Devor-tom tutashuvi hal qilinganmi?<br><br>
            <b>4.</b> Devor-pol tutashuvi tekshirilganmi?<br><br>
            <b>5.</b> Thermal bridge zonalari aniqlanganmi?<br><br>
            <b>6.</b> Deraza va eshik atrofi tekshirilganmi?<br><br>
            <b>7.</b> Balkon va plita chekkasi koordinatsiya qilinganmi?<br><br>
            <b>8.</b> Parapet detaili tushunarlimi?<br><br>
            <b>9.</b> BIM model va kesimlar bir-biriga mosmi?
            """,
        },
        {
            "title": "Modul yakuni",
            "type": "highlight",
            "text": """
            Siz endi:

            <br><br>

            ✓ building envelope tushunchasini bilasiz;<br>
            ✓ izolyatsiya continuity'ni tekshirasiz;<br>
            ✓ thermal bridge zonalarini taniysiz;<br>
            ✓ deraza, balkon va parapet detallarini tushunasiz;<br>
            ✓ BIM modeldagi qatlamlar mantig'ini audit qilasiz.

            <br><br>

            Keyingi modul:
            <b>Seysmika asoslari.</b>
            """,
        },
    ],
}


# ============================================================
# QUIZ
# Q091-Q105
# ============================================================

LEVEL08_MODULE07_QUIZ = {
    "L08_M07_001": [
        {
            "code": "L08_Q091",
            "question": "Issiqlik izolyatsiyasi building envelope orqali issiqlik almashinuvini boshqarishga yordam beradimi?",
            "explanation": (
                "Izolyatsiya bino ichki va tashqi muhiti orasidagi issiqlik almashinuvini kamaytirishga yordam beradi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L08_Q092",
            "question": "Issiqlik himoyasi faqat izolyatsiya qalinligini oshirishdan iboratmi?",
            "explanation": (
                "Material, uzluksizlik, tutashuvlar va umumiy detail ham muhim."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L08_Q093",
            "question": "Arxitektor building envelope'ni uzluksiz tizim sifatida tushunishi kerakmi?",
            "explanation": (
                "Bu turli qobiq elementlarini bir-biriga to'g'ri ulash uchun muhim."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L08_M07_002": [
        {
            "code": "L08_Q094",
            "question": "Devor va tomdagi izolyatsiya qatlamlari o'zaro uzluksiz tutashishi kerakmi?",
            "explanation": (
                "Building envelope'dagi himoya qatlamlarining uzluksizligi muhim."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L08_Q095",
            "question": "Deraza atrofi issiqlik himoyasi uchun kritik tutashuv bo'lishi mumkinmi?",
            "explanation": (
                "Frame va devor qatlamlari uchrashadigan joyda uzilishlar paydo bo'lishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L08_Q096",
            "question": "Parapet zonasida devor va tom izolyatsiyasi uzilib qolsa bu muammo emasmi?",
            "explanation": (
                "Izolyatsiya continuity buzilishi issiqlik himoyasiga salbiy ta'sir qilishi mumkin."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
    ],

    "L08_M07_003": [
        {
            "code": "L08_Q097",
            "question": "Thermal bridge issiqlik oqimi kuchayishi mumkin bo'lgan lokal zona hisoblanadimi?",
            "explanation": (
                "Thermal bridge bino qobig'idagi lokal issiqlik uzatish yo'li bo'lishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L08_Q098",
            "question": "Balkon-plita tutashuvi thermal bridge zonasi bo'lishi mumkinmi?",
            "explanation": (
                "Ichki konstruktiv plitaning tashqi zonaga davom etishi alohida tekshiriladigan holatdir."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L08_Q099",
            "question": "Thermal bridge ta'sirini aniq baholash uchun texnik hisob umuman kerak emasmi?",
            "explanation": (
                "Aniq baholash tegishli texnik tahlil va hisoblar bilan amalga oshiriladi."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
    ],

    "L08_M07_004": [
        {
            "code": "L08_Q100",
            "question": "Deraza frame'i va devor qatlamlari o'zaro koordinatsiya qilinadimi?",
            "explanation": (
                "Deraza o'rnatish zonasi building envelope'ning muhim detalidir."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L08_Q101",
            "question": "Balkon-plita tutashuvi faqat konstruktiv masalami?",
            "explanation": (
                "Bu zona konstruksiya bilan birga issiqlik va gidroizolyatsiya masalalarini ham birlashtiradi."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L08_Q102",
            "question": "Parapetda tom va devor izolyatsiyasining mantiqiy tutashuvi tekshiriladimi?",
            "explanation": (
                "Parapet building envelope continuity uchun kritik zona bo'lishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L08_M07_005": [
        {
            "code": "L08_Q103",
            "question": "Issiqlik izolyatsiyasi auditida building envelope continuity tekshiriladimi?",
            "explanation": (
                "Professional audit himoya qatlamlarining butun bino bo'ylab uzluksizligini tekshiradi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L08_Q104",
            "question": "Plan va kesimdagi wall build-up bir-biridan farq qilsa bu koordinatsiya muammosi bo'lishi mumkinmi?",
            "explanation": (
                "Turli loyiha ko'rinishlari bir xil konstruktiv va qatlam ma'lumotini ifodalashi kerak."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L08_Q105",
            "question": "Issiqlik izolyatsiyasi bilan professional ishlashdagi to'g'ri umumiy workflow qaysi?",
            "explanation": (
                "Avval building envelope aniqlanadi, himoya qatlamlari uzluksizligi tekshiriladi, thermal bridge va tutashuvlar koordinatsiya qilinadi, so'ng BIM audit bajariladi."
            ),
            "options": [
                (
                    "A",
                    "Envelope → insulation continuity → thermal bridge → openings/tutashuvlar → BIM audit",
                    True,
                ),
                (
                    "B",
                    "Faqat izolyatsiya qalinligini tanlash → tutashuvlarni tekshirmaslik → audit qilmaslik",
                    False,
                ),
            ],
        },
    ],
}


# ============================================================
# DATABASE SEED
# ============================================================

def seed_level08_module07():
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
        ) in LEVEL08_MODULE07_LESSONS:

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
