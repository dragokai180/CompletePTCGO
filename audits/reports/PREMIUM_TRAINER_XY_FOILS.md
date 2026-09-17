# Premium Trainer's XY Collection: original foil masks

## Evidence and cause

Both local cbrew cache snapshots were inspected under `A:/PTCGO`.
All 14 exact alternate-art masks are present as native Texture2D assets.
The old importer ignored their suffixed names and copied regular masks instead.
The material metadata also inherited the regular print's settings.

`spirit/game/foil_variants.py` now records the exact internal-slot/native-asset
mapping. Delinquent 98b uses `098xy`; `098ya` identifies the other 98a print.
These are distinct from the numeric `128` mask also present in that set.

The original [Rotom metadata export](https://malie.io/static/metamon/rotom.v4.json)
confirms Rainbow, intensity 201 and FullArt for these variants. Jirachi uses
the Holo mask class; the other 13 use Etched. These are exact-print settings,
not a rarity-based fallback.

## Changes

- Imported all 14 original variant masks, with the newest cached revision
  taking precedence.
- Removed regular/reverse copies for Blacksmith, Hex Maniac, Delinquent, N,
  Shauna and Team Flare Grunt; their original prints remain untouched.
- Removed regular-mask aliases for these 14 variants. The importer works on
  a clean checkout without requiring a generated local alias file.
- Forced re-import removes obsolete alternate masks if no exact replacement
  exists in the selected caches, rather than substituting a regular mask.
- Exact material corrections override older incorrect metadata and survive
  future metadata synchronization.

## Verification

`tests/test_premium_xy_foils.py` covers all 14 mappings, exact materials,
numeric-slot collisions, removal of stale reverse masks, missing exact masks,
and preservation of regular prints. Installed mask pixels were compared with
their corresponding native cache textures before rebuilding the foil bundles.

Imported textures and generated bundles remain local-only and are not committed.
