# Template collection

For a new deck, choose by audience and content, then copy the selected HTML. Each file is a self-contained, four-slide starting point with inline CSS/JS and system fonts. Open `assets/templates/index.html` for visual previews. The original `assets/deck-template.html` remains the minimal two-slide starter.

| Template | Good fit | Compositions | Main adjustments |
|---|---|---|---|
| `assets/templates/editorial.html` | Research, essays, retrospectives | Typographic cover, evidence split, statement, closing | Serif heading stack, paper surface, rust accent |
| `assets/templates/nocturne.html` | Technical demos, product launches | Signal cover, workflow panel, three-step proof, closing | Dark surface, lime accent, monospace labels |
| `assets/templates/swiss.html` | Proposals, strategy, structured talks | Numbered poster, agenda rows, comparison, decision | Strong grid, red accent, heavy sans-serif headings |
| `assets/templates/atelier.html` | Design reviews, portfolios, creative work | Abstract cover, palette, case study, closing | Warm neutrals, organic shapes, serif headings |
| `assets/templates/blueprint.html` | System explanations, engineering plans | Grid cover, boundary panel, process, next action | Blue graph paper, linework, monospace labels |
| `assets/templates/seminar.html` | Paper talks, research updates | Research question, hypothesis, evidence table, limits | Serif headings, blue rail, visible source lines |
| `assets/templates/poster.html` | Workshops, events, creative proposals | Poster cover, bold tiles, statement, call to action | Pink/lime/violet, hard shadows, heavy typography |
| `assets/templates/prism.html` | Product launches, vision talks | Centered stage, value split, chapter, closing | Dark indigo, soft light, restrained glass panels |
| `assets/templates/console.html` | Code walkthroughs, engineering changes | Terminal cover, pseudocode, diff, verification | Monospace, amber, dark neutral surfaces |
| `assets/templates/monograph.html` | Portfolios, brand studies, ideas | Type-led cover, exhibit, statement, closing | Black/white, generous whitespace, large type |
| `assets/templates/workshop.html` | Workshops, retrospectives, team sessions | Sticky-note cover, observations, action worksheet, closing | Dotted board, soft yellow/blue/pink notes |
| `assets/templates/ledger.html` | Data briefs, business reviews | Report cover, sample bar chart, evidence table, decision | Cool neutrals, blue bars, visible scope/source notes |
| `assets/templates/dispatch.html` | Weekly updates, editorial narratives | Masthead, three columns, editorial statement, follow-up | Newsprint, serif type, double rules |
| `assets/templates/passage.html` | Milestone reviews, roadmaps, project history | Station cover, stage map, decision record, checkpoint | Warm paper, route markers, explicit status labels |
| `assets/templates/cabinet.html` | Product series, collections, design reviews | Series cover, collection cards, detail/specifications, review | Cool gallery surfaces, original CSS forms, consistent captions |
| `assets/templates/profile.html` | Speaker introductions, personal profiles, team introductions | Name card, experience rows, contribution comparison, contact | Deep green identity block, date column, explicit role boundaries |

## Choose by the story you need to tell

| Story | Start with | Adaptation |
|---|---|---|
| A short talk with one thought per slide | Monograph | Repeat the statement composition with short phrases; keep detailed evidence on separate slides rather than shrinking the type |
| Compare a series of works | Cabinet | Replace all three CSS forms with actual works; keep comparable captions and specification fields |
| A product or portfolio walkthrough | Monograph or Atelier | Replace the decorative exhibit with real work; keep screenshot text legible and the relevant UI intact |
| Explain a small code change | Console | Pair a short excerpt with its explanation; use successive slides when the explanation needs steps |
| Explain how a project changed direction | Passage | Put the original judgment, new evidence, and revised decision together; label stages with actual status and dates |
| Report what changed in the data | Ledger | Keep comparison scale, unit, period, and source explicit; separate observation from possible explanation |
| Work toward a shared next action | Workshop | Collect observations, then fill in the action worksheet with an owner and review time |

