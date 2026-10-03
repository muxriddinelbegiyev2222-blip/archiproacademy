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


from database.database import get_connection


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
# EXPECTED ARCHIPRO STRUCTURE
# ============================================================

EXPECTED_LEVEL_CODES = [
    f"LEVEL_{number:02d}"
    for number in range(16)
]


EXPECTED_MODULE_COUNTS = {
    "LEVEL_00": 1,
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


# ============================================================
# HELPERS
# ============================================================

def add_pass(message: str) -> None:
    PASSES.append(message)
    print(f"{GREEN}[PASS]{RESET} {message}")


def add_warning(message: str) -> None:
    WARNINGS.append(message)
    print(f"{YELLOW}[WARN]{RESET} {message}")


def add_error(message: str) -> None:
    ERRORS.append(message)
    print(f"{RED}[ERROR]{RESET} {message}")


def section(title: str) -> None:
    print()
    print(f"{BOLD}{CYAN}{'=' * 74}{RESET}")
    print(f"{BOLD}{CYAN}{title}{RESET}")
    print(f"{BOLD}{CYAN}{'=' * 74}{RESET}")


def table_exists(cursor, table_name: str) -> bool:
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


def get_table_columns(cursor, table_name: str) -> list[str]:
    cursor.execute(
        f"PRAGMA table_info({table_name})"
    )

    rows = cursor.fetchall()

    columns: list[str] = []

    for row in rows:
        try:
            columns.append(row["name"])
        except (TypeError, KeyError):
            columns.append(row[1])

    return columns


def row_value(row: Any, key: str, index: int | None = None):
    try:
        return row[key]
    except (TypeError, KeyError, IndexError):
        if index is not None:
            try:
                return row[index]
            except (TypeError, IndexError):
                return None

    return None


# ============================================================
# 1. DATABASE CONNECTION
# ============================================================

def audit_connection() -> None:
    section("1. DATABASE CONNECTION")

    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            "SELECT sqlite_version() AS version"
        )

        row = cursor.fetchone()

        version = row_value(
            row,
            "version",
            0,
        )

        add_pass(
            f"SQLite connection ishladi. "
            f"Version: {version}"
        )

    finally:
        connection.close()


# ============================================================
# 2. REQUIRED TABLES
# ============================================================

def audit_required_tables() -> None:
    section("2. REQUIRED TABLES")

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
                    f"{table_name} jadvali topilmadi."
                )

    finally:
        connection.close()


# ============================================================
# 3. LEVEL AUDIT
# ============================================================

def audit_levels() -> None:
    section("3. COURSE LEVEL AUDIT")

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

        columns = get_table_columns(
            cursor,
            "course_levels",
        )

        if "code" not in columns:
            add_error(
                "course_levels ichida code ustuni yo'q."
            )
            return

        cursor.execute(
            """
            SELECT *
            FROM course_levels
            ORDER BY id
            """
        )

        rows = cursor.fetchall()

        codes = [
            row_value(row, "code")
            for row in rows
        ]

        print(
            f"Bazada level soni: {len(rows)}"
        )

        if len(rows) == 16:
            add_pass(
                "LEVEL soni 16 ta."
            )
        else:
            add_error(
                f"LEVEL soni {len(rows)} ta. "
                f"Kutilgani 16 ta."
            )

        duplicate_codes = [
            code
            for code, count
            in Counter(codes).items()
            if code and count > 1
        ]

        if duplicate_codes:
            for code in duplicate_codes:
                add_error(
                    f"Duplicate LEVEL code: {code}"
                )
        else:
            add_pass(
                "Duplicate LEVEL code topilmadi."
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
                f"Yetishmayotgan LEVELlar: {missing}"
            )

        if extra:
            add_warning(
                f"Kutilmagan LEVELlar: {extra}"
            )

        if not missing and not extra:
            add_pass(
                "LEVEL_00 dan LEVEL_15 gacha "
                "barcha level mavjud."
            )

    finally:
        connection.close()


# ============================================================
# 4. MODULE AUDIT
# ============================================================

