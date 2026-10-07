# Visual update validation

The 255-lesson checkpoint passed all 24 release regression tests under real PySide6 widgets with QT_QPA_PLATFORM=offscreen (313.639 seconds, exit 0). The suite opens all 680 lesson pages and checks the full PRO flow through 16 levels. Original lesson blocks, quiz data and progress behavior are covered by the release suite.

The subsequent 270-lesson checkpoint passed the four focused visual tests: worked lesson/catalog alignment, complete asset inventory, zoom/font/layout/quiz gates, and missing-image fallback (5.831 seconds, exit 0). A separate inventory check confirms 213 AI render lessons plus 57 screenshot-only lessons, disjoint and unique. All 680 lesson contents still match the saved original content inventory.

Two newly revised lessons (L05_M09_004 and L05_M10_005) were also opened in the actual lesson UI at 1366 × 768; content width matched the scroll viewport width. A damaged L02_M04_003 JPEG was regenerated from its intact original PNG; the previous decoder warning disappeared.

These checks do not constitute a Windows executable build test, SHNQ verification or completion of the remaining 410 topic reviews.

The 275-lesson checkpoint additionally passed the same four focused tests (5.938 seconds, exit 0); 214 AI and 61 screenshot-only reviews are disjoint and unique. All original content blocks remain equal to the saved 680-lesson inventory. 405 lessons remain for topic review.

## Final static inventory validation

The completed topic-specific visual inventory now covers all 680 lesson codes.

Static repository checks on the current visual-review branch confirmed:
- 680 rows in REALISTIC_LESSON_COVERAGE.csv with 680 unique lesson codes.
- Status totals of 222 reviewed_material_render, 78 reviewed_documented_screenshots and 380 reviewed_architectural_sketch.
- Zero missing asset files referenced by REALISTIC_LESSON_COVERAGE.csv.
- Zero reviewed lesson codes missing visual metadata across lesson_figures.json, realistic_figures.json and archicad_figures.json.
- Zero metadata entries pointing to missing visual asset files.
- 680 rows and 680 unique lesson codes in VISUAL_LESSON_COVERAGE.csv, with the same lesson-code set as REALISTIC_LESSON_COVERAGE.csv.
- 380 architectural-sketch coverage rows resolve to 380 unique asset blobs; zero duplicate-sketch groups remain after the topic-specific redraw pass.
- Asset mapping is consistent: all 380 architectural-sketch coverage rows point to the same asset recorded in both VISUAL_LESSON_COVERAGE.csv and lesson_figures.json.

This is a static inventory/consistency audit. It does not replace a fresh Windows executable build, a fresh full PySide6 UI regression run, or deferred SHNQ/normative verification.
