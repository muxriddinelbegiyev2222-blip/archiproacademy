from datetime import datetime

from PySide6.QtCore import Qt
from PySide6.QtGui import QGuiApplication
from PySide6.QtWidgets import (
    QFrame,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from licensing.device_id import get_device_id
from licensing.license_service import validate_installed_license


class LicenseWindow(QMainWindow):
    def __init__(
        self,
        user: dict,
    ):
        super().__init__()

        self.user = user

        self.setWindowTitle(
            "ARCHIPRO UZ - Litsenziya"
        )

        self.resize(
            720,
            650,
        )

        self.setMinimumSize(
            650,
            560,
        )

        self.build_ui()

    def _format_datetime(
        self,
        value,
    ) -> str:
        if not value:
            return "Muddatsiz"

        try:
            parsed = datetime.fromisoformat(
                str(value)
            )

            return parsed.strftime(
                "%d.%m.%Y %H:%M"
            )

        except Exception:
            return str(value)

    def _add_info_row(
        self,
        layout,
        title: str,
        value: str,
    ):
        row = QFrame()

        row.setObjectName(
            "infoRow"
        )

        row_layout = QVBoxLayout(
            row
        )

        row_layout.setContentsMargins(
            16,
            12,
            16,
            12,
        )

        row_layout.setSpacing(
            5
        )

        title_label = QLabel(
            title
        )

        title_label.setObjectName(
            "rowTitle"
        )

        value_label = QLabel(
            value
        )

        value_label.setObjectName(
            "rowValue"
        )

        value_label.setWordWrap(
            True
        )

        value_label.setTextInteractionFlags(
            Qt.TextInteractionFlag.TextSelectableByMouse
        )

        row_layout.addWidget(
            title_label
        )

        row_layout.addWidget(
            value_label
        )

        layout.addWidget(
            row
        )

    def build_ui(self):
        central = QWidget()

        self.setCentralWidget(
            central
        )

        self.setStyleSheet(
            """
            QMainWindow,
            QWidget {
                background-color: #0B1220;
                color: #F8FAFC;
                font-family: Segoe UI;
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

            QFrame#statusOk {
                background-color: #10251C;
                border: 1px solid #15803D;
                border-radius: 12px;
            }

            QFrame#statusError {
                background-color: #2A1515;
                border: 1px solid #B91C1C;
                border-radius: 12px;
            }

            QLabel#statusTitle {
                font-size: 16px;
                font-weight: 800;
                color: #FFFFFF;
            }

            QLabel#statusText {
                font-size: 12px;
                color: #CBD5E1;
            }

            QFrame#infoRow {
                background-color: #111827;
                border: 1px solid #1E293B;
                border-radius: 10px;
            }

            QLabel#rowTitle {
                font-size: 11px;
                color: #64748B;
            }

            QLabel#rowValue {
                font-size: 14px;
                font-weight: 600;
                color: #F8FAFC;
            }

            QPushButton#copyButton {
                background-color: #1E293B;
                border: 1px solid #334155;
                border-radius: 9px;
                padding: 11px 16px;
                color: #FFFFFF;
                font-size: 13px;
                font-weight: 600;
            }

            QPushButton#copyButton:hover {
                background-color: #334155;
            }

            QPushButton#refreshButton {
                background-color: #2563EB;
                border: none;
                border-radius: 9px;
                padding: 11px 16px;
                color: #FFFFFF;
                font-size: 13px;
                font-weight: 700;
            }

            QPushButton#refreshButton:hover {
                background-color: #3B82F6;
            }
            """
        )

        root = QVBoxLayout(
            central
        )

        root.setContentsMargins(
            32,
            28,
            32,
            28,
        )

        root.setSpacing(
            14
        )

        title = QLabel(
            "Litsenziya ma'lumotlari"
        )

        title.setObjectName(
            "title"
        )

        subtitle = QLabel(
            "Ushbu kompyuterda faollashtirilgan ARCHIPRO UZ "
            "litsenziyasi haqida ma'lumot."
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

        result = (
            validate_installed_license()
        )

        status = QFrame()

        if result.get(
            "valid"
        ):
            status.setObjectName(
                "statusOk"
            )

            status_title_text = (
                "✓ LITSENZIYA FAOL"
            )

            status_text_value = (
                result.get(
                    "message",
                    "Litsenziya haqiqiy.",
                )
            )

        else:
            status.setObjectName(
                "statusError"
            )

            status_title_text = (
                "LITSENZIYA MUAMMOSI"
            )

            status_text_value = (
                result.get(
                    "message",
                    "Litsenziya haqiqiy emas.",
                )
            )

        status_layout = QVBoxLayout(
            status
        )

        status_layout.setContentsMargins(
            18,
            14,
            18,
            14,
        )

        status_layout.setSpacing(
            5
        )

        status_title = QLabel(
            status_title_text
        )

        status_title.setObjectName(
            "statusTitle"
        )

        status_text = QLabel(
            status_text_value
        )

        status_text.setObjectName(
            "statusText"
        )

        status_text.setWordWrap(
            True
        )

        status_layout.addWidget(
            status_title
        )

        status_layout.addWidget(
            status_text
        )

        root.addWidget(
            status
        )

        payload = result.get(
            "payload",
            {},
        )

        full_name = (
            payload.get(
                "full_name"
            )
            or self.user.get(
                "full_name"
            )
            or self.user.get(
                "username"
            )
            or "-"
        )

        username = (
            payload.get(
                "username"
            )
            or self.user.get(
                "username"
            )
            or "-"
        )

        license_type = (
            payload.get(
                "license_type"
            )
            or self.user.get(
                "license_type"
            )
            or "PRO"
        )

        device_id = (
            get_device_id()
        )

        self._add_info_row(
            root,
            "Foydalanuvchi",
            str(
                full_name
            ),
        )

        self._add_info_row(
            root,
            "Login",
            str(
                username
            ),
        )

        self._add_info_row(
            root,
            "Litsenziya turi",
            str(
                license_type
            ),
        )

        self._add_info_row(
            root,
            "Device ID",
            str(
                device_id
            ),
        )

        self._add_info_row(
            root,
            "Berilgan sana",
            self._format_datetime(
                payload.get(
                    "issued_at"
                )
            ),
        )

        self._add_info_row(
            root,
            "Amal qilish muddati",
            self._format_datetime(
                payload.get(
                    "expires_at"
                )
            ),
        )

        if payload.get(
            "license_id"
        ):
            self._add_info_row(
                root,
                "License ID",
                str(
                    payload.get(
                        "license_id"
                    )
                ),
            )

        buttons = QHBoxLayout()

        buttons.setSpacing(
            10
        )

        copy_button = QPushButton(
            "DEVICE ID NUSXA OLISH"
        )

        copy_button.setObjectName(
            "copyButton"
        )

        copy_button.clicked.connect(
            self.copy_device_id
        )

        refresh_button = QPushButton(
            "YANGILASH"
        )

        refresh_button.setObjectName(
            "refreshButton"
        )

        refresh_button.clicked.connect(
            self.refresh_window
        )

        buttons.addWidget(
            copy_button
        )

        buttons.addStretch()

        buttons.addWidget(
            refresh_button
        )

        root.addLayout(
            buttons
        )

        root.addStretch()

    def copy_device_id(self):
        clipboard = (
            QGuiApplication.clipboard()
        )

        clipboard.setText(
            get_device_id()
        )

        QMessageBox.information(
            self,
            "Device ID",
            "Device ID nusxalandi.",
        )

    def refresh_window(self):
        self.build_ui()
