from __future__ import annotations

import sys
import traceback
from collections import Counter
from pathlib import Path
from typing import Any


# ============================================================
# PATH SETUP
# ============================================================

CURRENT_FILE = Path(__file__).resolve()
TOOLS_DIR = CURRENT_FILE.parent
APP_DIR = TOOLS_DIR.parent

if str(APP_DIR) not in sys.path:
    sys.path.insert(0, str(APP_DIR))


# ============================================================
# IMPORTS
# ============================================================

from database.database import (
    get_connection,
    initialize_database,
)

from courses.seed_courses import (
    seed_course_structure,
)

from courses.quiz_service import (
    seed_quizzes,
)

from courses.exam_service import (
    seed_level_exams,
)

from courses.content_registry import (
    get_all_lesson_content,
    get_all_quiz_data,
)

from main import (
    MODULE_SEEDERS,
    CUSTOM_EXAM_SEEDERS,
)


# ============================================================
# COLORS
# ============================================================

RESET = "\033[0m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
CYAN = "\033[96m"
BOLD = "\033[1m"


# ============================================================
# EXPECTED STRUCTURE
# ============================================================

EXPECTED_LEVEL_CODES = [
    f"LEVEL_{number:02d}"
    for number in range(16)
]


EXPECTED_MODULE_COUNTS = {
    "LEVEL_00": 5,
    "LEVEL_01": 6,
    "LEVEL_02": 10,
    "LEVEL_03": 8,
    "LEVEL_04": 8,
    "LEVEL_05": 10,
    "LEVEL_06": 10,
    "LEVEL_07": 9,
    "LEVEL_08": 9,
    "LEVEL_09": 8,
    "LEVEL_10": 11,
    "LEVEL_11": 9,
    "LEVEL_12": 10,
    "LEVEL_13": 8,
    "LEVEL_14": 8,
    "LEVEL_15": 8,
}


EXPECTED_TOTAL_MODULES = sum(
    EXPECTED_MODULE_COUNTS.values()
)


EXPECTED_CUSTOM_EXAM_LEVELS = {
    f"LEVEL_{number:02d}"
    for number in range(2, 16)
}


# ============================================================
# RESULTS
# ============================================================

ERRORS: list[str] = []
WARNINGS: list[str] = []
PASSES: list[str] = []

SEED_ERRORS: list[str] = []


# ============================================================
# HELPERS
# ============================================================

def add_pass(message: str) -> None:
    PASSES.append(message)
    print(
        f"{GREEN}[PASS]{RESET} {message}"
    )


def add_warning(message: str) -> None:
    WARNINGS.append(message)
    print(
        f"{YELLOW}[WARN]{RESET} {message}"
    )


def add_error(message: str) -> None:
    ERRORS.append(message)
    print(
        f"{RED}[ERROR]{RESET} {message}"
    )


def section(title: str) -> None:
    print()
    print(
        f"{BOLD}{CYAN}"
        f"{'=' * 76}"
        f"{RESET}"
    )
    print(
        f"{BOLD}{CYAN}"
        f"{title}"
        f"{RESET}"
    )
    print(
        f"{BOLD}{CYAN}"
        f"{'=' * 76}"
        f"{RESET}"
    )


def row_value(
    row: Any,
    key: str,
    index: int | None = None,
):
    if row is None:
        return None

    try:
        return row[key]

    except (
        TypeError,
        KeyError,
        IndexError,
    ):
        pass

    if index is not None:
        try:
            return row[index]

        except (
            TypeError,
            IndexError,
        ):
            pass

    return None


def table_exists(
    cursor,
    table_name: str,
) -> bool:

    cursor.execute(
        """
        SELECT name
        FROM sqlite_master
        WHERE type = 'table'
          AND name = ?
        LIMIT 1
        """,
        (table_name,),
    )

    return (
        cursor.fetchone()
        is not None
    )


def get_table_columns(
    cursor,
    table_name: str,
) -> list[str]:

    cursor.execute(
        f"PRAGMA table_info({table_name})"
    )

    rows = cursor.fetchall()

    columns: list[str] = []

    for row in rows:
        name = row_value(
            row,
            "name",
            1,
        )

        if name:
            columns.append(name)

    return columns


def get_unique_indexes(
    cursor,
    table_name: str,
) -> list[tuple[str, list[str]]]:

    cursor.execute(
        f"PRAGMA index_list({table_name})"
    )

    rows = cursor.fetchall()

    result = []

    for row in rows:
        index_name = row_value(
            row,
            "name",
            1,
        )

        is_unique = row_value(
            row,
            "unique",
            2,
        )

        if not index_name:
            continue

        if not is_unique:
            continue

        cursor.execute(
            f"PRAGMA index_info({index_name})"
        )

        info_rows = cursor.fetchall()

        columns = []

        for info_row in info_rows:
            column_name = row_value(
                info_row,
                "name",
                2,
            )

            if column_name:
                columns.append(
                    column_name
                )

        result.append(
            (
                index_name,
                columns,
            )
        )

    return result


