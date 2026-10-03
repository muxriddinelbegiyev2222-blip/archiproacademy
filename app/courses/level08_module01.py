from database.database import get_connection


# ============================================================
# LEVEL 8
# MODULE 01 - FUNDAMENT
# ============================================================

LEVEL08_MODULE01_LESSONS = [
    (
        "L08_M01",
        "L08_M01_001",
        "Fundament tushunchasi",
        "theory",
        "Fundamentning bino yuklarini gruntga uzatishdagi vazifasi va umumiy konstruktiv mantig'ini tushunish.",
        1,
        40,
        20,
    ),
    (
        "L08_M01",
        "L08_M01_002",
        "Fundamentning asosiy turlari",
        "theory",
        "Lenta, alohida tayanch, plita va qoziqli fundamentlarning umumiy qo'llanish mantig'ini farqlash.",
        2,
        45,
        20,
    ),
    (
        "L08_M01",
        "L08_M01_003",
        "Grunt va fundament munosabati",
        "practice",
        "Grunt sharoiti, yer osti suvlari va bino yuklari fundament tanloviga qanday ta'sir qilishini tushunish.",
        3,
        50,
        20,
    ),
    (
        "L08_M01",
        "L08_M01_004",
        "Arxitektura loyihasida fundament koordinatsiyasi",
        "practice",
        "Devorlar, ustunlar, o'qlar, qavat balandliklari va muhandislik yechimlarini fundament bilan koordinatsiya qilish.",
        4,
        50,
        20,
    ),
    (
        "L08_M01",
        "L08_M01_005",
        "Fundament professional audit",
        "practice",
        "Arxitektura modeli va konstruktiv fundament yechimi o'rtasidagi asosiy muvofiqliklarni tekshirish.",
        5,
        55,
        25,
    ),
]


# ============================================================
# CONTENT
# ============================================================

