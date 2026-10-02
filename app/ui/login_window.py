from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QFrame,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class LoginWindow(QWidget):
    login_requested = Signal(str, str)

    def __init__(self):
        super().__init__()

        self.setWindowTitle("ARCHIPRO UZ - Login")
        self.resize(1100, 700)

        self.setStyleSheet(
            """
            QWidget {
                background-color: #0B1220;
                color: #F8FAFC;
                font-family: Segoe UI;
            }

            QLabel#brandTitle {
                font-size: 34px;
                font-weight: 700;
                color: #FFFFFF;
            }

            QLabel#brandSubtitle {
                font-size: 15px;
                color: #94A3B8;
            }

            QLabel#formTitle {
                font-size: 28px;
                font-weight: 700;
                color: #F8FAFC;
            }

            QLabel#formSubtitle {
                font-size: 14px;
                color: #94A3B8;
            }

            QLabel#fieldLabel {
                font-size: 13px;
                color: #CBD5E1;
            }

            QLineEdit {
                min-height: 46px;
                background-color: #111827;
                border: 1px solid #263245;
                border-radius: 10px;
                padding-left: 14px;
                padding-right: 14px;
                font-size: 14px;
                color: #F8FAFC;
            }

            QLineEdit:focus {
                border: 1px solid #3B82F6;
            }

            QPushButton#loginButton {
                min-height: 48px;
                background-color: #2563EB;
                border: none;
                border-radius: 10px;
                font-size: 15px;
                font-weight: 600;
                color: white;
            }

            QPushButton#loginButton:hover {
                background-color: #3B82F6;
            }

            QPushButton#loginButton:pressed {
                background-color: #1D4ED8;
            }

            QFrame#loginCard {
                background-color: #0F172A;
                border: 1px solid #1E293B;
                border-radius: 18px;
            }

            QLabel#errorLabel {
                color: #F87171;
                font-size: 13px;
            }

            QLabel#footerLabel {
                color: #64748B;
                font-size: 12px;
            }
            """
        )

        main_layout = QHBoxLayout(self)
        main_layout.setContentsMargins(60, 50, 60, 50)
        main_layout.setSpacing(70)

        # LEFT SIDE
        left_layout = QVBoxLayout()
        left_layout.setSpacing(18)
        left_layout.setAlignment(Qt.AlignmentFlag.AlignVCenter)

        brand_title = QLabel("ARCHIPRO UZ")
        brand_title.setObjectName("brandTitle")

        brand_subtitle = QLabel(
            "O'zbekiston sharoitida 1-2 qavatli uylarni\n"
            "0 dan professional darajagacha loyihalash akademiyasi."
        )
        brand_subtitle.setObjectName("brandSubtitle")
        brand_subtitle.setWordWrap(True)

        feature_1 = QLabel("✓ Arxitektura 0 dan")
        feature_2 = QLabel("✓ Archicad professional daraja")
        feature_3 = QLabel("✓ SHNQ va normativlar")
        feature_4 = QLabel("✓ Amaliy loyihalar")
        feature_5 = QLabel("✓ Testlar va imtihonlar")

        feature_font = QFont("Segoe UI", 13)

        for feature in [
            feature_1,
            feature_2,
            feature_3,
            feature_4,
            feature_5,
        ]:
            feature.setFont(feature_font)
            feature.setStyleSheet("color: #CBD5E1;")

        left_layout.addWidget(brand_title)
        left_layout.addWidget(brand_subtitle)
        left_layout.addSpacing(20)
        left_layout.addWidget(feature_1)
        left_layout.addWidget(feature_2)
        left_layout.addWidget(feature_3)
        left_layout.addWidget(feature_4)
        left_layout.addWidget(feature_5)
        left_layout.addStretch()

        footer = QLabel("ARCHIPRO UZ © 2026")
        footer.setObjectName("footerLabel")
        left_layout.addWidget(footer)

        # RIGHT SIDE
        card = QFrame()
        card.setObjectName("loginCard")
        card.setFixedWidth(430)

        card_layout = QVBoxLayout(card)
        card_layout.setContentsMargins(42, 42, 42, 42)
        card_layout.setSpacing(14)

        form_title = QLabel("Kirish")
        form_title.setObjectName("formTitle")

        form_subtitle = QLabel(
            "Dasturga kirish uchun login va parolingizni kiriting."
        )
        form_subtitle.setObjectName("formSubtitle")
        form_subtitle.setWordWrap(True)

        login_label = QLabel("Login")
        login_label.setObjectName("fieldLabel")

        self.login_input = QLineEdit()
        self.login_input.setPlaceholderText("Login kiriting")

        password_label = QLabel("Parol")
        password_label.setObjectName("fieldLabel")

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Parol kiriting")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        self.error_label = QLabel("")
        self.error_label.setObjectName("errorLabel")
        self.error_label.setWordWrap(True)

        self.login_button = QPushButton("KIRISH")
        self.login_button.setObjectName("loginButton")
        self.login_button.setCursor(Qt.CursorShape.PointingHandCursor)
        self.login_button.clicked.connect(self.handle_login)

        self.password_input.returnPressed.connect(self.handle_login)

        card_layout.addWidget(form_title)
        card_layout.addWidget(form_subtitle)
        card_layout.addSpacing(18)
        card_layout.addWidget(login_label)
        card_layout.addWidget(self.login_input)
        card_layout.addWidget(password_label)
        card_layout.addWidget(self.password_input)
        card_layout.addWidget(self.error_label)
        card_layout.addSpacing(8)
        card_layout.addWidget(self.login_button)
        card_layout.addStretch()

        main_layout.addLayout(left_layout, 1)
        main_layout.addWidget(card)

    def handle_login(self):
        login = self.login_input.text().strip()
        password = self.password_input.text().strip()

        self.error_label.clear()

        if not login:
            self.error_label.setText("Login kiritilmagan.")
            self.login_input.setFocus()
            return

        if not password:
            self.error_label.setText("Parol kiritilmagan.")
            self.password_input.setFocus()
            return

        self.login_requested.emit(login, password)
