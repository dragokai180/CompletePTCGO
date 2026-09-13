# XY rules audit

Updated: 2026-09-13

## Scope and method

Execution sweep: XY0 through XY12, Generations (TwentiethAnn), and Promo_XY.
The initial sweep returned 3,035 passing callback cases, 54 skips, and no
execution errors or reported unimplemented callbacks. Import-only reprints
are not independent cases in this tool. Skips are not approvals.

This is an execution sweep with targeted semantic tests, not an exhaustive
certification of every XY interaction. Several reproduced defects below
passed the smoke harness because it does not assert printed outcomes.

## Reproduced and corrected

- Regice (Ancient Origins), Resistance Blizzard: protection now checks for
  uppercase Pokemon-EX. Ordinary Pokemon and modern lowercase Pokemon ex
  are not blocked. The shared shield applies its attacker predicate to
  attack effects as well as damage.
- Pokemon Ranger (Steam Siege): no longer shuffles the deck. Temporary
  passives now retain attack provenance, allowing Ranger to remove
  attack-granted passives without removing Trainer/Ability-granted ones.
- Greninja (BREAKpoint), Shadow Stitching: now suppresses the opposing
  player's Abilities in play, hand, and discard through their next turn,
  including Pokemon entering later. The player-scoped attack effect can
  be removed by Pokemon Ranger.
- Greninja (BREAKpoint), Moonlight Slash: the optional Energy return is
  decided once before damage; returning it grants the printed 20 bonus.
  Declining retains 60 damage and does not return an Energy.

## Validation

All new defect regressions failed before their respective fixes.
Five regression methods in tests/test_xy_rules_audit.py cover both positive
and negative outcomes, EX/ex distinction, later arrivals, and Ranger.

Full suite: 400 tests passed (python -m unittest discover -s tests -q).
Existing ResourceWarning messages concerning SQLite cleanup were emitted.

## Follow-up: skipped fixtures and compound effects

The neutral-board callback sweep during the follow-up returned 3,032 passes
and 56 skips. Stricter legal-target predicates can increase skips without
introducing a regression. Those skips now have valid, outcome-asserting
scenarios in test_xy_completion.py, test_archie_maxie.py and
test_trainer_followup_audit.py; the neutral-board sweep itself is not changed
to pretend those prerequisites are present.

Covered prerequisite families include public-pile recovery, Blacksmith,
Tool removal/retrieval, Target Whistle, Revive, Mega Turbo, Mega Catcher,
Devolution Spray, status healing, Ace Trainer, Delinquent, Rough Seas,
All-Night Party, Puzzle of Time, Drive Change, Tear Away, Mega Boost,
Wonder Lock, Burning Road, Victory Kiss, Purifying Fire, Stand In and
Farewell Letter. Tests include the affected XY printings and positive and
negative cases rather than merely checking callback completion.

Additional corrections:

- Pokemon Ranger now tracks attack provenance in turn-state restrictions,
  forced coin checks, damage modifiers, bonus-prize watches and GX locks.
  It preserves Trainer/Ability effects, damage, Special Conditions, history
  and spent once-per-game tokens.
- Item reminder text no longer contaminates recovery predicates.
  Revitalizer selects Grass Pokemon; Fossil Excavation Kit selects only
  its three named Fossils.
- Blacksmith and other public-pile attachment effects can resolve with fewer
  Energy cards than the printed maximum; this does not relax discard costs.
- Puzzle of Time distinguishes a single copy (reorder three cards) from a
  pair (recover two), consumes the second copy, and excludes both played
  copies from recovery.
- Trick Shovel selects either nonempty deck, reveals only to the acting
  player, and allows declining the discard.
- Hand Control reveals the opponent's hand and permits declining. A selected
  playable Supporter resolves for its owner, with choices made by the attacker,
  then goes to its owner's discard; the attacking player does not draw its cards.
- Mist Purge recognizes Special Energy for both its bonus and team healing.
- Solar Birth attaches searched Energy to the Pokemon it actually benches.
- Burning Icicles and Frosty Thunder enforce their additional Energy
  requirements for Bench damage.
- Lock-On's additional damage applies after Weakness/Resistance and expires.
- Vanishing Strike applies its Stadium-dependent bonus and protection bypass.
- Stardust grants protection only after an actual Special Energy discard.
- Magical Symphony checks whether a Supporter was played.
- Link Fusion adds the distinct named Bench bonuses cumulatively.
- Energy Glide and Quiver Dance perform their secondary effects only after
  successful attachment.
- Flare Up requires ten Fire Energy cards in the discard pile.
- Tidal Storm moves Energy by provided units and damages only uppercase
  Pokemon-EX on the opposing Bench.
- Coordinate handles distinct eligible Benched recipients.

The new suite also asserts Metal Rain's repeated target selection,
Jagged Saber's recipient healing, Dragon Dance's non-stacking lifetime,
Rare Candy evolution timing, typed Special Energy restrictions, Double Dragon
Energy cost payment, and Burning Energy's attack-only reattachment.

## Follow-up validation

43 new regression methods in tests/test_xy_completion.py.
Final full-suite run: 462 tests passed
(`python -m unittest discover -s tests -q`).

Exact-text instrumentation sweep:

- 1,323 attack families: 1,320 observed; Flare Up and Grass Fire require
  missing fixture resources, and Mist Purge requires attached Special Energy.
  Dedicated tests assert their positive and negative outcomes.
- 70 activated Ability families: 70 observed.
- 69 Trainer families: 64 observed; Revitalizer, Fossil Excavation Kit and
  Ace Trainer lack prerequisites on the neutral board; Ranger has no attack
  restrictions to clear there. Puzzle's single-copy branch intentionally
  does not recover cards. Dedicated tests cover all five flagged families.

These instrumentation counts are execution evidence, not proof that every
printed clause or cross-era combination has been validated.

## Verification limits

The skipped-fixture coverage and Ranger turn-state work are addressed.
An exhaustive outcome matrix for every printed effect/reprint and every
cross-era interaction is not claimed. Native two-client multiplayer and
animation validation remain unperformed.

No server restart, commit, or push was performed.
