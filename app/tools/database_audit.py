from __future__ import annotations

import atexit
import importlib
import os
import re
import shutil
import sys
import tempfile
import traceback
from pathlib import Path


# ============================================================
# PATH SETUP
# ============================================================

CURRENT_FILE = Path(__file__).resolve()
TOOLS_DIR = CURRENT_FILE.parent
APP_DIR = TOOLS_DIR.parent
COURSES_DIR = APP_DIR / "courses"

if str(APP_DIR) not in sys.path:
    sys.path.insert(0, str(APP_DIR))


# ============================================================
# ISOLATED AUDIT DATABASE
#
# Audit hech qachon foydalanuvchining real progress DB sini
# seed yoki o'zgartirmaydi.
# ============================================================

AUDIT_TEMP_DIR = Path(
    tempfile.mkdtemp(
        prefix="archipro_db_audit_"
    )
)

AUDIT_DATABASE_PATH = (
    AUDIT_TEMP_DIR
    / "archipro_audit.db"
)

os.environ[
    "ARCHIPRO_UZ_DATABASE_PATH"
] = str(
    AUDIT_DATABASE_PATH
)


def _cleanup_audit_database() -> None:
    shutil.rmtree(
        AUDIT_TEMP_DIR,
        ignore_errors=True,
    )


atexit.register(
    _cleanup_audit_database
)


# ============================================================
# CORE IMPORTS
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

PASSES: list[str] = []
WARNINGS: list[str] = []
ERRORS: list[str] = []


# ============================================================
# OUTPUT HELPERS
# ============================================================

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


# ============================================================
# SQLITE HELPERS
# ============================================================

def row_value(
    row,
    key: str,
    index: int = 0,
):
    if row is None:
        return None

    try:
        return row[key]
    except Exception:
        pass

    try:
        return row[index]
    except Exception:
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

    return cursor.fetchone() is not None


def table_columns(
    cursor,
    table_name: str,
) -> set[str]:

    cursor.execute(
        f"PRAGMA table_info({table_name})"
    )

    columns = set()

    for row in cursor.fetchall():
        name = row_value(
            row,
            "name",
            1,
        )

        if name:
            columns.add(name)

    return columns


def unique_indexes(
    cursor,
    table_name: str,
) -> list[tuple[str, list[str]]]:

    cursor.execute(
        f"PRAGMA index_list({table_name})"
    )

    result = []

    for row in cursor.fetchall():

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

        columns = []

        for info_row in cursor.fetchall():
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


# ============================================================
# DYNAMIC SEEDER DISCOVERY
# ============================================================

def discover_module_seeders():
    seeders = []

    pattern = re.compile(
        r"^level(\d{2})_module(\d{2})\.py$"
    )

    files = sorted(
        COURSES_DIR.glob(
            "level??_module??.py"
        )
    )

    for file_path in files:

        match = pattern.match(
            file_path.name
        )

        if not match:
            continue

        level_number = match.group(1)
        module_number = match.group(2)

        module_name = (
            f"courses.level"
            f"{level_number}"
            f"_module"
            f"{module_number}"
        )

        function_name = (
            f"seed_level"
            f"{level_number}"
            f"_module"
            f"{module_number}"
        )

        try:
            module = importlib.import_module(
                module_name
            )

        except Exception as exc:
            add_error(
                f"{module_name} import FAILED: "
                f"{exc.__class__.__name__}: "
                f"{exc}"
            )
            continue

        function = getattr(
            module,
            function_name,
            None,
        )

        if callable(function):
            seeders.append(
                (
                    function_name,
                    function,
                )
            )

        else:
            add_error(
                f"{module_name}: "
                f"{function_name} topilmadi."
            )

    # --------------------------------------------------------
    # SPECIAL COURSE SEEDERS
    # --------------------------------------------------------

    special_seeders = [
        (
            "courses.level00_extra",
            "seed_level00_extra",
        ),
        (
            "courses.level01_content",
            "seed_level01_lessons",
        ),
    ]

    for (
        module_name,
        function_name,
    ) in special_seeders:

        try:
            module = importlib.import_module(
                module_name
            )

            function = getattr(
                module,
                function_name,
                None,
            )

            if callable(function):
                seeders.append(
                    (
                        function_name,
                        function,
                    )
                )

            else:
                add_error(
                    f"{module_name}: "
                    f"{function_name} topilmadi."
                )

        except Exception as exc:
            add_error(
                f"{module_name} import FAILED: "
                f"{exc.__class__.__name__}: "
                f"{exc}"
            )

    return seeders


