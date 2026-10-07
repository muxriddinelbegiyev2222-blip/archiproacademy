# Davom etayotgan eskiz sifati yangilanishi — 2026-10-07

19 zarur darsning eski sxemalari yangi, ko‘rib chiqilgan izohli arxitektura eskizlariga almashtirildi: L06_M10_001–005, L07_M01_001/002/004/005, L07_M02_001–005 va L07_M03_001–005. L07_M01_003 rasm kerak bo‘lmagan dars sifatida o‘tkazildi. Haqiqiy Graphisoft skrinshotlari saqlanadi.

282 zarur eski eskiz darsidan ushbu 19 dars va avvalgi L15_M08_003 yangilangan: 262 zarur eskiz dars hali ushbu sifat qayta ko‘rigidan o‘tmagan. Materialli tasvirlar va haqiqiy skrinshotlar bu hisobdan alohida; umumiy sifat ishi tugallangan deb belgilanmadi.

[Promptlar, tasvirlar va tekshiruv qaydi](VISUAL_QUALITY_REWORK_2026_10_07.json). Rasmlar asl 1536×1024 piksel o‘lchamida joylandi. Oldingi 11 rasm uchun Windows auditi, to‘liq regressiya va haqiqiy EXE tekshiruvi muvaffaqiyatli yakunlandi (run 37573365600); qo‘shimcha 8 rasm keyingi commit tekshiruviga kiradi.

---
# Rasm zarurligi bo‘yicha yangi qaror — 2026-10-07

680 darsning maqsadi va amaliyoti qayta ko‘rib chiqildi: 65 darsga alohida rasm kerak emas (C), 44 darsda ixtiyoriy (B), 571 darsda ko‘rgazmali misol saqlanadi (A). C va B uchun jami 109 ta yangi rasm yasash majburiy emas. A soni yangi AI rasm ishlab chiqish soni emas: mavjud sifatli chizma yoki haqiqiy skrinshot yetarli bo‘lishi mumkin.

[To‘liq rasm zarurligi auditi](LESSON_IMAGE_NECESSITY_2026_10_07.md) va [680 dars reyestri](LESSON_IMAGE_NECESSITY_2026_10_07.csv). Bu bosqich mavjud asset yoki dars bog‘lanishini o‘zgartirmadi; oldingi 680/680 texnik qamrov bilan ta’limiy zarurat alohida baholandi.

---

# Current quality recheck — 2026-10-07

Technical coverage is 680/680. This does not establish that all drawings meet the requested hand-sketch quality.
Three final lessons (L15_M08_003–005) have new illustrated architectural sketches and corresponding Uzbek captions.
The other 377 entries from the previous 380-sketch group await visual-style recheck. See [QUALITY_RECHECK_2026_10_07.md](QUALITY_RECHECK_2026_10_07.md).
The earlier inventory record below is retained as history, not a final quality acceptance.

---

# Visual review progress

680 of 680 lessons have completed the current topic-specific visual review: 222 AI material-render lessons, 78 lessons using documented Graphisoft screenshots and 380 lessons using topic-specific architectural sketches. 0 lessons remain for topic-specific visual review.

Review details are tracked in REALISTIC_LESSON_COVERAGE.csv, SCREENSHOT_LESSON_REVIEW.csv and VISUAL_LESSON_COVERAGE.csv. This pass changes visual teaching support and related metadata; original lesson blocks, quizzes and application behavior are not intentionally changed by the visual review.

For L05_M01, generic SVG supplements were replaced by inspected screenshots with distinct Uzbek explanations for Toolbox, Info Box, Navigator, Tab Overview, Zoom to Selection and Navigator Preview panning. Graphisoft’s Archicad 28 documentation reuses some Archicad 24 screenshots; the lesson captions state that limitation explicitly. SHNQ verification is deferred.

L05_M02: Project Map, View Map, saving a view, placing a Drawing and updating a Layout reviewed against official documentation.

L05_M03: Wall Settings height linking, Basic versus Composite thickness, Reference Line faces, chained walls and junction checks reviewed. Documentation examples are explicitly distinguished from the numeric training model.

L05_M04: Slab structure, Top/Bottom reference plane, contour editing, selected Slab hole creation and actual 3D hole outcome reviewed. Numeric area applies to the defined exercise polygon, not automatically to a slab extending over walls.

L05_M05: Window screenshots no longer stand in for door swing instruction. Actual placement, plan swing and Flip before/after images added; sill reference and reveal depth distinguished; Library 26/Window 20 labels disclosed.

L05_M06: Column cross-section versus height, centered reference axis and Beam reference elevation reviewed. Four screenshot lessons plus one original AI material frame for the mini-project; real Settings screenshots remain alongside that render.

