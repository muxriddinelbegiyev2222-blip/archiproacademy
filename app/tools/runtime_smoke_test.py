from __future__ import annotations

import importlib
import py_compile
import re
import sys
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
# COLORS
# ============================================================

RESET = "\033[0m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
CYAN = "\033[96m"
BOLD = "\033[1m"


# ============================================================
# RESULTS
# ============================================================

ERRORS: list[str] = []
WARNINGS: list[str] = []
PASSES: list[str] = []

COMPILED_FILES = 0
IMPORTED_MODULES = 0


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
    print(f"{BOLD}{CYAN}{'=' * 76}{RESET}")
    print(f"{BOLD}{CYAN}{title}{RESET}")
    print(f"{BOLD}{CYAN}{'=' * 76}{RESET}")


def safe_import(module_name: str):
    global IMPORTED_MODULES

    try:
        module = importlib.import_module(
            module_name
        )

        IMPORTED_MODULES += 1

        add_pass(
            f"Import ishladi: {module_name}"
        )

        return module

    except Exception as exc:
        add_error(
            f"Import FAILED: {module_name} | "
            f"{exc.__class__.__name__}: {exc}"
        )

        return None


def module_path_to_import_name(
    path: Path,
) -> str | None:

    try:
        relative = path.relative_to(
            APP_DIR
        )

    except ValueError:
        return None

    if path.name == "__init__.py":
        parts = list(
            relative.parent.parts
        )
    else:
        parts = list(
            relative.with_suffix("").parts
        )

    if not parts:
        return None

    return ".".join(parts)


# ============================================================
# 1. PYTHON VERSION
# ============================================================

def audit_python_version() -> None:
    section("1. PYTHON RUNTIME")

    version = sys.version_info

    print(
        "Python version: "
        f"{version.major}."
        f"{version.minor}."
        f"{version.micro}"
    )

    if version.major != 3:
        add_error(
            "Python 3 ishlatilmayapti."
        )
    else:
        add_pass(
            "Python 3 runtime ishlayapti."
        )


# ============================================================
# 2. APP STRUCTURE
# ============================================================

def audit_directories() -> None:
    section("2. PROJECT STRUCTURE")

    required_paths = [
        APP_DIR / "main.py",
        APP_DIR / "auth",
        APP_DIR / "courses",
        APP_DIR / "database",
        APP_DIR / "ui",
        APP_DIR / "tools",
    ]

    for path in required_paths:
        if path.exists():
            add_pass(
                f"Mavjud: {path.relative_to(APP_DIR.parent)}"
            )
        else:
            add_error(
                f"Topilmadi: {path}"
            )


# ============================================================
# 3. SYNTAX COMPILE TEST
# ============================================================

def audit_python_syntax() -> None:
    global COMPILED_FILES

    section("3. PYTHON SYNTAX COMPILE TEST")

    python_files = sorted(
        path
        for path in APP_DIR.rglob("*.py")
        if "__pycache__" not in path.parts
    )

    print(
        f"Topilgan Python fayllari: "
        f"{len(python_files)}"
    )

    for path in python_files:
        relative = path.relative_to(
            APP_DIR.parent
        )

        try:
            py_compile.compile(
                str(path),
                doraise=True,
            )

            COMPILED_FILES += 1

        except py_compile.PyCompileError as exc:
            add_error(
                f"Syntax xato: {relative}\n"
                f"{exc.msg}"
            )

        except Exception as exc:
            add_error(
                f"Compile xato: {relative} | "
                f"{exc.__class__.__name__}: {exc}"
            )

    if (
        python_files
        and COMPILED_FILES == len(python_files)
    ):
        add_pass(
            f"Barcha {COMPILED_FILES} ta "
            "Python fayl syntax testdan o'tdi."
        )


# ============================================================
# 4. CRITICAL PACKAGE IMPORTS
# ============================================================

