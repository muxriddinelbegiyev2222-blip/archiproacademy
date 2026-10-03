from database.database import get_connection


# ============================================================
# LEVEL 7
# MODULE 03 - MODEL VIEW OPTIONS
# ============================================================

LEVEL07_MODULE03_LESSONS = [
    (
        "L07_M03",
        "L07_M03_001",
        "Model View Options tushunchasi",
        "theory",
        "Bitta BIM modelni turli hujjatlashtirish maqsadlari uchun turlicha ko'rsatish mantig'ini tushunish.",
        1,
        30,
        20,
    ),
    (
        "L07_M03",
        "L07_M03_002",
        "Model ko'rinishini boshqarish",
        "theory",
        "Model elementlarining viewdagi grafik va detallashtirish ko'rinishlarini maqsadga mos boshqarish.",
        2,
        35,
        20,
    ),
    (
        "L07_M03",
        "L07_M03_003",
        "MVO Combination",
        "practice",
        "Turli loyiha vazifalari uchun tartibli Model View Options kombinatsiyalarini tashkil qilish.",
        3,
        35,
        20,
    ),
    (
        "L07_M03",
        "L07_M03_004",
        "View va MVO workflow",
        "practice",
        "Plan va boshqa viewlarni maqsadiga mos MVO sozlamalari bilan boshqarish.",
        4,
        40,
        20,
    ),
    (
        "L07_M03",
        "L07_M03_005",
        "Model View Options professional audit",
        "practice",
        "MVO kombinatsiyalari, view maqsadi va grafik natijalarni kompleks tekshirish.",
        5,
        40,
        25,
    ),
]


# ============================================================
# CONTENT
# ============================================================

