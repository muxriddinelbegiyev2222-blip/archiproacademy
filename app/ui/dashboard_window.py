from ui.app_shell import (
    AppShell,
)


class DashboardWindow(
    AppShell
):
    """
    main.py va login tizimi uchun
    compatibility entry point.
    """

    def __init__(
        self,
        user: dict,
    ):
        super().__init__(
            user=user
        )
