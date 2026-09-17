# Damage-counter targets, Special Energy types, and Pokemon Ranger

## Corrected

- Giant Water Shuriken chooses one opposing Pokemon and places all six counters on it. Its Water Energy discard filters cards in the hand, so Splash Energy is not eligible.
- Shared single-target counter attacks and knockout reactions no longer use the free-distribution picker. Examples include Plentiful Placement, Sneaky Placement, and Final Hour.
- Shocking Light only targets Pokemon-EX and is unavailable without one. Assassin's Magic requires a Special Condition and restricts its counter target to the Bench.
- Variable counter totals now honor the printed quantities for Fireworks Bomb, Supernatural Dance, Enemy Show, Mysterious Dance, and Re-Brew. Re-Brew returns the counted basic Grass Energy to the deck after placing counters.
- The hand-size counter template no longer also applies a second fixed counter placement.
- Special Energy type checks distinguish outside-play types from live attached provision. Restricted energies such as Splash do not have their attached type in the hand, deck, or discard. Rainbow, Prism, Blend, Unit, and Beast retain their printed outside-play Colorless identity. Unconditional older Darkness and Metal Energy keep their types outside play.
- Attached type checks honor valid holders, dynamic provision, and Special Energy suppression. Unit Energy supplies its printed alternatives; Beast Energy supplies all types only on an Ultra Beast.
- A disabled Dusknoir no longer continues reducing Special Energy to one Colorless Energy through the separate Energy-value path.
- Pokemon Ranger requires an ongoing, unexpired attack effect it can actually remove. Damage, Special Conditions, a spent GX action, and effects originating from Abilities/Trainers do not enable it. The same predicate is scoped to the appropriate player for Channeler.

## Validation

- Final full regression run: 958 tests passed. Dedicated counter/Energy/Ranger coverage: 16 tests. All 312 Energy script files also passed syntax checks.
- Dedicated result-based regressions: `tests/test_counter_energy_audit.py`.
- Existing battle-style Energy tests now check both an invalid holder and an eligible Single/Rapid/Fusion Strike holder, instead of incorrectly expecting typed provision on Eternatus V.
- The broader regression suite exercises counter protections, Energy values, paid costs, attachment restrictions, suppression, and Ranger/Channeler removal.

This is a targeted audit of the shared implementations and affected card families, not a claim that every printed effect in the catalog has been exhaustively proved correct.
