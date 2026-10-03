from database.database import get_connection


# ============================================================
# LEVEL 7
# MODULE 04 - RENOVATION
# ============================================================

LEVEL07_MODULE04_LESSONS = [
    (
        "L07_M04",
        "L07_M04_001",
        "Renovation tushunchasi",
        "theory",
        "Mavjud bino, buziladigan va yangi elementlarni bitta BIM model ichida boshqarish mantig'ini tushunish.",
        1,
        40,
        20,
    ),
    (
        "L07_M04",
        "L07_M04_002",
        "Renovation Status",
        "theory",
        "Elementlarni Existing, Demolished va New holatlari bo'yicha mantiqan ajratish.",
        2,
        45,
        20,
    ),
    (
        "L07_M04",
        "L07_M04_003",
        "Renovation Filters",
        "practice",
        "Turli loyiha bosqichlarini alohida ko'rsatish uchun Renovation Filter mantig'idan foydalanish.",
        3,
        50,
        20,
    ),
    (
        "L07_M04",
        "L07_M04_004",
        "Rekonstruksiya modeli workflow",
        "practice",
        "O'lchovdan mavjud modelgacha, buzish va yangi loyiha bosqichlarini tartibli BIM workflowda tashkil qilish.",
        4,
        50,
        20,
    ),
    (
        "L07_M04",
        "L07_M04_005",
        "Renovation professional audit",
        "practice",
        "Renovation Status, Filter, model geometriyasi va rekonstruksiya hujjatlarini kompleks tekshirish.",
        5,
        55,
        25,
    ),
]


# ============================================================
# CONTENT
# ============================================================

