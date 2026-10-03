from database.database import get_connection


# ============================================================
# LEVEL 7
# MODULE 09 - PROFESSIONAL TEMPLATE
# ============================================================

LEVEL07_MODULE09_LESSONS = [
    (
        "L07_M09",
        "L07_M09_001",
        "Professional Template tushunchasi",
        "theory",
        "Professional Archicad template nima ekanini va nima uchun loyiha standartining asosi ekanini tushunish.",
        1,
        70,
        20,
    ),
    (
        "L07_M09",
        "L07_M09_002",
        "Template strukturasi",
        "theory",
        "Layers, Favorites, Attributes, Views va boshqa asosiy qismlarni yagona mantiqiy tizimga yig'ish.",
        2,
        80,
        20,
    ),
    (
        "L07_M09",
        "L07_M09_003",
        "View, Graphic va Documentation standard",
        "practice",
        "Graphic Overrides, Model View Options, View Map va hujjatlashtirish sozlamalarini standartlashtirish.",
        3,
        85,
        20,
    ),
    (
        "L07_M09",
        "L07_M09_004",
        "BIM data standard",
        "practice",
        "Properties, Classification, Schedules va element ma'lumotlarini professional template ichida standartlashtirish.",
        4,
        85,
        20,
    ),
    (
        "L07_M09",
        "L07_M09_005",
        "Professional Template audit",
        "practice",
        "Template'ni real loyiha boshlashga tayyor holatda kompleks audit qilish va versiyalash.",
        5,
        100,
        25,
    ),
]


# ============================================================
# CONTENT
# ============================================================

