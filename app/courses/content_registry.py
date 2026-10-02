from courses.lesson_content import (
    LESSON_CONTENT,
)

from courses.level00_extra import (
    LEVEL00_EXTRA_CONTENT,
    LEVEL00_EXTRA_QUIZ,
)

from courses.level01_content import (
    LEVEL01_CONTENT,
    LEVEL01_QUIZ,
)

from courses.quiz_data import (
    QUIZ_DATA,
)


# ============================================================
# LESSON CONTENT REGISTRY
# ============================================================

def get_all_lesson_content():
    """
    Barcha Level va modullardagi dars kontentlarini
    bitta katta lug'atga birlashtiradi.

    Keyinchalik yangi Level yoki modul qo'shilsa,
    faqat shu registry'ga ulash kifoya bo'ladi.
    """

    combined = {}

    combined.update(
        LESSON_CONTENT
    )

    combined.update(
        LEVEL00_EXTRA_CONTENT
    )

    combined.update(
        LEVEL01_CONTENT
    )

    return combined


def get_lesson_content_by_code(
    lesson_code: str,
):
    """
    Dars kodi bo'yicha uning to'liq kontentini qaytaradi.
    """

    all_content = (
        get_all_lesson_content()
    )

    return all_content.get(
        lesson_code,
        [],
    )


# ============================================================
# QUIZ REGISTRY
# ============================================================

def get_all_quiz_data():
    """
    Barcha mini-test savollarini
    bitta tizimga birlashtiradi.
    """

    combined = {}

    combined.update(
        QUIZ_DATA
    )

    combined.update(
        LEVEL00_EXTRA_QUIZ
    )

    combined.update(
        LEVEL01_QUIZ
    )

    return combined