LEVEL07_MODULE04_CONTENT = {
    "L07_M04_001": [
        {
            "title": "Rekonstruksiya nima?",
            "type": "highlight",
            "text": """
            Rekonstruksiya loyihasida
            biz noldan bo'sh yerda
            bino qurmaymiz.

            <br><br>

            Mavjud bino bilan
            ishlaymiz va uning
            ayrim qismlarini:

            <br><br>

            • saqlaymiz;<br>
            • buzamiz;<br>
            • o'zgartiramiz;<br>
            • yangisini qo'shamiz.
            """,
        },
        {
            "title": "Asosiy muammo",
            "type": "normal",
            "text": """
            Oddiy modelda
            barcha elementlar
            bir xil ko'rinsa,

            <br><br>

            qaysi devor mavjud,
            qaysi biri buziladi,
            qaysi biri yangi ekanini

            <br><br>

            tushunish qiyinlashadi.
            """,
        },
        {
            "title": "Renovation tizimi",
            "type": "highlight",
            "text": """
            Renovation tizimi
            rekonstruksiya modelidagi
            elementlarni

            <br><br>

            ularning loyiha holati
            bo'yicha boshqarishga
            yordam beradi.
            """,
        },
        {
            "title": "Tasavvur qiling",
            "type": "example",
            "text": """
            Eski bir qavatli uy bor.

            <br><br>

            Loyiha bo'yicha:

            • tashqi devorlarning ko'pi saqlanadi;<br>
            • bitta ichki devor buziladi;<br>
            • yangi oshxona devori quriladi;<br>
            • yangi eshik ochiladi.

            <br><br>

            Shu qarorlarning
            barchasi bitta
            rekonstruksiya modelida
            boshqarilishi kerak.
            """,
        },
        {
            "title": "Bitta model prinsipi",
            "type": "normal",
            "text": """
            Professional yondashuvda
            mavjud holat,
            buzish rejasi
            va yangi loyiha

            <br><br>

            uchta butunlay
            alohida model sifatida
            chizilishi shart emas.

            <br><br>

            Ularni bitta
            tartibli BIM model
            orqali boshqarish mumkin.
            """,
        },
        {
            "title": "Muhim qoida",
            "type": "warning",
            "text": """
            Renovation —
            mavjud bino haqidagi
            noto'g'ri ma'lumotni
            tuzatmaydi.

            <br><br>

            Mavjud holat
            avval imkon qadar
            to'g'ri o'rganilishi
            va modellashtirilishi kerak.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Oddiy mavjud uy planini
            tasavvur qiling.

            <br><br>

            10 ta elementdan:

            • qaysilari saqlanadi;<br>
            • qaysilari buziladi;<br>
            • qaysilari yangi bo'ladi

            <br><br>

            degan ro'yxat tuzing.
            """,
        },
    ],

    "L07_M04_002": [
        {
            "title": "Renovation Status",
            "type": "highlight",
            "text": """
            Rekonstruksiya modelida
            elementga uning
            loyiha holatini
            ifodalovchi status beriladi.

            <br><br>

            Asosiy mantiq:

            <br><br>

            • Existing;<br>
            • Demolished;<br>
            • New.
            """,
        },
        {
            "title": "Existing",
            "type": "normal",
            "text": """
            Existing —
            mavjud binoning
            saqlanadigan qismi.

            <br><br>

            Masalan:

            • saqlanadigan tashqi devor;<br>
            • mavjud ustun;<br>
            • saqlanadigan slab;<br>
            • mavjud deraza.
            """,
        },
        {
            "title": "Demolished",
            "type": "normal",
            "text": """
            Demolished —
            loyiha bo'yicha
            olib tashlanadigan
            mavjud element.

            <br><br>

            Masalan:

            • buziladigan devor;<br>
            • olib tashlanadigan eshik;<br>
            • yechiladigan konstruktiv bo'lmagan element.
            """,
        },
        {
            "title": "New",
            "type": "normal",
            "text": """
            New —
            rekonstruksiya davomida
            yangi quriladigan
            yoki o'rnatiladigan element.

            <br><br>

            Masalan:

            • yangi devor;<br>
            • yangi eshik;<br>
            • yangi deraza;<br>
            • yangi qo'shimcha hajm.
            """,
        },
        {
            "title": "Status — grafik bezak emas",
            "type": "warning",
            "text": """
            Renovation Status
            faqat elementni
            boshqa rangda
            ko'rsatish uchun emas.

            <br><br>

            U rekonstruksiya
            loyihasining ma'nosini
            ifodalaydi.
            """,
        },
        {
            "title": "Noto'g'ri status",
            "type": "example",
            "text": """
            Tasavvur qiling:

            <br><br>

            buzilishi kerak bo'lgan
            devorga Existing
            status berilgan.

            <br><br>

            Grafik jihatdan
            chizma chiroyli
            ko'rinishi mumkin.

            <br><br>

            Lekin loyiha ma'lumoti
            noto'g'ri bo'ladi.
            """,
        },
        {
            "title": "Statusni geometriyadan ajrating",
            "type": "highlight",
            "text": """
            Devorning geometriyasi —
            uning shakli va joylashuvi.

            <br><br>

            Renovation Status esa —
            loyiha jarayonidagi
            holati.

            <br><br>

            Bu ikki tushunchani
            aralashtirmang.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            6 ta element yozing:

            <br><br>

            2 ta Existing<br>
            2 ta Demolished<br>
            2 ta New

            <br><br>

            Har biriga
            nima uchun shu status
            berilganini tushuntiring.
            """,
        },
    ],

    "L07_M04_003": [
        {
            "title": "Renovation Filter",
            "type": "highlight",
            "text": """
            Renovation Filter —
            turli statusdagi
            elementlarni

            <br><br>

            ma'lum loyiha
            bosqichiga mos
            ko'rinishda boshqarishga
            yordam beradi.
            """,
        },
        {
            "title": "Nega Filter kerak?",
            "type": "normal",
            "text": """
            Bir vaqtning o'zida
            Existing,
            Demolished
            va New elementlarning

            <br><br>

            barchasini bir xil
            ko'rinishda ko'rsatish
            har doim ham qulay emas.

            <br><br>

            Hujjat maqsadi
            qaysi ma'lumotni
            ko'rsatishni belgilaydi.
            """,
        },
        {
            "title": "Existing holat view",
            "type": "example",
            "text": """
            Mavjud holat
            chizmasida

            <br><br>

            asosiy maqsad —
            rekonstruksiyadan oldingi
            binoni tushuntirish.

            <br><br>

            Shu sabab view
            mavjud holatni
            aniq ko'rsatishi kerak.
            """,
        },
        {
            "title": "Demolition view",
            "type": "example",
            "text": """
            Buzish rejasida
            foydalanuvchi

            <br><br>

            aynan qaysi
            elementlar olib
            tashlanishini

            <br><br>

            tez tushunishi kerak.
            """,
        },
        {
            "title": "New construction view",
            "type": "example",
            "text": """
            Yangi loyiha viewida
            rekonstruksiyadan keyingi
            yechim

            <br><br>

            aniq va tushunarli
            ko'rinishi kerak.
            """,
        },
        {
            "title": "Filter va Status farqi",
            "type": "highlight",
            "text": """
            <b>Status</b> —
            elementning holati.

            <br><br>

            <b>Filter</b> —
            shu holatdagi
            elementlar viewda
            qanday ko'rsatilishini
            boshqarish vositasi.
            """,
        },
        {
            "title": "Filter bilan xatoni yashirmang",
            "type": "warning",
            "text": """
            Agar elementga
            noto'g'ri status berilgan bo'lsa,

            <br><br>

            yaxshi Filter ham
            loyiha ma'lumotini
            to'g'rilamaydi.

            <br><br>

            Avval Status,
            keyin Filter.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            3 ta view
            konsepsiyasi tuzing:

            <br><br>

            1. Existing Plan<br>
            2. Demolition Plan<br>
            3. Proposed Plan

            <br><br>

            Har birida
            qaysi ma'lumot
            asosiy bo'lishini
            yozing.
            """,
        },
    ],

    "L07_M04_004": [
        {
            "title": "Rekonstruksiya workflow",
            "type": "highlight",
            "text": """
            Professional workflow
            odatda quyidagi
            mantiqqa ega:

            <br><br>

            1. mavjud holatni o'rganish;<br>
            2. Existing model yaratish;<br>
            3. buziladigan qismlarni aniqlash;<br>
            4. yangi loyiha elementlarini yaratish;<br>
            5. Statuslarni tekshirish;<br>
            6. kerakli viewlarni tayyorlash.
            """,
        },
        {
            "title": "1. Mavjud holat",
            "type": "normal",
            "text": """
            Rekonstruksiya loyihasi
            mavjud bino haqidagi
            ma'lumotdan boshlanadi.

            <br><br>

            Noto'g'ri existing model
            keyingi barcha
            qarorlarga salbiy
            ta'sir qilishi mumkin.
            """,
        },
        {
            "title": "O'lchov ma'lumoti",
            "type": "warning",
            "text": """
            Real loyihada
            mavjud geometriya
            ishonchli o'lchov,
            mavjud hujjatlar
            va tegishli tekshiruvlarga
            asoslanishi kerak.

            <br><br>

            Taxminiy chizilgan modelni
            fakt sifatida
            qabul qilmang.
            """,
        },
        {
            "title": "2. Buzish qarori",
            "type": "normal",
            "text": """
            Buziladigan element
            tasodifiy tanlanmaydi.

            <br><br>

            U arxitektura,
            konstruksiya,
            muhandislik
            va loyiha vazifasi
            bilan bog'liq bo'lishi mumkin.
            """,
        },
        {
            "title": "Konstruktiv ehtiyotkorlik",
            "type": "warning",
            "text": """
            Devorni modelda
            Demolished qilish

            <br><br>

            real binoda uni
            xavfsiz buzish mumkin
            degani emas.

            <br><br>

            Yuk ko'taruvchi
            yoki konstruktiv
            elementlar bo'yicha
            tegishli mutaxassis
            tekshiruvi talab qilinadi.
            """,
        },
        {
            "title": "3. Yangi loyiha",
            "type": "normal",
            "text": """
            Yangi elementlar
            mavjud bino bilan

            <br><br>

            geometriya,
            funksional aloqa,
            konstruksiya
            va muhandislik
            nuqtayi nazaridan
            uyg'unlashishi kerak.
            """,
        },
        {
            "title": "Door misoli",
            "type": "example",
            "text": """
            Eski eshik
            yopilishi kerak.

            <br><br>

            Yangi joyda
            boshqa eshik
            ochiladi.

            <br><br>

            Bu bitta
            “eshikni ko'chirish”
            emas.

            <br><br>

            BIM ma'nosida:

            • eski eshik — Demolished;<br>
            • yangi eshik — New.
            """,
        },
        {
            "title": "4. Viewlar",
            "type": "normal",
            "text": """
            Yakunda kamida
            loyiha maqsadiga mos
            tushunarli viewlar kerak.

            <br><br>

            Masalan:

            • Existing;<br>
            • Demolition;<br>
            • Proposed.

            <br><br>

            Aniq hujjatlar tarkibi
            loyiha talabi va
            amaldagi me'yorlarga
            qarab belgilanadi.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Oddiy bir xona
            rekonstruksiyasini
            rejalashtiring.

            <br><br>

            Masalan:

            • eski partition buziladi;<br>
            • yangi partition quriladi;<br>
            • eski door yopiladi;<br>
            • yangi door ochiladi.

            <br><br>

            Har bir elementga
            to'g'ri status yozing.
            """,
        },
    ],

    "L07_M04_005": [
        {
            "title": "Renovation professional audit",
            "type": "highlight",
            "text": """
            Rekonstruksiya modelini
            quyidagi zanjir bo'yicha
            tekshiramiz:

            <br><br>

            Existing model
            → Status
            → Filters
            → Views
            → Documentation
            """,
        },
        {
            "title": "1. Existing model",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • mavjud bino to'g'ri modellashtirilganmi?<br>
            • asosiy devor va ochilishlar joyidami?<br>
            • taxminiy ma'lumot fakt sifatida kiritilmaganmi?
            """,
        },
        {
            "title": "2. Status audit",
            "type": "example",
            "text": """
            Har bir tegishli
            element uchun tekshiring:

            <br><br>

            • Existingmi?<br>
            • Demolishedmi?<br>
            • Newmi?

            <br><br>

            Status loyiha
            qaroriga mosmi?
            """,
        },
        {
            "title": "3. Demolition audit",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • buziladigan elementlar aniqmi?<br>
            • saqlanadigan element tasodifan Demolished bo'lmaganmi?<br>
            • konstruktiv xavf bo'lishi mumkin bo'lgan elementlar alohida ko'rib chiqilganmi?
            """,
        },
        {
            "title": "4. New element audit",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • barcha yangi elementlar New statusdami?<br>
            • Existing element tasodifan New bo'lib qolmaganmi?<br>
            • yangi va mavjud geometriya bir-biriga mosmi?
            """,
        },
        {
            "title": "5. Filter audit",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • Existing View tushunarlimi?<br>
            • Demolition View buzishni aniq ko'rsatadimi?<br>
            • Proposed View yakuniy yechimni tushuntiradimi?
            """,
        },
        {
            "title": "6. View audit",
            "type": "normal",
            "text": """
            Faqat Floor Plan emas,

            <br><br>

            loyiha zaruratiga qarab
            Section,
            Elevation
            va boshqa viewlarda ham

            <br><br>

            rekonstruksiya ma'lumotini
            tekshirish kerak bo'lishi mumkin.
            """,
        },
        {
            "title": "Xatoni toping",
            "type": "warning",
            "text": """
            Rekonstruksiya modeli tayyor.

            <br><br>

            Lekin:

            • eski va yangi devorlar aralash;<br>
            • buziladigan devor Existing statusda;<br>
            • yangi door Existing statusda;<br>
            • Demolition Viewda yangi elementlar chalkashtiradi;<br>
            • Proposed Viewda buzilgan element qolib ketgan.

            <br><br>

            Muammo —
            geometriya bor,
            lekin Renovation
            ma'lumotlari audit
            qilinmagan.
            """,
        },
        {
            "title": "Professional checklist",
            "type": "example",
            "text": """
            Renovation loyihasini tekshiring:

            <br><br>

            <b>1.</b> Existing model ishonchlimi?<br><br>
            <b>2.</b> Statuslar to'g'rimi?<br><br>
            <b>3.</b> Demolished elementlar aniqmi?<br><br>
            <b>4.</b> New elementlar to'g'ri belgilanganmi?<br><br>
            <b>5.</b> Filters vazifaga mosmi?<br><br>
            <b>6.</b> Viewlar tushunarlimi?<br><br>
            <b>7.</b> Model va real konstruktiv qarorlar aralashtirilmaganmi?
            """,
        },
        {
            "title": "Modul yakuni",
            "type": "highlight",
            "text": """
            Siz endi:

            <br><br>

            ✓ Renovation mantig'ini tushunasiz;<br>
            ✓ Existing, Demolished va New statuslarini farqlaysiz;<br>
            ✓ Renovation Filter vazifasini bilasiz;<br>
            ✓ rekonstruksiya BIM workflowini tuzasiz;<br>
            ✓ Existing, Demolition va Proposed viewlarni tashkil qilasiz;<br>
            ✓ Renovation modelini professional audit qilasiz.

            <br><br>

            Keyingi modul:
            <b>Schedules.</b>
            """,
        },
    ],
}


