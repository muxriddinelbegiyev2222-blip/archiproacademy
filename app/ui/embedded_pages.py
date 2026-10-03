from PySide6.QtCore import (
    Qt,
    QTimer,
)

from PySide6.QtWidgets import (
    QAbstractScrollArea,
    QHBoxLayout,
    QPushButton,
    QScrollArea,
)

from ui.exam_window import (
    ExamWindow,
)

from ui.lesson_window import (
    LessonWindow,
)

from ui.quiz_window import (
    QuizWindow,
)

from ui.theme import (
    fix_scroll_surfaces,
)


# ============================================================
# COMMON EMBEDDED STYLE
# ============================================================

EMBEDDED_QSS = """
QMainWindow {
    background-color: #08111F;
}

QWidget {
    font-family: "Segoe UI";
    color: #EAF1FA;
}

QScrollArea,
QAbstractScrollArea {
    background-color: #08111F;
    border: none;
}

QAbstractScrollArea::viewport {
    background-color: #08111F;
}

QScrollArea > QWidget,
QScrollArea > QWidget > QWidget {
    background-color: #08111F;
}

QScrollBar:vertical {
    background-color: #0B1627;
    width: 12px;
    margin: 3px;
}

QScrollBar::handle:vertical {
    background-color: #314561;
    min-height: 45px;
    border-radius: 5px;
}

QScrollBar::handle:vertical:hover {
    background-color: #465F82;
}

QScrollBar::add-line:vertical,
QScrollBar::sub-line:vertical {
    height: 0px;
}

QScrollBar::add-page:vertical,
QScrollBar::sub-page:vertical {
    background: none;
}
"""


# ============================================================
# LESSON
# ============================================================

class LessonPage(
    LessonWindow
):
    def __init__(
        self,
        lesson: dict,
        user: dict,
        back_callback=None,
        open_quiz_callback=None,
    ):
        self.back_callback = (
            back_callback
        )

        self.open_quiz_callback = (
            open_quiz_callback
        )

        super().__init__(
            lesson=lesson,
            user=user,
        )

        QTimer.singleShot(
            0,
            self._polish_page,
        )

    def setup_styles(self):
        super().setup_styles()

        self.setStyleSheet(
            self.styleSheet()
            + EMBEDDED_QSS
            + """
            QLabel {
                color: #DCE5F1;
            }

            QLabel#lessonTitle {
                color: #F4F7FB;
                font-size: 34px;
                font-weight: 800;
            }

            QLabel#lessonLevel {
                color: #69A0FF;
                font-size: 15px;
                font-weight: 650;
            }

            QLabel#lessonMeta {
                color: #9AAAC0;
                font-size: 15px;
            }

            QLabel#sectionTitle {
                color: #EDF3FA;
                font-size: 20px;
                font-weight: 700;
            }

            QLabel#bodyText {
                color: #CFD9E7;
                font-size: 16px;
            }

            QFrame {
                background-color: #101C2F;
                border: 1px solid #243953;
                border-radius: 13px;
            }

            QPushButton#quizButton {
                background-color: #356FE0;
                border: 1px solid #4F8CFF;
                color: #FFFFFF;
                padding: 11px 22px;
                font-size: 15px;
                font-weight: 750;
                border-radius: 10px;
            }

            QPushButton#quizButton:hover {
                background-color: #467FE8;
            }

            QPushButton#backButton {
                background-color: #15243A;
                border: 1px solid #2A3D59;
                color: #DCE5F1;
                padding: 8px 16px;
                font-size: 14px;
                border-radius: 9px;
            }
            """
        )

    def build_ui(self):
        super().build_ui()

        self._connect_embedded_back()

        QTimer.singleShot(
            0,
            self._polish_page,
        )

    def _polish_page(self):
        fix_scroll_surfaces(
            self
        )

        for scroll in self.findChildren(
            QScrollArea
        ):
            scroll.viewport().setStyleSheet(
                """
                background-color: #08111F;
                border: none;
                """
            )

            content = scroll.widget()

            if content is not None:
                content.setStyleSheet(
                    content.styleSheet()
                    + """
                    background-color: #08111F;
                    """
                )

    def _connect_embedded_back(self):
        back_button = self.findChild(
            QPushButton,
            "backButton",
        )

        if (
            back_button is not None
            and self.back_callback is not None
        ):
            try:
                back_button.clicked.disconnect()

            except (
                RuntimeError,
                TypeError,
            ):
                pass

            back_button.clicked.connect(
                self.back_callback
            )

    def start_quiz(self):
        if self.open_quiz_callback is not None:
            self.open_quiz_callback(
                self
            )

            return

        super().start_quiz()

    def quiz_success(self):
        self.lesson_completed.emit(
            self.lesson_id
        )


