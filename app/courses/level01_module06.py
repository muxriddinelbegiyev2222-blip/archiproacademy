from database.database import get_connection


# ============================================================
# LEVEL 1
# MODULE 06 - ARXITEKTURA USLUBLARI
# ============================================================

LEVEL01_MODULE06_LESSONS = [
    (
        "L01_M06",
        "L01_M06_001",
        "Arxitektura uslubi nima?",
        "theory",
        "Uslubni faqat dekor emas, umumiy arxitektura tili sifatida tushunish.",
        1,
        30,
        15,
    ),
    (
        "L01_M06",
        "L01_M06_002",
        "Zamonaviy arxitektura",
        "theory",
        "Zamonaviy turar joylarning asosiy kompozitsion xususiyatlarini tushunish.",
        2,
        35,
        15,
    ),
    (
        "L01_M06",
        "L01_M06_003",
        "Minimalizm",
        "theory",
        "Minimal arxitekturada soddalik, proporsiya va detal nazoratini tushunish.",
        3,
        35,
        15,
    ),
    (
        "L01_M06",
        "L01_M06_004",
        "Loft uslubi",
        "theory",
        "Loftning material, hajm va sanoat xarakterini tushunish.",
        4,
        35,
        15,
    ),
    (
        "L01_M06",
        "L01_M06_005",
        "Klassik va neoklassik yo'nalish",
        "theory",
        "Klassik kompozitsiya va zamonaviy neoklassik turar joyni farqlash.",
        5,
        40,
        20,
    ),
    (
        "L01_M06",
        "L01_M06_006",
        "Milliy elementlarni zamonaviy uyga qo'shish",
        "practice",
        "O'zbek milliy elementlarini zamonaviy arxitektura bilan uyg'unlashtirish.",
        6,
        40,
        20,
    ),
    (
        "L01_M06",
        "L01_M06_007",
        "Stilni ko'r-ko'rona ko'chirish xatolari",
        "practice",
        "Pinterest va tayyor fasadlarni nusxalash o'rniga ongli uslub tanlash.",
        7,
        45,
        25,
    ),
]


# ============================================================
# LESSON CONTENT
# ============================================================

