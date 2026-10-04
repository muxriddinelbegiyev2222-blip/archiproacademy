from PySide6.QtWidgets import (
    QFrame,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QScrollArea,
    QVBoxLayout,
    QWidget,
)


GLOSSARY = [
    ("BIM", "Building Information Modeling — bino haqidagi geometrik va ma'lumotli model bilan ishlash usuli."),
    ("Genplan", "Uchastkada bino, kirish, yo'l, ko'kalamzor, parking va boshqa tashqi elementlar joylashuvi."),
    ("Fasad", "Binoning tashqi ko'rinishi; old, yon va orqa tomon proyeksiyalari."),
    ("Kesim", "Binoni vertikal tekislik bilan kesib ko'rsatilgan chizma."),
    ("Plan", "Binoning gorizontal kesimi va xonalar joylashuvi ko'rsatilgan chizma."),
    ("Setback", "Bino bilan uchastka chegarasi yoki boshqa obyekt orasidagi chekinish masofasi."),
    ("Sill", "Deraza pastki qismi yoki deraza tokchasi sathi."),
    ("Head", "Deraza yoki eshik ochilishining yuqori sathi."),
    ("Opening", "Devor yoki konstruksiyadagi eshik, deraza va boshqa ochilish."),
    ("Grid", "O'qlar tizimi; elementlarni koordinatsiya qilish uchun ishlatiladi."),
    ("Level", "Balandlik yoki qavat sathi."),
    ("Storey", "Binoning qavati."),
    ("Slab", "Pol yoki orayopma plitasi."),
    ("Beam", "Yukni tayanchlarga uzatuvchi gorizontal konstruktiv element."),
    ("Column", "Vertikal yuk ko'taruvchi konstruktiv element."),
    ("Foundation", "Binodan keladigan yuklarni gruntga uzatuvchi poydevor."),
    ("Roof", "Tom konstruksiyasi va uning geometriyasi."),
    ("Elevation", "Fasad ko'rinishi yoki balandlik proyeksiyasi."),
    ("Section", "Kesim chizmasining inglizcha atamasi."),
    ("Detail", "Loyihaning kichik qismini yirik masshtabda tushuntiruvchi chizma."),
    ("Annotation", "O'lcham, belgi, yozuv va boshqa tushuntiruvchi grafik ma'lumot."),
    ("Dimension", "Chizmadagi o'lcham ko'rsatkichi."),
    ("Zone", "Xona yoki funksional hududni ma'lumot bilan belgilash vositasi."),
    ("Layer", "Elementlarni guruhlash va ko'rinishini boshqarish qatlami."),
    ("Hotlink", "Tashqi yoki takroriy model qismini bog'lab ishlatish usuli."),
    ("Template", "Oldindan tayyorlangan loyiha sozlamalari va standartlari to'plami."),
    ("Layout", "Chizmalarni varaqda joylashtirish sahifasi."),
    ("Publisher", "Archicad'da chizma va hujjatlarni eksport qilish tizimi."),
    ("SHNQ", "O'zbekistondagi shaharsozlik normalari va qoidalari."),
    ("Ergonomika", "Inson uchun qulay va xavfsiz o'lcham hamda harakat sharoitlarini tashkil qilish."),
]


class GlossaryPage(QWidget):
    def __init__(self):
        super().__init__()
        self.cards = []
        self.build_ui()

    def build_ui(self):
        root = QVBoxLayout(self)
        root.setContentsMargins(30, 26, 30, 24)
        root.setSpacing(16)

        header = QFrame()
        header.setObjectName("overviewHeader")
        h = QVBoxLayout(header)
        h.setContentsMargins(24, 20, 24, 20)

        title = QLabel("Terminlar lug'ati")
        title.setObjectName("overviewTitle")

        subtitle = QLabel(
            "Arxitektura, Archicad, BIM va qurilishda uchraydigan asosiy atamalar."
        )
        subtitle.setObjectName("overviewSubtitle")
        subtitle.setWordWrap(True)

        h.addWidget(title)
        h.addWidget(subtitle)
        root.addWidget(header)

        self.search = QLineEdit()
        self.search.setPlaceholderText("Masalan: BIM, fasad, setback, SHNQ...")
        self.search.setClearButtonEnabled(True)
        self.search.setStyleSheet(
            """
            QLineEdit {
                background-color: #0A1627;
                border: 1px solid #304763;
                border-radius: 10px;
                padding: 11px 14px;
                color: #E7EEF7;
                font-size: 14px;
            }
            QLineEdit:focus {
                border: 1px solid #4F86EB;
            }
            """
        )
        self.search.textChanged.connect(self.filter_terms)
        root.addWidget(self.search)

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)

        content = QWidget()
        self.list_layout = QVBoxLayout(content)
        self.list_layout.setContentsMargins(0, 0, 8, 20)
        self.list_layout.setSpacing(10)

        scroll.setWidget(content)
        root.addWidget(scroll, 1)

        self.render_terms(GLOSSARY)

    def render_terms(self, items):
        while self.list_layout.count():
            item = self.list_layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()

        for term, explanation in items:
            card = QFrame()
            card.setObjectName("levelOverviewCard")

            layout = QVBoxLayout(card)
            layout.setContentsMargins(18, 14, 18, 14)
            layout.setSpacing(6)

            t = QLabel(term)
            t.setObjectName("levelName")

            e = QLabel(explanation)
            e.setObjectName("levelDesc")
            e.setWordWrap(True)

            layout.addWidget(t)
            layout.addWidget(e)
            self.list_layout.addWidget(card)

        if not items:
            empty = QLabel("Mos termin topilmadi.")
            empty.setObjectName("overviewSubtitle")
            self.list_layout.addWidget(empty)

        self.list_layout.addStretch()

    def filter_terms(self, text):
        query = str(text or "").strip().lower()

        if not query:
            self.render_terms(GLOSSARY)
            return

        items = [
            item
            for item in GLOSSARY
            if (
                query in item[0].lower()
                or query in item[1].lower()
            )
        ]

        self.render_terms(items)
