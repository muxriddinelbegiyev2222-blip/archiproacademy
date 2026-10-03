import sys
from pathlib import Path


APP_DIR = Path(__file__).resolve().parents[1]

if str(APP_DIR) not in sys.path:
    sys.path.insert(
        0,
        str(APP_DIR),
    )


EXPECTED_LEVELS = 16
EXPECTED_MODULES = 137
EXPECTED_LESSON_CONTENT = 680
EXPECTED_QUIZ_GROUPS = 680
EXPECTED_QUIZ_QUESTIONS = 2041


def pass_message(text):
    print(
        f"[PASS] {text}"
    )


def error_message(text):
    print(
        f"[ERROR] {text}"
    )


def main():
    print(
        "=" * 60
    )

    print(
        "ARCHIPRO UZ CONTENT GUARD"
    )

    print(
        "=" * 60
    )

    errors = []

    # ========================================================
    # LEVEL VA MODULE
    # ========================================================

    try:
        from courses.seed_courses import (
            LEVELS,
            MODULES,
        )
    except ImportError:
        try:
            from seed_courses import (
                LEVELS,
                MODULES,
            )
        except Exception as exc:
            error_message(
                f"LEVEL/MODULE yuklanmadi: {exc}"
            )
            return 1

    level_count = len(
        LEVELS
    )

    module_count = sum(
        len(modules)
        for modules in MODULES.values()
    )

    if level_count == EXPECTED_LEVELS:
        pass_message(
            f"Level soni: {level_count}"
        )
    else:
        errors.append(
            f"Level soni o'zgargan: "
            f"{level_count} / "
            f"kutilgan {EXPECTED_LEVELS}"
        )

    if module_count == EXPECTED_MODULES:
        pass_message(
            f"Modul soni: {module_count}"
        )
    else:
        errors.append(
            f"Modul soni o'zgargan: "
            f"{module_count} / "
            f"kutilgan {EXPECTED_MODULES}"
        )

    # ========================================================
    # CONTENT REGISTRY
    # ========================================================

    try:
        from courses.content_registry import (
            get_all_lesson_content,
            get_all_quiz_data,
        )
    except Exception as exc:
        error_message(
            f"content_registry yuklanmadi: {exc}"
        )
        return 1

    lesson_content = (
        get_all_lesson_content()
    )

    quiz_data = (
        get_all_quiz_data()
    )

    lesson_count = len(
        lesson_content
    )

    quiz_group_count = len(
        quiz_data
    )

    quiz_question_count = 0

    for questions in quiz_data.values():
        if isinstance(
            questions,
            list,
        ):
            quiz_question_count += len(
                questions
            )

        elif isinstance(
            questions,
            dict,
        ):
            possible_questions = (
                questions.get(
                    "questions",
                    [],
                )
            )

            if isinstance(
                possible_questions,
                list,
            ):
                quiz_question_count += len(
                    possible_questions
                )

    if lesson_count == EXPECTED_LESSON_CONTENT:
        pass_message(
            f"Lesson content: {lesson_count}"
        )
    else:
        errors.append(
            f"Lesson content soni o'zgargan: "
            f"{lesson_count} / "
            f"kutilgan {EXPECTED_LESSON_CONTENT}"
        )

    if quiz_group_count == EXPECTED_QUIZ_GROUPS:
        pass_message(
            f"Quiz group: {quiz_group_count}"
        )
    else:
        errors.append(
            f"Quiz group soni o'zgargan: "
            f"{quiz_group_count} / "
            f"kutilgan {EXPECTED_QUIZ_GROUPS}"
        )

    if quiz_question_count == EXPECTED_QUIZ_QUESTIONS:
        pass_message(
            f"Quiz savollari: {quiz_question_count}"
        )
    else:
        errors.append(
            f"Quiz savollari soni o'zgargan: "
            f"{quiz_question_count} / "
            f"kutilgan {EXPECTED_QUIZ_QUESTIONS}"
        )

    # ========================================================
    # NATIJA
    # ========================================================

    print()
    print(
        "=" * 60
    )

    if errors:
        print(
            "CONTENT GUARD: FAILED"
        )

        print()

        for error in errors:
            error_message(
                error
            )

        print()
        print(
            "DIQQAT: kontent kamaygan yoki o'zgargan."
        )

        print(
            "RELEASE BUILD QILMANG."
        )

        return 1

    print(
        "CONTENT GUARD: PASSED"
    )

    print()

    print(
        "Barcha asosiy darslar va testlar saqlangan."
    )

    print(
        "Keyingi UI o'zgarishlarini davom ettirish mumkin."
    )

    return 0


if __name__ == "__main__":
    raise SystemExit(
        main()
    )
