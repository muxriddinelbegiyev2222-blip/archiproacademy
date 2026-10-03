from database.database import get_connection


# ============================================================
# LEVEL 8
# MODULE 02 - DEVOR KONSTRUKSIYASI
# ============================================================

LEVEL08_MODULE02_LESSONS = [
    (
        "L08_M02",
        "L08_M02_001",
        "Devorning konstruktiv vazifasi",
        "theory",
        "Devorning arxitektura elementi va konstruktiv tizimdagi vazifalarini farqlash.",
        1,
        40,
        20,
    ),
    (
        "L08_M02",
        "L08_M02_002",
        "Yuk ko'taruvchi va to'ldiruvchi devor",
        "theory",
        "Yuk ko'taruvchi devor bilan karkas orasini to'ldiruvchi devorning asosiy farqlarini tushunish.",
        2,
        45,
        20,
    ),
    (
        "L08_M02",
        "L08_M02_003",
        "Devorlar, ochilishlar va yuk yo'li",
        "practice",
        "Eshik, deraza va boshqa ochilishlarning devor konstruktiv mantig'iga ta'sirini tushunish.",
        3,
        50,
        20,
    ),
    (
        "L08_M02",
        "L08_M02_004",
        "Qavatlararo devor koordinatsiyasi",
        "practice",
        "Turli qavatlardagi devorlar, tayanchlar, plitalar va o'qlarni o'zaro koordinatsiya qilish.",
        4,
        50,
        20,
    ),
    (
        "L08_M02",
        "L08_M02_005",
        "Devor konstruksiyasi professional audit",
        "practice",
        "Arxitektura modeli va konstruktiv devor tizimi o'rtasidagi asosiy muvofiqliklarni tekshirish.",
        5,
        55,
        25,
    ),
]


# ============================================================
# CONTENT
# ============================================================

