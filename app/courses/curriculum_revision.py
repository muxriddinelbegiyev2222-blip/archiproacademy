"""Add practice material without mutating original lessons or changing their IDs.

Case quizzes are reading/application checks, not a professional design assessment.
The independent exercise rubric is the evidence of practical skill.
"""
from copy import deepcopy
from html import escape
import hashlib
from courses.workbook_data import WORKBOOKS, MODULE_MISSTEPS
from courses.teaching.guides import GUIDES, guide_for_lesson
from courses.teaching.lesson_examples import EXAMPLES
from courses.teaching.terms import TERMS
import re

REVISION = 'ARCHIPRO_TEACHING_SOLUTIONS_2026_10_04_V2'
MODULES = {unit['code']: (guide, unit) for guide in WORKBOOKS.values() for unit in guide['units']}
HELP = 'https://help.graphisoft.com/AC/28/INT/_AC28_Help/'
SCHEDULE_HELP = HELP + '050_ViewsVB/050_ViewsVB-97.htm'
PUBLISHER_HELP = HELP + '070_Documentation/070_Documentation-119.htm'
GENERAL_HELP = HELP + '140_UserInterfaceDialogBoxes/140_UserInterfaceDialogBoxes-1.htm'
NORM_SOURCE = 'https://gov.uz/oz/mc'

# Distractors describe invalid evidence or unsupported shortcuts, not alternate
# legitimate project solutions. Correct answers are in the lesson's case.
DISTRACTORS = {
    'intro': [
        'Faqat chiroyli tasvir yetarli; foydalanish ssenariysini tekshirmang.',
        'Natijani o‘lchamasdan ekran ko‘rinishi bilan to‘liq tasdiqlang.',
        'Bir chizmaga qarab boshqa ko‘rinishlar ham mos deb hisoblang.'],
    'model': [
        'Faqat plandagi ko‘rinish yetarli; sath va modelni tekshirmang.',
        'Parametrni taxmin qiling; element sozlamalari dalil bo‘lishi shart emas.',
        'Bitta yaxshi render barcha model ma’lumotlari to‘g‘riligini tasdiqlaydi.'],
    'engineering': [
        'Eskizdagi kesimni hisob va mutaxassis tasdig‘isiz qurilishga tayyor deb qabul qiling.',
        'Faqat tashqi ko‘rinish bilan texnik moslikni tasdiqlang.',
        'Konfliktni boshqa mutaxassisga bildirmasdan yashiring.'],
    'norms': [
        'Manba va bandni aniqlamasdan boshqa loyihadagi raqamni qo‘llang.',
        'Faqat internetdagi skrinshot bilan amaldagi talabni tasdiqlang.',
        'Chizma chiroyli bo‘lsa, hujjat doirasi va tahririni tekshirmang.'],
    'documentation': [
        'Export tugagani yetarli; chiqarilgan faylni ochib tekshirmang.',
        'Jadval satrlari bilan model manbasini solishtirmang.',
        'Oldingi revisionni yangi paket bilan bir xil deb qabul qiling.'],
    'client': [
        'Taxminni mijoz tasdiqlagan talab sifatida qayd eting.',
        'Mijozga foyda haqida ayting, lekin qarorning yo‘qotishini yashiring.',
        'O‘zgarishning scope va boshqa hujjatlarga ta’sirini tekshirmang.'],
    'final': [
        'Faqat test bali amaliy ko‘nikma va loyiha vakolatini to‘liq isbotlaydi.',
        'Tasdiqlanmagan taxminni professional hisob natijasi deb taqdim eting.',
        'Paketni qayta tekshirmasdan barcha fayllar mos deb qabul qiling.'],
}

def category(code):
    level=int(code[1:3])
    if level in (5,6,7): return 'model'
    if level in (8,11): return 'engineering'
    if level==9: return 'norms'
    if level==12: return 'documentation'
    if level==13: return 'client'
    if level==15: return 'final'
    return 'intro'


