# Generic interpreter: conditional clauses and KO reactions

Date: 2026-09-17

This continues `GENERIC_TEXT_AND_REPRINT_FOLLOWUP.md`. It audits imported
exact-text families and corrects confirmed semantic mismatches; it is not a
claim that every card combination has been exhaustively verified.

## Discovery coverage

The discovery runs covered 4,981 attack families, 520 Ability families,
377 Trainer families and 789 passive-text families. These are distinct texts,
not counts of independently tested printings. Passive classification found
648 mapped mechanisms and 141 high-risk review candidates; a mapping is not
proof of correct behavior.

The final attack smoke run completed without exceptions: 4,947 observed,
20 partial/suspect, seven without an observed effect and seven skipped by
their activation conditions. A smoke board deliberately cannot satisfy every
card's prerequisites. Newly enforced prerequisites and conditional effects
can therefore increase these flags without representing regressions.

Examples of fixture-dependent flags include damaged Vespiquen for Enraged
Assault, ten discarded Fire Energy for Flare Up, opposing Grass Pokemon for
Grass Fire, Illumise for Illumisile, damaged opposing Pokemon for Moon's
Invite, opposing discarded Pokemon for Supernatural Dance, and promotion or
evolution history for Tandem Shock and Tentavolve. Nadir Needle,
Improvisational Performance and Primordial Boom have positive and negative
directed regression tests rather than relying on the smoke board.

## Corrections

### Printed prerequisites and conditional attack clauses

- Imported attacks now install explicit activation predicates for supported
  printed restrictions: Prize counts, first-turn restrictions, required
  Pokemon/types on the Bench, damage or Special Conditions, Lost Zone counts,
  and attacks used during the owning player's previous turn. Execution and
  copied attacks revalidate these predicates as well as the action menu.
- Angelite checks the owning player's previous attack even if its previous
  user left play; it can resolve against one remaining Benched Pokemon and
  respects protection from attack effects.
- A dedicated conditional-clause resolver evaluates public prerequisites
  before the attack changes them. It handles only complete recognized texts;
  unknown text is delegated to the existing specialized/generic resolvers.
  Coin flips, searches and payments are not assumed to have succeeded.
- Hand and Prize thresholds, damage counters, status, typed Pokemon in play,
  Stadium ownership, Energy units, prior attacks and promotion history now
  control their printed bonuses and secondary effects. Examples include All
  Out, Sledgehammer, Turning Point, Chain-Crazed, Crazy Hammer, Powerful
  Friends, Charged Web and Gulf Stream.
- Independent clauses remain independent: Link Fusion can gain both printed
  bonuses; Primordial Boom distinguishes the player's Stadium from the
  opponent's; Improvisational Performance applies only its matching branch.
- Legacy named-source wording and status removal are preserved, including
  Poison Effect and Wake-Up Slap. Modern Pokemon ex/V and legacy Pokemon-EX
  remain distinct qualifiers.
- Staggering Steps and Untamed Punch no longer apply self-confusion outside
  the relevant coin/damage condition. Caturday sleeps only after drawing;
  Poisonous Musculature poisons only after a successful Energy attachment;
  Hypno Headbutt asks before its optional damage/self-sleep branch.
- Turn state records Tools actually attached from hand and attack damage
  received while Active. Whip Expert and related clauses no longer infer
  those facts from merely having a Tool or damage. Typed attack-KO history
  excludes Checkup and non-attack counters.

### Survival and Knock Out reactions

- Sturdy and Resolute Heart leave the Pokemon in play at the printed HP.
  Only survival Tools that explicitly discard themselves do so.
- Tangled Feet and Adrena-Pheromone require their printed status/Energy
  prerequisite before rolling the prevention coin. Active-only retaliation
  recognizes both old and modern wording.
- Destiny Burst waits for an actual attack KO rather than predicting one
  before survival effects resolve. Its counters are not attack damage.
- Lamentation does not discard twice on a lethal hit. Cursed Duster waits for
  the KO rather than triggering whenever damage is received.
- Electrical Grounding supports its printed Energy wording, including
  eligible Special Energy; Basic-only qualifications remain where printed.
- Heavy Baton validates the effective retreat cost at the time of the KO.
  Diver's Catch validates the Pokemon's type at that same moment.
  KO hooks receive snapshots of types, retreat cost and provided Energy types
  before stacks leave play, and cannot transfer a card already recovered by
  another effect.

## Regression coverage

Final full-suite result: **1,028 tests passed** in 116.6 seconds, including
37 new directed tests in this continuation. `git diff --check` found no
whitespace errors. The installer tests deliberately simulate unavailable
networks and missing textures; their diagnostic output is expected.

New directed test modules:

- `tests/test_generic_attack_clauses.py`: printed prerequisites, private
  search outcomes, coin/status sequencing, copied attacks and Angelite.
- `tests/test_attack_public_state.py`: thresholds on both sides of each
  boundary, independent bonus clauses, legacy wording, Energy units,
  type/subtype distinctions, state history and conditional Bench damage.
- `tests/test_generic_passive_clauses.py`: survival, conditional shields,
  actual-KO timing, single reactions, Energy recovery and pre-KO snapshots.

Run `python -m unittest discover -s tests` for the full suite. Raw discovery
JSON is local-only under `audits/results/`. The existing audit tools remain
useful for discovery, but observing one draw, damage event or attachment does
not certify all clauses, choices or multi-turn interactions of a card.

No server restart, commit or GitHub push was performed for this follow-up.
