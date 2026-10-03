from PySide6.QtCore import Qt

from PySide6.QtWidgets import (
    QHBoxLayout,
    QPushButton,
)

from ui.lesson_window import LessonWindow
from ui.quiz_window import QuizWindow
from ui.exam_window import ExamWindow


# ============================================================
# LESSON PAGE
# ============================================================


class LessonPage(LessonWindow):
    """
    Eski LessonWindow logikasi saqlanadi.

    Farqi:
    - alohida Windows bo'lib ochilmaydi;
    - ORQAGA AppShell ichida ishlaydi;
    - mini-test AppShell ichida ochiladi;
    - quiz tugagach lesson_completed signali saqlanadi.
    """

    def __init__(
        self,
        lesson: dict,
        user: dict,
        back_callback=None,
        open_quiz_callback=None,
    ):
        self.back_callback = back_callback
        self.open_quiz_callback = open_quiz_callback

        super().__init__(
            lesson=lesson,
            user=user,
        )

    # ========================================================
    # STYLE
    # ========================================================

    def setup_styles(self):
        super().setup_styles()

        self.setStyleSheet(
            self.styleSheet()
            + """
            QLabel#lessonLevel {
                font-size: 15px;
                font-weight: 650;
            }

            QLabel#lessonTitle {
                font-size: 34px;
                font-weight: 800;
            }

            QLabel#lessonMeta {
                font-size: 15px;
                color: #A8B3C7;
            }

            QLabel#sectionTitle {
                font-size: 21px;
                font-weight: 750;
            }

            QLabel#bodyText {
                font-size: 17px;
                color: #D2DAE5;
            }

            QPushButton#backButton {
                font-size: 14px;
                min-height: 34px;
            }

            QPushButton#quizButton {
                font-size: 15px;
                min-height: 40px;
                padding-left: 22px;
                padding-right: 22px;
            }
            """
        )

    # ========================================================
    # BUILD
    # ========================================================

    def build_ui(self):
        super().build_ui()

        self._connect_embedded_back()

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

    # ========================================================
    # QUIZ
    # ========================================================

    def start_quiz(self):
        if self.open_quiz_callback is not None:
            self.open_quiz_callback(
                self
            )

            return

        # Fallback:
        # callback bo'lmasa eski tizim ishlayveradi.
        super().start_quiz()

    # ========================================================
    # QUIZ PASSED
    # ========================================================

    def quiz_success(self):
        """
        Eski LessonWindow.quiz_success() signal yuborib,
        oynani close qilardi.

        Embedded rejimda close qilmaymiz.
        AppShell qaysi sahifaga qaytishni o'zi boshqaradi.
        """

        self.lesson_completed.emit(
            self.lesson_id
        )


# ============================================================
# QUIZ PAGE
# ============================================================


class QuizPage(QuizWindow):
    """
    Eski QuizWindow logikasi to'liq saqlanadi.

    Farqi:
    - darsga qaytish AppShell orqali;
    - test o'tilganda embedded navigation ishlaydi.
    """

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

    # ========================================================
    # STYLE
    # ========================================================

    def setup_styles(self):
        super().setup_styles()

        self.setStyleSheet(
            self.styleSheet()
            + """
            QLabel#pageTitle {
                font-size: 32px;
                font-weight: 800;
            }

            QLabel#subtitle {
                font-size: 16px;
                color: #A8B3C7;
            }

            QLabel#scoreInfo {
                font-size: 15px;
            }

            QLabel#questionText {
                font-size: 18px;
                font-weight: 650;
            }

            QLabel#explanation {
                font-size: 15px;
            }

            QRadioButton {
                font-size: 16px;
                spacing: 11px;
                padding: 9px;
            }

            QPushButton#submitButton,
            QPushButton#retryButton,
            QPushButton#continueButton {
                font-size: 15px;
                min-height: 40px;
            }

            QPushButton#backButton {
                font-size: 14px;
                min-height: 34px;
            }
            """
        )

    # ========================================================
    # BUILD
    # ========================================================

    def build_ui(self):
        super().build_ui()

        self._connect_embedded_back()

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

    # ========================================================
    # SUCCESS
    # ========================================================

    def continue_after_pass(self):
        """
        Eski QuizWindow bu yerda self.close() qilardi.
        Embedded rejimda faqat signal yuboramiz.
        """

        self.quiz_passed.emit()


# ============================================================
# EXAM PAGE
# ============================================================


class ExamPage(ExamWindow):
    """
    Eski ExamWindow:
    - savollar
    - scoring
    - passing score
    - exam attempt
    - XP
    - success/failure

    logikasini saqlaydi.

    Faqat AppShell ichiga joylashtiriladi.
    """

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

    # ========================================================
    # STYLE
    # ========================================================

    def setup_styles(self):
        super().setup_styles()

        self.setStyleSheet(
            self.styleSheet()
            + """
            QLabel#examLabel {
                font-size: 15px;
            }

            QLabel#examTitle {
                font-size: 32px;
                font-weight: 800;
            }

            QLabel#examSubtitle {
                font-size: 16px;
                color: #A8B3C7;
            }

            QLabel#badge,
            QLabel#xpBadge {
                font-size: 14px;
            }

            QLabel#questionText {
                font-size: 18px;
                font-weight: 650;
            }

            QLabel#explanation {
                font-size: 15px;
            }

            QRadioButton {
                font-size: 16px;
                padding: 9px;
            }

            QPushButton#submitButton,
            QPushButton#retryButton {
                font-size: 15px;
                min-height: 40px;
            }

            QLabel#successResult,
            QLabel#failResult {
                font-size: 16px;
            }

            QPushButton#embeddedBackButton {
                background-color: #1E293B;
                color: #FFFFFF;
                border: none;
                border-radius: 8px;
                padding: 9px 16px;
                font-size: 14px;
                font-weight: 650;
                min-height: 34px;
            }

            QPushButton#embeddedBackButton:hover {
                background-color: #334155;
            }
            """
        )

    # ========================================================
    # BUILD
    # ========================================================

    def build_ui(self):
        super().build_ui()

        self._add_embedded_back()

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

    # ========================================================
    # SUCCESS FINISH
    # ========================================================

    def finish_success(self):
        """
        Eski ExamWindow self.close() qilardi.
        Embedded rejimda AppShell boshqaradi.
        """

        self.exam_passed.emit()
