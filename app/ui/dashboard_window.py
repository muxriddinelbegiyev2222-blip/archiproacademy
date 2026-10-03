from PySide6.QtCore import (
    QTimer,
)

from PySide6.QtWidgets import (
    QFrame,
)

from ui.app_shell import (
    AppShell,
)

from ui.developer_badge import (
    DeveloperBadge,
)

from ui.theme import (
    install_premium_theme,
)


class DashboardWindow(
    AppShell
):
    """
    ARCHIPRO UZ asosiy application shell.

    AppShell:
    - navigation
    - PRO / MASTER
    - learning
    - lesson
    - quiz
    - exam

    logikasini boshqaradi.

    DashboardWindow:
    - premium theme
    - developer information
    - final presentation layer

    bilan shug'ullanadi.
    """

    def __init__(
        self,
        user: dict,
    ):
        super().__init__(
            user=user
        )

        self.developer_badge = None

        install_premium_theme(
            self
        )

        self._install_developer_card()

        QTimer.singleShot(
            0,
            self._final_ui_polish,
        )

    # ========================================================
    # DEVELOPER INFO
    # ========================================================

    def _install_developer_card(
        self,
    ):
        sidebar = self.findChild(
            QFrame,
            "sidebar",
        )

        if sidebar is None:
            return

        layout = sidebar.layout()

        if layout is None:
            return

        self.developer_badge = (
            DeveloperBadge(
                sidebar
            )
        )

        layout.addWidget(
            self.developer_badge
        )

    # ========================================================
    # FINAL POLISH
    # ========================================================

    def _final_ui_polish(
        self,
    ):
        install_premium_theme(
            self
        )