def discover_exam_seeders():
    seeders = []

    pattern = re.compile(
        r"^level(\d{2})_exam\.py$"
    )

    files = sorted(
        COURSES_DIR.glob(
            "level??_exam.py"
        )
    )

    for file_path in files:

        match = pattern.match(
            file_path.name
        )

        if not match:
            continue

        level_number = match.group(1)

        module_name = (
            f"courses.level"
            f"{level_number}_exam"
        )

        function_name = (
            f"seed_level"
            f"{level_number}_exam"
        )

        try:
            module = importlib.import_module(
                module_name
            )

        except Exception as exc:
            add_error(
                f"{module_name} import FAILED: "
                f"{exc.__class__.__name__}: "
                f"{exc}"
            )
            continue

        function = getattr(
            module,
            function_name,
            None,
        )

        if callable(function):
            seeders.append(
                (
                    function_name,
                    function,
                )
            )

        else:
            add_error(
                f"{module_name}: "
                f"{function_name} topilmadi."
            )

    return seeders


# ============================================================
# SEED RUNNER
# ============================================================

def run_seeder(
    name: str,
    function,
) -> bool:

    try:
        function()

        add_pass(
            f"Seeder ishladi: {name}"
        )

        return True

    except Exception as exc:

        add_error(
            f"Seeder FAILED: {name} | "
            f"{exc.__class__.__name__}: "
            f"{exc}"
        )

        return False


# ============================================================
# 0. DATABASE PREPARATION
# ============================================================

def prepare_database() -> None:
    section(
        "0. DATABASE PREPARATION"
    )

    try:
        initialize_database()

        add_pass(
            "initialize_database() ishladi."
        )

    except Exception as exc:
        add_error(
            "initialize_database() FAILED: "
            f"{exc.__class__.__name__}: "
            f"{exc}"
        )

        return

    # --------------------------------------------------------
    # LEVELS + MODULES + STARTER LESSONS
    # --------------------------------------------------------

    run_seeder(
        "seed_course_structure",
        seed_course_structure,
    )

    # --------------------------------------------------------
    # ALL LESSON MODULES
    # --------------------------------------------------------

    module_seeders = (
        discover_module_seeders()
    )

    print()
    print(
        "Topilgan lesson/module "
        f"seederlar: {len(module_seeders)}"
    )

    for (
        name,
        function,
    ) in module_seeders:

        run_seeder(
            name,
            function,
        )

    # --------------------------------------------------------
    # QUIZ
    # --------------------------------------------------------

    run_seeder(
        "seed_quizzes",
        seed_quizzes,
    )

    # --------------------------------------------------------
    # BASE EXAMS
    # --------------------------------------------------------

    run_seeder(
        "seed_level_exams",
        seed_level_exams,
    )

    # --------------------------------------------------------
    # CUSTOM EXAMS
    # --------------------------------------------------------

    exam_seeders = (
        discover_exam_seeders()
    )

    print()
    print(
        "Topilgan custom exam "
        f"seederlar: {len(exam_seeders)}"
    )

    for (
        name,
        function,
    ) in exam_seeders:

        run_seeder(
            name,
            function,
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
            """
        )

        version = row_value(
            cursor.fetchone(),
            "sqlite_version()",
            0,
        )

        add_pass(
            "SQLite connection ishladi. "
            f"Version: {version}"
        )

        cursor.execute(
            """
            PRAGMA foreign_keys
            """
        )

        foreign_keys = row_value(
            cursor.fetchone(),
            "foreign_keys",
            0,
        )

        if foreign_keys == 1:
            add_pass(
                "SQLite foreign_keys ON."
            )
        else:
            add_warning(
                "SQLite foreign_keys OFF."
            )

    finally:
        connection.close()


# ============================================================
# 2. REQUIRED TABLES
# ============================================================

def audit_tables() -> None:
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
        "lesson_bookmarks",
        "lesson_notes",
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
# 3. LEVELS
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
            SELECT code
            FROM course_levels
            ORDER BY sort_order, id
            """
        )

        rows = cursor.fetchall()

        codes = [
            row_value(
                row,
                "code",
                0,
            )
            for row in rows
        ]

        print(
            f"LEVEL soni: {len(codes)}"
        )

        if len(codes) == 16:
            add_pass(
                "16 ta LEVEL mavjud."
            )
        else:
            add_error(
                f"LEVEL soni {len(codes)} ta. "
                "Kutilgani 16 ta."
            )

        missing = sorted(
            set(EXPECTED_LEVEL_CODES)
            - set(codes)
        )

        if missing:
            add_error(
                "Yetishmayotgan LEVELlar: "
                f"{missing}"
            )
        else:
            add_pass(
                "LEVEL_00 — LEVEL_15 "
                "barchasi mavjud."
            )

        if len(codes) != len(set(codes)):
            add_error(
                "Duplicate LEVEL code mavjud."
            )
        else:
            add_pass(
                "Duplicate LEVEL code "
                "topilmadi."
            )

    finally:
        connection.close()


