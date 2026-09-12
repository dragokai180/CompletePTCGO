# XY rules audit

Date: 2026-09-12

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

## Remaining work

- Build valid fixtures for the 54 skipped execution cases.
- Continue outcome-level review of every printed effect and reprint;
  smoke success alone does not establish semantic correctness.
- Extend attack-effect provenance beyond temporary passives to the other
  turn-state restriction collections before treating Ranger as exhaustively
  audited.
- No client multiplayer or animation validation was performed in this pass.

No server restart, commit, or push was performed.