def source_block(code):
    level=int(code[1:3]); module=code[:7]
    if level in (5,6,7,12) or module=='L10_M06' or module=='L11_M08' or module=='L15_M02':
        url = SCHEDULE_HELP if module in ('L07_M05','L12_M03') else PUBLISHER_HELP if module in ('L12_M07','L12_M08','L12_M09','L12_M10') else GENERAL_HELP
        return ('Archicad 28 INT qo‘llanmasi', '<p>Asbob va menyu nomlari Archicad 28 INT bo‘yicha berilgan. Boshqa versiya yoki til uchun joylashuv farq qilishi mumkin. '
                f'<a href="{url}">Graphisoft rasmiy yordam sahifasi</a>. Havola uchun internet kerak; dars matni oflayn ishlaydi.</p>')
    if level in (8,9) or module in ('L11_M03','L11_M04','L11_M06','L14_M03'):
        return ('Manba va tekshiruv doirasi', f'<p>Bu mashq tushuncha va koordinatsiyani o‘rgatadi. Berilgan sonlar o‘quv shartlari, normativ minimum yoki hisoblangan konstruksiya emas. '
                f'<a href="{NORM_SOURCE}">Qurilish vazirligi rasmiy portali</a> orqali tegishli hujjatni izlang; asl hujjatning qo‘llanish doirasi, amaldagi tahriri va bandini tekshiring. '
                'Aniq loyiha uchun tegishli mutaxassis tasdig‘ini qayd eting. Havola uchun internet kerak.</p>')
    return ('O‘quv misolining chegarasi', '<p>Misol va sonlar mashq uchun berilgan. Ularni boshqa site, oila yoki loyiha talabiga tekshirmasdan ko‘chirmang. '
            'O‘z qaroringizni boshlang‘ich ma’lumot, foydalanish va tekshiruv dalili bilan asoslang.</p>')


def enhance_content(code, original):
    """Keep source lessons intact and append worked, module-specific teaching."""
    if not original:
        return []
    workbook, unit = MODULES[code]
    guide, index, units = guide_for_lesson(code)
    stage = guide['stages'][index]
    def paragraph(text):
        return '<p>' + escape(text) + '</p>'
    def items(values):
        return '<ol>' + ''.join('<li>' + escape(value) + '</li>' for value in values) + '</ol>'
    rows = ''.join('<tr><td>' + escape(topic['title']) + '</td><td>' +
                   escape(method.rsplit('→', 1)[-1].strip()) + '</td></tr>'
                   for topic, method in zip(units, guide['stages']))
    table = ('<table border="1" cellspacing="0" cellpadding="7" width="100%">'
             '<tr><th>Mavzu</th><th>Namuna oxirida tekshiriladigan natija</th></tr>' + rows + '</table>')
    case = (paragraph(guide['case']) + '<p><b>Namunaning yechimi:</b></p>' +
            paragraph(guide['answer']) + table +
            '<p>Bu bir modul bo‘ylab davom etadigan o‘quv misoli. Jadvaldagi bosqichlar bir ishning '
            'turli tomonlarini ko‘rsatadi. Hozirgi mavzu: <b>' + escape(unit['title']) + '</b>.</p>')
    instructions = stage.strip()
    steps = [value.strip() for value in re.split(r'(?<=[.!?])\s+', instructions) if value.strip()]
    term_context = unit['title'] + ' ' + instructions
    glossary = ''.join('<li><b>' + escape(term) + '</b> — ' + escape(meaning) + '</li>'
                       for term, meaning in TERMS.items()
                       if re.search(r'(?<!\w)' + re.escape(term) + r'(?!\w)', term_context, re.I))
    term_help = '<p><b>Atamalarni sodda tushunamiz:</b></p><ul>' + glossary + '</ul>' if glossary else ''
    method = (term_help + '<p><b>Ushbu mavzuni bajarish:</b></p>' + items(steps) +
              '<p><b>Bu namunaning xulosasi:</b> ' + escape(guide['answer']) + '</p>' +
              '<p><b>Modul misolining to‘liq ketma-ketligi:</b></p>' + items(guide['stages']) +
              EXAMPLES.get(code, ''))
    exercise = ('<p><b>Ko‘p uchraydigan xato va tuzatish:</b></p>' + paragraph(guide['error']) +
                '<p>Xatoni yashirish uchun faqat yozuv yoki rasmni tuzatmang. Yuqoridagi bajarish '
                'ketma-ketligida ma’lumot manbasiga qayting va natijani qayta tekshiring.</p>' +
                '<p><b>Mustaqil mashqning boshlang‘ich sharti:</b></p>' + paragraph(workbook['case']) +
                '<p><b>Vazifa:</b> ' + escape(unit['action']) + '</p>' +
                '<p><b>Yechimni solishtirish:</b> ' + escape(unit['result']) + '</p>' +
                '<p><b>Yuqoridagi ishlangan namunaga boshqa shart va yechim yo‘li:</b></p>' +
                paragraph(guide['variation']) +
                '<p>Mustaqil mashq bilan ishlangan namunaning boshlang‘ich shartlarini aralashtirmang. '
                'Natijangizni aynan o‘zingiz bajargan shart bo‘yicha tekshiring.</p>' +
                '<p><b>Saqlanadigan dalil:</b> boshlang‘ich shart, bajarilgan chizma/jadval yoki hisob, '
                'tekshirilgan natija va xato bo‘lsa uning tuzatilgan holati. Namuna matnini ko‘chirish '
                'ish bajarilganini isbotlamaydi. Test amaliy faylni avtomatik baholamaydi.</p>')
    name, source = source_block(code)
    source += ('<p><b>O‘quv misoli haqida:</b> sonlar mashq shartidir. Geometrik hisobning to‘g‘riligi '
               'foydalanish, konstruktiv, muhandislik yoki normativ moslikni avtomatik tasdiqlamaydi. '
               'Tegishli loyiha talabini va zarur mutaxassis tekshiruvini alohida aniqlang.</p>')
    added = [
        {'title': 'O‘quv holati va dars vazifasi', 'type': 'example', 'text': case},
        {'title': 'Bajarish tartibi va namunaviy xulosa', 'type': 'normal', 'text': method},
        {'title': 'Mustaqil mashq va o‘zini tekshirish', 'type': 'highlight', 'text': exercise},
        {'title': name, 'type': 'normal', 'text': source},
    ]
    for block in added:
        block['teaching_revision'] = REVISION
        block['teaching_lesson'] = code
    return deepcopy(original) + added


