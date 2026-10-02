from database.database import get_connection


# ============================================================
# LEVEL 5
# MODULE 03 - WALL TOOL
# ============================================================

LEVEL05_MODULE03_LESSONS = [
    (
        "L05_M03",
        "L05_M03_001",
        "Wall Tool asoslari",
        "theory",
        "Archicadda devor yaratish mantig'i va asosiy parametrlarni tushunish.",
        1,
        40,
        20,
    ),
    (
        "L05_M03",
        "L05_M03_002",
        "Reference Line",
        "theory",
        "Devorning reference line tomonini tushunish va nazorat qilish.",
        2,
        40,
        20,
    ),
    (
        "L05_M03",
        "L05_M03_003",
        "Devor geometriyasi",
        "practice",
        "To'g'ri, ketma-ket va egri devorlarni yaratish.",
        3,
        45,
        20,
    ),
    (
        "L05_M03",
        "L05_M03_004",
        "Devorlarni ulash va tahrirlash",
        "practice",
        "Devorlarning kesishishi, ulanishi va asosiy tahrirlash usullarini o'rganish.",
        4,
        50,
        20,
    ),
    (
        "L05_M03",
        "L05_M03_005",
        "Wall Tool mini-loyiha",
        "practice",
        "Oddiy uy konturini Wall Tool yordamida to'g'ri yaratish va tekshirish.",
        5,
        60,
        25,
    ),
]


# ============================================================
# CONTENT
# ============================================================