def audit_critical_packages() -> None:
    section("4. CRITICAL PACKAGE IMPORTS")

    required_packages = [
        "PySide6",
        "sqlite3",
    ]

    for package in required_packages:
        safe_import(package)


# ============================================================
# 5. DATABASE MODULE IMPORT
# ============================================================

def audit_database_imports() -> None:
    section("5. DATABASE IMPORTS")

    database_module = safe_import(
        "database.database"
    )

    if database_module is None:
        return

    required_functions = [
        "get_connection",
        "initialize_database",
    ]

    for function_name in required_functions:
        value = getattr(
            database_module,
            function_name,
            None,
        )

        if value is None:
            add_error(
                "database.database ichida "
                f"{function_name} topilmadi."
            )

        elif not callable(value):
            add_error(
                "database.database."
                f"{function_name} callable emas."
            )

        else:
            add_pass(
                "database.database."
                f"{function_name} mavjud."
            )


# ============================================================
# 6. AUTH IMPORTS
# ============================================================

def audit_auth_imports() -> None:
    section("6. AUTH IMPORTS")

    auth_service = safe_import(
        "auth.auth_service"
    )

    if auth_service is None:
        return

    required_functions = [
        "authenticate_user",
        "create_user",
    ]

    for function_name in required_functions:
        function = getattr(
            auth_service,
            function_name,
            None,
        )

        if callable(function):
            add_pass(
                f"auth_service.{function_name} mavjud."
            )
        else:
            add_error(
                f"auth_service.{function_name} "
                "topilmadi yoki callable emas."
            )


# ============================================================
# 7. COURSE SERVICE IMPORTS
# ============================================================

def audit_course_services() -> None:
    section("7. COURSE SERVICE IMPORTS")

    checks = {
        "courses.course_service": [
            "initialize_user_progress",
        ],
        "courses.access_sync": [
            "synchronize_user_access",
        ],
        "courses.quiz_service": [
            "seed_quizzes",
        ],
        "courses.exam_service": [
            "initialize_user_levels",
            "seed_level_exams",
        ],
        "courses.seed_courses": [
            "seed_course_structure",
        ],
        "courses.user_features": [
            "get_recent_lessons",
            "set_lesson_bookmark",
            "save_lesson_note",
            "get_user_notes_map",
            "export_user_backup",
            "import_user_backup",
        ],
    }

    for module_name, functions in checks.items():
        module = safe_import(
            module_name
        )

        if module is None:
            continue

        for function_name in functions:
            function = getattr(
                module,
                function_name,
                None,
            )

            if callable(function):
                add_pass(
                    f"{module_name}."
                    f"{function_name} mavjud."
                )
            else:
                add_error(
                    f"{module_name}."
                    f"{function_name} "
                    "topilmadi yoki callable emas."
                )


# ============================================================
# 8. ALL LEVEL MODULE IMPORTS
# ============================================================

def audit_level_modules() -> None:
    section("8. ALL LEVEL MODULE IMPORTS")

    if not COURSES_DIR.exists():
        add_error(
            "courses papkasi topilmadi."
        )
        return

    files = sorted(
        COURSES_DIR.glob(
            "level??_module??.py"
        )
    )

    print(
        f"Topilgan level module fayllari: "
        f"{len(files)}"
    )

    for path in files:
        match = re.fullmatch(
            r"level(\d{2})_module(\d{2})\.py",
            path.name,
        )

        if not match:
            continue

        level_number = match.group(1)
        module_number = match.group(2)

        import_name = (
            f"courses.level{level_number}"
            f"_module{module_number}"
        )

        module = safe_import(
            import_name
        )

        if module is None:
            continue

        expected_seeder = (
            f"seed_level{level_number}"
            f"_module{module_number}"
        )

        seeder = getattr(
            module,
            expected_seeder,
            None,
        )

        if callable(seeder):
            add_pass(
                f"{import_name}: "
                f"{expected_seeder} mavjud."
            )
        else:
            add_error(
                f"{import_name}: "
                f"{expected_seeder} topilmadi."
            )


