from database.database import get_connection


# ============================================================
# LEVEL 2
# MODULE 07 - BOLALAR XONASI
# ============================================================

LEVEL02_MODULE07_LESSONS = [
    (
        "L02_M07",
        "L02_M07_001",
        "Bolalar xonasi funksiyalari",
        "theory",
        "Bolalar xonasidagi uyqu, o'qish, o'yin va saqlash zonalarini tushunish.",
        1,
        35,
        20,
    ),
    (
        "L02_M07",
        "L02_M07_002",
        "Yoshga mos rejalashtirish",
        "theory",
        "Bolaning yoshi o'zgarganda xona funksiyalari qanday o'zgarishini tushunish.",
        2,
        35,
        20,
    ),
    (
        "L02_M07",
        "L02_M07_003",
        "Xavfsizlik va ergonomika",
        "practice",
        "Mebel, deraza, eshik va harakat zonalarini xavfsiz tashkil qilish.",
        3,
        35,
        20,
    ),
    (
        "L02_M07",
        "L02_M07_004",
        "Study, play va storage zonalari",
        "practice",
        "O'qish, o'yin va saqlash zonalarini bir-biriga xalaqit bermaydigan qilib joylashtirish.",
        4,
        35,
        20,
    ),
    (
        "L02_M07",
        "L02_M07_005",
        "Bolalar xonasi auditi",
        "practice",
        "Bolalar xonasini yosh, xavfsizlik, ergonomika va kelajakdagi o'zgarishlar bo'yicha tekshirish.",
        5,
        40,
        25,
    ),
]


# ============================================================
# CONTENT
# ============================================================

