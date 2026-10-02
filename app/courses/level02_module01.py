from database.database import get_connection


# ============================================================
# LEVEL 2
# MODULE 01 - INSON MASSHTABI VA ERGONOMIKA
# ============================================================

LEVEL02_MODULE01_LESSONS = [
    (
        "L02_M01",
        "L02_M01_001",
        "Ergonomika nima?",
        "theory",
        "Uy makonini insonning real harakati va qulayligi asosida loyihalash.",
        1,
        30,
        15,
    ),
    (
        "L02_M01",
        "L02_M01_002",
        "Inson tanasi va makon",
        "theory",
        "Inson o'lchami makon hajmiga qanday ta'sir qilishini tushunish.",
        2,
        35,
        15,
    ),
    (
        "L02_M01",
        "L02_M01_003",
        "Mebel va foydalanish zonasi",
        "theory",
        "Mebelning o'zi bilan uning atrofidagi foydalanish maydonini farqlash.",
        3,
        35,
        20,
    ),
    (
        "L02_M01",
        "L02_M01_004",
        "Yurish yo'llari",
        "practice",
        "Uy ichidagi asosiy harakat yo'nalishlarini to'g'ri tashkil qilish.",
        4,
        40,
        20,
    ),
    (
        "L02_M01",
        "L02_M01_005",
        "Ergonomik xatolarni topish",
        "practice",
        "Real uy planidagi noqulay harakat va mebel xatolarini aniqlash.",
        5,
        45,
        25,
    ),
]


# ============================================================
# CONTENT
# ============================================================

