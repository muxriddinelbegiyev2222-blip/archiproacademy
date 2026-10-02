from database.database import get_connection


# ============================================================
# 16 TA ASOSIY LEVEL
# ============================================================

LEVELS = [
    (
        "LEVEL_00",
        "Absolute Zero",
        "Arxitekturaga mutlaqo noldan kirish",
        "Arxitektura haqida hech qanday bilimga ega bo'lmagan "
        "foydalanuvchi uchun boshlang'ich bosqich.",
        0,
    ),
    (
        "LEVEL_01",
        "Architecture Fundamentals",
        "Arxitektura asoslari",
        "Arxitekturaning fundamental qonuniyatlari, chizma va "
        "fazoviy fikrlash asoslari.",
        1,
    ),
    (
        "LEVEL_02",
        "Spatial Thinking",
        "Fazoviy fikrlash va ergonomika",
        "Xonalar, odam harakati, proporsiya va qulay rejalashtirish.",
        2,
    ),
    (
        "LEVEL_03",
        "Site Planning",
        "Uchastka va genplan",
        "Yer uchastkasini tahlil qilish va binoni to'g'ri joylashtirish.",
        3,
    ),
    (
        "LEVEL_04",
        "Uzbekistan Residential Design",
        "O'zbekiston sharoitidagi turar joy",
        "Mahalliy iqlim, turmush tarzi va hovlili uylarni loyihalash.",
        4,
    ),
    (
        "LEVEL_05",
        "Archicad Beginner",
        "Archicad boshlang'ich",
        "Archicad interfeysi va asosiy instrumentlarni noldan o'rganish.",
        5,
    ),
    (
        "LEVEL_06",
        "Archicad Intermediate",
        "Archicad o'rta daraja",
        "Professional model yaratish va loyiha strukturasini boshqarish.",
        6,
    ),
    (
        "LEVEL_07",
        "Archicad Advanced",
        "Archicad yuqori daraja",
        "Murakkab modellashtirish, avtomatlashtirish va BIM workflow.",
        7,
    ),
    (
        "LEVEL_08",
        "Construction Fundamentals",
        "Qurilish konstruksiyalari",
        "Arxitektor bilishi kerak bo'lgan konstruktiv bilimlar.",
        8,
    ),
    (
        "LEVEL_09",
        "SHNQ & Regulations",
        "SHNQ va normativlar",
        "O'zbekiston sharoitida normativ savodxonlik va loyiha tekshiruvi.",
        9,
    ),
    (
        "LEVEL_10",
        "One-Storey House Professional",
        "1 qavatli uy PRO",
        "Bir qavatli uyni texnik topshiriqdan loyiha albomigacha yaratish.",
        10,
    ),
    (
        "LEVEL_11",
        "Two-Storey House Professional",
        "2 qavatli uy PRO",
        "Ikki qavatli turar joyni professional darajada loyihalash.",
        11,
    ),
    (
        "LEVEL_12",
        "BIM & Documentation",
        "BIM va ishchi hujjatlar",
        "Professional BIM model va ishchi loyiha albomini tayyorlash.",
        12,
    ),
    (
        "LEVEL_13",
        "Client & Real Project Workflow",
        "Mijoz va real loyiha",
        "Real buyurtma, texnik topshiriq, muzokara va loyiha himoyasi.",
        13,
    ),
    (
        "LEVEL_14",
        "Advanced Residential Designer",
        "Advanced Residential Designer",
        "Murakkab uchastkalar va yuqori darajadagi turar joy loyihalari.",
        14,
    ),
    (
        "LEVEL_15",
        "PRO Final",
        "Professional yakuniy bosqich",
        "Mustaqil loyiha, imtihon, portfolio va PRO final.",
        15,
    ),
]


# ============================================================
# BARCHA LEVEL MODULLARI
# ============================================================

