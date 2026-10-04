from __future__ import annotations

import importlib
import os
import re
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
# RESULT STORAGE
# ============================================================

ERRORS: list[str] = []
WARNINGS: list[str] = []
PASSES: list[str] = []

ALL_LESSON_CODES: list[str] = []
ALL_QUIZ_CODES: list[str] = []

IMPORTED_MODULE_COUNT = 0
IMPORTED_EXAM_COUNT = 0

TOTAL_CONTENT_LESSONS = 0
TOTAL_QUIZ_GROUPS = 0
TOTAL_QUIZ_QUESTIONS = 0


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
    print(f"{BOLD}{CYAN}{'=' * 72}{RESET}")
    print(f"{BOLD}{CYAN}{title}{RESET}")
    print(f"{BOLD}{CYAN}{'=' * 72}{RESET}")


def safe_import(module_name: str):
    try:
        return importlib.import_module(module_name)
    except Exception as exc:
        add_error(
            f"{module_name} import bo'lmadi: "
            f"{exc.__class__.__name__}: {exc}"
        )
        return None


def get_level_module_info(filename: str):
    match = re.fullmatch(
        r"level(\d{2})_module(\d{2})\.py",
        filename,
    )

    if not match:
        return None

    level_number = int(match.group(1))
    module_number = int(match.group(2))

    return level_number, module_number


def expected_names(
    level_number: int,
    module_number: int,
):
    level_text = f"{level_number:02d}"
    module_text = f"{module_number:02d}"

    base = f"LEVEL{level_text}_MODULE{module_text}"

    return {
        "lessons": f"{base}_LESSONS",
        "content": f"{base}_CONTENT",
        "quiz": f"{base}_QUIZ",
        "seeder": f"seed_level{level_text}_module{module_text}",
        "prefix": f"L{level_text}_M{module_text}",
    }


def validate_options(
    module_name: str,
    lesson_code: str,
    question_code: str,
    options: Any,
) -> None:
    if not isinstance(options, (list, tuple)):
        add_error(
            f"{module_name} | {lesson_code} | {question_code}: "
            f"'options' list/tuple emas."
        )
        return

    if len(options) < 2:
        add_error(
            f"{module_name} | {lesson_code} | {question_code}: "
            f"kamida 2 ta variant bo'lishi kerak."
        )
        return

    correct_count = 0
    option_letters: list[str] = []

    for index, option in enumerate(options, start=1):
        if not isinstance(option, (list, tuple)):
            add_error(
                f"{module_name} | {lesson_code} | {question_code}: "
                f"{index}-variant tuple/list emas."
            )
            continue

        if len(option) != 3:
            add_error(
                f"{module_name} | {lesson_code} | {question_code}: "
                f"{index}-variant 3 elementdan iborat emas."
            )
            continue

        letter, text, is_correct = option

        if not isinstance(letter, str) or not letter.strip():
            add_error(
                f"{module_name} | {lesson_code} | {question_code}: "
                f"variant harfi noto'g'ri."
            )
        else:
            option_letters.append(letter.strip())

        if not isinstance(text, str) or not text.strip():
            add_error(
                f"{module_name} | {lesson_code} | {question_code}: "
                f"variant matni bo'sh."
            )

        if not isinstance(is_correct, bool):
            add_error(
                f"{module_name} | {lesson_code} | {question_code}: "
                f"correct qiymati bool emas."
            )
        elif is_correct:
            correct_count += 1

    if len(option_letters) != len(set(option_letters)):
        add_error(
            f"{module_name} | {lesson_code} | {question_code}: "
            f"variant harflari takrorlangan."
        )

    if correct_count != 1:
        add_error(
            f"{module_name} | {lesson_code} | {question_code}: "
            f"aniq 1 ta to'g'ri javob bo'lishi kerak, "
            f"hozir {correct_count} ta."
        )


