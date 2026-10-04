from PySide6.QtCore import Signal
from PySide6.QtWidgets import (
    QFrame,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QScrollArea,
    QVBoxLayout,
    QWidget,
)

from courses.course_service import get_learning_overview


class TestsPage(QWidget):
    open_level_requested = Signal(
        list,
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
            "testsPage"
        )

        self.build_ui()

    def _clear_layout(
        self,
        layout,
    ):
        while layout.count():
            item = layout.takeAt(
                0
            )

            widget = item.widget()
            child_layout = (
                item.layout()
            )

            if widget is not None:
                widget.deleteLater()

            elif child_layout is not None:
                self._clear_layout(
                    child_layout
                )

    def build_ui(self):
        if self.layout() is None:
            root = QVBoxLayout(
                self
            )
        else:
            root = self.layout()

            self._clear_layout(
                root
            )

        root.setContentsMargins(
            34,
            30,
            34,
            24,
        )

        root.setSpacing(
            16
        )

        self.setStyleSheet(
            """
            QWidget#testsPage {
                background-color: #F5F1E7;
            }

            QScrollArea,
            QAbstractScrollArea::viewport {
                background-color: #F5F1E7;
                border: none;
            }

            QWidget#testsContent {
                background-color: #F5F1E7;
            }

            QLabel#pageTitle {
                color: #203B36;
                font-size: 32px;
                font-weight: 800;
            
                font-family: "Georgia";
}

            QLabel#pageSubtitle {
                color: #586B64;
                font-size: 16px;
            }

            QFrame#testCard {
                background-color: #FFFDF7;
                border: 1px solid #D5CBBB;
                border-radius: 14px;
            }

            QLabel#levelTitle {
                color: #203B36;
                font-size: 20px;
                font-weight: 750;
            
                font-family: "Georgia";
}

            QLabel#levelSubtitle {
                color: #586B64;
                font-size: 15px;
            }

            QLabel#stats {
                color: #203B36;
                font-size: 14px;
            }

            QLabel#statusOpen {
                color: #0E5558;
                font-size: 14px;
                font-weight: 700;
            }

            QLabel#statusLocked {
                color: #586B64;
                font-size: 14px;
                font-weight: 650;
            }

            QLabel#statusDone {
                color: #27624A;
                font-size: 14px;
                font-weight: 700;
            }

            QPushButton#openButton {
                background-color: #0E5558;
                color: white;
                border: none;
                border-radius: 9px;
                padding: 12px 18px;
                font-size: 14px;
                font-weight: 700;
            }

            QPushButton#openButton:hover {
                background-color: #0E5558;
            }
            """
        )

        title = QLabel(
            "Testlar"
        )

        title.setObjectName(
            "pageTitle"
        )

        root.addWidget(
            title
        )

        subtitle = QLabel(
            "Mini-testlar har bir darsga biriktirilgan. "
            "Testga dars ichidan kiriladi; shu sabab "
            "o'quv ketma-ketligi va qulflar buzilmaydi."
        )

        subtitle.setObjectName(
            "pageSubtitle"
        )

        subtitle.setWordWrap(
            True
        )

        root.addWidget(
            subtitle
        )

        scroll = QScrollArea()

        scroll.setWidgetResizable(
            True
        )

        content = QWidget()

        content.setObjectName(
            "testsContent"
        )

        content_layout = QVBoxLayout(
            content
        )

        content_layout.setContentsMargins(
            0,
            4,
            8,
            20,
        )

        content_layout.setSpacing(
            12
        )

        levels = get_learning_overview(
            self.user["id"]
        )

        for level in levels:
            total = int(
                level.get(
                    "total_lessons",
                    0,
                )
                or 0
            )

            completed = int(
                level.get(
                    "completed_lessons",
                    0,
                )
                or 0
            )

            available = 0
            locked = 0

            for module in level.get(
                "modules",
                [],
            ):
                for lesson in module.get(
                    "lessons",
                    [],
                ):
                    status = lesson.get(
                        "status",
                        "locked",
                    )

                    if status == "available":
                        available += 1

                    elif status == "locked":
                        locked += 1

            card = QFrame()

            card.setObjectName(
                "testCard"
            )

            card_layout = QHBoxLayout(
                card
            )

            card_layout.setContentsMargins(
                20,
                18,
                20,
                18,
            )

            card_layout.setSpacing(
                18
            )

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

            level_title = QLabel(
                f"{readable}  •  "
                f"{level.get('title', '')}"
            )

            level_title.setObjectName(
                "levelTitle"
            )

            text_area.addWidget(
                level_title
            )

            desc = QLabel(
                level.get(
                    "subtitle",
                    "",
                )
                or "Dars mini-testlari"
            )

            desc.setObjectName(
                "levelSubtitle"
            )

            desc.setWordWrap(
                True
            )

            text_area.addWidget(
                desc
            )

            stats = QLabel(
                f"Jami mini-test: {total}"
                f"   •   Tugallangan: {completed}"
                f"   •   Hozir ochiq: {available}"
                f"   •   Qulflangan: {locked}"
            )

            stats.setObjectName(
                "stats"
            )

            text_area.addWidget(
                stats
            )

            if (
                completed == total
                and total > 0
            ):
                status_label = QLabel(
                    "✓ Ushbu Bosqich dars "
                    "testlari tugallangan"
                )

                status_label.setObjectName(
                    "statusDone"
                )

            elif available > 0:
                status_label = QLabel(
                    "▶ Keyingi mini-testga "
                    "dars ichidan kirish mumkin"
                )

                status_label.setObjectName(
                    "statusOpen"
                )

            else:
                status_label = QLabel(
                    "🔒 Testlar o'quv "
                    "ketma-ketligi bo'yicha ochiladi"
                )

                status_label.setObjectName(
                    "statusLocked"
                )

            text_area.addWidget(
                status_label
            )

            card_layout.addLayout(
                text_area,
                1,
            )

            button = QPushButton(
                "BOSQICH DARSLARI VA TESTLARI  →"
            )

            button.setObjectName(
                "openButton"
            )

            code = level.get(
                "code",
                "",
            )

            button.clicked.connect(
                lambda checked=False,
                c=code,
                t=readable,
                lt=level.get(
                    "title",
                    "",
                ):
                self.open_level_requested.emit(
                    [c],
                    f"{t} — Testlar",
                    (
                        f"{lt}. Mini-testlar "
                        "dars yakunida ochiladi."
                    ),
                )
            )

            card_layout.addWidget(
                button
            )

            content_layout.addWidget(
                card
            )

        content_layout.addStretch()

        scroll.setWidget(
            content
        )

        root.addWidget(
            scroll,
            1,
        )

    def refresh_page(self):
        self.build_ui()