def run_seeder(
    seeder,
    label: str,
) -> bool:

    try:
        seeder()

        add_pass(
            f"Seeder ishladi: {label}"
        )

        return True

    except Exception as exc:
        message = (
            f"Seeder FAILED: {label} | "
            f"{exc.__class__.__name__}: {exc}"
        )

        SEED_ERRORS.append(message)
        add_error(message)

        return False


# ============================================================
# 0. PREPARE DATABASE
# ============================================================

def prepare_database() -> None:
    section(
        "0. DATABASE PREPARATION / SEED TEST"
    )

    print(
        "Local test database "
        "initialize va seed qilinmoqda..."
    )

    print()

    # --------------------------------------------------------
    # DATABASE SCHEMA
    # --------------------------------------------------------

    try:
        initialize_database()

        add_pass(
            "initialize_database() ishladi."
        )

    except Exception as exc:
        add_error(
            "initialize_database() FAILED: "
            f"{exc.__class__.__name__}: {exc}"
        )

        return

    # --------------------------------------------------------
    # LEVEL + MODULE STRUCTURE
    # --------------------------------------------------------

    if not run_seeder(
        seed_course_structure,
        "seed_course_structure",
    ):
        add_error(
            "Asosiy course structure "
            "seed bo'lmadi."
        )

    # --------------------------------------------------------
    # ALL MODULE LESSON SEEDERS
    # --------------------------------------------------------

    print()
    print(
        f"Module seederlar: "
        f"{len(MODULE_SEEDERS)} ta"
    )

    for seeder in MODULE_SEEDERS:
        name = getattr(
            seeder,
            "__name__",
            str(seeder),
        )

        run_seeder(
            seeder,
            name,
        )

    # --------------------------------------------------------
    # QUIZZES
    # --------------------------------------------------------

    run_seeder(
        seed_quizzes,
        "seed_quizzes",
    )

    # --------------------------------------------------------
    # BASE EXAMS
    # --------------------------------------------------------

    run_seeder(
        seed_level_exams,
        "seed_level_exams",
    )

    # --------------------------------------------------------
    # CUSTOM EXAMS
    # --------------------------------------------------------

    print()
    print(
        f"Custom exam seederlar: "
        f"{len(CUSTOM_EXAM_SEEDERS)} ta"
    )

    for seeder in CUSTOM_EXAM_SEEDERS:
        name = getattr(
            seeder,
            "__name__",
            str(seeder),
        )

        run_seeder(
            seeder,
            name,
        )

    # --------------------------------------------------------
    # RESULT
    # --------------------------------------------------------

    if SEED_ERRORS:
        add_error(
            f"Seed bosqichida "
            f"{len(SEED_ERRORS)} ta xato bor."
        )

    else:
        add_pass(
            "Database preparation "
            "to'liq yakunlandi."
        )


# ============================================================
# 1. CONNECTION
# ============================================================

