import sys

from PySide6.QtWidgets import QApplication, QMessageBox

from ui.login_window import LoginWindow


def main():
    app = QApplication(sys.argv)

    app.setApplicationName("ARCHIPRO UZ")
    app.setOrganizationName("ARCHIPRO UZ")

    login_window = LoginWindow()

    def process_login(login: str, password: str):
        # Hozircha vaqtinchalik test login.
        # Keyingi bosqichda bu joy database va license tizimiga ulanadi.

        if login == "admin" and password == "12345":
            QMessageBox.information(
                login_window,
                "ARCHIPRO UZ",
                "Kirish muvaffaqiyatli.",
            )
        else:
            login_window.error_label.setText(
                "Login yoki parol noto'g'ri."
            )

    login_window.login_requested.connect(process_login)

    login_window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
