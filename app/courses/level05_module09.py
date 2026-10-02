from database.database import get_connection


# ============================================================
# LEVEL 5
# MODULE 09 - DIMENSION
# ============================================================

LEVEL05_MODULE09_LESSONS = [
    (
        "L05_M09",
        "L05_M09_001",
        "Dimension Tool asoslari",
        "theory",
        "Archicadda o'lcham qo'yish mantig'i va asosiy dimension elementlarini tushunish.",
        1,
        40,
        20,
    ),
    (
        "L05_M09",
        "L05_M09_002",
        "Tashqi o'lchamlar",
        "practice",
        "Bino tashqi konturi va asosiy gabaritlariga tartibli o'lcham qo'yish.",
        2,
        45,
        20,
    ),
    (
        "L05_M09",
        "L05_M09_003",
        "Ichki o'lchamlar",
        "practice",
        "Xonalar, devorlar, eshik va boshqa elementlarga kerakli ichki o'lchamlarni qo'yish.",
        3,
        45,
        20,
    ),
    (
        "L05_M09",
        "L05_M09_004",
        "Chain dimension va grafik tartib",
        "practice",
        "Ketma-ket o'lchamlar va chizma o'qiluvchanligini boshqarish.",
        4,
        50,
        20,
    ),
    (
        "L05_M09",
        "L05_M09_005",
        "Dimension mini-loyiha",
        "practice",
        "Oddiy turar joy planini professional tarzda o'lchamlash va tekshirish.",
        5,
        60,
        25,
    ),
]


# ============================================================
# CONTENT
# ============================================================

