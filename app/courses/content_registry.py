import importlib
import re


# ============================================================
# ARCHIPRO UZ
# LAZY CONTENT REGISTRY V2
#
# Maqsad:
#
# Oldingi tizim:
#   content_registry import bo'lishi bilan
#   barcha Level content modullari yuklanardi.
#
# Yangi tizim:
#   faqat kerakli dars tegishli modul yuklanadi.
#
# Masalan:
#
#   L05_M03_002
#
#   faqat:
#
#   courses.level05_module03
#
#   yuklanadi.
#
# FULL AUDIT uchun get_all_* funksiyalari saqlanadi.
# ============================================================


LESSON_CODE_PATTERN = re.compile(
    r"^L(?P<level>\d{2})_M(?P<module>\d{2})_\d+$"
)


# ============================================================
# CURRICULUM MODULE COUNTS
#
# 16 LEVEL
# 137 MODULE
# ============================================================


LEVEL_MODULE_COUNTS = {
    0: 5,
    1: 6,
    2: 10,
    3: 8,
    4: 8,
    5: 10,
    6: 10,
    7: 9,
    8: 9,
    9: 8,
    10: 11,
    11: 9,
    12: 10,
    13: 8,
    14: 8,
    15: 8,
}


# ============================================================
# SMALL MODULE CACHE
#
# Bir modul birinchi marta ochilgandan keyin
# qayta import qilinmaydi.
#
# Masalan:
# LEVEL 05 / MODULE 03 ichidagi 5 ta dars uchun
# modul faqat bir marta yuklanadi.
# ============================================================


_module_cache = {}

_content_cache = {}

_quiz_cache = {}


# ============================================================
# LESSON CODE PARSER
# ============================================================


def parse_lesson_code(
    lesson_code: str,
):
    if not lesson_code:
        return None

    match = LESSON_CODE_PATTERN.match(
        str(
            lesson_code
        ).strip()
    )

    if match is None:
        return None

    return (
        int(
            match.group(
                "level"
            )
        ),
        int(
            match.group(
                "module"
            )
        ),
    )


# ============================================================
# MODULE DESCRIPTOR
# ============================================================


def get_module_descriptor(
    level_number: int,
    module_number: int,
):
    """
    Berilgan Level / Module uchun:
    - Python module
    - content constant
    - quiz constant

    nomlarini qaytaradi.
    """

    # ========================================================
    # LEVEL 00 / MODULE 01
    # ========================================================

    if (
        level_number == 0
        and module_number == 1
    ):
        return {
            "content_module": (
                "courses.lesson_content"
            ),
            "content_name": (
                "LESSON_CONTENT"
            ),
            "quiz_module": (
                "courses.quiz_data"
            ),
            "quiz_name": (
                "QUIZ_DATA"
            ),
        }

    # ========================================================
    # LEVEL 00 / MODULE 02-05
    #
    # Hammasi level00_extra.py ichida.
    # ========================================================

    if (
        level_number == 0
        and 2 <= module_number <= 5
    ):
        return {
            "content_module": (
                "courses.level00_extra"
            ),
            "content_name": (
                "LEVEL00_EXTRA_CONTENT"
            ),
            "quiz_module": (
                "courses.level00_extra"
            ),
            "quiz_name": (
                "LEVEL00_EXTRA_QUIZ"
            ),
        }

    # ========================================================
    # LEVEL 01 / MODULE 01
    # ========================================================

    if (
        level_number == 1
        and module_number == 1
    ):
        return {
            "content_module": (
                "courses.level01_content"
            ),
            "content_name": (
                "LEVEL01_CONTENT"
            ),
            "quiz_module": (
                "courses.level01_content"
            ),
            "quiz_name": (
                "LEVEL01_QUIZ"
            ),
        }

    # ========================================================
    # LEVEL 01 / MODULE 02-06
    # ========================================================

    if (
        level_number == 1
        and 2 <= module_number <= 6
    ):
        level_text = "01"

        module_text = (
            f"{module_number:02d}"
        )

        module_path = (
            "courses."
            f"level{level_text}_"
            f"module{module_text}"
        )

        return {
            "content_module": (
                module_path
            ),
            "content_name": (
                f"LEVEL{level_text}_"
                f"MODULE{module_text}_CONTENT"
            ),
            "quiz_module": (
                module_path
            ),
            "quiz_name": (
                f"LEVEL{level_text}_"
                f"MODULE{module_text}_QUIZ"
            ),
        }

    # ========================================================
    # LEVEL 02 - LEVEL 15
    # ========================================================

    if 2 <= level_number <= 15:

        max_modules = (
            LEVEL_MODULE_COUNTS.get(
                level_number,
                0,
            )
        )

        if not (
            1
            <= module_number
            <= max_modules
        ):
            return None

        level_text = (
            f"{level_number:02d}"
        )

        module_text = (
            f"{module_number:02d}"
        )

        module_path = (
            "courses."
            f"level{level_text}_"
            f"module{module_text}"
        )

        return {
            "content_module": (
                module_path
            ),
            "content_name": (
                f"LEVEL{level_text}_"
                f"MODULE{module_text}_CONTENT"
            ),
            "quiz_module": (
                module_path
            ),
            "quiz_name": (
                f"LEVEL{level_text}_"
                f"MODULE{module_text}_QUIZ"
            ),
        }

    return None


