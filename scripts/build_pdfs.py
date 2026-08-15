#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Build every docs/<language>/rules.md file into a stable PDF."""

from __future__ import annotations

import html
import re
from pathlib import Path
from urllib.parse import quote

from reportlab import rl_config
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    Paragraph,
    SimpleDocTemplate,
    Spacer,
)


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUTPUT = ROOT / "output" / "pdf"
FONTS = ROOT / "assets" / "fonts"
REPOSITORY = "https://github.com/jonnydee/collapsi"
BLUE = colors.HexColor("#182e45")
LINK = colors.HexColor("#245f8f")
MUTED = colors.HexColor("#667085")
GOLD = colors.HexColor("#c6a15b")


class RulebookDocTemplate(SimpleDocTemplate):
    """Draw running furniture after content so split lists cannot cover it."""

    def afterPage(self) -> None:
        page_decoration(self.canv, self)


def register_fonts() -> None:
    pdfmetrics.registerFont(TTFont("NotoSans", FONTS / "NotoSans-Regular.ttf"))
    pdfmetrics.registerFont(TTFont("NotoSans-Bold", FONTS / "NotoSans-Bold.ttf"))
    pdfmetrics.registerFont(TTFont("NotoSans-Italic", FONTS / "NotoSans-Italic.ttf"))
    pdfmetrics.registerFont(
        TTFont("NotoSans-BoldItalic", FONTS / "NotoSans-BoldItalic.ttf")
    )
    pdfmetrics.registerFontFamily(
        "NotoSans",
        normal="NotoSans",
        bold="NotoSans-Bold",
        italic="NotoSans-Italic",
        boldItalic="NotoSans-BoldItalic",
    )


def read_setting(name: str) -> str:
    return (ROOT / name).read_text(encoding="utf-8").strip()


def title_from(source: str) -> str:
    match = re.search(r"^#\s+(.+?)\s*$", source, flags=re.MULTILINE)
    if not match:
        raise ValueError("Every rulebook must begin with a level-one title")
    return match.group(1)


def github_url(target: str, source_file: Path) -> str:
    if target.startswith(("#", "http://", "https://", "mailto:")):
        return target
    path_text, separator, fragment = target.partition("#")
    resolved = (source_file.parent / path_text).resolve()
    try:
        relative = resolved.relative_to(ROOT).as_posix()
    except ValueError:
        return target
    url = f"{REPOSITORY}/blob/main/{quote(relative, safe='/')}"
    if separator:
        url += f"#{quote(fragment)}"
    return url


def inline_markup(text: str, source_file: Path) -> str:
    """Convert the small inline Markdown subset used by the rulebooks."""
    placeholders: dict[str, str] = {}

    def link(match: re.Match[str]) -> str:
        key = f"@@LINK{len(placeholders)}@@"
        label = html.escape(match.group(1))
        target = html.escape(github_url(match.group(2), source_file), quote=True)
        placeholders[key] = f'<a href="{target}" color="#245f8f">{label}</a>'
        return key

    converted = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", link, text)
    converted = html.escape(converted)
    converted = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", converted)
    converted = converted.replace("&lt;small&gt;", '<font size="8" color="#667085">')
    converted = converted.replace("&lt;/small&gt;", "</font>")
    for key, value in placeholders.items():
        converted = converted.replace(key, value)
    return converted


def styles() -> dict[str, ParagraphStyle]:
    base = getSampleStyleSheet()
    return {
        "body": ParagraphStyle(
            "Body",
            parent=base["BodyText"],
            fontName="NotoSans",
            fontSize=9.7,
            leading=14.3,
            textColor=colors.HexColor("#17212b"),
            spaceAfter=7,
            splitLongWords=False,
        ),
        "bullet": ParagraphStyle(
            "Bullet",
            parent=base["BodyText"],
            fontName="NotoSans",
            fontSize=9.7,
            leading=14.3,
            textColor=colors.HexColor("#17212b"),
            bulletFontName="NotoSans",
            bulletFontSize=8,
            bulletColor=GOLD,
            leftIndent=7,
            bulletIndent=-7,
            spaceAfter=5,
            splitLongWords=False,
        ),
        "nav": ParagraphStyle(
            "Navigation",
            parent=base["BodyText"],
            fontName="NotoSans",
            fontSize=8.5,
            leading=12,
            textColor=MUTED,
            spaceAfter=10,
        ),
        "h1": ParagraphStyle(
            "Heading1",
            parent=base["Heading1"],
            fontName="NotoSans-Bold",
            fontSize=23,
            leading=27,
            textColor=BLUE,
            spaceAfter=14,
            keepWithNext=True,
        ),
        "h2": ParagraphStyle(
            "Heading2",
            parent=base["Heading2"],
            fontName="NotoSans-Bold",
            fontSize=14.5,
            leading=18,
            textColor=BLUE,
            spaceBefore=16,
            spaceAfter=7,
            keepWithNext=True,
        ),
        "h3": ParagraphStyle(
            "Heading3",
            parent=base["Heading3"],
            fontName="NotoSans-Bold",
            fontSize=11.5,
            leading=15,
            textColor=BLUE,
            spaceBefore=12,
            spaceAfter=5,
            keepWithNext=True,
        ),
        "h4": ParagraphStyle(
            "Heading4",
            parent=base["Heading4"],
            fontName="NotoSans-Bold",
            fontSize=9.8,
            leading=13,
            textColor=BLUE,
            spaceBefore=9,
            spaceAfter=4,
            keepWithNext=True,
        ),
    }


