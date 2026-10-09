"""Explicitly reviewed lesson-to-figure mappings; no keyword-based guessing.

Every lesson has an explicit mapping. Original content is never modified.
The packaged JSON holds topic diagrams and documented interface examples.
"""
from pathlib import Path
import json
import logging

ASSETS = Path(__file__).resolve().parent / 'visual_assets'
EDUCATIONAL = ('O‘quv misoli: chizmadan qurilish o‘lchami, element kesimi yoki '
               'majburiy normativ talabni ko‘chirib olmang. Aniq loyiha shartlari alohida tekshiriladi.')
CATALOG = {}


def add(code, asset, title, explanation, exercise, solution, block=0,
        boundary=EDUCATIONAL, credit='ARCHIPRO UZ — mavzu uchun tayyorlangan o‘quv chizmasi',
        source_url=None):
    spec = dict(asset=asset, title=title, explanation=tuple(explanation),
                exercise=exercise, solution=solution, boundary=boundary,
                credit=credit, source_url=source_url, block=block)
    CATALOG.setdefault(code, []).append(spec)


add('L00_M01_001', 'architecture.svg', 'Ehtiyojdan makonga',
    ['Oila qanday yashashini aniqlash xonalar ro‘yxatidan oldin keladi.',
     'Chizmada ehtiyoj → makon → tekshiruv zanjiri ko‘rsatilgan.'],
    'Mehmon kelishi va bolaning dars tayyorlashini ikkita ehtiyoj sifatida yozing.',
    'Mehmon qabul qilish joyi va tinch o‘qish joyi alohida vazifalardir; oqimlarni solishtiring.')
add('L00_M01_002', 'architect.svg', 'Istakni aniq topshiriqqa aylantirish',
    ['“Katta xona” aniq topshiriq emas. Kim foydalanishi va nima qilishi aniqlanadi.',
     'Savollar natijasi xonalar va vazifalar ro‘yxatiga aylanadi.'],
    '“Katta mehmonxona” istagiga ikkita aniqlashtiruvchi savol tuzing.',
    'Bir vaqtda nechta mehmon keladi? Ovqatlanish ham shu xonada bo‘ladimi?')
add('L00_M01_003', 'project.svg', 'Bir bino — bir-biriga mos hujjatlar',
    ['Plan joylashuvni; fasad tashqi ko‘rinishni; kesim ichki sathlarni tushuntiradi.',
     'Eshik yoki deraza o‘zgarsa, tegishli ko‘rinishlar ham tekshiriladi.'],
    'Planda deraza ko‘chirilsa, qaysi hujjat tekshiriladi?',
    'Tegishli fasad, kesim va derazaga oid hujjatlar bilan muvofiqlik tekshiriladi.')
add('L00_M02_001', 'plan.svg', 'Planda harakat yo‘lini kuzating',
    ['O‘quv binosining ikki xonasi markazdagi yo‘lakka ulangan.',
     'Kirish va derazalar fasaddagi namunada ham shu joylarda ko‘rsatiladi.'],
    'Kirishdan B xonaga borish yo‘lini toping.',
    'Kirish → yo‘lak → B xona. A xonadan o‘tish kerak emas.')
add('L00_M02_002', 'facade.svg', 'Plan bilan bog‘langan old fasad',
    ['Kirish markazda, ikkita deraza uning chap va o‘ng tomonida.',
     'Fasad xona ichki joylashuvini emas, tashqi vertikal ko‘rinishni beradi.'],
    'Chap derazani plan bilan solishtiring.',
    'Chapdagi A xona old devoridagi deraza fasadning chap tomoniga mos keladi.')
add('L00_M02_003', 'section.svg', 'Pol, shift va tomni ajrating',
    ['Kesim bino ichki vertikal tuzilishini tushuntiradi.',
     'Pol sathi, shift va tom bir xil element emas.'],
    'Planda ko‘rinmaydigan ikkita ma’lumotni ayting.',
    'Ichki balandlik va tomning vertikal tuzilishi kesimda tekshiriladi.')