# ============================================================
# SAFE IMPORT
# ============================================================


def load_module(
    module_name: str,
):
    cached = _module_cache.get(
        module_name
    )

    if cached is not None:
        return cached

    module = importlib.import_module(
        module_name
    )

    _module_cache[
        module_name
    ] = module

    return module


# ============================================================
# DICTIONARY LOADER
# ============================================================


def load_dictionary(
    module_name: str,
    constant_name: str,
):
    module = load_module(
        module_name
    )

    value = getattr(
        module,
        constant_name,
        None,
    )

    if value is None:
        raise AttributeError(
            f"{module_name} ichida "
            f"{constant_name} topilmadi."
        )

    if not isinstance(
        value,
        dict,
    ):
        raise TypeError(
            f"{module_name}."
            f"{constant_name} dict emas."
        )

    return value


# ============================================================
# LAZY LESSON CONTENT
# ============================================================


def get_lesson_content_by_code(
    lesson_code: str,
):
    """
    Faqat bitta darsga kerakli modulni yuklaydi.

    680 ta content dictionary'ni birdan yaratmaydi.
    """

    lesson_code = str(
        lesson_code
    ).strip()

    cached = _content_cache.get(
        lesson_code
    )

    if cached is not None:
        return cached

    parsed = parse_lesson_code(
        lesson_code
    )

    if parsed is None:
        return []

    (
        level_number,
        module_number,
    ) = parsed

    descriptor = (
        get_module_descriptor(
            level_number,
            module_number,
        )
    )

    if descriptor is None:
        return []

    content_dictionary = (
        load_dictionary(
            descriptor[
                "content_module"
            ],
            descriptor[
                "content_name"
            ],
        )
    )

    content = (
        content_dictionary.get(
            lesson_code,
            [],
        )
    )

    _content_cache[
        lesson_code
    ] = content

    return content


# ============================================================
# LAZY QUIZ DATA
# ============================================================


def get_quiz_data_by_code(
    lesson_code: str,
):
    """
    Bitta lesson uchun quiz ma'lumotini yuklaydi.
    """

    lesson_code = str(
        lesson_code
    ).strip()

    cached = _quiz_cache.get(
        lesson_code
    )

    if cached is not None:
        return cached

    parsed = parse_lesson_code(
        lesson_code
    )

    if parsed is None:
        return []

    (
        level_number,
        module_number,
    ) = parsed

    descriptor = (
        get_module_descriptor(
            level_number,
            module_number,
        )
    )

    if descriptor is None:
        return []

    quiz_dictionary = (
        load_dictionary(
            descriptor[
                "quiz_module"
            ],
            descriptor[
                "quiz_name"
            ],
        )
    )

    quiz = quiz_dictionary.get(
        lesson_code,
        [],
    )

    _quiz_cache[
        lesson_code
    ] = quiz

    return quiz


