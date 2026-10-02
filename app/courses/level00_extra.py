from database.database import get_connection


# ============================================================
# LEVEL 0 - QO'SHIMCHA DARSLAR
# ============================================================

LEVEL00_EXTRA_LESSONS = [
    # --------------------------------------------------------
    # MODULE 04 - BINO ELEMENTLARI
    # --------------------------------------------------------
    (
        "L00_M04",
        "L00_M04_001",
        "Fundament nima?",
        "theory",
        "Uy yukini yerga uzatadigan asosiy konstruktiv qism.",
        1,
        25,
        15,
    ),
    (
        "L00_M04",
        "L00_M04_002",
        "Devor nima va turlari",
        "theory",
        "Tashqi, ichki va yuk ko'taruvchi devorlarni tushunish.",
        2,
        30,
        15,
    ),
    (
        "L00_M04",
        "L00_M04_003",
        "Ustun va rigel nima?",
        "theory",
        "Karkasli binodagi ustun va rigel vazifasi.",
        3,
        30,
        15,
    ),
    (
        "L00_M04",
        "L00_M04_004",
        "Pol, plita va shift",
        "theory",
        "Qavatning gorizontal elementlarini tushunish.",
        4,
        30,
        15,
    ),
    (
        "L00_M04",
        "L00_M04_005",
        "Tom nima va qanday ishlaydi?",
        "theory",
        "Tomning vazifasi va asosiy shakllari.",
        5,
        30,
        15,
    ),
    (
        "L00_M04",
        "L00_M04_006",
        "Eshik va deraza",
        "theory",
        "Eshik va derazaning rejalashtirishdagi ahamiyati.",
        6,
        30,
        15,
    ),

    # --------------------------------------------------------
    # MODULE 05 - BIRINCHI ARXITEKTURA TAHLILI
    # --------------------------------------------------------
    (
        "L00_M05",
        "L00_M05_001",
        "Yaxshi planni qanday taniymiz?",
        "practice",
        "Oddiy uy planini funksional jihatdan tahlil qilish.",
        1,
        35,
        20,
    ),
    (
        "L00_M05",
        "L00_M05_002",
        "Yomon plandagi xatolar",
        "practice",
        "Boshlovchilar ko'p qiladigan rejalashtirish xatolari.",
        2,
        35,
        20,
    ),
    (
        "L00_M05",
        "L00_M05_003",
        "Fasadni tahlil qilish",
        "practice",
        "Fasadga faqat chiroyli yoki xunuk deb emas, professional qarash.",
        3,
        35,
        20,
    ),
    (
        "L00_M05",
        "L00_M05_004",
        "LEVEL 0 yakuniy tahlil",
        "practice",
        "Plan, fasad, kesim, genplan va bino elementlarini birlashtirish.",
        4,
        45,
        30,
    ),
]


# ============================================================
# DARSLARNING SODDA VA QIZIQARLI KONTENTI
# ============================================================

