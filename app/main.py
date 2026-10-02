import sys

from PySide6.QtWidgets import QApplication, QMessageBox

from auth.auth_service import authenticate_user, create_user
from database.database import initialize_database
from ui.login_window import LoginWindow


def prepare_application():
    """
    Dastur ishga tushishidan oldin lokal database tayyorlanadi.
    """

    initialize_database()

    # Hozircha dastur ishlab chiqish bosqichida
    # vaqtinchalik test foydalanuvchisi yaratiladi.
    #
    # Agar bazada allaqachon mavjud bo'lsa,
    # create_user False qaytaradi va hech narsa buzilmaydi.

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

    def process_login(login: str, password: str):
        user = authenticate_user(login, password)

        if user is None:
            login_window.error_label.setText(
                "Login yoki parol noto'g'ri."
            )
            return

        login_window.error_label.clear()

        full_name = user.get("full_name") or user.get("username")
        license_type = user.get("license_type", "PRO")

        QMessageBox.information(
            login_window,
            "ARCHIPRO UZ",
            (
                f"Xush kelibsiz, {full_name}!\n\n"
                f"Litsenziya: {license_type}"
            ),
        )

    login_window.login_requested.connect(process_login)

    login_window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
