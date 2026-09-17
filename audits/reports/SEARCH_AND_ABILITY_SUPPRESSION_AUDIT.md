# Deck-search and Ability-suppression audit — 2026-09-16

## Scope

Follow-up to the full-catalog semantic audit, prompted by Aero Blitz selecting
only one card and Shadow Stitching suppressing Old Cemetery. This pass combines
a catalog-wide automated sweep with outcome regressions for related rule
families. It is not a manual playthrough of every printing or every interaction.

## Confirmed causes and changes

### Printed searches

The attack fallback used a numeric-only expression and defaulted to one card
when the text said "up to 2". Separate attack/Ability branches also disagreed
about card filters, quantities, optional selections and public revelation.

The shared search implementation now handles:

- Fixed, "up to", "any N", coin-dependent and Bench-capacity quantities.
  Aero Blitz requires one or two cards without revealing them when the deck
  is nonempty; zero is only possible when no cards remain in the deck.
- Supporter, Tool, Special Energy, typed Pokemon/Energy, stage, named Pokemon,
  owner-tagged Pokemon, battle-style and printed-HP restrictions. Filter
  parsing stops at the search descriptor rather than consuming later text
  about another Pokemon. Colorless symbol notation is accepted.
- Stage 1/2 Pokemon explicitly put on the Bench are not incorrectly restricted
  to Basics. Mirage Step, Psy Call, Spreading Light, Afterimage Assault,
  Division, Multiply, Bee March, Come Along and Flock have outcome coverage.
- Searches for different types or different names exclude already-selected
  types/names, not just the physical card. Covered by Energy Salon and Call
  for Greatness.
- Compound searches preserve one slot per requirement: Diamond Gate selects
  a Supporter and a Stadium; Dratini's Signs of Evolution selects one of each
  named evolution; Roll Call selects the named Pokemon separately.
- Named effects accept the requested Pokemon, not any unrelated card.
  Warble and Fraxure's Signs of Evolution have explicit filter regressions.
- Older "show it/them to your opponent" revelation wording, alongside "reveal".
- Two-heads conditions and variable coin quantities. A failed coin-gated
  search no longer opens the deck or shuffles it anyway.
- Super Growth selects the player's Grass Pokemon and can complete both
  evolutions. Ultra Evolution puts the named evolution into play rather than
  adding it to the hand. These paths retain effect-driven evolution and a
  single final shuffle.

Searches with a specified criterion can still fail. Unrestricted, unrevealed
fixed-quantity searches retain their required minimum. Unrestricted "up to"
searches require at least one card when available, including attack effects.
This exception is explicit in the official February 2026 rules update:
https://professorprogram.pokemon.com/news/11473085

### Ability suppression and effect identity

Trainer/Stadium triggers reuse the internal Ability callback class. The
suppression check previously treated that implementation detail as a Pokemon
Ability, incorrectly stopping Old Cemetery under Shadow Stitching/Hex Maniac.

- Pokemon-only suppression no longer suppresses non-Pokemon callbacks or
  Tool-granted effects. Genuine Abilities on Fossils treated as Pokemon are
  not broadly exempted.
- Trigger effect classification distinguishes a Pokemon Ability from a
  Stadium callback, so Pokemon Ability immunity does not shield a target from
  a Stadium effect.
- Ability-based suppressors disabled by an attack, Trainer or Stadium stop
  contributing their suppression. Shadow Stitching can disable an opposing
  Garbotoxin without leaving that Garbotoxin suppressing the attacker's side.
- A disabled Tool Concealment no longer keeps Tools disabled. Tool Jammer's
  own Tool effect remains effective under Pokemon Ability suppression.
- Old Cemetery checks effective Pokemon types, including in-play type changes.
- Existing Shadow Stitching duration, later-arrival and Pokemon Ranger
  regressions remain passing.

## Verification

- Final full unittest suite: **942 passed**, including 20 new test methods
  with parameterized outcomes and catalog-family loops in
  `tests/test_search_and_suppression_audit.py`.
- Catalog: 14,828 cards. Printed Pokemon contracts: 12,386 comparisons,
  zero unmatched records, zero discrepancies, zero identity collisions.
- Broad runtime sweep: 10,460 probes, 10,318 PASS and 142 conditional SKIP;
  no execution failures.
- Full shared-effect tracing: 4,981 attack families, 523 Ability families and
  377 Trainer families. Alerts are conditional-fixture/trace limitations
  already described in `FULL_CATALOG_SEMANTIC_AUDIT.md`, not silently counted
  as successful semantic verification.
- Final search-focused tracing: 302 attack families with observed operations;
  70 Ability families (69 observed, one conditional skip); 88 Trainer families
  (84 observed, four conditional skips).
- Passive inventory: 789 families / 1,254 printings; 648 mapped and 141
  high-risk-review labels, no unmapped families. Mapping alone does not prove
  a rule outcome.
- `git diff --check`: clean.

The generic probes can observe a shuffle even when a search predicate or
quantity is wrong. That limitation explains why the new regressions assert
actual selected cards, destinations, counts and exclusion rules instead of
relying only on traced operations. Conditional skips are not passes.

## Reproduction

Run from the repository root with the project's Python environment:

```text
python -m unittest tests.test_search_and_suppression_audit
python -m unittest discover -s tests
python -m spirit.tools.audit_card_contracts --source-dir ../work/standard-current --external-catalog-dir ../outputs --json audits/results/card-contracts-search-followup-2026-09-16.json
python -m spirit.tools.audit_sm_swsh_runtime --set-pattern ".*" --json audits/results/runtime-search-followup-2026-09-16.json
python -m spirit.tools.semantic_effect_audit --kind attack --match "search your deck" --json audits/results/search-attacks-2026-09-16.json
python -m spirit.tools.semantic_effect_audit --kind ability --match "search your deck" --json audits/results/search-abilities-2026-09-16.json
python -m spirit.tools.semantic_effect_audit --kind trainer --match "search your deck" --json audits/results/search-trainers-2026-09-16.json
python -m spirit.tools.passive_semantic_audit --top 0 --json audits/results/passives-search-followup-2026-09-16.json
```

Raw generated reports stay in the ignored `audits/results` directory. Existing
unrelated work, account data, configuration, artwork and bundles were preserved.
No server restart or GitHub push was performed.

Native-client multiplayer prompts and the full combinatorial space of competing
continuous effects are not exhaustively covered. This completes an audit pass,
not a guarantee that every remaining card interaction is bug-free.
