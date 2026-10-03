from PySide6.QtCore import Qt

from PySide6.QtWidgets import (
    QFrame,
    QHBoxLayout,
    QLabel,
    QListWidget,
    QListWidgetItem,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from courses.course_service import (
    complete_lesson,
    get_current_level,
    get_next_available_lesson,
    get_user_course_stats,
)

from ui.learning_window import (
    LearningWindow,
)

from ui.lesson_window import (
    LessonWindow,
)

from ui.license_window import (
    LicenseWindow,
)


class DashboardWindow(QMainWindow):
    def __init__(
        self,
        user: dict,
    ):
        super().__init__()

        self.user = user

        self.lesson_window = None
        self.learning_window = None
        self.license_window = None

        self.is_master = (
            str(
                self.user.get(
                    "license_type",
                    "",
                )
            ).upper()
            == "MASTER"
        )

        self.setWindowTitle(
            "ARCHIPRO UZ"
        )

        self.resize(
            1450,
            850,
        )

        self.reload_data()

        self.build_ui()

    # ========================================================
    # DATA
    # ========================================================

    def reload_data(self):
        self.stats = (
            get_user_course_stats(
                self.user["id"]
            )
        )

        self.current_level = (
            get_current_level(
                self.user["id"]
            )
        )

        self.next_lesson = (
            get_next_available_lesson(
                self.user["id"]
            )
        )

    # ========================================================
    # UI