def validate_quiz_question(
    module_name: str,
    lesson_code: str,
    question: Any,
) -> None:
    global TOTAL_QUIZ_QUESTIONS

    TOTAL_QUIZ_QUESTIONS += 1

    if not isinstance(question, dict):
        add_error(
            f"{module_name} | {lesson_code}: "
            f"quiz savoli dict emas."
        )
        return

    required_fields = (
        "code",
        "question",
        "explanation",
        "options",
    )

    for field in required_fields:
        if field not in question:
            add_error(
                f"{module_name} | {lesson_code}: "
                f"quiz savolida '{field}' yo'q."
            )

    question_code = question.get("code")

    if not isinstance(question_code, str) or not question_code.strip():
        add_error(
            f"{module_name} | {lesson_code}: "
            f"quiz code noto'g'ri."
        )
        question_code = "<NO_CODE>"
    else:
        ALL_QUIZ_CODES.append(question_code)

    question_text = question.get("question")

    if not isinstance(question_text, str) or not question_text.strip():
        add_error(
            f"{module_name} | {lesson_code} | {question_code}: "
            f"savol matni bo'sh."
        )

    explanation = question.get("explanation")

    if not isinstance(explanation, str):
        add_warning(
            f"{module_name} | {lesson_code} | {question_code}: "
            f"explanation string emas."
        )

    validate_options(
        module_name=module_name,
        lesson_code=lesson_code,
        question_code=question_code,
        options=question.get("options"),
    )


# ============================================================
# MODULE AUDIT
# ============================================================

