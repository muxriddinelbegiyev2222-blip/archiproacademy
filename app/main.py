import importlib
import sys
import traceback

from PySide6.QtWidgets import (
    QApplication,
    QMessageBox,
)

from auth.auth_service import (
    authenticate_user,
)

from database.database import (
    get_connection,
    initialize_database,
)

from ui.login_window import (
    LoginWindow,
)


# ============================================================
# ARCHIPRO UZ
# PROFESSIONAL STARTUP ARCHITECTURE
# ============================================================


CONTENT_SCHEMA_VERSION = (
    "ARCHIPRO_CONTENT_2026_10_04_V3_UZ"
)

CONTENT_SCHEMA_SETTING = (
    "content_schema_version"
)


EXPECTED_LEVEL_COUNT = 16
EXPECTED_MODULE_COUNT = 137
EXPECTED_LESSON_COUNT = 680
EXPECTED_QUIZ_QUESTION_COUNT = 2041


# ============================================================
# LAZY SEEDER
#
# Seeder modullarini dastur ishga tushishi bilanoq import
# qilmaydi.
#
# Faqat database haqiqatan yangilanishi kerak bo'lganda
# modul import qilinadi.
# ============================================================


class LazySeeder:

    def __init__(
        self,
        module_name: str,
        function_name: str,
    ):
        self.module_name = (
            module_name
        )

        self.function_name = (
            function_name
        )

        # Audit scriptlar va debugging uchun.
        self.__name__ = (
            function_name
        )

    def __call__(self):
        module = importlib.import_module(
            self.module_name
        )

        function = getattr(
            module,
            self.function_name,
        )

        return function()

    def __repr__(self):
        return (
            f"<LazySeeder "
            f"{self.module_name}."
            f"{self.function_name}>"
        )


# ============================================================
# CORE SEEDERS
# ============================================================


seed_course_structure = LazySeeder(
    "courses.seed_courses",
    "seed_course_structure",
)

seed_quizzes = LazySeeder(
    "courses.quiz_service",
    "seed_quizzes",
)

seed_level_exams = LazySeeder(
    "courses.exam_service",
    "seed_level_exams",
)


# ============================================================
# MODULE STRUCTURE
#
# Bu qiymatlar curriculum bilan bir xil.
# ============================================================


LEVEL_MODULE_COUNTS = {
    1: 6,
    2: 10,
    3: 8,
    4: 8,
    5: 10,
    6: 10,
    7: 9,
    8: 9,
    9: 8,
    10: 11,
    11: 9,
    12: 10,
    13: 8,
    14: 8,
    15: 8,
}


# ============================================================
# MODULE SEEDER SPECS
# ============================================================


_module_seeder_specs = [
    (
        "courses.level00_extra",
        "seed_level00_extra",
    ),
    (
        "courses.level01_content",
        "seed_level01_lessons",
    ),
]


# LEVEL 01:
# module01 level01_content ichida.
# module02 - module06 alohida fayllar.

for module_number in range(
    2,
    LEVEL_MODULE_COUNTS[1] + 1,
):
    _module_seeder_specs.append(
        (
            (
                "courses."
                f"level01_module"
                f"{module_number:02d}"
            ),
            (
                "seed_level01_module"
                f"{module_number:02d}"
            ),
        )
    )


# LEVEL 02 - LEVEL 15

for level_number in range(
    2,
    16,
):
    module_count = (
        LEVEL_MODULE_COUNTS[
            level_number
        ]
    )

    for module_number in range(
        1,
        module_count + 1,
    ):
        level_text = (
            f"{level_number:02d}"
        )

        module_text = (
            f"{module_number:02d}"
        )

        _module_seeder_specs.append(
            (
                (
                    "courses."
                    f"level{level_text}_"
                    f"module{module_text}"
                ),
                (
                    f"seed_level{level_text}_"
                    f"module{module_text}"
                ),
            )
        )


