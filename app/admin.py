import sys

from PySide6.QtWidgets import (
    QApplication,
    QComboBox,
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

from licensing.license_generator import (
    generate_license,
    get_private_key_path,
    private_key_exists,
    save_license,
)


class AdminWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle(
            "ARCHIPRO ADMIN"
        )

        self.resize(
            720,
            720,
        )

        self.setMinimumSize(
            650,
            650,
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

            QLabel#proInfo {
                background-color: #0F1F3D;
                border: 1px solid #1D4ED8;
                border-radius: 9px;
                padding: 11px;
                color: #BFDBFE;
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
            16
        )

        title = QLabel(
            "ARCHIPRO ADMIN"
        )

        title.setObjectName(
            "title"
        )

        subtitle = QLabel(
            "ARCHIPRO UZ mijoz litsenziyasini yaratish"
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
            "DIQQAT: Ushbu dastur va private key faqat "
            "ARCHIPRO UZ egasida saqlanadi. "
            "Mijozga ARCHIPRO ADMIN.exe berilmaydi."
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

        self.key_status = QLabel()

        self.key_status.setWordWrap(
            True
        )

        if private_key_exists():

            self.key_status.setObjectName(
                "keyOk"
            )

            self.key_status.setText(
                "✓ PRIVATE KEY TOPILDI\n"
                + str(
                    get_private_key_path()
                )
            )

        else:

            self.key_status.setObjectName(
                "keyError"
            )

            self.key_status.setText(
                "PRIVATE KEY TOPILMADI.\n"
                "Avval GENERATE_LICENSE_KEYS.bat "
                "faylini ishga tushiring."
            )

        root.addWidget(
            self.key_status
        )

        pro_info = QLabel(
            "Mijoz litsenziyasi: PRO\n"
            "MASTER test rejimi mijozlarga chiqarilmaydi."
        )

        pro_info.setObjectName(
            "proInfo"
        )

        pro_info.setWordWrap(
            True
        )

        root.addWidget(
            pro_info
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

        self.device_input.setPlaceholderText(
            "ARCHIPRO-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX"
        )

        self.full_name_input = QLineEdit()

        self.full_name_input.setPlaceholderText(
            "Masalan: Ali Valiyev"
        )

        self.username_input = QLineEdit()

        self.username_input.setPlaceholderText(
            "Masalan: ali2026"
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

        self.duration_combo = QComboBox()

        self.duration_combo.addItem(
            "Muddatsiz",
            "PERMANENT",
        )

        self.duration_combo.addItem(
            "30 kun",
            "30",
        )

        self.duration_combo.addItem(
            "90 kun",
            "90",
        )

        self.duration_combo.addItem(
            "180 kun",
            "180",
        )

        self.duration_combo.addItem(
            "365 kun",
            "365",
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

        license_label = QLabel(
            "PRO"
        )

        license_label.setStyleSheet(
            """
            QLabel {
                background-color: #0F172A;
                border: 1px solid #334155;
                border-radius: 8px;
                padding: 11px;
                color: #60A5FA;
                font-size: 14px;
                font-weight: 700;
            }
            """
        )

        form.addRow(
            "Litsenziya:",
            license_label,
        )

        form.addRow(
            "Amal qilish muddati:",
            self.duration_combo,
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
            "LICENSE YARATISH"
        )

        create_button.setObjectName(
            "createButton"
        )

        create_button.clicked.connect(
            self.create_license
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
        self.device_input.clear()
        self.full_name_input.clear()
        self.username_input.clear()
        self.password_input.clear()
        self.password_confirm_input.clear()

        self.duration_combo.setCurrentIndex(
            0
        )

        self.device_input.setFocus()

    def create_license(self):
        if not private_key_exists():

            QMessageBox.critical(
                self,
                "Private key",
                (
                    "Private key topilmadi.\n\n"
                    "Avval GENERATE_LICENSE_KEYS.bat "
                    "faylini ishga tushiring."
                ),
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

        duration_code = (
            self.duration_combo
            .currentData()
        )

        if not device_id:

            QMessageBox.warning(
                self,
                "Device ID",
                "Mijoz Device ID'sini kiriting.",
            )

            return

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

            license_data = generate_license(
                device_id=device_id,
                username=username,
                password=password,
                full_name=full_name,

                # MIJOZ UCHUN FAQAT PRO
                license_type="PRO",

                duration_code=duration_code,
            )

        except Exception as exc:

            QMessageBox.critical(
                self,
                "License yaratilmadi",
                str(
                    exc
                ),
            )

            return

        suggested_name = (
            f"{username}_ARCHIPRO.archiprolic"
        )

        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "ARCHIPRO litsenziyasini saqlash",
            suggested_name,
            "ARCHIPRO License (*.archiprolic)",
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

        payload = license_data[
            "payload"
        ]

        expires_at = (
            payload.get(
                "expires_at"
            )
            or "Muddatsiz"
        )

        QMessageBox.information(
            self,
            "ARCHIPRO LICENSE",
            (
                "Litsenziya muvaffaqiyatli yaratildi.\n\n"
                f"Foydalanuvchi: {full_name}\n"
                f"Login: {username}\n"
                "Litsenziya: PRO\n"
                f"Muddati: {expires_at}\n\n"
                f"Fayl:\n{saved_path}"
            ),
        )

        self.clear_form()


def main():
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
