import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QFileDialog,
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

from licensing.device_id import get_device_id

from licensing.license_generator import (
    generate_license,
    get_private_key_path,
    private_key_exists,
    save_license,
)


class OwnerWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle(
            "ARCHIPRO OWNER"
        )

        self.resize(
            720,
            700,
        )

        self.setMinimumSize(
            650,
            620,
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
                background-color: #080D18;
            }

            QWidget {
                color: #F8FAFC;
                font-family: Segoe UI;
            }

            QFrame#card {
                background-color: #111827;
                border: 1px solid #293548;
                border-radius: 16px;
            }

            QLabel#title {
                font-size: 30px;
                font-weight: 800;
                color: #FFFFFF;
            }

            QLabel#subtitle {
                font-size: 13px;
                color: #94A3B8;
            }

            QLabel#warning {
                background-color: #251D06;
                border: 1px solid #A16207;
                border-radius: 10px;
                padding: 13px;
                color: #FDE68A;
                font-size: 12px;
            }

            QLabel#masterInfo {
                background-color: #172554;
                border: 1px solid #2563EB;
                border-radius: 9px;
                padding: 12px;
                color: #BFDBFE;
                font-size: 13px;
                font-weight: 700;
            }

            QLabel#keyOk {
                background-color: #10251C;
                border: 1px solid #15803D;
                border-radius: 9px;
                padding: 11px;
                color: #BBF7D0;
                font-size: 12px;
            }

            QLabel#keyError {
                background-color: #291914;
                border: 1px solid #C2410C;
                border-radius: 9px;
                padding: 11px;
                color: #FED7AA;
                font-size: 12px;
            }

            QLineEdit {
                background-color: #0F172A;
                border: 1px solid #334155;
                border-radius: 8px;
                padding: 11px;
                color: #FFFFFF;
                font-size: 14px;
            }

            QLineEdit:focus {
                border: 1px solid #3B82F6;
            }

            QLineEdit:read-only {
                color: #93C5FD;
                background-color: #111827;
            }

            QPushButton#createButton {
                background-color: #A16207;
                border: none;
                border-radius: 9px;
                padding: 14px 20px;
                color: #FFFFFF;
                font-size: 14px;
                font-weight: 800;
            }

            QPushButton#createButton:hover {
                background-color: #CA8A04;
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
            16
        )

        title = QLabel(
            "ARCHIPRO OWNER"
        )

        title.setObjectName(
            "title"
        )

        subtitle = QLabel(
            "Faqat dastur egasi uchun MASTER litsenziya markazi"
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
            "DIQQAT: ARCHIPRO OWNER.exe va private key "
            "hech qachon mijozga berilmaydi. "
            "Bu dastur faqat dastur egasining shaxsiy "
            "MASTER litsenziyasini yaratish uchun."
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

        if private_key_exists():

            self.key_status = QLabel(
                "✓ PRIVATE KEY TOPILDI\n"
                + str(
                    get_private_key_path()
                )
            )

            self.key_status.setObjectName(
                "keyOk"
            )

        else:

            self.key_status = QLabel(
                "PRIVATE KEY TOPILMADI.\n"
                "MASTER litsenziya yaratib bo'lmaydi."
            )

            self.key_status.setObjectName(
                "keyError"
            )

        self.key_status.setWordWrap(
            True
        )

        root.addWidget(
            self.key_status
        )

        master_info = QLabel(
            "★ MASTER — barcha Level va darslarni "
            "blokirovkasiz tekshirish rejimi"
        )

        master_info.setObjectName(
            "masterInfo"
        )

        master_info.setWordWrap(
            True
        )

        root.addWidget(
            master_info
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

        self.device_input = QLineEdit()

        self.device_input.setText(
            get_device_id()
        )

        self.device_input.setReadOnly(
            True
        )

        self.full_name_input = QLineEdit()

        self.full_name_input.setPlaceholderText(
            "Masalan: Muxriddin Elbegiyev"
        )

        self.username_input = QLineEdit()

        self.username_input.setPlaceholderText(
            "Masalan: owner"
        )

        self.password_input = QLineEdit()

        self.password_input.setEchoMode(
            QLineEdit.EchoMode.Password
        )

        self.password_input.setPlaceholderText(
            "Kamida 8 belgili parol"
        )

        self.password_confirm_input = QLineEdit()

        self.password_confirm_input.setEchoMode(
            QLineEdit.EchoMode.Password
        )

        self.password_confirm_input.setPlaceholderText(
            "Parolni qayta kiriting"
        )

        license_info = QLabel(
            "MASTER / MUDDATSIZ"
        )

        license_info.setStyleSheet(
            """
            QLabel {
                color: #FACC15;
                font-weight: 800;
                padding: 8px;
            }
            """
        )

        form.addRow(
            "Device ID:",
            self.device_input,
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
            license_info,
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
            "MASTER LICENSE YARATISH"
        )

        create_button.setObjectName(
            "createButton"
        )

        create_button.clicked.connect(
            self.create_master_license
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

        self.device_input.setText(
            get_device_id()
        )

        self.full_name_input.setFocus()

    def create_master_license(self):
        if not private_key_exists():

            QMessageBox.critical(
                self,
                "Private key",
                "Private key topilmadi.",
            )

            return

        device_id = (
            self.device_input
            .text()
            .strip()
        )

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

        if not full_name:

            QMessageBox.warning(
                self,
                "F.I.Sh.",
                "F.I.Sh. kiriting.",
            )

            return

        if not username:

            QMessageBox.warning(
                self,
                "Login",
                "Login kiriting.",
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

            license_data = generate_license(
                device_id=device_id,
                username=username,
                password=password,
                full_name=full_name,
                license_type="MASTER",
                duration_code="PERMANENT",
            )

        except Exception as exc:

            QMessageBox.critical(
                self,
                "MASTER license yaratilmadi",
                str(
                    exc
                ),
            )

            return

        suggested_name = (
            f"{username}_ARCHIPRO_MASTER.archiprolic"
        )

        file_path, _ = (
            QFileDialog.getSaveFileName(
                self,
                "MASTER litsenziyani saqlash",
                suggested_name,
                (
                    "ARCHIPRO License "
                    "(*.archiprolic)"
                ),
            )
        )

        if not file_path:
            return

        try:

            saved_path = save_license(
                license_data,
                file_path,
            )

        except Exception as exc:

            QMessageBox.critical(
                self,
                "Saqlash xatosi",
                str(
                    exc
                ),
            )

            return

        QMessageBox.information(
            self,
            "ARCHIPRO MASTER",
            (
                "MASTER litsenziya muvaffaqiyatli yaratildi.\n\n"
                f"Device ID: {device_id}\n"
                f"Login: {username}\n"
                "Litsenziya: MASTER\n"
                "Muddati: Muddatsiz\n\n"
                f"Fayl:\n{saved_path}"
            ),
        )

        self.clear_form()


def main():
    app = QApplication(
        sys.argv
    )

    app.setApplicationName(
        "ARCHIPRO OWNER"
    )

    app.setOrganizationName(
        "ARCHIPRO UZ"
    )

    window = OwnerWindow()

    window.show()

    sys.exit(
        app.exec()
    )


if __name__ == "__main__":
    main()
