from database.database import get_connection


# ============================================================
# LEVEL 1
# MODULE 05 - FORMA VA HAJM
# ============================================================

LEVEL01_MODULE05_LESSONS = [
    (
        "L01_M05",
        "L01_M05_001",
        "Forma va hajm tushunchasi",
        "theory",
        "Arxitekturadagi forma, hajm va uch o'lchamli fikrlash asoslarini tushunish.",
        1,
        35,
        20,
    ),
    (
        "L01_M05",
        "L01_M05_002",
        "Oddiy geometrik hajmlar",
        "theory",
        "Kub, prizma, silindr va boshqa oddiy hajmlarni arxitektura nuqtai nazaridan tahlil qilish.",
        2,
        35,
        20,
    ),
    (
        "L01_M05",
        "L01_M05_003",
        "Hajmlarni birlashtirish",
        "practice",
        "Bir nechta geometrik hajmni yagona arxitektura kompozitsiyasiga birlashtirish.",
        3,
        35,
        20,
    ),
    (
        "L01_M05",
        "L01_M05_004",
        "Bo'shliq, kesish va chiqarish",
        "practice",
        "Hajmni kesish, chiqarish va bo'shliq hosil qilish orqali forma yaratishni tushunish.",
        4,
        35,
        20,
    ),
    (
        "L01_M05",
        "L01_M05_005",
        "3D forma tahlili",
        "practice",
        "Turar joy hajmini proporsiya, kompozitsiya va 3D fikrlash asosida tahlil qilish.",
        5,
        40,
        25,
    ),
]


# ============================================================
# CONTENT
# ============================================================

