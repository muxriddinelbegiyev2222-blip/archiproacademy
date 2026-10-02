import sys

from PySide6.QtWidgets import QApplication

from auth.auth_service import authenticate_user, create_user
from courses.course_service import initialize_user_progress
from courses.seed_courses import seed_course_structure
from database.database import initialize_database
from ui.dashboard_window import DashboardWindow
from ui.login_window import LoginWindow


def prepare_application():
    """
    ARCHIPRO UZ ishga tushishidan oldin
    database va o'quv tizimini tayyorlaydi.
    """

    initialize_database()

    seed_course_structure()

    # Development account.
    # Sotuv versiyasida olib tashlanadi.
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

        initialize_user_progress(
            user["id"]
        )

        dashboard = DashboardWindow(
            user
        )

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
