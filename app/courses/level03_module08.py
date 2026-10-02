from database.database import get_connection


# ============================================================
# LEVEL 3
# MODULE 08 - GENPLAN YARATISH
# ============================================================

LEVEL03_MODULE08_LESSONS = [
    (
        "L03_M08",
        "L03_M08_001",
        "Genplan tarkibi",
        "theory",
        "Professional turar joy genplanida qanday elementlar bo'lishini tushunish.",
        1,
        45,
        25,
    ),
    (
        "L03_M08",
        "L03_M08_002",
        "Genplan zonalash sxemasi",
        "practice",
        "Uy, hovli, parking, piyoda va service zonalarini yagona plan ichida bog'lash.",
        2,
        50,
        25,
    ),
    (
        "L03_M08",
        "L03_M08_003",
        "Harakat va tashqi aloqalarni tekshirish",
        "practice",
        "Piyoda, avtomobil, mehmon va service oqimlarini yakuniy genplanda tekshirish.",
        3,
        50,
        25,
    ),
    (
        "L03_M08",
        "L03_M08_004",
        "Genplan professional auditi",
        "practice",
        "Quyosh, privacy, relyef, yashil zona va funksional aloqalarni kompleks tekshirish.",
        4,
        55,
        30,
    ),
    (
        "L03_M08",
        "L03_M08_005",
        "LEVEL 3 yakuniy genplan case",
        "case",
        "Turar joy uchastkasi uchun to'liq site analysis va yakuniy genplan yechimini ishlab chiqish.",
        5,
        70,
        40,
    ),
]


# ============================================================
# CONTENT
# ============================================================

