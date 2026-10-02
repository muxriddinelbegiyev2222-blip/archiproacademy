import sys

from PySide6.QtWidgets import QApplication

from auth.auth_service import (
    authenticate_user,
    create_user,
)

from courses.access_sync import (
    synchronize_user_access,
)

from courses.course_service import (
    initialize_user_progress,
)

from courses.exam_service import (
    initialize_user_levels,
    seed_level_exams,
)

from courses.level00_extra import (
    seed_level00_extra,
)

from courses.level01_content import (
    seed_level01_lessons,
)

from courses.level01_module02 import (
    seed_level01_module02,
)

from courses.level01_module03 import (
    seed_level01_module03,
)

from courses.level01_module04 import (
    seed_level01_module04,
)

from courses.level01_module05 import (
    seed_level01_module05,
)

from courses.level01_module06 import (
    seed_level01_module06,
)

from courses.level02_module01 import (
    seed_level02_module01,
)

from courses.level02_module02 import (
    seed_level02_module02,
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
    # ========================================================
    # DATABASE
    # ========================================================

    initialize_database()

    # ========================================================
    # COURSE STRUCTURE
    # ========================================================

    seed_course_structure()

    # ========================================================
    # LEVEL 0
    # ========================================================

    seed_level00_extra()

    # ========================================================
    # LEVEL 1
    # ========================================================

    seed_level01_lessons()
    seed_level01_module02()
    seed_level01_module03()
    seed_level01_module04()
    seed_level01_module05()
    seed_level01_module06()

    # ========================================================
    # LEVEL 2
    # ========================================================

    seed_level02_module01()
    seed_level02_module02()

    # ========================================================
    # QUIZZES
    # ========================================================

    seed_quizzes()

    # ========================================================
    # FINAL EXAMS
    # ========================================================

    seed_level_exams()

    # ========================================================
    # DEVELOPMENT MASTER ACCOUNT
    #
    # Sotuv versiyasida olib tashlanadi.
    # ========================================================

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

        # 1. Level progress
        initialize_user_levels(
            user["id"]
        )

        # 2. Lesson progress
        initialize_user_progress(
            user["id"]
        )

        # 3. Access synchronization
        synchronize_user_access(
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