LEVEL07_MODULE03_CONTENT = {
    "L07_M03_001": [
        {
            "title": "Model View Options nima?",
            "type": "highlight",
            "text": """
            Model View Options
            yoki MVO —

            <br><br>

            BIM modelning ayrim
            elementlari viewda
            qanday ko'rinishini

            <br><br>

            maqsadga qarab
            boshqarishga yordam
            beradigan tizim.
            """,
        },
        {
            "title": "Bitta model",
            "type": "normal",
            "text": """
            Professional BIM workflowda
            har bir chizma uchun
            yangi model yaratilmaydi.

            <br><br>

            Bitta asosiy model
            saqlanadi.

            <br><br>

            Turli viewlarda esa
            kerakli ma'lumot
            turlicha ko'rsatiladi.
            """,
        },
        {
            "title": "Tasavvur qiling",
            "type": "example",
            "text": """
            Sizda bitta uy modeli bor.

            <br><br>

            Lekin:

            • ishchi plan;<br>
            • konseptual plan;<br>
            • presentation plan;<br>
            • boshqa hujjat

            <br><br>

            bir xil darajada
            detallangan bo'lishi
            shart emas.
            """,
        },
        {
            "title": "Modelni buzmasdan",
            "type": "highlight",
            "text": """
            Muhim prinsip:

            <br><br>

            ko'rinishni o'zgartirish
            uchun modelni
            qayta qurish shart emas.

            <br><br>

            View sozlamalari
            modelning qanday
            ifodalanishini boshqaradi.
            """,
        },
        {
            "title": "MVO va model farqi",
            "type": "warning",
            "text": """
            Viewdagi element
            soddaroq ko'rinishi

            <br><br>

            uning BIM modeldan
            o'chirilganini anglatmaydi.

            <br><br>

            Model va uning
            grafik ko'rinishini
            adashtirmang.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Bitta uy planini
            tasavvur qiling.

            <br><br>

            Shu modeldan:

            1. sodda konseptual view;<br>
            2. batafsil ishchi view

            <br><br>

            kerak.

            <br><br>

            Savol:
            buning uchun ikki xil
            uy modeli kerakmi?

            <br><br>

            Yo'q.
            To'g'ri view workflow
            kerak.
            """,
        },
    ],

    "L07_M03_002": [
        {
            "title": "Detallashtirish darajasi",
            "type": "highlight",
            "text": """
            Har bir view
            bir xil miqdordagi
            grafik ma'lumotni
            talab qilmaydi.

            <br><br>

            View maqsadi
            ko'rsatiladigan detal
            darajasiga ta'sir qiladi.
            """,
        },
        {
            "title": "Ko'proq ma'lumot doim yaxshi emas",
            "type": "warning",
            "text": """
            Chizmaga mumkin bo'lgan
            barcha detallarni
            chiqarish

            <br><br>

            uni professional
            qilmaydi.

            <br><br>

            Ortiqcha grafik
            chizmani o'qishni
            qiyinlashtirishi mumkin.
            """,
        },
        {
            "title": "View maqsadini aniqlang",
            "type": "normal",
            "text": """
            Avval savol bering:

            <br><br>

            bu view kim uchun?

            <br><br>

            • loyiha ishlab chiqish uchunmi?<br>
            • tekshiruv uchunmi?<br>
            • ishchi hujjat uchunmi?<br>
            • taqdimot uchunmi?

            <br><br>

            Keyin grafik darajani
            tanlang.
            """,
        },
        {
            "title": "Element ko'rinishi",
            "type": "normal",
            "text": """
            MVO ayrim
            model elementlarining

            <br><br>

            viewdagi ifodalanish
            usulini boshqarishda
            ishtirok etadi.

            <br><br>

            Aniq imkoniyatlar
            element turi va
            Archicad versiyasiga
            qarab farqlanishi mumkin.
            """,
        },
        {
            "title": "Tasavvur qiling",
            "type": "example",
            "text": """
            Presentation plan
            juda toza va
            tushunarli bo'lishi kerak.

            <br><br>

            Ishchi plan esa
            ko'proq texnik
            ma'lumot talab qiladi.

            <br><br>

            Bir xil model
            ikki xil maqsadda
            ikki xil ko'rinishi mumkin.
            """,
        },
        {
            "title": "MVO modelni tuzatmaydi",
            "type": "warning",
            "text": """
            Modeldagi xatoni
            MVO bilan yashirish

            <br><br>

            xatoni tuzatish emas.

            <br><br>

            Noto'g'ri model
            avval modelning o'zida
            tuzatilishi kerak.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Bir xil plan uchun
            ikkita maqsad yozing:

            <br><br>

            A — Presentation<br>
            B — Working Drawing

            <br><br>

            So'ng qaysi viewda
            ko'proq yoki kamroq
            grafik detal kerakligini
            tushuntiring.
            """,
        },
    ],

    "L07_M03_003": [
        {
            "title": "MVO Combination",
            "type": "highlight",
            "text": """
            MVO Combination —
            turli Model View
            sozlamalarini

            <br><br>

            aniq maqsad uchun
            bitta tartibli
            konfiguratsiyada
            saqlash usuli.
            """,
        },
        {
            "title": "Nega Combination kerak?",
            "type": "normal",
            "text": """
            Har safar
            barcha parametrlarni
            qo'lda o'zgartirish

            <br><br>

            sekin va
            xatoga moyil.

            <br><br>

            Combination
            tayyor standart
            sifatida ishlatiladi.
            """,
        },
        {
            "title": "Naming",
            "type": "highlight",
            "text": """
            Combination nomi
            uning maqsadini
            bildirib tursin.

            <br><br>

            Masalan:

            PRESENTATION<br>
            WORKING PLAN<br>
            MODEL CHECK

            <br><br>

            kabi nomlash mumkin.

            <br><br>

            Bu nomlar
            namuna xolos.
            """,
        },
        {
            "title": "Yomon naming",
            "type": "warning",
            "text": """
            MVO 1<br>
            MVO 2<br>
            New MVO<br>
            Final<br>
            Final 2

            <br><br>

            kabi nomlar
            katta loyihada
            tez chalkashadi.
            """,
        },
        {
            "title": "Kamroq, lekin aniq",
            "type": "normal",
            "text": """
            Keraksiz juda ko'p
            MVO Combination

            <br><br>

            yaratish professional
            tizim emas.

            <br><br>

            Har bir kombinatsiyaning
            aniq vazifasi bo'lsin.
            """,
        },
        {
            "title": "Standartlashtirish",
            "type": "highlight",
            "text": """
            Tartibli MVO
            kombinatsiyalari

            <br><br>

            loyiha bo'ylab
            bir xil grafik
            standartni saqlashga
            yordam beradi.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            3 ta MVO
            Combination konsepsiyasi
            yarating:

            <br><br>

            1. PRESENTATION<br>
            2. WORKING DRAWING<br>
            3. MODEL AUDIT

            <br><br>

            Har birining
            maqsadini bitta
            jumlada yozing.
            """,
        },
    ],

    "L07_M03_004": [
        {
            "title": "View + MVO",
            "type": "highlight",
            "text": """
            Professional workflowda
            View faqat

            <br><br>

            kamera yoki
            zoom holati emas.

            <br><br>

            U ma'lum
            loyiha maqsadiga
            xizmat qiladigan
            saqlangan ko'rinishdir.
            """,
        },
        {
            "title": "View maqsadi",
            "type": "normal",
            "text": """
            View yaratishda
            quyidagilarni
            o'ylang:

            <br><br>

            • kim foydalanadi?<br>
            • nima uchun kerak?<br>
            • qanday ma'lumot ko'rinishi kerak?<br>
            • grafik darajasi qanday bo'lishi kerak?
            """,
        },
        {
            "title": "Bir plan — bir nechta View",
            "type": "example",
            "text": """
            Bitta Floor Plan
            asosida:

            <br><br>

            • Floor Plan — Presentation;<br>
            • Floor Plan — Working;<br>
            • Floor Plan — Audit

            <br><br>

            kabi alohida
            Viewlar bo'lishi mumkin.

            <br><br>

            Lekin ularning
            asosiy modeli bir xil.
            """,
        },
        {
            "title": "Qo'lda almashtirish xavfi",
            "type": "warning",
            "text": """
            Har safar chizma
            chiqarishdan oldin

            <br><br>

            MVO'ni qo'lda
            eslab almashtirish

            <br><br>

            noto'g'ri view
            chiqishiga sabab
            bo'lishi mumkin.
            """,
        },
        {
            "title": "View standartlari",
            "type": "highlight",
            "text": """
            Professional loyiha
            workflowida

            <br><br>

            View va uning
            kerakli grafik
            sozlamalari

            <br><br>

            oldindan tartibli
            tashkil qilinadi.
            """,
        },
        {
            "title": "Graphic Overrides bilan farqi",
            "type": "normal",
            "text": """
            Graphic Overrides
            elementlarni criteria
            va qoidalar orqali
            grafik ajratishga
            yordam beradi.

            <br><br>

            Model View Options esa
            model elementlarining
            viewdagi ifodalanish
            darajasini boshqaradi.

            <br><br>

            Ikkalasi birgalikda
            professional View
            workflowining qismlari.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Bitta loyiha uchun
            3 ta View rejalashtiring.

            <br><br>

            Har biriga:

            • View nomi;<br>
            • maqsadi;<br>
            • kerakli MVO Combination

            <br><br>

            yozing.
            """,
        },
    ],

    "L07_M03_005": [
        {
            "title": "MVO professional audit",
            "type": "highlight",
            "text": """
            Endi tizimni

            <br><br>

            Model → MVO → View → Output

            <br><br>

            zanjiri bo'yicha
            tekshiramiz.
            """,
        },
        {
            "title": "1. Combination naming",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • nomi tushunarlimi?<br>
            • maqsadi nomidan bilinadimi?<br>
            • Final2 kabi noma'lum variantlar qolmaganmi?
            """,
        },
        {
            "title": "2. Sozlamalar",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • kerakli elementlar to'g'ri ko'rinyaptimi?<br>
            • keraksiz detal chiqmayaptimi?<br>
            • zarur ma'lumot yashirinib qolmaganmi?
            """,
        },
        {
            "title": "3. View bilan bog'lanish",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • Presentation View uchun mos MVO ishlatilganmi?<br>
            • Working View uchun kerakli detallar bormi?<br>
            • Audit View maqsadiga mosmi?
            """,
        },
        {
            "title": "4. Model yashirilmaganmi?",
            "type": "warning",
            "text": """
            MVO yordamida
            modeldagi real xato

            <br><br>

            ko'zdan yashirinib
            qolmaganini tekshiring.

            <br><br>

            Grafik boshqaruv
            model sifatini
            almashtirmaydi.
            """,
        },
        {
            "title": "5. Izchillik",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • bir xil maqsaddagi Viewlar bir xil standartdami?<br>
            • qo'lda tasodifiy o'zgarishlar yo'qmi?<br>
            • loyiha jamoasi tizimni tushunadimi?
            """,
        },
        {
            "title": "Xatoni toping",
            "type": "warning",
            "text": """
            Loyihada:

            <br><br>

            • MVO 1;<br>
            • MVO Copy;<br>
            • Final MVO;<br>
            • New Final MVO

            <br><br>

            mavjud.

            <br><br>

            Qaysi biri
            working drawing uchun
            ekanini hech kim bilmaydi.

            <br><br>

            Ayrim viewlar
            har safar qo'lda
            o'zgartiriladi.

            <br><br>

            Muammo —
            MVO bor,
            lekin tizim yo'q.
            """,
        },
        {
            "title": "Professional checklist",
            "type": "example",
            "text": """
            MVO tizimini tekshiring:

            <br><br>

            <b>1.</b> Har bir Combination maqsadga egami?<br><br>
            <b>2.</b> Naming izchilmi?<br><br>
            <b>3.</b> Grafik natija tushunarlimi?<br><br>
            <b>4.</b> View bilan to'g'ri ishlayaptimi?<br><br>
            <b>5.</b> Modeldagi xato yashirilmaganmi?<br><br>
            <b>6.</b> Takroriy qo'lda sozlash kamayganmi?
            """,
        },
        {
            "title": "Modul yakuni",
            "type": "highlight",
            "text": """
            Siz endi:

            <br><br>

            ✓ Model View Options mantig'ini tushunasiz;<br>
            ✓ view va model farqini bilasiz;<br>
            ✓ MVO Combination tuzasiz;<br>
            ✓ turli maqsadli Viewlar yaratasiz;<br>
            ✓ grafik standartni boshqarasiz;<br>
            ✓ MVO tizimini professional audit qilasiz.

            <br><br>

            Keyingi modul:
            <b>Renovation.</b>
            """,
        },
    ],
}


