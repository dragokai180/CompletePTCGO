# Contributing to CompletePTCGO

CompletePTCGO keeps executable rules and reproducible metadata in Git while
leaving copyrighted artwork, proprietary AssetBundles, generated caches, and
runtime account data outside the repository.

## Before opening a pull request

1. Keep each change focused on one engine rule, card family, set, or tooling
   concern.
2. Add a regression test for every rules correction.
3. Do not commit card or product PNGs, generated bundles, local databases,
   certificates, logs, audit output, or files extracted from the cbrew bundles.
4. Do not commit the local Pokemon TCG Live cache importer.
5. Run the functional engine suite:

   ```powershell
   python -m spirit.tools.engine_selftest
   ```

6. Run the unit tests:

   ```powershell
   python -m unittest discover -s tests
   ```

## Card implementations

Card definitions belong under `spirit/game/scripts/cards/<SET_CODE>/`. Shared
mechanics belong in `spirit/game/card_effects/`; card-specific behavior should
remain in its set module when reuse is unlikely. Use the printed English text
as the semantic source and preserve player choice, hidden-information rules,
timing, and animation boundaries.

Generated audit reports are local artifacts. Commit the audit tool or a focused
regression test, not its full JSON output.