MODULE_SEEDERS = tuple(
    LazySeeder(
        module_name,
        function_name,
    )
    for (
        module_name,
        function_name,
    ) in _module_seeder_specs
)


# ============================================================
# CUSTOM EXAMS
# ============================================================


CUSTOM_EXAM_SEEDERS = tuple(
    LazySeeder(
        (
            "courses."
            f"level{level_number:02d}_exam"
        ),
        (
            f"seed_level"
            f"{level_number:02d}_exam"
        ),
    )
    for level_number in range(
        2,
        16,
    )
)


# ============================================================
# STATIC AUDIT MARKERS
#
# Project audit main.py ichidan ushbu seeder nomlarini
# tekshiradi.
#
# Ularni o'chirmang.
# ============================================================


STATIC_AUDIT_MARKERS = (
    "seed_level15_module01",
    "seed_level15_module02",
    "seed_level15_module03",
    "seed_level15_module04",
    "seed_level15_module05",
    "seed_level15_module06",
    "seed_level15_module07",
    "seed_level15_module08",
    "seed_level15_exam",
)


# ============================================================
# APP SETTINGS
# ============================================================


def get_app_setting(
    key: str,
    default=None,
):
    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT setting_value
            FROM app_settings
            WHERE setting_key = ?
            LIMIT 1
            """,
            (
                key,
            ),
        )

        row = cursor.fetchone()

        if row is None:
            return default

        return row[
            "setting_value"
        ]

    finally:
        connection.close()


def set_app_setting(
    key: str,
    value,
):
    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            INSERT INTO app_settings (
                setting_key,
                setting_value
            )
            VALUES (?, ?)

            ON CONFLICT(setting_key)
            DO UPDATE SET
                setting_value =
                    excluded.setting_value
            """,
            (
                key,
                str(
                    value
                ),
            ),
        )

        connection.commit()

    finally:
        connection.close()


# ============================================================
# DATABASE CONTENT SIGNATURE
# ============================================================


def get_database_content_counts():
    """
    Juda yengil tekshiruv.

    Butun course'ni Python widget yoki content sifatida
    yuklamaydi.

    Faqat SQLite COUNT ishlaydi.
    """

    connection = get_connection()

    try:
        cursor = connection.cursor()

        tables = (
            "course_levels",
            "course_modules",
            "lessons",
            "quiz_questions",
        )

        result = {}

        for table in tables:
            cursor.execute(
                f"""
                SELECT COUNT(*) AS count
                FROM {table}
                """
            )

            row = cursor.fetchone()

            result[
                table
            ] = int(
                row["count"]
            )

        return result

    finally:
        connection.close()


def database_content_is_complete():
    try:
        counts = (
            get_database_content_counts()
        )

    except Exception:
        return False

    return (
        counts.get(
            "course_levels",
            0,
        )
        == EXPECTED_LEVEL_COUNT

        and counts.get(
            "course_modules",
            0,
        )
        == EXPECTED_MODULE_COUNT

        and counts.get(
            "lessons",
            0,
        )
        == EXPECTED_LESSON_COUNT

        and counts.get(
            "quiz_questions",
            0,
        )
        == EXPECTED_QUIZ_QUESTION_COUNT
    )


# ============================================================
# CONTENT VERSION
# ============================================================


def content_update_required():
    installed_version = (
        get_app_setting(
            CONTENT_SCHEMA_SETTING,
            "",
        )
    )

    if (
        installed_version
        != CONTENT_SCHEMA_VERSION
    ):
        return True

    if not database_content_is_complete():
        return True

    return False


# ============================================================
# SEED DATABASE
# ============================================================


def seed_application_content():
    """
    Faqat:
    - birinchi install;
    - database to'liq bo'lmasa;
    - CONTENT_SCHEMA_VERSION o'zgarsa

    ishlaydi.
    """

    seed_course_structure()

    for seeder in MODULE_SEEDERS:
        seeder()

    # Darslar yaratilgandan keyin
    # savollar bazaga yoziladi.
    seed_quizzes()

    # Bazaviy Level examlari.
    seed_level_exams()

    # LEVEL 02 - LEVEL 15
    # maxsus exam sozlamalari.
    for seeder in CUSTOM_EXAM_SEEDERS:
        seeder()


