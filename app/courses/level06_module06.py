from database.database import get_connection


# ============================================================
# LEVEL 6
# MODULE 06 - ROOF TOOL
# ============================================================

LEVEL06_MODULE06_LESSONS = [
    (
        "L06_M06",
        "L06_M06_001",
        "Roof Tool asoslari",
        "theory",
        "Archicadda tom elementi, roof pitch va asosiy geometriya mantig'ini tushunish.",
        1,
        60,
        20,
    ),
    (
        "L06_M06",
        "L06_M06_002",
        "Single-plane va Multi-plane Roof",
        "theory",
        "Bir tekislikli va ko'p tekislikli tomlar o'rtasidagi farq va qo'llanishini tushunish.",
        2,
        65,
        20,
    ),
    (
        "L06_M06",
        "L06_M06_003",
        "Pitch, overhang va tom konturi",
        "practice",
        "Tom qiyaligi, chiqishi va konturini loyiha geometriyasiga mos boshqarish.",
        3,
        70,
        20,
    ),
    (
        "L06_M06",
        "L06_M06_004",
        "Murakkab tom tutashuvlari",
        "practice",
        "Bir nechta roof tekisliklari, turli hajmlar va tom kesishmalarini nazorat qilish.",
        4,
        80,
        20,
    ),
    (
        "L06_M06",
        "L06_M06_005",
        "Roof professional audit",
        "practice",
        "Tom geometriyasi, pitch, overhang, tutashuvlar va 3D natijani kompleks tekshirish.",
        5,
        85,
        25,
    ),
]


# ============================================================
# CONTENT
# ============================================================

