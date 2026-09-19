# Sword & Shield Black Star Promos completion

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
- Anniversary novelty cards explicitly disallowed at official tournaments are
  collectible but banned from deck formats; their text is not treated as an
  ordinary legal tournament card.

## Artwork and installer

The local cbrew bundle source supplied 222 original promo textures. The other
82 physical printings retain English downloaded artwork. No artwork or foil
files are included in this change.

`install_recent_card_art swshp --cbrew-source <path>` prefers available original
textures and downloads missing ones. Fallback URLs preserve padded identifiers
such as `SWSH001`. Missing V-UNION combined faces can be assembled from downloaded
quadrants, including alternate Morpeko; native combined faces take precedence.

## Verification

The final full regression suite passed all **1,325 tests**.

Catalog tests compare all 304 identities and artwork mappings, and ordinary
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
