from PySide6.QtCore import (
    Qt,
    QTimer,
)

from PySide6.QtWidgets import (
    QFrame,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QListWidget,
    QListWidgetItem,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QStackedWidget,
    QVBoxLayout,
    QWidget,
)

from courses.course_service import (
    get_current_level,
    get_next_available_lesson,
    get_user_course_stats,
)

from ui.course_overview_page import (
    CourseOverviewPage,
)

from ui.curriculum_map import (
    CURRICULUM_SECTIONS,
    get_section,
    validate_curriculum_map,
)

from ui.embedded_pages import (
    ExamPage,
    LessonPage,
    QuizPage,
)

from ui.exams_page import (
    ExamsPage,
)

from ui.learning_page import (
    LearningPage,
)

from ui.license_window import (
    LicenseWindow,
)

from ui.tests_page import (
    TestsPage,
)


class AppShell(QMainWindow):
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

        self.page_cache = {}

        self.current_page_key = None

        mapping_check = (
            validate_curriculum_map()
        )

        if not mapping_check["ok"]:
            raise RuntimeError(
                "Curriculum UI mapping xato: "
                f"missing={mapping_check['missing']}, "
                f"duplicates={mapping_check['duplicates']}, "
                f"unknown={mapping_check['unknown']}"
            )

        self.setWindowTitle(
            "ARCHIPRO UZ"
        )

        self.setMinimumSize(
            1150,
            720,
        )

        self.build_shell()

        self.open_home()

        QTimer.singleShot(
            0,
            self.showMaximized,
        )

    # ========================================================
    # SHELL
    # ========================================================

    def build_shell(self):
        root_widget = QWidget()

        root_widget.setObjectName(
            "appRoot"
        )

        self.setCentralWidget(
            root_widget
        )

        root = QHBoxLayout(
            root_widget
        )

        root.setContentsMargins(
            0,
            0,
            0,
            0,
        )

        root.setSpacing(
            0
        )

        # ====================================================
        # SIDEBAR
        # ====================================================

        sidebar = QFrame()

        sidebar.setObjectName(
            "sidebar"
        )

        sidebar.setFixedWidth(
            270
        )

        sidebar_layout = QVBoxLayout(
            sidebar
        )

        sidebar_layout.setContentsMargins(
            16,
            22,
            16,
            14,
        )

        sidebar_layout.setSpacing(
            7
        )

        logo = QLabel(
            "ARCHIPRO UZ"
        )

        logo.setObjectName(
            "logo"
        )

        logo_sub = QLabel(
            "Architecture Academy"
        )

        logo_sub.setObjectName(
            "logoSub"
        )

        sidebar_layout.addWidget(
            logo
        )

        sidebar_layout.addWidget(
            logo_sub
        )

        sidebar_layout.addSpacing(
            14
        )

        self.menu = QListWidget()

        self.menu_items = [
            "Bosh sahifa",
            "Mening o'qishim",

            "Arxitektura",
            "Archicad",
            "Qurilish konstruksiyalari",
            "SHNQ va normativlar",
            "Amaliyot",
            "BIM va real loyiha",
            "Portfolio / PRO Final",

            "Testlar",
            "Imtihonlar",
            "Kutubxona",
            "Statistika",
            "Litsenziya",
            "Sozlamalar",
        ]

        for text in self.menu_items:
            self.menu.addItem(
                QListWidgetItem(
                    text
                )
            )

        self.menu.itemClicked.connect(
            self.handle_menu
        )

        sidebar_layout.addWidget(
            self.menu,
            1,
        )

        user_name = (
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

        user_info = QLabel(
            f"{user_name}\n"
            f"{license_type}"
        )

        user_info.setObjectName(
            "userInfo"
        )

        user_info.setWordWrap(
            True
        )

        sidebar_layout.addWidget(
            user_info
        )

        # DeveloperBadge DashboardWindow tomonidan
        # shu layout oxiriga qo'shiladi.

        self.stack = QStackedWidget()

        root.addWidget(
            sidebar
        )

        root.addWidget(
            self.stack,
            1,
        )

    # ========================================================
    # MENU
    # ========================================================

    def handle_menu(
        self,
        item,
    ):
        text = item.text()

        if text == "Bosh sahifa":
            self.open_home()
            return

        if text == "Mening o'qishim":
            self.open_learning_overview()
            return

        if text in CURRICULUM_SECTIONS:
            self.open_section_overview(
                text
            )
            return

        if text == "Testlar":
            self.open_tests()
            return

        if text == "Imtihonlar":
            self.open_exams()
            return

        if text == "Statistika":
            self.open_statistics()
            return

        if text == "Litsenziya":
            self.open_license()
            return

        if text == "Kutubxona":
            self.open_info_page(
                "library",
                "Kutubxona",
                (
                    "ARCHIPRO kutubxonasi keyingi funksional "
                    "bosqichda loyiha shablonlari, chek-listlar, "
                    "SHNQ materiallari va amaliy fayllar bilan "
                    "to'ldiriladi."
                ),
            )
            return

        if text == "Sozlamalar":
            self.open_info_page(
                "settings",
                "Sozlamalar",
                (
                    "Interfeys, profil va dastur parametrlarini "
                    "boshqarish markazi."
                ),
            )

    # ========================================================
    # PAGE MANAGER
    # ========================================================

    def show_page(
        self,
        key: str,
        page: QWidget,
    ):
        old = self.page_cache.get(
            key
        )

        if old is not None:
            self.stack.setCurrentWidget(
                old
            )

            self.current_page_key = key

            return old

        page.setParent(
            self.stack
        )

        page.setWindowFlags(
            Qt.WindowType.Widget
        )

        self.stack.addWidget(
            page
        )

        self.page_cache[key] = page

        self.stack.setCurrentWidget(
            page
        )

        self.current_page_key = key

        return page

    def show_cached(
        self,
        key: str,
    ):
        page = self.page_cache.get(
            key
        )

        if page is None:
            self.open_home()
            return

        self.stack.setCurrentWidget(
            page
        )

        self.current_page_key = key

    def drop_page(
        self,
        key: str,
    ):
        page = self.page_cache.pop(
            key,
            None,
        )

        if page is None:
            return

        self.stack.removeWidget(
            page
        )

        page.deleteLater()

    def set_menu(
        self,
        title: str,
    ):
        try:
            self.menu.setCurrentRow(
                self.menu_items.index(
                    title
                )
            )

        except ValueError:
            pass

    # ========================================================
    # HOME
    # ========================================================

    def open_home(self):
        self.set_menu(
            "Bosh sahifa"
        )

        # Faqat home ma'lumotlari dinamik.
        self.drop_page(
            "home"
        )

        stats = get_user_course_stats(
            self.user["id"]
        )

        current_level = get_current_level(
            self.user["id"]
        )

        next_lesson = get_next_available_lesson(
            self.user["id"]
        )

        page = QWidget()

        layout = QVBoxLayout(
            page
        )

        layout.setContentsMargins(
            30,
            26,
            30,
            26,
        )

        layout.setSpacing(
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
            "Bosh sahifa"
        )

        title.setObjectName(
            "overviewTitle"
        )

        subtitle = QLabel(
            "Arxitektura va turar joy loyihalash bo'yicha "
            "shaxsiy o'quv markazingiz."
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

        layout.addWidget(
            header
        )

        # ====================================================
        # STATS
        # ====================================================

        stats_grid = QGridLayout()

        stats_grid.setSpacing(
            13
        )

        if self.is_master:
            current_text = "MASTER"

        elif current_level:
            current_text = (
                current_level["code"]
                .replace(
                    "LEVEL_",
                    "LEVEL ",
                )
            )

        else:
            current_text = "—"

        values = [
            (
                "JORIY BOSQICH",
                current_text,
            ),
            (
                "TUGALLANGAN DARSLAR",
                (
                    f"{stats['completed_lessons']} / "
                    f"{stats['total_lessons']}"
                ),
            ),
            (
                "UMUMIY PROGRESS",
                f"{stats['progress_percent']}%",
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
                17,
                20,
                17,
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

            stats_grid.addWidget(
                card,
                index // 2,
                index % 2,
            )

        layout.addLayout(
            stats_grid
        )

        # ====================================================
        # CONTINUE
        # ====================================================

        continue_card = QFrame()

        continue_card.setObjectName(
            "levelOverviewCard"
        )

        continue_layout = QHBoxLayout(
            continue_card
        )

        continue_layout.setContentsMargins(
            22,
            18,
            22,
            18,
        )

        continue_text_layout = (
            QVBoxLayout()
        )

        small = QLabel(
            "KEYINGI QADAM"
        )

        small.setObjectName(
            "levelCode"
        )

        if next_lesson:
            message = (
                f"{next_lesson['level_code'].replace('LEVEL_', 'LEVEL ')}"
                f"  •  "
                f"{next_lesson['module_title']}"
                f"  •  "
                f"{next_lesson['title']}"
            )

        elif self.is_master:
            message = (
                "MASTER rejimida barcha "
                "Level va darslar tekshirish uchun mavjud."
            )

        else:
            message = (
                "Keyingi ochiq dars topilmadi. "
                "Level yakuniy holatini tekshiring."
            )

        next_label = QLabel(
            message
        )

        next_label.setObjectName(
            "levelName"
        )

        next_label.setWordWrap(
            True
        )

        continue_text_layout.addWidget(
            small
        )

        continue_text_layout.addWidget(
            next_label
        )

        continue_layout.addLayout(
            continue_text_layout,
            1,
        )

        button = QPushButton(
            "O'QISHNI DAVOM ETTIRISH  →"
        )

        button.setObjectName(
            "openLevelButton"
        )

        button.clicked.connect(
            self.open_learning_overview
        )

        continue_layout.addWidget(
            button
        )

        layout.addWidget(
            continue_card
        )

        layout.addStretch()

        self.show_page(
            "home",
            page,
        )

    # ========================================================
    # COURSE OVERVIEW
    # ========================================================

    def open_learning_overview(
        self,
    ):
        self.set_menu(
            "Mening o'qishim"
        )

        key = "overview::all"

        page = self.page_cache.get(
            key
        )

        if page is None:
            page = CourseOverviewPage(
                user=self.user,
                title="Mening o'qishim",
                subtitle=(
                    "LEVEL 00 dan LEVEL 15 gacha "
                    "bo'lgan to'liq professional o'quv yo'li."
                ),
            )

            page.open_level_requested.connect(
                lambda code, title, subtitle:
                self.open_single_level(
                    code,
                    title,
                    subtitle,
                    key,
                )
            )

            self.show_page(
                key,
                page,
            )

        else:
            self.show_cached(
                key
            )

    # ========================================================
    # SECTION OVERVIEW
    # ========================================================

    def open_section_overview(
        self,
        section_name: str,
    ):
        section = get_section(
            section_name
        )

        if section is None:
            return

        self.set_menu(
            section_name
        )

        key = (
            "overview::"
            + section_name
        )

        page = self.page_cache.get(
            key
        )

        if page is None:
            page = CourseOverviewPage(
                user=self.user,
                title=section[
                    "title"
                ],
                subtitle=section[
                    "subtitle"
                ],
                level_codes=section[
                    "levels"
                ],
            )

            page.open_level_requested.connect(
                lambda code,
                title,
                subtitle,
                source_key=key:
                self.open_single_level(
                    code,
                    title,
                    subtitle,
                    source_key,
                )
            )

            self.show_page(
                key,
                page,
            )

        else:
            self.show_cached(
                key
            )

    # ========================================================
    # SINGLE LEVEL
    # ========================================================

    def open_single_level(
        self,
        code: str,
        title: str,
        subtitle: str,
        source_key: str,
    ):
        key = (
            "level::"
            + code
        )

        page = self.page_cache.get(
            key
        )

        if page is None:
            readable_code = (
                code.replace(
                    "LEVEL_",
                    "LEVEL ",
                )
            )

            page = LearningPage(
                user=self.user,
                focus_level_codes=[
                    code
                ],
                custom_title=(
                    f"{readable_code}  •  {title}"
                ),
                custom_subtitle=(
                    subtitle
                ),
                back_callback=(
                    lambda k=source_key:
                    self.show_cached(
                        k
                    )
                ),
                open_lesson_callback=(
                    self.open_lesson_page
                ),
                open_exam_callback=(
                    self.open_exam_from_learning
                ),
            )

            self.show_page(
                key,
                page,
            )

        else:
            # Navigatsiyada qayta BUILD YO'Q.
            # Shu performance uchun juda muhim.
            self.show_cached(
                key
            )

    # ========================================================
    # LESSON
    # ========================================================

    def open_lesson_page(
        self,
        lesson_data: dict,
        source_learning_page,
    ):
        source_key = (
            self.current_page_key
        )

        key = (
            "lesson::"
            + str(
                lesson_data["id"]
            )
        )

        # Dars har ochilganda yangilansin,
        # lekin faqat BITTA dars.
        self.drop_page(
            key
        )

        page = LessonPage(
            lesson=lesson_data,
            user=self.user,
            back_callback=(
                lambda k=source_key:
                self.show_cached(
                    k
                )
            ),
            open_quiz_callback=(
                self.open_quiz_page
            ),
        )

        page.lesson_completed.connect(
            lambda lesson_id,
            source=source_learning_page,
            return_key=source_key:
            self.lesson_completed(
                lesson_id,
                source,
                return_key,
            )
        )

        self.show_page(
            key,
            page,
        )

    # ========================================================
    # QUIZ
    # ========================================================

    def open_quiz_page(
        self,
        lesson_page,
    ):
        lesson_key = (
            self.current_page_key
        )

        lesson = dict(
            lesson_page.lesson
        )

        key = (
            "quiz::"
            + str(
                lesson["id"]
            )
        )

        self.drop_page(
            key
        )

        page = QuizPage(
            user=self.user,
            lesson=lesson,
            back_callback=(
                lambda k=lesson_key:
                self.show_cached(
                    k
                )
            ),
        )

        page.quiz_passed.connect(
            lesson_page.quiz_success
        )

        self.show_page(
            key,
            page,
        )

    # ========================================================
    # LESSON COMPLETED
    # ========================================================

    def lesson_completed(
        self,
        lesson_id,
        source_page,
        return_key,
    ):
        # Original service/progress logikasi.
        source_page.lesson_finished(
            lesson_id
        )

        # Faqat o'zgargan Level sahifasini refresh qilamiz.
        source_page.refresh_page()

        # Overview'larni keyingi kirishda qayta qurish uchun
        # cache'dan chiqaramiz.
        overview_keys = [
            key
            for key in self.page_cache
            if key.startswith(
                "overview::"
            )
        ]

        for key in overview_keys:
            self.drop_page(
                key
            )

        # Test / exam status ham o'zgarishi mumkin.
        self.drop_page(
            "tests"
        )

        self.drop_page(
            "exams"
        )

        self.show_cached(
            return_key
        )

    # ========================================================
    # TESTS
    # ========================================================

    def open_tests(self):
        self.set_menu(
            "Testlar"
        )

        key = "tests"

        page = self.page_cache.get(
            key
        )

        if page is None:
            page = TestsPage(
                self.user
            )

            page.open_level_requested.connect(
                lambda level_codes,
                title,
                subtitle:
                self.open_single_level(
                    level_codes[0],
                    title,
                    subtitle,
                    "tests",
                )
            )

            self.show_page(
                key,
                page,
            )

        else:
            self.show_cached(
                key
            )

    # ========================================================
    # EXAMS
    # ========================================================

    def open_exams(self):
        self.set_menu(
            "Imtihonlar"
        )

        key = "exams"

        page = self.page_cache.get(
            key
        )

        if page is None:
            page = ExamsPage(
                self.user
            )

            page.open_exam_requested.connect(
                lambda exam:
                self.open_exam_page(
                    exam,
                    "exams",
                )
            )

            self.show_page(
                key,
                page,
            )

        else:
            self.show_cached(
                key
            )

    def open_exam_from_learning(
        self,
        exam,
        source_page,
    ):
        self.open_exam_page(
            exam,
            self.current_page_key,
        )

    def open_exam_page(
        self,
        exam: dict,
        source_key: str,
    ):
        exam_data = dict(
            exam
        )

        exam_data[
            "master_mode"
        ] = self.is_master

        key = (
            "exam::"
            + str(
                exam_data["id"]
            )
        )

        self.drop_page(
            key
        )

        page = ExamPage(
            user=self.user,
            exam=exam_data,
            back_callback=(
                lambda k=source_key:
                self.show_cached(
                    k
                )
            ),
        )

        page.exam_passed.connect(
            lambda k=source_key:
            self.exam_completed(
                k
            )
        )

        self.show_page(
            key,
            page,
        )

    def exam_completed(
        self,
        return_key,
    ):
        # Exam progress o'zgardi.
        # Dinamik sahifalarning cache'ini tozalaymiz.

        keys = list(
            self.page_cache.keys()
        )

        for key in keys:
            if (
                key.startswith(
                    "overview::"
                )
                or key.startswith(
                    "level::"
                )
                or key
                in {
                    "tests",
                    "exams",
                    "home",
                }
            ):
                self.drop_page(
                    key
                )

        self.open_home()

    # ========================================================
    # STATISTICS
    # ========================================================

    def open_statistics(self):
        self.set_menu(
            "Statistika"
        )

        stats = get_user_course_stats(
            self.user["id"]
        )

        text = (
            f"Tugallangan darslar: "
            f"{stats['completed_lessons']} / "
            f"{stats['total_lessons']}\n\n"

            f"Umumiy progress: "
            f"{stats['progress_percent']}%\n\n"

            f"Dars XP: "
            f"{stats['lesson_xp']}\n\n"

            f"Imtihon XP: "
            f"{stats['exam_xp']}\n\n"

            f"Jami XP: "
            f"{stats['xp']}"
        )

        self.open_info_page(
            "statistics",
            "Statistika",
            text,
            replace=True,
        )

    # ========================================================
    # LICENSE
    # ========================================================

    def open_license(self):
        self.set_menu(
            "Litsenziya"
        )

        key = "license"

        page = self.page_cache.get(
            key
        )

        if page is None:
            page = LicenseWindow(
                self.user
            )

            self.show_page(
                key,
                page,
            )

        else:
            self.show_cached(
                key
            )

    # ========================================================
    # INFO PAGE
    # ========================================================

    def open_info_page(
        self,
        key,
        title,
        text,
        replace=False,
    ):
        if replace:
            self.drop_page(
                key
            )

        elif key in self.page_cache:
            self.show_cached(
                key
            )

            return

        page = QWidget()

        layout = QVBoxLayout(
            page
        )

        layout.setContentsMargins(
            30,
            26,
            30,
            26,
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

        heading = QLabel(
            title
        )

        heading.setObjectName(
            "overviewTitle"
        )

        body = QLabel(
            text
        )

        body.setObjectName(
            "overviewSubtitle"
        )

        body.setWordWrap(
            True
        )

        header_layout.addWidget(
            heading
        )

        header_layout.addWidget(
            body
        )

        layout.addWidget(
            header
        )

        layout.addStretch()

        self.show_page(
            key,
            page,
        )
