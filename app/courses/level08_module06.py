from database.database import get_connection


# ============================================================
# LEVEL 8
# MODULE 06 - GIDROIZOLYATSIYA
# ============================================================

LEVEL08_MODULE06_LESSONS = [
    (
        "L08_M06",
        "L08_M06_001",
        "Namlik va gidroizolyatsiya tushunchasi",
        "theory",
        "Binoga namlik qayerdan kelishi va gidroizolyatsiyaning umumiy vazifasini tushunish.",
        1,
        30,
        20,
    ),
    (
        "L08_M06",
        "L08_M06_002",
        "Fundament va yer bilan tutashuv",
        "theory",
        "Yer osti va yerga yaqin konstruksiyalarda namlikdan himoya mantig'ini tushunish.",
        2,
        35,
        20,
    ),
    (
        "L08_M06",
        "L08_M06_003",
        "Tom, balkon va tashqi zonalar",
        "practice",
        "Tom, balkon va ochiq tashqi yuzalarda suvni boshqarish va gidroizolyatsiya uzluksizligini tushunish.",
        3,
        35,
        20,
    ),
    (
        "L08_M06",
        "L08_M06_004",
        "Wet room va ichki nam zonalar",
        "practice",
        "Sanuzel va boshqa nam xonalarda gidroizolyatsiya, sath va suv chiqishi koordinatsiyasini tushunish.",
        4,
        40,
        20,
    ),
    (
        "L08_M06",
        "L08_M06_005",
        "Gidroizolyatsiya professional audit",
        "practice",
        "Namlik yo'llari, uzluksizlik, tutashuvlar, penetratsiyalar va BIM detallarini kompleks tekshirish.",
        5,
        40,
        25,
    ),
]


# ============================================================
# CONTENT
# ============================================================

