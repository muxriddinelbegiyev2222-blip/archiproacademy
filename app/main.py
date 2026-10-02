import sys

from PySide6.QtWidgets import (
    QApplication,
)

from auth.auth_service import (
    authenticate_user,
    create_user,
)

from courses.course_service import (
    initialize_user_progress,
)

from courses.level00_extra import (
    seed_level00_extra,
)

from courses.quiz_service import (
    seed_quizzes,
)

from courses.seed_courses import (
    seed_course_structure,
)

from database.database import (
    initialize_database,
)

from ui.dashboard_window import (
    DashboardWindow,
)

from ui.login_window import (
    LoginWindow,
)


def prepare_application():
    """
    ARCHIPRO UZ ishga tushishidan oldin
    barcha lokal ma'lumotlar tayyorlanadi.
    """

    # 1. Database jadvallari
    initialize_database()

    # 2. Level va modullar
    seed_course_structure()

    # 3. Level 0 qo'shimcha darslari
    seed_level00_extra()

    # 4. Barcha testlar
    seed_quizzes()

    # 5. Development foydalanuvchi
    # Sotuv versiyasida bu olib tashlanadi.
    create_user(
        username="admin",
        password="12345",
        full_name="Administrator",
        license_type="MASTER",
    )


def main():
    app = QApplication(
        sys.argv
    )

    app.setApplicationName(
        "ARCHIPRO UZ"
    )

    app.setOrganizationName(
        "ARCHIPRO UZ"
    )

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

        # Yangi darslar paydo bo'lsa,
        # foydalanuvchi progressiga ham qo'shiladi.
        initialize_user_progress(
            user["id"]
        )

        dashboard = DashboardWindow(
            user
        )

        windows[
            "dashboard"
        ] = dashboard

        dashboard.show()

        login_window.hide()

    login_window.login_requested.connect(
        process_login
    )

    login_window.show()

    sys.exit(
        app.exec()
    )


if __name__ == "__main__":
    main()
