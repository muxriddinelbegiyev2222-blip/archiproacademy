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
    def __init__(self, user: dict):
        super().__init__()
        self.user = user
        self.setWindowTitle("ARCHIPRO UZ - Litsenziya")
        self.resize(720, 650)
        self.setMinimumSize(650, 560)
        self.build_ui()

    def _format_datetime(self, value) -> str:
        if not value:
            return "Muddatsiz"
        try:
            parsed = datetime.fromisoformat(str(value))
            return parsed.strftime("%d.%m.%Y %H:%M")
        except Exception:
            return str(value)

    def _add_info_row(self, layout, title: str, value: str):
        row = QFrame()
        row.setObjectName("infoRow")
        row_layout = QVBoxLayout(row)
        row_layout.setContentsMargins(16, 12, 16, 12)
        row_layout.setSpacing(5)

        title_label = QLabel(title)
        title_label.setObjectName("rowTitle")

        value_label = QLabel(value)
        value_label.setObjectName("rowValue")
        value_label.setWordWrap(True)
        value_label.setTextInteractionFlags(
            Qt.TextInteractionFlag.TextSelectableByMouse
        )

        row_layout.addWidget(title_label)
        row_layout.addWidget(value_label)
        layout.addWidget(row)

    def build_ui(self):
        central = QWidget()
        self.setCentralWidget(central)

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
