---
name: collapsi-localization
description: Add, translate, synchronize, and validate localized Collapsi repository documentation and rulebooks, including reproducible PDF generation. Use when adding a language, propagating a semantic documentation change across languages, reviewing translation consistency, updating language navigation, or rebuilding and checking all localized Markdown and PDFs in the Collapsi repository.
---

# Collapsi localization

Maintain every supported language as an equal, semantically equivalent edition. Do not assume English is always authoritative.

## Load the repository contract

Read [references/rulebook-contract.md](references/rulebook-contract.md) completely before translating or synchronizing rulebooks. Treat its mechanics, attribution, licensing, versioning, paths, and naming rules as invariants.

Inspect the repository before editing. If its current structure or build commands differ from the reference, follow the repository and update this skill only when the user asks to change the workflow.

## Distinguish source from generated files

- Edit `docs/<language-tag>/rules.md`, `README.md`, and `README.<language-tag>.md`.
- Treat `output/pdf/*.pdf` as generated artifacts. Never edit a PDF manually.
- Keep shared build code, fonts, licensing, and contributor files language-independent.
- Use lowercase BCP 47-compatible tags such as `en`, `de`, `fr`, or `pt-br`.
- Keep English at `README.md`; use `README.<tag>.md` for every non-English language.
- Expect `output/pdf/collapsi-revival-rules-<tag>.pdf` for every `docs/<tag>/rules.md`.

The PDF generator discovers `docs/*/rules.md` automatically. Do not add a per-language build configuration.

## Synchronize an existing change

1. Identify the intended source language and semantic delta. Compare Git history when useful.
2. Compare actions, timing, conditions, choices, prohibitions, scope, frequency, exceptions, affected players, card types, and all numbers.
3. Stop and report a conflict if existing languages disagree and neither repository history nor the user's request establishes the intended rule.
4. Determine every affected rulebook, README, credit, link, version reference, and contributor entry.
5. Rewrite the equivalent passages idiomatically in every target language. Preserve normative strength: distinctions such as *must*, *may*, *cannot*, *exactly*, and *once per game* are mechanics.
6. Preserve each language's established terminology and rulebook voice. Translate semantic units, not sentences mechanically.
7. Update language navigation and README language tables when the set of languages changes.
8. Run the complete validation and PDF workflow below.

Do not propagate purely stylistic differences. Do not invent a rule to resolve an ambiguity.

## Add a language

1. Inspect all current editions and select the source requested by the user. Otherwise choose the most complete current edition and cross-check it against at least one other language.
2. Choose a lowercase BCP 47-compatible tag. Use a regional subtag only when the content genuinely targets that locale.
3. Establish natural, consistent board-game terms for recurring concepts before translating the full text.
4. Create `docs/<tag>/rules.md` with the same semantic sections, rules, numbers, links, unobtrusive Revival version line, credits, attribution, and license scope.
5. Create `README.<tag>.md` for non-English languages. Keep `README.md` as the English landing page.
6. Update the language switcher in every README and rulebook. Update every README's language table with Markdown and PDF links for every language.
7. Add the translator and language to `CONTRIBUTORS.md` only with the contributor's consent. Do not infer a real name from an account name.
8. Do not change `VERSION` merely for a translation unless the user explicitly requests a release. If making a release, follow `CONTRIBUTING.md` and update all release metadata together.
9. Run the complete validation and PDF workflow below. The existing generator must create the new PDF without a build-script registration step.

## Build and validate all languages

From the repository root, run:

```sh
uv sync --locked
uv run --locked python .agents/skills/collapsi-localization/scripts/verify_localizations.py --root . --build
```

The verifier must:

- discover every `docs/*/rules.md` source;
- check repository naming, matching READMEs, required metadata, navigation, and relative links;
- invoke the repository's `scripts/build_pdfs.py` twice;
- require one correctly named PDF per language and no stale language PDFs;
- fail if the two builds produce different bytes.

Do not replace `--locked` with an unlocked dependency update. Do not call a different PDF renderer. If setup cannot use `uv`, report the blocker instead of claiming a reproducible build.

After any generated PDF changes, use the PDF skill to render and visually inspect every changed PDF page. Check missing glyphs, clipped text, overlaps, awkward headings, isolated lines, page breaks, page numbers, and link appearance. A successful script is not visual proof. If a new writing system is unsupported by the vendored fonts, update the shared font/build setup deliberately and recheck every language.

Run `git diff --check` and inspect the complete diff. Keep source Markdown and generated PDFs together in the same change.

## Translation quality

- Write like a native modern board-game rulebook, not like translated prose.
- Preserve proper names: Collapsi, Mark S. Ball, Johann Duscher, and Jonny Dee.
- Preserve exact URL destinations and translate only surrounding text.
- Preserve structure where it helps comparison, but prefer natural localized headings and phrasing.
- Recompute card totals and compare every numeric rule explicitly.
- Preserve ambiguity when the source is ambiguous and report it.
- Never change game design during localization.

## Definition of done

Finish only when:

1. all affected Markdown editions are semantically synchronized and idiomatic;
2. every README and rulebook exposes complete language navigation;
3. credits, license scope, URLs, and project version agree;
4. the verifier passes and produces deterministic PDFs for every language;
5. every changed PDF has passed visual inspection;
6. no unrelated files or manual PDF edits are present.

Report the source language, changed files, generated PDFs, validation result, deterministic-build result, visual-review result, and any unresolved semantic conflict.