def options(code,index,correct,wrong):
    position=int(hashlib.sha256(f'{code}:{index}'.encode()).hexdigest()[:8],16)%4
    choices=list(wrong);choices.insert(position,correct)
    return [(letter,text,i==position) for i,(letter,text) in enumerate(zip('ABCD',choices))]


def enhance_quiz(code, original):
    if not original: return []
    # Retain the existing richer four-option checks in the introductory lessons.
    if all(len(q['options'])==4 for q in original): return deepcopy(original)
    guide,unit=MODULES[code]
    wrong=[MODULE_MISSTEPS[code[:7]], *DISTRACTORS[category(code)][1:]]
    prompts=[
        (f"{unit['title']}. Holat: {guide['case']} Darsdagi vazifaga mos tekshirish amali qaysi?",unit['action']),
        (f"{unit['title']}. Topshiriq: {unit['action']} Qaysi xulosa darsdagi tushunchaga mos?",unit['result']),
        (f"{unit['title']}. {unit['action']} Ish yakunini qanday dalil bilan asoslash kerak?",
         f"Bajarilgan ishni holat shartlari bilan solishtirib, xulosani dalillash: {unit['result']}"),
    ]
    result=[]
    for i,q in enumerate(original):
        prompt,answer=prompts[i%3]
        if i>=3: prompt=f"{prompt} Qo‘shimcha tekshiruv {i+1}."
        result.append({'code':q['code'],'question':prompt,
                       'explanation':f"O‘quv holati bo‘yicha vazifa: {unit['action']} Asos: {unit['result']} Noma’lum shartni tasdiqlangan fakt deb ko‘rsatmaslik kerak.",
                       'options':options(code,i,answer,wrong)})
    return result


def validate_revision(content, quizzes):
    """Structural release gate; this cannot certify architectural correctness."""
    if len(WORKBOOKS)!=137 or len(MODULES)!=680 or set(content)!=set(MODULES) or set(quizzes)!=set(content):
        raise ValueError('Workbook coverage must match all 137 modules / 680 lessons')
    if len(GUIDES) != 137 or sum(len(g['stages']) for g in GUIDES.values()) != 680:
        raise ValueError('Worked teaching coverage is incomplete')
    signatures=set(); question_ids=set()
    for code,blocks in content.items():
        if get_revision_block_count(blocks)!=4:
            raise ValueError('Missing practice/source blocks: '+code)
        if any(b.get('teaching_revision') != REVISION or b.get('teaching_lesson') != code for b in blocks[-4:]):
            raise ValueError('Wrong teaching revision or lesson identity: ' + code)
        if 'Namunaning yechimi' not in blocks[-4]['text'] or 'Ushbu mavzuni bajarish' not in blocks[-3]['text']:
            raise ValueError('Missing worked teaching: ' + code)
        signature=tuple(q['question'] for q in quizzes[code])
        if signature in signatures: raise ValueError('Repeated complete quiz: '+code)
        signatures.add(signature)
        for q in quizzes[code]:
            if q['code'] in question_ids: raise ValueError('Repeated question ID: '+q['code'])
            question_ids.add(q['code'])
            opts=q['options']
            if len(opts)!=4 or len({o[1] for o in opts})!=4 or sum(bool(o[2]) for o in opts)!=1:
                raise ValueError('Invalid four-choice question: '+q['code'])
    if len(question_ids)!=2041: raise ValueError('Question identity/count changed')
    return {'revision':REVISION,'workbook_modules':137,'workbook_lessons':680,'questions':2041,'worked_modules':137,'worked_lesson_stages':680}


def get_revision_block_count(blocks):
    names={'O‘quv holati va dars vazifasi','Bajarish tartibi va namunaviy xulosa',
           'Mustaqil mashq va o‘zini tekshirish'}
    return sum(b['title'] in names or b['title'] in
               {'Archicad 28 INT qo‘llanmasi','Manba va tekshiruv doirasi','O‘quv misolining chegarasi'} for b in blocks)
