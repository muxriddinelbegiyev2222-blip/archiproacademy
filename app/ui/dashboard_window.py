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
    get_next_available_lesson,
    get_user_course_stats,
)

from ui.lesson_window import LessonWindow


class DashboardWindow(QMainWindow):
    def __init__(self, user: dict):
        super().__init__()

        self.user = user
        self.lesson_window = None

        self.setWindowTitle(
            "ARCHIPRO UZ"
        )

        self.resize(
            1450,
            850,
        )

        self.reload_data()
        self.build_ui()

    def reload_data(self):
        self.stats = get_user_course_stats(
            self.user["id"]
        )

        self.next_lesson = get_next_available_lesson(
            self.user["id"]
        )

    def build_ui(self):
        central_widget = QWidget()

        self.setCentralWidget(
            central_widget
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

            QListWidget::item:selected {
                background-color: #1D4ED8;
                color: white;
            }

            QLabel#pageTitle {
                font-size: 30px;
                font-weight: 700;
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
                font-size: 13px;
                color: #94A3B8;
            }

            QLabel#cardValue {
                font-size: 27px;
                font-weight: 700;
            }

            QLabel#sectionTitle {
                font-size: 19px;
                font-weight: 600;
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
            """
        )

        root_layout = QHBoxLayout(
            central_widget
        )

        root_layout.setContentsMargins(
            0,
            0,
            0,
            0,
        )

        root_layout.setSpacing(
            0
        )

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

        logo_title = QLabel(
            "ARCHIPRO UZ"
        )

        logo_title.setObjectName(
            "logoTitle"
        )

        logo_subtitle = QLabel(
            "Architecture Academy"
        )

        logo_subtitle.setObjectName(
            "logoSubtitle"
        )

        sidebar_layout.addWidget(
            logo_title
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

        for text in menu_items:
            self.menu.addItem(
                QListWidgetItem(
                    text
                )
            )

        self.menu.setCurrentRow(
            0
        )

        sidebar_layout.addWidget(
            self.menu
        )

        sidebar_layout.addStretch()

        user_name = (
            self.user.get("full_name")
            or self.user.get("username")
        )

        license_type = self.user.get(
            "license_type",
            "PRO",
        )

        user_label = QLabel(
            f"{user_name}\n{license_type}"
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
            "Professional arxitektura yo'lingizni davom ettiring."
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

        stats_layout = QHBoxLayout()

        stats_layout.setSpacing(
            16
        )

        progress_percent = self.stats[
            "progress_percent"
        ]

        completed = self.stats[
            "completed_lessons"
        ]

        total = self.stats[
            "total_lessons"
        ]

        xp_value = self.stats[
            "xp"
        ]

        stats_layout.addWidget(
            self.create_stat_card(
                "Umumiy progress",
                f"{progress_percent}%",
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
                f"{completed}/{total}",
            )
        )

        stats_layout.addWidget(
            self.create_stat_card(
                "XP",
                str(xp_value),
            )
        )

        content_layout.addLayout(
            stats_layout
        )

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

        title = QLabel(
            "O'qishni davom ettirish"
        )

        title.setObjectName(
            "sectionTitle"
        )

        learning_layout.addWidget(
            title
        )

        if self.next_lesson:
            level = QLabel(
                self.next_lesson[
                    "level_title"
                ]
            )

            level.setObjectName(
                "infoText"
            )

            lesson = QLabel(
                self.next_lesson[
                    "title"
                ]
            )

            lesson.setStyleSheet(
                """
                QLabel {
                    font-size: 18px;
                    font-weight: 600;
                    color: white;
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

            progress = QProgressBar()

            progress.setRange(
                0,
                100,
            )

            progress.setValue(
                progress_percent
            )

            button = QPushButton(
                "DAVOM ETTIRISH"
            )

            button.setObjectName(
                "continueButton"
            )

            button.clicked.connect(
                self.open_next_lesson
            )

            learning_layout.addWidget(
                level
            )

            learning_layout.addWidget(
                lesson
            )

            learning_layout.addWidget(
                summary
            )

            learning_layout.addWidget(
                progress
            )

            learning_layout.addWidget(
                button,
                alignment=Qt.AlignmentFlag.AlignLeft,
            )

        else:
            finished = QLabel(
                "Barcha mavjud darslar tugatilgan."
            )

            finished.setObjectName(
                "infoText"
            )

            learning_layout.addWidget(
                finished
            )

        content_layout.addWidget(
            learning_card
        )

        content_layout.addStretch()

        root_layout.addWidget(
            sidebar
        )

        root_layout.addWidget(
            content,
            1,
        )

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

        layout.addWidget(
            title_label
        )

        layout.addWidget(
            value_label
        )

        return card

    def open_next_lesson(self):
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

        if not result["success"]:
            return

        self.reload_data()
        self.build_ui()
