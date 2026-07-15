---
name: create-html-deck
description: Create, edit, and verify polished browser-native HTML slide decks. Use when the user asks for an HTML presentation, browser-based PPT, weekly-share deck, technical talk, or a slide deck that must display safely on laptops and 16:9 projectors.
---

# Create HTML Deck

Build a complete local HTML presentation with a fixed 1920×1080 design canvas, responsive viewport fitting, keyboard navigation, portable assets, and evidence-based visual verification.

## Preserve the output contract

- Deliver a presentation, not a long document broken into pages. Make each slide legible in a few seconds and useful while someone is speaking.
- Treat supplied notes, screenshots, specs, handoffs, and existing decks as source material. Do not ask again for facts already present there.
- Ask only when a missing choice would materially change the audience, story, brand, or delivery format. Otherwise state the assumption and proceed.
- Produce working HTML and assets. Do not stop at an outline, mockup screenshot, or design recommendation unless the user requested only that stage.
- Keep claims honest and source links recoverable. Mark uncertain or draft content instead of polishing it into a false fact.

## Choose the path

- For a new deck, copy `assets/deck-template.html` into the requested output location and replace its sample content.
- For an existing deck, inspect its HTML, CSS, JavaScript, images, and current screenshots before editing. Preserve its visual language unless the user asks for a redesign.
- If the user explicitly requires `.pptx`, use a PowerPoint-specific skill instead. Do not rename HTML to `.pptx`.

## Build the story first

1. Identify the audience, speaking time, central claim, source material, and desired ending.
2. Write a one-sentence narrative spine: problem → change → evidence → conclusion. Let every slide advance it.
3. Give each slide one job. Prefer a claim, comparison, sequence, demonstration, or decision over a topic label.
4. Keep slides sparse enough to present aloud. Move explanation into the speaker's delivery rather than shrinking text.
5. Use supplied screenshots and diagrams as evidence, not decoration. Crop them around the point being discussed and keep source links clickable when appropriate.
6. Do not invent metrics, quotes, product capabilities, or external claims. Verify unstable claims before placing them in the deck.

Before implementation, create a compact slide map with the slide number, claim, evidence, and intended visual form. Do not turn that map into a separate deliverable unless it helps the user review the story.

## Define one visual system

Choose and reuse a small system across the deck:

- two type roles and a deliberate scale
- one neutral surface family plus one primary accent
- one layout grid and consistent outer margins
- a limited vocabulary for rules, labels, cards, diagrams, and image frames
- a clear posture for corners, borders, shadows, and motion

Vary composition to support the story, not to prove that every slide is different. Avoid endless equal card grids, decorative charts, stock-photo heroes, vague icons, and gradients that carry no meaning. Prefer typography, contrast, alignment, and interruption as the main hierarchy tools.

## Preserve the presentation contract

Use these defaults unless the existing deck has an intentional alternative:

- 1920×1080 fixed design canvas
- one self-contained HTML file plus a sibling `assets/` directory
- no remote runtime dependency unless explicitly justified
- keyboard navigation with Arrow keys, Home, End, Page Up, and Page Down
- visible current/total slide count
- localStorage persistence for the current slide
- print rules that expose every slide
- 44px minimum hit targets for controls
- 24px or larger body text on the design canvas

For small screens, center and scale the canvas with this geometry:

```css
.stage { position: relative; width: 100%; height: 100%; overflow: hidden; }
.deck { position: absolute; left: 50%; top: 50%; width: 1920px; height: 1080px; }
```

```js
const scale = Math.min(window.innerWidth / 1920, window.innerHeight / 1080);
deck.style.transform = `translate(-50%, -50%) scale(${scale})`;
```

Do not rely on `display: grid; place-items: center` plus `scale(...)` for a fixed-width deck. The unscaled layout box can overflow a laptop viewport and clip one side.

## Use assets portably

- Store local images under a sibling `assets/` directory and reference them with relative paths.
- Copy the HTML and its assets together when making a desktop or shareable copy.
- Add meaningful `alt` text.
- Avoid embedding large screenshots as base64 unless a single-file deliverable is explicitly required.

## Implement the complete deck

- Start from the bundled template for a new standalone deck, then replace every sample title, footer, and placeholder.
- Keep navigation state in one small controller and derive the counter from the actual slide list.
- Make previous/next controls operable with mouse, keyboard, and touch-sized hit targets.
- Add meaningful document and slide titles. Use semantic headings, `aria-hidden` for inactive slides, and visible focus states.
- Respect `prefers-reduced-motion`. Keep transitions short and functional.
- Preserve the user's existing design language when editing a deck unless a redesign was requested.
- Keep the console clean. Remove abandoned styles, unused sample assets, and unreachable slides before delivery.

## Verify before delivery

Run the portable structural check:

```bash
python3 <skill-dir>/scripts/check_deck.py /absolute/path/to/deck.html
```

Then open the deck in a real browser and inspect it. At minimum test:

| Viewport | Purpose |
|---|---|
| 1512×982 | 14-inch MacBook full screen |
| 1512×850 | 14-inch MacBook browser window |
| 1366×768 | smaller laptop |
| 1920×1080 | standard projector |

For every viewport, confirm:

- the deck rectangle stays fully inside the viewport
- no document scrollbar appears
- first and last slides render correctly
- every local image has a non-zero natural size
- keyboard navigation reaches every slide and stops at both ends
- the slide counter matches the actual slide count
- the browser reports no console or page errors
- controls remain large enough to use without covering important content
- text remains readable at normal laptop viewing distance

Inspect screenshots at laptop and projector sizes when visual quality matters. A passing DOM check does not prove that line breaks, density, or image crops look good.

If the deck contains a critical screenshot, diagram, hover explanation, or embedded link, exercise it explicitly. If external assets are unavoidable, test the deck once with normal network access and state that dependency in the handoff.

## Deliver

Return the exact HTML path and, when present, the containing folder that must travel with it. State the slide count, the viewports actually tested, and any remaining remote dependency or browser caveat. If a desktop copy was requested, synchronize it only after the source version passes verification.
