# Collapsi: Joker Edition & Revival Variations

[English](README.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [Español](README.es.md)

This repository contains an **unofficial** multilingual rules edition for [Collapsi](https://riffleshuffleandroll.itch.io/collapsi), the abstract strategy game invented by **Mark S. Ball** of Riffle Shuffle & Roll.

The edition uses Jokers as starting cards and includes optional **Revival Variations** created by **Johann Duscher (a.k.a. Jonny Dee)**. These additions let collapsed cards return to play in several controlled ways. This project is independent and is not an official release by Mark S. Ball.

## Original reference and this edition

The downloadable original rulebook identifies itself as **Collapsi v1.3.1**, last updated July 9, 2025. It uses two Jacks as starting cards, and each Jack allows a one-space opening move. This unofficial edition deliberately uses two Jokers instead, with a choice of 1, 2, 3, or 4 spaces, and adds the Revival Variations. Other explanations on the [Riffle Shuffle & Roll YouTube channel](https://www.youtube.com/@riffleshuffleandroll) may reflect different stages of the original game's development; this repository does not infer an official version number for them.

## Rules

| Language | Markdown | PDF |
| --- | --- | --- |
| English | [Read online](docs/en/rules.md) | [Download PDF](output/pdf/collapsi-revival-rules-en.pdf) |
| Deutsch | [Online lesen](docs/de/rules.md) | [PDF herunterladen](output/pdf/collapsi-revival-rules-de.pdf) |
| Français | [Lire en ligne](docs/fr/rules.md) | [Télécharger le PDF](output/pdf/collapsi-revival-rules-fr.pdf) |
| Español | [Leer en línea](docs/es/rules.md) | [Descargar PDF](output/pdf/collapsi-revival-rules-es.pdf) |

The root README is English because GitHub displays `README.md` automatically. Every README and rulebook starts with a compact language switcher, so readers can reach their language in one click.

## Versioning

The Revival edition has its **own semantic version**. Releases and Git tags use `edition-vMAJOR.MINOR.PATCH`, for example `edition-v1.0.0`. Follow the [release checklist](RELEASE.md) when publishing a version.

This number identifies only this unofficial edition. It is deliberately independent of unknown or changing versions of the original Collapsi rules and must not be presented as an official Collapsi version. Compatibility with a particular original rules release should be documented in release notes instead of encoded in the version number.

## Repository layout

```text
docs/<language>/rules.md    Translated Markdown sources
output/pdf/                 Generated PDFs
assets/fonts/               Vendored fonts for stable layout
scripts/build_pdfs.py       One build for every language
.github/workflows/          Automated PDF verification
```

Language directories use short, lowercase, BCP 47-compatible tags such as `en`, `de`, `fr`, or `pt-br`. Only translated prose belongs below `docs/<language>/`. Fonts, build logic, licensing, contributor guidance, and workflows stay language-independent at the repository root.

## Building the PDFs

The PDF pipeline uses [ReportLab](https://www.reportlab.com/opensource/). It avoids a LaTeX installation and native HTML-rendering dependencies while supporting embedded fonts, controlled page breaks, page numbers, links, and PDF metadata.

```sh
uv sync --locked
uv run python scripts/build_pdfs.py
```

Pinned dependencies, one shared renderer, vendored Noto Sans fonts, fixed release metadata, and stable filenames make builds reproducible. The GitHub Actions workflow rebuilds every language and rejects stale committed PDFs; it also publishes the PDFs as a workflow artifact.

## License and attribution

Johann Duscher's original text and Revival contributions are offered under [CC BY-NC-SA 4.0](LICENSE.md). This permits reuse and adaptation, but not commercial use, and requires adaptations to use the same license. Please keep every distributed rules edition available free of charge. Collapsi itself and material attributable to Mark S. Ball remain subject to his rights and are not relicensed by this repository.

If you derive a variant from these Revival rules, retain credit to both Mark S. Ball and Johann Duscher. A variant that does not use or derive from the Revival rules does not require attribution to Johann Duscher. See [LICENSE.md](LICENSE.md) for the precise scope and [CONTRIBUTORS.md](CONTRIBUTORS.md) for roles.

## Contributing translations

New translations are welcome. The checklist in [CONTRIBUTING.md](CONTRIBUTING.md) explains how to add a language without duplicating build configuration.
