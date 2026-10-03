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

from ui.learning_window import LearningWindow
from ui.license_window import LicenseWindow


SECTION_DATA = {
    "Arxitektura": {
        "title": "Arxitektura",
        "subtitle": "Arxitekturani noldan professional fikrlashgacha o'rganish.",
        "section_levels": [
            "LEVEL_00",
            "LEVEL_01",
            "LEVEL_02",
            "LEVEL_03",
            "LEVEL_04",
        ],
        "items": [
            {
                "title": "LEVEL 00",
                "subtitle": "Absolute Zero — arxitekturaga mutlaqo noldan kirish",
                "levels": ["LEVEL_00"],
            },
            {
                "title": "LEVEL 01",
                "subtitle": "Arxitektura asoslari",
                "levels": ["LEVEL_01"],
            },
            {
                "title": "LEVEL 02",
                "subtitle": "Fazoviy fikrlash va ergonomika",
                "levels": ["LEVEL_02"],
            },
            {
                "title": "LEVEL 03",
                "subtitle": "Uchastka va genplan",
                "levels": ["LEVEL_03"],
            },
            {
                "title": "LEVEL 04",
                "subtitle": "O'zbekiston sharoitidagi turar joy",
                "levels": ["LEVEL_04"],
            },
        ],
    },

    "Archicad": {
        "title": "Archicad",
        "subtitle": "Archicad'ni boshlang'ichdan professional darajagacha o'rganish.",
        "section_levels": [
            "LEVEL_05",
            "LEVEL_06",
            "LEVEL_07",
        ],
        "items": [
            {
                "title": "LEVEL 05",
                "subtitle": "Archicad boshlang'ich",
                "levels": ["LEVEL_05"],
            },
            {
                "title": "LEVEL 06",
                "subtitle": "Archicad o'rta daraja",
                "levels": ["LEVEL_06"],
            },
            {
                "title": "LEVEL 07",
                "subtitle": "Archicad yuqori daraja",
                "levels": ["LEVEL_07"],
            },
        ],
    },

    "SHNQ va normativlar": {
        "title": "SHNQ va normativlar",
        "subtitle": "Loyihalashda normativ savodxonlik va tekshiruv.",
        "section_levels": [
            "LEVEL_09",
        ],
        "items": [
            {
                "title": "LEVEL 09",
                "subtitle": "SHNQ va normativlar",
                "levels": ["LEVEL_09"],
            },
            {
                "title": "Amaliy tekshiruv",
                "subtitle": "Normativlarni loyihada to'g'ri qo'llash",
                "levels": ["LEVEL_09"],
            },
        ],
    },

    "Amaliyot": {
        "title": "Amaliyot",
        "subtitle": "Nazariy bilimlarni amaliy vazifalarda mustahkamlash.",
        "section_levels": [
            "LEVEL_08",
            "LEVEL_10",
            "LEVEL_11",
            "LEVEL_12",
            "LEVEL_13",
            "LEVEL_14",
            "LEVEL_15",
        ],
        "items": [
            {
                "title": "Konstruksiya",
                "subtitle": "Qurilish konstruksiyalari va amaliy yechimlar",
                "levels": ["LEVEL_08"],
            },
            {
                "title": "1 qavatli uy",
                "subtitle": "Bir qavatli turar joyni professional loyihalash",
                "levels": ["LEVEL_10"],
            },
            {
                "title": "2 qavatli uy",
                "subtitle": "Ikki qavatli turar joyni professional loyihalash",
                "levels": ["LEVEL_11"],
            },
            {
                "title": "Professional amaliyot",
                "subtitle": "Yuqori bosqichdagi loyiha va amaliy mashqlar",
                "levels": [
                    "LEVEL_12",
                    "LEVEL_13",
                    "LEVEL_14",
                    "LEVEL_15",
                ],
            },
        ],
    },

    "Loyihalar": {
        "title": "Loyihalar",
        "subtitle": "Turar joy loyihalarini bosqichma-bosqich ishlab chiqish.",
        "section_levels": [
            "LEVEL_10",
            "LEVEL_11",
            "LEVEL_12",
            "LEVEL_13",
            "LEVEL_14",
            "LEVEL_15",
        ],
        "items": [
            {
                "title": "1 qavatli uy loyihasi",
                "subtitle": "Texnik topshiriqdan loyiha albomigacha",
                "levels": ["LEVEL_10"],
            },
            {
                "title": "2 qavatli uy loyihasi",
                "subtitle": "Murakkab turar joy loyihasi",
                "levels": ["LEVEL_11"],
            },
            {
                "title": "Yakuniy loyiha",
                "subtitle": "Professional yakuniy loyiha va portfolio",
                "levels": [
                    "LEVEL_12",
                    "LEVEL_13",
                    "LEVEL_14",
                    "LEVEL_15",
                ],
            },
        ],
    },

    "Testlar": {
        "title": "Testlar",
        "subtitle": "Darslar bo'yicha bilimni tekshirish.",
        "section_levels": [],
        "items": [
            {
                "title": "Barcha dars testlari",
                "subtitle": "Kerakli Levelni tanlang va dars testlarini bajaring",
                "levels": [],
            },
        ],
    },

    "Imtihonlar": {
        "title": "Imtihonlar",
        "subtitle": "Level yakuniy imtihonlariga kirish.",
        "section_levels": [],
        "items": [
            {
                "title": "Barcha yakuniy imtihonlar",
                "subtitle": "Level yakuniy imtihonlari o'quv dasturi ichida joylashgan",
                "levels": [],
            },
        ],
    },

    "Kutubxona": {
        "title": "Kutubxona",
        "subtitle": "ARCHIPRO UZ o'quv materiallari.",
        "section_levels": [],
        "items": [
            {
                "title": "Arxitektura materiallari",
                "subtitle": "Arxitektura va turar joy loyihalash bo'yicha bilimlar",
                "levels": [
                    "LEVEL_00",
                    "LEVEL_01",
                    "LEVEL_02",
                    "LEVEL_03",
                    "LEVEL_04",
                ],
            },
            {
                "title": "Archicad materiallari",
                "subtitle": "Archicad va BIM bo'yicha darslar",
                "levels": [
                    "LEVEL_05",
                    "LEVEL_06",
                    "LEVEL_07",
                ],
            },
            {
                "title": "Normativ materiallar",
                "subtitle": "SHNQ va normativ savodxonlik",
                "levels": ["LEVEL_09"],
            },
        ],
    },

    "Portfolio": {
        "title": "Portfolio",
        "subtitle": "Professional portfolio uchun loyiha bilimlari.",
        "section_levels": [
            "LEVEL_10",
            "LEVEL_11",
            "LEVEL_12",
            "LEVEL_13",
            "LEVEL_14",
            "LEVEL_15",
        ],
        "items": [
            {
                "title": "Portfolio tayyorlash",
                "subtitle": "Professional loyiha va taqdimot bosqichlari",
                "levels": [
                    "LEVEL_10",
                    "LEVEL_11",
                    "LEVEL_12",
                    "LEVEL_13",
                    "LEVEL_14",
                    "LEVEL_15",
                ],
            },
        ],
    },

    "Statistika": {
        "title": "Statistika",
        "subtitle": "O'quv progressi va natijalaringiz.",
        "section_levels": [],
        "items": [
            {
                "title": "O'quv progressi",
                "subtitle": "Darslar, testlar, imtihonlar va XP natijalari",
                "levels": [],
            },
        ],
    },

    "Sozlamalar": {
        "title": "Sozlamalar",
        "subtitle": "Profil va ARCHIPRO UZ sozlamalari.",
        "section_levels": [],
        "items": [
            {
                "title": "Litsenziya ma'lumotlari",
                "subtitle": "Faol litsenziya va Device ID ma'lumotlari",
                "action": "license",
                "levels": [],
            },
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

        self.section_data = SECTION_DATA.get(
            section_name,
            {
                "title": section_name,
                "subtitle": "ARCHIPRO UZ bo'limi.",
                "section_levels": [],
                "items": [],
            },
        )

        self.setWindowTitle(
            f"ARCHIPRO UZ - {self.section_data['title']}"
        )

        self.setup_styles()
        self.build_ui()

    # ========================================================
    # STYLE
    # ========================================================

    def setup_styles(self):
        self.setStyleSheet(
            """
            QMainWindow {
                background-color: #0B1220;
            }

            QWidget {
                color: #F8FAFC;
                font-family: Segoe UI;
            }

            QWidget#pageRoot {
                background-color: #0B1220;
            }

            QWidget#scrollContent {
                background-color: #0B1220;
            }

            QScrollArea {
                background-color: #0B1220;
                border: none;
            }

            QScrollArea > QWidget {
                background-color: #0B1220;
            }

            QScrollArea > QWidget > QWidget {
                background-color: #0B1220;
            }

            QAbstractScrollArea::viewport {
                background-color: #0B1220;
            }

            QLabel#pageTitle {
                font-size: 30px;
                font-weight: 800;
                color: #FFFFFF;
                background-color: transparent;
            }

            QLabel#pageSubtitle {
                font-size: 14px;
                color: #94A3B8;
                background-color: transparent;
            }

            QFrame#sectionCard {
                background-color: #111827;
                border: 1px solid #1E293B;
                border-radius: 14px;
            }

            QLabel#cardTitle {
                font-size: 17px;
                font-weight: 700;
                color: #FFFFFF;
                background-color: transparent;
            }

            QLabel#cardSubtitle {
                font-size: 13px;
                color: #94A3B8;
                background-color: transparent;
            }

            QPushButton#openButton {
                background-color: #2563EB;
                color: #FFFFFF;
                border: none;
                border-radius: 9px;
                padding: 11px 17px;
                font-size: 13px;
                font-weight: 700;
            }

            QPushButton#openButton:hover {
                background-color: #3B82F6;
            }

            QFrame#topInfo {
                background-color: #111827;
                border: 1px solid #1E293B;
                border-radius: 14px;
            }

            QScrollBar:vertical {
                background-color: #0F172A;
                width: 11px;
            }

            QScrollBar::handle:vertical {
                background-color: #334155;
                min-height: 30px;
                border-radius: 5px;
            }

            QScrollBar::handle:vertical:hover {
                background-color: #475569;
            }

            QScrollBar::add-line:vertical,
            QScrollBar::sub-line:vertical {
                height: 0px;
            }
            """
        )

    # ========================================================
    # UI
    # ========================================================

    def build_ui(self):
        central = QWidget()

        central.setObjectName(
            "pageRoot"
        )

        central.setStyleSheet(
            """
            QWidget#pageRoot {
                background-color: #0B1220;
            }
            """
        )

        self.setCentralWidget(
            central
        )

        root = QVBoxLayout(
            central
        )

        root.setContentsMargins(
            34,
            30,
            34,
            24,
        )

        root.setSpacing(
            18
        )

        title = QLabel(
            self.section_data[
                "title"
            ]
        )

        title.setObjectName(
            "pageTitle"
        )

        subtitle = QLabel(
            self.section_data[
                "subtitle"
            ]
        )

        subtitle.setObjectName(
            "pageSubtitle"
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

        scroll = QScrollArea()

        scroll.setWidgetResizable(
            True
        )

        scroll.setFrameShape(
            QScrollArea.Shape.NoFrame
        )

        scroll.setStyleSheet(
            """
            QScrollArea {
                background-color: #0B1220;
                border: none;
            }

            QScrollArea QWidget {
                background-color: #0B1220;
            }

            QAbstractScrollArea::viewport {
                background-color: #0B1220;
            }
            """
        )

        scroll.viewport().setStyleSheet(
            """
            background-color: #0B1220;
            """
        )

        scroll_content = QWidget()

        scroll_content.setObjectName(
            "scrollContent"
        )

        scroll_content.setStyleSheet(
            """
            QWidget#scrollContent {
                background-color: #0B1220;
            }
            """
        )

        scroll_layout = QVBoxLayout(
            scroll_content
        )

        scroll_layout.setContentsMargins(
            0,
            5,
            8,
            20,
        )

        scroll_layout.setSpacing(
            12
        )

        for item in self.section_data[
            "items"
        ]:
            card = self.create_item_card(
                item
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

    # ========================================================
    # CARD
    # ========================================================

    def create_item_card(
        self,
        item: dict,
    ):
        card = QFrame()

        card.setObjectName(
            "sectionCard"
        )

        layout = QHBoxLayout(
            card
        )

        layout.setContentsMargins(
            20,
            18,
            20,
            18,
        )

        layout.setSpacing(
            16
        )

        text_area = QVBoxLayout()

        title = QLabel(
            item["title"]
        )

        title.setObjectName(
            "cardTitle"
        )

        subtitle = QLabel(
            item["subtitle"]
        )

        subtitle.setObjectName(
            "cardSubtitle"
        )

        subtitle.setWordWrap(
            True
        )

        text_area.addWidget(
            title
        )

        text_area.addWidget(
            subtitle
        )

        layout.addLayout(
            text_area
        )

        layout.addStretch()

        button = QPushButton(
            "OCHISH  →"
        )

        button.setObjectName(
            "openButton"
        )

        button.setCursor(
            Qt.CursorShape.PointingHandCursor
        )

        button.clicked.connect(
            lambda checked=False, data=item:
            self.open_item(
                data
            )
        )

        layout.addWidget(
            button
        )

        return card

    # ========================================================
    # OPEN ITEM
    # ========================================================

    def open_item(
        self,
        item: dict,
    ):
        if item.get(
            "action"
        ) == "license":

            self.license_window = LicenseWindow(
                self.user
            )

            self.license_window.show()

            return

        level_codes = item.get(
            "levels",
            []
        )

        self.learning_window = LearningWindow(
            user=self.user,
            focus_level_codes=level_codes,
            custom_title=item["title"],
            custom_subtitle=item["subtitle"],
        )

        self.learning_window.show()

    # ========================================================
    # WHOLE SECTION
    # ========================================================

    def open_whole_section(
        self,
    ):
        self.learning_window = LearningWindow(
            user=self.user,
            focus_level_codes=self.section_data.get(
                "section_levels",
                [],
            ),
            custom_title=self.section_data[
                "title"
            ],
            custom_subtitle=self.section_data[
                "subtitle"
            ],
        )

        self.learning_window.show()
