from database.database import get_connection


# ============================================================
# LEVEL 2
# MODULE 08 - MEHMONXONA VA FAMILY ROOM ERGONOMIKASI
# ============================================================

LEVEL02_MODULE08_LESSONS = [
    (
        "L02_M08",
        "L02_M08_001",
        "Mehmonxona ergonomikasi",
        "theory",
        "Divan, TV, suhbat va harakat zonalari asosida qulay mehmonxona yaratish.",
        1,
        35,
        20,
    ),
    (
        "L02_M08",
        "L02_M08_002",
        "Divan va TV joylashuvi",
        "theory",
        "Ko'rish yo'nalishi va sirkulyatsiyani buzmasdan TV zonasini tashkil qilish.",
        2,
        35,
        20,
    ),
    (
        "L02_M08",
        "L02_M08_003",
        "Suhbat zonasi",
        "theory",
        "Odamlar bir-birini ko'ra oladigan va tabiiy muloqot qiladigan o'tirish tizimini yaratish.",
        3,
        40,
        20,
    ),
    (
        "L02_M08",
        "L02_M08_004",
        "Family room va katta zalni zonalash",
        "practice",
        "Bitta katta makonda oilaviy va mehmon funksiyalarini mantiqiy ajratish.",
        4,
        40,
        20,
    ),
    (
        "L02_M08",
        "L02_M08_005",
        "Mehmonxona xatolarini topish",
        "practice",
        "Real planlarda TV, divan va asosiy harakat yo'llaridagi xatolarni aniqlash.",
        5,
        45,
        25,
    ),
]


# ============================================================
# CONTENT
# ============================================================