LEVEL08_MODULE06_CONTENT = {
    "L08_M06_001": [
        {
            "title": "Gidroizolyatsiya nima?",
            "type": "highlight",
            "text": """
            Gidroizolyatsiya —
            konstruksiya va
            ichki makonni

            <br><br>

            zararli namlik
            va suv ta'siridan
            himoya qilish
            tizimlaridan biri.
            """,
        },
        {
            "title": "Namlik qayerdan keladi?",
            "type": "normal",
            "text": """
            Namlik:

            <br><br>

            • gruntdan;<br>
            • yomg'irdan;<br>
            • tomdan;<br>
            • balkon va terassadan;<br>
            • sanuzeldan;<br>
            • muhandislik tizimlaridan

            <br><br>

            kelishi mumkin.
            """,
        },
        {
            "title": "Suv faqat yuqoridan kelmaydi",
            "type": "warning",
            "text": """
            Namlik muammosini
            faqat yomg'ir bilan
            bog'lash noto'g'ri.

            <br><br>

            Yer osti
            va ichki nam zonalar
            ham muhim.
            """,
        },
        {
            "title": "Asosiy fikr",
            "type": "highlight",
            "text": """
            Professional yechimda
            asosiy savol:

            <br><br>

            “Suv qayerdan keladi
            va qayerga ketadi?”
            """,
        },
        {
            "title": "Continuity",
            "type": "normal",
            "text": """
            Gidroizolyatsiya
            alohida-alohida
            bo'laklar emas,

            <br><br>

            uzluksiz himoya
            mantig'ida ishlashi kerak.
            """,
        },
        {
            "title": "Zaif nuqtalar",
            "type": "warning",
            "text": """
            Eng ko'p muammo
            ko'pincha

            <br><br>

            katta tekis yuzada emas,

            <br><br>

            balki:

            • burchaklarda;<br>
            • tutashuvlarda;<br>
            • teshiklarda;<br>
            • eshik yonida;<br>
            • quvur o'tishlarida

            <br><br>

            paydo bo'ladi.
            """,
        },
        {
            "title": "Tasavvur qiling",
            "type": "example",
            "text": """
            Tom yuzasi
            yaxshi himoyalangan,

            <br><br>

            lekin chimney
            atrofidagi tutashuv
            noto'g'ri.

            <br><br>

            Muammo butun tomda
            emas, aynan
            bitta detaldan
            boshlanishi mumkin.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Uyda namlik
            tushishi mumkin bo'lgan

            <br><br>

            kamida 6 ta
            zonani yozing.

            <br><br>

            Har biri uchun
            suv manbasini belgilang.
            """,
        },
    ],

    "L08_M06_002": [
        {
            "title": "Yer bilan tutashuv",
            "type": "highlight",
            "text": """
            Fundament va
            yerga yaqin qismlar

            <br><br>

            namlik bilan
            doimiy aloqada
            bo'lishi mumkin.
            """,
        },
        {
            "title": "Kapillyar namlik",
            "type": "normal",
            "text": """
            Namlik
            ayrim materiallarda

            <br><br>

            kapillyar yo'l
            bilan yuqoriga
            harakat qilishi mumkin.
            """,
        },
        {
            "title": "Fundament himoyasi",
            "type": "normal",
            "text": """
            Yer osti
            konstruksiyalari

            <br><br>

            loyiha yechimiga
            qarab tashqi
            namlikdan

            <br><br>

            himoyalanishi kerak.
            """,
        },
        {
            "title": "Faqat membrana emas",
            "type": "highlight",
            "text": """
            Yer osti namligi
            bilan ishlash

            <br><br>

            faqat bitta
            gidroizolyatsiya qatlamidan
            iborat bo'lmasligi mumkin.

            <br><br>

            Suvni boshqarish
            umumiy tizim sifatida
            qaraladi.
            """,
        },
        {
            "title": "Tutashuvlar",
            "type": "warning",
            "text": """
            Devor va fundament
            tutashuvi

            <br><br>

            gidroizolyatsiyaning
            muhim nuqtalaridan biri.
            """,
        },
        {
            "title": "Penetratsiyalar",
            "type": "warning",
            "text": """
            Quvur
            yoki boshqa
            kommunikatsiya

            <br><br>

            yer osti devoridan
            o'tsa,

            <br><br>

            shu joy alohida
            detail talab qiladi.
            """,
        },
        {
            "title": "Geologiya va suv",
            "type": "normal",
            "text": """
            Yer osti
            sharoitlari haqida

            <br><br>

            real ma'lumot
            bo'lmasa,

            <br><br>

            himoya yechimi
            taxmin bilan
            tanlanmasligi kerak.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Fundament devori
            kesimini tasavvur qiling.

            <br><br>

            Belgilang:

            • grunt tomoni;<br>
            • ichki tomon;<br>
            • namlik kelishi mumkin bo'lgan joy;<br>
            • penetratsiya;<br>
            • tutashuv zonasi.
            """,
        },
    ],

    "L08_M06_003": [
        {
            "title": "Tom va suv",
            "type": "highlight",
            "text": """
            Tomdagi asosiy
            vazifalardan biri —

            <br><br>

            suvni binodan
            xavfsiz chiqarish.
            """,
        },
        {
            "title": "Nishabning ahamiyati",
            "type": "normal",
            "text": """
            Suv turib qolmasligi
            uchun

            <br><br>

            sath va nishab
            mantig'i muhim.
            """,
        },
        {
            "title": "Drainage",
            "type": "normal",
            "text": """
            Suvni qayerga
            olib chiqish

            <br><br>

            tom va balkon
            dizaynining
            bir qismi.
            """,
        },
        {
            "title": "Balkon",
            "type": "highlight",
            "text": """
            Balkon
            ochiq tashqi zona
            bo'lsa,

            <br><br>

            unda:

            • nishab;<br>
            • suv chiqishi;<br>
            • gidroizolyatsiya;<br>
            • eshik tutashuvi

            <br><br>

            birgalikda hal qilinadi.
            """,
        },
        {
            "title": "Eshik threshold",
            "type": "warning",
            "text": """
            Balkon yoki terassadan
            ichki xonaga kirish

            <br><br>

            eng nozik
            tutashuvlardan biri
            bo'lishi mumkin.
            """,
        },
        {
            "title": "Parapet",
            "type": "normal",
            "text": """
            Parapet
            va tom yuzasi
            tutashuvi

            <br><br>

            ham uzluksiz
            himoya mantig'ida
            hal qilinadi.
            """,
        },
        {
            "title": "Roof penetration",
            "type": "warning",
            "text": """
            Chimney,
            vent
            yoki boshqa
            chiqishlar

            <br><br>

            gidroizolyatsiya
            qatlamini buzadigan
            nuqta bo'lishi mumkin.
            """,
        },
        {
            "title": "Tasavvur qiling",
            "type": "example",
            "text": """
            Balkon sathi
            deyarli tekis.

            <br><br>

            Drain joyi
            noto'g'ri.

            <br><br>

            Suv eshik
            oldida to'planadi.

            <br><br>

            Bu faqat
            finishing xatosi emas,
            balki koordinatsiya
            muammosi.
            """,
        },
    ],

    "L08_M06_004": [
        {
            "title": "Wet room",
            "type": "highlight",
            "text": """
            Sanuzel,
            dush
            va boshqa nam xonalar

            <br><br>

            ichki gidroizolyatsiya
            talab qiladigan
            zonalardan.
            """,
        },
        {
            "title": "Suv manbasi",
            "type": "normal",
            "text": """
            Wet roomda suv:

            <br><br>

            • dushdan;<br>
            • vannadan;<br>
            • lavabo yoki quvurdan;<br>
            • avariya holatidan

            <br><br>

            kelishi mumkin.
            """,
        },
        {
            "title": "Floor + wall junction",
            "type": "warning",
            "text": """
            Pol va devor
            tutashuvi

            <br><br>

            nam xonalardagi
            muhim detal
            hisoblanadi.
            """,
        },
        {
            "title": "Drain",
            "type": "normal",
            "text": """
            Dush yoki
            boshqa wet zone'da

            <br><br>

            suvning drain tomon
            harakat qilishi

            <br><br>

            sath va nishab
            bilan koordinatsiya qilinadi.
            """,
        },
        {
            "title": "Pipe penetration",
            "type": "warning",
            "text": """
            Quvur
            devor yoki poldan
            o'tganda

            <br><br>

            gidroizolyatsiya
            uzluksizligi
            shu joyda
            alohida tekshiriladi.
            """,
        },
        {
            "title": "Eshik zonasi",
            "type": "normal",
            "text": """
            Wet room
            eshigi oldida

            <br><br>

            suvning boshqa
            xonaga chiqib ketmasligi

            <br><br>

            loyiha detali
            bilan boshqariladi.
            """,
        },
        {
            "title": "Tiles waterproofing emas",
            "type": "warning",
            "text": """
            Keramika yoki
            finishing qatlam

            <br><br>

            avtomatik ravishda
            to'liq gidroizolyatsiya
            tizimi degani emas.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Dush xonasi uchun
            5 ta kritik
            nuqtani yozing.

            <br><br>

            Masalan:

            • drain;<br>
            • floor-wall junction;<br>
            • quvur o'tishi;<br>
            • eshik zonasi.
            """,
        },
    ],

    "L08_M06_005": [
        {
            "title": "Gidroizolyatsiya professional audit",
            "type": "highlight",
            "text": """
            Audit zanjiri:

            <br><br>

            Suv manbasi
            → Yo'l
            → Himoya
            → Tutashuv
            → Penetratsiya
            → Drainage
            → BIM detail
            """,
        },
        {
            "title": "1. Suv manbasi",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • suv qayerdan kelishi mumkin?<br>
            • yomg'irmi?<br>
            • gruntmi?<br>
            • ichki wet zone'mi?
            """,
        },
        {
            "title": "2. Suv yo'li",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • suv qayerga oqadi?<br>
            • turib qoladigan joy bormi?<br>
            • noto'g'ri nishab bormi?
            """,
        },
        {
            "title": "3. Continuity",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • himoya uzluksizmi?<br>
            • burchaklarda uzilish yo'qmi?<br>
            • boshqa qatlam bilan tutashuvi tushunarlimi?
            """,
        },
        {
            "title": "4. Penetratsiyalar",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • quvurlar qayerdan o'tadi?<br>
            • shaftlar bormi?<br>
            • chimney va vent chiqishlari qanday hal qilingan?
            """,
        },
        {
            "title": "5. Drainage",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • drain joylashuvi to'g'rimi?<br>
            • suv unga yetib boradimi?<br>
            • overflow xavfi bormi?
            """,
        },
        {
            "title": "6. Threshold va tutashuvlar",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • balkon eshigi;<br>
            • wet room eshigi;<br>
            • parapet;<br>
            • devor-pol tutashuvi

            <br><br>

            yechilganmi?
            """,
        },
        {
            "title": "7. BIM detail",
            "type": "normal",
            "text": """
            BIM modelda
            faqat umumiy
            geometriya emas,

            <br><br>

            kritik detallar
            ham mantiqan
            tushunarli bo'lishi kerak.
            """,
        },
        {
            "title": "Xatoni toping",
            "type": "warning",
            "text": """
            Loyihada:

            <br><br>

            • balkon drain'i yuqori nuqtada;<br>
            • sanuzel eshigi oldida sath nazorati yo'q;<br>
            • quvur o'tishlari detallanmagan;<br>
            • parapet tutashuvi ko'rsatilmagan;<br>
            • fundamentdagi penetratsiya himoyasiz.

            <br><br>

            Bu loyiha
            gidroizolyatsiya
            auditiga qaytariladi.
            """,
        },
        {
            "title": "Professional checklist",
            "type": "example",
            "text": """
            Gidroizolyatsiya audit:

            <br><br>

            <b>1.</b> Suv manbalari aniqlanganmi?<br><br>
            <b>2.</b> Suv chiqish yo'li tushunarlimi?<br><br>
            <b>3.</b> Gidroizolyatsiya uzluksizmi?<br><br>
            <b>4.</b> Burchaklar va tutashuvlar hal qilinganmi?<br><br>
            <b>5.</b> Penetratsiyalar detallanganmi?<br><br>
            <b>6.</b> Drainage ishlaydimi?<br><br>
            <b>7.</b> Balkon va tom zonalari koordinatsiya qilinganmi?<br><br>
            <b>8.</b> Wet room detallar tekshirilganmi?<br><br>
            <b>9.</b> BIM model va detallar bir-biriga mosmi?
            """,
        },
        {
            "title": "Modul yakuni",
            "type": "highlight",
            "text": """
            Siz endi:

            <br><br>

            ✓ namlik manbalarini aniqlaysiz;<br>
            ✓ gidroizolyatsiya continuity mantig'ini tushunasiz;<br>
            ✓ fundament va tom zonalarini tekshirasiz;<br>
            ✓ wet room detallarini tushunasiz;<br>
            ✓ penetratsiyalar va drainage'ni koordinatsiya qilasiz;<br>
            ✓ gidroizolyatsiya bo'yicha professional audit qilasiz.

            <br><br>

            Keyingi modul:
            <b>Issiqlik izolyatsiyasi.</b>
            """,
        },
    ],
}


