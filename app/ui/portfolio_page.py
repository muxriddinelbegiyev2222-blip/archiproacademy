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
                background-color: #0B1220;
            }

            QScrollArea {
                background-color: #0B1220;
                border: none;
            }

            QAbstractScrollArea::viewport {
                background-color: #0B1220;
            }

            QWidget#portfolioContent {
                background-color: #0B1220;
            }

            QLabel#pageTitle {
                color: #FFFFFF;
                font-size: 32px;
                font-weight: 800;
            }

            QLabel#pageSubtitle {
                color: #94A3B8;
                font-size: 14px;
            }

            QFrame#heroCard {
                background-color: #111827;
                border: 1px solid #334155;
                border-radius: 16px;
            }

            QFrame#portfolioCard {
                background-color: #111827;
                border: 1px solid #1E293B;
                border-radius: 14px;
            }

            QFrame#finalCard {
                background-color: #181609;
                border: 1px solid #A16207;
                border-radius: 14px;
            }

            QLabel#heroTitle {
                color: #FFFFFF;
                font-size: 21px;
                font-weight: 800;
            }

            QLabel#cardTitle {
                color: #FFFFFF;
                font-size: 17px;
                font-weight: 700;
            }

            QLabel#cardText {
                color: #94A3B8;
                font-size: 13px;
            }

            QLabel#badge {
                color: #93C5FD;
                font-size: 12px;
                font-weight: 700;
            }

            QLabel#finalBadge {
                color: #FACC15;
                font-size: 12px;
                font-weight: 800;
            }

            QPushButton#openButton {
                background-color: #2563EB;
                border: none;
                border-radius: 9px;
                padding: 11px 18px;
                color: #FFFFFF;
                font-size: 13px;
                font-weight: 700;
            }

            QPushButton#openButton:hover {
                background-color: #3B82F6;
            }

            QPushButton#finalButton {
                background-color: #A16207;
                border: none;
                border-radius: 9px;
                padding: 11px 18px;
                color: #FFFFFF;
                font-size: 13px;
                font-weight: 800;
            }

            QPushButton#finalButton:hover {
                background-color: #CA8A04;
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
            "O'quv jarayonidagi bilim va loyihalarni "
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

        # ====================================================
        # HERO
        # ====================================================

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

        hero_layout.setSpacing(
            9
        )

        hero_title = QLabel(
            "Professional portfolio yo'li"
        )

        hero_title.setObjectName(
            "heroTitle"
        )

        hero_text = QLabel(
            "Portfolio faqat chiroyli rasmlar to'plami emas. "
            "Unda rejalashtirish, fasad, kesim, BIM hujjatlar, "
            "mijoz bilan ishlash, murakkab loyiha va yakuniy "
            "loyihani professional tarzda taqdim etish ko'nikmalari "
            "bir tizimda namoyon bo'ladi."
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

        # ====================================================
        # SCROLL
        # ====================================================

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
                "LEVEL 10",
                "1 qavatli uy loyihasi",
                (
                    "Texnik topshiriqdan boshlab bir qavatli "
                    "uyni loyiha albomigacha ishlab chiqish."
                ),
                ["LEVEL_10"],
            ),
            (
                "LEVEL 11",
                "2 qavatli uy loyihasi",
                (
                    "Ikki qavatli turar joyni professional "
                    "darajada rejalashtirish va loyihalash."
                ),
                ["LEVEL_11"],
            ),
            (
                "LEVEL 12",
                "BIM va ishchi hujjatlar",
                (
                    "Professional BIM model, chizmalar va "
                    "ishchi loyiha hujjatlarini tayyorlash."
                ),
                ["LEVEL_12"],
            ),
            (
                "LEVEL 13",
                "Mijoz va real loyiha",
                (
                    "Real buyurtma, texnik topshiriq, muzokara, "
                    "qarorlarni tushuntirish va loyiha himoyasi."
                ),
                ["LEVEL_13"],
            ),
            (
                "LEVEL 14",
                "Advanced Residential Designer",
                (
                    "Murakkab uchastka, katta villa, premium fasad "
                    "va advanced case study'lar."
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

            card = self.create_card(
                badge_text=badge_text,
                title_text=title_text,
                description=description,
                levels=levels,
            )

            content_layout.addWidget(
                card
            )

        # ====================================================
        # LEVEL 15 / FINAL
        # ====================================================

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

        final_layout.setSpacing(
            18
        )

        final_text_area = QVBoxLayout()

        final_badge = QLabel(
            "LEVEL 15 • PRO FINAL"
        )

        final_badge.setObjectName(
            "finalBadge"
        )

        final_title = QLabel(
            "Yakuniy loyiha + himoya + portfolio"
        )

        final_title.setObjectName(
            "cardTitle"
        )

        final_text = QLabel(
            "LEVEL 15 ichida yakuniy texnik topshiriq, "
            "mustaqil 1 yoki 2 qavatli loyiha, loyihani himoya "
            "qilish, professional portfolio va PRO Final mavjud."
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
            "LEVEL 15 NI OCHISH  →"
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
                    "Final loyiha, loyiha himoyasi, "
                    "portfolio va PRO Final."
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
        badge_text: str,
        title_text: str,
        description: str,
        levels: list,
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

        description_label = QLabel(
            description
        )

        description_label.setObjectName(
            "cardText"
        )

        description_label.setWordWrap(
            True
        )

        text_area.addWidget(
            badge
        )

        text_area.addWidget(
            title
        )

        text_area.addWidget(
            description_label
        )

        layout.addLayout(
            text_area,
            1,
        )

        button = QPushButton(
            "OCHISH  →"
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