def audit_modules() -> None:
    section("4. COURSE MODULE AUDIT")

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
            f"Bazada module soni: {total}"
        )

        expected_total = sum(
            EXPECTED_MODULE_COUNTS.values()
        )

        if total == expected_total:
            add_pass(
                f"Module soni {expected_total} ta."
            )
        else:
            add_error(
                f"Module soni {total} ta. "
                f"Kutilgani {expected_total} ta."
            )

        columns = get_table_columns(
            cursor,
            "course_modules",
        )

        if "code" in columns:
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
                        "Duplicate module code: "
                        f"{row_value(row, 'code', 0)} "
                        f"({row_value(row, 'qty', 1)} marta)"
                    )
            else:
                add_pass(
                    "Duplicate module code topilmadi."
                )

        if "level_id" not in columns:
            add_error(
                "course_modules ichida level_id yo'q."
            )
            return

        cursor.execute(
            """
            SELECT
                l.code AS level_code,
                COUNT(m.id) AS module_count
            FROM course_levels l
            LEFT JOIN course_modules m
                ON m.level_id = l.id
            GROUP BY l.id, l.code
            ORDER BY l.id
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

            expected = EXPECTED_MODULE_COUNTS.get(
                level_code
            )

            if expected is None:
                add_warning(
                    f"{level_code}: "
                    f"expected module soni belgilanmagan."
                )
                continue

            if module_count == expected:
                add_pass(
                    f"{level_code}: "
                    f"{module_count}/{expected} modul."
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
                m.id,
                m.code
            FROM course_modules m
            LEFT JOIN course_levels l
                ON l.id = m.level_id
            WHERE l.id IS NULL
            """
        )

        orphan_modules = cursor.fetchall()

        if orphan_modules:
            for row in orphan_modules:
                add_error(
                    "Levelsiz module: "
                    f"{row_value(row, 'code', 1)}"
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
    section("5. LESSON AUDIT")

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

        total = row_value(
            cursor.fetchone(),
            "total",
            0,
        )

        print(
            f"Bazada lesson soni: {total}"
        )

        if total > 0:
            add_pass(
                "Lessons bazaga seed qilingan."
            )
        else:
            add_error(
                "Lessons jadvali bo'sh."
            )

        columns = get_table_columns(
            cursor,
            "lessons",
        )

        if "code" in columns:
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
                        "Duplicate lesson code: "
                        f"{row_value(row, 'code', 0)} "
                        f"({row_value(row, 'qty', 1)} marta)"
                    )
            else:
                add_pass(
                    "Duplicate lesson code topilmadi."
                )

        if "module_id" in columns:
            cursor.execute(
                """
                SELECT
                    l.id,
                    l.code
                FROM lessons l
                LEFT JOIN course_modules m
                    ON m.id = l.module_id
                WHERE m.id IS NULL
                """
            )

            orphan_lessons = cursor.fetchall()

            if orphan_lessons:
                for row in orphan_lessons:
                    add_error(
                        "Modulesiz lesson: "
                        f"{row_value(row, 'code', 1)}"
                    )
            else:
                add_pass(
                    "Orphan lesson topilmadi."
                )

        if "passing_score" in columns:
            cursor.execute(
                """
                SELECT code, passing_score
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
                        f"{row_value(row, 'code', 0)}: "
                        f"passing_score "
                        f"{row_value(row, 'passing_score', 1)}"
                    )
            else:
                add_pass(
                    "Lesson passing_score qiymatlari normal."
                )

        if "estimated_minutes" in columns:
            cursor.execute(
                """
                SELECT code, estimated_minutes
                FROM lessons
                WHERE estimated_minutes IS NULL
                   OR estimated_minutes <= 0
                """
            )

            bad_minutes = cursor.fetchall()

            if bad_minutes:
                for row in bad_minutes:
                    add_warning(
                        f"{row_value(row, 'code', 0)}: "
                        "estimated_minutes noto'g'ri."
                    )
            else:
                add_pass(
                    "Lesson duration qiymatlari normal."
                )

    finally:
        connection.close()


# ============================================================
# 6. QUIZ DATABASE AUDIT
# ============================================================

def audit_quizzes() -> None:
    section("6. QUIZ DATABASE AUDIT")

    connection = get_connection()

    try:
        cursor = connection.cursor()

        for table_name in (
            "quiz_questions",
            "quiz_options",
        ):
            if not table_exists(
                cursor,
                table_name,
            ):
                add_error(
                    f"{table_name} mavjud emas."
                )
                return

        cursor.execute(
            """
            SELECT COUNT(*) AS total
            FROM quiz_questions
            """
        )

        question_total = row_value(
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

        option_total = row_value(
            cursor.fetchone(),
            "total",
            0,
        )

        print(
            f"Quiz questions: {question_total}"
        )

        print(
            f"Quiz options: {option_total}"
        )

        if question_total > 0:
            add_pass(
                "Quiz savollari bazaga seed qilingan."
            )
        else:
            add_error(
                "quiz_questions jadvali bo'sh."
            )

        question_columns = get_table_columns(
            cursor,
            "quiz_questions",
        )

        option_columns = get_table_columns(
            cursor,
            "quiz_options",
        )

        if "code" in question_columns:
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
                        "Duplicate quiz question code: "
                        f"{row_value(row, 'code', 0)} "
                        f"({row_value(row, 'qty', 1)} marta)"
                    )
            else:
                add_pass(
                    "Duplicate quiz question code topilmadi."
                )

        if "lesson_id" in question_columns:
            cursor.execute(
                """
                SELECT
                    q.id,
                    q.code
                FROM quiz_questions q
                LEFT JOIN lessons l
                    ON l.id = q.lesson_id
                WHERE l.id IS NULL
                """
            )

            orphan_questions = cursor.fetchall()

            if orphan_questions:
                for row in orphan_questions:
                    add_error(
                        "Lessonsiz quiz question: "
                        f"{row_value(row, 'code', 1)}"
                    )
            else:
                add_pass(
                    "Orphan quiz question topilmadi."
                )

            cursor.execute(
                """
                SELECT
                    l.code AS lesson_code,
                    COUNT(q.id) AS question_count
                FROM lessons l
                LEFT JOIN quiz_questions q
                    ON q.lesson_id = l.id
                GROUP BY l.id, l.code
                HAVING COUNT(q.id) = 0
                ORDER BY l.code
                """
            )

            no_quiz_lessons = cursor.fetchall()

            if no_quiz_lessons:
                for row in no_quiz_lessons:
                    add_error(
                        "Quiz savoli yo'q lesson: "
                        f"{row_value(row, 'lesson_code', 0)}"
                    )
            else:
                add_pass(
                    "Barcha bazadagi lessonlarda quiz savoli mavjud."
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

            orphan_options = cursor.fetchall()

            if orphan_options:
                add_error(
                    f"{len(orphan_options)} ta "
                    "orphan quiz option topildi."
                )
            else:
                add_pass(
                    "Orphan quiz option topilmadi."
                )

            cursor.execute(
                """
                SELECT
                    q.id,
                    q.code,
                    COUNT(o.id) AS option_count
                FROM quiz_questions q
                LEFT JOIN quiz_options o
                    ON o.question_id = q.id
                GROUP BY q.id, q.code
                HAVING COUNT(o.id) < 2
                """
            )

            bad_option_counts = cursor.fetchall()

            if bad_option_counts:
                for row in bad_option_counts:
                    add_error(
                        f"{row_value(row, 'code', 1)}: "
                        f"faqat "
                        f"{row_value(row, 'option_count', 2)} "
                        "ta option."
                    )
            else:
                add_pass(
                    "Har quiz savolida kamida 2 ta option mavjud."
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
            and "question_id" in option_columns
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

            invalid_correct = cursor.fetchall()

            if invalid_correct:
                for row in invalid_correct:
                    add_error(
                        f"{row_value(row, 'code', 0)}: "
                        f"{row_value(row, 'correct_count', 1)} "
                        "ta to'g'ri option."
                    )
            else:
                add_pass(
                    "Har quiz savolida aynan "
                    "1 ta to'g'ri javob mavjud."
                )


    finally:
        connection.close()


# ============================================================
# 7. EXAM AUDIT
# ============================================================

def audit_exams() -> None:
    section("7. LEVEL EXAM AUDIT")

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
            f"Bazada level exam soni: {total}"
        )

        if total > 0:
            add_pass(
                "Level examlar mavjud."
            )
        else:
            add_error(
                "level_exams jadvali bo'sh."
            )

        columns = get_table_columns(
            cursor,
            "level_exams",
        )

        if "level_id" in columns:
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

            duplicates = cursor.fetchall()

            if duplicates:
                for row in duplicates:
                    add_error(
                        "Bitta LEVEL uchun bir nechta exam: "
                        f"level_id={row_value(row, 'level_id', 0)}"
                    )
            else:
                add_pass(
                    "Har LEVEL uchun maximum 1 ta exam mavjud."
                )

            cursor.execute(
                """
                SELECT
                    e.id,
                    l.code AS level_code
                FROM level_exams e
                LEFT JOIN course_levels l
                    ON l.id = e.level_id
                WHERE l.id IS NULL
                """
            )

            orphan_exams = cursor.fetchall()

            if orphan_exams:
                add_error(
                    f"{len(orphan_exams)} ta orphan level exam topildi."
                )
            else:
                add_pass(
                    "Orphan level exam topilmadi."
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
            ORDER BY l.id
            """
        )

        exams = cursor.fetchall()

        exam_level_codes = set()

        for row in exams:
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
                not isinstance(question_count, int)
                or question_count <= 0
            ):
                add_error(
                    f"{level_code}: "
                    f"question_count noto'g'ri."
                )

            if (
                not isinstance(passing_score, int)
                or not 0 < passing_score <= 100
            ):
                add_error(
                    f"{level_code}: "
                    f"passing_score noto'g'ri."
                )

            if (
                xp_reward is None
                or xp_reward < 0
            ):
                add_error(
                    f"{level_code}: "
                    f"xp_reward noto'g'ri."
                )

        missing_custom = sorted(
            EXPECTED_CUSTOM_EXAM_LEVELS
            - exam_level_codes
        )

        if missing_custom:
            add_error(
                "Custom exam topilmagan LEVELlar: "
                f"{missing_custom}"
            )
        else:
            add_pass(
                "LEVEL_02 dan LEVEL_15 gacha "
                "custom final examlar mavjud."
            )

    finally:
        connection.close()