def audit_course_modules() -> None:
    global IMPORTED_MODULE_COUNT
    global TOTAL_CONTENT_LESSONS
    global TOTAL_QUIZ_GROUPS

    section("1. LEVEL MODULE FILE AUDIT")

    if not COURSES_DIR.exists():
        add_error(
            f"courses papkasi topilmadi: {COURSES_DIR}"
        )
        return

    files = sorted(
        file
        for file in COURSES_DIR.iterdir()
        if file.is_file()
        and get_level_module_info(file.name)
    )

    if not files:
        add_error(
            "levelXX_moduleYY.py fayllari topilmadi."
        )
        return

    print(
        f"Topilgan modul fayllari: {len(files)}"
    )

    for file in files:
        info = get_level_module_info(file.name)

        if info is None:
            continue

        level_number, module_number = info

        module_name = (
            f"courses."
            f"level{level_number:02d}_module{module_number:02d}"
        )

        names = expected_names(
            level_number,
            module_number,
        )

        print()
        print(
            f"{BOLD}Tekshirilmoqda: "
            f"{module_name}{RESET}"
        )

        imported = safe_import(module_name)

        if imported is None:
            continue

        IMPORTED_MODULE_COUNT += 1

        # ----------------------------------------------------
        # REQUIRED VARIABLES / FUNCTIONS
        # ----------------------------------------------------

        for key in (
            "lessons",
            "content",
            "quiz",
            "seeder",
        ):
            attribute_name = names[key]

            if not hasattr(imported, attribute_name):
                add_error(
                    f"{module_name}: "
                    f"{attribute_name} topilmadi."
                )

        if not hasattr(imported, names["content"]):
            continue

        if not hasattr(imported, names["quiz"]):
            continue

        content = getattr(
            imported,
            names["content"],
        )

        quiz = getattr(
            imported,
            names["quiz"],
        )

        lessons = getattr(
            imported,
            names["lessons"],
            None,
        )

        seeder = getattr(
            imported,
            names["seeder"],
            None,
        )

        # ----------------------------------------------------
        # SEEDER
        # ----------------------------------------------------

        if seeder is not None:
            if callable(seeder):
                add_pass(
                    f"{module_name}: "
                    f"{names['seeder']} mavjud."
                )
            else:
                add_error(
                    f"{module_name}: "
                    f"{names['seeder']} callable emas."
                )

        # ----------------------------------------------------
        # LESSONS LIST
        # ----------------------------------------------------

        lesson_list_codes: list[str] = []

        if lessons is None:
            add_error(
                f"{module_name}: "
                f"{names['lessons']} yo'q."
            )

        elif not isinstance(lessons, (list, tuple)):
            add_error(
                f"{module_name}: "
                f"{names['lessons']} list/tuple emas."
            )

        else:
            for row_index, row in enumerate(
                lessons,
                start=1,
            ):
                if not isinstance(row, (list, tuple)):
                    add_error(
                        f"{module_name}: "
                        f"LESSONS {row_index}-qator "
                        f"tuple/list emas."
                    )
                    continue

                if len(row) < 2:
                    add_error(
                        f"{module_name}: "
                        f"LESSONS {row_index}-qator "
                        f"juda qisqa."
                    )
                    continue

                module_code = row[0]
                lesson_code = row[1]

                if module_code != names["prefix"]:
                    add_error(
                        f"{module_name}: "
                        f"{lesson_code} modul kodi "
                        f"{module_code}, "
                        f"kutilgani {names['prefix']}."
                    )

                if not isinstance(
                    lesson_code,
                    str,
                ):
                    add_error(
                        f"{module_name}: "
                        f"lesson code string emas."
                    )
                    continue

                lesson_list_codes.append(
                    lesson_code
                )

        # ----------------------------------------------------
        # CONTENT
        # ----------------------------------------------------

        if not isinstance(content, dict):
            add_error(
                f"{module_name}: "
                f"{names['content']} dict emas."
            )
            continue

        content_codes = list(
            content.keys()
        )

        TOTAL_CONTENT_LESSONS += len(
            content_codes
        )

        for lesson_code in content_codes:
            if not isinstance(
                lesson_code,
                str,
            ):
                add_error(
                    f"{module_name}: "
                    f"CONTENT lesson code string emas."
                )
                continue

            ALL_LESSON_CODES.append(
                lesson_code
            )

            if not lesson_code.startswith(
                names["prefix"] + "_"
            ):
                add_error(
                    f"{module_name}: "
                    f"{lesson_code} "
                    f"{names['prefix']}_ bilan "
                    f"boshlanmaydi."
                )

            blocks = content.get(
                lesson_code
            )

            if not isinstance(
                blocks,
                (list, tuple),
            ):
                add_error(
                    f"{module_name}: "
                    f"{lesson_code} content "
                    f"list/tuple emas."
                )
                continue

            if len(blocks) == 0:
                add_warning(
                    f"{module_name}: "
                    f"{lesson_code} content bo'sh."
                )

            for block_index, block in enumerate(
                blocks,
                start=1,
            ):
                if not isinstance(
                    block,
                    dict,
                ):
                    add_error(
                        f"{module_name}: "
                        f"{lesson_code} "
                        f"{block_index}-content block "
                        f"dict emas."
                    )
                    continue

                for required in (
                    "title",
                    "type",
                    "text",
                ):
                    if required not in block:
                        add_error(
                            f"{module_name}: "
                            f"{lesson_code} "
                            f"{block_index}-blockda "
                            f"'{required}' yo'q."
                        )

        # ----------------------------------------------------
        # QUIZ
        # ----------------------------------------------------

        if not isinstance(quiz, dict):
            add_error(
                f"{module_name}: "
                f"{names['quiz']} dict emas."
            )
            continue

        quiz_lesson_codes = list(
            quiz.keys()
        )

        TOTAL_QUIZ_GROUPS += len(
            quiz_lesson_codes
        )

        for lesson_code, questions in quiz.items():
            if not isinstance(
                lesson_code,
                str,
            ):
                add_error(
                    f"{module_name}: "
                    f"QUIZ lesson code string emas."
                )
                continue

            if lesson_code not in content:
                add_error(
                    f"{module_name}: "
                    f"Quiz {lesson_code} uchun "
                    f"content topilmadi."
                )

            if not isinstance(
                questions,
                (list, tuple),
            ):
                add_error(
                    f"{module_name}: "
                    f"{lesson_code} quiz list/tuple emas."
                )
                continue

            if len(questions) == 0:
                add_warning(
                    f"{module_name}: "
                    f"{lesson_code} quiz bo'sh."
                )

            for question in questions:
                validate_quiz_question(
                    module_name=module_name,
                    lesson_code=lesson_code,
                    question=question,
                )

        # ----------------------------------------------------
        # CROSS CHECK
        # ----------------------------------------------------

        content_set = set(
            content_codes
        )

        quiz_set = set(
            quiz_lesson_codes
        )

        if lesson_list_codes:
            lesson_list_set = set(
                lesson_list_codes
            )

            missing_content = (
                lesson_list_set - content_set
            )

            extra_content = (
                content_set - lesson_list_set
            )

            if missing_content:
                add_error(
                    f"{module_name}: "
                    f"LESSONS bor, CONTENT yo'q: "
                    f"{sorted(missing_content)}"
                )

            if extra_content:
                add_error(
                    f"{module_name}: "
                    f"CONTENT bor, LESSONS yo'q: "
                    f"{sorted(extra_content)}"
                )

        missing_quiz = (
            content_set - quiz_set
        )

        extra_quiz = (
            quiz_set - content_set
        )

        if missing_quiz:
            add_error(
                f"{module_name}: "
                f"quiz yo'q lessonlar: "
                f"{sorted(missing_quiz)}"
            )

        if extra_quiz:
            add_error(
                f"{module_name}: "
                f"content yo'q quiz lessonlar: "
                f"{sorted(extra_quiz)}"
            )

        if (
            not missing_quiz
            and not extra_quiz
            and content_set
        ):
            add_pass(
                f"{module_name}: "
                f"content va quiz lessonlari mos "
                f"({len(content_set)} ta)."
            )