add('L00_M02_004', 'site.svg', 'Uy uchastkada qanday joylashgan?',
    ['Ko‘cha, uchastka chegarasi, uy, hovli va kirish ajratilgan.',
     'Bu genplan xona plani emas; masofalar ushbu sxemada me’yorlanmagan.'],
    'Ko‘chadan uyga kirish yo‘lini toping.',
    'Ko‘cha → uchastka kirishi → hovli → uy. Haqiqiy loyihada chegara va talablar alohida tekshiriladi.')
add('L00_M03_001', 'scale.svg', '1:100 masshtabdagi aniq hisob',
    ['Haqiqiy 4 000 mm uzunlik 1:100 masshtabda 40 mm bo‘ladi.',
     'Ekranda rasm kattalashsa, modeldagi haqiqiy uzunlik o‘zgarmaydi.'],
    '3 000 mm uzunlik 1:100 da nechaga teng?', '3 000 ÷ 100 = 30 mm.')
add('L00_M03_002', 'dimension.svg', 'Millimetrni metrga aylantiring',
    ['O‘lcham yozuvi 4 000 mm; bu 4 m ga teng.',
     'Chizmadan ko‘z bilan taxmin qilish o‘rniga birlik bilan yozilgan qiymatni o‘qing.'],
    '2 500 mm ni metrda yozing.', '2 500 ÷ 1 000 = 2,5 m.')
add('L00_M03_003', 'levels.svg', 'Tayanch sathga nisbatan balandlik',
    ['±0.000 — qabul qilingan tayanch sath.',
     '+0.450 shu sathdan 450 mm yuqorida; bu bino umumiy balandligi emas.'],
    '−0.150 va +0.450 orasidagi farqni hisoblang.', '0,450 − (−0,150) = 0,600 m = 600 mm.')
add('L00_M04_001', 'foundation.svg', 'Fundament yukni gruntga uzatadi',
    ['Strelkalar yuqoridagi elementdan fundament va gruntgacha yo‘lni ko‘rsatadi.',
     'Fundament turi va o‘lchami sxema ko‘rinishidan tanlanmaydi.'],
    'Yuk yo‘lining oxirgi bosqichini ayting.', 'Fundament orqali gruntga uzatiladi; grunt sharoiti va konstruktiv hisob kerak.')
add('L00_M04_002', 'walls.svg', 'Devor vazifasini aniqlash',
    ['Yuk ko‘taruvchi va bo‘luvchi devorlar vazifasi farq qiladi.',
     'Qalinlikning o‘zi konstruktiv vazifani isbotlamaydi.'],
    'Bo‘luvchi devorni olib tashlashni rasmga qarab tasdiqlash mumkinmi?',
    'Yo‘q. Loyiha, konstruktiv vazifa va boshqa bog‘langan tizimlar tekshiriladi.')
add('L00_M04_003', 'frame.svg', 'Rigel va ustun aloqasi',
    ['Gorizontal rigel yukni vertikal ustunlarga uzatadi.',
     'Chizma prinsipni tushuntiradi, birikma yoki element kesimini belgilamaydi.'],
    'Rigelning ikkita tayanchini toping.', 'Chap va o‘ng ustun; ulardan pastki konstruksiyalarga yuk o‘tadi.')
add('L00_M04_004', 'slab.svg', 'Pol, plita va shift bir xil emas',
    ['Yuqori qavatdagi pol, konstruktiv yopma va pastki xonaning shiftini ajrating.',
     'Pardoz qatlami bilan yuk ko‘taruvchi qatlam vazifasi farq qiladi.'],
    'Shift pardozini konstruktiv plita deb qabul qilish to‘g‘rimi?', 'Yo‘q. Konstruktiv element va pardoz loyiha qatlamlari orqali aniqlanadi.')
add('L00_M04_005', 'roof-concept.jpg', 'Tom, devor va pastki tayanchlar',
    ['Tom qoplamasi va uning ostidagi tayanch tizimi ajratib ko‘rsatilgan.',
     'Yukning uzatilishini roof-load sxemasidagi strelkalar bilan solishtiring.'],
    'Tom qoplamasi bilan konstruktiv tayanchni ajrating.', 'Qoplama ustki himoya; ostidagi konstruktiv tizim yuk uzatishda qatnashadi.',
    credit='ARCHIPRO UZ — AI yordamida yaratilgan konseptual tasvir; konstruktiv detal emas')
