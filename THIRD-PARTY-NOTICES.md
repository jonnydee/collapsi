# Third-party notices

This file identifies third-party material used by this repository. It is an
inventory and does not replace the applicable license texts.

## Bundled assets

### Noto Sans

The PDF generator embeds the Noto Sans Regular, Italic, Bold, and Bold Italic
font files from `assets/fonts/`. Noto Sans is licensed under the SIL Open Font
License 1.1. The complete, unmodified license text and the Noto copyright notice
are in [LICENSES/OFL-1.1.md](LICENSES/OFL-1.1.md).

## Build-time dependencies

### ReportLab 4.4.9

The PDF build uses [ReportLab](https://www.reportlab.com/opensource/) version
4.4.9, as pinned in `pyproject.toml` and `uv.lock`. ReportLab is available under
the BSD license; see its [package metadata](https://pypi.org/project/reportlab/)
and the license supplied with the installed package.

ReportLab is a build-time dependency. Its source code and binaries are not
vendored in this repository or included with the generated rulebook PDFs.

## Project licenses

The repository's own build script and workflow are under the
[MIT License](LICENSES/MIT.md). Johann Duscher's covered Revival contributions
are under [CC BY-NC-SA 4.0](LICENSES/CC-BY-NC-SA-4.0.md); the precise scope and
the exclusion of original Collapsi material are explained in
[LICENSE.md](LICENSE.md).
