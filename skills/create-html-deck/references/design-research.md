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

## Candidate queue — README reviewed, implementation deferred

These candidates were discovered after the first 13 templates. Reading their README is not proof of build quality, visual correctness, or every advertised capability.

| Candidate | Evidence read | What to inspect next | Scope decision |
|---|---|---|---|
| [Tahta](https://github.com/zcag/tahta) | README describes a token-based layout library and variants; links a live explorer | Compare its timeline, feature, and showcase compositions in the actual explorer | Look for a missing composition; do not import the design-system runtime |
| [Crimson Deck / noninsurance](https://github.com/alili/slidev-theme-noninsurance) | README documents a 1920×1080 canvas and timeline/code/chart layouts | Inspect timeline and code-plus-explanation screenshots, then check source structure | Potential milestone-story direction; avoid another generic dark recolor |
| [Takahashi](https://github.com/kecrily/slidev-theme-takahashi) | README exposes default/reverse layouts and screenshot links | Inspect large-type pacing and contrast in the screenshots | Potential lightning-talk template with intentionally very little text |
| [Bento](https://github.com/nyblnet/bento) | README describes single-file decks and links its gallery | Inspect designed gallery examples for useful compositions | Editor, collaboration, and self-updates are outside this template expansion |
| [CushLabs Scrollytelling](https://github.com/RCushmaniii/cushlabs-scrollytelling) | README describes scroll-driven narration and presentation/browse modes | Examine narrative pacing only if it offers a useful fixed-slide translation | Do not add scroll locking, audio autoplay, or a second presentation engine |
