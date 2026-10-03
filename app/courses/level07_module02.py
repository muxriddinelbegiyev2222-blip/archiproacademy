from database.database import get_connection


# ============================================================
# LEVEL 7
# MODULE 02 - GRAPHIC OVERRIDES
# ============================================================

LEVEL07_MODULE02_LESSONS = [
    (
        "L07_M02",
        "L07_M02_001",
        "Graphic Overrides tushunchasi",
        "theory",
        "Model geometriyasini o'zgartirmasdan elementlarni qoidalar asosida grafik ko'rinishda boshqarish.",
        1,
        40,
        20,
    ),
    (
        "L07_M02",
        "L07_M02_002",
        "Graphic Override Rules",
        "theory",
        "Elementlarni mezonlar orqali aniqlash va ularga grafik override qoidasini berish.",
        2,
        45,
        20,
    ),
    (
        "L07_M02",
        "L07_M02_003",
        "Graphic Override Combination",
        "practice",
        "Bir nechta override qoidalarini maqsadga mos kombinatsiya sifatida boshqarish.",
        3,
        50,
        20,
    ),
    (
        "L07_M02",
        "L07_M02_004",
        "Modelni tahliliy ko'rinishlarda ko'rsatish",
        "practice",
        "Graphic Overrides yordamida loyiha nazorati va tahliliy viewlar yaratish.",
        4,
        50,
        20,
    ),
    (
        "L07_M02",
        "L07_M02_005",
        "Graphic Overrides professional audit",
        "practice",
        "Override mezonlari, qoidalar, kombinatsiyalar va view natijalarini kompleks tekshirish.",
        5,
        55,
        25,
    ),
]


# ============================================================
# CONTENT
# ============================================================

