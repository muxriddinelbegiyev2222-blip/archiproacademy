"""Verify the curriculum embedded in the running application, without user data."""
import json
from pathlib import Path
import sys
import traceback


def write_validation_report(output_path):
    from version import APP_VERSION
    report = {"version": APP_VERSION, "frozen": bool(getattr(sys, "frozen", False)),
              "success": False}
    try:
        from courses.content_registry import get_all_lesson_content, get_all_quiz_data
        content = get_all_lesson_content()
        quizzes = get_all_quiz_data()
        if len(content) != 680 or set(content) != set(quizzes):
            raise ValueError("Expected matching content and quizzes for all 680 lessons")
        for code, blocks in content.items():
            if not blocks or any(not isinstance(block, dict) or
                                 not str(block.get("text", "")).strip() for block in blocks):
                raise ValueError("Empty or invalid lesson: " + code)
            if not quizzes[code]:
                raise ValueError("Empty quiz: " + code)
        first = content["L00_M01_001"]
        if len(first) != 11 or "qulay, xavfsiz" not in first[1]["text"]:
            raise ValueError("The first lesson is missing its complete teaching content")
        from courses.curriculum_revision import validate_revision
        report.update(validate_revision(content, quizzes))
        report.update(success=True, lessons=len(content), quizzes=len(quizzes),
                      first_lesson_blocks=len(first))
    except Exception:
        report["error"] = traceback.format_exc()
    Path(output_path).write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    return 0 if report["success"] else 1
