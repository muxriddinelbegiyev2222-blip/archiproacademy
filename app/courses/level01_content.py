from database.database import get_connection


# ============================================================
# LEVEL 1 - MODULE 01
# ARXITEKTURA KOMPOZITSIYASI
# ============================================================

LEVEL01_LESSONS = [
    (
        "L01_M01",
        "L01_M01_001",
        "Kompozitsiya nima?",
        "theory",
        "Arxitekturadagi elementlarni tartibli va yaxlit tashkil qilish.",
        1,
        25,
        15,
    ),
    (
        "L01_M01",
        "L01_M01_002",
        "Kompozitsion markaz",
        "theory",
        "Ko'z birinchi qaraydigan asosiy elementni tushunish.",
        2,
        25,
        15,
    ),
    (
        "L01_M01",
        "L01_M01_003",
        "Vizual balans",
        "theory",
        "Fasaddagi elementlarning vizual og'irligini muvozanatlash.",
        3,
        30,
        15,
    ),
    (
        "L01_M01",
        "L01_M01_004",
        "Dominanta va aksent",
        "theory",
        "Asosiy va yordamchi elementlar ierarxiyasini yaratish.",
        4,
        30,
        15,
    ),
    (
        "L01_M01",
        "L01_M01_005",
        "Kompozitsiyadagi tipik xatolar",
        "practice",
        "Turar joy fasadlaridagi kompozitsion xatolarni aniqlash.",
        5,
        35,
        20,
    ),
]


# ============================================================
# LESSON CONTENT
# ============================================================

