from PySide6.QtCore import (
    Qt,
    Signal,
)
from PySide6.QtGui import (
    QGuiApplication,
)
from PySide6.QtWidgets import (
    QFileDialog,
    QFrame,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMessageBox,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from licensing.device_id import (
    get_device_id,
)

from licensing.license_service import (
    install_license,
)


class ActivationWindow(QWidget):
    activation_successful = Signal()

    def __init__(self):
        super().__init__()

        self.setWindowTitle(
            "ARCHIPRO UZ - Aktivatsiya"
        )

        self.resize(
            760,
            560,
        )

        self.setMinimumSize(
            650,
            500,
        )

        self.setup_ui()

    def setup_ui(self):
        self.setStyleSheet(
            """
            QWidget {
                background-color: #F5F1E7;
                color: #0E5558;
                font-family: Segoe UI;
            }

            QFrame#card {
                background-color: #FFFDF7;
                border: 1px solid #D5CBBB;
                border-radius: 16px;
            }

            QLabel#title {
                font-size: 28px;
                font-weight: 800;
                color: #203B36;
            
                font-family: "Georgia";
}

            QLabel#subtitle {
                font-size: 14px;
                color: #586B64;
            }

            QLabel#label {
                font-size: 13px;
                color: #203B36;
            }

            QLabel#info {
                font-size: 12px;
                color: #586B64;
            }

            QLabel#error {
                font-size: 13px;
                color: #A53832;
            }

            QLineEdit {
                background-color: #FFFDF7;
                border: 1px solid #D5CBBB;
                border-radius: 9px;
                padding: 11px;
                color: #203B36;
                font-size: 13px;
            }

            QPushButton#copyButton {
                background-color: #FFFDF7;
                border: 1px solid #D5CBBB;
                border-radius: 8px;
                padding: 10px 14px;
                color: #203B36;
                font-weight: 600;
            }

            QPushButton#copyButton:hover {
                background-color: #FFFDF7;
            }

            QPushButton#activateButton {
                background-color: #0E5558;
                border: none;
                border-radius: 9px;
                padding: 12px 18px;
                color: #FFFDF7;
                font-size: 14px;
                font-weight: 700;
            }

            QPushButton#activateButton:hover {
                background-color: #0E5558;
            }
            """
        )

        root = QVBoxLayout(
            self
        )

        root.setContentsMargins(
            38,
            32,
            38,
            32,
        )

        root.setSpacing(
            18
        )

        title = QLabel(
            "ARCHIPRO UZ aktivatsiyasi"
        )

        title.setObjectName(
            "title"
        )

        subtitle = QLabel(
            "Dastur ushbu kompyuter uchun chiqarilgan "
            "litsenziya fayli bilan faollashtiriladi."
        )

        subtitle.setObjectName(
            "subtitle"
        )

        subtitle.setWordWrap(
            True
        )

        root.addWidget(
            title
        )

        root.addWidget(
            subtitle
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
            14
        )

        device_label = QLabel(
            "Sizning Device ID:"
        )

        device_label.setObjectName(
            "label"
        )

        card_layout.addWidget(
            device_label
        )

        device_row = QHBoxLayout()

        self.device_input = (
            QLineEdit()
        )

        self.device_input.setReadOnly(
            True
        )

        self.device_input.setText(
            get_device_id()
        )

        copy_button = QPushButton(
            "NUSXA OLISH"
        )

        copy_button.setObjectName(
            "copyButton"
        )

        copy_button.clicked.connect(
            self.copy_device_id
        )

        device_row.addWidget(
            self.device_input,
            1,
        )

        device_row.addWidget(
            copy_button
        )

        card_layout.addLayout(
            device_row
        )

        info = QLabel(
            "1. Device ID'ni ARCHIPRO administratoriga yuboring.\n"
            "2. Sizga .archiprolic litsenziya fayli beriladi.\n"
            "3. Quyidagi tugma orqali shu faylni tanlang."
        )

        info.setObjectName(
            "info"
        )

        info.setWordWrap(
            True
        )

        card_layout.addWidget(
            info
        )

        card_layout.addSpacing(
            8
        )

        activate_button = QPushButton(
            "LITSENZIYA FAYLINI TANLASH"
        )

        activate_button.setObjectName(
            "activateButton"
        )

        activate_button.clicked.connect(
            self.select_license
        )

        card_layout.addWidget(
            activate_button
        )

        self.error_label = QLabel(
            ""
        )

        self.error_label.setObjectName(
            "error"
        )

        self.error_label.setWordWrap(
            True
        )

        card_layout.addWidget(
            self.error_label
        )

        root.addWidget(
            card
        )

        root.addStretch()

    def copy_device_id(self):
        clipboard = (
            QGuiApplication.clipboard()
        )

        clipboard.setText(
            self.device_input.text()
        )

        QMessageBox.information(
            self,
            "Device ID",
            "Device ID nusxalandi.",
        )

    def select_license(self):
        file_path, _ = (
            QFileDialog.getOpenFileName(
                self,
                "ARCHIPRO litsenziya faylini tanlang",
                "",
                (
                    "ARCHIPRO License "
                    "(*.archiprolic);;"
                    "Barcha fayllar (*)"
                ),
            )
        )

        if not file_path:
            return

        result = install_license(
            file_path
        )

        if not result.get(
            "valid"
        ):
            self.error_label.setText(
                result.get(
                    "message",
                    "Litsenziya qabul qilinmadi.",
                )
            )

            QMessageBox.warning(
                self,
                "Aktivatsiya amalga oshmadi",
                self.error_label.text(),
            )

            return

        self.error_label.clear()

        payload = result.get(
            "payload",
            {},
        )

        username = payload.get(
            "username",
            "",
        )

        QMessageBox.information(
            self,
            "ARCHIPRO UZ",
            (
                "Dastur muvaffaqiyatli faollashtirildi.\n\n"
                f"Login: {username}\n\n"
                "Endi login va parol bilan dasturga kiring."
            ),
        )

        self.activation_successful.emit()

        self.close()