LEVEL02_MODULE01_CONTENT = {
    "L02_M01_001": [
        {
            "title": "Ergonomika nima?",
            "type": "highlight",
            "text": """
            Ergonomika — makon, jihoz va elementlarni
            <b>inson uchun qulay ishlaydigan qilib</b>
            tashkil qilish.

            <br><br>

            Arxitekturada bu juda muhim.

            <br><br>

            Chunki chiroyli plan
            foydalanishga noqulay bo'lsa,
            loyiha yaxshi ishlamaydi.
            """,
        },
        {
            "title": "Tasavvur qiling",
            "type": "example",
            "text": """
            Oshxonada muzlatkich juda yaxshi joyda ko'rinadi.

            <br><br>

            Lekin eshigi ochilganda
            odam o'tadigan yo'lni butunlay yopib qo'yadi.

            <br><br>

            Plan chiroyli.

            <br>
            Lekin foydalanish noqulay.

            <br><br>

            Bu ergonomik muammo.
            """,
        },
        {
            "title": "Ergonomika nimani tekshiradi?",
            "type": "normal",
            "text": """
            Masalan:

            <br><br>

            • odam bemalol yura oladimi;<br>
            • eshik bemalol ochiladimi;<br>
            • mebeldan foydalanish mumkinmi;<br>
            • odam o'tirganda boshqa odam o'ta oladimi;<br>
            • shkaf ochilganda yo'l to'silmaydimi;<br>
            • xona faqat qog'ozda emas, hayotda ham ishlaydimi.
            """,
        },
        {
            "title": "Boshlovchi xatosi",
            "type": "warning",
            "text": """
            Xona ichiga mebel belgilarini joylashtirishning o'zi
            ergonomik loyiha degani emas.

            <br><br>

            Mebel atrofida odamning
            <b>foydalanish va harakat zonasi</b>
            ham bo'lishi kerak.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            O'z xonangizga qarang.

            <br><br>

            Bitta mebel tanlang.

            <br><br>

            Masalan, shkaf.

            <br><br>

            Faqat shkaf egallagan joyni emas,
            uning oldida eshikni ochish va turish uchun
            kerak bo'lgan makonni ham kuzating.
            """,
        },
        {
            "title": "Eslab qoling",
            "type": "highlight",
            "text": """
            <b>
            Makon odamga moslashishi kerak.
            Odam makonga majburan moslashmasligi kerak.
            </b>
            """,
        },
    ],

    "L02_M01_002": [
        {
            "title": "Inson — asosiy o'lchov",
            "type": "highlight",
            "text": """
            Uy inson uchun yaratiladi.

            <br><br>

            Shuning uchun arxitektor
            odamning turishi, yurishi, o'tirishi,
            egilishi va foydalanishini tasavvur qilishi kerak.
            """,
        },
        {
            "title": "Plan ichidagi odam",
            "type": "example",
            "text": """
            Plan chizayotganda faqat devorlarni ko'rmang.

            <br><br>

            Xayolan odamni plan ichiga joylashtiring.

            <br><br>

            U:

            <br><br>

            • eshikdan kiradi;<br>
            • kiyimini yechadi;<br>
            • yuradi;<br>
            • o'tiradi;<br>
            • shkaf ochadi;<br>
            • ovqat tayyorlaydi;<br>
            • boshqa xonaga o'tadi.

            <br><br>

            Har bir harakat joy talab qiladi.
            """,
        },
        {
            "title": "Faqat xona maydoni yetmaydi",
            "type": "normal",
            "text": """
            Ikki xona bir xil 16 m² bo'lishi mumkin.

            <br><br>

            Lekin biri qulay,
            ikkinchisi noqulay bo'lishi mumkin.

            <br><br>

            Sababi:

            <br><br>

            • xona proporsiyasi;<br>
            • eshik joyi;<br>
            • deraza joyi;<br>
            • mebel joylashuvi;<br>
            • yurish yo'li.
            """,
        },
        {
            "title": "Xato",
            "type": "warning",
            "text": """
            “Xona 20 kvadrat ekan,
            demak juda qulay.”

            <br><br>

            Bu avtomatik to'g'ri emas.

            <br><br>

            Foydali maydon qanday ishlatilayotgani muhim.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            4 × 4 metr va 2 × 8 metr
            ikkita xonani tasavvur qiling.

            <br><br>

            Ikkalasi ham 16 m².

            <br><br>

            Lekin mebel joylashtirish va foydalanish
            qanchalik farq qilishini o'ylang.
            """,
        },
    ],

    "L02_M01_003": [
        {
            "title": "Mebel egallagan joy yetmaydi",
            "type": "highlight",
            "text": """
            Mebelning o'lchami —
            uning ishlashi uchun kerak bo'lgan
            umumiy makon emas.

            <br><br>

            Mebel atrofida
            <b>foydalanish zonasi</b> ham kerak.
            """,
        },
        {
            "title": "Shkaf misoli",
            "type": "example",
            "text": """
            Shkaf devorga sig'di.

            <br><br>

            Demak masala hal bo'ldimi?

            <br><br>

            Yo'q.

            <br><br>

            Shkaf eshigini ochish,
            uning oldida turish,
            kiyim olish uchun ham makon kerak.
            """,
        },
        {
            "title": "Ovqat stoli",
            "type": "example",
            "text": """
            Stolning o'zi plan ichiga sig'ishi mumkin.

            <br><br>

            Lekin stulni orqaga surib o'tirish uchun
            joy qolmasa, stol amalda ishlamaydi.

            <br><br>

            Shuning uchun faqat stol konturiga qaralmaydi.
            """,
        },
        {
            "title": "Yotoq",
            "type": "normal",
            "text": """
            Krovatni xonaga joylashtirganda:

            <br><br>

            • unga yaqinlashish;<br>
            • yonidan yurish;<br>
            • tumba ishlatish;<br>
            • shkafga o'tish;<br>
            • eshikni ochish

            <br><br>

            kabi vaziyatlar ham tekshiriladi.
            """,
        },
        {
            "title": "Boshlovchi xatosi",
            "type": "warning",
            "text": """
            Plan ichiga iloji boricha ko'p mebel
            joylashtirish yaxshi rejalashtirish emas.

            <br><br>

            Ba'zan kamroq mebel
            ancha qulay makon yaratadi.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Yotoqxona planini oling.

            <br><br>

            Krovat, shkaf va tumbani belgilang.

            <br><br>

            Keyin har birining
            foydalanish zonasini xayolan chizing.

            <br><br>

            Bu zonalar bir-biriga to'qnashyaptimi?
            """,
        },
    ],

    "L02_M01_004": [
        {
            "title": "Uy ichidagi harakat",
            "type": "highlight",
            "text": """
            Odam uy ichida nuqtadan nuqtaga
            doim harakat qiladi.

            <br><br>

            Shu harakat yo'llarini oldindan ko'rish
            yaxshi plan yaratishning asosiy qismlaridan biri.
            """,
        },
        {
            "title": "Tasavvur qiling",
            "type": "example",
            "text": """
            Kirish eshigidan oshxonaga borish uchun
            mehmonxonaning televizor oldidan
            kesib o'tish kerak.

            <br><br>

            Har safar odam televizor qarshisidan o'tadi.

            <br><br>

            Bu harakat yo'nalishi
            yashash zonasiga xalaqit berishi mumkin.
            """,
        },
        {
            "title": "Asosiy va ikkilamchi yo'llar",
            "type": "normal",
            "text": """
            Uyda ayrim yo'llar juda ko'p ishlatiladi.

            <br><br>

            Masalan:

            <br><br>

            kirish → oshxona;<br>
            kirish → mehmonxona;<br>
            yotoqxona → sanuzel;<br>
            oshxona → ovqatlanish zonasi.

            <br><br>

            Bu yo'nalishlarni imkon qadar
            sodda va tushunarli qilish kerak.
            """,
        },
        {
            "title": "Keraksiz aylanish",
            "type": "warning",
            "text": """
            Ikki xona yonma-yon.

            <br><br>

            Lekin biridan ikkinchisiga borish uchun
            uzun koridorni aylanib o'tish kerak.

            <br><br>

            Bu plan funksiyasini qayta tekshirish uchun signal.
            """,
        },
        {
            "title": "Harakat chizig'i",
            "type": "example",
            "text": """
            Plan ustida qalam bilan odam yuradigan
            yo'llarni chizing.

            <br><br>

            Agar chiziqlar:

            <br><br>

            • haddan tashqari ko'p kesishsa;<br>
            • mebel ichidan o'tsa;<br>
            • televizor qarshisidan o'tsa;<br>
            • stol va stullar bilan to'qnashsa

            <br><br>

            planni qayta ko'rib chiqish kerak.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Bitta uy planini tanlang.

            <br><br>

            Uchta yo'nalishni chizing:

            <br><br>

            1. Kirish → oshxona<br>
            2. Kirish → mehmonxona<br>
            3. Yotoqxona → sanuzel

            <br><br>

            Qaysi yo'l eng noqulay?
            Nega?
            """,
        },
    ],

    "L02_M01_005": [
        {
            "title": "Endi plan xatolarini ovlaymiz",
            "type": "highlight",
            "text": """
            Bu darsda xona chiroyli yoki xunukligini emas,
            <b>odam qanday foydalanishini</b>
            tekshiramiz.
            """,
        },
        {
            "title": "Xato 1 — eshik va mebel to'qnashuvi",
            "type": "warning",
            "text": """
            Eshik ochilganda shkafga uriladi.

            <br><br>

            Plan ko'rinishida ikkala element ham sig'gan.

            <br><br>

            Lekin amalda bir-biriga xalaqit beradi.
            """,
        },
        {
            "title": "Xato 2 — stol bor, lekin o'tirib bo'lmaydi",
            "type": "warning",
            "text": """
            Ovqat stoli va stullar joylashtirilgan.

            <br><br>

            Lekin stulni orqaga surish uchun
            yetarli makon yo'q.

            <br><br>

            Bu mebel konturi bilan
            foydalanish zonasini adashtirishdir.
            """,
        },
        {
            "title": "Xato 3 — yurish zonasi krovat ichidan o'tadi",
            "type": "warning",
            "text": """
            Xonaga kirganda shkafga borish uchun
            krovatni aylanib juda tor yo'ldan o'tish kerak.

            <br><br>

            Mebel joylashuvi qayta ko'rib chiqiladi.
            """,
        },
        {
            "title": "Xato 4 — foydasiz katta xona",
            "type": "warning",
            "text": """
            Xona juda katta.

            <br><br>

            Lekin eshik va deraza noto'g'ri joylashgani sababli
            asosiy devorlardan foydalanib bo'lmaydi.

            <br><br>

            Katta kvadrat metr doim
            yaxshi foydali maydon degani emas.
            """,
        },
        {
            "title": "Xato 5 — yo'llar bir-birini kesadi",
            "type": "warning",
            "text": """
            Oshxona, kirish, zinapoya va mehmonxona
            harakat yo'llari bitta nuqtada to'planib qolgan.

            <br><br>

            Uyda doimiy “tirbandlik” zonasi paydo bo'lishi mumkin.
            """,
        },
        {
            "title": "Professional tekshiruv",
            "type": "example",
            "text": """
            Har bir xona uchun:

            <br><br>

            <b>1.</b> Odam qayerdan kiradi?<br><br>
            <b>2.</b> Birinchi qayerga yuradi?<br><br>
            <b>3.</b> Mebelni qanday ishlatadi?<br><br>
            <b>4.</b> Eshiklar bemalol ochiladimi?<br><br>
            <b>5.</b> Harakat va mebel zonalari to'qnashadimi?
            """,
        },
        {
            "title": "Mini-loyiha",
            "type": "example",
            "text": """
            Internetdan kichik uy planini toping.

            <br><br>

            Kamida 5 ta ergonomik nuqtani tekshiring.

            <br><br>

            “Yaxshi/yomon” deb yozmang.

            <br><br>

            Masalan:

            <br>
            “Shkaf eshigi bilan xona eshigi to'qnashishi mumkin.”

            <br>
            “Ovqatlanish zonasidan o'tish yo'li o'tgan.”

            <br>
            “Krovat yonidagi harakat zonasi noqulay.”
            """,
        },
        {
            "title": "Modul yakuni",
            "type": "highlight",
            "text": """
            Siz endi:

            <br><br>

            ✓ ergonomika;<br>
            ✓ inson masshtabi;<br>
            ✓ mebel foydalanish zonasi;<br>
            ✓ yurish yo'llari;<br>
            ✓ ergonomik plan xatolari

            <br><br>

            tushunchalarini amaliy tahlil qila boshlaysiz.

            <br><br>

            Keyingi modulda
            <b>funksional zonalash</b>ga o'tamiz.
            """,
        },
    ],
}


