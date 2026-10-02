from database.database import get_connection


# ============================================================
# LEVEL 4
# MODULE 07 - ISSIQ IQLIMDA LOYIHA
# ============================================================

LEVEL04_MODULE07_LESSONS = [
    (
        "L04_M07",
        "L04_M07_001",
        "Issiq iqlimni tushunish",
        "theory",
        "Issiq iqlimning uy rejasiga, fasadga va hovliga ta'sirini tushunish.",
        1,
        40,
        20,
    ),
    (
        "L04_M07",
        "L04_M07_002",
        "Quyosh va orientatsiya",
        "theory",
        "Uy va asosiy xonalarni quyosh yo'nalishi bilan bog'lab tahlil qilish.",
        2,
        45,
        20,
    ),
    (
        "L04_M07",
        "L04_M07_003",
        "Deraza va soyalanish",
        "theory",
        "Deraza ochilishlari va tashqi soyalanish elementlarini iqlim bilan bog'lash.",
        3,
        45,
        20,
    ),
    (
        "L04_M07",
        "L04_M07_004",
        "Tabiiy shamollatish va hovli mikroiqlimi",
        "practice",
        "Havo harakati, yashil hudud va yarim ochiq makonlardan foydalanish.",
        4,
        50,
        20,
    ),
    (
        "L04_M07",
        "L04_M07_005",
        "Issiq iqlim loyihasi auditi",
        "practice",
        "Issiq iqlimdagi turar joy loyihasining tipik xatolarini aniqlash.",
        5,
        60,
        25,
    ),
]


# ============================================================
# CONTENT
# ============================================================