LEVEL01_MODULE06_CONTENT = {
    "L01_M06_001": [
        {
            "title": "Uslub nima?",
            "type": "highlight",
            "text": """
            Arxitektura uslubi — bu faqat fasadga
            bir nechta dekor qo'shish emas.

            <br><br>

            Uslub binoning:

            <br><br>

            • shakli;<br>
            • proporsiyasi;<br>
            • materiali;<br>
            • derazalari;<br>
            • tomi;<br>
            • detallari;<br>
            • umumiy xarakteri

            <br><br>

            orqali shakllanadigan
            <b>umumiy arxitektura tili</b>.
            """,
        },
        {
            "title": "Oddiy misol",
            "type": "example",
            "text": """
            Oddiy zamonaviy uyga
            ikkita klassik ustun qo'shsangiz,
            u avtomatik klassik uy bo'lib qolmaydi.

            <br><br>

            Chunki qolgan hajm, deraza, tom va proporsiyalar
            boshqa tilda gapirishi mumkin.
            """,
        },
        {
            "title": "Uslubni nimadan taniymiz?",
            "type": "normal",
            "text": """
            Uyga qaraganda birinchi navbatda:

            <br><br>

            1. Hajm qanday?<br>
            2. Tom qanday?<br>
            3. Deraza proporsiyasi qanday?<br>
            4. Materiallar qanday?<br>
            5. Dekor qancha?<br>
            6. Kompozitsiya qanday?

            <br><br>

            degan savollarni bering.
            """,
        },
        {
            "title": "Xato",
            "type": "warning",
            "text": """
            Faqat bitta detalga qarab:

            <br><br>

            “Bu loft.”

            <br>
            “Bu klassika.”

            <br>
            “Bu minimalizm.”

            <br><br>

            deyish noto'g'ri bo'lishi mumkin.

            <br><br>

            Uslub — umumiy tizim.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Sizga yoqadigan bitta uy tanlang.

            <br><br>

            Uslub nomini yozishdan oldin
            uning 5 ta asosiy belgilarini yozing.

            <br><br>

            Keyin qaysi yo'nalishga yaqinligini aniqlang.
            """,
        },
    ],

    "L01_M06_002": [
        {
            "title": "Zamonaviy arxitektura",
            "type": "highlight",
            "text": """
            Zamonaviy arxitektura deganda
            faqat tekis tomli oq uy tushunilmaydi.

            <br><br>

            Muhim jihatlardan biri —
            <b>funksiya, hajm va materialning aniq ishlashi</b>.
            """,
        },
        {
            "title": "Ko'p uchraydigan belgilar",
            "type": "normal",
            "text": """
            Zamonaviy turar joylarda ko'pincha:

            <br><br>

            • sodda geometrik hajmlar;<br>
            • katta ochilishlar;<br>
            • kamroq ortiqcha dekor;<br>
            • material kontrasti;<br>
            • ichki va tashqi makon aloqasi;<br>
            • aniq kompozitsion ierarxiya

            <br><br>

            uchraydi.
            """,
        },
        {
            "title": "Panoramali deraza",
            "type": "example",
            "text": """
            Katta panoramali deraza
            zamonaviy uyda kuchli element bo'lishi mumkin.

            <br><br>

            Lekin uni faqat chiroyli ko'ringani uchun
            har qanday xonaga qo'yish to'g'ri emas.

            <br><br>

            Orientatsiya, quyosh, maxfiylik va ichki funksiya
            ham tekshiriladi.
            """,
        },
        {
            "title": "Zamonaviy = tasodifiy qutilar emas",
            "type": "warning",
            "text": """
            Bir nechta qutini turli joyga surib,
            fasadga yog'och va qora material qo'shish
            avtomatik zamonaviy arxitektura yaratmaydi.

            <br><br>

            Hajmlarning mantiqi bo'lishi kerak.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Bitta zamonaviy uy toping.

            <br><br>

            Unda:

            <br>
            • asosiy hajm;<br>
            • asosiy material;<br>
            • asosiy aksent;<br>
            • katta ochilish;<br>
            • kirish

            <br><br>

            qayerda ekanini toping.
            """,
        },
    ],

    "L01_M06_003": [
        {
            "title": "Minimalizm = bo'sh uy emas",
            "type": "highlight",
            "text": """
            Minimalizm — shunchaki kam detal ishlatish emas.

            <br><br>

            Kam element bilan
            <b>aniq va nazorat qilingan kompozitsiya</b>
            yaratishdir.
            """,
        },
        {
            "title": "Kam detalda xato ko'proq ko'rinadi",
            "type": "normal",
            "text": """
            Minimal fasadda 20 ta dekor yo'q.

            <br><br>

            Shuning uchun:

            <br><br>

            • noto'g'ri deraza;<br>
            • yomon proporsiya;<br>
            • noto'g'ri chok;<br>
            • material tutashuvi;<br>
            • noto'g'ri soya

            <br><br>

            tez ko'zga tashlanadi.
            """,
        },
        {
            "title": "Misol",
            "type": "example",
            "text": """
            Oq devor.

            <br>
            Bitta katta qora ramkali deraza.

            <br>
            Yog'och kirish.

            <br><br>

            Elementlar juda kam.

            <br><br>

            Lekin ularning proporsiyasi mukammal bo'lmasa,
            fasad zaif ko'rinadi.
            """,
        },
        {
            "title": "Minimalizm va material",
            "type": "normal",
            "text": """
            Minimal arxitekturada material
            ko'pincha dekor vazifasini ham bajaradi.

            <br><br>

            Shuning uchun materiallarning:

            <br><br>

            • teksturasi;<br>
            • choklari;<br>
            • birikishi;<br>
            • rangi

            <br><br>

            juda muhim.
            """,
        },
        {
            "title": "Xato",
            "type": "warning",
            "text": """
            Fasadni bo'sh qoldirib:

            <br><br>

            “Minimalizm qildim.”

            <br><br>

            deyish yetarli emas.

            <br><br>

            Minimalizmda har bir qaror
            yanada aniq asoslangan bo'lishi kerak.
            """,
        },
    ],

    "L01_M06_004": [
        {
            "title": "Loft qayerdan kelgan?",
            "type": "highlight",
            "text": """
            Loft estetikasi sanoat makonlari bilan bog'liq.

            <br><br>

            Shu sababli unda xom va konstruktiv
            materiallarning xarakteri ko'p uchraydi.
            """,
        },
        {
            "title": "Loftda ko'p uchraydigan elementlar",
            "type": "normal",
            "text": """
            Masalan:

            <br><br>

            • g'isht;<br>
            • beton;<br>
            • qora metall;<br>
            • katta ochilishlar;<br>
            • ochiq konstruktiv xarakter;<br>
            • sodda sanoat detali.
            """,
        },
        {
            "title": "Loft uyda qanday ishlatiladi?",
            "type": "example",
            "text": """
            Zamonaviy xususiy uyda
            qora metall soyabon,
            g'isht teksturasi va
            katta oynalar ishlatilishi mumkin.

            <br><br>

            Lekin ular bir-biri bilan
            umumiy konsepsiyada ishlashi kerak.
            """,
        },
        {
            "title": "Loft = hamma narsani qora qilish emas",
            "type": "warning",
            "text": """
            Qora rang + g'isht qo'shishning o'zi
            professional loft yaratmaydi.

            <br><br>

            Proporsiya, hajm va materiallarning
            tabiiy xarakteri muhim.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Loftga yaqin uy toping.

            <br><br>

            Unda kamida 3 ta loft xarakterini
            berayotgan elementni yozing.

            <br><br>

            Keyin bittasini olib tashlasangiz
            xarakter qanchalik o'zgarishini o'ylang.
            """,
        },
    ],

    "L01_M06_005": [
        {
            "title": "Klassik arxitektura",
            "type": "highlight",
            "text": """
            Klassik kompozitsiyada ko'pincha:

            <br><br>

            • simmetriya;<br>
            • aniq o'q;<br>
            • tartib;<br>
            • proporsiya;<br>
            • klassik elementlar

            <br><br>

            kuchli rol o'ynaydi.
            """,
        },
        {
            "title": "Neoklassika",
            "type": "normal",
            "text": """
            Neoklassik yo'nalishda klassik til
            zamonaviyroq va soddalashtirilgan
            ko'rinishda ishlatilishi mumkin.

            <br><br>

            Masalan, dekor kamroq,
            lekin simmetriya va proporsiya saqlanadi.
            """,
        },
        {
            "title": "Ustun qo'ysak klassika bo'ladimi?",
            "type": "warning",
            "text": """
            Yo'q.

            <br><br>

            Zamonaviy quti shaklidagi uyga
            tasodifiy ikkita klassik ustun qo'shish
            stilistik yaxlitlik yaratmaydi.
            """,
        },
        {
            "title": "Proporsiya muhim",
            "type": "example",
            "text": """
            Klassik fasadda portal,
            ustun, deraza va tom o'rtasidagi
            nisbatlar juda muhim.

            <br><br>

            Elementning o'zi to'g'ri bo'lsa ham,
            noto'g'ri proporsiyada ishlatilsa
            fasad sun'iy ko'rinishi mumkin.
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Bitta klassik va bitta neoklassik uy toping.

            <br><br>

            Ularni quyidagicha solishtiring:

            <br><br>

            • simmetriya;<br>
            • dekor miqdori;<br>
            • deraza;<br>
            • ustun;<br>
            • material.
            """,
        },
    ],

    "L01_M06_006": [
        {
            "title": "Milliy element = nusxa emas",
            "type": "highlight",
            "text": """
            Zamonaviy uyga milliy xarakter berish uchun
            tarixiy binoni to'liq nusxalash shart emas.

            <br><br>

            Muhim narsa —
            <b>mazmunni zamonaviy tilda qayta ishlash</b>.
            """,
        },
        {
            "title": "Nimalardan foydalanish mumkin?",
            "type": "normal",
            "text": """
            Masalan:

            <br><br>

            • naqsh geometriyasi;<br>
            • yog'och elementlar;<br>
            • soyali ayvon;<br>
            • ichki hovli prinsipi;<br>
            • mahalliy material;<br>
            • ritm;<br>
            • ranglar;<br>
            • panjara yoki ekranlar.
            """,
        },
        {
            "title": "Zamonaviy talqin",
            "type": "example",
            "text": """
            An'anaviy yog'och naqshni
            aynan eski ko'rinishda ko'chirish o'rniga,
            uning geometrik prinsipini
            zamonaviy metall ekran shaklida ishlatish mumkin.

            <br><br>

            Bu milliy motivning zamonaviy talqini bo'lishi mumkin.
            """,
        },
        {
            "title": "Haddan tashqari dekor",
            "type": "warning",
            "text": """
            Bitta fasadga:

            <br><br>

            • ko'p naqsh;<br>
            • rang;<br>
            • ustun;<br>
            • bezak;<br>
            • milliy ornament

            <br><br>

            joylashtirish milliylikni avtomatik kuchaytirmaydi.

            <br><br>

            Aksincha, arxitektura og'irlashishi mumkin.
            """,
        },
        {
            "title": "O'zbekiston uyi uchun muhimroq savol",
            "type": "highlight",
            "text": """
            Milliy arxitektura faqat ornament emas.

            <br><br>

            <b>
            Hovli, ayvon, soya, mehmon kutish,
            ichki-tashqi makon aloqasi kabi
            yashash prinsiplari ham muhim.
            </b>
            """,
        },
        {
            "title": "Mini-amaliyot",
            "type": "example",
            "text": """
            Zamonaviy o'zbek uyi uchun
            3 ta milliy element tanlang.

            <br><br>

            Lekin har biri uchun:

            <br><br>

            “Nega aynan shu element?”

            <br><br>

            degan savolga javob yozing.
            """,
        },
    ],

    "L01_M06_007": [
        {
            "title": "Pinterest — manba, loyiha emas",
            "type": "highlight",
            "text": """
            Internetdagi yaxshi uylarni ko'rish foydali.

            <br><br>

            Lekin tayyor uyni
            ko'r-ko'rona ko'chirish
            professional loyiha jarayoni emas.
            """,
        },
        {
            "title": "Nega nusxa ishlamasligi mumkin?",
            "type": "normal",
            "text": """
            Siz ko'rgan uy boshqa:

            <br><br>

            • uchastkada;<br>
            • iqlimda;<br>
            • orientatsiyada;<br>
            • oilada;<br>
            • budjetda;<br>
            • konstruktiv tizimda

            <br><br>

            yaratilgan bo'lishi mumkin.
            """,
        },
        {
            "title": "Eng xavfli xato",
            "type": "warning",
            "text": """
            Mijoz rasm yubordi.

            <br><br>

            Arxitektor esa:

            <br><br>

            “Xuddi shuni qilamiz.”

            <br><br>

            dedi.

            <br><br>

            Bu yerda loyiha tahlili,
            uchastka va funksiya yo'qolib ketadi.
            """,
        },
        {
            "title": "To'g'ri usul",
            "type": "example",
            "text": """
            Reference rasmga qarab:

            <br><br>

            “Sizga aynan nimasi yoqdi?”

            <br><br>

            deb so'rang.

            <br><br>

            Masalan:

            <br>
            • rangmi?<br>
            • katta derazami?<br>
            • tommi?<br>
            • materialmi?<br>
            • umumiy soddalikmi?<br>
            • kirish portalimi?

            <br><br>

            Shunda rasmni nusxalamay,
            mijozning istagini tushunasiz.
            """,
        },
        {
            "title": "Uslub tanlash algoritmi",
            "type": "example",
            "text": """
            <b>1.</b> Mijoz istagini tushuning.<br><br>
            <b>2.</b> Uchastkani tahlil qiling.<br><br>
            <b>3.</b> Plan funksiyasini hal qiling.<br><br>
            <b>4.</b> Hajm konsepsiyasini yarating.<br><br>
            <b>5.</b> Mos arxitektura tilini tanlang.<br><br>
            <b>6.</b> Reference'dan g'oya oling, nusxa emas.
            """,
        },
        {
            "title": "LEVEL 1 yakuni",
            "type": "highlight",
            "text": """
            LEVEL 1 davomida siz:

            <br><br>

            ✓ kompozitsiya;<br>
            ✓ proporsiya;<br>
            ✓ ritm;<br>
            ✓ simmetriya;<br>
            ✓ asimmetriya;<br>
            ✓ forma;<br>
            ✓ hajm;<br>
            ✓ arxitektura uslublari

            <br><br>

            bo'yicha asosiy professional fikrlashni o'rgandingiz.

            <br><br>

            Keyingi qadam:
            <b>LEVEL 1 YAKUNIY IMTIHON.</b>
            """,
        },
    ],
}


