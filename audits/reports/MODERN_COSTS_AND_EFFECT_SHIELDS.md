# Mandatory costs, Mega ex evolution, and attack-effect shields

## Scope

Targeted follow-up to Morty's Conviction, modern Mega ex evolution, and
Emperor's Stance versus Chaotic Pain. The review also inspected the shared
Trainer discard-cost parser and text-based continuous attack shields across
the loaded catalog. This is not an exhaustive proof of every card effect.

## Corrections

- Recognize "discard another card" as a mandatory one-card cost, both when
  determining play permission and before resolving the Trainer effect.
  A short or failed payment stops resolution. Optional and post-draw discards
  are not converted into mandatory upfront costs.
- Affected shared implementations include Morty's Conviction, Iris's Fighting
  Spirit, Earthen Vessel (SFA), and Techno Radar (PRE), including their reprints.
  Morty requires an opposing Bench and cards to draw. Iris evaluates the refill
  after its discard cost. Techno Radar's search now filters Future Pokemon.
- Generic `MEGA` metadata on a modern `ex`/`SV_Mega` never triggers the old XY
  end-turn rule. XY Mega Evolution and matching Spirit Link behavior remain.
- Emperor's Stance recognizes modern attack-effect wording, stopping counters
  without stopping normal attack damage or counters from Abilities.
- Text-based damage/effect shields share the printed scope: carrier versus
  friendly team, Active/Bench requirements, Energy/type restrictions, and
  attacking Pokemon class. Related families include Protective Mycelium,
  Mystic Heart, Dragon Guard, Repelling Veil, Wind Charm, Storehouse Hideaway,
  Sparkling Scales, Bright Down, Safeguard, Scoundrel Guard, Neutral Shield,
  Smug Face, Iceberg Shield, and Mighty Shell.
- Force Canceler receives the actual attack context so its GX-only protection
  does not rely on the attacker's Pokemon class.
- Shared primitives now check shields when setting damage counters, removing
  attached cards, moving a Pokemon's stack, devolving it, or applying a retreat
  lock or temporary Pokemon-carried effect. Rule-based knockout cleanup and
  player-wide rules are kept separate from effects on an individual Pokemon.

## Regression coverage

`tests/test_modern_costs_and_shields.py` uses real card definitions/board
entities for paid costs, interrupted costs, search restrictions, modern Mega
printings, XY Spirit Links, Chaotic Pain, normal damage, Ability counters,
suppression, conditional shields, and protected stack moves/KO cleanup.

Validation: all 1,161 tests passed, including 17 targeted regression tests.

Run from the repository root:

```text
python -m unittest discover -s tests
```

## Automatic forced hand payments

The common card picker now skips the redundant hand-selection prompt when
the acting player must select exactly all eligible cards from their own hand.
This handles discard costs (Ultra Ball), filtered return costs (Pokemon
Communication / Energy Exchanger), and Lost Zone costs without changing each
card implementation. Movement, reveals, shuffling and subsequent searches
still execute normally; the played source itself is never auto-selected.

Selections remain manual with surplus or insufficient eligible cards, an
optional minimum, an ordering requirement, a displayed browser, another
player's hand, or a non-hand zone. Private deck searches keep their existing
failure rules. Optional effects still require their initial acceptance.

`tests/test_automatic_hand_costs.py` checks the actual Ultra Ball discard,
HGSS/BW/SM Pokemon Communication returns, filtered costs for both players,
and the exclusions above, without replacing the common picker.
