from PySide6.QtCore import (
    Qt,
    Signal,
)

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

    login_requested = Signal(
        str,
        str,
    )

    def __init__(self):
        super().__init__()

        self.setWindowTitle(
            "ARCHIPRO UZ — Kirish"
        )

        self.setMinimumSize(
            1100,
            700,
        )

        self.resize(
            1280,
            780,
        )

        self.setObjectName(
            "loginRoot"
        )

        self.setup_styles()
        self.build_ui()

    # ========================================================
    # STYLE
    # ========================================================

    def setup_styles(self):
        self.setStyleSheet(
            """
            QWidget#loginRoot {
                background-color: #F5F1E7;
                font-family: "Segoe UI";
                color: #0E5558;
            }


            /* ================================================
               LEFT PANEL
               ================================================ */

            QFrame#brandPanel {
                background-color: #F5F1E7;

                border: 1px solid #D5CBBB;
                border-radius: 22px;
            }

            QLabel#brandEyebrow {
                color: #0E5558;

                font-size: 12px;
                font-weight: 800;
            }

            QLabel#brandTitle {
                color: #0E5558;

                font-size: 40px;
                font-weight: 900;
            
                font-family: "Georgia";
}

            QLabel#brandSubtitle {
                color: #586B64;

                font-size: 16px;
            }

            QLabel#brandDescription {
                color: #203B36;

                font-size: 15px;
            }


            /* ================================================
               FEATURE CARDS
               ================================================ */

            QFrame#featureCard {
                background-color: #FFFDF7;

                border: 1px solid #D5CBBB;
                border-radius: 13px;
            }

            QLabel#featureIndex {
                background-color: #FFFDF7;

                border: 1px solid #4B7B78;
                border-radius: 7px;

                color: #0E5558;

                min-width: 28px;
                max-width: 28px;

                min-height: 28px;
                max-height: 28px;

                font-size: 11px;
                font-weight: 800;
            }

            QLabel#featureTitle {
                color: #0E5558;

                font-size: 14px;
                font-weight: 700;
            }

            QLabel#featureText {
                color: #586B64;

                font-size: 12px;
            }


            /* ================================================
               RIGHT LOGIN CARD
               ================================================ */

            QFrame#loginCard {
                background-color: #FFFDF7;

                border: 1px solid #D5CBBB;
                border-radius: 22px;
            }

            QLabel#loginEyebrow {
                color: #0E5558;

                font-size: 11px;
                font-weight: 800;
            }

            QLabel#formTitle {
                color: #0E5558;

                font-size: 30px;
                font-weight: 850;
            
                font-family: "Georgia";
}

            QLabel#formSubtitle {
                color: #586B64;

                font-size: 14px;
            }

            QLabel#fieldLabel {
                color: #203B36;

                font-size: 13px;
                font-weight: 650;
            }


            /* ================================================
               INPUT
               ================================================ */

            QLineEdit {
                background-color: #F5F1E7;

                border: 1px solid #D5CBBB;
                border-radius: 11px;

                min-height: 48px;

                padding-left: 14px;
                padding-right: 14px;

                color: #0E5558;

                font-size: 14px;

                selection-background-color: #0E5558;
            }

            QLineEdit:hover {
                border-color: #D5CBBB;
            }

            QLineEdit:focus {
                background-color: #FFFDF7;

                border: 1px solid #4B7B78;
            }


            /* ================================================
               LOGIN BUTTON
               ================================================ */

            QPushButton#loginButton {
                background-color: #0E5558;

                border: 1px solid #4B7B78;
                border-radius: 11px;

                min-height: 48px;

                color: #FFFDF7;

                font-size: 14px;
                font-weight: 800;
            }

            QPushButton#loginButton:hover {
                background-color: #0E5558;

                border-color: #4B7B78;
            }

            QPushButton#loginButton:pressed {
                background-color: #0E5558;
            }


            /* ================================================
               ERROR
               ================================================ */

            QLabel#errorLabel {
                background-color: transparent;

                color: #A53832;

                font-size: 12px;
                font-weight: 600;
            }


            /* ================================================
               SECURITY INFO
               ================================================ */

            QFrame#securityCard {
                background-color: #F5F1E7;

                border: 1px solid #D5CBBB;
                border-radius: 11px;
            }

            QLabel#securityTitle {
                color: #27624A;

                font-size: 11px;
                font-weight: 800;
            }

            QLabel#securityText {
                color: #586B64;

                font-size: 11px;
            }


            /* ================================================
               DEVELOPER
               ================================================ */

            QFrame#developerCard {
                background-color: #F5F1E7;

                border: 1px solid #D5CBBB;
                border-radius: 12px;
            }

            QLabel#developerTitle {
                color: #0E5558;

                font-size: 10px;
                font-weight: 800;
            }

            QLabel#developerName {
                color: #0E5558;

                font-size: 12px;
                font-weight: 700;
            }

            QLabel#developerPhone {
                color: #586B64;

                font-size: 11px;
            }

            QLabel#versionText {
                color: #586B64;

                font-size: 10px;
            }
            """
        )

    # ========================================================
    # BUILD UI
    # ========================================================

    def build_ui(self):
        main = QHBoxLayout(
            self
        )

        main.setContentsMargins(
            34,
            34,
            34,
            34,
        )

        main.setSpacing(
            24
        )

        # ====================================================
        # LEFT — BRAND / PRODUCT
        # ====================================================

        left = QFrame()

        left.setObjectName(
            "brandPanel"
        )

        left_layout = QVBoxLayout(
            left
        )

        left_layout.setContentsMargins(
            38,
            36,
            38,
            32,
        )

        left_layout.setSpacing(
            13
        )

        eyebrow = QLabel(
            "PROFESSIONAL ARCHITECTURE EDUCATION"
        )

        eyebrow.setObjectName(
            "brandEyebrow"
        )

        brand = QLabel(
            "ARCHIPRO UZ"
        )

        brand.setObjectName(
            "brandTitle"
        )

        subtitle = QLabel(
            "Arxitektura • Archicad • Qurilish • BIM"
        )

        subtitle.setObjectName(
            "brandSubtitle"
        )

        description = QLabel(
            "O'zbekiston sharoitida 1–2 qavatli "
            "turar joylarni loyihalashni nazariya, "
            "amaliyot, test va real loyiha bosqichlari "
            "orqali o'rganish tizimi."
        )

        description.setObjectName(
            "brandDescription"
        )

        description.setWordWrap(
            True
        )

        left_layout.addWidget(
            eyebrow
        )

        left_layout.addWidget(
            brand
        )

        left_layout.addWidget(
            subtitle
        )

        left_layout.addWidget(
            description
        )

        left_layout.addSpacing(
            15
        )

        # ====================================================
        # FEATURES
        # ====================================================

        features = [
            (
                "01",
                "Arxitektura asoslari",
                "0 dan boshlab fazoviy fikrlash va rejalashtirish.",
            ),
            (
                "02",
                "Archicad workflow",
                "Boshlang'ich vositalardan professional BIM ish jarayonigacha.",
            ),
            (
                "03",
                "Qurilish va normativlar",
                "Konstruksiya, SHNQ va real loyiha mantig'i.",
            ),
            (
                "04",
                "Amaliy nazorat",
                "Mini-test, Bosqich imtihonlari va progress tizimi.",
            ),
        ]

        for (
            index,
            title,
            text,
        ) in features:
            left_layout.addWidget(
                self.create_feature_card(
                    index,
                    title,
                    text,
                )
            )

        left_layout.addStretch()

        # ====================================================
        # DEVELOPER INFO
        # ====================================================

        developer = QFrame()

        developer.setObjectName(
            "developerCard"
        )

        developer_layout = QVBoxLayout(
            developer
        )

        developer_layout.setContentsMargins(
            14,
            11,
            14,
            11,
        )

        developer_layout.setSpacing(
            3
        )

        developer_title = QLabel(
            "DASTUR HAQIDA"
        )

        developer_title.setObjectName(
            "developerTitle"
        )

        developer_name = QLabel(
            "Dasturchi: Muxriddin Faxriddinovich"
        )

        developer_name.setObjectName(
            "developerName"
        )

        developer_name.setWordWrap(
            True
        )

        phone_1 = QLabel(
            "+998 94 788 88 99"
        )

        phone_1.setObjectName(
            "developerPhone"
        )

        phone_2 = QLabel(
            "+998 33 911 22 22"
        )

        phone_2.setObjectName(
            "developerPhone"
        )

        version = QLabel(
            "ARCHIPRO UZ  •  Offline Desktop Academy"
        )

        version.setObjectName(
            "versionText"
        )

        developer_layout.addWidget(
            developer_title
        )

        developer_layout.addWidget(
            developer_name
        )

        developer_layout.addWidget(
            phone_1
        )

        developer_layout.addWidget(
            phone_2
        )

        developer_layout.addWidget(
            version
        )

        left_layout.addWidget(
            developer
        )

        # ====================================================
        # RIGHT — LOGIN
        # ====================================================

        right_wrapper = QVBoxLayout()

        right_wrapper.setContentsMargins(
            0,
            30,
            0,
            30,
        )

        right_wrapper.addStretch()

        card = QFrame()

        card.setObjectName(
            "loginCard"
        )

        card.setMinimumWidth(
            410
        )

        card.setMaximumWidth(
            460
        )

        card_layout = QVBoxLayout(
            card
        )

        card_layout.setContentsMargins(
            34,
            32,
            34,
            32,
        )

        card_layout.setSpacing(
            11
        )

        login_eyebrow = QLabel(
            "FOYDALANUVCHI KABINETI"
        )

        login_eyebrow.setObjectName(
            "loginEyebrow"
        )

        form_title = QLabel(
            "Tizimga kirish"
        )

        form_title.setObjectName(
            "formTitle"
        )

        form_subtitle = QLabel(
            "ARCHIPRO UZ o'quv platformasini "
            "davom ettirish uchun ma'lumotlaringizni kiriting."
        )

        form_subtitle.setObjectName(
            "formSubtitle"
        )

        form_subtitle.setWordWrap(
            True
        )

        card_layout.addWidget(
            login_eyebrow
        )

        card_layout.addWidget(
            form_title
        )

        card_layout.addWidget(
            form_subtitle
        )

        card_layout.addSpacing(
            13
        )

        # ====================================================
        # LOGIN
        # ====================================================

        login_label = QLabel(
            "Login"
        )

        login_label.setObjectName(
            "fieldLabel"
        )

        self.login_input = QLineEdit()

        self.login_input.setPlaceholderText(
            "Loginingizni kiriting"
        )

        self.login_input.setClearButtonEnabled(
            True
        )

        card_layout.addWidget(
            login_label
        )

        card_layout.addWidget(
            self.login_input
        )

        card_layout.addSpacing(
            5
        )

        # ====================================================
        # PASSWORD
        # ====================================================

        password_label = QLabel(
            "Parol"
        )

        password_label.setObjectName(
            "fieldLabel"
        )

        self.password_input = QLineEdit()

        self.password_input.setPlaceholderText(
            "Parolingizni kiriting"
        )

        self.password_input.setEchoMode(
            QLineEdit.EchoMode.Password
        )

        card_layout.addWidget(
            password_label
        )

        card_layout.addWidget(
            self.password_input
        )

        # ====================================================
        # ERROR
        # ====================================================

        self.error_label = QLabel(
            ""
        )

        self.error_label.setObjectName(
            "errorLabel"
        )

        self.error_label.setWordWrap(
            True
        )

        self.error_label.setMinimumHeight(
            20
        )

        card_layout.addWidget(
            self.error_label
        )

        # ====================================================
        # BUTTON
        # ====================================================

        self.login_button = QPushButton(
            "KIRISH  →"
        )

        self.login_button.setObjectName(
            "loginButton"
        )

        self.login_button.setCursor(
            Qt.CursorShape.PointingHandCursor
        )

        self.login_button.clicked.connect(
            self.handle_login
        )

        self.password_input.returnPressed.connect(
            self.handle_login
        )

        self.login_input.returnPressed.connect(
            self.focus_password
        )

        card_layout.addWidget(
            self.login_button
        )

        card_layout.addSpacing(
            12
        )

        # ====================================================
        # SECURITY
        # ====================================================

        security = QFrame()

        security.setObjectName(
            "securityCard"
        )

        security_layout = QVBoxLayout(
            security
        )

        security_layout.setContentsMargins(
            13,
            10,
            13,
            10,
        )

        security_layout.setSpacing(
            3
        )

        security_title = QLabel(
            "OFFLINE ISH REJIMI"
        )

        security_title.setObjectName(
            "securityTitle"
        )

        security_text = QLabel(
            "Darslar, progress va o'quv ma'lumotlari "
            "kompyuterning lokal bazasida ishlaydi."
        )

        security_text.setObjectName(
            "securityText"
        )

        security_text.setWordWrap(
            True
        )

        security_layout.addWidget(
            security_title
        )

        security_layout.addWidget(
            security_text
        )

        card_layout.addWidget(
            security
        )

        right_wrapper.addWidget(
            card,
            0,
            Qt.AlignmentFlag.AlignHCenter,
        )

        right_wrapper.addStretch()

        # ====================================================
        # ADD PANELS
        # ====================================================

        main.addWidget(
            left,
            3,
        )

        main.addLayout(
            right_wrapper,
            2,
        )

        self.login_input.setFocus()

    # ========================================================
    # FEATURE CARD
    # ========================================================

    def create_feature_card(
        self,
        index: str,
        title: str,
        text: str,
    ):
        card = QFrame()

        card.setObjectName(
            "featureCard"
        )

        layout = QHBoxLayout(
            card
        )

        layout.setContentsMargins(
            13,
            11,
            13,
            11,
        )

        layout.setSpacing(
            11
        )

        number = QLabel(
            index
        )

        number.setObjectName(
            "featureIndex"
        )

        number.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        text_layout = QVBoxLayout()

        text_layout.setSpacing(
            2
        )

        title_label = QLabel(
            title
        )

        title_label.setObjectName(
            "featureTitle"
        )

        body = QLabel(
            text
        )

        body.setObjectName(
            "featureText"
        )

        body.setWordWrap(
            True
        )

        text_layout.addWidget(
            title_label
        )

        text_layout.addWidget(
            body
        )

        layout.addWidget(
            number,
            0,
            Qt.AlignmentFlag.AlignTop,
        )

        layout.addLayout(
            text_layout,
            1,
        )

        return card

    # ========================================================
    # INPUT FLOW
    # ========================================================

    def focus_password(self):
        self.password_input.setFocus()

    # ========================================================
    # LOGIN
    # ========================================================

    def handle_login(self):
        login = (
            self.login_input
            .text()
            .strip()
        )

        password = (
            self.password_input
            .text()
            .strip()
        )

        self.error_label.clear()

        if not login:
            self.error_label.setText(
                "Login kiritilmagan."
            )

            self.login_input.setFocus()

            return

        if not password:
            self.error_label.setText(
                "Parol kiritilmagan."
            )

            self.password_input.setFocus()

            return

        # Login paytida button ikki marta bosilib
        # ketmasligi uchun qisqa blok.
        self.login_button.setEnabled(
            False
        )

        self.login_button.setText(
            "TEKSHIRILMOQDA..."
        )

        self.login_requested.emit(
            login,
            password,
        )

        # Agar authentication muvaffaqiyatsiz bo'lsa,
        # main.py error_label'ga xabar yozadi.
        # Window yopilmagan bo'lsa tugmani qayta yoqamiz.
        self.login_button.setEnabled(
            True
        )

        self.login_button.setText(
            "KIRISH  →"
        )