For screenshots, use a local `<img>` with meaningful `alt` text and `object-fit: contain` when the full interface is evidence. Use `cover` only for an intentional crop, and label what the crop shows. Remove the original decorative pseudo-elements when replacing a CSS exhibit; do not leave them over the screenshot. Check readability at the smallest target viewport after adding actual images.

For code walkthroughs, keep the code and its explanation visible together. Duplicate a slide to explain the next excerpt instead of adding a second click-to-reveal state machine. Update footer page markers after duplicating slides. These are authoring recommendations, not additional implemented layout modes or an upstream theme port.

Replace all sample content, including document/slide titles, headers, footers, and labels. The statement in Editorial is original sample copy, not an attributed quotation. The workflow and portfolio panels are placeholders, not evidence of real results. Replace decorative CSS art with actual project evidence when appropriate. Keep footer content clear of the fixed controls.

Ledger contains explicitly fictional example values (12, 18, 24) on a zero-based 0–24 scale. When replacing them, update bar widths, tick labels, units, accessible chart description, and source text together. Workshop is a presentation layout, not a collaborative or draggable whiteboard.

Passage uses equally spaced stages, not a proportional time axis or progress meter. Replace sample status words and marker classes (`done`, `current`, or neither) together; retain text labels so status does not depend on color. Replace dates, evidence, owners, and checkpoint criteria with actual project content.

Cabinet uses original decorative CSS forms, not product photographs or measured geometry. Replace the entire `.object` element with the actual image rather than leaving its pseudo-elements in place. Keep image descriptions, work names, captions, dimensions, materials, and evidence consistent; remove the sample labels only after inserting real content.

Profile contains prompts rather than a fictional biography. Replace the name, role, date ranges, contribution descriptions, and contact fields together. If replacing the name mark with a portrait, use an authorized local image and meaningful alt text. Keep personal contributions distinct from team outcomes and leave unverified claims out.

Customize the `:root` tokens and theme-layout CSS near the end of the style block. Duplicate or remove `<article class="slide">` sections for the story; update static footer page markers to match. The navigation counter derives its total from the slide list. Copying only the selected HTML is sufficient until you add local assets. System fonts vary across machines; recheck Chinese line breaks on the presentation device.

Run `scripts/check_deck.py` on the resulting deck and follow the browser verification in SKILL.md. Screenshots in the gallery show the bundled sample covers; regenerate them if those covers change.

## Design research

See [design-research.md](design-research.md) for inspected open-source projects, adopted design ideas, deferred candidates, and reuse notes. The templates are original implementations rather than ports of upstream themes.

## Maintaining the gallery

Add the standalone HTML and its metadata in `assets/templates/catalog.json`, then run:

```bash
python3 <skill-dir>/scripts/build_gallery.py
```

The gallery is static HTML with a small inline filter controller. It works from `file://` without fetching the catalog. The catalog is only an authoring input. Generate a cover screenshot under `assets/templates/previews/<slug>.png` before publishing gallery changes.

For collection-wide browser verification, `scripts/verify_templates.mjs` exports `verifyTemplates(task, options)` for an existing ego-browser TaskSpace. Read the installed ego-browser guide first; the caller owns the TaskSpace lifecycle and local HTTP server. Serve the repository root, then import the verifier in an ego-browser script:

```js
const { verifyTemplates } = await import('file:///absolute/skill-dir/scripts/verify_templates.mjs');
await verifyTemplates(task, {
  baseURL: 'http://127.0.0.1:8765/skills/create-html-deck/assets/templates',
  slugs: ['editorial', 'nocturne'],
  outputDir: '/absolute/temporary/qa-output',
  previewDir: '/absolute/skill-dir/assets/templates/previews', // optional
});
```

This checks all slides at the four required viewports, keyboard/button navigation, persistence, page bounds, text overflow, uncaught page errors, and print visibility. It captures laptop/projector screenshots for human inspection. It does not prove visual quality or validate physical printing. The screenshot pass disables the slide fade only for deterministic captures.