LEVEL08_MODULE02_CONTENT = {
    "L08_M02_001": [
        {
            "title": "Devor faqat xona ajratmaydi",
            "type": "highlight",
            "text": """
            Devor arxitekturada
            xonalarni ajratishi mumkin.

            <br><br>

            Lekin ayrim devorlar
            binoning konstruktiv
            tizimida ham

            <br><br>

            muhim vazifa bajaradi.
            """,
        },
        {
            "title": "Devorning ikki xil roli",
            "type": "normal",
            "text": """
            Devor:

            <br><br>

            1. faqat makonni ajratishi;<br>
            2. yuk ko'taruvchi tizimning qismi bo'lishi

            <br><br>

            mumkin.
            """,
        },
        {
            "title": "Arxitektura qarori",
            "type": "highlight",
            "text": """
            Arxitektor
            plan chizayotganda

            <br><br>

            qaysi devor
            konstruktiv ahamiyatga
            ega ekanini

            <br><br>

            boshidan tushunishi
            kerak.
            """,
        },
        {
            "title": "Tasavvur qiling",
            "type": "example",
            "text": """
            Uy planida
            20 ta devor bor.

            <br><br>

            Ularning ayrimlari
            xonalarni ajratadi,

            <br><br>

            ayrimlari esa
            yuqoridan kelayotgan
            yuklarni qabul qiladi.

            <br><br>

            Ularni bir xil
            deb qarash mumkin emas.
            """,
        },
        {
            "title": "Devor va yuk yo'li",
            "type": "normal",
            "text": """
            Agar devor
            yuk ko'taruvchi bo'lsa,

            <br><br>

            undan kelayotgan yuk
            pastdagi konstruktiv
            elementlarga

            <br><br>

            mantiqiy uzatilishi
            kerak.
            """,
        },
        {
            "title": "Tasodifiy o'zgarish xavfi",
            "type": "warning",
            "text": """
            Yuk ko'taruvchi
            devorni

            <br><br>

            faqat interyer
            qulayligi uchun
            ko'chirish yoki olib tashlash

            <br><br>

            oddiy plan
            tuzatishi emas.
            """,
        },
        {
            "title": "Arxitektorning vazifasi",
            "type": "normal",
            "text": """
            Arxitektor
            konstruktiv hisobni
            konstruktor o'rniga
            bajarmaydi.

            <br><br>

            Lekin konstruktiv
            sxemani tushunib,

            <br><br>

            loyiha qarorlarini
            unga moslashtiradi.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Oddiy uy planini
            tasavvur qiling.

            <br><br>

            Devorlarni
            ikki guruhga ajrating:

            <br><br>

            • konstruktiv ahamiyatga ega bo'lishi mumkin;<br>
            • faqat makonni ajratishi mumkin.

            <br><br>

            Nima uchun shunday
            ajratganingizni yozing.
            """,
        },
    ],

    "L08_M02_002": [
        {
            "title": "Yuk ko'taruvchi devor",
            "type": "highlight",
            "text": """
            Yuk ko'taruvchi devor
            bino yuklarini

            <br><br>

            qabul qiluvchi va
            pastdagi konstruktiv
            tizimga uzatuvchi

            <br><br>

            elementlardan biri
            bo'lishi mumkin.
            """,
        },
        {
            "title": "To'ldiruvchi devor",
            "type": "normal",
            "text": """
            Karkasli binoda
            asosiy yuklarni

            <br><br>

            ustun va rigellar
            ko'tarishi mumkin.

            <br><br>

            Ularning orasidagi
            devor esa

            <br><br>

            ko'proq to'ldiruvchi
            vazifada ishlashi mumkin.
            """,
        },
        {
            "title": "Bir xil ko'rinish — boshqa vazifa",
            "type": "warning",
            "text": """
            Planda ikki devor
            bir-biriga o'xshash
            ko'rinishi mumkin.

            <br><br>

            Lekin ularning
            konstruktiv vazifasi
            mutlaqo boshqa
            bo'lishi mumkin.
            """,
        },
        {
            "title": "Konstruktiv sxema",
            "type": "highlight",
            "text": """
            Avval bino
            qaysi konstruktiv
            tizimda ishlashi

            <br><br>

            tushuniladi.

            <br><br>

            Keyin devorlarning
            vazifasi shu tizim
            ichida aniqlanadi.
            """,
        },
        {
            "title": "Materialning o'zi yetarli emas",
            "type": "warning",
            "text": """
            Devor materiali
            uning konstruktiv
            vazifasini

            <br><br>

            har doim yolg'iz
            o'zi aniqlab bermaydi.

            <br><br>

            Umumiy konstruktiv
            sxema muhim.
            """,
        },
        {
            "title": "Tashqi va ichki devor",
            "type": "normal",
            "text": """
            Tashqi devor
            avtomatik ravishda
            yuk ko'taruvchi,

            <br><br>

            ichki devor esa
            avtomatik ravishda
            yengil partition

            <br><br>

            degani emas.
            """,
        },
        {
            "title": "Karkasli bino misoli",
            "type": "example",
            "text": """
            Bino ustun-rigel
            karkasida ishlaydi.

            <br><br>

            Tashqi fasad devori
            xonani tashqi muhitdan
            ajratadi,

            <br><br>

            lekin asosiy vertikal
            yukni karkas
            qabul qilishi mumkin.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Quyidagi ikki sxemani
            taqqoslang:

            <br><br>

            A — yuk ko'taruvchi devorli bino;<br>
            B — ustun-rigel karkasli bino.

            <br><br>

            Har birida devorning
            vazifasi qanday
            farq qilishini yozing.
            """,
        },
    ],

    "L08_M02_003": [
        {
            "title": "Ochilish nima?",
            "type": "highlight",
            "text": """
            Eshik,
            deraza
            yoki boshqa teshik

            <br><br>

            devorning uzluksizligini
            o'zgartiradi.
            """,
        },
        {
            "title": "Yuk ko'taruvchi devordagi ochilish",
            "type": "warning",
            "text": """
            Yuk ko'taruvchi
            devorda katta
            ochilish yaratish

            <br><br>

            faqat fasad yoki
            interyer qarori emas.

            <br><br>

            Bu konstruktiv
            tizimga ta'sir
            qilishi mumkin.
            """,
        },
        {
            "title": "Ochilish ustidagi zona",
            "type": "normal",
            "text": """
            Ochilish ustidagi
            yuklar

            <br><br>

            yon tayanchlarga
            qanday uzatilishi

            <br><br>

            konstruktiv yechimda
            hal qilinadi.
            """,
        },
        {
            "title": "Tasavvur qiling",
            "type": "example",
            "text": """
            Dastlab devorda
            kichik deraza bor edi.

            <br><br>

            Mijoz keyin
            butun devor bo'ylab
            katta vitraj

            <br><br>

            xohladi.

            <br><br>

            Bu o'zgarish
            konstruktor bilan
            qayta koordinatsiya
            qilinishi kerak.
            """,
        },
        {
            "title": "Ochilishlarning bir-biriga yaqinligi",
            "type": "warning",
            "text": """
            Ko'p ochilishlar
            juda yaqin
            joylashtirilsa,

            <br><br>

            devorning qolgan
            qismlari konstruktiv
            jihatdan muhim
            bo'lishi mumkin.

            <br><br>

            Aniq baho
            hisob bilan beriladi.
            """,
        },
        {
            "title": "Eshikni keyin ko'chirish",
            "type": "normal",
            "text": """
            Partition devorda
            eshikni ko'chirish
            bilan

            <br><br>

            yuk ko'taruvchi
            devorda eshikni
            ko'chirish

            <br><br>

            bir xil darajadagi
            o'zgarish emas.
            """,
        },
        {
            "title": "MEP o'tishlari",
            "type": "warning",
            "text": """
            Muhandislik tizimlari
            uchun katta

            <br><br>

            teshik yoki kanal
            konstruktiv devordan
            o'tkazilsa,

            <br><br>

            bu oldindan
            konstruktor bilan
            kelishilishi kerak.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Devor bo'yicha
            uchta o'zgarishni yozing:

            <br><br>

            • yangi eshik;<br>
            • katta deraza;<br>
            • muhandislik teshigi.

            <br><br>

            Qaysi holatda
            konstruktor bilan
            albatta koordinatsiya
            kerakligini tushuntiring.
            """,
        },
    ],

    "L08_M02_004": [
        {
            "title": "Qavatlararo davomiylik",
            "type": "highlight",
            "text": """
            Ko'p qavatli
            yoki ikki qavatli
            uyda

            <br><br>

            yuqori qavatdagi
            yuk ko'taruvchi elementlar

            <br><br>

            pastdagi konstruktiv
            tizim bilan
            koordinatsiyada bo'lishi kerak.
            """,
        },
        {
            "title": "Devor ustida devor",
            "type": "normal",
            "text": """
            Yuk ko'taruvchi
            devorlarning

            <br><br>

            qavatlar bo'yicha
            mantiqiy davom etishi

            <br><br>

            yuk yo'lini
            soddalashtirishi mumkin.
            """,
        },
        {
            "title": "Siljigan devor",
            "type": "warning",
            "text": """
            Ikkinchi qavatdagi
            yuk ko'taruvchi devor

            <br><br>

            pastdagi tayanchdan
            keskin siljigan bo'lsa,

            <br><br>

            qo'shimcha konstruktiv
            yechim talab qilinishi
            mumkin.
            """,
        },
        {
            "title": "Plita bilan aloqa",
            "type": "normal",
            "text": """
            Devor,
            plita
            va boshqa tayanchlar

            <br><br>

            bitta umumiy
            yuk uzatish tizimida
            ishlaydi.
            """,
        },
        {
            "title": "O'qlar",
            "type": "highlight",
            "text": """
            Konstruktiv devorlar
            va tayanchlar

            <br><br>

            o'qlar bilan
            tartibli bog'lansa,

            <br><br>

            loyiha koordinatsiyasi
            ancha tushunarli
            bo'ladi.
            """,
        },
        {
            "title": "Birinchi va ikkinchi qavat",
            "type": "example",
            "text": """
            1-qavatda katta
            ochiq mehmonxona bor.

            <br><br>

            2-qavatda esa
            shu zonaning ustida
            bir nechta devor bor.

            <br><br>

            Arxitektura jihatdan
            qulay bo'lishi mumkin,

            <br><br>

            lekin konstruktiv
            yuk yo'li alohida
            tekshiriladi.
            """,
        },
        {
            "title": "Plan + Section + 3D",
            "type": "normal",
            "text": """
            Devor koordinatsiyasi
            faqat planda emas.

            <br><br>

            Plan,
            kesim
            va 3D modelda

            <br><br>

            bir xil mantiq
            ko'rinishi kerak.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Ikki qavatli uyda
            devorlarni tekshiring:

            <br><br>

            • 2-qavat devori tagida nima bor?<br>
            • o'qlar mosmi?<br>
            • plita bilan aloqa tushunarlimi?<br>
            • katta siljishlar bormi?
            """,
        },
    ],

    "L08_M02_005": [
        {
            "title": "Devor konstruksiyasi auditi",
            "type": "highlight",
            "text": """
            Audit zanjiri:

            <br><br>

            Konstruktiv sxema
            → Devor vazifasi
            → Ochilishlar
            → Qavatlararo moslik
            → O'qlar
            → BIM model
            → Koordinatsiya
            """,
        },
        {
            "title": "1. Devor vazifasi",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • qaysi devor yuk ko'taruvchi?<br>
            • qaysi devor to'ldiruvchi?<br>
            • qaysi devor oddiy partition?
            """,
        },
        {
            "title": "2. Qavatlararo moslik",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • yuqori qavat devori pastdagi tayanchga mosmi?<br>
            • keskin siljish bormi?<br>
            • yuk yo'li tushunarlimi?
            """,
        },
        {
            "title": "3. Ochilishlar",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • eshik va derazalar qayerda?<br>
            • katta ochilishlar bormi?<br>
            • konstruktiv yechim bilan kelishilganmi?
            """,
        },
        {
            "title": "4. O'qlar",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • devorlar o'qlarga mosmi?<br>
            • konstruktor chizmasi bilan koordinatsiya bormi?<br>
            • planlar orasida siljish yo'qmi?
            """,
        },
        {
            "title": "5. Material va qatlamlar",
            "type": "normal",
            "text": """
            Tekshiring:

            <br><br>

            • devor turi to'g'rimi?<br>
            • BIM modelda kerakli konstruktsiya ishlatilganmi?<br>
            • finishing va konstruktiv qatlamlar chalkashmaganmi?
            """,
        },
        {
            "title": "6. MEP koordinatsiyasi",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • katta teshiklar bormi?<br>
            • kommunikatsiyalar devor bilan to'qnashyaptimi?<br>
            • konstruktiv devorda ruxsatsiz teshik rejalashtirilmaganmi?
            """,
        },
        {
            "title": "7. Model muvofiqligi",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • plan;<br>
            • kesim;<br>
            • fasad;<br>
            • 3D

            <br><br>

            bir xil devor
            holatini ko'rsatyaptimi?
            """,
        },
        {
            "title": "Xatoni toping",
            "type": "warning",
            "text": """
            Ikki qavatli uyda:

            <br><br>

            • 2-qavat yuk ko'taruvchi devori pastda tayanchsiz;<br>
            • katta vitraj keyin qo'shilgan;<br>
            • bitta konstruktiv devorda MEP teshigi bor;<br>
            • plan va kesimda devor joyi farq qiladi;<br>
            • konstruktor eski plan bilan ishlayapti.

            <br><br>

            Bu loyiha
            qayta koordinatsiya
            qilinishi kerak.
            """,
        },
        {
            "title": "Professional checklist",
            "type": "example",
            "text": """
            Devor konstruksiyasi
            audit checklist:

            <br><br>

            <b>1.</b> Konstruktiv sxema aniqmi?<br><br>
            <b>2.</b> Yuk ko'taruvchi va to'ldiruvchi devorlar farqlanganmi?<br><br>
            <b>3.</b> Qavatlararo yuk yo'li tushunarlimi?<br><br>
            <b>4.</b> Ochilishlar koordinatsiya qilinganmi?<br><br>
            <b>5.</b> Devorlar o'qlarga mosmi?<br><br>
            <b>6.</b> MEP o'tishlari tekshirilganmi?<br><br>
            <b>7.</b> Plan, kesim va 3D bir-biriga mosmi?<br><br>
            <b>8.</b> Konstruktor bilan oxirgi versiya kelishilganmi?
            """,
        },
        {
            "title": "Modul yakuni",
            "type": "highlight",
            "text": """
            Siz endi:

            <br><br>

            ✓ devorning konstruktiv vazifasini tushunasiz;<br>
            ✓ yuk ko'taruvchi va to'ldiruvchi devorni farqlaysiz;<br>
            ✓ ochilishlarning ahamiyatini tushunasiz;<br>
            ✓ qavatlararo devorlarni koordinatsiya qilasiz;<br>
            ✓ o'qlar va yuk yo'lini tekshirasiz;<br>
            ✓ devor konstruksiyasini arxitektura darajasida audit qilasiz.

            <br><br>

            Keyingi modul:
            <b>Karkas.</b>
            """,
        },
    ],
}