LEVEL05_MODULE03_CONTENT = {
    "L05_M03_001": [
        {
            "title": "Wall Tool — modelning asosiy instrumentlaridan biri",
            "type": "highlight",
            "text": """
            Turar joy loyihasida
            devorlar modelning asosiy
            elementlaridan biri hisoblanadi.

            <br><br>

            Archicadda devor
            oddiy 2D chiziq emas.

            <br><br>

            U balandlikka,
            qalinlikka
            va boshqa BIM xususiyatlariga ega element.
            """,
        },
        {
            "title": "Wall Toolni toping",
            "type": "normal",
            "text": """
            ToolBox ichidan
            <b>Wall Tool</b>ni tanlang.

            <br><br>

            Tool faol bo'lgach
            Info Boxdagi parametrlar
            devor bilan bog'liq holatga o'tadi.
            """,
        },
        {
            "title": "Devor yaratishdan oldin",
            "type": "highlight",
            "text": """
            Professional odat:

            <br><br>

            <b>
            TOOL → SETTINGS → CHIZISH
            </b>

            <br><br>

            Avval parametrlarni tekshiring,
            keyin devor yarating.
            """,
        },
        {
            "title": "Asosiy parametrlar",
            "type": "normal",
            "text": """
            Boshlang'ich bosqichda
            quyidagilarni tushunish muhim:

            <br><br>

            • devor balandligi;<br>
            • devor qalinligi;<br>
            • reference line;<br>
            • geometry method;<br>
            • qaysi qavatda yaratilayotgani.
            """,
        },
        {
            "title": "Tasavvur qiling",
            "type": "example",
            "text": """
            Siz 10 metrli devor chizdingiz.

            <br><br>

            Plan to'g'ri ko'rinadi.

            <br><br>

            Lekin 3Dga o'tganda
            devor balandligi noto'g'ri.

            <br><br>

            Demak muammo chizishda emas,
            parametrda.
            """,
        },
        {
            "title": "2D va 3Dni birga tekshiring",
            "type": "normal",
            "text": """
            Wall Tool bilan ishlaganda
            faqat Floor Planga qaramang.

            <br><br>

            Vaqti-vaqti bilan
            3Dda ham tekshiring.

            <br><br>

            Bu noto'g'ri balandlik,
            noto'g'ri ulanish
            va boshqa xatolarni tezroq ko'rsatadi.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            1. Wall Toolni tanlang.<br><br>
            2. Info Boxni kuzating.<br><br>
            3. Bitta devor yarating.<br><br>
            4. Uni 3Dda ko'ring.<br><br>
            5. Devorning parametrlarini toping.
            """,
        },
    ],

    "L05_M03_002": [
        {
            "title": "Reference Line nima?",
            "type": "highlight",
            "text": """
            Devorning reference line'i —
            uni joylashtirish va bog'lashda
            ishlatiladigan asosiy nazorat chizig'i.

            <br><br>

            Boshlovchi uchun
            bu tushuncha juda muhim.
            """,
        },
        {
            "title": "Nega muhim?",
            "type": "normal",
            "text": """
            Bir xil qalinlikdagi devorni
            bir xil nuqtalar orasida chizishingiz mumkin.

            <br><br>

            Lekin reference line tomoni o'zgarsa,
            devor qalinligi boshqa tomonga
            rivojlanishi mumkin.
            """,
        },
        {
            "title": "Oddiy misol",
            "type": "example",
            "text": """
            Siz tashqi kontur bo'ylab
            devor chizyapsiz.

            <br><br>

            Reference line tashqi tomonda bo'lsa,
            devor qalinligi ichkariga qarab
            joylashishi mumkin.

            <br><br>

            Reference line teskari tomonda bo'lsa,
            umumiy kontur siljib ketishi mumkin.
            """,
        },
        {
            "title": "Reference Line va o'lcham",
            "type": "highlight",
            "text": """
            Devorni aniq joylashtirishda
            qaysi nuqta bo'yicha
            o'lcham olayotganingizni bilish kerak.

            <br><br>

            Aks holda plan
            bir necha santimetr yoki undan ko'proq
            siljishi mumkin.
            """,
        },
        {
            "title": "Bir xil tizim ishlating",
            "type": "normal",
            "text": """
            Bir bino konturida
            reference line'larni
            mantiqan bir xil prinsipda ishlatish
            ishni tartibli qiladi.

            <br><br>

            Tasodifiy almashtirish
            xatolarni ko'paytiradi.
            """,
        },
        {
            "title": "Xatoni toping",
            "type": "warning",
            "text": """
            To'rtburchak uy chizildi.

            <br><br>

            Uchta devorda reference line
            bir xil tomonda.

            <br><br>

            To'rtinchi devorda esa
            teskari tomonda.

            <br><br>

            Natijada burchak va kontur
            kutilganidek chiqmayapti.

            <br><br>

            Muammo:
            reference line nazorat qilinmagan.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Bitta devor yarating.

            <br><br>

            So'ng uning reference line tomonini
            o'zgartirib kuzating.

            <br><br>

            Devorning qaysi tomonga
            siljishini tushuning.
            """,
        },
    ],

    "L05_M03_003": [
        {
            "title": "Devor faqat bitta to'g'ri chiziq emas",
            "type": "highlight",
            "text": """
            Wall Tool yordamida
            turli geometriyadagi
            devorlar yaratilishi mumkin.

            <br><br>

            Hozir uchta asosiy holatni o'rganamiz.
            """,
        },
        {
            "title": "Straight Wall",
            "type": "normal",
            "text": """
            Eng oddiy usul —
            boshlanish va tugash nuqtasi
            orasida to'g'ri devor yaratish.

            <br><br>

            Turar joy planlarida
            eng ko'p ishlatiladigan holatlardan biri.
            """,
        },
        {
            "title": "Ketma-ket devor",
            "type": "normal",
            "text": """
            Bir nechta devorni
            ketma-ket yaratishda

            <br><br>

            har bir segmentni
            alohida qayta boshlash shart bo'lmasligi mumkin.

            <br><br>

            Bu uy konturini
            tezroq yaratishga yordam beradi.
            """,
        },
        {
            "title": "Curved Wall",
            "type": "normal",
            "text": """
            Egri shakldagi arxitektura uchun
            curved wall ishlatilishi mumkin.

            <br><br>

            Lekin boshlovchi
            uni faqat dizayn uchun
            tasodifiy ishlatmasligi kerak.

            <br><br>

            Har bir egri elementning
            arxitektura sababi bo'lishi kerak.
            """,
        },
        {
            "title": "Aniq kiritish",
            "type": "highlight",
            "text": """
            Professional modelda
            devorni ko'z bilan taxminan
            chizish yetarli emas.

            <br><br>

            Masofa,
            yo'nalish
            va geometriyani
            aniq boshqarishga odatlaning.
            """,
        },
        {
            "title": "90° burchakni tekshirish",
            "type": "example",
            "text": """
            To'g'ri to'rtburchak xona chizyapsiz.

            <br><br>

            Ko'z bilan 90°ga o'xshatib
            chizish emas,

            <br><br>

            haqiqatan ortogonal
            geometriya yaratilganini tekshiring.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Uchta mashq bajaring:

            <br><br>

            1. Bitta straight wall.<br><br>
            2. To'rtta devordan to'rtburchak xona.<br><br>
            3. Bitta curved wall.

            <br><br>

            Keyin hammasini 3Dda ko'ring.
            """,
        },
    ],

    "L05_M03_004": [
        {
            "title": "Devorlarni chizish yetarli emas",
            "type": "highlight",
            "text": """
            Professional modelda
            devorlar bir-biri bilan
            mantiqan ulanishi kerak.

            <br><br>

            Burchaklar va kesishmalar
            alohida tekshiriladi.
            """,
        },
        {
            "title": "Burchak ulanishi",
            "type": "normal",
            "text": """
            Ikki devor uchrashganda
            ular orasida keraksiz bo'shliq
            qolmasligi kerak.

            <br><br>

            Plan va 3Dda
            birgalikda tekshiring.
            """,
        },
        {
            "title": "T shaklidagi ulanish",
            "type": "normal",
            "text": """
            Ichki devor
            tashqi devorga kelib ulanadigan joy
            T ko'rinishidagi ulanishga misol.

            <br><br>

            Ulanish nuqtasini
            aniq tutashtirish muhim.
            """,
        },
        {
            "title": "Elementni tahrirlash",
            "type": "normal",
            "text": """
            Mavjud devorni tanlab:

            <br><br>

            • uzunligini;<br>
            • joylashuvini;<br>
            • ayrim parametrlarini;<br>
            • uch nuqtalarini

            <br><br>

            tahrirlash mumkin.
            """,
        },
        {
            "title": "O'chirib qayta chizish har doim shart emas",
            "type": "highlight",
            "text": """
            Boshlovchilar ko'pincha
            kichik xato qilsa ham
            devorni o'chirib qayta chizadi.

            <br><br>

            Professional workflowda
            mavjud elementni to'g'ri
            tahrirlashni o'rganish muhim.
            """,
        },
        {
            "title": "3D tekshiruv",
            "type": "example",
            "text": """
            Planda burchak
            to'g'ridek ko'rinishi mumkin.

            <br><br>

            3Dga o'tib
            yuqori qism,
            balandlik
            va elementlarning uzluksizligini ham
            tekshiring.
            """,
        },
        {
            "title": "Tipik xato",
            "type": "warning",
            "text": """
            Ikki devor ko'z bilan
            bir-biriga yaqin olib kelingan.

            <br><br>

            Lekin aslida ularning
            uch nuqtalari tutashmagan.

            <br><br>

            Natijada modelda
            kichik uzilish qolgan.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            1. To'rtburchak xona yarating.<br><br>
            2. Ichiga bitta partition wall qo'shing.<br><br>
            3. T-connectionni tekshiring.<br><br>
            4. Bir devorni uzaytiring.<br><br>
            5. 3Dda tekshiring.
            """,
        },
    ],

    "L05_M03_005": [
        {
            "title": "Wall Tool mini-loyiha",
            "type": "highlight",
            "text": """
            Endi alohida devor emas,
            kichik bino konturini yaratasiz.

            <br><br>

            Maqsad —
            tez chizish emas.

            <br><br>

            Maqsad —
            to'g'ri workflow.
            """,
        },
        {
            "title": "Vazifa",
            "type": "example",
            "text": """
            Oddiy bir qavatli uy uchun
            boshlang'ich devor sxemasini yarating.

            <br><br>

            Shartli tarkib:

            <br><br>

            • tashqi kontur;<br>
            • living;<br>
            • oshxona;<br>
            • 2 ta yotoqxona;<br>
            • sanuzel;<br>
            • koridor.
            """,
        },
        {
            "title": "1-bosqich — tashqi kontur",
            "type": "normal",
            "text": """
            Avval tashqi devorlarni yarating.

            <br><br>

            Reference line
            bir xil mantiqda ishlatilganini
            tekshiring.
            """,
        },
        {
            "title": "2-bosqich — ichki devorlar",
            "type": "normal",
            "text": """
            Keyin partition devorlarni kiriting.

            <br><br>

            Xonalar o'rtasidagi
            funksional aloqani ham unutmang.
            """,
        },
        {
            "title": "3-bosqich — connection",
            "type": "normal",
            "text": """
            Har bir burchak va
            T-connectionni yaqinlashtirib tekshiring.

            <br><br>

            Bo'shliqlar qolmaganiga
            ishonch hosil qiling.
            """,
        },
        {
            "title": "4-bosqich — 3D",
            "type": "normal",
            "text": """
            Endi 3Dga o'ting.

            <br><br>

            Tekshiring:

            <br><br>

            • barcha devorlar mavjudmi;<br>
            • balandlik bir xilmi;<br>
            • tasodifiy devor yo'qmi;<br>
            • kontur mantiqiymi.
            """,
        },
        {
            "title": "Xatoni toping",
            "type": "warning",
            "text": """
            O'quvchi tashqi devorlarning
            ayrimlarini reference line
            tashqarida,

            <br><br>

            ayrimlarini esa ichkarida
            ishlatib chizdi.

            <br><br>

            Yakunda bino o'lchamlari
            kutilganidan farq qildi.

            <br><br>

            Sabab:
            reference line tizimi nazorat qilinmagan.
            """,
        },
        {
            "title": "Professional checklist",
            "type": "example",
            "text": """
            Wall modelni tekshiring:

            <br><br>

            <b>1.</b> Wall Tool parametrlari to'g'rimi?<br><br>
            <b>2.</b> Reference line nazoratdami?<br><br>
            <b>3.</b> Tashqi kontur yopiqmi?<br><br>
            <b>4.</b> Ichki devorlar tutashganmi?<br><br>
            <b>5.</b> Keraksiz devor yo'qmi?<br><br>
            <b>6.</b> 3Dda balandlik to'g'rimi?<br><br>
            <b>7.</b> Plan arxitektura mantiqiga mosmi?
            """,
        },
        {
            "title": "Modul yakuni",
            "type": "highlight",
            "text": """
            Siz endi:

            <br><br>

            ✓ Wall Toolni ishlata olasiz;<br>
            ✓ asosiy parametrlarni tushunasiz;<br>
            ✓ reference line'ni nazorat qilasiz;<br>
            ✓ turli geometriyadagi devor yaratasiz;<br>
            ✓ devorlarni ulaysiz;<br>
            ✓ modelni 2D va 3Dda tekshirasiz.

            <br><br>

            Keyingi modul:
            <b>Slab Tool.</b>
            """,
        },
    ],
}


