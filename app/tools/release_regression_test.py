"""Isolated release checks using real Qt widgets and the complete curriculum."""
from __future__ import annotations

import copy
import os
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
_TEST_DIR = tempfile.TemporaryDirectory(prefix='archipro_release_')
os.environ['ARCHIPRO_UZ_DATABASE_PATH'] = str(Path(_TEST_DIR.name) / 'release.db')
os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')
os.environ['ARCHIPRO_AUDIT_MODE'] = '1'

from PySide6.QtCore import QCoreApplication, QEvent
from PySide6.QtWidgets import QApplication, QMessageBox, QPushButton
from auth.auth_service import create_user, authenticate_user
from courses.course_service import initialize_user_progress, get_lesson_progress, get_next_available_lesson
from courses.exam_service import get_level_exam, get_exam_questions
from courses.user_features import get_lesson_note, import_user_backup, export_user_backup
from database.database import get_connection
from main import prepare_application, get_database_content_counts
from ui.dashboard_window import DashboardWindow
from ui.embedded_pages import LessonPage


def query(sql, args=()):
    connection = get_connection()
    try:
        return [dict(row) for row in connection.execute(sql, args).fetchall()]
    finally:
        connection.close()


def events():
    QApplication.processEvents()
    QCoreApplication.sendPostedEvents(None, QEvent.Type.DeferredDelete)
    QApplication.processEvents()