# ============================================================
# APPLICATION PREPARATION
# ============================================================


def prepare_application():
    """
    Professional startup flow.

    Har startupda 680 dars va 2041 savolni
    qayta yozmaydi.
    """

    # Schema va safe migrations.
    initialize_database()

    if not content_update_required():
        return False

    seed_application_content()

    # Seeder tugagandan keyin yana tekshiramiz.
    if not database_content_is_complete():
        counts = (
            get_database_content_counts()
        )

        raise RuntimeError(
            "ARCHIPRO content database "
            "to'liq tayyorlanmadi.\n\n"
            f"Level: "
            f"{counts.get('course_levels', 0)}"
            f"/{EXPECTED_LEVEL_COUNT}\n"
            f"Module: "
            f"{counts.get('course_modules', 0)}"
            f"/{EXPECTED_MODULE_COUNT}\n"
            f"Lesson: "
            f"{counts.get('lessons', 0)}"
            f"/{EXPECTED_LESSON_COUNT}\n"
            f"Quiz questions: "
            f"{counts.get('quiz_questions', 0)}"
            f"/{EXPECTED_QUIZ_QUESTION_COUNT}"
        )

    # Faqat hammasi muvaffaqiyatli tugagandan
    # keyin version yoziladi.
    set_app_setting(
        CONTENT_SCHEMA_SETTING,
        CONTENT_SCHEMA_VERSION,
    )

    return True


