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
    QRadioButton,
    QScrollArea,
    QVBoxLayout,
    QWidget,
)

from courses.exam_service import (
    get_exam_questions,
    save_level_exam_attempt,
)

from database.database import (
    get_connection,
)


# ============================================================
# EXAM WINDOW
# ============================================================

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

        self.result_label = None
        self.retry_button = None
        self.submit_button = None
        self.progress_bar = None

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

            QLabel#masterBadge {
                background-color: #2E1065;
                border: 1px solid #7C3AED;
                border-radius: 8px;
                padding: 7px 11px;
                color: #DDD6FE;
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
    # HELPERS
    # ========================================================

    def is_master_mode(self) -> bool:
        license_type = str(
            self.user.get(
                "license_type",
                "",
            )
        ).upper()

        return license_type == "MASTER"

    def format_level_code(
        self,
        code: str,
    ) -> str:
        """
        LEVEL_03 -> LEVEL 3
        LEVEL_10 -> LEVEL 10
        """

        if not code:
            return ""

        if code.startswith(
            "LEVEL_"
        ):
            number_part = code.replace(
                "LEVEL_",
                "",
                1,
            )

            try:
                number = int(
                    number_part
                )

                return (
                    f"LEVEL {number}"
                )

            except ValueError:
                pass

        return code.replace(
            "_",
            " ",
        )

    def get_level_transition_info(self):
        """
        Joriy Final Exam qaysi LEVELga tegishli ekanini
        database'dan aniqlaydi.

        Keyin navbatdagi LEVELni topadi.

        Bu funksiya LEVEL 0, 1, 2...
        va keyingi barcha LEVELlar uchun universal.
        """

        connection = get_connection()

        try:
            cursor = connection.cursor()

            # ------------------------------------------------
            # CURRENT LEVEL
            # ------------------------------------------------

            cursor.execute(
                """
                SELECT
                    course_levels.id,
                    course_levels.code,
                    course_levels.title,
                    course_levels.sort_order

                FROM level_exams

                INNER JOIN course_levels
                    ON course_levels.id =
                       level_exams.level_id

                WHERE level_exams.id = ?

                LIMIT 1
                """,
                (
                    self.exam["id"],
                ),
            )

            current_level = (
                cursor.fetchone()
            )

            if current_level is None:
                return {
                    "current": None,
                    "next": None,
                }

            # ------------------------------------------------
            # NEXT LEVEL
            # ------------------------------------------------

            cursor.execute(
                """
                SELECT
                    id,
                    code,
                    title,
                    sort_order

                FROM course_levels

                WHERE sort_order > ?

                ORDER BY sort_order ASC

                LIMIT 1
                """,
                (
                    current_level[
                        "sort_order"
                    ],
                ),
            )

            next_level = (
                cursor.fetchone()
            )

            return {
                "current": (
                    dict(current_level)
                    if current_level
                    else None
                ),
                "next": (
                    dict(next_level)
                    if next_level
                    else None
                ),
            }

        finally:
            connection.close()

    def get_success_transition_text(
        self,
    ) -> str:
        """
        Natijada avtomatik:

        LEVEL 1 ochildi.
        LEVEL 2 ochildi.
        LEVEL 3 ochildi.
        ...

        deb ko'rsatadi.
        """

        try:
            transition = (
                self.get_level_transition_info()
            )

            next_level = transition.get(
                "next"
            )

            if next_level:
                next_label = (
                    self.format_level_code(
                        next_level.get(
                            "code",
                            "",
                        )
                    )
                )

                next_title = (
                    next_level.get(
                        "title",
                        "",
                    )
                )

                if next_title:
                    return (
                        f"{next_label} ochildi.\n"
                        f"{next_title}"
                    )

                return (
                    f"{next_label} ochildi."
                )

            return (
                "TABRIKLAYMIZ!\n"
                "Siz akademiyaning oxirgi LEVELini "
                "ham muvaffaqiyatli yakunladingiz."
            )

        except Exception:
            # Database'dan transition matni olinmasa ham
            # imtihon natijasini buzmaymiz.
            return (
                "Keyingi bosqich uchun "
                "progress yangilandi."
            )

    # ========================================================
    # LOAD EXAM
    # ========================================================

    def load_exam(self):
        self.questions = (
            get_exam_questions(
                self.exam["id"]
            )
        )

        self.answer_groups = []

        self.build_ui()

    # ========================================================
    # UI
    # ========================================================

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
        # INFO BADGES
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

        if self.is_master_mode():
            master_badge = QLabel(
                "★ MASTER TEST MODE"
            )

            master_badge.setObjectName(
                "masterBadge"
            )

            info_layout.addWidget(
                master_badge
            )

        info_layout.addStretch()

        root.addLayout(
            info_layout
        )

        # ====================================================
        # PROGRESS
        # ====================================================

        self.progress_bar = (
            QProgressBar()
        )

        self.progress_bar.setRange(
            0,
            100,
        )

        self.progress_bar.setValue(
            0
        )

        root.addWidget(
            self.progress_bar
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

        if not self.questions:
            no_questions = QLabel(
                "Bu Final Exam uchun "
                "savollar topilmadi."
            )

            no_questions.setObjectName(
                "examSubtitle"
            )

            no_questions.setWordWrap(
                True
            )

            content_layout.addWidget(
                no_questions
            )

        for index, question in enumerate(
            self.questions,
            start=1,
        ):
            card = (
                self.create_question_card(
                    index=index,
                    question=question,
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

        if not self.questions:
            self.submit_button.setEnabled(
                False
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
                letter = (
                    display_letters[
                        option_index
                    ]
                )

            else:
                letter = str(
                    option_index + 1
                )

            button = QRadioButton(
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

            button.toggled.connect(
                self.update_progress
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
                "explanation": (
                    explanation_label
                ),
            }
        )

        return card

    # ========================================================
    # PROGRESS
    # ========================================================

    def update_progress(self):
        if not self.answer_groups:
            self.progress_bar.setValue(
                0
            )

            return

        answered = 0

        for item in self.answer_groups:
            if (
                item["group"].checkedButton()
                is not None
            ):
                answered += 1

        progress = round(
            (
                answered
                / len(self.answer_groups)
            )
            * 100
        )

        self.progress_bar.setValue(
            progress
        )

    # ========================================================
    # CHECK EXAM
    # ========================================================

    def check_exam(self):
        if not self.questions:
            QMessageBox.warning(
                self,
                "Imtihon",
                "Imtihon savollari topilmadi.",
            )

            return

        # ====================================================
        # ALL QUESTIONS ANSWERED?
        # ====================================================

        for item in self.answer_groups:
            if (
                item[
                    "group"
                ].checkedButton()
                is None
            ):
                QMessageBox.warning(
                    self,
                    "Javob yetishmayapti",
                    (
                        "Barcha savollarga "
                        "javob bering.\n\n"
                        "Javobsiz savol "
                        "qoldirmang."
                    ),
                )

                return

        correct_count = 0
        wrong_count = 0

        # ====================================================
        # CHECK ANSWERS
        # ====================================================

        for item in self.answer_groups:
            selected = (
                item[
                    "group"
                ].checkedButton()
            )

            selected_correct = bool(
                selected.property(
                    "is_correct"
                )
            )

            # Natijadan keyin
            # javob o'zgarmaydi.
            for button in item[
                "buttons"
            ]:
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

                selected.setStyleSheet(
                    """
                    QRadioButton {
                        color: #FCA5A5;
                        font-weight: 700;
                    }
                    """
                )

                card = item[
                    "card"
                ]

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
                    item[
                        "question"
                    ].get(
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

        passing_score = int(
            self.exam[
                "passing_score"
            ]
        )

        passed = (
            score
            >= passing_score
        )

        # ====================================================
        # SAVE RESULT
        # ====================================================

        save_level_exam_attempt(
            user_id=self.user["id"],
            exam_id=self.exam["id"],
            score=score,
            correct_answers=correct_count,
            total_questions=total,
            passed=passed,
        )

        self.progress_bar.setValue(
            100
        )

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

        transition_text = (
            self.get_success_transition_text()
        )

        master_note = ""

        if self.is_master_mode():
            master_note = (
                "\n\n"
                "★ MASTER TEST MODE\n"
                "Bu natija developer/test "
                "akkauntida bajarildi."
            )

        self.result_label.setText(
            (
                "🏆 LEVEL MUVAFFAQIYATLI "
                "YAKUNLANDI\n\n"

                f"Natija: {score}%\n"

                f"To'g'ri: "
                f"{correct_count}/{total}\n"

                f"Noto'g'ri: "
                f"{wrong_count}/{total}\n\n"

                f"Talab: "
                f"{self.exam['passing_score']}%\n\n"

                f"{transition_text}"

                f"{master_note}"
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

        continue_button.setCursor(
            Qt.CursorShape.PointingHandCursor
        )

        continue_button.clicked.connect(
            self.finish_success
        )

        self.centralWidget().layout().addWidget(
            continue_button,
            alignment=(
                Qt.AlignmentFlag.AlignRight
            ),
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

        missing_score = max(
            0,
            int(
                self.exam[
                    "passing_score"
                ]
            )
            - score,
        )

        self.result_label.setText(
            (
                "IMTIHON HALI "
                "TOPSHIRILMADI\n\n"

                f"Natija: {score}%\n"

                f"To'g'ri: "
                f"{correct_count}/{total}\n"

                f"Noto'g'ri: "
                f"{wrong_count}/{total}\n\n"

                f"Kamida "
                f"{self.exam['passing_score']}% "
                f"kerak.\n"

                f"Yetishmayapti: "
                f"{missing_score} foiz punkt.\n\n"

                "Xato savollardagi "
                "tushuntirishlarni ko'rib "
                "chiqing va yangi variant "
                "bilan qayta urinib ko'ring."
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