add('L00_M04_006', 'openings.svg', 'Eshik va derazani planda o‘qish',
    ['Eshik yoyi ochilish yo‘lini, to‘g‘ri chiziq ochilgan tabaqani ko‘rsatadi.',
     'Bu belgi barcha eshiklar bir tomonga ochilishi shart degani emas.'],
    'Eshik yo‘nalishini tanlashda nimalar tekshiriladi?',
    'Bino turi, evakuatsiya talabi, jihoz va yurish yo‘li bilan to‘qnashuv tekshiriladi.')
add('L00_M05_001', 'plan-check.svg', 'Yaxshi plan uchun savol',
    ['Namunada B xonaga borish A yotoqxonasidan o‘tadi — maxfiylik bo‘yicha muammo.',
     'Yaxshi plan deb baholashdan oldin foydalanish ssenariysini tekshiring.'],
    'A xonadan o‘tishni qanday bartaraf qilish mumkin?',
    'B xonaga umumiy yo‘lakdan alohida kirish variantini chizing, so‘ng maydon va aloqani qayta tekshiring.')
add('L00_M05_002', 'plan-error.svg', 'Xatoni nomlang va yechim bering',
    ['Muammo: yo‘l xususiy yotoqxona orqali o‘tmoqda.',
     'Faqat “plan yomon” deyish o‘rniga muammo, oqibat va tuzatish yoziladi.'],
    'Muammoning oqibatini ayting.', 'B xonaga kirish A xonadagi tinchlik va maxfiylikka ta’sir qiladi; alohida yo‘l kerak.')
add('L00_M05_003', 'facade-check.svg', 'Fasadni dalil bilan baholang',
    ['Fasadning derazasi plandagi xonaga mos bo‘lishi kerak.',
     'Faqat bezakni baholash plan-fasad muvofiqligini tekshirmaydi.'],
    'Planda deraza o‘chirilsa, fasadda nima tekshiriladi?', 'O‘sha ochilishning fasad, kesim va hujjatlardagi holati tekshiriladi.')
add('L00_M05_004', 'intro-audit.svg', 'Yakuniy tahlil: qarorni asoslash',
    ['Ehtiyoj, chizma va yechim dalili bir-biriga bog‘langan.',
     'Plan, fasad, kesim va genplan bitta loyiha bo‘yicha solishtiriladi.'],
    'Bitta qarorni uch dalil bilan asoslang.', 'Foydalanish ehtiyoji, chizmadagi aloqa va tekshiruv natijasini ko‘rsating.')

add('L08_M05_001', 'roof-concept.jpg', 'Tomning vazifasini tasvirdan ajrating',
    ['Ustki qoplama, konstruktiv tizim, devor va pastki tayanchlarni toping.',
     'Tasvir faqat tushuntirish uchun: birikma va kesimlar tasdiqlangan konstruktiv yechim emas.'],
    'Tomni faqat tashqi ko‘rinish deb baholashda nima unutiladi?',
    'Himoya, yuk uzatilishi, tayanchlar va suv chiqarish aloqasi unutiladi.', block=1,
    credit='ARCHIPRO UZ — AI yordamida yaratilgan konseptual tasvir')
add('L08_M05_001', 'roof-load.svg', 'Yukning pastga uzatilishini kuzating',
    ['Tom → tayanch → devor yoki ustun → fundament → grunt zanjirini kuzating.',
     'Qor, shamol va o‘z og‘irligi haqiqiy loyihada alohida yuk holatlari sifatida hisoblanadi.'],
    'Tom ostidagi tayanch olib tashlansa nima tekshiriladi?',
    'Yuk yo‘li va konstruktiv hisob qayta tekshiriladi; arxitekturaviy o‘zgarishning o‘zi yetarli emas.', block=6)
