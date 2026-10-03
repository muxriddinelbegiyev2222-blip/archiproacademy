from database.database import get_connection


# ============================================================
# LEVEL 8
# MODULE 08 - SEYSMIKA ASOSLARI
# ============================================================

LEVEL08_MODULE08_LESSONS = [
    (
        "L08_M08",
        "L08_M08_001",
        "Seysmik yuk tushunchasi",
        "theory",
        "Zilzila paytida bino massasiga ta'sir qiluvchi inertsiya kuchlari va umumiy seysmik yuk mantig'ini tushunish.",
        1,
        50,
        20,
    ),
    (
        "L08_M08",
        "L08_M08_002",
        "Bino shakli va konstruktiv muntazamlik",
        "theory",
        "Oddiy, muntazam va tushunarli bino shaklining seysmik xatti-harakatga ta'sirini tushunish.",
        2,
        55,
        20,
    ),
    (
        "L08_M08",
        "L08_M08_003",
        "Vertikal uzluksizlik va yumshoq qavat",
        "practice",
        "Qavatlar bo'yicha tayanchlarning uzluksizligi va yumshoq yoki zaif qavat xavfini tushunish.",
        3,
        60,
        20,
    ),
    (
        "L08_M08",
        "L08_M08_004",
        "Massa, nosimmetriya va arxitektura qarorlari",
        "practice",
        "Bino massasining notekis taqsimlanishi, nosimmetriya va katta ochilishlarning seysmik tizimga ta'sirini tushunish.",
        4,
        65,
        20,
    ),
    (
        "L08_M08",
        "L08_M08_005",
        "Seysmik loyiha professional audit",
        "practice",
        "Arxitektura va konstruktiv modelda muntazamlik, uzluksizlik, tayanchlar va seysmik koordinatsiyani kompleks tekshirish.",
        5,
        70,
        25,
    ),
]


# ============================================================
# CONTENT
# ============================================================