LEVEL02_MODULE07_CONTENT = {
    "L02_M07_001": [
        {
            "title": "Bolalar xonasi bitta funksiyali emas",
            "type": "highlight",
            "text": """
            Bolalar xonasi
            faqat uxlash uchun
            ishlatilmaydi.

            <br><br>

            Bu makonda:

            <br><br>

            • uyqu;<br>
            • o'qish;<br>
            • o'yin;<br>
            • kiyim saqlash;<br>
            • shaxsiy buyumlar;<br>
            • dam olish

            <br><br>

            birgalikda mavjud bo'lishi mumkin.
            """,
        },
        {
            "title": "4 ta asosiy zona",
            "type": "normal",
            "text": """
            Boshlang'ich rejalashtirishda
            xonani 4 asosiy zona sifatida
            tasavvur qilish mumkin:

            <br><br>

            <b>1. Sleep</b><br>
            <b>2. Study</b><br>
            <b>3. Play</b><br>
            <b>4. Storage</b>
            """,
        },
        {
            "title": "Zonalar bir-biriga xalaqit bermasin",
            "type": "highlight",
            "text": """
            Har bir zona
            alohida xona bo'lishi shart emas.

            <br><br>

            Lekin ularning
            foydalanish mantig'i
            bir-birini buzmasligi kerak.
            """,
        },
        {
            "title": "Tasavvur qiling",
            "type": "example",
            "text": """
            Study table
            xonaning eng qorong'i burchagida.

            <br><br>

            O'yin zonasi esa
            eshik oldidagi
            asosiy circulation yo'lida.

            <br><br>

            Mebel sig'gan,
            lekin funksional zoning yaxshi emas.
            """,
        },
        {
            "title": "Mini-vazifa",
            "type": "example",
            "text": """
            Oddiy bolalar xonasi chizing.

            <br><br>

            Rang yoki belgilar bilan ajrating:

            <br><br>

            SLEEP<br>
            STUDY<br>
            PLAY<br>
            STORAGE
            """,
        },
    ],

    "L02_M07_002": [
        {
            "title": "Bola ulg'ayadi",
            "type": "highlight",
            "text": """
            Bolalar xonasining
            eng muhim xususiyatlaridan biri —

            <br><br>

            foydalanuvchi tez o'zgaradi.

            <br><br>

            4 yoshli bola uchun
            yaxshi xona

            <br><br>

            14 yoshli bola uchun
            o'sha holatda qulay bo'lmasligi mumkin.
            """,
        },
        {
            "title": "Maktabgacha yosh",
            "type": "normal",
            "text": """
            Kichik yoshda
            o'yin zonasi
            muhimroq bo'lishi mumkin.

            <br><br>

            Ochiq pol maydoni
            va xavfsiz circulation
            alohida ahamiyat kasb etadi.
            """,
        },
        {
            "title": "Maktab yoshi",
            "type": "normal",
            "text": """
            Maktab yoshida:

            <br><br>

            • study desk;<br>
            • kitoblar;<br>
            • storage;<br>
            • tinch o'qish zonasi

            <br><br>

            ko'proq ahamiyatga ega bo'ladi.
            """,
        },
        {
            "title": "O'smirlik davri",
            "type": "normal",
            "text": """
            O'smir uchun
            xonada privacy,
            study
            va shaxsiy storage
            yanada muhimlashishi mumkin.
            """,
        },
        {
            "title": "Moslashuvchanlik",
            "type": "highlight",
            "text": """
            Yaxshi reja
            har yosh o'zgarishida
            butun xonani buzib
            qayta qurishni talab qilmasligi ma'qul.

            <br><br>

            Mebel va zonalarni
            keyinchalik o'zgartirish imkonini
            oldindan tasavvur qiling.
            """,
        },
        {
            "title": "Tipik xato",
            "type": "warning",
            "text": """
            Xona faqat
            kichik bola uchun
            juda tematik va qattiq
            geometriyada rejalashtirilgan.

            <br><br>

            Bir necha yildan keyin
            study zona uchun
            joy topilmayapti.

            <br><br>

            Demak kelajakdagi
            o'zgarish hisobga olinmagan.
            """,
        },
        {
            "title": "Mini-vazifa",
            "type": "example",
            "text": """
            Bir xil xona uchun
            3 holatni tasavvur qiling:

            <br><br>

            • 5 yosh;<br>
            • 10 yosh;<br>
            • 15 yosh.

            <br><br>

            Qaysi mebel va zonalar
            o'zgarishini yozing.
            """,
        },
    ],

    "L02_M07_003": [
        {
            "title": "Xavfsizlik birinchi o'rinda",
            "type": "highlight",
            "text": """
            Bolalar xonasida
            estetika va mebeldan oldin
            xavfsizlik ham tekshiriladi.
            """,
        },
        {
            "title": "Circulationni ochiq saqlang",
            "type": "normal",
            "text": """
            Xona ichida
            eshikdan krovat,
            study
            va storage zonalariga

            <br><br>

            tushunarli va ochiq
            harakat yo'li bo'lishi kerak.
            """,
        },
        {
            "title": "O'tkir konfliktlar",
            "type": "warning",
            "text": """
            Mebel joylashuvida
            bolalar faol harakat qilishini
            hisobga oling.

            <br><br>

            Tor o'tish,
            noqulay chiqib turgan element
            yoki bir-biriga juda yaqin mebel
            xavfni oshirishi mumkin.
            """,
        },
        {
            "title": "Deraza bilan aloqa",
            "type": "normal",
            "text": """
            Deraza oldidagi
            mebel joylashuvi
            alohida o'ylanadi.

            <br><br>

            Study zonasi
            tabiiy yorug'likdan
            foydalanishi mumkin,

            <br><br>

            lekin derazadan
            xavfsiz foydalanish
            ham hisobga olinishi kerak.
            """,
        },
        {
            "title": "Door opening",
            "type": "example",
            "text": """
            Xona eshigi ochilganda
            study deskga urilsa,

            <br><br>

            bola stulda o'tirganida
            konflikt paydo bo'lishi mumkin.

            <br><br>

            Eshik swingini
            mebel bilan birga tekshiring.
            """,
        },
        {
            "title": "Bunk bed va yuqori elementlar",
            "type": "warning",
            "text": """
            Ikki qavatli krovat
            yoki boshqa baland mebel
            ishlatilsa,

            <br><br>

            ularni oddiy mebeldek
            faqat planda ko'rish yetarli emas.

            <br><br>

            Foydalanish xavfsizligi
            va real sharoit alohida
            baholanishi kerak.
            """,
        },
        {
            "title": "Mini-vazifa",
            "type": "example",
            "text": """
            Bolalar xonasi planida
            3 ta ehtimoliy xavfni toping.

            <br><br>

            Masalan:

            • door conflict;<br>
            • tor circulation;<br>
            • noto'g'ri mebel joylashuvi.
            """,
        },
    ],

    "L02_M07_004": [
        {
            "title": "Study zone",
            "type": "highlight",
            "text": """
            Study zona
            faqat stol qo'yilgan burchak emas.

            <br><br>

            Unda:

            <br><br>

            • o'tirish;<br>
            • yozish;<br>
            • kitob saqlash;<br>
            • kompyuter ishlatish

            <br><br>

            kabi vazifalar bo'lishi mumkin.
            """,
        },
        {
            "title": "Study va play aloqasi",
            "type": "normal",
            "text": """
            Study va play
            bir xonada bo'lishi mumkin,

            <br><br>

            lekin o'qish paytida
            o'yin zonasi
            ishni doimiy buzmasligi kerak.
            """,
        },
        {
            "title": "Play zone",
            "type": "normal",
            "text": """
            Kichik yoshdagi bola uchun
            polning ochiq qismi
            haqiqiy foydalanish maydoni.

            <br><br>

            Xonani mebel bilan
            to'liq to'ldirib yubormang.
            """,
        },
        {
            "title": "Storage",
            "type": "highlight",
            "text": """
            Bolalar xonasida
            storage juda muhim.

            <br><br>

            Alohida joy kerak bo'lishi mumkin:

            <br><br>

            • kiyimlar;<br>
            • kitoblar;<br>
            • o'yinchoqlar;<br>
            • maktab buyumlari;<br>
            • shaxsiy predmetlar.
            """,
        },
        {
            "title": "Foydalanuvchiga mos storage",
            "type": "normal",
            "text": """
            Tez-tez ishlatiladigan
            buyumlar

            <br><br>

            foydalanuvchi uchun
            mantiqiy va qulay joyda
            bo'lishi kerak.
            """,
        },
        {
            "title": "Storage bilan xonani bo'g'mang",
            "type": "warning",
            "text": """
            Juda ko'p shkaf
            xona maydonini
            olib qo'yishi mumkin.

            <br><br>

            Storage va ochiq maydon
            o'rtasida balans kerak.
            """,
        },
        {
            "title": "Mini-vazifa",
            "type": "example",
            "text": """
            Bitta plan chizing.

            <br><br>

            Belgilang:

            <br><br>

            • study desk;<br>
            • book storage;<br>
            • toy storage;<br>
            • play zone;<br>
            • sleeping zone.

            <br><br>

            Har bir zonaga
            alohida kirish mumkinmi?
            """,
        },
    ],

    "L02_M07_005": [
        {
            "title": "Bolalar xonasi auditi",
            "type": "highlight",
            "text": """
            Endi bolalar xonasini
            faqat chiroyli interyer sifatida emas,

            <br><br>

            o'zgarib boradigan
            real yashash makoni sifatida
            tekshiramiz.
            """,
        },
        {
            "title": "1. Yosh",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • bola necha yoshda?<br>
            • hozir qanday faoliyatlar kerak?<br>
            • 3-5 yildan keyin nimalar o'zgaradi?
            """,
        },
        {
            "title": "2. Funksiyalar",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • sleep zona bormi?<br>
            • study zona bormi?<br>
            • play yoki erkin zona bormi?<br>
            • storage yetarlimi?
            """,
        },
        {
            "title": "3. Xavfsizlik",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • circulation ochiqmi?<br>
            • eshik mebelga urilmayaptimi?<br>
            • deraza zonasi mantiqiymi?<br>
            • noqulay chiqib turgan elementlar yo'qmi?
            """,
        },
        {
            "title": "4. Moslashuvchanlik",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • mebelni keyin o'zgartirish mumkinmi?<br>
            • katta study desk uchun joy bo'ladimi?<br>
            • storage tizimi kengayishi mumkinmi?
            """,
        },
        {
            "title": "Xatoni toping",
            "type": "warning",
            "text": """
            Bolalar xonasi juda chiroyli.

            <br><br>

            Krovat,
            shkaf,
            katta o'yinchoq javoni
            va dekorlar ko'p.

            <br><br>

            Lekin:

            <br><br>

            • study desk uchun joy yo'q;<br>
            • polning ochiq qismi juda kichik;<br>
            • eshik shkafga uriladi.

            <br><br>

            Demak xona vizual jihatdan
            yaxshi ko'rinsa ham,
            funksional emas.
            """,
        },
        {
            "title": "Professional checklist",
            "type": "example",
            "text": """
            Bolalar xonasini tekshiring:

            <br><br>

            <b>1.</b> Yoshga mosmi?<br><br>
            <b>2.</b> Sleep zona qulaymi?<br><br>
            <b>3.</b> Study zona mantiqiymi?<br><br>
            <b>4.</b> Play uchun ochiq joy bormi?<br><br>
            <b>5.</b> Storage yetarlimi?<br><br>
            <b>6.</b> Circulation xavfsizmi?<br><br>
            <b>7.</b> Kelajakda o'zgartirish mumkinmi?
            """,
        },
        {
            "title": "Modul yakuni",
            "type": "highlight",
            "text": """
            Siz endi:

            <br><br>

            ✓ bolalar xonasini zonalaysiz;<br>
            ✓ yoshga mos reja tuzasiz;<br>
            ✓ xavfsizlikni tekshirasiz;<br>
            ✓ study va play zonalarini ajratasiz;<br>
            ✓ storage tizimini rejalashtirasiz;<br>
            ✓ kelajakdagi o'zgarishni hisobga olasiz;<br>
            ✓ bolalar xonasini audit qilasiz.

            <br><br>

            Keyingi modul:
            <b>Sanuzel ergonomikasi.</b>
            """,
        },
    ],
}


