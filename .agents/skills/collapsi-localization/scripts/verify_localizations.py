#!/usr/bin/env python3
"""Validate localized Collapsi sources and reproducible PDF builds."""

from __future__ import annotations

import argparse
import hashlib
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit


TAG_PATTERN = re.compile(r"^[a-z]{2,3}(?:-[a-z0-9]{2,8})*$")
LINK_PATTERN = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")
OFFICIAL_URL = "https://riffleshuffleandroll.itch.io/collapsi"
REPOSITORY_URL = "https://github.com/jonnydee/collapsi"
YOUTUBE_URL = "https://www.youtube.com/@riffleshuffleandroll"
LICENSE_ID = "CC BY-NC-SA 4.0"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument(
        "--build",
        action="store_true",
        help="run the repository PDF builder twice and compare output bytes",
    )
    return parser.parse_args()


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relative_targets(markdown: Path) -> set[Path]:
    targets: set[Path] = set()
    for raw_target in LINK_PATTERN.findall(markdown.read_text(encoding="utf-8")):
        target = raw_target.strip().split(maxsplit=1)[0].strip("<>")
        parts = urlsplit(target)
        if parts.scheme or target.startswith(("#", "mailto:")):
            continue
        path_text = unquote(parts.path)
        if path_text:
            targets.add((markdown.parent / path_text).resolve())
    return targets


def expected_readme(root: Path, tag: str) -> Path:
    return root / ("README.md" if tag == "en" else f"README.{tag}.md")


def validate(root: Path, require_pdfs: bool) -> tuple[list[str], list[Path]]:
    errors: list[str] = []
    sources = sorted((root / "docs").glob("*/rules.md"))
    if not sources:
        return ["no docs/<language-tag>/rules.md files found"], []

    version_file = root / "VERSION"
    if not version_file.is_file():
        errors.append("missing VERSION")
        version = ""
    else:
        version = version_file.read_text(encoding="utf-8").strip()

    edition_name_file = root / "EDITION_NAME"
    if not edition_name_file.is_file():
        errors.append("missing EDITION_NAME")
        edition_name = ""
    else:
        edition_name = edition_name_file.read_text(encoding="utf-8").strip()

    tags = [source.parent.name for source in sources]
    for tag in tags:
        if not TAG_PATTERN.fullmatch(tag):
            errors.append(f"invalid lowercase BCP 47-compatible language tag: {tag}")

    readmes = [expected_readme(root, tag) for tag in tags]
    for readme in readmes:
        if not readme.is_file():
            errors.append(f"missing localized README: {readme.relative_to(root)}")

    required_text = (
        OFFICIAL_URL,
        YOUTUBE_URL,
        LICENSE_ID,
        "Mark S. Ball",
        "Johann Duscher",
    )
    rule_targets = {source.resolve() for source in sources}
    readme_targets = {readme.resolve() for readme in readmes}
    pdfs = [
        root / "output" / "pdf" / f"collapsi-rules-{tag}.pdf"
        for tag in tags
    ]
    pdf_targets = {pdf.resolve() for pdf in pdfs}

    for source in sources:
        text = source.read_text(encoding="utf-8")
        label = source.relative_to(root)
        for required in (*required_text, REPOSITORY_URL):
            if required not in text:
                errors.append(f"{label}: missing required text or URL: {required}")
        if version and version not in text:
            errors.append(f"{label}: does not contain VERSION value {version}")
        if edition_name and edition_name not in text:
            errors.append(
                f"{label}: does not contain EDITION_NAME value {edition_name}"
            )
        targets = relative_targets(source)
        missing_navigation = rule_targets - targets - {source.resolve()}
        for target in sorted(missing_navigation):
            errors.append(
                f"{label}: language switcher does not link to {target.relative_to(root)}"
            )

    for readme in readmes:
        if not readme.is_file():
            continue
        label = readme.relative_to(root)
        text = readme.read_text(encoding="utf-8")
        for required in required_text:
            if required not in text:
                errors.append(f"{label}: missing required text or URL: {required}")
        if version and version not in text:
            errors.append(f"{label}: does not contain VERSION value {version}")
        if edition_name and edition_name not in text:
            errors.append(
                f"{label}: does not contain EDITION_NAME value {edition_name}"
            )
        targets = relative_targets(readme)
        expected = rule_targets | readme_targets | pdf_targets
        for target in sorted(expected - targets - {readme.resolve()}):
            errors.append(
                f"{label}: missing language navigation link to {target.relative_to(root)}"
            )

    markdown_files = [*sources, *(path for path in readmes if path.is_file())]
    for markdown in markdown_files:
        for target in sorted(relative_targets(markdown)):
            try:
                target.relative_to(root)
            except ValueError:
                errors.append(
                    f"{markdown.relative_to(root)}: relative link escapes repository: {target}"
                )
                continue
            if not target.exists():
                errors.append(
                    f"{markdown.relative_to(root)}: broken relative link: "
                    f"{target.relative_to(root)}"
                )

    if require_pdfs:
        for pdf in pdfs:
            if not pdf.is_file():
                errors.append(f"missing generated PDF: {pdf.relative_to(root)}")
            elif not pdf.read_bytes().startswith(b"%PDF-"):
                errors.append(f"invalid PDF signature: {pdf.relative_to(root)}")
        output_dir = root / "output" / "pdf"
        actual = set(output_dir.glob("collapsi-*.pdf"))
        stale = actual - set(pdfs)
        for pdf in sorted(stale):
            errors.append(f"stale generated language PDF: {pdf.relative_to(root)}")

    return errors, pdfs


def run_build(root: Path) -> None:
    builder = root / "scripts" / "build_pdfs.py"
    if not builder.is_file():
        raise SystemExit("missing repository builder: scripts/build_pdfs.py")
    subprocess.run([sys.executable, str(builder)], cwd=root, check=True)


def main() -> int:
    args = parse_args()
    root = args.root.resolve()
    initial_errors, pdfs = validate(root, require_pdfs=False)
    if initial_errors:
        for error in initial_errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    if args.build:
        run_build(root)
        first = {pdf.relative_to(root): digest(pdf) for pdf in pdfs}
        run_build(root)
        second = {pdf.relative_to(root): digest(pdf) for pdf in pdfs}
        if first != second:
            for pdf in sorted(set(first) | set(second)):
                if first.get(pdf) != second.get(pdf):
                    print(f"ERROR: non-deterministic PDF: {pdf}", file=sys.stderr)
            return 1

    errors, pdfs = validate(root, require_pdfs=args.build)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    languages = ", ".join(
        source.parent.name for source in sorted((root / "docs").glob("*/rules.md"))
    )
    print(f"Validated {len(pdfs)} language(s): {languages}")
    if args.build:
        print("PDF build is byte-for-byte reproducible across two consecutive runs.")
        for pdf in pdfs:
            print(f"{pdf.relative_to(root).as_posix()}  {digest(pdf)}")
    else:
        print("Source validation passed; PDF build was not requested.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