# ============================================================
# SPECIAL LEVEL 0 / LEVEL 1 BASE FILE AUDIT
# ============================================================

def audit_special_course_files() -> None:
    section("2. SPECIAL COURSE FILE AUDIT")

    special_modules = [
        (
            "courses.level00_extra",
            "LEVEL00_EXTRA_CONTENT",
            "LEVEL00_EXTRA_QUIZ",
            "seed_level00_extra",
        ),
        (
            "courses.level01_content",
            "LEVEL01_CONTENT",
            "LEVEL01_QUIZ",
            "seed_level01_lessons",
        ),
    ]

    for (
        module_name,
        content_name,
        quiz_name,
        seeder_name,
    ) in special_modules:

        imported = safe_import(
            module_name
        )

        if imported is None:
            continue

        for attribute_name in (
            content_name,
            quiz_name,
            seeder_name,
        ):
            if not hasattr(
                imported,
                attribute_name,
            ):
                add_error(
                    f"{module_name}: "
                    f"{attribute_name} topilmadi."
                )

        seeder = getattr(
            imported,
            seeder_name,
            None,
        )

        if seeder is not None:
            if callable(seeder):
                add_pass(
                    f"{module_name}: "
                    f"{seeder_name} mavjud."
                )
            else:
                add_error(
                    f"{module_name}: "
                    f"{seeder_name} callable emas."
                )


# ============================================================
# EXAM FILE AUDIT
# ============================================================

def audit_exam_files() -> None:
    global IMPORTED_EXAM_COUNT

    section("3. LEVEL EXAM FILE AUDIT")

    exam_files = sorted(
        file
        for file in COURSES_DIR.glob(
            "level??_exam.py"
        )
        if file.is_file()
    )

    if not exam_files:
        add_warning(
            "levelXX_exam.py fayllari topilmadi."
        )
        return

    print(
        f"Topilgan maxsus exam fayllari: "
        f"{len(exam_files)}"
    )

    for file in exam_files:
        match = re.fullmatch(
            r"level(\d{2})_exam\.py",
            file.name,
        )

        if not match:
            continue

        level_number = int(
            match.group(1)
        )

        module_name = (
            f"courses.level{level_number:02d}_exam"
        )

        exam_var = (
            f"LEVEL{level_number:02d}_EXAM"
        )

        seeder_name = (
            f"seed_level{level_number:02d}_exam"
        )

        imported = safe_import(
            module_name
        )

        if imported is None:
            continue

        IMPORTED_EXAM_COUNT += 1

        if not hasattr(
            imported,
            exam_var,
        ):
            add_error(
                f"{module_name}: "
                f"{exam_var} topilmadi."
            )

        if not hasattr(
            imported,
            seeder_name,
        ):
            add_error(
                f"{module_name}: "
                f"{seeder_name} topilmadi."
            )

        else:
            seeder = getattr(
                imported,
                seeder_name,
            )

            if not callable(seeder):
                add_error(
                    f"{module_name}: "
                    f"{seeder_name} callable emas."
                )

        exam_data = getattr(
            imported,
            exam_var,
            None,
        )

        if exam_data is None:
            continue

        if not isinstance(
            exam_data,
            dict,
        ):
            add_error(
                f"{module_name}: "
                f"{exam_var} dict emas."
            )
            continue

        required_fields = (
            "level_code",
            "title",
            "description",
            "question_count",
            "passing_score",
            "xp_reward",
        )

        for field in required_fields:
            if field not in exam_data:
                add_error(
                    f"{module_name}: "
                    f"exam field '{field}' yo'q."
                )

        expected_level_code = (
            f"LEVEL_{level_number:02d}"
        )

        if (
            exam_data.get("level_code")
            != expected_level_code
        ):
            add_error(
                f"{module_name}: "
                f"level_code "
                f"{exam_data.get('level_code')} "
                f"kutilgani "
                f"{expected_level_code}."
            )

        question_count = exam_data.get(
            "question_count"
        )

        if not isinstance(
            question_count,
            int,
        ) or question_count <= 0:
            add_error(
                f"{module_name}: "
                f"question_count noto'g'ri."
            )

        passing_score = exam_data.get(
            "passing_score"
        )

        if not isinstance(
            passing_score,
            int,
        ) or not 0 < passing_score <= 100:
            add_error(
                f"{module_name}: "
                f"passing_score noto'g'ri."
            )

        add_pass(
            f"{module_name}: "
            f"exam strukturasi tekshirildi."
        )


