import sys

from PySide6.QtWidgets import QApplication

from auth.auth_service import authenticate_user, create_user
from database.database import initialize_database
from ui.dashboard_window import DashboardWindow
from ui.login_window import LoginWindow


def prepare_application():
    """
    Dastur ishga tushishidan oldin lokal database tayyorlanadi.
    """

    initialize_database()

    # Bu foydalanuvchi faqat ishlab chiqish davri uchun.
    # Sotuv versiyasida bu olib tashlanadi.
    create_user(
        username="admin",
        password="12345",
        full_name="Administrator",
        license_type="MASTER",
    )


def main():
    app = QApplication(sys.argv)

    app.setApplicationName("ARCHIPRO UZ")
    app.setOrganizationName("ARCHIPRO UZ")

    prepare_application()

    login_window = LoginWindow()

    # Dashboard reference saqlanishi kerak.
    windows = {
        "dashboard": None,
    }

    def process_login(
        login: str,
        password: str,
    ):
        user = authenticate_user(
            login,
            password,
        )

        if user is None:
            login_window.error_label.setText(
                "Login yoki parol noto'g'ri."
            )
            return

        login_window.error_label.clear()

        dashboard = DashboardWindow(user)

        windows["dashboard"] = dashboard

        dashboard.show()
        login_window.hide()

    login_window.login_requested.connect(
        process_login
    )

    login_window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
