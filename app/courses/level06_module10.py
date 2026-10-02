from database.database import get_connection


# ============================================================
# LEVEL 6
# MODULE 10 - ZONES
# ============================================================

LEVEL06_MODULE10_LESSONS = [
    (
        "L06_M10",
        "L06_M10_001",
        "Zone tushunchasi",
        "theory",
        "Archicadda xona va funksional makonlarni Zone elementi orqali BIM ma'lumot sifatida boshqarish.",
        1,
        40,
        20,
    ),
    (
        "L06_M10",
        "L06_M10_002",
        "Zone chegarasi va maydon",
        "theory",
        "Xona chegaralari va Zone maydoni o'rtasidagi bog'lanish mantig'ini tushunish.",
        2,
        45,
        20,
    ),
    (
        "L06_M10",
        "L06_M10_003",
        "Zone Stamp va xona ma'lumotlari",
        "practice",
        "Xona nomi, raqami, maydoni va boshqa Zone ma'lumotlarini chizmada tartibli ko'rsatish.",
        3,
        50,
        20,
    ),
    (
        "L06_M10",
        "L06_M10_004",
        "Funksional zonalar va loyiha tahlili",
        "practice",
        "Xonalarni funksiyasi bo'yicha tashkil qilish va Zone ma'lumotlari orqali loyiha rejasini tahlil qilish.",
        4,
        50,
        20,
    ),
    (
        "L06_M10",
        "L06_M10_005",
        "Zones professional audit",
        "practice",
        "Zone nomlari, chegaralar, maydonlar, stamp va xona strukturasini kompleks tekshirish.",
        5,
        55,
        25,
    ),
]


# ============================================================
# CONTENT
# ============================================================

