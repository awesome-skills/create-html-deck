#!/usr/bin/env python3
"""Portable structural checks for fixed-canvas HTML slide decks."""

from __future__ import annotations

import argparse
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlparse


class DeckParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.slide_count = 0
        self.image_sources: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        classes = set((values.get("class") or "").split())
        if tag == "article" and "slide" in classes:
            self.slide_count += 1
        if tag == "img" and values.get("src"):
            self.image_sources.append(values["src"] or "")


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

    if parser.slide_count == 0:
        errors.append("no <article class=\"slide\"> elements found")

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
    for source in parser.image_sources:
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
        local_asset_path(deck_path, source) is not None for source in parser.image_sources
    )
    print(
        f"PASS: {parser.slide_count} slides; "
        f"{len(parser.image_sources)} images ({local_assets} local); structural contract present"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
