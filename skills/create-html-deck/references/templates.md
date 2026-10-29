# Template collection

For a new deck, choose by audience and content, then copy the selected HTML. Each file is a self-contained, four-slide starting point with inline CSS/JS and system fonts. Open `assets/templates/index.html` for visual previews. The original `assets/deck-template.html` remains the minimal two-slide starter.

| Template | Good fit | Compositions | Main adjustments |
|---|---|---|---|
| `assets/templates/editorial.html` | Research, essays, retrospectives | Typographic cover, evidence split, statement, closing | Serif heading stack, paper surface, rust accent |
| `assets/templates/nocturne.html` | Technical demos, product launches | Signal cover, workflow panel, three-step proof, closing | Dark surface, lime accent, monospace labels |
| `assets/templates/swiss.html` | Proposals, strategy, structured talks | Numbered poster, agenda rows, comparison, decision | Strong grid, red accent, heavy sans-serif headings |
| `assets/templates/atelier.html` | Design reviews, portfolios, creative work | Abstract cover, palette, case study, closing | Warm neutrals, organic shapes, serif headings |

Replace all sample content, including document/slide titles, headers, footers, and labels. The statement in Editorial is original sample copy, not an attributed quotation. The workflow and portfolio panels are placeholders, not evidence of real results. Replace decorative CSS art with actual project evidence when appropriate. Keep footer content clear of the fixed controls.

Customize the `:root` tokens and theme-layout CSS near the end of the style block. Duplicate or remove `<article class="slide">` sections for the story; update static footer page markers to match. The navigation counter derives its total from the slide list. Copying only the selected HTML is sufficient until you add local assets. System fonts vary across machines; recheck Chinese line breaks on the presentation device.

Run `scripts/check_deck.py` on the resulting deck and follow the browser verification in SKILL.md. Screenshots in the gallery show the bundled sample covers; regenerate them if those covers change.

## Design research / 2026-10-29

These are discovery and design references, not bundled dependencies or imported themes. The four templates contain original CSS compositions and sample copy; no third-party theme code, fonts, photography, logos, or screenshots are redistributed.

| Source | Observation used | Local interpretation |
|---|---|---|
| [Slidev official themes](https://github.com/slidevjs/themes), [theme gallery](https://sli.dev/resources/theme-gallery) | Seriph offers a formal serif direction; Apple Basic demonstrates restrained black/white presentation styling | Editorial separates serif statements from utility labels; Nocturne uses sparse, high-contrast content |
| [Reveal.js themes](https://revealjs.com/themes/), [repository](https://github.com/hakimel/reveal.js) | Distinct light, dark, serif, and accent palettes can share one presentation runtime | Four standalone visual systems retain this project's fixed canvas and controls |
| [Awesome-Marp](https://github.com/favourhong/Awesome-Marp) | A browsable presentation-theme collection makes selection easier | A local gallery pairs cover previews with intended use and playable examples |

Swiss grid and Atelier's geometric artwork are original explorations of familiar editorial and studio-design conventions, not ports of a named upstream theme. If you later copy third-party code or assets, check that source's license and preserve the required attribution separately.