LEVEL05_MODULE09_CONTENT = {
    "L05_M09_001": [
        {
            "title": "Dimension nima uchun kerak?",
            "type": "highlight",
            "text": """
            Arxitektura chizmasi
            faqat shaklni ko'rsatmaydi.

            <br><br>

            U bino elementlarining
            aniq joylashuvi va
            o'lchamlarini ham tushuntirishi kerak.

            <br><br>

            Dimension Tool
            shu maqsadga xizmat qiladi.
            """,
        },
        {
            "title": "O'lcham faqat raqam emas",
            "type": "normal",
            "text": """
            Dimension tarkibida
            bir nechta grafik qism mavjud bo'lishi mumkin:

            <br><br>

            • dimension line;<br>
            • witness line;<br>
            • marker;<br>
            • raqamli qiymat.
            """,
        },
        {
            "title": "Modeldan o'lcham olish",
            "type": "highlight",
            "text": """
            To'g'ri workflowda
            o'lcham model elementlariga
            bog'liq holda qo'yiladi.

            <br><br>

            Maqsad —
            raqamni qo'lda yozib qo'yish emas.
            """,
        },
        {
            "title": "Tasavvur qiling",
            "type": "example",
            "text": """
            Devorga 5000 mm deb
            oddiy Text yozildi.

            <br><br>

            Keyin devor uzunligi o'zgardi.

            <br><br>

            Text esa eski qiymatda qoldi.

            <br><br>

            Shuning uchun real dimension
            bilan oddiy textni aralashtirmang.
            """,
        },
        {
            "title": "Dimensionning vazifasi",
            "type": "normal",
            "text": """
            O'lcham:

            <br><br>

            • qurilishni tushuntirishi;<br>
            • element joylashuvini aniqlashtirishi;<br>
            • plan geometriyasini tekshirishga yordam berishi;<br>
            • chizmani o'qishni osonlashtirishi kerak.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Oddiy to'rtburchak xona yarating.

            <br><br>

            Uning ikki tomoniga
            Dimension Tool bilan
            o'lcham qo'ying.

            <br><br>

            Keyin devor uzunligini o'zgartirib,
            dimension qanday javob berishini kuzating.
            """,
        },
    ],

    "L05_M09_002": [
        {
            "title": "Tashqi dimension",
            "type": "highlight",
            "text": """
            Tashqi o'lchamlar
            bino konturini
            tushunishga yordam beradi.

            <br><br>

            Ular odatda plan tashqarisida
            tartibli joylashtiriladi.
            """,
        },
        {
            "title": "Nimani o'lchaymiz?",
            "type": "normal",
            "text": """
            Tashqi dimensionda
            loyihaga qarab:

            <br><br>

            • bino umumiy gabariti;<br>
            • devor segmentlari;<br>
            • opening joylari;<br>
            • asosiy o'qlar

            <br><br>

            ko'rsatilishi mumkin.
            """,
        },
        {
            "title": "Umumiy gabarit",
            "type": "highlight",
            "text": """
            Foydalanuvchi
            bino umumiy uzunligi va kengligini
            tez tushuna olishi kerak.
            """,
        },
        {
            "title": "Bir o'lcham yetmaydi",
            "type": "example",
            "text": """
            Faqat umumiy 12 000 mm yozilgan.

            <br><br>

            Lekin deraza,
            eshik
            va devor segmentlari
            qayerda ekanini aniqlab bo'lmaydi.

            <br><br>

            Demak chizma maqsadiga qarab
            qo'shimcha dimension chain kerak bo'lishi mumkin.
            """,
        },
        {
            "title": "Dimension line masofasi",
            "type": "normal",
            "text": """
            Tashqi dimension line
            devorga haddan tashqari
            yaqin joylashtirilsa,

            <br><br>

            plan grafikasi bilan
            aralashib ketishi mumkin.

            <br><br>

            Uni o'qish oson bo'ladigan
            masofada joylashtiring.
            """,
        },
        {
            "title": "Ortiqcha o'lcham",
            "type": "warning",
            "text": """
            Har bir kichik segmentga
            alohida-alohida o'lcham qo'yish
            chizmani professional qilmaydi.

            <br><br>

            Faqat kerakli axborotni bering.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Kichik uy planining
            to'rt tomoniga tashqi dimension qo'ying.

            <br><br>

            Tekshiring:

            <br><br>

            • umumiy gabarit ko'rinadimi;<br>
            • dimensionlar bir-birini to'smayaptimi;<br>
            • plan bilan aralashib ketmaganmi.
            """,
        },
    ],

    "L05_M09_003": [
        {
            "title": "Ichki dimension",
            "type": "highlight",
            "text": """
            Ichki dimensionlar
            xona va ichki elementlarning
            joylashuvini tushuntirishga yordam beradi.
            """,
        },
        {
            "title": "Xona o'lchami",
            "type": "normal",
            "text": """
            Xonaning faqat maydoni emas,
            uning real eni va uzunligi ham
            loyiha uchun muhim.

            <br><br>

            Masalan:
            tor va uzun xona bilan
            kvadratga yaqin xona
            bir xil m² bo'lishi mumkin.
            """,
        },
        {
            "title": "Eshik va opening",
            "type": "normal",
            "text": """
            Eshik yoki openingning
            devordagi joylashuvini
            tushuntirish uchun ham
            dimension kerak bo'lishi mumkin.
            """,
        },
        {
            "title": "Mebel bilan to'qnashuv",
            "type": "warning",
            "text": """
            Ichki dimensionlarni
            mebel,
            room name
            va boshqa yozuvlar ustiga
            joylashtirmang.

            <br><br>

            Chizma o'qiluvchan bo'lishi kerak.
            """,
        },
        {
            "title": "Har xonaga hammasini yozish shart emas",
            "type": "highlight",
            "text": """
            Professional chizma —
            eng ko'p dimension qo'yilgan chizma emas.

            <br><br>

            Professional chizma —
            kerakli dimension
            aniq va mantiqiy berilgan chizma.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Bitta bedroomni tanlang.

            <br><br>

            Unda:

            <br><br>

            • xona eni;<br>
            • xona uzunligi;<br>
            • eshik joylashuvi

            <br><br>

            uchun kerakli dimensionlarni qo'ying.

            <br><br>

            Keyin grafikani tozalang.
            """,
        },
    ],

    "L05_M09_004": [
        {
            "title": "Chain Dimension",
            "type": "highlight",
            "text": """
            Bir nechta nuqta orasidagi
            ketma-ket o'lchamlarni
            bitta tizimda ko'rsatish
            chain dimension mantiqiga kiradi.
            """,
        },
        {
            "title": "Nega foydali?",
            "type": "normal",
            "text": """
            Masalan bitta fasad bo'ylab:

            <br><br>

            devor → deraza → devor →
            eshik → devor

            <br><br>

            segmentlarini
            ketma-ket ko'rsatish mumkin.
            """,
        },
        {
            "title": "Dimension qatlamlari",
            "type": "example",
            "text": """
            Tashqi plan atrofida
            bir nechta dimension qatori bo'lishi mumkin.

            <br><br>

            Masalan:

            <br><br>

            1-qator — openinglar;<br>
            2-qator — asosiy segmentlar;<br>
            3-qator — umumiy gabarit.

            <br><br>

            Bu qat'iy universal formula emas.

            <br><br>

            Maqsad —
            axborotni ierarxik va tushunarli berish.
            """,
        },
        {
            "title": "Witness line tartibi",
            "type": "normal",
            "text": """
            Witness linelar
            boshqa dimension,
            matn va grafikalar bilan
            keraksiz kesishib ketmasligi kerak.
            """,
        },
        {
            "title": "Takroriy dimension",
            "type": "warning",
            "text": """
            Bir xil o'lcham
            bir chizmada
            3-4 marta takrorlansa,

            <br><br>

            foydali axborot o'rniga
            grafik shovqin paydo bo'lishi mumkin.
            """,
        },
        {
            "title": "Dimensionni tahrirlash",
            "type": "normal",
            "text": """
            Dimension joylashuvi
            yoki grafik ko'rinishi
            chizmani yaxshilash uchun
            tahrirlanishi mumkin.

            <br><br>

            Lekin raqamni
            shunchaki chiroyli chiqishi uchun
            noto'g'ri qiymatga almashtirmang.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Bitta tashqi devorda:

            <br><br>

            • 2 ta deraza;<br>
            • 1 ta eshik

            <br><br>

            mavjud deb tasavvur qiling.

            <br><br>

            Openinglar uchun
            tartibli chain dimension yarating.

            <br><br>

            Keyin umumiy gabaritni qo'shing.
            """,
        },
    ],

    "L05_M09_005": [
        {
            "title": "Dimension mini-loyiha",
            "type": "highlight",
            "text": """
            Endi oldingi modullarda
            yaratilgan kichik uy planini
            to'liq o'lchamlashni boshlaymiz.

            <br><br>

            Maqsad —
            har bir bo'sh joyga raqam qo'yish emas.

            <br><br>

            Maqsad —
            chizmani boshqa odam
            tushuna oladigan holatga keltirish.
            """,
        },
        {
            "title": "1-bosqich — tashqi gabarit",
            "type": "normal",
            "text": """
            Avval bino umumiy
            uzunligi va kengligini ko'rsating.

            <br><br>

            Dimensionlarni plan tashqarisida
            tartibli joylashtiring.
            """,
        },
        {
            "title": "2-bosqich — openinglar",
            "type": "normal",
            "text": """
            Muhim eshik va derazalarning
            devordagi joylashuvini
            tushuntiradigan dimensionlarni qo'shing.
            """,
        },
        {
            "title": "3-bosqich — ichki xonalar",
            "type": "normal",
            "text": """
            Kerakli xonalarning
            asosiy eni va uzunligini
            ko'rsating.

            <br><br>

            Har bir kichik bo'lakni
            o'lchamlash shart emas.
            """,
        },
        {
            "title": "4-bosqich — grafik audit",
            "type": "normal",
            "text": """
            Tekshiring:

            <br><br>

            • dimension textlar o'qiladimi;<br>
            • line'lar bir-birini kesmayaptimi;<br>
            • xona nomlari yopilmaganmi;<br>
            • eshik swinglari ko'rinadimi;<br>
            • ortiqcha dimension bormi.
            """,
        },
        {
            "title": "5-bosqich — modelni o'zgartirib ko'ring",
            "type": "example",
            "text": """
            Bitta devor uzunligini o'zgartiring.

            <br><br>

            Keyin dimensionlarni tekshiring.

            <br><br>

            Model va chizma
            bir-biriga mos qolganini
            kuzating.
            """,
        },
        {
            "title": "Xatoni toping",
            "type": "warning",
            "text": """
            O'quvchi 4000 mm dimension
            yoniga oddiy Text bilan
            yana “4.0 m” deb yozdi.

            <br><br>

            Keyin devor o'zgardi.

            <br><br>

            Dimension yangilandi,
            oddiy Text esa eskicha qoldi.

            <br><br>

            Natija:
            bitta joyda ikki xil qiymat.

            <br><br>

            Keraksiz qo'lda yozilgan
            dimensionlardan qoching.
            """,
        },
        {
            "title": "Professional checklist",
            "type": "example",
            "text": """
            Dimensionlarni tekshiring:

            <br><br>

            <b>1.</b> Umumiy gabarit bormi?<br><br>
            <b>2.</b> Muhim segmentlar tushunarlimi?<br><br>
            <b>3.</b> Openinglar kerakli joyda o'lchamlanganmi?<br><br>
            <b>4.</b> Ichki dimensionlar ortiqcha emasmi?<br><br>
            <b>5.</b> Dimension textlar o'qiladimi?<br><br>
            <b>6.</b> Takroriy o'lchamlar yo'qmi?<br><br>
            <b>7.</b> Model o'zgarsa dimension to'g'ri qoladimi?
            """,
        },
        {
            "title": "Modul yakuni",
            "type": "highlight",
            "text": """
            Siz endi:

            <br><br>

            ✓ Dimension Toolni tushunasiz;<br>
            ✓ tashqi o'lcham qo'yasiz;<br>
            ✓ ichki o'lchamlarni boshqarasiz;<br>
            ✓ chain dimension bilan ishlaysiz;<br>
            ✓ takroriy dimensionlarni kamaytirasiz;<br>
            ✓ chizma o'qiluvchanligini tekshirasiz.

            <br><br>

            Keyingi modul:
            <b>Birinchi Archicad loyiha.</b>
            """,
        },
    ],
}


