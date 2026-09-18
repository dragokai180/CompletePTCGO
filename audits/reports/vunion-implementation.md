# Original PTCGO V-UNION implementation

## Scope

The five original V-UNION, comprising 20 physical cards:

- Pikachu: SWSH139–142
- Greninja: SWSH155–158
- Mewtwo: SWSH159–162
- Zacian: SWSH163–166
- Morpeko: SWSH215–218

The later Morpeko SWSH287–290 artwork is not included: it is absent from
the supplied native cache.

## Sources and assets

All 20 individual faces, five combined faces and 25 exact masks were imported
from `SM Cache.zip` in the supplied PTCGO directory. The dedicated importer is:

```powershell
python -m spirit.tools.import_vunion --source A:/PTCGO
```

The regular native asset importer also calls it. Generated set bundles include
the combined texture names (`139to142`, `155to158`, `159to162`, `163to166`,
`215to218`), without creating extra collectible cards.

The native installer includes these assets in default and `--cards-only` runs.
`--vunion-only` refreshes only the V-UNION assets. All 25 faces and 25 standard
foil masks are validated; missing or invalid files return exit code 2 instead
of reporting a partial installation as complete. Re-running with valid assets
already installed is safe. UI-only and other targeted imports remain isolated.

Print identities and foil parameters were verified against the original Rotom
Promo_SWSH export, checksum `18b7dccc078300c1b1d82029e4a4dfb4`. Every included
printing uses the original Holo / SunPillar treatment, intensity 201; no inferred
VMAX/full-art foil or generated mask is substituted.

## Rules and protocol

- Four different owned parts must be in the discard pile, with room on the Bench.
- The once-per-game restriction is tracked independently for each owner/name.
- Assembly is a rule action, not an Ability; suppression cannot prevent it.
- Fragments are neither Basic nor Evolution Pokemon. They have no attacks or HP
  and cannot enter play individually through another effect.
- The assembled Pokemon awards three Prizes. All four physical cards separate
  when it leaves play; the runtime wrapper never enters a private pile.
- Native fragments use HalfLegend/CardType 1 with stage VUNION, without LEGEND's
  combined-render flag. The assembled entity uses the combined native texture.
- CreateVUnion contains AttachToVUnion with four movements and a final PlayCard
  sequence. Nested sequence serialization supports this second nesting level.
- Reconnect and zoom serialize one complete card plus actual attachments, without
  duplicating its four pieces as additional attached Pokemon.

## Verification

`tests/test_vunion.py` covers 23 scenarios, including all 20 attacks' printed
costs/damage, all bespoke effects, all five assemblies and Knock Outs, physical
card identity/recovery, type-dependent energy recovery, suppression, temporary
effects, damage-counter allocation and three-Prize resolution. The existing
nine LEGEND protocol/lifecycle regressions also pass.

The full regression suite passes: 1,241 tests. The 32 V-UNION/LEGEND tests
also pass with the condition-refresh integration exercised through the session.

After the entry-rule and installer updates, the full suite passes 1,260 tests.
The installer-focused suite passes 19 tests, and a native-cache installation
through `--vunion-only` confirms all 50 required files are present and valid.

Compiled artwork and foil bundles were opened and checked for all five combined
textures. These are engine/protocol/asset tests, not a visual playthrough in the
native client; final visual confirmation in a live match remains unperformed.
