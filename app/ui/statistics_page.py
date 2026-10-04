from PySide6.QtCore import Signal

from PySide6.QtWidgets import (
    QFrame,
    QGridLayout,
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
    get_user_course_stats,
)


class StatisticsPage(QWidget):
    open_level_requested = Signal(
        str,
        str,
        str,
    )

    def __init__(
        self,
        user: dict,
    ):
        super().__init__()

        self.user = user

        self.setObjectName(
            "statisticsPage"
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
            "Statistika"
        )

        title.setObjectName(
            "overviewTitle"
        )

        subtitle = QLabel(
            "O'qish jarayoningiz, Bosqich progressi, "
            "XP va tugallangan darslar holati."
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

        stats = get_user_course_stats(
            self.user["id"]
        )

        levels = get_learning_overview(
            self.user["id"]
        )

        # ====================================================
        # MAIN STATS
        # ====================================================

        grid = QGridLayout()

        grid.setSpacing(
            13
        )

        completed_levels = sum(
            1
            for level in levels
            if level.get(
                "level_status"
            ) == "completed"
        )

        values = [
            (
                "UMUMIY PROGRESS",
                f"{stats['progress_percent']}%",
            ),
            (
                "TUGALLANGAN DARSLAR",
                (
                    f"{stats['completed_lessons']} / "
                    f"{stats['total_lessons']}"
                ),
            ),
            (
                "TUGALLANGAN LEVEL",
                f"{completed_levels} / {len(levels)}",
            ),
            (
                "JAMI XP",
                str(
                    stats["xp"]
                ),
            ),
        ]

        for index, (
            label_text,
            value_text,
        ) in enumerate(
            values
        ):
            card = QFrame()

            card.setObjectName(
                "levelOverviewCard"
            )

            card_layout = QVBoxLayout(
                card
            )

            card_layout.setContentsMargins(
                20,
                18,
                20,
                18,
            )

            label = QLabel(
                label_text
            )

            label.setObjectName(
                "levelCode"
            )

            value = QLabel(
                value_text
            )

            value.setObjectName(
                "levelName"
            )

            card_layout.addWidget(
                label
            )

            card_layout.addWidget(
                value
            )

            grid.addWidget(
                card,
                index // 2,
                index % 2,
            )

        root.addLayout(
            grid
        )

        # ====================================================
        # LEVEL PROGRESS
        # ====================================================

        section_title = QLabel(
            "Bosqich bo'yicha progress"
        )

        section_title.setObjectName(
            "levelName"
        )

        root.addWidget(
            section_title
        )

        scroll = QScrollArea()

        scroll.setWidgetResizable(
            True
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
            10
        )

        for level in levels:
            content_layout.addWidget(
                self.create_level_row(
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
    # LEVEL ROW
    # ========================================================

    def create_level_row(
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
            18,
            15,
            18,
            15,
        )

        layout.setSpacing(
            18
        )

        # ----------------------------------------------------
        # TEXT
        # ----------------------------------------------------

        text_area = QVBoxLayout()

        readable = (
            level.get(
                "code",
                "",
            )
            .replace(
                "LEVEL_",
                "BOSQICH ",
            )
        )

        title = QLabel(
            f"{readable}  •  "
            f"{level.get('title', '')}"
        )

        title.setObjectName(
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

        text_area.addWidget(
            title
        )

        text_area.addWidget(
            desc
        )

        layout.addLayout(
            text_area,
            4,
        )

        # ----------------------------------------------------
        # PROGRESS
        # ----------------------------------------------------

        progress_area = QVBoxLayout()

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
            int(
                completed
                / total
                * 100
            )
            if total
            else 0
        )

        progress_text = QLabel(
            f"{completed}/{total} dars  •  {percent}%"
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

        progress_area.addWidget(
            progress_text
        )

        progress_area.addWidget(
            progress
        )

        layout.addLayout(
            progress_area,
            2,
        )

        # ----------------------------------------------------
        # OPEN
        # ----------------------------------------------------

        button = QPushButton(
            "KO'RISH  →"
        )

        button.setObjectName(
            "openLevelButton"
        )

        code = level.get(
            "code",
            "",
        )

        level_title = level.get(
            "title",
            "",
        )

        subtitle = level.get(
            "subtitle",
            "",
        )

        button.clicked.connect(
            lambda checked=False,
            c=code,
            t=level_title,
            s=subtitle:
            self.open_level_requested.emit(
                c,
                t,
                s or "",
            )
        )

        layout.addWidget(
            button
        )

        return card

    def refresh_page(self):
        self.build_ui()
