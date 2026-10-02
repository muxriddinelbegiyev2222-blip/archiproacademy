from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QFrame,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QScrollArea,
    QVBoxLayout,
    QWidget,
)

from courses.course_service import (
    complete_lesson,
    get_learning_overview,
)

from ui.lesson_window import LessonWindow


class LearningWindow(QMainWindow):
    def __init__(self, user: dict):
        super().__init__()

        self.user = user
        self.lesson_window = None

        self.setWindowTitle(
            "ARCHIPRO UZ - Mening o'qishim"
        )

        self.resize(
            1350,
            850,
        )

        self.setMinimumSize(
            950,
            650,
        )

        self.setup_styles()

        self.reload_data()

        self.build_ui()

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

            QScrollArea {
                background-color: transparent;
                border: none;
            }

            QLabel#pageTitle {
                font-size: 30px;
                font-weight: 700;
                color: white;
            }

            QLabel#pageSubtitle {
                font-size: 14px;
                color: #94A3B8;
            }

            QFrame#levelCard {
                background-color: #0F172A;
                border: 1px solid #1E293B;
                border-radius: 16px;
            }

            QFrame#moduleCard {
                background-color: #111827;
                border: 1px solid #1E293B;
                border-radius: 12px;
            }

            QFrame#lessonAvailable {
                background-color: #12203A;
                border: 1px solid #2563EB;
                border-radius: 10px;
            }

            QFrame#lessonCompleted {
                background-color: #10251C;
                border: 1px solid #15803D;
                border-radius: 10px;
            }

            QFrame#lessonLocked {
                background-color: #111827;
                border: 1px solid #1E293B;
                border-radius: 10px;
            }

            QLabel#levelTitle {
                font-size: 22px;
                font-weight: 700;
                color: white;
            }

            QLabel#levelSubtitle {
                font-size: 14px;
                color: #94A3B8;
            }

            QLabel#moduleTitle {
                font-size: 17px;
                font-weight: 700;
                color: white;
            }

            QLabel#lessonTitle {
                font-size: 14px;
                font-weight: 600;
                color: #E2E8F0;
            }

            QLabel#meta {
                font-size: 12px;
                color: #64748B;
            }

            QProgressBar {
                border: none;
                background-color: #1E293B;
                border-radius: 6px;
                height: 11px;
                color: transparent;
            }

            QProgressBar::chunk {
                background-color: #2563EB;
                border-radius: 6px;
            }

            QPushButton#openLesson {
                background-color: #2563EB;
                color: white;
                border: none;
                border-radius: 8px;
                padding: 9px 15px;
                font-weight: 600;
            }

            QPushButton#openLesson:hover {
                background-color: #3B82F6;
            }

            QPushButton#backButton {
                background-color: #1E293B;
                color: white;
                border: none;
                border-radius: 8px;
                padding: 9px 15px;
            }
            """
        )

    def reload_data(self):
        self.levels = get_learning_overview(
            self.user["id"]
        )

    def build_ui(self):
        central = QWidget()

        self.setCentralWidget(
            central
        )

        root = QVBoxLayout(
            central
        )

        root.setContentsMargins(
            30,
            24,
            30,
            24,
        )

        root.setSpacing(
            16
        )

        top = QHBoxLayout()

        back_button = QPushButton(
            "← ORQAGA"
        )

        back_button.setObjectName(
            "backButton"
        )

        back_button.clicked.connect(
            self.close
        )

        top.addWidget(
            back_button
        )

        top.addStretch()

        root.addLayout(
            top
        )

        title = QLabel(
            "Mening o'qishim"
        )

        title.setObjectName(
            "pageTitle"
        )

        subtitle = QLabel(
            "0 dan PRO darajagacha bo'lgan to'liq o'quv yo'lingiz"
        )

        subtitle.setObjectName(
            "pageSubtitle"
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

        content = QWidget()

        content_layout = QVBoxLayout(
            content
        )

        content_layout.setContentsMargins(
            0,
            8,
            12,
            30,
        )

        content_layout.setSpacing(
            18
        )

        for level in self.levels:
            level_card = self.create_level_card(
                level
            )

            content_layout.addWidget(
                level_card
            )

        content_layout.addStretch()

        scroll.setWidget(
            content
        )

        root.addWidget(
            scroll,
            1,
        )

    def create_level_card(
        self,
        level: dict,
    ):
        card = QFrame()

        card.setObjectName(
            "levelCard"
        )

        layout = QVBoxLayout(
            card
        )

        layout.setContentsMargins(
            22,
            20,
            22,
            20,
        )

        layout.setSpacing(
            13
        )

        header = QHBoxLayout()

        title_area = QVBoxLayout()

        title = QLabel(
            f"{level['code']}  •  {level['title']}"
        )

        title.setObjectName(
            "levelTitle"
        )

        subtitle = QLabel(
            level.get(
                "subtitle",
                "",
            )
        )

        subtitle.setObjectName(
            "levelSubtitle"
        )

        title_area.addWidget(
            title
        )

        title_area.addWidget(
            subtitle
        )

        header.addLayout(
            title_area
        )

        header.addStretch()

        progress_text = QLabel(
            f"{level['completed_lessons']}/"
            f"{level['total_lessons']} dars"
        )

        progress_text.setObjectName(
            "meta"
        )

        header.addWidget(
            progress_text
        )

        layout.addLayout(
            header
        )

        progress = QProgressBar()

        progress.setRange(
            0,
            100,
        )

        progress.setValue(
            level["progress_percent"]
        )

        layout.addWidget(
            progress
        )

        if not level["modules"]:
            empty_label = QLabel(
                "Bu Level kontenti keyingi bosqichlarda qo'shiladi."
            )

            empty_label.setObjectName(
                "meta"
            )

            layout.addWidget(
                empty_label
            )

        for module in level["modules"]:
            module_card = self.create_module_card(
                module
            )

            layout.addWidget(
                module_card
            )

        return card

    def create_module_card(
        self,
        module: dict,
    ):
        card = QFrame()

        card.setObjectName(
            "moduleCard"
        )

        layout = QVBoxLayout(
            card
        )

        layout.setContentsMargins(
            18,
            16,
            18,
            16,
        )

        layout.setSpacing(
            10
        )

        title = QLabel(
            module["title"]
        )

        title.setObjectName(
            "moduleTitle"
        )

        layout.addWidget(
            title
        )

        info = QLabel(
            f"{module['completed_lessons']}/"
            f"{module['total_lessons']} dars tugallangan"
        )

        info.setObjectName(
            "meta"
        )

        layout.addWidget(
            info
        )

        for lesson in module["lessons"]:
            lesson_row = self.create_lesson_row(
                lesson
            )

            layout.addWidget(
                lesson_row
            )

        return card

    def create_lesson_row(
        self,
        lesson: dict,
    ):
        status = lesson[
            "status"
        ]

        row = QFrame()

        if status == "completed":
            row.setObjectName(
                "lessonCompleted"
            )

            status_text = "✓"

        elif status == "available":
            row.setObjectName(
                "lessonAvailable"
            )

            status_text = "▶"

        else:
            row.setObjectName(
                "lessonLocked"
            )

            status_text = "🔒"

        layout = QHBoxLayout(
            row
        )

        layout.setContentsMargins(
            14,
            11,
            14,
            11,
        )

        status_label = QLabel(
            status_text
        )

        status_label.setFixedWidth(
            25
        )

        title_area = QVBoxLayout()

        title = QLabel(
            lesson["title"]
        )

        title.setObjectName(
            "lessonTitle"
        )

        meta = QLabel(
            f"{lesson['estimated_minutes']} daqiqa"
            f"   •   {lesson['xp_reward']} XP"
        )

        meta.setObjectName(
            "meta"
        )

        title_area.addWidget(
            title
        )

        title_area.addWidget(
            meta
        )

        layout.addWidget(
            status_label
        )

        layout.addLayout(
            title_area
        )

        layout.addStretch()

        if status == "available":
            button = QPushButton(
                "OCHISH"
            )

            button.setObjectName(
                "openLesson"
            )

            button.clicked.connect(
                lambda checked=False, data=lesson:
                    self.open_lesson(data)
            )

            layout.addWidget(
                button
            )

        elif status == "completed":
            score = QLabel(
                f"Eng yaxshi test: "
                f"{lesson['best_score']}%"
            )

            score.setObjectName(
                "meta"
            )

            layout.addWidget(
                score
            )

        return row

    def open_lesson(
        self,
        lesson: dict,
    ):
        level_title = ""

        module_title = ""

        for level in self.levels:
            for module in level["modules"]:
                for module_lesson in module["lessons"]:
                    if module_lesson["id"] == lesson["id"]:
                        level_title = level["title"]
                        module_title = module["title"]

        lesson_data = dict(
            lesson
        )

        lesson_data["level_title"] = (
            level_title
        )

        lesson_data["module_title"] = (
            module_title
        )

        self.lesson_window = LessonWindow(
            lesson=lesson_data,
            user=self.user,
        )

        self.lesson_window.lesson_completed.connect(
            self.lesson_finished
        )

        self.lesson_window.show()

    def lesson_finished(
        self,
        lesson_id: int,
    ):
        complete_lesson(
            self.user["id"],
            lesson_id,
        )

        self.reload_data()

        self.build_ui()
