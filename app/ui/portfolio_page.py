from PySide6.QtCore import Signal
from PySide6.QtWidgets import (
    QFrame,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QScrollArea,
    QVBoxLayout,
    QWidget,
)


class PortfolioPage(QWidget):
    open_levels_requested = Signal(
        list,
        str,
        str,
    )

    def __init__(
        self,
        user: dict,
    ):
        super().__init__()

        self.user = user

        self.setObjectName(
            "portfolioPage"
        )

        self.setup_styles()
        self.build_ui()

    def setup_styles(self):
        self.setStyleSheet(
            """
            QWidget#portfolioPage {
                background-color: #F5F1E7;
            }

            QScrollArea {
                background-color: #F5F1E7;
                border: none;
            }

            QAbstractScrollArea::viewport {
                background-color: #F5F1E7;
            }

            QWidget#portfolioContent {
                background-color: #F5F1E7;
            }

            QLabel#pageTitle {
                color: #203B36;
                font-size: 32px;
                font-weight: 800;
            
                font-family: "Georgia";
}

            QLabel#pageSubtitle {
                color: #586B64;
                font-size: 14px;
            }

            QFrame#heroCard {
                background-color: #FFFDF7;
                border: 1px solid #D5CBBB;
                border-radius: 16px;
            }

            QFrame#portfolioCard {
                background-color: #FFFDF7;
                border: 1px solid #D5CBBB;
                border-radius: 14px;
            }

            QFrame#finalCard {
                background-color: #F4E9D7;
                border: 1px solid #D5CBBB;
                border-radius: 14px;
            }

            QLabel#heroTitle {
                color: #203B36;
                font-size: 21px;
                font-weight: 800;
            
                font-family: "Georgia";
}

            QLabel#cardTitle {
                color: #203B36;
                font-size: 17px;
                font-weight: 700;
            }

            QLabel#cardText {
                color: #586B64;
                font-size: 13px;
            }

            QLabel#badge {
                color: #0E5558;
                font-size: 12px;
                font-weight: 700;
            }

            QLabel#finalBadge {
                color: #A65D35;
                font-size: 12px;
                font-weight: 800;
            }

            QPushButton#openButton {
                background-color: #0E5558;
                border: none;
                border-radius: 9px;
                padding: 11px 18px;
                color: #FFFDF7;
                font-size: 13px;
                font-weight: 700;
            }

            QPushButton#openButton:hover {
                background-color: #0E5558;
            }

            QPushButton#finalButton {
                background-color: #A65D35;
                border: none;
                border-radius: 9px;
                padding: 11px 18px;
                color: #203B36;
                font-size: 13px;
                font-weight: 800;
            }

            QPushButton#finalButton:hover {
                background-color: #A65D35;
            }
            """
        )

    def build_ui(self):
        root = QVBoxLayout(
            self
        )

        root.setContentsMargins(
            34,
            30,
            34,
            24,
        )

        root.setSpacing(
            16
        )

        title = QLabel(
            "Portfolio"
        )

        title.setObjectName(
            "pageTitle"
        )

        subtitle = QLabel(
            "O'quv jarayonida tayyorlangan loyihalarni "
            "professional portfolio darajasiga olib chiqish."
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

        hero = QFrame()

        hero.setObjectName(
            "heroCard"
        )

        hero_layout = QVBoxLayout(
            hero
        )

        hero_layout.setContentsMargins(
            22,
            20,
            22,
            20,
        )

        hero_title = QLabel(
            "Professional portfolio yo'li"
        )

        hero_title.setObjectName(
            "heroTitle"
        )

        hero_text = QLabel(
            "Portfolio faqat 3D rasmlar to'plami emas. "
            "Unda texnik topshiriq, genplan, qavat rejasi, "
            "fasadlar, kesimlar, konstruktiv fikrlash, "
            "BIM hujjatlar, mijoz bilan ishlash va yakuniy "
            "loyihani professional himoya qilish jarayoni aks etadi."
        )

        hero_text.setObjectName(
            "cardText"
        )

        hero_text.setWordWrap(
            True
        )

        hero_layout.addWidget(
            hero_title
        )

        hero_layout.addWidget(
            hero_text
        )

        root.addWidget(
            hero
        )

        scroll = QScrollArea()

        scroll.setWidgetResizable(
            True
        )

        content = QWidget()

        content.setObjectName(
            "portfolioContent"
        )

        content_layout = QVBoxLayout(
            content
        )

        content_layout.setContentsMargins(
            0,
            4,
            8,
            20,
        )

        content_layout.setSpacing(
            12
        )

        sections = [
            (
                "BOSQICH 03",
                "Uchastka va genplan",
                (
                    "Yer uchastkasini tahlil qilish, "
                    "uy joylashuvi va genplan yechimlari."
                ),
                ["LEVEL_03"],
            ),
            (
                "BOSQICH 04",
                "O'zbekiston turar joyi",
                (
                    "Mahalliy iqlim, hovli, turmush tarzi "
                    "va turar joy rejalashtirish yechimlari."
                ),
                ["LEVEL_04"],
            ),
            (
                "BOSQICH 05–07",
                "Archicad loyiha ko'nikmalari",
                (
                    "Model yaratish, fasad, kesim, tom, "
                    "zinapoya, BIM va professional Archicad workflow."
                ),
                [
                    "LEVEL_05",
                    "LEVEL_06",
                    "LEVEL_07",
                ],
            ),
            (
                "BOSQICH 10",
                "1 qavatli uy loyihasi",
                (
                    "Texnik topshiriqdan boshlab bir qavatli "
                    "uyni loyiha albomigacha ishlab chiqish."
                ),
                ["LEVEL_10"],
            ),
            (
                "BOSQICH 11",
                "2 qavatli uy loyihasi",
                (
                    "Ikki qavatli turar joyni professional "
                    "darajada rejalashtirish va loyihalash."
                ),
                ["LEVEL_11"],
            ),
            (
                "BOSQICH 12",
                "BIM va ishchi hujjatlar",
                (
                    "Professional BIM model, chizmalar va "
                    "ishchi loyiha hujjatlarini tayyorlash."
                ),
                ["LEVEL_12"],
            ),
            (
                "BOSQICH 13",
                "Mijoz va real loyiha",
                (
                    "Real buyurtma, texnik topshiriq, muzokara, "
                    "loyiha taqdimoti va himoyasi."
                ),
                ["LEVEL_13"],
            ),
            (
                "BOSQICH 14",
                "Advanced Residential Designer",
                (
                    "Murakkab uchastka, katta villa, premium "
                    "fasad va murakkab real loyiha vaziyatlari."
                ),
                ["LEVEL_14"],
            ),
        ]

        for (
            badge_text,
            title_text,
            description,
            levels,
        ) in sections:

            content_layout.addWidget(
                self.create_card(
                    badge_text,
                    title_text,
                    description,
                    levels,
                )
            )

        final_card = QFrame()

        final_card.setObjectName(
            "finalCard"
        )

        final_layout = QHBoxLayout(
            final_card
        )

        final_layout.setContentsMargins(
            22,
            20,
            22,
            20,
        )

        final_text_area = QVBoxLayout()

        final_badge = QLabel(
            "BOSQICH 15 • PRO FINAL"
        )

        final_badge.setObjectName(
            "finalBadge"
        )

        final_title = QLabel(
            "Final loyiha • Himoya • Portfolio • PRO Final"
        )

        final_title.setObjectName(
            "cardTitle"
        )

        final_text = QLabel(
            "Yakuniy texnik topshiriq, mustaqil loyiha, "
            "loyihani professional asoslash, portfolio tayyorlash "
            "va yakuniy baholash."
        )

        final_text.setObjectName(
            "cardText"
        )

        final_text.setWordWrap(
            True
        )

        final_text_area.addWidget(
            final_badge
        )

        final_text_area.addWidget(
            final_title
        )

        final_text_area.addWidget(
            final_text
        )

        final_layout.addLayout(
            final_text_area,
            1,
        )

        final_button = QPushButton(
            "BOSQICH 15 NI KO'RISH  →"
        )

        final_button.setObjectName(
            "finalButton"
        )

        final_button.clicked.connect(
            lambda:
            self.open_levels_requested.emit(
                ["LEVEL_15"],
                "Professional yakuniy bosqich",
                (
                    "Final loyiha, himoya, portfolio "
                    "va PRO Final."
                ),
            )
        )

        final_layout.addWidget(
            final_button
        )

        content_layout.addWidget(
            final_card
        )

        content_layout.addStretch()

        scroll.setWidget(
            content
        )

        root.addWidget(
            scroll,
            1,
        )

    def create_card(
        self,
        badge_text,
        title_text,
        description,
        levels,
    ):
        card = QFrame()

        card.setObjectName(
            "portfolioCard"
        )

        layout = QHBoxLayout(
            card
        )

        layout.setContentsMargins(
            22,
            18,
            22,
            18,
        )

        layout.setSpacing(
            18
        )

        text_area = QVBoxLayout()

        badge = QLabel(
            badge_text
        )

        badge.setObjectName(
            "badge"
        )

        title = QLabel(
            title_text
        )

        title.setObjectName(
            "cardTitle"
        )

        text = QLabel(
            description
        )

        text.setObjectName(
            "cardText"
        )

        text.setWordWrap(
            True
        )

        text_area.addWidget(
            badge
        )

        text_area.addWidget(
            title
        )

        text_area.addWidget(
            text
        )

        layout.addLayout(
            text_area,
            1,
        )

        button = QPushButton(
            "KO'RISH  →"
        )

        button.setObjectName(
            "openButton"
        )

        button.clicked.connect(
            lambda:
            self.open_levels_requested.emit(
                levels,
                title_text,
                description,
            )
        )

        layout.addWidget(
            button
        )

        return card