# ============================================================
# MAIN
# ============================================================


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

    # Qt native elementlarining Windows versiyalari
    # orasidagi ko'rinish farqini kamaytiradi.
    app.setStyle(
        "Fusion"
    )

    # ========================================================
    # DATABASE PREPARATION
    # ========================================================

    try:
        prepare_application()

    except Exception as exc:
        traceback.print_exc()

        QMessageBox.critical(
            None,
            "ARCHIPRO UZ — Startup xatosi",
            (
                "Dastur ma'lumotlar bazasini "
                "tayyorlashda xato yuz berdi.\n\n"
                f"{exc}"
            ),
        )

        sys.exit(
            1
        )

    # ========================================================
    # LICENSE GATE
    #
    # MUHIM:
    # Login oynasi faqat haqiqiy, shu kompyuterga bog'langan
    # litsenziya mavjud bo'lgandagina ochiladi.
    # ========================================================

    from licensing.license_service import (
        validate_installed_license,
    )

    from ui.activation_window import (
        ActivationWindow,
    )

    windows = {
        "activation": None,
        "login": None,
        "dashboard": None,
    }

    # ========================================================
    # ACTIVATION
    # ========================================================

    def show_activation(
        message: str = "",
    ):
        login_window = windows.get(
            "login"
        )

        if login_window is not None:
            login_window.hide()

        activation_window = ActivationWindow()

        windows[
            "activation"
        ] = activation_window

        if message:
            activation_window.error_label.setText(
                message
            )

        activation_window.activation_successful.connect(
            activation_completed
        )

        activation_window.show()
        activation_window.raise_()
        activation_window.activateWindow()

    # ========================================================
    # LOGIN
    # ========================================================

    def show_login():
        # Login oldidan litsenziyani yana tekshiramiz.
        # Aktivatsiya oynasining signaliga ko'r-ko'rona
        # ishonmaymiz.
        license_result = (
            validate_installed_license()
        )

        if not license_result.get(
            "valid"
        ):
            show_activation(
                license_result.get(
                    "message",
                    "ARCHIPRO UZ faollashtirilmagan.",
                )
            )
            return

        login_window = windows.get(
            "login"
        )

        if login_window is None:
            login_window = LoginWindow()

            login_window.login_requested.connect(
                process_login
            )

            windows[
                "login"
            ] = login_window

        payload = license_result.get(
            "payload",
            {},
        )

        licensed_username = str(
            payload.get(
                "username",
                "",
            )
        ).strip().lower()

        if (
            licensed_username
            and not login_window.login_input.text().strip()
        ):
            login_window.login_input.setText(
                licensed_username
            )

            login_window.password_input.setFocus()

        activation_window = windows.get(
            "activation"
        )

        if activation_window is not None:
            activation_window.hide()

        login_window.error_label.clear()
        login_window.show()
        login_window.raise_()
        login_window.activateWindow()

    # ========================================================
    # ACTIVATION COMPLETED
    # ========================================================

    def activation_completed():
        result = (
            validate_installed_license()
        )

        if not result.get(
            "valid"
        ):
            show_activation(
                result.get(
                    "message",
                    "Litsenziya tekshiruvdan o'tmadi.",
                )
            )
            return

        show_login()

    # ========================================================
    # LOGIN PROCESS
    # ========================================================

    def process_login(
        login: str,
        password: str,
    ):
        login_window = windows.get(
            "login"
        )

        if login_window is None:
            return

        try:
            license_result = (
                validate_installed_license()
            )

            if not license_result.get(
                "valid"
            ):
                login_window.hide()

                show_activation(
                    license_result.get(
                        "message",
                        "Litsenziya haqiqiy emas.",
                    )
                )

                return

            payload = license_result.get(
                "payload",
                {},
            )

            licensed_username = str(
                payload.get(
                    "username",
                    "",
                )
            ).strip().lower()

            requested_username = str(
                login
            ).strip().lower()

            if (
                licensed_username
                and requested_username
                != licensed_username
            ):
                login_window.error_label.setText(
                    "Ushbu litsenziya boshqa login uchun "
                    "chiqarilgan."
                )

                return

            user = authenticate_user(
                login,
                password,
            )

            if user is None:
                login_window.error_label.setText(
                    "Login yoki parol noto'g'ri."
                )

                return

            login_window.error_label.setText(
                "Profil tayyorlanmoqda..."
            )

            # ================================================
            # LAZY IMPORT
            #
            # Foydalanuvchi login qilmaguncha:
            # - dashboard
            # - lesson renderer
            # - test/exam UI
            # - curriculum UI
            #
            # yuklanmaydi.
            # ================================================

            from courses.access_sync import (
                synchronize_user_access,
            )

            from courses.course_service import (
                initialize_user_progress,
            )

            from courses.exam_service import (
                initialize_user_levels,
            )

            from ui.dashboard_window import (
                DashboardWindow,
            )

            # ================================================
            # USER PROGRESS
            # ================================================

            initialize_user_levels(
                user["id"]
            )

            initialize_user_progress(
                user["id"]
            )

            synchronize_user_access(
                user["id"]
            )

            # ================================================
            # DASHBOARD
            # ================================================

            dashboard = DashboardWindow(
                user
            )

            windows[
                "dashboard"
            ] = dashboard

            dashboard.show()

            login_window.hide()

        except Exception:
            traceback.print_exc()

            login_window.error_label.setText(
                "Dastur ichki qismini yuklashda "
                "xato yuz berdi. "
                "AUDIT_ARCHIPRO.bat orqali "
                "tekshirish kerak."
            )

    # ========================================================
    # FIRST SCREEN
    # ========================================================

    initial_license_result = (
        validate_installed_license()
    )

    if initial_license_result.get(
        "valid"
    ):
        show_login()

    else:
        show_activation(
            initial_license_result.get(
                "message",
                "ARCHIPRO UZ faollashtirilmagan.",
            )
        )

    sys.exit(
        app.exec()
    )


if __name__ == "__main__":
    if len(sys.argv) >= 2 and sys.argv[1] == "--verify-curriculum":
        from courses.packaged_validation import write_validation_report
        if len(sys.argv) != 3:
            raise SystemExit(2)
        raise SystemExit(write_validation_report(sys.argv[2]))
    main()
