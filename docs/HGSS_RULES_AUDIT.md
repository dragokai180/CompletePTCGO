# HGSS rules audit — semantic passes

Date: 2026-09-12

## Scope and status

HeartGold & SoulSilver (`HGSS1`), Unleashed (`HGSS2`), Undaunted (`HGSS3`),
Triumphant (`HGSS4`), Call of Legends (`COL`), and HGSS Black Star Promos
(`Promo_HGSS`). This is a rules audit, not a foil/art audit.

**Status: server-side audit pass completed for all six sets.**

The final pass reviewed the remaining attack families, activated powers,
continuous rules, Trainers, LEGEND play and end-of-effect resolution. This is
not a claim that every possible cross-era combination or native-client visual
has been exhaustively tested. The verification limits are listed below.

The initial semantic smoke scan exercised 470 attack cases, 48 power cases,
and 44 Trainer cases. Its event-based checks reported an observed operation
for every attack and power, and 43 Trainers; Full Heal was skipped on the
unconditioned baseline board. These results did not prove correct amounts,
targets, costs, order, or eligibility. Manual review found errors despite
those apparently successful results.

## Changes in this batch

### Eligibility and passive scope

- Enforce the printed Special Condition restriction on legacy Poke-Powers.
  Do not apply that restriction to modern Abilities or powers without it.
- Recognize the printed Pokemon name in Active/Bench requirements, including
  Forest Breath and Retreat Aid.
- Reject draw powers when the deck is empty or the hand already meets the
  printed draw-until limit.
- Afterburner requires a matching Energy in the public discard pile.
- Damage-counter removal powers require an applicable damaged Pokemon.
- Sweet Sleeping Face protects its holder only while Asleep.
- Shell Barricade protects Shuckle only on the Bench.
- Red Armor requires Special Energy on the attacker, not the defender.
- Defense Sign protects the owner's Grass Bench, not other types or the Active.
- Green Shield removes Weakness from allied Grass Pokemon, without requiring
  Energy on them, instead of affecting only Metapod.

### Attack and power resolution

- Dragon Steam checks the opponent's entire board for Fire Pokemon and changes
  its base damage before Weakness, Resistance, and other modifiers.
- Flare Destroy discards one Energy from each Pokemon. Removed a second generic
  defender-discard pass which could repeat the discard and bypass coin gates.
- Afterburner places its damage counter on the recipient after a successful
  attachment, not when attachment fails.
- Second Sight lets the acting player choose either deck. Corrected the HGSS1
  printing's locally stored text as well as resolution for the COL printing.
- Poison Moth Wind applies Poison to the correct side for each coin result.
- Blissful Nurse heals first, then discards Energy from the Pokemon that had
  damage. Energy on previously undamaged Pokemon remains attached.
- Hustle Step and Sunny Heal now resolve their damage-counter removal clauses.
- Stardust Song flips three coins and attaches the corresponding Psychic Energy
  cards to Jirachi, rather than skipping the flips or offering arbitrary targets.
- Energymite queues Electrode's Knock Out before distributing the viewed Energy;
  Electrode cannot be an attachment target. The unchosen cards are discarded.
- Ocean Grow is an on-entry trigger: attach all Energy among the five viewed
  cards to Lugia LEGEND and discard the rest. Full two-half play integration is
  still pending the separate LEGEND review below.
- Recognize legacy Energy attachment wording without the optional word `card`.
- Match `move` as a word, not inside `remove`, and recognize Psychic Energy in
  the legacy typed movement family.

### Trainers and errata

- Strip the HGSS Supporter rule reminder before parsing its actual effect.
  Previously the reminder's word `Supporter` could turn Pokemon Collector's
  search into a Supporter search.
- Flower Shop Lady selects three Pokemon and three basic Energy separately,
  resolving the available amount of each category rather than three combined.
- Good Rod, Junk Arm, Dimension Transfer, Allergy Flower, and Fake Tears use
  the Item category rather than all Trainer subclasses.
- Junk Arm needs an eligible Item other than Junk Arm already in the discard.
- Apply current Rare Candy rules to its HGSS printing by reusing the existing
  implementation: Stage 2 only, no first-turn or same-turn Basic evolution.
- Apply PlusPower's errata to its HGSS printing by reusing the BW implementation:
  it does not attach, and its +10 per copy applies for the turn after switching.
- Correct Defender's rule text to cover attack damage from either player.
- Restore the optional wording of Unown CURE.

## Second pass: passive conditions and events

Reproduced and corrected:

- Psychic Float granted free retreat without Psychic Energy on the Active.
  It now checks the owner, Active position and Energy on that Pokemon rather
  than Energy elsewhere on the board.
- Tangling Tendrils (Victreebel) and Tenacity (HGSS promo Wobbuffet) reduced
  retreat instead of increasing it. The parser found `less` inside `Colorless`.
  It now matches the comparative word separately and limits this surcharge
  to the opposing Active while the source is Active.
- Ultra-Thick Skin reduced damage without Energy attached to Phanpy. An
  actual Energy card is now required; other attachments do not qualify.