LEVEL03_MODULE08_CONTENT = {
    "L03_M08_001": [
        {
            "title": "Genplan — faqat uy konturi emas",
            "type": "highlight",
            "text": """
            Professional genplan
            uchastkadagi barcha asosiy
            elementlarni bir tizimga birlashtiradi.

            <br><br>

            <b>
            Genplan — uy va yerning
            birgalikda qanday ishlashini ko'rsatadi.
            </b>
            """,
        },
        {
            "title": "Genplanda nimalar bo'ladi?",
            "type": "normal",
            "text": """
            Turar joy genplanida odatda:

            <br><br>

            • uchastka chegarasi;<br>
            • uy konturi;<br>
            • asosiy kirish;<br>
            • piyoda yo'llari;<br>
            • avtomobil yo'li;<br>
            • parking yoki navес;<br>
            • family hovli;<br>
            • yashil zona;<br>
            • service zona;<br>
            • shimol yo'nalishi

            <br><br>

            kabi elementlar ko'rsatiladi.
            """,
        },
        {
            "title": "Qatlamli fikrlash",
            "type": "example",
            "text": """
            Genplanni bitta rasm sifatida emas,
            qatlamlar sifatida o'ylang.

            <br><br>

            1. Uchastka<br>
            2. Tabiiy sharoit<br>
            3. Bino<br>
            4. Harakat<br>
            5. Hovli zonalari<br>
            6. Landshaft<br>
            7. Service
            """,
        },
        {
            "title": "Boshlovchi xatosi",
            "type": "warning",
            "text": """
            Avval uy chizib,
            keyin qolgan bo'sh joylarga
            tasodifiy parking va hovli joylashtirish

            <br><br>

            kuchsiz genplan beradi.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Oldingi uchastkangiz uchun
            genplan tarkibidagi
            10 ta asosiy element ro'yxatini tuzing.
            """,
        },
    ],

    "L03_M08_002": [
        {
            "title": "Avval zonalar, keyin detallar",
            "type": "highlight",
            "text": """
            Genplan yaratishda
            darhol daraxt yoki yo'lak detalidan boshlamang.

            <br><br>

            Avval katta zonalarni joylashtiring.
            """,
        },
        {
            "title": "Asosiy zonalar",
            "type": "normal",
            "text": """
            Birinchi sxemada:

            <br><br>

            • HOUSE;<br>
            • PUBLIC FRONT;<br>
            • PRIVATE FAMILY;<br>
            • PARKING;<br>
            • SERVICE;<br>
            • GREEN

            <br><br>

            zonalarni ajrating.
            """,
        },
        {
            "title": "Aloqalarni tekshiring",
            "type": "example",
            "text": """
            Masalan:

            <br><br>

            living → family hovli<br>
            kitchen → outdoor dining<br>
            parking → uy kirishi<br>
            service → xo'jalik zona

            <br><br>

            mantiqiy bog'langanmi?
            """,
        },
        {
            "title": "Hovli markazi",
            "type": "normal",
            "text": """
            Kuchli genplanda
            tashqi makonning ham
            aniq markazi bo'lishi mumkin.

            <br><br>

            Masalan:

            <br><br>

            terassa,
            daraxt,
            gazebo,
            yashil maydon.
            """,
        },
        {
            "title": "Muvozanat",
            "type": "warning",
            "text": """
            Parking juda katta,
            family hovli juda kichik bo'lsa,

            <br><br>

            uchastka avtomobilga
            haddan tashqari bo'ysunib qolishi mumkin.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Genplaningizda 6 ta katta zona chizing.

            <br><br>

            Hali mayda detallar qo'ymang.

            <br><br>

            Faqat funksional balansni tekshiring.
            """,
        },
    ],

    "L03_M08_003": [
        {
            "title": "Genplan — harakat tizimi",
            "type": "highlight",
            "text": """
            Yaxshi genplanda
            odamlar va avtomobillar
            qayerdan kirib, qayerga borishi aniq.
            """,
        },
        {
            "title": "Piyoda oqimi",
            "type": "normal",
            "text": """
            Tekshiring:

            <br><br>

            ko'cha → piyoda darvozasi →
            asosiy eshik

            <br><br>

            yo'li tushunarlimi?
            """,
        },
        {
            "title": "Avtomobil oqimi",
            "type": "normal",
            "text": """
            Tekshiring:

            <br><br>

            ko'cha → avtomobil darvozasi →
            parking → chiqish

            <br><br>

            real ishlaydimi?
            """,
        },
        {
            "title": "Mehmon oqimi",
            "type": "example",
            "text": """
            Mehmon:

            <br><br>

            • private hovlini kesadimi?<br>
            • parking orasidan yuradimi?<br>
            • asosiy kirishni oson topadimi?
            """,
        },
        {
            "title": "Service oqimi",
            "type": "normal",
            "text": """
            Tekshiring:

            <br><br>

            • mahsulot;<br>
            • chiqindi;<br>
            • xo'jalik ishlari;<br>
            • tashqi xizmat

            <br><br>

            qayerdan yuradi?
            """,
        },
        {
            "title": "Konflikt xaritasi",
            "type": "warning",
            "text": """
            Harakat yo'llari kesishadigan
            barcha nuqtalarni belgilang.

            <br><br>

            Ayniqsa:

            <br><br>

            mashina ↔ bola<br>
            mashina ↔ mehmon<br>
            service ↔ family hovli
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Genplan ustida 4 xil oqim chizing:

            <br><br>

            • FAMILY<br>
            • GUEST<br>
            • CAR<br>
            • SERVICE

            <br><br>

            va konflikt nuqtalarini belgilang.
            """,
        },
    ],

    "L03_M08_004": [
        {
            "title": "Genplan auditini boshlaymiz",
            "type": "highlight",
            "text": """
            Endi genplanni
            faqat chiroyli ko'rinish bilan emas,
            professional savollar orqali tekshiramiz.
            """,
        },
        {
            "title": "1. Uchastka",
            "type": "example",
            "text": """
            • chegaralar aniqmi?<br>
            • ko'cha qayerda?<br>
            • mavjud elementlar hisobga olinganmi?<br>
            • relyef tushunilganmi?
            """,
        },
        {
            "title": "2. Quyosh",
            "type": "example",
            "text": """
            • shimol ko'rsatilganmi?<br>
            • asosiy hovli orientatsiyasi mantiqiymi?<br>
            • kuchli quyosh tomoni hisobga olinganmi?
            """,
        },
        {
            "title": "3. Uy joylashuvi",
            "type": "example",
            "text": """
            • uy uchastkani bo'lib yubormaganmi?<br>
            • living yaxshi hovliga qaraganmi?<br>
            • private zona himoyalanganmi?
            """,
        },
        {
            "title": "4. Parking",
            "type": "example",
            "text": """
            • mashina qulay kiradimi?<br>
            • qulay chiqadimi?<br>
            • piyoda bilan konflikt bormi?<br>
            • fasadni to'liq egallamaganmi?
            """,
        },
        {
            "title": "5. Hovli",
            "type": "example",
            "text": """
            • family zona bormi?<br>
            • guest zona bormi?<br>
            • outdoor dining bormi?<br>
            • yashil zona bormi?<br>
            • xo'jalik qayerda?
            """,
        },
        {
            "title": "6. Relyef va suv",
            "type": "example",
            "text": """
            • baland-past nuqtalar tushunilganmi?<br>
            • suv uyga qarab oqmayaptimi?<br>
            • parking nishabi mantiqiymi?
            """,
        },
        {
            "title": "Professional qoida",
            "type": "highlight",
            "text": """
            <b>
            Har bir element uchun
            “nega aynan shu joyda?”
            degan savolga javob bo'lishi kerak.
            </b>
            """,
        },
    ],

    "L03_M08_005": [
        {
            "title": "LEVEL 3 YAKUNIY CASE",
            "type": "highlight",
            "text": """
            Endi sizga
            to'liq turar joy uchastkasini
            noldan tahlil qilish vazifasi beriladi.

            <br><br>

            Maqsad — professional genplan fikrlashini ko'rsatish.
            """,
        },
        {
            "title": "Vaziyat",
            "type": "example",
            "text": """
            Uchastka:

            <br><br>

            25 × 40 metr.

            <br><br>

            Oila:

            <br><br>

            • ota-ona;<br>
            • ikki bola;<br>
            • mehmonlar tez-tez keladi;<br>
            • 2 ta avtomobil;<br>
            • yozgi ovqatlanish kerak;<br>
            • private family hovli kerak.
            """,
        },
        {
            "title": "1. Site Analysis",
            "type": "example",
            "text": """
            Belgilang:

            <br><br>

            • ko'cha;<br>
            • shimol;<br>
            • quyosh;<br>
            • mavjud elementlar;<br>
            • kuchli tomon;<br>
            • zaif tomon.
            """,
        },
        {
            "title": "2. Uy joylashuvi",
            "type": "example",
            "text": """
            Uy konturini joylashtiring.

            <br><br>

            Keyin yozing:

            <br><br>

            nima uchun aynan shu joy?
            """,
        },
        {
            "title": "3. Parking",
            "type": "example",
            "text": """
            Ikki avtomobil uchun:

            <br><br>

            • darvoza;<br>
            • parking;<br>
            • navес;<br>
            • chiqish

            <br><br>

            sxemasini ko'rsating.
            """,
        },
        {
            "title": "4. Hovli",
            "type": "example",
            "text": """
            Joylashtiring:

            <br><br>

            • family hovli;<br>
            • outdoor dining;<br>
            • gazebo;<br>
            • mangal;<br>
            • bolalar zonasi;<br>
            • yashil zona.
            """,
        },
        {
            "title": "5. Service",
            "type": "example",
            "text": """
            Belgilang:

            <br><br>

            • xo'jalik zona;<br>
            • ombor;<br>
            • chiqindi nuqtasi;<br>
            • service harakati.
            """,
        },
        {
            "title": "6. Relyef",
            "type": "example",
            "text": """
            Agar uchastkada nishab bo'lsa:

            <br><br>

            • yuqori tomon;<br>
            • past tomon;<br>
            • suv oqimi;<br>
            • platformalar

            <br><br>

            ni ko'rsating.
            """,
        },
        {
            "title": "7. Oqimlarni chizing",
            "type": "example",
            "text": """
            Genplan ustida:

            <br><br>

            FAMILY<br>
            GUEST<br>
            CAR<br>
            SERVICE

            <br><br>

            harakatini alohida ko'rsating.
            """,
        },
        {
            "title": "8. Yakuniy audit",
            "type": "warning",
            "text": """
            Kamida 10 ta savol bilan
            o'z genplaningizni tekshiring.

            <br><br>

            Har bir muammo uchun:

            <br><br>

            <b>MUAMMO → SABAB → YECHIM</b>

            <br><br>

            yozing.
            """,
        },
        {
            "title": "LEVEL 3 yakuni",
            "type": "highlight",
            "text": """
            LEVEL 3 davomida siz:

            <br><br>

            ✓ uchastkani o'qish;<br>
            ✓ shimol va quyosh;<br>
            ✓ ko'cha va kirish;<br>
            ✓ uy joylashtirish;<br>
            ✓ hovli zonalari;<br>
            ✓ parking;<br>
            ✓ relyef;<br>
            ✓ professional genplan

            <br><br>

            bo'yicha to'liq boshlang'ich
            site planning tizimini o'rgandingiz.

            <br><br>

            Keyingi qadam:
            <b>LEVEL 3 FINAL EXAM.</b>
            """,
        },
    ],
}


