from database.database import get_connection


# ============================================================
# LEVEL 8
# MODULE 03 - KARKAS
# ============================================================

LEVEL08_MODULE03_LESSONS = [
    (
        "L08_M03",
        "L08_M03_001",
        "Karkas konstruktiv tizimi",
        "theory",
        "Ustun va rigellardan tashkil topgan karkas tizimining umumiy ishlash mantig'ini tushunish.",
        1,
        50,
        20,
    ),
    (
        "L08_M03",
        "L08_M03_002",
        "Ustun, rigel va yuk yo'li",
        "theory",
        "Yuklarning plita va boshqa elementlardan rigel, ustun va fundamentga uzatilish mantig'ini tushunish.",
        2,
        55,
        20,
    ),
    (
        "L08_M03",
        "L08_M03_003",
        "Grid, o'qlar va span mantig'i",
        "practice",
        "Karkas elementlarini o'qlar orqali tartibga solish va tayanchlar oralig'i mantig'ini tushunish.",
        3,
        60,
        20,
    ),
    (
        "L08_M03",
        "L08_M03_004",
        "Arxitektura va karkas koordinatsiyasi",
        "practice",
        "Xonalar, fasad, zinapoya, muhandislik tizimlari va karkas elementlarini o'zaro koordinatsiya qilish.",
        4,
        65,
        20,
    ),
    (
        "L08_M03",
        "L08_M03_005",
        "Karkas professional audit",
        "practice",
        "Ustunlar, rigellar, o'qlar, qavatlararo davomiylik va BIM modeldagi konstruktiv karkasni kompleks tekshirish.",
        5,
        70,
        25,
    ),
]


# ============================================================
# CONTENT
# ============================================================

