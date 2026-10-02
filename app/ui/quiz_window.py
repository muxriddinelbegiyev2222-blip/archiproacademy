from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import (
    QButtonGroup,
    QFrame,
    QLabel,
    QMessageBox,
    QMainWindow,
    QPushButton,
    QRadioButton,
    QScrollArea,
    QVBoxLayout,
    QWidget,
)

from courses.quiz_service import (
    get_quiz_for_lesson,
    save_quiz_attempt,
)


class QuizWindow(QMainWindow):
    quiz_passed = Signal()

    def __init__(
        self,
        user: dict,
        lesson: dict,
    ):
        super().__init__()

        self.user = user
        self.lesson = lesson

        self.questions = get_quiz_for_lesson(
            lesson["id"]
        )

        self.answer_groups = []

        self.setWindowTitle(
            f"ARCHIPRO UZ - Test - {lesson['title']}"
        )

        self.resize(
            950,
            760,
        )

        self.setStyleSheet(
            """
            QMainWindow {
                background-color: #0B1220;
            }

            QWidget {
                font-family: Segoe UI;
                color: #F8FAFC;
            }

            QLabel#title {
                font-size: 28px;
                font-weight: 700;
                color: white;
            }

            QLabel#subtitle {
                font-size: 14px;
                color: #94A3B8;
            }

            QFrame#questionCard {
                background-color: #111827;
                border: 1px solid #1E293B;
                border-radius: 14px;
            }

            QLabel#question {
                font-size: 16px;
                font-weight: 600;
                color: white;
            }

            QRadioButton {
                font-size: 14px;
                color: #CBD5E1;
                padding: 7px;
            }

            QRadioButton:hover {
                color: white;
            }

            QPushButton#submitButton {
                background-color: #2563EB;
                color: white;
                border: none;
                border-radius: 10px;
                padding: 13px 22px;
                font-size: 14px;
                font-weight: 700;
            }

            QPushButton#submitButton:hover {
                background-color: #3B82F6;
            }
            """
        )

        self.build_ui()

    def build_ui(self):
        central = QWidget()
        self.setCentralWidget(central)

        root = QVBoxLayout(central)

        root.setContentsMargins(
            30,
            25,
            30,
            25,
        )

        root.setSpacing(15)

        title = QLabel(
            "Dars bo'yicha mini-test"
        )

        title.setObjectName(
            "title"
        )

        subtitle = QLabel(
            "Keyingi dars ochilishi uchun kamida 80% natija oling."
        )

        subtitle.setObjectName(
            "subtitle"
        )

        root.addWidget(title)
        root.addWidget(subtitle)

        scroll = QScrollArea()

        scroll.setWidgetResizable(True)

        scroll.setFrameShape(
            QScrollArea.Shape.NoFrame
        )

        content = QWidget()

        content_layout = QVBoxLayout(
            content
        )

        content_layout.setSpacing(
            16
        )

        for index, question in enumerate(
            self.questions,
            start=1,
        ):
            card = QFrame()

            card.setObjectName(
                "questionCard"
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

            question_label = QLabel(
                f"{index}. {question['question_text']}"
            )

            question_label.setObjectName(
                "question"
            )

            question_label.setWordWrap(True)

            layout.addWidget(
                question_label
            )

            group = QButtonGroup(
                self
            )

            group.setExclusive(True)

            for option in question["options"]:
                button = QRadioButton(
                    f"{option['option_key']}. "
                    f"{option['option_text']}"
                )

                button.setProperty(
                    "is_correct",
                    option["is_correct"],
                )

                group.addButton(
                    button
                )

                layout.addWidget(
                    button
                )

            self.answer_groups.append(
                (
                    question,
                    group,
                )
            )

            content_layout.addWidget(
                card
            )

        content_layout.addStretch()

        scroll.setWidget(
            content
        )

        root.addWidget(
            scroll,
            1,
        )

        submit_button = QPushButton(
            "TESTNI TEKSHIRISH"
        )

        submit_button.setObjectName(
            "submitButton"
        )

        submit_button.setCursor(
            Qt.CursorShape.PointingHandCursor
        )

        submit_button.clicked.connect(
            self.check_answers
        )

        root.addWidget(
            submit_button,
            alignment=Qt.AlignmentFlag.AlignRight,
        )

    def check_answers(self):
        if not self.questions:
            self.quiz_passed.emit()
            self.close()
            return

        for question, group in self.answer_groups:
            if group.checkedButton() is None:
                QMessageBox.warning(
                    self,
                    "Test",
                    "Barcha savollarga javob bering.",
                )
                return

        correct_count = 0

        wrong_explanations = []

        for question, group in self.answer_groups:
            selected = group.checkedButton()

            is_correct = bool(
                selected.property(
                    "is_correct"
                )
            )

            if is_correct:
                correct_count += 1
            else:
                wrong_explanations.append(
                    question.get(
                        "explanation",
                        "",
                    )
                )

        total = len(
            self.questions
        )

        score = round(
            (correct_count / total) * 100
        )

        passed = score >= 80

        save_quiz_attempt(
            user_id=self.user["id"],
            lesson_id=self.lesson["id"],
            score=score,
            passed=passed,
        )

        if passed:
            QMessageBox.information(
                self,
                "Ajoyib!",
                (
                    f"Natija: {score}%\n\n"
                    "Test muvaffaqiyatli topshirildi.\n"
                    "Keyingi dars ochiladi."
                ),
            )

            self.quiz_passed.emit()
            self.close()

        else:
            explanation_text = "\n\n".join(
                [
                    text
                    for text in wrong_explanations
                    if text
                ]
            )

            message = (
                f"Natija: {score}%\n\n"
                "Kamida 80% kerak.\n"
                "Darsni yana bir marta ko'rib chiqing."
            )

            if explanation_text:
                message += (
                    "\n\nE'tibor bering:\n"
                    + explanation_text
                )

            QMessageBox.warning(
                self,
                "Yana urinib ko'ring",
                message,
            )