# ============================================================
# 9. SPECIAL CONTENT FILES
# ============================================================

def audit_special_content_files() -> None:
    section("9. SPECIAL CONTENT IMPORTS")

    checks = {
        "courses.level00_extra": [
            "LEVEL00_EXTRA_CONTENT",
            "LEVEL00_EXTRA_QUIZ",
            "seed_level00_extra",
        ],
        "courses.level01_content": [
            "LEVEL01_CONTENT",
            "LEVEL01_QUIZ",
            "seed_level01_lessons",
        ],
    }

    for module_name, names in checks.items():
        module = safe_import(
            module_name
        )

        if module is None:
            continue

        for name in names:
            if hasattr(
                module,
                name,
            ):
                add_pass(
                    f"{module_name}.{name} mavjud."
                )
            else:
                add_error(
                    f"{module_name}.{name} topilmadi."
                )


# ============================================================
# 10. EXAM IMPORTS
# ============================================================

def audit_exam_modules() -> None:
    section("10. LEVEL EXAM IMPORTS")

    exam_files = sorted(
        COURSES_DIR.glob(
            "level??_exam.py"
        )
    )

    print(
        f"Topilgan custom exam fayllari: "
        f"{len(exam_files)}"
    )

    for path in exam_files:
        match = re.fullmatch(
            r"level(\d{2})_exam\.py",
            path.name,
        )

        if not match:
            continue

        level_number = match.group(1)

        module_name = (
            f"courses.level{level_number}_exam"
        )

        module = safe_import(
            module_name
        )

        if module is None:
            continue

        exam_name = (
            f"LEVEL{level_number}_EXAM"
        )

        seeder_name = (
            f"seed_level{level_number}_exam"
        )

        if hasattr(
            module,
            exam_name,
        ):
            add_pass(
                f"{module_name}.{exam_name} mavjud."
            )
        else:
            add_error(
                f"{module_name}.{exam_name} topilmadi."
            )

        seeder = getattr(
            module,
            seeder_name,
            None,
        )

        if callable(seeder):
            add_pass(
                f"{module_name}.{seeder_name} mavjud."
            )
        else:
            add_error(
                f"{module_name}.{seeder_name} "
                "topilmadi yoki callable emas."
            )


# ============================================================
# 11. CONTENT REGISTRY RUNTIME
# ============================================================

def audit_content_registry() -> None:
    section("11. CONTENT REGISTRY RUNTIME")

    registry = safe_import(
        "courses.content_registry"
    )

    if registry is None:
        return

    try:
        lesson_content = (
            registry.get_all_lesson_content()
        )

        quiz_data = (
            registry.get_all_quiz_data()
        )

        if isinstance(
            lesson_content,
            dict,
        ):
            add_pass(
                "get_all_lesson_content() ishladi: "
                f"{len(lesson_content)} lesson content."
            )
        else:
            add_error(
                "get_all_lesson_content() "
                "dict qaytarmadi."
            )

        if isinstance(
            quiz_data,
            dict,
        ):
            question_count = 0

            for questions in quiz_data.values():
                if isinstance(
                    questions,
                    (list, tuple),
                ):
                    question_count += len(
                        questions
                    )

            add_pass(
                "get_all_quiz_data() ishladi: "
                f"{len(quiz_data)} lesson group, "
                f"{question_count} savol."
            )

        else:
            add_error(
                "get_all_quiz_data() dict qaytarmadi."
            )

    except Exception as exc:
        add_error(
            "Content registry runtime xato: "
            f"{exc.__class__.__name__}: {exc}"
        )


# ============================================================
# 12. UI IMPORTS
# ============================================================