add('L08_M05_002', 'roof-load.svg', 'Uzilishsiz yuk yo‘li',
    ['Strelkalar yukning tomdan tayanchlarga va pastga uzatilish prinsipini ko‘rsatadi.',
     'Chizma faqat vertikal yo‘l misoli; shamol va seysmik ta’sirning barcha yo‘nalishlarini qamramaydi.'],
    'Tayanch joyi ko‘chirilsa qaysi bog‘lanish tekshiriladi?',
    'Tom elementi, tayanch va uning ostidagi konstruktiv tizimning muvofiqligi konstruktor bilan tekshiriladi.')
add('L08_M05_003', 'roof-pitch.svg', 'Nishab, cho‘qqi va bo‘g‘ot',
    ['Cho‘qqi yuqorida; bo‘g‘ot tomning pastki chekkasida.',
     'Simmetrik 6 m oraliqda bitta nishabning gorizontal masofasi 3 m.'],
    'Rasmdagi ko‘tarilish 1,5 m bo‘lsa qiyalikni toping.',
    '1,5 ÷ 3 × 100 = 50%. Foiz va gradusni aralashtirmang; materialga ruxsat etilgan nishab alohida tekshiriladi.')
add('L08_M05_004', 'roof-opening.svg', 'Tom oynasini tayanch bilan solishtirish',
    ['Ko‘k ochilish ikki konseptual tayanch oralig‘ida ko‘rsatilgan.',
     'Bu joylashuv hali tayyor yechim emas: rama, yuk, suv oqimi va gidroizolyatsiya tekshiriladi.'],
    'Oynani tayanch chizig‘i ustiga ko‘chirish mumkinmi?',
    'Buni hisob va koordinatsiyasiz tasdiqlamang; tayanch o‘zgarishi konstruktor, detal esa material tizimi bilan kelishiladi.')
add('L08_M05_005', 'roof-audit.svg', 'Plan, fasad va kesimni moslashtirish',
    ['Bir tomning konturi, ochilishi, cho‘qqisi va bo‘g‘ot sathlari solishtiriladi.',
     'Normativ yoki konstruktiv savol javobsiz qolsa, audit yakunlangan hisoblanmaydi.'],
    'Tom oynasi qo‘shilganda tekshiriladigan uch qismni ayting.',
    'Plan/ko‘rinishlar, konstruktiv tayanchlar va suv-gidroizolyatsiya detali qayta tekshiriladi.')

GRAPHISOFT = 'https://help.graphisoft.com/AC/28/INT/_AC28_Help/040_ElementsVB/040_ElementsVB-7.htm'
for code, asset, title, explanation, exercise, solution in [
    ('L05_M03_001', 'archicad-reference-menu.png', 'Wall Tool: reference line menyusi',
     ['Bu Graphisoft Archicad 28 INT qo‘llanmasidagi haqiqiy interfeys tasviri.',
      'Wall Settings yoki Info Box orqali reference line o‘rni tanlanadi; bu rasm barcha Wall Settings maydonlarini ko‘rsatmaydi.'],
     'Ichki 4 000 × 3 000 mm xonani chizishda nimani nazorat qilasiz?',
     'Reference line tomonini va chizish yo‘nalishini nazorat qiling; o‘lchamni ichki yuzalar orasida tekshiring.'),
    ('L05_M03_002', 'archicad-reference-plan.png', 'Reference line: plandagi yo‘nalish',
     ['Ko‘rinishni yoqish: View → On-Screen View Options → Walls & Beams Reference Lines.',
      'Strelka devor chizilgan yo‘nalishni ko‘rsatadi; interfeys tiliga qarab buyruq nomi farq qilishi mumkin.'],
     'Devorning ichki/tashqi tomoni nega almashtib qolishi mumkin?',
     'Reference line o‘rni va chizish yo‘nalishini tekshiring; o‘zgarishdan keyin plan hamda 3Dni solishtiring.'),
]:
    add(code, asset, title, explanation, exercise, solution,
        boundary='Archicad 28 INT namunasi. Boshqa versiya yoki interfeys tilida ko‘rinish farq qilishi mumkin.',
        credit='Graphisoft Archicad 28 Help — rasmiy qo‘llanmadagi skrinshot; © Graphisoft', source_url=GRAPHISOFT)


