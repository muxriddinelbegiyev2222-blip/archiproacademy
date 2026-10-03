import sys

from PySide6.QtWidgets import QApplication

from auth.auth_service import authenticate_user, create_user

from courses.access_sync import synchronize_user_access
from courses.course_service import initialize_user_progress
from courses.exam_service import initialize_user_levels, seed_level_exams
from courses.quiz_service import seed_quizzes
from courses.seed_courses import seed_course_structure

from database.database import initialize_database

from ui.dashboard_window import DashboardWindow
from ui.login_window import LoginWindow


from courses.level00_extra import seed_level00_extra

from courses.level01_content import seed_level01_lessons
from courses.level01_module02 import seed_level01_module02
from courses.level01_module03 import seed_level01_module03
from courses.level01_module04 import seed_level01_module04
from courses.level01_module05 import seed_level01_module05
from courses.level01_module06 import seed_level01_module06

from courses.level02_module01 import seed_level02_module01
from courses.level02_module02 import seed_level02_module02
from courses.level02_module03 import seed_level02_module03
from courses.level02_module04 import seed_level02_module04
from courses.level02_module05 import seed_level02_module05
from courses.level02_module06 import seed_level02_module06
from courses.level02_module07 import seed_level02_module07
from courses.level02_module08 import seed_level02_module08
from courses.level02_module09 import seed_level02_module09
from courses.level02_module10 import seed_level02_module10
from courses.level02_exam import seed_level02_exam

from courses.level03_module01 import seed_level03_module01
from courses.level03_module02 import seed_level03_module02
from courses.level03_module03 import seed_level03_module03
from courses.level03_module04 import seed_level03_module04
from courses.level03_module05 import seed_level03_module05
from courses.level03_module06 import seed_level03_module06
from courses.level03_module07 import seed_level03_module07
from courses.level03_module08 import seed_level03_module08
from courses.level03_exam import seed_level03_exam

from courses.level04_module01 import seed_level04_module01
from courses.level04_module02 import seed_level04_module02
from courses.level04_module03 import seed_level04_module03
from courses.level04_module04 import seed_level04_module04
from courses.level04_module05 import seed_level04_module05
from courses.level04_module06 import seed_level04_module06
from courses.level04_module07 import seed_level04_module07
from courses.level04_module08 import seed_level04_module08
from courses.level04_exam import seed_level04_exam

from courses.level05_module01 import seed_level05_module01
from courses.level05_module02 import seed_level05_module02
from courses.level05_module03 import seed_level05_module03
from courses.level05_module04 import seed_level05_module04
from courses.level05_module05 import seed_level05_module05
from courses.level05_module06 import seed_level05_module06
from courses.level05_module07 import seed_level05_module07
from courses.level05_module08 import seed_level05_module08
from courses.level05_module09 import seed_level05_module09
from courses.level05_module10 import seed_level05_module10
from courses.level05_exam import seed_level05_exam

from courses.level06_module01 import seed_level06_module01
from courses.level06_module02 import seed_level06_module02
from courses.level06_module03 import seed_level06_module03
from courses.level06_module04 import seed_level06_module04
from courses.level06_module05 import seed_level06_module05
from courses.level06_module06 import seed_level06_module06
from courses.level06_module07 import seed_level06_module07
from courses.level06_module08 import seed_level06_module08
from courses.level06_module09 import seed_level06_module09
from courses.level06_module10 import seed_level06_module10
from courses.level06_exam import seed_level06_exam

from courses.level07_module01 import seed_level07_module01
from courses.level07_module02 import seed_level07_module02
from courses.level07_module03 import seed_level07_module03
from courses.level07_module04 import seed_level07_module04
from courses.level07_module05 import seed_level07_module05
from courses.level07_module06 import seed_level07_module06
from courses.level07_module07 import seed_level07_module07
from courses.level07_module08 import seed_level07_module08
from courses.level07_module09 import seed_level07_module09
from courses.level07_exam import seed_level07_exam

from courses.level08_module01 import seed_level08_module01
from courses.level08_module02 import seed_level08_module02
from courses.level08_module03 import seed_level08_module03
from courses.level08_module04 import seed_level08_module04
from courses.level08_module05 import seed_level08_module05
from courses.level08_module06 import seed_level08_module06
from courses.level08_module07 import seed_level08_module07
from courses.level08_module08 import seed_level08_module08
from courses.level08_module09 import seed_level08_module09
from courses.level08_exam import seed_level08_exam

from courses.level09_module01 import seed_level09_module01
from courses.level09_module02 import seed_level09_module02
from courses.level09_module03 import seed_level09_module03
from courses.level09_module04 import seed_level09_module04
from courses.level09_module05 import seed_level09_module05
from courses.level09_module06 import seed_level09_module06
from courses.level09_module07 import seed_level09_module07
from courses.level09_module08 import seed_level09_module08
from courses.level09_exam import seed_level09_exam

