from PySide6.QtCore import Signal

from PySide6.QtWidgets import (
    QFrame,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from database.database import (
    DATABASE_PATH,
)


class SettingsPage(QWidget):
    clear_cache_requested = Signal()
    reload_home_requested = Signal()

    def __init__(
        self,
        user: dict,
    ):
        super().__init__()

        self.user = user

        self.build_ui()

    def build_ui(self):
        root = QVBoxLayout(
            self
        )

        root.setContentsMargins(
            30,
            26,
            30,
            24,
        )

        root.setSpacing(
            16
        )

        # ====================================================
        # HEADER
        # ====================================================

        header = QFrame()

        header.setObjectName(
            "overviewHeader"
        )

        header_layout = QVBoxLayout(
            header
        )

        header_layout.setContentsMargins(
            24,
            20,
            24,
            20,
        )

        title = QLabel(
            "Sozlamalar"
        )

        title.setObjectName(
            "overviewTitle"
        )

        subtitle = QLabel(
            "ARCHIPRO UZ interfeysi va lokal "
            "ma'lumotlari boshqaruvi."
        )

        subtitle.setObjectName(
            "overviewSubtitle"
        )

        header_layout.addWidget(
            title
        )

        header_layout.addWidget(
            subtitle
        )

        root.addWidget(
            header
        )

        # ====================================================
        # PROFILE
        # ====================================================

        profile_card = QFrame()

        profile_card.setObjectName(
            "levelOverviewCard"
        )

        profile_layout = QVBoxLayout(
            profile_card
        )

        profile_layout.setContentsMargins(
            20,
            17,
            20,
            17,
        )

        profile_title = QLabel(
            "FOYDALANUVCHI"
        )

        profile_title.setObjectName(
            "levelCode"
        )

        name = (
            self.user.get(
                "full_name"
            )
            or self.user.get(
                "username"
            )
            or "Foydalanuvchi"
        )

        license_type = str(
            self.user.get(
                "license_type",
                "PRO",
            )
        ).upper()

        profile_text = QLabel(
            f"{name}\n"
            f"Litsenziya: {license_type}"
        )

        profile_text.setObjectName(
            "levelName"
        )

        profile_layout.addWidget(
            profile_title
        )

        profile_layout.addWidget(
            profile_text
        )

        root.addWidget(
            profile_card
        )

        # ====================================================
        # PERFORMANCE
        # ====================================================

        performance = QFrame()

        performance.setObjectName(
            "levelOverviewCard"
        )

        performance_layout = QHBoxLayout(
            performance
        )

        performance_layout.setContentsMargins(
            20,
            17,
            20,
            17,
        )

        text_area = QVBoxLayout()

        title = QLabel(
            "INTERFEYS KESHI"
        )

        title.setObjectName(
            "levelCode"
        )

        text = QLabel(
            "Agar uzoq ishlagandan keyin interfeys "
            "og'irlashsa, vaqtinchalik sahifa keshini "
            "tozalash mumkin. Dars progressi va test "
            "natijalari o'chmaydi."
        )

        text.setObjectName(
            "levelDesc"
        )

        text.setWordWrap(
            True
        )

        text_area.addWidget(
            title
        )

        text_area.addWidget(
            text
        )

        performance_layout.addLayout(
            text_area,
            1,
        )

        clear_button = QPushButton(
            "KESHNI TOZALASH"
        )

        clear_button.setObjectName(
            "openLevelButton"
        )

        clear_button.clicked.connect(
            self.clear_cache_requested
        )

        performance_layout.addWidget(
            clear_button
        )

        root.addWidget(
            performance
        )

        # ====================================================
        # REFRESH HOME
        # ====================================================

        refresh = QFrame()

        refresh.setObjectName(
            "levelOverviewCard"
        )

        refresh_layout = QHBoxLayout(
            refresh
        )

        refresh_layout.setContentsMargins(
            20,
            17,
            20,
            17,
        )

        refresh_text = QVBoxLayout()

        title = QLabel(
            "MA'LUMOTLARNI YANGILASH"
        )

        title.setObjectName(
            "levelCode"
        )

        desc = QLabel(
            "Bosh sahifadagi progress, XP va "
            "keyingi dars ma'lumotlarini qayta hisoblash."
        )

        desc.setObjectName(
            "levelDesc"
        )

        refresh_text.addWidget(
            title
        )

        refresh_text.addWidget(
            desc
        )

        refresh_layout.addLayout(
            refresh_text,
            1,
        )

        button = QPushButton(
            "YANGILASH"
        )

        button.setObjectName(
            "openLevelButton"
        )

        button.clicked.connect(
            self.reload_home_requested
        )

        refresh_layout.addWidget(
            button
        )

        root.addWidget(
            refresh
        )

        # ====================================================
        # DATABASE INFO
        # ====================================================

        database = QFrame()

        database.setObjectName(
            "levelOverviewCard"
        )

        database_layout = QVBoxLayout(
            database
        )

        database_layout.setContentsMargins(
            20,
            17,
            20,
            17,
        )

        title = QLabel(
            "LOKAL MA'LUMOTLAR BAZASI"
        )

        title.setObjectName(
            "levelCode"
        )

        path = QLabel(
            str(
                DATABASE_PATH
            )
        )

        path.setObjectName(
            "levelDesc"
        )

        path.setWordWrap(
            True
        )

        database_layout.addWidget(
            title
        )

        database_layout.addWidget(
            path
        )

        root.addWidget(
            database
        )

        root.addStretch()