MODULES = {
    # --------------------------------------------------------
    # LEVEL 00
    # --------------------------------------------------------
    "LEVEL_00": [
        (
            "L00_M01",
            "Arxitektura bilan tanishuv",
            "Arxitektura nima va arxitektor qanday fikrlaydi.",
            1,
            90,
        ),
        (
            "L00_M02",
            "Chizmalarni tushunish",
            "Plan, fasad, kesim va genplan tushunchalari.",
            2,
            120,
        ),
        (
            "L00_M03",
            "Masshtab va o'lchamlar",
            "Chizmalardagi o'lcham va masshtabni tushunish.",
            3,
            120,
        ),
        (
            "L00_M04",
            "Bino elementlari",
            "Bino qanday qismlardan tashkil topishini tushunish.",
            4,
            150,
        ),
        (
            "L00_M05",
            "Birinchi arxitektura tahlili",
            "Tayyor uylarni arxitektor ko'zi bilan tahlil qilish.",
            5,
            180,
        ),
    ],

    # --------------------------------------------------------
    # LEVEL 01
    # --------------------------------------------------------
    "LEVEL_01": [
        (
            "L01_M01",
            "Arxitektura kompozitsiyasi",
            "Kompozitsiya, markaz, balans va vizual tartib.",
            1,
            180,
        ),
        (
            "L01_M02",
            "Proporsiya va masshtab",
            "Bino qismlari o'rtasidagi to'g'ri nisbatlar.",
            2,
            180,
        ),
        (
            "L01_M03",
            "Ritm va takrorlanish",
            "Fasad va interyerdagi ritm tushunchasi.",
            3,
            150,
        ),
        (
            "L01_M04",
            "Simmetriya va asimmetriya",
            "Arxitekturadagi muvozanatni tushunish.",
            4,
            150,
        ),
        (
            "L01_M05",
            "Forma va hajm",
            "Arxitektura shakllarini 3D fikrlash.",
            5,
            180,
        ),
        (
            "L01_M06",
            "Arxitektura uslublari",
            "Asosiy zamonaviy va tarixiy uslublar.",
            6,
            240,
        ),
    ],

    # --------------------------------------------------------
    # LEVEL 02
    # --------------------------------------------------------
    "LEVEL_02": [
        (
            "L02_M01",
            "Inson ergonomikasi",
            "Odam tanasi va makon o'lchamlari.",
            1,
            240,
        ),
        (
            "L02_M02",
            "Funksional zonalash",
            "Public, private va service zonalar.",
            2,
            240,
        ),
        (
            "L02_M03",
            "Harakat yo'llari",
            "Uy ichidagi circulation va qulay yurish yo'llari.",
            3,
            180,
        ),
        (
            "L02_M04",
            "Mehmonxona loyihalash",
            "Mehmonxona ergonomikasi va mebel joylashuvi.",
            4,
            240,
        ),
        (
            "L02_M05",
            "Oshxona loyihalash",
            "Oshxona ergonomikasi va ishchi uchburchak.",
            5,
            300,
        ),
        (
            "L02_M06",
            "Yotoqxona loyihalash",
            "Master bedroom va oddiy yotoqxona.",
            6,
            240,
        ),
        (
            "L02_M07",
            "Bolalar xonasi",
            "Yoshga mos xavfsiz va funksional makon.",
            7,
            180,
        ),
        (
            "L02_M08",
            "Sanuzel ergonomikasi",
            "Sanitar jihozlar va qulay masofalar.",
            8,
            240,
        ),
        (
            "L02_M09",
            "Koridor va kirish",
            "Tambur, hallway va harakat zonalari.",
            9,
            180,
        ),
        (
            "L02_M10",
            "Yordamchi xonalar",
            "Garderob, laundry, ombor va texnik xonalar.",
            10,
            180,
        ),
    ],

    # --------------------------------------------------------
    # LEVEL 03
    # --------------------------------------------------------
    "LEVEL_03": [
        (
            "L03_M01",
            "Uchastkani o'qish",
            "Yer shakli, o'lchami va mavjud sharoitlarni tushunish.",
            1,
            180,
        ),
        (
            "L03_M02",
            "Shimol va quyosh",
            "Orientatsiya va quyosh harakatini hisobga olish.",
            2,
            240,
        ),
        (
            "L03_M03",
            "Ko'cha va kirish",
            "Piyoda va avtomobil kirishini tashkil qilish.",
            3,
            180,
        ),
        (
            "L03_M04",
            "Uy joylashtirish",
            "Uyni uchastkada to'g'ri joylashtirish.",
            4,
            300,
        ),
        (
            "L03_M05",
            "Hovli zonalari",
            "Dam olish, xo'jalik va yashil zonalar.",
            5,
            240,
        ),
        (
            "L03_M06",
            "Avtomobil zonasi",
            "Navес, parking va kirish yo'li.",
            6,
            180,
        ),
        (
            "L03_M07",
            "Relyef",
            "Nishab va balandlik farqlari bilan ishlash.",
            7,
            240,
        ),
        (
            "L03_M08",
            "Genplan yaratish",
            "To'liq turar joy genplanini ishlab chiqish.",
            8,
            360,
        ),
    ],

    # --------------------------------------------------------
    # LEVEL 04
    # --------------------------------------------------------
    "LEVEL_04": [
        (
            "L04_M01",
            "O'zbek oilasi uchun uy",
            "Mahalliy oilaviy turmush tarzini hisobga olish.",
            1,
            240,
        ),
        (
            "L04_M02",
            "Mehmon kutish madaniyati",
            "Mehmonxona va mehmon harakatini rejalashtirish.",
            2,
            180,
        ),
        (
            "L04_M03",
            "Ichki hovli",
            "Hovli va yashash makoni aloqasi.",
            3,
            240,
        ),
        (
            "L04_M04",
            "Ayvon va terassa",
            "Ochiq va yarim ochiq makonlarni loyihalash.",
            4,
            180,
        ),
        (
            "L04_M05",
            "Yozgi oshxona",
            "O'zbekiston sharoitida yozgi oshxona.",
            5,
            180,
        ),
        (
            "L04_M06",
            "Banja va yordamchi bino",
            "Qo'shimcha funksiyalarni to'g'ri joylashtirish.",
            6,
            180,
        ),
        (
            "L04_M07",
            "Issiq iqlimda loyiha",
            "Yozgi issiqlik va quyoshdan himoyalanish.",
            7,
            240,
        ),
        (
            "L04_M08",
            "Mahalliy fasad",
            "Zamonaviy va milliy elementlarni uyg'unlashtirish.",
            8,
            240,
        ),
    ],

    # --------------------------------------------------------
    # LEVEL 05
    # --------------------------------------------------------
    "LEVEL_05": [
        (
            "L05_M01",
            "Archicad interfeysi",
            "Dastur oynalari va asosiy boshqaruv.",
            1,
            240,
        ),
        (
            "L05_M02",
            "Navigator",
            "Project Map, View Map va Layout Book.",
            2,
            180,
        ),
        (
            "L05_M03",
            "Wall Tool",
            "Devorlarni professional yaratish.",
            3,
            300,
        ),
        (
            "L05_M04",
            "Slab Tool",
            "Pol va plitalar bilan ishlash.",
            4,
            240,
        ),
        (
            "L05_M05",
            "Door va Window",
            "Eshik va derazalarni boshqarish.",
            5,
            300,
        ),
        (
            "L05_M06",
            "Column va Beam",
            "Ustun va rigel elementlari.",
            6,
            240,
        ),
        (
            "L05_M07",
            "Object Tool",
            "Mebel va obyektlar bilan ishlash.",
            7,
            180,
        ),
        (
            "L05_M08",
            "2D instrumentlar",
            "Line, Polyline, Fill, Text va Label.",
            8,
            300,
        ),
        (
            "L05_M09",
            "Dimension",
            "Professional o'lcham qo'yish.",
            9,
            240,
        ),
        (
            "L05_M10",
            "Birinchi Archicad loyiha",
            "Oddiy uy modelini noldan yaratish.",
            10,
            480,
        ),
    ],

    # --------------------------------------------------------
    # LEVEL 06
    # --------------------------------------------------------
    "LEVEL_06": [
        (
            "L06_M01",
            "Stories",
            "Qavatlar tizimini professional boshqarish.",
            1,
            180,
        ),
        (
            "L06_M02",
            "Layers",
            "Layer va Layer Combination.",
            2,
            240,
        ),
        (
            "L06_M03",
            "Building Materials",
            "Materiallarning BIM xususiyatlari.",
            3,
            240,
        ),
        (
            "L06_M04",
            "Composite Structures",
            "Ko'p qatlamli devor va konstruksiyalar.",
            4,
            300,
        ),
        (
            "L06_M05",
            "Complex Profiles",
            "Maxsus profillar yaratish.",
            5,
            300,
        ),
        (
            "L06_M06",
            "Roof Tool",
            "Murakkab tomlarni yaratish.",
            6,
            360,
        ),
        (
            "L06_M07",
            "Stair Tool",
            "Professional zinapoya.",
            7,
            360,
        ),
        (
            "L06_M08",
            "Railing",
            "Zinapoya va balkon to'siqlari.",
            8,
            240,
        ),
        (
            "L06_M09",
            "Mesh",
            "Relyef va yer modelini yaratish.",
            9,
            300,
        ),
        (
            "L06_M10",
            "Zones",
            "Xona maydonlari va zonalar.",
            10,
            240,
        ),
    ],

    # --------------------------------------------------------
    # LEVEL 07
    # --------------------------------------------------------
    "LEVEL_07": [
        (
            "L07_M01",
            "Favorites",
            "Standart elementlarni tez ishlatish.",
            1,
            180,
        ),
        (
            "L07_M02",
            "Graphic Overrides",
            "Modelni turli grafik ko'rinishlarda boshqarish.",
            2,
            240,
        ),
        (
            "L07_M03",
            "Model View Options",
            "View sozlamalari.",
            3,
            180,
        ),
        (
            "L07_M04",
            "Renovation",
            "Rekonstruksiya loyihalari.",
            4,
            240,
        ),
        (
            "L07_M05",
            "Schedules",
            "Avtomatik spetsifikatsiyalar.",
            5,
            360,
        ),
        (
            "L07_M06",
            "Properties",
            "BIM parametr va xususiyatlar.",
            6,
            240,
        ),
        (
            "L07_M07",
            "Classification",
            "Elementlarni BIM klassifikatsiyalash.",
            7,
            180,
        ),
        (
            "L07_M08",
            "Hotlink va Modules",
            "Murakkab loyiha strukturalari.",
            8,
            240,
        ),
        (
            "L07_M09",
            "Professional Template",
            "O'z ishchi Archicad template'ingizni yaratish.",
            9,
            420,
        ),
    ],

    # --------------------------------------------------------
    # LEVEL 08
    # --------------------------------------------------------
    "LEVEL_08": [
        (
            "L08_M01",
            "Fundament",
            "Asosiy fundament turlari.",
            1,
            240,
        ),
        (
            "L08_M02",
            "Devor konstruksiyasi",
            "Yuk ko'taruvchi va to'ldiruvchi devorlar.",
            2,
            240,
        ),
        (
            "L08_M03",
            "Karkas",
            "Ustun-rigel konstruktiv tizimi.",
            3,
            300,
        ),
        (
            "L08_M04",
            "Plitalar",
            "Qavatlararo yopmalar.",
            4,
            240,
        ),
        (
            "L08_M05",
            "Tom konstruksiyasi",
            "Tomning asosiy konstruktiv elementlari.",
            5,
            300,
        ),
        (
            "L08_M06",
            "Gidroizolyatsiya",
            "Namlikdan himoya asoslari.",
            6,
            180,
        ),
        (
            "L08_M07",
            "Issiqlik izolyatsiyasi",
            "Uyda issiqlik himoyasi.",
            7,
            180,
        ),
        (
            "L08_M08",
            "Seysmika asoslari",
            "Arxitektor uchun seysmik fikrlash.",
            8,
            300,
        ),
        (
            "L08_M09",
            "Konstruktor bilan ishlash",
            "Arxitektor va konstruktor hamkorligi.",
            9,
            180,
        ),
    ],

    # --------------------------------------------------------
    # LEVEL 09
    # --------------------------------------------------------
    "LEVEL_09": [
        (
            "L09_M01",
            "Normativ savodxonlik",
            "SHNQ va boshqa normativlarni to'g'ri o'qish.",
            1,
            240,
        ),
        (
            "L09_M02",
            "Turar joy talablari",
            "Turar joy obyektlariga tegishli asosiy talablar.",
            2,
            360,
        ),
        (
            "L09_M03",
            "Uchastka talablari",
            "Joylashtirish va shaharsozlik talablari.",
            3,
            300,
        ),
        (
            "L09_M04",
            "Yoritish va insolyatsiya",
            "Tabiiy yorug'lik talablarini tushunish.",
            4,
            240,
        ),
        (
            "L09_M05",
            "Yong'in xavfsizligi asoslari",
            "Arxitektor bilishi kerak bo'lgan minimum.",
            5,
            240,
        ),
        (
            "L09_M06",
            "Evakuatsiya asoslari",
            "Xavfsiz chiqish va harakat tushunchalari.",
            6,
            180,
        ),
        (
            "L09_M07",
            "Accessibility asoslari",
            "Qulay va inklyuziv makon.",
            7,
            180,
        ),
        (
            "L09_M08",
            "Normativ xatolar",
            "Amaliy loyihalardagi tipik me'yoriy xatolar.",
            8,
            300,
        ),
    ],

    # --------------------------------------------------------
    # LEVEL 10
    # --------------------------------------------------------
    "LEVEL_10": [
        (
            "L10_M01",
            "Texnik topshiriq",
            "1 qavatli uy uchun professional brief.",
            1,
            240,
        ),
        (
            "L10_M02",
            "Site Analysis",
            "Uchastkani loyiha oldidan tahlil qilish.",
            2,
            300,
        ),
        (
            "L10_M03",
            "Bubble Diagram",
            "Funksional sxemani yaratish.",
            3,
            240,
        ),
        (
            "L10_M04",
            "Eskiz plan",
            "Bir qavatli uy rejasining birinchi varianti.",
            4,
            360,
        ),
        (
            "L10_M05",
            "Plan optimizatsiyasi",
            "Maydon va harakatni optimallashtirish.",
            5,
            360,
        ),
        (
            "L10_M06",
            "Archicad modeli",
            "Eskizni professional BIM modelga aylantirish.",
            6,
            480,
        ),
        (
            "L10_M07",
            "Fasad",
            "1 qavatli uy fasadini ishlab chiqish.",
            7,
            360,
        ),
        (
            "L10_M08",
            "Tom",
            "Uy tomini loyihalash.",
            8,
            300,
        ),
        (
            "L10_M09",
            "Kesim",
            "Professional kesimlar.",
            9,
            300,
        ),
        (
            "L10_M10",
            "Genplan",
            "Uy va hovlining yakuniy genplani.",
            10,
            360,
        ),
        (
            "L10_M11",
            "Loyiha albomi",
            "Bir qavatli uy loyiha albomini tayyorlash.",
            11,
            480,
        ),
    ],

    # --------------------------------------------------------
    # LEVEL 11
    # --------------------------------------------------------
    "LEVEL_11": [
        (
            "L11_M01",
            "2 qavatli uy konsepsiyasi",
            "Vertikal funksional aloqalarni tushunish.",
            1,
            300,
        ),
        (
            "L11_M02",
            "Qavatlar zonalashi",
            "1 va 2-qavat funksiyalarini ajratish.",
            2,
            300,
        ),
        (
            "L11_M03",
            "Zinapoya PRO",
            "Zinapoyani funksional va xavfsiz loyihalash.",
            3,
            420,
        ),
        (
            "L11_M04",
            "Vertikal kommunikatsiyalar",
            "Sanuzel va muhandislik zonalarini moslashtirish.",
            4,
            300,
        ),
        (
            "L11_M05",
            "Void va ikkinchi yorug'lik",
            "Murakkab ikki qavatli makon.",
            5,
            300,
        ),
        (
            "L11_M06",
            "Balkon va terassa",
            "Tashqi yuqori qavat makonlari.",
            6,
            240,
        ),
        (
            "L11_M07",
            "2 qavatli fasad",
            "Proporsiya va vertikal kompozitsiya.",
            7,
            360,
        ),
        (
            "L11_M08",
            "To'liq Archicad model",
            "2 qavatli professional BIM model.",
            8,
            600,
        ),
        (
            "L11_M09",
            "Ishchi loyiha",
            "2 qavatli uy ishchi hujjatlari.",
            9,
            540,
        ),
    ],

    # --------------------------------------------------------
    # LEVEL 12
    # --------------------------------------------------------
    "LEVEL_12": [
        (
            "L12_M01",
            "BIM tushunchasi",
            "Oddiy 3D model va BIM farqi.",
            1,
            240,
        ),
        (
            "L12_M02",
            "Element Information",
            "Model ma'lumotlarini boshqarish.",
            2,
            240,
        ),
        (
            "L12_M03",
            "Spetsifikatsiyalar",
            "Eshik, deraza va xona jadvallari.",
            3,
            360,
        ),
        (
            "L12_M04",
            "View Map PRO",
            "Professional view struktura.",
            4,
            300,
        ),
        (
            "L12_M05",
            "Layout Book",
            "Loyiha varaqalarini professional yig'ish.",
            5,
            360,
        ),
        (
            "L12_M06",
            "Shtamp va standartlar",
            "Ishchi albom dizayni.",
            6,
            240,
        ),
        (
            "L12_M07",
            "Publisher",
            "PDF va boshqa formatlarda chiqarish.",
            7,
            240,
        ),
        (
            "L12_M08",
            "DWG almashinuvi",
            "AutoCAD bilan to'g'ri ma'lumot almashish.",
            8,
            240,
        ),
        (
            "L12_M09",
            "IFC asoslari",
            "BIM koordinatsiya.",
            9,
            240,
        ),
        (
            "L12_M10",
            "Final loyiha albomi",
            "Professional hujjatlar to'plami.",
            10,
            480,
        ),
    ],

    # --------------------------------------------------------
    # LEVEL 13
    # --------------------------------------------------------
    "LEVEL_13": [
        (
            "L13_M01",
            "Mijoz bilan birinchi suhbat",
            "To'g'ri savollar berish.",
            1,
            240,
        ),
        (
            "L13_M02",
            "Professional brief",
            "Mijoz gapini texnik topshiriqqa aylantirish.",
            2,
            300,
        ),
        (
            "L13_M03",
            "Budjet",
            "Budjet va loyiha qarorlari o'rtasidagi aloqa.",
            3,
            240,
        ),
        (
            "L13_M04",
            "Variantlar tayyorlash",
            "Mijozga bir nechta yechim ko'rsatish.",
            4,
            300,
        ),
        (
            "L13_M05",
            "Loyiha taqdimoti",
            "Loyihani professional ko'rsatish.",
            5,
            240,
        ),
        (
            "L13_M06",
            "Mijoz tuzatishlari",
            "Revision va o'zgarishlarni boshqarish.",
            6,
            300,
        ),
        (
            "L13_M07",
            "Qarorni himoya qilish",
            "Nega aynan shu yechim tanlanganini tushuntirish.",
            7,
            240,
        ),
        (
            "L13_M08",
            "Real loyiha simulyatori",
            "Boshlanishidan yakunigacha real buyurtma.",
            8,
            600,
        ),
    ],

    # --------------------------------------------------------
    # LEVEL 14
    # --------------------------------------------------------
    "LEVEL_14": [
        (
            "L14_M01",
            "Tor uchastka",
            "Tor yerlarda professional rejalashtirish.",
            1,
            360,
        ),
        (
            "L14_M02",
            "Noto'g'ri shakldagi uchastka",
            "Murakkab geometriyali yer.",
            2,
            360,
        ),
        (
            "L14_M03",
            "Nishabli yer",
            "Relyefli uchastkada turar joy.",
            3,
            420,
        ),
        (
            "L14_M04",
            "Katta villa",
            "400+ m² turar joylarni rejalashtirish.",
            4,
            480,
        ),
        (
            "L14_M05",
            "Ko'p avlodli oila",
            "Bir nechta avlod uchun uy.",
            5,
            360,
        ),
        (
            "L14_M06",
            "Premium fasad",
            "Yuqori darajadagi fasad kompozitsiyasi.",
            6,
            420,
        ),
        (
            "L14_M07",
            "Design Clinic",
            "Muammoli loyihalarni professional tuzatish.",
            7,
            480,
        ),
        (
            "L14_M08",
            "Advanced Case Studies",
            "Murakkab real vaziyatlarni yechish.",
            8,
            600,
        ),
    ],

    # --------------------------------------------------------
    # LEVEL 15
    # --------------------------------------------------------
    "LEVEL_15": [
        (
            "L15_M01",
            "PRO nazariya imtihoni",
            "Arxitektura bo'yicha yakuniy nazariya.",
            1,
            360,
        ),
        (
            "L15_M02",
            "Archicad PRO imtihoni",
            "Professional Archicad amaliyoti.",
            2,
            480,
        ),
        (
            "L15_M03",
            "Xatoni top PRO",
            "Murakkab loyihalardagi xatolarni topish.",
            3,
            360,
        ),
        (
            "L15_M04",
            "Final texnik topshiriq",
            "Yakuniy loyiha uchun yangi real vazifa.",
            4,
            180,
        ),
        (
            "L15_M05",
            "Final loyiha",
            "Mustaqil 1 yoki 2 qavatli turar joy loyihasi.",
            5,
            1200,
        ),
        (
            "L15_M06",
            "Loyihani himoya qilish",
            "Qarorlarni professional asoslash.",
            6,
            360,
        ),
        (
            "L15_M07",
            "Portfolio",
            "Professional portfolio tayyorlash.",
            7,
            360,
        ),
        (
            "L15_M08",
            "PRO Final",
            "Yakuniy baholash va natija.",
            8,
            300,
        ),
    ],
}


