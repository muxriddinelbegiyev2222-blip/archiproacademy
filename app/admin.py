import sys

from PySide6.QtWidgets import (
    QApplication,
    QComboBox,
    QFormLayout,
    QFrame,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from auth.auth_service import create_user
from database.database import initialize_database


class AdminWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle(
            "ARCHIPRO ADMIN"
        )

        self.resize(
            620,
            560,
        )

        self.setMinimumSize(
            560,
            520,
        )

        self.setup_ui()

    def setup_ui(self):
        central = QWidget()

        self.setCentralWidget(
            central
        )

        self.setStyleSheet(
            """
            QMainWindow {
                background-color: #0B1220;
            }

            QWidget {
                color: #F8FAFC;
                font-family: Segoe UI;
            }

            QFrame#card {
                background-color: #111827;
                border: 1px solid #1E293B;
                border-radius: 16px;
            }

            QLabel#title {
                font-size: 28px;
                font-weight: 800;
                color: #FFFFFF;
            }

            QLabel#subtitle {
                font-size: 13px;
                color: #94A3B8;
            }

            QLabel#warning {
                background-color: #291914;
                border: 1px solid #9A3412;
                border-radius: 9px;
                padding: 12px;
                color: #FED7AA;
                font-size: 12px;
            }

            QLineEdit,
            QComboBox {
                background-color: #0F172A;
                border: 1px solid #334155;
                border-radius: 8px;
                padding: 11px;
                color: #FFFFFF;
                font-size: 14px;
            }

            QLineEdit:focus,
            QComboBox:focus {
                border: 1px solid #3B82F6;
            }

            QPushButton#createButton {
                background-color: #2563EB;
                border: none;
                border-radius: 9px;
                padding: 13px 20px;
                color: #FFFFFF;
                font-size: 14px;
                font-weight: 700;
            }

            QPushButton#createButton:hover {
                background-color: #3B82F6;
            }

            QPushButton#clearButton {
                background-color: #1E293B;
                border: 1px solid #334155;
                border-radius: 9px;
                padding: 13px 20px;
                color: #FFFFFF;
                font-size: 14px;
                font-weight: 600;
            }

            QPushButton#clearButton:hover {
                background-color: #334155;
            }
            """
        )

        root = QVBoxLayout(
            central
        )

        root.setContentsMargins(
            34,
            30,
            34,
            30,
        )

        root.setSpacing(
            18
        )

        title = QLabel(
            "ARCHIPRO ADMIN"
        )

        title.setObjectName(
            "title"
        )

        subtitle = QLabel(
            "ARCHIPRO UZ foydalanuvchilarini yaratish vositasi"
        )

        subtitle.setObjectName(
            "subtitle"
        )

        root.addWidget(
            title
        )

        root.addWidget(
            subtitle
        )

        warning = QLabel(
            "DIQQAT: Bu dastur faqat ARCHIPRO UZ egasi yoki "
            "vakolatli administrator uchun. "
            "Mijozlarga ARCHIPRO ADMIN.exe berilmaydi."
        )

        warning.setObjectName(
            "warning"
        )

        warning.setWordWrap(
            True
        )

        root.addWidget(
            warning
        )

        card = QFrame()

        card.setObjectName(
            "card"
        )

        card_layout = QVBoxLayout(
            card
        )

        card_layout.setContentsMargins(
            24,
            24,
            24,
            24,
        )

        card_layout.setSpacing(
            18
        )

        form = QFormLayout()

        form.setSpacing(
            14
        )

        self.full_name_input = (
            QLineEdit()
        )

        self.full_name_input.setPlaceholderText(
            "Masalan: Ali Valiyev"
        )

        self.username_input = (
            QLineEdit()
        )

        self.username_input.setPlaceholderText(
            "Masalan: ali2026"
        )

        self.password_input = (
            QLineEdit()
        )

        self.password_input.setEchoMode(
            QLineEdit.EchoMode.Password
        )

        self.password_input.setPlaceholderText(
            "Kamida 8 belgili parol"
        )

        self.password_confirm_input = (
            QLineEdit()
        )

        self.password_confirm_input.setEchoMode(
            QLineEdit.EchoMode.Password
        )

        self.password_confirm_input.setPlaceholderText(
            "Parolni qayta kiriting"
        )

        self.license_combo = (
            QComboBox()
        )

        self.license_combo.addItem(
            "PRO"
        )

        self.license_combo.addItem(
            "MASTER"
        )

        form.addRow(
            "F.I.Sh.:",
            self.full_name_input,
        )

        form.addRow(
            "Login:",
            self.username_input,
        )

        form.addRow(
            "Parol:",
            self.password_input,
        )

        form.addRow(
            "Parolni tasdiqlash:",
            self.password_confirm_input,
        )

        form.addRow(
            "Litsenziya:",
            self.license_combo,
        )

        card_layout.addLayout(
            form
        )

        buttons = QHBoxLayout()

        clear_button = QPushButton(
            "TOZALASH"
        )

        clear_button.setObjectName(
            "clearButton"
        )

        clear_button.clicked.connect(
            self.clear_form
        )

        create_button = QPushButton(
            "FOYDALANUVCHI YARATISH"
        )

        create_button.setObjectName(
            "createButton"
        )

        create_button.clicked.connect(
            self.create_new_user
        )

        buttons.addWidget(
            clear_button
        )

        buttons.addStretch()

        buttons.addWidget(
            create_button
        )

        card_layout.addLayout(
            buttons
        )

        root.addWidget(
            card
        )

        root.addStretch()

    def clear_form(self):
        self.full_name_input.clear()

        self.username_input.clear()

        self.password_input.clear()

        self.password_confirm_input.clear()

        self.license_combo.setCurrentText(
            "PRO"
        )

        self.username_input.setFocus()

    def create_new_user(self):
        full_name = (
            self.full_name_input
            .text()
            .strip()
        )

        username = (
            self.username_input
            .text()
            .strip()
        )

        password = (
            self.password_input
            .text()
        )

        password_confirm = (
            self.password_confirm_input
            .text()
        )

        license_type = (
            self.license_combo
            .currentText()
            .strip()
        )

        if not full_name:
            QMessageBox.warning(
                self,
                "Ma'lumot yetishmayapti",
                "F.I.Sh. kiriting.",
            )
            return

        if not username:
            QMessageBox.warning(
                self,
                "Ma'lumot yetishmayapti",
                "Login kiriting.",
            )
            return

        if len(username) < 3:
            QMessageBox.warning(
                self,
                "Login",
                "Login kamida 3 ta belgidan iborat bo'lsin.",
            )
            return

        if len(password) < 8:
            QMessageBox.warning(
                self,
                "Parol",
                "Parol kamida 8 ta belgidan iborat bo'lsin.",
            )
            return

        if password != password_confirm:
            QMessageBox.warning(
                self,
                "Parol",
                "Kiritilgan parollar bir xil emas.",
            )
            return

        try:
            result = create_user(
                username=username,
                password=password,
                full_name=full_name,
                license_type=license_type,
            )

        except Exception as exc:
            QMessageBox.critical(
                self,
                "Xato",
                (
                    "Foydalanuvchi yaratilmadi.\n\n"
                    f"{exc}"
                ),
            )
            return

        if result:
            QMessageBox.information(
                self,
                "Tayyor",
                (
                    "Foydalanuvchi muvaffaqiyatli yaratildi.\n\n"
                    f"Login: {username}\n"
                    f"Litsenziya: {license_type}"
                ),
            )

            self.clear_form()

        else:
            QMessageBox.warning(
                self,
                "Yaratilmadi",
                (
                    "Foydalanuvchi yaratilmadi.\n\n"
                    "Bu login avval yaratilgan bo'lishi mumkin."
                ),
            )


def main():
    initialize_database()

    app = QApplication(
        sys.argv
    )

    app.setApplicationName(
        "ARCHIPRO ADMIN"
    )

    app.setOrganizationName(
        "ARCHIPRO UZ"
    )

    window = AdminWindow()

    window.show()

    sys.exit(
        app.exec()
    )


if __name__ == "__main__":
    main()
