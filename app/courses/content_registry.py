from courses.lesson_content import LESSON_CONTENT

from courses.level00_extra import (
    LEVEL00_EXTRA_CONTENT,
    LEVEL00_EXTRA_QUIZ,
)

from courses.level01_content import (
    LEVEL01_CONTENT,
    LEVEL01_QUIZ,
)

from courses.level01_module02 import (
    LEVEL01_MODULE02_CONTENT,
    LEVEL01_MODULE02_QUIZ,
)

from courses.level01_module03 import (
    LEVEL01_MODULE03_CONTENT,
    LEVEL01_MODULE03_QUIZ,
)

from courses.level01_module04 import (
    LEVEL01_MODULE04_CONTENT,
    LEVEL01_MODULE04_QUIZ,
)

from courses.level01_module05 import (
    LEVEL01_MODULE05_CONTENT,
    LEVEL01_MODULE05_QUIZ,
)

from courses.level01_module06 import (
    LEVEL01_MODULE06_CONTENT,
    LEVEL01_MODULE06_QUIZ,
)

from courses.level02_module01 import (
    LEVEL02_MODULE01_CONTENT,
    LEVEL02_MODULE01_QUIZ,
)

from courses.level02_module02 import (
    LEVEL02_MODULE02_CONTENT,
    LEVEL02_MODULE02_QUIZ,
)

from courses.level02_module03 import (
    LEVEL02_MODULE03_CONTENT,
    LEVEL02_MODULE03_QUIZ,
)

from courses.level02_module04 import (
    LEVEL02_MODULE04_CONTENT,
    LEVEL02_MODULE04_QUIZ,
)

from courses.level02_module05 import (
    LEVEL02_MODULE05_CONTENT,
    LEVEL02_MODULE05_QUIZ,
)

from courses.level02_module06 import (
    LEVEL02_MODULE06_CONTENT,
    LEVEL02_MODULE06_QUIZ,
)

from courses.level02_module07 import (
    LEVEL02_MODULE07_CONTENT,
    LEVEL02_MODULE07_QUIZ,
)

from courses.level02_module08 import (
    LEVEL02_MODULE08_CONTENT,
    LEVEL02_MODULE08_QUIZ,
)

from courses.level02_module09 import (
    LEVEL02_MODULE09_CONTENT,
    LEVEL02_MODULE09_QUIZ,
)

from courses.level02_module10 import (
    LEVEL02_MODULE10_CONTENT,
    LEVEL02_MODULE10_QUIZ,
)

from courses.level03_module01 import (
    LEVEL03_MODULE01_CONTENT,
    LEVEL03_MODULE01_QUIZ,
)

from courses.level03_module02 import (
    LEVEL03_MODULE02_CONTENT,
    LEVEL03_MODULE02_QUIZ,
)

from courses.level03_module03 import (
    LEVEL03_MODULE03_CONTENT,
    LEVEL03_MODULE03_QUIZ,
)

from courses.level03_module04 import (
    LEVEL03_MODULE04_CONTENT,
    LEVEL03_MODULE04_QUIZ,
)

from courses.level03_module05 import (
    LEVEL03_MODULE05_CONTENT,
    LEVEL03_MODULE05_QUIZ,
)

from courses.level03_module06 import (
    LEVEL03_MODULE06_CONTENT,
    LEVEL03_MODULE06_QUIZ,
)

from courses.level03_module07 import (
    LEVEL03_MODULE07_CONTENT,
    LEVEL03_MODULE07_QUIZ,
)

from courses.level03_module08 import (
    LEVEL03_MODULE08_CONTENT,
    LEVEL03_MODULE08_QUIZ,
)

from courses.level04_module01 import (
    LEVEL04_MODULE01_CONTENT,
    LEVEL04_MODULE01_QUIZ,
)

from courses.level04_module02 import (
    LEVEL04_MODULE02_CONTENT,
    LEVEL04_MODULE02_QUIZ,
)

from courses.level04_module03 import (
    LEVEL04_MODULE03_CONTENT,
    LEVEL04_MODULE03_QUIZ,
)

from courses.level04_module04 import (
    LEVEL04_MODULE04_CONTENT,
    LEVEL04_MODULE04_QUIZ,
)

from courses.level04_module05 import (
    LEVEL04_MODULE05_CONTENT,
    LEVEL04_MODULE05_QUIZ,
)

from courses.level04_module06 import (
    LEVEL04_MODULE06_CONTENT,
    LEVEL04_MODULE06_QUIZ,
)