LEVEL00_EXTRA_CONTENT = {
    # ========================================================
    # 11-DARS
    # ========================================================
    "L00_M04_001": [
        {
            "title": "Bugun nimani bilib olamiz?",
            "type": "highlight",
            "text": """
            Uy qurilganda uning barcha og'irligi oxir-oqibat
            yerga tushadi.

            <br><br>

            Shu yukni xavfsiz tarzda yerga uzatadigan qism
            <b>fundament</b> deyiladi.
            """,
        },
        {
            "title": "Fundamentni oddiy misolda tushunamiz",
            "type": "normal",
            "text": """
            Tasavvur qiling, yumshoq tuproq ustiga og'ir shkaf
            qo'ydingiz.

            <br><br>

            Uning oyoqlari juda ingichka bo'lsa,
            tuproqqa botishi mumkin.

            <br><br>

            Agar tagiga katta va mustahkam asos qo'ysangiz,
            og'irlik kattaroq maydonga tarqaladi.

            <br><br>

            Fundamentning vazifasi ham shunga o'xshaydi.
            """,
        },
        {
            "title": "Arxitektor uchun nima muhim?",
            "type": "example",
            "text": """
            Arxitektor fundamentni konstruktor kabi hisoblamaydi.

            <br><br>

            Lekin u:

            <br>
            • fundament bino ostida joylashishini;<br>
            • konstruktiv sxema bilan bog'liqligini;<br>
            • yer va geologiya muhimligini;<br>
            • fundament turi o'zboshimchalik bilan tanlanmasligini

            <br><br>

            tushunishi kerak.
            """,
        },
        {
            "title": "Muhim ogohlantirish",
            "type": "warning",
            "text": """
            <b>
            Fundament o'lchami yoki armaturasini shunchaki
            internetdagi boshqa uyga qarab ko'chirish mumkin emas.
            </b>

            <br><br>

            Bu konstruktiv hisob va geologik sharoitga bog'liq.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Savol:

            <br><br>

            Uyda devor, tom, mebel va odamlar yukini
            oxirida qaysi element yerga uzatadi?

            <br><br>

            Javob: <b>fundament</b>.
            """,
        },
    ],

    # ========================================================
    # 12-DARS
    # ========================================================
    "L00_M04_002": [
        {
            "title": "Devor — shunchaki chiziq emas",
            "type": "highlight",
            "text": """
            Archicad'da devor bir necha soniyada chiziladi.

            <br><br>

            Lekin arxitektor uchun har bir devorning
            <b>vazifasi</b> bor.
            """,
        },
        {
            "title": "Asosiy devor turlari",
            "type": "normal",
            "text": """
            Boshlang'ich darajada uchta tushunchani ajrating:

            <br><br>

            <b>Tashqi devor</b> — ichki makonni tashqi muhitdan ajratadi.

            <br><br>

            <b>Ichki devor</b> — xonalarni bir-biridan ajratadi.

            <br><br>

            <b>Yuk ko'taruvchi devor</b> — konstruktiv yuklarni
            qabul qilishi mumkin.
            """,
        },
        {
            "title": "Nega devor qalinligi bir xil emas?",
            "type": "example",
            "text": """
            Masalan, sanuzel bilan koridor orasidagi ichki
            ajratuvchi devor va uyning tashqi devori bir xil
            vazifani bajarmaydi.

            <br><br>

            Shuning uchun ularning:

            <br>
            • qalinligi;<br>
            • materiali;<br>
            • qatlamlari;<br>
            • konstruktiv vazifasi

            <br><br>

            turlicha bo'lishi mumkin.
            """,
        },
        {
            "title": "Boshlovchilar xatosi",
            "type": "warning",
            "text": """
            Plan chiroyli chiqishi uchun yuk ko'taruvchi devorni
            xohlagan joyda olib tashlash mumkin deb o'ylamang.

            <br><br>

            Arxitektura va konstruksiya bir-biridan ajralgan
            ikki dunyo emas.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Uyingizdagi tashqi va ichki devorlarni ko'z oldingizga
            keltiring.

            <br><br>

            Qaysi devorlar qalinroq?

            <br>
            Nima uchun shunday bo'lishi mumkin?
            """,
        },
    ],

    # ========================================================
    # 13-DARS
    # ========================================================
    "L00_M04_003": [
        {
            "title": "Ustun va rigel",
            "type": "highlight",
            "text": """
            Karkasli binoni inson skeletiga o'xshatish mumkin.

            <br><br>

            <b>Ustun</b> — vertikal tayanch.

            <br>
            <b>Rigel yoki to'sin</b> — gorizontal tayanch.
            """,
        },
        {
            "title": "Oddiy tasavvur",
            "type": "normal",
            "text": """
            Stolni tasavvur qiling.

            <br><br>

            Stol oyoqlari — ustunga o'xshaydi.

            <br><br>

            Ularning ustidagi gorizontal element esa
            to'sin yoki rigel prinsipiga yaqin.

            <br><br>

            Albatta bino konstruksiyasi bundan murakkab,
            lekin boshlang'ich tushuncha shunday.
            """,
        },
        {
            "title": "Arxitektorga nima uchun kerak?",
            "type": "example",
            "text": """
            Siz katta mehmonxona yaratmoqchisiz.

            <br><br>

            Lekin konstruktiv ustun xona o'rtasiga tushib qolsa,
            rejalashtirishga ta'sir qiladi.

            <br><br>

            Shuning uchun professional arxitektor konstruktiv
            sxemani erta bosqichdan hisobga oladi.
            """,
        },
        {
            "title": "Xato fikr",
            "type": "warning",
            "text": """
            <b>“Avval plan chizaman, konstruktor keyin o'zi hal qiladi”</b>
            degan yondashuv murakkab muammolarga olib kelishi mumkin.

            <br><br>

            Yaxshi loyiha — mutaxassislar hamkorligining natijasi.
            """,
        },
    ],

    # ========================================================
    # 14-DARS
    # ========================================================
    "L00_M04_004": [
        {
            "title": "Pol, plita va shiftni adashtirmaymiz",
            "type": "highlight",
            "text": """
            Boshlovchilar bu uchta tushunchani ko'pincha aralashtirib yuboradi.

            <br><br>

            Bugun ularning farqini juda sodda tushunamiz.
            """,
        },
        {
            "title": "Pol nima?",
            "type": "normal",
            "text": """
            <b>Pol</b> — siz xonada yurganingizda oyog'ingiz tegadigan
            tayyor sath.

            <br><br>

            Masalan:

            <br>
            laminat, parket, keramika yoki boshqa qoplama.
            """,
        },
        {
            "title": "Plita nima?",
            "type": "normal",
            "text": """
            <b>Plita</b> — qavat yoki yopmaning konstruktiv qismi
            bo'lishi mumkin.

            <br><br>

            U tayyor pol qoplamasining o'zi emas.
            """,
        },
        {
            "title": "Shift nima?",
            "type": "normal",
            "text": """
            Xonada boshingizni yuqoriga ko'targanda ko'radigan
            ichki yuqori sath — <b>shift</b>.

            <br><br>

            Shift bilan konstruktiv plita orasida turli qatlamlar
            va kommunikatsiyalar bo'lishi mumkin.
            """,
        },
        {
            "title": "Nega kesimda yaxshi tushuniladi?",
            "type": "example",
            "text": """
            Plan orqali xona eni va uzunligini ko'ramiz.

            <br><br>

            Pol, plita va shiftning vertikal bog'lanishini esa
            <b>kesimda</b> yaxshiroq tushunamiz.
            """,
        },
    ],

    # ========================================================
    # 15-DARS
    # ========================================================
    "L00_M04_005": [
        {
            "title": "Tomning vazifasi",
            "type": "highlight",
            "text": """
            Tom faqat uyni chiroyli ko'rsatish uchun emas.

            <br><br>

            U binoni yog'ingarchilik, quyosh va tashqi muhit
            ta'sirlaridan himoya qilishda muhim rol o'ynaydi.
            """,
        },
        {
            "title": "Asosiy shakllar",
            "type": "normal",
            "text": """
            Boshlang'ich darajada:

            <br><br>

            • tekis tom;<br>
            • bir nishabli tom;<br>
            • ikki nishabli tom;<br>
            • to'rt nishabli tom

            <br><br>

            kabi shakllarni tanib olish kifoya.

            Keyinroq ularni Archicad'da alohida o'rganamiz.
            """,
        },
        {
            "title": "Tom va fasad",
            "type": "example",
            "text": """
            Bir xil uy planiga ikki xil tom qo'ysangiz,
            uyning tashqi ko'rinishi keskin o'zgarishi mumkin.

            <br><br>

            Demak, tom — fasad kompozitsiyasining ham
            muhim elementi.
            """,
        },
        {
            "title": "Faqat ko'rinishni o'ylamang",
            "type": "warning",
            "text": """
            Tom tanlashda faqat Instagramdagi ko'rinishga qarab
            qaror qilish noto'g'ri.

            <br><br>

            Konstruksiya, suvni chiqarish, iqlim va boshqa
            texnik masalalar ham bor.
            """,
        },
    ],

    # ========================================================
    # 16-DARS
    # ========================================================
    "L00_M04_006": [
        {
            "title": "Eshik va deraza kichik detal emas",
            "type": "highlight",
            "text": """
            Eshik va derazalarning joyi noto'g'ri bo'lsa,
            yaxshi xona ham noqulay bo'lib qolishi mumkin.
            """,
        },
        {
            "title": "Eshik nima qiladi?",
            "type": "normal",
            "text": """
            Eshik ikki makonni bog'laydi.

            <br><br>

            Lekin arxitektor:

            <br>
            • qayerga qo'yish;<br>
            • qaysi tomonga ochish;<br>
            • mebelga xalal bermasligi;<br>
            • odam harakatiga xalaqit bermasligini

            <br><br>

            o'ylashi kerak.
            """,
        },
        {
            "title": "Deraza nima qiladi?",
            "type": "normal",
            "text": """
            Deraza:

            <br><br>

            • tabiiy yorug'lik;<br>
            • tashqi ko'rinish;<br>
            • shamollatish;<br>
            • fasad kompozitsiyasi

            <br><br>

            bilan bog'liq.
            """,
        },
        {
            "title": "Oddiy xato",
            "type": "warning",
            "text": """
            Yotoqxonaga katta shkaf qo'yiladigan devorning o'rtasiga
            katta deraza qo'yib yuborsangiz, keyin mebel joylashishi
            qiyinlashadi.

            <br><br>

            Plan, mebel va fasadni birga o'ylash kerak.
            """,
        },
    ],

    # ========================================================
    # 17-DARS
    # ========================================================
    "L00_M05_001": [
        {
            "title": "Yaxshi plan nimadan bilinadi?",
            "type": "highlight",
            "text": """
            Yaxshi plan degani xonalar shunchaki chiroyli
            joylashgan plan emas.

            <br><br>

            Unda yashash qulay bo'lishi kerak.
            """,
        },
        {
            "title": "5 ta tezkor tekshiruv",
            "type": "normal",
            "text": """
            Plan ko'rsangiz, avval shularni tekshiring:

            <br><br>

            <b>1.</b> Kirish tushunarlimi?<br><br>
            <b>2.</b> Public va private zonalar ajralganmi?<br><br>
            <b>3.</b> Keraksiz uzun koridor bormi?<br><br>
            <b>4.</b> Xonalarga mebel sig'adimi?<br><br>
            <b>5.</b> Xonalar o'zaro mantiqan bog'langanmi?
            """,
        },
        {
            "title": "Misol",
            "type": "example",
            "text": """
            Oshxona ovqatlanish zonasi yonida.

            <br>
            Mehmonxona kirishga yaqin.

            <br>
            Yotoqxonalar esa tinchroq ichki zonada.

            <br><br>

            Bu funksional zonalash yaxshi tashkil etilganidan
            darak berishi mumkin.
            """,
        },
        {
            "title": "Sizning vazifangiz",
            "type": "example",
            "text": """
            Internetdan istalgan uy planini toping.

            <br><br>

            Unga endi “chiroyli” deb emas, yuqoridagi
            5 ta savol orqali qarang.

            <br><br>

            Kamida bitta yaxshi va bitta zaif jihatini toping.
            """,
        },
    ],

    # ========================================================
    # 18-DARS
    # ========================================================
    "L00_M05_002": [
        {
            "title": "Xatoni ko'ra bilish — katta ko'nikma",
            "type": "highlight",
            "text": """
            Professional bo'lish uchun faqat yaxshi loyihalarni
            ko'rish yetmaydi.

            <br><br>

            Yomon yechim nima uchun yomonligini ham tushunish kerak.
            """,
        },
        {
            "title": "Ko'p uchraydigan xatolar",
            "type": "warning",
            "text": """
            Boshlang'ich loyihalarda tez-tez uchraydi:

            <br><br>

            • juda uzun koridor;<br>
            • eshiklar bir-biriga urilishi;<br>
            • yotoqxona public zonada;<br>
            • sanuzel noqulay joyda;<br>
            • xonada mebel uchun joy qolmasligi;<br>
            • kirishdan butun private zona ko'rinishi.
            """,
        },
        {
            "title": "O'lik maydon",
            "type": "normal",
            "text": """
            Uyda maydon bor, lekin undan normal foydalanib bo'lmasa,
            bu <b>foydasiz yoki o'lik maydon</b> bo'lishi mumkin.

            <br><br>

            Masalan, juda keng va uzun koridor katta kvadrat metrni
            egallaydi, lekin yashash funksiyasi bermaydi.
            """,
        },
        {
            "title": "Muhim fikr",
            "type": "example",
            "text": """
            200 m² yaxshi rejalashtirilgan uy ba'zan
            250 m² yomon rejalashtirilgan uydan qulayroq bo'lishi mumkin.

            <br><br>

            <b>Ko'p kvadrat metr = yaxshi arxitektura</b>
            degani emas.
            """,
        },
    ],

    # ========================================================
    # 19-DARS
    # ========================================================
    "L00_M05_003": [
        {
            "title": "Fasadga professional qarash",
            "type": "highlight",
            "text": """
            Endi fasad ko'rganda faqat:

            <br><br>

            “Menga yoqdi” yoki “yoqmadi”

            <br><br>

            demaslikni o'rganamiz.
            """,
        },
        {
            "title": "5 ta savol",
            "type": "normal",
            "text": """
            Fasadni ko'rganda so'rang:

            <br><br>

            <b>1.</b> Asosiy kirish aniq ko'rinadimi?<br><br>
            <b>2.</b> Derazalar proporsiyasi qanday?<br><br>
            <b>3.</b> Materiallar haddan tashqari ko'p emasmi?<br><br>
            <b>4.</b> Tom umumiy kompozitsiyaga mosmi?<br><br>
            <b>5.</b> Plan va fasad bir-biriga mos keladimi?
            """,
        },
        {
            "title": "Material ko'p bo'lsa chiroylimi?",
            "type": "warning",
            "text": """
            Har doim emas.

            <br><br>

            Tosh + yog'och + metall + marmar + dekorativ suvoq +
            yana bir nechta material qo'shish fasadni avtomatik
            ravishda premium qilmaydi.

            <br><br>

            Ba'zan kamroq material bilan toza kompozitsiya
            kuchliroq natija beradi.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Sizga yoqadigan bitta uy fasadini tanlang.

            <br><br>

            Endi nima uchun yoqishini kamida 3 ta professional
            sabab bilan tushuntirishga harakat qiling.

            <br><br>

            Masalan:

            <br>
            “Derazalar ritmi tartibli.”

            <br>
            “Kirish qismi yaxshi ajratilgan.”

            <br>
            “Materiallar soni nazorat qilingan.”
            """,
        },
    ],

    # ========================================================
    # 20-DARS
    # ========================================================
    "L00_M05_004": [
        {
            "title": "LEVEL 0 yakuni",
            "type": "highlight",
            "text": """
            Siz kursni arxitektura haqida mutlaqo
            hech narsa bilmasdan boshladingiz.

            <br><br>

            Endi esa asosiy professional tilni tushuna boshladingiz.
            """,
        },
        {
            "title": "Nimalarni bilasiz?",
            "type": "normal",
            "text": """
            Siz endi quyidagi tushunchalarni ajrata olasiz:

            <br><br>

            ✓ arxitektura;<br>
            ✓ arxitektor vazifasi;<br>
            ✓ loyiha;<br>
            ✓ plan;<br>
            ✓ fasad;<br>
            ✓ kesim;<br>
            ✓ genplan;<br>
            ✓ masshtab;<br>
            ✓ o'lcham;<br>
            ✓ otmetka;<br>
            ✓ fundament;<br>
            ✓ devor;<br>
            ✓ ustun va rigel;<br>
            ✓ pol, plita va shift;<br>
            ✓ tom;<br>
            ✓ eshik va deraza.
            """,
        },
        {
            "title": "Eng muhim o'zgarish",
            "type": "example",
            "text": """
            Eng katta natija terminlarni yodlaganingiz emas.

            <br><br>

            Siz uyga asta-sekin:

            <br><br>

            <b>“Nega aynan shunday?”</b>

            <br><br>

            degan savol bilan qarashni boshlayapsiz.

            <br><br>

            Mana shu savol professional fikrlashning asosidir.
            """,
        },
        {
            "title": "Keyingi bosqich",
            "type": "highlight",
            "text": """
            LEVEL 1 da arxitekturaning yanada chuqur qismiga o'tamiz:

            <br><br>

            • kompozitsiya;<br>
            • proporsiya;<br>
            • ritm;<br>
            • simmetriya;<br>
            • asimmetriya;<br>
            • forma;<br>
            • hajm;<br>
            • arxitektura uslublari.

            <br><br>

            Endi siz shunchaki termin o'rganuvchi emas,
            <b>arxitektura fikrlashiga kirayotgan o'quvchisiz</b>.
            """,
        },
    ],
}


