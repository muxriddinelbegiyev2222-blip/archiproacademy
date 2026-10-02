from database.database import get_connection


# ============================================================
# LEVEL 6
# MODULE 07 - STAIR TOOL
# ============================================================

LEVEL06_MODULE07_LESSONS = [
    (
        "L06_M07",
        "L06_M07_001",
        "Stair Tool va zinapoya geometriyasi",
        "theory",
        "Archicaddagi Stair Tool va zinapoyaning asosiy geometrik qismlarini tushunish.",
        1,
        60,
        20,
    ),
    (
        "L06_M07",
        "L06_M07_002",
        "Tread, riser, flight va landing",
        "theory",
        "Zinapoya pog'onalari, marshlar va maydonchalar o'rtasidagi funksional aloqani tushunish.",
        2,
        65,
        20,
    ),
    (
        "L06_M07",
        "L06_M07_003",
        "Qavatlararo bog'lanish",
        "practice",
        "Zinapoyani Stories va qavat balandliklari bilan mantiqiy bog'lash.",
        3,
        70,
        20,
    ),
    (
        "L06_M07",
        "L06_M07_004",
        "Murakkab Stair geometriyasi",
        "practice",
        "Burilishlar, landinglar va turli zinapoya sxemalarini modelda boshqarish.",
        4,
        80,
        20,
    ),
    (
        "L06_M07",
        "L06_M07_005",
        "Stair professional audit",
        "practice",
        "Zinapoyani geometriya, harakat, qavat aloqasi, 3D va Section bo'yicha kompleks tekshirish.",
        5,
        85,
        25,
    ),
]


# ============================================================
# CONTENT
# ============================================================