# ============================================================
# GLOBAL DUPLICATE AUDIT
# ============================================================

def audit_duplicates() -> None:
    section("4. GLOBAL DUPLICATE AUDIT")

    lesson_counter = Counter(
        ALL_LESSON_CODES
    )

    duplicate_lessons = sorted(
        code
        for code, count
        in lesson_counter.items()
        if count > 1
    )

    if duplicate_lessons:
        for code in duplicate_lessons:
            add_error(
                f"Duplicate lesson code: "
                f"{code} "
                f"({lesson_counter[code]} marta)"
            )
    else:
        add_pass(
            "Level modul fayllarida "
            "duplicate lesson code topilmadi."
        )

    quiz_counter = Counter(
        ALL_QUIZ_CODES
    )

    duplicate_quizzes = sorted(
        code
        for code, count
        in quiz_counter.items()
        if count > 1
    )

    if duplicate_quizzes:
        for code in duplicate_quizzes:
            add_error(
                f"Duplicate quiz code: "
                f"{code} "
                f"({quiz_counter[code]} marta)"
            )
    else:
        add_pass(
            "Level modul fayllarida "
            "duplicate quiz code topilmadi."
        )


# ============================================================
# REGISTRY IMPORT AUDIT
# ============================================================

def audit_content_registry() -> None:
    section("5. CONTENT REGISTRY AUDIT")

    registry = safe_import(
        "courses.content_registry"
    )

    if registry is None:
        return

    required_functions = (
        "get_all_lesson_content",
        "get_lesson_content_by_code",
        "get_all_quiz_data",
    )

    for function_name in required_functions:
        function = getattr(
            registry,
            function_name,
            None,
        )

        if function is None:
            add_error(
                f"content_registry.py: "
                f"{function_name} yo'q."
            )

        elif not callable(function):
            add_error(
                f"content_registry.py: "
                f"{function_name} callable emas."
            )

        else:
            add_pass(
                f"content_registry.py: "
                f"{function_name} mavjud."
            )

    try:
        all_content = (
            registry.get_all_lesson_content()
        )

        all_quiz = (
            registry.get_all_quiz_data()
        )

        if not isinstance(
            all_content,
            dict,
        ):
            add_error(
                "get_all_lesson_content() "
                "dict qaytarmadi."
            )

        else:
            add_pass(
                f"Registry lesson content: "
                f"{len(all_content)} ta."
            )

        if not isinstance(
            all_quiz,
            dict,
        ):
            add_error(
                "get_all_quiz_data() "
                "dict qaytarmadi."
            )

        else:
            registry_question_count = 0

            for questions in all_quiz.values():
                if isinstance(
                    questions,
                    (list, tuple),
                ):
                    registry_question_count += len(
                        questions
                    )

            add_pass(
                f"Registry quiz lesson groups: "
                f"{len(all_quiz)} ta."
            )

            add_pass(
                f"Registry quiz questions: "
                f"{registry_question_count} ta."
            )

    except Exception as exc:
        add_error(
            "content_registry funksiyalarini "
            f"ishga tushirishda xato: {exc}"
        )


# ============================================================
# MAIN.PY STATIC CHECK
# ============================================================

