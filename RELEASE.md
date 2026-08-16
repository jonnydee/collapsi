# Preparing and publishing a release

This is the release procedure for the unofficial Collapsi rules collection. It
applies to the first release as well as later releases. Every release has both
a semantic version and a release-specific edition name. Neither belongs to the
official Collapsi version line, and neither implies endorsement by Mark S.
Ball.

## Choose the version and edition name

Use [Semantic Versioning](https://semver.org/):

- **PATCH** (`1.0.1`) for corrections that do not change the rules, including
  layout and translation corrections.
- **MINOR** (`1.1.0`) for backward-compatible additions, such as an optional
  Revival variation or a completed language edition.
- **MAJOR** (`2.0.0`) for an incompatible rule or interpretation change.

For the first public release, use `1.0.0` when the rules and accompanying
materials are considered stable.

Every release must explicitly define a new edition name in `EDITION_NAME`.
Never carry the previous release's name forward automatically. Choose a concise
name that reflects the release's defining rules. For version `1.0.0`, the name
is `Collapsi Revival Edition`. Edition names are human-readable release titles;
Git tags remain stable and use `edition-vMAJOR.MINOR.PATCH`.

## Release checklist

1. Decide the final edition name, version, and UTC release date in ISO 8601
   form: `YYYY-MM-DD`. Confirm that the name is new for this release, accurately
   describes its defining rules, and is not presented as an official Collapsi
   title.
2. Review the complete working tree. Include only release-ready changes and
   remove no third-party license notices, original-game attribution, or the
   statement that the edition is unofficial.
3. Synchronize every rulebook in `docs/*/rules.md`. Check the rules' actions,
   timing, exceptions, players, card counts, distances, and once-per-game
   limits in every language. Every edition must retain the official-game link,
   repository link, credits, and CC BY-NC-SA 4.0 scope.
4. Update the release metadata together:

   | Location | Required change |
   | --- | --- |
   | `EDITION_NAME` | Release-specific edition name, for example `Collapsi Revival Edition`; choose a new name for every release. |
   | `VERSION` | Final SemVer release version, for example `1.0.0`. |
   | `RELEASE_DATE` | Final UTC date, for example `2026-08-15`; use the actual publication date. |
   | `pyproject.toml` | Matching PEP 440 project version (`1.0.0` for a final release). |
   | `docs/*/rules.md` | Set the unobtrusive edition and version line to `EDITION_NAME` and `VERSION`; remove any pre-release wording if present. |
   | `CHANGELOG.md` | Add an entry headed `## VERSION - YYYY-MM-DD - EDITION_NAME`, with concise user-visible changes. |
   | `README*.md` | Update the displayed current edition name and version. |
   | `LICENSE.md`, `CONTRIBUTORS.md`, and `LICENSES/README.md` | Review for accuracy; update only if rights, attribution, contributors, or bundled dependencies changed. |

5. Verify the language switchers and every README table link to every existing
   README, Markdown rulebook, and generated PDF. Verify that the language list
   includes all directories under `docs/`.
6. Build and validate from a clean locked environment:

   ```sh
   uv sync --locked
   uv run --locked python .agents/skills/collapsi-localization/scripts/verify_localizations.py --root . --build
   git diff --check
   ```

   The validator builds each PDF twice and must report byte-for-byte identical
   output. Commit the resulting `output/pdf/collapsi-rules-<language-tag>.pdf`
   files; do not edit PDFs by hand.
7. Render and visually review every changed PDF page. Check glyph coverage,
   headings, page breaks, isolated lines, clipping, overlapping text, page
   numbers, and link appearance.
8. Review the final diff and run the validation commands once more. Confirm
   that `git status` shows only intentional release files.
9. Commit the release metadata, sources, and generated PDFs together. Create
   an annotated tag named `edition-vMAJOR.MINOR.PATCH`, for example
   `edition-v1.0.0`, on that exact commit.
10. Push the commit and tag. Create the GitHub Release from the annotated tag,
    title it `EDITION_NAME vMAJOR.MINOR.PATCH`, for example
    `Collapsi Revival Edition v1.0.0`, and use the matching changelog entry as
    its notes. State clearly that it is an unofficial Collapsi rules release
    and summarize its defining rules. Attach the four language PDFs if they
    are not otherwise easy to download from the release page.
11. After publication, confirm the tag resolves to the release commit, the
    release links work, the PDFs download correctly, and the release notes do
    not call this an official Collapsi release.