LEVEL06_MODULE07_CONTENT = {
    "L06_M07_001": [
        {
            "title": "Stair Tool nima?",
            "type": "highlight",
            "text": """
            Stair Tool —
            Archicadda qavatlar orasidagi
            vertikal harakat elementini
            BIM model sifatida yaratish
            uchun ishlatiladi.

            <br><br>

            Zinapoya faqat
            pog'onalar to'plami emas.

            <br><br>

            U:

            <br><br>

            • qavatlarni bog'laydi;<br>
            • circulation yaratadi;<br>
            • plan va sectionga ta'sir qiladi;<br>
            • ichki makon hajmini shakllantiradi.
            """,
        },
        {
            "title": "Zinapoya — vertikal circulation",
            "type": "highlight",
            "text": """
            Oldingi darslarda
            gorizontal circulationni
            o'rgandik.

            <br><br>

            Zinapoya esa
            odamni bir qavatdan
            boshqa qavatga olib o'tadigan
            vertikal circulation elementi.
            """,
        },
        {
            "title": "Asosiy qismlar",
            "type": "normal",
            "text": """
            Zinapoya tarkibida
            quyidagi tushunchalar uchraydi:

            <br><br>

            • tread;<br>
            • riser;<br>
            • flight;<br>
            • landing;<br>
            • boshlanish nuqtasi;<br>
            • tugash nuqtasi.
            """,
        },
        {
            "title": "Avval makonni tushuning",
            "type": "warning",
            "text": """
            Stair Toolni ochib
            darhol zinapoya chizishdan oldin

            <br><br>

            uning qayerdan
            boshlanishi va
            qayerga chiqishini
            tushunish kerak.
            """,
        },
        {
            "title": "Tasavvur qiling",
            "type": "example",
            "text": """
            2 qavatli uyda
            zinapoya chiroyli.

            <br><br>

            Lekin 1-qavatda
            living circulationini kesadi,

            <br><br>

            2-qavatda esa
            noqulay burchakka chiqadi.

            <br><br>

            Geometriya ishlagan,
            lekin arxitektura ishlamagan.
            """,
        },
        {
            "title": "Stair Toolning vazifasi",
            "type": "normal",
            "text": """
            Stair Tool
            geometriyani yaratishga
            yordam beradi.

            <br><br>

            Lekin zinapoyaning
            qayerda va qanday
            joylashishi haqidagi qarorni

            <br><br>

            arxitektor beradi.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Ikki qavatli uy planini oling.

            <br><br>

            Zinapoya uchun
            3 ta savolga javob bering:

            <br><br>

            1. Qayerdan boshlanadi?<br>
            2. Qayerga chiqadi?<br>
            3. Qaysi circulation yo'lini bog'laydi?

            <br><br>

            Keyin Stair Toolni ishlating.
            """,
        },
    ],

    "L06_M07_002": [
        {
            "title": "Tread nima?",
            "type": "highlight",
            "text": """
            Tread —
            odam oyoq bosadigan
            gorizontal pog'ona qismi.
            """,
        },
        {
            "title": "Riser nima?",
            "type": "normal",
            "text": """
            Riser —
            ketma-ket ikki tread
            orasidagi vertikal
            balandlik qismi.
            """,
        },
        {
            "title": "Tread va riser birga ishlaydi",
            "type": "highlight",
            "text": """
            Zinapoya qulayligi
            faqat treadga
            yoki faqat riserga
            bog'liq emas.

            <br><br>

            Ularning o'zaro
            proporsiyasi va
            umumiy qavat balandligi
            birgalikda ko'riladi.
            """,
        },
        {
            "title": "Flight nima?",
            "type": "normal",
            "text": """
            Flight —
            ketma-ket pog'onalardan
            tashkil topgan
            zinapoya marshi.

            <br><br>

            Bitta zinapoyada
            bir yoki bir nechta
            flight bo'lishi mumkin.
            """,
        },
        {
            "title": "Landing",
            "type": "normal",
            "text": """
            Landing —
            marshlar orasidagi
            yoki qavatga chiqishdagi
            tekis maydon.

            <br><br>

            U yo'nalishni
            o'zgartirish yoki
            harakatni tashkil qilishda
            muhim rol o'ynashi mumkin.
            """,
        },
        {
            "title": "Faqat pog'ona soniga qaramang",
            "type": "warning",
            "text": """
            Zinapoya sig'ishi
            uning qulay ekanini
            anglatmaydi.

            <br><br>

            Tekshirish kerak:

            <br><br>

            • yurish mantig'i;<br>
            • qavatga chiqish nuqtasi;<br>
            • landing;<br>
            • yuqori va pastki circulation.
            """,
        },
        {
            "title": "Normativ o'lchamlar",
            "type": "highlight",
            "text": """
            Tread,
            riser,
            kenglik
            va boshqa aniq qiymatlar

            <br><br>

            loyiha turiga va
            amaldagi normativ talablarga
            bog'liq bo'lishi mumkin.

            <br><br>

            Bu bosqichda
            raqam yodlash emas,
            geometriya mantig'ini
            tushunamiz.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Stair Toolda
            bitta oddiy stair yarating.

            <br><br>

            Keyin alohida aniqlang:

            <br><br>

            • tread;<br>
            • riser;<br>
            • flight;<br>
            • landing.

            <br><br>

            Har birining
            vazifasini tushuntiring.
            """,
        },
    ],

    "L06_M07_003": [
        {
            "title": "Stair va Stories",
            "type": "highlight",
            "text": """
            Zinapoya
            qavatlarni bog'lagani uchun

            <br><br>

            Story tizimi bilan
            bevosita aloqada ishlaydi.
            """,
        },
        {
            "title": "Boshlanish va tugash",
            "type": "normal",
            "text": """
            Stair yaratishda
            uning boshlanish sathi

            <br><br>

            va chiqadigan
            yuqori sathi

            <br><br>

            mantiqan to'g'ri
            tashkil qilinishi kerak.
            """,
        },
        {
            "title": "Qavat balandligi o'zgarsa",
            "type": "highlight",
            "text": """
            Loyiha davomida
            Story balandligi
            o'zgarishi mumkin.

            <br><br>

            Bunday holatda
            Stair geometriyasini
            qayta tekshirish kerak.
            """,
        },
        {
            "title": "Tasavvur qiling",
            "type": "example",
            "text": """
            Zinapoya
            First Floorga chiqishi kerak.

            <br><br>

            Lekin yuqori Story
            balandligi o'zgartirildi.

            <br><br>

            Stair eski parametrda
            qolib ketsa,

            <br><br>

            qavat bilan zinapoya
            orasida xato
            paydo bo'lishi mumkin.
            """,
        },
        {
            "title": "Slab opening",
            "type": "normal",
            "text": """
            Zinapoya yuqori qavatga
            chiqishi uchun

            <br><br>

            qavatlararo yopmada
            tegishli ochilish
            kerak bo'lishi mumkin.

            <br><br>

            Stair va slab
            bir-biridan mustaqil
            o'ylamasligi kerak.
            """,
        },
        {
            "title": "Section nazorati",
            "type": "highlight",
            "text": """
            Stair bilan ishlaganda
            Section juda muhim.

            <br><br>

            Unda:

            <br><br>

            • qavat sathlari;<br>
            • marshlar;<br>
            • landing;<br>
            • yuqori chiqish;<br>
            • slab aloqasi

            <br><br>

            ko'rinadi.
            """,
        },
        {
            "title": "3D nazorat",
            "type": "normal",
            "text": """
            3Dda esa
            stairning butun
            fazoviy holatini
            ko'rish mumkin.

            <br><br>

            Plan va Section bilan
            birgalikda ishlating.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Ground Floor va
            First Floor orasiga
            stair yarating.

            <br><br>

            Keyin:

            • Story aloqasini;<br>
            • slab openingni;<br>
            • yuqori chiqish joyini;<br>
            • 3D natijani

            <br><br>

            tekshiring.
            """,
        },
    ],

    "L06_M07_004": [
        {
            "title": "Zinapoya sxemalari",
            "type": "highlight",
            "text": """
            Hamma zinapoya
            bitta to'g'ri marsh
            shaklida bo'lmaydi.

            <br><br>

            Loyihaga qarab
            turli sxemalar
            ishlatilishi mumkin.
            """,
        },
        {
            "title": "Straight Stair",
            "type": "normal",
            "text": """
            Straight Stair —
            harakat yo'nalishi
            deyarli o'zgarmaydigan
            sodda sxema.

            <br><br>

            U tushunarli,
            lekin uzunroq
            joy talab qilishi mumkin.
            """,
        },
        {
            "title": "Turning Stair",
            "type": "normal",
            "text": """
            Buriluvchi stairda
            harakat yo'nalishi
            landing yoki boshqa
            geometriya orqali o'zgaradi.

            <br><br>

            Bu kompaktroq
            yechim berishi mumkin.
            """,
        },
        {
            "title": "Landingni tasodifiy qo'ymang",
            "type": "warning",
            "text": """
            Landing faqat
            Stair Tool yaratgan
            bo'sh joy emas.

            <br><br>

            U real odam harakati
            va yo'nalish o'zgarishiga
            xizmat qilishi kerak.
            """,
        },
        {
            "title": "Plan geometriyasi",
            "type": "highlight",
            "text": """
            Stairning Plan'dagi
            shakli uy rejasiga
            kuchli ta'sir qiladi.

            <br><br>

            Zinapoya:

            • koridorni yopmasin;<br>
            • entrance'ni buzmasin;<br>
            • living circulationini kesmasin;<br>
            • yuqori qavatdagi yo'lni buzmasin.
            """,
        },
        {
            "title": "Bo'shliq bilan ishlash",
            "type": "normal",
            "text": """
            Stair atrofidagi
            bo'sh joy ham
            arxitekturaning bir qismi.

            <br><br>

            U yerda:

            • circulation;<br>
            • void;<br>
            • landing;<br>
            • railing;<br>
            • yoritish

            <br><br>

            kabi elementlar
            birgalikda ishlashi mumkin.
            """,
        },
        {
            "title": "Murakkablik uchun murakkablik kerak emas",
            "type": "warning",
            "text": """
            Murakkab Stair
            avtomatik ravishda
            professional Stair degani emas.

            <br><br>

            Eng sodda ishlaydigan
            geometriya ko'pincha
            yaxshi boshlanish nuqtasi.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Bir xil qavat balandligi uchun
            2 ta variant yarating:

            <br><br>

            1. Straight Stair;<br>
            2. Turning Stair.

            <br><br>

            Qaysi variant:

            • kamroq maydon oladi;<br>
            • yaxshiroq circulation beradi;<br>
            • qavatga qulayroq chiqadi

            <br><br>

            tahlil qiling.
            """,
        },
    ],

    "L06_M07_005": [
        {
            "title": "Stair professional audit",
            "type": "highlight",
            "text": """
            Endi zinapoyani
            faqat Stair Tool natijasi sifatida emas,

            <br><br>

            ikki qavatni bog'lovchi
            arxitektura va circulation
            tizimi sifatida tekshiramiz.
            """,
        },
        {
            "title": "1. Boshlanish",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • stair qayerdan boshlanadi?<br>
            • pastki circulation bilan mosmi?<br>
            • kirish yo'li to'silmaganmi?
            """,
        },
        {
            "title": "2. Yuqori chiqish",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • stair qayerga chiqadi?<br>
            • yuqori hallway bilan aloqa to'g'rimi?<br>
            • eshik yoki boshqa element bilan konflikt yo'qmi?
            """,
        },
        {
            "title": "3. Geometriya",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • flightlar mantiqiymi?<br>
            • landinglar to'g'ri joydami?<br>
            • direction tushunarlimi?<br>
            • geometriya ortiqcha murakkab emasmi?
            """,
        },
        {
            "title": "4. Story va slab",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • qavat balandliklari to'g'rimi?<br>
            • stair yuqori Storyga to'g'ri chiqadimi?<br>
            • slab opening mosmi?
            """,
        },
        {
            "title": "5. Plan, Section va 3D",
            "type": "highlight",
            "text": """
            Stairni kamida:

            <br><br>

            • Plan;<br>
            • Section;<br>
            • 3D

            <br><br>

            ko'rinishlarida tekshiring.

            <br><br>

            Bitta view
            barcha xatolarni ko'rsatmaydi.
            """,
        },
        {
            "title": "6. Normativ tekshiruv",
            "type": "normal",
            "text": """
            Tread,
            riser,
            stair width,
            landing,
            headroom
            va boshqa aniq parametrlar

            <br><br>

            loyiha turiga mos
            amaldagi normativlar
            asosida tekshirilishi kerak.

            <br><br>

            Bu modulda
            geometriya va workflow
            mantig'ini o'rgandik.
            """,
        },
        {
            "title": "Xatoni toping",
            "type": "warning",
            "text": """
            Zinapoya 3Dda
            chiroyli ko'rinadi.

            <br><br>

            Lekin:

            <br><br>

            • Ground Floorda entrance yo'lini kesadi;<br>
            • landing eshik oldiga tushgan;<br>
            • yuqorida corridor markaziga noqulay chiqadi;<br>
            • slab opening stairga mos emas.

            <br><br>

            Muammo:

            <br><br>

            Stair geometriyasi yaratilgan,
            lekin qavatlararo circulation
            professional o'ylanmagan.
            """,
        },
        {
            "title": "Professional checklist",
            "type": "example",
            "text": """
            Stairni tekshiring:

            <br><br>

            <b>1.</b> Boshlanish joyi mantiqiymi?<br><br>
            <b>2.</b> Yuqori chiqish mantiqiymi?<br><br>
            <b>3.</b> Flight va landinglar to'g'rimi?<br><br>
            <b>4.</b> Story aloqasi to'g'rimi?<br><br>
            <b>5.</b> Slab opening mosmi?<br><br>
            <b>6.</b> Plan, Section va 3D tekshirildimi?<br><br>
            <b>7.</b> Aniq o'lchamlar amaldagi normativlar bo'yicha tekshiriladimi?
            """,
        },
        {
            "title": "Modul yakuni",
            "type": "highlight",
            "text": """
            Siz endi:

            <br><br>

            ✓ Stair Tool mantig'ini tushunasiz;<br>
            ✓ tread va riserni farqlaysiz;<br>
            ✓ flight va landingni tushunasiz;<br>
            ✓ Stairni Stories bilan bog'laysiz;<br>
            ✓ slab openingni tekshirasiz;<br>
            ✓ murakkab stair geometriyasini tahlil qilasiz;<br>
            ✓ Stair auditini bajarasiz.

            <br><br>

            Keyingi modul:
            <b>Railing.</b>
            """,
        },
    ],
}