# ============================================================
# QUIZ
# Q076-Q090
# ============================================================

LEVEL08_MODULE06_QUIZ = {
    "L08_M06_001": [
        {
            "code": "L08_Q076",
            "question": "Gidroizolyatsiyaning vazifasi konstruksiya va makonni zararli namlikdan himoya qilishmi?",
            "explanation": (
                "Gidroizolyatsiya suv va namlik ta'sirini boshqarishga yordam beradi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L08_Q077",
            "question": "Namlik faqat yomg'irdan keladimi?",
            "explanation": (
                "Namlik grunt, tom, wet room va muhandislik tizimlari kabi turli manbalardan kelishi mumkin."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L08_Q078",
            "question": "Gidroizolyatsiya tutashuv va penetratsiyalarda ham uzluksiz bo'lishi kerakmi?",
            "explanation": (
                "Ko'p suv muammolari aynan tutashuvlar va teshiklarda yuzaga keladi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L08_M06_002": [
        {
            "code": "L08_Q079",
            "question": "Yer osti konstruksiyalari namlikdan himoya talab qilishi mumkinmi?",
            "explanation": (
                "Yer bilan tutashadigan konstruktsiyalar grunt namligi va yer osti sharoitlariga bog'liq."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L08_Q080",
            "question": "Yer osti devoridan o'tadigan quvur joyi alohida detail talab qilishi mumkinmi?",
            "explanation": (
                "Penetratsiya gidroizolyatsiya qatlamining kritik uzilish nuqtasi bo'lishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L08_Q081",
            "question": "Grunt va yer osti suv sharoitlarini bilmasdan himoya yechimini taxmin bilan tanlash professional yondashuvmi?",
            "explanation": (
                "Real sharoitlar haqida ma'lumot loyiha qarori uchun muhim."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
    ],

    "L08_M06_003": [
        {
            "code": "L08_Q082",
            "question": "Tom va balkonda suvning qayerga oqishi oldindan rejalashtiriladimi?",
            "explanation": (
                "Nishab va drainage suvni xavfsiz chiqarishning asosiy qismlaridir."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L08_Q083",
            "question": "Balkon eshigi tutashuvi gidroizolyatsiya uchun muhim bo'lishi mumkinmi?",
            "explanation": (
                "Ichki va tashqi sathlar uchrashadigan threshold zonasi kritik detal bo'lishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L08_Q084",
            "question": "Chimney yoki vent o'tishi gidroizolyatsiya qatlamiga umuman ta'sir qilmaydimi?",
            "explanation": (
                "Tom penetratsiyalari himoya qatlamining uzluksizligiga ta'sir qiladi."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
    ],

    "L08_M06_004": [
        {
            "code": "L08_Q085",
            "question": "Wet roomlarda floor-wall junction muhim gidroizolyatsiya detali hisoblanadimi?",
            "explanation": (
                "Pol va devor tutashuvi suv ta'siri yuqori bo'lgan kritik zonalardan biridir."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L08_Q086",
            "question": "Keramika qoplama mavjud bo'lsa alohida gidroizolyatsiya mantig'i umuman kerak emasmi?",
            "explanation": (
                "Finishing qatlam va waterproofing tizimi bir xil tushuncha emas."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L08_Q087",
            "question": "Wet roomdagi drain sath va nishab bilan koordinatsiya qilinadimi?",
            "explanation": (
                "Suvning drain tomon oqishi uchun geometriya va sathlar o'zaro mos bo'lishi kerak."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L08_M06_005": [
        {
            "code": "L08_Q088",
            "question": "Gidroizolyatsiya auditida suv manbasi, drainage va penetratsiyalar tekshiriladimi?",
            "explanation": (
                "Professional audit suvning butun yo'lini va himoya tizimining uzluksizligini tekshiradi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L08_Q089",
            "question": "Balkon drain'i suv yig'iladigan zonaga mos kelmasa bu loyiha muammosi bo'lishi mumkinmi?",
            "explanation": (
                "Drainage va sath noto'g'ri bo'lsa suv turib qolishi yoki noto'g'ri tomonga oqishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L08_Q090",
            "question": "Gidroizolyatsiya bilan professional ishlashdagi to'g'ri umumiy workflow qaysi?",
            "explanation": (
                "Avval suv manbasi va yo'li aniqlanadi, uzluksiz himoya, penetratsiyalar va drainage koordinatsiya qilinadi, so'ng detallar audit qilinadi."
            ),
            "options": [
                (
                    "A",
                    "Suv manbasi → suv yo'li → himoya continuity → penetratsiyalar → drainage → audit",
                    True,
                ),
                (
                    "B",
                    "Faqat finishing tanlash → suv yo'lini tekshirmaslik → detallarni keyinga qoldirish",
                    False,
                ),
            ],
        },
    ],
}


# ============================================================
# DATABASE SEED
# ============================================================

def seed_level08_module06():
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
        ) in LEVEL08_MODULE06_LESSONS:

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
