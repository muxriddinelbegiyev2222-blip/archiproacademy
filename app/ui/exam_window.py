from ui.answer_radio_button import AnswerRadioButton

import re

from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import (
    QButtonGroup,
    QFrame,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QMessageBox,
    QProgressBar,
    QPushButton,
    QScrollArea,
    QVBoxLayout,
    QWidget,
)

from courses.exam_service import (
    get_exam_questions,
    save_level_exam_attempt,
)


class ExamWindow(QMainWindow):
    exam_passed = Signal()

    def __init__(
        self,
        user: dict,
        exam: dict,
    ):
        super().__init__()

        self.user = user
        self.exam = exam

        self.questions = []
        self.answer_groups = []

        self.setWindowTitle(
            f"ARCHIPRO UZ - {exam['title']}"
        )

        self.resize(
            1100,
            850,
        )

        self.setMinimumSize(
            900,
            650,
        )

        self.setup_styles()

        self.load_exam()

    # ========================================================
    # STYLES
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

            QLabel#examLabel {
                color: #FBBF24;
                font-size: 13px;
                font-weight: 700;
            }

            QLabel#examTitle {
                color: #FFFFFF;
                font-size: 30px;
                font-weight: 700;
            }

            QLabel#examSubtitle {
                color: #94A3B8;
                font-size: 14px;
            }

            QLabel#badge {
                background-color: #172554;
                border: 1px solid #1D4ED8;
                border-radius: 8px;
                padding: 7px 11px;
                color: #BFDBFE;
                font-size: 12px;
                font-weight: 600;
            }

            QLabel#xpBadge {
                background-color: #2A2109;
                border: 1px solid #A16207;
                border-radius: 8px;
                padding: 7px 11px;
                color: #FDE68A;
                font-size: 12px;
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

            QLabel#questionText {
                color: #FFFFFF;
                font-size: 16px;
                font-weight: 600;
            }

            QLabel#explanation {
                background-color: #1E293B;
                border-radius: 8px;
                padding: 10px;
                color: #CBD5E1;
                font-size: 13px;
            }

            QRadioButton {
                color: #CBD5E1;
                font-size: 14px;
                padding: 8px;
            }

            QRadioButton:hover {
                color: #FFFFFF;
            }

            QProgressBar {
                border: none;
                background-color: #1E293B;
                border-radius: 6px;
                height: 10px;
                color: transparent;
            }

            QProgressBar::chunk {
                background-color: #2563EB;
                border-radius: 6px;
            }

            QPushButton#submitButton {
                background-color: #2563EB;
                color: #FFFFFF;
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

            QLabel#successResult {
                background-color: #10251C;
                border: 1px solid #15803D;
                border-radius: 12px;
                padding: 18px;
                color: #BBF7D0;
                font-size: 15px;
                font-weight: 600;
            }

            QLabel#failResult {
                background-color: #291914;
                border: 1px solid #C2410C;
                border-radius: 12px;
                padding: 18px;
                color: #FED7AA;
                font-size: 15px;
                font-weight: 600;
            }
            """
        )

    # ========================================================
    # EXAM LOAD
    # ========================================================

    def load_exam(self):
        self.questions = get_exam_questions(
            self.exam["id"]
        )

        self.answer_groups = []

        self.build_ui()

    # ========================================================
    # UI
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
            14
        )

        # ====================================================
        # HEADER
        # ====================================================

        exam_label = QLabel(
            "MASTERY GATE"
        )

        exam_label.setObjectName(
            "examLabel"
        )

        title = QLabel(
            self.exam["title"]
        )

        title.setObjectName(
            "examTitle"
        )

        title.setWordWrap(
            True
        )

        subtitle = QLabel(
            self.exam.get(
                "description",
                "",
            )
        )

        subtitle.setObjectName(
            "examSubtitle"
        )

        subtitle.setWordWrap(
            True
        )

        root.addWidget(
            exam_label
        )

        root.addWidget(
            title
        )

        root.addWidget(
            subtitle
        )

        # ====================================================
        # INFO
        # ====================================================

        info_layout = QHBoxLayout()

        question_badge = QLabel(
            f"{len(self.questions)} ta savol"
        )

        question_badge.setObjectName(
            "badge"
        )

        passing_badge = QLabel(
            f"O'tish bali: "
            f"{self.exam['passing_score']}%"
        )

        passing_badge.setObjectName(
            "badge"
        )

        xp_badge = QLabel(
            f"+{self.exam['xp_reward']} XP"
        )

        xp_badge.setObjectName(
            "xpBadge"
        )

        info_layout.addWidget(
            question_badge
        )

        info_layout.addWidget(
            passing_badge
        )

        info_layout.addWidget(
            xp_badge
        )

        info_layout.addStretch()

        root.addLayout(
            info_layout
        )

        progress = QProgressBar()

        progress.setRange(
            0,
            100,
        )

        progress.setValue(
            0
        )

        root.addWidget(
            progress
        )

        # ====================================================
        # QUESTIONS
        # ====================================================

        scroll = QScrollArea()

        scroll.setWidgetResizable(
            True
        )

        scroll.setFrameShape(
            QScrollArea.Shape.NoFrame
        )

        content = QWidget()

        content_layout = QVBoxLayout(
            content
        )

        content_layout.setContentsMargins(
            0,
            8,
            12,
            25,
        )

        content_layout.setSpacing(
            16
        )

        for index, question in enumerate(
            self.questions,
            start=1,
        ):
            card = self.create_question_card(
                index=index,
                question=question,
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

        # ====================================================
        # RESULT
        # ====================================================

        self.result_label = QLabel()

        self.result_label.setWordWrap(
            True
        )

        self.result_label.hide()

        root.addWidget(
            self.result_label
        )

        # ====================================================
        # BUTTONS
        # ====================================================

        button_layout = QHBoxLayout()

        button_layout.addStretch()

        self.retry_button = QPushButton(
            "YANGI IMTIHONNI BOSHLASH"
        )

        self.retry_button.setObjectName(
            "retryButton"
        )

        self.retry_button.hide()

        self.retry_button.clicked.connect(
            self.retry_exam
        )

        self.submit_button = QPushButton(
            "IMTIHONNI YAKUNLASH"
        )

        self.submit_button.setObjectName(
            "submitButton"
        )

        self.submit_button.setCursor(
            Qt.CursorShape.PointingHandCursor
        )

        self.submit_button.clicked.connect(
            self.check_exam
        )

        button_layout.addWidget(
            self.retry_button
        )

        button_layout.addWidget(
            self.submit_button
        )

        root.addLayout(
            button_layout
        )

    # ========================================================
    # QUESTION CARD
    # ========================================================

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
            8
        )

        question_label = QLabel(
            f"{index}. "
            f"{question['question_text']}"
        )

        question_label.setObjectName(
            "questionText"
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
                letter = display_letters[
                    option_index
                ]

            else:
                letter = str(
                    option_index + 1
                )

            button = AnswerRadioButton(
                f"{letter}. "
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

        explanation_label = QLabel()

        explanation_label.setObjectName(
            "explanation"
        )

        explanation_label.setWordWrap(
            True
        )

        explanation_label.hide()

        layout.addWidget(
            explanation_label
        )

        self.answer_groups.append(
            {
                "question": question,
                "group": group,
                "buttons": buttons,
                "card": card,
                "explanation": explanation_label,
            }
        )

        return card

    # ========================================================
    # CHECK EXAM
    # ========================================================

    def check_exam(self):
        if self._submitted:
            return
        if not self.questions:
            QMessageBox.warning(
                self,
                "Imtihon",
                "Imtihon savollari topilmadi.",
            )

            return

        # Barcha savollarga javob berilganmi?
        for item in self.answer_groups:
            if (
                item["group"].checkedButton()
                is None
            ):
                QMessageBox.warning(
                    self,
                    "Javob yetishmayapti",
                    (
                        "Barcha savollarga javob bering.\n\n"
                        "Javobsiz savol qoldirmang."
                    ),
                )

                return

        correct_count = 0
        wrong_count = 0

        for item in self.answer_groups:
            selected = (
                item["group"].checkedButton()
            )

            selected_correct = bool(
                selected.property(
                    "is_correct"
                )
            )

            # Natijadan keyin javoblarni
            # o'zgartirib bo'lmaydi.
            for button in item["buttons"]:
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
                            font-weight: 700;
                        }
                        """
                    )

            if selected_correct:
                correct_count += 1

            else:
                wrong_count += 1

                card = item["card"]

                card.setObjectName(
                    "wrongCard"
                )

                card.style().unpolish(
                    card
                )

                card.style().polish(
                    card
                )

                explanation = (
                    item["question"].get(
                        "explanation",
                        "",
                    )
                )

                if explanation:
                    item[
                        "explanation"
                    ].setText(
                        "Tushuntirish: "
                        + explanation
                    )

                    item[
                        "explanation"
                    ].show()

        total = len(
            self.questions
        )

        score = round(
            (
                correct_count
                / total
            )
            * 100
        )

        passed = (
            score
            >= self.exam[
                "passing_score"
            ]
        )

        save_level_exam_attempt(
            user_id=self.user["id"],
            exam_id=self.exam["id"],
            score=score,
            correct_answers=correct_count,
            total_questions=total,
            passed=passed,
        )
        self._submitted = True


        self.submit_button.hide()

        if passed:
            self.show_success(
                score=score,
                correct_count=correct_count,
                wrong_count=wrong_count,
                total=total,
            )

        else:
            self.show_failure(
                score=score,
                correct_count=correct_count,
                wrong_count=wrong_count,
                total=total,
            )

    # ========================================================
    # LEVEL NUMBER
    # ========================================================

    def get_current_level_number(self):
        title = str(
            self.exam.get(
                "title",
                "",
            )
        )

        match = re.search(
            r"(?:LEVEL|BOSQICH)\s*0*(\d+)",
            title,
            flags=re.IGNORECASE,
        )

        if match is None:
            return None

        try:
            return int(
                match.group(1)
            )

        except ValueError:
            return None

    def get_success_message(self):
        current_level = (
            self.get_current_level_number()
        )

        if current_level is None:
            return (
                "Imtihon muvaffaqiyatli "
                "yakunlandi."
            )

        if current_level >= 15:
            return (
                "ARCHIPRO UZ o'quv dasturining "
                "barcha bosqichlari "
                "muvaffaqiyatli yakunlandi."
            )

        next_level = (
            current_level + 1
        )

        return (
            f"BOSQICH {next_level} ochildi."
        )

    # ========================================================
    # SUCCESS
    # ========================================================

    def show_success(
        self,
        score: int,
        correct_count: int,
        wrong_count: int,
        total: int,
    ):
        self.result_label.setObjectName(
            "successResult"
        )

        success_message = (
            self.get_success_message()
        )

        self.result_label.setText(
            (
                "🏆 BOSQICH MUVAFFAQIYATLI "
                "YAKUNLANDI\n\n"

                f"Natija: {score}%\n"

                f"To'g'ri: "
                f"{correct_count}/{total}\n"

                f"Noto'g'ri: "
                f"{wrong_count}/{total}\n\n"

                f"Talab: "
                f"{self.exam['passing_score']}%\n\n"

                f"{success_message}"
            )
        )

        self.result_label.style().unpolish(
            self.result_label
        )

        self.result_label.style().polish(
            self.result_label
        )

        self.result_label.show()

        continue_button = QPushButton(
            "AKADEMIYAGA QAYTISH  →"
        )

        continue_button.setObjectName(
            "submitButton"
        )

        continue_button.clicked.connect(
            self.finish_success
        )

        self.centralWidget().layout().addWidget(
            continue_button,
            alignment=Qt.AlignmentFlag.AlignRight,
        )

    # ========================================================
    # FAILURE
    # ========================================================

    def show_failure(
        self,
        score: int,
        correct_count: int,
        wrong_count: int,
        total: int,
    ):
        self.result_label.setObjectName(
            "failResult"
        )

        self.result_label.setText(
            (
                "IMTIHON HALI TOPSHIRILMADI\n\n"

                f"Natija: {score}%\n"

                f"To'g'ri: "
                f"{correct_count}/{total}\n"

                f"Noto'g'ri: "
                f"{wrong_count}/{total}\n\n"

                f"Kamida "
                f"{self.exam['passing_score']}% "
                f"kerak.\n\n"

                "Xato savollardagi "
                "tushuntirishlarni "
                "ko'rib chiqing va "

                "yangi variant bilan "
                "qayta urinib ko'ring."
            )
        )

        self.result_label.style().unpolish(
            self.result_label
        )

        self.result_label.style().polish(
            self.result_label
        )

        self.result_label.show()

        self.retry_button.show()

    # ========================================================
    # RETRY
    # ========================================================

    def retry_exam(self):
        self.load_exam()

    # ========================================================
    # FINISH
    # ========================================================

    def finish_success(self):
        self.exam_passed.emit()

        self.close()