# ============================================================
# QUIZ
# Q091-Q105
# ============================================================

LEVEL06_MODULE07_QUIZ = {
    "L06_M07_001": [
        {
            "code": "L06_Q091",
            "question": "Stair qavatlar orasidagi vertikal circulation elementi hisoblanadimi?",
            "explanation": (
                "Zinapoya odamlarni turli qavatlar orasida bog'laydigan vertikal harakat elementidir."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L06_Q092",
            "question": "Stair Toolning o'zi zinapoyaning uy ichidagi eng yaxshi joyini avtomatik tanlaydimi?",
            "explanation": (
                "Tool geometriya yaratishga yordam beradi, lekin joylashuv va circulation qarorini loyihachi beradi."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L06_Q093",
            "question": "Zinapoyani loyihalashda pastki va yuqori circulationni birgalikda ko'rish kerakmi?",
            "explanation": (
                "Stair ikki qavatdagi harakat tizimini bog'lagani uchun ikkala tomonni ham tahlil qilish kerak."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L06_M07_002": [
        {
            "code": "L06_Q094",
            "question": "Tread odam oyoq bosadigan gorizontal pog'ona qismimi?",
            "explanation": (
                "Tread zinapoyadagi gorizontal bosish qismidir."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L06_Q095",
            "question": "Flight ketma-ket pog'onalardan tashkil topgan marshni anglatadimi?",
            "explanation": (
                "Flight zinapoyaning ketma-ket pog'onalardan iborat harakat qismidir."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L06_Q096",
            "question": "Zinapoya sig'sa, uning circulation va landinglarini tekshirmasa ham bo'ladimi?",
            "explanation": (
                "Zinapoya geometriyasidan tashqari real yurish va landinglar ham tekshiriladi."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
    ],

    "L06_M07_003": [
        {
            "code": "L06_Q097",
            "question": "Stair qavatlar bilan ishlagani uchun Stories tizimi bilan bog'liqmi?",
            "explanation": (
                "Zinapoya boshlanish va tugash qavatlari bilan vertikal aloqada ishlaydi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L06_Q098",
            "question": "Story balandligi o'zgarsa Stairni qayta tekshirish kerakmi?",
            "explanation": (
                "Qavat balandligi o'zgarishi zinapoya geometriyasiga va yuqori chiqishiga ta'sir qilishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L06_Q099",
            "question": "Stair va slab opening bir-biriga aloqasiz elementlarmi?",
            "explanation": (
                "Qavatlararo zinapoya uchun yopmadagi ochilish bilan Stair geometriyasi o'zaro mos bo'lishi kerak."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
    ],

    "L06_M07_004": [
        {
            "code": "L06_Q100",
            "question": "Zinapoya turli sxema va burilishlarda tashkil qilinishi mumkinmi?",
            "explanation": (
                "Loyiha vazifasiga qarab straight yoki buriluvchi kabi turli stair geometriyalari ishlatilishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L06_Q101",
            "question": "Murakkab Stair har doim sodda Stairdan yaxshiroqmi?",
            "explanation": (
                "Murakkablikning o'zi sifat belgisi emas; geometriya loyiha va circulationga mos bo'lishi kerak."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L06_Q102",
            "question": "Landingning joyi odam harakati bilan bog'liqmi?",
            "explanation": (
                "Landing marshlar va yo'nalish o'zgarishini funksional tashkil qilishga yordam beradi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L06_M07_005": [
        {
            "code": "L06_Q103",
            "question": "Stair auditida pastki va yuqori chiqish joylari tekshiriladimi?",
            "explanation": (
                "Zinapoya ikkala qavat circulationi bilan to'g'ri bog'lanishi kerak."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L06_Q104",
            "question": "Stair 3Dda chiroyli ko'rinsa Plan va Sectionni tekshirmasa ham bo'ladimi?",
            "explanation": (
                "Plan, Section va 3D turli xatolarni ko'rsatadi, shuning uchun birgalikda tekshiriladi."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L06_Q105",
            "question": "Stair Tool bilan professional ishlashdagi to'g'ri workflow qaysi?",
            "explanation": (
                "Avval qavatlar va circulation aniqlanadi, keyin Stair geometriyasi tuziladi va bir nechta viewda tekshiriladi."
            ),
            "options": [
                (
                    "A",
                    "Qavatlar → circulation → Stair geometriyasi → slab opening → Plan/Section/3D audit",
                    True,
                ),
                (
                    "B",
                    "Bo'sh qolgan joyga tasodifiy Stair joylashtirish",
                    False,
                ),
            ],
        },
    ],
}


# ============================================================
# DATABASE SEED
# ============================================================

def seed_level06_module07():
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
        ) in LEVEL06_MODULE07_LESSONS:

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
