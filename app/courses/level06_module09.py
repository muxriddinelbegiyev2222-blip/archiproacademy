from database.database import get_connection


# ============================================================
# LEVEL 6
# MODULE 09 - MESH
# ============================================================

LEVEL06_MODULE09_LESSONS = [
    (
        "L06_M09",
        "L06_M09_001",
        "Mesh Tool va relyef tushunchasi",
        "theory",
        "Archicadda yer sathi va relyefni Mesh elementi orqali modellashtirish mantig'ini tushunish.",
        1,
        50,
        20,
    ),
    (
        "L06_M09",
        "L06_M09_002",
        "Mesh konturi va balandlik nuqtalari",
        "theory",
        "Yer modeli konturi va turli balandlik nuqtalarini tartibli tashkil qilish.",
        2,
        55,
        20,
    ),
    (
        "L06_M09",
        "L06_M09_003",
        "Nishabli uchastka modeli",
        "practice",
        "Turli balandliklardan foydalanib nishabli uchastkaning 3D relyef modelini yaratish.",
        3,
        60,
        20,
    ),
    (
        "L06_M09",
        "L06_M09_004",
        "Uy va relyef aloqasi",
        "practice",
        "Bino sathi, kirish, hovli va yer modeli o'rtasidagi vertikal munosabatni tahlil qilish.",
        4,
        65,
        20,
    ),
    (
        "L06_M09",
        "L06_M09_005",
        "Mesh professional audit",
        "practice",
        "Yer konturi, balandliklar, nishablar, bino aloqasi va 3D natijani kompleks tekshirish.",
        5,
        70,
        25,
    ),
]


# ============================================================
# CONTENT
# ============================================================

