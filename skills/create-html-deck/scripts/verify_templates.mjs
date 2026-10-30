/** Run with an existing ego-browser TaskSpace; see references/templates.md.
 * The caller owns the browser lifecycle and local HTTP server.
 */
import { mkdir, writeFile } from 'node:fs/promises';
import { join } from 'node:path';

export async function verifyTemplates(task, { baseURL, slugs, outputDir, previewDir }) {
  const page = task.page('p1');
  const results = [];
  await mkdir(outputDir, { recursive: true });
  const hook = await page.cdp('Page.addScriptToEvaluateOnNewDocument', {
    source: `window.__deckErrors = [];
      window.addEventListener('error', event => window.__deckErrors.push(event.message));
      window.addEventListener('unhandledrejection', event => window.__deckErrors.push(String(event.reason)));`,
  });
  try {
    for (const slug of slugs) {
      await page.goto(`${baseURL}/${slug}.html`);
      // Disable only the presentation fade to make per-slide captures deterministic.
      await page.evaluate(() => document.querySelectorAll('.slide').forEach(slide => { slide.style.transition = 'none'; }));
      const count = await page.evaluate(() => document.querySelectorAll('.slide').length);
      for (const [width, height] of [[1512, 982], [1512, 850], [1366, 768], [1920, 1080]]) {
        await page.cdp('Emulation.setDeviceMetricsOverride', { width, height, deviceScaleFactor: 1, mobile: false });
        await page.keyboard.press('Home');
        for (let index = 0; index < count; index++) {
          const state = await page.evaluate(() => {
            const slide = document.querySelector('.slide.active');
            const deck = document.querySelector('.deck').getBoundingClientRect();
            const body = slide.querySelector('.body').getBoundingClientRect();
            const footer = slide.querySelector('.foot').getBoundingClientRect();
            const content = [...slide.querySelectorAll('.body *')];
            return {
              counter: document.getElementById('counter').textContent,
              fits: deck.left >= -1 && deck.top >= -1 && deck.right <= innerWidth + 1 && deck.bottom <= innerHeight + 1,
              scrolls: document.documentElement.scrollWidth > innerWidth || document.documentElement.scrollHeight > innerHeight,
              bodyFits: body.bottom <= footer.top + 1,
              overflowing: content.filter(e => {
                // SVG scrollWidth/clientWidth do not describe text overflow reliably.
                if (e instanceof SVGElement) {
                  if (!e.ownerSVGElement) return false;
                  const rect = e.getBoundingClientRect();
                  const viewport = e.ownerSVGElement.getBoundingClientRect();
                  return rect.width > 0 && (rect.left < viewport.left - 2 || rect.right > viewport.right + 2 || rect.top < viewport.top - 2 || rect.bottom > viewport.bottom + 2);
                }
                return e.clientWidth && getComputedStyle(e).overflowX !== 'hidden' && e.scrollWidth > e.clientWidth + 2;
              }).map(e => e.getAttribute('class') || e.tagName),
              textOutside: content.filter(e => !e.children.length && e.textContent.trim()).filter(e => {
                const rect = e.getBoundingClientRect();
                return rect.bottom > footer.top + 1 || rect.top < body.top - 1;
              }).map(e => e.textContent),
              errors: window.__deckErrors,
            };
          });
          const result = { slug, width, height, index, ...state };
          results.push(result);
          if (!state.fits || state.scrolls || !state.bodyFits || state.overflowing.length || state.textOutside.length || state.errors.length || state.counter !== `${index + 1} / ${count}`) {
            throw new Error(JSON.stringify(result));
          }
          if ((width === 1512 && height === 850) || width === 1920) {
            await page.screenshot({ path: join(outputDir, `${slug}-${width}-${index + 1}.png`) });
          }
          await page.keyboard.press('ArrowRight');
        }
        if (await page.evaluate(() => document.getElementById('counter').textContent) !== `${count} / ${count}`) throw new Error(`${slug}: end boundary`);
      }
      await page.reload();
      if (await page.evaluate(() => document.getElementById('counter').textContent) !== `${count} / ${count}`) throw new Error(`${slug}: persistence`);
      await page.keyboard.press('PageUp');
      if (await page.evaluate(() => document.getElementById('counter').textContent) !== `${count - 1} / ${count}`) throw new Error(`${slug}: PageUp`);
      await page.keyboard.press('PageDown');
      await page.keyboard.press('Home');
      await page.keyboard.press('ArrowLeft');
      if (await page.evaluate(() => document.getElementById('counter').textContent) !== `1 / ${count}`) throw new Error(`${slug}: start boundary`);
      await page.click('#next');
      if (await page.evaluate(() => document.getElementById('counter').textContent) !== `2 / ${count}`) throw new Error(`${slug}: next button`);
      await page.keyboard.press('ArrowLeft');
      if (await page.evaluate(() => document.getElementById('counter').textContent) !== `1 / ${count}`) throw new Error(`${slug}: keyboard after click`);
      await page.keyboard.press('ArrowRight');
      await page.click('#prev');
      await page.cdp('Emulation.setEmulatedMedia', { media: 'print' });
      if (!await page.evaluate(() => [...document.querySelectorAll('.slide')].every(s => getComputedStyle(s).visibility === 'visible'))) throw new Error(`${slug}: print visibility`);
      await page.cdp('Emulation.setEmulatedMedia', { media: '' });
      if (previewDir) {
        await mkdir(previewDir, { recursive: true });
        await page.cdp('Emulation.setDeviceMetricsOverride', { width: 960, height: 540, deviceScaleFactor: 1, mobile: false });
        await page.evaluate(() => {
          document.querySelector('.controls').style.visibility = 'hidden';
          document.querySelectorAll('.slide').forEach(slide => { slide.style.transition = 'none'; });
        });
        await page.screenshot({ path: join(previewDir, `${slug}.png`) });
      }
      console.log(`PASS ${slug}: ${count} slides × 4 viewports, navigation, persistence, print styles`);
    }
  } finally {
    await page.cdp('Page.removeScriptToEvaluateOnNewDocument', { identifier: hook.identifier });
    await page.cdp('Emulation.setEmulatedMedia', { media: '' });
    await writeFile(join(outputDir, 'results.json'), JSON.stringify(results, null, 2));
  }
  return results;
}
