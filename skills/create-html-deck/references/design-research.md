# Open-source design research

Reviewed 2026-10-29. This is a design-source notebook, not a ranking or a claim that every upstream project has been installed or tested. The bundled templates use original CSS, artwork, and sample copy. No upstream theme code, photos, logos, or fonts are redistributed.

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
| [Bento](https://github.com/nyblnet/bento) | MIT license, gallery asset source ledger, builder lines 1–150, live gallery, Terra cover and collection slide | Develop an original collection/detail layout with local placeholder art; validate independently | Product-series storytelling is a useful candidate; editor, collaboration, and self-updates remain out of scope |

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