- Exoskeleton and Ultra-Thick Skin incorrectly ignored attacks from the
  owner's own Pokemon. Reductions without an opponent-only clause now apply
  to attack damage from either side. Counter placement remains unaffected.
- Energy Signal and Eye of Disaster checked for the power title inside its
  rules text, so the actual HGSS definitions never matched. They now recognize
  the printed clauses. Roserade observes the correct recipient, Energy type,
  owner's turn and Special Condition restriction, and permits declining the
  power. Rainbow Energy satisfies both of its independent type clauses.
- Heal Block also prevented moving damage counters because that operation
  called the healing primitive. Moving counters now updates HP without healing
  locks, healing multipliers, healing statistics or healed-this-turn flags.
  Effect shields and explicit prohibitions on moving counters remain checked.
- Earthquake and Mini Earthquake omitted damage to the owner's Bench. The
  shared spread-damage family now handles either side and keeps each clause's
  coin gate, fixing Blizzard's heads/opposing-Bench and tails/own-Bench split.
  An integration test confirms Exoskeleton prevents Earthquake damage to a
  benched Donphan while unprotected allies still take the printed damage.

Verified without changing the underlying rules:

- Dittobolic limits the opponent to four Benched Pokemon, lets that opponent
  choose the discarded full stack and does not award prizes for that discard.
- Catastrophe sends the opposing Knocked Out Pokemon and its evolution cards
  to the Lost Zone while attachments are discarded. It works for non-attack
  Knock Outs and stops applying when Gengar is on the Bench.
- Energy Healer heals only the Onix receiving the owner's from-hand attachment;
  another Pokemon's attachment and the non-hand attachment primitive do not
  heal it.
- Sacred Rainbow preserves Double Colorless Energy's two units while changing
  their type on Ho-Oh LEGEND, and does not change another Pokemon's Energy.
- Pheromone Stamina counts allied Nidoqueen only and updates when one leaves.

Added 16 regression tests in this pass (45 HGSS tests in total), including
multi-case tests for ownership, position, Energy type, turn and optional use.
LEGEND pairing/play itself remains outside these passive callback tests.

## Completion pass

### Compound attacks and copied attacks

- Added a scoped HGSS resolver for compound texts whose clauses cannot safely
  be inferred independently. Copied attacks carry their printed set and name,
  while payments, damage and self-references use the actual attacking Pokemon.
- Corrected coin totals, partial results, typed Energy counts, hand/field counts,
  chosen Bench targets and dependent Special Conditions. Dedicated positive and
  negative scenarios cover Illumisile, Enraged Assault, Ninja Fang, Tentavolve
  and Pheromone Poison instead of accepting their empty neutral-board traces.
