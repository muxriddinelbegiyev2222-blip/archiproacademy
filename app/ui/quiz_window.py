from PySide6.QtCore import (
    Qt,
    Signal,
)

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

        self.lesson_id = (
            lesson["id"]
        )

        # ====================================================
        # DYNAMIC PASSING SCORE
        # ====================================================

        self.passing_score = int(
            lesson.get(
                "passing_score",
                80,
            )
        )

        self.questions = []

        self.answer_groups = []

        self.setWindowTitle(
            (
                "ARCHIPRO UZ - MINI TEST - "
                f"{lesson.get('title', 'Dars')}"
            )
        )

        self.resize(
            1050,
            800,
        )

        self.setMinimumSize(
            850,
            650,
        )

        self.setup_styles()

        self.load_quiz()

        self.build_ui()

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

            QScrollArea {
                background-color: transparent;
                border: none;
            }

            QLabel#pageTitle {
                font-size: 28px;
                font-weight: 700;
                color: #FFFFFF;
            }

            QLabel#subtitle {
                font-size: 13px;
                color: #94A3B8;
            }

            QLabel#scoreInfo {
                font-size: 13px;
                color: #FBBF24;
                font-weight: 600;
            }

            QFrame#questionCard {
                background-color: #111827;
                border: 1px solid #1E293B;
                border-radius: 14px;
            }

            QFrame#questionCorrect {
                background-color: #10251C;
                border: 1px solid #15803D;
                border-radius: 14px;
            }

            QFrame#questionWrong {
                background-color: #2A1914;
                border: 1px solid #C2410C;
                border-radius: 14px;
            }

            QLabel#questionText {
                color: #FFFFFF;
                font-size: 16px;
                font-weight: 600;
            }

            QLabel#explanation {
                color: #FDBA74;
                font-size: 13px;
            }

            QRadioButton {
                color: #CBD5E1;
                font-size: 14px;
                spacing: 10px;
                padding: 7px;
            }

            QRadioButton:hover {
                background-color: #172033;
                border-radius: 6px;
            }

            QRadioButton#correctAnswer {
                color: #86EFAC;
                font-weight: 700;
            }

            QRadioButton#wrongAnswer {
                color: #FDBA74;
                font-weight: 700;
            }

            QPushButton#submitButton {
                background-color: #2563EB;
                color: #FFFFFF;
                border: none;
                border-radius: 10px;
                padding: 13px 22px;
                font-size: 14px;
                font-weight: 700;
            }

            QPushButton#submitButton:hover {
                background-color: #3B82F6;
            }

            QPushButton#retryButton {
                background-color: #C2410C;
                color: white;
                border: none;
                border-radius: 10px;
                padding: 13px 22px;
                font-size: 14px;
                font-weight: 700;
            }

            QPushButton#retryButton:hover {
                background-color: #EA580C;
            }

            QPushButton#continueButton {
                background-color: #15803D;
                color: white;
                border: none;
                border-radius: 10px;
                padding: 13px 22px;
                font-size: 14px;
                font-weight: 700;
            }

            QPushButton#continueButton:hover {
                background-color: #16A34A;
            }

            QPushButton#backButton {
                background-color: #1E293B;
                color: #FFFFFF;
                border: none;
                border-radius: 8px;
                padding: 9px 15px;
            }

            QPushButton#backButton:hover {
                background-color: #334155;
            }
            """
        )

    # ========================================================
    # LOAD QUIZ
    # ========================================================

    def load_quiz(self):
        self.questions = (
            get_quiz_for_lesson(
                lesson_id=self.lesson_id,
                shuffle_questions=True,
                shuffle_options=True,
            )
        )

    # ========================================================
    # BUILD UI
    # ========================================================

    def build_ui(self):
        self._submitted = False
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
            15
        )

        # ====================================================
        # TOP
        # ====================================================

        top = QHBoxLayout()

        back_button = QPushButton(
            "← DARSга QAYTISH".replace(
                "га",
                "GA",
            )
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

        # ====================================================
        # HEADER
        # ====================================================

        title = QLabel(
            "MINI-TEST"
        )

        title.setObjectName(
            "pageTitle"
        )

        root.addWidget(
            title
        )

        lesson_title = QLabel(
            self.lesson.get(
                "title",
                "",
            )
        )

        lesson_title.setObjectName(
            "subtitle"
        )

        root.addWidget(
            lesson_title
        )

        best_score = (
            get_best_quiz_score(
                self.user["id"],
                self.lesson_id,
            )
        )

        question_count = len(
            self.questions
        )

        info = QLabel(
            (
                f"Savollar: {question_count}"
                f"   •   "
                f"O'tish talabi: {self.passing_score}%"
                f"   •   "
                f"Eng yaxshi natija: {best_score}%"
            )
        )

        info.setObjectName(
            "scoreInfo"
        )

        root.addWidget(
            info
        )

        # ====================================================
        # NO QUESTIONS
        # ====================================================

        if not self.questions:

            no_questions = QLabel(
                (
                    "Ushbu dars uchun test savollari "
                    "hali mavjud emas."
                )
            )

            no_questions.setObjectName(
                "subtitle"
            )

            root.addWidget(
                no_questions
            )

            root.addStretch()

            return

        # ====================================================
        # SCROLL
        # ====================================================

        scroll = QScrollArea()

        scroll.setWidgetResizable(
            True
        )

        scroll.setFrameShape(
            QScrollArea.Shape.NoFrame
        )

        scroll_content = QWidget()

        self.questions_layout = (
            QVBoxLayout(
                scroll_content
            )
        )

        self.questions_layout.setContentsMargins(
            0,
            10,
            12,
            25,
        )

        self.questions_layout.setSpacing(
            15
        )

        self.answer_groups = []

        letters = [
            "A",
            "B",
            "C",
            "D",
            "E",
            "F",
        ]

        for index, question in enumerate(
            self.questions,
            start=1,
        ):
            question_card = QFrame()

            question_card.setObjectName(
                "questionCard"
            )

            card_layout = QVBoxLayout(
                question_card
            )

            card_layout.setContentsMargins(
                20,
                18,
                20,
                18,
            )

            card_layout.setSpacing(
                10
            )

            question_label = QLabel(
                (
                    f"{index}. "
                    f"{question['question_text']}"
                )
            )

            question_label.setObjectName(
                "questionText"
            )

            question_label.setWordWrap(
                True
            )

            card_layout.addWidget(
                question_label
            )

            group = QButtonGroup(
                question_card
            )

            group.setExclusive(
                True
            )

            option_buttons = []

            for option_index, option in enumerate(
                question["options"]
            ):

                letter = (
                    letters[option_index]
                    if option_index < len(letters)
                    else str(
                        option_index + 1
                    )
                )

                button = QRadioButton(
                    (
                        f"{letter}. "
                        f"{option['option_text']}"
                    )
                )

                button.setProperty(
                    "is_correct",
                    bool(
                        option["is_correct"]
                    ),
                )

                group.addButton(
                    button
                )

                option_buttons.append(
                    button
                )

                card_layout.addWidget(
                    button
                )

            explanation = QLabel(
                ""
            )

            explanation.setObjectName(
                "explanation"
            )

            explanation.setWordWrap(
                True
            )

            explanation.hide()

            card_layout.addWidget(
                explanation
            )

            self.answer_groups.append(
                {
                    "question": question,
                    "group": group,
                    "buttons": option_buttons,
                    "card": question_card,
                    "explanation": explanation,
                }
            )

            self.questions_layout.addWidget(
                question_card
            )

        self.questions_layout.addStretch()

        scroll.setWidget(
            scroll_content
        )

        root.addWidget(
            scroll,
            1,
        )

        # ====================================================
        # RESULT
        # ====================================================

        self.result_label = QLabel(
            ""
        )

        self.result_label.setWordWrap(
            True
        )

        self.result_label.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        self.result_label.hide()

        root.addWidget(
            self.result_label
        )

        # ====================================================
        # BUTTONS
        # ====================================================

        buttons = QHBoxLayout()

        buttons.addStretch()

        self.retry_button = QPushButton(
            "QAYTA URINISH"
        )

        self.retry_button.setObjectName(
            "retryButton"
        )

        self.retry_button.clicked.connect(
            self.retry_quiz
        )

        self.retry_button.hide()

        self.submit_button = QPushButton(
            "JAVOBLARNI TEKSHIRISH"
        )

        self.submit_button.setObjectName(
            "submitButton"
        )

        self.submit_button.clicked.connect(
            self.check_answers
        )

        self.continue_button = QPushButton(
            "DAVOM ETISH  →"
        )

        self.continue_button.setObjectName(
            "continueButton"
        )

        self.continue_button.clicked.connect(
            self.continue_after_pass
        )

        self.continue_button.hide()

        buttons.addWidget(
            self.retry_button
        )

        buttons.addWidget(
            self.submit_button
        )

        buttons.addWidget(
            self.continue_button
        )

        root.addLayout(
            buttons
        )

    # ========================================================
    # CHECK ANSWERS
    # ========================================================

    def check_answers(self):
        if self._submitted or not self.answer_groups:
            return
        # Avval barcha savolga javob berilganini
        # tekshiramiz.
        for item in self.answer_groups:

            selected = (
                item["group"].checkedButton()
            )

            if selected is None:

                QMessageBox.warning(
                    self,
                    "Javob yetishmaydi",
                    (
                        "Barcha savollarga javob bering."
                    ),
                )

                return

        correct_answers = 0

        total_questions = len(
            self.answer_groups
        )

        # ====================================================
        # RESULT PER QUESTION
        # ====================================================

        for item in self.answer_groups:

            selected = (
                item["group"].checkedButton()
            )

            selected_correct = bool(
                selected.property(
                    "is_correct"
                )
            )

            if selected_correct:
                correct_answers += 1

                item["card"].setObjectName(
                    "questionCorrect"
                )

            else:
                item["card"].setObjectName(
                    "questionWrong"
                )

            # Variantlarni bloklaymiz va
            # to'g'ri/noto'g'ri ranglaymiz.
            for button in item[
                "buttons"
            ]:

                button.setEnabled(
                    False
                )

                is_correct = bool(
                    button.property(
                        "is_correct"
                    )
                )

                if is_correct:
                    button.setObjectName(
                        "correctAnswer"
                    )

                elif button is selected:
                    button.setObjectName(
                        "wrongAnswer"
                    )

                button.style().unpolish(
                    button
                )

                button.style().polish(
                    button
                )

            # Noto'g'ri bo'lsa explanation.
            if not selected_correct:

                explanation_text = (
                    item["question"].get(
                        "explanation",
                        "",
                    )
                )

                if explanation_text:

                    item[
                        "explanation"
                    ].setText(
                        (
                            "Izoh: "
                            f"{explanation_text}"
                        )
                    )

                    item[
                        "explanation"
                    ].show()

            item["card"].style().unpolish(
                item["card"]
            )

            item["card"].style().polish(
                item["card"]
            )

        # ====================================================
        # SCORE
        # ====================================================

        if total_questions == 0:
            score = 0

        else:
            score = round(
                (
                    correct_answers
                    / total_questions
                )
                * 100
            )

        passed = (
            score
            >= self.passing_score
        )

        # ====================================================
        # SAVE
        # ====================================================

        save_quiz_attempt(
            user_id=self.user["id"],
            lesson_id=self.lesson_id,
            score=score,
            passed=passed,
        )
        self._submitted = True


        # ====================================================
        # SHOW RESULT
        # ====================================================

        wrong_answers = (
            total_questions
            - correct_answers
        )

        self.result_label.show()

        if passed:

            self.result_label.setStyleSheet(
                """
                QLabel {
                    background-color: #10251C;
                    border: 1px solid #15803D;
                    border-radius: 12px;
                    padding: 16px;
                    color: #86EFAC;
                    font-size: 15px;
                    font-weight: 700;
                }
                """
            )

            self.result_label.setText(
                (
                    "✓ MINI-TEST MUVAFFAQIYATLI\n\n"
                    f"Natija: {score}%\n"
                    f"To'g'ri: {correct_answers}/{total_questions}\n"
                    f"Noto'g'ri: {wrong_answers}/{total_questions}\n\n"
                    "Dars muvaffaqiyatli o'zlashtirildi."
                )
            )

            self.submit_button.hide()

            self.retry_button.hide()

            self.continue_button.show()

        else:

            self.result_label.setStyleSheet(
                """
                QLabel {
                    background-color: #2A1914;
                    border: 1px solid #C2410C;
                    border-radius: 12px;
                    padding: 16px;
                    color: #FDBA74;
                    font-size: 15px;
                    font-weight: 700;
                }
                """
            )

            self.result_label.setText(
                (
                    "Mini-testdan o'tilmadi.\n\n"
                    f"Natija: {score}%\n"
                    f"Talab: {self.passing_score}%\n"
                    f"To'g'ri: {correct_answers}/{total_questions}\n"
                    f"Noto'g'ri: {wrong_answers}/{total_questions}\n\n"
                    "Xato javoblarning izohlarini ko'rib, "
                    "qayta urinib ko'ring."
                )
            )

            self.submit_button.hide()

            self.retry_button.show()

    # ========================================================
    # RETRY
    # ========================================================

    def retry_quiz(self):
        self.load_quiz()

        self.build_ui()

    # ========================================================
    # CONTINUE
    # ========================================================

    def continue_after_pass(self):
        self.quiz_passed.emit()

        self.close()
