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

from courses.course_service import (
    get_learning_overview,
)

from courses.exam_service import (
    are_all_level_lessons_completed,
    get_level_exam,
    get_level_exam_stats,
)


class ExamsPage(QWidget):
    open_exam_requested = Signal(
        dict
    )

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

        self.setObjectName(
            "examsPage"
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
            QWidget#examsPage {
                background-color: #F5F1E7;
            }

            QScrollArea,
            QAbstractScrollArea::viewport {
                background-color: #F5F1E7;
                border: none;
            }

            QWidget#examsContent {
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

            QFrame#examCard {
                background-color: #FFFDF7;
                border: 1px solid #D5CBBB;
                border-radius: 14px;
            }

            QFrame#examReady {
                background-color: #F5F1E7;
                border: 1px solid #D5CBBB;
                border-radius: 14px;
            }

            QFrame#examDone {
                background-color: #F5F1E7;
                border: 1px solid #D5CBBB;
                border-radius: 14px;
            }

            QLabel#examTitle {
                color: #203B36;
                font-size: 20px;
                font-weight: 750;
            
                font-family: "Georgia";
}

            QLabel#meta {
                color: #203B36;
                font-size: 14px;
            }

            QLabel#locked {
                color: #586B64;
                font-size: 14px;
                font-weight: 650;
            }

            QLabel#ready {
                color: #A65D35;
                font-size: 14px;
                font-weight: 700;
            }

            QLabel#done {
                color: #27624A;
                font-size: 14px;
                font-weight: 700;
            }

            QPushButton#examButton {
                background-color: #A65D35;
                color: white;
                border: none;
                border-radius: 9px;
                padding: 12px 18px;
                font-size: 14px;
                font-weight: 800;
            }

            QPushButton#examButton:hover {
                background-color: #A65D35;
            }
            """
        )

        title = QLabel(
            "Imtihonlar"
        )

        title.setObjectName(
            "pageTitle"
        )

        root.addWidget(
            title
        )

        subtitle = QLabel(
            "Har bir Bosqich yakuniy imtihoni "
            "faqat shu Bosqichdagi barcha majburiy "
            "darslar tugallangandan keyin ochiladi. "
            "MASTER rejimi faqat administrator "
            "testi uchun."
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
            "examsContent"
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
            exam = get_level_exam(
                level.get(
                    "code",
                    "",
                )
            )

            if not exam:
                continue

            stats = get_level_exam_stats(
                self.user["id"],
                level.get(
                    "code",
                    "",
                ),
            )

            completed = (
                stats.get(
                    "status"
                )
                == "completed"
            )

            lessons_done = (
                are_all_level_lessons_completed(
                    self.user["id"],
                    level["id"],
                )
            )

            level_locked = (
                level.get(
                    "level_status",
                    "locked",
                )
                == "locked"
            )

            ready = (
                self.is_master
                or (
                    lessons_done
                    and not level_locked
                )
            )

            card = QFrame()

            if completed:
                card.setObjectName(
                    "examDone"
                )

            elif ready:
                card.setObjectName(
                    "examReady"
                )

            else:
                card.setObjectName(
                    "examCard"
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

            title_label = QLabel(
                f"{readable} — YAKUNIY IMTIHON"
            )

            title_label.setObjectName(
                "examTitle"
            )

            text_area.addWidget(
                title_label
            )

            meta = QLabel(
                f"{exam.get('question_count', 0)} ta savol"
                f"   •   Talab: "
                f"{exam.get('passing_score', 0)}%"
                f"   •   +"
                f"{exam.get('xp_reward', 0)} XP"
            )

            meta.setObjectName(
                "meta"
            )

            text_area.addWidget(
                meta
            )

            if completed:
                state = QLabel(
                    "✓ Tugallangan"
                    f"   •   Eng yaxshi natija: "
                    f"{stats.get('best_exam_score', 0)}%"
                    f"   •   Urinishlar: "
                    f"{stats.get('exam_attempts', 0)}"
                )

                state.setObjectName(
                    "done"
                )

            elif self.is_master:
                state = QLabel(
                    "★ MASTER ACCESS — "
                    "tekshirish uchun imtihon ochiq"
                )

                state.setObjectName(
                    "ready"
                )

            elif level_locked:
                state = QLabel(
                    "🔒 Avval oldingi Bosqichni "
                    "muvaffaqiyatli yakunlang"
                )

                state.setObjectName(
                    "locked"
                )

            elif not lessons_done:
                remaining = max(
                    0,
                    int(
                        level.get(
                            "total_lessons",
                            0,
                        )
                    )
                    -
                    int(
                        level.get(
                            "completed_lessons",
                            0,
                        )
                    ),
                )

                state = QLabel(
                    "🔒 Imtihon ochilishi uchun "
                    f"yana {remaining} ta darsni tugating"
                )

                state.setObjectName(
                    "locked"
                )

            else:
                state = QLabel(
                    "✓ Barcha majburiy darslar "
                    "tugallandi — imtihon ochiq"
                )

                state.setObjectName(
                    "ready"
                )

            text_area.addWidget(
                state
            )

            card_layout.addLayout(
                text_area,
                1,
            )

            if (
                ready
                and not completed
            ):
                button = QPushButton(
                    "IMTIHONNI BOSHLASH  →"
                )

                button.setObjectName(
                    "examButton"
                )

                exam_data = dict(
                    exam
                )

                button.clicked.connect(
                    lambda checked=False,
                    data=exam_data:
                    self.open_exam_requested.emit(
                        data
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