def paragraph_text(lines: list[str], source_file: Path) -> str:
    parts: list[str] = []
    for line in lines:
        hard_break = line.endswith("  ")
        parts.append(inline_markup(line.rstrip(), source_file))
        parts.append("<br/>" if hard_break else " ")
    return "".join(parts).strip()


def flowables(source: str, source_file: Path) -> list[object]:
    style = styles()
    result: list[object] = []
    lines = source.splitlines()
    index = 0
    first_content = True

    while index < len(lines):
        line = lines[index]
        stripped = line.strip()
        if not stripped or stripped == "---":
            index += 1
            continue

        heading = re.match(r"^(#{1,4})\s+(.+)$", stripped)
        if heading:
            level = len(heading.group(1))
            result.append(
                Paragraph(inline_markup(heading.group(2), source_file), style[f"h{level}"])
            )
            if level == 1:
                result.append(Spacer(1, 2,))
            index += 1
            first_content = False
            continue

        if stripped.startswith("- "):
            while index < len(lines) and lines[index].strip().startswith("- "):
                item_text = lines[index].strip()[2:]
                result.append(
                    Paragraph(
                        inline_markup(item_text, source_file),
                        style["bullet"],
                        bulletText="•",
                    )
                )
                index += 1
                while index < len(lines) and not lines[index].strip():
                    index += 1
            continue

        block: list[str] = []
        while index < len(lines):
            candidate = lines[index]
            value = candidate.strip()
            if not value or value == "---" or value.startswith("- ") or re.match(
                r"^#{1,4}\s+", value
            ):
                break
            block.append(candidate)
            index += 1

        result.append(
            Paragraph(
                paragraph_text(block, source_file),
                style["nav"] if first_content else style["body"],
            )
        )
        first_content = False

    return result


def page_decoration(canvas, document) -> None:
    canvas.saveState()
    canvas.setFillColor(MUTED)
    canvas.setFont("NotoSans", 7.5)
    if document.page > 1:
        canvas.drawString(document.leftMargin, A4[1] - 11 * mm, document.title)
    canvas.setFont("NotoSans", 8)
    canvas.drawCentredString(A4[0] / 2, 7.5 * mm, str(document.page))
    canvas.restoreState()


def build(
    source_file: Path, edition_name: str, version: str, release_date: str
) -> Path:
    language = source_file.parent.name
    source = source_file.read_text(encoding="utf-8")
    title = title_from(source)
    OUTPUT.mkdir(parents=True, exist_ok=True)
    target = OUTPUT / f"collapsi-rules-{language}.pdf"

    document = RulebookDocTemplate(
        str(target),
        pagesize=A4,
        leftMargin=18 * mm,
        rightMargin=18 * mm,
        topMargin=19 * mm,
        bottomMargin=14 * mm,
        title=title,
        author="Mark S. Ball; Johann Duscher",
        subject=(
            f"{edition_name} - unofficial Collapsi rules {version} ({release_date})"
        ),
        creator=f"Collapsi PDF build {version}",
        invariant=1,
    )
    document.build(flowables(source, source_file))
    return target


def main() -> None:
    rl_config.invariant = 1
    register_fonts()
    edition_name = read_setting("EDITION_NAME")
    version = read_setting("VERSION")
    release_date = read_setting("RELEASE_DATE")
    sources = sorted(DOCS.glob("*/rules.md"))
    if not sources:
        raise SystemExit("No docs/<language>/rules.md files found")
    for source_file in sources:
        print(
            build(source_file, edition_name, version, release_date)
            .relative_to(ROOT)
            .as_posix()
        )


if __name__ == "__main__":
    main()
