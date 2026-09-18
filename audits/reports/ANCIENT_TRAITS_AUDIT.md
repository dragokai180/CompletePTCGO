# Ancient Traits audit — 2026-09-18

The initial test-only audit identified two defect families. Both were corrected
after the user's follow-up request. A subsequent Compendium interaction audit
is documented in [Omega Barrier](OMEGA_BARRIER_COMPENDIUM.md).

## Scope and execution

- Compared the loaded passive text for all 58 Ancient Trait printings in XY5,
  XY6, XY7 and XY Promos against the local pokemon-tcg-data snapshot.
- Exercised the ten trait families through headless engine tests. Coverage
  includes legal actions, actual manual attachments, evolution, healing,
  damage, attack resolution, promotion after a knockout and a Trainer effect.
- Initially ran 17 test methods: 14 passed; 3 failed with seven failed subcases/assertions.
  These failures represented two defect families, not seven independent bugs.
- After the initial fixes, all 23 Ancient Trait regression tests passed. The combined
  Ancient Trait, XY and search/suppression suite passes all 93 tests.
- Initial full regression run: `python -m unittest discover -s tests -q` completed
  successfully with 1,283 tests (exit status 0).
- Final run, including the Compendium corrections and Wyndon regression:
  all 1,295 tests pass (143 seconds, exit status 0); 24 cover Ancient Traits.
- The 58-print metadata comparison uses an optional local pokemon-tcg-data
  snapshot and is skipped when that snapshot is absent. It ran in this audit.
- The client UI, animation, and every possible card interaction were not tested.
- Reproduction: `python -m unittest tests.test_ancient_traits_audit -v`.
  The original failing assertions remain as passing regressions.

## Confirmed findings and fixes

### 1. All three theta Max printings inherit a different Ancient Trait

| Printing | Expected | Loaded instead | HP after evolving in test |
| --- | --- | --- | --- |
| Primal Kyogre-EX AOR 96 | theta Max | alpha Growth | 80/240, not 240/240 |
| Primal Groudon-EX AOR 97 | theta Max | omega Barrier | 80/240, not 240/240 |
| M Rayquaza-EX AOR 98 | theta Max | delta Evolution | 70/220, not 220/220 |

Each script cloned a previous version with the same attacks, but a different
Ancient Trait. `mechanics_signature` in `spirit/tools/import_standard_sets.py`
omitted `ancientTrait`; the XY importer uses this signature when choosing
reprint bases, incorrectly treating these versions as mechanically identical.

Reproduced by evolving a damaged Kyogre-EX, Groudon-EX or Rayquaza-EX from hand
using the real evolution engine. Damage was preserved instead of fully healed.
The other 55 printings already had the expected Ancient Trait text.

The three printings now explicitly replace the cloned passive with theta Max,
without modifying their original versions. The importer signature now includes
Ancient Traits. Evolution healing also receives its source zone, so theta Max
works for effect-driven evolution from the deck while Regenerative Energy keeps
its printed from-hand restriction. Tests verify the obsolete Growth, Barrier
and Evolution traits are no longer granted to these theta Max versions.
The final hook review also updated Wyndon Stadium's signature and retained its
from-hand restriction. An additional engine test evolves Aegislash V into VMAX
from hand and from the deck to verify both outcomes.

### 2. Omega Barrier does not protect attached Energy from Crushing Hammer

Reproduced with Primal Groudon-EX PRC 86, attached basic Energy and the
opponent's actual Crushing Hammer effect. A forced heads result followed by a
valid Pokemon/Energy selection moved the Energy to the discard pile.

The Trainer shield checked whether the affected entity was the Pokemon itself.
When the discard primitive checks the attached Energy entity, this identity
check did not match. The shield now resolves the affected card's Pokemon holder,
without extending protection to detached cards or exempt Stadium/Tool sources.

The actual Crushing Hammer regression now leaves the Energy attached. Additional
tests cover attached Tools, opposing Supporters, own effects, Stadiums, Tool
sources and attack-driven Energy discard.

## Passing tested behavior

- Alpha Growth: second normal attachment is restricted to the same Pokemon;
  a third is unavailable. Effect-driven attachment does not spend that allowance.
- Alpha Recovery: healing doubles, does not spill to another Pokemon and caps at maximum HP.
- Delta Evolution: permits a matching evolution on the first turn, including a newly played Basic.
- Delta Plus: extra Prize modifier applies to opposing attack-damage knockouts,
  including Benched targets; does not apply to unrecorded attack damage or own Pokemon.
- Delta Wild: 20 reduction applies to the four printed attacking types,
  after weakness, and does not reduce damage counters.
- Theta Double: two Tool slots are available; a third Tool cannot target that Pokemon.
- Theta Stop: opposing Ability damage counters are prevented; own effects are not.
- Omega Barrage: two attacks resolve, other card plays are unavailable between
  them, and the second attack is available after a knockout and opposing promotion.
- Omega Barrier: direct Item/Supporter target shielding and owner distinction work;
  Stadiums and Tools remain exempt in the tested shield checks.
- Card-level trait passives remain active under Hex Maniac and opposing Garbotoxin.

Ancient Traits are not Abilities; the distinction is documented in the
[official rulebook](https://assets.pokemon.com/assets/cms2-nb-no/pdf/trading-card-game/rulebook/swsh12_rulebook_en.pdf).