LEVEL02_MODULE08_CONTENT = {
    "L02_M08_001": [
        {
            "title": "Mehmonxona — faqat katta xona emas",
            "type": "highlight",
            "text": """
            Mehmonxona ko'pincha uy ichidagi
            eng muhim public makonlardan biridir.

            <br><br>

            Bu yerda:

            <br><br>

            • suhbat;<br>
            • dam olish;<br>
            • TV ko'rish;<br>
            • mehmon kutish;<br>
            • oilaviy yig'ilish

            <br><br>

            bir makonda sodir bo'lishi mumkin.
            """,
        },
        {
            "title": "Mebelni devorga yopishtirish shart emas",
            "type": "normal",
            "text": """
            Boshlovchilar ko'pincha barcha mebelni
            xona devorlariga yopishtirib chiqadi.

            <br><br>

            Lekin katta mehmonxonada
            divan makonni zonalash vositasi ham bo'lishi mumkin.
            """,
        },
        {
            "title": "Harakat yo'lini tekshiring",
            "type": "example",
            "text": """
            Tasavvur qiling:

            <br><br>

            hovliga chiqish uchun odam
            har safar divan va TV orasidan o'tadi.

            <br><br>

            Bu dam olish zonasini
            asosiy koridorga aylantiradi.
            """,
        },
        {
            "title": "Mehmonxona markazi",
            "type": "normal",
            "text": """
            Har bir mehmonxonada kompozitsion markaz
            bir xil bo'lishi shart emas.

            <br><br>

            U:

            <br><br>

            • TV;<br>
            • kamin;<br>
            • tashqi manzara;<br>
            • suhbat markazi;<br>
            • hovliga qaragan katta ochilish

            <br><br>

            bo'lishi mumkin.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Bir mehmonxona planini toping.

            <br><br>

            Unda:

            <br><br>

            1. Asosiy markaz qayerda?<br>
            2. Divanlar qayerga qaragan?<br>
            3. Odamlar qayerdan o'tadi?<br>
            4. Yurish dam olish zonasini kesadimi?
            """,
        },
    ],

    "L02_M08_002": [
        {
            "title": "TV devori ham plan elementi",
            "type": "highlight",
            "text": """
            TV qayerga qo'yilishi
            butun mehmonxona mebel sxemasiga
            ta'sir qilishi mumkin.
            """,
        },
        {
            "title": "TV va deraza",
            "type": "warning",
            "text": """
            TV katta derazaga qarama-qarshi bo'lsa,
            kunduzgi yorug'lik ekran ko'rinishiga
            xalaqit berishi mumkin.

            <br><br>

            Bu faqat interyer masalasi emas,
            plan va ochilishlar bilan bog'liq.
            """,
        },
        {
            "title": "TV va sirkulyatsiya",
            "type": "example",
            "text": """
            Divan bilan TV orasidagi yo'ldan
            odamlar doim o'tsa,

            <br><br>

            TV ko'rayotgan odamga
            doim xalaqit beriladi.
            """,
        },
        {
            "title": "Masofa",
            "type": "normal",
            "text": """
            TV bilan o'tirish joyi o'rtasidagi masofa
            ekran o'lchami va foydalanish turiga qarab
            tanlanadi.

            <br><br>

            Muhim prinsip:

            <br><br>

            juda yaqin ham,
            juda uzoq ham bo'lmasligi kerak.
            """,
        },
        {
            "title": "Boshlovchi xatosi",
            "type": "warning",
            "text": """
            Avval xona chiziladi.

            <br><br>

            Keyin “TV qayerga sig'adi?”
            deb qolgan bitta devor tanlanadi.

            <br><br>

            Professional loyihada TV va mebel
            oldindan hisobga olinadi.
            """,
        },
    ],

    "L02_M08_003": [
        {
            "title": "Suhbat zonasi",
            "type": "highlight",
            "text": """
            Mehmonxona faqat televizor ko'rish uchun emas.

            <br><br>

            Odamlar bir-biri bilan gaplashishi uchun
            o'tirish joylari mantiqiy joylashishi kerak.
            """,
        },
        {
            "title": "Bir-birini ko'rish",
            "type": "example",
            "text": """
            6 kishi bir xonada o'tirgan.

            <br><br>

            Lekin barcha divan va kreslolar
            faqat TV tomon burilgan.

            <br><br>

            Odamlar suhbatlashish uchun
            boshini keskin burishi kerak.

            <br><br>

            Bu TV uchun yaxshi,
            lekin suhbat uchun zaif bo'lishi mumkin.
            """,
        },
        {
            "title": "U shaklidagi suhbat",
            "type": "normal",
            "text": """
            Divan va kreslolarni
            bir-biriga qaragan yoki yarim yopiq
            kompozitsiyada joylashtirish

            <br><br>

            tabiiy suhbat muhitini yaratishi mumkin.
            """,
        },
        {
            "title": "Jurnal stoli",
            "type": "normal",
            "text": """
            Jurnal stoli yoki markaziy element
            suhbat zonasini birlashtirishi mumkin.

            <br><br>

            Lekin uning atrofida yurish
            uchun ham joy qolishi kerak.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            5–6 kishilik mehmonxona uchun
            o'tirish sxemasini tasavvur qiling.

            <br><br>

            Shunday joylashtiringki:

            <br><br>

            • TV ko'rish mumkin bo'lsin;<br>
            • odamlar bir-birini ko'rsin;<br>
            • asosiy yurish yo'li zonani kesmasin.
            """,
        },
    ],

    "L02_M08_004": [
        {
            "title": "Family room nima?",
            "type": "highlight",
            "text": """
            Family room — oilaning kundalik
            dam olishi va norasmiy foydalanishi uchun
            mo'ljallangan makon.

            <br><br>

            U formal mehmonxonadan farq qilishi mumkin.
            """,
        },
        {
            "title": "Ikki xil hayot tarzi",
            "type": "example",
            "text": """
            Ba'zi oilalarda:

            <br><br>

            mehmonlar uchun alohida formal zal,

            <br>
            oila uchun esa alohida family room

            <br><br>

            bo'lishi mumkin.

            <br><br>

            Boshqa oilada ikkalasi bitta makonda birlashadi.
            """,
        },
        {
            "title": "Katta zalni zonalash",
            "type": "normal",
            "text": """
            Katta makonni faqat mebel bilan
            bir nechta funksional zonaga ajratish mumkin.

            <br><br>

            Masalan:

            <br><br>

            • TV zona;<br>
            • suhbat zona;<br>
            • o'qish burchagi;<br>
            • hovliga chiqish yo'li.
            """,
        },
        {
            "title": "Mebel bilan chegara",
            "type": "example",
            "text": """
            Divanning orqa qismi
            family room va dining orasidagi
            yumshoq chegara vazifasini bajarishi mumkin.

            <br><br>

            Har doim devor qurish shart emas.
            """,
        },
        {
            "title": "Xato",
            "type": "warning",
            "text": """
            Juda katta zal yaratildi.

            <br><br>

            Lekin ichida aniq funksional zonalar yo'q.

            <br><br>

            Natijada katta maydon
            “bo'sh” va boshqarilmagan ko'rinishi mumkin.
            """,
        },
    ],

    "L02_M08_005": [
        {
            "title": "Mehmonxona xatolarini ovlaymiz",
            "type": "highlight",
            "text": """
            Endi katta zal va family room'ni
            real foydalanish bo'yicha tekshiramiz.
            """,
        },
        {
            "title": "Xato 1 — TV va divan orasidan yuriladi",
            "type": "warning",
            "text": """
            Hovliga yoki boshqa xonaga
            o'tish uchun odamlar doim
            TV va divan orasidan yuradi.

            <br><br>

            Dam olish zonasi sirkulyatsiya yo'liga aylangan.
            """,
        },
        {
            "title": "Xato 2 — barcha mebel devorda",
            "type": "warning",
            "text": """
            50 m² katta zal.

            <br><br>

            Barcha divan va kreslolar
            devor bo'ylab tarqalib ketgan.

            <br><br>

            Markaz bo'sh,
            odamlar esa bir-biridan juda uzoq.
            """,
        },
        {
            "title": "Xato 3 — TV uchun noto'g'ri devor",
            "type": "warning",
            "text": """
            TV eng yaxshi devorga qo'yilgan.

            <br><br>

            Lekin uning qarshisida
            katta deraza mavjud.

            <br><br>

            Yorug'lik va refleksiya
            foydalanishni qiyinlashtirishi mumkin.
            """,
        },
        {
            "title": "Xato 4 — suhbat zonasi ishlamaydi",
            "type": "warning",
            "text": """
            O'tirish joylari juda uzoq
            yoki bir-biriga orqa bilan joylashgan.

            <br><br>

            Mehmonxona katta,
            lekin odamlar suhbatlashishi noqulay.
            """,
        },
        {
            "title": "Xato 5 — katta zalda zona yo'q",
            "type": "warning",
            "text": """
            Bitta juda katta ochiq makon mavjud.

            <br><br>

            Lekin:

            <br><br>

            • qayerda dam olish;<br>
            • qayerda TV ko'rish;<br>
            • qayerdan yurish

            <br><br>

            aniq emas.
            """,
        },
        {
            "title": "Professional tahlil",
            "type": "example",
            "text": """
            Mehmonxona planini ko'rsangiz:

            <br><br>

            <b>1.</b> Asosiy markaz nima?<br><br>
            <b>2.</b> TV qayerda?<br><br>
            <b>3.</b> Odamlar bir-birini ko'ra oladimi?<br><br>
            <b>4.</b> Asosiy yurish yo'li qayerdan o'tadi?<br><br>
            <b>5.</b> Hovliga chiqish dam olish zonasini kesadimi?<br><br>
            <b>6.</b> Katta xona zonalarga ajratilganmi?
            """,
        },
        {
            "title": "Mini-loyiha",
            "type": "example",
            "text": """
            35–60 m² katta living space toping.

            <br><br>

            Uni quyidagicha tahlil qiling:

            <br><br>

            • TV zona;<br>
            • suhbat zona;<br>
            • family foydalanish;<br>
            • mehmon foydalanish;<br>
            • asosiy harakat;<br>
            • hovli bilan aloqa.

            <br><br>

            Kamida 3 ta yaxshi va
            2 ta zaif nuqtani yozing.
            """,
        },
        {
            "title": "Modul yakuni",
            "type": "highlight",
            "text": """
            Siz endi:

            <br><br>

            ✓ mehmonxona ergonomikasi;<br>
            ✓ TV zonasi;<br>
            ✓ suhbat zonasi;<br>
            ✓ family room;<br>
            ✓ katta zalni zonalash;<br>
            ✓ harakat va dam olish zonasi

            <br><br>

            bo'yicha professional tahlil qila olasiz.

            <br><br>

            Keyingi modul:
            <b>Bolalar xonasi va oilaviy makon.</b>
            """,
        },
    ],
}


