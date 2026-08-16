# Collapsi rulebook contract

Read this entire reference before adding or synchronizing a rulebook language.

## Repository conventions

- Rulebook Markdown: `docs/<lowercase-bcp47-tag>/rules.md`
- English landing page: `README.md`
- Other landing pages: `README.<tag>.md`
- Generated PDF: `output/pdf/collapsi-rules-<tag>.pdf`
- Shared generator: `scripts/build_pdfs.py`
- Locked environment: `pyproject.toml` and `uv.lock`
- Shared metadata: `EDITION_NAME`, `VERSION`, and `RELEASE_DATE`
- Contribution/release policy: `CONTRIBUTING.md`

The generator sorts and builds every `docs/*/rules.md`; a new language needs no registry entry. It uses pinned ReportLab, vendored Noto Sans fonts, fixed metadata, and invariant output. Never manually edit generated PDFs.

All README language switchers must link to all localized READMEs. All rulebook switchers must link to all localized rulebooks. Every README language table must link to every rulebook Markdown file and its PDF.

## Semantic translation rules

Preserve meaning rather than source wording. For each rule unit compare:

- action and actor;
- timing and sequence;
- condition and scope;
- mandatory, optional, and prohibited behavior;
- allowed choices and exceptions;
- frequency limits;
- affected card and player types;
- every number, dimension, and movement distance.

Do not turn “exactly” into “up to,” “once per game” into “once per turn,” “final space” into an intermediate space, or “orthogonally adjacent” into diagonal adjacency.

## Base rules and quantities

For the standard 2-player 4 × 4 game, require:

- 2 different Jokers;
- 4 Aces;
- 4 Twos;
- 4 Threes;
- 2 Fours;
- 16 cards total.

For the inventor's updated standard 2-player 4 × 4 setup, replace the two
Jokers with two different Jacks. The first Jack dealt belongs to Player 1 and
the second to Player 2. Each player's first move from their starting Jack is
exactly one space. All other normal 2-player rules remain in effect.

For the 3-player 5 × 5 game, require 3 Jokers, 6 Aces, 6 Twos, 6 Threes, and 4 Fours: 25 cards total.

For the 4-player 6 × 6 game, require 4 Jokers and 8 each of Aces, Twos, Threes, and Fours: 36 cards total. If fewer than four players use this board, unused Jokers start face down.

A Joker allows a move of 1, 2, 3, or 4 spaces. Movement is orthogonal and may change direction. The board wraps at opposite outer edges. A move must cover its full required distance, may not traverse the same card twice, may not end on its starting card or another pawn, and may not use collapsed cards unless an optional rule expressly permits it. The starting card collapses after a successful move. The game ends immediately when a player cannot complete a legal move; the last player to complete one wins.

## Revival invariants

### Joker Revival

- Each player may use it once per game.
- A collapsed Joker may be the final destination, never an intermediate collapsed space.
- Turn the Joker face up; the original starting card still collapses normally.
- The next move from the revived Joker is 1, 2, 3, or 4 spaces; it then collapses normally.
- A player may revive any Joker regardless of original ownership.
- Another player may later revive the same Joker if that player's ability remains unused.

### Adjacent Revival

- Each player may use it once per game.
- Complete the normal move and collapse the starting card first.
- Revive a collapsed card orthogonally adjacent to the pawn's final position.
- Do not revive the card that collapsed during the current turn.
- The pawn does not move onto the revived card.
- The card returns to normal use; a revived Joker has normal Joker behavior.

### Reconstruction

- Each player may use it once per game.
- Complete the normal move and collapse first.
- Restore one collapsed card, then collapse a different face-up unoccupied card.
- Never sacrifice a card containing any pawn.
- The newly collapsed starting card may be restored.
- Restored and sacrificed cards must differ.
- A restored Joker has normal Joker behavior.
- The total number of active cards does not increase.

## Identity, version, and upstream distinction

- Mark S. Ball created Collapsi.
- Johann Duscher (a.k.a. Jonny Dee) originated the Revival concept and Revival Variations.
- This repository is unofficial and must not imply Mark S. Ball's endorsement.
- The original downloadable rulebook identifies itself as Collapsi v1.3.1, last updated July 9, 2025. It uses Jacks with a one-space opening move.
- The current release documents the inventor's updated 2-player Jack setup with
  a one-space opening move alongside the earlier Joker setup.
- The Revival Variations deliberately remain based on Jokers with a choice of
  1–4 spaces.
- Every release has a release-specific name from `EDITION_NAME` and its own version from `VERSION`.
- Display the edition name and version visibly but unobtrusively in every rulebook.
- Never present the edition name or version as official Collapsi metadata.

Do not change the edition name or bump the project version only because a translation was added unless preparing a release at the user's request. For a release, explicitly confirm `EDITION_NAME`, follow Semantic Versioning, and update `VERSION`, `RELEASE_DATE`, every rulebook edition/version line, every README, and `CHANGELOG.md` together. Compatible patch releases may retain their edition name; releases that add variants or change the edition's scope require a new name. Tags use `edition-vMAJOR.MINOR.PATCH`.

## Attribution, licensing, and links

Every rulebook and README must preserve the distinction between original and Revival material.

Required identities and destinations (the repository URL is mandatory in every rulebook; the
other destinations belong wherever the corresponding attribution is stated):

- Official game page: `https://riffleshuffleandroll.itch.io/collapsi`
- Repository: `https://github.com/jonnydee/collapsi`
- Riffle Shuffle & Roll YouTube: `https://www.youtube.com/@riffleshuffleandroll`
- License identifier for Johann Duscher's covered work: `CC BY-NC-SA 4.0`
- Canonical license path from rulebooks: `../../LICENSE.md`

State that the original designer asks web apps and 3D-printable implementations to remain demonetized and always free to play, with credit and an official-page link and, where possible, a YouTube link.

State that Johann Duscher's own contributions are offered under CC BY-NC-SA 4.0 while Collapsi and material attributable to Mark S. Ball remain subject to his rights and are not relicensed. Do not describe the whole repository or original game as Creative Commons licensed.

For variants derived from the Revival rules, retain credits to both Mark S. Ball and Johann Duscher. Variants unrelated to the Revival rules do not owe Johann Duscher attribution merely because this repository exists.

Read `LICENSE.md` before changing any license or attribution wording. Do not infer broader permission from the original designer's targeted statement to web developers and 3D modelers.