LEVEL06_MODULE09_CONTENT = {
    "L06_M09_001": [
        {
            "title": "Mesh Tool nima?",
            "type": "highlight",
            "text": """
            Mesh Tool —
            Archicadda yer sathi
            va relyefni

            <br><br>

            uch o'lchamli model
            sifatida yaratishga
            yordam beradigan vosita.
            """,
        },
        {
            "title": "Yer har doim tekis emas",
            "type": "normal",
            "text": """
            Real uchastkada
            yer sathi:

            <br><br>

            • tekis;<br>
            • qiya;<br>
            • notekis;<br>
            • turli balandlikli

            <br><br>

            bo'lishi mumkin.

            <br><br>

            Shuning uchun binoni
            faqat tekis platformada
            tasavvur qilish yetarli emas.
            """,
        },
        {
            "title": "Mesh va Genplan",
            "type": "highlight",
            "text": """
            Mesh modeli
            genplandagi ma'lumotni

            <br><br>

            3D makonda
            tushunishga yordam beradi.

            <br><br>

            Bu ayniqsa
            nishabli uchastkalarda
            muhim.
            """,
        },
        {
            "title": "Tasavvur qiling",
            "type": "example",
            "text": """
            Planda uchastka
            oddiy to'rtburchak.

            <br><br>

            Lekin ko'cha tomoni
            yuqoriroq,

            <br><br>

            hovlining orqa qismi
            esa pastroq.

            <br><br>

            Faqat 2D plan
            bu farqni to'liq
            his qildirmaydi.

            <br><br>

            3D relyef modeli
            vaziyatni ancha
            tushunarli qiladi.
            """,
        },
        {
            "title": "Mesh faqat dekor emas",
            "type": "warning",
            "text": """
            Meshni faqat
            renderda yer ko'rsatish
            uchun ishlatish

            <br><br>

            uning imkoniyatini
            juda tor tushunishdir.

            <br><br>

            U bino va uchastkaning
            vertikal munosabatini
            tahlil qilishga ham yordam beradi.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Oddiy uchastka chizing.

            <br><br>

            Avval uni
            butunlay tekis Mesh
            sifatida yarating.

            <br><br>

            Keyin 3Dda ko'rib,
            yer modelining
            bino loyihasidagi
            vazifasini tushuntiring.
            """,
        },
    ],

    "L06_M09_002": [
        {
            "title": "Mesh konturi",
            "type": "highlight",
            "text": """
            Meshning tashqi konturi
            modellashtirilayotgan
            yer hududining

            <br><br>

            chegarasini belgilaydi.
            """,
        },
        {
            "title": "Kontur uchastkaga mos bo'lsin",
            "type": "normal",
            "text": """
            Yer modeli konturi
            tasodifiy shaklda
            chizilmasligi kerak.

            <br><br>

            U loyiha uchun
            kerakli hududni
            mantiqan qamrab olishi kerak.
            """,
        },
        {
            "title": "Balandlik nuqtalari",
            "type": "highlight",
            "text": """
            Relyefni yaratishda
            turli nuqtalarga

            <br><br>

            turli balandlik qiymatlari
            berish mumkin.

            <br><br>

            Natijada tekis sath
            o'rniga nishabli
            yoki notekis yer
            hosil bo'ladi.
            """,
        },
        {
            "title": "Ma'lumot qayerdan keladi?",
            "type": "normal",
            "text": """
            Real loyihada
            yer balandliklari

            <br><br>

            tegishli geodezik
            yoki topografik
            ma'lumotlardan olinadi.

            <br><br>

            Relyefni ko'z bilan
            taxmin qilib yaratish
            professional o'lchov
            o'rnini bosa olmaydi.
            """,
        },
        {
            "title": "Ortiqcha nuqta",
            "type": "warning",
            "text": """
            Keraksiz juda ko'p
            balandlik nuqtalari

            <br><br>

            Meshni boshqarishni
            murakkablashtirishi mumkin.

            <br><br>

            Faqat model uchun
            zarur geometriyani yarating.
            """,
        },
        {
            "title": "Kam nuqta ham muammo",
            "type": "normal",
            "text": """
            Aksincha,
            relyef murakkab bo'lsa

            <br><br>

            juda kam nuqta
            yer shaklini
            noto'g'ri soddalashtirishi mumkin.

            <br><br>

            Maqsad —
            yetarli aniqlik
            va boshqaruv o'rtasida balans.
            """,
        },
        {
            "title": "3D bilan tekshiring",
            "type": "highlight",
            "text": """
            Balandlik qiymatlarini
            kiritgandan keyin

            <br><br>

            faqat Floor Planga emas,
            3D ko'rinishga ham qarang.

            <br><br>

            Noto'g'ri bitta nuqta
            keskin yer cho'qqisi
            yoki chuqurlik
            yaratishi mumkin.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            To'rtburchak Mesh yarating.

            <br><br>

            Uning turli qismlariga
            turli balandlik qiymatlari bering.

            <br><br>

            Keyin 3Dda
            qaysi yo'nalishda
            nishab hosil bo'lganini
            tushuntiring.
            """,
        },
    ],

    "L06_M09_003": [
        {
            "title": "Nishab nima?",
            "type": "highlight",
            "text": """
            Nishab —
            yer sathining
            bir balandlikdan

            <br><br>

            boshqa balandlikka
            o'zgarishi natijasida
            hosil bo'ladigan qiyalik.
            """,
        },
        {
            "title": "Nishab yo'nalishi",
            "type": "normal",
            "text": """
            Relyefni tahlil qilganda
            faqat balandlik farqiga emas,

            <br><br>

            yerning qaysi tomonga
            pasayib yoki ko'tarilib
            borayotganiga ham qarang.
            """,
        },
        {
            "title": "Tasavvur qiling",
            "type": "example",
            "text": """
            Uchastkaning
            ko'cha tomoni baland,

            <br><br>

            orqa hovli
            esa past.

            <br><br>

            Bu:

            • kirish yo'liga;<br>
            • uy sathiga;<br>
            • hovli harakatiga;<br>
            • landshaft yechimiga

            <br><br>

            ta'sir qilishi mumkin.
            """,
        },
        {
            "title": "Keskin sakrashlardan ehtiyot bo'ling",
            "type": "warning",
            "text": """
            Qo'shni nuqtalarning
            balandliklari noto'g'ri
            kiritilsa,

            <br><br>

            real relyefda bo'lmagan
            keskin qiya yuza
            paydo bo'lishi mumkin.
            """,
        },
        {
            "title": "Section bilan tahlil",
            "type": "highlight",
            "text": """
            Relyefni Sectionda
            tekshirish juda foydali.

            <br><br>

            Section orqali:

            • yer profili;<br>
            • bino sathi;<br>
            • yuqori va past zonalar;<br>
            • vertikal farqlar

            <br><br>

            aniqroq ko'rinadi.
            """,
        },
        {
            "title": "Tekislashtirishni darhol boshlamang",
            "type": "normal",
            "text": """
            Nishabli yer ko'rsangiz
            hamma joyni darhol
            bitta sathga keltirish

            <br><br>

            yagona loyiha yechimi emas.

            <br><br>

            Avval tabiiy relyef
            va bino o'rtasidagi
            munosabatni tahlil qiling.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Nishabli Mesh yarating.

            <br><br>

            So'ng uchastka bo'ylab
            bitta Section oling.

            <br><br>

            Yuqori va past
            nuqtalarni belgilang

            <br><br>

            va bino uchun
            qaysi zona qulayroq
            ekanini tahlil qiling.
            """,
        },
    ],

    "L06_M09_004": [
        {
            "title": "Uy va yer birga ishlaydi",
            "type": "highlight",
            "text": """
            Uy modelini
            relyefdan alohida
            loyihalash to'g'ri emas.

            <br><br>

            Bino sathi
            uchastkaning real
            vertikal holati bilan
            bog'liq.
            """,
        },
        {
            "title": "0.000 va yer sathi",
            "type": "normal",
            "text": """
            Binodagi loyiha sathlari
            va tashqi yer sathi

            <br><br>

            bir-biri bilan
            mantiqiy bog'lanishi kerak.

            <br><br>

            Ularning qiymatlarini
            tasodifiy aralashtirmang.
            """,
        },
        {
            "title": "Kirish zonasi",
            "type": "highlight",
            "text": """
            Uyga kirish
            real yer sathidan
            juda yuqori yoki past
            bo'lib qolishi mumkin.

            <br><br>

            Shu sabab:

            • entrance;<br>
            • porch;<br>
            • steps;<br>
            • driveway;<br>
            • pedestrian path

            <br><br>

            relyef bilan birga
            tahlil qilinadi.
            """,
        },
        {
            "title": "Avtomobil kirishi",
            "type": "normal",
            "text": """
            Nishabli uchastkada
            avtomobil yo'li ham

            <br><br>

            yer balandliklariga
            bevosita bog'liq.

            <br><br>

            Parking yoki carportni
            faqat plandagi bo'sh joyga
            qarab joylashtirmang.
            """,
        },
        {
            "title": "Cut va Fill tushunchasi",
            "type": "highlight",
            "text": """
            Bino va hovli sathini
            relyefga moslashtirishda

            <br><br>

            ayrim joylarda
            yer qazilishi,

            <br><br>

            ayrim joylarda esa
            yer ko'tarilishi
            talab qilinishi mumkin.

            <br><br>

            Bu yer ishlari
            cut va fill mantig'i
            bilan bog'liq.
            """,
        },
        {
            "title": "Muhim eslatma",
            "type": "warning",
            "text": """
            Ushbu dars
            aniq yer ishlari hajmini
            avtomatik hisoblash
            metodikasi emas.

            <br><br>

            Bu bosqichda
            bino va relyefning
            fazoviy munosabatini
            tushunamiz.
            """,
        },
        {
            "title": "Tasavvur qiling",
            "type": "example",
            "text": """
            Uy nishabning
            eng yuqori joyiga
            joylashtirildi.

            <br><br>

            Natijada:

            • kirish juda baland;<br>
            • hovli bilan katta farq paydo bo'ldi;<br>
            • avtomobil kirishi murakkablashdi.

            <br><br>

            Muammo faqat Meshda emas,
            uy joylashuv qarorida ham.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Nishabli uchastkaga
            kichik uy joylashtiring.

            <br><br>

            Keyin:

            • entrance;<br>
            • driveway;<br>
            • terrace;<br>
            • hovli

            <br><br>

            sathlarini 3D va
            Section orqali tekshiring.
            """,
        },
    ],

    "L06_M09_005": [
        {
            "title": "Mesh professional audit",
            "type": "highlight",
            "text": """
            Endi yer modelini
            faqat yashil 3D yuza
            sifatida emas,

            <br><br>

            butun loyiha uchun
            muhim vertikal baza
            sifatida tekshiramiz.
            """,
        },
        {
            "title": "1. Kontur",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • Mesh kerakli hududni qamrab olganmi?<br>
            • tashqi kontur mantiqiymi?<br>
            • keraksiz qo'shimcha geometriya yo'qmi?
            """,
        },
        {
            "title": "2. Balandliklar",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • balandlik nuqtalari mantiqiymi?<br>
            • tasodifiy juda baland yoki past nuqta yo'qmi?<br>
            • 3D relyef real ma'lumotga mosmi?
            """,
        },
        {
            "title": "3. Nishablar",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • qiyalik yo'nalishi tushunarlimi?<br>
            • keskin sun'iy sakrashlar yo'qmi?<br>
            • Sectionda relyef to'g'ri ko'rinadimi?
            """,
        },
        {
            "title": "4. Uy va Mesh",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • bino yerga mantiqiy o'tirganmi?<br>
            • bino havoda qolmaganmi?<br>
            • yer bino ichiga noto'g'ri kirib ketmaganmi?<br>
            • kirish sathi tushunarlimi?
            """,
        },
        {
            "title": "5. Hovli va circulation",
            "type": "example",
            "text": """
            Tekshiring:

            <br><br>

            • pedestrian yo'llar relyefga mosmi?<br>
            • avtomobil kirishi mantiqiymi?<br>
            • terrace va hovli sathlari bir-biriga mosmi?
            """,
        },
        {
            "title": "6. Cut / Fill mantig'i",
            "type": "normal",
            "text": """
            Tekshiring:

            <br><br>

            • binoni joylashtirish uchun qayerda yer o'zgarishi kerak?<br>
            • ortiqcha relyef buzilishi yaratilmaganmi?<br>
            • bino tabiiy yer bilan qanday munosabatda?
            """,
        },
        {
            "title": "Xatoni toping",
            "type": "warning",
            "text": """
            Uy modeli yaxshi.

            <br><br>

            Mesh ham mavjud.

            <br><br>

            Lekin:

            • entrance yer sathidan juda baland;<br>
            • driveway keskin nishabda;<br>
            • terrace yer ichiga kirib ketgan;<br>
            • bitta Mesh nuqtasi noto'g'ri balandlikda;<br>
            • Sectionda uy va yer munosabati buzilgan.

            <br><br>

            Muammo:

            <br><br>

            bino va relyef
            alohida modellashtirilgan,
            lekin birgalikda
            audit qilinmagan.
            """,
        },
        {
            "title": "Professional checklist",
            "type": "example",
            "text": """
            Meshni tekshiring:

            <br><br>

            <b>1.</b> Kontur to'g'rimi?<br><br>
            <b>2.</b> Balandliklar mantiqiymi?<br><br>
            <b>3.</b> Nishab yo'nalishi to'g'rimi?<br><br>
            <b>4.</b> Bino relyefga to'g'ri joylashganmi?<br><br>
            <b>5.</b> Entrance va hovli sathlari mosmi?<br><br>
            <b>6.</b> Driveway va piyoda yo'llari tekshirildimi?<br><br>
            <b>7.</b> Plan, 3D va Section birgalikda audit qilindimi?
            """,
        },
        {
            "title": "Modul yakuni",
            "type": "highlight",
            "text": """
            Siz endi:

            <br><br>

            ✓ Mesh Tool vazifasini tushunasiz;<br>
            ✓ yer konturini yaratasiz;<br>
            ✓ turli balandliklar bilan ishlaysiz;<br>
            ✓ nishabli relyefni modellashtirasiz;<br>
            ✓ uy va yer sathini bog'laysiz;<br>
            ✓ cut/fill mantig'ini tushunasiz;<br>
            ✓ professional Mesh auditini bajarasiz.

            <br><br>

            Keyingi modul:
            <b>Zones.</b>
            """,
        },
    ],
}