_LOAD_ERRORS = []
for manifest in ('lesson_figures.json', 'archicad_figures.json'):
    try:
        records = json.loads((ASSETS / manifest).read_text(encoding='utf-8'))
        staged = []
        for record in records:
            entry = dict(record)
            entry.pop('recipe', None)
            entry.pop('source_image_url', None)
            staged.append(entry)
        for entry in staged:
            add(**entry)
    except Exception as exc:
        # Reading a lesson must remain possible if media was omitted/damaged.
        # Release validation rejects the incomplete package below.
        _LOAD_ERRORS.append(manifest + ': ' + str(exc))
        logging.error('Lesson visual manifest unavailable: %s', _LOAD_ERRORS[-1])


# Reviewed material illustrations replace schematic supplements only for the
# explicitly listed lessons. Genuine software documentation captures remain.
try:
    realistic_records = json.loads((ASSETS / 'realistic_figures.json').read_text(encoding='utf-8'))
    reviewed = {}
    for record in realistic_records:
        entry = dict(record)
        code = entry.pop('code')
        if code not in CATALOG or code in reviewed:
            raise ValueError('Unknown or duplicate realistic lesson: ' + code)
        if not entry['asset'].startswith('realistic-') or not entry['asset'].endswith('.jpg'):
            raise ValueError('Unexpected realistic image: ' + code)
        if set(entry) != {'asset', 'title', 'explanation', 'exercise', 'solution',
                          'block', 'boundary', 'credit', 'source_url'}:
            raise ValueError('Incomplete realistic metadata: ' + code)
        reviewed[code] = entry
    # Validate the complete manifest before replacing any mapping.
    for code, entry in reviewed.items():
        preserved = [spec for spec in CATALOG[code]
                     if spec['asset'].lower().endswith('.svg')
                     or spec['asset'].startswith('sketch-')
                     or (spec.get('source_url') or '').startswith('https://help.graphisoft.com/')]
        CATALOG[code] = preserved
        add(code, **entry)
except Exception as exc:
    _LOAD_ERRORS.append('realistic_figures.json: ' + str(exc))
    logging.error('Realistic lesson manifest unavailable: %s', _LOAD_ERRORS[-1])



# Every lesson keeps at least one lightweight topic sketch. Rendered material
# studies and official Archicad screenshots remain as supplemental visuals.
try:
    supplemental_records = json.loads((ASSETS / 'supplemental_sketches.json').read_text(encoding='utf-8'))
    for entry in supplemental_records:
        add(**entry)
except Exception as exc:
    _LOAD_ERRORS.append('supplemental_sketches.json: ' + str(exc))
    logging.error('Supplemental sketch manifest unavailable: %s', _LOAD_ERRORS[-1])

def asset_path(filename):
    """Catalog paths stay beneath the packaged figures directory."""
    path = ASSETS / filename
    if Path(filename).name != filename or path.suffix.lower() not in {'.svg', '.png', '.jpg'}:
        raise ValueError('Invalid figure asset path')
    return path


def visuals_for_block(code, block_index):
    return tuple(spec for spec in CATALOG.get(code, ()) if spec['block'] == block_index)


def validate_visual_catalog(contents):
    errors = list(_LOAD_ERRORS)
    if set(contents) != set(CATALOG):
        errors.append('Visual coverage must match every lesson exactly')
    for code, specs in CATALOG.items():
        if code not in contents:
            errors.append('Unknown lesson: ' + code)
            continue
        for spec in specs:
            if not 0 <= spec['block'] < len(contents[code]):
                errors.append('Invalid block: ' + code)
            if not asset_path(spec['asset']).is_file():
                errors.append('Missing asset: ' + spec['asset'])
            if any(not spec[key] for key in ('title', 'explanation', 'exercise', 'solution', 'boundary')):
                errors.append('Incomplete teaching figure: ' + code)
    if errors:
        raise ValueError('\n'.join(errors))
    return dict(total_lessons=len(contents), illustrated_lessons=len(CATALOG),
                pending_lessons=len(contents) - len(CATALOG),
                figures=sum(map(len, CATALOG.values())),
                realistic_lessons=len(reviewed) if not _LOAD_ERRORS else 0,
                realistic_pending=len(contents) - (len(reviewed) if not _LOAD_ERRORS else 0))