LEVEL01_MODULE05_CONTENT = {
    "L01_M05_001": [
        {
            "title": "Forma nima?",
            "type": "highlight",
            "text": """
            Forma —
            obyektning tashqi
            geometrik ko'rinishi.

            <br><br>

            Arxitekturada forma
            faqat fasad chizig'i emas.

            <br><br>

            U binoning
            umumiy shaklini
            ifodalaydi.
            """,
        },
        {
            "title": "Hajm nima?",
            "type": "normal",
            "text": """
            Hajm —
            uch o'lchamli makonda
            mavjud bo'lgan shakl.

            <br><br>

            Unda:

            <br><br>

            • uzunlik;<br>
            • kenglik;<br>
            • balandlik

            <br><br>

            mavjud.
            """,
        },
        {
            "title": "Plan yetarli emas",
            "type": "highlight",
            "text": """
            Arxitektor faqat
            Floor Planni ko'rmaydi.

            <br><br>

            Plan chizayotganda ham
            binoning 3D hajmini
            tasavvur qilish kerak.
            """,
        },
        {
            "title": "Tasavvur qiling",
            "type": "example",
            "text": """
            Planda oddiy
            to'rtburchak uy bor.

            <br><br>

            Lekin uning:

            <br><br>

            • balandligi;<br>
            • tom shakli;<br>
            • kirish hajmi;<br>
            • ayvoni;<br>
            • deraza chuqurligi

            <br><br>

            binoning 3D obrazini
            butunlay o'zgartirishi mumkin.
            """,
        },
        {
            "title": "2D → 3D fikrlash",
            "type": "normal",
            "text": """
            Plan ko'rganda
            o'zingizdan so'rang:

            <br><br>

            Bu devor qancha baland?

            <br><br>

            Bu qism oldinga chiqadimi?

            <br><br>

            Bu xona tashqaridan
            qanday hajm beradi?

            <br><br>

            Tom bu forma bilan
            qanday ishlaydi?
            """,
        },
        {
            "title": "Mini-vazifa",
            "type": "example",
            "text": """
            Qog'ozda bitta
            to'rtburchak chizing.

            <br><br>

            Keyin uni:

            <br><br>

            1. past bino;<br>
            2. baland bino;<br>
            3. kub shaklidagi bino

            <br><br>

            sifatida tasavvur qiling.

            <br><br>

            Plan bir xil bo'lsa ham
            hajm qanday o'zgarishini
            tushuntiring.
            """,
        },
    ],

    "L01_M05_002": [
        {
            "title": "Oddiy hajmlardan boshlang",
            "type": "highlight",
            "text": """
            Murakkab arxitektura
            ko'pincha oddiy
            geometrik hajmlardan
            tashkil topadi.

            <br><br>

            Masalan:

            <br><br>

            • kub;<br>
            • to'g'ri to'rtburchak prizma;<br>
            • silindr;<br>
            • uchburchak prizma.
            """,
        },
        {
            "title": "Kub",
            "type": "normal",
            "text": """
            Kub juda aniq
            va barqaror forma beradi.

            <br><br>

            Uning barcha yo'nalishlari
            kuchli geometrik tartib
            yaratadi.
            """,
        },
        {
            "title": "Cho'zilgan prizma",
            "type": "normal",
            "text": """
            To'g'ri to'rtburchak prizma
            bir yo'nalishda cho'zilsa,

            <br><br>

            binoda gorizontal
            yoki vertikal xarakter
            kuchayishi mumkin.
            """,
        },
        {
            "title": "Silindrik forma",
            "type": "normal",
            "text": """
            Yumaloq yoki silindrik hajm
            to'g'ri chiziqli hajmlardan
            boshqacha xarakter beradi.

            <br><br>

            U kompozitsiyada
            aksent sifatida ishlashi mumkin.
            """,
        },
        {
            "title": "Geometriya va funksiya",
            "type": "highlight",
            "text": """
            Forma faqat
            tashqi ko'rinish uchun
            tanlanmaydi.

            <br><br>

            Ichki funksiya ham
            hajm bilan bog'liq.
            """,
        },
        {
            "title": "Tasavvur qiling",
            "type": "example",
            "text": """
            Bir qavatli uyda:

            <br><br>

            living —
            kattaroq hajm;

            <br><br>

            yordamchi xonalar —
            pastroq yoki kichikroq hajm

            <br><br>

            sifatida ifodalangan.

            <br><br>

            Natijada bino
            funksiyasi tashqi hajmda
            ham o'qilishi mumkin.
            """,
        },
        {
            "title": "Mini-vazifa",
            "type": "example",
            "text": """
            3 ta oddiy shakl chizing:

            <br><br>

            • kub;<br>
            • uzun prizma;<br>
            • silindr.

            <br><br>

            Har biridan
            qanday turdagi bino qismi
            yaratish mumkinligini o'ylang.
            """,
        },
    ],

    "L01_M05_003": [
        {
            "title": "Hajmlar birlashadi",
            "type": "highlight",
            "text": """
            Bino har doim
            bitta geometrik blokdan
            iborat bo'lishi shart emas.

            <br><br>

            Bir nechta hajm
            bir kompozitsiyaga
            birlashtirilishi mumkin.
            """,
        },
        {
            "title": "Asosiy va ikkilamchi hajm",
            "type": "normal",
            "text": """
            Kompozitsiyada
            bitta asosiy hajm

            <br><br>

            va unga bo'ysunuvchi
            ikkilamchi hajmlar
            bo'lishi mumkin.
            """,
        },
        {
            "title": "Masalan",
            "type": "example",
            "text": """
            Uyda:

            <br><br>

            asosiy yashash qismi —
            katta hajm;

            <br><br>

            kirish —
            kichik chiqib turgan hajm;

            <br><br>

            ayvon —
            yengil qo'shimcha hajm.

            <br><br>

            Uchala qism birga
            yagona kompozitsiya yaratadi.
            """,
        },
        {
            "title": "Tasodifiy qo'shmang",
            "type": "warning",
            "text": """
            Har bir xona uchun
            tashqariga alohida
            geometrik blok chiqarish

            <br><br>

            fasadni va umumiy
            hajmni tartibsiz qilishi mumkin.
            """,
        },
        {
            "title": "Birlashtiruvchi prinsip",
            "type": "normal",
            "text": """
            Hajmlar orasida
            aloqa bo'lishi kerak.

            <br><br>

            Masalan:

            <br><br>

            • umumiy o'q;<br>
            • proporsiya;<br>
            • balandlik;<br>
            • material;<br>
            • ritm

            <br><br>

            orqali ular birlashtirilishi mumkin.
            """,
        },
        {
            "title": "Dominant hajm",
            "type": "highlight",
            "text": """
            Kompozitsiyada
            hamma hajm
            bir xil kuchli bo'lsa,

            <br><br>

            vizual markaz
            yo'qolishi mumkin.

            <br><br>

            Ba'zan bitta hajm
            dominant sifatida ishlaydi.
            """,
        },
        {
            "title": "Mini-vazifa",
            "type": "example",
            "text": """
            3 ta to'rtburchak hajm
            tasavvur qiling.

            <br><br>

            1 ta katta,
            2 ta kichik.

            <br><br>

            Ularni:

            <br><br>

            • tartibli;<br>
            • balansli;<br>
            • bitta dominant bilan

            <br><br>

            birlashtirishga harakat qiling.
            """,
        },
    ],

    "L01_M05_004": [
        {
            "title": "Forma faqat qo'shish bilan yaratilmaydi",
            "type": "highlight",
            "text": """
            Arxitektura formasini
            yaratishda ikki asosiy
            fikrlash usuli mavjud:

            <br><br>

            <b>qo'shish</b>

            <br><br>

            va

            <br><br>

            <b>ayirish.</b>
            """,
        },
        {
            "title": "Qo'shish",
            "type": "normal",
            "text": """
            Asosiy hajmga
            boshqa hajm qo'shilishi mumkin.

            <br><br>

            Masalan:

            <br><br>

            • kirish bloki;<br>
            • ayvon;<br>
            • erker;<br>
            • qo'shimcha xona hajmi.
            """,
        },
        {
            "title": "Ayirish",
            "type": "normal",
            "text": """
            Asosiy hajmdan
            ma'lum qism olib tashlangandek
            forma hosil qilish mumkin.

            <br><br>

            Masalan:

            <br><br>

            • terassa uchun recess;<br>
            • kirish chuqurligi;<br>
            • balkon;<br>
            • yopiq ayvon.
            """,
        },
        {
            "title": "Bo'shliq ham kompozitsiya",
            "type": "highlight",
            "text": """
            Arxitekturada
            faqat qattiq hajm emas,

            <br><br>

            uning ichidagi
            yoki orasidagi bo'shliq ham
            kompozitsiyaning bir qismi.
            """,
        },
        {
            "title": "Tasavvur qiling",
            "type": "example",
            "text": """
            Oddiy kub shaklidagi
            uy hajmi bor.

            <br><br>

            Kirish qismidan
            kichik bo'lak ichkariga olindi.

            <br><br>

            Natijada:

            <br><br>

            • soyali kirish;<br>
            • chuqurlik;<br>
            • fasadda yangi plastika

            <br><br>

            paydo bo'ldi.
            """,
        },
        {
            "title": "Ortiqcha plastika",
            "type": "warning",
            "text": """
            Ko'p chiqish,
            chuqurlik,
            kesish
            va dekorativ hajmlar

            <br><br>

            avtomatik ravishda
            yaxshi arxitektura yaratmaydi.

            <br><br>

            Har bir qarorning
            sababi bo'lishi kerak.
            """,
        },
        {
            "title": "Mini-vazifa",
            "type": "example",
            "text": """
            Bitta kub oling.

            <br><br>

            1-variant:
            unga kichik hajm qo'shing.

            <br><br>

            2-variant:
            uning bir qismini
            olib tashlang.

            <br><br>

            Qaysi variantda
            qanday arxitektura xarakteri
            paydo bo'lganini tahlil qiling.
            """,
        },
    ],

    "L01_M05_005": [
        {
            "title": "3D forma auditi",
            "type": "highlight",
            "text": """
            Endi binoni
            faqat old fasaddan emas,

            <br><br>

            to'liq uch o'lchamli
            obyekt sifatida tahlil qilamiz.
            """,
        },
        {
            "title": "1. Asosiy hajm",
            "type": "example",
            "text": """
            Savollar:

            <br><br>

            • binoning asosiy hajmi qaysi?<br>
            • uni bir qarashda tushunish mumkinmi?<br>
            • keraksiz bo'linishlar bormi?
            """,
        },
        {
            "title": "2. Proporsiya",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • hajm juda uzun emasmi?<br>
            • juda baland emasmi?<br>
            • asosiy qismlar o'zaro mosmi?
            """,
        },
        {
            "title": "3. Dominanta",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • qaysi qism asosiy?<br>
            • kirish o'qiladimi?<br>
            • barcha hajmlar bir-biri bilan raqobatlashmayaptimi?
            """,
        },
        {
            "title": "4. Qo'shish va ayirish",
            "type": "example",
            "text": """
            Har bir chiqib turgan
            yoki ichkariga kirgan qismga
            savol bering:

            <br><br>

            <b>
            Nega bu yerda aynan shu forma kerak?
            </b>
            """,
        },
        {
            "title": "5. Barcha tomonlarni ko'ring",
            "type": "highlight",
            "text": """
            Bino faqat
            old fasaddan ko'rilmaydi.

            <br><br>

            Uni:

            <br><br>

            • old;<br>
            • yon;<br>
            • orqa;<br>
            • yuqoridan;<br>
            • perspektivada

            <br><br>

            tasavvur qiling.
            """,
        },
        {
            "title": "Xatoni toping",
            "type": "warning",
            "text": """
            Uyning old fasadi
            juda chiroyli.

            <br><br>

            Lekin yon tomondan
            qaralganda:

            <br><br>

            • uchta tasodifiy blok;<br>
            • turli balandliklar;<br>
            • tushunarsiz chiqishlar

            <br><br>

            ko'rinadi.

            <br><br>

            Muammo:

            <br><br>

            bino fasad sifatida chizilgan,
            3D hajm sifatida
            o'ylanmagan.
            """,
        },
        {
            "title": "Professional checklist",
            "type": "example",
            "text": """
            Formani tekshiring:

            <br><br>

            <b>1.</b> Asosiy hajm aniqmi?<br><br>
            <b>2.</b> Proporsiyalar yaxshi ishlayaptimi?<br><br>
            <b>3.</b> Dominanta bormi?<br><br>
            <b>4.</b> Qo'shimcha hajmlar asoslanganmi?<br><br>
            <b>5.</b> Bo'shliqlar mantiqiymi?<br><br>
            <b>6.</b> Barcha fasadlar bir butunmi?<br><br>
            <b>7.</b> 3D obraz tushunarlimi?
            """,
        },
        {
            "title": "Modul yakuni",
            "type": "highlight",
            "text": """
            Siz endi:

            <br><br>

            ✓ forma va hajmni farqlaysiz;<br>
            ✓ oddiy geometrik hajmlarni tahlil qilasiz;<br>
            ✓ hajmlarni birlashtirasiz;<br>
            ✓ qo'shish va ayirish prinsipini tushunasiz;<br>
            ✓ bo'shliqni kompozitsiya elementi sifatida ko'rasiz;<br>
            ✓ plandan 3D hajmni tasavvur qilasiz;<br>
            ✓ binoni barcha tomonlardan tahlil qilasiz.

            <br><br>

            Keyingi modul:
            <b>Arxitektura uslublari.</b>
            """,
        },
    ],
}


