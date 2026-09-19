# Sword & Shield Black Star Promos completion

## Native-foil and novelty-card follow-up

The current catalog contains **298** of the 304 source entries. Dragapult 132,
Zacian LV.X 135, Mimikyu delta 136, Light Toxtricity 137, Hydreigon C 138 and
Greninja star 144 were removed at the user's request because their printed
rules prohibit official tournament use. The loader and artwork/mask importers
also reject obsolete copies of these scripts left by an older installation.
The catalog generator cannot recreate them; stale format bans were removed.

The local native import wrote 224 physical-print mask files, including secondary
layers. Standard masks are present for 214 remaining printings. The dedicated
V-UNION import also verified all 25 original faces and their 25 standard masks.
63 known foil printings have no standard mask in the supplied bundles; no
replacement or guessed masks were created. These counts describe source
availability, not a claim that every promo foil was recoverable.

Native installation includes these masks by default and with --cards-only.
The artwork downloader also imports them with `swshp --cbrew-source <path>`.
All images and masks remain local and are excluded from GitHub.

## Catalog and effects

- Added 283 missing English printings, completing all 304 entries in the
  bundled `swshp.json` catalog. The highest collector number is SWSH307;
  gaps in the published numbering are not synthesized.
- Exact mechanical reprints reuse existing card definitions. Unique printings
  use the shared effect engine with explicit compound handlers for Teapot of
  Surprises, Twinkle Gathering, Mixed Call, Flight Up, Tail Charge, Grand Falls,
  Pursuit Claw, Psychic Javelin, Pulling Currents, Flaring Dash, Shake and Gather
  and Protective DNA. Newly authored VSTAR attacks retain the once-per-game rule.
- Added alternate Morpeko V-UNION SWSH287-290. Mixed original/alternate quadrants
  can assemble, but duplicate quadrants cannot substitute for a missing quadrant.
- The six anniversary novelty cards were initially collectible but banned;
  the follow-up above removes them from the catalog altogether.

## Artwork and installer

The local cbrew bundle source supplied 222 original promo textures. The other
82 physical printings retain English downloaded artwork. No artwork or foil
files are included in this change.

`install_recent_card_art swshp --cbrew-source <path>` prefers available original
textures and downloads missing ones. Fallback URLs preserve padded identifiers
such as `SWSH001`. Missing V-UNION combined faces can be assembled from downloaded
quadrants, including alternate Morpeko; native combined faces take precedence.

## Verification

The native-foil/exclusion follow-up passed all **1,331 tests** in the full
regression suite (the original completion run passed 1,325).

Catalog tests check all 304 source rows, including six explicit exclusions,
and compare remaining identities, artwork mappings and ordinary
Pokemon HP, attack names and costs against the source data. Focused tests cover
compound targets and quantities, private results, opponent ownership, V-UNION
assembly, padded URLs, native-art priority and combined image generation.

The full-set execution smoke run covered 515 cases: 511 passed, four skipped;
all 398 scripted effects exercised completed without an exception. This is an
execution check, not proof of every possible multiplayer interaction. Native
client graphical playtesting was not performed for every promo.

```text
python -m unittest tests.test_swsh_promos_completion tests.test_vunion tests.test_vunion_installation tests.test_install_recent_card_art
python -m spirit.tools.effect_smoke --set Promo_SWSH --all
python -m unittest discover -s tests
```