# ============================================================
# QUIZ
# Q046-Q060
# ============================================================

LEVEL07_MODULE04_QUIZ = {
    "L07_M04_001": [
        {
            "code": "L07_Q046",
            "question": "Renovation tizimi mavjud, buziladigan va yangi elementlarni bitta BIM modelda boshqarishga yordam beradimi?",
            "explanation": (
                "Renovation rekonstruksiya modelidagi elementlarni loyiha holati bo'yicha boshqarishga yordam beradi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L07_Q047",
            "question": "Rekonstruksiya loyihasida har bir bosqich uchun mutlaqo alohida BIM model yaratish har doim shartmi?",
            "explanation": (
                "Renovation workflow mavjud, buziladigan va yangi holatlarni bitta tartibli model orqali boshqarishga imkon beradi."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L07_Q048",
            "question": "Noto'g'ri Existing model keyingi rekonstruksiya qarorlariga ta'sir qilishi mumkinmi?",
            "explanation": (
                "Mavjud holat modeli noto'g'ri bo'lsa buzish va yangi loyiha qarorlari ham noto'g'ri asosga qurilishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L07_M04_002": [
        {
            "code": "L07_Q049",
            "question": "Existing status saqlanadigan mavjud elementni ifodalashi mumkinmi?",
            "explanation": (
                "Existing rekonstruksiyadan oldin mavjud bo'lgan va saqlanadigan elementlar uchun ishlatiladi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L07_Q050",
            "question": "Demolished status yangi quriladigan elementni anglatadimi?",
            "explanation": (
                "Demolished olib tashlanadigan mavjud elementni, New esa yangi quriladigan elementni ifodalaydi."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L07_Q051",
            "question": "Renovation Status elementning loyiha jarayonidagi holatini ifodalaydimi?",
            "explanation": (
                "Status elementning Existing, Demolished yoki New kabi rekonstruksiya holatini ko'rsatadi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L07_M04_003": [
        {
            "code": "L07_Q052",
            "question": "Renovation Filter turli statusdagi elementlarni view maqsadiga qarab ko'rsatishga yordam beradimi?",
            "explanation": (
                "Filter rekonstruksiya bosqichlariga mos grafik va ko'rinish boshqaruvini tashkil qilishga yordam beradi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L07_Q053",
            "question": "Status va Renovation Filter aynan bir xil tushunchami?",
            "explanation": (
                "Status element holatini bildiradi, Filter esa turli statuslarni viewda qanday ko'rsatishni boshqaradi."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L07_Q054",
            "question": "Noto'g'ri Renovation Status'ni yaxshi Filter avtomatik ravishda to'g'rilaydimi?",
            "explanation": (
                "Filter faqat ko'rinishni boshqaradi; noto'g'ri element statusi alohida tuzatilishi kerak."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
    ],

    "L07_M04_004": [
        {
            "code": "L07_Q055",
            "question": "Rekonstruksiya workflowi mavjud holatni o'rganishdan boshlanishi kerakmi?",
            "explanation": (
                "Ishonchli Existing model keyingi buzish va yangi loyiha qarorlarining asosidir."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L07_Q056",
            "question": "Modelda devorga Demolished status berish uni real binoda xavfsiz buzish mumkinligini avtomatik isbotlaydimi?",
            "explanation": (
                "Renovation status BIM loyiha ma'lumotidir; konstruktiv xavfsizlik tegishli mutaxassislar tomonidan alohida tekshiriladi."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L07_Q057",
            "question": "Eski eshik olib tashlanib boshqa joyga yangi eshik qo'yilsa, eski va yangi eshik alohida rekonstruksiya holatlariga ega bo'lishi mumkinmi?",
            "explanation": (
                "Eski element Demolished, yangi element esa New statusida boshqarilishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L07_M04_005": [
        {
            "code": "L07_Q058",
            "question": "Renovation auditida Existing model, Status, Filter va Viewlar tekshiriladimi?",
            "explanation": (
                "Professional audit butun rekonstruksiya axborot zanjirini tekshiradi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L07_Q059",
            "question": "Proposed Viewda buzib tashlanishi kerak bo'lgan element noto'g'ri qolib ketishi rekonstruksiya xatosi bo'lishi mumkinmi?",
            "explanation": (
                "Yakuniy view rekonstruksiyadan keyingi loyiha holatini aniq ifodalashi kerak."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L07_Q060",
            "question": "Renovation bilan professional ishlashdagi to'g'ri workflow qaysi?",
            "explanation": (
                "Mavjud holat o'rganiladi, Existing model yaratiladi, elementlarga status beriladi, filter va viewlar tayyorlanadi, so'ng audit qilinadi."
            ),
            "options": [
                (
                    "A",
                    "Existing holat → model → Status → Filters → Views → audit",
                    True,
                ),
                (
                    "B",
                    "Tasodifiy buzish → yangi element chizish → status bermaslik → tekshirmaslik",
                    False,
                ),
            ],
        },
    ],
}


# ============================================================
# DATABASE SEED
# ============================================================

def seed_level07_module04():
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
        ) in LEVEL07_MODULE04_LESSONS:

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
