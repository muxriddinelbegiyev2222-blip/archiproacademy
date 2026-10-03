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


class AppShell(
    QMainWindow
):
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

        if not mapping_check[
            "ok"
        ]:
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
            1100,
            700,
        )

        self._setup_style()
        self._build_shell()

        self.open_home()

        QTimer.singleShot(
            0,
            self.showMaximized,
        )

    # ========================================================
    # STYLE
    # ========================================================

    def _setup_style(self):
        self.setStyleSheet(
            """
            QMainWindow,
            QWidget#appRoot,
            QStackedWidget {
                background-color: #0B1220;
            }

            QWidget {
                color: #F8FAFC;
                font-family: 'Segoe UI';
            }

            QFrame#sidebar {
                background-color: #0F172A;
                border-right: 1px solid #1E293B;
            }

            QLabel#logo {
                color: #FFFFFF;
                font-size: 25px;
                font-weight: 800;
            }

            QLabel#logoSub {
                color: #94A3B8;
                font-size: 13px;
            }

            QListWidget {
                background: transparent;
                border: none;
                outline: none;
                color: #D6DEE9;
                font-size: 15px;
                font-weight: 500;
            }

            QListWidget::item {
                padding: 12px 14px;
                margin: 2px 0px;
                border-radius: 8px;
            }

            QListWidget::item:hover {
                background-color: #172033;
            }

            QListWidget::item:selected {
                background-color: #2563EB;
                color: #FFFFFF;
            }

            QLabel#userInfo {
                background-color: #111827;
                border: 1px solid #1E293B;
                border-radius: 10px;
                padding: 12px;
                color: #E2E8F0;
                font-size: 13px;
            }

            QLabel#pageTitle {
                color: #FFFFFF;
                font-size: 34px;
                font-weight: 800;
            }

            QLabel#pageSubtitle {
                color: #A8B3C7;
                font-size: 16px;
            }

            QFrame#masterBanner {
                background-color: #251D06;
                border: 1px solid #A16207;
                border-radius: 14px;
            }

            QLabel#masterTitle {
                color: #FACC15;
                font-size: 18px;
                font-weight: 800;
            }

            QLabel#masterText {
                color: #FDE68A;
                font-size: 14px;
            }

            QFrame#statCard,
            QFrame#continueCard {
                background-color: #111827;
                border: 1px solid #1E293B;
                border-radius: 14px;
            }

            QLabel#cardLabel {
                color: #A8B3C7;
                font-size: 14px;
            }

            QLabel#cardValue {
                color: #FFFFFF;
                font-size: 26px;
                font-weight: 800;
            }

            QLabel#sectionTitle {
                color: #FFFFFF;
                font-size: 21px;
                font-weight: 700;
            }

            QLabel#bodyText {
                color: #CBD5E1;
                font-size: 15px;
            }

            QProgressBar {
                border: none;
                background-color: #1E293B;
                border-radius: 7px;
                height: 14px;
                color: transparent;
            }

            QProgressBar::chunk {
                background-color: #2563EB;
                border-radius: 7px;
            }

            QPushButton#primaryButton {
                background-color: #2563EB;
                color: #FFFFFF;
                border: none;
                border-radius: 9px;
                padding: 12px 18px;
                font-size: 15px;
                font-weight: 700;
            }

            QPushButton#primaryButton:hover {
                background-color: #3B82F6;
            }
            """
        )

    # ========================================================
    # SHELL
    # ========================================================

    def _build_shell(self):
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

        sidebar = QFrame()

        sidebar.setObjectName(
            "sidebar"
        )

        sidebar.setFixedWidth(
            285
        )

        sidebar_layout = QVBoxLayout(
            sidebar
        )

        sidebar_layout.setContentsMargins(
            18,
            24,
            18,
            16,
        )

        sidebar_layout.setSpacing(
            8
        )

        logo = QLabel(
            "ARCHIPRO UZ"
        )

        logo.setObjectName(
            "logo"
        )

        sidebar_layout.addWidget(
            logo
        )

        logo_sub = QLabel(
            "Architecture Academy"
        )

        logo_sub.setObjectName(
            "logoSub"
        )

        sidebar_layout.addWidget(
            logo_sub
        )

        sidebar_layout.addSpacing(
            18
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
            self._handle_menu
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

        self.stack = QStackedWidget()

        root.addWidget(
            sidebar
        )

        root.addWidget(
            self.stack,
            1,
        )

    # ========================================================
    # ROUTER
    # ========================================================

    def _handle_menu(
        self,
        item,
    ):
        text = item.text()

        if text == "Bosh sahifa":
            self.open_home()

        elif text == "Mening o'qishim":
            self.open_learning()

        elif text in CURRICULUM_SECTIONS:
            self.open_section(
                text
            )

        elif text == "Testlar":
            self.open_tests()

        elif text == "Imtihonlar":
            self.open_exams()

        elif text == "Kutubxona":
            self.open_info_page(
                "library",
                "Kutubxona",
                (
                    "Kutubxona uchun qo'shimcha "
                    "resurslar keyingi bosqichda ulanadi. "
                    "Mavjud o'quv kontenti saqlangan."
                ),
            )

        elif text == "Statistika":
            self.open_statistics()

        elif text == "Litsenziya":
            self.open_license()

        elif text == "Sozlamalar":
            self.open_info_page(
                "settings",
                "Sozlamalar",
                (
                    "Profil va dastur sozlamalari "
                    "keyingi UI bosqichida "
                    "shu sahifaga ulanadi."
                ),
            )

    # ========================================================
    # PAGE MANAGER
    # ========================================================

    def _show_page(
        self,
        key: str,
        page: QWidget,
    ):
        existing = self.page_cache.get(
            key
        )

        if existing is not None:
            self.stack.setCurrentWidget(
                existing
            )

            self.current_page_key = key

            return existing

        page.setParent(
            self.stack
        )

        page.setWindowFlags(
            Qt.WindowType.Widget
        )

        self.stack.addWidget(
            page
        )

        self.page_cache[
            key
        ] = page

        self.stack.setCurrentWidget(
            page
        )

        self.current_page_key = key

        return page

    def _show_cached(
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

    def _drop_cached_page(
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

    def _set_menu_row(
        self,
        label: str,
    ):
        try:
            self.menu.setCurrentRow(
                self.menu_items.index(
                    label
                )
            )

        except ValueError:
            pass

    # ========================================================
    # REFRESH
    # ========================================================

    def _refresh_learning_pages(self):
        for key, page in list(
            self.page_cache.items()
        ):
            if isinstance(
                page,
                LearningPage,
            ):
                page.refresh_page()

            elif (
                key in {
                    "tests",
                    "exams",
                }
                and hasattr(
                    page,
                    "refresh_page",
                )
            ):
                page.refresh_page()

    # ========================================================
    # HOME
    # ========================================================

    def open_home(self):
        self._set_menu_row(
            "Bosh sahifa"
        )

        self._drop_cached_page(
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
            34,
            30,
            34,
            30,
        )

        layout.setSpacing(
            18
        )

        title = QLabel(
            "Bosh sahifa"
        )

        title.setObjectName(
            "pageTitle"
        )

        layout.addWidget(
            title
        )

        subtitle = QLabel(
            "Arxitekturani 0 dan professional "
            "turar joy loyihalashgacha "
            "bosqichma-bosqich o'rganing."
        )

        subtitle.setObjectName(
            "pageSubtitle"
        )

        subtitle.setWordWrap(
            True
        )

        layout.addWidget(
            subtitle
        )

        if self.is_master:
            banner = QFrame()

            banner.setObjectName(
                "masterBanner"
            )

            banner_layout = QHBoxLayout(
                banner
            )

            banner_layout.setContentsMargins(
                18,
                14,
                18,
                14,
            )

            text_area = QVBoxLayout()

            banner_title = QLabel(
                "★ MASTER TEST MODE FAOL"
            )

            banner_title.setObjectName(
                "masterTitle"
            )

            banner_text = QLabel(
                "Bu rejim faqat dastur egasi uchun. "
                "Barcha Level va darslarni "
                "blokirovkasiz tekshirish mumkin."
            )

            banner_text.setObjectName(
                "masterText"
            )

            banner_text.setWordWrap(
                True
            )

            text_area.addWidget(
                banner_title
            )

            text_area.addWidget(
                banner_text
            )

            banner_layout.addLayout(
                text_area,
                1,
            )

            button = QPushButton(
                "BARCHA LEVELLARNI KO'RISH"
            )

            button.setObjectName(
                "primaryButton"
            )

            button.clicked.connect(
                self.open_learning
            )

            banner_layout.addWidget(
                button
            )

            layout.addWidget(
                banner
            )

        cards = QGridLayout()

        cards.setHorizontalSpacing(
            14
        )

        cards.setVerticalSpacing(
            14
        )

        if self.is_master:
            current_level_text = "MASTER"

        elif current_level:
            current_level_text = (
                current_level[
                    "code"
                ]
                .replace(
                    "LEVEL_",
                    "LEVEL ",
                )
            )

        else:
            current_level_text = "—"

        card_data = [
            (
                "Joriy bosqich",
                current_level_text,
            ),
            (
                "Tugallangan darslar",
                (
                    f"{stats['completed_lessons']} / "
                    f"{stats['total_lessons']}"
                ),
            ),
            (
                "Umumiy progress",
                f"{stats['progress_percent']}%",
            ),
            (
                "Jami XP",
                str(
                    stats["xp"]
                ),
            ),
        ]

        for index, (
            label,
            value,
        ) in enumerate(
            card_data
        ):
            card = QFrame()

            card.setObjectName(
                "statCard"
            )

            card_layout = QVBoxLayout(
                card
            )

            card_layout.setContentsMargins(
                18,
                16,
                18,
                16,
            )

            label_widget = QLabel(
                label
            )

            label_widget.setObjectName(
                "cardLabel"
            )

            value_widget = QLabel(
                value
            )

            value_widget.setObjectName(
                "cardValue"
            )

            card_layout.addWidget(
                label_widget
            )

            card_layout.addWidget(
                value_widget
            )

            cards.addWidget(
                card,
                index // 2,
                index % 2,
            )

        layout.addLayout(
            cards
        )

        progress = QProgressBar()

        progress.setRange(
            0,
            100,
        )

        progress.setValue(
            stats[
                "progress_percent"
            ]
        )

        layout.addWidget(
            progress
        )

        continue_card = QFrame()

        continue_card.setObjectName(
            "continueCard"
        )

        continue_layout = QHBoxLayout(
            continue_card
        )

        continue_layout.setContentsMargins(
            20,
            18,
            20,
            18,
        )

        text_area = QVBoxLayout()

        continue_title = QLabel(
            "Keyingi dars"
        )

        continue_title.setObjectName(
            "sectionTitle"
        )

        if next_lesson:
            continue_text_value = (
                f"{next_lesson['level_code'].replace('LEVEL_', 'LEVEL ')}"
                f"  •  "
                f"{next_lesson['module_title']}"
                f"  •  "
                f"{next_lesson['title']}"
            )

        elif self.is_master:
            continue_text_value = (
                "MASTER rejimida barcha mavjud "
                "darslarni Mening o'qishim "
                "bo'limidan tekshirish mumkin."
            )

        else:
            continue_text_value = (
                "Hozir ochiq keyingi dars topilmadi. "
                "Level imtihoni yoki progressni tekshiring."
            )

        continue_text = QLabel(
            continue_text_value
        )

        continue_text.setObjectName(
            "bodyText"
        )

        continue_text.setWordWrap(
            True
        )

        text_area.addWidget(
            continue_title
        )

        text_area.addWidget(
            continue_text
        )

        continue_layout.addLayout(
            text_area,
            1,
        )

        continue_button = QPushButton(
            "O'QISHNI DAVOM ETTIRISH"
        )

        continue_button.setObjectName(
            "primaryButton"
        )

        continue_button.clicked.connect(
            self.open_learning
        )

        continue_layout.addWidget(
            continue_button
        )

        layout.addWidget(
            continue_card
        )

        layout.addStretch()

        self._show_page(
            "home",
            page,
        )

    # ========================================================
    # LEARNING PAGE CREATOR
    # ========================================================

    def _create_learning_page(
        self,
        *,
        key,
        level_codes=None,
        title=None,
        subtitle=None,
        back_callback=None,
    ):
        page = LearningPage(
            user=self.user,
            focus_level_codes=(
                level_codes
            ),
            custom_title=(
                title
            ),
            custom_subtitle=(
                subtitle
            ),
            back_callback=(
                back_callback
            ),
            open_lesson_callback=(
                self._open_lesson_page
            ),
            open_exam_callback=(
                self._open_exam_from_learning
            ),
        )

        self._show_page(
            key,
            page,
        )

        return page

    # ========================================================
    # ALL LEARNING
    # ========================================================

    def open_learning(self):
        self._set_menu_row(
            "Mening o'qishim"
        )

        key = "learning_all"

        page = self.page_cache.get(
            key
        )

        if page is None:
            self._create_learning_page(
                key=key,
                title="Mening o'qishim",
                subtitle=(
                    "LEVEL 00 dan LEVEL 15 gacha "
                    "bo'lgan to'liq o'quv yo'lingiz."
                ),
                back_callback=self.open_home,
            )

        else:
            page.refresh_page()

            self._show_cached(
                key
            )

    # ========================================================
    # CURRICULUM SECTIONS
    # ========================================================

    def open_section(
        self,
        section_name: str,
    ):
        section = get_section(
            section_name
        )

        if section is None:
            return

        self._set_menu_row(
            section_name
        )

        key = (
            "section::"
            + section_name
        )

        page = self.page_cache.get(
            key
        )

        if page is None:
            self._create_learning_page(
                key=key,
                level_codes=(
                    section[
                        "levels"
                    ]
                ),
                title=(
                    section[
                        "title"
                    ]
                ),
                subtitle=(
                    section[
                        "subtitle"
                    ]
                ),
                back_callback=(
                    self.open_home
                ),
            )

        else:
            page.refresh_page()

            self._show_cached(
                key
            )

    # ========================================================
    # EMBEDDED LESSON
    # ========================================================

    def _open_lesson_page(
        self,
        lesson_data: dict,
        source_learning_page,
    ):
        source_key = (
            self.current_page_key
        )

        lesson_id = (
            lesson_data[
                "id"
            ]
        )

        key = (
            f"lesson::{lesson_id}"
        )

        # Dars sahifasini har safar yangi quramiz.
        self._drop_cached_page(
            key
        )

        page = LessonPage(
            lesson=lesson_data,
            user=self.user,
            back_callback=(
                lambda k=source_key:
                self._show_cached(
                    k
                )
            ),
            open_quiz_callback=(
                self._open_quiz_page
            ),
        )

        page.lesson_completed.connect(
            lambda completed_id,
            source=source_learning_page,
            return_key=source_key:
            self._lesson_completed(
                completed_id,
                source,
                return_key,
            )
        )

        self._show_page(
            key,
            page,
        )

    # ========================================================
    # EMBEDDED QUIZ
    # ========================================================

    def _open_quiz_page(
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
            f"quiz::{lesson['id']}"
        )

        # Har urinishda yangi savol tartibi.
        self._drop_cached_page(
            key
        )

        quiz_page = QuizPage(
            user=self.user,
            lesson=lesson,
            back_callback=(
                lambda k=lesson_key:
                self._show_cached(
                    k
                )
            ),
        )

        quiz_page.quiz_passed.connect(
            lesson_page.quiz_success
        )

        self._show_page(
            key,
            quiz_page,
        )

    # ========================================================
    # LESSON COMPLETE
    # ========================================================

    def _lesson_completed(
        self,
        lesson_id: int,
        source_learning_page,
        return_key: str,
    ):
        """
        Original LearningWindow.lesson_finished()
        aynan progress service'ni ishlatadi.

        Uni qayta yozmaymiz — original metodni
        o'zidan foydalanamiz.
        """

        source_learning_page.lesson_finished(
            lesson_id
        )

        self._refresh_learning_pages()

        tests = self.page_cache.get(
            "tests"
        )

        if tests is not None:
            tests.refresh_page()

        exams = self.page_cache.get(
            "exams"
        )

        if exams is not None:
            exams.refresh_page()

        self._show_cached(
            return_key
        )

    # ========================================================
    # TESTS
    # ========================================================

    def open_tests(self):
        self._set_menu_row(
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
                self._open_level_from_tests
            )

            self._show_page(
                key,
                page,
            )

        else:
            page.refresh_page()

            self._show_cached(
                key
            )

    def _open_level_from_tests(
        self,
        level_codes,
        title,
        subtitle,
    ):
        code_key = "_".join(
            level_codes
        )

        key = (
            "tests_level::"
            + code_key
        )

        page = self.page_cache.get(
            key
        )

        if page is None:
            self._create_learning_page(
                key=key,
                level_codes=(
                    level_codes
                ),
                title=(
                    title
                ),
                subtitle=(
                    subtitle
                ),
                back_callback=(
                    self.open_tests
                ),
            )

        else:
            page.refresh_page()

            self._show_cached(
                key
            )

    # ========================================================
    # EXAMS
    # ========================================================

    def open_exams(self):
        self._set_menu_row(
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
                self._open_exam_from_exams
            )

            self._show_page(
                key,
                page,
            )

        else:
            page.refresh_page()

            self._show_cached(
                key
            )

    def _open_exam_from_exams(
        self,
        exam: dict,
    ):
        self._open_exam_page(
            exam=exam,
            source_key="exams",
        )

    def _open_exam_from_learning(
        self,
        exam: dict,
        source_learning_page,
    ):
        source_key = (
            self.current_page_key
        )

        self._open_exam_page(
            exam=exam,
            source_key=source_key,
        )

    def _open_exam_page(
        self,
        *,
        exam: dict,
        source_key: str,
    ):
        exam_data = dict(
            exam
        )

        exam_data[
            "master_mode"
        ] = self.is_master

        exam_id = (
            exam_data[
                "id"
            ]
        )

        key = (
            f"exam::{exam_id}"
        )

        self._drop_cached_page(
            key
        )

        page = ExamPage(
            user=self.user,
            exam=exam_data,
            back_callback=(
                lambda k=source_key:
                self._show_cached(
                    k
                )
            ),
        )

        page.exam_passed.connect(
            lambda return_key=source_key:
            self._exam_completed(
                return_key
            )
        )

        self._show_page(
            key,
            page,
        )

    def _exam_completed(
        self,
        return_key: str,
    ):
        self._refresh_learning_pages()

        tests = self.page_cache.get(
            "tests"
        )

        if tests is not None:
            tests.refresh_page()

        exams = self.page_cache.get(
            "exams"
        )

        if exams is not None:
            exams.refresh_page()

        self._show_cached(
            return_key
        )

    # ========================================================
    # STATISTICS
    # ========================================================

    def open_statistics(self):
        self._set_menu_row(
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
        self._set_menu_row(
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

            self._show_page(
                key,
                page,
            )

        else:
            self._show_cached(
                key
            )

    # ========================================================
    # INFO PAGE
    # ========================================================

    def open_info_page(
        self,
        key: str,
        title: str,
        text: str,
        replace=False,
    ):
        if replace:
            self._drop_cached_page(
                key
            )

        else:
            old = self.page_cache.get(
                key
            )

            if old is not None:
                self._show_cached(
                    key
                )

                return

        page = QWidget()

        layout = QVBoxLayout(
            page
        )

        layout.setContentsMargins(
            34,
            30,
            34,
            30,
        )

        layout.setSpacing(
            16
        )

        heading = QLabel(
            title
        )

        heading.setObjectName(
            "pageTitle"
        )

        body = QLabel(
            text
        )

        body.setObjectName(
            "bodyText"
        )

        body.setWordWrap(
            True
        )

        layout.addWidget(
            heading
        )

        layout.addWidget(
            body
        )

        layout.addStretch()

        self._show_page(
            key,
            page,
        )
