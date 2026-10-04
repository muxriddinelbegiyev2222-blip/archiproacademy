from PySide6.QtCore import Signal
from PySide6.QtWidgets import (
    QFrame,
    QHBoxLayout,
    QLabel,
    QProgressBar,
    QPushButton,
    QScrollArea,
    QVBoxLayout,
    QWidget,
)

from courses.course_service import (
    get_learning_overview,
)


class CourseOverviewPage(QWidget):
    """
    Yengil curriculum overview.

    MUHIM:
    Bu sahifa darslarning o'zini render qilmaydi.
    Faqat Bosqich kartalarini ko'rsatadi.

    Shu sabab:
    - tez ochiladi;
    - UI qotmaydi;
    - 680 ta dars birdan widgetga aylanmaydi.
    """

    open_level_requested = Signal(
        str,
        str,
        str,
    )

    def __init__(
        self,
        user: dict,
        title: str,
        subtitle: str,
        level_codes=None,
    ):
        super().__init__()

        self.user = user
        self.title_text = title
        self.subtitle_text = subtitle

        self.level_codes = list(
            level_codes or []
        )

        self.is_master = (
            str(
                user.get(
                    "license_type",
                    "",
                )
            ).upper()
            == "MASTER"
        )

        self.setObjectName(
            "courseOverviewPage"
        )

        self.build_ui()

    # ========================================================
    # HELPERS
    # ========================================================

    def clear_layout(
        self,
        layout,
    ):
        while layout.count():
            item = layout.takeAt(0)

            widget = item.widget()

            child_layout = item.layout()

            if widget is not None:
                widget.deleteLater()

            elif child_layout is not None:
                self.clear_layout(
                    child_layout
                )

    # ========================================================
    # UI
    # ========================================================

    def build_ui(self):
        if self.layout() is None:
            root = QVBoxLayout(
                self
            )
        else:
            root = self.layout()

            self.clear_layout(
                root
            )

        root.setContentsMargins(
            30,
            26,
            30,
            24,
        )

        root.setSpacing(
            18
        )

        # ====================================================
        # HEADER CARD
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
            21,
            24,
            21,
        )

        header_layout.setSpacing(
            7
        )

        title = QLabel(
            self.title_text
        )

        title.setObjectName(
            "overviewTitle"
        )

        subtitle = QLabel(
            self.subtitle_text
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

        # ====================================================
        # SCROLL
        # ====================================================

        scroll = QScrollArea()

        scroll.setWidgetResizable(
            True
        )

        scroll.setObjectName(
            "overviewScroll"
        )

        content = QWidget()

        content.setObjectName(
            "overviewContent"
        )

        content_layout = QVBoxLayout(
            content
        )

        content_layout.setContentsMargins(
            0,
            0,
            8,
            20,
        )

        content_layout.setSpacing(
            13
        )

        levels = get_learning_overview(
            self.user["id"]
        )

        if self.level_codes:
            allowed = set(
                self.level_codes
            )

            levels = [
                level
                for level in levels
                if level.get(
                    "code"
                ) in allowed
            ]

        for level in levels:
            content_layout.addWidget(
                self.create_level_card(
                    level
                )
            )

        content_layout.addStretch()

        scroll.setWidget(
            content
        )

        root.addWidget(
            scroll,
            1,
        )

    # ========================================================
    # LEVEL CARD
    # ========================================================

    def create_level_card(
        self,
        level: dict,
    ):
        card = QFrame()

        card.setObjectName(
            "levelOverviewCard"
        )

        layout = QHBoxLayout(
            card
        )

        layout.setContentsMargins(
            22,
            19,
            22,
            19,
        )

        layout.setSpacing(
            22
        )

        # ====================================================
        # LEFT
        # ====================================================

        left = QVBoxLayout()

        left.setSpacing(
            6
        )

        code = (
            level.get(
                "code",
                "",
            )
            .replace(
                "LEVEL_",
                "BOSQICH ",
            )
        )

        level_code = QLabel(
            code
        )

        level_code.setObjectName(
            "levelCode"
        )

        level_name = QLabel(
            level.get(
                "title",
                "",
            )
        )

        level_name.setObjectName(
            "levelName"
        )

        desc = QLabel(
            level.get(
                "subtitle",
                "",
            )
            or ""
        )

        desc.setObjectName(
            "levelDesc"
        )

        desc.setWordWrap(
            True
        )

        left.addWidget(
            level_code
        )

        left.addWidget(
            level_name
        )

        left.addWidget(
            desc
        )

        layout.addLayout(
            left,
            5,
        )

        # ====================================================
        # CENTER — PROGRESS
        # ====================================================

        center = QVBoxLayout()

        center.setSpacing(
            7
        )

        completed = int(
            level.get(
                "completed_lessons",
                0,
            )
            or 0
        )

        total = int(
            level.get(
                "total_lessons",
                0,
            )
            or 0
        )

        percent = (
            round(
                completed
                / total
                * 100
            )
            if total
            else 0
        )

        progress_text = QLabel(
            f"{completed} / {total} dars"
        )

        progress_text.setObjectName(
            "progressText"
        )

        progress = QProgressBar()

        progress.setRange(
            0,
            100,
        )

        progress.setValue(
            percent
        )

        progress.setTextVisible(
            False
        )

        center.addWidget(
            progress_text
        )

        center.addWidget(
            progress
        )

        layout.addLayout(
            center,
            2,
        )

        # ====================================================
        # RIGHT
        # ====================================================

        right = QVBoxLayout()

        right.setSpacing(
            8
        )

        status = level.get(
            "level_status",
            "locked",
        )

        if self.is_master:
            status_text = (
                "★ MASTER"
            )

            status_object = (
                "statusBadgeMaster"
            )

        elif status == "completed":
            status_text = (
                "✓ TUGALLANGAN"
            )

            status_object = (
                "statusBadgeCompleted"
            )

        elif status == "locked":
            status_text = (
                "🔒 YOPIQ"
            )

            status_object = (
                "statusBadgeLocked"
            )

        else:
            status_text = (
                "● OCHIQ"
            )

            status_object = (
                "statusBadgeAvailable"
            )

        badge = QLabel(
            status_text
        )

        badge.setObjectName(
            status_object
        )

        button = QPushButton(
            "BOSQICHNI KO'RISH  →"
        )

        button.setObjectName(
            "openLevelButton"
        )

        # PRO foydalanuvchi yopiq Level tarkibini
        # KO'RISHI mumkin.
        # Ammo darslar LearningWindow lock qoidasi
        # bo'yicha ochilmaydi.

        level_code_value = level.get(
            "code",
            "",
        )

        level_title_value = level.get(
            "title",
            "",
        )

        level_subtitle_value = (
            level.get(
                "subtitle",
                "",
            )
            or ""
        )

        button.clicked.connect(
            lambda checked=False,
            c=level_code_value,
            t=level_title_value,
            s=level_subtitle_value:
            self.open_level_requested.emit(
                c,
                t,
                s,
            )
        )

        right.addWidget(
            badge
        )

        right.addWidget(
            button
        )

        layout.addLayout(
            right,
            2,
        )

        return card

    # ========================================================
    # REFRESH
    # ========================================================

    def refresh_page(self):
        self.build_ui()
