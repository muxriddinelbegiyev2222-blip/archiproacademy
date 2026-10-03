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
    Mavjud LearningWindow'ning barcha
    progress va qulf logikasini saqlaydi.
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
                color: #8FA0B8;
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
                font-size: 13px;
                min-height: 32px;
            }
            """
        )

    def reload_data(self):
        super().reload_data()

        if self.focus_level_codes:
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

    def build_ui(self):
        super().build_ui()

        self._apply_shell_overrides()

    def _apply_shell_overrides(self):
        title = self.findChild(
            QLabel,
            "pageTitle",
        )

        if (
            title is not None
            and self.custom_title
        ):
            title.setText(
                self.custom_title
            )

        subtitle = self.findChild(
            QLabel,
            "pageSubtitle",
        )

        if (
            subtitle is not None
            and self.custom_subtitle
        ):
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

    def refresh_page(self):
        self.reload_data()

        self.build_ui()
