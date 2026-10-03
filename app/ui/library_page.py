from PySide6.QtCore import Signal

from PySide6.QtWidgets import (
    QFrame,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QScrollArea,
    QVBoxLayout,
    QWidget,
)

from courses.course_service import (
    get_learning_overview,
)


class LibraryPage(QWidget):
    open_level_requested = Signal(
        str,
        str,
        str,
    )

    MAX_VISIBLE_RESULTS = 50

    def __init__(
        self,
        user: dict,
    ):
        super().__init__()

        self.user = user

        self.lesson_index = []

        self.result_layout = None
        self.result_info = None

        self.build_index()

        self.build_ui()

    # ========================================================
    # INDEX
    # ========================================================

    def build_index(self):
        levels = get_learning_overview(
            self.user["id"]
        )

        result = []

        for level in levels:
            for module in level.get(
                "modules",
                [],
            ):
                for lesson in module.get(
                    "lessons",
                    [],
                ):
                    result.append(
                        {
                            "level_code": level.get(
                                "code",
                                "",
                            ),
                            "level_title": level.get(
                                "title",
                                "",
                            ),
                            "level_subtitle": level.get(
                                "subtitle",
                                "",
                            ),
                            "module_title": module.get(
                                "title",
                                "",
                            ),
                            "lesson_title": lesson.get(
                                "title",
                                "",
                            ),
                            "lesson_type": lesson.get(
                                "lesson_type",
                                "",
                            ),
                            "minutes": lesson.get(
                                "estimated_minutes",
                                0,
                            ),
                            "status": lesson.get(
                                "status",
                                "locked",
                            ),
                        }
                    )

        self.lesson_index = result

    # ========================================================
    # UI
    # ========================================================

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
            "Kutubxona"
        )

        title.setObjectName(
            "overviewTitle"
        )

        subtitle = QLabel(
            "ARCHIPRO UZ dagi barcha darslarni "
            "tez qidirish markazi."
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
        # SEARCH
        # ====================================================

        search_card = QFrame()

        search_card.setObjectName(
            "levelOverviewCard"
        )

        search_layout = QVBoxLayout(
            search_card
        )

        search_layout.setContentsMargins(
            18,
            15,
            18,
            15,
        )

        label = QLabel(
            "Dars, modul yoki Level nomini qidiring"
        )

        label.setObjectName(
            "levelCode"
        )

        self.search_input = QLineEdit()

        self.search_input.setPlaceholderText(
            "Masalan: fasad, Archicad, fundament, genplan..."
        )

        self.search_input.setClearButtonEnabled(
            True
        )

        self.search_input.setStyleSheet(
            """
            QLineEdit {
                background-color: #0A1627;
                border: 1px solid #304763;
                border-radius: 10px;
                padding: 11px 14px;
                color: #E7EEF7;
                font-size: 14px;
            }

            QLineEdit:focus {
                border: 1px solid #4F86EB;
            }
            """
        )

        self.search_input.textChanged.connect(
            self.update_results
        )

        search_layout.addWidget(
            label
        )

        search_layout.addWidget(
            self.search_input
        )

        root.addWidget(
            search_card
        )

        # ====================================================
        # RESULT INFO
        # ====================================================

        self.result_info = QLabel()

        self.result_info.setObjectName(
            "progressText"
        )

        root.addWidget(
            self.result_info
        )

        # ====================================================
        # RESULTS
        # ====================================================

        scroll = QScrollArea()

        scroll.setWidgetResizable(
            True
        )

        content = QWidget()

        content.setObjectName(
            "overviewContent"
        )

        self.result_layout = QVBoxLayout(
            content
        )

        self.result_layout.setContentsMargins(
            0,
            0,
            8,
            20,
        )

        self.result_layout.setSpacing(
            9
        )

        scroll.setWidget(
            content
        )

        root.addWidget(
            scroll,
            1,
        )

        self.update_results(
            ""
        )

    # ========================================================
    # RESULT
    # ========================================================

    def clear_results(self):
        while self.result_layout.count():
            item = self.result_layout.takeAt(
                0
            )

            widget = item.widget()

            if widget is not None:
                widget.deleteLater()

    def update_results(
        self,
        text: str,
    ):
        query = (
            text.strip().lower()
        )

        self.clear_results()

        if query:
            matches = [
                item
                for item in self.lesson_index
                if (
                    query
                    in item[
                        "lesson_title"
                    ].lower()
                    or query
                    in item[
                        "module_title"
                    ].lower()
                    or query
                    in item[
                        "level_title"
                    ].lower()
                    or query
                    in item[
                        "level_code"
                    ].lower()
                )
            ]

        else:
            matches = self.lesson_index

        visible = matches[
            :self.MAX_VISIBLE_RESULTS
        ]

        self.result_info.setText(
            f"Topildi: {len(matches)} ta"
            + (
                f"  •  dastlabki "
                f"{len(visible)} tasi ko'rsatilmoqda"
                if len(matches)
                > self.MAX_VISIBLE_RESULTS
                else ""
            )
        )

        for item in visible:
            self.result_layout.addWidget(
                self.create_result_card(
                    item
                )
            )

        if not visible:
            empty = QLabel(
                "Mos dars topilmadi."
            )

            empty.setObjectName(
                "overviewSubtitle"
            )

            self.result_layout.addWidget(
                empty
            )

        self.result_layout.addStretch()

    # ========================================================
    # CARD
    # ========================================================

    def create_result_card(
        self,
        item: dict,
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
            14,
            18,
            14,
        )

        layout.setSpacing(
            16
        )

        text_area = QVBoxLayout()

        lesson_title = QLabel(
            item[
                "lesson_title"
            ]
        )

        lesson_title.setObjectName(
            "levelName"
        )

        readable_level = (
            item[
                "level_code"
            ]
            .replace(
                "LEVEL_",
                "LEVEL ",
            )
        )

        meta = QLabel(
            f"{readable_level}"
            f"  •  "
            f"{item['module_title']}"
            f"  •  "
            f"{item['minutes']} daqiqa"
        )

        meta.setObjectName(
            "levelDesc"
        )

        text_area.addWidget(
            lesson_title
        )

        text_area.addWidget(
            meta
        )

        layout.addLayout(
            text_area,
            1,
        )

        button = QPushButton(
            "LEVELGA O'TISH  →"
        )

        button.setObjectName(
            "openLevelButton"
        )

        button.clicked.connect(
            lambda checked=False,
            data=item:
            self.open_level_requested.emit(
                data[
                    "level_code"
                ],
                data[
                    "level_title"
                ],
                data[
                    "level_subtitle"
                ],
            )
        )

        layout.addWidget(
            button
        )

        return card