LEVEL08_MODULE01_CONTENT = {
    "L08_M01_001": [
        {
            "title": "Fundament nima?",
            "type": "highlight",
            "text": """
            Fundament —
            binoning yuklarini

            <br><br>

            yer asosiga
            uzatadigan
            konstruktiv qism.
            """,
        },
        {
            "title": "Yuk qayerdan keladi?",
            "type": "normal",
            "text": """
            Binodagi yuklar
            yuqoridan pastga
            uzatiladi.

            <br><br>

            Masalan:

            tom
            → devor yoki karkas
            → fundament
            → grunt.
            """,
        },
        {
            "title": "Fundament faqat taglik emas",
            "type": "warning",
            "text": """
            Fundamentni
            shunchaki devor ostidagi
            beton deb tushunish
            noto'g'ri.

            <br><br>

            U butun binoning
            yuk uzatish tizimining
            muhim qismidir.
            """,
        },
        {
            "title": "Arxitektor nimani bilishi kerak?",
            "type": "highlight",
            "text": """
            Arxitektor:

            <br><br>

            • qaysi elementlar yuk ko'tarishini;<br>
            • tayanchlar qayerda joylashganini;<br>
            • bino massasi qanday taqsimlanganini;<br>
            • fundament uchun joy va koordinatsiyani

            <br><br>

            tushunishi kerak.
            """,
        },
        {
            "title": "Arxitektor hisobchi emas",
            "type": "warning",
            "text": """
            Fundamentning aniq:

            <br><br>

            • o'lchami;<br>
            • armaturasi;<br>
            • beton klassi;<br>
            • yuk ko'tarish qobiliyati

            <br><br>

            konstruktiv hisob
            asosida belgilanadi.

            <br><br>

            Buni faqat taxmin bilan
            tanlash mumkin emas.
            """,
        },
        {
            "title": "Tasavvur qiling",
            "type": "example",
            "text": """
            Ikki qavatli uyda
            yuk ko'taruvchi devor

            <br><br>

            birinchi qavatda
            bir joyda,

            <br><br>

            ikkinchi qavatda
            esa boshqa joyda.

            <br><br>

            Bu holat
            yuk uzatish
            mantig'ini murakkablashtiradi.
            """,
        },
        {
            "title": "Vertikal yuk yo'li",
            "type": "normal",
            "text": """
            Professional loyiha
            yaratishda

            <br><br>

            yuklarning
            imkon qadar

            <br><br>

            tushunarli va
            mantiqiy vertikal
            yo'l bilan uzatilishi

            <br><br>

            konstruktor bilan
            koordinatsiyani
            osonlashtiradi.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Oddiy bir qavatli
            uy planini
            tasavvur qiling.

            <br><br>

            Belgilang:

            • yuk ko'taruvchi devorlar;<br>
            • ustunlar bo'lsa ularning joyi;<br>
            • yukning fundamentga borish yo'li.
            """,
        },
    ],

    "L08_M01_002": [
        {
            "title": "Fundament turlari",
            "type": "highlight",
            "text": """
            Fundamentning
            yagona turi yo'q.

            <br><br>

            Tur tanlovi:

            • bino sxemasi;<br>
            • yuklar;<br>
            • grunt;<br>
            • yer osti suvlari;<br>
            • konstruktiv yechim

            <br><br>

            kabi omillarga bog'liq.
            """,
        },
        {
            "title": "Lenta fundament",
            "type": "normal",
            "text": """
            Lenta fundament
            odatda

            <br><br>

            uzluksiz devorlar
            ostida davom etuvchi
            tayanch sxemasi
            sifatida tasavvur qilinadi.
            """,
        },
        {
            "title": "Alohida tayanch fundament",
            "type": "normal",
            "text": """
            Alohida tayanch
            fundament

            <br><br>

            ustun yoki
            nuqtaviy tayanchlardan
            kelayotgan yuklarni

            <br><br>

            gruntga uzatish
            uchun ishlatilishi
            mumkin.
            """,
        },
        {
            "title": "Plita fundament",
            "type": "normal",
            "text": """
            Plita fundament
            bino tagida

            <br><br>

            katta yaxlit
            tayanch yuzasi
            hosil qiluvchi
            konstruktiv yechimdir.
            """,
        },
        {
            "title": "Qoziqli fundament",
            "type": "normal",
            "text": """
            Qoziqli tizimlarda
            yuklar

            <br><br>

            chuqurroq qatlamlarga
            uzatilishi mumkin.

            <br><br>

            Bunday yechim
            geologik va konstruktiv
            hisoblar bilan
            asoslanadi.
            """,
        },
        {
            "title": "Qaysi biri eng yaxshi?",
            "type": "warning",
            "text": """
            “Eng yaxshi fundament”
            degan universal
            javob yo'q.

            <br><br>

            Eng to'g'ri yechim —
            konkret loyiha
            sharoitiga mos
            yechim.
            """,
        },
        {
            "title": "Xatoni toping",
            "type": "warning",
            "text": """
            Loyiha muallifi:

            <br><br>

            “Qo'shnining uyida
            lenta fundament bor,
            demak bizda ham
            aynan shuni qilamiz”

            <br><br>

            dedi.

            <br><br>

            Muammo:
            bino va grunt
            sharoitlari bir xil
            ekanligi isbotlanmagan.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Quyidagi tizimlarni
            bir-biridan farqlang:

            <br><br>

            1. uzluksiz devor osti;<br>
            2. alohida ustunlar;<br>
            3. bino tagida yaxlit plita;<br>
            4. chuqur tayanchlar.

            <br><br>

            Har biri qaysi
            fundament konsepsiyasiga
            yaqinligini yozing.
            """,
        },
    ],

    "L08_M01_003": [
        {
            "title": "Fundament va grunt",
            "type": "highlight",
            "text": """
            Fundament
            grunt bilan
            birgalikda ishlaydi.

            <br><br>

            Shu sabab
            bino ostidagi yer

            <br><br>

            shunchaki fon
            emas.
            """,
        },
        {
            "title": "Grunt xususiyatlari",
            "type": "normal",
            "text": """
            Turli gruntlar:

            <br><br>

            • turli zichlikka;<br>
            • turli namlikka;<br>
            • turli deformatsiya xususiyatiga;<br>
            • turli yuk ko'tarish imkoniyatiga

            <br><br>

            ega bo'lishi mumkin.
            """,
        },
        {
            "title": "Geologik ma'lumot",
            "type": "highlight",
            "text": """
            Professional loyihada
            grunt haqida

            <br><br>

            real muhandislik-geologik
            ma'lumot

            <br><br>

            konstruktiv qaror
            uchun muhim.
            """,
        },
        {
            "title": "Yer osti suvlari",
            "type": "normal",
            "text": """
            Yer osti suvlari
            fundament va

            <br><br>

            yer osti qismlarining
            himoyasi,

            <br><br>

            gidroizolyatsiya
            va konstruktiv
            yechimlarga

            <br><br>

            ta'sir qilishi mumkin.
            """,
        },
        {
            "title": "Cho'kish",
            "type": "warning",
            "text": """
            Grunt va yuklar
            noto'g'ri baholansa,

            <br><br>

            bino qismlarida
            notekis deformatsiyalar
            paydo bo'lishi mumkin.

            <br><br>

            Shu sabab
            fundament yechimi
            hisob bilan aniqlanadi.
            """,
        },
        {
            "title": "Notekis bino massasi",
            "type": "example",
            "text": """
            Uyning bir qismi
            bir qavatli,

            <br><br>

            boshqa qismi
            ikki qavatli.

            <br><br>

            Demak yuklar
            bir xil taqsimlanmasligi
            mumkin.

            <br><br>

            Bu konstruktor bilan
            alohida koordinatsiya
            talab qiladi.
            """,
        },
        {
            "title": "Qiyalikdagi yer",
            "type": "example",
            "text": """
            Nishabli uchastkada
            fundament masalasi

            <br><br>

            tekis uchastkaga
            qaraganda

            <br><br>

            ko'proq koordinatsiya
            talab qilishi mumkin.

            <br><br>

            Faqat plan
            ko'rinishiga qarab
            qaror qilish yetarli emas.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Fundamentdan oldin
            konstruktor so'rashi
            mumkin bo'lgan

            <br><br>

            kamida 5 ta
            boshlang'ich ma'lumotni
            yozing.

            <br><br>

            Masalan:

            • qavatlar soni;<br>
            • tayanch sxemasi;<br>
            • grunt ma'lumoti.
            """,
        },
    ],

    "L08_M01_004": [
        {
            "title": "Arxitektura va fundament",
            "type": "highlight",
            "text": """
            Fundament
            alohida loyiha
            emas.

            <br><br>

            U arxitektura,
            konstruktsiya
            va muhandislik
            tizimlari bilan
            koordinatsiyada ishlaydi.
            """,
        },
        {
            "title": "O'qlar",
            "type": "normal",
            "text": """
            Ustunlar,
            yuk ko'taruvchi devorlar
            va fundamentlar

            <br><br>

            o'qlar bo'yicha
            tushunarli koordinatsiyaga
            ega bo'lishi kerak.
            """,
        },
        {
            "title": "Devor ustma-ustligi",
            "type": "normal",
            "text": """
            Qavatlardagi
            yuk ko'taruvchi elementlar

            <br><br>

            o'zaro mantiqiy
            joylashsa,

            <br><br>

            yuk uzatish
            sxemasi odatda
            tushunarliroq bo'ladi.
            """,
        },
        {
            "title": "Ustunlarni ko'chirish",
            "type": "warning",
            "text": """
            Arxitektura planida
            ustunni

            <br><br>

            faqat xona
            ko'rinishi uchun
            tasodifiy ko'chirish

            <br><br>

            fundament va
            konstruktiv sxemaga
            ta'sir qilishi mumkin.
            """,
        },
        {
            "title": "Muhandislik kirishlari",
            "type": "normal",
            "text": """
            Suv,
            kanalizatsiya,
            elektr
            va boshqa kommunikatsiyalar

            <br><br>

            fundament zonalari
            bilan to'qnashmasligi
            uchun oldindan
            koordinatsiya qilinadi.
            """,
        },
        {
            "title": "Texnik teshiklar",
            "type": "warning",
            "text": """
            Tayyor fundamentga
            keyin tasodifiy
            katta teshik ochish

            <br><br>

            oddiy arxitektura
            tuzatishi emas.

            <br><br>

            Bunday o'zgarish
            konstruktor bilan
            kelishilishi kerak.
            """,
        },
        {
            "title": "0.000 va fundament",
            "type": "normal",
            "text": """
            Arxitektura
            balandlik belgilarining

            <br><br>

            konstruktiv chizmalar
            bilan bir xil
            koordinata mantig'ida
            ishlashi muhim.
            """,
        },
        {
            "title": "Model koordinatsiyasi",
            "type": "highlight",
            "text": """
            BIM modelda
            fundament:

            <br><br>

            • plan;<br>
            • kesim;<br>
            • 3D;<br>
            • o'qlar;<br>
            • balandliklar

            <br><br>

            bo'yicha bir-biriga
            mos kelishi kerak.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Arxitektura planini
            ko'rib chiqayotganingizni
            tasavvur qiling.

            <br><br>

            Fundament bilan
            tekshirilishi kerak bo'lgan

            <br><br>

            5 ta koordinatsiya
            nuqtasini yozing.
            """,
        },
    ],

    "L08_M01_005": [
        {
            "title": "Fundament professional audit",
            "type": "highlight",
            "text": """
            Arxitektura darajasidagi
            fundament audit:

            <br><br>

            Arxitektura
            → Yuk yo'li
            → Tayanchlar
            → Fundament
            → Grunt
            → Koordinatsiya
            """,
        },
        {
            "title": "1. Yuk ko'taruvchi elementlar",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • yuk ko'taruvchi devorlar aniqmi?<br>
            • ustunlar aniqmi?<br>
            • yuqori qavat tayanchlari tushunarlimi?
            """,
        },
        {
            "title": "2. Vertikal moslik",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • yuqori qavat devorlari pastdagi tayanchlarga mosmi?<br>
            • ustunlar vertikal tizimda davom etadimi?<br>
            • keskin siljishlar bormi?
            """,
        },
        {
            "title": "3. O'qlar",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • arxitektura va konstruktsiya o'qlari mosmi?<br>
            • ustun markazlari to'g'rimi?<br>
            • fundamentlar tayanchlar bilan mosmi?
            """,
        },
        {
            "title": "4. Balandliklar",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • asosiy balandlik belgilar bir xilmi?<br>
            • kesimdagi va plandagi ma'lumot mosmi?<br>
            • yer sathi bilan aloqa tushunarlimi?
            """,
        },
        {
            "title": "5. Grunt ma'lumoti",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • geologik ma'lumot mavjudmi?<br>
            • konstruktor undan foydalanyaptimi?<br>
            • suv va yer sharoitlari hisobga olinganmi?
            """,
        },
        {
            "title": "6. Muhandislik tizimlari",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • kommunikatsiya kirishlari qayerda?<br>
            • fundament bilan to'qnashuv bormi?<br>
            • kerakli o'tish joylari oldindan koordinatsiya qilinganmi?
            """,
        },
        {
            "title": "7. BIM model",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • plan to'g'rimi?<br>
            • kesim to'g'rimi?<br>
            • 3D modelda siljish yo'qmi?<br>
            • elementlar dublikat emasmi?
            """,
        },
        {
            "title": "Xatoni toping",
            "type": "warning",
            "text": """
            Loyiha planida:

            <br><br>

            • 2-qavat devori pastdagi devordan siljigan;<br>
            • bitta ustun o'qdan chiqib ketgan;<br>
            • kanalizatsiya chiqishi fundament orqali o'tadi;<br>
            • geologik ma'lumot hali olinmagan;<br>
            • fundament turi allaqachon yakuniy deb yozilgan.

            <br><br>

            Bu loyiha
            koordinatsiyaga
            qaytarilishi kerak.
            """,
        },
        {
            "title": "Professional checklist",
            "type": "example",
            "text": """
            Fundament bo'yicha
            arxitektura audit:

            <br><br>

            <b>1.</b> Yuk ko'taruvchi tizim aniqmi?<br><br>
            <b>2.</b> Vertikal yuk yo'li tushunarlimi?<br><br>
            <b>3.</b> Ustun va devorlar o'qlarga mosmi?<br><br>
            <b>4.</b> Qavatlar o'zaro koordinatsiyalanganmi?<br><br>
            <b>5.</b> Fundament konstruktiv loyiha bilan mosmi?<br><br>
            <b>6.</b> Grunt ma'lumotlari mavjudmi?<br><br>
            <b>7.</b> Muhandislik kirishlari koordinatsiya qilinganmi?<br><br>
            <b>8.</b> Plan, kesim va 3D bir-biriga mosmi?<br><br>
            <b>9.</b> Konstruktor bilan o'zgarishlar kelishilganmi?
            """,
        },
        {
            "title": "Modul yakuni",
            "type": "highlight",
            "text": """
            Siz endi:

            <br><br>

            ✓ fundamentning vazifasini tushunasiz;<br>
            ✓ asosiy fundament turlarini farqlaysiz;<br>
            ✓ gruntning ahamiyatini bilasiz;<br>
            ✓ yuk uzatish mantig'ini tushunasiz;<br>
            ✓ arxitektura va fundamentni koordinatsiya qilasiz;<br>
            ✓ konstruktor bilan savodli ishlash uchun asosiy savollarni bilasiz.

            <br><br>

            Keyingi modul:
            <b>Devor konstruksiyasi.</b>
            """,
        },
    ],
}


# ============================================================
# QUIZ
# Q001-Q015
# ============================================================

LEVEL08_MODULE01_QUIZ = {
    "L08_M01_001": [
        {
            "code": "L08_Q001",
            "question": "Fundamentning asosiy vazifalaridan biri bino yuklarini gruntga uzatishmi?",
            "explanation": (
                "Fundament binodan kelayotgan yuklarni yer asosiga uzatadigan konstruktiv tizimning muhim qismidir."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L08_Q002",
            "question": "Fundamentning aniq o'lchami faqat arxitektorning taxmini bilan belgilanadimi?",
            "explanation": (
                "Aniq fundament yechimi grunt, yuklar va konstruktiv hisoblar asosida belgilanadi."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L08_Q003",
            "question": "Arxitektor yuklarning bino bo'ylab fundamentga qanday uzatilishini tushunishi kerakmi?",
            "explanation": (
                "Yuk yo'lini tushunish arxitektura va konstruktiv tizimni to'g'ri koordinatsiya qilishga yordam beradi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L08_M01_002": [
        {
            "code": "L08_Q004",
            "question": "Barcha binolar uchun bitta universal eng yaxshi fundament turi mavjudmi?",
            "explanation": (
                "Fundament turi bino sxemasi, yuklar, grunt va boshqa loyiha sharoitlariga qarab tanlanadi."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L08_Q005",
            "question": "Lenta fundament uzluksiz devorlar ostida ishlatiladigan tayanch sxemasi bo'lishi mumkinmi?",
            "explanation": (
                "Lenta fundament odatda uzluksiz yuk ko'taruvchi devorlar bilan bog'liq sxemalarda uchraydi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L08_Q006",
            "question": "Qo'shni binodagi fundament turini tekshirmasdan aynan ko'chirish professional yechimmi?",
            "explanation": (
                "Har bir bino va grunt sharoiti alohida baholanishi kerak."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
    ],

    "L08_M01_003": [
        {
            "code": "L08_Q007",
            "question": "Grunt xususiyatlari fundament tanloviga ta'sir qilishi mumkinmi?",
            "explanation": (
                "Gruntning xususiyatlari va yer osti sharoitlari konstruktiv fundament yechimiga bevosita ta'sir qiladi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L08_Q008",
            "question": "Muhandislik-geologik ma'lumot fundament loyihasi uchun muhim emasmi?",
            "explanation": (
                "Geologik ma'lumot yer asosining real sharoitlarini tushunish uchun muhim."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L08_Q009",
            "question": "Yer osti suvlari fundament va gidroizolyatsiya yechimlariga ta'sir qilishi mumkinmi?",
            "explanation": (
                "Yer osti suvlari yer osti konstruktsiyalarining himoyasi va loyiha yechimlariga ta'sir qilishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L08_M01_004": [
        {
            "code": "L08_Q010",
            "question": "Arxitektura va konstruktiv o'qlarni o'zaro koordinatsiya qilish kerakmi?",
            "explanation": (
                "Tayanchlar, ustunlar va fundamentlarning joylashuvi yagona koordinata tizimida ishlashi kerak."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L08_Q011",
            "question": "Ustunni arxitektura planida ko'chirish fundament yechimiga ta'sir qilmasligi kafolatlanganmi?",
            "explanation": (
                "Ustun joyining o'zgarishi yuk uzatish va fundament joylashuviga ta'sir qilishi mumkin."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L08_Q012",
            "question": "Muhandislik kommunikatsiyalarining fundament bilan to'qnashuvini oldindan tekshirish kerakmi?",
            "explanation": (
                "Kommunikatsiya o'tishlari va fundament zonalari oldindan koordinatsiya qilinishi kerak."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L08_M01_005": [
        {
            "code": "L08_Q013",
            "question": "Fundament auditida plan, kesim va 3D modelning o'zaro mosligi tekshiriladimi?",
            "explanation": (
                "Turli ko'rinishlardagi konstruktiv va arxitektura ma'lumotlari bir-biriga mos bo'lishi kerak."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L08_Q014",
            "question": "Fundament bo'yicha konstruktiv o'zgarishlarni konstruktor bilan kelishish kerakmi?",
            "explanation": (
                "Yuk ko'taruvchi tizim va fundamentga ta'sir qiluvchi o'zgarishlar mutaxassis bilan koordinatsiya qilinadi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L08_Q015",
            "question": "Fundament bilan professional ishlashdagi to'g'ri umumiy workflow qaysi?",
            "explanation": (
                "Avval bino va tayanchlar tushuniladi, grunt ma'lumotlari olinadi, konstruktiv yechim ishlab chiqiladi va arxitektura bilan koordinatsiya qilinadi."
            ),
            "options": [
                (
                    "A",
                    "Arxitektura → yuk yo'li → grunt ma'lumoti → konstruktiv yechim → koordinatsiya → audit",
                    True,
                ),
                (
                    "B",
                    "Qo'shni fundamentini ko'chirish → tekshirmaslik → qurishni boshlash",
                    False,
                ),
            ],
        },
    ],
}


# ============================================================
# DATABASE SEED
# ============================================================

def seed_level08_module01():
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
        ) in LEVEL08_MODULE01_LESSONS:

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
