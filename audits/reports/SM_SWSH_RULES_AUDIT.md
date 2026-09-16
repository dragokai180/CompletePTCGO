# Sun & Moon / Sword & Shield rules audit

Date: 2026-09-15

## Scope and status

Status: **completed for this audit pass**. The recorded follow-up queue has
been reviewed, the confirmed defects have been corrected, and the final
regression suite passes. See [follow-up coverage](SM_SWSH_AUDIT_COVERAGE.md)
for the disposition of the 56 passive risk families and conditional alerts.

This server-side audit pass inventories the full loaded Sun & Moon and
Sword & Shield catalog, including their promos and special expansions
(Shining Legends, Dragon Majesty, Hidden Fates, Detective Pikachu,
Celebrations, Pokemon GO and Crown Zenith). Reprints retain their shared
implementation.

The automated inventory covers 6,207 card definitions. This is a catalog-wide
audit pass, **not exhaustive semantic branch coverage or native-client
certification**. Passing a smoke probe proves execution in its fixture, not
that every target, amount, duration and optional decision is correct.

## Reported defects

- **Tag Call:** the generic search accepted ordinary Pokemon. Its filter now
  accepts only TAG TEAM cards, including TAG TEAM Supporters; private failure
  and the limit of two cards are preserved.
- **Altered Creation-GX:** the permanent damage modifier existed, but its extra
  Prize check read a flag absent from the actual attack-KO context. It now
  checks actual attack damage against the opposing Active Pokemon. The Water
  bonus requires Energy beyond the effective attack cost; a single Rainbow
  Energy cannot pay Metal and also count as the extra Water. Tests cover
  persistence, bench/counter exclusions and the actual KO/Prize resolver.
- **Power Accelerator:** its Darkness filter read Pokemon-type attributes on
  Energy cards, yielding no legal attachment. It now reads the Energy card's
  supplied types, offers only Benched targets, and still deals damage when
  no attachment can be made.

## Related corrections

### Energy identity and selection

Energy-only type reads were corrected throughout the authored SWSH scripts.
Affected families include Power Accelerator, Ice Dance, Dark Squall, Spring
Bloom, Sun Energy, Dark Patch, Nessa, Kindler, Energy Garden, basic-Energy
diversity attacks and other typed attachment/discard/recovery effects.

`energy_card_types` describes a card's types. It is not a replacement for
`energy_provided_options`, which handles attached Energy units and modifiers.

Special Energy definitions that provide their types only while attached now
declare that distinction explicitly. The metadata survives reprints.
Power Accelerator cannot treat an unattached Hiding Darkness Energy as
Darkness Energy. Existing callers of the EnergyCardDef constructor retain
positional compatibility.

### TAG TEAM-GX effects

29 additional GX attacks now resolve their base effects separately from the
bonus requiring Energy beyond the effective attack cost. Coverage includes:

- Magical Miracle, Dark Union, Acme of Heroism, Nasty Goo Mix, Beast Game;
- Gigafall, Lightning Ride, Tropical Hour, Thrilling Times, Bubble Launcher;
- Puffy Smashers, Chaotic Order, Supreme Puff, Horror House, Aero Unit;
- Crimson Flame Pillar, Cross Division, Dark Moon, Double Blaze, Evergreen;
- Full Metal Wall, GG End, Megaton Friends, Miraculous Duo, Pale Moon;
- Sky Legends, Solar Plant, Tag Bolt and Towering Splash.

Tests exercise both bonus states, printed amounts, target counts and
destinations. Additional integration cases cover Acme's survival, Pale Moon's
cancellation after switching, and protection against attack effects.
Full Metal Wall reduces opposing attack damage, not self-inflicted damage.

### Searches and ordered effects

- Shared filters distinguish Pokemon-GX/EX, Ultra Beasts, named Looker and
  Unidentified Fossil cards, Stadiums, and mixed elemental categories.
- Electromagnetic Radar, Net Ball, Ultra Space and Brooklet Hill use their
  actual categories, not a broad Pokemon filter.
- Friend Ball respects the types of the opponent's Pokemon in play.
- Beast Ring chooses one Ultra Beast and attaches both chosen Basic Energy
  cards to that Pokemon. Its public Prize-count restriction remains enforced.
- Dusk Stone checks a compatible public pre-evolution and evolves it directly,
  instead of putting the Evolution into the hand. It can fail a private search.
