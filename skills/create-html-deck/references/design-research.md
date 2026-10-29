# Open-source design research

Reviewed through 2026-10-30 (Asia/Shanghai). This is a design-source notebook, not a ranking or a claim that every upstream project has been installed or tested. The bundled templates use original CSS, artwork, and sample copy. No upstream theme code, photos, logos, or fonts are redistributed.

## Presentation systems and discovery

| Source | Inspected | Useful observation | Use in this collection |
|---|---|---|---|
| [Slidev official themes](https://github.com/slidevjs/themes) · [gallery](https://sli.dev/resources/theme-gallery) | Repository and official gallery | Serif and restrained black/white directions support different speaking contexts | Editorial's typography; distinct systems sharing one canvas contract |
| [Reveal.js](https://github.com/hakimel/reveal.js) · [themes](https://revealjs.com/themes/) | Official theme documentation | Light, dark, and serif palettes can share navigation | Reference for palette breadth; no runtime imported |
| [Awesome-Marp](https://github.com/favourhong/Awesome-Marp) | Repository overview | A collection needs visual discovery, not just filenames | Cover previews and intended-use labels |
| [Marp community gallery](https://github.com/rnd195/marp-community-themes) · [website](https://rnd195.github.io/marp-community-themes/) | Browser gallery | Theme thumbnails and light/dark categorization make comparison easier | Scene filters, tone labels, and direct previews |
| [Shower](https://github.com/shower/shower) · [Ribbon](https://github.com/shower/shower/tree/main/packages/ribbon) | README and Ribbon documentation | Themes remain separate from navigation; examples demonstrate usable layouts | Retain a small controller and document layout roles; no engine port |

## Themes and layout studies

| Source | Inspected | Useful observation | Local decision |
|---|---|---|---|
| [Neversink](https://github.com/gureckis/slidev-theme-neversink) · [demo](https://gureckis.github.io/slidev-theme-neversink/example/) | README, license, rendered second slide | Bright flat surfaces, education-focused layouts, and strong topic/content separation | Seminar uses a quiet accent rail and evidence-oriented structure; does not include Neversink components |
| [Geist](https://github.com/nico-bachner/slidev-theme-geist) · [demo](https://slidev-theme-geist-demo.vercel.app) | README, license, rendered cover | High-contrast type and restrained chrome | Monograph makes whitespace and large text the primary structure; no Vercel marks |
| [Scholarly](https://github.com/jxpeng98/slidev-theme-scholarly) · [demo](https://scholarly.jxpeng.dev/) | README, license, rendered cover | Academic layouts explicitly accommodate research evidence and references | Seminar includes a hypothesis block, source line, comparison table, and limits |
| [Academic](https://github.com/alexanderdavide/slidev-theme-academic) | README and license | Figure captions, source fields, and index layouts are first-class content | Preserve visible source placeholders rather than decorative fake data |
| [My Marp Themes](https://github.com/rnd195/my-marp-themes) | README, `graph_paper.css`, gallery thumbnails | Graph-paper texture and framed layouts give technical content a working-notes character | Blueprint uses an original blue grid, boundary panel, and process layout; does not import theme CSS |
| [Frontend Slides](https://github.com/zarazhangrui/frontend-slides) | README, license, Creative Mode design specification | Bold type, hard shadows, and flat color blocks create a more energetic speaking rhythm | Poster develops an original pink/lime/violet system and four compositions, without copying the specification or templates |
| [UoGSoE Marp themes](https://github.com/UoGSoE/marp-themes) | README and license | The `unrendered` direction treats source-code typography as a presentation language | Console uses an original terminal palette, pseudocode window, change comparison, and verification list |
| [Purplin](https://github.com/moudev/slidev-theme-purplin) | README and layout/component examples | Quote/image layouts and a deliberate footer treatment | Layout reference only; no direct port or dependency |
| [Unicorn](https://github.com/Dawntraoz/slidev-theme-unicorn) | README with light/dark layout examples; demo opened but initial content did not render in the first capture | Separate cover, section, centered-text, and image layouts vary pace within a theme | Prism explores an original centered stage and chapter transition; upstream demo not counted as visually verified |

## Beyond slide engines

| Source | Inspected | Useful observation | Local decision |
|---|---|---|---|
| [Tremor Dashboard OSS](https://github.com/tremorlabs/template-dashboard-oss) | README; linked live preview failed with a connection error | A report should separate overview and detail; README identifies Next.js/Tremor and Apache 2.0 | Inspiration shortlist only; no claim of a visually verified demo, no dashboard runtime imported |
| [Tremor Blocks](https://github.com/tremorlabs/tremor-blocks) · [catalog](https://blocks.tremor.so/blocks) | README and official category catalog | Chart compositions, KPI cards, and tables are distinct report building blocks | Ledger includes a focused comparison and evidence table; avoids compressing an entire dashboard into one slide |
| [Carbon](https://github.com/carbon-design-system/carbon) · [data visualization](https://www.carbondesignsystem.com/building-blocks/data-visualization/overview) | Repository README and rendered official chart overview | Charts serve a specific communication intent and need readable labels | Ledger uses a simple zero-based comparison with explicit fictional values and a source note; no Carbon assets copied |
| [Broadsheet](https://github.com/jonajinga/broadsheet) | README and `src/assets/css/tokens.css` | Editorial hierarchy separates masthead, headlines, body, and utility labels | Dispatch uses an original publication-style cover and three-column briefing; no CMS or site infrastructure imported |
| [Sticky](https://github.com/hamzasaleem2/sticky) | Archived repository README and board screenshot | Spatial note grouping can organize discussion; README says later development moved private | Workshop uses static observation notes and an action worksheet. It is not a port of the collaboration app. The archived code is identified as MIT by its README |

## Provenance and reuse notes

- MIT license files were read for Neversink, Geist, Scholarly, Academic, Frontend Slides, and UoGSoE Marp themes. This is repository-level evidence, not a license audit of every transitive asset.
- My Marp Themes' README distinguishes the GPL-licensed `beam` theme from the rest of its MIT-licensed code; several themes also import Google Fonts. Blueprint does not copy those styles or fonts.
- Shower's README identifies MIT licensing. Purplin and Unicorn did not expose a file at the checked `LICENSE` path; their exact licensing must be resolved before copying their code. That lookup failure alone does not establish that the projects lack a license.
- The collection relies on local system font stacks. No network request is needed to play a template. Actual Chinese glyphs and line breaks can differ by operating system.
- A researched theme does not automatically become a new template. Keep a candidate only when it adds a useful composition or speaking context; avoid multiplying near-identical color variants.

## Next research directions

Look beyond presentation engines for open-source editorial, documentation, portfolio, and data-report layouts. Favor a clear content role that the current collection lacks, and retain source links and the observed reason for adopting or declining each direction. Validate new local implementations independently of upstream screenshots.

## Candidate queue — further inspection pending

These candidates were discovered after the first 13 templates. Inspection depth is recorded per entry; README claims and source inspection do not establish rendered quality or runtime correctness.

| Candidate | Evidence read | What to inspect next | Scope decision |
|---|---|---|---|
| [Tahta](https://github.com/zcag/tahta) | README, showcase and code-explain layout source, MIT license; see study below | Explorer showcase and reference pages inspected below; image sizing and other variants remain unverified | Reuse existing portfolio/code templates first; stepped explanations remain deferred |
| [Takahashi](https://github.com/kecrily/slidev-theme-takahashi) | Default/reverse Vue layouts, typography CSS, package metadata; see study below | Inspect rendered screenshots; resolve exact license before any copying | Use Monograph for short, type-led talks; no separate near-duplicate template |
| [Bento](https://github.com/nyblnet/bento) | MIT license, gallery asset source ledger, builder lines 1–150, live gallery, Terra cover and collection slide | Cabinet now implements the collection/detail direction with original CSS forms; inspect other gallery directions only if they add a distinct use | Product-series storytelling is a useful candidate; editor, collaboration, and self-updates remain out of scope |

## Milestone study — 2026-10-29

[Crimson Deck / noninsurance](https://github.com/alili/slidev-theme-noninsurance) was inspected beyond its README: [timeline.vue](https://github.com/alili/slidev-theme-noninsurance/blob/main/layouts/timeline.vue), the [timeline screenshot](https://github.com/alili/slidev-theme-noninsurance/blob/main/assets/08-timeline.png) rendered in a browser, and the [MIT license](https://github.com/alili/slidev-theme-noninsurance/blob/main/LICENSE) (copyright Bestony, 2026). The repository is a fork of `bestony/slidev-theme-bestony2026`.

The inspected layout separates time, stage headline, description, and status markers. Its screenshot uses a dark surface with amber completed stages. This supports a milestone storytelling direction; it does not validate the upstream application or all advertised layouts. Code-plus-explanation layouts remain uninspected.

Passage is an original static implementation: a vertical station cover, a three-stage map with visible status words, a decision record, and a next-checkpoint layout. It uses warm paper and a rust accent; no upstream source, fonts, images, or runtime were copied. Equal stage spacing is explicitly identified as schematic so it cannot be mistaken for duration or completion percentage. The screenshot is research evidence only and is not shipped in the gallery.

## Composition study — 2026-10-29, second follow-up

### Tahta: media fit and code explanations

Read [`showcase.vue`](https://github.com/zcag/tahta/blob/main/packages/theme/layouts/showcase.vue) (file SHA `848347edef3dde0953271dbd1ca060befa73de1b`) and [`code-explain.vue`](https://github.com/zcag/tahta/blob/main/packages/theme/layouts/code-explain.vue) (file SHA `a96bac4ce3a5ec01b76b41eb2e46281d6f9599e3`), alongside the repository [MIT license](https://github.com/zcag/tahta/blob/main/LICENSE), copyright Cagdas Salur, 2026.

- Showcase selects left/right media placement and supports `contain` or `cover`, defaulting to cover. This distinction matters when replacing Monograph's decorative exhibit with an actual screenshot: full UI evidence should remain uncropped; a deliberately cropped detail needs a caption identifying its scope.
- Code-explain pairs a code slot with notes and uses Slidev click state to emphasize the current note. The static layout is useful for Console. The click synchronization is coupled to Slidev navigation and is deferred here; a sequence of ordinary slides can preserve a one-key/one-slide interaction.
- These are source-level findings. The layout CSS, `Fit` behavior, live explorer, accessibility, and upstream test claims were not verified in this pass. No upstream implementation or assets were copied.

Decision: add practical selection/adaptation guidance to the existing collection. A separate theme is not justified by these two compositions alone. Reconsider after viewing the explorer if it reveals a distinct layout that supports a missing speaking context.

### Takahashi: sparse text rather than another visual theme

Read [`default.vue`](https://github.com/kecrily/slidev-theme-takahashi/blob/master/layouts/default.vue), [`reverse.vue`](https://github.com/kecrily/slidev-theme-takahashi/blob/master/layouts/reverse.vue), [`styles/layout.css`](https://github.com/kecrily/slidev-theme-takahashi/blob/master/styles/layout.css), and [`package.json`](https://github.com/kecrily/slidev-theme-takahashi/blob/master/package.json). The two layout files center their content; reverse adds a black background and white text. Typography utilities make headings much larger than paragraph text. This supports a sparse, one-thought-per-slide speaking style.

The checked root `LICENSE` path returned 404 and package metadata did not declare a license. This does not establish that the repository has no license; exact reuse permission remains unresolved. No source or assets were copied. Rendered screenshots and Chinese line wrapping remain unverified.

Decision: recommend Monograph's existing statement composition for short, type-led talks. Keep evidence-heavy explanations in Seminar or Ledger. A separate black/white centered theme would duplicate existing capability without enough additional value.

## Gallery and licensing study — 2026-10-29, third follow-up

### Bento: a product collection needs image-led compositions

Inspected the live [gallery](https://bento.page/), the [Terra template](https://bento.page/gallery/terra-premium-product.bento.html) cover in its editor, and slide 3/5 in presentation mode. Screenshots were viewed after the transition settled; the first capture during transition was blank and was not treated as a layout result. The other gallery directions were identified from the landing page, not individually validated.

Terra's cover combines a dominant product image with smaller detail images. Its collection slide uses three consistent image cards, each with a name and a small metadata row, beneath a single headline. This creates a collection-to-detail storytelling opportunity beyond the current single-exhibit Monograph layout. The example's brand, inventory, and prices are fictional (the builder explicitly identifies gallery content as fictional); they are not evidence about real museum objects or businesses.

Read the [MIT license](https://github.com/nyblnet/bento/blob/main/LICENSE), [`build-example-decks.mjs` lines 1–150](https://github.com/nyblnet/bento/blob/main/scripts/build-example-decks.mjs#L1-L150) (file SHA `f2cc02140e74a79516bf2c7127544c421bde3699`), and [`gallery-photos/SOURCES.md`](https://github.com/nyblnet/bento/blob/main/scripts/gallery-photos/SOURCES.md). The inspected builder embeds image/font assets and constructs slide elements; it was not executed. The asset ledger identifies NASA/Library of Congress public-domain material, Met CC0 objects, and OFL fonts. These are upstream provenance records, not an independent verification of every original asset's rights.

Decision: shortlist an original product-series layout with an overview, a collection comparison, and a detail/specification page. Use original local placeholder art until actual user assets are supplied, and label all sample specifications. No images, fonts, source code, app shell, morph engine, editor, or collaboration behavior were imported. Runtime, offline longevity, performance, and security claims in the upstream README were not audited.

### Removed from the open-source candidate queue: CushLabs

The [LICENSE](https://github.com/RCushmaniii/cushlabs-scrollytelling/blob/main/LICENSE), file SHA `1f25e3a0f6525e77ab62f795c0742b89d5a8542f`, identifies the project as proprietary portfolio demonstration material and explicitly disallows using its code as a project template or starting point. Public GitHub visibility does not make it an open-source template. The earlier README-only shortlist was provisional and is corrected here.

Decision: exclude this repository from reusable template research. Only its README and license were read; no implementation was copied, cloned, installed, or adapted. Do not spend subsequent rounds exploring its source for reuse. The README's performance and production-readiness claims are not adopted as verified findings.

## Local implementation: Cabinet — 2026-10-29

Cabinet translates the previously inspected Bento Terra collection-to-detail idea into four original static layouts: series cover, a three-work comparison, detail/specification view, and review prompts. The cool neutral gallery, CSS arch/disc/layered forms, and Chinese copy were authored locally. No upstream code, product images, fonts, prices, or runtime were used. The forms are explicitly labeled conceptual placeholders; specification fields request actual information rather than inventing measurements. This adds a multi-work collection composition alongside Monograph's single exhibit and Atelier's palette/case study.

## New-source screening — 2026-10-30

Searched GitHub repository metadata for infographic slide themes, MIT workshop presentation themes, and editorial portfolio templates. These queries produced the candidates below; search ranking is not a quality assessment.

| Source | Evidence inspected | Decision and next useful check |
|---|---|---|
| [present-now](https://github.com/Taimoorkhan1122/present-now) | README, root MIT license, [`template/src/head.html` lines 1–100](https://github.com/Taimoorkhan1122/present-now/blob/main/template/src/head.html#L1-L100), file SHA `05c8bf6928f990035f9931e9de32fb89091be7da` | The inspected source uses a 1600×900 canvas, system fonts, warm serif headings, grids, and cards. Those compositions substantially overlap Editorial and Swiss; no new palette variant. The before/after and card-detail interactions were subsequently inspected in the bounded live study below; further palette-only exploration is deferred. No installation, scripts, or agent workflow was adopted. |
| [cooked-folio](https://github.com/shahriaravi/cooked-folio) | README, root MIT license (copyright 2025 Shahriar Avi), repository file tree, [`ExperienceList.tsx`](https://github.com/shahriaravi/cooked-folio/blob/main/src/components/sections/ExperienceList.tsx), file SHA `fa0f47a734238ad52020037f814adbcd4a0cc95b` | The source separates date metadata from role, company, and description using a responsive two-column grid. The subsequent live inspection and original Profile implementation are recorded below. Its 11px metadata and 16px body are website sizes, not suitable deck defaults. Live presence, booking, audio feedback, analytics, and extension-blocking features are outside scope. |
| [Workshop Materials](https://github.com/experimental-software/workshop-materials) | README and repository search metadata (archived) | The README identifies Hugo workshop pages, Reveal.js presentations, and Codelabs-inspired tutorials. It also credits a CC BY 3.0 homepage layout, Font Awesome icons, fonts, and separately licensed dependencies; a root MIT label does not resolve those assets. The subsequent source inspection below found placeholder exercises and a tutorial navigation shell; defer template adoption. |

The cooked-folio README's `Projects.tsx` path returned 404; the actual tree uses `ProjectList.tsx`. Only `ExperienceList.tsx` was inspected in this pass. README paths should be checked against the current tree before reuse. No live demos, screenshots, upstream builds, or runtime claims were verified in this screening pass, and no code, assets, personal profile content, or third-party instructions were imported. The collection had 15 distinct templates at this screening stage; later implementation notes record additions.

### present-now live inspection — 2026-10-30

Viewed the [demo cover](https://taimoorkhan1122.github.io/present-now/demo/deck.html#1), [six-part anatomy slide](https://taimoorkhan1122.github.io/present-now/demo/deck.html#4), and [before/after slide](https://taimoorkhan1122.github.io/present-now/demo/deck.html#8) in a real browser. Captured and inspected the cover, selected anatomy detail, and After state. Clicking the context card changed the detail panel; clicking After changed the displayed code and outcome label. This verifies those two mouse interactions only, not the full 18-slide deck, keyboard accessibility, printing, or technical claims made by the example content.

The card/detail pattern keeps an overview visible while focusing on one concept. The before/after layout reuses the same code region to emphasize a change. Both could help a guided live demonstration, but add hidden states that a static screenshot or printout may omit. For this collection, retain Console's visible comparison and use separate slides for focused explanations; defer an interactive template until it has a distinct use and all states can be checked in navigation and print. No upstream layout, code, sample claims, or runtime was copied. The prior README-only status for these two interactions is superseded by this bounded observation.

## Local implementation: Profile — 2026-10-30

Read cooked-folio's [`Hero.tsx`](https://github.com/shahriaravi/cooked-folio/blob/main/src/components/sections/Hero.tsx) and [`site-config.ts`](https://github.com/shahriaravi/cooked-folio/blob/main/src/lib/site-config.ts), then followed the latter's public site URL to [shahriaravi.me](https://shahriaravi.me). Viewed its identity/role introduction and experience list, and clicked the first experience row. The live site shows expandable rows and a text-led hero, which differ from the previously inspected source's portrait/status treatment and static experience rows. The deployed revision was not established; these are separate observations, not proof the checked source reproduces the current site.

Profile is an original, static adaptation of the information hierarchy: name/role, dated experience, specific contribution, and a discussion/contact ending. The large green identity block and 1920×1080 compositions were written locally. All biography, dates, achievements, and contact fields are prompts; no real person's text, portrait, logo, or credentials were copied. No external services or expandable state were introduced. This adds a speaker/self-introduction use distinct from Passage's project milestones and Cabinet's product collection.

### Workshop Materials source inspection — 2026-10-30

Read the [root MIT license](https://github.com/experimental-software/workshop-materials/blob/master/LICENSE) (copyright Jan Mewes, 2021), [`layouts/tutorial/list.html`](https://github.com/experimental-software/workshop-materials/blob/master/layouts/tutorial/list.html) (file SHA `8a6bb1c53711c1438991046a9f2d45d708295377`), and the [`overview`](https://github.com/experimental-software/workshop-materials/blob/master/archetypes/tutorial/0_overview.md) and [`first-step`](https://github.com/experimental-software/workshop-materials/blob/master/archetypes/tutorial/1_step1.md) archetypes. The archetypes contain placeholder prose, not a worked exercise or a validated teaching sequence.

The layout builds a numbered table of contents, per-step content cards, and previous/start/continue/finish controls. It references CDN-hosted Bootstrap, jQuery, and Font Awesome alongside local styles, fonts, and medium-zoom. Consequently this source is a multi-resource tutorial shell, not a drop-in standalone/offline deck. Its README's third-party attribution distinctions still apply despite the root MIT license.

Decision: close this candidate's immediate implementation pass. Step numbering alone is already covered by Blueprint and Passage, while Workshop covers discussion-to-action. No distinct exercise composition was established from the inspected files. Do not create a new visual theme merely from this navigation shell. Revisit only if a concrete teaching example supplies a missing learner task and completion-check layout. No code, assets, dependencies, or instructions were copied or executed; no browser or build validation was performed for this upstream project.

## Two-period comparison study and Ledger expansion — 2026-10-30

Discovered [FT Visual Vocabulary templates](https://github.com/ft-interactive/visual-vocabulary-templates) and [Gramener's Vega edition](https://github.com/gramener/visual-vocabulary-vega) via GitHub search. Read both READMEs, FT's [slope guide](https://github.com/ft-interactive/visual-vocabulary-templates/blob/main/slope/README.md), and [`slopeChart.js` lines 1–150](https://github.com/ft-interactive/visual-vocabulary-templates/blob/main/slope/slopeChart.js#L1-L150) (file SHA `4d859a4bc0c917a130afcecc868fe2720c136221`). The source connects two scaled observations with endpoint circles and labels. FT's guide limits this simplification to stories that do not lose important intermediate changes.

FT's README identifies MIT licensing for software while explicitly excluding FT content and branding. Gramener's checked root `LICENSE` path returned 404; reuse permission for its code/assets remains unresolved. No upstream code, data, typography, icons, branding, or charting runtime was copied. These were source/documentation inspections, not rendered upstream tests.

Ledger now includes an original inline-SVG comparison as a fifth slide rather than a new near-duplicate theme. Both fictional series share a 0–100 score scale; direct labels and solid/dashed lines distinguish them. Sample values, endpoint-only interpretation, and replacement instructions are explicit. The existing bar chart and evidence table remain. Gallery page counts now come from actual HTML slide elements, so the five-page sample is accurately labeled.

## Scrolling stories and workshop preparation — 2026-10-30

GitHub searches for journalism scrollytelling and workshop facilitation surfaced two directions worth distinguishing from slide themes:

- [Cerchie/svelte-scrollytale](https://github.com/Cerchie/svelte-scrollytale): its README points back to The Pudding's starter. Followed that primary source and read [the starter README, lines 1–35](https://github.com/the-pudding/svelte-starter/blob/main/README.md), its [MIT license](https://github.com/the-pudding/svelte-starter/blob/main/LICENSE) (The Pudding, 2022), and the complete [`Scrolly.svelte`](https://github.com/the-pudding/svelte-starter/blob/main/src/components/helpers/Scrolly.svelte) (file SHA `20ae743e1451548733725d04136879236ff63a6d`). The component observes direct children and selects the one with the highest intersection ratio; it supplies a scroll-driven index, not a finished chart composition. The README separately restricts reproduction of The Pudding's logos and fonts. Defer a runtime port: the existing slide sequence can already present successive evidence states, and no distinct visual composition was established from this helper. Inspect an actual story's figure-and-caption composition before reconsidering; do not equate a starter's helper list with rendered design evidence.
- [CoMo preparation canvases](https://github.com/ddd-crew/como-prep-canvas): inspected the README introduction, audience/structure, scoping, planning sections 4.2–4.7, closing usage notes, and license declaration (README file SHA `6b49c8758c6b27727404f5502e103e22b7b399e1`). The documentation separates the participant-facing scope/agenda from facilitator preparation, and connects session planning with outputs and follow-up. It declares **CC BY-SA 4.0**, rather than MIT; no canvas image, wording, or layout was imported into this MIT collection. This is a preparation resource, not evidence of a new presentation style. A subsequent browser inspection of the repository’s [planning canvas image](https://github.com/ddd-crew/como-prep-canvas/blob/main/resources/workshop-planning-and-design.jpg) on 2026-10-30 showed a large fill-in worksheet: a main grid for scope, success, agenda, people, methods, and tools, plus a separate optional-fields column. At fit-to-window size the explanatory text is very small. This is useful facilitator working material, but does not establish a missing participant-facing slide composition. Keep Workshop’s existing observation/action pages; close the immediate visual-inspection queue for this canvas. Only the static image was inspected, not a Miro board or collaborative workflow.

These were documentation and source inspections only: no upstream application was installed, run, or browser-validated. Search also returned `varunvash/Scrollytelling1`, but its checked root `README.md` returned 404; no design or license conclusion was drawn from that result. No bundled HTML, catalog, or previews changed in this pass, so prior browser checks remain historical evidence rather than a new visual-validation claim.


## Tahta explorer and Console reference appendix — 2026-10-30

Opened the [live explorer](https://tahta.cagdas.io/) and its gallery overview, then inspected settled full-slide screenshots of [Showcase, page 18](https://tahta.cagdas.io/gallery/#/18) and [Reference, page 31](https://tahta.cagdas.io/gallery/#/31). Early captures still showed the overview/transition and were discarded as evidence of the target slide. Showcase displayed a left text region with an empty dark right region in this session; this does not verify image rendering or sizing, nor establish the cause of the missing image. Other variants, the full 37-page deck, and upstream accessibility claims were not validated.

The reference page presents two labeled groups of term/description rows with rules separating entries. Read [`reference.vue`](https://github.com/zcag/tahta/blob/main/packages/theme/layouts/reference.vue) (file SHA `af58536b0e0e3d3b52e0c6e28fec1d399f8cc2ae`): it accepts grouped or flat item data inside the theme's frame and Fit components. The repository MIT license was checked in the earlier study; no source, font, screenshot, or sample command was copied.

Console now adds an original fifth-page reference appendix using semantic `dl`/`dt`/`dd` markup, two groups, and six short definitions tied to its existing pseudocode. It explicitly distinguishes these terms from executable commands. This adds a useful technical-talk handout composition without another visual theme. All five pages passed four-viewport checks, navigation after clicking controls, persistence, and print-media visibility; laptop/projector screenshots were inspected. Cover preview, catalog, gallery page count, and replacement guide were updated.

## Posterdown and Penguin source screening — 2026-10-30

GitHub repository searches surfaced two additional sources. Neither was installed or copied. The initial source-only screening was followed by the bounded Posterdown image inspection recorded below.

| Source and inspected scope | Finding and decision |
|---|---|
| [Posterdown](https://github.com/brentthorne/posterdown): README, `DESCRIPTION`, `LICENSE`, Betterland [`template.html` lines 1–285](https://github.com/brentthorne/posterdown/blob/master/inst/rmarkdown/templates/posterdown_betterland/resources/template.html) (file SHA `40f5efb5cc2c67096683b3ef1abed23dca22befc`), and [`skeleton.Rmd` lines 1–85](https://github.com/brentthorne/posterdown/blob/master/inst/rmarkdown/templates/posterdown_betterland/skeleton/skeleton.Rmd) | The landscape poster reserves its central half for a main finding, with supporting material in outside columns. Its default 46×32-inch print canvas, dense supporting text, CDN icon/font links, and non-self-contained sample output require adaptation rather than a direct deck port. `DESCRIPTION` declares MIT plus the license file, whose copyright record names William Brent Thorne (2019); third-party fonts/assets were not audited. Follow-up on 2026-10-30: opened the repository’s [Betterland sample image](https://github.com/brentthorne/posterdown/blob/master/images/betterland_july2019-1.png) in a real browser and inspected its fit-to-window screenshot. The central claim dominates; the narrow side columns contain methods, two plots, a table, and references that become very small at laptop size. This supports separating the main statement and detailed evidence across existing Monograph/Seminar slides, rather than adding a dense poster theme. Close the immediate inspection queue for this sample. This verifies only the supplied static image, not a local R build, HTML runtime, or print output. |
| [Penguin](https://github.com/alvarosabu/slidev-theme-penguin): README lines 1–180, [`text-window.vue`](https://github.com/alvarosabu/slidev-theme-penguin/blob/main/layouts/text-window.vue) (file SHA `97e62cb7b96fe5c71697a82e67db6e2c7de6ea17`), and `package.json` | The source pairs prose with a console window in two columns and supports reversing their order, with a decorative zigzag behind the window. This substantially overlaps Console's existing code/explanation page. Package metadata declares MIT, but the checked root `LICENSE` path returned 404; exact license text and font permissions remain unresolved for copying. Inter, Gilroy, and Fira Code are configured font names, not proof of redistribution rights. Defer this direction unless live inspection reveals a distinct composition; no dependency or branding imported. |

These findings extend the screening record only. The collection remains 16 templates / 66 sample pages; catalog and previews are unchanged. Follow-up screenshots cover upstream static reference images only; bundled deck browser checks were not rerun for these documentation edits.

## Mixed-aspect photo galleries — 2026-10-30

GitHub search surfaced [Nico Kaiser's Hugo Gallery](https://github.com/nicokaiser/hugo-theme-gallery). Read README lines 1–135, the MIT license (copyright 2023–2025 Nico Kaiser), [`gallery.html`](https://github.com/nicokaiser/hugo-theme-gallery/blob/main/layouts/partials/gallery.html) (file SHA `e07080d810fff43981078e8631b28a40523116a8`), [`gallery.js`](https://github.com/nicokaiser/hugo-theme-gallery/blob/main/assets/js/gallery.js) (file SHA `d04993c76f15495c5d66166caacc399502944cd8`), and the example site's README.

The HTML preserves each thumbnail's width/height ratio, takes its description from image metadata or front matter, and supplies separate full-image dimensions to a lightbox. The script computes justified rows from those aspect ratios and container width. This is a potentially useful direction for photographic essays with mixed portrait/landscape work, rather than Cabinet's equal-size product cards. Follow-up on 2026-10-30: opened the live [home page](https://nicokaiser.github.io/hugo-theme-gallery/) and [Nature album](https://nicokaiser.github.io/hugo-theme-gallery/nature/), inspected the album and first lightbox screenshots, and clicked Next to confirm its counter changed from 1/9 to 2/9. The album uses closely spaced mixed-aspect rows under a centered introduction. No per-image descriptive caption was visible in the inspected first-image lightbox; this does not establish whether other albums supply captions. These observations verify a limited browsing path, not all images, mobile behavior, accessibility, or a fixed-canvas composition. Close the immediate live-inspection queue and defer a new theme until a bounded image sequence demonstrates a presentation story; an album alone is not sufficient.

The example README downloads images from Unsplash. The theme's MIT license is not evidence of blanket permission for those photographs; no photos, source, lightbox, or layout engine were imported, and the download/install scripts were not run. Any future offline photo-essay adaptation should use original or authorized local images, an explicit narrative order, and visible captions rather than depending on a lightbox to explain the evidence. The existing template gallery has uniformly 16:9 covers, so it does not need justified-row layout.

## Academic blocks and multi-view design sheets — 2026-10-30

- [Frankfurt](https://github.com/MuTsunTsai/slidev-theme-frankfurt): read README, MIT license (Mu-Tsun Tsai, 2023–2025), and [`Item.vue`](https://github.com/MuTsunTsai/slidev-theme-frankfurt/blob/main/components/Item.vue) (file SHA `55e6a035e879bdd45015f380688fcc8288d0995f`). Its academic block is an optional title followed by a content slot; the README also describes section/progress navigation. The block alone overlaps Seminar's existing evidence/hypothesis structures. No CSS or navigation implementation was inspected, and no rendered quality or accessibility conclusion follows from this small component. Defer a separate theme; investigate section navigation only if a longer-deck use case makes it useful.
- [Editorial Portfolio Template](https://github.com/linsensjob-ola/editorial-portfolio-template): read README lines 1–130, MIT license (Portfolio Template Contributors, 2026), and [`characterBuildData.js`](https://github.com/linsensjob-ola/editorial-portfolio-template/blob/main/src/data/characterBuildData.js) (file SHA `a07dd0842ff3bed7601fe1416a48eb4e726e9bcc`). The data defines front/side/back views of one character, plus a turntable video. This suggests a potentially distinct **same-object multi-view sheet**, unlike Cabinet's comparison of separate works. However, the supplied views alternate only two generic placeholder SVGs; they do not establish consistent geometry or a finished character study. Keep this as a candidate for actual component/render inspection before implementation. The README's originality and test claims were not independently validated.

No code, artwork, fonts, biography, or runtime from either source was copied or executed. These are source-screening findings, not new bundled templates or browser-validation results.