from courses.quiz_data import QUIZ_DATA


def get_all_lesson_content():
    combined = {}

    combined.update(LESSON_CONTENT)
    combined.update(LEVEL00_EXTRA_CONTENT)

    combined.update(LEVEL01_CONTENT)
    combined.update(LEVEL01_MODULE02_CONTENT)
    combined.update(LEVEL01_MODULE03_CONTENT)
    combined.update(LEVEL01_MODULE04_CONTENT)
    combined.update(LEVEL01_MODULE05_CONTENT)
    combined.update(LEVEL01_MODULE06_CONTENT)

    combined.update(LEVEL02_MODULE01_CONTENT)
    combined.update(LEVEL02_MODULE02_CONTENT)
    combined.update(LEVEL02_MODULE03_CONTENT)
    combined.update(LEVEL02_MODULE04_CONTENT)
    combined.update(LEVEL02_MODULE05_CONTENT)
    combined.update(LEVEL02_MODULE06_CONTENT)
    combined.update(LEVEL02_MODULE07_CONTENT)
    combined.update(LEVEL02_MODULE08_CONTENT)
    combined.update(LEVEL02_MODULE09_CONTENT)
    combined.update(LEVEL02_MODULE10_CONTENT)

    combined.update(LEVEL03_MODULE01_CONTENT)
    combined.update(LEVEL03_MODULE02_CONTENT)
    combined.update(LEVEL03_MODULE03_CONTENT)
    combined.update(LEVEL03_MODULE04_CONTENT)
    combined.update(LEVEL03_MODULE05_CONTENT)
    combined.update(LEVEL03_MODULE06_CONTENT)
    combined.update(LEVEL03_MODULE07_CONTENT)
    combined.update(LEVEL03_MODULE08_CONTENT)

    combined.update(LEVEL04_MODULE01_CONTENT)
    combined.update(LEVEL04_MODULE02_CONTENT)
    combined.update(LEVEL04_MODULE03_CONTENT)
    combined.update(LEVEL04_MODULE04_CONTENT)
    combined.update(LEVEL04_MODULE05_CONTENT)
    combined.update(LEVEL04_MODULE06_CONTENT)

    return combined


def get_lesson_content_by_code(
    lesson_code: str,
):
    return get_all_lesson_content().get(
        lesson_code,
        [],
    )


def get_all_quiz_data():
    combined = {}

    combined.update(QUIZ_DATA)
    combined.update(LEVEL00_EXTRA_QUIZ)

    combined.update(LEVEL01_QUIZ)
    combined.update(LEVEL01_MODULE02_QUIZ)
    combined.update(LEVEL01_MODULE03_QUIZ)
    combined.update(LEVEL01_MODULE04_QUIZ)
    combined.update(LEVEL01_MODULE05_QUIZ)
    combined.update(LEVEL01_MODULE06_QUIZ)

    combined.update(LEVEL02_MODULE01_QUIZ)
    combined.update(LEVEL02_MODULE02_QUIZ)
    combined.update(LEVEL02_MODULE03_QUIZ)
    combined.update(LEVEL02_MODULE04_QUIZ)
    combined.update(LEVEL02_MODULE05_QUIZ)
    combined.update(LEVEL02_MODULE06_QUIZ)
    combined.update(LEVEL02_MODULE07_QUIZ)
    combined.update(LEVEL02_MODULE08_QUIZ)
    combined.update(LEVEL02_MODULE09_QUIZ)
    combined.update(LEVEL02_MODULE10_QUIZ)

    combined.update(LEVEL03_MODULE01_QUIZ)
    combined.update(LEVEL03_MODULE02_QUIZ)
    combined.update(LEVEL03_MODULE03_QUIZ)
    combined.update(LEVEL03_MODULE04_QUIZ)
    combined.update(LEVEL03_MODULE05_QUIZ)
    combined.update(LEVEL03_MODULE06_QUIZ)
    combined.update(LEVEL03_MODULE07_QUIZ)
    combined.update(LEVEL03_MODULE08_QUIZ)

    combined.update(LEVEL04_MODULE01_QUIZ)
    combined.update(LEVEL04_MODULE02_QUIZ)
    combined.update(LEVEL04_MODULE03_QUIZ)
    combined.update(LEVEL04_MODULE04_QUIZ)
    combined.update(LEVEL04_MODULE05_QUIZ)
    combined.update(LEVEL04_MODULE06_QUIZ)

    return combined
