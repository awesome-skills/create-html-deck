#!/usr/bin/env python3
"""Rebuild the offline template gallery from catalog.json (standard library only)."""
from html import escape
from html.parser import HTMLParser
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / 'assets' / 'templates'
CATEGORIES = {'all': '全部风格', 'technical': '技术与产品', 'research': '研究与观点', 'business': '提案与发布', 'creative': '设计与创意'}


class SlideCounter(HTMLParser):
    def __init__(self):
        super().__init__()
        self.count = 0

    def handle_starttag(self, tag, attrs):
        if 'slide' in (dict(attrs).get('class') or '').split():
            self.count += 1


def main():
    templates = json.loads((ROOT / 'catalog.json').read_text())
    cards = []
    slugs = set()
    for index, item in enumerate(templates, 1):
        slug = item['slug']
        if slug in slugs or not slug.replace('-', '').isalnum():
            raise ValueError(f'Invalid or duplicate slug: {slug}')
        slugs.add(slug)
        if item['category'] not in CATEGORIES or item['category'] == 'all':
            raise ValueError(f'Unknown category: {item["category"]}')
        if not (ROOT / f'{slug}.html').is_file():
            raise FileNotFoundError(slug)
        counter = SlideCounter()
        counter.feed((ROOT / f'{slug}.html').read_text())
        if not counter.count:
            raise ValueError(f'No slides found: {slug}')
        t = {key: escape(str(value), quote=True) for key, value in item.items()}
        cards.append(f'''<article class="card" data-category="{t['category']}">
          <a class="cover" href="{slug}.html" aria-label="预览 {t['name']}"><img src="previews/{slug}.png" alt="{t['name']}模板封面" width="960" height="540" loading="lazy"></a>
          <div class="details"><p class="eyebrow">{index:02} / {slug.upper()} <span>{'深色' if item['tone']=='dark' else '浅色'}</span></p>
          <h2>{t['name']}</h2><p class="description">{t['description']}</p><p class="use">{t['use']}</p><p class="layouts">{t['layouts']}</p>
          <div class="actions"><a href="{slug}.html">播放 {counter.count} 页示例 ↗</a><a href="{slug}.html" download="{slug}.html">下载 HTML ↓</a></div></div></article>''')
    filters = ''.join(f'<button type="button" data-filter="{key}" aria-pressed="{str(key=="all").lower()}">{label}</button>' for key,label in CATEGORIES.items())
    page = '''<!doctype html>
<html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Deck Collection · 模板画廊</title><style>
*{box-sizing:border-box}body{margin:0;background:#f1f0eb;color:#252822;font-family:"PingFang SC",system-ui,sans-serif}main{max-width:1440px;margin:auto;padding:64px 40px}header{border-top:2px solid;padding-top:24px;margin-bottom:44px}.eyebrow{font:13px/1.6 ui-monospace,monospace;letter-spacing:.1em}.eyebrow span{float:right;color:#64695f;font-family:inherit}h1{font-size:clamp(40px,6vw,76px);font-weight:550;letter-spacing:-.05em;margin:30px 0 20px}header p{font-size:18px;line-height:1.8;color:#5b6158;max-width:760px}.meta{display:flex;flex-wrap:wrap;gap:8px 24px;font-size:14px;color:#5b6158;margin-top:28px}.filters{display:flex;flex-wrap:wrap;gap:10px}.filters button{font:inherit;min-height:44px;border:1px solid #bfc3b7;background:transparent;padding:10px 18px;border-radius:100px;color:inherit;cursor:pointer}.filters button[aria-pressed=true]{background:#273b30;color:#fff;border-color:#273b30}.count{font-size:14px;color:#5b6158;margin:20px 0 26px}.grid{display:grid;grid-template-columns:1fr 1fr;gap:36px 30px}.card{border:1px solid #cfcec6;background:#faf9f5;min-width:0}.card[hidden]{display:none}.cover{display:block;overflow:hidden;background:#ddd}.cover img{width:100%;height:auto;display:block;transition:transform .2s}.cover:hover img{transform:scale(1.015)}a:focus-visible,button:focus-visible{outline:3px solid #a33f2b;outline-offset:4px}.details{padding:26px}.details .eyebrow{margin:0}.details h2{font-size:28px;font-weight:550;margin:14px 0}.description{font-size:16px;line-height:1.7;min-height:54px;margin:0}.use{font-size:14px;color:#475a4c;margin:18px 0 8px}.layouts{font-size:13px;color:#696c64;line-height:1.5;margin:0}.actions{display:flex;justify-content:space-between;gap:16px;flex-wrap:wrap;margin-top:22px;border-top:1px solid #dedfd6;padding-top:12px}.actions a{display:inline-flex;align-items:center;min-height:44px;color:#263b32;font-size:14px;text-decoration:underline;text-underline-offset:4px}.guide{margin-top:60px;padding:32px;background:#e6e9de;border:1px solid #cdd3c3}.guide h2{margin:0 0 16px;font-size:26px}.guide p{font-size:16px;line-height:1.8;margin:0;max-width:950px}footer{margin-top:40px;padding-top:22px;border-top:1px solid #bbbeb3;display:flex;flex-wrap:wrap;gap:12px 32px}footer a{color:inherit;display:inline-flex;align-items:center;min-height:44px;font-size:14px}@media(max-width:640px){main{padding:30px 20px}.grid{grid-template-columns:1fr}.description{min-height:0}header{margin-bottom:30px}.details{padding:22px}.guide{padding:24px}.filters{gap:8px}.filters button{padding:10px 14px}}@media(prefers-reduced-motion:reduce){.cover img{transition:none}}
</style></head><body><main><header><span class="eyebrow">CREATE HTML DECK / THE COLLECTION</span><h1>为你的故事，选一种表达。</h1><p>按内容挑风格，再用完整示例试播。每套包含多种构图，复制一个 HTML 就能开始；没有在线字体，也不用安装运行依赖。</p><div class="meta"><span>COUNT 套视觉模板</span><span>1920 × 1080 固定画布</span><span>中文示例 · 离线播放</span></div></header>
<nav class="filters" aria-label="按场景筛选模板">FILTERS</nav><p class="count" id="count" aria-live="polite">显示全部 COUNT 套模板</p><div class="grid">CARDS</div>
<section class="guide"><h2>选好之后，怎么开始？</h2><p>先播放示例，确认适合你的内容，再下载 HTML 并替换标题、正文和页脚。使用方向键翻页，Home / End 跳到首尾。新增图片时，把素材与 HTML 一起保存；上台之前，在实际设备上检查中文换行和字号。</p></section>
<footer><a href="../deck-template.html">基础模板 ↗</a><a href="../../references/templates.md">选择与定制指南 ↗</a><a href="../../references/design-research.md">开源设计参考 ↗</a></footer></main>
<script>
(() => {
 const buttons = [...document.querySelectorAll('[data-filter]')];
 const cards = [...document.querySelectorAll('[data-category]')];
 buttons.forEach(button => button.addEventListener('click', () => {
   const filter = button.dataset.filter;
   buttons.forEach(item => item.setAttribute('aria-pressed', String(item === button)));
   cards.forEach(card => { card.hidden = filter !== 'all' && card.dataset.category !== filter; });
   const visible = cards.filter(card => !card.hidden).length;
   document.getElementById('count').textContent = `显示 ${visible} / ${cards.length} 套模板`;
 }));
})();
</script></body></html>'''
    page = page.replace('FILTERS', filters).replace('CARDS', '\n'.join(cards)).replace('COUNT', str(len(templates)))
    (ROOT / 'index.html').write_text(page)
    print(f'Built gallery: {len(templates)} templates')


if __name__ == '__main__':
    main()