- Energy Spinner's larger search applies only on the second player's first turn.
- Red & Blue pays its optional discard when played, evolves a compatible
  Pokemon-GX directly, then attaches searched Energy to that same Pokemon.
  First-turn and entered-this-turn restrictions are preserved.
- Rainbow Brush keeps the old Energy attached if the private search fails.
- Fossil Excavation Map offers its deck/discard alternatives, including
  recovery with an empty deck.
- Pokemon Research Lab benches the correct Fossil Evolutions and ends the
  turn after a search, including deliberate failure.
- Existing Scoundrel Ring exclusions and uppercase EX/lowercase ex distinctions
  are preserved.

### Other effects

- Frozen Breath now pays its numeric discard cost before applying Paralysis.
- Surprise Fist's rock-paper-scissors result changes damage instead of
  incorrectly drawing/milling cards.
- Plural generic Ability costs ("discard 3 cards", including Spiritborne
  Evolution) no longer look for a card literally named "cards". Costs are
  paid before evolution; the same parser supplies public activation checks.
- One-card deck inspections still show the inspected card privately
  (Orbeetle, Lunatone, Gothita, Porygon and Duskull).
- Arc Phone only offers face-down Prize cards.
- The headless rock-paper-scissors scenario now produces a decisive result;
  it previously looped forever because both automated players always chose Rock.

## Continuation: knockout and end-of-turn scenarios

The follow-up pass exercises actual knockout resolution, not just direct
calls to the card callback.

Corrected:

- Energy Grounding: recognizes the printed rule instead of looking for the
  Ability title inside its description. It moves only to a surviving Lanturn
  and does not offer an Energy already moved or recovered by another observer.
- Hypnotic Pendulum: recognizes its printed trigger and lets Hypno's controller
  select the opponent's new Active on heads.
- Wishful Baton: restores the former holder from the KO snapshot after the
  Tool leaves play. All selected Energy cards go to one Benched Pokemon.
- Durable Blade: returns the Pokemon, including its evolution cards, without
  incorrectly also recovering Basic Energy. Self-inflicted attack damage does
  not satisfy its opposing-attack requirement.
- Spell Tag: retains its holder after the KO, checks Psychic type and requires
  opposing attack damage. Effective types are snapshotted before attachments
  and type-changing effects leave play.
- Emergency Jelly: a passive end-of-either-turn effect replaces its incorrect
  between-turns registration. It discards itself only after actual healing,
  never an unrelated Tool, and does not rescue a Pokemon already at zero HP.

Regression coverage also checks that Golden Wing can distribute Energy among
different Benched targets, Scatter triggers only at the end of the opponent's
turn and returns the full stack, and Gift Energy does not draw after a direct
effect KO without attack damage.

