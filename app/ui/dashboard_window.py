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

from ui.learning_window import LearningWindow
from ui.lesson_window import LessonWindow
from ui.license_window import LicenseWindow


class DashboardWindow(QMainWindow):
    def __init__(
        self,
        user: dict,
    ):
        super().__init__()

        self.user = user

        self.lesson_window = None
        self.learning_window = None
        self.license_window = None

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

        self.setMinimumSize(
            1100,
            700,
        )

        self.reload_data()
        self.build_ui()

    # ========================================================
    # DATA
    # ========================================================

    def reload_data(self):
        self.stats = get_user_course_stats(
            self.user["id"]
        )

        self.current_level = get_current_level(
            self.user["id"]
        )

        self.next_lesson = (
            get_next_available_lesson(
                self.user["id"]
            )
        )

    # ========================================================
    # MAIN UI
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

            QLabel#logoTitle {
                color: #FFFFFF;
                font-size: 24px;
                font-weight: 800;
            }

            QLabel#logoSubtitle {
                color: #64748B;
                font-size: 11px;
            }

            QListWidget {
                background-color: transparent;
                border: none;
                outline: none;
                color: #CBD5E1;
                font-size: 14px;
            }

            QListWidget::item {
                padding: 11px 13px;
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
                color: #FFFFFF;
                font-size: 30px;
                font-weight: 800;
            }

            QLabel#pageSubtitle {
                color: #94A3B8;
                font-size: 14px;
            }

            QFrame#card {
                background-color: #111827;
                border: 1px solid #1E293B;
                border-radius: 14px;
            }

            QLabel#cardTitle {
                color: #94A3B8;
                font-size: 12px;
            }

            QLabel#cardValue {
                color: #FFFFFF;
                font-size: 24px;
                font-weight: 700;
            }

            QLabel#sectionTitle {
                color: #FFFFFF;
                font-size: 19px;
                font-weight: 700;
            }

            QLabel#infoText {
                color: #94A3B8;
                font-size: 13px;
            }

            QLabel#xpInfo {
                color: #FBBF24;
                font-size: 12px;
            }

            QProgressBar {
                background-color: #1E293B;
                border: none;
                border-radius: 7px;
                height: 14px;
                color: transparent;
            }

            QProgressBar::chunk {
                background-color: #2563EB;
                border-radius: 7px;
            }

            QPushButton#primaryButton {
                background-color: #2563EB;
                border: none;
                border-radius: 9px;
                padding: 12px 18px;
                color: #FFFFFF;
                font-size: 14px;
                font-weight: 700;
            }

            QPushButton#primaryButton:hover {
                background-color: #3B82F6;
            }

            QPushButton#secondaryButton {
                background-color: #1E293B;
                border: 1px solid #334155;
                border-radius: 9px;
                padding: 12px 18px;
                color: #FFFFFF;
                font-size: 14px;
                font-weight: 600;
            }

            QPushButton#secondaryButton:hover {
                background-color: #334155;
            }

            QFrame#masterBanner {
                background-color: #251D06;
                border: 1px solid #A16207;
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

            QPushButton#masterButton {
                background-color: #A16207;
                border: none;
                border-radius: 9px;
                padding: 12px 18px;
                color: #FFFFFF;
                font-size: 13px;
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

        sidebar_layout.setSpacing(
            10
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
            20
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
            "Litsenziya",
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
            or "Foydalanuvchi"
        )

        license_type = (
            self.user.get(
                "license_type",
                "PRO",
            )
        )

        user_label = QLabel(
            f"{user_name}\n{license_type}"
        )

        user_label.setWordWrap(
            True
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
            20
        )

        page_title = QLabel(
            "Bosh sahifa"
        )

        page_title.setObjectName(
            "pageTitle"
        )

        page_subtitle = QLabel(
            "Arxitekturani bosqichma-bosqich "
            "o'rganish va amaliy ko'nikmalarni rivojlantirish."
        )

        page_subtitle.setObjectName(
            "pageSubtitle"
        )

        page_subtitle.setWordWrap(
            True
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
                "Barcha Level va mavjud darslarni "
                "blokirovkasiz tekshirishingiz mumkin."
            )

            master_text.setObjectName(
                "masterText"
            )

            master_text.setWordWrap(
                True
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
                "BARCHA LEVELLARNI OCHISH"
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
            current_level_text = str(
                self.current_level.get(
                    "code",
                    "LEVEL_00",
                )
            ).replace(
                "LEVEL_",
                "LEVEL ",
            )

        else:
            current_level_text = (
                "LEVEL 0"
            )

        # ====================================================
        # STATS
        # ====================================================

        stats_layout = QHBoxLayout()

        stats_layout.setSpacing(
            16
        )

        progress_percent = int(
            self.stats.get(
                "progress_percent",
                0,
            )
        )

        completed_lessons = int(
            self.stats.get(
                "completed_lessons",
                0,
            )
        )

        total_lessons = int(
            self.stats.get(
                "total_lessons",
                0,
            )
        )

        xp = int(
            self.stats.get(
                "xp",
                0,
            )
        )

        stats_layout.addWidget(
            self.create_stat_card(
                "Umumiy progress",
                f"{progress_percent}%",
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
                    f"{completed_lessons}/"
                    f"{total_lessons}"
                ),
            )
        )

        stats_layout.addWidget(
            self.create_stat_card(
                "Jami XP",
                str(
                    xp
                ),
            )
        )

        content_layout.addLayout(
            stats_layout
        )

        lesson_xp = int(
            self.stats.get(
                "lesson_xp",
                0,
            )
        )

        exam_xp = int(
            self.stats.get(
                "exam_xp",
                0,
            )
        )

        xp_info = QLabel(
            f"Darslardan: {lesson_xp} XP"
            f"   •   "
            f"Imtihonlardan: {exam_xp} XP"
        )

        xp_info.setObjectName(
            "xpInfo"
        )

        content_layout.addWidget(
            xp_info
        )

        # ====================================================
        # CONTINUE LEARNING CARD
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
                str(
                    self.next_lesson.get(
                        "level_title",
                        "",
                    )
                )
            )

            level_label.setObjectName(
                "infoText"
            )

            module_label = QLabel(
                str(
                    self.next_lesson.get(
                        "module_title",
                        "",
                    )
                )
            )

            module_label.setObjectName(
                "infoText"
            )

            lesson_title = QLabel(
                str(
                    self.next_lesson.get(
                        "title",
                        "",
                    )
                )
            )

            lesson_title.setWordWrap(
                True
            )

            lesson_title.setStyleSheet(
                """
                QLabel {
                    color: #FFFFFF;
                    font-size: 19px;
                    font-weight: 700;
                }
                """
            )

            summary = QLabel(
                str(
                    self.next_lesson.get(
                        "summary",
                        "",
                    )
                )
            )

            summary.setObjectName(
                "infoText"
            )

            summary.setWordWrap(
                True
            )

            estimated_minutes = (
                self.next_lesson.get(
                    "estimated_minutes",
                    0,
                )
            )

            xp_reward = (
                self.next_lesson.get(
                    "xp_reward",
                    0,
                )
            )

            lesson_meta = QLabel(
                f"{estimated_minutes} daqiqa"
                f"   •   "
                f"+{xp_reward} XP"
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
                progress_percent
            )

            continue_button = QPushButton(
                "DAVOM ETTIRISH"
            )

            continue_button.setObjectName(
                "primaryButton"
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
                    "Oddiy progress bo'yicha hozir ochiq dars yo'q."
                    if self.is_master
                    else
                    (
                        "Hozir ochiq dars yo'q.\n\n"
                        "Agar joriy Level ichidagi barcha darslarni "
                        "tugatgan bo'lsangiz, Mening o'qishim "
                        "bo'limidan yakuniy imtihonni tekshiring."
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
                "MENING O'QISHIM"
            )

            academy_button.setObjectName(
                "secondaryButton"
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
        menu_text = item.text()

        if (
            menu_text
            == "Mening o'qishim"
        ):
            self.open_learning_window()

        elif (
            menu_text
            == "Litsenziya"
        ):
            self.open_license_window()

    # ========================================================
    # LICENSE
    # ========================================================

    def open_license_window(
        self,
    ):
        self.license_window = (
            LicenseWindow(
                self.user
            )
        )

        self.license_window.show()

        self.license_window.raise_()

        self.license_window.activateWindow()

    # ========================================================
    # LEARNING
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

        self.lesson_window = (
            LessonWindow(
                lesson=self.next_lesson,
                user=self.user,
            )
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

        if not result.get(
            "success",
            False,
        ):
            return

        self.reload_data()
        self.build_ui()