- Corrected distributed counters (Solar Suggestion and Moon's Invite), optional
  choices, per-donor quotas and invalid destinations. Moving counters is not
  healing and does not apply Weakness, Resistance or damage multipliers.
- Corrected the chosen side of milling, spread damage, healing and hand effects,
  including Destructive Tsunami, Volcano Stomp, Eruption, Bench Manipulation,
  Plead, Selfish Draw, Recover, Energy Bloom and Future Sight.
- Corrected hand-return Energy payments, coin-dependent discards, Lost Crisis,
  Thunder Fall and attacks that shuffle the complete attacking/defending stack.
- Verified turn expiry and scope for Bulk Up, Headwind, Close Combat, Mach Wind,
  Leaf Guard, Moonlight Fang, Time Circle, Psychic Lock and Afterimage Strike.
- Self-damage from HGSS attacks now applies the actual user's Weakness and
  Resistance. This matters when a Psychic-weak Mew copies Balloon Tackle.

### Powers, passives and Trainers

- Lost Link reads both Lost Zones but excludes LEGEND halves: a half outside
  play does not provide a usable attack. Evolution Memories reads only the
  owner's in-play Eeveelutions.
- Portrait respects the copied Supporter's public prerequisites, tolerates
  definitions without an extra condition function and leaves the physical
  Supporter in the opponent's hand.
- Wash Out, Voltage Increase, Leaf Trans and Magical Trans share their legal
  candidate calculation with resolution. Fighting Tag requires movable Fighting
  Energy; Leap Frog requires an eligible Water Pokemon on the Bench.
- From-hand acceleration uses the from-hand attachment observers, preserves
  printed targets and does not consume the ordinary once-per-turn attachment.
  Rainbow Energy is Colorless outside play, not a typed search/attachment hit.
- Corrected Active Volcano, Trick Reveal, Luster Float, Boost Gas, Free Flight,
  Insomnia and Extreme Speed's provided-Energy count. Verified Insight, Berserk
  and specific Special Condition immunities with true/false scenarios.
- Corrected Emcee's Chatter, Cheerleader's Cheer, Judge, Life Herb, Energy
  Exchanger, Pokemon Communication, Fisherman and Energy Returner. Added tests
  for private Sage's Training selections, Moomoo Milk and full-stack Seeker.
- Healing Items without a valid healing/condition target and exchanges without
  their required hand card are unavailable. Twins and Black Belt require the
  printed Prize disadvantage. Seeker is legal when either player has a Bench.
- Implemented Tropical Tidal Wave's coin-selected side, attached Items and
  Stadium discard. Modern Pokemon Tools are not treated as Items.
- Implemented Lost World's clickable victory declaration: six opposing Pokemon
  in the Lost Zone, during the user's own turn, never automatically at Checkup.

### LEGEND and terminal resolution

- Ordinary LEGEND play requires complementary halves of the same Pokemon/set,
  uses one Bench space and triggers Ocean Grow only after both halves enter.
  Duplicate halves, mixed zones and a full Bench are rejected before movement.
- Both halves travel as one Pokemon stack in play; they are not an evolution
  line. Single-Pokemon LEGEND award one Prize and paired-Pokemon LEGEND two.
  Dual Weakness correctly compounds when both attacking types match.
- Legend Box uses actual Bench capacity and a complementary pair rather than
  treating two copies of the same half as a completed Pokemon.
- Take Away returns both complete stacks and promotes its user first. It does
  not award Prizes for returning Pokemon to the deck.
- Winning conditions are compared after the complete KO/Prize batch instead
  of awarding the match to whichever player is processed first. Two conditions
  beat one; equal simultaneous conditions start a new one-Prize Sudden Death
  round. The reset preserves physical cards, clears previous-round state and
  uses the existing coin/setup/mulligan/placement protocol.

## Verification

- `tests/test_hgss_rules.py`: 45 regression tests.
- `tests/test_hgss_attacks.py`: 32 regression tests.
- `tests/test_hgss_legend.py`: 6 regression tests.
- `tests/test_hgss_powers.py`: 7 regression tests.
- `tests/test_hgss_trainers.py`: 11 regression tests.
- `tests/test_hgss_edge_cases.py`: 23 regression tests.
- These 124 tests include further subcases for coin results, owner, target,
  damage, timing, card printing and board state.
- `python -X utf8 -B -m unittest discover -s tests -q`: **331 passed**.
- `python -X utf8 -B -m spirit.tools.engine_selftest`: **101/101 passed**.
  The deliberate bench-capacity reentrancy test emits an error-level diagnostic
  while checking its safety cap; the test passes.
- `git diff --check`: passed for the audit changes.

Final complete-family scans (exact-text groups, not individual printings):

| Kind | Families | Neutral-board result | Follow-up |
| --- | ---: | --- | --- |
| Attacks | 470 | 464 observed; 2 empty; 4 partial | Positive/negative outcome tests for Illumisile, Moon's Invite, Enraged Assault, Ninja Fang, Pheromone Poison and Tentavolve |
| Activated powers | 47 | 44 observed; 1 partial; 2 unavailable | Dimension Transfer heads/tails and typed-transfer eligibility tests for Voltage Increase and Wash Out |
| Trainers | 42 | 39 observed; 3 unavailable | Full Heal with conditions, Twins and Black Belt with a Prize disadvantage; actual effects also asserted |

No exception or timeout remained in these final scans. An observed event is
not counted as evidence that every clause resolved correctly; the separate
outcome tests and manual review are essential to the result.

The tests use the real board, definitions, legal-action conditions and effect
contexts with controlled choices and coin results. They do not replace a
two-client visual/network playthrough. Not every wording adjustment above has
an independent end-to-end scenario yet.

## Verification limits

The complete-family scans remain a diagnostic layer, not a correctness proof.
A conditional attack may correctly emit no event on a neutral fixture; the
positive/negative tests above exercise the identified branches separately.
Not every wording adjustment has its own independent end-to-end scenario.

No native-client two-player visual/network playthrough was run in this pass.
In particular, LEGEND presentation and the visual transition into Sudden Death
reuse existing protocol messages and have server-state regression coverage,
but still require a real-client smoke test before release. Foil/art assets,
server deployment and GitHub publication are outside this audit.

## Rule references

- [Official HGSS Card-Dex](https://assets.pokemon.com/assets/cms/pdf/tcg/carddex/heartgoldsoulsilver.pdf)
- [Official card errata](https://assets.pokemon.com/assets/cms/pdf/tcg/tcg_errata.pdf)
- [Pokemon Tool rule change](https://www.pokemon.com/us/news/2023-pokemon-tcg-standard-format-rotation-and-pokemon-tool-errata)
- [Official rulebook: simultaneous wins and Sudden Death](https://assets.pokemon.com/assets/cms/pdf/tcg/rulebooks/bw_dragons_exalted_rulebook.pdf)
- [Official TCG glossary](https://www.pokemon.com/us/play-pokemon/about/pokemon-tcg-glossary)
- [Translated Japanese Lost Link rulings](https://www.pokebeach.com/tcg/lost-link/faq)
- [Translated Japanese Revived Legends rulings](https://www.pokebeach.com/tcg/revived-legends/faq)
- [Translated Japanese Clash at the Summit rulings](https://www.pokebeach.com/tcg/clash-at-the-summit/faq)

The local `spirit/config.py` change was left untouched. This audit batch has
not been committed or pushed, and the server has not been restarted.
