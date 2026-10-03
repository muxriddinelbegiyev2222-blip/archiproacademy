from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QFrame,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QPushButton,
    QScrollArea,
    QVBoxLayout,
    QWidget,
)

from courses.course_service import get_user_course_stats
from ui.learning_window import LearningWindow
from ui.license_window import LicenseWindow


SECTION_DATA = {
    "Arxitektura": {
        "title": "Arxitektura",
        "subtitle": "Arxitekturani noldan professional fikrlashgacha o'rganish.",
        "items": [
            ("LEVEL 00", "Absolute Zero — arxitekturaga mutlaqo noldan kirish"),
            ("LEVEL 01", "Arxitektura asoslari"),
            ("LEVEL 02", "Fazoviy fikrlash va ergonomika"),
            ("LEVEL 03", "Uchastka va genplan"),
            ("LEVEL 04", "O'zbekiston sharoitidagi turar joy"),
        ],
    },

    "Archicad": {
        "title": "Archicad",
        "subtitle": "Archicad'ni boshlang'ichdan professional darajagacha o'rganish.",
        "items": [
            ("LEVEL 05", "Archicad boshlang'ich"),
            ("LEVEL 06", "Archicad o'rta daraja"),
            ("LEVEL 07", "Archicad yuqori daraja"),
        ],
    },

    "SHNQ va normativlar": {
        "title": "SHNQ va normativlar",
        "subtitle": "Loyihalashda normativ savodxonlik va tekshiruv.",
        "items": [
            ("LEVEL 09", "SHNQ va normativlar"),
            ("Amaliy tekshiruv", "Normativlarni loyihada to'g'ri qo'llash"),
        ],
    },

    "Amaliyot": {
        "title": "Amaliyot",
        "subtitle": "Nazariyani real loyiha vazifalarida mustahkamlash.",
        "items": [
            ("1 qavatli uy", "Texnik topshiriqdan tayyor loyihagacha"),
            ("2 qavatli uy", "Professional turar joy loyihasi"),
            ("Konstruksiya", "Arxitektor uchun konstruktiv fikrlash"),
            ("BIM", "Model va hujjatlar bilan ishlash"),
        ],
    },

    "Loyihalar": {
        "title": "Loyihalar",
        "subtitle": "O'quv jarayonidagi amaliy va yakuniy loyihalar.",
        "items": [
            ("1 qavatli loyiha", "Rejalashtirish, fasad va hujjatlar"),
            ("2 qavatli loyiha", "Murakkabroq turar joy loyihasi"),
            ("Yakuniy loyiha", "Portfolio darajasidagi loyiha"),
        ],
    },

    "Testlar": {
        "title": "Testlar",
        "subtitle": "Har bir darsdan keyingi bilim nazorati.",
        "items": [
            ("Dars testlari", "Har bir dars bo'yicha mini-test"),
            ("Natijalar", "Eng yaxshi natija va progress saqlanadi"),
            ("Takrorlash", "Tugallangan darslarni qayta ko'rish mumkin"),
        ],
    },

    "Imtihonlar": {
        "title": "Imtihonlar",
        "subtitle": "Har bir Level yakunidagi nazorat imtihonlari.",
        "items": [
            ("Level imtihoni", "Level yakunida bilimni tekshirish"),
            ("O'tish bali", "Talab qilingan natijaga erishish"),
            ("XP", "Imtihon natijasiga qarab XP olish"),
        ],
    },

    "Kutubxona": {
        "title": "Kutubxona",
        "subtitle": "ARCHIPRO UZ ichidagi o'quv materiallariga tezkor kirish.",
        "items": [
            ("Arxitektura", "Arxitektura asoslari va rejalashtirish"),
            ("Archicad", "Instrument va BIM workflow"),
            ("SHNQ", "Normativ savodxonlik"),
            ("Amaliy loyiha", "Uy loyihalash bo'yicha materiallar"),
        ],
    },

    "Portfolio": {
        "title": "Portfolio",
        "subtitle": "O'quv jarayonida bajarilgan ishlarni portfolio darajasiga olib chiqish.",
        "items": [
            ("Reja", "Uy rejalashtirish ishlari"),
            ("Fasad", "Fasad yechimlari"),
            ("Kesim", "Arxitektura kesimlari"),
            ("Final loyiha", "Yakuniy loyiha natijasi"),
        ],
    },

    "Sozlamalar": {
        "title": "Sozlamalar",
        "subtitle": "ARCHIPRO UZ foydalanuvchi va litsenziya ma'lumotlari.",
        "items": [
            ("Profil", "Foydalanuvchi hisob ma'lumotlari"),
            ("Litsenziya", "Faol litsenziyani tekshirish"),
        ],
    },
}