LEVEL06_MODULE10_CONTENT = {
    "L06_M10_001": [
        {
            "title": "Zone nima?",
            "type": "highlight",
            "text": """
            Zone —
            Archicadda xona
            yoki funksional makonni

            <br><br>

            BIM ma'lumotga ega
            alohida element sifatida
            belgilashga yordam beradi.
            """,
        },
        {
            "title": "Zone faqat yozuv emas",
            "type": "normal",
            "text": """
            Zone'ni faqat
            xona nomini yozadigan
            Text elementi deb
            tushunish xato.

            <br><br>

            Zone xona haqida
            turli ma'lumotlarni
            saqlashi mumkin.
            """,
        },
        {
            "title": "Zone nimani ifodalaydi?",
            "type": "highlight",
            "text": """
            Zone orqali:

            <br><br>

            • xona nomi;<br>
            • xona raqami;<br>
            • maydon;<br>
            • funksional kategoriya;<br>
            • boshqa xona ma'lumotlari

            <br><br>

            boshqarilishi mumkin.
            """,
        },
        {
            "title": "Tasavvur qiling",
            "type": "example",
            "text": """
            Planda 15 ta xona bor.

            <br><br>

            Har birining nomi
            oddiy Text bilan yozilgan.

            <br><br>

            Xona o'lchami o'zgarsa
            maydonni qo'lda
            qayta hisoblash kerak.

            <br><br>

            BIM workflowda esa
            xona ma'lumotini
            Zone bilan boshqarish
            ancha tartibli bo'lishi mumkin.
            """,
        },
        {
            "title": "Arxitektura va ma'lumot",
            "type": "normal",
            "text": """
            Zone —
            model geometriyasi
            va loyiha ma'lumotlari
            orasidagi bog'lovchi
            elementlardan biri.

            <br><br>

            Shu sabab uni
            faqat grafik belgi
            sifatida ko'rmang.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Oddiy uy planini oling.

            <br><br>

            5 ta xona uchun
            Zone yarating.

            <br><br>

            Masalan:

            • Living Room;<br>
            • Kitchen;<br>
            • Bedroom;<br>
            • Bathroom;<br>
            • Hallway.

            <br><br>

            Har biriga
            tushunarli nom bering.
            """,
        },
    ],

    "L06_M10_002": [
        {
            "title": "Zone chegarasi",
            "type": "highlight",
            "text": """
            Zone maydoni
            uning fazoviy
            chegarasi bilan
            bog'liq.

            <br><br>

            Shuning uchun
            xona chegaralari
            to'g'ri aniqlanishi kerak.
            """,
        },
        {
            "title": "Xona yopiqmi?",
            "type": "normal",
            "text": """
            Xona geometriyasida
            kutilmagan ochilish
            yoki uzilish bo'lsa,

            <br><br>

            Zone chegarasini
            aniqlashda muammo
            paydo bo'lishi mumkin.
            """,
        },
        {
            "title": "Automatic va manual mantiq",
            "type": "normal",
            "text": """
            Loyihaga qarab
            Zone chegarasi

            <br><br>

            mavjud xona
            geometriyasiga asoslanib
            yoki qo'lda belgilangan
            kontur orqali
            boshqarilishi mumkin.

            <br><br>

            Muhim narsa —
            yakuniy chegarani
            tekshirish.
            """,
        },
        {
            "title": "Maydon",
            "type": "highlight",
            "text": """
            Zone xona maydonini
            hisoblash va ko'rsatishda
            yordam beradi.

            <br><br>

            Lekin natija
            to'g'ri bo'lishi uchun

            <br><br>

            xona chegarasi ham
            to'g'ri bo'lishi kerak.
            """,
        },
        {
            "title": "Devor siljisa",
            "type": "example",
            "text": """
            Bedroom devori
            siljitildi.

            <br><br>

            Xona kattalashdi.

            <br><br>

            Zone bilan ishlaganda
            maydon va Zone chegarasini
            qayta tekshirish kerak.

            <br><br>

            Faqat eski yozuvga
            qarab qolmang.
            """,
        },
        {
            "title": "Maydon — faqat raqam emas",
            "type": "normal",
            "text": """
            Xona maydoni
            rejalashtirish qarorlarini
            tekshirishga yordam beradi.

            <br><br>

            Masalan:

            • xona haddan tashqari kattami?<br>
            • juda kichikmi?<br>
            • boshqa xonalarga nisbatan balanslimi?

            <br><br>

            kabi savollar beriladi.
            """,
        },
        {
            "title": "Normativ maydon",
            "type": "warning",
            "text": """
            Zone ko'rsatgan maydon
            avtomatik ravishda

            <br><br>

            xona barcha normativ
            talablarga javob beradi
            degani emas.

            <br><br>

            Normativ tekshiruv
            alohida bosqich.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Bitta xona yarating
            va unga Zone qo'ying.

            <br><br>

            Keyin devorni siljiting.

            <br><br>

            Zone chegarasi
            va maydon natijasini
            qayta tekshiring.
            """,
        },
    ],

    "L06_M10_003": [
        {
            "title": "Zone Stamp nima?",
            "type": "highlight",
            "text": """
            Zone Stamp —
            Zone haqidagi
            ma'lumotlarni

            <br><br>

            Floor Planda
            ko'rsatishga xizmat
            qiladigan grafik qism.
            """,
        },
        {
            "title": "Stampdagi ma'lumotlar",
            "type": "normal",
            "text": """
            Zone Stampda
            loyiha sozlamalariga qarab:

            <br><br>

            • xona nomi;<br>
            • xona raqami;<br>
            • maydon;<br>
            • boshqa parametrlar

            <br><br>

            ko'rsatilishi mumkin.
            """,
        },
        {
            "title": "Xona nomlari",
            "type": "highlight",
            "text": """
            Xona nomlari
            tartibli va izchil
            bo'lishi kerak.

            <br><br>

            Masalan bir joyda:

            Bedroom

            <br><br>

            boshqa joyda:

            Bed Room

            <br><br>

            uchinchi joyda:

            Spalnya

            <br><br>

            kabi tasodifiy aralash
            naming ishlatishdan
            qoching.
            """,
        },
        {
            "title": "Room numbering",
            "type": "normal",
            "text": """
            Katta loyihada
            xona raqamlari

            <br><br>

            xonalarni aniqlash
            va hujjatlarda
            topishni osonlashtiradi.

            <br><br>

            Raqamlash tizimi
            izchil bo'lishi kerak.
            """,
        },
        {
            "title": "Stamp joylashuvi",
            "type": "warning",
            "text": """
            Zone Stamp:

            <br><br>

            • devor ustiga chiqib ketmasin;<br>
            • mebelni keraksiz yopmasin;<br>
            • boshqa annotation bilan urishmasin;<br>
            • o'qilishi qiyin joyda qolmasin.
            """,
        },
        {
            "title": "Chizma aniqligi",
            "type": "normal",
            "text": """
            Professional plan
            faqat ma'lumotga boy emas,

            <br><br>

            uni tez o'qish
            ham mumkin bo'lishi kerak.

            <br><br>

            Zone Stamplar
            grafik tartibga
            yordam berishi kerak.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            5 ta xona uchun:

            <br><br>

            • nom;<br>
            • raqam;<br>
            • maydon

            <br><br>

            ko'rsatiladigan
            tartibli Zone Stamp
            ko'rinishini tayyorlang.

            <br><br>

            Keyin Floor Planni
            uzoqroq zoomda ko'rib,
            hammasi o'qilishini tekshiring.
            """,
        },
    ],

    "L06_M10_004": [
        {
            "title": "Zone va funksional tahlil",
            "type": "highlight",
            "text": """
            Zone faqat
            xonani belgilash uchun emas,

            <br><br>

            butun uyning
            funksional strukturasini
            tahlil qilishda ham
            foydali.
            """,
        },
        {
            "title": "Public zona",
            "type": "normal",
            "text": """
            Public zonaga
            masalan:

            <br><br>

            • Living Room;<br>
            • Dining;<br>
            • Guest Area

            <br><br>

            kabi umumiy foydalanish
            makonlari kirishi mumkin.
            """,
        },
        {
            "title": "Private zona",
            "type": "normal",
            "text": """
            Private zonaga
            masalan:

            <br><br>

            • Bedrooms;<br>
            • Master Bedroom;<br>
            • Family private spaces

            <br><br>

            kirishi mumkin.
            """,
        },
        {
            "title": "Service zona",
            "type": "normal",
            "text": """
            Service zonaga:

            <br><br>

            • laundry;<br>
            • storage;<br>
            • technical room;<br>
            • ayrim yordamchi xonalar

            <br><br>

            kiritilishi mumkin.
            """,
        },
        {
            "title": "Oldingi bilimlar bilan bog'lang",
            "type": "highlight",
            "text": """
            LEVEL 2 da
            public,
            private
            va service zonalashni
            o'rgangan edik.

            <br><br>

            Endi bu fikrni
            Archicaddagi Zone
            ma'lumotlari bilan
            bog'laymiz.
            """,
        },
        {
            "title": "Maydon balansi",
            "type": "example",
            "text": """
            Tasavvur qiling:

            <br><br>

            umumiy uy maydonining
            juda katta qismi

            <br><br>

            koridor va
            yordamchi harakat zonalariga
            ketib qolgan.

            <br><br>

            Zone ma'lumotlari
            bu muammoni
            tahlil qilishga yordam beradi.
            """,
        },
        {
            "title": "Area Schedule uchun poydevor",
            "type": "normal",
            "text": """
            Tartibli Zone ma'lumotlari
            keyinchalik xona ro'yxatlari

            <br><br>

            va Schedule workflowlari
            uchun ham foydali bo'ladi.

            <br><br>

            Bu mavzuni
            yuqori levelda
            chuqurlashtiramiz.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Kichik turar joydagi
            barcha xonalarni

            <br><br>

            3 guruhga ajrating:

            <br><br>

            1. Public<br>
            2. Private<br>
            3. Service

            <br><br>

            Keyin qaysi guruh
            uy maydonining
            katta qismini egallayotganini
            tahlil qiling.
            """,
        },
    ],

    "L06_M10_005": [
        {
            "title": "Zones professional audit",
            "type": "highlight",
            "text": """
            Endi Zones tizimini
            faqat xona nomlari
            sifatida emas,

            <br><br>

            loyiha ma'lumotlari
            va funksional tahlil
            tizimi sifatida
            tekshiramiz.
            """,
        },
        {
            "title": "1. Barcha xonalarda Zone bormi?",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • asosiy xonalar Zone bilan belgilanganmi?<br>
            • biror xona unutib qoldirilmaganmi?<br>
            • keraksiz Zone mavjud emasmi?
            """,
        },
        {
            "title": "2. Naming",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • xona nomlari tushunarlimi?<br>
            • naming bir xil tizimdami?<br>
            • Room 1, New Zone kabi nomlar qolmaganmi?
            """,
        },
        {
            "title": "3. Chegaralar",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • Zone xona chegarasiga mosmi?<br>
            • qo'shni xonaga o'tib ketmaganmi?<br>
            • bo'shliq yoki ochiq joy noto'g'ri qo'shilmaganmi?
            """,
        },
        {
            "title": "4. Maydon",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • maydon natijasi mantiqiymi?<br>
            • devor o'zgarishidan keyin Zone tekshirildimi?<br>
            • noodatiy katta yoki kichik natija yo'qmi?
            """,
        },
        {
            "title": "5. Zone Stamp",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • xona nomi o'qiladimi?<br>
            • maydon ko'rinadimi?<br>
            • stamp boshqa grafikani yopmayaptimi?<br>
            • plan tartibli ko'rinadimi?
            """,
        },
        {
            "title": "6. Funksional tahlil",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • public zona mantiqiymi?<br>
            • private zona himoyalanganmi?<br>
            • service zona to'g'ri joylashganmi?<br>
            • circulation haddan tashqari katta emasmi?
            """,
        },
        {
            "title": "Xatoni toping",
            "type": "warning",
            "text": """
            Uy plani tayyor.

            <br><br>

            Lekin:

            <br><br>

            • bir bedroomda Zone yo'q;<br>
            • oshxona Zone'i hallway ichiga o'tib ketgan;<br>
            • ikki xona bir xil raqamda;<br>
            • bir Stamp devor ustida;<br>
            • devor o'zgarganidan keyin Zone tekshirilmagan.

            <br><br>

            Muammo:

            <br><br>

            plan chizilgan,
            lekin xona ma'lumotlari
            professional audit
            qilinmagan.
            """,
        },
        {
            "title": "Professional checklist",
            "type": "example",
            "text": """
            Zones tizimini tekshiring:

            <br><br>

            <b>1.</b> Barcha kerakli xonalarda Zone bormi?<br><br>
            <b>2.</b> Xona nomlari izchilmi?<br><br>
            <b>3.</b> Xona raqamlari tartiblimi?<br><br>
            <b>4.</b> Zone chegaralari to'g'rimi?<br><br>
            <b>5.</b> Maydonlar mantiqiymi?<br><br>
            <b>6.</b> Zone Stamplar o'qiladimi?<br><br>
            <b>7.</b> Funksional zonalash bilan mosmi?
            """,
        },
        {
            "title": "LEVEL 6 yakuni",
            "type": "highlight",
            "text": """
            Siz LEVEL 6 davomida:

            <br><br>

            ✓ Stories;<br>
            ✓ Layers;<br>
            ✓ Building Materials;<br>
            ✓ Composite Structures;<br>
            ✓ Complex Profiles;<br>
            ✓ Roof Tool;<br>
            ✓ Stair Tool;<br>
            ✓ Railing;<br>
            ✓ Mesh;<br>
            ✓ Zones

            <br><br>

            bilan ishlash
            mantig'ini o'rgandingiz.

            <br><br>

            Endi Archicad modelini
            faqat element chizish
            darajasida emas,

            <br><br>

            strukturali BIM loyiha
            sifatida boshqarishga
            yaqinlashdingiz.

            <br><br>

            Keyingi bosqich:
            <b>LEVEL 6 yakuniy imtihoni.</b>
            """,
        },
    ],
}


