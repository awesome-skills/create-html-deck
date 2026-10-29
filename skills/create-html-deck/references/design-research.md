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
| [Tahta](https://github.com/zcag/tahta) | README, showcase and code-explain layout source, MIT license; see study below | Inspect actual explorer and layout CSS before evaluating typography or image sizing | Reuse existing portfolio/code templates first; stepped explanations remain deferred |
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
| [present-now](https://github.com/Taimoorkhan1122/present-now) | README, root MIT license, [`template/src/head.html` lines 1–100](https://github.com/Taimoorkhan1122/present-now/blob/main/template/src/head.html#L1-L100), file SHA `05c8bf6928f990035f9931e9de32fb89091be7da` | The inspected source uses a 1600×900 canvas, system fonts, warm serif headings, grids, and cards. Those compositions substantially overlap Editorial and Swiss; no new palette variant. The README's before/after and workshop interactions may warrant a future demo inspection, but their behavior was not tested. No installation, scripts, or agent workflow was adopted. |
| [cooked-folio](https://github.com/shahriaravi/cooked-folio) | README, root MIT license (copyright 2025 Shahriar Avi), repository file tree, [`ExperienceList.tsx`](https://github.com/shahriaravi/cooked-folio/blob/main/src/components/sections/ExperienceList.tsx), file SHA `fa0f47a734238ad52020037f814adbcd4a0cc95b` | The source separates date metadata from role, company, and description using a responsive two-column grid. A speaker profile or career narrative is a possible missing use; inspect the rendered composition before deciding to implement. Its 11px metadata and 16px body are website sizes, not suitable deck defaults. Live presence, booking, audio feedback, analytics, and extension-blocking features are outside scope. |
| [Workshop Materials](https://github.com/experimental-software/workshop-materials) | README and repository search metadata (archived) | The README identifies Hugo workshop pages, Reveal.js presentations, and Codelabs-inspired tutorials. It also credits a CC BY 3.0 homepage layout, Font Awesome icons, fonts, and separately licensed dependencies; a root MIT label does not resolve those assets. Defer copying and theme adoption. Inspect an exercise page only if it can contribute a distinct task/input/checkpoint composition beyond Workshop. |

The cooked-folio README's `Projects.tsx` path returned 404; the actual tree uses `ProjectList.tsx`. Only `ExperienceList.tsx` was inspected in this pass. README paths should be checked against the current tree before reuse. No live demos, screenshots, upstream builds, or runtime claims were verified in this screening pass, and no code, assets, personal profile content, or third-party instructions were imported. The collection remains at 15 distinct templates.

### present-now live inspection — 2026-10-30

Viewed the [demo cover](https://taimoorkhan1122.github.io/present-now/demo/deck.html#1), [six-part anatomy slide](https://taimoorkhan1122.github.io/present-now/demo/deck.html#4), and [before/after slide](https://taimoorkhan1122.github.io/present-now/demo/deck.html#8) in a real browser. Captured and inspected the cover, selected anatomy detail, and After state. Clicking the context card changed the detail panel; clicking After changed the displayed code and outcome label. This verifies those two mouse interactions only, not the full 18-slide deck, keyboard accessibility, printing, or technical claims made by the example content.

The card/detail pattern keeps an overview visible while focusing on one concept. The before/after layout reuses the same code region to emphasize a change. Both could help a guided live demonstration, but add hidden states that a static screenshot or printout may omit. For this collection, retain Console's visible comparison and use separate slides for focused explanations; defer an interactive template until it has a distinct use and all states can be checked in navigation and print. No upstream layout, code, sample claims, or runtime was copied. The prior README-only status for these two interactions is superseded by this bounded observation.

## Local implementation: Profile — 2026-10-30

Read cooked-folio's [`Hero.tsx`](https://github.com/shahriaravi/cooked-folio/blob/main/src/components/sections/Hero.tsx) and [`site-config.ts`](https://github.com/shahriaravi/cooked-folio/blob/main/src/lib/site-config.ts), then followed the latter's public site URL to [shahriaravi.me](https://shahriaravi.me). Viewed its identity/role introduction and experience list, and clicked the first experience row. The live site shows expandable rows and a text-led hero, which differ from the previously inspected source's portrait/status treatment and static experience rows. The deployed revision was not established; these are separate observations, not proof the checked source reproduces the current site.

Profile is an original, static adaptation of the information hierarchy: name/role, dated experience, specific contribution, and a discussion/contact ending. The large green identity block and 1920×1080 compositions were written locally. All biography, dates, achievements, and contact fields are prompts; no real person's text, portrait, logo, or credentials were copied. No external services or expandable state were introduced. This adds a speaker/self-introduction use distinct from Passage's project milestones and Cabinet's product collection.