def audit_ui_imports() -> None:
    section("12. UI IMPORTS")

    ui_files = sorted(
        path
        for path in (
            APP_DIR / "ui"
        ).glob("*.py")
        if path.name != "__init__.py"
    )

    if not ui_files:
        add_warning(
            "ui/*.py fayllari topilmadi."
        )
        return

    for path in ui_files:
        module_name = (
            f"ui.{path.stem}"
        )

        safe_import(
            module_name
        )


# ============================================================
# 13. EXAM WINDOW CONTRACT
# ============================================================

def audit_exam_window() -> None:
    section("13. EXAM WINDOW CONTRACT")

    module = safe_import(
        "ui.exam_window"
    )

    if module is None:
        return

    exam_window = getattr(
        module,
        "ExamWindow",
        None,
    )

    if exam_window is None:
        add_error(
            "ui.exam_window.ExamWindow topilmadi."
        )
        return

    add_pass(
        "ExamWindow class mavjud."
    )

    required_methods = [
        "load_exam",
        "show_success",
    ]

    for method_name in required_methods:
        method = getattr(
            exam_window,
            method_name,
            None,
        )

        if callable(method):
            add_pass(
                f"ExamWindow.{method_name} mavjud."
            )
        else:
            add_error(
                f"ExamWindow.{method_name} topilmadi."
            )


# ============================================================
# 14. MAIN.PY IMPORT TEST
# ============================================================

def audit_main_import() -> None:
    section("14. MAIN.PY IMPORT TEST")

    try:
        main_module = importlib.import_module(
            "main"
        )

        add_pass(
            "main.py import qilindi."
        )

    except Exception as exc:
        add_error(
            "main.py import FAILED: "
            f"{exc.__class__.__name__}: {exc}"
        )
        return

    prepare_application = getattr(
        main_module,
        "prepare_application",
        None,
    )

    main_function = getattr(
        main_module,
        "main",
        None,
    )

    if callable(
        prepare_application
    ):
        add_pass(
            "main.prepare_application mavjud."
        )
    else:
        add_error(
            "main.prepare_application "
            "topilmadi yoki callable emas."
        )

    if callable(
        main_function
    ):
        add_pass(
            "main.main mavjud."
        )
    else:
        add_error(
            "main.main topilmadi yoki callable emas."
        )

    module_seeders = getattr(
        main_module,
        "MODULE_SEEDERS",
        None,
    )

    if isinstance(
        module_seeders,
        (list, tuple),
    ):
        add_pass(
            "MODULE_SEEDERS runtime mavjud: "
            f"{len(module_seeders)} ta seeder."
        )

        bad_seeders = [
            seeder
            for seeder in module_seeders
            if not callable(seeder)
        ]

        if bad_seeders:
            add_error(
                "MODULE_SEEDERS ichida "
                f"{len(bad_seeders)} ta "
                "callable bo'lmagan element bor."
            )
        else:
            add_pass(
                "MODULE_SEEDERS ichidagi "
                "barcha element callable."
            )

    else:
        add_error(
            "main.MODULE_SEEDERS "
            "list/tuple sifatida topilmadi."
        )

    custom_exams = getattr(
        main_module,
        "CUSTOM_EXAM_SEEDERS",
        None,
    )

    if isinstance(
        custom_exams,
        (list, tuple),
    ):
        add_pass(
            "CUSTOM_EXAM_SEEDERS runtime mavjud: "
            f"{len(custom_exams)} ta."
        )

        bad_exams = [
            seeder
            for seeder in custom_exams
            if not callable(seeder)
        ]

        if bad_exams:
            add_error(
                "CUSTOM_EXAM_SEEDERS ichida "
                f"{len(bad_exams)} ta "
                "callable bo'lmagan element bor."
            )
        else:
            add_pass(
                "CUSTOM_EXAM_SEEDERS ichidagi "
                "barcha element callable."
            )

    else:
        add_error(
            "main.CUSTOM_EXAM_SEEDERS "
            "list/tuple sifatida topilmadi."
        )