# ============================================================
# LEVEL 0 DAGI HOZIRGI 10 TA DARS
# ============================================================

STARTER_LESSONS = [
    (
        "L00_M01",
        "L00_M01_001",
        "Arxitektura nima?",
        "theory",
        "Arxitekturaning mohiyati va vazifasi.",
        1,
        15,
    ),
    (
        "L00_M01",
        "L00_M01_002",
        "Arxitektor kim?",
        "theory",
        "Arxitektorning real loyihadagi roli.",
        2,
        15,
    ),
    (
        "L00_M01",
        "L00_M01_003",
        "Loyiha nima?",
        "theory",
        "Loyiha tushunchasi va loyiha tarkibi.",
        3,
        20,
    ),
    (
        "L00_M02",
        "L00_M02_001",
        "Plan nima?",
        "theory",
        "Qavat rejasini o'qishning boshlang'ich qoidalari.",
        1,
        20,
    ),
    (
        "L00_M02",
        "L00_M02_002",
        "Fasad nima?",
        "theory",
        "Binoning tashqi ko'rinish chizmalarini tushunish.",
        2,
        20,
    ),
    (
        "L00_M02",
        "L00_M02_003",
        "Kesim nima?",
        "theory",
        "Binoning vertikal kesimini o'qish.",
        3,
        20,
    ),
    (
        "L00_M02",
        "L00_M02_004",
        "Genplan nima?",
        "theory",
        "Uy va uchastka munosabatini tushunish.",
        4,
        20,
    ),
    (
        "L00_M03",
        "L00_M03_001",
        "Masshtab tushunchasi",
        "theory",
        "1:50, 1:100 va boshqa masshtablarni tushunish.",
        1,
        25,
    ),
    (
        "L00_M03",
        "L00_M03_002",
        "O'lchamlarni o'qish",
        "practice",
        "Arxitektura chizmalaridagi o'lchamlarni aniqlash.",
        2,
        25,
    ),
    (
        "L00_M03",
        "L00_M03_003",
        "Otmetka va balandlik",
        "theory",
        "0.000 va boshqa balandlik belgilarini tushunish.",
        3,
        25,
    ),
]