# ============================================================
# QUIZ DATA
# ============================================================

LEVEL02_MODULE01_QUIZ = {
    "L02_M01_001": [
        {
            "code": "L02_Q001",
            "question": "Arxitekturada ergonomika nimaga qaratilgan?",
            "explanation": (
                "Ergonomika makon va elementlarning inson uchun qulay ishlashini o'rganadi."
            ),
            "options": [
                ("A", "Inson uchun qulay foydalanishga", True),
                ("B", "Faqat fasad rangiga", False),
                ("C", "Faqat qurilish narxiga", False),
            ],
        },
        {
            "code": "L02_Q002",
            "question": "Mebel plan ichiga sig'ishi uning qulay ishlashini kafolatlaydimi?",
            "explanation": (
                "Mebel atrofida foydalanish va harakat maydoni ham kerak."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L02_Q003",
            "question": "Eshik ochilganda yo'lni to'sib qo'ysa bu nima bo'lishi mumkin?",
            "explanation": (
                "Bu ergonomik va harakat tashkiloti muammosi bo'lishi mumkin."
            ),
            "options": [
                ("A", "Ergonomik muammo", True),
                ("B", "Har doim yaxshi yechim", False),
            ],
        },
    ],

    "L02_M01_002": [
        {
            "code": "L02_Q004",
            "question": "Bir xil maydondagi ikki xona qulayligi bir xil bo'lishi shartmi?",
            "explanation": (
                "Xona proporsiyasi, eshik, deraza va mebel joylashuvi qulaylikni o'zgartiradi."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L02_Q005",
            "question": "Plan tuzishda odamning harakatini tasavvur qilish kerakmi?",
            "explanation": (
                "Makonning haqiqiy ishlashi inson harakati bilan tekshiriladi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L02_Q006",
            "question": "20 m² xona avtomatik ravishda qulay deganimi?",
            "explanation": (
                "Maydonning o'zi yetmaydi; uning shakli va tashkiloti muhim."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
    ],

    "L02_M01_003": [
        {
            "code": "L02_Q007",
            "question": "Mebel foydalanish zonasi nima?",
            "explanation": (
                "Mebelni ishlatish uchun uning atrofida kerak bo'ladigan qo'shimcha makon."
            ),
            "options": [
                ("A", "Mebel atrofidagi foydalanish maydoni", True),
                ("B", "Faqat mebelning o'z konturi", False),
            ],
        },
        {
            "code": "L02_Q008",
            "question": "Ovqat stolining faqat o'zi xonaga sig'ishi yetarlimi?",
            "explanation": (
                "Stulni surish, o'tirish va yurish uchun ham joy kerak."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L02_Q009",
            "question": "Shkaf oldida foydalanish zonasi kerakmi?",
            "explanation": (
                "Shkafni ochish va undan foydalanish uchun oldida makon kerak."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L02_M01_004": [
        {
            "code": "L02_Q010",
            "question": "Uy ichidagi harakat yo'llarini tekshirish kerakmi?",
            "explanation": (
                "Harakat yo'nalishlari xona va mebel bilan to'qnashmasligi kerak."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L02_Q011",
            "question": "Asosiy yurish yo'li televizor oldidan o'tishi noqulay bo'lishi mumkinmi?",
            "explanation": (
                "Doimiy harakat dam olish zonasiga xalaqit berishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L02_Q012",
            "question": "Keraksiz uzun aylanishlar nimani ko'rsatishi mumkin?",
            "explanation": (
                "Plan funksiyasini va xona aloqalarini qayta ko'rish kerakligini."
            ),
            "options": [
                ("A", "Plan aloqalarida muammo bo'lishi mumkin", True),
                ("B", "Har doim professional yechim", False),
            ],
        },
    ],

    "L02_M01_005": [
        {
            "code": "L02_Q013",
            "question": "Eshik va shkaf bir-biriga urilsa bu qanday xato?",
            "explanation": (
                "Bu elementlarning foydalanish zonasi hisobga olinmagan ergonomik xato."
            ),
            "options": [
                ("A", "Ergonomik xato", True),
                ("B", "Kompozitsion yutuq", False),
            ],
        },
        {
            "code": "L02_Q014",
            "question": "Katta xona har doim katta foydali maydon deganimi?",
            "explanation": (
                "Noto'g'ri eshik, deraza yoki mebel tashkiloti katta maydonni ham samarasiz qilishi mumkin."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L02_Q015",
            "question": "Plan tahlilida qaysi savol foydali?",
            "explanation": (
                "Odamning kirishi, yurishi va mebeldan qanday foydalanishi ergonomik tahlilning asosidir."
            ),
            "options": [
                ("A", "Odam bu xonada qanday harakat qiladi?", True),
                ("B", "Faqat devor rangi qanday?", False),
            ],
        },
    ],
}


# ============================================================
# DATABASE SEED
# ============================================================

def seed_level02_module01():
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
        ) in LEVEL02_MODULE01_LESSONS:

            cursor.execute(
                """
                SELECT id
                FROM course_modules
                WHERE code = ?
                LIMIT 1
                """,
                (
                    module_code,
                ),
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