# ============================================================
# QUIZ
# ============================================================

LEVEL05_MODULE03_QUIZ = {
    "L05_M03_001": [
        {
            "code": "L05_Q031",
            "question": "Archicaddagi Wall oddiy 2D chiziqdan farq qiladimi?",
            "explanation": (
                "Wall balandlik, qalinlik va boshqa BIM parametrlariga ega model elementi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L05_Q032",
            "question": "Devor chizishdan oldin uning parametrlarini tekshirish foydalimi?",
            "explanation": (
                "Tool va parametrlarni oldindan tekshirish noto'g'ri model yaratish xavfini kamaytiradi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L05_Q033",
            "question": "Wall modelini faqat Floor Planda tekshirish yetarlimi?",
            "explanation": (
                "3D tekshiruv balandlik va ulanish kabi xatolarni ko'rishga yordam beradi."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
    ],

    "L05_M03_002": [
        {
            "code": "L05_Q034",
            "question": "Reference line devor joylashuviga ta'sir qiladimi?",
            "explanation": (
                "Reference line qaysi tomonda ekaniga qarab devor qalinligining joylashishi farq qilishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L05_Q035",
            "question": "Bir bino konturida reference line'ni tasodifiy almashtirib ishlatish xato keltirib chiqarishi mumkinmi?",
            "explanation": (
                "Bir xil mantiqdagi reference line tizimi model aniqligini saqlashga yordam beradi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L05_Q036",
            "question": "Reference line va devor qalinligi bir-biriga bog'liq emasmi?",
            "explanation": (
                "Reference line devor qalinligining qaysi tomonga joylashishini boshqarishda muhim."
            ),
            "options": [
                ("A", "Ha, bog'liq emas", False),
                ("B", "Yo'q, bog'liq", True),
            ],
        },
    ],

    "L05_M03_003": [
        {
            "code": "L05_Q037",
            "question": "Wall Tool bilan to'g'ri va egri devorlar yaratish mumkinmi?",
            "explanation": (
                "Wall Tool turli geometriya usullari bilan ishlash imkonini beradi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L05_Q038",
            "question": "Professional modelda devorni faqat ko'z bilan taxminiy uzunlikda chizish yetarlimi?",
            "explanation": (
                "Aniq masofa va geometriyani nazorat qilish kerak."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L05_Q039",
            "question": "Egri devorni faqat dekor uchun sababsiz ishlatish shartmi?",
            "explanation": (
                "Har bir geometriya qarorining arxitektura va funksional sababi bo'lishi foydali."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
    ],

    "L05_M03_004": [
        {
            "code": "L05_Q040",
            "question": "Ikki devor orasidagi kichik bo'shliq model xatosi bo'lishi mumkinmi?",
            "explanation": (
                "Devor uchlari va ulanish nuqtalari aniq tekshirilishi kerak."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L05_Q041",
            "question": "Ichki devorning tashqi devorga kelib ulanishi T-connectionga misol bo'la oladimi?",
            "explanation": (
                "Bunday ulanish turar joy planlarida ko'p uchraydi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L05_Q042",
            "question": "Har kichik xatoda devorni o'chirib qayta chizish shartmi?",
            "explanation": (
                "Ko'p holatda mavjud elementni tahrirlash professionalroq workflow hisoblanadi."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
    ],

    "L05_M03_005": [
        {
            "code": "L05_Q043",
            "question": "Uy konturini yaratgandan keyin 3Dda tekshirish foydalimi?",
            "explanation": (
                "3D tekshiruv balandlik, kontur va keraksiz elementlarni aniqlashga yordam beradi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L05_Q044",
            "question": "Ichki devorlarning tashqi devorlarga to'g'ri ulanishi muhimmi?",
            "explanation": (
                "Toza connection model sifati va keyingi ishlar uchun muhim."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L05_Q045",
            "question": "Wall Tool bilan ishlashdagi to'g'ri workflow qaysi?",
            "explanation": (
                "Asbobni tanlash, parametrlarni tekshirish, chizish va modelni nazorat qilish kerak."
            ),
            "options": [
                (
                    "A",
                    "Tool → parametr → chizish → 2D/3D tekshiruv",
                    True,
                ),
                (
                    "B",
                    "Tasodifiy chizish → keyin ko'ramiz",
                    False,
                ),
            ],
        },
    ],
}


# ============================================================
# DATABASE SEED
# ============================================================

def seed_level05_module03():
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
        ) in LEVEL05_MODULE03_LESSONS:

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