# ============================================================
# QUIZ
# Q031-Q045
# ============================================================

LEVEL07_MODULE03_QUIZ = {
    "L07_M03_001": [
        {
            "code": "L07_Q031",
            "question": "Model View Options bitta BIM modelni turli maqsadlarda turlicha ko'rsatishga yordam beradimi?",
            "explanation": (
                "MVO model elementlarining viewdagi ifodalanishini maqsadga qarab boshqarishga yordam beradi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L07_Q032",
            "question": "Har bir grafik view uchun alohida BIM model yaratish kerakmi?",
            "explanation": (
                "Professional workflowda odatda bitta asosiy modeldan turli sozlangan viewlar olinadi."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L07_Q033",
            "question": "Viewda element soddaroq ko'rinsa u modeldan o'chirilgan deganimi?",
            "explanation": (
                "Grafik ifoda o'zgarishi model elementining o'zi yo'qolganini anglatmaydi."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
    ],

    "L07_M03_002": [
        {
            "code": "L07_Q034",
            "question": "Har bir view bir xil detallashtirish darajasiga ega bo'lishi shartmi?",
            "explanation": (
                "Viewning maqsadiga qarab kerakli grafik detal va ma'lumot miqdori farq qilishi mumkin."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L07_Q035",
            "question": "Ko'proq grafik ma'lumot har doim chizmani yaxshiroq qiladimi?",
            "explanation": (
                "Ortiqcha grafik ma'lumot chizmani o'qishni qiyinlashtirishi mumkin."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L07_Q036",
            "question": "MVO modeldagi haqiqiy xatoni tuzatish vositasimi?",
            "explanation": (
                "MVO grafik ifodani boshqaradi; modeldagi real xato modelning o'zida tuzatilishi kerak."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
    ],

    "L07_M03_003": [
        {
            "code": "L07_Q037",
            "question": "MVO Combination bir nechta view sozlamalarini maqsadli konfiguratsiyada saqlashga yordam beradimi?",
            "explanation": (
                "Combination tayyor MVO konfiguratsiyasini tartibli qayta ishlatishga yordam beradi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L07_Q038",
            "question": "MVO 1, MVO 2 va Final 2 kabi nomlar professional naming uchun idealmi?",
            "explanation": (
                "Combination nomidan uning maqsadi tushunarli bo'lishi yaxshiroq."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L07_Q039",
            "question": "Har bir kichik farq uchun juda ko'p MVO Combination yaratish boshqaruvni murakkablashtirishi mumkinmi?",
            "explanation": (
                "Faqat aniq vazifaga ega kombinatsiyalarni saqlash tizimni tartibli qiladi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L07_M03_004": [
        {
            "code": "L07_Q040",
            "question": "Bitta Floor Plan asosida turli maqsadli bir nechta View yaratish mumkinmi?",
            "explanation": (
                "Bir model asosida presentation, working va audit kabi turli viewlar tashkil qilinishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L07_Q041",
            "question": "View uchun kerakli MVO'ni har safar qo'lda eslab almashtirish xato xavfini oshirishi mumkinmi?",
            "explanation": (
                "Tartibli saqlangan view sozlamalari takroriy qo'lda o'zgartirishlarni kamaytiradi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L07_Q042",
            "question": "Graphic Overrides va Model View Options bir xil vazifani bajaradigan aynan bir xil tizimmi?",
            "explanation": (
                "Ular turli grafik boshqaruv vazifalariga ega, ammo view workflowida birgalikda ishlatilishi mumkin."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
    ],

    "L07_M03_005": [
        {
            "code": "L07_Q043",
            "question": "MVO auditida Combination naming va View bilan bog'lanish tekshiriladimi?",
            "explanation": (
                "Professional audit kombinatsiyaning maqsadi, nomi, grafik natijasi va tegishli view bilan ishlashini tekshiradi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L07_Q044",
            "question": "MVO yordamida modeldagi xatoni yashirib qo'yish uni tuzatgan hisoblanadimi?",
            "explanation": (
                "Grafik ko'rinish modelning haqiqiy sifat muammosini tuzatmaydi."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L07_Q045",
            "question": "Model View Options bilan professional ishlashdagi to'g'ri workflow qaysi?",
            "explanation": (
                "Avval view maqsadi aniqlanadi, so'ng MVO kombinatsiyasi tuziladi, viewga qo'llanadi va grafik natija audit qilinadi."
            ),
            "options": [
                (
                    "A",
                    "View maqsadi → MVO Combination → View → grafik tekshiruv → audit",
                    True,
                ),
                (
                    "B",
                    "Tasodifiy sozlash → model xatosini yashirish → tekshirmaslik",
                    False,
                ),
            ],
        },
    ],
}


# ============================================================
# DATABASE SEED
# ============================================================

def seed_level07_module03():
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
        ) in LEVEL07_MODULE03_LESSONS:

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
