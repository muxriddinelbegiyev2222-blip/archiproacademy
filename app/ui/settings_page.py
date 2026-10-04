from PySide6.QtCore import Signal

from PySide6.QtWidgets import (
    QFileDialog,
    QFrame,
    QHBoxLayout,
    QLabel,
    QMessageBox,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from courses.user_features import (
    export_user_backup,
    import_user_backup,
)

from database.database import (
    DATABASE_PATH,
)


class SettingsPage(QWidget):
    clear_cache_requested = Signal()
    reload_home_requested = Signal()
    backup_imported = Signal()

    def __init__(
        self,
        user: dict,
    ):
        super().__init__()

        self.user = user

        self.build_ui()

    def _action_card(
        self,
        title_text: str,
        description: str,
        button_text: str,
        callback,
    ):
        card = QFrame()
        card.setObjectName(
            "levelOverviewCard"
        )

        layout = QHBoxLayout(
            card
        )
        layout.setContentsMargins(
            20,
            17,
            20,
            17,
        )
        layout.setSpacing(
            18
        )

        text_area = QVBoxLayout()

        title = QLabel(
            title_text
        )
        title.setObjectName(
            "levelCode"
        )

        desc = QLabel(
            description
        )
        desc.setObjectName(
            "levelDesc"
        )
        desc.setWordWrap(
            True
        )

        text_area.addWidget(
            title
        )
        text_area.addWidget(
            desc
        )

        layout.addLayout(
            text_area,
            1,
        )

        button = QPushButton(
            button_text
        )
        button.setObjectName(
            "openLevelButton"
        )
        button.clicked.connect(
            callback
        )

        layout.addWidget(
            button
        )

        return card

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
            "ARCHIPRO UZ interfeysi, progress backup va "
            "lokal ma'lumotlar boshqaruvi."
        )
        subtitle.setObjectName(
            "overviewSubtitle"
        )
        subtitle.setWordWrap(
            True
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
            f"{name}\nLitsenziya: {license_type}"
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

        backup_card = QFrame()
        backup_card.setObjectName(
            "levelOverviewCard"
        )

        backup_layout = QVBoxLayout(
            backup_card
        )
        backup_layout.setContentsMargins(
            20,
            17,
            20,
            17,
        )
        backup_layout.setSpacing(
            10
        )

        backup_title = QLabel(
            "PROGRESS BACKUP"
        )
        backup_title.setObjectName(
            "levelCode"
        )

        backup_desc = QLabel(
            "Dars progressi, test va imtihon natijalari, "
            "bookmark hamda shaxsiy eslatmalarni "
            ".archiprobackup faylga saqlang. "
            "Backup litsenziya yoki parolni saqlamaydi."
        )
        backup_desc.setObjectName(
            "levelDesc"
        )
        backup_desc.setWordWrap(
            True
        )

        buttons = QHBoxLayout()
        buttons.setSpacing(
            10
        )

        export_button = QPushButton(
            "BACKUP YARATISH"
        )
        export_button.setObjectName(
            "openLevelButton"
        )
        export_button.clicked.connect(
            self.export_backup
        )

        import_button = QPushButton(
            "BACKUPNI TIKLASH"
        )
        import_button.setObjectName(
            "openLevelButton"
        )
        import_button.clicked.connect(
            self.import_backup
        )

        buttons.addWidget(
            export_button
        )
        buttons.addWidget(
            import_button
        )
        buttons.addStretch()

        backup_layout.addWidget(
            backup_title
        )
        backup_layout.addWidget(
            backup_desc
        )
        backup_layout.addLayout(
            buttons
        )

        root.addWidget(
            backup_card
        )

        root.addWidget(
            self._action_card(
                "INTERFEYS KESHI",
                (
                    "Agar uzoq ishlagandan keyin interfeys "
                    "og'irlashsa, vaqtinchalik sahifa keshini "
                    "tozalash mumkin. Progress o'chmaydi."
                ),
                "KESHNI TOZALASH",
                self.clear_cache_requested,
            )
        )

        root.addWidget(
            self._action_card(
                "MA'LUMOTLARNI YANGILASH",
                (
                    "Bosh sahifadagi progress, XP, yaqinda "
                    "ko'rilganlar va keyingi dars ma'lumotlarini "
                    "qayta hisoblash."
                ),
                "YANGILASH",
                self.reload_home_requested,
            )
        )

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

        database_title = QLabel(
            "LOKAL MA'LUMOTLAR BAZASI"
        )
        database_title.setObjectName(
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
            database_title
        )
        database_layout.addWidget(
            path
        )

        root.addWidget(
            database
        )
        root.addStretch()

    def export_backup(self):
        suggested = (
            f"{self.user.get('username', 'archipro')}"
            "_progress.archiprobackup"
        )

        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "ARCHIPRO progress backup",
            suggested,
            "ARCHIPRO Backup (*.archiprobackup)",
        )

        if not file_path:
            return

        try:
            saved = export_user_backup(
                self.user["id"],
                file_path,
            )

        except Exception as exc:
            QMessageBox.critical(
                self,
                "Backup xatosi",
                str(
                    exc
                ),
            )
            return

        QMessageBox.information(
            self,
            "Backup tayyor",
            (
                "Progress backup muvaffaqiyatli yaratildi.\n\n"
                f"{saved}"
            ),
        )

    def import_backup(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "ARCHIPRO progress backupni tanlang",
            "",
            "ARCHIPRO Backup (*.archiprobackup)",
        )

        if not file_path:
            return

        confirm = QMessageBox.question(
            self,
            "Backupni tiklash",
            (
                "Backup ma'lumotlari joriy profilga "
                "qo'shiladi va progress bilan birlashtiriladi. "
                "Davom etilsinmi?"
            ),
        )

        if confirm != QMessageBox.StandardButton.Yes:
            return

        try:
            result = import_user_backup(
                self.user["id"],
                file_path,
            )

        except Exception as exc:
            QMessageBox.critical(
                self,
                "Backup tiklanmadi",
                str(
                    exc
                ),
            )
            return

        QMessageBox.information(
            self,
            "Backup tiklandi",
            result.get(
                "message",
                "Backup tiklandi.",
            ),
        )

        self.backup_imported.emit()
        self.reload_home_requested.emit()
