from PySide6.QtCore import (
    Qt,
    Signal,
)

from PySide6.QtWidgets import (
    QFrame,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QScrollArea,
    QVBoxLayout,
    QWidget,
)

from courses.content_registry import (
    get_lesson_content_by_code,
)

from ui.exam_window import (
    ExamWindow,
)

from ui.quiz_window import (
    QuizWindow,
)


# ============================================================
# ARCHIPRO UZ
# EMBEDDED PAGES V4
#
# Lesson:
#   yangi professional renderer.
#
# Quiz / Exam:
#   mavjud ishlaydigan mexanizm saqlanadi.
# ============================================================


# ============================================================
# LESSON PAGE V4
# ============================================================


class LessonPage(QWidget):

    lesson_completed = Signal(
        int
    )

    def __init__(
        self,
        lesson: dict,
        user: dict,
        back_callback=None,
        open_quiz_callback=None,
    ):
        super().__init__()

        self.lesson = dict(
            lesson
        )

        self.user = user

        self.lesson_id = int(
            self.lesson[
                "id"
            ]
        )

        self.back_callback = (
            back_callback
        )

        self.open_quiz_callback = (
            open_quiz_callback
        )

        self.setObjectName(
            "lessonV4Page"
        )

        self.build_ui()

    # ========================================================
    # STYLE
    # ========================================================

    def setup_styles(self):
        self.setStyleSheet(
            """
            /* ================================================
               ROOT
               ================================================ */

            QWidget#lessonV4Page {
                background-color: #08111F;
                font-family: "Segoe UI";
            }

            QWidget#lessonContent {
                background-color: #08111F;
            }


            /* ================================================
               TOP BAR
               ================================================ */

            QFrame#lessonTopBar {
                background-color: #0B1728;

                border: 1px solid #243953;
                border-radius: 14px;
            }

            QPushButton#backButton {
                background-color: #15243A;

                border: 1px solid #314765;
                border-radius: 9px;

                color: #DCE6F2;

                padding: 8px 16px;

                min-height: 34px;

                font-size: 13px;
                font-weight: 650;
            }

            QPushButton#backButton:hover {
                background-color: #1C304C;

                border-color: #496D98;
            }

            QLabel#xpBadge {
                background-color: #24200F;

                border: 1px solid #7A6427;
                border-radius: 8px;

                color: #F3CB5B;

                padding: 7px 11px;

                font-size: 12px;
                font-weight: 800;
            }


            /* ================================================
               HERO
               ================================================ */

            QFrame#lessonHero {
                background-color: #0E1B2E;

                border: 1px solid #2D4666;
                border-radius: 18px;
            }

            QLabel#lessonLevel {
                color: #68A0FF;

                font-size: 13px;
                font-weight: 800;
            }

            QLabel#lessonTitle {
                color: #F5F8FC;

                font-size: 32px;
                font-weight: 800;
            }

            QLabel#lessonMeta {
                color: #9EADC1;

                font-size: 14px;
                font-weight: 500;
            }

            QLabel#lessonPurpose {
                color: #C9D5E4;

                font-size: 14px;
            }


            /* ================================================
               CONTENT CARD — COMMON
               ================================================ */

            QFrame#contentNormal,
            QFrame#contentHighlight,
            QFrame#contentExample,
            QFrame#contentWarning,
            QFrame#contentPractice {
                border-radius: 15px;
            }


            /* ================================================
               NORMAL THEORY
               ================================================ */

            QFrame#contentNormal {
                background-color: #0E1A2C;

                border: 1px solid #263B57;
            }


            /* ================================================
               IMPORTANT / HIGHLIGHT
               ================================================ */

            QFrame#contentHighlight {
                background-color: #102441;

                border: 1px solid #366BC7;
            }


            /* ================================================
               EXAMPLE
               ================================================ */

            QFrame#contentExample {
                background-color: #10251F;

                border: 1px solid #347257;
            }


            /* ================================================
               WARNING / COMMON MISTAKE
               ================================================ */

            QFrame#contentWarning {
                background-color: #2A1D19;

                border: 1px solid #945A3B;
            }


            /* ================================================
               PRACTICE
               ================================================ */

            QFrame#contentPractice {
                background-color: #211D31;

                border: 1px solid #665696;
            }


            /* ================================================
               CARD BADGES
               ================================================ */

            QLabel#typeNormal,
            QLabel#typeHighlight,
            QLabel#typeExample,
            QLabel#typeWarning,
            QLabel#typePractice {
                border-radius: 7px;

                padding: 5px 9px;

                font-size: 10px;
                font-weight: 800;
            }

            QLabel#typeNormal {
                background-color: #17263A;

                border: 1px solid #304761;

                color: #AFC0D4;
            }

            QLabel#typeHighlight {
                background-color: #173460;

                border: 1px solid #3975D9;

                color: #9EC0FF;
            }

            QLabel#typeExample {
                background-color: #17392D;

                border: 1px solid #367B5D;

                color: #8EE0B5;
            }

            QLabel#typeWarning {
                background-color: #44291E;

                border: 1px solid #A4603E;

                color: #F0B083;
            }

            QLabel#typePractice {
                background-color: #332A4C;

                border: 1px solid #7762AA;

                color: #C4B5FD;
            }


            /* ================================================
               CONTENT TEXT
               ================================================ */

            QLabel#blockTitle {
                color: #F0F5FA;

                font-size: 18px;
                font-weight: 750;
            }

            QLabel#blockText {
                color: #CBD6E4;

                font-size: 15px;
                font-weight: 400;
            }


            /* ================================================
               FOOTER
               ================================================ */

            QFrame#lessonFooter {
                background-color: #0B1728;

                border: 1px solid #243953;
                border-radius: 14px;
            }

            QLabel#footerTitle {
                color: #EDF3F9;

                font-size: 15px;
                font-weight: 750;
            }

            QLabel#footerText {
                color: #8FA1B8;

                font-size: 12px;
            }

            QPushButton#quizButton {
                background-color: #356FE0;

                border: 1px solid #5992FA;
                border-radius: 10px;

                color: #FFFFFF;

                padding: 11px 23px;

                min-height: 40px;

                font-size: 14px;
                font-weight: 800;
            }

            QPushButton#quizButton:hover {
                background-color: #477FE5;

                border-color: #79A9FF;
            }


            /* ================================================
               SCROLL
               ================================================ */

            QScrollArea {
                background-color: #08111F;

                border: none;
            }

            QAbstractScrollArea::viewport {
                background-color: #08111F;
            }

            QScrollBar:vertical {
                background-color: #0A1525;

                width: 11px;

                margin: 3px;

                border: none;
            }

            QScrollBar::handle:vertical {
                background-color: #344B68;

                min-height: 50px;

                border-radius: 5px;
            }

            QScrollBar::handle:vertical:hover {
                background-color: #4B688B;
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
        )

    # ========================================================
    # BUILD
    # ========================================================

    def build_ui(self):
        self.setup_styles()

        root = QVBoxLayout(
            self
        )

        root.setContentsMargins(
            26,
            22,
            26,
            18,
        )

        root.setSpacing(
            14
        )

        # ====================================================
        # TOP BAR
        # ====================================================

        top_bar = QFrame()

        top_bar.setObjectName(
            "lessonTopBar"
        )

        top_layout = QHBoxLayout(
            top_bar
        )

        top_layout.setContentsMargins(
            14,
            10,
            14,
            10,
        )

        back_button = QPushButton(
            "← ORQAGA"
        )

        back_button.setObjectName(
            "backButton"
        )

        back_button.setCursor(
            Qt.CursorShape.PointingHandCursor
        )

        if self.back_callback is not None:
            back_button.clicked.connect(
                self.back_callback
            )

        top_layout.addWidget(
            back_button
        )

        top_layout.addStretch()

        xp = self.lesson.get(
            "xp_reward",
            0,
        )

        xp_badge = QLabel(
            f"+{xp} XP"
        )

        xp_badge.setObjectName(
            "xpBadge"
        )

        top_layout.addWidget(
            xp_badge
        )

        root.addWidget(
            top_bar
        )

        # ====================================================
        # HERO
        # ====================================================

        hero = QFrame()

        hero.setObjectName(
            "lessonHero"
        )

        hero_layout = QVBoxLayout(
            hero
        )

        hero_layout.setContentsMargins(
            22,
            20,
            22,
            20,
        )

        hero_layout.setSpacing(
            8
        )

        level_title = (
            self.lesson.get(
                "level_title",
                "",
            )
            or "ARCHIPRO UZ"
        )

        module_title = (
            self.lesson.get(
                "module_title",
                "",
            )
            or ""
        )

        level_label = QLabel(
            level_title
        )

        level_label.setObjectName(
            "lessonLevel"
        )

        lesson_title = QLabel(
            self.lesson.get(
                "title",
                "Dars",
            )
        )

        lesson_title.setObjectName(
            "lessonTitle"
        )

        lesson_title.setWordWrap(
            True
        )

        minutes = self.lesson.get(
            "estimated_minutes",
            0,
        )

        lesson_type = (
            self.lesson.get(
                "lesson_type",
                "theory",
            )
            or "theory"
        )

        passing_score = self.lesson.get(
            "passing_score",
            80,
        )

        type_text = {
            "theory": "NAZARIYA",
            "practice": "AMALIYOT",
        }.get(
            str(
                lesson_type
            ).lower(),
            str(
                lesson_type
            ).upper(),
        )

        meta = QLabel(
            f"{module_title}"
            f"   •   "
            f"{type_text}"
            f"   •   "
            f"{minutes} daqiqa"
            f"   •   "
            f"Mini-test {passing_score}%"
        )

        meta.setObjectName(
            "lessonMeta"
        )

        meta.setWordWrap(
            True
        )

        summary = (
            self.lesson.get(
                "summary",
                "",
            )
            or ""
        )

        hero_layout.addWidget(
            level_label
        )

        hero_layout.addWidget(
            lesson_title
        )

        hero_layout.addWidget(
            meta
        )

        if summary:
            purpose = QLabel(
                summary
            )

            purpose.setObjectName(
                "lessonPurpose"
            )

            purpose.setWordWrap(
                True
            )

            hero_layout.addWidget(
                purpose
            )

        root.addWidget(
            hero
        )

        # ====================================================
        # CONTENT
        # ====================================================

        scroll = QScrollArea()

        scroll.setWidgetResizable(
            True
        )

        content_widget = QWidget()

        content_widget.setObjectName(
            "lessonContent"
        )

        content_layout = QVBoxLayout(
            content_widget
        )

        content_layout.setContentsMargins(
            0,
            0,
            7,
            18,
        )

        content_layout.setSpacing(
            12
        )

        lesson_code = self.lesson.get(
            "code",
            "",
        )

        blocks = (
            get_lesson_content_by_code(
                lesson_code
            )
            or []
        )

        if blocks:
            for index, block in enumerate(
                blocks,
                start=1,
            ):
                content_layout.addWidget(
                    self.create_content_card(
                        block,
                        index,
                    )
                )

        else:
            # Content registrida dars matni topilmasa
            # dastur yiqilmaydi.
            fallback = {
                "title": (
                    self.lesson.get(
                        "title",
                        "Dars",
                    )
                ),
                "type": "normal",
                "text": (
                    self.lesson.get(
                        "summary",
                        "",
                    )
                    or
                    "Ushbu dars kontenti hozircha mavjud emas."
                ),
            }

            content_layout.addWidget(
                self.create_content_card(
                    fallback,
                    1,
                )
            )

        content_layout.addStretch()

        scroll.setWidget(
            content_widget
        )

        root.addWidget(
            scroll,
            1,
        )

        # ====================================================
        # FOOTER
        # ====================================================

        footer = QFrame()

        footer.setObjectName(
            "lessonFooter"
        )

        footer_layout = QHBoxLayout(
            footer
        )

        footer_layout.setContentsMargins(
            18,
            14,
            18,
            14,
        )

        footer_layout.setSpacing(
            18
        )

        footer_text_area = QVBoxLayout()

        footer_title = QLabel(
            "Bilimingizni tekshiring"
        )

        footer_title.setObjectName(
            "footerTitle"
        )

        footer_text = QLabel(
            "Mini-testdan o'tgach dars tugallangan hisoblanadi "
            "va o'quv ketma-ketligi bo'yicha keyingi dars ochiladi."
        )

        footer_text.setObjectName(
            "footerText"
        )

        footer_text.setWordWrap(
            True
        )

        footer_text_area.addWidget(
            footer_title
        )

        footer_text_area.addWidget(
            footer_text
        )

        footer_layout.addLayout(
            footer_text_area,
            1,
        )

        quiz_button = QPushButton(
            "MINI-TESTNI BOSHLASH  →"
        )

        quiz_button.setObjectName(
            "quizButton"
        )

        quiz_button.setCursor(
            Qt.CursorShape.PointingHandCursor
        )

        quiz_button.clicked.connect(
            self.start_quiz
        )

        footer_layout.addWidget(
            quiz_button
        )

        root.addWidget(
            footer
        )

    # ========================================================
    # CONTENT CARD
    # ========================================================

    def create_content_card(
        self,
        block: dict,
        index: int,
    ):
        block_type = str(
            block.get(
                "type",
                "normal",
            )
        ).lower()

        # Har qanday yangi content type paydo bo'lsa
        # normal cardga tushadi.
        if block_type in {
            "highlight",
            "important",
            "key",
        }:
            frame_name = (
                "contentHighlight"
            )

            type_name = (
                "typeHighlight"
            )

            badge_text = (
                "MUHIM"
            )

        elif block_type in {
            "example",
            "case",
        }:
            frame_name = (
                "contentExample"
            )

            type_name = (
                "typeExample"
            )

            badge_text = (
                "MISOL"
            )

        elif block_type in {
            "warning",
            "mistake",
            "error",
        }:
            frame_name = (
                "contentWarning"
            )

            type_name = (
                "typeWarning"
            )

            badge_text = (
                "E'TIBOR"
            )

        elif block_type in {
            "practice",
            "task",
            "exercise",
        }:
            frame_name = (
                "contentPractice"
            )

            type_name = (
                "typePractice"
            )

            badge_text = (
                "AMALIYOT"
            )

        else:
            frame_name = (
                "contentNormal"
            )

            type_name = (
                "typeNormal"
            )

            badge_text = (
                f"{index:02d}"
            )

        card = QFrame()

        card.setObjectName(
            frame_name
        )

        layout = QVBoxLayout(
            card
        )

        layout.setContentsMargins(
            20,
            17,
            20,
            18,
        )

        layout.setSpacing(
            10
        )

        # ----------------------------------------------------
        # CARD HEADER
        # ----------------------------------------------------

        header = QHBoxLayout()

        header.setSpacing(
            10
        )

        badge = QLabel(
            badge_text
        )

        badge.setObjectName(
            type_name
        )

        badge.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        title = QLabel(
            block.get(
                "title",
                "",
            )
            or ""
        )

        title.setObjectName(
            "blockTitle"
        )

        title.setWordWrap(
            True
        )

        header.addWidget(
            badge,
            0,
            Qt.AlignmentFlag.AlignTop,
        )

        header.addWidget(
            title,
            1,
        )

        layout.addLayout(
            header
        )

        # ----------------------------------------------------
        # CARD BODY
        # ----------------------------------------------------

        text = QLabel()

        text.setObjectName(
            "blockText"
        )

        text.setWordWrap(
            True
        )

        text.setTextFormat(
            Qt.TextFormat.RichText
        )

        text.setTextInteractionFlags(
            Qt.TextInteractionFlag.TextSelectableByMouse
        )

        raw_text = (
            block.get(
                "text",
                "",
            )
            or ""
        )

        # Mavjud HTML matn aynan saqlanadi.
        # Faqat umumiy o'qish formatini qo'shamiz.
        html = f"""
        <div style="
            font-family: 'Segoe UI';
            font-size: 15px;
            line-height: 1.55;
            color: #CBD6E4;
        ">
            {raw_text}
        </div>
        """

        text.setText(
            html
        )

        layout.addWidget(
            text
        )

        return card

    # ========================================================
    # QUIZ
    # ========================================================

    def start_quiz(self):
        if self.open_quiz_callback is not None:
            self.open_quiz_callback(
                self
            )

    # ========================================================
    # QUIZ PASSED
    # ========================================================

    def quiz_success(self):
        self.lesson_completed.emit(
            self.lesson_id
        )


# ============================================================
# QUIZ PAGE
# ============================================================


class QuizPage(QuizWindow):

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

    def setup_styles(self):
        super().setup_styles()

        self.setStyleSheet(
            self.styleSheet()
            + """
            QMainWindow,
            QWidget {
                background-color: #08111F;
                font-family: "Segoe UI";
            }

            QLabel#pageTitle {
                color: #F5F8FC;

                font-size: 31px;
                font-weight: 800;
            }

            QLabel#subtitle {
                color: #9DADC1;

                font-size: 15px;
            }

            QLabel#questionText {
                color: #EEF4FA;

                font-size: 18px;
                font-weight: 650;
            }

            QLabel#explanation {
                background-color: #15243A;

                border: 1px solid #304866;
                border-radius: 10px;

                color: #CDD8E6;

                padding: 12px;

                font-size: 14px;
            }

            QRadioButton {
                background-color: #0E1A2C;

                border: 1px solid #263B57;
                border-radius: 10px;

                color: #DCE5EF;

                padding: 11px;

                spacing: 10px;

                font-size: 15px;
            }

            QRadioButton:hover {
                background-color: #12233C;

                border-color: #44668F;
            }

            QPushButton#submitButton,
            QPushButton#retryButton,
            QPushButton#continueButton {
                background-color: #356FE0;

                border: 1px solid #5992FA;
                border-radius: 10px;

                color: white;

                min-height: 40px;

                font-size: 14px;
                font-weight: 750;
            }
            """
        )

    def build_ui(self):
        super().build_ui()

        self.connect_embedded_back()

    def connect_embedded_back(self):
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
# EXAM PAGE
# ============================================================


class ExamPage(ExamWindow):

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

    def setup_styles(self):
        super().setup_styles()

        self.setStyleSheet(
            self.styleSheet()
            + """
            QMainWindow,
            QWidget {
                background-color: #08111F;
                font-family: "Segoe UI";
            }

            QLabel#examLabel {
                color: #EBC65B;

                font-size: 13px;
                font-weight: 800;
            }

            QLabel#examTitle {
                color: #F5F8FC;

                font-size: 31px;
                font-weight: 800;
            }

            QLabel#examSubtitle {
                color: #9DADC1;

                font-size: 15px;
            }

            QLabel#questionText {
                color: #EEF4FA;

                font-size: 18px;
                font-weight: 650;
            }

            QLabel#explanation {
                background-color: #15243A;

                border: 1px solid #304866;
                border-radius: 10px;

                color: #CDD8E6;

                padding: 12px;

                font-size: 14px;
            }

            QRadioButton {
                color: #DCE5EF;

                font-size: 15px;

                padding: 9px;
            }

            QPushButton#embeddedBackButton {
                background-color: #15243A;

                border: 1px solid #314765;
                border-radius: 9px;

                color: #DCE6F2;

                padding: 8px 16px;

                min-height: 34px;

                font-size: 13px;
                font-weight: 650;
            }
            """
        )

    def build_ui(self):
        super().build_ui()

        self.add_embedded_back()

    def add_embedded_back(self):
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
