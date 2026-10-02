from database.database import get_connection


# ============================================================
# LEVEL 1
# MODULE 02 - PROPORSIYA VA MASSHTAB
# ============================================================

LEVEL01_MODULE02_LESSONS = [
    (
        "L01_M02",
        "L01_M02_001",
        "Proporsiya nima?",
        "theory",
        "Arxitektura elementlari o'rtasidagi nisbatlarni tushunish.",
        1,
        30,
        15,
    ),
    (
        "L01_M02",
        "L01_M02_002",
        "Inson va bino masshtabi",
        "theory",
        "Bino elementlarini inson o'lchami bilan solishtirish.",
        2,
        30,
        15,
    ),
    (
        "L01_M02",
        "L01_M02_003",
        "Deraza va eshik proporsiyasi",
        "theory",
        "Fasaddagi ochilishlarning hajm bilan munosabatini tushunish.",
        3,
        30,
        15,
    ),
    (
        "L01_M02",
        "L01_M02_004",
        "Fasad proporsiyasi",
        "practice",
        "Fasad qismlari o'rtasidagi nisbatlarni tahlil qilish.",
        4,
        35,
        20,
    ),
    (
        "L01_M02",
        "L01_M02_005",
        "Proporsiyadagi xatolarni topish",
        "practice",
        "Turar joy loyihalaridagi noto'g'ri nisbatlarni aniqlash.",
        5,
        40,
        20,
    ),
]


# ============================================================
# LESSON CONTENT
# ============================================================