# ============================================================
# QUIZ DATA
# ============================================================

LEVEL01_MODULE06_QUIZ = {
    "L01_M06_001": [
        {
            "code": "L01_Q076",
            "question": "Arxitektura uslubi faqat dekor bilan belgilanadimi?",
            "explanation": (
                "Uslub hajm, proporsiya, material, deraza, tom va boshqa elementlarning umumiy tilidir."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L01_Q077",
            "question": "Bitta klassik ustun qo'shilsa uy avtomatik klassik bo'ladimi?",
            "explanation": (
                "Bitta detal butun binoning stilistik tilini belgilamaydi."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L01_Q078",
            "question": "Uslubni tahlil qilishda qaysi omil muhim?",
            "explanation": (
                "Hajm, tom, deraza, material va kompozitsiya birgalikda tahlil qilinadi."
            ),
            "options": [
                ("A", "Umumiy arxitektura tizimi", True),
                ("B", "Faqat bitta rang", False),
            ],
        },
    ],

    "L01_M06_002": [
        {
            "code": "L01_Q079",
            "question": "Zamonaviy arxitektura faqat tekis tomli oq uy deganimi?",
            "explanation": (
                "Zamonaviy arxitektura bundan kengroq tushuncha."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L01_Q080",
            "question": "Panoramali deraza joylashtirishda orientatsiya muhimmi?",
            "explanation": (
                "Quyosh, maxfiylik va ichki funksiya ham hisobga olinadi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L01_Q081",
            "question": "Tasodifiy qutilar zamonaviy arxitektura yaratadimi?",
            "explanation": (
                "Hajmlarning funksional va kompozitsion mantiqi bo'lishi kerak."
            ),
            "options": [
                ("A", "Har doim", False),
                ("B", "Yo'q", True),
            ],
        },
    ],

    "L01_M06_003": [
        {
            "code": "L01_Q082",
            "question": "Minimalizm nimani anglatadi?",
            "explanation": (
                "Kam element bilan aniq va nazorat qilingan kompozitsiya yaratishni."
            ),
            "options": [
                ("A", "Shunchaki bo'sh fasad", False),
                ("B", "Nazorat qilingan sodda kompozitsiya", True),
            ],
        },
        {
            "code": "L01_Q083",
            "question": "Minimal fasadda detal sifati muhimmi?",
            "explanation": (
                "Elementlar kam bo'lgani uchun har bir detal yanada sezilarli bo'ladi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L01_Q084",
            "question": "Minimalizmda material tutashuvlari muhimmi?",
            "explanation": (
                "Minimal kompozitsiyada material va detallarning sifati katta rol o'ynaydi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L01_M06_004": [
        {
            "code": "L01_Q085",
            "question": "Loft estetikasi qaysi muhit bilan bog'liq?",
            "explanation": (
                "Loft sanoat va ishlab chiqarish makonlari estetikasi bilan bog'liq."
            ),
            "options": [
                ("A", "Sanoat makonlari", True),
                ("B", "Faqat klassik saroylar", False),
            ],
        },
        {
            "code": "L01_Q086",
            "question": "Qora rangning o'zi loft yaratadimi?",
            "explanation": (
                "Loft umumiy material, hajm va sanoat xarakteriga bog'liq."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L01_Q087",
            "question": "G'isht va metall loft xarakterida ishlatilishi mumkinmi?",
            "explanation": (
                "Bu materiallar loft estetikasida tez-tez uchraydi."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L01_M06_005": [
        {
            "code": "L01_Q088",
            "question": "Klassik kompozitsiyada simmetriya tez-tez uchraydimi?",
            "explanation": (
                "Klassik arxitekturada simmetriya va aniq o'q muhim vositalardir."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L01_Q089",
            "question": "Neoklassika klassik elementlarni soddalashtirib ishlatishi mumkinmi?",
            "explanation": (
                "Neoklassik yo'nalishda klassik til zamonaviyroq shaklda ishlatilishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L01_Q090",
            "question": "Klassik elementning proporsiyasi muhimmi?",
            "explanation": (
                "Noto'g'ri proporsiya klassik elementni sun'iy ko'rsatishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
    ],

    "L01_M06_006": [
        {
            "code": "L01_Q091",
            "question": "Milliy arxitektura faqat ornamentdan iboratmi?",
            "explanation": (
                "Hovli, ayvon, soya va yashash prinsiplari ham milliy arxitektura xarakterining bir qismi."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L01_Q092",
            "question": "Milliy naqshni zamonaviy materialda qayta talqin qilish mumkinmi?",
            "explanation": (
                "An'anaviy geometrik prinsip zamonaviy shakl va materialda ishlatilishi mumkin."
            ),
            "options": [
                ("A", "Ha", True),
                ("B", "Yo'q", False),
            ],
        },
        {
            "code": "L01_Q093",
            "question": "Ko'proq milliy dekor har doim yaxshiroqmi?",
            "explanation": (
                "Ortiqcha dekor kompozitsiyani og'irlashtirishi mumkin."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
    ],

    "L01_M06_007": [
        {
            "code": "L01_Q094",
            "question": "Pinterestdagi uyni to'liq nusxalash professional loyiha usulimi?",
            "explanation": (
                "Reference g'oya beradi, lekin loyiha uchastka, iqlim va mijozga mos yaratilishi kerak."
            ),
            "options": [
                ("A", "Ha", False),
                ("B", "Yo'q", True),
            ],
        },
        {
            "code": "L01_Q095",
            "question": "Mijoz rasm yuborsa qaysi savol foydali?",
            "explanation": (
                "Mijozga aynan qaysi element yoqqanini aniqlash uning haqiqiy istagini tushunishga yordam beradi."
            ),
            "options": [
                ("A", "Sizga aynan nimasi yoqdi?", True),
                ("B", "Xuddi shuni ko'chiraymi?", False),
            ],
        },
        {
            "code": "L01_Q096",
            "question": "Reference'dan qanday foydalanish ma'qul?",
            "explanation": (
                "Reference'dan prinsip va g'oya olinadi, loyiha esa kontekstga mos qayta yaratiladi."
            ),
            "options": [
                ("A", "G'oya va prinsip olish", True),
                ("B", "Ko'r-ko'rona nusxalash", False),
            ],
        },
    ],
}


# ============================================================
# DATABASE SEED
# ============================================================

def seed_level01_module06():
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
        ) in LEVEL01_MODULE06_LESSONS:

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