LEVEL04_MODULE07_CONTENT = {
    "L04_M07_001": [
        {
            "title": "Iqlim — loyiha qarorining bir qismi",
            "type": "highlight",
            "text": """
            Uy faqat uchastka va xona talablariga qarab
            loyihalanmaydi.

            <br><br>

            Iqlim ham:

            <br><br>

            • fasadga;<br>
            • oynalarga;<br>
            • hovliga;<br>
            • ayvonga;<br>
            • xonalar joylashuviga

            <br><br>

            ta'sir qiladi.
            """,
        },
        {
            "title": "Issiq iqlimdagi asosiy savollar",
            "type": "normal",
            "text": """
            Loyiha vaqtida so'rang:

            <br><br>

            • kuchli quyosh qayerdan keladi?<br>
            • qaysi xonalar ko'proq qizishi mumkin?<br>
            • qayerda soya kerak?<br>
            • hovli qayerda qulayroq ishlaydi?<br>
            • havo harakati qanday tashkil qilinadi?
            """,
        },
        {
            "title": "Tasavvur qiling",
            "type": "example",
            "text": """
            Ikki bir xil uy bor.

            <br><br>

            Birinchisida katta oynalar
            eng kuchli quyosh tomoniga
            himoyasiz qaragan.

            <br><br>

            Ikkinchisida esa
            oynalar, ayvon va soyalanish
            birgalikda o'ylangan.

            <br><br>

            Plan bir xil bo'lishi mumkin,
            lekin foydalanish sifati farq qiladi.
            """,
        },
        {
            "title": "Iqlimga javob beruvchi arxitektura",
            "type": "highlight",
            "text": """
            Maqsad faqat
            “issiqni bloklash” emas.

            <br><br>

            Maqsad:

            <br><br>

            <b>
            yorug'lik + soya + havo + hovli
            </b>

            <br><br>

            o'rtasida muvozanat yaratish.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Bitta uyni tanlang.

            <br><br>

            Unda issiq iqlimga ta'sir qiluvchi
            kamida 6 ta arxitektura elementini belgilang.
            """,
        },
    ],

    "L04_M07_002": [
        {
            "title": "Orientatsiya xonalarni o'zgartiradi",
            "type": "highlight",
            "text": """
            Bir xil xona
            turli orientatsiyada
            turlicha ishlashi mumkin.
            """,
        },
        {
            "title": "Ertalab va kechki quyosh",
            "type": "normal",
            "text": """
            Sharq tomoni ko'proq
            ertalabki quyoshni olishi mumkin.

            <br><br>

            G'arb tomoni esa
            kechki payt kuchliroq
            qizishi mumkin.
            """,
        },
        {
            "title": "Living",
            "type": "example",
            "text": """
            Living qayerga qarashi
            faqat manzara bilan emas,

            <br><br>

            quyosh,
            hovli
            va kundalik foydalanish

            <br><br>

            bilan birga tahlil qilinadi.
            """,
        },
        {
            "title": "Service xonalar",
            "type": "normal",
            "text": """
            Ayrim hollarda:

            <br><br>

            • ombor;<br>
            • texnik xona;<br>
            • sanuzel;<br>
            • garderob

            <br><br>

            kuchli tashqi ta'sirli tomonda
            buffer vazifasini bajarishi mumkin.
            """,
        },
        {
            "title": "Universal formula yo'q",
            "type": "warning",
            "text": """
            “Bu xona har doim faqat
            shu tomonga qarashi kerak”

            <br><br>

            degan oddiy universal qoida
            bilan loyiha qilish noto'g'ri.

            <br><br>

            Uchastka, qo'shni, manzara,
            hovli va boshqa omillar
            birgalikda ko'riladi.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Bitta uy planida belgilang:

            <br><br>

            • ertalab faol xonalar;<br>
            • kechki faol xonalar;<br>
            • private xonalar;<br>
            • service xonalar.

            <br><br>

            So'ng orientatsiya bilan solishtiring.
            """,
        },
    ],

    "L04_M07_003": [
        {
            "title": "Deraza — yorug'lik ham, issiqlik ham",
            "type": "highlight",
            "text": """
            Katta deraza
            doim yaxshi yechim emas.

            <br><br>

            U:

            <br><br>

            • tabiiy yorug'lik;<br>
            • ko'rinish;<br>
            • quyosh issiqligi;<br>
            • privacy

            <br><br>

            bilan birga tahlil qilinadi.
            """,
        },
        {
            "title": "Deraza yo'nalishi",
            "type": "normal",
            "text": """
            Bir xil o'lchamdagi deraza
            turli fasadlarda
            turlicha quyosh ta'siriga ega bo'lishi mumkin.
            """,
        },
        {
            "title": "Tashqi soyalanish",
            "type": "normal",
            "text": """
            Quyoshni bino ichiga kirgandan keyin emas,
            tashqarida boshqarish foydali bo'lishi mumkin.

            <br><br>

            Buning uchun:

            <br><br>

            • ayvon;<br>
            • soyabon;<br>
            • pergola;<br>
            • lamel;<br>
            • daraxt

            <br><br>

            kabi elementlardan foydalanish mumkin.
            """,
        },
        {
            "title": "Gorizontal va vertikal himoya",
            "type": "example",
            "text": """
            Quyoshning kelish burchagi
            fasadga qarab farq qiladi.

            <br><br>

            Shu sababli faqat
            bitta turdagi soyabon
            hamma tomonda bir xil natija bermaydi.
            """,
        },
        {
            "title": "Derazani kichraytirishning o'zi yechim emas",
            "type": "warning",
            "text": """
            Issiqdan qo'rqib
            barcha oynalarni juda kichik qilish

            <br><br>

            tabiiy yorug'lik va
            fazoviy sifatni ham pasaytirishi mumkin.

            <br><br>

            Maqsad — balans.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            4 ta fasad chizing:

            <br><br>

            NORTH<br>
            SOUTH<br>
            EAST<br>
            WEST

            <br><br>

            Har birida oynalar va
            soyalanish strategiyasini
            alohida ko'rsating.
            """,
        },
    ],

    "L04_M07_004": [
        {
            "title": "Tabiiy shamollatish haqida fikrlash",
            "type": "highlight",
            "text": """
            Havo harakati
            uy ichidagi qulaylikka
            yordam berishi mumkin.

            <br><br>

            Lekin bu faqat
            “derazani ochish” degani emas.
            """,
        },
        {
            "title": "Ochilishlarning aloqasi",
            "type": "normal",
            "text": """
            Qarama-qarshi yoki
            mantiqiy bog'langan ochilishlar

            <br><br>

            havo harakati uchun
            imkon yaratishi mumkin.
            """,
        },
        {
            "title": "Ichki eshiklar",
            "type": "normal",
            "text": """
            Tashqi derazalar ochiq bo'lsa ham,

            <br><br>

            ichki plan havo yo'lini
            butunlay to'sib qo'yishi mumkin.

            <br><br>

            Shuning uchun plan ham muhim.
            """,
        },
        {
            "title": "Hovli mikroiqlimi",
            "type": "highlight",
            "text": """
            Hovlining sifati
            faqat m² bilan o'lchanmaydi.

            <br><br>

            Unda:

            <br><br>

            • soya;<br>
            • daraxt;<br>
            • yashil zona;<br>
            • yarim ochiq makon;<br>
            • havo harakati

            <br><br>

            birga ishlashi mumkin.
            """,
        },
        {
            "title": "Qattiq qoplama",
            "type": "warning",
            "text": """
            Hovlining deyarli hammasi
            qattiq qoplama bo'lsa,

            <br><br>

            yozgi tashqi makon sifati
            pasayishi mumkin.
            """,
        },
        {
            "title": "Daraxt va ayvon",
            "type": "example",
            "text": """
            Bitta yaxshi joylashtirilgan daraxt,
            ayvon va living ochilishi

            <br><br>

            birgalikda
            kuchli family tashqi makon
            yaratishi mumkin.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Genplaningizda:

            <br><br>

            • soyali zona;<br>
            • quyoshli zona;<br>
            • yashil zona;<br>
            • shamollatish yo'nalishi;<br>
            • ayvon

            <br><br>

            ni belgilang.
            """,
        },
    ],

    "L04_M07_005": [
        {
            "title": "Issiq iqlim auditini boshlaymiz",
            "type": "highlight",
            "text": """
            Endi loyiha
            faqat plan sifatida emas,

            <br><br>

            iqlimga javob beruvchi
            yashash tizimi sifatida tekshiriladi.
            """,
        },
        {
            "title": "Xato 1 — katta oynalar himoyasiz",
            "type": "warning",
            "text": """
            Katta shisha fasad mavjud,

            <br><br>

            lekin kuchli quyosh tomonida
            hech qanday tashqi soyalanish yo'q.
            """,
        },
        {
            "title": "Xato 2 — terassa kun bo'yi quyoshda",
            "type": "warning",
            "text": """
            Outdoor dining mavjud,

            <br><br>

            lekin foydalaniladigan vaqtda
            uning katta qismi
            soyasiz qoladi.
            """,
        },
        {
            "title": "Xato 3 — shamollatish yo'li yopiq",
            "type": "warning",
            "text": """
            Ko'p derazalar mavjud,

            <br><br>

            lekin ichki plan
            havo harakatini
            samarali davom ettirishga
            imkon bermaydi.
            """,
        },
        {
            "title": "Xato 4 — hovli faqat beton",
            "type": "warning",
            "text": """
            Katta hovli mavjud,

            <br><br>

            lekin soya,
            daraxt va yashil hudud
            deyarli yo'q.
            """,
        },
        {
            "title": "Xato 5 — orientatsiya tekshirilmagan",
            "type": "warning",
            "text": """
            Plan xonalari qulay,

            <br><br>

            ammo bino uchastkaga
            qaysi yo'nalishda o'tirgani
            hisobga olinmagan.
            """,
        },
        {
            "title": "Professional checklist",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            <b>1.</b> Shimol qayerda?<br><br>
            <b>2.</b> Kuchli quyosh qayerdan keladi?<br><br>
            <b>3.</b> Qaysi oynalar himoya talab qiladi?<br><br>
            <b>4.</b> Ayvon qayerda ishlaydi?<br><br>
            <b>5.</b> Havo harakati uchun imkon bormi?<br><br>
            <b>6.</b> Family hovli soyalanadimi?<br><br>
            <b>7.</b> Yashil zona mikroiqlimga yordam beradimi?
            """,
        },
        {
            "title": "Mini-case",
            "type": "example",
            "text": """
            1 qavatli oilaviy uy.

            <br><br>

            Talab:

            <br><br>

            • katta living;<br>
            • private hovli;<br>
            • 8 kishilik terassa;<br>
            • katta oynalar;<br>
            • yashil zona;<br>
            • yozgi foydalanish qulay bo'lsin.

            <br><br>

            Plan + fasad + genplan
            bo'yicha iqlimiy konsepsiya yarating.

            <br><br>

            Har bir qarorga
            “nega?” deb javob yozing.
            """,
        },
        {
            "title": "Modul yakuni",
            "type": "highlight",
            "text": """
            Siz endi:

            <br><br>

            ✓ iqlimni loyiha omili sifatida ko'rish;<br>
            ✓ orientatsiyani tahlil qilish;<br>
            ✓ oynalarni boshqarish;<br>
            ✓ soyalanishni rejalash;<br>
            ✓ tabiiy shamollatishni hisobga olish;<br>
            ✓ hovli mikroiqlimini yaxshilash

            <br><br>

            ko'nikmalariga ega bo'ldingiz.

            <br><br>

            Keyingi modul:
            <b>Mahalliy fasad.</b>
            """,
        },
    ],
}


# ============================================================
# QUIZ
# ============================================================

LEVEL04_MODULE07_QUIZ = {
    "L04_M07_001": [
        {
            "code": "L04_Q091",
            "question": "Iqlim uy rejasiga va fasadiga ta'sir qiladimi?",
            "explanation": (
                "Quyosh, soya, havo va tashqi makon loyiha qarorlariga ta'sir qiladi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L04_Q092",
            "question": "Issiq iqlimda faqat konditsioner haqida o'ylash yetarlimi?",
            "explanation": (
                "Arxitektura darajasida orientatsiya, soya, deraza va hovli ham hisobga olinadi."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L04_Q093",
            "question": "Yorug'lik va soya o'rtasida balans kerakmi?",
            "explanation": (
                "Issiq iqlimdagi loyiha faqat barcha quyoshni to'sish emas, sifatli muvozanat yaratishdir."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L04_M07_002": [
        {
            "code": "L04_Q094",
            "question": "Bir xil xona turli orientatsiyada turlicha ishlashi mumkinmi?",
            "explanation": (
                "Quyoshning vaqti va intensivligi yo'nalishga qarab farq qiladi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L04_Q095",
            "question": "G'arb tomoni kechki quyosh ta'sirini ko'proq olishi mumkinmi?",
            "explanation": (
                "G'arbiy fasad kechki paytdagi quyosh bilan alohida tahlil qilinadi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L04_Q096",
            "question": "Har bir xona uchun universal bitta orientatsiya qoidasi bormi?",
            "explanation": (
                "Uchastka, hovli, qo'shni va foydalanish omillari ham hisobga olinadi."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
    ],

    "L04_M07_003": [
        {
            "code": "L04_Q097",
            "question": "Katta deraza issiqlik ta'siriga ham ega bo'lishi mumkinmi?",
            "explanation": (
                "Deraza yorug'lik va ko'rinish bilan birga quyosh issiqligiga ham ta'sir qiladi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L04_Q098",
            "question": "Tashqi soyalanish elementlari quyoshni boshqarishga yordam beradimi?",
            "explanation": (
                "Ayvon, pergola, lamel va daraxtlar tashqi soyalanish vositasi bo'lishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L04_Q099",
            "question": "Barcha derazalarni juda kichraytirish doim eng yaxshi iqlimiy yechimmi?",
            "explanation": (
                "Bu tabiiy yorug'lik va makon sifatini pasaytirishi mumkin; balans kerak."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
    ],

    "L04_M07_004": [
        {
            "code": "L04_Q100",
            "question": "Tabiiy shamollatish faqat bitta derazani ochishdan iboratmi?",
            "explanation": (
                "Ochilishlarning o'zaro aloqasi va ichki plan ham havo harakatiga ta'sir qiladi."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L04_Q101",
            "question": "Ichki plan havo harakatini to'sishi mumkinmi?",
            "explanation": (
                "Tashqi ochilishlar bo'lsa ham ichki zonalash havo yo'lini to'sib qo'yishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L04_Q102",
            "question": "Daraxt va yashil zona hovli mikroiqlimiga yordam berishi mumkinmi?",
            "explanation": (
                "Soya va tashqi makon sifati orqali ular hovlining qulayligiga ta'sir qilishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L04_M07_005": [
        {
            "code": "L04_Q103",
            "question": "Kuchli quyosh tomonidagi katta oynalarni soyasiz qoldirish muammo bo'lishi mumkinmi?",
            "explanation": (
                "Quyosh ta'siri va tashqi soyalanish birgalikda tahlil qilinadi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L04_Q104",
            "question": "Katta hovlining deyarli to'liq qattiq qoplama bo'lishi yozgi qulaylikni kamaytirishi mumkinmi?",
            "explanation": (
                "Soya, yashil hudud va yarim ochiq makonlar tashqi muhit sifatiga ta'sir qiladi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L04_Q105",
            "question": "Issiq iqlim loyihasi auditidagi muhim savollardan biri qaysi?",
            "explanation": (
                "Orientatsiya, quyosh, soyalanish va shamollatish birgalikda tekshiriladi."
            ),
            "options": [
                ("A", "Kuchli quyosh qayerdan keladi?", True),
                ("B", "Faqat devor rangi qanday?", False),
            ],
        },
    ],
}


# ============================================================
# DATABASE SEED
# ============================================================

def seed_level04_module07():
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
        ) in LEVEL04_MODULE07_LESSONS:

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
