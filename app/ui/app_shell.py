from PySide6.QtCore import (
    Qt,
    QTimer,
)

from PySide6.QtGui import (
    QKeySequence,
    QShortcut,
)

from PySide6.QtWidgets import (
    QFrame,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QListWidget,
    QListWidgetItem,
    QMainWindow,
    QMessageBox,
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

from courses.user_features import (
    get_recent_lessons,
    mark_lesson_opened,
)

from ui.course_overview_page import (
    CourseOverviewPage,
)

from ui.curriculum_map import (
    CURRICULUM_SECTIONS,
    get_section,
    validate_curriculum_map,
)

from ui.exams_page import (
    ExamsPage,
)

from ui.learning_page import (
    LearningPage,
)

from ui.library_page import (
    LibraryPage,
)

from ui.license_window import (
    LicenseWindow,
)

from ui.glossary_page import (
    GlossaryPage,
)

from ui.help_page import (
    HelpPage,
)

from ui.settings_page import (
    SettingsPage,
)

from ui.statistics_page import (
    StatisticsPage,
)

from ui.tests_page import (
    TestsPage,
)


# ============================================================
# ARCHIPRO UZ
# APP SHELL V4
#
# PERFORMANCE:
# - lazy lesson/quiz/exam import
# - max 3 cached Level page
# - transient page cleanup
# - no double Level refresh
# ============================================================


class AppShell(QMainWindow):

    MAX_CACHED_LEVEL_PAGES = 3

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

        # ====================================================
        # PAGE CACHE
        # ====================================================

        self.page_cache = {}

        self.current_page_key = None

        # Faqat Level page uchun LRU.
        self.level_page_lru = []

        # Transient sahifa -> qaytish sahifasi.
        self.transient_return_keys = {}

        # Global keyboard shortcutlar GC bo'lib ketmasligi uchun.
        self.shortcuts = []

        # ====================================================
        # CURRICULUM CHECK
        # ====================================================

        mapping_check = (
            validate_curriculum_map()
        )

        if not mapping_check["ok"]:
            raise RuntimeError(
                "Curriculum UI mapping xato: "
                f"missing="
                f"{mapping_check['missing']}, "
                f"duplicates="
                f"{mapping_check['duplicates']}, "
                f"unknown="
                f"{mapping_check['unknown']}"
            )

        # ====================================================
        # WINDOW
        # ====================================================

        self.setWindowTitle(
            "ARCHIPRO UZ"
        )

        self.setMinimumSize(
            1150,
            720,
        )

        self.build_shell()

        self.install_shortcuts()

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

        # ====================================================
        # LOGO
        # ====================================================

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

        # ====================================================
        # MENU
        # ====================================================

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
            "Terminlar lug'ati",
            "Statistika",
            "Litsenziya",
            "Yordam",
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

        # ====================================================
        # USER INFO
        # ====================================================

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

        # DashboardWindow DeveloperBadge'ni
        # aynan shu sidebar layout oxiriga qo'shadi.

        # ====================================================
        # CONTENT STACK
        # ====================================================

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

        # Menu bosilganda eski transient dars/test/exam
        # sahifalarini saqlab yurish shart emas.
        self.cleanup_transient_pages()

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

        if text == "Kutubxona":
            self.open_library()
            return

        if text == "Terminlar lug'ati":
            self.open_glossary()
            return

        if text == "Statistika":
            self.open_statistics()
            return

        if text == "Litsenziya":
            self.open_license()
            return

        if text == "Yordam":
            self.open_help()
            return

        if text == "Sozlamalar":
            self.open_settings()
            return

    # ========================================================
    # PAGE CACHE
    # ========================================================

    def show_page(
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

            self.touch_level_page(
                key
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

        self.current_page_key = key

        self.touch_level_page(
            key
        )

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
            return False

        self.stack.setCurrentWidget(
            page
        )

        self.current_page_key = key

        self.touch_level_page(
            key
        )

        return True

    def drop_page(
        self,
        key: str,
    ):
        page = self.page_cache.pop(
            key,
            None,
        )

        self.transient_return_keys.pop(
            key,
            None,
        )

        if page is None:
            return

        if key in self.level_page_lru:
            try:
                self.level_page_lru.remove(
                    key
                )

            except ValueError:
                pass

        self.stack.removeWidget(
            page
        )

        page.setParent(
            None
        )

        page.deleteLater()

    # ========================================================
    # LEVEL LRU CACHE
    # ========================================================

    def touch_level_page(
        self,
        key: str,
    ):
        if not key.startswith(
            "level::"
        ):
            return

        if key in self.level_page_lru:
            self.level_page_lru.remove(
                key
            )

        self.level_page_lru.append(
            key
        )

    def trim_level_cache(
        self,
        protected_keys=None,
    ):
        """
        Faqat eng oxirgi 3 ta Level page RAM'da qoladi.

        Hozir ochiq Level va kerakli return page
        o'chirilmaydi.
        """

        protected = set(
            protected_keys or []
        )

        if self.current_page_key:
            protected.add(
                self.current_page_key
            )

        while (
            len(
                self.level_page_lru
            )
            > self.MAX_CACHED_LEVEL_PAGES
        ):
            candidate = None

            for key in list(
                self.level_page_lru
            ):
                if key in protected:
                    continue

                candidate = key
                break

            if candidate is None:
                break

            self.drop_page(
                candidate
            )

    # ========================================================
    # TRANSIENT CLEANUP
    # ========================================================

    def cleanup_transient_pages(
        self,
        except_keys=None,
    ):
        """
        Lesson / quiz / exam vaqtinchalik sahifalar.

        Menu almashtirilganda ular RAM'da
        qolib ketmaydi.
        """

        protected = set(
            except_keys or []
        )

        keys = list(
            self.page_cache.keys()
        )

        for key in keys:
            if key in protected:
                continue

            if (
                key.startswith(
                    "lesson::"
                )
                or key.startswith(
                    "quiz::"
                )
                or key.startswith(
                    "exam::"
                )
            ):
                self.drop_page(
                    key
                )

                self.transient_return_keys.pop(
                    key,
                    None,
                )

    # ========================================================
    # BACK FROM TRANSIENT
    # ========================================================

    def return_from_transient(
        self,
        return_key: str,
        transient_key: str,
    ):
        """
        Avval oldingi sahifaga o'tadi,
        keyin vaqtinchalik sahifani delete qiladi.
        """

        success = self.show_cached(
            return_key
        )

        if not success:
            return

        self.transient_return_keys.pop(
            transient_key,
            None,
        )

        QTimer.singleShot(
            0,
            lambda:
            self.drop_page(
                transient_key
            ),
        )

    # ========================================================
    # MENU SELECTION
    # ========================================================

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

        # Home progress dinamik.
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

        recent_lessons = get_recent_lessons(
            self.user["id"],
            limit=3,
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

        header_layout.setSpacing(
            6
        )

        title = QLabel(
            "Bosh sahifa"
        )

        title.setObjectName(
            "overviewTitle"
        )

        subtitle = QLabel(
            "Arxitektura va turar joy loyihalash "
            "bo'yicha shaxsiy o'quv markazingiz."
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

        layout.addWidget(
            header
        )

        # ====================================================
        # MASTER
        # ====================================================

        if self.is_master:
            master = QFrame()

            master.setObjectName(
                "levelOverviewCard"
            )

            master_layout = QHBoxLayout(
                master
            )

            master_layout.setContentsMargins(
                20,
                16,
                20,
                16,
            )

            text_layout = QVBoxLayout()

            master_title = QLabel(
                "★ MASTER TEST MODE FAOL"
            )

            master_title.setObjectName(
                "levelCode"
            )

            master_text = QLabel(
                "Barcha Level va darslarni "
                "tekshirish imkoniyati faol."
            )

            master_text.setObjectName(
                "levelDesc"
            )

            master_text.setWordWrap(
                True
            )

            text_layout.addWidget(
                master_title
            )

            text_layout.addWidget(
                master_text
            )

            master_layout.addLayout(
                text_layout,
                1,
            )

            button = QPushButton(
                "BARCHA LEVELLAR  →"
            )

            button.setObjectName(
                "openLevelButton"
            )

            button.clicked.connect(
                self.open_learning_overview
            )

            master_layout.addWidget(
                button
            )

            layout.addWidget(
                master
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
                current_level[
                    "code"
                ].replace(
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

            card_layout.setSpacing(
                6
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
        # NEXT STEP
        # ====================================================

        next_card = QFrame()

        next_card.setObjectName(
            "levelOverviewCard"
        )

        next_layout = QHBoxLayout(
            next_card
        )

        next_layout.setContentsMargins(
            22,
            18,
            22,
            18,
        )

        next_layout.setSpacing(
            20
        )

        text_layout = QVBoxLayout()

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
                "darslar tekshirish uchun mavjud."
            )

        else:
            message = (
                "Keyingi ochiq dars topilmadi."
            )

        message_label = QLabel(
            message
        )

        message_label.setObjectName(
            "levelName"
        )

        message_label.setWordWrap(
            True
        )

        text_layout.addWidget(
            small
        )

        text_layout.addWidget(
            message_label
        )

        next_layout.addLayout(
            text_layout,
            1,
        )

        button = QPushButton(
            "O'QISHNI DAVOM ETTIRISH  →"
        )

        button.setObjectName(
            "openLevelButton"
        )

        button.clicked.connect(
            self.continue_learning
        )

        next_layout.addWidget(
            button
        )

        layout.addWidget(
            next_card
        )

        if recent_lessons:
            recent_title = QLabel(
                "YAQINDA KO'RILGAN DARSLAR"
            )
            recent_title.setObjectName(
                "levelCode"
            )
            layout.addWidget(
                recent_title
            )

            for recent in recent_lessons:
                recent_card = QFrame()
                recent_card.setObjectName(
                    "levelOverviewCard"
                )

                recent_layout = QHBoxLayout(
                    recent_card
                )
                recent_layout.setContentsMargins(
                    18,
                    13,
                    18,
                    13,
                )

                recent_text = QVBoxLayout()

                recent_name = QLabel(
                    recent.get(
                        "title",
                        "Dars",
                    )
                )
                recent_name.setObjectName(
                    "levelName"
                )

                recent_meta = QLabel(
                    (
                        recent.get(
                            "level_code",
                            "",
                        ).replace(
                            "LEVEL_",
                            "LEVEL ",
                        )
                        + "  •  "
                        + recent.get(
                            "module_title",
                            "",
                        )
                    )
                )
                recent_meta.setObjectName(
                    "levelDesc"
                )

                recent_text.addWidget(
                    recent_name
                )
                recent_text.addWidget(
                    recent_meta
                )

                recent_layout.addLayout(
                    recent_text,
                    1,
                )

                open_recent = QPushButton(
                    "OCHISH  →"
                )
                open_recent.setObjectName(
                    "openLevelButton"
                )
                open_recent.clicked.connect(
                    lambda checked=False,
                    data=dict(
                        recent
                    ):
                    self.open_lesson_from_summary(
                        data,
                        "home",
                    )
                )

                recent_layout.addWidget(
                    open_recent
                )
                layout.addWidget(
                    recent_card
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
                    "bo'lgan to'liq o'quv yo'li."
                ),
            )

            page.open_level_requested.connect(
                lambda code,
                title,
                subtitle:
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

            # Signal zanjiri ham saqlanadi: callback kelajakda
            # olib tashlansa yoki standalone embedded rejim ishlatilsa,
            # navigatsiya kontrakti yo'qolmaydi.
            page.lesson_open_requested.connect(
                self.open_lesson_page
            )

            page.exam_open_requested.connect(
                self.open_exam_from_learning
            )

            self.show_page(
                key,
                page,
            )

        else:
            page.back_callback = (
                lambda k=source_key:
                self.show_cached(
                    k
                )
            )

            try:
                page._apply_back_button()
            except Exception:
                pass

            self.show_cached(
                key
            )

        # Eng eski Level page'larni tozalash.
        self.trim_level_cache(
            protected_keys={
                key,
            }
        )

    # ========================================================
    # LESSON
    # ========================================================

    def open_lesson_page(
        self,
        lesson_data: dict,
        source_learning_page,
    ):
        """
        Dars ochishning yagona embedded yo'li.

        Source key faqat current_page_key ga bog'lanmaydi:
        haqiqiy LearningPage cache ichidan topiladi. Bu tez
        navigatsiya yoki refresh paytida stale current key sabab
        dars tugmasi javobsiz qolishini oldini oladi.
        """

        if not isinstance(
            lesson_data,
            dict,
        ):
            return

        lesson_id_value = lesson_data.get(
            "id"
        )

        if lesson_id_value is None:
            return

        source_key = next(
            (
                cache_key
                for cache_key, cached_page
                in self.page_cache.items()
                if cached_page
                is source_learning_page
            ),
            self.current_page_key,
        )

        if not source_key:
            source_key = "overview::all"

        lesson_id = str(
            lesson_id_value
        )

        key = (
            "lesson::"
            + lesson_id
        )

        try:
            # Faqat boshqa transient sahifalarni tozalaymiz.
            self.cleanup_transient_pages(
                except_keys={
                    key,
                }
            )

            from ui.embedded_pages import (
                LessonPage,
            )

            try:
                mark_lesson_opened(
                    self.user["id"],
                    int(
                        lesson_id_value
                    ),
                )
            except Exception:
                # Recent-history yozuvi yordamchi funksiya.
                # U ishlamasa ham darsning o'zi ochilishi shart.
                pass

            self.transient_return_keys[
                key
            ] = source_key

            # Shu lesson oldin cache'da qolgan bo'lsa stale widget emas,
            # yangi ma'lumot bilan toza sahifa yaratiladi.
            self.drop_page(
                key
            )

            self.transient_return_keys[
                key
            ] = source_key

            page = LessonPage(
                lesson=dict(
                    lesson_data
                ),
                user=self.user,
                back_callback=(
                    lambda k=source_key,
                    transient_key=key:
                    self.return_from_transient(
                        k,
                        transient_key,
                    )
                ),
                open_quiz_callback=(
                    self.open_quiz_page
                ),
                open_next_lesson_callback=(
                    self.open_next_lesson
                ),
            )

            page.lesson_completed.connect(
                lambda completed_lesson_id,
                source=source_learning_page,
                return_key=source_key,
                lesson_key=key:
                self.lesson_completed(
                    completed_lesson_id,
                    source,
                    return_key,
                    lesson_key,
                )
            )

            self.show_page(
                key,
                page,
            )

        except Exception as exc:
            # Klikning jim qolishi mumkin emas. Foydalanuvchiga
            # tushunarli xabar beriladi va Level sahifasi buzilmaydi.
            QMessageBox.critical(
                self,
                "Darsni ochib bo'lmadi",
                (
                    "Dars sahifasini yuklashda ichki xato yuz berdi.\n\n"
                    f"{exc}"
                ),
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

        self.transient_return_keys[
            key
        ] = lesson_key

        # Lazy import.
        from ui.embedded_pages import (
            QuizPage,
        )

        page = QuizPage(
            user=self.user,
            lesson=lesson,
            back_callback=(
                lambda return_key=lesson_key,
                transient_key=key:
                self.return_from_transient(
                    return_key,
                    transient_key,
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
        lesson_key,
    ):
        """
        Muhim performance fix:

        lesson_finished() o'zi progressni yozib,
        LearningWindow'ni yangilaydi.

        Shuning uchun undan keyin yana
        source_page.refresh_page() chaqirmaymiz.
        """

        source_page.lesson_finished(
            lesson_id
        )

        # Overview progress keyingi kirishda yangilanadi.
        overview_keys = [
            key
            for key in list(
                self.page_cache.keys()
            )
            if key.startswith(
                "overview::"
            )
        ]

        for key in overview_keys:
            self.drop_page(
                key
            )

        self.drop_page(
            "tests"
        )

        self.drop_page(
            "exams"
        )

        self.drop_page(
            "statistics"
        )

        self.drop_page(
            "home"
        )

        # Mini-testdan o'tgach dars sahifasida qolamiz.
        # Foydalanuvchi "KEYINGI DARS" tugmasini ongli bosadi.
        lesson_page = self.page_cache.get(
            lesson_key
        )

        if lesson_page is not None:
            try:
                lesson_page.mark_completed()
            except Exception:
                pass

            self.show_cached(
                lesson_key
            )

            quiz_key = (
                "quiz::"
                + str(
                    lesson_id
                )
            )

            self.transient_return_keys.pop(
                quiz_key,
                None,
            )

            QTimer.singleShot(
                0,
                lambda k=quiz_key:
                self.drop_page(
                    k
                ),
            )

        else:
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

    # ========================================================
    # EXAM FROM LEARNING
    # ========================================================

    def open_exam_from_learning(
        self,
        exam,
        source_page,
    ):
        self.open_exam_page(
            exam,
            self.current_page_key,
        )

    # ========================================================
    # EXAM PAGE
    # ========================================================

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

        self.cleanup_transient_pages()

        # Lazy import.
        from ui.embedded_pages import (
            ExamPage,
        )

        self.transient_return_keys[
            key
        ] = source_key

        page = ExamPage(
            user=self.user,
            exam=exam_data,
            back_callback=(
                lambda return_key=source_key,
                transient_key=key:
                self.return_from_transient(
                    return_key,
                    transient_key,
                )
            ),
        )

        page.exam_passed.connect(
            lambda:
            self.exam_completed()
        )

        self.show_page(
            key,
            page,
        )

    # ========================================================
    # EXAM COMPLETED
    # ========================================================

    def exam_completed(self):
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
                or key.startswith(
                    "exam::"
                )
                or key
                in {
                    "tests",
                    "exams",
                    "statistics",
                    "home",
                }
            ):
                self.drop_page(
                    key
                )

        self.level_page_lru.clear()

        self.open_home()

    # ========================================================
    # LIBRARY
    # ========================================================

    def open_library(self):
        self.set_menu(
            "Kutubxona"
        )

        key = "library"

        page = self.page_cache.get(
            key
        )

        if page is None:
            page = LibraryPage(
                self.user
            )

            page.open_level_requested.connect(
                lambda code,
                title,
                subtitle:
                self.open_single_level(
                    code,
                    title,
                    subtitle,
                    "library",
                )
            )

            page.open_lesson_requested.connect(
                lambda lesson:
                self.open_lesson_from_summary(
                    lesson,
                    "library",
                )
            )

            self.show_page(
                key,
                page,
            )

        else:
            try:
                page.reload_index()
                page.update_results(
                    page.search_input.text()
                )
            except Exception:
                pass

            self.show_cached(
                key
            )

    # ========================================================
    # STATISTICS
    # ========================================================

    def open_statistics(self):
        self.set_menu(
            "Statistika"
        )

        key = "statistics"

        # Har safar real progress.
        self.drop_page(
            key
        )

        page = StatisticsPage(
            self.user
        )

        page.open_level_requested.connect(
            lambda code,
            title,
            subtitle:
            self.open_single_level(
                code,
                title,
                subtitle,
                "statistics",
            )
        )

        self.show_page(
            key,
            page,
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
    # SETTINGS
    # ========================================================

    def open_settings(self):
        self.set_menu(
            "Sozlamalar"
        )

        key = "settings"

        page = self.page_cache.get(
            key
        )

        if page is None:
            page = SettingsPage(
                self.user
            )

            page.clear_cache_requested.connect(
                self.clear_ui_cache
            )

            page.reload_home_requested.connect(
                self.open_home
            )

            page.backup_imported.connect(
                self.refresh_after_backup_import
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
    # CLEAR UI CACHE
    # ========================================================

    def clear_ui_cache(self):
        """
        Faqat RAM/UI cache tozalanadi.

        Database'dagi:
        - progress
        - score
        - XP
        - exam
        - license

        o'zgarmaydi.
        """

        keep_keys = {
            "settings",
        }

        keys = list(
            self.page_cache.keys()
        )

        for key in keys:
            if key in keep_keys:
                continue

            self.drop_page(
                key
            )

        self.level_page_lru.clear()
        self.transient_return_keys.clear()

        # Lazy content registry cache ham tozalanadi.
        try:
            from courses.content_registry import (
                clear_registry_cache,
            )

            clear_registry_cache()

        except Exception:
            # UI cache cleanup registry sabab yiqilmasin.
            pass


    # ========================================================
    # CUSTOMER CONVENIENCE
    # ========================================================

    def install_shortcuts(self):
        shortcut_specs = [
            (
                "Ctrl+K",
                self.open_global_search,
            ),
            (
                "Esc",
                self.smart_back,
            ),
            (
                "Ctrl+Right",
                self.open_next_from_current,
            ),
        ]

        for sequence, callback in shortcut_specs:
            shortcut = QShortcut(
                QKeySequence(
                    sequence
                ),
                self,
            )

            shortcut.setContext(
                Qt.ShortcutContext.ApplicationShortcut
            )

            shortcut.activated.connect(
                callback
            )

            self.shortcuts.append(
                shortcut
            )

    def open_global_search(self):
        self.open_library()

        page = self.page_cache.get(
            "library"
        )

        if page is not None:
            QTimer.singleShot(
                0,
                page.focus_search,
            )

    def smart_back(self):
        current_key = self.current_page_key

        if not current_key:
            return

        return_key = self.transient_return_keys.get(
            current_key
        )

        if return_key:
            self.return_from_transient(
                return_key,
                current_key,
            )

    def open_next_from_current(self):
        current_key = self.current_page_key or ""

        if not current_key.startswith(
            "lesson::"
        ):
            return

        page = self.page_cache.get(
            current_key
        )

        if page is None:
            return

        try:
            if page.next_lesson_button.isEnabled():
                page.open_next_lesson()
        except Exception:
            pass

    def continue_learning(self):
        lesson = get_next_available_lesson(
            self.user["id"]
        )

        if lesson is None:
            self.open_learning_overview()
            return

        self.open_lesson_from_summary(
            lesson,
            "home",
        )

    def open_lesson_from_summary(
        self,
        lesson: dict,
        source_key: str,
    ):
        level_code = str(
            lesson.get(
                "level_code",
                "",
            )
        )

        if not level_code:
            self.open_learning_overview()
            return

        status = str(
            lesson.get(
                "status",
                "available",
            )
        ).lower()

        if (
            not self.is_master
            and status
            not in {
                "available",
                "completed",
            }
        ):
            self.open_single_level(
                level_code,
                lesson.get(
                    "level_title",
                    "",
                ),
                lesson.get(
                    "level_subtitle",
                    "",
                ),
                source_key,
            )
            return

        self.open_single_level(
            level_code,
            lesson.get(
                "level_title",
                "",
            ),
            lesson.get(
                "level_subtitle",
                "",
            ),
            source_key,
        )

        level_key = (
            "level::"
            + level_code
        )

        source_page = self.page_cache.get(
            level_key
        )

        if source_page is None:
            return

        lesson_data = dict(
            lesson
        )

        lesson_data[
            "level_title"
        ] = lesson.get(
            "level_title",
            "",
        )

        lesson_data[
            "module_title"
        ] = lesson.get(
            "module_title",
            "",
        )

        lesson_data[
            "master_mode"
        ] = self.is_master

        self.open_lesson_page(
            lesson_data,
            source_page,
        )

    def open_next_lesson(
        self,
        lesson_page,
    ):
        next_lesson = get_next_available_lesson(
            self.user["id"]
        )

        if next_lesson is None:
            return_key = self.transient_return_keys.get(
                self.current_page_key,
                "overview::all",
            )

            if not self.show_cached(
                return_key
            ):
                self.open_learning_overview()

            return

        current_id = int(
            lesson_page.lesson.get(
                "id",
                0,
            )
        )

        if int(
            next_lesson.get(
                "id",
                0,
            )
        ) == current_id:
            return

        source_key = self.transient_return_keys.get(
            self.current_page_key,
            "overview::all",
        )

        self.open_lesson_from_summary(
            next_lesson,
            source_key,
        )

    def open_glossary(self):
        self.set_menu(
            "Terminlar lug'ati"
        )

        key = "glossary"
        page = self.page_cache.get(
            key
        )

        if page is None:
            page = GlossaryPage()

            self.show_page(
                key,
                page,
            )
        else:
            self.show_cached(
                key
            )

    def open_help(self):
        self.set_menu(
            "Yordam"
        )

        key = "help"
        page = self.page_cache.get(
            key
        )

        if page is None:
            page = HelpPage()

            self.show_page(
                key,
                page,
            )
        else:
            self.show_cached(
                key
            )

    def refresh_after_backup_import(self):
        keep = {
            "settings",
        }

        for key in list(
            self.page_cache.keys()
        ):
            if key not in keep:
                self.drop_page(
                    key
                )

        self.level_page_lru.clear()
        self.transient_return_keys.clear()