LEVEL01_MODULE02_CONTENT = {
    # ========================================================
    # 1-DARS
    # ========================================================

    "L01_M02_001": [
        {
            "title": "Proporsiya nima?",
            "type": "highlight",
            "text": """
            Proporsiya — ikki yoki undan ortiq elementning
            <b>bir-biriga nisbatan o'lchami</b>.

            <br><br>

            Arxitekturada bir element alohida qaralganda
            normal ko'rinishi mumkin.

            <br><br>

            Lekin boshqa element yoniga qo'yilganda
            juda katta yoki juda kichik tuyulishi mumkin.
            """,
        },
        {
            "title": "Oddiy misol",
            "type": "example",
            "text": """
            Tasavvur qiling, oddiy bir qavatli uy bor.

            <br><br>

            Uning asosiy kirish eshigi ustiga
            uyning deyarli yarmi kattaligida portal qo'yildi.

            <br><br>

            Portalning o'zi chiroyli bo'lishi mumkin.

            <br><br>

            Ammo uy hajmiga nisbatan juda katta bo'lsa,
            kompozitsiya og'ir va g'alati ko'rinadi.

            <br><br>

            Muammo portalda emas.

            <br><br>

            <b>Muammo uning proporsiyasida.</b>
            """,
        },
        {
            "title": "Proporsiyani qanday tekshiramiz?",
            "type": "normal",
            "text": """
            Elementga yolg'iz qaramang.

            <br><br>

            Uni boshqa elementlar bilan solishtiring:

            <br><br>

            • deraza devorga nisbatan qanday?<br>
            • eshik portalga nisbatan qanday?<br>
            • tom uy hajmiga nisbatan qanday?<br>
            • ayvon fasadga nisbatan qanday?<br>
            • ustun balandligiga nisbatan qanchalik qalin?
            """,
        },
        {
            "title": "Boshlovchilar xatosi",
            "type": "warning",
            "text": """
            “Kattaroq qilsam, hashamatliroq ko'rinadi”
            degan fikr doim to'g'ri emas.

            <br><br>

            Juda katta element boshqa qismlarni
            vizual jihatdan bosib ketishi mumkin.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Bir uy fasadini oling.

            <br><br>

            Uchta element tanlang:

            <br><br>

            1. Deraza<br>
            2. Kirish portali<br>
            3. Tom

            <br><br>

            Har biri uchun:

            <br><br>

            <b>“Bu element butun uyga nisbatan juda katta,
            juda kichik yoki normalmi?”</b>

            <br><br>

            deb baholang.
            """,
        },
        {
            "title": "Eslab qoling",
            "type": "highlight",
            "text": """
            <b>
            Proporsiya — o'lchamning o'zi emas,
            o'lchamlar orasidagi munosabatdir.
            </b>
            """,
        },
    ],

    # ========================================================
    # 2-DARS
    # ========================================================

    "L01_M02_002": [
        {
            "title": "Inson masshtabi",
            "type": "highlight",
            "text": """
            Arxitektura odam uchun yaratiladi.

            <br><br>

            Shuning uchun bino qanchalik katta yoki kichik
            ekanini tushunish uchun eng muhim o'lchovlardan biri
            — <b>insonning o'zi</b>.
            """,
        },
        {
            "title": "Tasavvur qiling",
            "type": "example",
            "text": """
            Siz render ko'rdingiz.

            <br><br>

            Lekin rasmda odam, avtomobil, eshik yoki
            boshqa tanish o'lchamdagi obyekt yo'q.

            <br><br>

            Bino 3 metr balandmi yoki 15 metr balandmi
            darhol tushunish qiyinlashadi.

            <br><br>

            Tanish obyektlar bizga
            <b>masshtabni his qilishga</b> yordam beradi.
            """,
        },
        {
            "title": "Uyda inson masshtabi",
            "type": "normal",
            "text": """
            Turar joyda quyidagilar inson masshtabini
            his qilishga yordam beradi:

            <br><br>

            • eshik;<br>
            • deraza;<br>
            • zinapoya;<br>
            • mebel;<br>
            • avtomobil;<br>
            • ayvon;<br>
            • odam figurasi.
            """,
        },
        {
            "title": "Juda monumental uy",
            "type": "warning",
            "text": """
            Bir qavatli oilaviy uyda kirish portali
            haddan tashqari baland va massiv bo'lsa,
            uy odamga yaqin turar joy emas,
            katta jamoat binosiga o'xshab qolishi mumkin.

            <br><br>

            Ba'zida bu ataylab qilinadi.

            <br><br>

            Lekin qaror ongli bo'lishi kerak.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Internetdan katta villa rasmini tanlang.

            <br><br>

            Rasmdagi eshik yoki avtomobilni toping.

            <br><br>

            Endi shu tanish element yordamida
            bino qanchalik katta ekanini tasavvur qiling.

            <br><br>

            Agar odam va eshiklarni olib tashlasak,
            masshtabni his qilish qiyinlashadimi?
            """,
        },
    ],

    # ========================================================
    # 3-DARS
    # ========================================================

    "L01_M02_003": [
        {
            "title": "Deraza va eshik ham proporsiya yaratadi",
            "type": "highlight",
            "text": """
            Deraza faqat yorug'lik uchun teshik emas.

            <br><br>

            Eshik ham faqat kirish elementi emas.

            <br><br>

            Ularning eni, balandligi va joylashuvi
            fasad proporsiyasiga kuchli ta'sir qiladi.
            """,
        },
        {
            "title": "Tor va baland deraza",
            "type": "example",
            "text": """
            Tor va baland deraza fasadni
            vertikalroq his qildirishi mumkin.

            <br><br>

            Keng gorizontal deraza esa fasadni
            gorizontal yo'nalishda cho'zilgan qilib ko'rsatishi mumkin.

            <br><br>

            Demak, deraza shakli ham kompozitsiya vositasi.
            """,
        },
        {
            "title": "Derazani faqat tashqaridan o'ylamang",
            "type": "normal",
            "text": """
            Deraza proporsiyasi bir vaqtning o'zida:

            <br><br>

            • fasad;<br>
            • ichki xona;<br>
            • tabiiy yorug'lik;<br>
            • mebel;<br>
            • tashqi ko'rinish

            <br><br>

            bilan bog'liq.
            """,
        },
        {
            "title": "Kirish eshigi",
            "type": "example",
            "text": """
            Asosiy kirish eshigi juda kichik bo'lsa,
            katta fasadda yo'qolib ketishi mumkin.

            <br><br>

            Juda katta bo'lsa esa turar joy masshtabini
            buzishi mumkin.

            <br><br>

            Shuning uchun eshikni faqat katalogdagi
            chiroyli model sifatida tanlamaymiz.
            """,
        },
        {
            "title": "Xato",
            "type": "warning",
            "text": """
            Fasadni chiroyli qilish uchun derazalarni
            tashqaridan ideal ritmda joylashtirib,
            ichkaridagi mebel va xona funksiyasini unutish
            noto'g'ri.

            <br><br>

            <b>Plan va fasad birga ishlashi kerak.</b>
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Bitta fasaddagi barcha derazalarni kuzating.

            <br><br>

            Savollar:

            <br><br>

            • ularning balandligi bir tizimga tushganmi?<br>
            • ayrim derazalar sababsiz juda kichikmi?<br>
            • kirish eshigi fasadda yo'qolib qolganmi?<br>
            • derazalar ichki funksiyaga mos ko'rinadimi?
            """,
        },
    ],

    # ========================================================
    # 4-DARS
    # ========================================================

    "L01_M02_004": [
        {
            "title": "Endi butun fasadni ko'ramiz",
            "type": "highlight",
            "text": """
            Fasad yaxshi ko'rinishi uchun faqat
            bitta derazani yaxshi tanlash yetmaydi.

            <br><br>

            Barcha qismlar orasidagi nisbatni
            birgalikda ko'rish kerak.
            """,
        },
        {
            "title": "Fasadni bo'laklarga ajrating",
            "type": "normal",
            "text": """
            Fasadni xayolan quyidagi qismlarga ajrating:

            <br><br>

            • asosiy bino hajmi;<br>
            • tom;<br>
            • kirish;<br>
            • derazalar;<br>
            • ayvon yoki balkon;<br>
            • sokol;<br>
            • dekorativ hajmlar.

            <br><br>

            Keyin ularning o'zaro nisbatini solishtiring.
            """,
        },
        {
            "title": "Misol",
            "type": "example",
            "text": """
            Bir qavatli uy balandligi uncha katta emas.

            <br><br>

            Lekin tom juda baland qilindi.

            <br><br>

            Natijada tom fasadning asosiy qismidan
            ham kuchliroq ko'rina boshladi.

            <br><br>

            Bu ataylab yaratilgan kompozitsiya bo'lishi mumkin.

            <br><br>

            Ammo tasodifan yuz bergan bo'lsa,
            proporsiyani qayta ko'rib chiqish kerak.
            """,
        },
        {
            "title": "1/2 yoki 1/3 ni yodlash shartmi?",
            "type": "normal",
            "text": """
            Arxitekturada turli proporsional tizimlar mavjud.

            <br><br>

            Lekin boshlang'ich bosqichda eng muhim narsa
            barcha loyihaga bitta matematik formulani majburan
            qo'llash emas.

            <br><br>

            Avval <b>nisbatni ko'ra bilish</b>ni rivojlantiring.
            """,
        },
        {
            "title": "Professional savol",
            "type": "highlight",
            "text": """
            Fasadga qaraganda:

            <br><br>

            <b>
            “Qaysi element o'ziga ajratilgan hajmga nisbatan
            haddan tashqari katta yoki kichik?”
            </b>

            <br><br>

            deb so'rang.
            """,
        },
        {
            "title": "Amaliy topshiriq",
            "type": "example",
            "text": """
            Ikkita bir qavatli uy fasadini tanlang.

            <br><br>

            Birinchi fasadda proporsiya yaxshi deb o'ylagan
            3 ta elementni yozing.

            <br><br>

            Ikkinchi fasadda esa yaxshilash mumkin bo'lgan
            3 ta nisbatni aniqlang.

            <br><br>

            “Yoqdi/yoqmadi” deb emas,
            sabab bilan yozing.
            """,
        },
    ],

    # ========================================================
    # 5-DARS
    # ========================================================

    "L01_M02_005": [
        {
            "title": "Proporsiya xatosini topamiz",
            "type": "highlight",
            "text": """
            Endi arxitektor ko'zi bilan
            noto'g'ri nisbatlarni aniqlashni mashq qilamiz.
            """,
        },
        {
            "title": "Xato 1 — ulkan kirish portali",
            "type": "warning",
            "text": """
            Oddiy bir qavatli uy.

            <br><br>

            Lekin kirish portali butun fasad balandligining
            deyarli hammasini egallagan.

            <br><br>

            Agar bunga kompozitsion sabab bo'lmasa,
            kirish uyning qolgan qismini bosib ketishi mumkin.
            """,
        },
        {
            "title": "Xato 2 — juda kichik derazalar",
            "type": "warning",
            "text": """
            Katta devor yuzasida juda kichkina derazalar
            tasodifiy joylashtirilgan.

            <br><br>

            Fasad og'ir va yopiq ko'rinishi mumkin.

            <br><br>

            Shu bilan birga ichki xona yorug'ligi ham
            alohida tekshirilishi kerak.
            """,
        },
        {
            "title": "Xato 3 — tom uyni yutib yubordi",
            "type": "warning",
            "text": """
            Tom hajmi shu qadar katta bo'ldiki,
            ko'z avval uyga emas, faqat tomga qaraydi.

            <br><br>

            Bu har doim xato emas.

            <br><br>

            Lekin tom dominanta bo'lishi
            loyiha konsepsiyasiga mos kelishi kerak.
            """,
        },
        {
            "title": "Xato 4 — ustun juda nozik",
            "type": "warning",
            "text": """
            Katta va og'ir ayvon tomi ostida juda nozik
            ko'rinadigan ustunlar ishlatilgan.

            <br><br>

            Hatto konstruktiv jihatdan yechim topilgan bo'lsa ham,
            vizual jihatdan ishonchsiz ko'rinishi mumkin.

            <br><br>

            Arxitekturadagi proporsiya insonning
            <b>barqarorlik hissiga</b> ham ta'sir qiladi.
            """,
        },
        {
            "title": "Xatoni topish algoritmi",
            "type": "example",
            "text": """
            Har safar quyidagi 5 savolni bering:

            <br><br>

            <b>1.</b> Qaysi element juda katta?<br><br>
            <b>2.</b> Qaysi element juda kichik?<br><br>
            <b>3.</b> Bino inson masshtabida sezilyaptimi?<br><br>
            <b>4.</b> Deraza va eshiklar hajmga mosmi?<br><br>
            <b>5.</b> Tom va asosiy bino hajmi muvozanatlimi?
            """,
        },
        {
            "title": "Mini-loyiha",
            "type": "example",
            "text": """
            Bir uy fasadini tanlang va
            kamida 5 ta asosiy elementini yozing.

            <br><br>

            Har biriga:

            <br><br>

            • juda katta;<br>
            • normal;<br>
            • juda kichik

            <br><br>

            bahosidan birini bering.

            <br><br>

            Keyin har bir bahoni bitta gap bilan asoslang.
            """,
        },
        {
            "title": "Modul xulosasi",
            "type": "highlight",
            "text": """
            Siz endi:

            <br><br>

            ✓ proporsiya;<br>
            ✓ inson masshtabi;<br>
            ✓ deraza va eshik nisbati;<br>
            ✓ fasad qismlari nisbati;<br>
            ✓ noto'g'ri proporsiyani aniqlash

            <br><br>

            bo'yicha boshlang'ich professional fikrlashga egasiz.

            <br><br>

            Keyingi modul:
            <b>Ritm va takrorlanish.</b>
            """,
        },
    ],
}


