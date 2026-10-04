from PySide6.QtWidgets import (
    QFrame,
    QLabel,
    QScrollArea,
    QVBoxLayout,
    QWidget,
)


HELP_ITEMS = [
    (
        "Dasturga qanday kiraman?",
        "Birinchi ishga tushirishda Device ID chiqadi. Shu Device ID asosida yaratilgan .archiprolic faylni tanlaysiz. Aktivatsiyadan keyin litsenziyada berilgan login va parol bilan kirasiz.",
    ),
    (
        "Darslar qanday ochiladi?",
        "PRO rejimida darslar ketma-ket ochiladi. Joriy dars va uning mini-testini muvaffaqiyatli yakunlaganingizdan keyin keyingi dars ochiladi.",
    ),
    (
        "MASTER rejimi nima?",
        "MASTER — faqat dastur egasi uchun test rejimi. U barcha Level, dars va imtihonlarni blokirovkasiz tekshirish imkonini beradi.",
    ),
    (
        "Progress qayerda saqlanadi?",
        "Progress lokal SQLite bazada saqlanadi. Sozlamalar bo'limidan progress backup yaratish va keyin uni tiklash mumkin.",
    ),
    (
        "Bookmark nima?",
        "Muhim darsni saqlab qo'yish uchun dars ichidagi BOOKMARK tugmasidan foydalaning. Keyin Kutubxonada bookmark qilingan darslarni topish oson bo'ladi.",
    ),
    (
        "Eslatma qanday yoziladi?",
        "Har bir dars ichida Mening eslatmam maydoni bor. Yozgan matningiz shu foydalanuvchi uchun lokal saqlanadi.",
    ),
    (
        "Qidiruvni qanday tez ochaman?",
        "Ctrl+K tugmalarini bosing. Kutubxona ochiladi va qidiruv maydoni fokusga keladi.",
    ),
    (
        "Orqaga tez qaytish",
        "Dars, mini-test yoki imtihonda Esc tugmasi oldingi sahifaga qaytish uchun ishlatiladi.",
    ),
    (
        "Keyingi darsga o'tish",
        "Dars mini-testidan o'tgach KEYINGI DARS tugmasi orqali navbatdagi ochilgan darsga o'tishingiz mumkin.",
    ),
    (
        "Windows qayta o'rnatilsa nima qilaman?",
        "Oldindan Sozlamalar → Progress backup orqali .archiprobackup fayl yarating. Keyin yangi aktivatsiyadan so'ng shu faylni import qiling.",
    ),
    (
        "Internet kerakmi?",
        "Yo'q. ARCHIPRO UZ asosiy o'quv jarayoni va litsenziya tekshiruvi offline ishlaydi.",
    ),
]


class HelpPage(QWidget):
    def __init__(self):
        super().__init__()
        self.build_ui()

    def build_ui(self):
        root = QVBoxLayout(self)
        root.setContentsMargins(30, 26, 30, 24)
        root.setSpacing(16)

        header = QFrame()
        header.setObjectName("overviewHeader")
        h = QVBoxLayout(header)
        h.setContentsMargins(24, 20, 24, 20)

        title = QLabel("Yordam markazi")
        title.setObjectName("overviewTitle")

        subtitle = QLabel(
            "ARCHIPRO UZ dan foydalanish bo'yicha qisqa va amaliy qo'llanma."
        )
        subtitle.setObjectName("overviewSubtitle")
        subtitle.setWordWrap(True)

        h.addWidget(title)
        h.addWidget(subtitle)
        root.addWidget(header)

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)

        content = QWidget()
        layout = QVBoxLayout(content)
        layout.setContentsMargins(0, 0, 8, 20)
        layout.setSpacing(10)

        for question, answer in HELP_ITEMS:
            card = QFrame()
            card.setObjectName("levelOverviewCard")

            c = QVBoxLayout(card)
            c.setContentsMargins(18, 14, 18, 14)
            c.setSpacing(6)

            q = QLabel(question)
            q.setObjectName("levelName")
            q.setWordWrap(True)

            a = QLabel(answer)
            a.setObjectName("levelDesc")
            a.setWordWrap(True)

            c.addWidget(q)
            c.addWidget(a)
            layout.addWidget(card)

        layout.addStretch()

        scroll.setWidget(content)
        root.addWidget(scroll, 1)