LEVEL07_MODULE09_CONTENT = {
    "L07_M09_001": [
        {
            "title": "Template nima?",
            "type": "highlight",
            "text": """
            Professional Template —
            yangi loyiha boshlanganda

            <br><br>

            qayta-qayta
            bir xil sozlamalarni
            noldan yaratmaslik uchun

            <br><br>

            oldindan tayyorlangan
            ishchi loyiha bazasi.
            """,
        },
        {
            "title": "Template faqat bo'sh fayl emas",
            "type": "warning",
            "text": """
            Ichida hech narsa
            bo'lmagan bo'sh fayl

            <br><br>

            professional Template
            degani emas.

            <br><br>

            Template ichida
            loyiha standartlari
            oldindan tashkil
            qilingan bo'lishi kerak.
            """,
        },
        {
            "title": "Template nimani tejaydi?",
            "type": "highlight",
            "text": """
            To'g'ri Template:

            <br><br>

            • vaqtni tejaydi;<br>
            • xatolarni kamaytiradi;<br>
            • naming'ni standartlashtiradi;<br>
            • jamoaviy ishlashni osonlashtiradi;<br>
            • loyiha sifatini barqaror qiladi.
            """,
        },
        {
            "title": "Tasavvur qiling",
            "type": "example",
            "text": """
            Har bir yangi loyiha
            boshlaganda siz:

            <br><br>

            Layers yaratishingiz,
            Favorites tayyorlashingiz,
            pen va materiallarni tekshirishingiz,
            view sozlashingiz,
            schedules yaratishingiz kerak.

            <br><br>

            Bu ishlarning katta qismi
            Template ichida
            oldindan tayyor bo'lishi mumkin.
            """,
        },
        {
            "title": "Template — standart",
            "type": "normal",
            "text": """
            Template
            loyihaning boshlang'ich
            texnik va BIM
            standartini belgilaydi.

            <br><br>

            U foydalanuvchini
            yaxshi workflowga
            yo'naltiradi.
            """,
        },
        {
            "title": "Template hamma loyihaga bir xil emas",
            "type": "warning",
            "text": """
            Har qanday Template
            barcha loyiha turlariga
            ideal bo'lishi shart emas.

            <br><br>

            Turar joy,
            villa,
            rekonstruksiya
            yoki boshqa loyiha turi

            <br><br>

            turli sozlamalarni
            talab qilishi mumkin.
            """,
        },
        {
            "title": "Template maqsadini aniqlash",
            "type": "highlight",
            "text": """
            Template yaratishdan oldin
            aniqlang:

            <br><br>

            • qaysi loyiha turi uchun?<br>
            • kim ishlatadi?<br>
            • qanday standart kerak?<br>
            • qaysi hujjatlar chiqariladi?
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            O'zingiz yaratmoqchi bo'lgan
            Professional Template uchun

            <br><br>

            5 ta asosiy maqsad yozing.

            <br><br>

            Masalan:

            • turar joy loyihasi;<br>
            • standart layerlar;<br>
            • tayyor views;<br>
            • tayyor schedules;<br>
            • yagona naming.
            """,
        },
    ],

    "L07_M09_002": [
        {
            "title": "Template strukturasi",
            "type": "highlight",
            "text": """
            Professional Template
            alohida sozlamalar
            to'plami emas.

            <br><br>

            U yagona tizim
            bo'lishi kerak.
            """,
        },
        {
            "title": "Layers",
            "type": "normal",
            "text": """
            Layerlar:

            <br><br>

            • tushunarli naming;<br>
            • aniq vazifa;<br>
            • keraksiz dublikatlarsiz;<br>
            • loyiha workflowiga mos

            <br><br>

            bo'lishi kerak.
            """,
        },
        {
            "title": "Layer Combination",
            "type": "normal",
            "text": """
            Faqat Layer yaratish
            yetarli emas.

            <br><br>

            Kerakli viewlar uchun
            Layer Combination
            mantiqi ham
            oldindan tashkil
            qilinishi mumkin.
            """,
        },
        {
            "title": "Favorites",
            "type": "highlight",
            "text": """
            Favorites ichida
            tez-tez ishlatiladigan
            standart elementlar

            <br><br>

            oldindan
            saqlanishi mumkin.

            <br><br>

            Masalan:

            • standart devor;<br>
            • eshik;<br>
            • deraza;<br>
            • slab;<br>
            • boshqa elementlar.
            """,
        },
        {
            "title": "Building Materials",
            "type": "normal",
            "text": """
            Building Materials
            naming va
            parametrlar bo'yicha

            <br><br>

            izchil bo'lishi
            kerak.
            """,
        },
        {
            "title": "Composites",
            "type": "normal",
            "text": """
            Tez-tez ishlatiladigan
            devor va boshqa
            ko'p qatlamli
            konstruksiyalar

            <br><br>

            Template ichida
            oldindan tayyor
            bo'lishi mumkin.
            """,
        },
        {
            "title": "Complex Profiles",
            "type": "normal",
            "text": """
            Agar loyiha workflowda
            takror ishlatiladigan
            maxsus profillar bo'lsa,

            <br><br>

            ular ham
            Template tizimiga
            kirishi mumkin.
            """,
        },
        {
            "title": "Attributes tartibi",
            "type": "warning",
            "text": """
            Keraksiz,
            test uchun yaratilgan
            yoki dublikat Attributes

            <br><br>

            Template ichida
            qolib ketmasligi kerak.
            """,
        },
        {
            "title": "Naming tizimi",
            "type": "highlight",
            "text": """
            Professional Template
            ichida naming

            <br><br>

            bitta umumiy
            mantiqqa ega bo'lishi kerak.

            <br><br>

            Tasodifiy nomlar
            kelajakda katta
            chalkashlik yaratadi.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Template uchun
            quyidagilarni yozing:

            <br><br>

            • 5 ta Layer;<br>
            • 3 ta Favorite;<br>
            • 3 ta Composite;<br>
            • 3 ta Building Material;<br>
            • bitta naming qoidasi.
            """,
        },
    ],

    "L07_M09_003": [
        {
            "title": "View standard",
            "type": "highlight",
            "text": """
            Professional Template'da
            Views tasodifiy
            yaratilmaydi.

            <br><br>

            Har bir View
            aniq vazifaga
            ega bo'lishi kerak.
            """,
        },
        {
            "title": "View Map",
            "type": "normal",
            "text": """
            View Map ichida
            loyiha hujjatlari

            <br><br>

            tushunarli papkalar
            va naming orqali
            tashkil qilinishi
            mumkin.
            """,
        },
        {
            "title": "Graphic Overrides",
            "type": "highlight",
            "text": """
            Graphic Overrides
            Template ichida

            <br><br>

            modelni tahlil qilish
            uchun standart
            grafik kombinatsiyalar
            yaratishda foydali.
            """,
        },
        {
            "title": "MVO",
            "type": "normal",
            "text": """
            Model View Options
            turli hujjatlarda
            model tafsilotlarini

            <br><br>

            izchil ko'rsatish
            uchun Template'da
            standartlashtirilishi
            mumkin.
            """,
        },
        {
            "title": "Existing, Demolition, Proposed",
            "type": "example",
            "text": """
            Rekonstruksiya Template'da
            loyiha maqsadiga qarab

            <br><br>

            Existing,
            Demolition
            va Proposed

            <br><br>

            view konsepsiyalari
            oldindan tayyor
            bo'lishi mumkin.
            """,
        },
        {
            "title": "View naming",
            "type": "warning",
            "text": """
            “View 1”,
            “New View”,
            “Copy 2”

            <br><br>

            kabi nomlar
            professional Template
            uchun yaxshi standart emas.
            """,
        },
        {
            "title": "Documentation standard",
            "type": "highlight",
            "text": """
            Template'da
            loyiha hujjatlari uchun

            <br><br>

            umumiy grafik va
            naming standard
            bo'lishi kerak.
            """,
        },
        {
            "title": "Bir xil loyiha tili",
            "type": "normal",
            "text": """
            Plan,
            Section,
            Elevation
            va boshqa chizmalar

            <br><br>

            bir xil loyiha
            grafik tilida
            ishlashi kerak.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Template uchun
            View strukturasi tuzing.

            <br><br>

            Masalan:

            01_PLANS<br>
            02_SECTIONS<br>
            03_ELEVATIONS<br>
            04_SCHEDULES<br>
            05_PRESENTATION

            <br><br>

            Bu faqat namuna.
            O'zingizga mos
            tizim yarating.
            """,
        },
    ],

    "L07_M09_004": [
        {
            "title": "BIM data standard",
            "type": "highlight",
            "text": """
            Professional Template
            faqat grafik sozlamalar
            emas.

            <br><br>

            BIM ma'lumotlari
            ham oldindan
            standartlashtiriladi.
            """,
        },
        {
            "title": "Properties",
            "type": "normal",
            "text": """
            Tez-tez kerak bo'ladigan
            custom Properties

            <br><br>

            Template ichida
            oldindan tashkil
            qilinishi mumkin.
            """,
        },
        {
            "title": "Classification",
            "type": "normal",
            "text": """
            Element Classification
            BIM ma'lumot
            strukturasining

            <br><br>

            izchil ishlashi
            uchun tekshiriladi.
            """,
        },
        {
            "title": "Schedules",
            "type": "highlight",
            "text": """
            Professional Template'da
            kerakli Schedules

            <br><br>

            oldindan tayyor
            bo'lishi mumkin.

            <br><br>

            Masalan:

            • Door Schedule;<br>
            • Window Schedule;<br>
            • Zone Schedule;<br>
            • audit Schedule.
            """,
        },
        {
            "title": "Schedule — audit qismi",
            "type": "normal",
            "text": """
            Template'dagi Schedule
            faqat yakuniy jadval
            uchun emas.

            <br><br>

            U yangi loyihani
            boshidan audit
            qilishga ham
            yordam berishi mumkin.
            """,
        },
        {
            "title": "Bo'sh Properties",
            "type": "warning",
            "text": """
            Template ichida
            Property mavjud bo'lishi

            <br><br>

            barcha loyihalarda
            uni avtomatik
            to'ldiradi degani emas.

            <br><br>

            Foydalanuvchi workflowi
            ham to'g'ri bo'lishi kerak.
            """,
        },
        {
            "title": "Data overload",
            "type": "warning",
            "text": """
            Juda ko'p
            Properties,
            Classifications
            va Schedules

            <br><br>

            Template'ni
            keraksiz murakkablashtirishi
            mumkin.

            <br><br>

            Faqat ishlatiladigan
            tizimni saqlang.
            """,
        },
        {
            "title": "BIM audit workflow",
            "type": "highlight",
            "text": """
            Professional Template:

            <br><br>

            Model
            → Classification
            → Properties
            → Schedule
            → Audit

            <br><br>

            zanjirini qo'llab-quvvatlashi
            kerak.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Template uchun
            BIM data paketini
            rejalashtiring:

            <br><br>

            • 5 ta Property;<br>
            • Classification konsepsiyasi;<br>
            • 3 ta Schedule;<br>
            • 1 ta audit Schedule.
            """,
        },
    ],

    "L07_M09_005": [
        {
            "title": "Professional Template audit",
            "type": "highlight",
            "text": """
            Template auditini
            quyidagi zanjirda
            bajaramiz:

            <br><br>

            Structure
            → Attributes
            → Favorites
            → Views
            → Graphics
            → BIM Data
            → Schedules
            → Test Project
            """,
        },
        {
            "title": "1. Structure audit",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • Template maqsadi aniqmi?<br>
            • loyiha turi belgilanganmi?<br>
            • papka va naming tizimi tushunarlimi?
            """,
        },
        {
            "title": "2. Layers audit",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • keraksiz Layer yo'qmi?<br>
            • dublikat Layer yo'qmi?<br>
            • naming izchilmi?<br>
            • Layer Combinations ishlayaptimi?
            """,
        },
        {
            "title": "3. Attributes audit",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • Building Materials tartiblimi?<br>
            • Composites keraklimi?<br>
            • Profiles tushunarlimi?<br>
            • test Attributes qolmaganmi?
            """,
        },
        {
            "title": "4. Favorites audit",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • Favorites haqiqatan ishlatiladimi?<br>
            • naming aniqmi?<br>
            • eski yoki noto'g'ri Favorites yo'qmi?
            """,
        },
        {
            "title": "5. Views audit",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • View Map tartiblimi?<br>
            • kerakli Views bormi?<br>
            • naming izchilmi?<br>
            • keraksiz test Views qolmaganmi?
            """,
        },
        {
            "title": "6. Graphic standard audit",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • Graphic Overrides ishlayaptimi?<br>
            • MVO combinations tushunarlimi?<br>
            • turli Views bir xil grafik standardga egami?
            """,
        },
        {
            "title": "7. BIM Data audit",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • Properties keraklimi?<br>
            • Classification izchilmi?<br>
            • keraksiz BIM data yo'qmi?<br>
            • naming standartmi?
            """,
        },
        {
            "title": "8. Schedule audit",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • Door Schedule ishlayaptimi?<br>
            • Window Schedule ishlayaptimi?<br>
            • Zone Schedule ishlayaptimi?<br>
            • audit Schedules foydalimi?
            """,
        },
        {
            "title": "9. Test Project",
            "type": "highlight",
            "text": """
            Template'ni
            faqat sozlamalarga qarab
            baholamang.

            <br><br>

            U bilan kichik
            test loyiha
            boshlab ko'ring.
            """,
        },
        {
            "title": "Test scenario",
            "type": "example",
            "text": """
            Test loyihada:

            <br><br>

            • 4 ta devor;<br>
            • 2 ta eshik;<br>
            • 2 ta deraza;<br>
            • 1 ta xona;<br>
            • 1 ta Schedule;<br>
            • 1 ta Plan View

            <br><br>

            yaratib Template
            qanday ishlashini
            tekshiring.
            """,
        },
        {
            "title": "10. Versioning",
            "type": "highlight",
            "text": """
            Professional Template
            vaqt o'tishi bilan
            rivojlanadi.

            <br><br>

            O'zgarishlarni
            versiyalar orqali
            nazorat qilish
            foydali.
            """,
        },
        {
            "title": "Version misoli",
            "type": "example",
            "text": """
            Masalan:

            <br><br>

            ARCHIPRO_TEMPLATE_V1<br>
            ARCHIPRO_TEMPLATE_V2

            <br><br>

            yoki sana asosidagi
            naming ishlatilishi mumkin.

            <br><br>

            Bu faqat naming
            konsepsiyasi.
            """,
        },
        {
            "title": "Eski Template'ni saqlash",
            "type": "normal",
            "text": """
            Template yangilanganda
            oldingi versiyani
            darhol yo'q qilish

            <br><br>

            har doim ham
            yaxshi qaror emas.

            <br><br>

            Kerak bo'lsa
            arxiv versiyasi
            saqlanishi mumkin.
            """,
        },
        {
            "title": "Xatoni toping",
            "type": "warning",
            "text": """
            Template ichida:

            <br><br>

            • 70 ta tushunarsiz Layer;<br>
            • ko'p dublikat material;<br>
            • Favorites nomlari chalkash;<br>
            • View Map tartibsiz;<br>
            • 25 ta keraksiz Property;<br>
            • Schedules ishlamaydi;<br>
            • test loyiha qilinmagan.

            <br><br>

            Fayl katta,
            lekin professional
            Template emas.
            """,
        },
        {
            "title": "Professional checklist",
            "type": "example",
            "text": """
            Final Template audit:

            <br><br>

            <b>1.</b> Maqsad aniqmi?<br><br>
            <b>2.</b> Layers standartmi?<br><br>
            <b>3.</b> Favorites tayyormi?<br><br>
            <b>4.</b> Building Materials to'g'rimi?<br><br>
            <b>5.</b> Composites va Profiles tartiblimi?<br><br>
            <b>6.</b> Graphic Overrides tayyormi?<br><br>
            <b>7.</b> MVO tayyormi?<br><br>
            <b>8.</b> View Map tartiblimi?<br><br>
            <b>9.</b> Properties standartmi?<br><br>
            <b>10.</b> Classification to'g'rimi?<br><br>
            <b>11.</b> Schedules ishlayaptimi?<br><br>
            <b>12.</b> Keraksiz sozlamalar tozalanganmi?<br><br>
            <b>13.</b> Test Project o'tkazilganmi?<br><br>
            <b>14.</b> Version nomi berilganmi?
            """,
        },
        {
            "title": "LEVEL 7 yakuni",
            "type": "highlight",
            "text": """
            LEVEL 7 davomida siz:

            <br><br>

            ✓ Favorites bilan ishladingiz;<br>
            ✓ Graphic Overrides'ni o'rgandingiz;<br>
            ✓ Model View Options'ni o'rgandingiz;<br>
            ✓ Renovation workflowini tushundingiz;<br>
            ✓ Schedules tuzdingiz;<br>
            ✓ Properties bilan ishladingiz;<br>
            ✓ Classification'ni o'rgandingiz;<br>
            ✓ Hotlink va Modules bilan ishladingiz;<br>
            ✓ Professional Template tuzishni o'rgandingiz.

            <br><br>

            Endi LEVEL 7
            final imtihoniga
            tayyorlanasiz.
            """,
        },
    ],
}


