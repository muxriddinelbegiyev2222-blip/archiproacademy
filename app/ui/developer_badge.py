from PySide6.QtCore import (
    Qt,
)

from PySide6.QtWidgets import (
    QFrame,
    QLabel,
    QVBoxLayout,
)


class DeveloperBadge(
    QFrame
):
    def __init__(
        self,
        parent=None,
    ):
        super().__init__(
            parent
        )

        self.setObjectName(
            "developerCard"
        )

        self.setCursor(
            Qt.CursorShape.ArrowCursor
        )

        self.setStyleSheet(
            """
            QFrame#developerCard {
                background-color: #0D192B;
                border: 1px solid #29415F;
                border-radius: 12px;
            }

            QLabel#devSmallTitle {
                color: #6F9BFF;
                font-size: 11px;
                font-weight: 800;
            }

            QLabel#devName {
                color: #E7EEF8;
                font-size: 12px;
                font-weight: 700;
            }

            QLabel#devContact {
                color: #9FB0C6;
                font-size: 11px;
            }

            QLabel#devBrand {
                color: #657B97;
                font-size: 10px;
            }
            """
        )

        layout = QVBoxLayout(
            self
        )

        layout.setContentsMargins(
            12,
            10,
            12,
            10,
        )

        layout.setSpacing(
            4
        )

        title = QLabel(
            "DASTUR HAQIDA"
        )

        title.setObjectName(
            "devSmallTitle"
        )

        name = QLabel(
            "Dasturchi: Muxriddin Faxriddinovich"
        )

        name.setObjectName(
            "devName"
        )

        name.setWordWrap(
            True
        )

        phone_1 = QLabel(
            "+998 94 788 88 99"
        )

        phone_1.setObjectName(
            "devContact"
        )

        phone_2 = QLabel(
            "+998 33 911 22 22"
        )

        phone_2.setObjectName(
            "devContact"
        )

        brand = QLabel(
            "ARCHIPRO UZ  •  2026"
        )

        brand.setObjectName(
            "devBrand"
        )

        layout.addWidget(
            title
        )

        layout.addWidget(
            name
        )

        layout.addWidget(
            phone_1
        )

        layout.addWidget(
            phone_2
        )

        layout.addWidget(
            brand
        )
