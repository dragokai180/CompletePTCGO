# Full-catalog semantic audit — 2026-09-16

## Scope and evidence

This pass covers the complete loaded catalog, not just the four reported effects.
It separates data contracts, broad execution probes, text-family tracing, and
scenario tests that assert actual rule outcomes. A passing smoke probe only means
that its fixture executed without an exception; it is **not** evidence that every
clause of that card works in every matchup.

- Catalog identity and registry checks: 14,828 cards.
- Printed Pokemon contracts: 12,386 printings, no unmatched records, no remaining
  contract discrepancies, and no duplicate image or collector slots.
- Broad runtime pass: 10,460 probes; 10,318 executed, 142 conditional skips.
  Skips are not passes and remain visible in the generated report.
- Text-family attack tracing: 4,981 families (4,966 observed, 9 partial suspects,
  6 without a traced event).
- Activated-Ability tracing: 523 families (514 observed, 1 partial suspect,
  8 fixture skips).
- Trainer tracing: 377 families (359 observed, 1 partial suspect,
  2 without a traced event, 15 fixture skips).
- Final passive inventory: 789 families / 1,254 printings; 648 mapped,
  141 marked for high-risk review, no unmapped families. A mapped hook is not
  proof of semantic correctness.
- Outcome regressions are in the full unittest suite and in the new
  `test_catalog_startup_contracts` and `test_semantic_catalog_findings` modules.
  Final run: **920 tests passed**, including 29 newly added tests.

The printed-contract sources are the repository's English card JSONs, the local
recent-set records and the original Pobre TCG catalog where those JSONs stop.
This audit does not independently authenticate every upstream record. Actual
official errata override stale data: for example, Cinderace SWSH 36 has a retreat
cost of **two**, not one.

