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

from ui.exam_window import (
    ExamWindow,
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

        self.exam_window = None

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
                    "resurslar keyingi kontent "
                    "bosqichida ulanadi. "
                    "Mavjud 680 darsning o'zi "
                    "o'quv bo'limlarida saqlangan."
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

        return page

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

    def _drop_cached_page(
        self,
        key: str,
    ):
        page = self.page_cache.pop(
            key,
            None,
        )

        if page is not None:
            self.stack.removeWidget(
                page
            )

            page.deleteLater()

    def _refresh_learning_pages(
        self,
    ):
        for key, page in list(
            self.page_cache.items()
        ):
            if isinstance(
                page,
                LearningPage,
            ):
                page.refresh_page()

            elif (
                hasattr(
                    page,
                    "refresh_page",
                )
                and key
                in {
                    "tests",
                    "exams",
                }
            ):
                page.refresh_page()

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

        next_lesson = (
            get_next_available_lesson(
                self.user["id"]
            )
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
            current_level_text = (
                "MASTER"
            )

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

    def open_learning(self):
        self._set_menu_row(
            "Mening o'qishim"
        )

        key = "learning_all"

        page = self.page_cache.get(
            key
        )

        if page is None:
            page = LearningPage(
                user=self.user,
                custom_title=(
                    "Mening o'qishim"
                ),
                custom_subtitle=(
                    "LEVEL 00 dan LEVEL 15 gacha "
                    "bo'lgan to'liq o'quv yo'lingiz."
                ),
                back_callback=(
                    self.open_home
                ),
            )

            self._show_page(
                key,
                page,
            )

        else:
            page.refresh_page()

            self.stack.setCurrentWidget(
                page
            )

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
            page = LearningPage(
                user=self.user,
                focus_level_codes=(
                    section[
                        "levels"
                    ]
                ),
                custom_title=(
                    section[
                        "title"
                    ]
                ),
                custom_subtitle=(
                    section[
                        "subtitle"
                    ]
                ),
                back_callback=(
                    self.open_home
                ),
            )

            self._show_page(
                key,
                page,
            )

        else:
            page.refresh_page()

            self.stack.setCurrentWidget(
                page
            )

    def open_level_from_tests(
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
                    self.open_tests
                ),
            )

            self._show_page(
                key,
                page,
            )

        else:
            page.refresh_page()

            self.stack.setCurrentWidget(
                page
            )

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
                self.open_level_from_tests
            )

            self._show_page(
                key,
                page,
            )

        else:
            page.refresh_page()

            self.stack.setCurrentWidget(
                page
            )

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
                self._open_exam_window
            )

            self._show_page(
                key,
                page,
            )

        else:
            page.refresh_page()

            self.stack.setCurrentWidget(
                page
            )

    def _open_exam_window(
        self,
        exam: dict,
    ):
        exam_data = dict(
            exam
        )

        exam_data[
            "master_mode"
        ] = self.is_master

        self.exam_window = ExamWindow(
            user=self.user,
            exam=exam_data,
        )

        self.exam_window.exam_passed.connect(
            self._exam_finished
        )

        self.exam_window.show()

    def _exam_finished(self):
        self._refresh_learning_pages()

        self.open_home()

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
            self.stack.setCurrentWidget(
                page
            )

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
                self.stack.setCurrentWidget(
                    old
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