def audit_main_file() -> None:
    section("6. MAIN.PY STATIC AUDIT")

    main_file = APP_DIR / "main.py"

    if not main_file.exists():
        add_error(
            f"main.py topilmadi: "
            f"{main_file}"
        )
        return

    try:
        source = main_file.read_text(
            encoding="utf-8"
        )
    except Exception as exc:
        add_error(
            f"main.py o'qilmadi: {exc}"
        )
        return

    required_texts = [
        "seed_level15_module01",
        "seed_level15_module02",
        "seed_level15_module03",
        "seed_level15_module04",
        "seed_level15_module05",
        "seed_level15_module06",
        "seed_level15_module07",
        "seed_level15_module08",
        "seed_level15_exam",
    ]

    for text_value in required_texts:
        if text_value not in source:
            add_error(
                f"main.py ichida "
                f"{text_value} topilmadi."
            )
        else:
            add_pass(
                f"main.py: "
                f"{text_value} topildi."
            )

    if (
        'username="admin"' in source
        and 'password="12345"' in source
    ):
        add_warning(
            "main.py ichida development "
            "MASTER admin / 12345 mavjud. "
            "Sotuv versiyasidan oldin olib tashlanadi."
        )

    # --------------------------------------------------------
    # LICENSE / ACTIVATION GATE
    # --------------------------------------------------------

    activation_required_texts = [
        "validate_installed_license",
        "ActivationWindow",
        "show_activation",
        "show_login",
        "activation_successful.connect",
    ]

    for text_value in activation_required_texts:
        if text_value not in source:
            add_error(
                "main.py startup license gate ichida "
                f"{text_value} topilmadi."
            )
        else:
            add_pass(
                "main.py startup license gate: "
                f"{text_value} mavjud."
            )

    if "initial_license_result" in source:
        add_pass(
            "main.py: birinchi ekran license holatiga bog'langan."
        )
    else:
        add_error(
            "main.py: initial license gate topilmadi."
        )

    # --------------------------------------------------------
    # APP SHELL MENU CONTRACT
    # --------------------------------------------------------

    app_shell_file = APP_DIR / "ui" / "app_shell.py"

    if app_shell_file.exists():
        try:
            app_shell_source = app_shell_file.read_text(
                encoding="utf-8"
            )

            if (
                '"Testlar",\\n            "Testlar",'
                in app_shell_source
            ):
                add_error(
                    "app_shell.py menu ichida Testlar dublikat."
                )
            else:
                add_pass(
                    "app_shell.py menu: Testlar dublikat emas."
                )

            required_menu_items = [
                "Qurilish konstruksiyalari",
                "SHNQ va normativlar",
                "BIM va real loyiha",
                "Portfolio / PRO Final",
                "Litsenziya",
            ]

            for menu_text in required_menu_items:
                if menu_text in app_shell_source:
                    add_pass(
                        f"app_shell.py menu: {menu_text} mavjud."
                    )
                else:
                    add_error(
                        f"app_shell.py menu: {menu_text} topilmadi."
                    )

        except Exception as exc:
            add_error(
                "app_shell.py menu audit xatosi: "
                f"{exc}"
            )


# ============================================================
# CUSTOMER CONVENIENCE AUDIT
# ============================================================