# ============================================================
# QUIZ
# Q121-Q135
# ============================================================

LEVEL06_MODULE09_QUIZ = {
    "L06_M09_001": [
        {
            "code": "L06_Q121",
            "question": "Mesh Tool Archicadda yer sathi va relyefni 3D modellashtirish uchun ishlatilishi mumkinmi?",
            "explanation": (
                "Mesh yer geometriyasini uch o'lchamli model sifatida ifodalashga yordam beradi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L06_Q122",
            "question": "Real uchastka har doim mutlaqo tekis bo'ladimi?",
            "explanation": (
                "Uchastkalar tekis, nishabli yoki murakkab relyefga ega bo'lishi mumkin."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L06_Q123",
            "question": "Mesh bino va uchastkaning vertikal munosabatini tahlil qilishga yordam beradimi?",
            "explanation": (
                "3D yer modeli binoning real relyefga qanday joylashishini ko'rishga yordam beradi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L06_M09_002": [
        {
            "code": "L06_Q124",
            "question": "Meshdagi turli nuqtalarga turli balandlik qiymatlari berish orqali relyef yaratish mumkinmi?",
            "explanation": (
                "Turli balandliklar Mesh yuzasida nishab va relyef shakllarini hosil qiladi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L06_Q125",
            "question": "Real loyiha relyefini faqat ko'z bilan taxmin qilish geodezik ma'lumot o'rnini bosadimi?",
            "explanation": (
                "Professional loyiha uchun tegishli o'lchov va topografik ma'lumotlar talab qilinishi mumkin."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L06_Q126",
            "question": "Meshga noto'g'ri balandlik berilgan bitta nuqta 3D relyefni buzishi mumkinmi?",
            "explanation": (
                "Noto'g'ri nuqta keskin cho'qqi yoki chuqurlik kabi xato geometriya yaratishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L06_M09_003": [
        {
            "code": "L06_Q127",
            "question": "Nishab yer sathining balandligi yo'nalish bo'yicha o'zgarishi bilan bog'liqmi?",
            "explanation": (
                "Nishab baland va past nuqtalar orasidagi yer qiyaligini ifodalaydi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L06_Q128",
            "question": "Relyefni Section orqali tekshirish foydalimi?",
            "explanation": (
                "Section yer profili va bino sathlari o'rtasidagi vertikal munosabatni ko'rsatadi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L06_Q129",
            "question": "Nishabli uchastkani har doim to'liq tekis qilish yagona to'g'ri arxitektura yechimimi?",
            "explanation": (
                "Avval tabiiy relyef va bino o'rtasidagi loyiha munosabati tahlil qilinadi."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
    ],

    "L06_M09_004": [
        {
            "code": "L06_Q130",
            "question": "Bino sathi va tashqi yer sathi bir-biri bilan mantiqiy bog'liq bo'lishi kerakmi?",
            "explanation": (
                "Entrance, hovli, terrace va boshqa elementlar bino hamda relyef sathlariga bog'liq."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L06_Q131",
            "question": "Nishabli uchastkada avtomobil kirishini faqat 2D plandagi joyga qarab hal qilish yetarlimi?",
            "explanation": (
                "Drivewayning vertikal holati va yer nishabi ham tekshirilishi kerak."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L06_Q132",
            "question": "Cut va fill tushunchasi yerning ayrim joylarini qazish yoki ko'tarish mantig'i bilan bog'liqmi?",
            "explanation": (
                "Bino va hovlini relyefga moslashtirishda yer sathini mahalliy o'zgartirish talab qilinishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L06_M09_005": [
        {
            "code": "L06_Q133",
            "question": "Mesh auditida bino va yerning o'zaro joylashuvi tekshiriladimi?",
            "explanation": (
                "Bino yerga mantiqiy o'tirishi va vertikal sathlar bir-biriga mos bo'lishi kerak."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L06_Q134",
            "question": "Mesh 3Dda ko'rinsa Plan va Sectionda tekshirmasa ham bo'ladimi?",
            "explanation": (
                "Plan, 3D va Section relyef haqida turli ma'lumotlarni beradi va birgalikda audit qilinadi."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L06_Q135",
            "question": "Mesh bilan professional ishlashdagi to'g'ri workflow qaysi?",
            "explanation": (
                "Avval yer konturi va balandliklar yaratiladi, keyin relyef, bino aloqasi va turli ko'rinishlarda natija tekshiriladi."
            ),
            "options": [
                (
                    "A",
                    "Kontur → balandliklar → relyef → bino aloqasi → Plan/3D/Section audit",
                    True,
                ),
                (
                    "B",
                    "Tasodifiy notekis Mesh yaratib uy ostiga qo'yish",
                    False,
                ),
            ],
        },
    ],
}


# ============================================================
# DATABASE SEED
# ============================================================

def seed_level06_module09():
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
        ) in LEVEL06_MODULE09_LESSONS:

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