LEVEL06_MODULE06_CONTENT = {
    "L06_M06_001": [
        {
            "title": "Roof Tool nima?",
            "type": "highlight",
            "text": """
            Roof Tool —
            Archicadda tom
            geometriyasini BIM model
            sifatida yaratish uchun
            ishlatiladigan asosiy vosita.

            <br><br>

            Tom faqat
            yuqoridan yopuvchi
            dekorativ shakl emas.

            <br><br>

            U binoning:

            <br><br>

            • hajmiga;<br>
            • fasadiga;<br>
            • kesimiga;<br>
            • umumiy arxitektura obraziga

            <br><br>

            kuchli ta'sir qiladi.
            """,
        },
        {
            "title": "Roof pitch",
            "type": "normal",
            "text": """
            Pitch —
            tom tekisligining
            qiyalik darajasini
            ifodalaydi.

            <br><br>

            Pitch o'zgarsa:

            <br><br>

            • ridge balandligi;<br>
            • tom hajmi;<br>
            • fasad ko'rinishi;<br>
            • ichki tom osti hajmi

            <br><br>

            ham o'zgarishi mumkin.
            """,
        },
        {
            "title": "Tomni plandan emas, hajmdan o'ylang",
            "type": "highlight",
            "text": """
            Roof Tool bilan ishlaganda
            faqat Floor Plandagi
            konturga qaramang.

            <br><br>

            Tomni 3D hajm
            sifatida tasavvur qiling.
            """,
        },
        {
            "title": "Tasavvur qiling",
            "type": "example",
            "text": """
            Planda uy
            L shaklida.

            <br><br>

            Agar tom oddiy
            to'rtburchak shaklda
            o'ylansa,

            <br><br>

            tom va bino geometriyasi
            bir-biriga mos kelmasligi mumkin.

            <br><br>

            Demak tom
            uy hajmiga javob berishi kerak.
            """,
        },
        {
            "title": "Tom va fasad",
            "type": "normal",
            "text": """
            Roof pitch
            va tom balandligi

            <br><br>

            fasad proporsiyasini
            sezilarli o'zgartiradi.

            <br><br>

            Shu sabab tomni
            faqat texnik yopma
            sifatida ko'rmang.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Oddiy to'rtburchak
            uy hajmini oling.

            <br><br>

            Shu uy uchun
            3 xil tom variantini
            tasavvur qiling:

            <br><br>

            1. past pitch;<br>
            2. o'rtacha pitch;<br>
            3. balandroq pitch.

            <br><br>

            Fasad xarakteri
            qanday o'zgarishini
            solishtiring.
            """,
        },
    ],

    "L06_M06_002": [
        {
            "title": "Single-plane Roof",
            "type": "highlight",
            "text": """
            Single-plane Roof —
            bitta asosiy tom
            tekisligi bilan
            ishlashga imkon beradi.

            <br><br>

            Bu usul
            individual tekislikni
            aniq boshqarish kerak
            bo'lgan holatlarda foydali.
            """,
        },
        {
            "title": "Multi-plane Roof",
            "type": "normal",
            "text": """
            Multi-plane Roof —
            bir-biriga bog'langan
            bir nechta tom tekisligini

            <br><br>

            yagona tom sistemi
            sifatida tashkil qilishga
            yordam beradi.
            """,
        },
        {
            "title": "Qaysi biri yaxshi?",
            "type": "warning",
            "text": """
            Single-plane
            yoki Multi-plane'dan

            <br><br>

            biri har doim
            boshqasidan yaxshi emas.

            <br><br>

            Tanlov tom geometriyasi
            va boshqaruv vazifasiga
            bog'liq.
            """,
        },
        {
            "title": "Oddiy uy misoli",
            "type": "example",
            "text": """
            Oddiy to'rt tomonga
            qiyalangan uy tomida

            <br><br>

            Multi-plane Roof
            qulay workflow
            berishi mumkin.
            """,
        },
        {
            "title": "Murakkab hajm misoli",
            "type": "example",
            "text": """
            Asosiy uyga
            pastroq qo'shimcha hajm
            biriktirilgan.

            <br><br>

            Ayrim hollarda
            tom qismlarini
            alohida nazorat qilish
            kerak bo'lishi mumkin.

            <br><br>

            Bunday vaziyatda
            individual roof plane
            mantig'i muhimlashadi.
            """,
        },
        {
            "title": "3D nazorat",
            "type": "highlight",
            "text": """
            Roof turini tanlagandan keyin
            3D ko'rinishda tekshiring:

            <br><br>

            • qiyaliklar;<br>
            • ridge;<br>
            • valley;<br>
            • eave;<br>
            • turli hajmlar tutashuvi.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Bir xil uy uchun:

            <br><br>

            1. Single-plane asosida;<br>
            2. Multi-plane asosida

            <br><br>

            tom yaratish workflowini
            solishtiring.

            <br><br>

            Qaysi usulda
            nazorat qulayroq ekanini
            tahlil qiling.
            """,
        },
    ],

    "L06_M06_003": [
        {
            "title": "Tom konturi",
            "type": "highlight",
            "text": """
            Tom konturi
            bino tashqi chegarasiga
            bog'liq bo'lishi mumkin,

            <br><br>

            lekin har doim
            devor konturining
            aynan nusxasi emas.
            """,
        },
        {
            "title": "Overhang",
            "type": "normal",
            "text": """
            Overhang —
            tomning devor
            tashqarisiga chiqib
            turadigan qismi.

            <br><br>

            U fasad,
            soyalanish
            va tom obraziga
            ta'sir qiladi.
            """,
        },
        {
            "title": "Bir xil overhang",
            "type": "normal",
            "text": """
            Oddiy tomlarda
            overhangni bir xil
            boshqarish mumkin.

            <br><br>

            Lekin murakkab fasadda
            turli qismlar
            alohida nazorat
            talab qilishi mumkin.
            """,
        },
        {
            "title": "Pitch o'zgarsa nima bo'ladi?",
            "type": "highlight",
            "text": """
            Pitch oshsa yoki kamayса:

            <br><br>

            ridge balandligi
            va tomning umumiy
            hajmi ham o'zgaradi.

            <br><br>

            Shu sabab pitchni
            tasodifiy tanlamang.
            """,
        },
        {
            "title": "Fasad bilan tekshiring",
            "type": "example",
            "text": """
            Roof pitch
            Floor Planda yaxshi
            ko'rinishi mumkin.

            <br><br>

            Lekin fasadda
            tom juda baland
            yoki juda past
            ko'rinishi mumkin.

            <br><br>

            Shuning uchun Elevation
            va 3D nazorat zarur.
            """,
        },
        {
            "title": "Tom konturidagi xato",
            "type": "warning",
            "text": """
            Tom konturi
            noto'g'ri chizilsa:

            <br><br>

            • eave noto'g'ri chiqadi;<br>
            • overhang buziladi;<br>
            • fasad asimmetrik ko'rinishi mumkin;<br>
            • boshqa roof qismlari bilan tutashuv buziladi.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Bitta tom yarating.

            <br><br>

            Keyin ketma-ket:

            • pitchni o'zgartiring;<br>
            • overhangni o'zgartiring;<br>
            • kontur burchagini o'zgartiring.

            <br><br>

            Har bir o'zgarishni
            3D va Elevationda
            kuzating.
            """,
        },
    ],

    "L06_M06_004": [
        {
            "title": "Murakkab tom nima?",
            "type": "highlight",
            "text": """
            Murakkab tom —
            faqat ko'p qiyalikli
            tom degani emas.

            <br><br>

            Turli bino hajmlari,
            balandliklari va
            qiyaliklar birlashganda

            <br><br>

            tom tizimi
            murakkablashadi.
            """,
        },
        {
            "title": "Ridge",
            "type": "normal",
            "text": """
            Ridge —
            yuqori tom tekisliklari
            uchrashadigan
            asosiy chiziqlardan biri.

            <br><br>

            Uning joylashuvi
            tom kompozitsiyasiga
            kuchli ta'sir qiladi.
            """,
        },
        {
            "title": "Valley",
            "type": "normal",
            "text": """
            Ikki roof tekisligi
            ichkariga yo'nalgan holda
            tutashganda

            <br><br>

            valley hosil bo'lishi mumkin.

            <br><br>

            Murakkab tomlarda
            bu zonalarni
            aniq tekshirish muhim.
            """,
        },
        {
            "title": "Turli balandlikdagi hajmlar",
            "type": "example",
            "text": """
            Asosiy uy baland.

            <br><br>

            Unga bir qavatli
            pastroq veranda
            biriktirilgan.

            <br><br>

            Ikkala tomni
            bitta pitch va
            bitta balandlik bilan
            majburan yechish

            <br><br>

            yaxshi natija
            bermasligi mumkin.
            """,
        },
        {
            "title": "Tomlar bir-birini kesmasin",
            "type": "warning",
            "text": """
            Bir nechta Roof
            yaratganda

            <br><br>

            3Dda ular
            bir-birining ichidan
            noto'g'ri o'tib ketishi mumkin.

            <br><br>

            Faqat Plan'ga qarab
            xulosa qilmang.
            """,
        },
        {
            "title": "Section nazorati",
            "type": "highlight",
            "text": """
            Murakkab tomda
            Section juda foydali.

            <br><br>

            U orqali:

            <br><br>

            • roof elevation;<br>
            • pitch;<br>
            • ridge height;<br>
            • wall-roof relation

            <br><br>

            tekshiriladi.
            """,
        },
        {
            "title": "Hajmlar ierarxiyasi",
            "type": "normal",
            "text": """
            Har bir kichik hajmga
            alohida dramatik roof
            berish shart emas.

            <br><br>

            Asosiy roof
            va ikkilamchi rooflar
            o'rtasida

            <br><br>

            vizual ierarxiya
            bo'lishi mumkin.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            L shaklidagi
            uy hajmini oling.

            <br><br>

            Asosiy blok uchun
            bir roof,

            <br><br>

            ikkilamchi blok uchun
            boshqa roof yarating.

            <br><br>

            Ridge va valley
            joylarini 3Dda
            tahlil qiling.
            """,
        },
    ],

    "L06_M06_005": [
        {
            "title": "Roof professional audit",
            "type": "highlight",
            "text": """
            Endi tomni
            faqat bino ustidagi
            geometriya sifatida emas,

            <br><br>

            butun arxitektura
            kompozitsiyasining
            muhim qismi sifatida
            tekshiramiz.
            """,
        },
        {
            "title": "1. Roof geometriyasi",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • tom bino hajmiga mosmi?<br>
            • konturlar to'g'rimi?<br>
            • keraksiz roof planes yo'qmi?
            """,
        },
        {
            "title": "2. Pitch",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • pitch mantiqiymi?<br>
            • turli tom qismlari bir-biriga mosmi?<br>
            • roof height fasadga mosmi?
            """,
        },
        {
            "title": "3. Overhang",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • overhang tartiblimi?<br>
            • fasadda tasodifiy farqlar yo'qmi?<br>
            • eave chiziqlari bir-biriga mosmi?
            """,
        },
        {
            "title": "4. Tutashuvlar",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • ridge to'g'rimi?<br>
            • valley to'g'rimi?<br>
            • rooflar bir-birini kesmayaptimi?<br>
            • turli balandlikdagi bloklar to'g'ri ulanadimi?
            """,
        },
        {
            "title": "5. Wall va Roof aloqasi",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • devorlar tomga yetib boryaptimi?<br>
            • devorlar tomdan ortiqcha chiqib ketmaganmi?<br>
            • sectionda vertikal aloqa to'g'rimi?
            """,
        },
        {
            "title": "6. Barcha ko'rinishlar",
            "type": "highlight",
            "text": """
            Roof auditni:

            <br><br>

            • Floor Plan;<br>
            • 3D;<br>
            • Section;<br>
            • Elevation

            <br><br>

            orqali bajaring.

            <br><br>

            Bitta ko'rinish
            barcha xatolarni
            ko'rsatmaydi.
            """,
        },
        {
            "title": "Xatoni toping",
            "type": "warning",
            "text": """
            Uy Floor Planda
            yaxshi ko'rinadi.

            <br><br>

            Lekin 3Dda:

            <br><br>

            • asosiy roof juda baland;<br>
            • veranda roofi devor ichiga kirgan;<br>
            • ikki roof bir-birini kesgan;<br>
            • overhanglar turlicha;<br>
            • ridge markazdan siljigan.

            <br><br>

            Muammo:

            <br><br>

            tom chizilgan,
            lekin professional
            audit qilinmagan.
            """,
        },
        {
            "title": "Professional checklist",
            "type": "example",
            "text": """
            Roofni tekshiring:

            <br><br>

            <b>1.</b> Kontur to'g'rimi?<br><br>
            <b>2.</b> Pitch mantiqiymi?<br><br>
            <b>3.</b> Overhang tartiblimi?<br><br>
            <b>4.</b> Ridge va valley to'g'rimi?<br><br>
            <b>5.</b> Rooflar to'g'ri tutashganmi?<br><br>
            <b>6.</b> Wall-Roof aloqasi to'g'rimi?<br><br>
            <b>7.</b> Plan, 3D, Section va Elevation tekshirildimi?
            """,
        },
        {
            "title": "Modul yakuni",
            "type": "highlight",
            "text": """
            Siz endi:

            <br><br>

            ✓ Roof Tool mantig'ini tushunasiz;<br>
            ✓ Single-plane va Multi-plane farqini bilasiz;<br>
            ✓ pitchni boshqarasiz;<br>
            ✓ overhangni nazorat qilasiz;<br>
            ✓ murakkab roof tutashuvlarini tahlil qilasiz;<br>
            ✓ 3D va Section orqali tekshirasiz;<br>
            ✓ professional Roof auditini bajarasiz.

            <br><br>

            Keyingi modul:
            <b>Stair Tool.</b>
            """,
        },
    ],
}


# ============================================================
# QUIZ
# Q076-Q090
# ============================================================

LEVEL06_MODULE06_QUIZ = {
    "L06_M06_001": [
        {
            "code": "L06_Q076",
            "question": "Roof Tool Archicadda tom geometriyasini BIM model sifatida yaratish uchun ishlatiladimi?",
            "explanation": (
                "Roof Tool tomning 3D va BIM geometriyasini boshqarishga xizmat qiladi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L06_Q077",
            "question": "Roof pitch tomning umumiy hajmiga ta'sir qilishi mumkinmi?",
            "explanation": (
                "Pitch o'zgarishi ridge balandligi va tom obrazini o'zgartirishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L06_Q078",
            "question": "Tomni faqat Floor Planda tekshirish yetarlimi?",
            "explanation": (
                "Tom uch o'lchamli element bo'lgani uchun 3D, Section va Elevation nazorati ham muhim."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
    ],

    "L06_M06_002": [
        {
            "code": "L06_Q079",
            "question": "Single-plane Roof bitta roof tekisligini alohida boshqarishga yordam beradimi?",
            "explanation": (
                "Single-plane Roof individual tom tekisligini alohida nazorat qilish imkonini beradi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L06_Q080",
            "question": "Multi-plane Roof bir nechta bog'langan roof tekisligini boshqarishi mumkinmi?",
            "explanation": (
                "Multi-plane Roof bir nechta qiyalikni yagona tom sistemi sifatida tashkil qilishga yordam beradi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L06_Q081",
            "question": "Single-plane har qanday roof vazifasi uchun doim eng yaxshi tanlovmi?",
            "explanation": (
                "Roof usuli loyiha geometriyasi va boshqaruv ehtiyojiga qarab tanlanadi."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
    ],

    "L06_M06_003": [
        {
            "code": "L06_Q082",
            "question": "Overhang tomning devordan tashqariga chiqib turadigan qismi bo'lishi mumkinmi?",
            "explanation": (
                "Overhang roof konturi va fasad kompozitsiyasining muhim qismlaridan biridir."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L06_Q083",
            "question": "Pitch o'zgarganda ridge balandligi ham o'zgarishi mumkinmi?",
            "explanation": (
                "Tom qiyaligi umumiy vertikal geometriyaga ta'sir qiladi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L06_Q084",
            "question": "Roof konturini o'zgartirgandan keyin 3D natijani tekshirish kerakmi?",
            "explanation": (
                "Kontur o'zgarishi eave, overhang va tom tutashuvlariga ta'sir qilishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L06_M06_004": [
        {
            "code": "L06_Q085",
            "question": "Murakkab tomlarda ridge va valley zonalarini tekshirish muhimmi?",
            "explanation": (
                "Bu zonalar roof tekisliklari tutashuvining asosiy qismlaridir."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L06_Q086",
            "question": "Turli balandlikdagi bino hajmlariga doim aynan bitta roof balandligi va pitch berish shartmi?",
            "explanation": (
                "Turli hajmlar tom geometriyasida alohida yechim talab qilishi mumkin."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L06_Q087",
            "question": "Murakkab roofni Sectionda tekshirish foydalimi?",
            "explanation": (
                "Section roof elevation, pitch va devor-tom aloqasini ko'rishga yordam beradi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L06_M06_005": [
        {
            "code": "L06_Q088",
            "question": "Roof auditida pitch, overhang va tutashuvlar tekshiriladimi?",
            "explanation": (
                "Bu parametrlar roof geometriyasi va umumiy arxitektura natijasi uchun muhim."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L06_Q089",
            "question": "Floor Planda tom yaxshi ko'rinsa boshqa ko'rinishlarda tekshirmasa ham bo'ladimi?",
            "explanation": (
                "3D, Section va Elevationda Floor Planda ko'rinmaydigan xatolar chiqishi mumkin."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L06_Q090",
            "question": "Roof Tool bilan professional ishlashdagi to'g'ri workflow qaysi?",
            "explanation": (
                "Avval bino hajmi va roof geometriyasi aniqlanadi, so'ng pitch, overhang va tutashuvlar tekshiriladi."
            ),
            "options": [
                (
                    "A",
                    "Hajm → roof turi → pitch/overhang → tutashuv → 3D/Section audit",
                    True,
                ),
                (
                    "B",
                    "Faqat yuqoridan tom konturini chizish",
                    False,
                ),
            ],
        },
    ],
}


# ============================================================
# DATABASE SEED
# ============================================================

def seed_level06_module06():
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
        ) in LEVEL06_MODULE06_LESSONS:

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