# ============================================================
# ALL DESCRIPTORS
#
# AUDIT va seeding uchun.
# Oddiy dars ochilishida ishlatilmaydi.
# ============================================================


def iter_all_descriptors():
    # LEVEL 00
    for module_number in range(
        1,
        LEVEL_MODULE_COUNTS[0] + 1,
    ):
        descriptor = (
            get_module_descriptor(
                0,
                module_number,
            )
        )

        if descriptor is not None:
            yield descriptor

    # LEVEL 01
    for module_number in range(
        1,
        LEVEL_MODULE_COUNTS[1] + 1,
    ):
        descriptor = (
            get_module_descriptor(
                1,
                module_number,
            )
        )

        if descriptor is not None:
            yield descriptor

    # LEVEL 02 - LEVEL 15
    for level_number in range(
        2,
        16,
    ):
        for module_number in range(
            1,
            (
                LEVEL_MODULE_COUNTS[
                    level_number
                ]
                + 1
            ),
        ):
            descriptor = (
                get_module_descriptor(
                    level_number,
                    module_number,
                )
            )

            if descriptor is not None:
                yield descriptor


# ============================================================
# UNIQUE SOURCES
# ============================================================


def get_unique_content_sources():
    result = []

    seen = set()

    for descriptor in (
        iter_all_descriptors()
    ):
        source = (
            descriptor[
                "content_module"
            ],
            descriptor[
                "content_name"
            ],
        )

        if source in seen:
            continue

        seen.add(
            source
        )

        result.append(
            source
        )

    return result


def get_unique_quiz_sources():
    result = []

    seen = set()

    for descriptor in (
        iter_all_descriptors()
    ):
        source = (
            descriptor[
                "quiz_module"
            ],
            descriptor[
                "quiz_name"
            ],
        )

        if source in seen:
            continue

        seen.add(
            source
        )

        result.append(
            source
        )

    return result


# ============================================================
# FULL LESSON CONTENT
#
# CONTENT_GUARD / AUDIT uchun.
# ============================================================


def get_all_lesson_content():
    """
    Barcha 680 lesson contentni birlashtiradi.

    Bu funksiya audit va maintenance uchun.

    Oddiy lesson sahifasi bundan foydalanmasligi kerak.
    """

    combined = {}

    for (
        module_name,
        constant_name,
    ) in get_unique_content_sources():

        dictionary = (
            load_dictionary(
                module_name,
                constant_name,
            )
        )

        combined.update(
            dictionary
        )

    return combined


# ============================================================
# FULL QUIZ DATA
#
# CONTENT_GUARD / AUDIT / SEEDING uchun.
# ============================================================


def get_all_quiz_data():
    """
    Barcha quiz lesson group va savollarni birlashtiradi.

    Oddiy lesson render paytida chaqirilmaydi.
    """

    combined = {}

    for (
        module_name,
        constant_name,
    ) in get_unique_quiz_sources():

        dictionary = (
            load_dictionary(
                module_name,
                constant_name,
            )
        )

        combined.update(
            dictionary
        )

    return combined


# ============================================================
# CACHE MANAGEMENT
# ============================================================


def clear_registry_cache():
    """
    Faqat Python runtime cache.

    Database va foydalanuvchi progressiga tegmaydi.
    """

    _content_cache.clear()

    _quiz_cache.clear()

    _module_cache.clear()


def get_registry_cache_info():
    """
    Debug / performance monitoring uchun.
    """

    return {
        "loaded_modules": len(
            _module_cache
        ),
        "cached_lessons": len(
            _content_cache
        ),
        "cached_quizzes": len(
            _quiz_cache
        ),
    }
