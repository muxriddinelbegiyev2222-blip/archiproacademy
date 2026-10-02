from PySide6.QtCore import Qt

from PySide6.QtWidgets import (
    QFrame,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QScrollArea,
    QVBoxLayout,
    QWidget,
)

from courses.course_service import (
    complete_lesson,
    get_learning_overview,
)

from courses.exam_service import (
    are_all_level_lessons_completed,
    get_level_exam,
    get_level_exam_stats,
)

from ui.exam_window import (
    ExamWindow,
)

from ui.lesson_window import (
    LessonWindow,
)


class LearningWindow(QMainWindow):
    def __init__(
        self,
        user: dict,
    ):
        super().__init__()

        self.user = user

        self.lesson_window = None
        self.exam_window = None

        self.setWindowTitle(
            "ARCHIPRO UZ - Mening o'qishim"
        )

        self.resize(
            1350,
            850,
        )

        self.setMinimumSize(
            950,
            650,
        )

        self.setup_styles()

        self.reload_data()

        self.build_ui()

    # ========================================================
    # STYLE
    # ========================================================

    def setup_styles(self):
        self.setStyleSheet(
            """
            QMainWindow {
                background-color: #0B1220;
            }

            QWidget {
                font-family: Segoe UI;
                color: #F8FAFC;
            }

            QScrollArea {
                background-color: transparent;
                border: none;
            }

            QLabel#pageTitle {
                font-size: 30px;
                font-weight: 700;
                color: white;
            }

            QLabel#pageSubtitle {
                font-size: 14px;
                color: #94A3B8;
            }

            QFrame#levelCard {
                background-color: #0F172A;
                border: 1px solid #1E293B;
                border-radius: 16px;
            }

            QFrame#levelLocked {
                background-color: #0D1422;
                border: 1px solid #1E293B;
                border-radius: 16px;
            }

            QFrame#levelCompleted {
                background-color: #0E1D18;
                border: 1px solid #166534;
                border-radius: 16px;
            }

            QFrame#moduleCard {
                background-color: #111827;
                border: 1px solid #1E293B;
                border-radius: 12px;
            }

            QFrame#lessonAvailable {
                background-color: #12203A;
                border: 1px solid #2563EB;
                border-radius: 10px;
            }

            QFrame#lessonCompleted {
                background-color: #10251C;
                border: 1px solid #15803D;
                border-radius: 10px;
            }

            QFrame#lessonLocked {
                background-color: #111827;
                border: 1px solid #1E293B;
                border-radius: 10px;
            }

            QFrame#examAvailable {
                background-color: #2A2109;
                border: 1px solid #CA8A04;
                border-radius: 14px;
            }

            QFrame#examLocked {
                background-color: #111827;
                border: 1px solid #334155;
                border-radius: 14px;
            }

            QFrame#examCompleted {
                background-color: #10251C;
                border: 1px solid #16A34A;
                border-radius: 14px;
            }

            QLabel#levelTitle {
                font-size: 22px;
                font-weight: 700;
                color: white;
            }

            QLabel#levelSubtitle {
                font-size: 14px;
                color: #94A3B8;
            }

            QLabel#moduleTitle {
                font-size: 17px;
                font-weight: 700;
                color: white;
            }

            QLabel#lessonTitle {
                font-size: 14px;
                font-weight: 600;
                color: #E2E8F0;
            }

            QLabel#meta {
                font-size: 12px;
                color: #64748B;
            }

            QLabel#availableStatus {
                color: #60A5FA;
                font-size: 12px;
                font-weight: 700;
            }

            QLabel#completedStatus {
                color: #86EFAC;
                font-size: 12px;
                font-weight: 700;
            }

            QLabel#lockedStatus {
                color: #64748B;
                font-size: 12px;
                font-weight: 700;
            }

            QLabel#examTitle {
                font-size: 18px;
                font-weight: 700;
                color: #FDE68A;
            }

            QLabel#examCompletedTitle {
                font-size: 18px;
                font-weight: 700;
                color: #86EFAC;
            }

            QProgressBar {
                border: none;
                background-color: #1E293B;
                border-radius: 6px;
                height: 11px;
                color: transparent;
            }

            QProgressBar::chunk {
                background-color: #2563EB;
                border-radius: 6px;
            }

            QPushButton#openLesson {
                background-color: #2563EB;
                color: white;
                border: none;
                border-radius: 8px;
                padding: 9px 15px;
                font-weight: 600;
            }

            QPushButton#openLesson:hover {
                background-color: #3B82F6;
            }

            QPushButton#examButton {
                background-color: #CA8A04;
                color: #FFFFFF;
                border: none;
                border-radius: 9px;
                padding: 11px 18px;
                font-size: 13px;
                font-weight: 700;
            }

            QPushButton#examButton:hover {
                background-color: #EAB308;
            }

            QPushButton#backButton {
                background-color: #1E293B;
                color: white;
                border: none;
                border-radius: 8px;
                padding: 9px 15px;
            }

            QPushButton#backButton:hover {
                background-color: #334155;
            }
            """
        )

    # ========================================================
    # DATA
    # ========================================================

    def reload_data(self):
        self.levels = (
            get_learning_overview(
                self.user["id"]
            )
        )

    # ========================================================
    # BUILD UI
    # ========================================================

    def build_ui(self):
        central = QWidget()

        self.setCentralWidget(
            central
        )

        root = QVBoxLayout(
            central
        )

        root.setContentsMargins(
            30,
            24,
            30,
            24,
        )

        root.setSpacing(
            16
        )

        # ====================================================
        # TOP
        # ====================================================

        top = QHBoxLayout()

        back_button = QPushButton(
            "← ORQAGA"
        )

        back_button.setObjectName(
            "backButton"
        )

        back_button.clicked.connect(
            self.close
        )

        top.addWidget(
            back_button
        )

        top.addStretch()

        root.addLayout(
            top
        )

        title = QLabel(
            "Mening o'qishim"
        )

        title.setObjectName(
            "pageTitle"
        )

        subtitle = QLabel(
            (
                "0 dan professional turar joy "
                "loyihalashgacha bo'lgan o'quv yo'lingiz"
            )
        )

        subtitle.setObjectName(
            "pageSubtitle"
        )

        root.addWidget(
            title
        )

        root.addWidget(
            subtitle
        )

        # ====================================================
        # SCROLL
        # ====================================================

        scroll = QScrollArea()

        scroll.setWidgetResizable(
            True
        )

        scroll.setFrameShape(
            QScrollArea.Shape.NoFrame
        )

        content = QWidget()

        content_layout = QVBoxLayout(
            content
        )

        content_layout.setContentsMargins(
            0,
            8,
            12,
            30,
        )

        content_layout.setSpacing(
            18
        )

        for level in self.levels:

            level_card = (
                self.create_level_card(
                    level
                )
            )

            content_layout.addWidget(
                level_card
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

        level_status = level.get(
            "level_status",
            "locked",
        )

        if level_status == "completed":
            card.setObjectName(
                "levelCompleted"
            )

        elif level_status == "locked":
            card.setObjectName(
                "levelLocked"
            )

        else:
            card.setObjectName(
                "levelCard"
            )

        layout = QVBoxLayout(
            card
        )

        layout.setContentsMargins(
            22,
            20,
            22,
            20,
        )

        layout.setSpacing(
            13
        )

        # ====================================================
        # HEADER
        # ====================================================

        header = QHBoxLayout()

        title_area = QVBoxLayout()

        title = QLabel(
            f"{level['code']}  •  "
            f"{level['title']}"
        )

        title.setObjectName(
            "levelTitle"
        )

        subtitle = QLabel(
            level.get(
                "subtitle",
                "",
            )
        )

        subtitle.setObjectName(
            "levelSubtitle"
        )

        title_area.addWidget(
            title
        )

        title_area.addWidget(
            subtitle
        )

        header.addLayout(
            title_area
        )

        header.addStretch()

        if level_status == "completed":

            status_label = QLabel(
                "✓ TUGALLANGAN"
            )

            status_label.setObjectName(
                "completedStatus"
            )

        elif level_status == "available":

            status_label = QLabel(
                "▶ OCHIQ"
            )

            status_label.setObjectName(
                "availableStatus"
            )

        else:

            status_label = QLabel(
                "🔒 YOPIQ"
            )

            status_label.setObjectName(
                "lockedStatus"
            )

        header.addWidget(
            status_label
        )

        progress_text = QLabel(
            f"{level['completed_lessons']}/"
            f"{level['total_lessons']} dars"
        )

        progress_text.setObjectName(
            "meta"
        )

        header.addWidget(
            progress_text
        )

        layout.addLayout(
            header
        )

        progress = QProgressBar()

        progress.setRange(
            0,
            100,
        )

        progress.setValue(
            level[
                "progress_percent"
            ]
        )

        layout.addWidget(
            progress
        )

        # ====================================================
        # MODULES
        # ====================================================

        for module in level[
            "modules"
        ]:

            module_card = (
                self.create_module_card(
                    module=module,
                    level_status=level_status,
                )
            )

            layout.addWidget(
                module_card
            )

        # ====================================================
        # FINAL EXAM
        #
        # Endi LEVEL_00 bilan cheklanmaydi.
        # Database'da Final Exam mavjud bo'lsa ko'rsatiladi.
        # ====================================================

        exam = get_level_exam(
            level["code"]
        )

        if exam is not None:

            exam_card = (
                self.create_level_exam_card(
                    level=level,
                    exam=exam,
                )
            )

            layout.addWidget(
                exam_card
            )

        return card

    # ========================================================
    # MODULE CARD
    # ========================================================

    def create_module_card(
        self,
        module: dict,
        level_status: str,
    ):
        card = QFrame()

        card.setObjectName(
            "moduleCard"
        )

        layout = QVBoxLayout(
            card
        )

        layout.setContentsMargins(
            18,
            16,
            18,
            16,
        )

        layout.setSpacing(
            10
        )

        title = QLabel(
            module["title"]
        )

        title.setObjectName(
            "moduleTitle"
        )

        layout.addWidget(
            title
        )

        info = QLabel(
            f"{module['completed_lessons']}/"
            f"{module['total_lessons']} "
            "dars tugallangan"
        )

        info.setObjectName(
            "meta"
        )

        layout.addWidget(
            info
        )

        if not module[
            "lessons"
        ]:

            if level_status == "locked":

                no_lessons_text = (
                    "🔒 Ushbu Level hali yopiq."
                )

            else:

                no_lessons_text = (
                    "Bu modul darslari "
                    "keyingi bosqichda qo'shiladi."
                )

            no_lessons = QLabel(
                no_lessons_text
            )

            no_lessons.setObjectName(
                "meta"
            )

            layout.addWidget(
                no_lessons
            )

        for lesson in module[
            "lessons"
        ]:

            lesson_row = (
                self.create_lesson_row(
                    lesson
                )
            )

            layout.addWidget(
                lesson_row
            )

        return card

    # ========================================================
    # LESSON ROW
    # ========================================================

    def create_lesson_row(
        self,
        lesson: dict,
    ):
        status = lesson[
            "status"
        ]

        row = QFrame()

        if status == "completed":

            row.setObjectName(
                "lessonCompleted"
            )

            status_text = "✓"

        elif status == "available":

            row.setObjectName(
                "lessonAvailable"
            )

            status_text = "▶"

        else:

            row.setObjectName(
                "lessonLocked"
            )

            status_text = "🔒"

        layout = QHBoxLayout(
            row
        )

        layout.setContentsMargins(
            14,
            11,
            14,
            11,
        )

        status_label = QLabel(
            status_text
        )

        status_label.setFixedWidth(
            26
        )

        title_area = QVBoxLayout()

        title = QLabel(
            lesson["title"]
        )

        title.setObjectName(
            "lessonTitle"
        )

        meta = QLabel(
            f"{lesson['estimated_minutes']} daqiqa"
            f"   •   "
            f"{lesson['xp_reward']} XP"
        )

        meta.setObjectName(
            "meta"
        )

        title_area.addWidget(
            title
        )

        title_area.addWidget(
            meta
        )

        layout.addWidget(
            status_label
        )

        layout.addLayout(
            title_area
        )

        layout.addStretch()

        if status == "available":

            button = QPushButton(
                "OCHISH"
            )

            button.setObjectName(
                "openLesson"
            )

            button.clicked.connect(
                lambda checked=False, data=lesson:
                self.open_lesson(
                    data
                )
            )

            layout.addWidget(
                button
            )

        elif status == "completed":

            score = QLabel(
                f"Eng yaxshi test: "
                f"{lesson['best_score']}%"
            )

            score.setObjectName(
                "meta"
            )

            layout.addWidget(
                score
            )

        return row

    # ========================================================
    # EXAM CARD
    # ========================================================

    def create_level_exam_card(
        self,
        level: dict,
        exam: dict,
    ):
        card = QFrame()

        exam_stats = (
            get_level_exam_stats(
                self.user["id"],
                level["code"],
            )
        )

        lessons_completed = (
            are_all_level_lessons_completed(
                self.user["id"],
                level["id"],
            )
        )

        level_status = level.get(
            "level_status",
            "locked",
        )

        exam_completed = (
            exam_stats["status"]
            == "completed"
        )

        if exam_completed:

            card.setObjectName(
                "examCompleted"
            )

        elif (
            lessons_completed
            and level_status != "locked"
        ):

            card.setObjectName(
                "examAvailable"
            )

        else:

            card.setObjectName(
                "examLocked"
            )

        layout = QHBoxLayout(
            card
        )

        layout.setContentsMargins(
            18,
            16,
            18,
            16,
        )

        text_area = QVBoxLayout()

        level_number = (
            level["code"].replace(
                "LEVEL_",
                "",
            )
        )

        if exam_completed:

            title = QLabel(
                f"🏆 LEVEL {level_number} "
                "YAKUNIY IMTIHON — TUGALLANGAN"
            )

            title.setObjectName(
                "examCompletedTitle"
            )

        else:

            title = QLabel(
                f"🏆 LEVEL {level_number} "
                "YAKUNIY IMTIHON"
            )

            title.setObjectName(
                "examTitle"
            )

        details = QLabel(
            f"{exam['question_count']} ta savol"
            f"   •   "
            f"{exam['passing_score']}% talab"
            f"   •   "
            f"+{exam['xp_reward']} XP"
        )

        details.setObjectName(
            "meta"
        )

        text_area.addWidget(
            title
        )

        text_area.addWidget(
            details
        )

        if exam_completed:

            result = QLabel(
                f"Eng yaxshi natija: "
                f"{exam_stats['best_exam_score']}%"
                f"   •   "
                f"Urinishlar: "
                f"{exam_stats['exam_attempts']}"
            )

            result.setObjectName(
                "meta"
            )

            text_area.addWidget(
                result
            )

        elif level_status == "locked":

            locked = QLabel(
                "🔒 Avval oldingi Level'ni "
                "muvaffaqiyatli yakunlang."
            )

            locked.setObjectName(
                "meta"
            )

            text_area.addWidget(
                locked
            )

        elif not lessons_completed:

            remaining = (
                level["total_lessons"]
                - level["completed_lessons"]
            )

            locked = QLabel(
                f"🔒 Imtihon ochilishi uchun "
                f"yana {remaining} ta darsni tugating."
            )

            locked.setObjectName(
                "meta"
            )

            text_area.addWidget(
                locked
            )

        else:

            ready = QLabel(
                (
                    "✓ Barcha majburiy darslar tugallandi. "
                    "Final Exam ochildi."
                )
            )

            ready.setObjectName(
                "meta"
            )

            text_area.addWidget(
                ready
            )

        layout.addLayout(
            text_area
        )

        layout.addStretch()

        if (
            lessons_completed
            and not exam_completed
            and level_status != "locked"
        ):

            button = QPushButton(
                "IMTIHONNI BOSHLASH"
            )

            button.setObjectName(
                "examButton"
            )

            button.clicked.connect(
                lambda checked=False, exam_data=exam:
                self.open_exam(
                    exam_data
                )
            )

            layout.addWidget(
                button
            )

        return card

    # ========================================================
    # OPEN LESSON
    # ========================================================

    def open_lesson(
        self,
        lesson: dict,
    ):
        level_title = ""
        module_title = ""

        for level in self.levels:

            for module in level[
                "modules"
            ]:

                for module_lesson in module[
                    "lessons"
                ]:

                    if (
                        module_lesson["id"]
                        == lesson["id"]
                    ):
                        level_title = (
                            level["title"]
                        )

                        module_title = (
                            module["title"]
                        )

        lesson_data = dict(
            lesson
        )

        lesson_data[
            "level_title"
        ] = level_title

        lesson_data[
            "module_title"
        ] = module_title

        self.lesson_window = (
            LessonWindow(
                lesson=lesson_data,
                user=self.user,
            )
        )

        self.lesson_window.lesson_completed.connect(
            self.lesson_finished
        )

        self.lesson_window.show()

    # ========================================================
    # LESSON COMPLETE
    # ========================================================

    def lesson_finished(
        self,
        lesson_id: int,
    ):
        complete_lesson(
            self.user["id"],
            lesson_id,
        )

        self.reload_data()

        self.build_ui()

    # ========================================================
    # OPEN EXAM
    # ========================================================

    def open_exam(
        self,
        exam: dict,
    ):
        self.exam_window = (
            ExamWindow(
                user=self.user,
                exam=exam,
            )
        )

        self.exam_window.exam_passed.connect(
            self.exam_finished
        )

        self.exam_window.show()

    # ========================================================
    # EXAM COMPLETE
    # ========================================================

    def exam_finished(
        self,
    ):
        self.reload_data()

        self.build_ui()