L05_M07: Object library gabarits, placement anchor, rotation/mirroring, base elevation and Drag a Copy reviewed. Bedroom access and dining-chair use illustrated with two new realistic renders; original lesson content remains unchanged.

L05_M08: Line/Polyline distinction, Fill controls, Text readability, associative label placement and example model labels reviewed. Manual label text is not falsely described as automatically updating.

L05_M09: Associative dimensions, outer/core faces, room clear distances, linear chains and flexible text arrangement reviewed. 9000 mm worked example and 6000 mm independent exercises explicitly distinguished.

L05_M10: First project reviewed with Story Settings, Wall/Slab, Window, Dimension, Zone and Object elevation captures; three new realistic material examples explain wall–slab contact, room access and a deliberately floating desk versus corrected placement.

L06_M01: Story height/elevation distinction, Home Story, Top Link, offsets, relinking and multi-story audit reviewed. New realistic two-story cutaway shows vertically aligned walls and intermediate slab; circulation and engineering design are not claimed.

L06_M02: Layer and combination distinctions, visibility/locking, new combination creation, Update persistence, intersection groups and saved-view audits reviewed. Legacy v2022 capture reused by official AC28 Help explicitly disclosed.

L06_M03: Building Material versus Surface, Cut Fill/pens, intersection priority and project-wide attribute effects reviewed. Realistic brick samples explain appearance difference without implying a changed substrate or an engineered wall detail.

L06_M04: Composite skins versus separators, material selection, Core/Finish/Other, thickness totals and composite reference lines reviewed. Four-layer exploded material sample illustrates the exercise without claiming a complete wall assembly.

L06_M05: Complex Profile concept, Profile Editor workflow, Use with availability, profile origin, Fill/Building Material logic and Plan/Section/3D audit reviewed against official Archicad 28 Help. Generic SVG supplements were removed for these five lessons; exact exercise values remain in native lesson text.

L06_M06: Roof Settings, Single/Multi-plane selection, pitch units, overhang distinction and multi-view Roof audit reviewed. Four existing high-quality realistic roof teaching renders were remapped with lesson-specific explanations; generic repeated SVG roof diagrams were removed.

L06_M07: Stair Top Link/Home Story, tread-riser controls, configurable Rules & Standards, turning types and multi-view Stair audit reviewed using actual Archicad 28 screenshots. Repeated 3000/18 generic SVG diagrams were removed; SHNQ verification remains deferred.

L06_M08: Railing hierarchy, Segment/Node structure, Pattern Editor components, associativity to Stair/Slab and pattern distribution reviewed using actual Archicad 28 screenshots. Generic railing SVG supplements were removed; numeric safety compliance remains outside this deferred SHNQ phase.

L06_M09: Mesh reference plane/construction methods and New Mesh Points workflow reviewed. Survey, sloping site, house-on-slope and terrain-audit material renders were remapped with Mesh-specific explanations; repeated slope SVG diagrams were removed.

L06_M10: Zone concept, boundary/area response, Zone Stamp readability, functional grouping and multi-source Zone audit reviewed. Five repetitive generic diagrams were rebuilt as topic-specific light architectural sketches while the genuine Archicad screenshots remain as software references.

L07_M01: Favorites concept, create/apply workflow, library organization, standardization and audit reviewed. Five repeated generic diagrams were rebuilt as topic-specific light architectural workflow sketches; official Archicad screenshots remain as the software reference layer.

L07_M02: Graphic Override concept, rule logic, combinations, analytical views and audit reviewed. Five repetitive diagrams were rebuilt as topic-specific light architectural analysis sketches; official Archicad screenshots remain available for interface reference.

L07_M03: Model View Options concept, component display control, MVO combinations, saved-view workflow and audit reviewed. Five repeated diagrams were rebuilt as topic-specific light architectural sketches; the genuine MVO screenshot remains the interface reference.

L07_M04: Renovation concept, status assignment, filters, reconstruction workflow and audit reviewed. Five generic diagrams were rebuilt as topic-specific light architectural sketches; the genuine Renovation screenshot remains the interface reference.

L07_M05: Schedule concept, Criteria/Fields, sorting/grouping, Door-Window-Zone schedules and audit reviewed. Five generic diagrams were rebuilt as topic-specific architectural/data sketches; genuine Scheme/Criteria/Fields screenshots remain the software references.

L07_M06: BIM Properties concept, Property definition, data standardization, Schedule integration and professional audit reviewed. Five generic diagrams were rebuilt as topic-specific architectural/data sketches; genuine Property Manager and Schedule screenshots remain software references.

L07_M07: BIM Classification concept, element type distinction, Property linkage, Schedule usage and professional audit reviewed. Five generic diagrams were rebuilt as topic-specific architectural/data sketches; the genuine Classification Manager screenshot remains the software reference.