The end-of-turn/Checkup distinction is consistent with the
[official Pokemon rulebook](https://assets.pokemon.com/assets/cms2/pdf/trading-card-game/rulebook/pal_rulebook_en.pdf),
which describes Pokemon Checkup as the separate step between turns.

New test module: `tests/test_sm_knockout_timing.py` (12 tests passed).
Full regression suite after this continuation: **677 tests passed**.

These scenarios reduce the untested timing surface but do not close every
conditional branch listed in the initial inventory below.

## Conditional continuation: attachment, setup and per-player history

This pass adds scenario-specific coverage rather than overriding card
conditions to make the generic smoke fixture pass.

Corrected:

- Energy Evolution recognizes its printed description, asks before the
  optional search, filters by the attached Basic Energy type and evolves
  the Pokemon. Evolution retains Harmonics' pending attachment target.
- Harmonics grants one additional normal attachment to that same friendly
  Pokemon, not an extra attachment per Primarina or per effect attachment.
- Speed Cheer respects its non-stacking clause in the shared attack-cost
  pipeline. No-op or opposing copies do not consume another copy's key.
- Bursting Spores observes both Basic and Evolution Pokemon with Spore
  played from hand; it does not rely on finding the Ability title inside
  the printed description.
- Hazardous Evolution remains an on-evolution trigger instead of becoming
  a global Checkup passive. Its Poison places three counters per Checkup.
- Hand-only evolution triggers and Wyndon Stadium inspect the actual source
  zone. A visual introduction flag no longer substitutes for the hand rule.
- Electric Start permits Manectric in either opening position only for the
  player going second. It does not make Manectric a Basic Pokemon.
- Summoning Star and Regi Gate use the effective Bench capacity, including
  both expansion and reduction effects.
- Sun Energy recognizes Lunatone's evolution identity rather than a
  localization key, in both Pokemon GO and Crown Zenith implementations.
- Slumbering Forest requires two heads for either player's sleeping Pokemon.
- Previous-turn attack records are also retained per player. Dede-Short,
  Peko Blaster, Cavern Tackle, Powdery Uppercut, Pikachu's Dede-Short bonus,
  Plusle's Minun bonus, Grapploct's Full Nelson bonus, Cross Fist and
  Zebstrika's Rapid Strike bonus no longer consult the opponent's intervening
  turn. Team conditions use the recorded attacker identity even after it
  leaves play. Self-specific requirements still require that Pokemon.
  The immediate-last-turn ledger remains separate for retaliation triggers.

New regression modules:

- `tests/test_sm_conditional_coverage.py`
- `tests/test_swsh_conditional_coverage.py`

The tests additionally cover the previously skipped Electrocharger, Lure
Ball, Tag Switch, Great Catcher, Dana and Evelyn prerequisites and selectors;
the Dusk Stone and Beast Ring cases were covered by the preceding pass.
Other assertions cover non-stacking damage/HP/energy modifiers, the distinct
Guts and Sturdy requirements, attack-damage-only reactions, named Energy
recipients, Ancient Wisdom, Special Transfer, Phantom Transformation, Lost
Zone attacks and Twilight Inspiration. The Tag Switch test checks its
single-source/single-destination dispatch; shared transfer execution has
separate tests.

This closes the listed shared-Trainer fixture omissions, **not every runtime
skip or every passive interaction in the initial inventory**. The old skip
counts below are historical probe results, not a current count of defects
and not evidence that untested conditional branches work.

## Continuation: confirmed semantic defects and conditional scenarios

This continuation adds dedicated scenarios rather than treating generic
prerequisite skips as successful tests. It closes the confirmed defects
listed here; unexercised catalog branches remain outside that claim.

### Trainer selection, costs and independent effects

- Aether Foundation Employee recovers only Alolan Pokemon; Lusamine accepts
  either Supporters or Stadiums. Lana's Fishing Rod has separate Pokemon
  and Tool slots, including partial resolution when only one category exists.
- Beast Ball and Lusamine Prism Star recognize the normalized Ultra Beast
  subtype. Zinnia recognizes the singular previous-turn knockout wording.
- Recovery predicates read the recovered category, not the preceding payment:
  Molayne's Metal Energy cost must not turn its Trainer recovery into an
  Energy search. Crasher Wake's Water Energy cost likewise does not restrict
  its unrestricted deck search to Water cards.
- Cynthia & Caitlin pays its optional discard before recovering a Supporter;
  it cannot recover the just-paid card or another Cynthia & Caitlin. The draw
  bonus remains usable independently when the public recovery has no target.
- Mallow & Lana optionally pays before switching and heals the outgoing
  Pokemon only when paid. Guzma & Hala uses three independent search slots
  when its bonus is paid. Bellelba & Brycen-Man pays its optional cost before
  milling and resolves the opponent's Bench choice first.
- Star Alchemy, Raihan, Cursed Message, Camping Gear, Package Delivery and
  Farewell Bell require a selection for their unrestricted, non-revealing
  searches. Explicit up-to searches remain optional. Sordward & Shielbert
  reveals the selected Trainer before the opponent's decision.
- Raihan requires recoverable Basic Energy; Rose requires both a VMAX and
  recoverable Basic Energy. Adaman, Mirage Gate, Familiar Bell and Wait and
  See Turbo also require a nonempty deck, without checking private matches.
- Rescue Carrier checks printed HP. Urn of Vitality requires Single Strike
  Energy, not any Single Strike card. Siebold and Suspicious Food Tin offer
  healable, damaged recipients rather than healthy Pokemon.
- Faba accepts the opponent's Tools or Special Energy and either player's
  targetable Stadium, and sends the choice to its owner's Lost Zone. Its
  wording is kept distinct from Xerosic's both-sides discard effect.
- Dangerous Drill and Flannery respect Prism Star Stadium protection.
  Shared Stadium removal now honors Trainer immunity and the Lost Zone
  replacement instead of moving every Stadium directly to discard.
- Bonnie grants a turn-scoped exception only to Zygarde-GX, including copied
  attack execution; it does not reset the player's general GX allowance.
  Its independent permission still works with a protected Stadium.
  See the [Bonnie/Prism Star ruling discussion and official FAQ link](https://www.pokebeach.com/forums/threads/bonnie-and-prism-stadiums.149502/).
- Devolution Spray Z permits a partial devolution and prevents the remaining
  Pokemon from evolving again that turn.
- Fantina and Shield Star register a single side-wide reduction, not one
  cumulative reduction per Pokemon. They affect newcomers and expire.
- Phoebe and Ultra Forest Kartenvoy are turn-scoped subtype effects:
  newcomers benefit, unrelated Pokemon do not, and protection on opposing
  Benched Pokemon is not bypassed.
- Twenty-four generated attack definitions no longer apply a self-lock when
  their printed text instead restricts the opponent or grants protection.
  Genuine self-locking attacks retain their restrictions.

### Attachments, entries and reactive effects

- Dance of the Ancients resolves with only one eligible Lightning Energy or
  one recipient, without requiring two of each to start the effect.
- Rogue Fangs counts Single Strike Pokemon in the discard, not Single Strike
  Trainer or Energy cards.
- Effect-driven Bench entries reset stale damage, conditions and usage state.
  Echoing Horn still places the Pokemon on its owner's Bench.
- Recycle Energy and U-Turn Board resolve their replacements while the entire
  stack is still in play. Both bulk discard and actual knockout resolution
  return them to hand; discarding them from hand does not.
- Dragon Talon and Giant Bomb tests cover Bench versus Active, damage counters
  versus attack damage, the Dragon requirement/180-damage threshold, and
  Giant Bomb's opponent-turn expiry.
- Slaking V's Kinda Lazy restriction is lifted when its Ability is suppressed;
  both printings have even/odd Prize-count regression coverage.

Additional scenarios assert the behavior of Counter Catcher, Lt. Surge's
Strategy, Molayne, Melony, Metal Saucer, Tool Scrapper, Field Blower, Magma
Basin, Crystal Cave, Volo, Toy Catcher, Crossceiver, Team Yell's Cheer,
Professor Laventon, Fan of Waves and Eneporter.
The final scenario pass also covers Brock's Training's named recipients,
Giovanni's Exile's undamaged Bench requirement, Last Chance Potion's remaining
HP threshold, Welcoming Lantern/Scrounge recovery categories and Dream Ball's
non-hand play restriction and ability to Bench an Evolution Pokemon.

New regression modules in this continuation:

- tests/test_sm_trainer_continuation.py
- tests/test_sm_swsh_optional_recovery.py
- tests/test_sm_tag_team_supporters.py
- tests/test_swsh_remaining_scenarios.py
- tests/test_sm_swsh_trainer_scopes.py
- tests/test_sm_turn_exceptions.py
- tests/test_sm_swsh_field_control.py
- tests/test_sm_swsh_final_trainers.py


## Conditional follow-up: Energy costs, searches and Scrolls

Added 15 regression tests in `tests/test_sm_swsh_conditional_closure.py`.
Confirmed and corrected:

- Eight attack families (12 printings) discarded physical cards instead of
  provided Energy units: Bright Flame, Iron Wings, Hazardous Claws, Hail
  Prison, Draconic Impulse, Sonic Strike, Radiating Pulse and Meteor.
  A Double Colorless Energy can now satisfy a two-Energy discard without
  discarding an additional Basic Energy. Iron Wings also recognizes a single
  attached Double Colorless card as a usable payment.
- Rosa now uses separate Pokemon, Trainer and Basic Energy selection slots,
  rather than the generic single-category search. Each private search slot
  remains optional; selected cards are revealed and the deck is shuffled.
- Lance Prism Star can put evolved Dragon Pokemon directly onto the Bench.
  Its search is capped by available Bench spaces, and a full Bench prevents
  activation. The prior-opponent-turn KO prerequisite is preserved.

Other scenarios passed without requiring gameplay changes: Morgan's named
discard cost and top-12 Energy attachment, Wait and See Hammer's turn window,
Thorton's transfer of damage/conditions/attachments/turn state, Lost Vacuum's
cost-before-target order, Lysandre Prism Star's Fire count and Lost Zone
destination, and Oricorio-GX's shared once-per-turn Dance of Tribute.
All six Scroll families now have matching battle-style permission coverage;
tests also exercise damage counters, multiple Energy units, full opposing
field damage, protection/Weakness bypass and all-Energy discard ordering.

Energy-versus-card distinction reference: Pokemon TCG
[Advanced Players' Rulebook](https://asia.pokemon-card.com/hk-en/wp-content/uploads/sites/6/2022/08/advanced-manual_EN.pdf).
Printed bonuses that explicitly count discarded *cards* must continue to
count cards, not the Energy units those cards previously provided. This pass
does not blanket-replace every Energy-card selection with a unit selection.

## Final closure: passive hooks, Stadium actions and Energy units

The closing pass adds 23 tests across `test_sm_passive_closure`,
`test_sm_stadium_closure` and `test_swsh_energy_discard_closure`.

Confirmed defects corrected:

- Victory Star (SM2 Victini) now participates in the actual attack-coin
  reroll flow instead of being registered as a manually activated Ability.
  The shared hook recognizes both "results" and older "effects" wording,
  preserves the once-per-turn limit, and keeps Tool-granted rerolls such as
  Trick Coin exclusive to their holder.
- Seven further Energy-discard families now count provided units: Ripping
  Horn, Field Trap, Smashing Edge, Burning Licks, Electron Crush, Body Splash
  and Electro Blaster. Positive tests reproduce the unnecessary extra
  discard before the fix. Max Lance retains its explicit per-card bonus.
- Viridian Forest, Giant Hearth, Mt. Coronet, Heat Factory Prism Star,
  Brooklet Hill and Ultra Space now execute their third-person Stadium
  instructions instead of falling through the Pokemon Ability interpreter.
  Costs are paid first, searches/recovery use exact types and counts, and
  destinations are correct for either player. Heat Factory no longer draws
  without discarding Fire Energy. Private searches can fail, but still pay
  their cost and shuffle. The once-per-player-turn limit is regression-tested.

The remaining reactive/KO/attachment flags have dedicated scenarios in the
coverage index, including Lost Out, Last Pattern, Grim Marking, Natural Cure,
Charmed Charm, Dashing Pouch, Lillie's Poke Doll, Commotion and the damage
reactions. No confirmed defect identified by this audit is left open.

## Final validation and testing limits

Automated inventory reports from the initial pass:

Initial-pass regression suite: **665 tests passed**; the earlier continuation
reached **677**. The previous continuation passed **779 tests**. The latest
conditional follow-up passed **794 tests**. The closing pass passed **817
tests** (23 additional tests), with no failures. The latest full suite ran
in 71.079 seconds; git diff --check also passed.

Final catalog dispatch rerun: **6,207 definitions**, **5,608 grouped probes**,
**5,470 PASS**, **138 SKIP**, **zero runtime errors**.
The probe count changed because shared implementations are grouped by their
callable identity. Skips remain prerequisite-dependent probes, not passing
semantic tests; named regression scenarios above cover many of these paths.
The local detailed report is
`audits/results/sm-swsh-runtime-audit-20260915-complete.json` (not versioned).

The final shared-text rerun contains 1,740 attack families (1,737 observed,
3 conditional-healing alerts), 185 Ability families (184 observed, Shell On
skipped for its prerequisite) and 148 Trainer families (138 observed,
9 prerequisite skips and Channeler's raw-state-only effect). Each remaining
alert has a scenario/disposition in the coverage index; there are no new
unresolved findings from this final rerun.

The following table preserves the **initial inventory** for comparison:

| Layer | Result |
| --- | --- |
| Runtime catalog | 6,207 card definitions |
| Authored/runtime probes | 5,603; 5,461 passed, 142 skipped, no exceptions |
| Shared attack text families | 1,740; 1,737 observed, 3 conditional-healing alerts |
| Shared Ability text families | 184; 183 observed, 1 prerequisite skip |
| Shared Trainer text families | 148; 139 observed, 8 prerequisite skips, 1 raw-state effect |
| Passive inventory | 275 SM/SWSH families; 219 mapped, 56 flagged for deeper timing/interaction review |

The three healing alerts are Iron Fist, Iron Hand and Poison Absorption:
dedicated tests exercise the Regice/Poison prerequisites and verify both
healing and non-healing outcomes. Shell On and Spiritborne Evolution have
dedicated cost/evolution tests. Channeler's raw-state removal is tested
directly, rather than being mistaken for an absent effect.

The initial 142 runtime skips became 138 after corrections. They remain
**skips in the generic fixture**, not passing semantic tests. Their missing
prerequisites include named Pokemon, a prior KO, Lost Zone counts and
recoverable cards; follow-up scenarios cover these conditions separately.
The 56 passive risk flags were reviewed with scenario coverage, as indexed
in SM_SWSH_AUDIT_COVERAGE.md. They were review flags, not 56 confirmed bugs.
The follow-up queue is closed; unenumerated card combinations and exhaustive
native-client testing remain outside the certification boundary of this pass.

Focused tests:

- `tests/test_sm_swsh_semantics.py`
- `tests/test_sm_tag_team_gx.py`
- `tests/test_sm_searches.py`
- `tests/test_sm_swsh_resolution.py`

Reproduction commands (from the repository root):

```text
python -c "from pathlib import Path; Path('audits/results').mkdir(parents=True, exist_ok=True)"
python -m unittest discover -s tests
python -m spirit.tools.audit_sm_swsh_runtime --json audits/results/sm-swsh-runtime.json
python -m spirit.tools.semantic_effect_audit --kind attack --set-pattern "(SM[0-9]+|Promo_SM|SL|DM|HF|GUM|SWSH[0-9]+|Promo_SWSH|CEL25|PGO|CZ)" --only-problems --json audits/results/sm-swsh-attacks.json
```

Repeat the last command with `--kind ability` and `--kind trainer`.
No production account data, foil assets or server configuration were changed
by this audit. A running server needs a controlled restart to load the new
Python code; this pass does not restart it or push a Git remote automatically.

## Follow-up: no-Prize knockout rules (2026-09-15)

Lillie's Poke Doll's prohibition now takes precedence over Altered Creation-GX,
attack-local extra Prizes and turn-scoped bonus watchers. The rule is evaluated
per knocked-out Pokemon, so simultaneous knockouts still grant the Prizes due
for other Pokemon. Numerical reductions such as Life Dew remain distinct.

Seven regressions in `test_lillies_poke_doll_knockout` cover both players,
attachments, promotion, the last Pokemon leaving play, mixed knockouts and
valid bonuses. The same seven scenarios were also executed with Robo Substitute
substituted into the fixture; all passed through the shared no-Prize rule.
The complete local test suite passed **824 tests** before publication.

## Follow-up: Chromashift, Eternal Zone and Dread End

Chromashift correctly computed Kecleon's current types, but Eternal Zone and
Dread End still used a printed-type predicate. A basic Darkness Energy therefore
changed Kecleon's type without enabling the eight-slot Bench or adding its
30 damage to Dread End. Both field queries now use effective Pokemon types.
The alternate Eternatus VMAX printing shares this implementation; the gallery
reprint inherits it. Hidden-zone type predicates are unchanged.

Seven tests in `test_chromashift_eternal_zone` reproduce and cover the interaction:
all three printings and both owners, multiple basic Energy types, Energy removal,
Special Energy exclusion, Silent Lab suppression and restoration, other
non-Darkness Pokemon, excess-Bench discard without Prizes, and printed types
outside play. Dread End assertions execute the attack and inspect actual HP.

## Follow-up: Eternal Zone entry permissions

The previous type-query correction did not implement Eternal Zone's separate
prohibition on putting non-Darkness Pokemon into play. The Ability now provides
an any-zone entry restriction, distinct from effects that only forbid playing
Pokemon from hand.

The hand menu and authoritative hand-play, effect-Bench, evolution and identity
replacement executors enforce the restriction before moving a card. Generic
direct-to-Bench searches and relevant shared Trainer selectors filter forbidden
entries while preserving private-search failure. An attachment to an existing
Benched Pokemon is not an entry and does not use this filter.

`test_eternal_zone_entry_permissions` covers all three printings, both players,
hand/deck/discard entry, non-Darkness evolution, replacement, Ability suppression,
the all-Darkness prerequisite, legal field movement and private search choices.

## Follow-up: GX/VSTAR budgets and original playmat markers

`_clone_ability` preserved VSTAR but omitted GX. Consequently, 402 GX attacks
on reprints lost their match-wide restriction, marker animation and GX-specific
rules. Both Ability and Attack cloning now preserve the GX flag. A catalog-wide
regression checks GX titles and once-per-game reminders, including granted powers.
Execution revalidates spent GX/VSTAR budgets for stale actions, in addition to
the existing menu and copied-attack checks. Bonnie's scoped exception remains
valid; Clear Vision-GX still overrides it. GX and VSTAR budgets are independent.

Deck initialization recognizes Tool-granted VSTAR Powers (all three Seal Stones),
so their marker exists even without a VSTAR Pokemon. Marker flip messages reach
both players and the spent PlayerEntity attributes remain available for snapshots.

The local GX and VSTAR templates were verified byte-for-byte against the original
SM Cache bundles. The served VSTAR bundle was restored from that archive; GX was
already original. Startup now publishes these original atlases unchanged instead
of compiling custom marker PNGs. The manifest includes native case-sensitive
marker aliases and releases its file handles after reading the bundles.

Regressions: `test_once_per_game_powers`, `test_original_marker_bundles`, and the
existing Bonnie/copy cases in `test_sm_turn_exceptions`. Native client rendering
still requires a server restart and a new/reconnected client session for review.

## Follow-up: Restoration and expanded Bench capacity

Restoration's shared `requires_bench_space` condition used a fixed five-slot
limit even while Eternal Zone allowed eight. It now queries the owner's live
Bench capacity, respecting both expansion and reduction effects. Existing
same-name Pokemon and use of Restoration by another copy remain independent.

`test_restoration_bench_capacity` covers all five Darkrai-GX printings, both
players, five to seven occupied slots, actual restoration into the eighth slot
with the chosen Darkness Energy, a full Bench, the normal five-slot limit,
Ability suppression and Collapsed Stadium. The change only updates the space
predicate; entry restrictions are still enforced separately by the engine.

## Follow-up: deck-to-Bench searches with variable capacity

The shared `search_to_bench` factory also retained the fixed five-slot limit,
both in its play condition and its selection count. Both now use the current
owner-specific Bench capacity. Search candidates honor entry restrictions,
including Eternal Zone, without turning private target availability into a
play prerequisite: a nonempty deck with no matching card can still be searched
and failed. A full Bench remains a public restriction.

`test_search_bench_capacity` exercises Buddy-Buddy Poffin, Gloria and Call for
Family with Sky Field and Eternal Zone, both owners, the last free slot, a
full Bench, Collapsed Stadium, prohibited non-Darkness entries, private failure,
an empty deck and callbacks receiving only successfully Benched Pokemon.

## Follow-up: Item-Pokemon knockout animation deadlock

The native client log showed NullReferenceException in EntityUtil.IsLegendPokemon
called from the Knockout executor (N.k). Inspection of that installed executor
confirmed it selects its victim with IsPokemon(), which checks CARD_TYPE rather
than the entity class. Lillie's Poke Doll, Robo Substitute and Fossil Items keep
Trainer type; no victim is selected and the animation queue stops before the
new Active offer. Earlier headless promotion tests did not cover this contract.

Knockouts of these cards now use GroupedMove, retaining the complete stack,
HP/visual resets and all server-side KO, Prize and promotion rules. Printed
Pokemon still use the native Knockout sequence. Regression tests cover both
players' human replacement offers, every registered Item-Pokemon definition
with an attached Energy, and ordinary Pokemon choreography. Native UI replay
still requires restarting the server and testing in the client.

## Requested interaction: Sinister Hand / Damage Swap

After choosing a source Pokemon, the native multi-click counter picker now
previews 10 damage removed per click. Done accepts any positive number up to
the source's available counters and the largest receiver's remaining HP.
Only then is a receiver selected; receivers with less remaining HP than the
selected damage are excluded and rejected again at execution. Equal HP is
allowed, including a Knock Out. Selection alone never mutates damage.

Damage Swap's two Reuniclus printings previously reused Sinister Hand's
opposing-field predicate and effect; they now operate on the owner's field.
The native picker retains exact-count behavior for existing callers. Six
regressions in test_damage_transfer_selection cover both players, all four
prints, partial confirmation, previews, recipient limits and invalid replies.