LEVEL01_CONTENT = {
    # ========================================================
    # 1-DARS
    # ========================================================
    "L01_M01_001": [
        {
            "title": "Bugungi maqsad",
            "type": "highlight",
            "text": """
            Bugun <b>kompozitsiya</b> degan muhim tushunchani
            juda sodda qilib tushunamiz.

            <br><br>

            Dars oxirida siz fasadga qarab:

            <br>
            “Elementlar nega tartibli ko'rinyapti?”
            yoki
            “Nega bu fasad chalkash ko'rinyapti?”

            <br><br>

            degan savollarga javob bera boshlaysiz.
            """,
        },
        {
            "title": "Kompozitsiya nima?",
            "type": "normal",
            "text": """
            Kompozitsiya — bu turli elementlarni
            <b>bir butun, tartibli va tushunarli ko'rinishga</b>
            keltirish.

            <br><br>

            Masalan, uy fasadida:

            <br><br>

            • derazalar;<br>
            • eshik;<br>
            • tom;<br>
            • ayvon;<br>
            • balkon;<br>
            • materiallar;<br>
            • ranglar

            <br><br>

            mavjud.

            <br><br>

            Ularning har birini alohida chiroyli qilish yetmaydi.

            <br><br>

            <b>Ular birgalikda yaxshi ishlashi kerak.</b>
            """,
        },
        {
            "title": "Oddiy hayotiy misol",
            "type": "example",
            "text": """
            Stol ustiga telefon, daftar, kalit, stakan va
            boshqa buyumlarni tartibsiz tashlab qo'ying.

            <br><br>

            Keyin ularni tartibli joylashtiring.

            <br><br>

            Buyumlar o'sha-o'sha.

            <br>
            Lekin umumiy taassurot butunlay o'zgaradi.

            <br><br>

            Arxitekturadagi kompozitsiya ham shunga o'xshaydi.
            """,
        },
        {
            "title": "Uy fasadidagi misol",
            "type": "example",
            "text": """
            Tasavvur qiling:

            <br><br>

            Fasadning chap tomonida katta deraza,
            o'ng tomonida uchta kichik deraza,
            o'rtada kirish,
            tepada esa katta tom elementi bor.

            <br><br>

            Agar ular orasida tartib bo'lmasa,
            ko'z qayerga qarashni bilmay qoladi.

            <br><br>

            Natijada fasad <b>chalkash</b> tuyuladi.
            """,
        },
        {
            "title": "Boshlovchi xatosi",
            "type": "warning",
            "text": """
            Boshlovchilar ko'pincha:

            <br><br>

            “Bu yer bo'sh ekan, yana dekor qo'yamiz.”

            <br><br>

            deb o'ylaydi.

            <br><br>

            Lekin har bir bo'sh joyni to'ldirish shart emas.

            <br><br>

            Ba'zan <b>bo'sh joyning o'zi kompozitsiyaning
            muhim qismi</b>.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Internetdan bir uy fasadini tanlang.

            <br><br>

            Undagi elementlarni sanang:

            <br><br>

            1. Kirish<br>
            2. Derazalar<br>
            3. Tom<br>
            4. Materiallar<br>
            5. Dekor

            <br><br>

            Keyin savol bering:

            <br><br>

            <b>“Bular bir-biriga mos ishlayaptimi?”</b>
            """,
        },
        {
            "title": "Eslab qoling",
            "type": "highlight",
            "text": """
            <b>
            Kompozitsiya — elementlarning soni emas,
            ular orasidagi tartibdir.
            </b>
            """,
        },
    ],

    # ========================================================
    # 2-DARS
    # ========================================================
    "L01_M01_002": [
        {
            "title": "Kompozitsion markaz nima?",
            "type": "highlight",
            "text": """
            Fasadga birinchi marta qaraganingizda
            ko'zingiz birinchi bo'lib qayerga tushadi?

            <br><br>

            Ko'pincha shu joy
            <b>kompozitsion markaz</b> vazifasini bajaradi.
            """,
        },
        {
            "title": "Nega markaz kerak?",
            "type": "normal",
            "text": """
            Agar fasaddagi barcha elementlar bir xil kuchli bo'lsa,
            ko'z uchun tartib yo'qolishi mumkin.

            <br><br>

            Kompozitsion markaz:

            <br><br>

            • asosiy joyni belgilaydi;<br>
            • ko'zni boshqaradi;<br>
            • fasadga ierarxiya beradi;<br>
            • muhim elementni ajratadi.
            """,
        },
        {
            "title": "Kirish qismi misoli",
            "type": "example",
            "text": """
            Turar joy fasadida asosiy kirish ko'pincha
            kompozitsion markaz bo'lishi mumkin.

            <br><br>

            Uni ajratish uchun:

            <br><br>

            • soyabon;<br>
            • boshqa material;<br>
            • chuqurlik;<br>
            • balandroq portal;<br>
            • yoritish

            <br><br>

            ishlatilishi mumkin.
            """,
        },
        {
            "title": "Lekin markaz doim o'rtadami?",
            "type": "normal",
            "text": """
            Yo'q.

            <br><br>

            Kompozitsion markaz geometrik markaz bilan
            bir xil tushuncha emas.

            <br><br>

            Fasad asimmetrik bo'lishi mumkin,
            lekin baribir aniq kompozitsion markazga ega bo'ladi.
            """,
        },
        {
            "title": "Xato",
            "type": "warning",
            "text": """
            Bir fasadda bir vaqtning o'zida:

            <br><br>

            • juda katta portal;<br>
            • juda katta balkon;<br>
            • juda yorqin material;<br>
            • juda katta tom elementi

            <br><br>

            bir-biri bilan raqobat qilsa,
            asosiy markaz yo'qoladi.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Bir fasadga 3 soniya qarang.

            <br><br>

            Keyin ko'zingizni yuming.

            <br><br>

            Birinchi esingizda qolgan element nima?

            <br><br>

            Nega aynan o'sha element e'tiboringizni tortdi?
            """,
        },
    ],

    # ========================================================
    # 3-DARS
    # ========================================================
    "L01_M01_003": [
        {
            "title": "Vizual balans nima?",
            "type": "highlight",
            "text": """
            Vizual balans — fasadning bir tomoni
            haddan tashqari “og'ir”, ikkinchi tomoni esa
            haddan tashqari “bo'sh” ko'rinmasligi.
            """,
        },
        {
            "title": "Vizual og'irlik",
            "type": "normal",
            "text": """
            Elementning real kilogrammi haqida gapirmayapmiz.

            <br><br>

            Ko'z uchun ayrim elementlar kuchliroq ko'rinadi.

            <br><br>

            Masalan:

            <br><br>

            • katta qora hajm;<br>
            • katta deraza;<br>
            • kuchli tekstura;<br>
            • katta balkon;<br>
            • yorqin rang

            <br><br>

            vizual jihatdan og'irroq ko'rinishi mumkin.
            """,
        },
        {
            "title": "Oddiy misol",
            "type": "example",
            "text": """
            Fasadning chap tomonida ulkan qoramtir hajm bor.

            <br><br>

            O'ng tomonda esa kichik oq devor va bitta
            kichkina deraza.

            <br><br>

            Ko'zga chap tomon juda og'ir tuyulishi mumkin.

            <br><br>

            Arxitektor balansni boshqa elementlar orqali
            tiklashga harakat qiladi.
            """,
        },
        {
            "title": "Balans = simmetriya emas",
            "type": "highlight",
            "text": """
            <b>
            Balansli fasad albatta simmetrik bo'lishi shart emas.
            </b>

            <br><br>

            Asimmetrik fasad ham juda muvozanatli bo'lishi mumkin.
            """,
        },
        {
            "title": "Boshlovchi xatosi",
            "type": "warning",
            "text": """
            “Ikki tomonni aynan bir xil qilsam,
            fasad professional bo'ladi.”

            <br><br>

            Bu doim to'g'ri emas.

            <br><br>

            Simmetriya — vosita.

            <br>
            Balans esa umumiy natija.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Fasad rasmini xayolan o'rtadan ikkiga bo'ling.

            <br><br>

            Chap tomon va o'ng tomonning
            vizual og'irligini solishtiring.

            <br><br>

            Qaysi tomon kuchliroq?

            <br>
            Nima sababdan?
            """,
        },
    ],

    # ========================================================
    # 4-DARS
    # ========================================================
    "L01_M01_004": [
        {
            "title": "Dominanta nima?",
            "type": "highlight",
            "text": """
            Dominanta — kompozitsiyadagi boshqa elementlardan
            kuchliroq seziladigan asosiy element.
            """,
        },
        {
            "title": "Aksent nima?",
            "type": "normal",
            "text": """
            Aksent — ma'lum nuqtaga e'tibor qaratish uchun
            ishlatiladigan element.

            <br><br>

            Masalan:

            <br><br>

            • boshqa rang;<br>
            • boshqa material;<br>
            • yoritish;<br>
            • chuqurlik;<br>
            • vertikal element

            <br><br>

            orqali aksent yaratish mumkin.
            """,
        },
        {
            "title": "Uy misoli",
            "type": "example",
            "text": """
            Oq rangli sodda fasadni tasavvur qiling.

            <br><br>

            Kirish qismi yog'och teksturali katta portal bilan
            ajratilgan.

            <br><br>

            Ko'z darhol kirish qismiga boradi.

            <br><br>

            Bu yerda yog'och portal
            <b>aksent</b> vazifasini bajarishi mumkin.
            """,
        },
        {
            "title": "Hammasi aksent bo'lsa nima bo'ladi?",
            "type": "warning",
            "text": """
            Qizil eshik.

            <br>
            Qora balkon.

            <br>
            Oltin dekor.

            <br>
            Tosh devor.

            <br>
            Yog'och tom.

            <br>
            Ko'k yoritish.

            <br><br>

            Agar hamma element “menga qara” desa,
            hech biri haqiqiy aksent bo'lib qolmaydi.
            """,
        },
        {
            "title": "Muhim qoida",
            "type": "highlight",
            "text": """
            <b>
            Kuchli kompozitsiyada elementlar orasida
            ierarxiya bo'lishi kerak.
            </b>

            <br><br>

            Asosiy element bor.

            <br>
            Yordamchi elementlar bor.

            <br>
            Fon vazifasini bajaradigan elementlar bor.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Bir uy fasadini tanlang.

            <br><br>

            Unda:

            <br><br>

            1. Dominantani toping.<br>
            2. Bitta aksentni toping.<br>
            3. Fon vazifasidagi elementni toping.
            """,
        },
    ],

    # ========================================================
    # 5-DARS
    # ========================================================
    "L01_M01_005": [
        {
            "title": "Endi xatolarni topamiz",
            "type": "highlight",
            "text": """
            Bu darsda yangi termin yodlashdan ko'ra,
            oldingi 4 darsni amalda ishlatamiz.
            """,
        },
        {
            "title": "Xato 1 — hamma narsa kuchli",
            "type": "warning",
            "text": """
            Agar fasadning har bir qismi alohida e'tibor talab qilsa,
            ko'z charchaydi.

            <br><br>

            Kuchli fasad ko'pincha:
            <b>asosiy + yordamchi + fon</b>
            ierarxiyasiga ega.
            """,
        },
        {
            "title": "Xato 2 — balans yo'q",
            "type": "warning",
            "text": """
            Fasadning bir tomonida:

            <br>
            katta balkon + qora material + katta deraza,

            <br><br>

            ikkinchi tomonida esa juda kichik elementlar bo'lsa,
            fasad bir tomonga “og'ib” ko'rinishi mumkin.
            """,
        },
        {
            "title": "Xato 3 — kirish topilmaydi",
            "type": "warning",
            "text": """
            Mehmon uy oldiga keldi.

            <br><br>

            Lekin asosiy eshik qayerdaligini darhol tushunmadi.

            <br><br>

            Bu kompozitsion ierarxiya yetarli emasligining
            belgisi bo'lishi mumkin.
            """,
        },
        {
            "title": "Xato 4 — dekor bilan muammoni yashirish",
            "type": "warning",
            "text": """
            Asosiy proporsiya va kompozitsiya noto'g'ri bo'lsa,
            ustiga ko'proq dekor qo'shish muammoni hal qilmaydi.

            <br><br>

            Avval umumiy hajm va tartibni tuzatish kerak.
            """,
        },
        {
            "title": "Professional tahlil formulasi",
            "type": "example",
            "text": """
            Fasadda muammo ko'rsangiz, shunday fikrlang:

            <br><br>

            <b>1.</b> Ko'zim birinchi qayerga tushdi?<br><br>
            <b>2.</b> Asosiy markaz tushunarlimi?<br><br>
            <b>3.</b> Chap va o'ng tomon balanslimi?<br><br>
            <b>4.</b> Aksentlar juda ko'p emasmi?<br><br>
            <b>5.</b> Keraksiz dekor bormi?
            """,
        },
        {
            "title": "Mini-loyiha",
            "type": "example",
            "text": """
            Internetdan sizga yoqmaydigan bitta uy fasadini tanlang.

            <br><br>

            “Xunuk” deb yozish mumkin emas.

            <br><br>

            Kamida 3 ta professional sabab yozing.

            <br><br>

            Masalan:

            <br>
            “Kompozitsion markaz noaniq.”

            <br>
            “Chap tomon vizual og'ir.”

            <br>
            “Aksentlar haddan tashqari ko'p.”
            """,
        },
        {
            "title": "Modul xulosasi",
            "type": "highlight",
            "text": """
            Endi siz:

            <br><br>

            ✓ kompozitsiya;<br>
            ✓ kompozitsion markaz;<br>
            ✓ vizual balans;<br>
            ✓ dominanta;<br>
            ✓ aksent

            <br><br>

            tushunchalarini bilasiz.

            <br><br>

            Keyingi modulda
            <b>proporsiya va masshtab</b>ni chuqur o'rganamiz.
            """,
        },
    ],
}