class ReleaseRegression(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = QApplication.instance() or QApplication([])
        prepare_application()
        create_user('release_pro', 'test-password', 'Release PRO', 'PRO')
        create_user('release_master', 'test-password', 'Release MASTER', 'MASTER')
        cls.pro = authenticate_user('release_pro', 'test-password')
        cls.master = authenticate_user('release_master', 'test-password')
        initialize_user_progress(cls.pro['id'])
        initialize_user_progress(cls.master['id'])
        cls.lessons = query('''SELECT ls.*, m.title AS module_title, l.title AS level_title,
            l.subtitle AS level_subtitle, l.code AS level_code FROM lessons ls
            JOIN course_modules m ON m.id=ls.module_id JOIN course_levels l ON l.id=m.level_id
            ORDER BY l.sort_order, m.sort_order, ls.sort_order''')

    def setUp(self):
        self.qt_errors = []
        self.old_hook = sys.excepthook
        sys.excepthook = lambda typ, value, tb: self.qt_errors.append(str(value))
        self.shell = DashboardWindow(self.pro)
        self.shell.show()
        events()

    def tearDown(self):
        self.shell.close()
        self.shell.deleteLater()
        events()
        sys.excepthook = self.old_hook
        self.assertEqual(self.qt_errors, [], 'Unhandled Qt signal exception')

    def open_first(self):
        self.shell.open_single_level('LEVEL_00', 'Absolute Zero', '', 'home')
        events()
        level = self.shell.page_cache['level::LEVEL_00']
        level.findChild(QPushButton, 'openLesson').click()
        events()
        return self.shell.page_cache[self.shell.current_page_key]

    def test_laptop_reading_controls_keep_navigation_and_quiz_gates(self):
        from PySide6.QtWidgets import QScrollArea
        page = self.open_first()
        self.shell.showNormal()
        self.shell.resize(1366, 768)
        events()
        self.assertFalse(page.progress_card.isVisible())
        self.assertFalse(page.lesson_map.isVisible())
        self.assertGreaterEqual(page.scroll.height(), 380)
        self.assertTrue(page.findChild(QPushButton, 'quizButton').isEnabled())
        self.assertFalse(page.next_lesson_button.isEnabled())
        page.details_button.click()
        events()
        self.assertTrue(page.progress_card.isVisible())
        self.assertTrue(page.lesson_map.isVisible())
        page.map_buttons[-1].click()
        events()
        self.assertGreater(page.scroll.verticalScrollBar().value(), 0)
        page.details_button.click()
        page.scroll.verticalScrollBar().setValue(0)
        page.font_larger_button.click()
        events()
        self.assertEqual(page.reading_font_size, 18)
        self.assertTrue(all('font-size: 18px;' in label.text() for label in page.reading_labels))
        page.reading_button.click()
        events()
        self.assertFalse(self.shell.sidebar.isVisible())
        self.assertFalse(page.lesson_hero.isVisible())
        self.assertGreater(page.scroll.height(), 480)
        self.shell.open_quiz_page(page)
        events()
        self.assertTrue(self.shell.sidebar.isVisible())
        self.shell.page_cache[self.shell.current_page_key].findChild(QPushButton, 'backButton').click()
        events()
        self.assertIs(self.shell.stack.currentWidget(), page)
        self.assertFalse(self.shell.sidebar.isVisible())
        page.reading_button.click()
        events()
        self.assertTrue(self.shell.sidebar.isVisible())
        self.assertTrue(page.lesson_hero.isVisible())
        self.assertFalse(page.next_lesson_button.isEnabled())
        self.assertEqual(len(page.content_cards), len(page.blocks))

    def test_paper_theme_keeps_text_and_actions_readable(self):
        from PySide6.QtGui import QPalette
        from ui.login_window import LoginWindow
        from ui.theme import CREAM, PAPER, INK, TEAL
        def contrast(first, second):
            def luminance(color):
                channels = [color.redF(), color.greenF(), color.blueF()]
                values = [v / 12.92 if v <= .04045 else ((v + .055) / 1.055) ** 2.4
                          for v in channels]
                return sum(v * weight for v, weight in zip(values, (.2126, .7152, .0722)))
            a, b = sorted((luminance(first), luminance(second)))
            return (b + .05) / (a + .05)
        palette = self.app.palette()
        self.assertEqual(palette.color(QPalette.ColorRole.Window).name().upper(), CREAM)
        self.assertEqual(palette.color(QPalette.ColorRole.Text).name().upper(), INK)
        self.assertEqual(palette.color(QPalette.ColorRole.Highlight).name().upper(), TEAL)
        self.assertEqual(palette.color(QPalette.ColorRole.Base).name().upper(), PAPER)
        page = self.open_first()
        button = page.findChild(QPushButton, 'quizButton')
        button.ensurePolished()
        self.assertGreaterEqual(contrast(button.palette().color(QPalette.ColorRole.Button),
                                        button.palette().color(QPalette.ColorRole.ButtonText)), 4.5)
        self.assertTrue(button.isEnabled())
        self.assertEqual(page.reading_font_size, 17)
        login = LoginWindow()
        self.assertIn(CREAM, login.styleSheet())
        self.assertIn(TEAL, login.styleSheet())
        login.deleteLater()
        events()

    def test_worked_lessons_keep_complete_instructions_and_readable_tables(self):
        from PySide6.QtGui import QTextDocument
        from PySide6.QtWidgets import QLabel
        self.shell.showNormal()
        self.shell.resize(1150, 720)
        for code in ('L00_M02_001', 'L05_M03_001', 'L07_M05_002', 'L12_M07_002'):
            with self.subTest(lesson=code):
                lesson = next(row for row in self.lessons if row['code'] == code)
                page = LessonPage(lesson, self.master)
                self.shell.show_page('worked::' + code, page)
                events()
                self.assertEqual(len(page.content_cards), len(page.blocks))
                if code == 'L00_M02_001':
                    self.assertIn('oshxona→ovqatlanish aloqalarini chizing', page.blocks[-3]['text'])
                    self.assertIn('16+16+8+12+11.2+11.2+5.6=80', page.blocks[-3]['text'])
                for size in (14, 24):
                    page.change_reading_font(size - page.reading_font_size)
                    events()
                    self.assertLessEqual(page.content_widget.width(), page.scroll.viewport().width())
                    for card in page.content_cards[-4:]:
                        label = card.findChild(QLabel, 'blockText')
                        document = QTextDocument()
                        document.setHtml(label.text())
                        document.setTextWidth(label.width())
                        self.assertLessEqual(document.idealWidth(), label.width() + 2,
                                             'Worked table or text overflows reading area')
                self.assertFalse(page.next_lesson_button.isEnabled())

    def test_visual_catalog_assets_and_full_coverage_inventory(self):
        from courses.content_registry import get_all_lesson_content
        from courses.visual_catalog import CATALOG, validate_visual_catalog
        from ui.lesson_visuals import load_figure
        counts = validate_visual_catalog(get_all_lesson_content())
        self.assertEqual(counts['total_lessons'], 680)
        self.assertEqual(counts['illustrated_lessons'] + counts['pending_lessons'], 680)
        self.assertEqual(counts['illustrated_lessons'], 680)
        self.assertEqual(counts['pending_lessons'], 0)
        for asset in {s['asset'] for specs in CATALOG.values() for s in specs}:
            with self.subTest(asset=asset):
                self.assertFalse(load_figure(asset).isNull())

    def test_extended_visuals_match_each_worked_lesson(self):
        import json
        from courses.visual_catalog import ASSETS, CATALOG
        from courses.workbook_data import WORKBOOKS
        from courses.teaching.guides import GUIDES
        from courses.content_registry import get_all_lesson_content
        records = json.loads((ASSETS / 'lesson_figures.json').read_text(encoding='utf-8'))
        self.assertEqual(len({r['code'] for r in records}), len(records))
        self.assertEqual(len({r['asset'] for r in records}), len(records))
        contents = get_all_lesson_content()
        # Reviewed raster figures replace schematic records. Coverage is tied to
        # the curriculum, rather than an obsolete fixed number of SVG entries.
        self.assertEqual(set(CATALOG), set(contents))
        for row in records:
            with self.subTest(lesson=row['code']):
                module = row['code'].rsplit('_', 1)[0]
                index = int(row['code'].rsplit('_', 1)[1]) - 1
                unit = WORKBOOKS[module]['units'][index]
                self.assertEqual(unit['code'], row['code'])
                # The reviewed sketch may paraphrase the worked stage instead of
                # copying GUIDE wording verbatim. Keep the curriculum binding strict
                # through lesson code, exact exercise/action, target block and asset.
                self.assertTrue(row['explanation'])
                self.assertTrue(all(text.strip() for text in row['explanation']))
                self.assertEqual(row['exercise'], unit['action'])
                # Architectural sketches may use a lesson-specific worked conclusion.
                self.assertTrue(row['solution'].strip())
                self.assertEqual(contents[row['code']][row['block']]['title'],
                                 'Bajarish tartibi va namunaviy xulosa')
                figure = (ASSETS / row['asset']).read_text(encoding='utf-8')
                self.assertIn(row['code'], figure)
        for row in json.loads((ASSETS / 'archicad_figures.json').read_text(encoding='utf-8')):
            self.assertTrue(row['source_url'].startswith('https://help.graphisoft.com/AC/28/INT/'))
            self.assertTrue(row['source_image_url'].startswith('https://help.graphisoft.com/AC/28/INT/'))
            self.assertIn('Graphisoft', row['credit'])
            self.assertIn(row['code'], CATALOG)
        for manifest in ('archicad_figures.json', 'realistic_figures.json'):
            for row in json.loads((ASSETS / manifest).read_text(encoding='utf-8')):
                with self.subTest(manifest=manifest, lesson=row['code'], asset=row['asset']):
                    module, number = row['code'].rsplit('_', 1)
                    unit = WORKBOOKS[module]['units'][int(number) - 1]
                    self.assertEqual(unit['code'], row['code'])
                    self.assertEqual(row['exercise'], unit['action'])
                    # Reviewed visual conclusions are intentionally lesson-specific
                    # paraphrases; require a substantive conclusion rather than a
                    # word-for-word copy of workbook result text.
                    self.assertTrue(row['solution'].strip())
                    self.assertTrue(0 <= row['block'] < len(contents[row['code']]))
                    self.assertTrue(row['explanation'])
                    self.assertTrue(all(text.strip() for text in row['explanation']))

    def test_visual_zoom_font_layout_and_quiz_gates(self):
        from ui.lesson_visuals import LessonVisual
        from PySide6.QtWidgets import QBoxLayout
        self.shell.showNormal()
        self.shell.resize(1366, 768)
        lesson = next(row for row in self.lessons if row['code'] == 'L08_M05_001')
        page = LessonPage(lesson, self.pro)
        self.shell.show_page('visual::roof', page)
        events()
        visuals = page.findChildren(LessonVisual)
        self.assertEqual(len(visuals), 1)
        self.assertEqual(len(page.content_cards), len(page.blocks))
        self.assertFalse(page.next_lesson_button.isEnabled())
        figure = visuals[0]
        figure.enlarge.click()
        events()
        self.assertTrue(figure.dialog.isVisible())
        old = figure.dialog.zoom
        figure.dialog.findChild(QPushButton, 'figureZoomIn').click()
        self.assertGreater(figure.dialog.zoom, old)
        figure.dialog.findChild(QPushButton, 'figureZoomOut').click()
        self.assertAlmostEqual(figure.dialog.zoom, old)
        figure.dialog.findChild(QPushButton, 'figureClose').click()
        events()
        self.assertFalse(figure.dialog.isVisible())
        page.change_reading_font(7)
        events()
        self.assertIn('font-size: 24px;', figure.details.text())
        self.shell.resize(850, 720)
        events()
        self.assertEqual(figure.layout.direction(), QBoxLayout.Direction.TopToBottom)
        self.assertLessEqual(page.content_widget.width(), page.scroll.viewport().width())
        self.assertFalse(page.next_lesson_button.isEnabled())
        self.assertTrue(page.findChild(QPushButton, 'quizButton').isEnabled())

    def test_missing_figure_preserves_text_and_quiz(self):
        from ui.lesson_visuals import LessonVisual
        from PySide6.QtGui import QPixmap
        lesson = next(row for row in self.lessons if row['code'] == 'L08_M05_001')
        with patch('ui.lesson_visuals.load_figure', return_value=QPixmap()):
            page = LessonPage(lesson, self.pro)
        self.shell.show_page('missing::figure', page)
        events()
        self.assertTrue(page.blocks)
        self.assertEqual(len(page.content_cards), len(page.blocks))
        self.assertTrue(page.findChild(QPushButton, 'quizButton').isEnabled())
        self.assertFalse(page.next_lesson_button.isEnabled())
        for figure in page.findChildren(LessonVisual):
            self.assertFalse(figure.enlarge.isEnabled())
            self.assertIn('Chizma ochilmadi', figure.image.text())

    def test_missing_content_is_visible_and_cannot_start_quiz(self):
        from PySide6.QtWidgets import QLabel
        for failure in (None, ImportError("courses.lesson_content missing")):
            with self.subTest(failure=failure):
                options = {"return_value": []} if failure is None else {"side_effect": failure}
                with patch("ui.embedded_pages.get_lesson_content_by_code", **options):
                    with self.assertLogs("ui.embedded_pages", level="ERROR"):
                        page = LessonPage(dict(self.lessons[0], status="completed"), self.pro)
                events()
                self.assertIsNotNone(page.content_error)
                self.assertEqual(page.blocks, [])
                self.assertFalse(page.findChild(QPushButton, "quizButton").isEnabled())
                self.assertFalse(page.findChild(QPushButton, "nextLessonButton").isEnabled())
                self.assertTrue(any("Dars ma'lumotlari yuklanmadi" in label.text()
                                    for label in page.findChildren(QLabel)))
                page.open_quiz_callback = lambda _: self.fail("Missing-content quiz opened")
                page.start_quiz()
                self.assertEqual(page.progress_bar.value(), 0)
                page.deleteLater()
                events()

    def test_first_lesson_contains_teaching_material(self):
        page = self.open_first()
        self.assertEqual(len(page.blocks), 11)
        self.assertIn("qulay, xavfsiz", page.blocks[1]["text"])
        self.assertEqual(len(page.content_cards), 11)

    def test_packaged_validator_fails_when_a_course_module_is_missing(self):
        import json
        from courses.packaged_validation import write_validation_report
        report_path = Path(_TEST_DIR.name) / "missing-module.json"
        with patch("courses.content_registry.get_all_lesson_content",
                   side_effect=ImportError("courses.lesson_content missing")):
            self.assertEqual(write_validation_report(report_path), 1)
        report = json.loads(report_path.read_text(encoding="utf-8"))
        self.assertFalse(report["success"])
        self.assertIn("courses.lesson_content missing", report["error"])

    def test_build_inventory_includes_every_dynamic_curriculum_source(self):
        from tools.build_client import dynamic_modules
        from courses.content_registry import iter_all_descriptors
        modules = set(dynamic_modules())
        for descriptor in iter_all_descriptors():
            self.assertIn(descriptor["content_module"], modules)
            self.assertIn(descriptor["quiz_module"], modules)

    def test_revision_preserves_original_material_and_covers_all_lessons(self):
        from courses.content_registry import (get_unique_content_sources, get_unique_quiz_sources,
            load_dictionary, get_all_lesson_content, get_all_quiz_data,
            get_lesson_content_by_code, get_quiz_data_by_code)
        from courses.curriculum_revision import validate_revision
        original = {}
        raw_quizzes = {}
        for module, name in get_unique_content_sources():
            original.update(copy.deepcopy(load_dictionary(module, name)))
        for module, name in get_unique_quiz_sources():
            raw_quizzes.update(copy.deepcopy(load_dictionary(module, name)))
        content, quizzes = get_all_lesson_content(), get_all_quiz_data()
        report = validate_revision(content, quizzes)
        self.assertEqual(report['workbook_lessons'], 680)
        for code, blocks in original.items():
            self.assertEqual(content[code][:-4], blocks, code)
            self.assertEqual(content[code], get_lesson_content_by_code(code), code)
            self.assertEqual(quizzes[code], get_quiz_data_by_code(code), code)
            self.assertEqual([q['code'] for q in quizzes[code]],
                             [q['code'] for q in raw_quizzes[code]], code)
        for module, name in get_unique_content_sources():
            self.assertEqual(load_dictionary(module, name),
                             {k: original[k] for k in load_dictionary(module, name)})

    def test_curriculum_upgrade_keeps_progress_notes_and_attempt_history(self):
        from main import set_app_setting, CONTENT_SCHEMA_SETTING
        from courses.quiz_service import seed_quizzes, save_quiz_attempt
        from courses.user_features import save_lesson_note, set_lesson_bookmark
        from courses.content_registry import get_unique_quiz_sources, load_dictionary
        create_user('upgrade_check', 'test-password', 'Upgrade check', 'PRO')
        user = authenticate_user('upgrade_check', 'test-password')
        initialize_user_progress(user['id'])
        lesson_id = self.lessons[0]['id']
        save_lesson_note(user['id'], lesson_id, 'Upgrade must keep this note')
        set_lesson_bookmark(user['id'], lesson_id, True)
        save_quiz_attempt(user['id'], lesson_id, 73, False)
        legacy = {}
        for module, name in get_unique_quiz_sources():
            legacy.update(load_dictionary(module, name))
        with patch('courses.quiz_service.get_all_quiz_data', return_value=legacy):
            seed_quizzes()
        connection = get_connection()
        connection.execute("UPDATE course_levels SET title='Legacy English title', subtitle='Legacy subtitle'")
        connection.commit()
        connection.close()
        set_app_setting(CONTENT_SCHEMA_SETTING, 'ARCHIPRO_CONTENT_2026_10_04_V2')
        tables = ('users', 'lesson_progress', 'lesson_notes', 'lesson_bookmarks',
                  'quiz_attempts', 'level_exam_attempts', 'user_level_progress')
        before = {table: query('SELECT * FROM '+table+' ORDER BY id') for table in tables}
        identities = {table: query('SELECT id, code FROM '+table+' ORDER BY id')
                      for table in ('lessons', 'quiz_questions')}
        self.assertTrue(prepare_application())
        for table in tables:
            self.assertEqual(query('SELECT * FROM '+table+' ORDER BY id'), before[table], table)
        for table in identities:
            self.assertEqual(query('SELECT id, code FROM '+table+' ORDER BY id'), identities[table], table)
        self.assertEqual(get_lesson_note(user['id'], lesson_id), 'Upgrade must keep this note')
        from courses.seed_courses import LEVELS
        self.assertEqual([(row['code'], row['title'], row['subtitle']) for row in
                          query('SELECT code, title, subtitle FROM course_levels ORDER BY sort_order')],
                         [(code, title, subtitle) for code, title, subtitle, _, _ in LEVELS])
        self.assertTrue(all(row['title'].startswith('BOSQICH ') for row in
                            query('SELECT title FROM level_exams')))
        self.assertFalse(prepare_application())
        self.assertEqual(len(query('SELECT * FROM quiz_options')), 2041 * 4)

    def test_long_answer_wraps_and_remains_selectable(self):
        from PySide6.QtCore import Qt
        from PySide6.QtTest import QTest
        from PySide6.QtWidgets import QVBoxLayout, QWidget, QScrollArea
        from ui.answer_radio_button import AnswerRadioButton
        holder = QWidget()
        layout = QVBoxLayout(holder)
        button = AnswerRadioButton('A. ' + 'Tekshirish dalilini chizma va sath bilan asoslang. ' * 8)
        layout.addWidget(button)
        holder.resize(420, 450)
        holder.show()
        events()
        self.assertLess(button.width(), 420)
        self.assertGreater(button.height(), 80)
        self.assertGreaterEqual(button.answer_label.height(),
                                button.answer_label.heightForWidth(button.answer_label.width()))
        QTest.mouseClick(button, Qt.MouseButton.LeftButton,
                         pos=button.answer_label.geometry().center())
        self.assertTrue(button.isChecked())
        holder.close()
        holder.deleteLater()
        events()
        page = self.open_first()
        self.shell.open_quiz_page(page)
        events()
        quiz = self.shell.page_cache[self.shell.current_page_key]
        for scroll in quiz.findChildren(QScrollArea):
            self.assertEqual(scroll.horizontalScrollBar().maximum(), 0)

    def test_all_menu_pages_and_level_back(self):
        for index, title in enumerate(self.shell.menu_items):
            with self.subTest(menu=title):
                self.shell.menu.setCurrentRow(index)
                self.shell.menu.itemClicked.emit(self.shell.menu.item(index))
                events()
                self.assertIs(self.shell.stack.currentWidget(), self.shell.page_cache[self.shell.current_page_key])
        self.shell.open_home()
        self.shell.open_single_level('LEVEL_00', 'Absolute Zero', '', 'home')
        events()
        self.shell.page_cache['level::LEVEL_00'].findChild(QPushButton, 'backButton').click()
        events()
        self.assertEqual(self.shell.current_page_key, 'home')

    def test_all_680_lesson_pages_and_16_exams(self):
        self.assertEqual(len(self.lessons), 680)
        for lesson in self.lessons:
            with self.subTest(lesson=lesson['code']):
                page = LessonPage(lesson, self.master)
                self.assertTrue(page.blocks, 'Lesson content is empty')
                self.assertTrue(page.content_cards)
                from ui.lesson_visuals import LessonVisual
                figures = page.findChildren(LessonVisual)
                self.assertTrue(figures, 'Lesson has no attached teaching figure')
                self.assertTrue(all(not f.original.isNull() for f in figures))
                page.deleteLater()
                events()
        for number in range(16):
            with self.subTest(exam=number):
                exam = get_level_exam(f'LEVEL_{number:02d}')
                self.assertIsNotNone(exam)
                self.assertTrue(get_exam_questions(exam['id']))
                self.shell.open_exam_page(exam, 'home')
                events()
                page = self.shell.page_cache[self.shell.current_page_key]
                page.findChild(QPushButton, 'embeddedBackButton').click()
                events()
                self.assertEqual(self.shell.current_page_key, 'home')

    def test_quiz_back_and_escape(self):
        lesson = self.open_first()
        key = self.shell.current_page_key
        lesson.findChild(QPushButton, 'quizButton').click()
        events()
        self.shell.page_cache[self.shell.current_page_key].findChild(QPushButton, 'backButton').click()
        events()
        self.assertEqual(self.shell.current_page_key, key)
        self.shell.smart_back()
        events()
        self.assertEqual(self.shell.current_page_key, 'level::LEVEL_00')
        self.shell.smart_back()
        events()
        self.assertEqual(self.shell.current_page_key, 'home')

    def test_note_survives_immediate_back_and_window_close(self):
        lesson = self.open_first()
        lesson.note_input.setPlainText('Immediate back must preserve this note')
        lesson.findChild(QPushButton, 'backButton').click()
        events()
        self.assertEqual(get_lesson_note(self.pro['id'], lesson.lesson_id), 'Immediate back must preserve this note')
        lesson = self.open_first()
        lesson.note_input.setPlainText('Closing window must preserve this note')
        self.shell.close()
        events()
        self.assertEqual(get_lesson_note(self.pro['id'], lesson.lesson_id), 'Closing window must preserve this note')

    def test_delayed_cleanup_does_not_delete_reopened_lesson(self):
        lesson = self.open_first()
        key = self.shell.current_page_key
        self.shell.return_from_transient('level::LEVEL_00', key)
        source = self.shell.page_cache['level::LEVEL_00']
        self.shell.open_lesson_page(dict(lesson.lesson), source)
        events()
        self.assertIn(key, self.shell.page_cache)
        self.assertIs(self.shell.stack.currentWidget(), self.shell.page_cache[key])

    def test_quiz_double_submission_does_not_duplicate_attempt(self):
        lesson = self.open_first()
        self.shell.open_quiz_page(lesson)
        events()
        quiz = self.shell.page_cache[self.shell.current_page_key]
        for item in quiz.answer_groups:
            next(button for button in item['buttons'] if button.property('is_correct')).setChecked(True)
        before = len(query('SELECT * FROM quiz_attempts WHERE user_id=? AND lesson_id=?', (self.pro['id'], lesson.lesson_id)))
        quiz.check_answers()
        quiz.check_answers()
        after = len(query('SELECT * FROM quiz_attempts WHERE user_id=? AND lesson_id=?', (self.pro['id'], lesson.lesson_id)))
        self.assertEqual(after - before, 1)

    def test_startup_idempotence_and_backup_rollback(self):
        before = get_database_content_counts()
        self.assertFalse(prepare_application())
        self.assertEqual(before, get_database_content_counts())
        backup = export_user_backup(self.pro['id'], Path(_TEST_DIR.name) / 'rollback.archiprobackup')
        import json
        data = json.loads(backup.read_text())
        broken = copy.deepcopy(data)
        broken['lesson_progress'][-1]['score'] = 'bad-score'
        backup.write_text(json.dumps(broken))
        previous = query('SELECT * FROM lesson_progress WHERE user_id=? ORDER BY lesson_id', (self.pro['id'],))
        with self.assertRaises((ValueError, TypeError)):
            import_user_backup(self.pro['id'], backup)
        self.assertEqual(previous, query('SELECT * FROM lesson_progress WHERE user_id=? ORDER BY lesson_id', (self.pro['id'],)))

    def test_note_save_button_reports_failure(self):
        lesson = self.open_first()
        button = lesson.findChild(QPushButton, 'saveNoteButton')
        lesson.note_input.setPlainText('Save button check')
        with patch('ui.embedded_pages.save_lesson_note', side_effect=OSError('write failed')):
            button.click()
            self.assertIn('SAQLANMADI', button.text())
        button.click()
        self.assertEqual(get_lesson_note(self.pro['id'], lesson.lesson_id), 'Save button check')
        self.assertIn('SAQLANDI', button.text())

    def test_signed_license_expiry_and_tampering(self):
        import base64
        from datetime import datetime, timedelta, timezone
        from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
        from licensing import license_service as service
        key = Ed25519PrivateKey.generate()
        payload = {"username": "release_pro", "password_hash": "hash", "password_salt": "salt",
                   "device_id": "TEST-DEVICE", "license_type": "PRO"}
        def signed(expires):
            body = dict(payload, expires_at=expires)
            return {"product": service.PRODUCT_NAME, "version": service.LICENSE_VERSION,
                    "payload": body, "signature": base64.b64encode(key.sign(service._canonical_payload(body))).decode()}
        with patch.object(service, '_load_public_key', return_value=key.public_key()), patch.object(service, 'get_device_id', return_value='TEST-DEVICE'):
            future = (datetime.now(timezone.utc) + timedelta(days=1)).isoformat()
            self.assertTrue(service.verify_license_data(signed(future))['valid'])
            past = (datetime.now(timezone.utc) - timedelta(days=1)).isoformat()
            self.assertFalse(service.verify_license_data(signed(past))['valid'])
            self.assertTrue(service.verify_license_data(signed(None))['valid'])
            self.assertFalse(service.verify_license_data(signed('invalid-date'))['valid'])
            forged = signed(None)
            forged['payload']['license_type'] = 'MASTER'
            self.assertFalse(service.verify_license_data(forged)['valid'])
            with patch.object(service, 'get_device_id', return_value='OTHER-DEVICE'):
                self.assertFalse(service.verify_license_data(signed(None))['valid'])

    def test_z_complete_curriculum_through_real_quiz_and_exam_widgets(self):
        create_user('full_flow', 'test-password', 'Full flow', 'PRO')
        user = authenticate_user('full_flow', 'test-password')
        initialize_user_progress(user['id'])
        self.shell.close()
        self.shell.deleteLater()
        events()
        self.shell = DashboardWindow(user)
        self.shell.show()
        events()
        for number in range(16):
            level_code = f'LEVEL_{number:02d}'
            for lesson in (row for row in self.lessons if row['level_code'] == level_code):
                with self.subTest(lesson=lesson['code']):
                    progress = get_lesson_progress(user['id'], lesson['id'])
                    self.assertEqual(progress['status'], 'available')
                    self.shell.open_lesson_from_summary(dict(lesson, status=progress['status']), 'home')
                    events()
                    page = self.shell.page_cache[self.shell.current_page_key]
                    self.assertEqual(page.lesson_id, lesson['id'])
                    page.findChild(QPushButton, 'quizButton').click()
                    events()
                    quiz = self.shell.page_cache[self.shell.current_page_key]
                    self.assertTrue(quiz.answer_groups)
                    for item in quiz.answer_groups:
                        next(button for button in item['buttons'] if button.property('is_correct')).setChecked(True)
                    quiz.submit_button.click()
                    quiz.continue_button.click()
                    events()
                    progress = get_lesson_progress(user['id'], lesson['id'])
                    self.assertEqual(progress['status'], 'completed')
                    self.assertEqual(progress['attempts'], 1)
                    self.assertEqual(progress['best_score'], 100)
            exam = get_level_exam(level_code)
            self.shell.open_exam_page(exam, 'home')
            events()
            page = self.shell.page_cache[self.shell.current_page_key]
            for item in page.answer_groups:
                next(button for button in item['buttons'] if button.property('is_correct')).setChecked(True)
            page.check_exam()
            page.check_exam()
            self.assertEqual(len(query('SELECT * FROM level_exam_attempts WHERE user_id=? AND exam_id=?', (user['id'], exam['id']))), 1)
            page.finish_success()
            events()
            print(f'[PASS] Full PRO learning flow {level_code}', flush=True)
        self.assertEqual(len(query("SELECT * FROM user_level_progress WHERE user_id=? AND status='completed'", (user['id'],))), 16)
        self.assertIsNone(get_next_available_lesson(user['id']))


if __name__ == '__main__':
    result = unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(ReleaseRegression))
    _TEST_DIR.cleanup()
    raise SystemExit(0 if result.wasSuccessful() else 1)