# ============================================================
# QUIZ DATA
# ============================================================

LEVEL01_MODULE02_QUIZ = {
    "L01_M02_001": [
        {
            "code": "L01_Q016",
            "question": "Arxitekturada proporsiya nimani anglatadi?",
            "explanation": (
                "Proporsiya elementlarning bir-biriga nisbatan o'lcham munosabatidir."
            ),
            "options": [
                ("A", "Faqat absolut o'lcham", False),
                ("B", "Elementlar o'lchamlari orasidagi nisbat", True),
                ("C", "Faqat material rangi", False),
                ("D", "Faqat narx", False),
            ],
        },
        {
            "code": "L01_Q017",
            "question": "Katta element har doim chiroyliroq ko'rinadimi?",
            "explanation": (
                "Elementning boshqa qismlarga nisbati muhim; kattalikning o'zi sifat belgisi emas."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L01_Q018",
            "question": "Proporsiyani tekshirishda nima muhim?",
            "explanation": (
                "Elementlarni alohida emas, boshqa qismlar bilan nisbatda ko'rish kerak."
            ),
            "options": [
                ("A", "Elementlarni o'zaro solishtirish", True),
                ("B", "Faqat bitta elementga qarash", False),
            ],
        },
    ],

    "L01_M02_002": [
        {
            "code": "L01_Q019",
            "question": "Inson masshtabi nima uchun kerak?",
            "explanation": (
                "U bino va makon o'lchamini inson bilan bog'lab his qilishga yordam beradi."
            ),
            "options": [
                ("A", "Bino hajmini his qilish uchun", True),
                ("B", "Faqat rang tanlash uchun", False),
            ],
        },
        {
            "code": "L01_Q020",
            "question": "Renderdagi odam figurasi masshtabni tushunishga yordam beradimi?",
            "explanation": (
                "Tanish o'lchamdagi odam figurasi bino kattaligini his qilishga yordam beradi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L01_Q021",
            "question": "Bir qavatli turar joydagi juda monumental portal har doim to'g'ri yechimmi?",
            "explanation": (
                "U loyiha konsepsiyasiga mos bo'lishi kerak; aks holda inson masshtabini buzishi mumkin."
            ),
            "options": [
                ("A", "Har doim", False),
                ("B", "Yo'q, loyiha sababiga bog'liq", True),
            ],
        },
    ],

    "L01_M02_003": [
        {
            "code": "L01_Q022",
            "question": "Deraza shakli fasadning vizual yo'nalishiga ta'sir qiladimi?",
            "explanation": (
                "Tor-baland yoki keng-gorizontal deraza fasadni turlicha his qildirishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L01_Q023",
            "question": "Derazani faqat fasaddan kelib chiqib joylashtirish to'g'rimi?",
            "explanation": (
                "Deraza ichki xona, mebel, yorug'lik va fasad bilan birga hal qilinadi."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L01_Q024",
            "question": "Asosiy kirish eshigi katta fasadda juda kichik bo'lsa nima yuz berishi mumkin?",
            "explanation": (
                "Kirish vizual jihatdan yo'qolib, ierarxiya zaiflashishi mumkin."
            ),
            "options": [
                ("A", "Kirish yo'qolib ketishi mumkin", True),
                ("B", "Har doim fasad yaxshilanadi", False),
            ],
        },
    ],

    "L01_M02_004": [
        {
            "code": "L01_Q025",
            "question": "Fasad proporsiyasini baholashda nimani solishtiramiz?",
            "explanation": (
                "Tom, bino hajmi, kirish, deraza va boshqa qismlar o'zaro tahlil qilinadi."
            ),
            "options": [
                ("A", "Fasad qismlarining o'zaro nisbatini", True),
                ("B", "Faqat fasad rangini", False),
            ],
        },
        {
            "code": "L01_Q026",
            "question": "Har bir loyihaga bir xil matematik proporsiyani majburan qo'llash kerakmi?",
            "explanation": (
                "Proporsional tizimlar vosita; loyiha konteksti va kompozitsiyasi ham muhim."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L01_Q027",
            "question": "Tomning hajmi asosiy bino hajmiga nisbatan tahlil qilinadimi?",
            "explanation": (
                "Tom va asosiy hajm o'rtasidagi nisbat fasad proporsiyasining bir qismidir."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L01_M02_005": [
        {
            "code": "L01_Q028",
            "question": "Juda katta kirish portali nimaga olib kelishi mumkin?",
            "explanation": (
                "Portal butun fasadni vizual bosib ketishi mumkin."
            ),
            "options": [
                ("A", "Fasadni vizual bosib ketishi mumkin", True),
                ("B", "Hech qachon ta'sir qilmaydi", False),
            ],
        },
        {
            "code": "L01_Q029",
            "question": "Katta devorda juda kichik derazalar fasadni qanday ko'rsatishi mumkin?",
            "explanation": (
                "Fasad og'ir va yopiq ko'rinishi mumkin."
            ),
            "options": [
                ("A", "Og'ir va yopiq", True),
                ("B", "Har doim yengil", False),
            ],
        },
        {
            "code": "L01_Q030",
            "question": "Proporsiya xatosini topishda qaysi savol foydali?",
            "explanation": (
                "Elementning boshqa qismlarga nisbatan juda katta yoki kichikligini aniqlash muhim."
            ),
            "options": [
                ("A", "Qaysi element juda katta yoki kichik?", True),
                ("B", "Faqat material narxi qancha?", False),
            ],
        },
    ],
}


# ============================================================
# DATABASE SEED
# ============================================================

def seed_level01_module02():
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
        ) in LEVEL01_MODULE02_LESSONS:

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