# ============================================================
# LEVEL 0 QO'SHIMCHA TESTLARI
# ============================================================

LEVEL00_EXTRA_QUIZ = {
    "L00_M04_001": [
        {
            "code": "Q031",
            "question": "Fundamentning asosiy vazifasi nima?",
            "explanation": (
                "Fundament bino yuklarini xavfsiz tarzda yerga uzatadi."
            ),
            "options": [
                ("A", "Faqat fasadni bezash", False),
                ("B", "Bino yuklarini yerga uzatish", True),
                ("C", "Faqat xonalarni ajratish", False),
            ],
        },
        {
            "code": "Q032",
            "question": "Fundamentni faqat tashqi ko'rinishga qarab tanlash mumkinmi?",
            "explanation": (
                "Fundament geologiya, konstruktiv sxema va hisob bilan bog'liq."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "Q033",
            "question": "Arxitektor fundamentni tushunishi kerakmi?",
            "explanation": (
                "Arxitektor konstruktor hisobini almashtirmaydi, lekin prinsipni bilishi kerak."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L00_M04_002": [
        {
            "code": "Q034",
            "question": "Tashqi va ichki devor har doim bir xil vazifani bajaradimi?",
            "explanation": "Ularning vazifasi va konstruktiv xususiyatlari farq qilishi mumkin.",
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "Q035",
            "question": "Yuk ko'taruvchi devorni xohlagancha olib tashlash mumkinmi?",
            "explanation": "Bu konstruktiv tizimga ta'sir qilishi mumkin.",
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "Q036",
            "question": "Archicad'dagi har bir devor faqat grafik chiziqmi?",
            "explanation": "Devor real bino elementi va turli vazifaga ega.",
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
    ],

    "L00_M04_003": [
        {
            "code": "Q037",
            "question": "Ustun asosan qaysi yo'nalishda joylashadi?",
            "explanation": "Ustun vertikal konstruktiv element.",
            "options": [
                ("A", "Vertikal", True),
                ("B", "Faqat gorizontal", False),
            ],
        },
        {
            "code": "Q038",
            "question": "Rigel yoki to'sin qaysi turdagi element?",
            "explanation": "Rigel odatda gorizontal konstruktiv element sifatida ishlaydi.",
            "options": [
                ("A", "Gorizontal", True),
                ("B", "Faqat dekor", False),
            ],
        },
        {
            "code": "Q039",
            "question": "Konstruktiv ustun planlashtirishga ta'sir qilishi mumkinmi?",
            "explanation": "Ustunlarning joylashuvi xonalar va mebelga ta'sir qilishi mumkin.",
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L00_M04_004": [
        {
            "code": "Q040",
            "question": "Pol nimani anglatadi?",
            "explanation": "Pol — xonada yuriladigan tayyor sath.",
            "options": [
                ("A", "Tayyor yuriladigan sath", True),
                ("B", "Faqat tom", False),
            ],
        },
        {
            "code": "Q041",
            "question": "Plita va tayyor pol aynan bir narsa deb qarash to'g'rimi?",
            "explanation": "Konstruktiv plita va tayyor pol qatlami boshqa tushunchalar.",
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "Q042",
            "question": "Pol, plita va shift bog'lanishini qaysi chizmada yaxshi ko'ramiz?",
            "explanation": "Vertikal qatlamlar kesimda yaxshiroq ko'rinadi.",
            "options": [
                ("A", "Kesim", True),
                ("B", "Genplan", False),
                ("C", "Faqat fasad", False),
            ],
        },
    ],

    "L00_M04_005": [
        {
            "code": "Q043",
            "question": "Tom faqat fasad uchun kerakmi?",
            "explanation": "Tom himoya va konstruktiv vazifalarga ham ega.",
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "Q044",
            "question": "Tom shakli fasadga ta'sir qiladimi?",
            "explanation": "Tom bino tashqi ko'rinishining muhim qismi.",
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "Q045",
            "question": "Tom tanlashda iqlimni hisobga olish kerakmi?",
            "explanation": "Iqlim va suv chiqarish kabi omillar tom yechimiga ta'sir qiladi.",
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L00_M04_006": [
        {
            "code": "Q046",
            "question": "Eshik ochilish yo'nalishi rejalashtirishga ta'sir qiladimi?",
            "explanation": "Eshik mebel va odam harakatiga xalaqit bermasligi kerak.",
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "Q047",
            "question": "Deraza faqat fasad bezagi hisoblanadimi?",
            "explanation": "Deraza yorug'lik, shamollatish va ichki makon bilan ham bog'liq.",
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "Q048",
            "question": "Mebel joylashuvi deraza pozitsiyasiga ta'sir qilishi mumkinmi?",
            "explanation": "Plan, mebel va deraza joylashuvi birga o'ylanishi kerak.",
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L00_M05_001": [
        {
            "code": "Q049",
            "question": "Yaxshi plan faqat xonalarning sig'ishi bilan belgilanadimi?",
            "explanation": "Xonalar o'rtasidagi funksional bog'lanish ham juda muhim.",
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "Q050",
            "question": "Private zona uchun qaysi xona ko'proq mos?",
            "explanation": "Yotoqxona shaxsiy hudud bo'lganligi sabab private zonaga kiradi.",
            "options": [
                ("A", "Yotoqxona", True),
                ("B", "Avtomobil kirishi", False),
                ("C", "Ko'cha", False),
            ],
        },
        {
            "code": "Q051",
            "question": "Keraksiz uzun koridor yaxshi planning belgisi hisoblanadimi?",
            "explanation": "Ortiqcha koridor foydasiz maydonni oshirishi mumkin.",
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
    ],

    "L00_M05_002": [
        {
            "code": "Q052",
            "question": "O'lik maydon nima?",
            "explanation": "Maydon mavjud, lekin undan samarali foydalanish qiyin bo'lgan joy.",
            "options": [
                ("A", "Foydalanish qiyin bo'lgan maydon", True),
                ("B", "Faqat hovli", False),
            ],
        },
        {
            "code": "Q053",
            "question": "250 m² uy har doim 200 m² uydan qulayroqmi?",
            "explanation": "Qulaylik faqat umumiy maydonga emas, rejalashtirish sifatiga bog'liq.",
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "Q054",
            "question": "Eshiklarning bir-biriga urilishi planning xatosi bo'lishi mumkinmi?",
            "explanation": "Eshiklar harakati oldindan tekshirilishi kerak.",
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L00_M05_003": [
        {
            "code": "Q055",
            "question": "Fasadni professional tahlil qilishda faqat rangga qaraymizmi?",
            "explanation": "Proporsiya, ritm, kirish, tom va materiallar ham tahlil qilinadi.",
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "Q056",
            "question": "Ko'p material ishlatish fasadni avtomatik premium qiladimi?",
            "explanation": "Materiallar soni emas, uyg'unlik va kompozitsiya muhim.",
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "Q057",
            "question": "Fasad va plan o'zaro bog'liqmi?",
            "explanation": "Deraza va eshik kabi elementlar plan va fasadni bog'laydi.",
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L00_M05_004": [
        {
            "code": "Q058",
            "question": "Plan nimani ko'proq ko'rsatadi?",
            "explanation": "Plan binoning gorizontal tashkil topishini ko'rsatadi.",
            "options": [
                ("A", "Gorizontal tashkil topish", True),
                ("B", "Faqat tom materiali", False),
            ],
        },
        {
            "code": "Q059",
            "question": "Kesim nimani tushunishga yordam beradi?",
            "explanation": "Kesim vertikal balandlik va konstruktiv bog'lanishni ko'rsatadi.",
            "options": [
                ("A", "Vertikal tuzilma", True),
                ("B", "Faqat yer chegarasi", False),
            ],
        },
        {
            "code": "Q060",
            "question": "Genplan nimani ko'rsatadi?",
            "explanation": "Genplan uchastkadagi umumiy joylashuvni ko'rsatadi.",
            "options": [
                ("A", "Uchastkadagi joylashuv", True),
                ("B", "Faqat ichki mebel", False),
            ],
        },
        {
            "code": "Q061",
            "question": "Professional arxitektor uchun eng muhim odatlardan biri qaysi?",
            "explanation": "Qarorlarning sababini tushunish uchun doim 'nega?' deb so'rash muhim.",
            "options": [
                ("A", "Faqat tez chizish", False),
                ("B", "Har bir qarorda 'nega?' deb so'rash", True),
                ("C", "Faqat render ko'rish", False),
            ],
        },
    ],
}


# ============================================================
# DATABASE'GA QO'SHISH
# ============================================================

def seed_level00_extra():
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
        ) in LEVEL00_EXTRA_LESSONS:

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


def get_level00_extra_content(
    lesson_code: str,
):
    return LEVEL00_EXTRA_CONTENT.get(
        lesson_code,
        [],
    )
