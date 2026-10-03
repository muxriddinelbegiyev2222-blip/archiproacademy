from PySide6.QtCore import Qt, QTimer

from PySide6.QtWidgets import (
    QFrame,
    QHBoxLayout,
    QLabel,
    QListWidget,
    QListWidgetItem,
    QMainWindow,
    QStackedWidget,
    QVBoxLayout,
    QWidget,
)

from ui.learning_window import LearningWindow
from ui.menu_section_window import MenuSectionWindow
from ui.license_window import LicenseWindow
from ui.portfolio_page import PortfolioPage


class AppShell(QMainWindow):
    def __init__(
        self,
        user: dict,
    ):
        super().__init__()

        self.user = user

        self.page_cache = {}

        self.setWindowTitle(
            "ARCHIPRO UZ"
        )

        self.setMinimumSize(
            1000,
            650,
        )

        self.setup_styles()
        self.build_ui()
        self.open_home()

        QTimer.singleShot(
            0,
            self.showMaximized,
        )

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
                font-family: Segoe UI;
                color: #F8FAFC;
            }

            QWidget#appRoot {
                background-color: #0B1220;
            }

            QFrame#sidebar {
                background-color: #0F172A;
                border-right: 1px solid #1E293B;
            }

            QLabel#logo {
                color: #FFFFFF;
                font-size: 24px;
                font-weight: 800;
                background-color: transparent;
            }

            QLabel#logoSub {
                color: #64748B;
                font-size: 11px;
                background-color: transparent;
            }

            QListWidget {
                background-color: transparent;
                border: none;
                outline: none;
                color: #CBD5E1;
                font-size: 14px;
            }

            QListWidget::viewport {
                background-color: transparent;
            }

            QListWidget::item {
                padding: 12px 14px;
                margin: 2px 0px;
                border-radius: 8px;
            }

            QListWidget::item:hover {
                background-color: #172033;
            }

            QListWidget::item:selected {
                background-color: #1D4ED8;
                color: #FFFFFF;
            }

            QLabel#userInfo {
                background-color: #111827;
                border: 1px solid #1E293B;
                border-radius: 10px;
                padding: 12px;
                color: #CBD5E1;
                font-size: 12px;
            }

            QStackedWidget {
                background-color: #0B1220;
                border: none;
            }

            QStackedWidget > QWidget {
                background-color: #0B1220;
            }

            QWidget#homePage {
                background-color: #0B1220;
            }

            QLabel#homeTitle {
                color: #FFFFFF;
                font-size: 32px;
                font-weight: 800;
                background-color: transparent;
            }

            QLabel#homeSub {
                color: #94A3B8;
                font-size: 14px;
                background-color: transparent;
            }

            QFrame#homeCard {
                background-color: #111827;
                border: 1px solid #1E293B;
                border-radius: 14px;
            }

            QLabel#cardTitle {
                color: #FFFFFF;
                font-size: 20px;
                font-weight: 700;
                background-color: transparent;
            }

            QLabel#cardText {
                color: #94A3B8;
                font-size: 13px;
                background-color: transparent;
            }

            QScrollArea {
                background-color: #0B1220;
                border: none;
            }

            QAbstractScrollArea::viewport {
                background-color: #0B1220;
            }
            """
        )

    # ========================================================
    # UI
    # ========================================================

    def build_ui(self):
        central = QWidget()

        central.setObjectName(
            "appRoot"
        )

        self.setCentralWidget(
            central
        )

        root = QHBoxLayout(
            central
        )

        root.setContentsMargins(
            0,
            0,
            0,
            0,
        )

        root.setSpacing(
            0
        )

        # ====================================================
        # SIDEBAR
        # ====================================================

        sidebar = QFrame()

        sidebar.setObjectName(
            "sidebar"
        )

        sidebar.setFixedWidth(
            255
        )

        sidebar_layout = QVBoxLayout(
            sidebar
        )

        sidebar_layout.setContentsMargins(
            16,
            24,
            16,
            16,
        )

        logo = QLabel(
            "ARCHIPRO UZ"
        )

        logo.setObjectName(
            "logo"
        )

        logo_sub = QLabel(
            "Architecture Academy"
        )

        logo_sub.setObjectName(
            "logoSub"
        )

        sidebar_layout.addWidget(
            logo
        )

        sidebar_layout.addWidget(
            logo_sub
        )

        sidebar_layout.addSpacing(
            20
        )

        self.menu = QListWidget()

        self.menu_items = [
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
            "Litsenziya",
            "Sozlamalar",
        ]

        for menu_text in self.menu_items:
            self.menu.addItem(
                QListWidgetItem(
                    menu_text
                )
            )

        self.menu.itemClicked.connect(
            self.handle_menu
        )

        sidebar_layout.addWidget(
            self.menu,
            1,
        )

        user_name = (
            self.user.get(
                "full_name"
            )
            or self.user.get(
                "username"
            )
            or "Foydalanuvchi"
        )

        license_type = self.user.get(
            "license_type",
            "PRO",
        )

        user_info = QLabel(
            f"{user_name}\n{license_type}"
        )

        user_info.setObjectName(
            "userInfo"
        )

        user_info.setWordWrap(
            True
        )

        sidebar_layout.addWidget(
            user_info
        )

        # ====================================================
        # STACK
        # ====================================================

        self.stack = QStackedWidget()

        root.addWidget(
            sidebar
        )

        root.addWidget(
            self.stack,
            1,
        )

    # ========================================================
    # MENU
    # ========================================================

    def handle_menu(
        self,
        item,
    ):
        menu_text = item.text()

        if menu_text == "Bosh sahifa":
            self.open_home()
            return

        if menu_text == "Mening o'qishim":
            self.open_learning()
            return

        if menu_text == "Portfolio":
            self.open_portfolio()
            return

        if menu_text == "Litsenziya":
            self.open_license()
            return

        self.open_section(
            menu_text
        )

    # ========================================================
    # PAGE MANAGER
    # ========================================================

    def show_page(
        self,
        key: str,
        widget: QWidget,
    ):
        existing = self.page_cache.get(
            key
        )

        if existing is not None:
            self.stack.setCurrentWidget(
                existing
            )
            return

        widget.setParent(
            self.stack
        )

        widget.setWindowFlags(
            Qt.WindowType.Widget
        )

        self.stack.addWidget(
            widget
        )

        self.page_cache[
            key
        ] = widget

        self.stack.setCurrentWidget(
            widget
        )

    # ========================================================
    # HOME
    # ========================================================

    def open_home(self):
        self.menu.setCurrentRow(
            0
        )

        if "home" in self.page_cache:
            self.stack.setCurrentWidget(
                self.page_cache[
                    "home"
                ]
            )
            return

        page = QWidget()

        page.setObjectName(
            "homePage"
        )

        layout = QVBoxLayout(
            page
        )

        layout.setContentsMargins(
            34,
            30,
            34,
            30,
        )

        layout.setSpacing(
            20
        )

        title = QLabel(
            "Bosh sahifa"
        )

        title.setObjectName(
            "homeTitle"
        )

        subtitle = QLabel(
            "Arxitekturani bosqichma-bosqich o'rganing "
            "va amaliy ko'nikmalaringizni rivojlantiring."
        )

        subtitle.setObjectName(
            "homeSub"
        )

        layout.addWidget(
            title
        )

        layout.addWidget(
            subtitle
        )

        card = QFrame()

        card.setObjectName(
            "homeCard"
        )

        card_layout = QVBoxLayout(
            card
        )

        card_layout.setContentsMargins(
            24,
            22,
            24,
            22,
        )

        card_title = QLabel(
            "ARCHIPRO UZ"
        )

        card_title.setObjectName(
            "cardTitle"
        )

        card_text = QLabel(
            "Barcha o'quv kontenti, testlar va imtihonlar "
            "saqlangan holda yagona oynada ishlaydi."
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

        layout.addWidget(
            card
        )

        layout.addStretch()

        self.show_page(
            "home",
            page,
        )

    # ========================================================
    # LEARNING
    # ========================================================

    def open_learning(
        self,
        level_codes=None,
        title=None,
        subtitle=None,
    ):
        level_codes = level_codes or []

        key = (
            "learning_all"
            if not level_codes
            else
            "learning_"
            + "_".join(level_codes)
        )

        if key in self.page_cache:
            page = self.page_cache[
                key
            ]

            if hasattr(
                page,
                "reload_data",
            ):
                page.reload_data()

            if hasattr(
                page,
                "build_ui",
            ):
                page.build_ui()

            self.stack.setCurrentWidget(
                page
            )

            return

        page = LearningWindow(
            user=self.user,
            focus_level_codes=level_codes,
            custom_title=title,
            custom_subtitle=subtitle,
        )

        self.show_page(
            key,
            page,
        )

    # ========================================================
    # PORTFOLIO
    # ========================================================

    def open_portfolio(self):
        key = "portfolio"

        if key in self.page_cache:
            self.stack.setCurrentWidget(
                self.page_cache[
                    key
                ]
            )
            return

        page = PortfolioPage(
            self.user
        )

        page.open_levels_requested.connect(
            self.open_learning
        )

        self.show_page(
            key,
            page,
        )

    # ========================================================
    # SECTIONS
    # ========================================================

    def open_section(
        self,
        section_name: str,
    ):
        key = (
            "section_"
            + section_name
        )

        if key in self.page_cache:
            self.stack.setCurrentWidget(
                self.page_cache[
                    key
                ]
            )
            return

        page = MenuSectionWindow(
            self.user,
            section_name,
        )

        self.show_page(
            key,
            page,
        )

    # ========================================================
    # LICENSE
    # ========================================================

    def open_license(self):
        key = "license"

        if key in self.page_cache:
            self.stack.setCurrentWidget(
                self.page_cache[
                    key
                ]
            )
            return

        page = LicenseWindow(
            self.user
        )

        self.show_page(
            key,
            page,
        )