# ============================================================
# DATABASE SEED
# ============================================================

def seed_course_structure():
    connection = get_connection()

    try:
        cursor = connection.cursor()

        # ----------------------------------------------------
        # LEVELS
        # ----------------------------------------------------

        for (
            code,
            title,
            subtitle,
            description,
            sort_order,
        ) in LEVELS:

            cursor.execute(
                """
                INSERT OR IGNORE INTO course_levels (
                    code,
                    title,
                    subtitle,
                    description,
                    sort_order
                )
                VALUES (?, ?, ?, ?, ?)
                """,
                (
                    code,
                    title,
                    subtitle,
                    description,
                    sort_order,
                ),
            )

        # ----------------------------------------------------
        # MODULES
        # ----------------------------------------------------

        for level_code, module_list in MODULES.items():

            cursor.execute(
                """
                SELECT id
                FROM course_levels
                WHERE code = ?
                """,
                (level_code,),
            )

            level_row = cursor.fetchone()

            if level_row is None:
                continue

            level_id = level_row["id"]

            for (
                module_code,
                title,
                description,
                sort_order,
                estimated_minutes,
            ) in module_list:

                cursor.execute(
                    """
                    INSERT OR IGNORE INTO course_modules (
                        level_id,
                        code,
                        title,
                        description,
                        sort_order,
                        estimated_minutes
                    )
                    VALUES (?, ?, ?, ?, ?, ?)
                    """,
                    (
                        level_id,
                        module_code,
                        title,
                        description,
                        sort_order,
                        estimated_minutes,
                    ),
                )

        # ----------------------------------------------------
        # LEVEL 0 LESSONS
        # ----------------------------------------------------

        for (
            module_code,
            lesson_code,
            title,
            lesson_type,
            summary,
            sort_order,
            estimated_minutes,
        ) in STARTER_LESSONS:

            cursor.execute(
                """
                SELECT id
                FROM course_modules
                WHERE code = ?
                """,
                (module_code,),
            )

            module_row = cursor.fetchone()

            if module_row is None:
                continue

            module_id = module_row["id"]

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
                    module_id,
                    lesson_code,
                    title,
                    lesson_type,
                    summary,
                    sort_order,
                    estimated_minutes,
                    10,
                    80,
                    1,
                ),
            )

        connection.commit()

    finally:
        connection.close()
