from database.database import get_connection


# ============================================================
# LEVEL 6
# MODULE 05 - COMPLEX PROFILES
# ============================================================

LEVEL06_MODULE05_LESSONS = [
    (
        "L06_M05",
        "L06_M05_001",
        "Complex Profile tushunchasi",
        "theory",
        "Standart geometriya yetarli bo'lmaganda maxsus kesim profillaridan foydalanish mantig'ini tushunish.",
        1,
        50,
        20,
    ),
    (
        "L06_M05",
        "L06_M05_002",
        "Profile Manager bilan ishlash",
        "theory",
        "Profile geometriyasini yaratish, tahrirlash va tartibli boshqarish.",
        2,
        55,
        20,
    ),
    (
        "L06_M05",
        "L06_M05_003",
        "Wall, Beam va Column profillari",
        "practice",
        "Maxsus profilni mos element turiga biriktirish va 3D natijani boshqarish.",
        3,
        60,
        20,
    ),
    (
        "L06_M05",
        "L06_M05_004",
        "Material va geometriya mantig'i",
        "practice",
        "Profil ichidagi geometriya va Building Materiallarni mantiqiy tashkil qilish.",
        4,
        65,
        20,
    ),
    (
        "L06_M05",
        "L06_M05_005",
        "Complex Profile professional audit",
        "practice",
        "Profil nomi, geometriya, material, elementga biriktirish va model natijasini kompleks tekshirish.",
        5,
        70,
        25,
    ),
]


# ============================================================
# CONTENT
# ============================================================

