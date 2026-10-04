"""Strict, fail-closed coverage for all teaching modules and their lesson stages."""
from courses.workbook_data import WORKBOOKS
from courses.teaching import foundations, modeling, project_work, professional_work


GUIDES = {}
for source in (foundations, modeling, project_work, professional_work):
    for line in source.DATA.splitlines():
        if not line.strip():
            continue
        code, case, methods, answer, error, variation = line.split('|')
        if code in GUIDES:
            raise ValueError('Duplicate teaching module: ' + code)
        stages = methods.split(';')
        if len(stages) != len(WORKBOOKS[code]['units']):
            raise ValueError('Teaching stages do not match lessons: ' + code)
        if any(not value.strip() for value in (case, answer, error, variation, *stages)):
            raise ValueError('Empty teaching material: ' + code)
        GUIDES[code] = dict(case=case, stages=stages, answer=answer,
                            error=error, variation=variation)

if set(GUIDES) != set(WORKBOOKS):
    raise ValueError('Worked examples must cover exactly all 137 modules')

all_stages = [stage for guide in GUIDES.values() for stage in guide['stages']]
if len(all_stages) != 680 or len(set(all_stages)) != 680:
    raise ValueError('Every lesson must have its own teaching stage')
if len({guide['case'] for guide in GUIDES.values()}) != 137:
    raise ValueError('Each module must have its own worked case')


def guide_for_lesson(code):
    module = code[:7]
    units = WORKBOOKS[module]['units']
    index = next(i for i, unit in enumerate(units) if unit['code'] == code)
    return GUIDES[module], index, units