# ============================================================
# QUIZ
# Q091-Q105 KODLARI SAQLANADI
# ============================================================

LEVEL02_MODULE07_QUIZ = {
    "L02_M07_001": [
        {
            "code": "L02_Q091",
            "question": "Bolalar xonasi faqat uxlash uchun mo'ljallangan makonmi?",
            "explanation": (
                "Bolalar xonasida uyqu, o'qish, o'yin va saqlash kabi bir nechta funksiyalar mavjud bo'lishi mumkin."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L02_Q092",
            "question": "Sleep, Study, Play va Storage bolalar xonasining asosiy zonalari bo'lishi mumkinmi?",
            "explanation": (
                "Bu zonalar xona funksiyalarini tushunishga yordam beradi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L02_Q093",
            "question": "Bolalar xonasida circulationni tekshirish kerakmi?",
            "explanation": (
                "Odam harakati va mebel o'rtasidagi konfliktlar xona qulayligiga ta'sir qiladi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L02_M07_002": [
        {
            "code": "L02_Q094",
            "question": "Bolalar xonasi bolaning yoshi o'zgarganda o'zgarishi mumkinmi?",
            "explanation": (
                "Bola ulg'aygani sari o'yin, o'qish, privacy va storage ehtiyojlari o'zgaradi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L02_Q095",
            "question": "5 yoshli va 15 yoshli bola uchun xona funksiyalari mutlaqo bir xil bo'lishi shartmi?",
            "explanation": (
                "Yoshga qarab study, play, privacy va storage ehtiyojlari farq qiladi."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L02_Q096",
            "question": "Xonani keyinchalik moslashtirish imkonini o'ylash foydalimi?",
            "explanation": (
                "Moslashuvchan reja bolaning ulg'ayishiga mos o'zgarishni osonlashtiradi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L02_M07_003": [
        {
            "code": "L02_Q097",
            "question": "Bolalar xonasida xavfsizlik rejalashtirishning muhim qismimi?",
            "explanation": (
                "Mebel, circulation, eshik va deraza aloqalari xavfsizlikka ta'sir qiladi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L02_Q098",
            "question": "Eshik study desk bilan konflikt qilishi mumkinmi?",
            "explanation": (
                "Door swing noto'g'ri joylashtirilgan mebel bilan to'qnashishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L02_Q099",
            "question": "Bolalar xonasini mebel bilan maksimal to'ldirish har doim yaxshi yechimmi?",
            "explanation": (
                "Ortiqcha mebel circulation va o'yin uchun ochiq maydonni kamaytirishi mumkin."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
    ],

    "L02_M07_004": [
        {
            "code": "L02_Q100",
            "question": "Study zona faqat stol konturidan iboratmi?",
            "explanation": (
                "Unda o'tirish, yozish, kitob saqlash va boshqa foydalanish maydonlari ham hisobga olinadi."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L02_Q101",
            "question": "Kichik yoshdagi bola uchun ochiq play zona foydali bo'lishi mumkinmi?",
            "explanation": (
                "Ochiq pol maydoni o'yin va faol harakat uchun ishlatilishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L02_Q102",
            "question": "Storage tizimi kiyim, kitob va o'yinchoqlarni tartibli saqlashga yordam beradimi?",
            "explanation": (
                "Turli buyumlar uchun mantiqiy storage xona foydalanishini yaxshilaydi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L02_M07_005": [
        {
            "code": "L02_Q103",
            "question": "Bolalar xonasi auditida bolaning yoshi hisobga olinadimi?",
            "explanation": (
                "Yosh xonaning funksiyalari va kelajakdagi o'zgarishlariga ta'sir qiladi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L02_Q104",
            "question": "Chiroyli xona avtomatik ravishda funksional va xavfsiz bo'ladimi?",
            "explanation": (
                "Estetikadan tashqari zoning, circulation, xavfsizlik va ergonomika ham tekshiriladi."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L02_Q105",
            "question": "Bolalar xonasini loyihalashdagi to'g'ri yondashuv qaysi?",
            "explanation": (
                "Yosh, funksiyalar, xavfsizlik va moslashuvchanlik birgalikda tahlil qilinadi."
            ),
            "options": [
                (
                    "A",
                    "Yosh → zoning → xavfsizlik → ergonomika → audit",
                    True,
                ),
                (
                    "B",
                    "Faqat dekor va rang tanlash",
                    False,
                ),
            ],
        },
    ],
}


# ============================================================
# DATABASE SEED
# ============================================================

def seed_level02_module07():
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
        ) in LEVEL02_MODULE07_LESSONS:

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