# ============================================================
# 4. MODULES
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
            f"Module soni: {total}"
        )

        if total == EXPECTED_TOTAL_MODULES:
            add_pass(
                f"Module soni "
                f"{EXPECTED_TOTAL_MODULES} ta."
            )
        else:
            add_error(
                f"Module soni {total}. "
                f"Kutilgani "
                f"{EXPECTED_TOTAL_MODULES}."
            )

        cursor.execute(
            """
            SELECT
                l.code AS level_code,
                COUNT(m.id) AS module_count
            FROM course_levels l
            LEFT JOIN course_modules m
                ON m.level_id = l.id
            GROUP BY l.id, l.code
            ORDER BY l.sort_order, l.id
            """
        )

        for row in cursor.fetchall():

            level_code = row_value(
                row,
                "level_code",
                0,
            )

            count = row_value(
                row,
                "module_count",
                1,
            )

            expected = (
                EXPECTED_MODULE_COUNTS.get(
                    level_code
                )
            )

            if count == expected:
                add_pass(
                    f"{level_code}: "
                    f"{count}/{expected} modul."
                )

            else:
                add_error(
                    f"{level_code}: "
                    f"{count} modul. "
                    f"Kutilgani {expected}."
                )

        cursor.execute(
            """
            SELECT code, COUNT(*) AS qty
            FROM course_modules
            GROUP BY code
            HAVING COUNT(*) > 1
            """
        )

        duplicates = cursor.fetchall()

        if duplicates:
            for row in duplicates:
                add_error(
                    "Duplicate module: "
                    f"{row_value(row, 'code', 0)}"
                )
        else:
            add_pass(
                "Duplicate module code "
                "topilmadi."
            )

    finally:
        connection.close()


# ============================================================
# 5. LESSONS
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

        registry_content = (
            get_all_lesson_content()
        )

        expected_codes = set(
            registry_content.keys()
        )

        cursor.execute(
            """
            SELECT code
            FROM lessons
            """
        )

        database_codes = {
            row_value(
                row,
                "code",
                0,
            )
            for row in cursor.fetchall()
        }

        print(
            "Registry lesson content: "
            f"{len(expected_codes)}"
        )

        print(
            "Database lessons: "
            f"{len(database_codes)}"
        )

        missing = sorted(
            expected_codes
            - database_codes
        )

        if missing:

            add_error(
                f"{len(missing)} ta "
                "lesson database'da yo'q."
            )

            for code in missing[:30]:
                print(
                    f"   MISSING: {code}"
                )

        else:
            add_pass(
                "Registry'dagi barcha "
                "lessonlar database'da mavjud."
            )

        cursor.execute(
            """
            SELECT code, COUNT(*) AS qty
            FROM lessons
            GROUP BY code
            HAVING COUNT(*) > 1
            """
        )

        duplicates = cursor.fetchall()

        if duplicates:
            for row in duplicates:
                add_error(
                    "Duplicate lesson: "
                    f"{row_value(row, 'code', 0)}"
                )
        else:
            add_pass(
                "Duplicate lesson code "
                "topilmadi."
            )

        cursor.execute(
            """
            SELECT l.code
            FROM lessons l
            LEFT JOIN course_modules m
                ON m.id = l.module_id
            WHERE m.id IS NULL
            """
        )

        orphans = cursor.fetchall()

        if orphans:
            add_error(
                f"{len(orphans)} ta "
                "modulesiz lesson."
            )
        else:
            add_pass(
                "Orphan lesson topilmadi."
            )

    finally:
        connection.close()


# ============================================================
# 6. QUIZZES
# ============================================================

