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

from courses.course_service import (
    complete_lesson,
    get_current_level,
    get_next_available_lesson,
    get_user_course_stats,
)

from ui.learning_window import (
    LearningWindow,
)

from ui.lesson_window import (
    LessonWindow,
)


class DashboardWindow(QMainWindow):
    def __init__(
        self,
        user: dict,
    ):
        super().__init__()

        self.user = user

        self.lesson_window = None
        self.learning_window = None

        self.is_master = (
            str(
                self.user.get(
                    "license_type",
                    "",
                )
            ).upper()
            == "MASTER"
        )

        self.setWindowTitle(
            "ARCHIPRO UZ"
        )

        self.resize(
            1450,
            850,
        )

        self.reload_data()

        self.build_ui()

    # ========================================================
    # DATA
    # ========================================================

    def reload_data(self):
        self.stats = (
            get_user_course_stats(
                self.user["id"]
            )
        )

        self.current_level = (
            get_current_level(
                self.user["id"]
            )
        )

        self.next_lesson = (
            get_next_available_lesson(
                self.user["id"]
            )
        )

    # ========================================================
    # UI
    # ========================================================

    def build_ui(self):
        central = QWidget()

        self.setCentralWidget(
            central
        )

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

            QFrame#masterBanner {
                background-color: #251D06;
                border: 1px solid #D4A72C;
                border-radius: 12px;
            }

            QLabel#masterTitle {
                color: #FACC15;
                font-size: 15px;
                font-weight: 800;
            }

            QLabel#masterText {
                color: #FDE68A;
                font-size: 12px;
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
            }

            QListWidget::item:selected {
                background-color: #1D4ED8;
                color: #FFFFFF;
            }

            QLabel#pageTitle {
                font-size: 30px;
                font-weight: 700;
                color: #FFFFFF;
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

            QFrame#masterCard {
                background-color: #181609;
                border: 1px solid #A16207;
                border-radius: 14px;
            }

            QLabel#cardTitle {
                font-size: 13px;
                color: #94A3B8;
            }

            QLabel#cardValue {
                font-size: 25px;
                font-weight: 700;
                color: #FFFFFF;
            }

            QLabel#sectionTitle {
                font-size: 19px;
                font-weight: 600;
                color: #FFFFFF;
            }

            QLabel#infoText {
                font-size: 13px;
                color: #94A3B8;
            }

            QLabel#xpInfo {
                font-size: 12px;
                color: #FBBF24;
            }

            QProgressBar {
                border: none;
                background-color: #1E293B;
                border-radius: 7px;
                height: 14px;
                color: transparent;
            }

            QProgressBar::chunk {
                background-color: #2563EB;
                border-radius: 7px;
            }

            QPushButton#continueButton {
                background-color: #2563EB;
                color: #FFFFFF;
                border: none;
                border-radius: 9px;
                padding: 12px 18px;
                font-size: 14px;
                font-weight: 600;
            }

            QPushButton#continueButton:hover {
                background-color: #3B82F6;
            }

            QPushButton#academyButton {
                background-color: #1E293B;
                color: #FFFFFF;
                border: 1px solid #334155;
                border-radius: 9px;
                padding: 12px 18px;
                font-size: 14px;
                font-weight: 600;
            }

            QPushButton#academyButton:hover {
                background-color: #334155;
            }

            QPushButton#masterButton {
                background-color: #A16207;
                color: #FFFFFF;
                border: none;
                border-radius: 9px;
                padding: 13px 20px;
                font-size: 14px;
                font-weight: 800;
            }

            QPushButton#masterButton:hover {
                background-color: #CA8A04;
            }
            """
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
            260
        )

        sidebar_layout = QVBoxLayout(
            sidebar
        )

        sidebar_layout.setContentsMargins(
            20,
            24,
            20,
            20,
        )

        logo = QLabel(
            "ARCHIPRO UZ"
        )

        logo.setObjectName(
            "logoTitle"
        )

        logo_subtitle = QLabel(
            "Architecture Academy"
        )

        logo_subtitle.setObjectName(
            "logoSubtitle"
        )

        sidebar_layout.addWidget(
            logo
        )

        sidebar_layout.addWidget(
            logo_subtitle
        )

        sidebar_layout.addSpacing(
            25
        )

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

        for menu_text in menu_items:
            self.menu.addItem(
                QListWidgetItem(
                    menu_text
                )
            )

        self.menu.setCurrentRow(
            0
        )

        self.menu.itemClicked.connect(
            self.handle_menu_click
        )

        sidebar_layout.addWidget(
            self.menu
        )

        sidebar_layout.addStretch()

        user_name = (
            self.user.get(
                "full_name"
            )
            or self.user.get(
                "username"
            )
        )

        license_type = (
            self.user.get(
                "license_type",
                "PRO",
            )
        )

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

        sidebar_layout.addWidget(
            user_label
        )

        # ====================================================
        # CONTENT
        # ====================================================

        content = QWidget()

        content_layout = QVBoxLayout(
            content
        )

        content_layout.setContentsMargins(
            34,
            28,
            34,
            28,
        )

        content_layout.setSpacing(
            22
        )

        page_title = QLabel(
            "Bosh sahifa"
        )

        page_title.setObjectName(
            "pageTitle"
        )

        page_subtitle = QLabel(
            (
                "Arxitekturani 0 dan professional "
                "darajagacha bosqichma-bosqich o'rganing."
            )
        )

        page_subtitle.setObjectName(
            "pageSubtitle"
        )

        content_layout.addWidget(
            page_title
        )

        content_layout.addWidget(
            page_subtitle
        )

        # ====================================================
        # MASTER BANNER
        # ====================================================

        if self.is_master:

            master_banner = QFrame()

            master_banner.setObjectName(
                "masterBanner"
            )

            master_layout = QHBoxLayout(
                master_banner
            )

            master_layout.setContentsMargins(
                18,
                14,
                18,
                14,
            )

            master_text_area = QVBoxLayout()

            master_title = QLabel(
                "★ MASTER TEST MODE FAOL"
            )

            master_title.setObjectName(
                "masterTitle"
            )

            master_text = QLabel(
                (
                    "Siz barcha Level va mavjud darslarni "
                    "blokirovkasiz tekshirishingiz mumkin."
                )
            )

            master_text.setObjectName(
                "masterText"
            )

            master_text_area.addWidget(
                master_title
            )

            master_text_area.addWidget(
                master_text
            )

            master_layout.addLayout(
                master_text_area
            )

            master_layout.addStretch()

            master_button = QPushButton(
                "BARCHA LEVELLARNI OCHISH  →"
            )

            master_button.setObjectName(
                "masterButton"
            )

            master_button.clicked.connect(
                self.open_learning_window
            )

            master_layout.addWidget(
                master_button
            )

            content_layout.addWidget(
                master_banner
            )

        # ====================================================
        # CURRENT LEVEL
        # ====================================================

        if self.is_master:

            current_level_text = (
                "MASTER"
            )

        elif self.current_level:

            current_level_text = (
                self.current_level[
                    "code"
                ].replace(
                    "LEVEL_",
                    "LEVEL ",
                )
            )

        else:

            current_level_text = (
                "LEVEL 0"
            )

        # ====================================================
        # STAT CARDS
        # ====================================================

        stats_layout = QHBoxLayout()

        stats_layout.setSpacing(
            16
        )

        stats_layout.addWidget(
            self.create_stat_card(
                "Umumiy progress",
                (
                    f"{self.stats['progress_percent']}%"
                ),
            )
        )

        stats_layout.addWidget(
            self.create_stat_card(
                (
                    "Rejim"
                    if self.is_master
                    else "Hozirgi daraja"
                ),
                current_level_text,
            )
        )

        stats_layout.addWidget(
            self.create_stat_card(
                "Tugallangan dars",
                (
                    f"{self.stats['completed_lessons']}/"
                    f"{self.stats['total_lessons']}"
                ),
            )
        )

        stats_layout.addWidget(
            self.create_stat_card(
                "Jami XP",
                str(
                    self.stats["xp"]
                ),
            )
        )

        content_layout.addLayout(
            stats_layout
        )

        xp_info = QLabel(
            (
                f"Darslardan: "
                f"{self.stats['lesson_xp']} XP"
                f"   •   "
                f"Imtihonlardan: "
                f"{self.stats['exam_xp']} XP"
            )
        )

        xp_info.setObjectName(
            "xpInfo"
        )

        content_layout.addWidget(
            xp_info
        )

        # ====================================================
        # MASTER QUICK ACCESS
        # ====================================================

        if self.is_master:

            master_card = QFrame()

            master_card.setObjectName(
                "masterCard"
            )

            master_card_layout = QVBoxLayout(
                master_card
            )

            master_card_layout.setContentsMargins(
                24,
                22,
                24,
                22,
            )

            master_card_layout.setSpacing(
                12
            )

            master_section_title = QLabel(
                "MASTER nazorat markazi"
            )

            master_section_title.setObjectName(
                "sectionTitle"
            )

            master_info = QLabel(
                (
                    "LEVEL 0 dan LEVEL 15 gacha bo'lgan "
                    "barcha tuzilmani ko'rishingiz mumkin. "
                    "Kontenti yaratilgan darslar darhol ochiladi. "
                    "Hali kontenti yozilmagan Level va modullar "
                    "ham skelet sifatida ko'rinadi."
                )
            )

            master_info.setObjectName(
                "infoText"
            )

            master_info.setWordWrap(
                True
            )

            open_all_button = QPushButton(
                "BARCHA LEVELLARNI KO'RISH  →"
            )

            open_all_button.setObjectName(
                "masterButton"
            )

            open_all_button.clicked.connect(
                self.open_learning_window
            )

            master_card_layout.addWidget(
                master_section_title
            )

            master_card_layout.addWidget(
                master_info
            )

            master_card_layout.addWidget(
                open_all_button,
                alignment=Qt.AlignmentFlag.AlignLeft,
            )

            content_layout.addWidget(
                master_card
            )

        # ====================================================
        # NORMAL CONTINUE CARD
        # ====================================================

        learning_card = QFrame()

        learning_card.setObjectName(
            "card"
        )

        learning_layout = QVBoxLayout(
            learning_card
        )

        learning_layout.setContentsMargins(
            24,
            22,
            24,
            22,
        )

        learning_layout.setSpacing(
            12
        )

        section_title = QLabel(
            (
                "Oddiy o'quvchi progressini tekshirish"
                if self.is_master
                else "O'qishni davom ettirish"
            )
        )

        section_title.setObjectName(
            "sectionTitle"
        )

        learning_layout.addWidget(
            section_title
        )

        if self.next_lesson:

            level_label = QLabel(
                self.next_lesson[
                    "level_title"
                ]
            )

            level_label.setObjectName(
                "infoText"
            )

            module_label = QLabel(
                self.next_lesson[
                    "module_title"
                ]
            )

            module_label.setObjectName(
                "infoText"
            )

            lesson_title = QLabel(
                self.next_lesson[
                    "title"
                ]
            )

            lesson_title.setStyleSheet(
                """
                QLabel {
                    font-size: 19px;
                    font-weight: 600;
                    color: #FFFFFF;
                }
                """
            )

            summary = QLabel(
                self.next_lesson.get(
                    "summary",
                    "",
                )
            )

            summary.setObjectName(
                "infoText"
            )

            summary.setWordWrap(
                True
            )

            lesson_meta = QLabel(
                (
                    f"{self.next_lesson['estimated_minutes']} daqiqa"
                    f"   •   "
                    f"+{self.next_lesson['xp_reward']} XP"
                )
            )

            lesson_meta.setObjectName(
                "xpInfo"
            )

            progress = QProgressBar()

            progress.setRange(
                0,
                100,
            )

            progress.setValue(
                self.stats[
                    "progress_percent"
                ]
            )

            continue_button = QPushButton(
                "DAVOM ETTIRISH"
            )

            continue_button.setObjectName(
                "continueButton"
            )

            continue_button.setCursor(
                Qt.CursorShape.PointingHandCursor
            )

            continue_button.clicked.connect(
                self.open_next_lesson
            )

            learning_layout.addWidget(
                level_label
            )

            learning_layout.addWidget(
                module_label
            )

            learning_layout.addWidget(
                lesson_title
            )

            learning_layout.addWidget(
                summary
            )

            learning_layout.addWidget(
                lesson_meta
            )

            learning_layout.addWidget(
                progress
            )

            learning_layout.addWidget(
                continue_button,
                alignment=Qt.AlignmentFlag.AlignLeft,
            )

        else:

            no_lesson = QLabel(
                (
                    "Oddiy progress bo'yicha hozir ochiq dars yo'q.\n\n"
                    "MASTER rejimida esa yuqoridagi tugma orqali "
                    "istalgan mavjud darsni ochishingiz mumkin."
                    if self.is_master
                    else
                    (
                        "Hozir ochiq dars yo'q.\n\n"
                        "Agar Level ichidagi barcha darslarni "
                        "tugatgan bo'lsangiz, Mening o'qishim "
                        "bo'limiga kirib yakuniy imtihonni topshiring."
                    )
                )
            )

            no_lesson.setObjectName(
                "infoText"
            )

            no_lesson.setWordWrap(
                True
            )

            academy_button = QPushButton(
                "MENING O'QISHIM  →"
            )

            academy_button.setObjectName(
                "academyButton"
            )

            academy_button.clicked.connect(
                self.open_learning_window
            )

            learning_layout.addWidget(
                no_lesson
            )

            learning_layout.addWidget(
                academy_button,
                alignment=Qt.AlignmentFlag.AlignLeft,
            )

        content_layout.addWidget(
            learning_card
        )

        content_layout.addStretch()

        root.addWidget(
            sidebar
        )

        root.addWidget(
            content,
            1,
        )

    # ========================================================
    # STAT CARD
    # ========================================================

    def create_stat_card(
        self,
        title: str,
        value: str,
    ):
        card = QFrame()

        card.setObjectName(
            "card"
        )

        layout = QVBoxLayout(
            card
        )

        layout.setContentsMargins(
            20,
            18,
            20,
            18,
        )

        title_label = QLabel(
            title
        )

        title_label.setObjectName(
            "cardTitle"
        )

        value_label = QLabel(
            value
        )

        value_label.setObjectName(
            "cardValue"
        )

        value_label.setWordWrap(
            True
        )

        layout.addWidget(
            title_label
        )

        layout.addWidget(
            value_label
        )

        return card

    # ========================================================
    # MENU
    # ========================================================

    def handle_menu_click(
        self,
        item,
    ):
        if (
            item.text()
            == "Mening o'qishim"
        ):
            self.open_learning_window()

    # ========================================================
    # LEARNING WINDOW
    # ========================================================

    def open_learning_window(
        self,
    ):
        self.learning_window = (
            LearningWindow(
                self.user
            )
        )

        self.learning_window.destroyed.connect(
            self.refresh_after_learning
        )

        self.learning_window.show()

    def refresh_after_learning(
        self,
    ):
        self.reload_data()

        self.build_ui()

    # ========================================================
    # LESSON
    # ========================================================

    def open_next_lesson(
        self,
    ):
        if not self.next_lesson:
            return

        self.lesson_window = LessonWindow(
            lesson=self.next_lesson,
            user=self.user,
        )

        self.lesson_window.lesson_completed.connect(
            self.handle_lesson_completed
        )

        self.lesson_window.show()

    def handle_lesson_completed(
        self,
        lesson_id: int,
    ):
        result = complete_lesson(
            self.user["id"],
            lesson_id,
        )

        if not result[
            "success"
        ]:
            return

        self.reload_data()

        self.build_ui()