Reference: [Official TCG errata](https://play.pokemon.com/en-us/resources/documents/tcg-errata/).

## Root causes of the reported regressions

### Rule registration was being overwritten during bundle generation

The startup bundler imported card scripts a second time through independent module
execution. That replaced the canonical definitions and Ability objects after the
loader had normalized them. Tests using only the loader could pass while server
startup silently restored the raw, incorrect definitions.

Bundle generation now reads the loader's existing models and definitions. A
regression snapshots the entire card and Ability registries and verifies that
bundle generation changes neither. It also verifies the exact image mappings.

### Mystical Fire and other source-zone mistakes

The importer inferred hand/discard activation from incidental mentions of those
zones in effect text. Drawing cards *into your hand* does not mean that Delphox
can activate from the hand.

Only explicit bearer-location clauses permit out-of-play activation. Forty raw
declarations were corrected, together with the shared normalizer and importer.
Mystical Fire is tested from hand, deck, discard and Bench, including drawing to
six and refusing activation at six. Legitimate hand/discard powers remain legal:
Propagation, Restoration, Emergency Surfacing, Beedrill, Greninja-GX, and others.

### Tepig LTR 25 was an artwork identity collision

Tepig itself was already defined as 70 HP / one Prize. Radiant Collection RC25 is
Meloetta-EX, with 110 HP / two Prizes. Both had been assigned image slot 025,
making one card appear to be the other.

All 25 Radiant Collection cards now use the client's separate slots 116–140,
while their printed card-number text remains RC1–RC25. Tepig remains slot 025.
GUIDs and saved decks were not rewritten. A deck that actually contains the
Meloetta-EX GUID will now display Meloetta-EX rather than being converted to Tepig.

### Red Banquet and Damage Swap

The previous committed corrections were revalidated rather than rewritten:
five Red Banquet tests cover attack-KO-only extra Prizes, independent players'
Altered Creation bonuses, blocked damage and zero-Prize substitutes; six damage
transfer tests cover ownership, source-counter selection, target selection and
the requested target-HP limit. Startup registration must preserve these rules.

## Additional corrected families

| Area | Correction |
| --- | --- |
| Missing attack data | Watchog BLW 79 now has Confuse Ray and Hyper Fang; Duskull SFA 18's Come and Get You is an attack, not an activated Ability. |
| Prize classification | Dialga-GX UPR and reprints, 17 Mega-era promo printings, and Mega Eelektross ex stage metadata. |
| Printed costs | Applin, Tatsugiri, Genesect, N's Darumaka/Darmanitan/Reshiram, Blaziken and inherited printings; Cinderace's official two-Energy retreat erratum. |
| Attack text | Blood Moon, Cruel Arrow and Irritated Outburst had missing/misplaced text. |
| Coin multipliers | Shared fixed-coin damage recognizes both “times the number of heads” and “for each heads”; all shared fixed-coin families are exercised across possible head counts. |
| Attack versus Ability | Dreaming Tone, Electrified Bite Mark and Spark Trap now create attack effects, not fake Abilities. Original-defender and next-turn behavior is tested. |
| Continuous effects | Blaziken's Double Type applies only in play and respects suppression. |
| Up-Tempo | The bottom-deck cost is considered before checking whether drawing to five can occur. |
| Seasoned Skill | Blood Moon is identified by the actual attack, not an exact unmodified five-Colorless cost; other cost modifiers no longer disable the discount. |
| Subjugating Chains | Excludes every Pecharunt ex printing, and uses live Pokemon types for legal Darkness targets. |
| Named searches | Arrokuda's Flock accepts other Arrokuda printings and remains correct when copied; Shiinotic checks the Stadium's name rather than one GUID. |
| Reprint metadata | Multi-Weakness LEGEND cards retain both Weaknesses through reprinting and import. |
| Tools and timing | Lum Berry and Sitrus Berry resolve at end of turn, before Checkup. Tucked evolution stacks work, and Sitrus discards itself rather than another Tool. |
| Ability-based attack locks | Power Saver, Act Freely and Kinda Lazy are passive restrictions, not copied attack conditions. Ability suppression, boundary counts, Stadium removal and alternate printings are tested. |

The new contract tool also flags Abilities without any implementation, with a
small explicit allowance for setup/entry rules and Additional Order, which are
implemented by their owning subsystem.

## Text-trace alert disposition

Trace alerts were not silently converted to passes. They were checked against
outcome tests and the following scenario families:

- Attacks: Enraged Assault, Ninja Fang, Pheromone Poison, Illumisile,
  Tentavolve, Moon Invite, Flare Up, Grass Fire, Mist Purge, Iron Hand,
  Iron Fist, Poison Absorption, Redirected Sunlight, Retaliatory Incisors,
  and Slurp Slurp.
- Abilities: Dimension Transfer (both coin outcomes), Up-Tempo,
  Flaring Magic (cost before drawing), Beckoning Tail, Rumbling Engine,
  Shell On, Wash Out and Voltage Increase.
- Trainers: Pokemon Ranger and Channeler clear state rather than move cards;
  Puzzle of Time's modes, Electrocharger, Lure Ball, Tag Switch, Evelyn,
  Dana, Dusk Stone, Beast Ring, Aether Foundation Employee, Great Catcher,
  Revitalizer, Fossil Excavation Kit, Ace Trainer, Black Belt, Twins and
  Full Heal require their relevant state/resource fixtures.
- Passive review uses the existing era-specific regression modules and
  `SM_SWSH_AUDIT_COVERAGE.md`, plus this pass's holder, suppression, timing,
  cost-modification and identity scenarios.

These checks include positive and negative outcomes, owner/opponent distinctions,
optional choices, costs, alternate prints, timing and copied-attack behavior where
relevant. They do not constitute a manual playthrough of every card combination.

## Reproduction

From the repository root, using the project's Python environment:

```text
python -m unittest discover -s tests
python -m spirit.tools.audit_card_contracts --source-dir ../work/standard-current --external-catalog-dir ../outputs --json audits/results/card-contracts-2026-09-16.json
python -m spirit.tools.audit_sm_swsh_runtime --set-pattern ".*" --json audits/results/runtime-full-catalog-2026-09-16.json
python -m spirit.tools.semantic_effect_audit --kind attack --json audits/results/semantic-full-attacks-2026-09-16.json
python -m spirit.tools.semantic_effect_audit --kind ability --json audits/results/semantic-full-abilities-2026-09-16.json
python -m spirit.tools.semantic_effect_audit --kind trainer --json audits/results/semantic-full-trainers-2026-09-16.json
python -m spirit.tools.passive_semantic_audit --json audits/results/semantic-full-passives-2026-09-16.json
```

The optional sibling source directories are local audit inputs, not runtime
dependencies. Generated JSON reports belong in the ignored `audits/results`
directory. Counts for text tracing record the audit phase; later regression fixes
can change classifications when the probes are rerun.

## Deployment and limits

No accounts, saved decks, configuration, original foil changes or running server
were changed by this pass. No GitHub push was made. A fresh server start must
load the corrected registries and rebuild changed Radiant Collection mappings;
an already-open client must reconnect to obtain updated archetypes/bundles.

This is a completed catalog-wide audit pass, **not a guarantee that all game
semantics are now bug-free**. Conditional smoke skips, native-client rendering,
real multiplayer prompt ordering and the combinatorial space of interactions are
not replaced by the automated counts above. The startup regression specifically
closes the gap where tests could pass but bundle construction undid their rules.
