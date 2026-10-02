from PySide6.QtCore import Qt, Signal
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

from courses.lesson_content import (
    get_lesson_content,
)

from courses.level00_extra import (
    get_level00_extra_content,
)

from courses.level01_content import (
    get_level01_content,
)

from ui.quiz_window import (
    QuizWindow,
)


class LessonWindow(QMainWindow):
    lesson_completed = Signal(int)

    def __init__(
        self,
        lesson: dict,
        user: dict,
    ):
        super().__init__()

        self.lesson = lesson
        self.user = user

        self.lesson_id = (
            lesson["id"]
        )

        self.quiz_window = None

        self.setWindowTitle(
            f"ARCHIPRO UZ - "
            f"{lesson.get('title', 'Dars')}"
        )

        self.resize(
            1220,
            820,
        )

        self.setMinimumSize(
            900,
            650,
        )

        self.setup_styles()
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

            QLabel#lessonLevel {
                color: #60A5FA;
                font-size: 13px;
                font-weight: 600;
            }

            QLabel#lessonTitle {
                color: #FFFFFF;
                font-size: 32px;
                font-weight: 700;
            }

            QLabel#lessonMeta {
                color: #94A3B8;
                font-size: 13px;
            }

            QFrame#contentCard {
                background-color: #111827;
                border: 1px solid #1E293B;
                border-radius: 16px;
            }

            QFrame#highlightCard {
                background-color: #12203A;
                border: 1px solid #2563EB;
                border-radius: 16px;
            }

            QFrame#exampleCard {
                background-color: #10251C;
                border: 1px solid #15803D;
                border-radius: 16px;
            }

            QFrame#warningCard {
                background-color: #2A1914;
                border: 1px solid #C2410C;
                border-radius: 16px;
            }

            QLabel#sectionTitle {
                color: #FFFFFF;
                font-size: 19px;
                font-weight: 700;
            }

            QLabel#bodyText {
                color: #CBD5E1;
                font-size: 15px;
            }

            QPushButton#backButton {
                background-color: #1E293B;
                color: #E2E8F0;
                border: none;
                border-radius: 9px;
                padding: 10px 18px;
                font-size: 13px;
                font-weight: 600;
            }

            QPushButton#backButton:hover {
                background-color: #334155;
            }

            QPushButton#quizButton {
                background-color: #2563EB;
                color: #FFFFFF;
                border: none;
                border-radius: 10px;
                padding: 13px 22px;
                font-size: 14px;
                font-weight: 700;
            }

            QPushButton#quizButton:hover {
                background-color: #3B82F6;
            }
            """
        )

    def build_ui(self):
        central = QWidget()

        self.setCentralWidget(
            central
        )

        root_layout = QVBoxLayout(
            central
        )

        root_layout.setContentsMargins(
            32,
            22,
            32,
            22,
        )

        root_layout.setSpacing(
            16
        )

        top_bar = QHBoxLayout()

        back_button = QPushButton(
            "← ORQAGA"
        )

        back_button.setObjectName(
            "backButton"
        )

        back_button.clicked.connect(
            self.close
        )

        top_bar.addWidget(
            back_button
        )

        top_bar.addStretch()

        xp_reward = self.lesson.get(
            "xp_reward",
            10,
        )

        xp_label = QLabel(
            f"+{xp_reward} XP"
        )

        xp_label.setStyleSheet(
            """
            QLabel {
                color: #FBBF24;
                font-size: 14px;
                font-weight: 700;
            }
            """
        )

        top_bar.addWidget(
            xp_label
        )

        root_layout.addLayout(
            top_bar
        )

        level_label = QLabel(
            self.lesson.get(
                "level_title",
                "ARCHIPRO UZ",
            )
        )

        level_label.setObjectName(
            "lessonLevel"
        )

        title_label = QLabel(
            self.lesson.get(
                "title",
                "Dars",
            )
        )

        title_label.setObjectName(
            "lessonTitle"
        )

        title_label.setWordWrap(
            True
        )

        module_title = self.lesson.get(
            "module_title",
            "",
        )

        lesson_type = self.lesson.get(
            "lesson_type",
            "theory",
        )

        minutes = self.lesson.get(
            "estimated_minutes",
            10,
        )

        type_names = {
            "theory": "NAZARIYA",
            "practice": "AMALIYOT",
            "quiz": "TEST",
            "project": "LOYIHA",
        }

        readable_type = type_names.get(
            lesson_type,
            lesson_type.upper(),
        )

        meta_label = QLabel(
            f"{module_title}"
            f"   •   {readable_type}"
            f"   •   {minutes} daqiqa"
        )

        meta_label.setObjectName(
            "lessonMeta"
        )

        root_layout.addWidget(
            level_label
        )

        root_layout.addWidget(
            title_label
        )

        root_layout.addWidget(
            meta_label
        )

        scroll = QScrollArea()

        scroll.setWidgetResizable(
            True
        )

        scroll.setFrameShape(
            QScrollArea.Shape.NoFrame
        )

        scroll_content = QWidget()

        scroll_layout = QVBoxLayout(
            scroll_content
        )

        scroll_layout.setContentsMargins(
            0,
            10,
            14,
            25,
        )

        scroll_layout.setSpacing(
            16
        )

        lesson_code = self.lesson.get(
            "code",
            "",
        )

        lesson_content = (
            self.find_lesson_content(
                lesson_code
            )
        )

        if lesson_content:

            for section in lesson_content:

                card = self.create_card(
                    title=section.get(
                        "title",
                        "",
                    ),
                    text=section.get(
                        "text",
                        "",
                    ),
                    object_name=(
                        self.get_card_object_name(
                            section.get(
                                "type",
                                "normal",
                            )
                        )
                    ),
                )

                scroll_layout.addWidget(
                    card
                )

        else:

            scroll_layout.addWidget(
                self.create_card(
                    title="Dars haqida",
                    text=self.lesson.get(
                        "summary",
                        (
                            "Ushbu darsning to'liq "
                            "kontenti tayyorlanmoqda."
                        ),
                    ),
                    object_name="contentCard",
                )
            )

        scroll_layout.addStretch()

        scroll.setWidget(
            scroll_content
        )

        root_layout.addWidget(
            scroll,
            1,
        )

        bottom_layout = QHBoxLayout()

        hint = QLabel(
            "Keyingi dars ochilishi uchun "
            "mini-testdan muvaffaqiyatli o'ting."
        )

        hint.setStyleSheet(
            """
            QLabel {
                color: #64748B;
                font-size: 12px;
            }
            """
        )

        self.quiz_button = QPushButton(
            "MINI-TESTNI BOSHLASH  →"
        )

        self.quiz_button.setObjectName(
            "quizButton"
        )

        self.quiz_button.clicked.connect(
            self.start_quiz
        )

        bottom_layout.addWidget(
            hint
        )

        bottom_layout.addStretch()

        bottom_layout.addWidget(
            self.quiz_button
        )

        root_layout.addLayout(
            bottom_layout
        )

    def find_lesson_content(
        self,
        lesson_code: str,
    ):
        content = get_lesson_content(
            lesson_code
        )

        if content:
            return content

        content = get_level00_extra_content(
            lesson_code
        )

        if content:
            return content

        content = get_level01_content(
            lesson_code
        )

        if content:
            return content

        return []

    def get_card_object_name(
        self,
        section_type: str,
    ) -> str:

        card_types = {
            "normal": "contentCard",
            "highlight": "highlightCard",
            "example": "exampleCard",
            "warning": "warningCard",
        }

        return card_types.get(
            section_type,
            "contentCard",
        )

    def create_card(
        self,
        title: str,
        text: str,
        object_name: str,
    ) -> QFrame:

        card = QFrame()

        card.setObjectName(
            object_name
        )

        layout = QVBoxLayout(
            card
        )

        layout.setContentsMargins(
            24,
            21,
            24,
            21,
        )

        layout.setSpacing(
            10
        )

        title_label = QLabel(
            title
        )

        title_label.setObjectName(
            "sectionTitle"
        )

        title_label.setWordWrap(
            True
        )

        body_label = QLabel(
            text
        )

        body_label.setObjectName(
            "bodyText"
        )

        body_label.setWordWrap(
            True
        )

        body_label.setTextFormat(
            Qt.TextFormat.RichText
        )

        body_label.setTextInteractionFlags(
            Qt.TextInteractionFlag.TextSelectableByMouse
        )

        layout.addWidget(
            title_label
        )

        layout.addWidget(
            body_label
        )

        return card

    def start_quiz(self):
        self.quiz_window = QuizWindow(
            user=self.user,
            lesson=self.lesson,
        )

        self.quiz_window.quiz_passed.connect(
            self.quiz_success
        )

        self.quiz_window.show()

    def quiz_success(self):
        self.lesson_completed.emit(
            self.lesson_id
        )

        self.close()