# ============================================================
# 15. DUPLICATE MODULE SEEDERS
# ============================================================

def audit_main_duplicates() -> None:
    section("15. MAIN SEEDER DUPLICATE TEST")

    main_module = sys.modules.get(
        "main"
    )

    if main_module is None:
        try:
            main_module = importlib.import_module(
                "main"
            )
        except Exception:
            add_warning(
                "main import bo'lmagani uchun "
                "duplicate seeder testi o'tkazilmadi."
            )
            return

    module_seeders = getattr(
        main_module,
        "MODULE_SEEDERS",
        (),
    )

    seeder_names = [
        getattr(
            item,
            "__name__",
            str(item),
        )
        for item in module_seeders
    ]

    duplicates = sorted(
        {
            name
            for name in seeder_names
            if seeder_names.count(name) > 1
        }
    )

    if duplicates:
        for name in duplicates:
            add_error(
                "MODULE_SEEDERS duplicate: "
                f"{name}"
            )
    else:
        add_pass(
            "MODULE_SEEDERS duplicate "
            "funksiya topilmadi."
        )

    exam_seeders = getattr(
        main_module,
        "CUSTOM_EXAM_SEEDERS",
        (),
    )

    exam_names = [
        getattr(
            item,
            "__name__",
            str(item),
        )
        for item in exam_seeders
    ]

    exam_duplicates = sorted(
        {
            name
            for name in exam_names
            if exam_names.count(name) > 1
        }
    )

    if exam_duplicates:
        for name in exam_duplicates:
            add_error(
                "CUSTOM_EXAM_SEEDERS duplicate: "
                f"{name}"
            )
    else:
        add_pass(
            "CUSTOM_EXAM_SEEDERS duplicate "
            "funksiya topilmadi."
        )


# ============================================================
# SUMMARY
# ============================================================

def print_summary() -> None:
    section("ARCHIPRO UZ RUNTIME SMOKE TEST SUMMARY")

    print(
        f"Compiled Python files: "
        f"{COMPILED_FILES}"
    )

    print(
        f"Successful imports: "
        f"{IMPORTED_MODULES}"
    )

    print()

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
            "TOPILGAN RUNTIME XATOLAR:"
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
            "RUNTIME SMOKE TEST: FAILED"
            f"{RESET}"
        )

        print(
            "Dastur release qilishdan oldin "
            "yuqoridagi runtime xatolarni "
            "tuzatamiz."
        )

    else:
        print(
            f"{GREEN}{BOLD}"
            "RUNTIME SMOKE TEST: PASSED"
            f"{RESET}"
        )

        print(
            "Syntax va import bosqichida "
            "kritik xato topilmadi."
        )


# ============================================================
# RUN
# ============================================================

def main() -> int:
    print()
    print(
        f"{BOLD}{CYAN}"
        "ARCHIPRO UZ — RUNTIME SMOKE TEST"
        f"{RESET}"
    )

    print(
        f"APP_DIR: {APP_DIR}"
    )

    audit_python_version()
    audit_directories()
    audit_python_syntax()
    audit_critical_packages()
    audit_database_imports()
    audit_auth_imports()
    audit_course_services()
    audit_level_modules()
    audit_special_content_files()
    audit_exam_modules()
    audit_content_registry()
    audit_ui_imports()
    audit_exam_window()
    audit_main_import()
    audit_main_duplicates()

    print_summary()

    return 1 if ERRORS else 0


if __name__ == "__main__":
    try:
        exit_code = main()
        raise SystemExit(
            exit_code
        )

    except KeyboardInterrupt:
        print()
        print(
            "Smoke test foydalanuvchi "
            "tomonidan to'xtatildi."
        )

        raise SystemExit(130)

    except Exception:
        print()
        print(
            f"{RED}{BOLD}"
            "KUTILMAGAN RUNTIME TEST XATOSI"
            f"{RESET}"
        )

        traceback.print_exc()

        raise SystemExit(2)