LEVEL06_MODULE05_CONTENT = {
    "L06_M05_001": [
        {
            "title": "Complex Profile nima?",
            "type": "highlight",
            "text": """
            Complex Profile —
            standart to'g'ri to'rtburchak
            yoki oddiy kesim yetarli bo'lmaganda

            <br><br>

            maxsus kesim shaklini
            yaratish imkonini beradigan
            Archicad vositasi.
            """,
        },
        {
            "title": "Qachon kerak bo'ladi?",
            "type": "normal",
            "text": """
            Masalan:

            <br><br>

            • maxsus fasad elementi;<br>
            • murakkab karniz;<br>
            • dekorativ profil;<br>
            • maxsus ustun kesimi;<br>
            • maxsus beam kesimi

            <br><br>

            kabi holatlarda
            Complex Profile foydali bo'lishi mumkin.
            """,
        },
        {
            "title": "Oddiy geometriya yetarlimi?",
            "type": "highlight",
            "text": """
            Har bir element uchun
            Complex Profile yaratish
            shart emas.

            <br><br>

            Agar oddiy Wall,
            Beam yoki Column
            yetarli bo'lsa,

            <br><br>

            ortiqcha murakkablik
            yaratish kerak emas.
            """,
        },
        {
            "title": "Tasavvur qiling",
            "type": "example",
            "text": """
            Fasad bo'ylab
            murakkab shakldagi
            dekorativ karniz ketmoqda.

            <br><br>

            Uni ko'plab
            alohida 3D elementlardan
            yig'ish mumkin.

            <br><br>

            Lekin bitta mantiqiy
            profil sifatida yaratish
            boshqaruvni soddalashtirishi mumkin.
            """,
        },
        {
            "title": "Profil — kesim",
            "type": "normal",
            "text": """
            Complex Profile bilan
            ishlaganda asosiy fikr:

            <br><br>

            siz elementning
            uzunligini emas,

            <br><br>

            uning kesim shaklini
            yaratyapsiz.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Qog'ozda 3 ta kesim chizing:

            <br><br>

            1. oddiy to'rtburchak;<br>
            2. L shaklli;<br>
            3. murakkab dekorativ profil.

            <br><br>

            Qaysi biri uchun
            Complex Profile kerakligini
            aniqlang.
            """,
        },
    ],

    "L06_M05_002": [
        {
            "title": "Profile Manager",
            "type": "highlight",
            "text": """
            Complex Profile yaratish
            va tahrirlash uchun

            <br><br>

            Profile Manager
            asosiy ish joylaridan biridir.
            """,
        },
        {
            "title": "Profil geometriyasi",
            "type": "normal",
            "text": """
            Profil ichida
            kerakli kesim shakli
            chiziladi.

            <br><br>

            Geometriya:

            <br><br>

            • aniq;<br>
            • yopiq;<br>
            • mantiqiy;<br>
            • ortiqcha chiziqlarsiz

            <br><br>

            bo'lishi kerak.
            """,
        },
        {
            "title": "Nomlash",
            "type": "highlight",
            "text": """
            Profil nomi
            uning vazifasini
            tushuntirishi kerak.

            <br><br>

            Masalan:

            Exterior Cornice 01

            <br><br>

            yoki

            Custom Column Square-Detail

            <br><br>

            kabi izchil nomlash
            foydali.
            """,
        },
        {
            "title": "Copy 1, Copy 2...",
            "type": "warning",
            "text": """
            Profil nomlarini:

            <br><br>

            Copy<br>
            Copy 2<br>
            Final<br>
            Final New

            <br><br>

            tarzida yuritish

            <br><br>

            keyinchalik qaysi profil
            qayerda ishlatilganini
            tushunishni qiyinlashtiradi.
            """,
        },
        {
            "title": "Profilni qayta ishlatish",
            "type": "normal",
            "text": """
            To'g'ri yaratilgan
            profilni bir nechta
            mos elementlarda
            qayta ishlatish mumkin.

            <br><br>

            Bu takroriy
            modellashtirishni kamaytiradi.
            """,
        },
        {
            "title": "O'zgartirishdan oldin tekshiring",
            "type": "warning",
            "text": """
            Mavjud profilni
            tahrirlashdan oldin

            <br><br>

            u loyiha ichida
            qayerlarda ishlatilganini
            hisobga olish kerak.

            <br><br>

            Profil o'zgarishi
            bir nechta elementga
            ta'sir qilishi mumkin.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Bitta sodda
            L shaklli profil yarating.

            <br><br>

            Keyin unga
            aniq nom bering.

            <br><br>

            So'ng geometriyani
            bir marta o'zgartirib,
            model natijasini kuzating.
            """,
        },
    ],

    "L06_M05_003": [
        {
            "title": "Profil elementga biriktiriladi",
            "type": "highlight",
            "text": """
            Complex Profile
            o'zi mustaqil bino elementi emas.

            <br><br>

            U mos element turiga
            biriktirilganda
            modelda ishlaydi.
            """,
        },
        {
            "title": "Profile Wall",
            "type": "normal",
            "text": """
            Maxsus kesimli
            devor kerak bo'lsa,

            <br><br>

            profilni Wall
            bilan ishlatish mumkin.
            """,
        },
        {
            "title": "Profile Beam",
            "type": "normal",
            "text": """
            Beam oddiy
            to'rtburchak kesimdan
            farqli shaklda bo'lishi kerak bo'lsa,

            <br><br>

            mos Complex Profile
            foydali bo'lishi mumkin.
            """,
        },
        {
            "title": "Profile Column",
            "type": "normal",
            "text": """
            Ustunning kesimi
            standart shakldan
            murakkabroq bo'lsa,

            <br><br>

            Column uchun
            maxsus profil ishlatilishi mumkin.
            """,
        },
        {
            "title": "Har profil har elementga emas",
            "type": "warning",
            "text": """
            Profil yaratganda
            uning qaysi element turi
            uchun mo'ljallanganini
            hisobga oling.

            <br><br>

            Noto'g'ri foydalanish
            workflowda chalkashlik
            keltirib chiqaradi.
            """,
        },
        {
            "title": "3D natijani tekshiring",
            "type": "highlight",
            "text": """
            Profil kesimda
            to'g'ri ko'rinishi mumkin.

            <br><br>

            Lekin elementga
            biriktirilgandan keyin

            <br><br>

            3D natijani ham
            albatta tekshiring.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Bitta profilni
            mos elementda ishlating.

            <br><br>

            Keyin:

            • Plan;<br>
            • Section;<br>
            • 3D

            <br><br>

            ko'rinishlarida
            natijani solishtiring.
            """,
        },
    ],

    "L06_M05_004": [
        {
            "title": "Profil ichidagi material",
            "type": "highlight",
            "text": """
            Complex Profile
            faqat geometriyadan
            iborat bo'lishi shart emas.

            <br><br>

            Uning qismlari
            Building Materiallar
            bilan bog'lanishi mumkin.
            """,
        },
        {
            "title": "Bir profil — bir nechta material",
            "type": "normal",
            "text": """
            Murakkab profil
            bir nechta material zonasidan
            tashkil topishi mumkin.

            <br><br>

            Masalan:

            <br><br>

            asosiy material +
            dekorativ qism +
            boshqa funksional qatlam.
            """,
        },
        {
            "title": "Material mantiqi",
            "type": "normal",
            "text": """
            Materialni
            faqat rang uchun tanlamang.

            <br><br>

            Oldingi Building Materials
            modulidagi BIM mantig'ini
            saqlang.
            """,
        },
        {
            "title": "Cut grafikasi",
            "type": "highlight",
            "text": """
            Profile Sectionda
            kesilganda

            <br><br>

            materiallar va
            ularning grafik ifodasi
            o'qilishi kerak.
            """,
        },
        {
            "title": "Geometriyani ortiqcha murakkablashtirmang",
            "type": "warning",
            "text": """
            Juda ko'p kichik
            segmentlar va
            keraksiz detallar

            <br><br>

            profilni tahrirlash
            va boshqarishni
            qiyinlashtirishi mumkin.
            """,
        },
        {
            "title": "Model maqsadini unutmang",
            "type": "normal",
            "text": """
            Har bir detal
            model maqsadiga mos
            darajada ishlab chiqilishi kerak.

            <br><br>

            Keraksiz ortiqcha
            murakkablik professional
            model degani emas.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Bitta profil ichida
            ikki material zonasini
            tasavvur qiling.

            <br><br>

            Har bir zona:

            • nima vazifa bajaradi?<br>
            • qaysi Building Materialga tegishli?<br>
            • Sectionda qanday o'qiladi?

            <br><br>

            tahlil qiling.
            """,
        },
    ],

    "L06_M05_005": [
        {
            "title": "Complex Profile audit",
            "type": "highlight",
            "text": """
            Endi profilni
            faqat chiroyli shakl sifatida emas,

            <br><br>

            professional BIM elementi
            sifatida tekshiramiz.
            """,
        },
        {
            "title": "1. Naming",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • profil nomi aniqmi?<br>
            • vazifasi nomidan bilinadimi?<br>
            • Copy va Test profillar qolmaganmi?
            """,
        },
        {
            "title": "2. Geometriya",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • kesim mantiqiymi?<br>
            • ortiqcha segmentlar yo'qmi?<br>
            • tasodifiy bo'shliq yo'qmi?<br>
            • shakl kerakli natijani beryaptimi?
            """,
        },
        {
            "title": "3. Building Materials",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • profil qismlari to'g'ri materialdami?<br>
            • cut grafikasi tushunarlimi?<br>
            • material ma'nosi modelga mosmi?
            """,
        },
        {
            "title": "4. Element assignment",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • profil to'g'ri elementda ishlatilganmi?<br>
            • Wall, Beam yoki Column tanlovi mantiqiymi?<br>
            • profil noto'g'ri elementlarda ishlatilmaganmi?
            """,
        },
        {
            "title": "5. Model natijasi",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • Plan to'g'rimi?<br>
            • Section to'g'rimi?<br>
            • 3D to'g'rimi?<br>
            • tutashuvlar mantiqiymi?
            """,
        },
        {
            "title": "Xatoni toping",
            "type": "warning",
            "text": """
            Fasad karnizi uchun
            Complex Profile yaratilgan.

            <br><br>

            Lekin:

            <br><br>

            • nomi Profile Copy 7;<br>
            • geometriyada keraksiz chiziqlar bor;<br>
            • noto'g'ri Building Material berilgan;<br>
            • 3Dda profil teskari ko'rinadi.

            <br><br>

            Profil mavjud,
            lekin professional
            boshqarilmagan.
            """,
        },
        {
            "title": "Professional checklist",
            "type": "example",
            "text": """
            Complex Profile'ni tekshiring:

            <br><br>

            <b>1.</b> Naming aniqmi?<br><br>
            <b>2.</b> Geometriya tozami?<br><br>
            <b>3.</b> Building Materials to'g'rimi?<br><br>
            <b>4.</b> Element turi to'g'rimi?<br><br>
            <b>5.</b> Plan natijasi to'g'rimi?<br><br>
            <b>6.</b> Section natijasi to'g'rimi?<br><br>
            <b>7.</b> 3D natijasi to'g'rimi?
            """,
        },
        {
            "title": "Modul yakuni",
            "type": "highlight",
            "text": """
            Siz endi:

            <br><br>

            ✓ Complex Profile nima ekanini bilasiz;<br>
            ✓ Profile Manager mantig'ini tushunasiz;<br>
            ✓ maxsus kesim yaratasiz;<br>
            ✓ Wall, Beam va Column profilini tushunasiz;<br>
            ✓ materiallarni profilga bog'laysiz;<br>
            ✓ profil natijasini 3D va Sectionda tekshirasiz;<br>
            ✓ Complex Profile auditini bajarasiz.

            <br><br>

            Keyingi modul:
            <b>Roof Tool.</b>
            """,
        },
    ],
}


# ============================================================
# QUIZ
# Q061-Q075
# ============================================================

LEVEL06_MODULE05_QUIZ = {
    "L06_M05_001": [
        {
            "code": "L06_Q061",
            "question": "Complex Profile maxsus kesim geometriyasini yaratish uchun ishlatilishi mumkinmi?",
            "explanation": (
                "Complex Profile standart kesim yetarli bo'lmagan elementlarda maxsus profil yaratishga yordam beradi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L06_Q062",
            "question": "Har bir oddiy element uchun Complex Profile yaratish shartmi?",
            "explanation": (
                "Oddiy Wall, Beam yoki Column yetarli bo'lsa ortiqcha murakkab profil kerak emas."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L06_Q063",
            "question": "Complex Profile asosan elementning kesim shaklini belgilashga yordam beradimi?",
            "explanation": (
                "Profilning asosiy mantig'i elementning maxsus kesim geometriyasidir."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L06_M05_002": [
        {
            "code": "L06_Q064",
            "question": "Profile Manager Complex Profile yaratish va tahrirlash uchun ishlatiladimi?",
            "explanation": (
                "Profile Manager profil geometriyasini boshqarishning asosiy vositalaridan biridir."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L06_Q065",
            "question": "Profil nomlarini Copy 1, Copy 2 tarzida yuritish professional namingmi?",
            "explanation": (
                "Profil nomi uning vazifasini tushunarli ko'rsatishi ma'qul."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L06_Q066",
            "question": "Mavjud profilni tahrirlash undan foydalangan boshqa elementlarga ham ta'sir qilishi mumkinmi?",
            "explanation": (
                "Qayta ishlatilayotgan profil o'zgarsa unga bog'langan elementlar ham o'zgarishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L06_M05_003": [
        {
            "code": "L06_Q067",
            "question": "Complex Profile Wall, Beam yoki Column kabi elementlarda ishlatilishi mumkinmi?",
            "explanation": (
                "Maxsus profil mos element turlariga biriktirib ishlatilishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L06_Q068",
            "question": "Profil kesimda to'g'ri ko'rinsa 3D natijani tekshirmasa ham bo'ladimi?",
            "explanation": (
                "Profil elementga biriktirilgandan keyin 3D natijani ham tekshirish kerak."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L06_Q069",
            "question": "Profilning qaysi element turi uchun mo'ljallanganini hisobga olish kerakmi?",
            "explanation": (
                "Element turi bilan profil vazifasi mantiqan mos bo'lishi kerak."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L06_M05_004": [
        {
            "code": "L06_Q070",
            "question": "Complex Profile ichida Building Materiallardan foydalanish mumkinmi?",
            "explanation": (
                "Profil qismlari BIM material ma'lumotlari bilan bog'lanishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L06_Q071",
            "question": "Murakkab profilni keraksiz kichik segmentlar bilan to'ldirish har doim yaxshi usulmi?",
            "explanation": (
                "Ortiqcha geometriya profilni boshqarish va tahrirlashni qiyinlashtirishi mumkin."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L06_Q072",
            "question": "Profil materiallarini faqat rangga qarab tanlash yetarlimi?",
            "explanation": (
                "Building Material BIM ma'nosi va grafik natijasi ham hisobga olinadi."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
    ],

    "L06_M05_005": [
        {
            "code": "L06_Q073",
            "question": "Complex Profile auditida naming va geometriya tekshiriladimi?",
            "explanation": (
                "Profilning nomi va kesim geometriyasi professional boshqaruvning asosiy qismlaridir."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L06_Q074",
            "question": "Profilni faqat bitta ko'rinishda tekshirish yetarlimi?",
            "explanation": (
                "Plan, Section va 3D ko'rinishlarda natijani tekshirish foydali."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L06_Q075",
            "question": "Complex Profiles bilan professional ishlashdagi to'g'ri workflow qaysi?",
            "explanation": (
                "Avval vazifa aniqlanadi, profil geometriyasi va materiallari tuziladi, so'ng elementga biriktirilib audit qilinadi."
            ),
            "options": [
                (
                    "A",
                    "Vazifa → profil → material → element → 3D/Section audit",
                    True,
                ),
                (
                    "B",
                    "Har bir element uchun tasodifiy profil yaratish",
                    False,
                ),
            ],
        },
    ],
}


# ============================================================
# DATABASE SEED
# ============================================================

def seed_level06_module05():
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
        ) in LEVEL06_MODULE05_LESSONS:

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
