# Interpreter transaction audit — 2026-09-17

## Scope and method

Reviewed shared text interpretation for attacks, Abilities and Trainers,
particularly overlapping templates, coin conditions, quantities and operation
order. The catalog scan now includes direct `bw_legacy_attack` and
`bw_legacy_ability` users, not only their Standard-era aliases.

The expanded attack smoke run covered 5,469 distinct exact-text families.
Its results were 5,408 observed, 33 partially suspect, 19 with no observed
effect and 9 skipped because the fixture did not satisfy the activation
condition. These are diagnostic classifications, **not correctness proofs**:
an observed effect can still run twice or choose the wrong quantity.
The first Ability/Trainer passes covered 520/377 families respectively.

Investigated suspicious text and operation overlaps using real card
definitions, explicit board states, controlled coin results, physical card
identities, destination checks and mock call counts. For example, Dimension
Transfer worked with an Item in the discard pile; the generic smoke fixture
had no eligible Item. Such fixture-dependent flags are not treated as bugs.

## Corrected behavior

- Cleffa's Eeeeeeek and related hand-reset attacks shuffle first, draw their
  printed quantity once, then apply the attacker's Sleep condition.
- Twins searches for two cards. Its play restriction does not make an
  unrestricted private search optional.
- Junk Hunt and overlapping Item/Supporter/Energy recovery templates resolve
  a single instruction once.
- Quick Draw, coin-dependent milling, False Swipe and Energy discards honor
  the condition attached to their own clause.
- Coin-based draw, deck search, attachment and Energy discard instructions
  use the number of heads, including zero. Hurricane Call restricts attachment
  to historical Pokémon-EX/Pokémon-GX.
- Barrage O'Clock counts Energy on both Active Pokémon; enhanced coin counts
  from attached Tools are recognized.
- Sneaky Pocket pays its Lost Zone cost before drawing; an empty hand does not
  grant the draw.
- Mountain Scrounging and Never Ever Enough preserve the viewed cards and resolve
  exactly one chosen branch.
- Bottom-of-deck draws use the physical bottom cards while retaining the
  normal draw choreography and statistics.
- Board-dependent draws and Summoning Draw's additional draw use their
  printed condition/count.
- Sage's Riddle gives cards only to the winner of the guess.
- Heart Wink prevents only the affected player's next mandatory turn draw;
  it does not cause the attacker to draw or block ordinary effect draws.
- Devastating Wind, Mischievous Tentacles and Fluorite resolve their
  shuffle/prompt/healing instruction once.
- Miraculous Shine and Time Spiral remove one evolution stage rather than
  falling through into a second devolution handler.
- Time Distortion and Digital Reboot let the player choose the Pokémon and
  number of stages once. Repeated devolution no longer targets a card already
  returned to the hand.
- Fully Singe discards once only from a modern Pokémon ex; ordinary Pokémon
  and historical Pokémon-EX are not valid targets.
- Daunting Eyes shuffles attached Energy into the opponent's deck according
  to its heads count.

## Regression coverage

- `tests/test_reported_legacy_resolutions.py`: original three reports and
  related reset/recovery variants.
- `tests/test_interpreter_transaction_audit.py`: transaction, condition,
  quantity, subtype and physical-card regressions.
- Existing private-search, suppression, full unit and functional engine suites
  are rerun alongside the focused tests.

Final validation: 1,136 unit tests passed, 101/101 functional engine tests
passed. The separate collection-filter patch passed all 16 foil truth cases,
preserving the original instructions and the other 30 filter branches.

No claim is made that every catalog card is now error-free. Conditional
states not represented by these fixtures, alternative printed wordings and
native-client presentation still need targeted gameplay coverage.

Raw scan output remains ignored under `audits/results/`. No account data,
local reward settings, artwork, foil assets or Live-import tools are included.