# ============================================================
# 8. EXAM QUESTION BANK CAPACITY
# ============================================================

def audit_exam_question_capacity() -> None:
    section("8. EXAM QUESTION BANK CAPACITY")

    connection = get_connection()

    try:
        cursor = connection.cursor()

        required_tables = (
            "course_levels",
            "course_modules",
            "lessons",
            "quiz_questions",
            "level_exams",
        )

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

        question_columns = get_table_columns(
            cursor,
            "quiz_questions",
        )

        if "lesson_id" not in question_columns:
            add_warning(
                "quiz_questions.lesson_id yo'q. "
                "Exam savol bankini LEVEL bo'yicha "
                "hisoblab bo'lmadi."
            )
            return

        cursor.execute(
            """
            SELECT
                l.code AS level_code,
                e.question_count AS requested_questions,
                COUNT(DISTINCT q.id) AS available_questions
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
            ORDER BY l.id
            """
        )

        rows = cursor.fetchall()

        for row in rows:
            level_code = row_value(
                row,
                "level_code",
                0,
            )

            requested = row_value(
                row,
                "requested_questions",
                1,
            )

            available = row_value(
                row,
                "available_questions",
                2,
            )

            if available < requested:
                add_error(
                    f"{level_code}: final exam "
                    f"{requested} savol so'raydi, "
                    f"lekin bankda faqat "
                    f"{available} ta savol bor."
                )
            else:
                add_pass(
                    f"{level_code}: "
                    f"{available} available / "
                    f"{requested} required."
                )

    finally:
        connection.close()


