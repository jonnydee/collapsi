# Contributing

Contributions and translations are welcome. Please preserve the distinction between the original Collapsi game and this unofficial rules collection.

## Add a translation

1. Create `docs/<language-tag>/rules.md` by translating the selected current source language. English is not required to be the master language; any existing language may be the source when adding or synchronizing documentation.
2. Use a short lowercase BCP 47-compatible directory tag such as `fr`, `es`, or `pt-br`.
3. Preserve the rule hierarchy, edition and version line, official Collapsi link, repository link, credits, and licensing notice.
4. Add the language to the switcher at the top of every README and rulebook.
5. Add Markdown and PDF links to both READMEs.
6. Run the complete locked validation and build. It discovers every language automatically, checks links and metadata, invokes the PDF generator twice, and verifies byte-for-byte reproducibility:

   ```sh
   uv sync --locked
   uv run --locked python .agents/skills/collapsi-localization/scripts/verify_localizations.py --root . --build
   ```

7. Review every generated PDF page for missing glyphs, bad breaks, clipped text, or broken links.
8. Add the translator to [CONTRIBUTORS.md](CONTRIBUTORS.md) with their consent.

Translate prose, but keep filenames and shared tooling stable. Do not copy the stylesheet or build script into language folders.

## AI-assisted contributions

This repository includes the local [`collapsi-localization`](.agents/skills/collapsi-localization/SKILL.md) skill for AI assistants that support repository skills. Invoke it with a request such as:

```text
Use $collapsi-localization to add <language> from the selected existing source
language, update all language navigation, and build and validate every Markdown
and PDF. The source language may be English, German, or any other supported
language.
```

Use the skill when adding a language, synchronizing a semantic rule change, reviewing cross-language consistency, or rebuilding the localized PDFs. It instructs the assistant to:

- inspect the repository before editing and treat any language as the change source;
- translate rule units idiomatically while preserving mechanics, numbers, credits, links, and license scope;
- create the language README and rulebook, update every language switcher and README table, and avoid per-language build configuration;
- run the repository's reproducible PDF generator through `verify_localizations.py`;
- report semantic conflicts instead of silently choosing one interpretation.

The skill does not replace human review. Check the complete diff, confirm that the translation is natural and semantically faithful, and visually inspect every changed PDF. If the assistant cannot access repository skills, follow the manual checklist above and run the verifier command yourself.

## Version changes

The project follows semantic versioning for the unofficial rules collection. Each release also has its own edition name in `EDITION_NAME`:

- **PATCH**: wording, typo, layout, or translation corrections that do not change rules.
- **MINOR**: backward-compatible additions such as a new optional Revival variant or a new language.
- **MAJOR**: incompatible changes to the Revival rules or their interpretation.

Before publishing, follow the complete [release checklist](RELEASE.md). It
identifies every version and date location, requires reproducible PDFs and
visual review, and covers tagging and GitHub Release publication. Update
`EDITION_NAME`, `VERSION`, `RELEASE_DATE`, `pyproject.toml`, the unobtrusive
edition and version line in every rulebook, every README's displayed release
identity, and `CHANGELOG.md` in the same change. Use Git tags in the form
`edition-vMAJOR.MINOR.PATCH`.

## Attribution

Do not remove the credit or official link for Mark S. Ball. If a contribution uses or derives from the Revival rules, do not remove the credit for Johann Duscher, the CC BY-NC-SA 4.0 notice, or the request to keep the rules free of charge. Contributions unrelated to the Revival rules do not need to attribute Johann Duscher merely because this repository exists.