def audit_quizzes() -> None:
    section(
        "6. QUIZ AUDIT"
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

        expected_codes = set()

        for questions in registry_quiz.values():

            if not isinstance(
                questions,
                (list, tuple),
            ):
                continue

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
                    expected_codes.add(
                        code
                    )

        cursor.execute(
            """
            SELECT code
            FROM quiz_questions
            """
        )

        database_codes = {
            row_value(
                row,
                "code",
                0,
            )
            for row in cursor.fetchall()
        }

        print(
            "Registry quiz savollari: "
            f"{len(expected_codes)}"
        )

        print(
            "Database quiz savollari: "
            f"{len(database_codes)}"
        )

        missing = sorted(
            expected_codes
            - database_codes
        )

        if missing:

            add_error(
                f"{len(missing)} ta "
                "quiz savoli database'da yo'q."
            )

            for code in missing[:30]:
                print(
                    f"   MISSING: {code}"
                )

        else:
            add_pass(
                "Registry'dagi barcha "
                "quiz savollari database'da mavjud."
            )

        cursor.execute(
            """
            SELECT code, COUNT(*) AS qty
            FROM quiz_questions
            GROUP BY code
            HAVING COUNT(*) > 1
            """
        )

        duplicates = cursor.fetchall()

        if duplicates:
            for row in duplicates:
                add_error(
                    "Duplicate quiz code: "
                    f"{row_value(row, 'code', 0)}"
                )
        else:
            add_pass(
                "Duplicate quiz code "
                "topilmadi."
            )

        question_columns = table_columns(
            cursor,
            "quiz_questions",
        )

        option_columns = table_columns(
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
                add_error(
                    f"{len(orphans)} ta "
                    "lessonsiz quiz question."
                )
            else:
                add_pass(
                    "Orphan quiz question "
                    "topilmadi."
                )

        if "question_id" in option_columns:

            cursor.execute(
                """
                SELECT o.id
                FROM quiz_options o
                LEFT JOIN quiz_questions q
                    ON q.id = o.question_id
                WHERE q.id IS NULL
                """
            )

            orphans = cursor.fetchall()

            if orphans:
                add_error(
                    f"{len(orphans)} ta "
                    "orphan quiz option."
                )
            else:
                add_pass(
                    "Orphan quiz option "
                    "topilmadi."
                )

        correct_column = None

        if "is_correct" in option_columns:
            correct_column = "is_correct"

        elif "correct" in option_columns:
            correct_column = "correct"

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

            bad = cursor.fetchall()

            if bad:

                for row in bad[:30]:
                    add_error(
                        f"{row_value(row, 'code', 0)}: "
                        "correct javob soni "
                        f"{row_value(row, 'correct_count', 1)}."
                    )

            else:
                add_pass(
                    "Har savolda aynan "
                    "1 ta correct javob mavjud."
                )

    finally:
        connection.close()


# ============================================================
# 7. EXAMS
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

        exam_levels = set()

        for row in rows:

            level_code = row_value(
                row,
                "level_code",
                0,
            )

            exam_levels.add(
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

            if (
                question_count is None
                or question_count <= 0
            ):
                add_error(
                    f"{level_code}: "
                    "question_count noto'g'ri."
                )

            if (
                passing_score is None
                or passing_score <= 0
                or passing_score > 100
            ):
                add_error(
                    f"{level_code}: "
                    "passing_score noto'g'ri."
                )

        missing = sorted(
            EXPECTED_CUSTOM_EXAM_LEVELS
            - exam_levels
        )

        if missing:
            add_error(
                "Final exam topilmagan "
                f"LEVELlar: {missing}"
            )
        else:
            add_pass(
                "LEVEL_02 — LEVEL_15 "
                "final examlari mavjud."
            )

        cursor.execute(
            """
            SELECT level_id, COUNT(*) AS qty
            FROM level_exams
            GROUP BY level_id
            HAVING COUNT(*) > 1
            """
        )

        duplicates = cursor.fetchall()

        if duplicates:
            add_error(
                f"{len(duplicates)} ta "
                "duplicate level exam."
            )
        else:
            add_pass(
                "Duplicate level exam "
                "topilmadi."
            )

    finally:
        connection.close()


# ============================================================
# 8. EXAM QUESTION CAPACITY
# ============================================================

def audit_exam_capacity() -> None:
    section(
        "8. EXAM QUESTION BANK CAPACITY"
    )

    connection = get_connection()

    try:
        cursor = connection.cursor()

        required_tables = [
            "course_levels",
            "course_modules",
            "lessons",
            "quiz_questions",
            "level_exams",
        ]

        for table_name in required_tables:

            if not table_exists(
                cursor,
                table_name,
            ):
                add_error(
                    f"{table_name} yo'q. "
                    "Exam capacity tekshirib bo'lmaydi."
                )
                return

        question_columns = table_columns(
            cursor,
            "quiz_questions",
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
                cl.code AS level_code,
                le.question_count AS required_count,
                COUNT(DISTINCT qq.id) AS available_count
            FROM level_exams le
            JOIN course_levels cl
                ON cl.id = le.level_id
            LEFT JOIN course_modules cm
                ON cm.level_id = cl.id
            LEFT JOIN lessons l
                ON l.module_id = cm.id
            LEFT JOIN quiz_questions qq
                ON qq.lesson_id = l.id
            GROUP BY
                cl.id,
                cl.code,
                le.question_count
            ORDER BY
                cl.sort_order,
                cl.id
            """
        )

        for row in cursor.fetchall():

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
                    f"exam {required_count} savol, "
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
# 9. FOREIGN KEY
# ============================================================

def audit_foreign_keys() -> None:
    section(
        "9. SQLITE FOREIGN KEY CHECK"
    )

    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            PRAGMA foreign_key_check
            """
        )

        rows = cursor.fetchall()

        if rows:
            for row in rows:
                add_error(
                    f"Foreign key xato: "
                    f"{tuple(row)}"
                )
        else:
            add_pass(
                "foreign_key_check: "
                "muammo topilmadi."
            )

    finally:
        connection.close()


# ============================================================
# 10. UNIQUE INDEXES
# ============================================================

def audit_unique_indexes() -> None:
    section(
        "10. UNIQUE INDEX AUDIT"
    )

    connection = get_connection()

    try:
        cursor = connection.cursor()

        checks = {
            "course_levels": "code",
            "course_modules": "code",
            "lessons": "code",
            "quiz_questions": "code",
            "level_exams": "level_id",
        }

        for (
            table_name,
            required_column,
        ) in checks.items():

            if not table_exists(
                cursor,
                table_name,
            ):
                add_error(
                    f"{table_name} yo'q."
                )
                continue

            indexes = unique_indexes(
                cursor,
                table_name,
            )

            found = any(
                required_column in columns
                for _, columns in indexes
            )

            if found:
                add_pass(
                    f"{table_name}."
                    f"{required_column}: "
                    "UNIQUE mavjud."
                )
            else:
                add_error(
                    f"{table_name}."
                    f"{required_column}: "
                    "UNIQUE topilmadi."
                )

        pair_checks = {
            "lesson_progress": {
                "user_id",
                "lesson_id",
            },
            "lesson_bookmarks": {
                "user_id",
                "lesson_id",
            },
            "lesson_notes": {
                "user_id",
                "lesson_id",
            },
            "user_level_progress": {
                "user_id",
                "level_id",
            },
        }

        for (
            table_name,
            required_columns,
        ) in pair_checks.items():

            if not table_exists(
                cursor,
                table_name,
            ):
                continue

            indexes = unique_indexes(
                cursor,
                table_name,
            )

            found = any(
                required_columns.issubset(
                    set(columns)
                )
                for _, columns in indexes
            )

            if found:
                add_pass(
                    f"{table_name}: "
                    f"{sorted(required_columns)} "
                    "UNIQUE mavjud."
                )
            else:
                add_warning(
                    f"{table_name}: "
                    f"{sorted(required_columns)} "
                    "UNIQUE topilmadi."
                )

    finally:
        connection.close()


# ============================================================
# 11. DATABASE HEALTH
# ============================================================

def audit_integrity() -> None:
    section(
        "11. SQLITE DATABASE HEALTH"
    )

    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            PRAGMA integrity_check
            """
        )

        result = row_value(
            cursor.fetchone(),
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
            "TOPILGAN DATABASE XATOLAR:"
            f"{RESET}"
        )

        for (
            number,
            message,
        ) in enumerate(
            ERRORS,
            start=1,
        ):
            print(
                f"{number}. {message}"
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
            message,
        ) in enumerate(
            WARNINGS,
            start=1,
        ):
            print(
                f"{number}. {message}"
            )

    print()

    if ERRORS:

        print(
            f"{RED}{BOLD}"
            "DATABASE AUDIT RESULT: FAILED"
            f"{RESET}"
        )

    else:

        print(
            f"{GREEN}{BOLD}"
            "DATABASE AUDIT RESULT: PASSED"
            f"{RESET}"
        )

        print(
            "Database strukturasi va "
            "seed jarayonida kritik "
            "xato topilmadi."
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

    audit_tables()

    audit_levels()

    audit_modules()

    audit_lessons()

    audit_quizzes()

    audit_exams()

    audit_exam_capacity()

    audit_foreign_keys()

    audit_unique_indexes()

    audit_integrity()

    print_summary()

    if ERRORS:
        return 1

    return 0


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
