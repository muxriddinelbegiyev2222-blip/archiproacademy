from database.database import get_connection


LEVEL09_MODULE06_LESSONS = [
    ("L09_M06", "L09_M06_001", "Evakuatsiya tushunchasi", "theory", "Favqulodda vaziyatda odamlarning xavfsiz hududga chiqish mantig'ini tushunish.", 1, 30, 20),
    ("L09_M06", "L09_M06_002", "Evakuatsiya yo'li", "theory", "Xonadan chiqishgacha bo'lgan yo'lning uzluksizligi va tushunarliligini tahlil qilish.", 2, 35, 20),
    ("L09_M06", "L09_M06_003", "Eshik, koridor va zinapoya", "practice", "Evakuatsiya yo'lidagi asosiy arxitektura elementlarini koordinatsiya qilish.", 3, 35, 20),
    ("L09_M06", "L09_M06_004", "To'siqlar va xato ssenariylar", "practice", "Evakuatsiya yo'lini buzadigan tipik arxitektura xatolarini aniqlash.", 4, 40, 20),
    ("L09_M06", "L09_M06_005", "Evakuatsiya professional audit", "practice", "Evakuatsiya yo'llarini kompleks checklist asosida tekshirish.", 5, 40, 25),
]


LEVEL09_MODULE06_CONTENT = {
    "L09_M06_001": [
        {"title": "Evakuatsiya nima?", "type": "highlight", "text": "Evakuatsiya — odamlarning xavfli zonadan xavfsiz yo'nalishda chiqishini tashkil qiluvchi tizim."},
        {"title": "Boshlanish nuqtasi", "type": "normal", "text": "Evakuatsiya tahlili odam qayerda turganidan va xavfsiz chiqishgacha qanday yo'l bosib o'tishidan boshlanadi."},
        {"title": "Aniq qiymatlar", "type": "warning", "text": "Evakuatsiya masofasi yoki kengligini amaldagi normativ manbasiz yoddan kiritmang."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Bir xonadan tashqarigacha bo'lgan chiqish yo'lini bosqichma-bosqich yozing."},
    ],

    "L09_M06_002": [
        {"title": "Yo'l uzluksizligi", "type": "highlight", "text": "Evakuatsiya yo'li xonadan boshlanib, kerakli oraliq zonalar orqali xavfsiz chiqishga olib borishi kerak."},
        {"title": "To'siqlar", "type": "warning", "text": "Mebel, eshik konfliktilari, torayish yoki boshi berk yo'l favqulodda chiqishni qiyinlashtirishi mumkin."},
        {"title": "Tushunarli yo'nalish", "type": "normal", "text": "Foydalanuvchi yo'lni intuitiv va xavfsiz tarzda davom ettira olishi kerak."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Plan bo'yicha boshi berk yoki to'siq bo'lishi mumkin bo'lgan nuqtalarni belgilang."},
    ],

    "L09_M06_003": [
        {"title": "Eshik", "type": "normal", "text": "Evakuatsiya yo'lidagi eshiklar harakat zanjirining muhim qismlaridir."},
        {"title": "Koridor", "type": "normal", "text": "Koridor va hall foydalanuvchini xavfsiz chiqishga olib boruvchi circulation tizimida ishlaydi."},
        {"title": "Zinapoya", "type": "highlight", "text": "Ko'p qavatli holatda zinapoya vertikal evakuatsiya yo'lining muhim elementi bo'lishi mumkin."},
        {"title": "Faqat dizayn emas", "type": "warning", "text": "Eshik, koridor va zinapoyani faqat estetik element sifatida ko'rmang."},
        {"title": "Mini-amaliyot", "type": "example", "text": "Eshik, koridor va zinapoya uchun bittadan evakuatsiya audit savolini yozing."},
    ],

    "L09_M06_004": [
        {"title": "Xato ssenariy", "type": "highlight", "text": "Favqulodda holatda normal kundalik vaziyatda sezilmaydigan xatolar jiddiy muammoga aylanishi mumkin."},
        {"title": "Misollar", "type": "normal", "text": "Qulflangan eshik, to'silgan koridor, keraksiz mebel, noaniq yo'nalish yoki chiqish oldidagi to'siq muammo bo'lishi mumkin."},
        {"title": "Kundalik holat yetmaydi", "type": "warning", "text": "Kundalik circulation ishlayotgani favqulodda vaziyatda ham xavfsiz degani emas."},
        {"title": "Mini-amaliyot", "type": "example", "text": "5 ta xato evakuatsiya ssenariysi va har biri uchun yechim prinsipini yozing."},
    ],

    "L09_M06_005": [
        {"title": "Evakuatsiya audit", "type": "highlight", "text": "Foydalanuvchi → boshlanish nuqtasi → yo'l → eshik → koridor/hall → zinapoya → tashqi chiqish → normativ tekshiruv."},
        {"title": "Audit status", "type": "normal", "text": "Har bir muammo uchun joy, tavsif, manba, status va yechim qayd qilinadi."},
        {"title": "Faqat belgi yetmaydi", "type": "warning", "text": "Faqat chiqish belgisi qo'yish bilan evakuatsiya masalasi to'liq hal bo'lmaydi."},
        {"title": "Professional checklist", "type": "example", "text": "1. Boshlanish nuqtasi aniqmi?<br><br>2. Yo'l uzluksizmi?<br><br>3. Eshiklar tekshirildimi?<br><br>4. Koridor/hall konfliktlari yo'qmi?<br><br>5. Zinapoya kerakli holatda ishlaydimi?<br><br>6. Tashqi chiqish aniqmi?<br><br>7. Tegishli normativ tekshirildimi?"},
    ],
}


LEVEL09_MODULE06_QUIZ = {
    "L09_M06_001": [
        {"code": "L09_Q076", "question": "Evakuatsiya odamlarni xavfli zonadan xavfsiz chiqishga olib borish tizimimi?", "explanation": "Bu evakuatsiyaning asosiy mantig'idir.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
        {"code": "L09_Q077", "question": "Evakuatsiya faqat chiqish belgisi bilan hal bo'ladimi?", "explanation": "Yo'lning o'zi va barcha elementlar tekshiriladi.", "options": [("A", "Ha", False), ("B", "Yo'q", True)]},
        {"code": "L09_Q078", "question": "Aniq evakuatsiya o'lchamlarini normativdan tekshirish kerakmi?", "explanation": "Aniq talablar tegishli amaldagi manbaga tayanadi.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
    ],
    "L09_M06_002": [
        {"code": "L09_Q079", "question": "Evakuatsiya yo'li uzluksiz bo'lishi kerakmi?", "explanation": "Yo'l xavfsiz chiqishgacha davom etadi.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
        {"code": "L09_Q080", "question": "Boshi berk yo'l evakuatsiya masalasiga ta'sir qilishi mumkinmi?", "explanation": "Yo'l strukturasiga qarab bu muammo bo'lishi mumkin.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
        {"code": "L09_Q081", "question": "Mebel evakuatsiya yo'lini to'sishi mumkinmi?", "explanation": "Harakat yo'li amalda ham ochiq qolishi kerak.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
    ],
    "L09_M06_003": [
        {"code": "L09_Q082", "question": "Eshik evakuatsiya tizimining elementi bo'lishi mumkinmi?", "explanation": "Eshik harakat zanjirining muhim qismidir.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
        {"code": "L09_Q083", "question": "Koridor va hall evakuatsiya bilan bog'liqmi?", "explanation": "Ular odamning xavfsiz chiqish yo'lida bo'lishi mumkin.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
        {"code": "L09_Q084", "question": "Zinapoya faqat estetik elementmi?", "explanation": "Ko'p qavatli binoda u xavfsiz vertikal harakat uchun ham muhim.", "options": [("A", "Ha", False), ("B", "Yo'q", True)]},
    ],
    "L09_M06_004": [
        {"code": "L09_Q085", "question": "Qulflangan eshik evakuatsiya muammosiga aylanishi mumkinmi?", "explanation": "Favqulodda vaziyatda chiqish imkoniyati muhim.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
        {"code": "L09_Q086", "question": "Kundalik circulation yaxshi bo'lsa evakuatsiyani alohida tekshirish shart emasmi?", "explanation": "Favqulodda holat alohida ssenariy sifatida ko'riladi.", "options": [("A", "Ha", False), ("B", "Yo'q", True)]},
        {"code": "L09_Q087", "question": "Evakuatsiyada xato ssenariylarni oldindan tahlil qilish foydalimi?", "explanation": "Bu potensial xavflarni loyiha bosqichida aniqlashga yordam beradi.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
    ],
    "L09_M06_005": [
        {"code": "L09_Q088", "question": "Evakuatsiya auditida tashqi chiqishgacha bo'lgan butun yo'l tekshiriladimi?", "explanation": "Audit yo'lning barcha qismlarini qamrab oladi.", "options": [("A", "Ha", True), ("B", "Yo'q", False)]},
        {"code": "L09_Q089", "question": "Faqat chiqish belgisi qo'yish butun evakuatsiya auditini almashtiradimi?", "explanation": "Arxitektura yo'li va elementlar ham tekshiriladi.", "options": [("A", "Ha", False), ("B", "Yo'q", True)]},
        {"code": "L09_Q090", "question": "Evakuatsiya auditining to'g'ri workflow'i qaysi?", "explanation": "Foydalanuvchidan tashqi chiqishgacha bo'lgan yo'l ketma-ket tekshiriladi.", "options": [("A", "Foydalanuvchi → yo'l → eshik → koridor/zinapoya → tashqi chiqish → audit", True), ("B", "Faqat exit belgisi → yakunlash", False)]},
    ],
}


def seed_level09_module06():
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
        ) in LEVEL09_MODULE06_LESSONS:

            cursor.execute(
                "SELECT id FROM course_modules WHERE code = ? LIMIT 1",
                (module_code,),
            )

            module = cursor.fetchone()

            if module is None:
                continue

            cursor.execute(
                """
                INSERT INTO lessons (
                    module_id, code, title, lesson_type, summary,
                    sort_order, estimated_minutes, xp_reward,
                    passing_score, is_required
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