# ============================================================
# QUIZ
# ============================================================

LEVEL03_MODULE08_QUIZ = {
    "L03_M08_001": [
        {
            "code": "L03_Q106",
            "question": "Genplan faqat uy konturini ko'rsatadimi?",
            "explanation": (
                "Genplan uy, hovli, parking, kirish, landshaft va boshqa site elementlarini birlashtiradi."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L03_Q107",
            "question": "Genplanda shimol yo'nalishi muhimmi?",
            "explanation": (
                "Orientatsiya va quyosh tahlili uchun shimol yo'nalishi muhim."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L03_Q108",
            "question": "Professional genplan uchastkadagi elementlarni tizim sifatida ko'radimi?",
            "explanation": (
                "Bino, hovli, harakat va tabiiy sharoit o'zaro bog'liq."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L03_M08_002": [
        {
            "code": "L03_Q109",
            "question": "Genplanda avval katta zonalarni joylashtirish foydalimi?",
            "explanation": (
                "Avval funksional struktura, keyin mayda detallar ishlab chiqiladi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L03_Q110",
            "question": "Living va family hovli o'rtasidagi aloqa genplanda muhimmi?",
            "explanation": (
                "Ichki va tashqi yashash makonlarining aloqasi site planningning muhim qismidir."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L03_Q111",
            "question": "Parking butun uchastkani boshqarib qolishi yaxshi balansmi?",
            "explanation": (
                "Avtomobil zonasi family, yashil va piyoda zonalari bilan muvozanatda bo'lishi kerak."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
    ],

    "L03_M08_003": [
        {
            "code": "L03_Q112",
            "question": "Genplanda piyoda va avtomobil oqimlari tekshiriladimi?",
            "explanation": (
                "Tashqi circulation professional genplan auditining muhim qismidir."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L03_Q113",
            "question": "Mehmon private family hovlisini kesib o'tishi muammo bo'lishi mumkinmi?",
            "explanation": (
                "Bu privacy va circulation sifatiga ta'sir qilishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L03_Q114",
            "question": "Service harakati ham genplanda ko'rib chiqiladimi?",
            "explanation": (
                "Mahsulot, chiqindi va xo'jalik oqimlari ham site tizimining bir qismi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L03_M08_004": [
        {
            "code": "L03_Q115",
            "question": "Professional genplan auditida quyosh va privacy tekshiriladimi?",
            "explanation": (
                "Genplan funksional, ekologik va fazoviy omillar bilan birga baholanadi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L03_Q116",
            "question": "Relyef va suv oqimi genplan auditiga kiradimi?",
            "explanation": (
                "Balandlik va drenaj site planningning muhim qismi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L03_Q117",
            "question": "Har bir element uchun 'nega aynan shu joyda?' degan savol foydalimi?",
            "explanation": (
                "Bu loyiha qarorining mantiqiy asosini tekshiradi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L03_M08_005": [
        {
            "code": "L03_Q118",
            "question": "Yakuniy genplan case oldingi modullardagi bilimlarni birlashtiradimi?",
            "explanation": (
                "Site analysisdan relyef va circulationgacha barcha mavzular birlashtiriladi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L03_Q119",
            "question": "Yakuniy genplanda o'z qarorlaringizni asoslash kerakmi?",
            "explanation": (
                "Professional loyiha faqat chizma emas, qaror sababini tushuntirishni ham talab qiladi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L03_Q120",
            "question": "LEVEL 3 ning asosiy natijasi nima?",
            "explanation": (
                "Uchastkani professional tahlil qilib, uy va hovli uchun mantiqiy genplan yaratish."
            ),
            "options": [
                ("A", "Professional genplan fikrlashi", True),
                ("B", "Faqat fasad rangini tanlash", False),
            ],
        },
    ],
}


# ============================================================
# DATABASE SEED
# ============================================================

def seed_level03_module08():
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
        ) in LEVEL03_MODULE08_LESSONS:

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
