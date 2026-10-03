from PySide6.QtCore import QTimer

from PySide6.QtWidgets import (
    QLabel,
    QPushButton,
)

from ui.learning_window import (
    LearningWindow,
)


class LearningPage(
    LearningWindow
):
    """
    Mavjud LearningWindow ichidagi:
    - PRO lock
    - MASTER access
    - lesson progress
    - level progress
    - exam lock

    qoidalari saqlanadi.

    Ushbu klass faqat:
    - LEVEL filter
    - embedded navigation
    - title/subtitle
    - readability

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
                "LEVEL 00 dan LEVEL 15 gacha "
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
            QLabel#pageTitle {
                font-size: 34px;
                font-weight: 800;
            }

            QLabel#pageSubtitle {
                font-size: 17px;
                color: #A8B3C7;
            }

            QLabel#masterTitle {
                font-size: 18px;
            }

            QLabel#masterText {
                font-size: 15px;
            }

            QLabel#levelTitle {
                font-size: 24px;
                font-weight: 800;
            }

            QLabel#levelSubtitle {
                font-size: 16px;
                color: #A8B3C7;
            }

            QLabel#moduleTitle {
                font-size: 19px;
                font-weight: 700;
            }

            QLabel#lessonTitle {
                font-size: 16px;
                font-weight: 650;
            }

            QLabel#meta {
                font-size: 14px;
                color: #91A2BA;
            }

            QLabel#availableStatus,
            QLabel#completedStatus,
            QLabel#lockedStatus,
            QLabel#masterStatus {
                font-size: 14px;
            }

            QLabel#examTitle,
            QLabel#examCompletedTitle {
                font-size: 20px;
            }

            QPushButton {
                font-size: 14px;
                min-height: 34px;
            }

            QPushButton#backButton {
                font-size: 14px;
                min-height: 34px;
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
    # TITLE / BACK
    # ========================================================

    def _apply_shell_overrides(self):
        title = self.findChild(
            QLabel,
            "pageTitle",
        )

        if title is not None:
            title.setText(
                self.custom_title
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

        self.setWindowTitle(
            f"ARCHIPRO UZ - "
            f"{self.custom_title}"
        )

    # ========================================================
    # OPEN LESSON
    # ========================================================

    def open_lesson(
        self,
        lesson: dict,
    ):
        """
        Original LearningWindow lesson ma'lumotiga
        level_title va module_title qo'shardi.

        Shu logikani aynan saqlaymiz.
        """

        level_title = ""
        module_title = ""

        for level in self.levels:

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

        if self.open_lesson_callback is not None:
            self.open_lesson_callback(
                lesson_data,
                self,
            )

            return

        # Fallback:
        # shell callback bo'lmasa eski usul.
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
