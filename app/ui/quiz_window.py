from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import (
    QButtonGroup,
    QFrame,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QRadioButton,
    QScrollArea,
    QVBoxLayout,
    QWidget,
)

from courses.quiz_service import (
    get_best_quiz_score,
    get_quiz_for_lesson,
    save_quiz_attempt,
)


PASSING_SCORE = 80


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

        self.questions = []
        self.answer_groups = []

        self.setWindowTitle(
            f"ARCHIPRO UZ - Test - "
            f"{lesson['title']}"
        )

        self.resize(
            1000,
            800,
        )

        self.setMinimumSize(
            850,
            650,
        )

        self.setup_styles()

        self.load_quiz()

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

            QLabel#title {
                font-size: 29px;
                font-weight: 700;
                color: #FFFFFF;
            }

            QLabel#subtitle {
                font-size: 14px;
                color: #94A3B8;
            }

            QLabel#infoBadge {
                background-color: #172554;
                border: 1px solid #1D4ED8;
                border-radius: 8px;
                padding: 7px 11px;
                color: #BFDBFE;
                font-size: 12px;
                font-weight: 600;
            }

            QLabel#bestScore {
                color: #FBBF24;
                font-size: 13px;
                font-weight: 700;
            }

            QFrame#questionCard {
                background-color: #111827;
                border: 1px solid #1E293B;
                border-radius: 14px;
            }

            QFrame#wrongCard {
                background-color: #291914;
                border: 1px solid #C2410C;
                border-radius: 14px;
            }

            QLabel#question {
                font-size: 16px;
                font-weight: 600;
                color: #FFFFFF;
            }

            QLabel#explanation {
                background-color: #1E293B;
                border-radius: 8px;
                padding: 10px;
                color: #CBD5E1;
                font-size: 13px;
            }

            QRadioButton {
                font-size: 14px;
                color: #CBD5E1;
                padding: 8px;
                spacing: 8px;
            }

            QRadioButton:hover {
                color: #FFFFFF;
            }

            QPushButton#submitButton {
                background-color: #2563EB;
                color: white;
                border: none;
                border-radius: 10px;
                padding: 13px 24px;
                font-size: 14px;
                font-weight: 700;
            }

            QPushButton#submitButton:hover {
                background-color: #3B82F6;
            }

            QPushButton#retryButton {
                background-color: #1E293B;
                color: #FFFFFF;
                border: 1px solid #334155;
                border-radius: 10px;
                padding: 13px 24px;
                font-size: 14px;
                font-weight: 600;
            }

            QPushButton#retryButton:hover {
                background-color: #334155;
            }

            QLabel#resultSuccess {
                background-color: #10251C;
                border: 1px solid #15803D;
                border-radius: 12px;
                padding: 16px;
                color: #BBF7D0;
                font-size: 15px;
                font-weight: 600;
            }

            QLabel#resultFail {
                background-color: #291914;
                border: 1px solid #C2410C;
                border-radius: 12px;
                padding: 16px;
                color: #FED7AA;
                font-size: 15px;
                font-weight: 600;
            }
            """
        )

    def load_quiz(self):
        self.questions = get_quiz_for_lesson(
            lesson_id=self.lesson["id"],
            shuffle_questions=True,
            shuffle_options=True,
        )

        self.answer_groups = []

        self.build_ui()

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
            25,
            30,
            25,
        )

        root.setSpacing(
            15
        )

        # =========================
        # HEADER
        # =========================

        title = QLabel(
            "Mini-test"
        )

        title.setObjectName(
            "title"
        )

        subtitle = QLabel(
            self.lesson.get(
                "title",
                "Dars testi",
            )
        )

        subtitle.setObjectName(
            "subtitle"
        )

        root.addWidget(
            title
        )

        root.addWidget(
            subtitle
        )

        info_layout = QHBoxLayout()

        passing_badge = QLabel(
            f"O'tish bali: {PASSING_SCORE}%"
        )

        passing_badge.setObjectName(
            "infoBadge"
        )

        question_count = QLabel(
            f"Savollar: {len(self.questions)} ta"
        )

        question_count.setObjectName(
            "infoBadge"
        )

        best_score_value = get_best_quiz_score(
            self.user["id"],
            self.lesson["id"],
        )

        best_score = QLabel(
            f"Eng yaxshi natija: "
            f"{best_score_value}%"
        )

        best_score.setObjectName(
            "bestScore"
        )

        info_layout.addWidget(
            passing_badge
        )

        info_layout.addWidget(
            question_count
        )

        info_layout.addStretch()

        info_layout.addWidget(
            best_score
        )

        root.addLayout(
            info_layout
        )

        # =========================
        # QUESTIONS
        # =========================

        scroll = QScrollArea()

        scroll.setWidgetResizable(
            True
        )

        scroll.setFrameShape(
            QScrollArea.Shape.NoFrame
        )

        content = QWidget()

        self.content_layout = QVBoxLayout(
            content
        )

        self.content_layout.setContentsMargins(
            0,
            5,
            12,
            20,
        )

        self.content_layout.setSpacing(
            16
        )

        for index, question in enumerate(
            self.questions,
            start=1,
        ):
            card = self.create_question_card(
                index,
                question,
            )

            self.content_layout.addWidget(
                card
            )

        self.content_layout.addStretch()

        scroll.setWidget(
            content
        )

        root.addWidget(
            scroll,
            1,
        )

        # =========================
        # RESULT
        # =========================

        self.result_label = QLabel()

        self.result_label.setWordWrap(
            True
        )

        self.result_label.hide()

        root.addWidget(
            self.result_label
        )

        # =========================
        # BUTTONS
        # =========================

        buttons = QHBoxLayout()

        buttons.addStretch()

        self.retry_button = QPushButton(
            "QAYTA URINISH"
        )

        self.retry_button.setObjectName(
            "retryButton"
        )

        self.retry_button.hide()

        self.retry_button.clicked.connect(
            self.retry_quiz
        )

        self.submit_button = QPushButton(
            "TESTNI TEKSHIRISH"
        )

        self.submit_button.setObjectName(
            "submitButton"
        )

        self.submit_button.setCursor(
            Qt.CursorShape.PointingHandCursor
        )

        self.submit_button.clicked.connect(
            self.check_answers
        )

        buttons.addWidget(
            self.retry_button
        )

        buttons.addWidget(
            self.submit_button
        )

        root.addLayout(
            buttons
        )

    def create_question_card(
        self,
        index: int,
        question: dict,
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

        layout.setSpacing(
            7
        )

        question_label = QLabel(
            f"{index}. "
            f"{question['question_text']}"
        )

        question_label.setObjectName(
            "question"
        )

        question_label.setWordWrap(
            True
        )

        layout.addWidget(
            question_label
        )

        group = QButtonGroup(
            self
        )

        group.setExclusive(
            True
        )

        buttons = []

        display_letters = [
            "A",
            "B",
            "C",
            "D",
            "E",
            "F",
        ]

        for option_index, option in enumerate(
            question["options"]
        ):
            if option_index < len(
                display_letters
            ):
                display_key = display_letters[
                    option_index
                ]
            else:
                display_key = str(
                    option_index + 1
                )

            button = QRadioButton(
                f"{display_key}. "
                f"{option['option_text']}"
            )

            button.setProperty(
                "is_correct",
                bool(
                    option[
                        "is_correct"
                    ]
                ),
            )

            group.addButton(
                button
            )

            layout.addWidget(
                button
            )

            buttons.append(
                button
            )

        explanation = QLabel()

        explanation.setObjectName(
            "explanation"
        )

        explanation.setWordWrap(
            True
        )

        explanation.hide()

        layout.addWidget(
            explanation
        )

        self.answer_groups.append(
            {
                "question": question,
                "group": group,
                "buttons": buttons,
                "card": card,
                "explanation": explanation,
            }
        )

        return card

    def check_answers(self):
        # Avval barcha savollarga javob
        # berilganini tekshiramiz.

        for item in self.answer_groups:
            group = item["group"]

            if group.checkedButton() is None:
                QMessageBox.warning(
                    self,
                    "Javob yetishmayapti",
                    (
                        "Barcha savollarga javob bering.\n\n"
                        "Keyin testni tekshiring."
                    ),
                )

                return

        correct_count = 0
        wrong_count = 0

        for item in self.answer_groups:
            question = item[
                "question"
            ]

            group = item[
                "group"
            ]

            buttons = item[
                "buttons"
            ]

            card = item[
                "card"
            ]

            explanation_label = item[
                "explanation"
            ]

            selected = (
                group.checkedButton()
            )

            selected_is_correct = bool(
                selected.property(
                    "is_correct"
                )
            )

            # Javoblarni o'zgartirib
            # bo'lmaydigan qilamiz.
            for button in buttons:
                button.setEnabled(
                    False
                )

                if bool(
                    button.property(
                        "is_correct"
                    )
                ):
                    button.setStyleSheet(
                        """
                        QRadioButton {
                            color: #86EFAC;
                            font-weight: 600;
                        }
                        """
                    )

            if selected_is_correct:
                correct_count += 1

            else:
                wrong_count += 1

                card.setObjectName(
                    "wrongCard"
                )

                card.style().unpolish(
                    card
                )

                card.style().polish(
                    card
                )

                explanation_text = (
                    question.get(
                        "explanation",
                        "",
                    )
                )

                if explanation_text:
                    explanation_label.setText(
                        "Tushuntirish: "
                        + explanation_text
                    )

                    explanation_label.show()

        total = len(
            self.questions
        )

        if total == 0:
            score = 100
        else:
            score = round(
                (
                    correct_count
                    / total
                )
                * 100
            )

        passed = (
            score >= PASSING_SCORE
        )

        save_quiz_attempt(
            user_id=self.user["id"],
            lesson_id=self.lesson["id"],
            score=score,
            passed=passed,
        )

        self.submit_button.hide()

        if passed:
            self.result_label.setObjectName(
                "resultSuccess"
            )

            self.result_label.setText(
                (
                    f"TEST MUVAFFAQIYATLI ✓\n\n"
                    f"Natija: {score}%\n"
                    f"To'g'ri javob: {correct_count}/{total}\n"
                    f"Noto'g'ri javob: {wrong_count}/{total}\n\n"
                    "Keyingi dars ochildi."
                )
            )

            self.result_label.show()

            continue_button = QPushButton(
                "DAVOM ETISH  →"
            )

            continue_button.setObjectName(
                "submitButton"
            )

            continue_button.clicked.connect(
                self.finish_successfully
            )

            self.centralWidget().layout().addWidget(
                continue_button,
                alignment=Qt.AlignmentFlag.AlignRight,
            )

        else:
            self.result_label.setObjectName(
                "resultFail"
            )

            self.result_label.setText(
                (
                    f"Natija: {score}%\n"
                    f"To'g'ri javob: {correct_count}/{total}\n"
                    f"Noto'g'ri javob: {wrong_count}/{total}\n\n"
                    f"Keyingi dars uchun kamida "
                    f"{PASSING_SCORE}% kerak.\n"
                    "Xato savollardagi tushuntirishlarni "
                    "o'qib, yana urinib ko'ring."
                )
            )

            self.result_label.show()

            self.retry_button.show()

    def retry_quiz(self):
        self.load_quiz()

    def finish_successfully(self):
        self.quiz_passed.emit()

        self.close()
