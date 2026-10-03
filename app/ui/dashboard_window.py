from ui.app_shell import AppShell


class DashboardWindow(AppShell):
    """
    ARCHIPRO UZ asosiy oynasi.

    Eski DashboardWindow nomi saqlab qolindi,
    chunki login/main.py shu klassni chaqiradi.

    Asosiy navigatsiya endi AppShell orqali
    bitta oynaning ichida ishlaydi.
    """

    def __init__(
        self,
        user: dict,
    ):
        super().__init__(
            user=user
        )