# ============================================================
# QUIZ
# ============================================================

class QuizPage(
    QuizWindow
):
    def __init__(
        self,
        user: dict,
        lesson: dict,
        back_callback=None,
    ):
        self.back_callback = (
            back_callback
        )

        super().__init__(
            user=user,
            lesson=lesson,
        )

        QTimer.singleShot(
            0,
            self._polish_page,
        )

    def setup_styles(self):
        super().setup_styles()

        self.setStyleSheet(
            self.styleSheet()
            + EMBEDDED_QSS
            + """
            QLabel#pageTitle {
                color: #F4F7FB;
                font-size: 32px;
                font-weight: 800;
            }

            QLabel#subtitle {
                color: #9AAAC0;
                font-size: 16px;
            }

            QLabel#questionText {
                color: #EEF4FB;
                font-size: 18px;
                font-weight: 650;
            }

            QLabel#explanation {
                background-color: #15243A;
                border: 1px solid #2B405E;
                border-radius: 9px;
                color: #C9D5E4;
                font-size: 15px;
                padding: 12px;
            }

            QRadioButton {
                background-color: #101C2F;
                border: 1px solid #263A55;
                border-radius: 9px;
                color: #D5DFEC;
                font-size: 16px;
                padding: 11px;
                spacing: 10px;
            }

            QRadioButton:hover {
                background-color: #142640;
                border-color: #3A5A84;
            }
            """
        )

    def build_ui(self):
        super().build_ui()

        self._connect_embedded_back()

        QTimer.singleShot(
            0,
            self._polish_page,
        )

    def _polish_page(self):
        fix_scroll_surfaces(
            self
        )

    def _connect_embedded_back(self):
        back_button = self.findChild(
            QPushButton,
            "backButton",
        )

        if (
            back_button is not None
            and self.back_callback is not None
        ):
            try:
                back_button.clicked.disconnect()

            except (
                RuntimeError,
                TypeError,
            ):
                pass

            back_button.clicked.connect(
                self.back_callback
            )

    def continue_after_pass(self):
        self.quiz_passed.emit()


# ============================================================
# EXAM
# ============================================================

class ExamPage(
    ExamWindow
):
    def __init__(
        self,
        user: dict,
        exam: dict,
        back_callback=None,
    ):
        self.back_callback = (
            back_callback
        )

        super().__init__(
            user=user,
            exam=exam,
        )

        QTimer.singleShot(
            0,
            self._polish_page,
        )

    def setup_styles(self):
        super().setup_styles()

        self.setStyleSheet(
            self.styleSheet()
            + EMBEDDED_QSS
            + """
            QLabel#examLabel {
                color: #E8B84D;
                font-size: 14px;
                font-weight: 750;
            }

            QLabel#examTitle {
                color: #F4F7FB;
                font-size: 32px;
                font-weight: 800;
            }

            QLabel#examSubtitle {
                color: #9AAAC0;
                font-size: 16px;
            }

            QLabel#questionText {
                color: #EDF3FA;
                font-size: 18px;
                font-weight: 650;
            }

            QLabel#explanation {
                background-color: #15243A;
                border: 1px solid #2B405E;
                border-radius: 9px;
                color: #C8D3E1;
                font-size: 15px;
                padding: 12px;
            }

            QFrame#questionCard {
                background-color: #101C2F;
                border: 1px solid #253A56;
                border-radius: 13px;
            }

            QFrame#wrongCard {
                background-color: #281B20;
                border: 1px solid #7B3948;
                border-radius: 13px;
            }

            QRadioButton {
                color: #D5DFEC;
                font-size: 16px;
                padding: 10px;
            }
            """
        )

    def build_ui(self):
        super().build_ui()

        self._add_embedded_back()

        QTimer.singleShot(
            0,
            self._polish_page,
        )

    def _polish_page(self):
        fix_scroll_surfaces(
            self
        )

    def _add_embedded_back(self):
        if self.back_callback is None:
            return

        central = self.centralWidget()

        if central is None:
            return

        root = central.layout()

        if root is None:
            return

        top = QHBoxLayout()

        back_button = QPushButton(
            "← ORQAGA"
        )

        back_button.setObjectName(
            "embeddedBackButton"
        )

        back_button.setCursor(
            Qt.CursorShape.PointingHandCursor
        )

        back_button.clicked.connect(
            self.back_callback
        )

        top.addWidget(
            back_button
        )

        top.addStretch()

        root.insertLayout(
            0,
            top,
        )

    def finish_success(self):
        self.exam_passed.emit()