from courses.level10_module01 import seed_level10_module01
from courses.level10_module02 import seed_level10_module02
from courses.level10_module03 import seed_level10_module03
from courses.level10_module04 import seed_level10_module04
from courses.level10_module05 import seed_level10_module05
from courses.level10_module06 import seed_level10_module06
from courses.level10_module07 import seed_level10_module07
from courses.level10_module08 import seed_level10_module08
from courses.level10_module09 import seed_level10_module09
from courses.level10_module10 import seed_level10_module10
from courses.level10_module11 import seed_level10_module11
from courses.level10_exam import seed_level10_exam

from courses.level11_module01 import seed_level11_module01
from courses.level11_module02 import seed_level11_module02
from courses.level11_module03 import seed_level11_module03
from courses.level11_module04 import seed_level11_module04
from courses.level11_module05 import seed_level11_module05
from courses.level11_module06 import seed_level11_module06
from courses.level11_module07 import seed_level11_module07
from courses.level11_module08 import seed_level11_module08
from courses.level11_module09 import seed_level11_module09
from courses.level11_exam import seed_level11_exam

from courses.level12_module01 import seed_level12_module01
from courses.level12_module02 import seed_level12_module02
from courses.level12_module03 import seed_level12_module03
from courses.level12_module04 import seed_level12_module04
from courses.level12_module05 import seed_level12_module05
from courses.level12_module06 import seed_level12_module06
from courses.level12_module07 import seed_level12_module07
from courses.level12_module08 import seed_level12_module08
from courses.level12_module09 import seed_level12_module09
from courses.level12_module10 import seed_level12_module10
from courses.level12_exam import seed_level12_exam


MODULE_SEEDERS = (
    seed_level00_extra,

    seed_level01_lessons,
    seed_level01_module02,
    seed_level01_module03,
    seed_level01_module04,
    seed_level01_module05,
    seed_level01_module06,

    seed_level02_module01,
    seed_level02_module02,
    seed_level02_module03,
    seed_level02_module04,
    seed_level02_module05,
    seed_level02_module06,
    seed_level02_module07,
    seed_level02_module08,
    seed_level02_module09,
    seed_level02_module10,

    seed_level03_module01,
    seed_level03_module02,
    seed_level03_module03,
    seed_level03_module04,
    seed_level03_module05,
    seed_level03_module06,
    seed_level03_module07,
    seed_level03_module08,

    seed_level04_module01,
    seed_level04_module02,
    seed_level04_module03,
    seed_level04_module04,
    seed_level04_module05,
    seed_level04_module06,
    seed_level04_module07,
    seed_level04_module08,

    seed_level05_module01,
    seed_level05_module02,
    seed_level05_module03,
    seed_level05_module04,
    seed_level05_module05,
    seed_level05_module06,
    seed_level05_module07,
    seed_level05_module08,
    seed_level05_module09,
    seed_level05_module10,

    seed_level06_module01,
    seed_level06_module02,
    seed_level06_module03,
    seed_level06_module04,
    seed_level06_module05,
    seed_level06_module06,
    seed_level06_module07,
    seed_level06_module08,
    seed_level06_module09,
    seed_level06_module10,

    seed_level07_module01,
    seed_level07_module02,
    seed_level07_module03,
    seed_level07_module04,
    seed_level07_module05,
    seed_level07_module06,
    seed_level07_module07,
    seed_level07_module08,
    seed_level07_module09,

    seed_level08_module01,
    seed_level08_module02,
    seed_level08_module03,
    seed_level08_module04,
    seed_level08_module05,
    seed_level08_module06,
    seed_level08_module07,
    seed_level08_module08,
    seed_level08_module09,

    seed_level09_module01,
    seed_level09_module02,
    seed_level09_module03,
    seed_level09_module04,
    seed_level09_module05,
    seed_level09_module06,
    seed_level09_module07,
    seed_level09_module08,

    seed_level10_module01,
    seed_level10_module02,
    seed_level10_module03,
    seed_level10_module04,
    seed_level10_module05,
    seed_level10_module06,
    seed_level10_module07,
    seed_level10_module08,
    seed_level10_module09,
    seed_level10_module10,
    seed_level10_module11,

    seed_level11_module01,
    seed_level11_module02,
    seed_level11_module03,
    seed_level11_module04,
    seed_level11_module05,
    seed_level11_module06,
    seed_level11_module07,
    seed_level11_module08,
    seed_level11_module09,

    seed_level12_module01,
    seed_level12_module02,
    seed_level12_module03,
    seed_level12_module04,
    seed_level12_module05,
    seed_level12_module06,
    seed_level12_module07,
    seed_level12_module08,
    seed_level12_module09,
    seed_level12_module10,
)


CUSTOM_EXAM_SEEDERS = (
    seed_level02_exam,
    seed_level03_exam,
    seed_level04_exam,
    seed_level05_exam,
    seed_level06_exam,
    seed_level07_exam,
    seed_level08_exam,
    seed_level09_exam,
    seed_level10_exam,
    seed_level11_exam,
    seed_level12_exam,
)


def prepare_application():
    initialize_database()
    seed_course_structure()

    for seeder in MODULE_SEEDERS:
        seeder()

    seed_quizzes()

    seed_level_exams()

    for seeder in CUSTOM_EXAM_SEEDERS:
        seeder()

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

    def process_login(login: str, password: str):
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

        initialize_user_levels(user["id"])
        initialize_user_progress(user["id"])
        synchronize_user_access(user["id"])

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