LEVEL08_MODULE08_CONTENT = {
    "L08_M08_001": [
        {
            "title": "Zilzila paytida nima sodir bo'ladi?",
            "type": "highlight",
            "text": """
            Zilzila vaqtida
            yer harakat qiladi.

            <br><br>

            Bino massasi esa
            inertsiya sababli

            <br><br>

            bu harakatga
            qarshilik ko'rsatadi.
            """,
        },
        {
            "title": "Faqat vertikal yuk emas",
            "type": "normal",
            "text": """
            Oddiy gravitatsion
            yuklardan tashqari,

            <br><br>

            zilzila paytida
            gorizontal yo'nalishdagi
            ta'sirlar ham

            <br><br>

            muhim bo'ladi.
            """,
        },
        {
            "title": "Bino bitta tizim",
            "type": "highlight",
            "text": """
            Seysmik holatda
            fundament,
            devor,
            karkas,
            plita
            va tom

            <br><br>

            bir-biridan alohida
            emas,

            <br><br>

            yagona konstruktiv
            tizim sifatida ishlaydi.
            """,
        },
        {
            "title": "Yuk yo'li",
            "type": "normal",
            "text": """
            Seysmik ta'sirda ham
            yuklarning

            <br><br>

            binodan fundamentgacha
            qanday uzatilishi

            <br><br>

            tushunarli bo'lishi kerak.
            """,
        },
        {
            "title": "Arxitektorning roli",
            "type": "highlight",
            "text": """
            Arxitektor:

            <br><br>

            • bino shaklini;<br>
            • qavatlar sxemasini;<br>
            • ochilishlarni;<br>
            • tayanchlarning joyini;<br>
            • katta konsollarni

            <br><br>

            konstruktor bilan
            koordinatsiya qiladi.
            """,
        },
        {
            "title": "Hisobni taxmin qilmang",
            "type": "warning",
            "text": """
            Seysmik:

            <br><br>

            • kuchlar;<br>
            • koeffitsiyentlar;<br>
            • armatura;<br>
            • element kesimlari;<br>
            • deformatsiyalar

            <br><br>

            aniq konstruktiv
            hisob bilan belgilanadi.
            """,
        },
        {
            "title": "Tasavvur qiling",
            "type": "example",
            "text": """
            Bino yuqori qismida
            juda og'ir elementlar bor,

            <br><br>

            pastki qavat esa
            juda ochiq.

            <br><br>

            Zilzila paytida
            massa va tayanch
            tizimi alohida
            ahamiyatga ega bo'ladi.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Oddiy ikki qavatli
            uy uchun

            <br><br>

            seysmik yuk yo'lini
            umumiy tarzda yozing:

            <br><br>

            bino massasi
            → konstruktiv tizim
            → fundament
            → grunt.
            """,
        },
    ],

    "L08_M08_002": [
        {
            "title": "Muntazam bino",
            "type": "highlight",
            "text": """
            Oddiy va
            tushunarli shakldagi

            <br><br>

            bino konstruktiv
            xatti-harakatini

            <br><br>

            tushunish odatda
            osonroq.
            """,
        },
        {
            "title": "Murakkab shakl",
            "type": "normal",
            "text": """
            Juda murakkab
            plan shakli

            <br><br>

            seysmik harakatda
            turli qismlarning

            <br><br>

            boshqacha ishlashiga
            olib kelishi mumkin.
            """,
        },
        {
            "title": "Nosimmetriya",
            "type": "warning",
            "text": """
            Konstruktiv elementlar
            faqat bitta tomda
            to'plansa,

            <br><br>

            bino seysmik
            javobi murakkablashishi
            mumkin.
            """,
        },
        {
            "title": "Plan bo'yicha tartib",
            "type": "normal",
            "text": """
            Tayanchlar
            va qattiqlik beruvchi
            elementlarni

            <br><br>

            plan bo'yicha
            mantiqiy joylashtirish

            <br><br>

            muhim loyiha
            prinsipidir.
            """,
        },
        {
            "title": "L-shaklli bino",
            "type": "example",
            "text": """
            L-shaklli bino
            arxitektura jihatdan
            qiziqarli bo'lishi mumkin.

            <br><br>

            Lekin uning
            konstruktiv xatti-harakati

            <br><br>

            oddiy to'rtburchak
            binodan murakkabroq
            bo'lishi mumkin.
            """,
        },
        {
            "title": "Muntazamlik = zerikarli emas",
            "type": "warning",
            "text": """
            Konstruktiv muntazamlik

            <br><br>

            arxitektura
            zerikarli bo'lishi
            kerak degani emas.

            <br><br>

            Forma va
            konstruktiv mantiq
            birgalikda ishlaydi.
            """,
        },
        {
            "title": "Katta chiqishlar",
            "type": "normal",
            "text": """
            Katta konsol,
            katta overhang
            yoki notekis hajmlar

            <br><br>

            konstruktor bilan
            boshidan
            muvofiqlashtiriladi.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Ikki plan chizing:

            <br><br>

            A — oddiy to'rtburchak;<br>
            B — murakkab notekis shakl.

            <br><br>

            Qaysi biri
            konstruktiv koordinatsiya
            jihatidan sodda ekanini
            tushuntiring.
            """,
        },
    ],

    "L08_M08_003": [
        {
            "title": "Vertikal uzluksizlik",
            "type": "highlight",
            "text": """
            Yuk ko'taruvchi
            elementlarning

            <br><br>

            qavatlar bo'yicha
            mantiqiy davom etishi

            <br><br>

            seysmik tizimda
            juda muhim.
            """,
        },
        {
            "title": "Ustunlar",
            "type": "normal",
            "text": """
            Yuqori qavatdagi
            ustunlar

            <br><br>

            pastdagi konstruktiv
            tizim bilan

            <br><br>

            tushunarli aloqaga
            ega bo'lishi kerak.
            """,
        },
        {
            "title": "Devorlar",
            "type": "normal",
            "text": """
            Konstruktiv devorlar
            qavatlar orasida

            <br><br>

            keskin yo'qolib
            yoki tasodifiy
            siljib qolmasligi

            <br><br>

            loyiha bosqichida
            tekshiriladi.
            """,
        },
        {
            "title": "Yumshoq qavat tushunchasi",
            "type": "highlight",
            "text": """
            Bir qavat
            boshqa qavatlarga
            nisbatan

            <br><br>

            ancha ochiq
            va kam qattiqlikka
            ega bo'lsa,

            <br><br>

            bu xavfli
            konstruktiv holat
            yaratishi mumkin.
            """,
        },
        {
            "title": "Birinchi qavatni to'liq ochish",
            "type": "warning",
            "text": """
            Pastki qavatda
            barcha devorlarni
            olib tashlab,

            <br><br>

            yuqori qavatlarda
            ko'p konstruktiv
            devor qoldirish

            <br><br>

            konstruktor bilan
            chuqur tekshirilishi kerak.
            """,
        },
        {
            "title": "Garaj misoli",
            "type": "example",
            "text": """
            Uy birinchi qavatida
            katta ochiq garaj,

            <br><br>

            yuqorida esa
            ko'p xona va devorlar
            bor.

            <br><br>

            Bu sxema
            vertikal muntazamlik
            nuqtai nazaridan
            tekshiriladi.
            """,
        },
        {
            "title": "Transfer element",
            "type": "normal",
            "text": """
            Agar yuqoridagi
            tayanch

            <br><br>

            pastda davom etmasa,

            <br><br>

            yukni boshqa
            yo'l bilan uzatish
            uchun

            <br><br>

            maxsus konstruktiv
            yechim kerak bo'lishi mumkin.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Ikki qavatli uyda
            tekshiring:

            <br><br>

            • ustunlar davom etadimi?<br>
            • konstruktiv devorlar mosmi?<br>
            • pastki qavat haddan tashqari ochiq emasmi?
            """,
        },
    ],

    "L08_M08_004": [
        {
            "title": "Massa muhim",
            "type": "highlight",
            "text": """
            Seysmik ta'sir
            bino massasi bilan
            bog'liq.

            <br><br>

            Shu sabab
            massaning qayerda
            joylashgani ham
            muhim.
            """,
        },
        {
            "title": "Og'ir elementlar",
            "type": "normal",
            "text": """
            Juda og'ir
            arxitektura yoki
            texnik elementlar

            <br><br>

            bino massasining
            taqsimlanishiga
            ta'sir qilishi mumkin.
            """,
        },
        {
            "title": "Notekis massa",
            "type": "warning",
            "text": """
            Binoning bir qismi
            juda og'ir,

            <br><br>

            boshqa qismi
            ancha yengil bo'lsa,

            <br><br>

            seysmik xatti-harakat
            murakkablashishi mumkin.
            """,
        },
        {
            "title": "Katta opening",
            "type": "normal",
            "text": """
            Konstruktiv devordagi
            katta openinglar

            <br><br>

            qattiqlik va
            yuk uzatish
            tizimiga

            <br><br>

            ta'sir qilishi mumkin.
            """,
        },
        {
            "title": "Fasad qarori",
            "type": "example",
            "text": """
            Arxitektor
            bir fasadni

            <br><br>

            deyarli to'liq
            vitraj qildi,

            <br><br>

            boshqa fasadda esa
            ko'p konstruktiv
            devor qoldi.

            <br><br>

            Bu konstruktiv
            nosimmetriya
            nuqtai nazaridan
            tekshirilishi kerak.
            """,
        },
        {
            "title": "Og'ir tom",
            "type": "warning",
            "text": """
            Tomga juda
            og'ir element
            qo'shish

            <br><br>

            faqat fasad
            yoki dizayn
            qarori emas.

            <br><br>

            Bino massasiga
            ta'sir qilishi mumkin.
            """,
        },
        {
            "title": "Arxitektura o'zgarishi",
            "type": "highlight",
            "text": """
            Katta:

            <br><br>

            • opening;<br>
            • konsol;<br>
            • ustun ko'chishi;<br>
            • devor olib tashlash;<br>
            • og'ir element qo'shish

            <br><br>

            konstruktor bilan
            qayta koordinatsiya qilinadi.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Seysmik loyiha uchun
            arxitektordan

            <br><br>

            konstruktor bilan
            kelishilishi kerak bo'lgan

            <br><br>

            6 ta katta
            o'zgarishni yozing.
            """,
        },
    ],

    "L08_M08_005": [
        {
            "title": "Seysmik professional audit",
            "type": "highlight",
            "text": """
            Audit zanjiri:

            <br><br>

            Forma
            → Massa
            → Tayanchlar
            → Vertikal uzluksizlik
            → Plan muntazamligi
            → Openings
            → BIM koordinatsiya
            """,
        },
        {
            "title": "1. Plan shakli",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • bino shakli tushunarlimi?<br>
            • juda murakkab chiqishlar bormi?<br>
            • nosimmetriya mavjudmi?
            """,
        },
        {
            "title": "2. Tayanch tizimi",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • ustunlar qayerda?<br>
            • konstruktiv devorlar qayerda?<br>
            • ular plan bo'yicha mantiqiymi?
            """,
        },
        {
            "title": "3. Vertikal uzluksizlik",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • ustunlar qavatlar bo'yicha davom etadimi?<br>
            • devorlar keskin yo'qolmayaptimi?<br>
            • transfer holatlar bormi?
            """,
        },
        {
            "title": "4. Yumshoq qavat xavfi",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • bitta qavat boshqalardan juda ochiqmi?<br>
            • birinchi qavatda tayanchlar kamayganmi?<br>
            • katta vitrinalar tizimga ta'sir qiladimi?
            """,
        },
        {
            "title": "5. Massa",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • katta og'ir elementlar qayerda?<br>
            • massalar notekis tarqalmaganmi?<br>
            • tomda katta og'irlik bormi?
            """,
        },
        {
            "title": "6. Openings",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • konstruktiv devorlardagi openings qayerda?<br>
            • keyin qo'shilgan openinglar bormi?<br>
            • konstruktor bilan kelishilganmi?
            """,
        },
        {
            "title": "7. Fundament bilan aloqa",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • ustun va devorlar fundament bilan mosmi?<br>
            • o'qlar bir xilmi?<br>
            • yuk yo'li gruntgacha tushunarlimi?
            """,
        },
        {
            "title": "8. BIM model",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • plan va kesim mosmi?<br>
            • qavatlar o'zaro mosmi?<br>
            • eski konstruktiv element qolmaganmi?<br>
            • arxitektura va konstruktor modeli bir versiyami?
            """,
        },
        {
            "title": "Xatoni toping",
            "type": "warning",
            "text": """
            Ikki qavatli uyda:

            <br><br>

            • 1-qavat deyarli to'liq ochiq;<br>
            • 2-qavatda ko'p konstruktiv devorlar bor;<br>
            • bir ustun qavatlar orasida siljigan;<br>
            • bir fasad to'liq vitrajga o'zgartirilgan;<br>
            • tomga og'ir element qo'shilgan;<br>
            • konstruktor eski plan bilan ishlayapti.

            <br><br>

            Bu loyiha
            seysmik koordinatsiyaga
            qaytarilishi kerak.
            """,
        },
        {
            "title": "Professional checklist",
            "type": "example",
            "text": """
            Seysmik arxitektura audit:

            <br><br>

            <b>1.</b> Bino shakli muntazamlashganmi?<br><br>
            <b>2.</b> Tayanch tizimi tushunarlimi?<br><br>
            <b>3.</b> Ustunlar qavatlar bo'yicha davom etadimi?<br><br>
            <b>4.</b> Konstruktiv devorlar uzluksizmi?<br><br>
            <b>5.</b> Yumshoq qavat xavfi ko'rib chiqilganmi?<br><br>
            <b>6.</b> Massa notekisligi tekshirilganmi?<br><br>
            <b>7.</b> Katta openings kelishilganmi?<br><br>
            <b>8.</b> Fundament bilan koordinatsiya bormi?<br><br>
            <b>9.</b> Arxitektura va konstruktor modeli mosmi?<br><br>
            <b>10.</b> Muhim o'zgarishlar qayta hisobga yuborilganmi?
            """,
        },
        {
            "title": "Muhim qoida",
            "type": "warning",
            "text": """
            Arxitektor
            seysmik konstruktiv
            hisobni

            <br><br>

            taxmin bilan
            almashtirmaydi.

            <br><br>

            Yakuniy konstruktiv
            qarorlar malakali
            konstruktor va

            <br><br>

            amaldagi me'yorlar
            asosida belgilanadi.
            """,
        },
        {
            "title": "Modul yakuni",
            "type": "highlight",
            "text": """
            Siz endi:

            <br><br>

            ✓ seysmik yukning umumiy mantig'ini tushunasiz;<br>
            ✓ bino shakli va muntazamlik ahamiyatini bilasiz;<br>
            ✓ vertikal uzluksizlikni tekshirasiz;<br>
            ✓ yumshoq qavat xavfini taniysiz;<br>
            ✓ massa va nosimmetriyani hisobga olasiz;<br>
            ✓ arxitektura va konstruktiv modelni seysmik nuqtai nazardan koordinatsiya qilasiz.

            <br><br>

            Keyingi modul:
            <b>Konstruktor bilan ishlash.</b>
            """,
        },
    ],
}