# ============================================================
# QUIZ
# ============================================================

LEVEL05_MODULE09_QUIZ = {
    "L05_M09_001": [
        {
            "code": "L05_Q121",
            "question": "Dimension Tool aniq o'lchamlarni ko'rsatish uchun ishlatiladimi?",
            "explanation": (
                "Dimension loyiha geometriyasini raqamli va grafik tarzda tushuntiradi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L05_Q122",
            "question": "O'lchamni oddiy Text bilan yozish real Dimension bilan bir xilmi?",
            "explanation": (
                "Oddiy Text model geometriyasiga bog'lanmagan bo'lishi mumkin."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L05_Q123",
            "question": "Dimension chizmani o'qishni osonlashtirishi kerakmi?",
            "explanation": (
                "O'lchamning vazifasi faqat raqam ko'paytirish emas, geometriyani tushuntirishdir."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L05_M09_002": [
        {
            "code": "L05_Q124",
            "question": "Tashqi dimension bino umumiy gabaritini ko'rsatishda foydalimi?",
            "explanation": (
                "Umumiy uzunlik va kenglik bino o'lchamini tez tushunishga yordam beradi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L05_Q125",
            "question": "Har bir kichik segmentga majburiy o'lcham qo'yish kerakmi?",
            "explanation": (
                "Faqat chizma maqsadi uchun kerakli dimensionlar berilishi kerak."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L05_Q126",
            "question": "Dimension line plan grafikasi bilan aralashib ketmasligi kerakmi?",
            "explanation": (
                "O'lchamlar o'qiladigan va tartibli joylashishi kerak."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L05_M09_003": [
        {
            "code": "L05_Q127",
            "question": "Ichki dimension xona o'lchamlarini tushuntirishga yordam beradimi?",
            "explanation": (
                "Xona eni va uzunligi real rejalashtirishni tushunishda muhim."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L05_Q128",
            "question": "Ichki dimensionlar mebel va yozuvlarni to'sib qo'yishi mumkinmi?",
            "explanation": (
                "Noto'g'ri joylashgan dimension chizma o'qiluvchanligini pasaytiradi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L05_Q129",
            "question": "Eng ko'p dimension qo'yilgan chizma avtomatik professional bo'ladimi?",
            "explanation": (
                "Professional chizma kerakli axborotni aniq va ortiqchasiz beradi."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
    ],

    "L05_M09_004": [
        {
            "code": "L05_Q130",
            "question": "Chain dimension bir nechta segmentni ketma-ket o'lchashga yordam beradimi?",
            "explanation": (
                "Chain dimension bir nechta nuqta orasidagi o'lchamlarni yagona qatorda ko'rsatishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L05_Q131",
            "question": "Bir xil dimensionni ko'p marta takrorlash grafik shovqin yaratishi mumkinmi?",
            "explanation": (
                "Takroriy axborot chizmani ortiqcha yuklashi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L05_Q132",
            "question": "Dimension qiymatini faqat chiroyli ko'rinishi uchun noto'g'ri raqamga almashtirish mumkinmi?",
            "explanation": (
                "Dimension haqiqiy loyiha geometriyasini ko'rsatishi kerak."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
    ],

    "L05_M09_005": [
        {
            "code": "L05_Q133",
            "question": "Plan o'lchamlangandan keyin grafik audit qilish foydalimi?",
            "explanation": (
                "Dimension line, text va boshqa grafikalar o'zaro to'qnashmasligi tekshiriladi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L05_Q134",
            "question": "Model geometriyasi o'zgarganda dimensionlarni qayta tekshirish kerakmi?",
            "explanation": (
                "Loyiha o'zgarishidan keyin hujjatning to'g'riligi nazorat qilinishi kerak."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L05_Q135",
            "question": "Professional dimension workflow qaysi?",
            "explanation": (
                "Avval muhim geometriya aniqlanadi, keyin kerakli o'lchamlar tartibli qo'yilib audit qilinadi."
            ),
            "options": [
                (
                    "A",
                    "Geometriya → kerakli dimension → grafik audit",
                    True,
                ),
                (
                    "B",
                    "Har bir joyga raqam qo'yish → tekshirmaslik",
                    False,
                ),
            ],
        },
    ],
}


# ============================================================
# DATABASE SEED
# ============================================================

def seed_level05_module09():
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
        ) in LEVEL05_MODULE09_LESSONS:

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