# ============================================================
# QUIZ
# ============================================================

LEVEL02_MODULE08_QUIZ = {
    "L02_M08_001": [
        {
            "code": "L02_Q106",
            "question": "Mehmonxona faqat divan va TV uchunmi?",
            "explanation": (
                "Mehmonxona suhbat, dam olish, mehmon kutish va boshqa funksiyalarni ham bajarishi mumkin."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L02_Q107",
            "question": "Asosiy yurish yo'li divan va TV orasidan o'tishi muammo bo'lishi mumkinmi?",
            "explanation": (
                "Bu dam olish va TV zonasiga doimiy xalaqit berishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L02_Q108",
            "question": "Mehmonxonaning asosiy markazi faqat TV bo'lishi shartmi?",
            "explanation": (
                "Kamin, manzara yoki suhbat zonasi ham markaz bo'lishi mumkin."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
    ],

    "L02_M08_002": [
        {
            "code": "L02_Q109",
            "question": "TV joylashuvi deraza bilan birga tahlil qilinadimi?",
            "explanation": (
                "Yorug'lik va refleksiya ekran ko'rinishiga ta'sir qilishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L02_Q110",
            "question": "TV zonasini loyiha oxirida qolgan devorga qo'yish har doim to'g'rimi?",
            "explanation": (
                "TV va mebel joylashuvi plan boshidan hisobga olinishi kerak."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L02_Q111",
            "question": "TV va divan orasidagi masofa foydalanishga ta'sir qiladimi?",
            "explanation": (
                "Ko'rish qulayligi uchun masofa ham muhim."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L02_M08_003": [
        {
            "code": "L02_Q112",
            "question": "Suhbat zonasida odamlarning bir-birini ko'rishi muhimmi?",
            "explanation": (
                "Muloqot uchun o'tirish joylarining o'zaro yo'nalishi muhim."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L02_Q113",
            "question": "Barcha o'tirish joylari faqat TVga qarashi suhbat uchun idealmi?",
            "explanation": (
                "Bu TV ko'rish uchun qulay bo'lishi mumkin, lekin suhbatni zaiflashtirishi mumkin."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L02_Q114",
            "question": "Markaziy jurnal stoli suhbat zonasini birlashtirishi mumkinmi?",
            "explanation": (
                "Markaziy element o'tirish kompozitsiyasini yig'ishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L02_M08_004": [
        {
            "code": "L02_Q115",
            "question": "Family room nimaga xizmat qiladi?",
            "explanation": (
                "Oilaning kundalik norasmiy dam olishi va birga vaqt o'tkazishiga."
            ),
            "options": [
                ("A", "Oilaviy kundalik foydalanishga", True),
                ("B", "Faqat texnik jihozlarga", False),
            ],
        },
        {
            "code": "L02_Q116",
            "question": "Katta zalni mebel orqali zonalash mumkinmi?",
            "explanation": (
                "Divan va boshqa mebellar yumshoq funksional chegaralar yaratishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L02_Q117",
            "question": "Juda katta zalda funksional zonalar bo'lmasa makon samarasiz bo'lishi mumkinmi?",
            "explanation": (
                "Katta maydonning vazifalari aniq bo'lmasa u boshqarilmagan ko'rinishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L02_M08_005": [
        {
            "code": "L02_Q118",
            "question": "Barcha mebelni devorga terish katta zalda har doim yaxshi yechimmi?",
            "explanation": (
                "Bu suhbat masofasini kattalashtirib, markazni bo'sh qoldirishi mumkin."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L02_Q119",
            "question": "Hovliga chiqish yo'li TV zonasini kesishi muammo bo'lishi mumkinmi?",
            "explanation": (
                "Doimiy yurish dam olish zonasiga xalaqit berishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L02_Q120",
            "question": "Mehmonxona tahlilida qaysi savol muhim?",
            "explanation": (
                "Asosiy markaz, yurish va o'tirish aloqalarini tekshirish kerak."
            ),
            "options": [
                ("A", "Asosiy yurish yo'li qayerdan o'tadi?", True),
                ("B", "Faqat fasad materiali nima?", False),
            ],
        },
    ],
}


# ============================================================
# DATABASE SEED
# ============================================================

def seed_level02_module08():
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
        ) in LEVEL02_MODULE08_LESSONS:

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