LEVEL08_MODULE03_CONTENT = {
    "L08_M03_001": [
        {
            "title": "Karkas nima?",
            "type": "highlight",
            "text": """
            Karkas —
            binoning asosiy
            yuk ko'taruvchi

            <br><br>

            elementlari
            o'zaro bog'langan
            konstruktiv tizim.
            """,
        },
        {
            "title": "Asosiy elementlar",
            "type": "normal",
            "text": """
            Oddiy karkas
            tushunchasida:

            <br><br>

            • ustunlar;<br>
            • rigellar yoki beamlar;<br>
            • plitalar;<br>
            • fundament

            <br><br>

            birgalikda ishlaydi.
            """,
        },
        {
            "title": "Ustunning vazifasi",
            "type": "normal",
            "text": """
            Ustun
            yuqoridan kelayotgan
            yuklarni

            <br><br>

            pastdagi konstruktiv
            tizimga uzatadi.
            """,
        },
        {
            "title": "Rigelning vazifasi",
            "type": "normal",
            "text": """
            Rigel yoki beam
            gorizontal yo'nalishda

            <br><br>

            yuklarni tayanchlarga
            uzatishda ishtirok etadi.
            """,
        },
        {
            "title": "Karkas va devor",
            "type": "highlight",
            "text": """
            Karkasli binoda
            asosiy yuklarni

            <br><br>

            ustun va rigellar
            ko'tarishi mumkin.

            <br><br>

            Devorlarning bir qismi
            esa to'ldiruvchi
            vazifada ishlashi mumkin.
            """,
        },
        {
            "title": "Karkas faqat ustunlar emas",
            "type": "warning",
            "text": """
            Faqat bir nechta
            ustun chizish

            <br><br>

            professional
            karkas tizimi
            degani emas.

            <br><br>

            Ularning o'zaro
            ishlash mantig'i
            bo'lishi kerak.
            """,
        },
        {
            "title": "Tasavvur qiling",
            "type": "example",
            "text": """
            Katta ochiq
            mehmonxona kerak.

            <br><br>

            Ichkarida ko'p
            yuk ko'taruvchi
            devor bo'lishini
            xohlamaysiz.

            <br><br>

            Karkas tizimi
            arxitekturada
            ko'proq erkinlik
            berishi mumkin.
            """,
        },
        {
            "title": "Arxitektor uchun ahamiyati",
            "type": "highlight",
            "text": """
            Arxitektor
            karkasni tushunsa:

            <br><br>

            • xonalarni yaxshiroq rejalaydi;<br>
            • ustun joyini oldindan hisobga oladi;<br>
            • fasadni koordinatsiya qiladi;<br>
            • konstruktor bilan tezroq ishlaydi.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Oddiy karkas sxemasini
            tasavvur qiling.

            <br><br>

            Yuk yo'lini yozing:

            <br><br>

            plita
            → rigel
            → ustun
            → fundament.
            """,
        },
    ],

    "L08_M03_002": [
        {
            "title": "Yuk yo'li",
            "type": "highlight",
            "text": """
            Karkasdagi
            har bir element

            <br><br>

            yuk uzatish
            zanjirining
            bir qismi.
            """,
        },
        {
            "title": "Plitadan rigelga",
            "type": "normal",
            "text": """
            Plitadagi yuklar
            konstruktiv sxemaga qarab

            <br><br>

            rigel,
            devor
            yoki boshqa tayanchlarga

            <br><br>

            uzatilishi mumkin.
            """,
        },
        {
            "title": "Rigeldan ustunga",
            "type": "normal",
            "text": """
            Rigel
            qabul qilgan yuklarni

            <br><br>

            ustunlarga
            uzatadi.
            """,
        },
        {
            "title": "Ustundan fundamentga",
            "type": "normal",
            "text": """
            Ustun yuklari
            pastga davom etib

            <br><br>

            fundament orqali
            gruntga uzatiladi.
            """,
        },
        {
            "title": "Ustun davomiyligi",
            "type": "highlight",
            "text": """
            Ko'p qavatli binoda
            ustunlarning

            <br><br>

            qavatlar bo'yicha
            mantiqiy davom etishi

            <br><br>

            yuk yo'lini
            tushunarli qiladi.
            """,
        },
        {
            "title": "Siljigan ustun",
            "type": "warning",
            "text": """
            Yuqori qavatdagi
            ustun

            <br><br>

            pastdagi ustundan
            keskin siljigan bo'lsa,

            <br><br>

            qo'shimcha konstruktiv
            yechim talab qilinishi
            mumkin.
            """,
        },
        {
            "title": "Tasavvur qiling",
            "type": "example",
            "text": """
            2-qavat ustuni
            pastdagi katta
            mehmonxona markaziga
            tushib qoldi.

            <br><br>

            Uni shunchaki
            yo'q qilish mumkin emas.

            <br><br>

            Konstruktiv yechim
            qayta ko'rib chiqiladi.
            """,
        },
        {
            "title": "Yuk yo'lidagi uzilish",
            "type": "warning",
            "text": """
            Agar yuk
            qayerdan qayerga
            o'tayotgani

            <br><br>

            tushunarsiz bo'lsa,

            <br><br>

            loyiha koordinatsiyasi
            yetarli emas.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Ikki qavatli
            karkasli uy uchun

            <br><br>

            bitta ustunni tanlang
            va uning yuk yo'lini

            <br><br>

            tomdan fundamentgacha
            yozing.
            """,
        },
    ],

    "L08_M03_003": [
        {
            "title": "Grid va o'qlar",
            "type": "highlight",
            "text": """
            Grid yoki o'qlar
            karkas elementlarini

            <br><br>

            tartibli koordinatsiya
            qilish uchun
            asosiy vositalardan biri.
            """,
        },
        {
            "title": "Ustun va o'q",
            "type": "normal",
            "text": """
            Ustunlar
            tartibli o'qlar

            <br><br>

            bo'yicha
            joylashtirilsa,

            <br><br>

            konstruktiv va
            arxitektura koordinatsiyasi
            osonlashadi.
            """,
        },
        {
            "title": "Span nima?",
            "type": "highlight",
            "text": """
            Span —
            ikki tayanch

            <br><br>

            orasidagi
            konstruktiv masofa
            tushunchasi.
            """,
        },
        {
            "title": "Span kattalashsa",
            "type": "normal",
            "text": """
            Tayanchlar oralig'i
            kattalashgani sari

            <br><br>

            konstruktiv elementlarga
            qo'yiladigan talablar
            o'zgarishi mumkin.

            <br><br>

            Aniq yechim
            hisob bilan belgilanadi.
            """,
        },
        {
            "title": "Arxitektura va span",
            "type": "example",
            "text": """
            Mijoz katta
            ustunsiz xona xohladi.

            <br><br>

            Bu faqat
            interyer qarori emas.

            <br><br>

            Katta span
            konstruktiv yechimga
            ta'sir qiladi.
            """,
        },
        {
            "title": "Tasodifiy grid",
            "type": "warning",
            "text": """
            Har bir xonaga
            alohida tasodifiy

            <br><br>

            ustun qo'yish
            karkasni tartibsiz
            qilishi mumkin.
            """,
        },
        {
            "title": "Gridning foydasi",
            "type": "normal",
            "text": """
            Tartibli grid:

            <br><br>

            • ustunlarni muvofiqlashtiradi;<br>
            • fasad modullarini tartiblaydi;<br>
            • plita va rigel sxemasini tushunarli qiladi;<br>
            • o'lcham va chizmalarni soddalashtiradi.
            """,
        },
        {
            "title": "Grid ham mutlaq emas",
            "type": "warning",
            "text": """
            Grid tartibli
            bo'lishi kerak,

            <br><br>

            lekin arxitekturani
            mantiqsiz ravishda
            faqat gridga
            bo'ysundirish ham

            <br><br>

            yaxshi loyiha
            degani emas.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Oddiy to'rtburchak
            uy uchun

            <br><br>

            o'qlar konsepsiyasini
            chizing.

            <br><br>

            Keyin:

            • ustunlar qayerda;<br>
            • asosiy spanlar qayerda

            <br><br>

            ekanini belgilang.
            """,
        },
    ],

    "L08_M03_004": [
        {
            "title": "Karkas va arxitektura",
            "type": "highlight",
            "text": """
            Professional loyiha
            arxitektura tayyor bo'lgach

            <br><br>

            keyin ustun qo'yish
            jarayoni emas.

            <br><br>

            Karkas boshidan
            arxitektura bilan
            birga o'ylanadi.
            """,
        },
        {
            "title": "Ustun va xona",
            "type": "normal",
            "text": """
            Ustunlar
            xonaning:

            <br><br>

            • harakat yo'liga;<br>
            • mebel joylashuviga;<br>
            • eshik va derazaga;<br>
            • umumiy kompozitsiyaga

            <br><br>

            ta'sir qilishi mumkin.
            """,
        },
        {
            "title": "Ustun va fasad",
            "type": "normal",
            "text": """
            Fasad oynalari
            va ustunlar

            <br><br>

            o'zaro koordinatsiya
            qilinmasa,

            <br><br>

            fasad ritmi
            va konstruktiv grid
            bir-biriga zid
            bo'lishi mumkin.
            """,
        },
        {
            "title": "Ustun va eshik",
            "type": "warning",
            "text": """
            Eshik joylashtirilgan
            nuqtada ustun chiqib qolsa,

            <br><br>

            bu modeldagi
            oddiy geometrik
            to'qnashuv emas.

            <br><br>

            Loyiha boshidan
            koordinatsiya
            yetarli bo'lmagan.
            """,
        },
        {
            "title": "Zinapoya va karkas",
            "type": "normal",
            "text": """
            Zinapoya bo'shlig'i
            plita,
            rigel
            va ustunlar bilan

            <br><br>

            koordinatsiyada
            hal qilinadi.
            """,
        },
        {
            "title": "MEP va karkas",
            "type": "warning",
            "text": """
            Ventilyatsiya,
            kanalizatsiya
            yoki boshqa
            kommunikatsiyalar

            <br><br>

            rigel yoki ustun
            bilan to'qnashsa,

            <br><br>

            ularni tasodifiy
            kesib o'tish
            mumkin emas.
            """,
        },
        {
            "title": "Balandlik koordinatsiyasi",
            "type": "normal",
            "text": """
            Rigel balandligi
            shift,
            eshik,
            deraza
            va MEP tizimlariga

            <br><br>

            ta'sir qilishi mumkin.
            """,
        },
        {
            "title": "BIM koordinatsiya",
            "type": "highlight",
            "text": """
            Karkasni:

            <br><br>

            • plan;<br>
            • kesim;<br>
            • fasad;<br>
            • 3D

            <br><br>

            orqali birgalikda
            tekshiring.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Bitta ustunni
            tanlang.

            <br><br>

            U bilan bog'liq
            5 ta arxitektura
            koordinatsiya savolini
            yozing.

            <br><br>

            Masalan:

            • eshikka halal bermaydimi?<br>
            • fasadga mosmi?
            """,
        },
    ],

    "L08_M03_005": [
        {
            "title": "Karkas professional audit",
            "type": "highlight",
            "text": """
            Audit zanjiri:

            <br><br>

            Grid
            → Ustun
            → Rigel
            → Plita
            → Yuk yo'li
            → Fundament
            → Arxitektura
            → BIM audit
            """,
        },
        {
            "title": "1. Grid audit",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • o'qlar tushunarlimi?<br>
            • naming izchilmi?<br>
            • ustunlar gridga mosmi?
            """,
        },
        {
            "title": "2. Ustun audit",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • ustunlar qavatlar bo'yicha davom etadimi?<br>
            • tasodifiy siljishlar bormi?<br>
            • arxitektura bilan to'qnashuv bormi?
            """,
        },
        {
            "title": "3. Rigel audit",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • rigellar tayanchlarga mantiqiy ulanganmi?<br>
            • asosiy spanlar tushunarlimi?<br>
            • shift va eshiklar bilan konflikt bormi?
            """,
        },
        {
            "title": "4. Qavatlararo moslik",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • yuqori qavat ustuni pastdagi tizimga mosmi?<br>
            • grid qavatlar bo'yicha bir xilmi?<br>
            • keskin transfer holatlari bormi?
            """,
        },
        {
            "title": "5. Fundament bilan aloqa",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • ustunlar fundamentlarga mos keladimi?<br>
            • o'qlar bir xilmi?<br>
            • yuk yo'li fundamentgacha tushunarlimi?
            """,
        },
        {
            "title": "6. Arxitektura koordinatsiyasi",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • ustun xona ichida noqulay joydami?<br>
            • eshik bilan konflikt bormi?<br>
            • fasad oynasi bilan mosmi?<br>
            • zinapoya bilan konflikt yo'qmi?
            """,
        },
        {
            "title": "7. MEP koordinatsiyasi",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • katta duct rigel bilan to'qnashyaptimi?<br>
            • quvurlar ustundan o'tmayaptimi?<br>
            • kerakli o'tishlar oldindan rejalashtirilganmi?
            """,
        },
        {
            "title": "8. BIM model audit",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • plan va 3D mosmi?<br>
            • dublikat ustunlar yo'qmi?<br>
            • elementlar noto'g'ri qavatda emasmi?<br>
            • o'qlar va elementlar bir-biriga mosmi?
            """,
        },
        {
            "title": "Xatoni toping",
            "type": "warning",
            "text": """
            Karkas modelida:

            <br><br>

            • bir ustun 2-qavatda siljigan;<br>
            • bitta rigel eshik ustidan juda past o'tgan;<br>
            • grid nomlari takrorlangan;<br>
            • ventilatsiya duct'i rigel bilan to'qnashgan;<br>
            • fundament modeli eski grid bo'yicha qolgan.

            <br><br>

            Bu loyiha
            kompleks koordinatsiya
            talab qiladi.
            """,
        },
        {
            "title": "Professional checklist",
            "type": "example",
            "text": """
            Karkas audit checklist:

            <br><br>

            <b>1.</b> Grid tizimi tushunarlimi?<br><br>
            <b>2.</b> Ustunlar o'qlarga mosmi?<br><br>
            <b>3.</b> Ustunlar qavatlar bo'yicha davom etadimi?<br><br>
            <b>4.</b> Rigellar mantiqiy ulanganmi?<br><br>
            <b>5.</b> Spanlar konstruktiv loyiha bilan mosmi?<br><br>
            <b>6.</b> Yuk yo'li fundamentgacha tushunarlimi?<br><br>
            <b>7.</b> Arxitektura bilan konfliktlar tekshirilganmi?<br><br>
            <b>8.</b> MEP bilan konfliktlar tekshirilganmi?<br><br>
            <b>9.</b> Plan, kesim va 3D o'zaro mosmi?<br><br>
            <b>10.</b> Konstruktor oxirgi versiya bilan ishlayaptimi?
            """,
        },
        {
            "title": "Modul yakuni",
            "type": "highlight",
            "text": """
            Siz endi:

            <br><br>

            ✓ karkas tizimining mantig'ini tushunasiz;<br>
            ✓ ustun va rigel vazifasini bilasiz;<br>
            ✓ yuk yo'lini o'qiysiz;<br>
            ✓ grid va span tushunchalarini bilasiz;<br>
            ✓ arxitektura bilan karkasni koordinatsiya qilasiz;<br>
            ✓ BIM modeldagi karkasni audit qilasiz.

            <br><br>

            Keyingi modul:
            <b>Plitalar.</b>
            """,
        },
    ],
}