# ============================================================
# QUIZ
# Q106-Q120
# ============================================================

LEVEL08_MODULE08_QUIZ = {
    "L08_M08_001": [
        {
            "code": "L08_Q106",
            "question": "Zilzila paytida bino massasiga inertsiya ta'siri yuzaga keladimi?",
            "explanation": (
                "Yer harakat qilganda bino massasi inertsiya sababli seysmik kuchlar hosil bo'lishiga sabab bo'ladi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L08_Q107",
            "question": "Seysmik holatda faqat tom alohida ishlaydi, qolgan bino tizimi ahamiyatsizmi?",
            "explanation": (
                "Bino fundamentdan tomgacha yagona konstruktiv tizim sifatida ishlaydi."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L08_Q108",
            "question": "Arxitektor seysmik yuk koeffitsiyentlarini taxmin bilan belgilashi kerakmi?",
            "explanation": (
                "Aniq seysmik hisob va parametrlar tegishli konstruktiv hisob va amaldagi me'yorlar asosida belgilanadi."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
    ],

    "L08_M08_002": [
        {
            "code": "L08_Q109",
            "question": "Oddiy va muntazam bino shakli konstruktiv xatti-harakatni tushunishni osonlashtirishi mumkinmi?",
            "explanation": (
                "Tushunarli geometrik va konstruktiv tizim odatda koordinatsiyani soddalashtiradi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L08_Q110",
            "question": "Juda murakkab va nosimmetrik bino shakli konstruktiv tahlilni murakkablashtirishi mumkinmi?",
            "explanation": (
                "Nosimmetriya va murakkab geometriya seysmik javobni murakkablashtirishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L08_Q111",
            "question": "Konstruktiv muntazamlik arxitektura albatta zerikarli bo'lishi kerak deganimi?",
            "explanation": (
                "Arxitektura ifodali bo'lishi mumkin, lekin konstruktiv mantiq bilan koordinatsiyada rivojlanadi."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
    ],

    "L08_M08_003": [
        {
            "code": "L08_Q112",
            "question": "Ustun va konstruktiv devorlarning qavatlar bo'yicha uzluksizligi muhimmi?",
            "explanation": (
                "Vertikal yuk va seysmik kuchlarning tushunarli uzatilishi uchun qavatlararo uzluksizlik muhim."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L08_Q113",
            "question": "Bir qavat boshqa qavatlarga nisbatan juda ochiq bo'lsa yumshoq qavat xavfi yuzaga kelishi mumkinmi?",
            "explanation": (
                "Qavatlar orasidagi katta qattiqlik farqi konstruktiv jihatdan kritik holat bo'lishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L08_Q114",
            "question": "Yuqori qavatdagi tayanch pastda davom etmasa konstruktor bilan qayta koordinatsiya kerak bo'lishi mumkinmi?",
            "explanation": (
                "Yukni boshqa yo'l orqali uzatish uchun maxsus konstruktiv yechim talab qilinishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L08_M08_004": [
        {
            "code": "L08_Q115",
            "question": "Bino massasining notekis taqsimlanishi seysmik xatti-harakatga ta'sir qilishi mumkinmi?",
            "explanation": (
                "Massaning joylashuvi va konstruktiv qattiqlikning taqsimlanishi seysmik javobga ta'sir qilishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L08_Q116",
            "question": "Konstruktiv devordagi katta opening seysmik tizimga umuman ta'sir qilmaydimi?",
            "explanation": (
                "Katta opening konstruktiv devorning qattiqligi va yuk uzatishiga ta'sir qilishi mumkin."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L08_Q117",
            "question": "Tomga katta og'ir element qo'shish konstruktor bilan koordinatsiya qilinishi kerakmi?",
            "explanation": (
                "Og'ir element bino massasini va konstruktiv hisobni o'zgartirishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L08_M08_005": [
        {
            "code": "L08_Q118",
            "question": "Seysmik auditda bino shakli, tayanchlar va vertikal uzluksizlik tekshiriladimi?",
            "explanation": (
                "Bular arxitektura va konstruktiv tizimning muhim koordinatsiya nuqtalaridir."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L08_Q119",
            "question": "Arxitektura modeli va konstruktor modeli turli versiyada bo'lsa bu jiddiy koordinatsiya muammosimi?",
            "explanation": (
                "Seysmik va umumiy konstruktiv qarorlar bir xil loyiha ma'lumotiga asoslanishi kerak."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L08_Q120",
            "question": "Seysmik loyiha bilan professional ishlashdagi to'g'ri umumiy workflow qaysi?",
            "explanation": (
                "Arxitektura shakli va massa tahlil qilinadi, tayanchlar va uzluksizlik tekshiriladi, muhim o'zgarishlar konstruktor bilan koordinatsiya qilinadi va model auditdan o'tkaziladi."
            ),
            "options": [
                (
                    "A",
                    "Forma/massa → tayanchlar → vertikal uzluksizlik → openings va o'zgarishlar → konstruktor koordinatsiyasi → audit",
                    True,
                ),
                (
                    "B",
                    "Faqat chiroyli forma → tayanchlarni keyin o'ylash → konstruktor bilan tekshirmaslik",
                    False,
                ),
            ],
        },
    ],
}


# ============================================================
# DATABASE SEED
# ============================================================

def seed_level08_module08():
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
        ) in LEVEL08_MODULE08_LESSONS:

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