class MenuSectionWindow(QMainWindow):
    def __init__(
        self,
        user: dict,
        section_name: str,
    ):
        super().__init__()

        self.user = user
        self.section_name = section_name

        self.learning_window = None
        self.license_window = None

        self.setWindowTitle(
            f"ARCHIPRO UZ - {section_name}"
        )

        self.resize(
            1050,
            760,
        )

        self.setMinimumSize(
            850,
            600,
        )

        self.build_ui()

    def build_ui(self):
        central = QWidget()
        self.setCentralWidget(central)

        self.setStyleSheet(
            """
            QMainWindow {
                background-color: #0B1220;
            }

            QWidget {
                color: #F8FAFC;
                font-family: Segoe UI;
            }

            QScrollArea {
                border: none;
                background: transparent;
            }

            QLabel#title {
                font-size: 30px;
                font-weight: 800;
                color: #FFFFFF;
            }

            QLabel#subtitle {
                font-size: 14px;
                color: #94A3B8;
            }

            QFrame#card {
                background-color: #111827;
                border: 1px solid #1E293B;
                border-radius: 12px;
            }

            QLabel#cardTitle {
                font-size: 17px;
                font-weight: 700;
                color: #FFFFFF;
            }

            QLabel#cardText {
                font-size: 13px;
                color: #94A3B8;
            }

            QLabel#statValue {
                font-size: 26px;
                font-weight: 800;
                color: #FFFFFF;
            }

            QLabel#statTitle {
                font-size: 12px;
                color: #94A3B8;
            }

            QPushButton#primary {
                background-color: #2563EB;
                border: none;
                border-radius: 9px;
                padding: 13px 20px;
                color: #FFFFFF;
                font-size: 14px;
                font-weight: 700;
            }

            QPushButton#primary:hover {
                background-color: #3B82F6;
            }

            QPushButton#secondary {
                background-color: #1E293B;
                border: 1px solid #334155;
                border-radius: 9px;
                padding: 13px 20px;
                color: #FFFFFF;
                font-size: 14px;
                font-weight: 600;
            }

            QPushButton#secondary:hover {
                background-color: #334155;
            }
            """
        )

        root = QVBoxLayout(central)

        root.setContentsMargins(
            32,
            28,
            32,
            28,
        )

        root.setSpacing(
            18
        )

        data = SECTION_DATA.get(
            self.section_name,
            {
                "title": self.section_name,
                "subtitle": "ARCHIPRO UZ bo'limi.",
                "items": [],
            },
        )

        title = QLabel(
            data["title"]
        )

        title.setObjectName(
            "title"
        )

        subtitle = QLabel(
            data["subtitle"]
        )

        subtitle.setObjectName(
            "subtitle"
        )

        subtitle.setWordWrap(
            True
        )

        root.addWidget(
            title
        )

        root.addWidget(
            subtitle
        )

        # ====================================================
        # STATISTIKA
        # ====================================================

        if self.section_name == "Statistika":
            self.build_statistics(
                root
            )

        else:
            scroll = QScrollArea()

            scroll.setWidgetResizable(
                True
            )

            scroll_content = QWidget()

            scroll_layout = QVBoxLayout(
                scroll_content
            )

            scroll_layout.setContentsMargins(
                0,
                5,
                8,
                5,
            )

            scroll_layout.setSpacing(
                12
            )

            for item_title, item_text in data["items"]:

                card = QFrame()

                card.setObjectName(
                    "card"
                )

                card_layout = QVBoxLayout(
                    card
                )

                card_layout.setContentsMargins(
                    20,
                    17,
                    20,
                    17,
                )

                card_title = QLabel(
                    item_title
                )

                card_title.setObjectName(
                    "cardTitle"
                )

                card_text = QLabel(
                    item_text
                )

                card_text.setObjectName(
                    "cardText"
                )

                card_text.setWordWrap(
                    True
                )

                card_layout.addWidget(
                    card_title
                )

                card_layout.addWidget(
                    card_text
                )

                scroll_layout.addWidget(
                    card
                )

            scroll_layout.addStretch()

            scroll.setWidget(
                scroll_content
            )

            root.addWidget(
                scroll,
                1,
            )

        # ====================================================
        # BUTTONS
        # ====================================================

        buttons = QHBoxLayout()

        learning_button = QPushButton(
            "O'QUV DASTURINI OCHISH"
        )

        learning_button.setObjectName(
            "primary"
        )

        learning_button.clicked.connect(
            self.open_learning
        )

        buttons.addWidget(
            learning_button
        )

        if self.section_name == "Sozlamalar":

            license_button = QPushButton(
                "LITSENZIYA MA'LUMOTLARI"
            )

            license_button.setObjectName(
                "secondary"
            )

            license_button.clicked.connect(
                self.open_license
            )

            buttons.addWidget(
                license_button
            )

        buttons.addStretch()

        root.addLayout(
            buttons
        )

    def build_statistics(
        self,
        root,
    ):
        stats = get_user_course_stats(
            self.user["id"]
        )

        row = QHBoxLayout()

        values = [
            (
                "Umumiy progress",
                f"{stats.get('progress_percent', 0)}%",
            ),
            (
                "Tugallangan dars",
                (
                    f"{stats.get('completed_lessons', 0)}/"
                    f"{stats.get('total_lessons', 0)}"
                ),
            ),
            (
                "Jami XP",
                str(
                    stats.get(
                        "xp",
                        0,
                    )
                ),
            ),
        ]

        for title_text, value_text in values:

            card = QFrame()

            card.setObjectName(
                "card"
            )

            layout = QVBoxLayout(
                card
            )

            layout.setContentsMargins(
                20,
                20,
                20,
                20,
            )

            stat_title = QLabel(
                title_text
            )

            stat_title.setObjectName(
                "statTitle"
            )

            stat_value = QLabel(
                value_text
            )

            stat_value.setObjectName(
                "statValue"
            )

            layout.addWidget(
                stat_title
            )

            layout.addWidget(
                stat_value
            )

            row.addWidget(
                card
            )

        root.addLayout(
            row
        )

        info = QFrame()

        info.setObjectName(
            "card"
        )

        info_layout = QVBoxLayout(
            info
        )

        lesson_xp = stats.get(
            "lesson_xp",
            0,
        )

        exam_xp = stats.get(
            "exam_xp",
            0,
        )

        details = QLabel(
            f"Darslardan: {lesson_xp} XP\n"
            f"Imtihonlardan: {exam_xp} XP"
        )

        details.setObjectName(
            "cardText"
        )

        info_layout.addWidget(
            details
        )

        root.addWidget(
            info
        )

        root.addStretch()

    def open_learning(
        self,
    ):
        self.learning_window = LearningWindow(
            self.user
        )

        self.learning_window.show()

        self.learning_window.raise_()

        self.learning_window.activateWindow()

    def open_license(
        self,
    ):
        self.license_window = LicenseWindow(
            self.user
        )

        self.license_window.show()

        self.license_window.raise_()

        self.license_window.activateWindow()