def audit_customer_features() -> None:
    section("7. CUSTOMER CONVENIENCE AUDIT")

    required_files = {
        APP_DIR / "courses" / "user_features.py": [
            "get_recent_lessons",
            "set_lesson_bookmark",
            "save_lesson_note",
            "get_user_notes_map",
            "export_user_backup",
            "import_user_backup",
        ],
        APP_DIR / "ui" / "library_page.py": [
            "open_lesson_requested",
            "FAQAT BOOKMARKLAR",
            "FAQAT ESLATMALAR",
            "focus_search",
        ],
        APP_DIR / "ui" / "glossary_page.py": [
            "GLOSSARY",
            "Terminlar lug'ati",
        ],
        APP_DIR / "ui" / "help_page.py": [
            "HELP_ITEMS",
            "Yordam markazi",
        ],
        APP_DIR / "ui" / "settings_page.py": [
            "BACKUP YARATISH",
            "BACKUPNI TIKLASH",
            "backup_imported",
        ],
        APP_DIR / "ui" / "embedded_pages.py": [
            "BOOKMARK",
            "MENING ESLATMAM",
            "KEYINGI DARS",
            "open_next_lesson_callback",
        ],
        APP_DIR / "ui" / "app_shell.py": [
            "Ctrl+K",
            "Ctrl+Right",
            "YAQINDA KO'RILGAN DARSLAR",
            "Terminlar lug'ati",
            "Yordam",
            "continue_learning",
        ],
        APP_DIR / "database" / "database.py": [
            "lesson_bookmarks",
            "lesson_notes",
            "idx_bookmarks_user",
            "idx_notes_user",
        ],
        APP_DIR / "tools" / "customer_features_smoke_test.py": [
            "CUSTOMER FEATURES SMOKE TEST",
            "export_user_backup",
            "import_user_backup",
        ],
    }

    for file_path, required_texts in required_files.items():
        if not file_path.exists():
            add_error(
                f"Customer feature fayli topilmadi: {file_path}"
            )
            continue

        try:
            source = file_path.read_text(
                encoding="utf-8"
            )
        except Exception as exc:
            add_error(
                f"{file_path.name} o'qilmadi: {exc}"
            )
            continue

        try:
            compile(
                source,
                str(
                    file_path
                ),
                "exec",
            )

            add_pass(
                f"{file_path.name}: Python syntax PASS."
            )

        except SyntaxError as exc:
            add_error(
                f"{file_path.name}: syntax xato: {exc}"
            )

        for text_value in required_texts:
            if text_value in source:
                add_pass(
                    f"{file_path.name}: {text_value} mavjud."
                )
            else:
                add_error(
                    f"{file_path.name}: {text_value} topilmadi."
                )

# ============================================================
# SUMMARY
# ============================================================

def print_summary() -> None:
    section("ARCHIPRO UZ AUDIT SUMMARY")

    print(
        f"Import bo'lgan level module fayllari: "
        f"{IMPORTED_MODULE_COUNT}"
    )

    print(
        f"Import bo'lgan custom exam fayllari: "
        f"{IMPORTED_EXAM_COUNT}"
    )

    print(
        f"Modul content lessonlari: "
        f"{TOTAL_CONTENT_LESSONS}"
    )

    print(
        f"Quiz lesson groups: "
        f"{TOTAL_QUIZ_GROUPS}"
    )

    print(
        f"Quiz savollari: "
        f"{TOTAL_QUIZ_QUESTIONS}"
    )

    print()
    print(
        f"{GREEN}PASS: "
        f"{len(PASSES)}{RESET}"
    )

    print(
        f"{YELLOW}WARNING: "
        f"{len(WARNINGS)}{RESET}"
    )

    print(
        f"{RED}ERROR: "
        f"{len(ERRORS)}{RESET}"
    )

    if ERRORS:
        print()
        print(
            f"{RED}{BOLD}"
            f"TOPILGAN XATOLAR:"
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
            f"OGOHLANTIRISHLAR:"
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
            f"AUDIT RESULT: FAILED"
            f"{RESET}"
        )
        print(
            "Avval yuqoridagi ERRORlarni "
            "tuzatish kerak."
        )
    else:
        print(
            f"{GREEN}{BOLD}"
            f"AUDIT RESULT: PASSED"
            f"{RESET}"
        )
        print(
            "Import va kontent strukturasi "
            "bo'yicha kritik xato topilmadi."
        )


# ============================================================
# RUN
# ============================================================

def main() -> int:
    print()
    print(
        f"{BOLD}{CYAN}"
        f"ARCHIPRO UZ — PROJECT AUDIT"
        f"{RESET}"
    )

    print(
        f"APP_DIR: {APP_DIR}"
    )

    print(
        f"COURSES_DIR: {COURSES_DIR}"
    )

    audit_course_modules()
    audit_special_course_files()
    audit_exam_files()
    audit_duplicates()
    audit_content_registry()
    audit_main_file()
    audit_customer_features()
    print_summary()

    return 1 if ERRORS else 0


if __name__ == "__main__":
    try:
        exit_code = main()
        raise SystemExit(exit_code)

    except KeyboardInterrupt:
        print(
            "\nAudit foydalanuvchi tomonidan "
            "to'xtatildi."
        )
        raise SystemExit(130)

    except Exception:
        print()
        print(
            f"{RED}{BOLD}"
            f"KUTILMAGAN AUDIT XATOSI"
            f"{RESET}"
        )
        traceback.print_exc()
        raise SystemExit(2)
