from PySide6.QtCore import (
    Qt,
    QTimer,
    Signal,
)

from PySide6.QtWidgets import (
    QFrame,
    QLabel,
    QPushButton,
    QScrollArea,
)

from ui.learning_window import (
    LearningWindow,
)


class LearningPage(
    LearningWindow
):
    lesson_open_requested = Signal(
        object,
        object,
    )

    exam_open_requested = Signal(
        object,
        object,
    )
    """
    ARCHIPRO UZ — Embedded Learning Page

    LearningWindow ichidagi asosiy qoidalar saqlanadi:
    - PRO lock
    - MASTER access
    - lesson progress
    - level progress
    - exam lock

    Bu klass:
    - single-window navigation
    - Bosqich filter
    - professional layout
    - scrollbar fix
    - duplicate header fix

    bilan shug'ullanadi.
    """

    def __init__(
        self,
        user: dict,
        focus_level_codes=None,
        custom_title=None,
        custom_subtitle=None,
        back_callback=None,
        open_lesson_callback=None,
        open_exam_callback=None,
    ):
        self.focus_level_codes = list(
            focus_level_codes
            or []
        )

        self.custom_title = (
            custom_title
            or "Mening o'qishim"
        )

        self.custom_subtitle = (
            custom_subtitle
            or (
                "BOSQICH 00 dan BOSQICH 15 gacha "
                "bo'lgan to'liq o'quv yo'lingiz."
            )
        )

        self.back_callback = (
            back_callback
        )

        self.open_lesson_callback = (
            open_lesson_callback
        )

        self.open_exam_callback = (
            open_exam_callback
        )

        super().__init__(
            user=user
        )

        QTimer.singleShot(
            0,
            self._apply_shell_overrides,
        )

    # ========================================================
    # STYLE
    # ========================================================

    def setup_styles(self):
        super().setup_styles()

        self.setStyleSheet(
            self.styleSheet()
            + """
            /* ===============================================
               PAGE HEADER
               =============================================== */

            QLabel#pageTitle {
                color: #0E5558;
                font-size: 32px;
                font-weight: 800;
            
                font-family: "Georgia";
}

            QLabel#pageSubtitle {
                color: #586B64;
                font-size: 15px;
            }

            /* ===============================================
               BOSQICH
               =============================================== */

            QLabel#levelTitle {
                color: #0E5558;
                font-size: 21px;
                font-weight: 800;
            
                font-family: "Georgia";
}

            QLabel#levelSubtitle {
                color: #586B64;
                font-size: 14px;
            }

            /* ===============================================
               MODULE
               =============================================== */

            QLabel#moduleTitle {
                color: #0E5558;
                font-size: 18px;
                font-weight: 700;
            }

            /* ===============================================
               LESSON
               =============================================== */

            QLabel#lessonTitle {
                color: #0E5558;
                font-size: 15px;
                font-weight: 650;
            }

            QLabel#meta {
                color: #586B64;
                font-size: 13px;
            }

            QLabel#availableStatus,
            QLabel#completedStatus,
            QLabel#lockedStatus,
            QLabel#masterStatus {
                font-size: 13px;
                font-weight: 700;
            }

            /* ===============================================
               EXAM
               =============================================== */

            QLabel#examTitle,
            QLabel#examCompletedTitle {
                font-size: 19px;
                font-weight: 750;
            }

            /* ===============================================
               BUTTONS
               =============================================== */

            QPushButton {
                font-size: 13px;
                min-height: 34px;
            }

            QPushButton#backButton {
                background-color: #FFFDF7;
                border: 1px solid #D5CBBB;
                border-radius: 9px;

                color: #0E5558;

                min-height: 34px;

                padding-left: 16px;
                padding-right: 16px;

                font-size: 13px;
                font-weight: 650;
            }

            QPushButton#backButton:hover {
                background-color: #FFFDF7;
                border-color: #D5CBBB;
            }

            /* ===============================================
               SCROLL AREA
               =============================================== */

            QScrollArea {
                background-color: #F5F1E7;
                border: none;
            }

            QScrollArea > QWidget > QWidget {
                background-color: #F5F1E7;
            }

            QAbstractScrollArea::viewport {
                background-color: #F5F1E7;
                border: none;
            }

            /* ===============================================
               VERTICAL SCROLLBAR
               =============================================== */

            QScrollBar:vertical {
                background-color: #F5F1E7;

                width: 10px;

                margin: 2px 1px 2px 1px;

                border: none;
                border-radius: 5px;
            }

            QScrollBar::handle:vertical {
                background-color: #BDB29E;

                min-height: 48px;

                border: none;
                border-radius: 5px;
            }

            QScrollBar::handle:vertical:hover {
                background-color: #A65D35;
            }

            QScrollBar::add-line:vertical,
            QScrollBar::sub-line:vertical {
                height: 0px;
                border: none;
                background: transparent;
            }

            QScrollBar::add-page:vertical,
            QScrollBar::sub-page:vertical {
                background: transparent;
            }

            /* ===============================================
               HORIZONTAL SCROLLBAR
               =============================================== */

            QScrollBar:horizontal {
                height: 0px;
                max-height: 0px;
                border: none;
                background: transparent;
            }

            QScrollBar::handle:horizontal {
                height: 0px;
                max-height: 0px;
                background: transparent;
            }

            QScrollBar::add-line:horizontal,
            QScrollBar::sub-line:horizontal {
                width: 0px;
                background: transparent;
                border: none;
            }
            """
        )

    # ========================================================
    # DATA
    # ========================================================

    def reload_data(self):
        super().reload_data()

        if not self.focus_level_codes:
            return

        allowed = set(
            self.focus_level_codes
        )

        self.levels = [
            level
            for level in self.levels
            if level.get(
                "code"
            ) in allowed
        ]

    # ========================================================
    # BUILD
    # ========================================================

    def build_ui(self):
        super().build_ui()

        self._apply_shell_overrides()

    # ========================================================
    # SHELL OVERRIDES
    # ========================================================

    def _apply_shell_overrides(self):
        self._apply_page_header()

        self._apply_back_button()

        self._apply_single_level_layout()

        self._fix_scroll_areas()

        self.setWindowTitle(
            f"ARCHIPRO UZ - "
            f"{self.custom_title}"
        )

    # ========================================================
    # PAGE HEADER
    # ========================================================

    def _apply_page_header(self):
        title = self.findChild(
            QLabel,
            "pageTitle",
        )

        if title is not None:
            title.setText(
                self.custom_title
            )

            title.setWordWrap(
                True
            )

        subtitle = self.findChild(
            QLabel,
            "pageSubtitle",
        )

        if subtitle is not None:
            subtitle.setText(
                self.custom_subtitle
            )

            subtitle.setWordWrap(
                True
            )

    # ========================================================
    # BACK BUTTON
    # ========================================================

    def _apply_back_button(self):
        back_button = self.findChild(
            QPushButton,
            "backButton",
        )

        if (
            back_button is None
            or self.back_callback is None
        ):
            return

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

    # ========================================================
    # SINGLE LEVEL PROFESSIONAL LAYOUT
    # ========================================================

    def _apply_single_level_layout(self):
        """
        Bitta Bosqich ochilganda tepada Bosqich nomi allaqachon
        pageTitle sifatida ko'rsatiladi.

        Shuning uchun Bosqich card ichida o'sha sarlavhani
        ikkinchi marta takrorlamaymiz.

        Card ichida foydalanuvchiga tushunarliroq
        "Darslar va modullar" nomini ko'rsatamiz.
        """

        if len(
            self.focus_level_codes
        ) != 1:
            return

        level_titles = self.findChildren(
            QLabel,
            "levelTitle",
        )

        if level_titles:
            level_titles[0].setText(
                "Darslar va modullar"
            )

        level_subtitles = self.findChildren(
            QLabel,
            "levelSubtitle",
        )

        if level_subtitles:
            level_subtitles[0].hide()

    # ========================================================
    # SCROLL FIX
    # ========================================================

    def _fix_scroll_areas(self):
        """
        Windows native oq scrollbar paydo bo'lishini
        oldini oladi.

        Horizontal scroll bu sahifaga kerak emas.
        Faqat vertikal scroll ishlaydi.
        """

        scroll_areas = self.findChildren(
            QScrollArea
        )

        for scroll in scroll_areas:
            scroll.setWidgetResizable(
                True
            )

            scroll.setFrameShape(
                QFrame.Shape.NoFrame
            )

            scroll.setHorizontalScrollBarPolicy(
                Qt.ScrollBarPolicy.ScrollBarAlwaysOff
            )

            scroll.setVerticalScrollBarPolicy(
                Qt.ScrollBarPolicy.ScrollBarAsNeeded
            )

            scroll.setAlignment(
                Qt.AlignmentFlag.AlignTop
                | Qt.AlignmentFlag.AlignLeft
            )

            # MUHIM:
            # viewport/content ga inline stylesheet bermaymiz.
            # Qt'da ota widget stylesheet'i bolalarga meros bo'lib,
            # module/lesson card border va backgroundlarini bosib ketishi
            # mumkin. Scroll ranglari yuqoridagi aniq QSS selectorlar
            # orqali boshqariladi.

    # ========================================================
    # OPEN LESSON
    # ========================================================

    def open_lesson(
        self,
        lesson: dict,
    ):
        """
        Lesson ma'lumotiga:
        - level_title
        - module_title
        - master_mode

        qo'shib embedded LessonPage'ga yuboradi.
        """

        level_title = ""
        module_title = ""

        for level in self.levels:

            found = False

            for module in level.get(
                "modules",
                [],
            ):

                for module_lesson in module.get(
                    "lessons",
                    [],
                ):

                    if (
                        module_lesson.get(
                            "id"
                        )
                        == lesson.get(
                            "id"
                        )
                    ):
                        level_title = (
                            level.get(
                                "title",
                                "",
                            )
                        )

                        module_title = (
                            module.get(
                                "title",
                                "",
                            )
                        )

                        found = True
                        break

                if found:
                    break

            if found:
                break

        lesson_data = dict(
            lesson
        )

        lesson_data[
            "level_title"
        ] = level_title

        lesson_data[
            "module_title"
        ] = module_title

        lesson_data[
            "master_mode"
        ] = self.is_master

        # Embedded shell uchun Qt signal ishlatiladi.
        # Bu lesson row QPushButton -> LearningPage -> AppShell
        # zanjirini aniq va tekshiriladigan qiladi.
        if self.open_lesson_callback is not None:
            self.open_lesson_callback(
                lesson_data,
                self,
            )
            return

        # Signal embedded sahifalar uchun fallback kontrakt.
        # Agar receiver bo'lmasa, standalone oynali usul ishlaydi.
        try:
            if self.receivers(
                self.lesson_open_requested
            ) > 0:
                self.lesson_open_requested.emit(
                    lesson_data,
                    self,
                )
                return
        except Exception:
            pass

        super().open_lesson(
            lesson
        )

    # ========================================================
    # OPEN EXAM
    # ========================================================

    def open_exam(
        self,
        exam: dict,
    ):
        exam_data = dict(
            exam
        )

        exam_data[
            "master_mode"
        ] = self.is_master

        if self.open_exam_callback is not None:
            self.open_exam_callback(
                exam_data,
                self,
            )
            return

        try:
            if self.receivers(
                self.exam_open_requested
            ) > 0:
                self.exam_open_requested.emit(
                    exam_data,
                    self,
                )
                return
        except Exception:
            pass

        super().open_exam(
            exam
        )

    # ========================================================
    # REFRESH
    # ========================================================

    def refresh_page(self):
        self.reload_data()

        self.build_ui()

        QTimer.singleShot(
            0,
            self._apply_shell_overrides,
        )
