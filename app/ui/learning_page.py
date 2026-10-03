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
    Mavjud LearningWindow'ning barcha real
    PRO / MASTER / LOCK / EXAM logikasini saqlaydi.

    Faqat:
    - kerakli LEVEL'larni filtrlash;
    - bitta oynadagi ORQAGA tugmasi;
    - sarlavha;
    - shrift o'lchamlari

    bilan shug'ullanadi.
    """

    def __init__(
        self,
        user: dict,
        focus_level_codes=None,
        custom_title=None,
        custom_subtitle=None,
        back_callback=None,
    ):
        self.focus_level_codes = list(
            focus_level_codes
            or []
        )

        self.custom_title = (
            custom_title
        )

        self.custom_subtitle = (
            custom_subtitle
        )

        self.back_callback = (
            back_callback
        )

        super().__init__(
            user=user
        )

    # ========================================================
    # READABILITY
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
            }

            QLabel#moduleTitle {
                font-size: 19px;
                font-weight: 700;
            }

            QLabel#lessonTitle {
                font-size: 16px;
                font-weight: 600;
            }

            QLabel#meta {
                font-size: 13px;
            }

            QPushButton {
                font-size: 14px;
                min-height: 34px;
            }

            QPushButton#backButton {
                font-size: 13px;
                min-height: 32px;
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

    def _apply_shell_overrides(self):
        if self.custom_title:

            title = self.findChild(
                QLabel,
                "pageTitle",
            )

            if title is not None:
                title.setText(
                    self.custom_title
                )

        if self.custom_subtitle:

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

        if self.back_callback is not None:

            back_button = self.findChild(
                QPushButton,
                "backButton",
            )

            if back_button is not None:

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
    # REFRESH
    # ========================================================

    def refresh_page(self):
        self.reload_data()
        self.build_ui()
