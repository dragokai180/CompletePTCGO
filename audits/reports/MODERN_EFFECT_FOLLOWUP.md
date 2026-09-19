# Stadium searches, hand entry, Energy consequences and V-UNION rendering

## Scope

Follow-up to Artazon, Swelling Flash, incomplete V-UNION artwork and Psychic
Embrace reports. This is a focused review of related effect families, not a
claim that every card in the catalog has been exhaustively tested.

## Findings and fixes

- **Artazon:** the shared interpreter expected second-person search wording,
  but Stadiums use "that player/their deck". Added an explicit handler shared
  by its reprints. It selects only Basic Pokemon without Rule Boxes, puts them
  on the acting player's Bench and shuffles. Failure remains permitted even
  with eligible hidden cards; a full Bench blocks activation.
- **Town Store, Mesagoza and Lumiose City:** the same wording defect left these
  searches incomplete. Implemented Tool-to-hand, coin-dependent Pokemon search,
  and Basic-to-Bench respectively. Lumiose ends the turn even after a failed
  search; Mesagoza tails neither searches nor shuffles.
- **Swelling Flash:** direct engine entry already succeeded with more Prizes
  remaining than the opponent. However, the menu also allowed activation when
  that prerequisite was false. Menu/execution now share hand-entry conditions.
  The entering card is publicly introduced and moved before the Ability
  announcement, avoiding an animation referencing a still-hidden source.
- **Emergency Rotation:** enforce the opposing Stage 2 prerequisite and Bench
  capacity. **Electric Swamp:** require four physical Lightning Energy cards,
  put Eelektross on the Bench first, then offer optional Energy movement.
  **Greninja-GX's Elusive Master:** enter the Bench before drawing three, and
  require it to be the last card in hand. Previously generic partial clauses
  could consume these compound effects without performing their entry.
- **Psychic Embrace:** the attachment branch returned before its two damage
  counters. Shared attachment follow-ups now handle both "if you do" and
  "if you attached Energy ... in this way". Psychic Embrace only offers Psychic
  targets with more than 20 HP, and only Basic Psychic Energy from the discard.
  Failed attachments do not place counters or heal.
- **Single Strike Roar:** both Houndoom printings now apply their counters only
  after a successful attachment, explicitly as non-attack counters. Afterburner
  and Sinister Surge are tested as related positive controls.
- **V-UNION artwork:** the native playmat renderer uses collector number plus
  the live string attribute **10020**, not image URL attribute **10510**.
  Assembled V-UNION now carry `to142`, `to158`, etc. on the entity, so the lookup
  reaches the already-imported complete texture. Physical parts stay unchanged.

## Verification

Full regression run: **1,309 tests passed**. The final focused run passed
**40 tests**, including an additional Emergency Surfacing regression: an empty
hand does not turn a discard-entry Ability into a hand-entry Ability.

Tests exercise real card effects and movement primitives, with selection UI
substituted. They cover all Artazon and Psychic Embrace printings, both players
for Artazon, private-search failure, coin branches, public activation conditions,
hidden-source message ordering, Energy/counter outcomes, and all five V-UNION
families with both owners. Related existing HGSS, SM, SWSH, entry and installation
tests remain in the full regression suite.

The V-UNION lookup was checked against the local native client:
`PlaymatCardImageRenderer.textureLookup`, `Q.j`, `S.y` and `P.F` attribute
definitions. Wire regressions check the resulting complete texture name and
the actual EntityIntroduced attributes. A graphical native-client match was
not performed; rendering validation here is protocol-based.

```text
python -m unittest tests.test_modern_effect_followup tests.test_vunion tests.test_ability_searches -v
python -m unittest discover -s tests -q
```
