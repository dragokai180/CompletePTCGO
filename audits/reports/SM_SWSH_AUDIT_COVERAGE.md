# Sun & Moon / Sword & Shield follow-up coverage

This index closes the follow-up review queue from the SM/SWSH audit. It is
an index of reviewed rule families and regression scenarios, not a claim
that every possible matchup or client animation has been tested.

## Passive review queue

All 56 `HIGH_RISK_REVIEW` families from the initial passive inventory were
reviewed. The grouped index below includes the special-expansion entries.
Some scenarios live in earlier audit modules because they exercise the same
shared rule; a card mentioned only as a fixture is not sufficient coverage.

| Reviewed families | Outcome scenarios |
| --- | --- |
| Energy Evolution, Harmonics | `test_sm_conditional_coverage`: optional matching evolution; hand-only attachments; one same-target bonus rather than stacking |
| Natural Cure, Charmed Charm | `test_sm_passive_closure`: actual attachment hooks, correct holder, matching Tool, optional acceptance |
| Bursting Spores, Hazardous Evolution | `test_sm_conditional_coverage`: own hand plays, Basic/evolution entries, no deck-entry trigger, Poison severity |
| Electric Start | `test_swsh_conditional_coverage`: second player only; Active and Bench setup positions |
| Fluffy Cotton, Evasion Jutsu, Guts, Sturdy | `test_sm_conditional_coverage`: both coin outcomes, attack/counter distinction, full-health versus damaged survival |
| Scatter, Hypnotic Pendulum | `test_sm_knockout_timing`: opponent-turn window, full-stack return, controller-selected opposing promotion |
| Victory Star | `test_sm_passive_closure`: actual coin reroll, shared once-per-turn use, no unrelated/defensive flips or manual activation |
| Armor of the Sunne, Blanket Weaver, Jungle Totem, Power Cheer, Speed Cheer, Strong Cheer, Vitality Cheer | `test_sm_conditional_coverage`: recipients, named prerequisites, both sides, non-stacking and Energy-unit values |
| Flaming Fighter, Slumbering Forest | `test_sm_conditional_coverage`: Burn rather than Poison, opponent rather than own side, two-head Sleep recovery |
| Poison Payback, Poison Point, Effect Spore, Incandescent Body, Cursed Body | `test_sm_conditional_coverage`: actual opposing attack damage; Active/Bench and damage-counter exclusions |
| Rough Skin, Spiky Shield, Counterattack, Commotion | `test_sm_passive_closure`: counter amounts, own-Bench versus attacking-Pokemon targets, Active-only and attack-damage requirements |
| Ear-Ringing Bell, Poison Barb | `test_sm_passive_closure`: holder and Active checks; Confusion/Poison; no trigger from damage counters |
| Lost Out, Last Pattern, Grim Marking | `test_sm_passive_closure`: actual KO resolver, entire-stack Lost Zone, random opposing hand discard, Active-only four-counter distribution |
| Durable Blade, Spell Tag, Wishful Baton, Energy Grounding, Golden Wing | `test_sm_knockout_timing`: KO snapshots, damage source, destinations, types, single/multiple recipients and already-moved Energy |
| Dragon Talon, Giant Bomb | `test_sm_swsh_final_trainers`: qualifying damage/type/position, counter exclusion, Giant Bomb threshold and expiry |
| Recycle Energy, U-Turn Board | `test_sm_swsh_final_trainers`: bulk movement and actual KO replacement while the full stack is still observable |
| Dashing Pouch, Lillie's Poke Doll | `test_sm_passive_closure`: retreat-only Energy return; Active-only bottom-deck action and separate attachment discard |
| Viridian Forest, Giant Hearth, Mt. Coronet, Heat Factory Prism Star, Brooklet Hill, Ultra Space | `test_sm_stadium_closure`: both players, payment before effect, exact filters/counts/destinations, partial public recovery, private failure, turn reset |
| Life Forest Prism Star | `test_trainer_followup_audit`: curing without damage, Grass targets and activation prerequisites |
| Pokemon Research Lab | `test_sm_searches`: correct fossil Evolutions, Bench placement and end-turn even on failed private search |

The shared reroll correction additionally has a Trick Coin holder-exclusivity
regression, because that Tool uses the same engine hook as Victory Star.

## Conditional runtime probes

The generic runtime fixture leaves 138 probes unactivated (108 distinct
card/action pairs before grouping printings). These remain `SKIP` in the raw
report: their prerequisites must not be disabled merely to turn them green.

Follow-up scenarios are indexed across:

- `test_sm_conditional_coverage`, `test_swsh_conditional_coverage`
- `test_sm_searches`, `test_sm_swsh_resolution`, `test_sm_tag_team_gx`
- `test_sm_trainer_continuation`, `test_sm_tag_team_supporters`
- `test_sm_swsh_optional_recovery`, `test_sm_swsh_field_control`
- `test_sm_swsh_trainer_scopes`, `test_sm_turn_exceptions`
- `test_sm_swsh_final_trainers`, `test_swsh_remaining_scenarios`
- `test_sm_swsh_conditional_closure`
- Existing Trainer/Ability activation-permission regressions

The review checks meaningful prerequisites (prior KO, public recoverable
cards, named Pokemon, Bench capacity, Prize window, Lost Zone size and
matching battle style), rather than treating a name match as proof of an
entire card's behavior.

## Shared text-family alerts

| Raw alert | Disposition |
| --- | --- |
| Iron Fist / Iron Hand did not heal in the generic fixture | Regice prerequisite and positive/negative healing outcomes asserted in `test_sm_swsh_semantics` |
| Poison Absorption did not heal | Opposing Poison prerequisite and both outcomes asserted in `test_sm_swsh_semantics` |
| Shell On could not activate | Shelmet cost and evolution resolution asserted in `test_sm_swsh_resolution` |
| Channeler produced no traced movement | Raw turn/effect state removal asserted in `test_sm_swsh_resolution`; movement is not its effect |
| Electrocharger, Lure Ball, Tag Switch, Evelyn, Dana | Prerequisites and outcomes asserted in `test_sm_conditional_coverage` |
| Aether Foundation Employee | Alolan recovery category asserted in `test_sm_trainer_continuation` |
| Dusk Stone, Beast Ring | Search, public prerequisites, actual destination and target limits asserted in `test_sm_searches` |
| Great Catcher | Cost, Bench and EX/GX restrictions asserted in `test_sm_conditional_coverage` |

## Closure criteria

The follow-up queue is closed when the final full regression suite passes,
the runtime inventory has no execution errors, each known text-family alert
has the disposition above, and all confirmed defects found in this pass
are corrected. The main audit report records the final run counts.

Remaining limits are testing boundaries, not a claim of an error-free game:
the native client was not exhaustively exercised, every possible card-pair
interaction was not enumerated, and future bug reports still require their
own reproducible scenarios. No accounts, artwork, production configuration,
Git remote or running server are changed by these checks.