# ============================================================
# QUIZ
# Q136-Q150
# ============================================================

LEVEL06_MODULE10_QUIZ = {
    "L06_M10_001": [
        {
            "code": "L06_Q136",
            "question": "Zone Archicadda xona yoki funksional makonni BIM ma'lumot sifatida boshqarishga yordam beradimi?",
            "explanation": (
                "Zone xona nomi, maydoni va boshqa ma'lumotlarni bitta BIM elementi orqali boshqarishga yordam beradi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L06_Q137",
            "question": "Zone oddiy Text elementi bilan aynan bir xilmi?",
            "explanation": (
                "Zone faqat yozuv emas; u xona haqida BIM ma'lumotlarini ham saqlashi mumkin."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L06_Q138",
            "question": "Zone orqali xona nomi va maydoni kabi ma'lumotlarni boshqarish mumkinmi?",
            "explanation": (
                "Zone xona haqida turli parametrlarni saqlash va ko'rsatishda ishlatiladi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L06_M10_002": [
        {
            "code": "L06_Q139",
            "question": "Zone maydoni xona chegarasi bilan bog'liqmi?",
            "explanation": (
                "Zone maydonining to'g'ri chiqishi uchun xona yoki Zone chegarasi to'g'ri aniqlanishi kerak."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L06_Q140",
            "question": "Xona devori o'zgarsa Zone natijasini qayta tekshirish kerakmi?",
            "explanation": (
                "Geometriya o'zgarishi xona chegarasi va maydoniga ta'sir qilishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L06_Q141",
            "question": "Zone maydoni chiqsa xona avtomatik ravishda barcha normativ talablarga javob beradimi?",
            "explanation": (
                "Zone maydonni hisoblashga yordam beradi, normativ muvofiqlik esa alohida tekshiriladi."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
    ],

    "L06_M10_003": [
        {
            "code": "L06_Q142",
            "question": "Zone Stamp xona ma'lumotlarini Floor Planda ko'rsatishga xizmat qiladimi?",
            "explanation": (
                "Zone Stamp xona nomi, raqami, maydoni va boshqa ma'lumotlarni grafik ko'rsatishda ishlatilishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L06_Q143",
            "question": "Xona naming tizimi loyiha bo'ylab izchil bo'lishi kerakmi?",
            "explanation": (
                "Izchil naming loyiha ma'lumotlarini o'qish va boshqarishni osonlashtiradi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L06_Q144",
            "question": "Zone Stamp boshqa chizma ma'lumotlarini yopib qo'ysa ham joylashuvi muhim emasmi?",
            "explanation": (
                "Zone Stamp o'qilishi va chizma grafik tartibiga mos joylashishi kerak."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
    ],

    "L06_M10_004": [
        {
            "code": "L06_Q145",
            "question": "Zone ma'lumotlari uyning funksional strukturasini tahlil qilishga yordam berishi mumkinmi?",
            "explanation": (
                "Xonalar va ularning maydonlarini tahlil qilish public, private va service zonalar balansini ko'rishga yordam beradi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L06_Q146",
            "question": "Public, private va service zonalash xona funksiyalari bilan bog'liqmi?",
            "explanation": (
                "Funksional zonalash xonalarni ularning foydalanish vazifasi bo'yicha tashkil qiladi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L06_Q147",
            "question": "Zone ma'lumotlari keyinchalik xona ro'yxati va Schedule workflowida ham foydali bo'lishi mumkinmi?",
            "explanation": (
                "Tartibli BIM xona ma'lumotlari keyingi schedule va hujjatlashtirish ishlariga asos bo'lishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L06_M10_005": [
        {
            "code": "L06_Q148",
            "question": "Zones auditida xona nomi, maydoni va chegarasi tekshiriladimi?",
            "explanation": (
                "Zone auditining asosiy qismlariga naming, boundary va maydon nazorati kiradi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L06_Q149",
            "question": "Plan chiroyli ko'rinsa Zone ma'lumotlaridagi xatolarni tekshirmasa ham bo'ladimi?",
            "explanation": (
                "Grafik ko'rinish to'g'ri bo'lsa ham xona BIM ma'lumotlarida xatolar bo'lishi mumkin."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L06_Q150",
            "question": "Zones bilan professional ishlashdagi to'g'ri workflow qaysi?",
            "explanation": (
                "Xonalar aniqlanadi, Zone va ma'lumotlari beriladi, boundary, maydon va stamp natijalari audit qilinadi."
            ),
            "options": [
                (
                    "A",
                    "Xonalar → Zone → naming/numbering → boundary/maydon → Stamp → audit",
                    True,
                ),
                (
                    "B",
                    "Har bir xonaga faqat oddiy Text yozish",
                    False,
                ),
            ],
        },
    ],
}


# ============================================================
# DATABASE SEED
# ============================================================

def seed_level06_module10():
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
        ) in LEVEL06_MODULE10_LESSONS:

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