L07_M08: Hotlink/Module concept, module boundaries, source-link updates, complex project structure and professional audit reviewed. Five generic diagrams were rebuilt as topic-specific architectural workflow sketches; genuine Hotlink Manager/Place Hotlink screenshots remain interface references.

L07_M09: Professional Template concept, template structure, view/graphic/documentation standard, BIM data standard and full template audit reviewed. Five generic diagrams were rebuilt as topic-specific architectural/workflow sketches; genuine Archicad layer/material/view/classification/story screenshots remain interface references.

L08_M06: Moisture sources, foundation/ground contact, roof and balcony drainage, wet-room waterproofing and professional audit reviewed. Five generic diagrams were rebuilt as topic-specific architectural section/detail sketches; SHNQ verification remains deferred.

L08_M07: Thermal insulation concept, envelope continuity, thermal bridges, window/balcony/parapet junctions and professional audit reviewed. Five generic diagrams were rebuilt as topic-specific architectural section/detail sketches; SHNQ and quantitative thermal verification remain deferred.

L08_M08: Seismic load concept, plan regularity, vertical continuity/soft-story risk, mass asymmetry and professional architectural-structural audit reviewed. Five generic diagrams were rebuilt as topic-specific conceptual architectural/structural sketches; no structural design values are inferred from the images.

L08_M09: Architect/structural-engineer roles, information package, issue workflow, version/change management and professional coordination audit reviewed. Five generic diagrams were rebuilt as topic-specific architectural coordination sketches; structural design remains the engineer’s calculation responsibility.

L09_M01: Normative document reading workflow, scope/object type, revision/date/status, clause/evidence linkage and professional normative audit reviewed. Five generic diagrams were rebuilt as topic-specific evidence/workflow sketches. Exact SHNQ/QMQ verification remains deferred.

L09_M02: Residential normative analysis, room functions/zoning, sanitary-support zones, vertical circulation and full residential audit reviewed. Five generic diagrams were rebuilt as topic-specific architectural plan/workflow sketches; exact normative values remain deferred to official-source verification.

L09_M03: Site/document context, boundaries and access, neighboring context, genplan coordination and full site audit reviewed. Five generic diagrams were rebuilt as topic-specific genplan sketches; exact site setbacks and planning requirements remain deferred to official-source verification.

L09_M04: Natural daylight, orientation/sun, external shading, plan-facade-section coordination and lighting/insolation audit reviewed. Five generic figures were rebuilt as topic-specific architectural lighting sketches; quantitative verification remains normative/calculation dependent.

L09_M05: Fire-safety systems thinking, people/routes/exits, construction/material links, site/external access and professional fire-safety audit reviewed. Five generic figures were rebuilt as topic-specific architectural safety sketches; exact values remain normative-source dependent.

L09_M06: Evacuation concept, route continuity, door-corridor-stair sequence, obstacle/error scenarios and professional evacuation audit reviewed. Five generic figures were rebuilt as topic-specific architectural escape-route sketches; exact dimensional requirements remain normative-source dependent.

L09_M07: Accessibility concept, entrance/movement chain, door-level-vertical circulation, sanitary/use zones and professional accessibility audit reviewed. Five generic figures were rebuilt as topic-specific architectural accessibility sketches; exact dimensional requirements remain normative-source dependent.

L13_M07: Trade-off explanation, disagreement management and decision-defense audit completed with topic-specific architectural workflow sketches.

L13_M08: First contact, brief/variants, client presentation, controlled revision/conflict and Level 13 full workflow audit completed with topic-specific architectural workflow sketches.

L14_M01: Narrow-site analysis, longitudinal zoning, daylight/courtyard strategy, circulation/privacy and professional audit completed with topic-specific architectural site/plan sketches.

L14_M02: Irregular-site reading, primary building axis, residual-zone use, facade/perspective control and professional audit completed with topic-specific architectural site sketches.

L14_M03: Sloped-site analysis, building level/terrain, split-level/terracing, drainage-retaining-access coordination and professional audit completed with topic-specific terrain/section sketches.

L14_M04: Large-villa program, functional clusters, guest/family/service circulation, massing/courtyard/landscape and professional audit completed with topic-specific architectural program/plan/massing sketches.

L14_M05: Multigenerational living scenarios, shared/private balance, future accessibility/adaptation, entrance-kitchen-service models and professional audit completed with topic-specific architectural planning sketches.

L14_M06: Premium-facade concept, proportion/massing, material/detail hierarchy, light-shadow-landscape and professional audit completed with topic-specific architectural facade sketches.