# ============================================================
# QUIZ
# Q061-Q075
# ============================================================

LEVEL01_MODULE05_QUIZ = {
    "L01_M05_001": [
        {
            "code": "L01_Q061",
            "question": "Arxitekturadagi hajm uch o'lchamli tushunchami?",
            "explanation": (
                "Hajm uzunlik, kenglik va balandlikka ega bo'lgan uch o'lchamli shakldir."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L01_Q062",
            "question": "Arxitektor faqat Floor Plan haqida o'ylashi yetarlimi?",
            "explanation": (
                "Plan bilan birga binoning uch o'lchamli hajmi ham tasavvur qilinadi."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L01_Q063",
            "question": "Bir xil plan turli balandliklarda turlicha 3D obraz berishi mumkinmi?",
            "explanation": (
                "Balandlik hajm proporsiyasi va binoning tashqi obraziga ta'sir qiladi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L01_M05_002": [
        {
            "code": "L01_Q064",
            "question": "Murakkab arxitektura oddiy geometrik hajmlardan tashkil topishi mumkinmi?",
            "explanation": (
                "Kub, prizma va boshqa oddiy hajmlar murakkab kompozitsiyaning asosiga aylanishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L01_Q065",
            "question": "Cho'zilgan prizma binoning gorizontal xarakterini kuchaytirishi mumkinmi?",
            "explanation": (
                "Hajm proporsiyasi binoning vizual yo'nalishini belgilashga yordam beradi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L01_Q066",
            "question": "Forma faqat tashqi ko'rinish uchun tanlanadimi?",
            "explanation": (
                "Forma bilan bino funksiyasi va ichki makon o'rtasida ham aloqa mavjud."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
    ],

    "L01_M05_003": [
        {
            "code": "L01_Q067",
            "question": "Bitta binoda bir nechta hajm birlashtirilishi mumkinmi?",
            "explanation": (
                "Asosiy va ikkilamchi hajmlar yagona kompozitsiya sifatida ishlashi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L01_Q068",
            "question": "Barcha hajmlarni bir xil kuchli qilish har doim yaxshi kompozitsiyami?",
            "explanation": (
                "Hajmlar o'rtasida ierarxiya va dominant mavjud bo'lishi kompozitsiyani tushunarli qilishi mumkin."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L01_Q069",
            "question": "Hajmlar proporsiya va o'q orqali bir-biriga bog'lanishi mumkinmi?",
            "explanation": (
                "Umumiy kompozitsion prinsiplar hajmlarni yagona arxitektura sifatida birlashtiradi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L01_M05_004": [
        {
            "code": "L01_Q070",
            "question": "Arxitektura formasini hajm qo'shish orqali yaratish mumkinmi?",
            "explanation": (
                "Asosiy hajmga qo'shimcha bloklar qo'shish forma yaratish usullaridan biridir."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L01_Q071",
            "question": "Hajmdan bir qismni ayirish ham arxitektura forma yaratishi mumkinmi?",
            "explanation": (
                "Recess, terassa yoki kirish chuqurligi kabi elementlar hajmdan ayirish orqali hosil qilinishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L01_Q072",
            "question": "Qancha ko'p chiqish va kesish bo'lsa, arxitektura shuncha yaxshi bo'ladimi?",
            "explanation": (
                "Har bir hajmiy qaror kompozitsion yoki funksional sababga ega bo'lishi kerak."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
    ],

    "L01_M05_005": [
        {
            "code": "L01_Q073",
            "question": "Binoni faqat old fasaddan tahlil qilish yetarlimi?",
            "explanation": (
                "Bino uch o'lchamli obyekt bo'lgani uchun barcha asosiy tomonlardan tahlil qilinadi."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L01_Q074",
            "question": "3D forma auditida asosiy va ikkilamchi hajmlar tahlil qilinadimi?",
            "explanation": (
                "Hajmlar ierarxiyasi umumiy kompozitsiyaning tushunarliligiga ta'sir qiladi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L01_Q075",
            "question": "Forma va hajm bilan ishlashdagi to'g'ri fikrlash qaysi?",
            "explanation": (
                "Arxitektura 2D plan, 3D hajm, proporsiya va kompozitsiyani birgalikda ko'rishni talab qiladi."
            ),
            "options": [
                (
                    "A",
                    "Plan → 3D hajm → proporsiya → kompozitsiya → audit",
                    True,
                ),
                (
                    "B",
                    "Faqat old fasadni bezash",
                    False,
                ),
            ],
        },
    ],
}


# ============================================================
# DATABASE SEED
# ============================================================

def seed_level01_module05():
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
        ) in LEVEL01_MODULE05_LESSONS:

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
