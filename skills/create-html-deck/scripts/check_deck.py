#!/usr/bin/env python3
"""Portable structural checks for fixed-canvas HTML slide decks."""

from __future__ import annotations

import argparse
import re
import sys
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlparse


class DeckParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.slide_count = 0
        self.html_lang = ""
        self.has_viewport = False
        self.has_title = False
        self.title_depth = 0
        self.ids: list[str] = []
        self.images: list[tuple[str, str | None]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        classes = set((values.get("class") or "").split())
        if tag == "html":
            self.html_lang = (values.get("lang") or "").strip()
        elif tag == "meta" and (values.get("name") or "").lower() == "viewport":
            self.has_viewport = bool((values.get("content") or "").strip())
        elif tag == "title":
            self.title_depth += 1
        if tag == "article" and "slide" in classes:
            self.slide_count += 1
        if tag == "img" and values.get("src"):
            self.images.append((values["src"] or "", values.get("alt")))
        if values.get("id"):
            self.ids.append(values["id"] or "")

    def handle_data(self, data: str) -> None:
        if self.title_depth and data.strip():
            self.has_title = True

    def handle_endtag(self, tag: str) -> None:
        if tag == "title" and self.title_depth:
            self.title_depth -= 1


def local_asset_path(deck_path: Path, source: str) -> Path | None:
    parsed = urlparse(source)
    if parsed.scheme in {"http", "https", "data"} or source.startswith("#"):
        return None
    if parsed.scheme == "file":
        return Path(unquote(parsed.path))
    return (deck_path.parent / unquote(parsed.path)).resolve()


def main() -> int:
    argument_parser = argparse.ArgumentParser(description=__doc__)
    argument_parser.add_argument("deck", type=Path, help="HTML deck to check")
    args = argument_parser.parse_args()
    deck_path = args.deck.expanduser().resolve()

    if not deck_path.is_file():
        print(f"ERROR: deck not found: {deck_path}", file=sys.stderr)
        return 1

    html = deck_path.read_text(encoding="utf-8")
    parser = DeckParser()
    parser.feed(html)
    errors: list[str] = []

    if not re.search(r"<!doctype\s+html", html, flags=re.IGNORECASE):
        errors.append("missing HTML5 doctype")
    if not parser.html_lang:
        errors.append("missing <html lang=\"…\">")
    if not parser.has_viewport:
        errors.append("missing viewport meta tag")
    if not parser.has_title:
        errors.append("missing non-empty <title>")
    if parser.slide_count == 0:
        errors.append("no <article class=\"slide\"> elements found")

    duplicate_ids = sorted(
        element_id for element_id, count in Counter(parser.ids).items() if count > 1
    )
    if duplicate_ids:
        errors.append(f"duplicate element ids: {', '.join(duplicate_ids)}")

    required_patterns = {
        "1920px design width": r"width\s*:\s*1920px",
        "1080px design height": r"height\s*:\s*1080px",
        "centered scale transform": r"translate\(\s*-50%\s*,\s*-50%\s*\)\s*scale\(",
        "keyboard navigation": r"keydown",
        "localStorage persistence": r"localStorage",
        "print styles": r"@media\s+print",
    }
    for label, pattern in required_patterns.items():
        if not re.search(pattern, html, flags=re.IGNORECASE):
            errors.append(f"missing {label}")

    page_markers = [
        (int(current), int(total))
        for current, total in re.findall(
            r'<span\s+class=["\']page["\']>\s*(\d+)\s*/\s*(\d+)\s*</span>',
            html,
            flags=re.IGNORECASE,
        )
    ]
    if page_markers:
        expected = list(range(1, parser.slide_count + 1))
        actual = [current for current, _ in page_markers]
        totals = {total for _, total in page_markers}
        if actual != expected or totals != {parser.slide_count}:
            errors.append(
                f"page markers do not match {parser.slide_count} slides: {page_markers}"
            )

    missing_assets: list[Path] = []
    for source, alt in parser.images:
        if alt is None:
            errors.append(f"image missing alt attribute: {source}")
        asset_path = local_asset_path(deck_path, source)
        if asset_path is not None and not asset_path.is_file():
            missing_assets.append(asset_path)
    if missing_assets:
        errors.extend(f"missing image asset: {path}" for path in missing_assets)

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    local_assets = sum(
        local_asset_path(deck_path, source) is not None for source, _ in parser.images
    )
    print(
        f"PASS: {parser.slide_count} slides; "
        f"{len(parser.images)} images ({local_assets} local); "
        f"{len(parser.ids)} unique ids; structural contract present"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
