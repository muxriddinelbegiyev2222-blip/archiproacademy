import logging
import re

from PySide6.QtCore import (
    Qt,
    Signal,
    QTimer,
)

from PySide6.QtWidgets import (
    QFrame,
    QHBoxLayout,
    QLabel,
    QPlainTextEdit,
    QProgressBar,
    QPushButton,
    QScrollArea,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)

from courses.content_registry import (
    get_lesson_content_by_code,
)

from courses.user_features import (
    get_lesson_note,
    is_lesson_bookmarked,
    save_lesson_note,
    set_lesson_bookmark,
)

from ui.exam_window import (
    ExamWindow,
)

from ui.quiz_window import (
    QuizWindow,
)


class LessonPage(QWidget):

    reading_mode_changed = Signal(bool)

    lesson_completed = Signal(
        int
    )

    def __init__(
        self,
        lesson: dict,
        user: dict,
        back_callback=None,
        open_quiz_callback=None,
        open_next_lesson_callback=None,
    ):
        super().__init__()

        self.lesson = dict(
            lesson
        )

        self.user = user

        self.lesson_id = int(
            self.lesson["id"]
        )

        self.back_callback = (
            back_callback
        )

        self.open_quiz_callback = (
            open_quiz_callback
        )

        self.open_next_lesson_callback = (
            open_next_lesson_callback
        )

        # Bookmark va content yordamchi imkoniyatlar.
        # Ularning bittasi xato qilsa ham asosiy dars sahifasi
        # ochilmay qolmasligi kerak.
        try:
            self.bookmarked = is_lesson_bookmarked(
                self.user["id"],
                self.lesson_id,
            )
        except Exception:
            self.bookmarked = False

        self.reading_mode = False
        self.reading_font_size = 17
        self.reading_labels = []
        self.content_cards = []

        self.map_buttons = []

        self.content_error = None
        try:
            self.blocks = (
                get_lesson_content_by_code(
                    self.lesson.get(
                        "code",
                        "",
                    )
                )
                or []
            )
            if not self.blocks:
                raise ValueError("Dars kontenti topilmadi: " + str(self.lesson.get("code", "")))
            if any(not isinstance(block, dict) or not str(block.get("text", "")).strip()
                   for block in self.blocks):
                raise ValueError("Dars kontenti noto'g'ri formatda")
        except Exception as exc:
            self.content_error = exc
            logging.getLogger(__name__).exception(
                "Lesson content load failed: %s", self.lesson.get("code", "")
            )
            self.blocks = []

        self.setObjectName(
            "lessonPage"
        )

        self.build_ui()

    # ========================================================
    # STYLES
    # ========================================================

    def setup_styles(self):
        self.setStyleSheet(
            """
            QWidget#lessonPage,
            QWidget#lessonContent {
                background-color: #F5F1E7;
                font-family: "Segoe UI";
            }

            /* TOP */

            QFrame#lessonTopBar {
                background-color: #FFFDF7;
                border: 1px solid #D5CBBB;
                border-radius: 14px;
            }

            QPushButton#backButton {
                background-color: #FFFDF7;
                border: 1px solid #D5CBBB;
                border-radius: 9px;
                color: #0E5558;
                padding: 8px 16px;
                min-height: 34px;
                font-size: 13px;
                font-weight: 650;
            }

            QPushButton#backButton:hover {
                background-color: #FFFDF7;
                border-color: #D5CBBB;
            }

            QLabel#xpBadge {
                background-color: #F4E9D7;
                border: 1px solid #D5CBBB;
                border-radius: 8px;
                color: #A65D35;
                padding: 7px 11px;
                font-size: 12px;
                font-weight: 800;
            }

            /* HERO */

            QFrame#lessonHero {
                background-color: #FFFDF7;
                border: 1px solid #D5CBBB;
                border-radius: 18px;
            }

            QLabel#lessonLevel {
                color: #0E5558;
                font-size: 13px;
                font-weight: 800;
            }

            QLabel#lessonTitle {
                color: #0E5558;
                font-size: 24px;
                font-weight: 800;
            
                font-family: "Georgia";
}

            QLabel#lessonMeta {
                color: #586B64;
                font-size: 14px;
            }

            QLabel#lessonPurpose {
                color: #203B36;
                font-size: 14px;
            }

            /* PROGRESS */

            QFrame#progressCard {
                background-color: #FFFDF7;
                border: 1px solid #D5CBBB;
                border-radius: 13px;
            }

            QLabel#progressTitle {
                color: #0E5558;
                font-size: 13px;
                font-weight: 700;
            }

            QLabel#progressText {
                color: #586B64;
                font-size: 12px;
            }

            QProgressBar {
                background-color: #FFFDF7;
                border: none;
                border-radius: 5px;
                height: 9px;
                text-align: center;
            }

            QProgressBar::chunk {
                background-color: #0E5558;
                border-radius: 5px;
            }

            /* MAP */

            QFrame#lessonMap {
                background-color: #FFFDF7;
                border: 1px solid #D5CBBB;
                border-radius: 13px;
            }

            QLabel#mapTitle {
                color: #586B64;
                font-size: 11px;
                font-weight: 800;
            }

            QPushButton#mapButton {
                background-color: #FFFDF7;
                border: 1px solid #D5CBBB;
                border-radius: 7px;
                color: #203B36;
                min-width: 34px;
                max-width: 34px;
                min-height: 30px;
                max-height: 30px;
                font-size: 11px;
                font-weight: 700;
            }

            QPushButton#mapButton:hover {
                background-color: #FFFDF7;
                border-color: #D5CBBB;
            }

            QPushButton#mapButton[active="true"] {
                background-color: #0E5558;
                border-color: #4B7B78;
                color: white;
            }

            /* CONTENT */

            QFrame#contentNormal,
            QFrame#contentHighlight,
            QFrame#contentExample,
            QFrame#contentWarning,
            QFrame#contentPractice {
                border-radius: 15px;
            }

            QFrame#contentNormal {
                background-color: #FFFDF7;
                border: 1px solid #D5CBBB;
            }

            QFrame#contentHighlight {
                background-color: #FFFDF7;
                border: 1px solid #4B7B78;
            }

            QFrame#contentExample {
                background-color: #E7F0E8;
                border: 1px solid #D5CBBB;
            }

            QFrame#contentWarning {
                background-color: #FFFDF7;
                border: 1px solid #B95045;
            }

            QFrame#contentPractice {
                background-color: #FFFDF7;
                border: 1px solid #D5CBBB;
            }

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
                background-color: #FFFDF7;
                border: 1px solid #D5CBBB;
                color: #203B36;
            }

            QLabel#typeHighlight {
                background-color: #FFFDF7;
                border: 1px solid #4B7B78;
                color: #0E5558;
            }

            QLabel#typeExample {
                background-color: #E7F0E8;
                border: 1px solid #D5CBBB;
                color: #27624A;
            }

            QLabel#typeWarning {
                background-color: #FBECE7;
                border: 1px solid #B95045;
                color: #A65D35;
            }

            QLabel#typePractice {
                background-color: #FFFDF7;
                border: 1px solid #D5CBBB;
                color: #0E5558;
            }

            QLabel#blockTitle {
                color: #0E5558;
                font-size: 18px;
                font-weight: 750;
            }

            QLabel#blockText {
                color: #203B36;
                font-size: 15px;
            }

            /* SUMMARY */

            QFrame#summaryCard {
                background-color: #FFFDF7;
                border: 1px solid #D5CBBB;
                border-radius: 15px;
            }

            QLabel#summaryTitle {
                color: #0E5558;
                font-size: 17px;
                font-weight: 800;
            }

            QLabel#summaryItem {
                color: #0E5558;
                font-size: 14px;
            }

            /* PRACTICAL REVIEW */

            QFrame#reviewCard {
                background-color: #FFFDF7;
                border: 1px solid #D5CBBB;
                border-radius: 15px;
            }

            QLabel#reviewTitle {
                color: #0E5558;
                font-size: 17px;
                font-weight: 800;
            }

            QLabel#reviewItem {
                color: #203B36;
                font-size: 14px;
            }

            /* PERSONAL TOOLS */

            QFrame#personalTools {
                background-color: #FFFDF7;
                border: 1px solid #D5CBBB;
                border-radius: 14px;
            }

            QLabel#personalTitle {
                color: #0E5558;
                font-size: 13px;
                font-weight: 800;
            }

            QPlainTextEdit#lessonNote {
                background-color: #F5F1E7;
                border: 1px solid #D5CBBB;
                border-radius: 10px;
                color: #0E5558;
                padding: 10px;
                font-size: 13px;
            }

            QPushButton#bookmarkButton,
            QPushButton#saveNoteButton,
            QPushButton#nextLessonButton {
                background-color: #FFFDF7;
                border: 1px solid #D5CBBB;
                border-radius: 9px;
                color: #0E5558;
                padding: 8px 14px;
                min-height: 34px;
                font-size: 12px;
                font-weight: 700;
            }

            QPushButton#bookmarkButton:hover,
            QPushButton#saveNoteButton:hover,
            QPushButton#nextLessonButton:hover {
                background-color: #FFFDF7;
                border-color: #D5CBBB;
            }

            QPushButton#nextLessonButton:disabled {
                background-color: #FFFDF7;
                border-color: #D5CBBB;
                color: #586B64;
            }

            /* FOOTER */

            QFrame#lessonFooter {
                background-color: #FFFDF7;
                border: 1px solid #D5CBBB;
                border-radius: 14px;
            }

            QLabel#footerTitle {
                color: #0E5558;
                font-size: 15px;
                font-weight: 750;
            }

            QLabel#footerText {
                color: #586B64;
                font-size: 12px;
            }

            QPushButton#quizButton {
                background-color: #0E5558;
                border: 1px solid #4B7B78;
                border-radius: 10px;
                color: #FFFDF7;
                padding: 7px 14px;
                min-height: 28px;
                font-size: 14px;
                font-weight: 800;
            }

            QPushButton#quizButton:hover {
                background-color: #0E5558;
                border-color: #4B7B78;
            }

            /* SCROLL */

            QScrollArea {
                background-color: #F5F1E7;
                border: none;
            }

            QAbstractScrollArea::viewport {
                background-color: #F5F1E7;
            }

            QScrollBar:vertical {
                background-color: #F5F1E7;
                width: 10px;
                margin: 2px;
                border: none;
                border-radius: 5px;
            }

            QScrollBar::handle:vertical {
                background-color: #BDB29E;
                min-height: 50px;
                border-radius: 5px;
            }

            QScrollBar::handle:vertical:hover {
                background-color: #A65D35;
            }

            QScrollBar::add-line:vertical,
            QScrollBar::sub-line:vertical {
                height: 0px;
            }

            QScrollBar::add-page:vertical,
            QScrollBar::sub-page:vertical {
                background: transparent;
            }

            QScrollBar:horizontal {
                height: 0px;
                max-height: 0px;
                background: transparent;
                border: none;
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
            16,
            10,
            16,
            10,
        )

        root.setSpacing(
            8
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
            10,
            5,
            10,
            5,
        )

        back_button = QPushButton(
            "← ORQAGA"
        )

        back_button.setObjectName(
            "backButton"
        )

        if self.back_callback is not None:
            back_button.clicked.connect(
                lambda checked=False: self.back_callback()
            )

        top_layout.addWidget(
            back_button
        )

        self.bookmark_button = QPushButton(
            "★ XATCHO‘PDA"
            if self.bookmarked
            else "☆ XATCHO‘P"
        )
        self.bookmark_button.setObjectName(
            "bookmarkButton"
        )
        self.bookmark_button.clicked.connect(
            self.toggle_bookmark
        )

        top_layout.addWidget(
            self.bookmark_button
        )

        self.details_button = QPushButton("DARS XARITASI")
        self.details_button.setObjectName("lessonDetailsButton")
        self.details_button.setCheckable(True)
        self.details_button.toggled.connect(self.set_details_visible)
        top_layout.addWidget(self.details_button)

        self.font_smaller_button = QPushButton("A−")
        self.font_smaller_button.setObjectName("readingFontSmaller")
        self.font_smaller_button.clicked.connect(lambda: self.change_reading_font(-1))
        top_layout.addWidget(self.font_smaller_button)
        self.font_size_label = QLabel("17 px")
        self.font_size_label.setObjectName("readingFontSize")
        self.font_size_label.setStyleSheet("color: #203B36; font-size: 12px;")
        top_layout.addWidget(self.font_size_label)
        self.font_larger_button = QPushButton("A+")
        self.font_larger_button.setObjectName("readingFontLarger")
        self.font_larger_button.clicked.connect(lambda: self.change_reading_font(1))
        top_layout.addWidget(self.font_larger_button)
        self.reading_button = QPushButton("O'QISH REJIMI")
        self.reading_button.setObjectName("readingModeButton")
        self.reading_button.setCheckable(True)
        self.reading_button.toggled.connect(self.set_reading_mode)
        top_layout.addWidget(self.reading_button)
        top_bar.setStyleSheet(
            "QPushButton { background-color: #FFFDF7; color: #0E5558;"
            " border: 1px solid #D5CBBB; border-radius: 7px;"
            " padding: 5px 9px; min-height: 24px; font-size: 12px; }"
            "QPushButton:hover { background-color: #FFFDF7; border-color: #4B7B78; }"
            "QPushButton:checked { background-color: #0E5558; border-color: #4B7B78; color: #FFFDF7; }"
            "QPushButton:disabled { background-color: #FFFDF7; color: #586B64; border-color: #D5CBBB; }"
        )
        top_layout.addStretch()

        xp_badge = QLabel(
            f"+{self.lesson.get('xp_reward', 0)} XP"
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
            14,
            9,
            14,
            9,
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

        hero_layout.addWidget(
            level_label
        )

        hero_layout.addWidget(
            lesson_title
        )

        hero_layout.addWidget(
            meta
        )

        summary = (
            self.lesson.get(
                "summary",
                "",
            )
            or ""
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

        self.lesson_hero = hero
        root.addWidget(
            hero
        )

        # ====================================================
        # PROGRESS
        # ====================================================

        progress_card = QFrame()

        progress_card.setObjectName(
            "progressCard"
        )

        progress_layout = QVBoxLayout(
            progress_card
        )

        progress_layout.setContentsMargins(
            15,
            11,
            15,
            11,
        )

        progress_layout.setSpacing(
            7
        )

        progress_top = QHBoxLayout()

        progress_title = QLabel(
            "DARS PROGRESSI"
        )

        progress_title.setObjectName(
            "progressTitle"
        )

        self.progress_text = QLabel(
            self._progress_label(
                1
            )
        )

        self.progress_text.setObjectName(
            "progressText"
        )

        progress_top.addWidget(
            progress_title
        )

        progress_top.addStretch()

        progress_top.addWidget(
            self.progress_text
        )

        self.progress_bar = QProgressBar()

        self.progress_bar.setRange(
            0,
            max(
                len(
                    self.blocks
                ),
                1,
            )
        )

        self.progress_bar.setValue(
            1
            if self.blocks
            else 0
        )

        self.progress_bar.setTextVisible(
            False
        )

        progress_layout.addLayout(
            progress_top
        )

        progress_layout.addWidget(
            self.progress_bar
        )

        self.progress_card = progress_card
        progress_card.hide()
        self.lesson_map = None
        root.addWidget(
            progress_card
        )

        # ====================================================
        # LESSON MAP
        # ====================================================

        if self.blocks:
            lesson_map = QFrame()

            lesson_map.setObjectName(
                "lessonMap"
            )

            map_layout = QHBoxLayout(
                lesson_map
            )

            map_layout.setContentsMargins(
                14,
                10,
                14,
                10,
            )

            map_layout.setSpacing(
                7
            )

            map_title = QLabel(
                "DARS XARITASI"
            )

            map_title.setObjectName(
                "mapTitle"
            )

            map_layout.addWidget(
                map_title
            )

            map_layout.addSpacing(
                6
            )

            for index in range(
                len(
                    self.blocks
                )
            ):
                button = QPushButton(
                    f"{index + 1:02d}"
                )

                button.setObjectName(
                    "mapButton"
                )

                button.setProperty(
                    "active",
                    index == 0,
                )

                button.clicked.connect(
                    lambda checked=False,
                    i=index:
                    self.jump_to_block(
                        i
                    )
                )

                self.map_buttons.append(
                    button
                )

                map_layout.addWidget(
                    button
                )

            map_layout.addStretch()

            self.lesson_map = lesson_map
            lesson_map.hide()
            root.addWidget(
                lesson_map
            )

        # ====================================================
        # SCROLL
        # ====================================================

        self.scroll = QScrollArea()

        self.scroll.setWidgetResizable(
            True
        )

        self.scroll.setHorizontalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOff
        )

        content_widget = QWidget()

        content_widget.setObjectName(
            "lessonContent"
        )

        self.content_widget = (
            content_widget
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

        if self.blocks:
            for index, block in enumerate(
                self.blocks,
                start=1,
            ):
                card = (
                    self.create_content_card(
                        block,
                        index,
                    )
                )

                self.content_cards.append(
                    card
                )

                content_layout.addWidget(
                    card
                )

        else:
            fallback = {
                "title": "Dars ma'lumotlari yuklanmadi",
                "type": "error",
                "text": (
                    "To'liq dars matnini ochib bo'lmadi. Dasturni qayta oching. "
                    "Muammo davom etsa, yangilangan dastur nusxasini o'rnating "
                    "yoki yordam xizmatiga murojaat qiling."
                ),
            }

            card = (
                self.create_content_card(
                    fallback,
                    1,
                )
            )

            self.content_cards.append(
                card
            )

            content_layout.addWidget(
                card
            )

        # ====================================================
        # PERSONAL NOTE
        # ====================================================

        personal_tools = QFrame()
        personal_tools.setObjectName(
            "personalTools"
        )

        personal_layout = QVBoxLayout(
            personal_tools
        )
        personal_layout.setContentsMargins(
            18,
            15,
            18,
            15,
        )
        personal_layout.setSpacing(
            8
        )

        personal_title = QLabel(
            "MENING ESLATMAM  •  AVTOMATIK SAQLANADI"
        )
        personal_title.setObjectName(
            "personalTitle"
        )

        self.note_input = QPlainTextEdit()
        self.note_input.setObjectName(
            "lessonNote"
        )
        self.note_input.setPlaceholderText(
            "Ushbu dars bo'yicha o'zingiz uchun qisqa eslatma yozing..."
        )
        self.note_input.setMaximumHeight(
            110
        )
        try:
            saved_note = get_lesson_note(
                self.user["id"],
                self.lesson_id,
            )
        except Exception:
            saved_note = ""

        self.note_input.setPlainText(
            saved_note
        )

        self.note_autosave_timer = QTimer(
            self
        )
        self.note_autosave_timer.setSingleShot(
            True
        )
        self.note_autosave_timer.timeout.connect(
            self.save_note_silent
        )
        self.note_input.textChanged.connect(
            lambda:
            self.note_autosave_timer.start(
                700
            )
        )

        save_note_button = QPushButton(
            "ESLATMANI SAQLASH"
        )
        save_note_button.setObjectName(
            "saveNoteButton"
        )
        save_note_button.clicked.connect(
            self.save_note
        )

        personal_layout.addWidget(
            personal_title
        )
        personal_layout.addWidget(
            self.note_input
        )
        personal_layout.addWidget(
            save_note_button,
            0,
            Qt.AlignmentFlag.AlignRight,
        )

        content_layout.addWidget(
            personal_tools
        )

        # ====================================================
        # SUMMARY CARD
        # ====================================================

        summary_card = (
            self.create_summary_card()
        )

        if summary_card is not None:
            content_layout.addWidget(
                summary_card
            )

        # ====================================================
        # PRACTICAL REVIEW
        # ====================================================

        review_card = (
            self.create_review_card()
        )

        if review_card is not None:
            content_layout.addWidget(
                review_card
            )

        content_layout.addStretch()

        self.scroll.setWidget(
            content_widget
        )

        self.scroll.verticalScrollBar(
        ).valueChanged.connect(
            self.update_scroll_progress
        )

        root.addWidget(
            self.scroll,
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
            12,
            6,
            12,
            6,
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
            "Mini-testdan muvaffaqiyatli o'tgach "
            "ushbu dars tugallangan hisoblanadi "
            "va keyingi dars ochiladi."
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

        quiz_button.setEnabled(bool(self.blocks))
        quiz_button.clicked.connect(
            self.start_quiz
        )

        footer_layout.addWidget(
            quiz_button
        )

        self.next_lesson_button = QPushButton(
            "KEYINGI DARS  →"
        )
        self.next_lesson_button.setObjectName(
            "nextLessonButton"
        )

        lesson_status = str(
            self.lesson.get(
                "status",
                "",
            )
        ).lower()

        self.next_lesson_button.setEnabled(
            bool(self.blocks) and lesson_status == "completed"
        )

        self.next_lesson_button.clicked.connect(
            self.open_next_lesson
        )

        footer_layout.addWidget(
            self.next_lesson_button
        )

        root.addWidget(
            footer
        )

        QTimer.singleShot(
            0,
            self.update_scroll_progress,
        )

    def set_details_visible(self, visible):
        self.progress_card.setVisible(visible)
        if self.lesson_map is not None:
            self.lesson_map.setVisible(visible)

    def set_reading_mode(self, enabled):
        self.reading_mode = bool(enabled)
        self.lesson_hero.setVisible(not enabled)
        self.reading_mode_changed.emit(self.reading_mode)

    def change_reading_font(self, delta):
        size = max(14, min(24, self.reading_font_size + delta))
        if size == self.reading_font_size:
            return
        self.reading_font_size = size
        for label in self.reading_labels:
            template = label.property("readingHtml")
            label.setText(re.sub(r"font-size: \d+px;", f"font-size: {size}px;", template, count=1))
            label.updateGeometry()
        self.font_size_label.setText(f"{size} px")
        self.font_smaller_button.setEnabled(size > 14)
        self.font_larger_button.setEnabled(size < 24)
        self.content_widget.adjustSize()

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

        card.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Maximum,
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
            Qt.TextInteractionFlag.TextSelectableByMouse | Qt.TextInteractionFlag.LinksAccessibleByMouse
        )
        text.setOpenExternalLinks(True)

        raw_text = (
            block.get(
                "text",
                "",
            )
            or ""
        )

        html = f"""
        <div style="
            font-family: 'Segoe UI';
            font-size: {self.reading_font_size}px;
            line-height: 1.55;
            color: #203B36;
        ">
            {raw_text}
        </div>
        """

        text.setProperty("readingHtml", html)
        self.reading_labels.append(text)
        text.setText(
            html
        )

        layout.addWidget(
            text
        )

        return card

    # ========================================================
    # SUMMARY
    # ========================================================

    def create_summary_card(self):
        if not self.blocks:
            return None

        titles = []

        for block in self.blocks:
            title = str(
                block.get(
                    "title",
                    "",
                )
                or ""
            ).strip()

            if (
                title
                and title not in titles
            ):
                titles.append(
                    title
                )

            if len(
                titles
            ) >= 8:
                break

        if not titles:
            return None

        card = QFrame()

        card.setObjectName(
            "summaryCard"
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
            8
        )

        title = QLabel(
            "DARS XULOSASI"
        )

        title.setObjectName(
            "summaryTitle"
        )

        layout.addWidget(
            title
        )

        for item in titles:
            label = QLabel(
                f"• {item}"
            )

            label.setObjectName(
                "summaryItem"
            )

            label.setWordWrap(
                True
            )

            layout.addWidget(
                label
            )

        return card

    # ========================================================
    # PRACTICAL REVIEW
    # ========================================================

    def create_review_card(self):
        relevant = []

        for block in self.blocks:
            block_type = str(
                block.get(
                    "type",
                    "",
                )
            ).lower()

            if block_type not in {
                "example",
                "case",
                "warning",
                "mistake",
                "error",
                "practice",
                "task",
                "exercise",
            }:
                continue

            title = str(
                block.get(
                    "title",
                    "",
                )
                or ""
            ).strip()

            if (
                title
                and title not in relevant
            ):
                relevant.append(
                    title
                )

            if len(
                relevant
            ) >= 6:
                break

        if not relevant:
            return None

        card = QFrame()

        card.setObjectName(
            "reviewCard"
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
            8
        )

        title = QLabel(
            "AMALIY ESLAB QOLISH"
        )

        title.setObjectName(
            "reviewTitle"
        )

        layout.addWidget(
            title
        )

        for item in relevant:
            label = QLabel(
                f"→ {item}"
            )

            label.setObjectName(
                "reviewItem"
            )

            label.setWordWrap(
                True
            )

            layout.addWidget(
                label
            )

        return card

    # ========================================================
    # MAP
    # ========================================================

    def jump_to_block(
        self,
        index: int,
    ):
        if not (
            0
            <= index
            < len(
                self.content_cards
            )
        ):
            return

        card = self.content_cards[
            index
        ]

        self.scroll.ensureWidgetVisible(
            card,
            0,
            20,
        )

        self.set_active_map_button(
            index
        )

    def set_active_map_button(
        self,
        active_index: int,
    ):
        for index, button in enumerate(
            self.map_buttons
        ):
            button.setProperty(
                "active",
                index == active_index,
            )

            button.style(
            ).unpolish(
                button
            )

            button.style(
            ).polish(
                button
            )

    # ========================================================
    # SCROLL PROGRESS
    # ========================================================

    def update_scroll_progress(
        self,
        value=None,
    ):
        if not self.blocks:
            self.progress_bar.setRange(0, 1)
            self.progress_bar.setValue(0)
            self.progress_text.setText("Dars yuklanmadi")
            return
        if not self.content_cards:
            return

        scrollbar = (
            self.scroll.verticalScrollBar()
        )

        maximum = max(
            scrollbar.maximum(),
            1,
        )

        current_value = (
            scrollbar.value()
        )

        ratio = (
            current_value
            / maximum
        )

        block_count = len(
            self.content_cards
        )

        active_index = min(
            int(
                ratio
                * block_count
            ),
            block_count - 1,
        )

        progress_value = min(
            active_index + 1,
            block_count,
        )

        self.progress_bar.setRange(
            0,
            block_count
        )

        self.progress_bar.setValue(
            progress_value
        )

        self.progress_text.setText(
            self._progress_label(
                progress_value
            )
        )

        self.set_active_map_button(
            active_index
        )

    def _progress_label(
        self,
        current: int,
    ):
        total = max(
            len(
                self.blocks
            ),
            1,
        )

        return (
            f"{current} / {total} blok"
        )

    # ========================================================
    # QUIZ
    # ========================================================

    def start_quiz(self):
        if not self.blocks:
            return
        if self.open_quiz_callback is not None:
            self.open_quiz_callback(
                self
            )

    def toggle_bookmark(self):
        requested_state = (
            not self.bookmarked
        )

        try:
            set_lesson_bookmark(
                self.user["id"],
                self.lesson_id,
                requested_state,
            )
            self.bookmarked = requested_state
        except Exception:
            return

        self.bookmark_button.setText(
            "★ XATCHO‘PDA"
            if self.bookmarked
            else "☆ XATCHO‘P"
        )

    def save_note_silent(self):
        try:
            save_lesson_note(
                self.user["id"], self.lesson_id,
                self.note_input.toPlainText(),
            )
            return True
        except Exception:
            return False

    def flush_pending_note(self):
        if self.note_autosave_timer.isActive():
            self.note_autosave_timer.stop()
            return self.save_note_silent()
        return True

    def save_note(self):
        self.note_autosave_timer.stop()
        saved = self.save_note_silent()
        sender = self.sender()
        if isinstance(sender, QPushButton):
            sender.setText("✓ SAQLANDI" if saved else "SAQLANMADI — QAYTA URINING")
            QTimer.singleShot(
                1200, sender,
                lambda: sender.setText("ESLATMANI SAQLASH"),
            )

    def open_next_lesson(self):
        if self.open_next_lesson_callback is not None:
            self.open_next_lesson_callback(
                self
            )

    def mark_completed(self):
        self.lesson[
            "status"
        ] = "completed"

        if hasattr(
            self,
            "next_lesson_button",
        ):
            self.next_lesson_button.setEnabled(
                True
            )

    def quiz_success(self):
        self.mark_completed()

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
                background-color: #F5F1E7;
                font-family: "Segoe UI";
            }

            QLabel#pageTitle {
                color: #0E5558;
                font-size: 31px;
                font-weight: 800;
            
                font-family: "Georgia";
}

            QLabel#subtitle {
                color: #586B64;
                font-size: 15px;
            }

            QLabel#questionText {
                color: #0E5558;
                font-size: 18px;
                font-weight: 650;
            }

            QLabel#explanation {
                background-color: #FFFDF7;
                border: 1px solid #D5CBBB;
                border-radius: 10px;
                color: #203B36;
                padding: 12px;
                font-size: 14px;
            }

            QRadioButton {
                background-color: #FFFDF7;
                border: 1px solid #D5CBBB;
                border-radius: 10px;
                color: #0E5558;
                padding: 11px;
                spacing: 10px;
                font-size: 15px;
            }

            QRadioButton:hover {
                background-color: #FFFDF7;
                border-color: #D5CBBB;
            }

            QPushButton#submitButton,
            QPushButton#retryButton,
            QPushButton#continueButton {
                background-color: #0E5558;
                border: 1px solid #4B7B78;
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
                lambda checked=False: self.back_callback()
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
                background-color: #F5F1E7;
                font-family: "Segoe UI";
            }

            QLabel#examLabel {
                color: #A65D35;
                font-size: 13px;
                font-weight: 800;
            }

            QLabel#examTitle {
                color: #0E5558;
                font-size: 31px;
                font-weight: 800;
            
                font-family: "Georgia";
}

            QLabel#examSubtitle {
                color: #586B64;
                font-size: 15px;
            }

            QLabel#questionText {
                color: #0E5558;
                font-size: 18px;
                font-weight: 650;
            }

            QLabel#explanation {
                background-color: #FFFDF7;
                border: 1px solid #D5CBBB;
                border-radius: 10px;
                color: #203B36;
                padding: 12px;
                font-size: 14px;
            }

            QRadioButton {
                color: #0E5558;
                font-size: 15px;
                padding: 9px;
            }

            QPushButton#embeddedBackButton {
                background-color: #FFFDF7;
                border: 1px solid #D5CBBB;
                border-radius: 9px;
                color: #0E5558;
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

        back_button.clicked.connect(
            lambda checked=False: self.back_callback()
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