# ============================================================
# 9. FOREIGN KEY CHECK
# ============================================================

def audit_foreign_keys() -> None:
    section("9. SQLITE FOREIGN KEY CHECK")

    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            "PRAGMA foreign_key_check"
        )

        rows = cursor.fetchall()

        if not rows:
            add_pass(
                "SQLite foreign_key_check: "
                "muammo topilmadi."
            )
        else:
            for row in rows:
                add_error(
                    "Foreign key muammo: "
                    f"{tuple(row)}"
                )

    finally:
        connection.close()


# ============================================================
# 10. UNIQUE INDEX CHECK
# ============================================================

def audit_unique_indexes() -> None:
    section("10. UNIQUE INDEX / ON CONFLICT AUDIT")

    connection = get_connection()

    try:
        cursor = connection.cursor()

        checks = {
            "lessons": "code",
            "quiz_questions": "code",
            "level_exams": "level_id",
            "lesson_progress": None,
            "user_level_progress": None,
        }

        for table_name, target_column in checks.items():
            if not table_exists(
                cursor,
                table_name,
            ):
                continue

            cursor.execute(
                f"PRAGMA index_list({table_name})"
            )

            indexes = cursor.fetchall()

            unique_indexes = []

            for index_row in indexes:
                try:
                    index_name = index_row["name"]
                    is_unique = index_row["unique"]
                except (TypeError, KeyError):
                    index_name = index_row[1]
                    is_unique = index_row[2]

                if not is_unique:
                    continue

                cursor.execute(
                    f"PRAGMA index_info({index_name})"
                )

                index_columns = []

                for info_row in cursor.fetchall():
                    try:
                        column_name = info_row["name"]
                    except (TypeError, KeyError):
                        column_name = info_row[2]

                    index_columns.append(
                        column_name
                    )

                unique_indexes.append(
                    (
                        index_name,
                        index_columns,
                    )
                )

            if not unique_indexes:
                add_warning(
                    f"{table_name}: "
                    "UNIQUE index topilmadi."
                )
                continue

            if target_column:
                matching = [
                    item
                    for item in unique_indexes
                    if target_column in item[1]
                ]

                if matching:
                    add_pass(
                        f"{table_name}.{target_column}: "
                        "UNIQUE constraint/index mavjud."
                    )
                else:
                    add_error(
                        f"{table_name}.{target_column}: "
                        "UNIQUE constraint topilmadi. "
                        "ON CONFLICT ishlamasligi mumkin."
                    )
            else:
                add_pass(
                    f"{table_name}: "
                    f"{len(unique_indexes)} ta "
                    "UNIQUE index mavjud."
                )

    finally:
        connection.close()