# ============================================================
# QUIZ
# Q016-Q030
# ============================================================

LEVEL08_MODULE02_QUIZ = {
    "L08_M02_001": [
        {
            "code": "L08_Q016",
            "question": "Barcha devorlar faqat xonalarni ajratish vazifasini bajaradimi?",
            "explanation": (
                "Ayrim devorlar makonni ajratish bilan birga konstruktiv yuk ko'taruvchi vazifaga ham ega bo'lishi mumkin."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L08_Q017",
            "question": "Arxitektor qaysi devorlar konstruktiv ahamiyatga ega ekanini tushunishi kerakmi?",
            "explanation": (
                "Bu bilim arxitektura va konstruktiv tizimni to'g'ri koordinatsiya qilish uchun muhim."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L08_Q018",
            "question": "Yuk ko'taruvchi devorni konstruktor bilan tekshirmasdan olib tashlash oddiy plan tuzatishimi?",
            "explanation": (
                "Yuk ko'taruvchi devordagi o'zgarish binoning yuk uzatish tizimiga ta'sir qilishi mumkin."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
    ],

    "L08_M02_002": [
        {
            "code": "L08_Q019",
            "question": "Yuk ko'taruvchi devor bino yuklarini boshqa konstruktiv elementlarga uzatishi mumkinmi?",
            "explanation": (
                "Yuk ko'taruvchi devor konstruktiv yuk yo'lining bir qismi bo'lishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L08_Q020",
            "question": "Karkasli binoda barcha devorlar asosiy vertikal yuklarni albatta ko'taradimi?",
            "explanation": (
                "Karkasli tizimda asosiy yuklarni ustun va rigellar qabul qilishi, devorlar esa to'ldiruvchi vazifada ishlashi mumkin."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L08_Q021",
            "question": "Tashqi devor har doim avtomatik ravishda yuk ko'taruvchi devormi?",
            "explanation": (
                "Devorning joylashuvi emas, umumiy konstruktiv tizim uning vazifasini belgilaydi."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
    ],

    "L08_M02_003": [
        {
            "code": "L08_Q022",
            "question": "Yuk ko'taruvchi devorda katta ochilish yaratish konstruktiv yechimga ta'sir qilishi mumkinmi?",
            "explanation": (
                "Ochilish devorning uzluksizligi va yuk uzatish mantig'ini o'zgartirishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L08_Q023",
            "question": "Katta vitraj qo'shilsa konstruktor bilan qayta koordinatsiya qilish kerak bo'lishi mumkinmi?",
            "explanation": (
                "Katta ochilish yuk ko'taruvchi yoki boshqa konstruktiv elementlarga ta'sir qilishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L08_Q024",
            "question": "Konstruktiv devordan katta MEP teshigini ruxsatsiz o'tkazish yaxshi amaliyotmi?",
            "explanation": (
                "Konstruktiv elementlardagi katta o'tishlar oldindan mutaxassis bilan koordinatsiya qilinishi kerak."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
    ],

    "L08_M02_004": [
        {
            "code": "L08_Q025",
            "question": "Ikki qavatli binoda yuqori qavatdagi yuk ko'taruvchi devorlar pastdagi konstruktiv tizim bilan koordinatsiya qilinadimi?",
            "explanation": (
                "Qavatlararo yuk yo'li tushunarli va uzluksiz bo'lishi uchun elementlar o'zaro koordinatsiya qilinadi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L08_Q026",
            "question": "Yuqori qavat devorining pastdagi tayanchdan keskin siljishi alohida konstruktiv tekshiruv talab qilishi mumkinmi?",
            "explanation": (
                "Bunday siljish yuklarni boshqa elementlar orqali uzatishni talab qilishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L08_Q027",
            "question": "Devor koordinatsiyasini faqat qavat planida tekshirish yetarlimi?",
            "explanation": (
                "Plan bilan birga kesim va 3D model ham qavatlararo munosabatlarni tushunishga yordam beradi."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
    ],

    "L08_M02_005": [
        {
            "code": "L08_Q028",
            "question": "Devor auditida yuk ko'taruvchi va to'ldiruvchi devorlarni farqlash kerakmi?",
            "explanation": (
                "Ularning konstruktiv vazifalari turlicha bo'lishi mumkin, shuning uchun auditda farqlanadi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L08_Q029",
            "question": "Plan va kesimda konstruktiv devor turli joyda ko'rsatilsa bu koordinatsiya muammosimi?",
            "explanation": (
                "Turli loyiha ko'rinishlaridagi devor holati bir-biriga mos bo'lishi kerak."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L08_Q030",
            "question": "Devor konstruksiyasi bilan professional ishlashdagi to'g'ri umumiy workflow qaysi?",
            "explanation": (
                "Avval konstruktiv sxema aniqlanadi, devor vazifalari tushuniladi, ochilish va qavatlararo moslik tekshiriladi, so'ng BIM model audit qilinadi."
            ),
            "options": [
                (
                    "A",
                    "Konstruktiv sxema → devor vazifasi → ochilishlar → qavatlararo koordinatsiya → audit",
                    True,
                ),
                (
                    "B",
                    "Devorlarni tasodifiy chizish → katta ochilishlar yaratish → konstruktor bilan tekshirmaslik",
                    False,
                ),
            ],
        },
    ],
}


# ============================================================
# DATABASE SEED
# ============================================================

def seed_level08_module02():
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
        ) in LEVEL08_MODULE02_LESSONS:

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
