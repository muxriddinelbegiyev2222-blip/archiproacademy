# Offline illustrations for all 680 lessons

The explicit catalog now covers all 680 lessons in 137 modules: 890 figure
supplements, zero lessons without a mapped visual. This change adds a separate
SVG for each of the previously unillustrated 653 lessons and 209 documentation
screenshot supplements. The earlier 27 lessons and their media remain available.
`VISUAL_LESSON_COVERAGE.csv` records every lesson, asset and supplement count.

## What pupils see

Original explanation blocks remain intact. A figure is placed with its relevant
worked example; Archicad documentation fragments appear with the introductory
explanation of the tool/panel. Each supplement includes an explanation, an
exercise and its sample result. Wide layouts show picture and explanation side
by side; narrower layouts stack them. Reading size controls also apply to figure
explanations. The enlargement dialog supports fit, bounded zoom and scrolling.

The illustrations include room furniture/use zones, courtyard/site relationships,
facade composition and dimensions, building sections and load paths, geometric
calculations, element/data comparisons, drawing sheets, revision records and
professional decision tables. Each generated SVG contains the lesson code,
title, worked case and the current worked step. Explicit module/stage recipes
select the diagram; there is no runtime title-keyword guessing.

The 653 new assets are vector teaching diagrams, not 653 AI photorealistic images
or engineering details. Related lessons use a consistent diagram vocabulary;
not every picture is an unrelated new building. Existing conceptual AI roof
imagery remains labelled as conceptual. Exact calculations use vector graphics.

Archicad lessons use 58 additional genuine documentation assets, supplementing
the existing two reference-line images. Every screenshot records the exact
Graphisoft source page and source image URL, attribution and documentation
version. The independent list is `ARCHICAD_FIGURE_SOURCES.csv`. The captured
fragment shows only the named panel/action; sample values and library names can
be different from the pupil's exercise and from a different Archicad version.

## Preservation and packaging

No original lesson block, ID, quiz/question/answer, progress schema, licensing or
authentication logic changed. Original and previously added worked content was
compared for all 680 lessons; the 2,041 quiz questions remain. Media does not
mark a lesson complete or unlock the next lesson. The existing roof-pitch
supplement's exercise was corrected to use the 1.5 m / 3 m / 50% shown in its
picture rather than a different input.

All pictures and both catalog JSON manifests are bundled by `build_client.py`.
Lessons render offline. If an individual asset or manifest is missing, original
lesson text and quiz behavior remain usable; release validation rejects an
incomplete media package. Catalog validation requires exact 680-lesson coverage.

## Verification scope

Regression checks require 680 illustrated lessons, 653 distinct new diagram
paths, valid assets, correct lesson/block mappings, worked-stage associations,
source attribution, existing quiz/progress behavior and all 680 real Qt lesson
pages. Package validation checks the manifests and files. Additional visual QA
checked SVG text bounds and intersecting text labels; identified intersections
were corrected. Representative Qt screenshots check wide/narrow layouts and
large reading fonts.

Coverage and passing software checks are not certification of all teaching
content or approval of an actual building design. These diagrams are schematic
and are not printed construction drawings. Structural capacities, seismic
checks, evacuation dimensions, accessibility limits and site setbacks need the
actual object's classification, an applicable effective regulation and the
responsible professional's calculations/review. Teaching numbers are not
mandatory Uzbek minimums. No new numerical SHNQ requirements are asserted.

## Official regulation references

- Ministry register: https://gov.uz/oz/mc/pages/shaharsozlik-normalari-va-qoidalari
- Fire safety SHNQ 2.01.02-04: https://mc.uz/uploads/mcuz_6099785631525.pdf
  Clauses 5.17/5.18 distinguish opening direction, exceptions and free opening
  of the listed evacuation doors from inside without a key. There is no
  blanket rule in these figures that every house door must open outward.
- Housing SHNQ 2.08.01-24: https://lex.uz/docs/7121730
  Amendments: https://lex.uz/docs/8029374 and https://lex.uz/docs/8156560
  Select the edition effective on the actual project date; the site may also
  display future editions.
- Graphisoft Archicad 28 INT Help: https://help.graphisoft.com/AC/28/INT/
  Copyright remains with Graphisoft; these are attributed teaching fragments,
  not an AI imitation of the application.

## Maintenance and rollback

Run `python devtools/author_lesson_figures.py` from the repository root to
regenerate the 653 SVGs and their catalog from the existing worked examples.
Curate `MODULE_RECIPES` explicitly when a teaching stage changes, then inspect
its output and rerun the release checks. Do not replace topic review with an
asset count. `devtools/fetch_archicad_figures.py` restores missing documentation
assets from the exact committed URLs; the customer application never runs it.

`stable-before-visual-lessons` preserves the earlier passing version at
`8f0f17cdf15aa8265a1110dc8cc505522c4342f4`; `visual-lessons-v1` preserves the
27-lesson implementation at `4c9fb40539cd90da9f238fee86af7c8470aba736`.

Rebuild the Windows EXE with `BUILD_RELEASE.bat` and check it on a customer
Windows device. Linux Qt/offscreen verification is not a Windows build or a
substitute for checking the generated executable.

## Follow-up teaching clarity review

The slope figures in L03_M07, L06_M09 and L14_M03 now explicitly label their
vertical exaggeration. Their displayed slope is calculated from the written
level difference and horizontal distance, not by measuring the picture angle.
Figures without a numbered marker no longer tell the student to find one.

L12_M07_004 now distinguishes Publishing Properties > Save files and Path
from Publisher > Format > PDF. The worked teaching stage, vector caption and
credited screenshot explanation are updated together. The original exercise,
expected result, quiz and progress rules are retained. Source:
https://help.graphisoft.com/AC/28/INT/_AC28_Help/070_Documentation/070_Documentation-118.htm
https://help.graphisoft.com/AC/28/INT/_AC28_Help/070_Documentation/070_Documentation-119.htm
