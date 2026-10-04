# Offline visual lessons — first implementation checkpoint

This is an incremental curriculum change, not completion of all visual lessons.
The complete 680-lesson / 137-module inventory is recorded in
`VISUAL_LESSON_COVERAGE.csv`. 27 lessons currently have 28 visual supplements;
653 lessons remain pending individual topic review and illustration authoring.

## Implemented

- All 20 introductory LEVEL_00 lessons, using linked plan/facade/section/site
  examples, scale and level arithmetic, conceptual structural roles and audits.
- All five L08_M05 roof lessons, including an AI conceptual illustration and
  deterministic load-path, slope, opening-coordination and document-audit figures.
- L05_M03_001 and L05_M03_002: actual Graphisoft Archicad 28 INT documentation
  screenshots for the reference-line controls and their floor-plan display.
- Figures render offline below the original block text. At wide widths the
  figure and explanation appear beside each other; narrower widths stack them.
- Zoom dialog supports fit, plus/minus, scrolling and close. Figure explanations
  follow the existing reading-size control. A missing image leaves lesson text
  and quizzes usable and displays a local fallback message.
- Build scripts collect the assets directory; packaged curriculum validation
  checks the catalog and asset inventory.

No original lesson block, lesson ID, quiz, answer key, progress schema, license
or authentication logic was modified. Media never marks a lesson completed.

## Technical / content boundary

AI illustrations are conceptual teaching images, not approved construction
details. The illustrated geometric examples are teaching inputs, not mandatory
Uzbek minimum dimensions, roof pitches, member sizes or engineering capacities.
Structural design, seismic checks, evacuation and material-specific requirements
need the applicable object classification, current regulation and engineering
review. Do not relabel a conceptual figure as SHNQ-compliant certified design.

## Primary sources checked on 2026-10-05 (Asia/Tashkent)

- Ministry official SHNQ 2.01.02-04: https://mc.uz/uploads/mcuz_6099785631525.pdf
  Clauses 5.17 and 5.18 distinguish exit-opening direction, exceptions and
  freely opening the listed evacuation doors from inside without a key.
- SHNQ 2.08.01-24: https://lex.uz/docs/7121730
  January 2026 amendment: https://lex.uz/docs/8029374
  April 2026 amendment: https://lex.uz/docs/8156560
  Confirm the edition effective on the actual project date; a future edition
  must not be silently substituted for the current one.
- Graphisoft Archicad 28 INT Wall Reference Line:
  https://help.graphisoft.com/AC/28/INT/_AC28_Help/040_ElementsVB/040_ElementsVB-7.htm
  The two bundled screenshots are credited to Graphisoft in the lesson;
  copyright remains with Graphisoft. They depict documentation UI fragments,
  not an AI imitation or a complete current user project. Their sample numeric
  settings must not be copied as project defaults. Version/language can differ.

## Continue the remaining work

Use `visual_catalog.CATALOG` as the only explicitly reviewed mapping. Do not
invent mappings from title keywords or count a reused generic picture as a
fully reviewed lesson. For each pending lesson:

1. Read every original block and its existing worked example.
2. Identify precisely what visual evidence teaches the current topic.
3. Verify every normative assertion from an applicable, effective official source.
4. Author the specific visual and its explanation, exercise, solution and boundary.
5. Add explicit mappings to the correct block index; retain original text.
6. Update coverage CSV and run catalog, real-widget and packaged-asset checks.

Architecture/room planning: Uzbek courtyard/family contexts with metric labels.
Geometry: precise SVGs for dimensions and calculations. Concept illustration:
AI visuals plus reviewed text. Software UI: actual version-labelled screenshots,
not AI-generated menus. Professional workflow topics: concrete case diagrams,
document examples and revisions rather than decorative house pictures.

## Rollback

`stable-before-visual-lessons` preserves the previously passing version at
`8f0f17cdf15aa8265a1110dc8cc505522c4342f4`.

Windows EXE rebuild and customer device validation remain required; Linux
Qt/offscreen checks do not constitute a Windows executable build.