# ============================================================
# QUIZ
# Q031-Q045
# ============================================================

LEVEL08_MODULE03_QUIZ = {
    "L08_M03_001": [
        {
            "code": "L08_Q031",
            "question": "Karkas tizimida ustun va rigellar asosiy yuk ko'taruvchi elementlar bo'lishi mumkinmi?",
            "explanation": (
                "Karkasli tizimlarda ustun va rigellar yuk uzatish tizimining asosiy qismlari bo'lishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L08_Q032",
            "question": "Bir nechta tasodifiy ustun chizishning o'zi professional karkas tizimi hisoblanadimi?",
            "explanation": (
                "Professional karkasda elementlar yagona konstruktiv va koordinatsion mantiqda ishlashi kerak."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L08_Q033",
            "question": "Karkas tizimi arxitekturaga katta ochiq makon yaratishda imkoniyat berishi mumkinmi?",
            "explanation": (
                "Karkas yuklarni ustun va rigellar orqali ko'tarib, ayrim devorlarni yuk ko'taruvchi vazifadan ozod qilishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L08_M03_002": [
        {
            "code": "L08_Q034",
            "question": "Karkasdagi yuklar rigel, ustun va fundament orqali uzatilishi mumkinmi?",
            "explanation": (
                "Bu karkasdagi asosiy yuk uzatish zanjirlaridan biridir."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L08_Q035",
            "question": "Yuqori qavat ustunining pastdagi tayanchdan keskin siljishi alohida konstruktiv yechim talab qilishi mumkinmi?",
            "explanation": (
                "Bunday holatda yuk yo'lini boshqa konstruktiv elementlar orqali tashkil qilish kerak bo'lishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L08_Q036",
            "question": "Yuk yo'li tushunarsiz bo'lsa bu koordinatsiya muammosi bo'lishi mumkinmi?",
            "explanation": (
                "Professional konstruktiv sxemada yuklarning tayanchlarga qanday uzatilishi tushunarli bo'lishi kerak."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L08_M03_003": [
        {
            "code": "L08_Q037",
            "question": "Grid va o'qlar karkas elementlarini tartibli koordinatsiya qilishga yordam beradimi?",
            "explanation": (
                "O'qlar ustun, rigel va boshqa konstruktiv elementlarning joylashuvini yagona tizimda boshqarishga yordam beradi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L08_Q038",
            "question": "Span ikki tayanch orasidagi konstruktiv masofa tushunchasimi?",
            "explanation": (
                "Span tayanchlar orasidagi masofani ifodalash uchun ishlatiladigan konstruktiv tushunchadir."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L08_Q039",
            "question": "Katta ustunsiz makon talab qilish konstruktiv yechimga ta'sir qilmaydimi?",
            "explanation": (
                "Katta spanlar element o'lchami va konstruktiv tizimga ta'sir qilishi mumkin."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
    ],

    "L08_M03_004": [
        {
            "code": "L08_Q040",
            "question": "Karkasni arxitektura loyiha yakunlangandan keyingina o'ylash yaxshi workflowmi?",
            "explanation": (
                "Konstruktiv va arxitektura tizimlari loyiha boshidan o'zaro koordinatsiyada rivojlantirilishi kerak."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L08_Q041",
            "question": "Ustun joylashuvi eshik, mebel va fasadga ta'sir qilishi mumkinmi?",
            "explanation": (
                "Ustun arxitektura makonining bir qismi bo'lgani uchun ko'plab elementlar bilan koordinatsiya qilinadi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L08_Q042",
            "question": "MEP tizimi rigel bilan to'qnashsa rigelni ruxsatsiz kesish mumkinmi?",
            "explanation": (
                "Konstruktiv elementlardagi o'zgarishlar konstruktor bilan muvofiqlashtirilishi kerak."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
    ],

    "L08_M03_005": [
        {
            "code": "L08_Q043",
            "question": "Karkas auditida grid, ustun, rigel va qavatlararo moslik tekshiriladimi?",
            "explanation": (
                "Professional audit karkas tizimining asosiy elementlari va ularning o'zaro aloqasini tekshiradi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L08_Q044",
            "question": "Fundament modeli eski grid bo'yicha qolsa bu koordinatsiya xatosimi?",
            "explanation": (
                "Ustun, grid va fundament bir xil loyiha versiyasi va koordinata mantig'ida ishlashi kerak."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L08_Q045",
            "question": "Karkas bilan professional ishlashdagi to'g'ri umumiy workflow qaysi?",
            "explanation": (
                "Grid va tayanchlar aniqlanadi, yuk yo'li tushuniladi, arxitektura va MEP bilan koordinatsiya qilinadi, so'ng model audit qilinadi."
            ),
            "options": [
                (
                    "A",
                    "Grid → ustun/rigel → yuk yo'li → arxitektura/MEP koordinatsiyasi → BIM audit",
                    True,
                ),
                (
                    "B",
                    "Tasodifiy ustunlar → grid yo'q → konfliktlarni tekshirmaslik",
                    False,
                ),
            ],
        },
    ],
}


# ============================================================
# DATABASE SEED
# ============================================================

def seed_level08_module03():
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
        ) in LEVEL08_MODULE03_LESSONS:

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