# ============================================================
# QUIZ
# Q121-Q135
# ============================================================

LEVEL07_MODULE09_QUIZ = {
    "L07_M09_001": [
        {
            "code": "L07_Q121",
            "question": "Professional Template yangi loyiha boshlash uchun oldindan tayyorlangan standart ishchi baza bo'lishi mumkinmi?",
            "explanation": (
                "Template yangi loyihalarda bir xil sozlamalarni qayta yaratishni kamaytiradi va standart workflow beradi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L07_Q122",
            "question": "Ichida hech qanday standart bo'lmagan bo'sh fayl avtomatik ravishda professional Template hisoblanadimi?",
            "explanation": (
                "Professional Template ichida loyiha va BIM standartlari oldindan tashkil qilingan bo'lishi kerak."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L07_Q123",
            "question": "Template loyiha turiga qarab farq qilishi mumkinmi?",
            "explanation": (
                "Turli loyiha turlari turli standart, view va BIM ma'lumot talablariga ega bo'lishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L07_M09_002": [
        {
            "code": "L07_Q124",
            "question": "Professional Template'da Layers, Favorites va Attributes izchil tizimda tashkil qilinishi kerakmi?",
            "explanation": (
                "Template alohida tasodifiy sozlamalar emas, yagona ishchi tizim bo'lishi kerak."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L07_Q125",
            "question": "Test va dublikat Attributes'ni Template ichida cheksiz qoldirish yaxshi amaliyotmi?",
            "explanation": (
                "Keraksiz va dublikat Attributes template sifatini pasaytiradi va boshqaruvni qiyinlashtiradi."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L07_Q126",
            "question": "Naming standard Template boshqaruvini yaxshilaydimi?",
            "explanation": (
                "Izchil naming jamoaga sozlamalarni tez tushunish va xatolarni kamaytirishga yordam beradi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L07_M09_003": [
        {
            "code": "L07_Q127",
            "question": "Template ichida View Map va grafik sozlamalarni oldindan standartlashtirish mumkinmi?",
            "explanation": (
                "Professional Template view va grafik workflowini oldindan tashkil qilishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L07_Q128",
            "question": "Graphic Overrides va MVO aynan bir xil vazifani bajaradimi?",
            "explanation": (
                "Graphic Overrides grafik tahlil va ko'rinish qoidalarini, MVO esa model ko'rinish tafsilotlarini boshqarishga xizmat qiladi."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L07_Q129",
            "question": "View naming tushunarli va izchil bo'lishi kerakmi?",
            "explanation": (
                "Tushunarli naming professional hujjatlashtirish va jamoaviy workflow uchun muhim."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L07_M09_004": [
        {
            "code": "L07_Q130",
            "question": "Professional Template ichida Properties, Classification va Schedules oldindan standartlashtirilishi mumkinmi?",
            "explanation": (
                "BIM ma'lumot strukturasini oldindan tashkil qilish yangi loyihalarda izchillik yaratadi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L07_Q131",
            "question": "Juda ko'p keraksiz BIM Properties Template'ni murakkablashtirishi mumkinmi?",
            "explanation": (
                "Faqat ishlatiladigan va maqsadli BIM ma'lumotlarni saqlash yaxshi amaliyot hisoblanadi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L07_Q132",
            "question": "Schedule Template ichida model audit vositasi sifatida ham ishlatilishi mumkinmi?",
            "explanation": (
                "Audit Schedules yangi loyiha modelidagi bo'sh yoki noto'g'ri ma'lumotlarni aniqlashga yordam beradi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L07_M09_005": [
        {
            "code": "L07_Q133",
            "question": "Professional Template'ni kichik test loyiha orqali tekshirish foydalimi?",
            "explanation": (
                "Test Project real workflowda Layers, Views, Favorites, Schedules va boshqa sozlamalar ishlashini tekshiradi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L07_Q134",
            "question": "Template versiyalarini nazorat qilish foydali bo'lishi mumkinmi?",
            "explanation": (
                "Versioning template'dagi o'zgarishlarni kuzatish va eski holatlarni boshqarishga yordam beradi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L07_Q135",
            "question": "Professional Template yaratishdagi to'g'ri umumiy workflow qaysi?",
            "explanation": (
                "Avval maqsad aniqlanadi, struktura va standartlar yaratiladi, BIM ma'lumotlari tashkil qilinadi, test loyiha bilan audit qilinadi va versiyalanadi."
            ),
            "options": [
                (
                    "A",
                    "Maqsad → Structure → Standards → BIM Data → Views/Schedules → Test → Audit → Version",
                    True,
                ),
                (
                    "B",
                    "Ko'p sozlama yaratish → naming bermaslik → test qilmaslik → darhol ishlatish",
                    False,
                ),
            ],
        },
    ],
}


# ============================================================
# DATABASE SEED
# ============================================================

def seed_level07_module09():
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
        ) in LEVEL07_MODULE09_LESSONS:

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