# ============================================================
# SUMMARY
# ============================================================

def print_summary() -> None:
    section("ARCHIPRO UZ DATABASE AUDIT SUMMARY")

    print(
        f"{GREEN}PASS: {len(PASSES)}{RESET}"
    )

    print(
        f"{YELLOW}WARNING: {len(WARNINGS)}{RESET}"
    )

    print(
        f"{RED}ERROR: {len(ERRORS)}{RESET}"
    )

    if ERRORS:
        print()
        print(
            f"{RED}{BOLD}"
            "TOPILGAN XATOLAR:"
            f"{RESET}"
        )

        for number, error in enumerate(
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

        for number, warning in enumerate(
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
            "ERRORlarni tuzatmasdan final "
            "release bosqichiga o'tmaymiz."
        )

    else:
        print(
            f"{GREEN}{BOLD}"
            "DATABASE AUDIT RESULT: PASSED"
            f"{RESET}"
        )

        print(
            "Database strukturasi bo'yicha "
            "kritik xato topilmadi."
        )


# ============================================================
# RUN
# ============================================================

def main() -> int:
    print()
    print(
        f"{BOLD}{CYAN}"
        "ARCHIPRO UZ — DATABASE AUDIT"
        f"{RESET}"
    )

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

    print_summary()

    return 1 if ERRORS else 0


if __name__ == "__main__":
    try:
        exit_code = main()
        raise SystemExit(exit_code)

    except KeyboardInterrupt:
        print()
        print(
            "Audit foydalanuvchi tomonidan "
            "to'xtatildi."
        )
        raise SystemExit(130)

    except Exception:
        print()
        print(
            f"{RED}{BOLD}"
            "KUTILMAGAN DATABASE AUDIT XATOSI"
            f"{RESET}"
        )

        traceback.print_exc()

        raise SystemExit(2)