def audit_connection() -> None:
    section(
        "1. DATABASE CONNECTION"
    )

    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT sqlite_version()
            AS version
            """
        )

        row = cursor.fetchone()

        version = row_value(
            row,
            "version",
            0,
        )

        add_pass(
            "SQLite connection ishladi. "
            f"Version: {version}"
        )

        cursor.execute(
            "PRAGMA foreign_keys"
        )

        fk_row = cursor.fetchone()

        fk_enabled = row_value(
            fk_row,
            "foreign_keys",
            0,
        )

        if fk_enabled == 1:
            add_pass(
                "SQLite foreign_keys ON."
            )
        else:
            add_warning(
                "SQLite foreign_keys "
                "bu connectionda OFF."
            )

    finally:
        connection.close()


# ============================================================
# 2. REQUIRED TABLES
# ============================================================

def audit_required_tables() -> None:
    section(
        "2. REQUIRED TABLES"
    )

    required_tables = [
        "users",
        "app_settings",
        "course_levels",
        "course_modules",
        "lessons",
        "lesson_progress",
        "quiz_questions",
        "quiz_options",
        "quiz_attempts",
        "level_exams",
        "level_exam_attempts",
        "user_level_progress",
    ]

    connection = get_connection()

    try:
        cursor = connection.cursor()

        for table_name in required_tables:

            if table_exists(
                cursor,
                table_name,
            ):
                add_pass(
                    f"{table_name} mavjud."
                )

            else:
                add_error(
                    f"{table_name} "
                    "jadvali topilmadi."
                )

    finally:
        connection.close()


# ============================================================
# 3. LEVEL AUDIT
# ============================================================

def audit_levels() -> None:
    section(
        "3. COURSE LEVEL AUDIT"
    )

    connection = get_connection()

    try:
        cursor = connection.cursor()

        if not table_exists(
            cursor,
            "course_levels",
        ):
            add_error(
                "course_levels mavjud emas."
            )
            return

        cursor.execute(
            """
            SELECT *
            FROM course_levels
            ORDER BY sort_order, id
            """
        )

        rows = cursor.fetchall()

        codes = [
            row_value(
                row,
                "code",
            )
            for row in rows
        ]

        print(
            f"Bazada LEVEL soni: "
            f"{len(rows)}"
        )

        if len(rows) == 16:
            add_pass(
                "LEVEL soni 16 ta."
            )
        else:
            add_error(
                f"LEVEL soni {len(rows)} ta. "
                "Kutilgani 16 ta."
            )

        missing = sorted(
            set(EXPECTED_LEVEL_CODES)
            - set(codes)
        )

        extra = sorted(
            set(codes)
            - set(EXPECTED_LEVEL_CODES)
        )

        if missing:
            add_error(
                "Yetishmayotgan LEVELlar: "
                f"{missing}"
            )

        if extra:
            add_warning(
                "Kutilmagan LEVELlar: "
                f"{extra}"
            )

        if (
            not missing
            and not extra
        ):
            add_pass(
                "LEVEL_00 dan LEVEL_15 "
                "gacha barchasi mavjud."
            )

        duplicates = [
            code
            for code, count
            in Counter(codes).items()
            if code
            and count > 1
        ]

        if duplicates:
            for code in duplicates:
                add_error(
                    "Duplicate LEVEL code: "
                    f"{code}"
                )
        else:
            add_pass(
                "Duplicate LEVEL code "
                "topilmadi."
            )

    finally:
        connection.close()


# ============================================================
# 4. MODULE AUDIT
# ============================================================

def audit_modules() -> None:
    section(
        "4. COURSE MODULE AUDIT"
    )

    connection = get_connection()

    try:
        cursor = connection.cursor()

        if not table_exists(
            cursor,
            "course_modules",
        ):
            add_error(
                "course_modules mavjud emas."
            )
            return

        cursor.execute(
            """
            SELECT COUNT(*) AS total
            FROM course_modules
            """
        )

        total = row_value(
            cursor.fetchone(),
            "total",
            0,
        )

        print(
            f"Bazada module soni: "
            f"{total}"
        )

        if total == EXPECTED_TOTAL_MODULES:
            add_pass(
                "Module soni "
                f"{EXPECTED_TOTAL_MODULES} ta."
            )
        else:
            add_error(
                f"Module soni {total} ta. "
                "Kutilgani "
                f"{EXPECTED_TOTAL_MODULES} ta."
            )

        cursor.execute(
            """
            SELECT
                code,
                COUNT(*) AS qty
            FROM course_modules
            GROUP BY code
            HAVING COUNT(*) > 1
            """
        )

        duplicates = cursor.fetchall()

        if duplicates:
            for row in duplicates:
                add_error(
                    "Duplicate module code: "
                    f"{row_value(row, 'code', 0)}"
                )
        else:
            add_pass(
                "Duplicate module code "
                "topilmadi."
            )

        cursor.execute(
            """
            SELECT
                l.code AS level_code,
                COUNT(m.id)
                AS module_count
            FROM course_levels l
            LEFT JOIN course_modules m
                ON m.level_id = l.id
            GROUP BY l.id, l.code
            ORDER BY l.sort_order, l.id
            """
        )

        rows = cursor.fetchall()

        for row in rows:
            level_code = row_value(
                row,
                "level_code",
                0,
            )

            module_count = row_value(
                row,
                "module_count",
                1,
            )

            expected = (
                EXPECTED_MODULE_COUNTS.get(
                    level_code
                )
            )

            if expected is None:
                add_warning(
                    f"{level_code}: "
                    "expected count yo'q."
                )
                continue

            if module_count == expected:
                add_pass(
                    f"{level_code}: "
                    f"{module_count}/"
                    f"{expected} modul."
                )

            else:
                add_error(
                    f"{level_code}: "
                    f"{module_count} modul. "
                    f"Kutilgani {expected}."
                )

        cursor.execute(
            """
            SELECT
                m.code
            FROM course_modules m
            LEFT JOIN course_levels l
                ON l.id = m.level_id
            WHERE l.id IS NULL
            """
        )

        orphans = cursor.fetchall()

        if orphans:
            for row in orphans:
                add_error(
                    "LEVELsiz module: "
                    f"{row_value(row, 'code', 0)}"
                )
        else:
            add_pass(
                "Orphan module topilmadi."
            )

    finally:
        connection.close()


# ============================================================
# 5. LESSON AUDIT
# ============================================================

def audit_lessons() -> None:
    section(
        "5. LESSON AUDIT"
    )

    connection = get_connection()

    try:
        cursor = connection.cursor()

        if not table_exists(
            cursor,
            "lessons",
        ):
            add_error(
                "lessons mavjud emas."
            )
            return

        cursor.execute(
            """
            SELECT COUNT(*) AS total
            FROM lessons
            """
        )

        database_total = row_value(
            cursor.fetchone(),
            "total",
            0,
        )

        registry_content = (
            get_all_lesson_content()
        )

        expected_codes = set(
            registry_content.keys()
        )

        expected_total = len(
            expected_codes
        )

        print(
            "Registry lesson content: "
            f"{expected_total}"
        )

        print(
            "Database lessons: "
            f"{database_total}"
        )

        if database_total > 0:
            add_pass(
                "Lessons bazaga tushgan."
            )
        else:
            add_error(
                "Lessons jadvali bo'sh."
            )

        cursor.execute(
            """
            SELECT code
            FROM lessons
            """
        )

        rows = cursor.fetchall()

        database_codes = {
            row_value(
                row,
                "code",
                0,
            )
            for row in rows
            if row_value(
                row,
                "code",
                0,
            )
        }

        missing = sorted(
            expected_codes
            - database_codes
        )

        extra = sorted(
            database_codes
            - expected_codes
        )

        if missing:
            add_error(
                f"Database'da "
                f"{len(missing)} ta "
                "registry lesson yo'q."
            )

            for code in missing[:30]:
                print(
                    f"   MISSING: {code}"
                )

            if len(missing) > 30:
                print(
                    "   ... qolganlari: "
                    f"{len(missing) - 30}"
                )

        else:
            add_pass(
                "Registry'dagi barcha "
                "lessonlar database'da mavjud."
            )

        if extra:
            add_warning(
                f"Database'da registry'da "
                f"yo'q {len(extra)} ta "
                "lesson mavjud."
            )

            for code in extra[:20]:
                print(
                    f"   EXTRA: {code}"
                )

        cursor.execute(
            """
            SELECT
                code,
                COUNT(*) AS qty
            FROM lessons
            GROUP BY code
            HAVING COUNT(*) > 1
            """
        )

        duplicates = cursor.fetchall()

        if duplicates:
            for row in duplicates:
                add_error(
                    "Duplicate lesson code: "
                    f"{row_value(row, 'code', 0)}"
                )
        else:
            add_pass(
                "Duplicate lesson code "
                "topilmadi."
            )

        cursor.execute(
            """
            SELECT
                l.code
            FROM lessons l
            LEFT JOIN course_modules m
                ON m.id = l.module_id
            WHERE m.id IS NULL
            """
        )

        orphans = cursor.fetchall()

        if orphans:
            for row in orphans:
                add_error(
                    "Modulesiz lesson: "
                    f"{row_value(row, 'code', 0)}"
                )
        else:
            add_pass(
                "Orphan lesson topilmadi."
            )

        columns = get_table_columns(
            cursor,
            "lessons",
        )

        if "passing_score" in columns:

            cursor.execute(
                """
                SELECT
                    code,
                    passing_score
                FROM lessons
                WHERE passing_score IS NULL
                   OR passing_score <= 0
                   OR passing_score > 100
                """
            )

            bad_scores = cursor.fetchall()

            if bad_scores:
                for row in bad_scores:
                    add_error(
                        f"{row_value(row, 'code', 0)} "
                        "passing_score noto'g'ri."
                    )
            else:
                add_pass(
                    "Lesson passing_score "
                    "qiymatlari normal."
                )

        if "estimated_minutes" in columns:

            cursor.execute(
                """
                SELECT
                    code,
                    estimated_minutes
                FROM lessons
                WHERE estimated_minutes IS NULL
                   OR estimated_minutes <= 0
                """
            )

            bad_times = cursor.fetchall()

            if bad_times:
                for row in bad_times:
                    add_warning(
                        f"{row_value(row, 'code', 0)} "
                        "estimated_minutes noto'g'ri."
                    )
            else:
                add_pass(
                    "Lesson duration "
                    "qiymatlari normal."
                )

    finally:
        connection.close()


# ============================================================
# 6. QUIZ AUDIT
# ============================================================

def audit_quizzes() -> None:
    section(
        "6. QUIZ DATABASE AUDIT"
    )

    connection = get_connection()

    try:
        cursor = connection.cursor()

        if not table_exists(
            cursor,
            "quiz_questions",
        ):
            add_error(
                "quiz_questions mavjud emas."
            )
            return

        if not table_exists(
            cursor,
            "quiz_options",
        ):
            add_error(
                "quiz_options mavjud emas."
            )
            return

        registry_quiz = (
            get_all_quiz_data()
        )

        expected_question_codes = set()
        expected_question_total = 0

        for questions in registry_quiz.values():

            if not isinstance(
                questions,
                (list, tuple),
            ):
                continue

            expected_question_total += len(
                questions
            )

            for question in questions:

                if not isinstance(
                    question,
                    dict,
                ):
                    continue

                code = question.get(
                    "code"
                )

                if code:
                    expected_question_codes.add(
                        code
                    )

        cursor.execute(
            """
            SELECT COUNT(*) AS total
            FROM quiz_questions
            """
        )

        db_question_total = row_value(
            cursor.fetchone(),
            "total",
            0,
        )

        cursor.execute(
            """
            SELECT COUNT(*) AS total
            FROM quiz_options
            """
        )

        db_option_total = row_value(
            cursor.fetchone(),
            "total",
            0,
        )

        print(
            "Registry quiz questions: "
            f"{expected_question_total}"
        )

        print(
            "Database quiz questions: "
            f"{db_question_total}"
        )

        print(
            "Database quiz options: "
            f"{db_option_total}"
        )

        if db_question_total > 0:
            add_pass(
                "Quiz savollari "
                "bazaga tushgan."
            )
        else:
            add_error(
                "quiz_questions bo'sh."
            )

        cursor.execute(
            """
            SELECT code
            FROM quiz_questions
            """
        )

        rows = cursor.fetchall()

        db_codes = {
            row_value(
                row,
                "code",
                0,
            )
            for row in rows
            if row_value(
                row,
                "code",
                0,
            )
        }

        missing = sorted(
            expected_question_codes
            - db_codes
        )

        extra = sorted(
            db_codes
            - expected_question_codes
        )

        if missing:
            add_error(
                f"Database'da "
                f"{len(missing)} ta "
                "quiz savoli yetishmaydi."
            )

            for code in missing[:30]:
                print(
                    f"   MISSING: {code}"
                )

            if len(missing) > 30:
                print(
                    "   ... qolganlari: "
                    f"{len(missing) - 30}"
                )

        else:
            add_pass(
                "Registry'dagi barcha "
                "quiz savollari "
                "database'da mavjud."
            )

        if extra:
            add_warning(
                f"Database'da registry'da "
                f"yo'q {len(extra)} ta "
                "quiz savoli mavjud."
            )

        cursor.execute(
            """
            SELECT
                code,
                COUNT(*) AS qty
            FROM quiz_questions
            GROUP BY code
            HAVING COUNT(*) > 1
            """
        )

        duplicate_questions = (
            cursor.fetchall()
        )

        if duplicate_questions:
            for row in duplicate_questions:
                add_error(
                    "Duplicate quiz code: "
                    f"{row_value(row, 'code', 0)}"
                )
        else:
            add_pass(
                "Duplicate quiz code "
                "topilmadi."
            )

        question_columns = get_table_columns(
            cursor,
            "quiz_questions",
        )

        option_columns = get_table_columns(
            cursor,
            "quiz_options",
        )

        if "lesson_id" in question_columns:

            cursor.execute(
                """
                SELECT q.code
                FROM quiz_questions q
                LEFT JOIN lessons l
                    ON l.id = q.lesson_id
                WHERE l.id IS NULL
                """
            )

            orphans = cursor.fetchall()

            if orphans:
                for row in orphans:
                    add_error(
                        "Lessonsiz quiz: "
                        f"{row_value(row, 'code', 0)}"
                    )
            else:
                add_pass(
                    "Orphan quiz question "
                    "topilmadi."
                )

            cursor.execute(
                """
                SELECT
                    l.code AS lesson_code
                FROM lessons l
                LEFT JOIN quiz_questions q
                    ON q.lesson_id = l.id
                GROUP BY l.id, l.code
                HAVING COUNT(q.id) = 0
                ORDER BY l.code
                """
            )

            lessons_without_quiz = (
                cursor.fetchall()
            )

            if lessons_without_quiz:
                add_error(
                    f"{len(lessons_without_quiz)} "
                    "ta lesson'da quiz savoli yo'q."
                )

                for row in lessons_without_quiz[:30]:
                    print(
                        "   NO QUIZ: "
                        f"{row_value(row, 'lesson_code', 0)}"
                    )

            else:
                add_pass(
                    "Barcha lessonlarda "
                    "quiz savoli mavjud."
                )

        if "question_id" in option_columns:

            cursor.execute(
                """
                SELECT
                    o.id
                FROM quiz_options o
                LEFT JOIN quiz_questions q
                    ON q.id = o.question_id
                WHERE q.id IS NULL
                """
            )

            orphan_options = (
                cursor.fetchall()
            )

            if orphan_options:
                add_error(
                    f"{len(orphan_options)} ta "
                    "orphan quiz option."
                )
            else:
                add_pass(
                    "Orphan quiz option "
                    "topilmadi."
                )

            cursor.execute(
                """
                SELECT
                    q.code,
                    COUNT(o.id)
                    AS option_count
                FROM quiz_questions q
                LEFT JOIN quiz_options o
                    ON o.question_id = q.id
                GROUP BY q.id, q.code
                HAVING COUNT(o.id) < 2
                """
            )

            bad_option_counts = (
                cursor.fetchall()
            )

            if bad_option_counts:
                for row in bad_option_counts:
                    add_error(
                        f"{row_value(row, 'code', 0)}: "
                        f"{row_value(row, 'option_count', 1)} "
                        "ta option."
                    )
            else:
                add_pass(
                    "Har savolda kamida "
                    "2 ta option mavjud."
                )

        correct_column = None

        for candidate in (
            "is_correct",
            "correct",
        ):
            if candidate in option_columns:
                correct_column = candidate
                break

        if (
            correct_column
            and "question_id"
            in option_columns
        ):

            cursor.execute(
                f"""
                SELECT
                    q.code,
                    SUM(
                        CASE
                            WHEN o.{correct_column} = 1
                            THEN 1
                            ELSE 0
                        END
                    ) AS correct_count
                FROM quiz_questions q
                LEFT JOIN quiz_options o
                    ON o.question_id = q.id
                GROUP BY q.id, q.code
                HAVING correct_count != 1
                """
            )

            bad_correct = (
                cursor.fetchall()
            )

            if bad_correct:
                for row in bad_correct:
                    add_error(
                        f"{row_value(row, 'code', 0)}: "
                        f"{row_value(row, 'correct_count', 1)} "
                        "ta correct option."
                    )

            else:
                add_pass(
                    "Har quiz savolida "
                    "aynan 1 ta correct "
                    "javob mavjud."
                )


    finally:
        connection.close()


# ============================================================
# 7. EXAM AUDIT
# ============================================================

def audit_exams() -> None:
    section(
        "7. LEVEL EXAM AUDIT"
    )

    connection = get_connection()

    try:
        cursor = connection.cursor()

        if not table_exists(
            cursor,
            "level_exams",
        ):
            add_error(
                "level_exams mavjud emas."
            )
            return

        cursor.execute(
            """
            SELECT COUNT(*) AS total
            FROM level_exams
            """
        )

        total = row_value(
            cursor.fetchone(),
            "total",
            0,
        )

        print(
            f"Bazada level exam soni: "
            f"{total}"
        )

        if total > 0:
            add_pass(
                "Level examlar mavjud."
            )
        else:
            add_error(
                "level_exams bo'sh."
            )

        cursor.execute(
            """
            SELECT
                level_id,
                COUNT(*) AS qty
            FROM level_exams
            GROUP BY level_id
            HAVING COUNT(*) > 1
            """
        )

        duplicate_exams = (
            cursor.fetchall()
        )

        if duplicate_exams:
            for row in duplicate_exams:
                add_error(
                    "Bitta LEVEL uchun "
                    "bir nechta exam: "
                    f"level_id="
                    f"{row_value(row, 'level_id', 0)}"
                )

        else:
            add_pass(
                "Bir LEVEL uchun "
                "duplicate exam topilmadi."
            )

        cursor.execute(
            """
            SELECT
                l.code AS level_code,
                e.question_count,
                e.passing_score,
                e.xp_reward
            FROM level_exams e
            JOIN course_levels l
                ON l.id = e.level_id
            ORDER BY l.sort_order, l.id
            """
        )

        rows = cursor.fetchall()

        exam_level_codes = set()

        for row in rows:
            level_code = row_value(
                row,
                "level_code",
                0,
            )

            exam_level_codes.add(
                level_code
            )

            question_count = row_value(
                row,
                "question_count",
                1,
            )

            passing_score = row_value(
                row,
                "passing_score",
                2,
            )

            xp_reward = row_value(
                row,
                "xp_reward",
                3,
            )

            if (
                not isinstance(
                    question_count,
                    int,
                )
                or question_count <= 0
            ):
                add_error(
                    f"{level_code}: "
                    "question_count noto'g'ri."
                )

            if (
                not isinstance(
                    passing_score,
                    int,
                )
                or not (
                    0
                    < passing_score
                    <= 100
                )
            ):
                add_error(
                    f"{level_code}: "
                    "passing_score noto'g'ri."
                )

            if (
                xp_reward is None
                or xp_reward < 0
            ):
                add_error(
                    f"{level_code}: "
                    "xp_reward noto'g'ri."
                )

        missing_custom = sorted(
            EXPECTED_CUSTOM_EXAM_LEVELS
            - exam_level_codes
        )

        if missing_custom:
            add_error(
                "Final exam topilmagan "
                "LEVELlar: "
                f"{missing_custom}"
            )
        else:
            add_pass(
                "LEVEL_02 dan LEVEL_15 "
                "gacha final examlar mavjud."
            )

        cursor.execute(
            """
            SELECT
                e.id
            FROM level_exams e
            LEFT JOIN course_levels l
                ON l.id = e.level_id
            WHERE l.id IS NULL
            """
        )

        orphan_exams = (
            cursor.fetchall()
        )

        if orphan_exams:
            add_error(
                f"{len(orphan_exams)} ta "
                "orphan exam topildi."
            )
        else:
            add_pass(
                "Orphan level exam "
                "topilmadi."
            )

    finally:
        connection.close()


# ============================================================
# 8. EXAM CAPACITY
# ============================================================

def audit_exam_question_capacity() -> None:
    section(
        "8. EXAM QUESTION BANK CAPACITY"
    )

    connection = get_connection()

    try:
        cursor = connection.cursor()

        required = [
            "course_levels",
            "course_modules",
            "lessons",
            "quiz_questions",
            "level_exams",
        ]

        for table_name in required:

            if not table_exists(
                cursor,
                table_name,
            ):
                add_error(
                    f"{table_name} yo'q. "
                    "Exam capacity "
                    "tekshirib bo'lmaydi."
                )
                return

        question_columns = (
            get_table_columns(
                cursor,
                "quiz_questions",
            )
        )

        if "lesson_id" not in question_columns:
            add_error(
                "quiz_questions.lesson_id "
                "topilmadi."
            )
            return

        cursor.execute(
            """
            SELECT
                l.code AS level_code,
                e.question_count
                    AS required_count,
                COUNT(DISTINCT q.id)
                    AS available_count
            FROM level_exams e
            JOIN course_levels l
                ON l.id = e.level_id
            LEFT JOIN course_modules m
                ON m.level_id = l.id
            LEFT JOIN lessons ls
                ON ls.module_id = m.id
            LEFT JOIN quiz_questions q
                ON q.lesson_id = ls.id
            GROUP BY
                l.id,
                l.code,
                e.question_count
            ORDER BY
                l.sort_order,
                l.id
            """
        )

        rows = cursor.fetchall()

        for row in rows:

            level_code = row_value(
                row,
                "level_code",
                0,
            )

            required_count = row_value(
                row,
                "required_count",
                1,
            )

            available_count = row_value(
                row,
                "available_count",
                2,
            )

            if available_count < required_count:

                add_error(
                    f"{level_code}: "
                    f"exam {required_count} "
                    "savol talab qiladi, "
                    f"bankda {available_count}."
                )

            else:
                add_pass(
                    f"{level_code}: "
                    f"{available_count} bank / "
                    f"{required_count} exam."
                )

    finally:
        connection.close()


# ============================================================
# 9. FOREIGN KEY CHECK
# ============================================================

def audit_foreign_keys() -> None:
    section(
        "9. SQLITE FOREIGN KEY CHECK"
    )

    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            "PRAGMA foreign_key_check"
        )

        rows = cursor.fetchall()

        if not rows:
            add_pass(
                "foreign_key_check: "
                "muammo topilmadi."
            )

        else:
            for row in rows:
                add_error(
                    "Foreign key xato: "
                    f"{tuple(row)}"
                )

    finally:
        connection.close()


# ============================================================
# 10. UNIQUE INDEX CHECK
# ============================================================

def audit_unique_indexes() -> None:
    section(
        "10. UNIQUE INDEX / ON CONFLICT AUDIT"
    )

    connection = get_connection()

    try:
        cursor = connection.cursor()

        checks = {
            "course_levels": [
                "code",
            ],
            "course_modules": [
                "code",
            ],
            "lessons": [
                "code",
            ],
            "quiz_questions": [
                "code",
            ],
            "level_exams": [
                "level_id",
            ],
        }

        for (
            table_name,
            required_columns,
        ) in checks.items():

            if not table_exists(
                cursor,
                table_name,
            ):
                add_error(
                    f"{table_name} yo'q."
                )
                continue

            unique_indexes = (
                get_unique_indexes(
                    cursor,
                    table_name,
                )
            )

            for required_column in (
                required_columns
            ):

                matched = False

                for (
                    index_name,
                    columns,
                ) in unique_indexes:

                    if (
                        required_column
                        in columns
                    ):
                        matched = True
                        break

                if matched:
                    add_pass(
                        f"{table_name}."
                        f"{required_column}: "
                        "UNIQUE mavjud."
                    )

                else:
                    add_error(
                        f"{table_name}."
                        f"{required_column}: "
                        "UNIQUE topilmadi. "
                        "ON CONFLICT ishlamasligi "
                        "mumkin."
                    )

        # ----------------------------------------------------
        # lesson_progress
        # ----------------------------------------------------

        if table_exists(
            cursor,
            "lesson_progress",
        ):

            indexes = get_unique_indexes(
                cursor,
                "lesson_progress",
            )

            pair_found = any(
                {
                    "user_id",
                    "lesson_id",
                }.issubset(
                    set(columns)
                )
                for _, columns
                in indexes
            )

            if pair_found:
                add_pass(
                    "lesson_progress "
                    "(user_id, lesson_id) "
                    "UNIQUE mavjud."
                )
            else:
                add_warning(
                    "lesson_progress "
                    "(user_id, lesson_id) "
                    "UNIQUE index topilmadi."
                )

        # ----------------------------------------------------
        # user_level_progress
        # ----------------------------------------------------

        if table_exists(
            cursor,
            "user_level_progress",
        ):

            indexes = get_unique_indexes(
                cursor,
                "user_level_progress",
            )

            pair_found = any(
                {
                    "user_id",
                    "level_id",
                }.issubset(
                    set(columns)
                )
                for _, columns
                in indexes
            )

            if pair_found:
                add_pass(
                    "user_level_progress "
                    "(user_id, level_id) "
                    "UNIQUE mavjud."
                )

            else:
                add_warning(
                    "user_level_progress "
                    "(user_id, level_id) "
                    "UNIQUE index topilmadi."
                )

    finally:
        connection.close()


# ============================================================
# 11. BASIC DATABASE HEALTH
# ============================================================

def audit_database_health() -> None:
    section(
        "11. SQLITE DATABASE HEALTH"
    )

    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            "PRAGMA integrity_check"
        )

        row = cursor.fetchone()

        result = row_value(
            row,
            "integrity_check",
            0,
        )

        if result == "ok":
            add_pass(
                "SQLite integrity_check = ok."
            )

        else:
            add_error(
                "SQLite integrity_check: "
                f"{result}"
            )

    finally:
        connection.close()


# ============================================================
# SUMMARY
# ============================================================

def print_summary() -> None:
    section(
        "ARCHIPRO UZ DATABASE AUDIT SUMMARY"
    )

    print(
        f"Expected LEVEL: 16"
    )

    print(
        "Expected MODULE: "
        f"{EXPECTED_TOTAL_MODULES}"
    )

    print()

    print(
        f"{GREEN}"
        f"PASS: {len(PASSES)}"
        f"{RESET}"
    )

    print(
        f"{YELLOW}"
        f"WARNING: {len(WARNINGS)}"
        f"{RESET}"
    )

    print(
        f"{RED}"
        f"ERROR: {len(ERRORS)}"
        f"{RESET}"
    )

    if ERRORS:

        print()

        print(
            f"{RED}{BOLD}"
            "TOPILGAN XATOLAR:"
            f"{RESET}"
        )

        for (
            number,
            error,
        ) in enumerate(
            ERRORS,
            start=1,
        ):
            print(
                f"{number}. {error}"
            )

    if WARNINGS:

        print()

        print(
            f"{YELLOW}{BOLD}"
            "OGOHLANTIRISHLAR:"
            f"{RESET}"
        )

        for (
            number,
            warning,
        ) in enumerate(
            WARNINGS,
            start=1,
        ):
            print(
                f"{number}. {warning}"
            )

    print()

    if ERRORS:

        print(
            f"{RED}{BOLD}"
            "DATABASE AUDIT RESULT: FAILED"
            f"{RESET}"
        )

        print(
            "Yuqoridagi ERRORlarni "
            "tuzatish kerak."
        )

    else:

        print(
            f"{GREEN}{BOLD}"
            "DATABASE AUDIT RESULT: PASSED"
            f"{RESET}"
        )

        print(
            "Database seed va struktura "
            "bo'yicha kritik xato "
            "topilmadi."
        )


# ============================================================
# MAIN
# ============================================================

def main() -> int:

    print()

    print(
        f"{BOLD}{CYAN}"
        "ARCHIPRO UZ — DATABASE AUDIT"
        f"{RESET}"
    )

    print(
        f"APP_DIR: {APP_DIR}"
    )

    prepare_database()

    audit_connection()

    audit_required_tables()

    audit_levels()

    audit_modules()

    audit_lessons()

    audit_quizzes()

    audit_exams()

    audit_exam_question_capacity()

    audit_foreign_keys()

    audit_unique_indexes()

    audit_database_health()

    print_summary()

    return (
        1
        if ERRORS
        else 0
    )


if __name__ == "__main__":

    try:

        exit_code = main()

        raise SystemExit(
            exit_code
        )

    except KeyboardInterrupt:

        print()

        print(
            "Audit foydalanuvchi "
            "tomonidan to'xtatildi."
        )

        raise SystemExit(130)

    except Exception:

        print()

        print(
            f"{RED}{BOLD}"
            "KUTILMAGAN DATABASE "
            "AUDIT XATOSI"
            f"{RESET}"
        )

        traceback.print_exc()

        raise SystemExit(2)