LEVEL07_MODULE02_CONTENT = {
    "L07_M02_001": [
        {
            "title": "Graphic Override nima?",
            "type": "highlight",
            "text": """
            Graphic Override —
            model elementining
            asl geometriyasini
            o'zgartirmasdan,

            <br><br>

            uni ma'lum shartlar
            asosida boshqa
            grafik ko'rinishda
            ko'rsatish imkoniyati.
            """,
        },
        {
            "title": "Model va ko'rinishni ajrating",
            "type": "normal",
            "text": """
            Muhim tushuncha:

            <br><br>

            <b>Model</b> —
            haqiqiy BIM elementlar.

            <br><br>

            <b>Graphic Override</b> —
            shu elementlarning
            ma'lum viewdagi
            grafik ifodasi.
            """,
        },
        {
            "title": "Tasavvur qiling",
            "type": "example",
            "text": """
            Loyihada tashqi
            va ichki devorlar bor.

            <br><br>

            Audit vaqtida
            tashqi devorlarni
            boshqa grafik usulda
            ajratib ko'rmoqchisiz.

            <br><br>

            Devorlarning o'zini
            o'zgartirmasdan

            <br><br>

            Graphic Override orqali
            ularni vizual ajratish
            mumkin.
            """,
        },
        {
            "title": "Nima uchun kerak?",
            "type": "highlight",
            "text": """
            Graphic Overrides:

            <br><br>

            • modelni tekshirish;<br>
            • elementlarni ajratish;<br>
            • xatolarni tezroq topish;<br>
            • tahliliy view yaratish;<br>
            • turli maqsad uchun bir modelni turlicha ko'rsatish

            <br><br>

            imkonini beradi.
            """,
        },
        {
            "title": "Bu materialni almashtirish emas",
            "type": "warning",
            "text": """
            Graphic Override orqali
            element boshqa rangda
            ko'rinsa,

            <br><br>

            bu uning haqiqiy
            Building Material
            yoki Surface parametri
            o'zgardi degani emas.
            """,
        },
        {
            "title": "Bir model — ko'p view",
            "type": "normal",
            "text": """
            Professional BIM workflowda
            bitta model

            <br><br>

            turli maqsadlarda
            turlicha grafik
            ko'rinishga ega
            bo'lishi mumkin.

            <br><br>

            Muhimi —
            modelning o'zi
            yagona va tartibli.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Bir uy modelini oling.

            <br><br>

            Quyidagi savolga javob bering:

            <br><br>

            “Modeldagi devorlarni
            o'zgartirmasdan,
            faqat audit uchun
            ayrim devorlarni qanday
            vizual ajratish mumkin?”

            <br><br>

            Javob:
            Graphic Override
            mantig'i orqali.
            """,
        },
    ],

    "L07_M02_002": [
        {
            "title": "Rule — qoida",
            "type": "highlight",
            "text": """
            Graphic Override Rule
            ikki asosiy savolga
            javob beradi:

            <br><br>

            <b>1.</b> Qaysi elementlar?<br>
            <b>2.</b> Ular qanday ko'rinsin?
            """,
        },
        {
            "title": "Criteria",
            "type": "normal",
            "text": """
            Criteria —
            qaysi elementlarga
            qoida qo'llanishini
            aniqlaydigan mezon.

            <br><br>

            Masalan,
            element turi,
            ma'lum xususiyat
            yoki boshqa BIM ma'lumot
            asosida saralash mumkin.
            """,
        },
        {
            "title": "Avval maqsad",
            "type": "warning",
            "text": """
            Criteria yaratishdan oldin
            maqsad aniq bo'lsin.

            <br><br>

            Masalan:

            “Barcha devorlarni
            bo'yayman”

            <br><br>

            juda umumiy.

            <br><br>

            “Muayyan tekshiruv uchun
            kerakli devor guruhini
            ajrataman”

            <br><br>

            ancha to'g'ri yondashuv.
            """,
        },
        {
            "title": "Override natijasi",
            "type": "highlight",
            "text": """
            Qoida mos kelgan
            elementlarning

            <br><br>

            grafik ifodasini
            vaqtincha o'zgartiradi.

            <br><br>

            Qaysi grafik parametrlar
            override qilinishi
            Archicad versiyasi
            va sozlamalarga
            bog'liq bo'lishi mumkin.
            """,
        },
        {
            "title": "Tasavvur qiling",
            "type": "example",
            "text": """
            Siz faqat
            bir turdagi elementlarni
            audit qilmoqchisiz.

            <br><br>

            Criteria orqali
            aynan shu guruhni
            aniqlaysiz.

            <br><br>

            So'ng ularga
            aniq grafik ifoda berasiz.
            """,
        },
        {
            "title": "Juda keng criteria",
            "type": "warning",
            "text": """
            Criteria noto'g'ri
            yoki juda keng bo'lsa,

            <br><br>

            kerak bo'lmagan
            elementlar ham
            override bo'lishi mumkin.

            <br><br>

            Natijani doimo
            modelda tekshiring.
            """,
        },
        {
            "title": "Juda tor criteria",
            "type": "normal",
            "text": """
            Criteria haddan tashqari
            tor bo'lsa,

            <br><br>

            tekshirilishi kerak
            bo'lgan ayrim elementlar
            qoidaga tushmay qolishi mumkin.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Bitta oddiy
            Graphic Override Rule
            konsepsiyasini tuzing:

            <br><br>

            <b>Maqsad:</b>
            ma'lum element guruhini
            ajratib ko'rsatish.

            <br><br>

            Yozing:

            1. Criteria nima?<br>
            2. Qaysi elementlar tushadi?<br>
            3. Grafik natija qanday bo'ladi?
            """,
        },
    ],

    "L07_M02_003": [
        {
            "title": "Combination nima?",
            "type": "highlight",
            "text": """
            Graphic Override Combination —
            bir yoki bir nechta
            Graphic Override Rule'larni

            <br><br>

            ma'lum maqsad uchun
            birlashtiradigan
            grafik konfiguratsiya.
            """,
        },
        {
            "title": "Rule va Combination farqi",
            "type": "normal",
            "text": """
            <b>Rule</b> —
            bitta grafik qoida.

            <br><br>

            <b>Combination</b> —
            bir nechta qoidalarni
            bir view maqsadi uchun
            birlashtirish usuli.
            """,
        },
        {
            "title": "Masalan",
            "type": "example",
            "text": """
            “MODEL AUDIT”
            degan Combination
            tasavvur qiling.

            <br><br>

            Unda:

            • bir guruh elementlar bir xil grafikada;<br>
            • boshqa guruh boshqa grafikada;<br>
            • qolgan elementlar neytral

            <br><br>

            ko'rsatilishi mumkin.
            """,
        },
        {
            "title": "Maqsadga qarab Combination",
            "type": "normal",
            "text": """
            Har bir Combination
            aniq vazifa uchun
            yaratilgani yaxshi.

            <br><br>

            Masalan:

            • Model Audit;<br>
            • Element Check;<br>
            • Documentation View;<br>
            • Presentation View.

            <br><br>

            Bu nomlar
            namuna xolos —
            universal standart emas.
            """,
        },
        {
            "title": "Juda ko'p qoida",
            "type": "warning",
            "text": """
            Bitta Combination ichiga
            keraksiz juda ko'p
            qoida qo'shilsa,

            <br><br>

            natijani tushunish
            qiyinlashishi mumkin.
            """,
        },
        {
            "title": "Qoidalar o'zaro ta'siri",
            "type": "normal",
            "text": """
            Bir element
            bir nechta mezonga
            mos kelishi mumkin.

            <br><br>

            Shu sabab
            Combination natijasini
            real modelda
            tekshirish muhim.
            """,
        },
        {
            "title": "View bilan bog'lash",
            "type": "highlight",
            "text": """
            Professional workflowda
            ma'lum Graphic Override
            Combination

            <br><br>

            ma'lum View
            maqsadi bilan
            birga ishlatiladi.

            <br><br>

            Shu orqali
            chizmalarni qayta
            tayyorlash kamayadi.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            3 ta Rule
            konsepsiyasini yarating.

            <br><br>

            Keyin ularni
            bitta “AUDIT”
            Combination ichida
            ishlatishni rejalashtiring.

            <br><br>

            Har bir rule
            nimani tekshirishi
            aniq bo'lsin.
            """,
        },
    ],

    "L07_M02_004": [
        {
            "title": "Graphic Overrides — audit vositasi",
            "type": "highlight",
            "text": """
            Graphic Overrides
            faqat chiroyli
            presentation uchun emas.

            <br><br>

            U kuchli
            vizual nazorat
            vositasi ham.
            """,
        },
        {
            "title": "Xatoni ko'z bilan topish",
            "type": "normal",
            "text": """
            Katta modelda
            yuzlab elementlar
            bo'lishi mumkin.

            <br><br>

            Jadvaldan xato
            topish qiyin bo'lsa,

            <br><br>

            elementlarni grafik
            ajratish xatoni
            tezroq ko'rishga
            yordam beradi.
            """,
        },
        {
            "title": "Misol — Layer audit",
            "type": "example",
            "text": """
            Tasavvur qiling:

            <br><br>

            ayrim elementlar
            noto'g'ri Layerda
            qolgan.

            <br><br>

            Tegishli mezonlar
            yordamida ularni
            ajratib ko'rsatish

            <br><br>

            audit jarayonini
            tezlashtirishi mumkin.
            """,
        },
        {
            "title": "Misol — BIM ma'lumot audit",
            "type": "example",
            "text": """
            Ayrim elementlarda
            kerakli BIM ma'lumot
            kiritilmagan.

            <br><br>

            Agar buni criteria orqali
            aniqlash mumkin bo'lsa,

            <br><br>

            Graphic Override
            vizual signal sifatida
            xizmat qilishi mumkin.
            """,
        },
        {
            "title": "Model o'zgarmaydi",
            "type": "highlight",
            "text": """
            Audit View
            boshqa grafikada
            ko'rinsa ham,

            <br><br>

            elementning asl
            model xususiyati
            o'zgartirilmagan bo'lishi mumkin.

            <br><br>

            Bu juda muhim
            BIM prinsipi.
            """,
        },
        {
            "title": "Audit va presentationni aralashtirmang",
            "type": "warning",
            "text": """
            Audit uchun yaratilgan
            kuchli kontrastli
            Graphic Override

            <br><br>

            mijozga beriladigan
            presentation view
            uchun mos bo'lmasligi mumkin.

            <br><br>

            Har bir viewning
            maqsadi alohida.
            """,
        },
        {
            "title": "Bir model, turli savollar",
            "type": "normal",
            "text": """
            Bitta modelga
            turli savollar berish mumkin:

            <br><br>

            • qaysi elementlar tekshirilmagan?<br>
            • qaysi guruh boshqa standartda?<br>
            • qaysi elementlar audit talab qiladi?

            <br><br>

            Graphic Overrides
            bu savollarga
            vizual yordam beradi.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Kichik uy modelida
            bitta audit vazifasini
            tanlang.

            <br><br>

            Masalan:

            “Noto'g'ri guruhdagi
            elementlarni aniqlash.”

            <br><br>

            So'ng shu vazifa uchun
            Graphic Override
            qanday ishlashini
            yozib chiqing.
            """,
        },
    ],

    "L07_M02_005": [
        {
            "title": "Graphic Overrides professional audit",
            "type": "highlight",
            "text": """
            Endi Graphic Overrides
            tizimini

            <br><br>

            Rule → Combination → View

            <br><br>

            zanjiri sifatida
            tekshiramiz.
            """,
        },
        {
            "title": "1. Maqsad",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • bu Graphic Override nima uchun yaratilgan?<br>
            • auditmi?<br>
            • documentationmi?<br>
            • presentationmi?

            <br><br>

            Maqsad noaniq bo'lsa,
            tizim ham chalkashadi.
            """,
        },
        {
            "title": "2. Criteria",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • criteria kerakli elementlarni topyaptimi?<br>
            • ortiqcha elementlar tushmayaptimi?<br>
            • kerakli elementlar tashqarida qolmayaptimi?
            """,
        },
        {
            "title": "3. Graphic natija",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • override ko'rinadimi?<br>
            • farq tushunarlimi?<br>
            • haddan tashqari murakkab grafik yaratilmaganmi?
            """,
        },
        {
            "title": "4. Combination",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • kerakli Rules kiritilganmi?<br>
            • keraksiz Rules yo'qmi?<br>
            • Combination nomi tushunarlimi?
            """,
        },
        {
            "title": "5. View",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • kerakli View to'g'ri Combination bilan ishlayaptimi?<br>
            • audit View va presentation View aralashmaganmi?
            """,
        },
        {
            "title": "6. Modelga ta'sir",
            "type": "normal",
            "text": """
            Tekshiring:

            <br><br>

            grafik ko'rinishni
            o'zgartirish uchun

            <br><br>

            asl BIM parametrlarini
            keraksiz o'zgartirib
            yubormaganmisiz?
            """,
        },
        {
            "title": "Xatoni toping",
            "type": "warning",
            "text": """
            “MODEL CHECK”
            Combination yaratildi.

            <br><br>

            Lekin:

            • criteria juda keng;<br>
            • deyarli barcha elementlar override bo'lgan;<br>
            • qaysi rang nimani anglatishi noma'lum;<br>
            • audit va presentation Rules aralashgan;<br>
            • Combination nomlari tushunarsiz.

            <br><br>

            Graphic Override bor,
            lekin nazorat tizimi
            yo'q.
            """,
        },
        {
            "title": "Professional checklist",
            "type": "example",
            "text": """
            Graphic Overrides tizimini tekshiring:

            <br><br>

            <b>1.</b> Maqsad aniqmi?<br><br>
            <b>2.</b> Criteria to'g'rimi?<br><br>
            <b>3.</b> Grafik natija tushunarlimi?<br><br>
            <b>4.</b> Rules tartiblimi?<br><br>
            <b>5.</b> Combination izchilmi?<br><br>
            <b>6.</b> View bilan to'g'ri bog'langanmi?<br><br>
            <b>7.</b> Modelning asl ma'lumoti saqlanib qolganmi?
            """,
        },
        {
            "title": "Modul yakuni",
            "type": "highlight",
            "text": """
            Siz endi:

            <br><br>

            ✓ Graphic Override mantig'ini tushunasiz;<br>
            ✓ Criteria va Rule vazifasini bilasiz;<br>
            ✓ Override Combination tuzasiz;<br>
            ✓ tahliliy viewlar yaratasiz;<br>
            ✓ modelni vizual audit qilasiz;<br>
            ✓ professional Graphic Override auditini bajarasiz.

            <br><br>

            Keyingi modul:
            <b>Model View Options.</b>
            """,
        },
    ],
}


# ============================================================
# QUIZ
# Q016-Q030
# ============================================================

LEVEL07_MODULE02_QUIZ = {
    "L07_M02_001": [
        {
            "code": "L07_Q016",
            "question": "Graphic Override model geometriyasini o'zgartirmasdan grafik ko'rinishni boshqarishga yordam beradimi?",
            "explanation": (
                "Graphic Overrides model elementlarini ma'lum qoidalar asosida boshqa grafik ko'rinishda ko'rsatishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L07_Q017",
            "question": "Graphic Override orqali element boshqa rangda ko'rinsa uning haqiqiy Building Material'i albatta o'zgargan bo'ladimi?",
            "explanation": (
                "Graphic Override grafik ifodani o'zgartirishi mumkin, elementning asl BIM parametri esa saqlanib qoladi."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L07_Q018",
            "question": "Bitta BIM modelni turli maqsad uchun turli grafik viewlarda ko'rsatish mumkinmi?",
            "explanation": (
                "Professional BIM workflowda bitta model turli audit, hujjat va presentation viewlarida turlicha ifodalanishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L07_M02_002": [
        {
            "code": "L07_Q019",
            "question": "Graphic Override Rule qaysi elementlar tanlanishi va ular qanday ko'rinishini belgilashga xizmat qiladimi?",
            "explanation": (
                "Rule criteria orqali elementlarni aniqlab, ularga grafik override belgilaydi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L07_Q020",
            "question": "Criteria juda keng bo'lsa keraksiz elementlar ham override bo'lishi mumkinmi?",
            "explanation": (
                "Noto'g'ri yoki juda keng criteria kutilmagan elementlarni ham qoidaga kiritishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L07_Q021",
            "question": "Graphic Override yaratishda maqsadni aniqlash shart emasmi?",
            "explanation": (
                "Avval audit yoki grafik vazifa aniqlansa criteria va override natijasini to'g'ri qurish osonlashadi."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
    ],

    "L07_M02_003": [
        {
            "code": "L07_Q022",
            "question": "Graphic Override Combination bir nechta Rule'larni bir maqsad uchun birlashtirishi mumkinmi?",
            "explanation": (
                "Combination ma'lum view yoki tahlil uchun bir nechta override qoidalarini birga ishlatadi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L07_Q023",
            "question": "Rule va Combination aynan bir xil tushunchami?",
            "explanation": (
                "Rule bitta qoida, Combination esa bir yoki bir nechta qoidalarning maqsadli to'plamidir."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L07_Q024",
            "question": "Combination natijasini real modelda tekshirish kerakmi?",
            "explanation": (
                "Qoidalar o'zaro ta'sir qilishi mumkin, shuning uchun yakuniy grafik natija modelda tekshiriladi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L07_M02_004": [
        {
            "code": "L07_Q025",
            "question": "Graphic Overrides model auditida vizual nazorat vositasi sifatida ishlatilishi mumkinmi?",
            "explanation": (
                "Elementlarni grafik ajratish xatolar va noodatiy BIM ma'lumotlarni tezroq aniqlashga yordam berishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L07_Q026",
            "question": "Audit uchun yaratilgan Graphic Override har doim mijoz presentationi uchun ham mosmi?",
            "explanation": (
                "Audit va presentation viewlari turli maqsadga ega, shuning uchun ularning grafikasi ham farq qilishi mumkin."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L07_Q027",
            "question": "Graphic Override orqali modeldagi ma'lum guruhlarni vizual ajratish katta modelni tekshirishni yengillashtirishi mumkinmi?",
            "explanation": (
                "Vizual ajratish katta BIM modeldagi ayrim holatlarni tezroq ko'rishga yordam beradi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L07_M02_005": [
        {
            "code": "L07_Q028",
            "question": "Graphic Overrides auditida criteria, rule va combination tekshiriladimi?",
            "explanation": (
                "Professional audit qaysi elementlar tanlangani, qanday override qo'llangani va qaysi kombinatsiyada ishlatilganini tekshiradi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L07_Q029",
            "question": "Graphic Override maqsadi tushunarsiz bo'lsa ham ko'p Rule yaratish yaxshi amaliyotmi?",
            "explanation": (
                "Avval aniq vazifa belgilanadi, keyin faqat zarur Rules va Combination quriladi."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L07_Q030",
            "question": "Graphic Overrides bilan professional ishlashdagi to'g'ri workflow qaysi?",
            "explanation": (
                "Avval maqsad belgilanadi, keyin criteria va rules yaratiladi, combination tuziladi va viewdagi natija audit qilinadi."
            ),
            "options": [
                (
                    "A",
                    "Maqsad → Criteria → Rule → Combination → View → audit",
                    True,
                ),
                (
                    "B",
                    "Ko'p rang tanlash → modelni o'zgartirish → tekshirmaslik",
                    False,
                ),
            ],
        },
    ],
}


# ============================================================
# DATABASE SEED
# ============================================================

def seed_level07_module02():
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
        ) in LEVEL07_MODULE02_LESSONS:

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