L14_M07: Design Clinic methodology, plan diagnostics, facade/massing diagnostics, BIM/technical diagnostics and final audit completed with topic-specific diagnostic architectural sketches.

L14_M08: Case-study analysis method, complex-site case, complex-family case, design/technical conflict case and Level 14 advanced-case audit completed with topic-specific architectural case sketches.

L15_M01: Integrated theory, site/planning/ergonomics, structure/normative thinking, BIM/documentation theory and PRO theory audit completed with topic-specific architectural/BIM sketches.

L15_M02: Model setup, modeling, advanced BIM, documentation and Archicad PRO audit challenges completed with topic-specific architectural/BIM sketches.

L15_M03: Plan, facade/section, structure/MEP, BIM/documentation error finding and Root Cause PRO audit completed with topic-specific diagnostic architectural sketches.

L15_M04: Final brief intake, requirement classification, constraints/risks, deliverables/success criteria and technical brief audit completed with topic-specific workflow sketches.

L15_M05: Final project concept, plan/site, BIM/technical coordination, facade/documentation and professional audit reviewed. Five generic visuals were rebuilt as topic-specific light architectural final-project sketches.

L15_M06: Defense story structure, evidence-based decisions, technical explanation, jury Q&A and final defense audit reviewed. Five generic visuals were rebuilt as topic-specific architectural presentation sketches.

L15_M07: Portfolio strategy, project selection, project story, graphic/text hierarchy and professional portfolio audit reviewed. Five generic visuals were rebuilt as topic-specific architectural portfolio sketches.

L15_M08: PRO readiness self-audit, weak-skill improvement, integrated case challenge, submission readiness and ARCHIPRO UZ final mastery audit reviewed. Five generic visuals were rebuilt as topic-specific architectural/mastery sketches.

L09_M08: Normative error taxonomy, source/context checking, plan/genplan conflicts, version/documentation coordination and final Level 9 audit reviewed. Five generic visuals were rebuilt as topic-specific architectural normative-audit sketches; exact SHNQ/QMQ verification remains deferred.

L10_M01: Client brief definition, family/lifestyle scenarios, room program, constraints/priorities and professional brief audit reviewed. Five generic visuals were rebuilt as topic-specific architectural brief sketches.

L10_M02: Site analysis concept, street/access/orientation, sun-wind-neighbor context, terrain/existing elements and professional site audit reviewed. Five generic visuals were rebuilt as topic-specific architectural site-analysis sketches.

L10_M03: Bubble Diagram concept, zoning/relationships, circulation, alternatives and professional bubble audit reviewed. Five generic visuals were rebuilt as topic-specific architectural bubble-diagram sketches.

L10_M04: Bubble-to-plan transition, room proportion/furniture testing, door/circulation coordination, facade-yard linkage and sketch-plan audit reviewed. Five generic visuals were rebuilt as topic-specific architectural sketch-plan visuals.

L10_M05: Plan optimization, dead-space efficiency, conflict resolution, structure/MEP logic and final plan audit rebuilt as topic-specific architectural sketches.

L10_M06: BIM model startup, stories/grid, core model elements, multi-view coordination and model audit rebuilt as topic-specific architectural/BIM sketches.

L10_M07: Facade concept, proportion/rhythm, opening/entrance emphasis, material/massing and facade audit rebuilt as architectural facade sketches.

L10_M08: Roof concept, slope/drainage, ridge/eave/junctions, facade coordination and roof audit rebuilt as architectural roof sketches.

L10_M09: Professional sections, levels/heights, structural openings, design checks and section audit rebuilt as architectural section sketches.

L10_M10: Genplan strategy, pedestrian/vehicle movement, outdoor functions, levels/drainage and genplan audit rebuilt as architectural site sketches.

L10_M11: Project album structure, plans/facades/sections, genplan/auxiliary drawings, layout quality and final Level 10 audit rebuilt as architectural documentation sketches.

## Final 680-lesson inventory audit

- REALISTIC_LESSON_COVERAGE.csv contains 680 unique lesson codes and no pending topic-review rows.
- Final status mix: 222 reviewed material-render lessons, 78 reviewed documented-screenshot lessons and 380 reviewed architectural-sketch lessons.
- Every reviewed coverage asset currently exists in app/courses/visual_assets.
- Every one of the 680 coverage lesson codes has at least one visual metadata entry across lesson_figures.json, realistic_figures.json or archicad_figures.json.
- VISUAL_LESSON_COVERAGE.csv also contains 680 unique lesson codes and matches the same lesson-code set.
- 380 architectural-sketch lessons now reference 380 unique asset blobs; the duplicate-sketch audit reports zero duplicate groups.
- SHNQ verification remains a separate later task unless explicitly completed elsewhere; this final count is the topic-specific visual review count.
