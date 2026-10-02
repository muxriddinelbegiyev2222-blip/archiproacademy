from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QFrame,
    QHBoxLayout,
    QLabel,
    QListWidget,
    QListWidgetItem,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class DashboardWindow(QMainWindow):
    def __init__(self, user: dict):
        super().__init__()

        self.user = user

        self.setWindowTitle("ARCHIPRO UZ")
        self.resize(1450, 850)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        self.setStyleSheet(
            """
            QMainWindow {
                background-color: #0B1220;
            }

            QWidget {
                color: #F8FAFC;
                font-family: Segoe UI;
            }

            QFrame#sidebar {
                background-color: #0F172A;
                border-right: 1px solid #1E293B;
            }

            QLabel#logoTitle {
                font-size: 24px;
                font-weight: 700;
                color: #FFFFFF;
            }

            QLabel#logoSubtitle {
                font-size: 11px;
                color: #64748B;
            }

            QListWidget {
                background-color: transparent;
                border: none;
                outline: none;
                font-size: 14px;
                color: #CBD5E1;
            }

            QListWidget::item {
                padding: 12px 14px;
                margin: 2px 0px;
                border-radius: 8px;
            }

            QListWidget::item:hover {
                background-color: #172033;
                color: #FFFFFF;
            }

            QListWidget::item:selected {
                background-color: #1D4ED8;
                color: #FFFFFF;
            }

            QLabel#pageTitle {
                font-size: 30px;
                font-weight: 700;
                color: #F8FAFC;
            }

            QLabel#pageSubtitle {
                font-size: 14px;
                color: #94A3B8;
            }

            QFrame#card {
                background-color: #111827;
                border: 1px solid #1E293B;
                border-radius: 14px;
            }

            QLabel#cardTitle {
                font-size: 14px;
                color: #94A3B8;
            }

            QLabel#cardValue {
                font-size: 28px;
                font-weight: 700;
                color: #FFFFFF;
            }

            QLabel#sectionTitle {
                font-size: 19px;
                font-weight: 600;
                color: #F8FAFC;
            }

            QLabel#infoText {
                font-size: 13px;
                color: #94A3B8;
            }

            QProgressBar {
                border: none;
                background-color: #1E293B;
                border-radius: 7px;
                height: 14px;
                text-align: center;
                color: transparent;
            }

            QProgressBar::chunk {
                background-color: #2563EB;
                border-radius: 7px;
            }

            QPushButton#continueButton {
                background-color: #2563EB;
                color: white;
                border: none;
                border-radius: 9px;
                padding: 12px 18px;
                font-size: 14px;
                font-weight: 600;
            }

            QPushButton#continueButton:hover {
                background-color: #3B82F6;
            }
            """
        )

        root_layout = QHBoxLayout(central_widget)
        root_layout.setContentsMargins(0, 0, 0, 0)
        root_layout.setSpacing(0)

        # -------------------------
        # SIDEBAR
        # -------------------------

        sidebar = QFrame()
        sidebar.setObjectName("sidebar")
        sidebar.setFixedWidth(260)

        sidebar_layout = QVBoxLayout(sidebar)
        sidebar_layout.setContentsMargins(20, 24, 20, 20)

        logo_title = QLabel("ARCHIPRO UZ")
        logo_title.setObjectName("logoTitle")

        logo_subtitle = QLabel("Architecture Academy")
        logo_subtitle.setObjectName("logoSubtitle")

        sidebar_layout.addWidget(logo_title)
        sidebar_layout.addWidget(logo_subtitle)
        sidebar_layout.addSpacing(25)

        self.menu = QListWidget()

        menu_items = [
            "Bosh sahifa",
            "Mening o'qishim",
            "Arxitektura",
            "Archicad",
            "SHNQ va normativlar",
            "Amaliyot",
            "Loyihalar",
            "Testlar",
            "Imtihonlar",
            "Kutubxona",
            "Portfolio",
            "Statistika",
            "Sozlamalar",
        ]

        for item_text in menu_items:
            item = QListWidgetItem(item_text)
            self.menu.addItem(item)

        self.menu.setCurrentRow(0)

        sidebar_layout.addWidget(self.menu)
        sidebar_layout.addStretch()

        user_name = self.user.get("full_name") or self.user.get("username")
        license_type = self.user.get("license_type", "PRO")

        user_label = QLabel(
            f"{user_name}\n"
            f"{license_type}"
        )
        user_label.setStyleSheet(
            """
            QLabel {
                background-color: #111827;
                border: 1px solid #1E293B;
                border-radius: 10px;
                padding: 12px;
                color: #CBD5E1;
                font-size: 12px;
            }
            """
        )

        sidebar_layout.addWidget(user_label)

        # -------------------------
        # MAIN CONTENT
        # -------------------------

        content = QWidget()

        content_layout = QVBoxLayout(content)
        content_layout.setContentsMargins(34, 28, 34, 28)
        content_layout.setSpacing(22)

        header_layout = QHBoxLayout()

        header_text_layout = QVBoxLayout()

        page_title = QLabel("Bosh sahifa")
        page_title.setObjectName("pageTitle")

        page_subtitle = QLabel(
            "Arxitektura bo'yicha professional yo'lingizni davom ettiring."
        )
        page_subtitle.setObjectName("pageSubtitle")

        header_text_layout.addWidget(page_title)
        header_text_layout.addWidget(page_subtitle)

        header_layout.addLayout(header_text_layout)
        header_layout.addStretch()

        content_layout.addLayout(header_layout)

        # -------------------------
        # STATS
        # -------------------------

        stats_layout = QHBoxLayout()
        stats_layout.setSpacing(16)

        stats_layout.addWidget(
            self.create_stat_card(
                "Umumiy progress",
                "0%",
            )
        )

        stats_layout.addWidget(
            self.create_stat_card(
                "Daraja",
                "STARTER",
            )
        )

        stats_layout.addWidget(
            self.create_stat_card(
                "Tugallangan dars",
                "0",
            )
        )

        stats_layout.addWidget(
            self.create_stat_card(
                "XP",
                "0",
            )
        )

        content_layout.addLayout(stats_layout)

        # -------------------------
        # CONTINUE LEARNING
        # -------------------------

        learning_card = QFrame()
        learning_card.setObjectName("card")

        learning_layout = QVBoxLayout(learning_card)
        learning_layout.setContentsMargins(24, 22, 24, 22)
        learning_layout.setSpacing(12)

        learning_title = QLabel("O'qishni davom ettirish")
        learning_title.setObjectName("sectionTitle")

        course_name = QLabel(
            "Level 0 — Arxitekturaga mutlaqo noldan kirish"
        )
        course_name.setObjectName("infoText")

        lesson_name = QLabel(
            "1-dars: Arxitektura nima?"
        )
        lesson_name.setStyleSheet(
            """
            QLabel {
                font-size: 17px;
                font-weight: 600;
                color: #FFFFFF;
            }
            """
        )

        progress = QProgressBar()
        progress.setMinimum(0)
        progress.setMaximum(100)
        progress.setValue(0)

        continue_button = QPushButton("DAVOM ETTIRISH")
        continue_button.setObjectName("continueButton")
        continue_button.setFixedWidth(180)

        learning_layout.addWidget(learning_title)
        learning_layout.addWidget(course_name)
        learning_layout.addWidget(lesson_name)
        learning_layout.addWidget(progress)
        learning_layout.addSpacing(4)
        learning_layout.addWidget(
            continue_button,
            alignment=Qt.AlignmentFlag.AlignLeft,
        )

        content_layout.addWidget(learning_card)

        # -------------------------
        # SKILLS
        # -------------------------

        skills_card = QFrame()
        skills_card.setObjectName("card")

        skills_layout = QVBoxLayout(skills_card)
        skills_layout.setContentsMargins(24, 22, 24, 22)
        skills_layout.setSpacing(12)

        skills_title = QLabel("Professional ko'nikmalar")
        skills_title.setObjectName("sectionTitle")

        skills_layout.addWidget(skills_title)

        skills_layout.addWidget(
            self.create_skill_row("Arxitektura", 0)
        )
        skills_layout.addWidget(
            self.create_skill_row("Archicad", 0)
        )
        skills_layout.addWidget(
            self.create_skill_row("Rejalashtirish", 0)
        )
        skills_layout.addWidget(
            self.create_skill_row("SHNQ", 0)
        )
        skills_layout.addWidget(
            self.create_skill_row("BIM", 0)
        )
        skills_layout.addWidget(
            self.create_skill_row("Konstruksiya", 0)
        )

        content_layout.addWidget(skills_card)

        content_layout.addStretch()

        root_layout.addWidget(sidebar)
        root_layout.addWidget(content, 1)

    def create_stat_card(
        self,
        title: str,
        value: str,
    ) -> QFrame:

        card = QFrame()
        card.setObjectName("card")

        layout = QVBoxLayout(card)
        layout.setContentsMargins(20, 18, 20, 18)

        title_label = QLabel(title)
        title_label.setObjectName("cardTitle")

        value_label = QLabel(value)
        value_label.setObjectName("cardValue")

        layout.addWidget(title_label)
        layout.addWidget(value_label)

        return card

    def create_skill_row(
        self,
        title: str,
        value: int,
    ) -> QWidget:

        container = QWidget()

        layout = QVBoxLayout(container)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(5)

        top_layout = QHBoxLayout()

        title_label = QLabel(title)
        title_label.setObjectName("infoText")

        value_label = QLabel(f"{value}%")
        value_label.setObjectName("infoText")

        top_layout.addWidget(title_label)
        top_layout.addStretch()
        top_layout.addWidget(value_label)

        progress = QProgressBar()
        progress.setMinimum(0)
        progress.setMaximum(100)
        progress.setValue(value)

        layout.addLayout(top_layout)
        layout.addWidget(progress)

        return container