# ============================================================
# QUIZZES
# ============================================================

LEVEL01_QUIZ = {
    "L01_M01_001": [
        {
            "code": "L01_Q001",
            "question": "Arxitekturada kompozitsiya nimani anglatadi?",
            "explanation": (
                "Kompozitsiya elementlarni yaxlit va tartibli tizimga birlashtiradi."
            ),
            "options": [
                ("A", "Faqat rang tanlash", False),
                ("B", "Elementlarni yaxlit va tartibli tashkil qilish", True),
                ("C", "Faqat dekor qo'shish", False),
                ("D", "Faqat simmetriya", False),
            ],
        },
        {
            "code": "L01_Q002",
            "question": "Har bir bo'sh joyni dekor bilan to'ldirish kerakmi?",
            "explanation": (
                "Bo'sh joy ham kompozitsiyaning muhim qismi bo'lishi mumkin."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L01_Q003",
            "question": "Kompozitsiyada eng muhim narsa qaysi?",
            "explanation": (
                "Elementlar sonidan ko'ra ularning o'zaro tartibi muhim."
            ),
            "options": [
                ("A", "Elementlar soni", False),
                ("B", "Elementlar orasidagi tartib", True),
                ("C", "Ko'proq material", False),
            ],
        },
    ],

    "L01_M01_002": [
        {
            "code": "L01_Q004",
            "question": "Kompozitsion markaz nima?",
            "explanation": (
                "Bu ko'z e'tiborini birinchi yoki kuchli tortadigan asosiy element."
            ),
            "options": [
                ("A", "Asosiy e'tibor nuqtasi", True),
                ("B", "Faqat geometrik o'rta", False),
                ("C", "Faqat tom", False),
            ],
        },
        {
            "code": "L01_Q005",
            "question": "Kompozitsion markaz doim fasad o'rtasida bo'lishi shartmi?",
            "explanation": (
                "Asimmetrik fasadda ham markaz boshqa joyda bo'lishi mumkin."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L01_Q006",
            "question": "Asosiy kirish kompozitsion markaz bo'lishi mumkinmi?",
            "explanation": (
                "Turar joylarda kirish qismi ko'pincha asosiy e'tibor nuqtasiga aylantiriladi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L01_M01_003": [
        {
            "code": "L01_Q007",
            "question": "Vizual balans nimani anglatadi?",
            "explanation": (
                "Fasad elementlarining ko'zga muvozanatli ko'rinishini anglatadi."
            ),
            "options": [
                ("A", "Vizual muvozanat", True),
                ("B", "Faqat bir xil rang", False),
                ("C", "Faqat bir xil deraza", False),
            ],
        },
        {
            "code": "L01_Q008",
            "question": "Balansli fasad doim simmetrik bo'lishi kerakmi?",
            "explanation": (
                "Asimmetrik kompozitsiya ham balansli bo'lishi mumkin."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L01_Q009",
            "question": "Katta qora hajm vizual jihatdan kuchli ko'rinishi mumkinmi?",
            "explanation": (
                "Rang, o'lcham va tekstura elementning vizual og'irligiga ta'sir qiladi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L01_M01_004": [
        {
            "code": "L01_Q010",
            "question": "Dominanta nima?",
            "explanation": (
                "Dominanta kompozitsiyadagi eng kuchli asosiy elementdir."
            ),
            "options": [
                ("A", "Asosiy kuchli element", True),
                ("B", "Har qanday kichik detal", False),
            ],
        },
        {
            "code": "L01_Q011",
            "question": "Aksentning vazifasi nima?",
            "explanation": (
                "Aksent ma'lum nuqtaga e'tibor qaratadi."
            ),
            "options": [
                ("A", "E'tibor qaratish", True),
                ("B", "Barcha elementni yashirish", False),
            ],
        },
        {
            "code": "L01_Q012",
            "question": "Fasaddagi barcha elementlar aksent bo'lishi kerakmi?",
            "explanation": (
                "Hamma element kuchli bo'lsa, ierarxiya yo'qoladi."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
    ],

    "L01_M01_005": [
        {
            "code": "L01_Q013",
            "question": "Kirishni darhol topib bo'lmasligi nimadan dalolat berishi mumkin?",
            "explanation": (
                "Kompozitsion ierarxiya va markaz noaniq bo'lishi mumkin."
            ),
            "options": [
                ("A", "Kompozitsiya noaniqligidan", True),
                ("B", "Uy juda yaxshi ekanidan", False),
            ],
        },
        {
            "code": "L01_Q014",
            "question": "Kompozitsiya muammosini faqat dekor ko'paytirib hal qilish mumkinmi?",
            "explanation": (
                "Avval hajm, proporsiya va umumiy tartibni tuzatish kerak."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L01_Q015",
            "question": "Professional fasad tahlilida qaysi savol foydali?",
            "explanation": (
                "Ko'z qayerga tushishi, balans va aksentlar professional tahlilning bir qismi."
            ),
            "options": [
                ("A", "Ko'zim birinchi qayerga tushdi?", True),
                ("B", "Necha kilogramm?", False),
                ("C", "Faqat narxi qancha?", False),
            ],
        },
    ],
}


# ============================================================
# DATABASE SEED
# ============================================================

def seed_level01_lessons():
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
        ) in LEVEL01_LESSONS:

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
                INSERT OR IGNORE INTO lessons (
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


def get_level01_content(
    lesson_code: str,
):
    return LEVEL01_CONTENT.get(
        lesson_code,
        [],
    )
