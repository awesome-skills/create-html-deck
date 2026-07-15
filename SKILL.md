---
name: create-html-deck
description: Create, edit, and verify polished browser-native HTML slide decks. Use when the user asks for an HTML presentation, browser-based PPT, weekly-share deck, technical talk, or a slide deck that must display safely on laptops and 16:9 projectors.
---

# Create HTML Deck

Build a complete local HTML presentation with a fixed 1920×1080 design canvas, responsive viewport fitting, keyboard navigation, and evidence-based visual verification.

## Choose the path

- For a new deck, copy `assets/deck-template.html` into the requested output location and replace its sample content.
- For an existing deck, inspect its HTML, CSS, JavaScript, images, and current screenshots before editing. Preserve its visual language unless the user asks for a redesign.
- If the user explicitly requires `.pptx`, use a PowerPoint-specific skill instead. Do not rename HTML to `.pptx`.

## Build the story first

1. Identify the audience, speaking time, central claim, source material, and desired ending.
2. Give each slide one job. Prefer a claim, comparison, sequence, or example over a topic label.
3. Keep slides sparse enough to present aloud. Move explanation into the speaker's delivery rather than shrinking text.
4. Use supplied screenshots and diagrams as evidence, not decoration. Keep source links clickable when appropriate.
5. Do not invent metrics, quotes, product capabilities, or external claims. Verify unstable claims before placing them in the deck.

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

Inspect screenshots at laptop and projector sizes when visual quality matters. A passing DOM check does not prove that line breaks, density, or image crops look good.

## Deliver

Return the exact HTML path and, when present, the containing folder that must travel with it. State the viewports actually tested. If a desktop copy was requested, synchronize it only after the source version passes verification.
