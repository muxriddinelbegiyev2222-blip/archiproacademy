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

from courses.user_features import (
    get_bookmarked_lesson_ids,
    get_user_notes_map,
)


class LibraryPage(QWidget):
    open_level_requested = Signal(
        str,
        str,
        str,
    )

    open_lesson_requested = Signal(
        dict
    )

    MAX_VISIBLE_RESULTS = 50

    def __init__(
        self,
        user: dict,
    ):
        super().__init__()

        self.user = user
        self.is_master = (
            str(
                user.get(
                    "license_type",
                    "",
                )
            ).upper()
            == "MASTER"
        )

        self.lesson_index = []
        self.bookmarked_ids = set()
        self.notes_map = {}
        self.only_bookmarks = False
        self.only_notes = False

        self.result_layout = None
        self.result_info = None

        self.reload_index()
        self.build_ui()

    def reload_index(self):
        self.bookmarked_ids = (
            get_bookmarked_lesson_ids(
                self.user["id"]
            )
        )

        self.notes_map = (
            get_user_notes_map(
                self.user["id"]
            )
        )

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
                    item = dict(
                        lesson
                    )

                    item.update(
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
                            "module_code": module.get(
                                "code",
                                "",
                            ),
                            "bookmarked": (
                                int(
                                    lesson.get(
                                        "id",
                                        0,
                                    )
                                )
                                in self.bookmarked_ids
                            ),
                            "note_text": self.notes_map.get(
                                int(
                                    lesson.get(
                                        "id",
                                        0,
                                    )
                                ),
                                "",
                            ),
                        }
                    )

                    result.append(
                        item
                    )

        self.lesson_index = result

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
            "Kutubxona va global qidiruv"
        )
        title.setObjectName(
            "overviewTitle"
        )

        subtitle = QLabel(
            "680 dars ichidan Level, modul, dars nomi, "
            "kod va qisqa mazmun bo'yicha tez qidiring. "
            "Ctrl+K bilan shu sahifani tez ochish mumkin."
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
        search_layout.setSpacing(
            10
        )

        label = QLabel(
            "Global qidiruv"
        )
        label.setObjectName(
            "levelCode"
        )

        controls = QHBoxLayout()
        controls.setSpacing(
            10
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

        self.bookmark_button = QPushButton(
            "★ FAQAT BOOKMARKLAR"
        )
        self.bookmark_button.setObjectName(
            "openLevelButton"
        )
        self.bookmark_button.setCheckable(
            True
        )
        self.bookmark_button.toggled.connect(
            self.toggle_bookmarks
        )

        self.notes_button = QPushButton(
            "✎ FAQAT ESLATMALAR"
        )
        self.notes_button.setObjectName(
            "openLevelButton"
        )
        self.notes_button.setCheckable(
            True
        )
        self.notes_button.toggled.connect(
            self.toggle_notes
        )

        controls.addWidget(
            self.search_input,
            1,
        )
        controls.addWidget(
            self.bookmark_button
        )
        controls.addWidget(
            self.notes_button
        )

        search_layout.addWidget(
            label
        )
        search_layout.addLayout(
            controls
        )

        root.addWidget(
            search_card
        )

        self.result_info = QLabel()
        self.result_info.setObjectName(
            "progressText"
        )

        root.addWidget(
            self.result_info
        )

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

    def focus_search(self):
        self.search_input.setFocus()
        self.search_input.selectAll()

    def toggle_bookmarks(
        self,
        enabled: bool,
    ):
        self.only_bookmarks = bool(
            enabled
        )

        self.update_results(
            self.search_input.text()
        )

    def toggle_notes(
        self,
        enabled: bool,
    ):
        self.only_notes = bool(
            enabled
        )

        self.update_results(
            self.search_input.text()
        )

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
            str(
                text
                or ""
            )
            .strip()
            .lower()
        )

        self.clear_results()

        matches = []

        for item in self.lesson_index:
            if (
                self.only_bookmarks
                and not item.get(
                    "bookmarked"
                )
            ):
                continue

            if (
                self.only_notes
                and not str(
                    item.get(
                        "note_text",
                        "",
                    )
                ).strip()
            ):
                continue

            haystack = " ".join(
                [
                    str(
                        item.get(
                            "title",
                            "",
                        )
                    ),
                    str(
                        item.get(
                            "summary",
                            "",
                        )
                    ),
                    str(
                        item.get(
                            "code",
                            "",
                        )
                    ),
                    str(
                        item.get(
                            "module_title",
                            "",
                        )
                    ),
                    str(
                        item.get(
                            "module_code",
                            "",
                        )
                    ),
                    str(
                        item.get(
                            "level_title",
                            "",
                        )
                    ),
                    str(
                        item.get(
                            "level_code",
                            "",
                        )
                    ),
                    str(
                        item.get(
                            "note_text",
                            "",
                        )
                    ),
                ]
            ).lower()

            if (
                not query
                or query in haystack
            ):
                matches.append(
                    item
                )

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

        title_text = str(
            item.get(
                "title",
                "Dars",
            )
        )

        if item.get(
            "bookmarked"
        ):
            title_text = (
                "★ "
                + title_text
            )

        lesson_title = QLabel(
            title_text
        )
        lesson_title.setObjectName(
            "levelName"
        )
        lesson_title.setWordWrap(
            True
        )

        readable_level = (
            str(
                item.get(
                    "level_code",
                    "",
                )
            )
            .replace(
                "LEVEL_",
                "LEVEL ",
            )
        )

        status = str(
            item.get(
                "status",
                "locked",
            )
        )

        meta = QLabel(
            f"{readable_level}"
            f"  •  "
            f"{item.get('module_title', '')}"
            f"  •  "
            f"{item.get('estimated_minutes', 0)} daqiqa"
            f"  •  "
            f"{status.upper()}"
        )
        meta.setObjectName(
            "levelDesc"
        )
        meta.setWordWrap(
            True
        )

        text_area.addWidget(
            lesson_title
        )
        text_area.addWidget(
            meta
        )

        note_text = str(
            item.get(
                "note_text",
                "",
            )
            or ""
        ).strip()

        if note_text:
            preview = note_text.replace(
                "\n",
                " ",
            )

            if len(
                preview
            ) > 120:
                preview = (
                    preview[:117]
                    + "..."
                )

            note_label = QLabel(
                "✎ "
                + preview
            )
            note_label.setObjectName(
                "progressText"
            )
            note_label.setWordWrap(
                True
            )

            text_area.addWidget(
                note_label
            )

        layout.addLayout(
            text_area,
            1,
        )

        can_open = (
            self.is_master
            or status
            in {
                "available",
                "completed",
            }
        )

        if can_open:
            button = QPushButton(
                "DARSNI OCHISH  →"
            )
            button.setObjectName(
                "openLevelButton"
            )
            button.clicked.connect(
                lambda checked=False,
                data=dict(
                    item
                ):
                self.open_lesson_requested.emit(
                    data
                )
            )

        else:
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
