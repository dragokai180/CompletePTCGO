# Restored Pokemon and Hero's Spirit entry rules

## Corrections

- Restored Pokemon cannot enter play through generic recovery or Bench effects.
  Anorith STS 56 is not a valid Maxie's Hidden Ball Trick target. Garbotoxin
  cannot remove a printed Restored rule, which is not an Ability.
- Preserve matching Fossil Items and explicit support: Twist Mountain,
  Omastar's Restoring Beam, and Fossil Researcher for Amaura/Tyrunt.
- Correct Archen NVI 66, Tirtouga NVI 25 and Aerodactyl DEX 53 from Basic to
  Restored. Their evolutions remain eligible for Archie/Maxie.
- Hero's Spirit is checked before selecting or moving Palafin ex into play.
  Archie can recover it only when the Ability is disabled in the discard.
  Cinnabar Lure cannot select it: Garbotoxin does not affect the deck.
- Zero to Hero still enters Palafin ex from the deck and transfers its state.
  Entry restrictions do not block switching Pokemon already in play.
- Invalid Archie/Maxie targets are filtered before playability is offered.
  Private deck views still show restricted cards but do not make them selectable.
- Fossil bottom-seven searches enforce the named species and available Bench
  space; a generic Item reminder is not a search descriptor.

## Tests

`tests/test_restricted_pokemon_entry.py` covers both Garbotoxin implementations,
all four Hero's Spirit prints, the requested attacks/Supporters, matching and
wrong Fossils, all catalogued Restored prints, explicit Restored support,
Zero to Hero, hand entry, stale selections and generic identity swaps.

Existing Archie/Maxie tests also cover normal evolutions, full arts, the last
card in hand, empty decks, Bench capacity and recovery-before-draw ordering.
These are automated engine tests, not a native-client visual playthrough.
The full regression suite passes: 1,254 tests, including 13 new test methods
with per-print and per-suppression-state cases.

## Rule references

- [Official rules, Appendix N, printed page 31](https://assets.pokemon.com/assets/cms2/pdf/trading-card-game/rulebook/sm5_rulebook_en.pdf)
- [Anorith STS 56](https://www.pokemon.com/uk/pokemon-tcg/pokemon-cards/series/xy11/56)
- [Palafin ex PRE 151](https://www.pokemon.com/us/pokemon-tcg/pokemon-cards/series/sv8pt5/151)
